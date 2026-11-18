#!/usr/bin/env node
"use strict";
// R020 second-pass reconstruction integrity verifier.
// Run from a complete checkout: node R020_VERIFY_RELATIONAL_V2.js
// Read only. A nonzero exit code means no checkpoint should be reused.
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const HERE=__dirname,ROOT=path.resolve(HERE,".."),RUN="R020_pythia-70m-representation-output-contrast";
const failure=[];
function assert(ok,why){if(!ok)failure.push(why);return ok}
function file(f){const p=path.resolve(HERE,f);const rel=path.relative(ROOT,p);if(!rel||rel===".."||rel.startsWith(".."+path.sep)||path.isAbsolute(rel))throw Error("unsafe path "+f);return p}
function json(f){return JSON.parse(fs.readFileSync(file(f),"utf8"))}
function sha(f){const b=fs.readFileSync(file(f));return crypto.createHash("sha1").update(Buffer.from("blob "+b.length+"\0")).update(b).digest("hex")}
function signature(g){return new Set(g.communities.flatMap(n=>n.representative_token_ids))}
function jaccard(A,B){let shared=0;for(const t of A)if(B.has(t))shared++;return shared/(A.size+B.size-shared||1)}
function main(){
 const manifest=json("R020_V2_CHECKPOINT_MANIFEST.json");
 assert(manifest.run_id===RUN,"wrong run id");
 assert(manifest.analysis_revision==="relational_v2","wrong analysis revision");
 assert(Array.isArray(manifest.artifacts),"missing pinned artefacts");
 const known=new Set;
 for(const p of manifest.artifacts){
   assert(!known.has(p.path),"duplicate pinned file "+p.path);known.add(p.path);
   assert(/^[0-9a-f]{40}$/.test(p.git_blob_sha),"malformed SHA "+p.path);
   try{assert(sha(p.path)===p.git_blob_sha,"SHA mismatch "+p.path)}catch(e){failure.push("missing or unreadable "+p.path+" "+e.message)}
 }
 if(failure.length){console.error(JSON.stringify({passed:false,failures:failure},null,2));process.exitCode=1;return}
 const shards=["01-08","09-16","17-24","25-32"].map((x,i)=>json("R020_RELATIONAL_MAP_D"+x+".json"));
 const graphs=shards.flatMap(x=>x.graphs),byKey=new Map,seen=new Set;let communities=0,modules=0,backbones=0;
 shards.forEach((sh,i)=>{assert(sh.network_count===128,"shard "+i+" network count");assert(sh.decisions[0]===i*8+1&&sh.decisions[1]===(i+1)*8,"shard "+i+" range");assert(sh.raw_network_git_blob_sha===manifest.raw_network_git_blob_sha,"shard raw source mismatch");});
 for(const g of graphs){
  const key=[g.decision_index,g.state_index,g.side].join("|");
  assert(!seen.has(key),"duplicate state-sector "+key);seen.add(key);byKey.set(key,g);
  assert(g.decision_index>=0&&g.decision_index<32&&g.state_index>=0&&g.state_index<8&&["positive_head","negative_tail"].includes(g.side),"invalid graph key "+key);
  assert(g.communities.length===g.community_count,"community count "+key);
  communities+=g.communities.length;modules+=g.modules.length;backbones+=g.backbone_edges.length;
  const nodes=new Map(g.communities.map(c=>[c.id,c])),counts=new Map;
  assert(nodes.size===g.communities.length,"duplicate community IDs "+key);
  for(const mod of g.modules){for(const id of mod.community_ids){assert(nodes.has(id),"orphan module ID "+key+"/"+id);counts.set(id,(counts.get(id)||0)+1);assert(nodes.get(id)?.module_id===mod.module_id,"module label mismatch "+key+"/"+id)}}
  for(const id of nodes.keys())assert(counts.get(id)===1,"community not in exactly one module "+key+"/"+id);
  for(const e of g.backbone_edges){assert(nodes.has(e.a)&&nodes.has(e.b),"orphan edge "+key);assert(e.count>0&&Number.isFinite(e.affinity)&&e.affinity>=0,"invalid edge weight "+key)}
 }
 assert(graphs.length===512&&seen.size===512,"expected 512 state-sector maps");
 assert(communities===6944,"expected 6944 communities");
 assert(modules===1231,"expected 1231 structural modules");
 const tr=json("R020_RELATIONAL_TRAJECTORIES.json");
 assert(tr.transitions.length===944,"expected 944 transition cases");
 const depth=tr.transitions.filter(x=>x.axis==="depth"),generation=tr.transitions.filter(x=>x.axis==="generation");
 assert(depth.length===448&&generation.length===496,"transition axis counts");
 assert(depth.reduce((n,x)=>n+x.candidate_count,0)===901&&generation.reduce((n,x)=>n+x.candidate_count,0)===1084,"candidate transition link counts");
 for(const t of tr.transitions){const a=byKey.get([t.from.decision_index,t.from.state_index,t.from.side].join("|")),b=byKey.get([t.to.decision_index,t.to.state_index,t.to.side].join("|"));assert(!!a&&!!b,"transition graph missing");
  assert(t.candidate_count===t.candidate_module_links.length,"candidate count mismatch");
  if(t.axis==="depth")assert(t.to.decision_index===t.from.decision_index&&t.to.state_index===t.from.state_index+1,"invalid depth transition");
  else assert(t.to.decision_index===t.from.decision_index+1&&t.to.state_index===t.from.state_index,"invalid generation transition");
  for(const l of t.candidate_module_links){assert(a.modules.some(x=>x.module_id===l.source_module)&&b.modules.some(x=>x.module_id===l.target_module),"orphan transition module");assert(l.shared>=4&&l.overlap>=.08,"unsupported module link");}
 }
 const diag=json("R020_REPRESENTATIVE_REUSE_DIAGNOSTICS.json");
 assert(diag.comparisons.length===16,"expected 8 states x 2 sectors reuse rows");
 assert(diag.current_input_token_ids.length===32,"input alignment missing");
 for(const q of diag.comparisons){const id=q.side==="positive_head"?"positive_head":"negative_tail";const arrays={same:[],other:[]};
   for(let a=0;a<32;a++)for(let b=a+1;b<32;b++){let A=signature(byKey.get([a,q.state,id].join("|"))),B=signature(byKey.get([b,q.state,id].join("|"))),val=jaccard(A,B);arrays[diag.current_input_token_ids[a]===diag.current_input_token_ids[b]?"same":"other"].push(val)}
   const means=k=>arrays[k].reduce((x,y)=>x+y,0)/arrays[k].length;
   assert(arrays.same.length===26&&arrays.other.length===470,"reuse pair counts");
   assert(Math.abs(means("same")-q.identical_input.mean)<1e-5&&Math.abs(means("other")-q.different_input.mean)<1e-5,"reuse mean fails "+id+" S"+q.state);
 }
 const html=fs.readFileSync(file("R020_RELATIONAL_SEMANTIC_MAPS.html"),"utf8");
 const match=html.match(/<script id="mapdata" type="application\/json">([\s\S]*?)<\/script>\s*<script>\s*([\s\S]*?)<\/script>/);
 assert(!!match,"interactive HTML data/scripts missing");
 if(match){try{const parsed=JSON.parse(match[1]);assert(parsed.graphs.length===512&&parsed.graphs.reduce((a,x)=>a+x.nodes.length,0)===6944,"HTML coverage mismatch");new Function(match[2])}catch(e){failure.push("HTML invalid "+e.message)}}
 const outcome={passed:failure.length===0,networks:graphs.length,communities,modules,display_backbone_edges:backbones,transitions:tr.transitions.length,candidate_module_links:1985,registered_artifacts:manifest.artifacts.length,human_usefulness:"pending",failures:failure};
 console.log(JSON.stringify(outcome,null,2));if(!outcome.passed)process.exitCode=1;
}
try{main()}catch(e){console.error("R020 relational verifier failed:",e.stack||e.message);process.exitCode=1}
