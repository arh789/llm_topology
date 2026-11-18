# R020 Hypothesis

## User prompt

i want to consider another run. the model used must be intentionally very small.

my hypotheses is that a very small model will produce a response to a prompt that is largely gibberish and fundamentally useless, but if we extract the top tokens from each transformer layer, we can extract semantic patterns about the topic that are useful. i consider this as evidence that extracting the learned semantic patters is more useful than the response itself.

thoughts?

## Codex response

Yes—this is a strong next experiment. The sharper hypothesis is:

> A model can retain recoverable, prompt-conditioned semantic organisation even when it lacks the capacity to turn that organisation into a useful continuation.

That would separate two capabilities often treated as identical:

```text
learned semantic associations
            ≠
ability to express them coherently
```

I would use an intentionally extreme model such as **Pythia 70M**. It is small enough to make the hypothesis meaningful, while fitting the existing hidden-state pipeline.

The run should compare two independently evaluated products from the same prompt:

1. A fixed-length greedy continuation.
2. Layer-wise vocabulary projections, networks, communities and inferred parent structures.

For a fair test:

- Use a base-model-compatible completion such as:  
  `The relationship between choke point, collapsible barrier, and spear is`
- Capture the final prompt-position state at every layer before generation.
- Reuse the three concept-order permutations.
- Keep generation deterministic.
- Judge the continuation and semantic reconstruction independently.
- Blind the semantic analyst to the generated continuation.
- Include the input-embedding state and a shuffled-token control, so apparent coherence cannot merely be supplied by the analyst.
- Treat top tokens as evidence inputs, but reconstruct communities and parent structures as in previous runs rather than relying on isolated token lists.

A successful result would look like:

```text
GENERATED CONTINUATION
incoherent, irrelevant or semantically incomplete

LAYER TOPOLOGY
stable topic-relevant structures such as:
├─ spatial boundary
├─ obstruction / restriction
├─ movement / approach
└─ weapon / piercing
```

Ideally, those structures would survive prompt-order changes and outperform both the static input-neighbourhood baseline and shuffled control.

The run would fail to support the hypothesis if:

- the continuation is already useful;
- the extracted topology is mostly prompt repetition or tokenizer noise;
- the structures vary arbitrarily between permutations;
- shuffled tokens appear equally interpretable; or
- useful patterns only appear once the analyst knows the intended topic.

If successful, the defensible conclusion would be:

> Poor generative output does not imply an absence of learned semantic structure. Representational analysis can expose useful associations that the model cannot reliably verbalise.

It would not prove that layer projections are literal reasoning or that they are always more useful than generated responses. It would establish the narrower—and genuinely important—result that **representational usefulness can exceed generative usefulness for the same model and prompt**.

## Prompt refinement

### User prompt

that question doesn't involve identifying interesting adjacent topics.

### Codex response

You’re right. The question should be trivial to answer but **semantically broad enough to activate several adjacent domains**.

A better prompt is:

```text
Question: Why would a city build a bridge across a river?
Answer:
```

The direct answer is simple:

> To connect places and allow people and goods to cross.

But its semantic neighbourhood can include:

```text
CITY / BRIDGE / RIVER
        |
        ├─ engineering / construction / materials
        ├─ transport / roads / movement
        ├─ geography / water / environment
        ├─ infrastructure / planning / government
        ├─ access / connectivity / communities
        └─ commerce / logistics / trade
```

This tests something more interesting than whether the layers recover the word `melts`. It asks whether a tiny model’s internal states expose a wider learned organisation around an elementary question.

The layer trajectory could potentially show:

```text
individual objects
city + bridge + river
        ↓
functional relation
crossing + connection
        ↓
adjacent systems
transport + infrastructure + planning
        ↓
broader consequences
access + trade + community development
```

The critical distinction would be:

- **Core structure:** what is required to answer the question.
- **Adjacent structure:** relevant learned associations not required in the minimal answer.
- **Noise:** unrelated or merely lexical material.

The input-embedding baseline would show the associations already attached to the individual words. Intermediate layers would only add value if they reorganise those associations around the combined situation—particularly ideas such as connectivity, infrastructure, movement or trade.

This is a much better R020 prompt: the answer is trivial, but the surrounding learned semantic topology is potentially rich.
