#!/usr/bin/env node
"use strict";

/**
 * Verify R020 checkpoint integrity locally before reusing recorded analysis.
 * Usage: node R020_VERIFY_CHECKPOINTS.js [--json]
 * Read-only, Node built-ins only. A failure exits non-zero; it never alters data.
 *
 * Data inside the run directory is git-attributes '-text', so working-tree
 * bytes must agree with the archived Git blob SHA1. Git blob SHA1 detects
 * accidental changes; it is not a substitute for analysis quality review.
 */
const fs = require("node:fs");
const path = require("node:path");
const crypto = require("node:crypto");

const ANALYSIS_DIR = __dirname;
const RUN_DIR = path.resolve(ANALYSIS_DIR, "..");
const EXPECTED_RUN = "R020_pythia-70m-representation-output-contrast";
const EXPECTED_STAGES = Array.from({length: 10}, (_, i) => "C" + String(i).padStart(2, "0"));
const SECTORS = new Set(["positive_head", "negative_tail"]);
const failures = [];
const verified = [];
let checkedCommunityRows = 0;

function check(condition, message) {
  if (!condition) failures.push(message);
  return !!condition;
}

function readJSON(filename) {
  return JSON.parse(fs.readFileSync(path.join(ANALYSIS_DIR, filename), "utf8"));
}

function gitBlobSha(bytes) {
  const header = Buffer.from("blob " + bytes.length + "\0", "utf8");
  return crypto.createHash("sha1").update(header).update(bytes).digest("hex");
}

function fileWithinRun(filename) {
  const full = path.resolve(ANALYSIS_DIR, filename);
  const relative = path.relative(RUN_DIR, full);
  if (!relative || relative === ".." || relative.startsWith(".." + path.sep) || path.isAbsolute(relative)) {
    throw Error("unsafe checkpoint path: " + filename);
  }
  return full;
}

function verifyOne(stageId, entry) {
  if (!check(entry && typeof entry.path === "string", stageId + ": invalid file entry")) return;
  if (!check(typeof entry.git_blob_sha === "string" && /^[a-f0-9]{40}$/.test(entry.git_blob_sha),
      stageId + ": invalid Git blob SHA for " + entry.path)) return;
  try {
    const file = fileWithinRun(entry.path);
    const data = fs.readFileSync(file);
    const actual = gitBlobSha(data);
    check(actual === entry.git_blob_sha,
      stageId + ": SHA MISMATCH " + entry.path +
      " expected " + entry.git_blob_sha + " actual " + actual);
    if (actual === entry.git_blob_sha) verified.push({stage: stageId, path: entry.path, sha: actual, bytes: data.length});
  } catch (err) {
    failures.push(stageId + ": cannot verify " + entry.path + ": " + err.message);
  }
}

