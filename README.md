# LLM Semantic Topology Research

This directory is a curated analysis package for an experimental project
examining semantic conflict, language-model behaviour and internal
representation geometry.

## Current evidence state

The package contains a research design, one behavioural case mapping and an
executed Pythia 410M baseline notebook. The saved notebook run demonstrates
behavioural limitations of a small base language model, including a confident
factual error, contradictory reasoning and instruction-following failure.

It does not contain activation captures, representation-geometry measurements,
causal interventions, model weights or evidence that semantic conflict
corresponds to geometric curvature.

## Reading order

1. [`PROJECT_HANDOVER.md`](PROJECT_HANDOVER.md) — the governing research
   objective, questions, epistemic distinctions and proposed phases.
2. [`ZOMBIE_CASE_STUDY.md`](ZOMBIE_CASE_STUDY.md) — how an existing
   ChatGPT zombie-survival interrogation relates to the proposed research,
   including limitations and a candidate controlled stimulus.
3. [`pythia_410m_prompt_playground.ipynb`](pythia_410m_prompt_playground.ipynb)
   — an executable prompt playground and saved RTX 4090 baseline run. Treat the
   outputs as a single-seed behavioural example, not topology evidence.
4. [`ANALYSIS_BRIEF.md`](ANALYSIS_BRIEF.md) — bounded questions for ChatGPT
   to analyse using the preceding material.

## Provenance

- The project handover was supplied by the project owner on 2026-11-12.
- The behavioural case is the public page
  [Zombie Survival by ChatGPT — Why the AI Lies (and How to Stop It)](https://decrepitfilth.art/art/zombie-survival-chatgpt-why-the-ai-lies-and-how-to-stop-it),
  inspected on 2026-11-12.
- The case-study mapping was prepared from the handover and the published page.
- The notebook was copied from the authoritative local `llm_topology`
  project at commit `99103c9212a0aa714995e1082bbba4da26f51965`.
  Its saved outputs were generated on 2026-11-12.
- Model weights are intentionally excluded. The notebook is configured to use
  the machine's shared Hugging Face cache.

This is an analysis copy. It is not an automatic mirror or an authoritative
experimental repository.

## Interpretation boundary

Keep these levels separate throughout analysis:

- observable model responses;
- researcher interpretations of those responses;
- model-generated explanations of its own behaviour;
- measured internal representations;
- causal conclusions supported by interventions.

The notebook and behavioural case provide observations at the first level.
The case also contains researcher interpretations and model-generated
explanations. The proposed project is intended to measure the fourth level and
test the fifth.