function verifyCoverage(ledger) {
  const expected = ledger.expected_coverage;
  check(expected.generated_decisions === 32 && expected.recorded_states === 8 &&
    expected.sectors === 2 && expected.network_cells === 512 &&
    expected.communities === 6944, "unexpected declared R020 coverage");

  const measured = readJSON("../measurement_results.json");
  check(measured.generated_token_count === 32 &&
    measured.recorded_state_count === 8 &&
    measured.network_count === 512 &&
    measured.state_local_community_count === 6944,
    "measurement-results coverage changed");
  check(measured.replay_generated_tokens_exact === true &&
    measured.replay_hidden_states_exact === true &&
    measured.replay_logits_exact === true,
    "measurement replay is not recorded as exact");

  const frozen = readJSON("../manifest.json");
  check(frozen.run_id === EXPECTED_RUN &&
    frozen.measurement_status === "measurement_successful" &&
    frozen.analysis_status === "not_started" &&
    frozen.run_status === "awaiting_semantic_analysis",
    "frozen measurement manifest status or identity changed");

  const manifest = readJSON("R020_ANALYSIS_MANIFEST.json");
  check(manifest.source_measurement_commit === ledger.measurement_source_commit &&
    manifest.analysis_status === "provisional_semantic_reconstruction_prepared" &&
    manifest.human_utility_evaluation === "pending",
    "analysis provenance or human review status differs from pinned checkpoint");
  check(manifest.analysis_scope.networks === 512 &&
    manifest.analysis_scope.measured_communities_reviewed_as_summaries === 6944,
    "analysis manifest scope does not match measurement");

  const recordsByCell = new Map();
  const seenCommunities = new Set();
  let classified = 0, mixed = 0, unresolved = 0;
  for (let shardIndex = 0; shardIndex < 4; shardIndex++) {
    const lower = shardIndex * 8 + 1, upper = lower + 7;
    const filename = "R020_COMMUNITIES_" + String(lower).padStart(2, "0") + "-" +
      String(upper).padStart(2, "0") + ".json";
    const shard = readJSON(filename);
    if (!check(Array.isArray(shard.records), filename + " missing records array")) continue;
    const observedDecisions = new Set();
    for (const row of shard.records) {
      const d = row.decision_index, state = row.state_index, side = row.side;
      const key = [d, state, side].join("/");
      if (!check(Number.isInteger(d) && d >= lower - 1 && d < upper &&
        row.generated_token_index === d + 1 && Number.isInteger(state) &&
        state >= 0 && state < 8 && SECTORS.has(side),
        filename + " invalid community position " + key)) continue;
      observedDecisions.add(d);
      const id = key + "/" + String(row.community_id);
      check(!seenCommunities.has(id), "duplicate community " + id);
      seenCommunities.add(id);
      recordsByCell.set(key, (recordsByCell.get(key) || 0) + 1);
      if (row.candidate_label === "mixed") mixed++;
      else if (typeof row.candidate_label === "string" && row.candidate_label.length) classified++;
      else unresolved++;
      checkedCommunityRows++;
    }
    check(observedDecisions.size === 8, filename + " does not cover all eight decisions");
  }
  check(checkedCommunityRows === 6944, "community total differs from 6944");
  check(classified === manifest.analysis_scope.candidate_labelled &&
    mixed === manifest.analysis_scope.mixed_competing &&
    unresolved === manifest.analysis_scope.unresolved,
    "labelled/mixed/unresolved totals do not reconcile");

  const cells = readJSON("R020_STATE_CELLS.json");
  check(Array.isArray(cells.cells) && cells.cells.length === 512,
    "not exactly 512 state/sector cells");
  const seenCells = new Set();
  for (const c of cells.cells || []) {
    const key = [c.decision_index, c.state_index, c.side].join("/");
    check(!seenCells.has(key), "duplicate cell " + key);
    seenCells.add(key);
    check(recordsByCell.get(key) === c.communities,
      "community count for " + key + " differs between shard and state cell");
  }
  check(recordsByCell.size === 512 && seenCells.size === 512,
    "expected 512 distinct decision/state/sector cells");
  check(cells.matches?.layer?.length === manifest.analysis_scope.matched_adjacent_depth_community_pairs &&
    cells.matches?.generation?.length === manifest.analysis_scope.matched_adjacent_generation_community_pairs,
    "recorded layer/generation matches do not reconcile");

  const diagnostic = readJSON("R020_DERIVED_DIAGNOSTICS.json");
  check(diagnostic.run_id === EXPECTED_RUN &&
    diagnostic.summary?.community_count === 6944 &&
    diagnostic.summary?.network_count === 512,
    "diagnostic summary does not reconcile with R020 measurement");
}

function run() {
  check(gitBlobSha(Buffer.from("test\n")) === "9daeafb9864cf43055ae93beb0afd6c7d144bfa4",
    "Git blob SHA calculation self-test failed");
  const ledger = readJSON("R020_CHECKPOINT_LEDGER.json");
  check(ledger.run_id === EXPECTED_RUN, "wrong checkpoint run identity");
  const stages = ledger.checkpoints;
  check(Array.isArray(stages) && stages.length === 10 &&
    stages.every((v, i) => v.id === EXPECTED_STAGES[i]), "checkpoint stages are missing, repeated or out of order");
  check(ledger.measurement_source_commit === "6d7d6547e04407556b303b1c8b3ce9941daa8138",
    "measurement source commit changed");

  const knownPaths = new Set();
  for (const stage of stages || []) {
    if (!Array.isArray(stage.paths)) {
      failures.push(stage.id + ": invalid paths");
      continue;
    }
    for (const entry of stage.paths) {
      check(!knownPaths.has(entry.path), "duplicate checkpoint file registration: " + entry.path);
      knownPaths.add(entry.path);
      verifyOne(stage.id, entry);
    }
  }

  if (failures.length === 0) {
    try { verifyCoverage(ledger); }
    catch (e) { failures.push("coverage verification failed: " + e.message); }
  }

  const result = {
    run_id: EXPECTED_RUN,
    passed: failures.length === 0,
    registered_files: knownPaths.size,
    verified_files: verified.length,
    checked_community_rows: checkedCommunityRows,
    human_utility_review: "pending",
    scientific_status: "provisional_semantic_reconstruction",
    failures
  };
  if (process.argv.includes("--json")) console.log(JSON.stringify(result, null, 2));
  else {
    console.log(result.passed ? "R020 CHECKPOINTS: VERIFIED" : "R020 CHECKPOINTS: FAILED");
    console.log(JSON.stringify(result, null, 2));
  }
  if (!result.passed) process.exitCode = 1;
}

run();
