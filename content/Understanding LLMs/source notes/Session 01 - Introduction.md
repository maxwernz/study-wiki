---
type: source_note
status: processed
scope: local
class: Understanding LLMs
project:
source_type: lecture slides
raw_path: raw/01-UnderLLMs-2026-introduction.pdf
created: 2026-05-14
updated: 2026-06-25
---

# Session 01 - Introduction

## Summary

The opening lecture frames the course around a single image: *"we built a creature —
but what does it do, how, and why?"* We can observe **training** and **inference**,
but its **behavior** and **internal mechanisms** are not yet understood — and closing
that gap is the course's mission. After course logistics (6 CP: homework + a
conceptual in-class exam; optional +3 CP project), it gives **a short history of
language modeling** that doubles as the syllabus map: from symbolic machine
translation and Shannon's information-theoretic next-symbol prediction, through
**n-gram/Markov** models and their sparsity problems (Zipf, smoothing), formal
grammars, ELIZA/PARRY, HMMs, IBM Model I, and **word2vec**, to LSTMs, transformers,
BERT/GPT, RLHF, and mechanistic interpretability. The throughline: today's LLMs pursue
the oldest goal (machines that converse) with the newest tools (scale + attention),
which is why the course pairs capability with **critical distrust**.

## Key points

- The course separates three explanatory targets: **training**, **inference
  behavior**, and **internal mechanisms** — we have the first two, not the last two.
- Goals: understand LM architectures/training/inference; use pretrained LMs well
  (in-context learning, prompting); know the assessment & interpretability literature;
  critically evaluate the technology's implications.
- Language modeling begins (Shannon) as **next-symbol prediction over a signal
  stream** — no need to predefine linguistic "units."
- The **Markov assumption** truncates history to the previous $k$ symbols → **n-gram
  models** ($n=k+1$), estimated from counts.
- **Zipf's law** (few frequent words, many rare ones) makes counts **sparse**;
  **smoothing** (add-$\alpha$) prevents zero probabilities for unseen events.
- The timeline runs: formal grammars → POS tagging → ELIZA/PARRY → **HMMs** → **IBM
  Model I** (data-driven MT, alignment) → **word2vec** (distributional embeddings) →
  LSTMs → transformers → BERT/GPT → RLHF → Mamba / interpretability.

## Important concepts

- [[NLP History in Understanding LLMs]]
- [[Language Models in Understanding LLMs]]
- [[Autoregressive Language Models in Understanding LLMs]]
- [[Neural Sequence Models in Understanding LLMs]]
- [[Transformer Architecture in Understanding LLMs]]
- [[Mechanistic Interpretability in Understanding LLMs]]
- [[Finetuning and RLHF in Understanding LLMs]]

## Methods, models, or theories

### Shannon's signal-stream view → Markov → n-grams
Treat text as a stream of characters and **predict the next one from history $h$**.
Full history is unwieldy, so assume only the previous $k$ symbols matter (the **$k$-th
order Markov assumption**), giving **n-gram models**. Probabilities come from
**counts** of length-$(k{+}1)$ sequences: $k{=}0$ unigram, $k{=}1$ bigram, $k{=}2$
trigram. This is the count-based ancestor of every model in the course (see
[[NLP History in Understanding LLMs]] for the worked bigram example).

### Zipf, sparsity, and smoothing
**Zipf's law** says a few terms are very frequent and most barely appear, so most
n-grams are unseen → MLE assigns them probability 0. **Add-$\alpha$ (Laplace)
smoothing** adds a small pseudo-count to every event, keeping a gap between "seen
once" and "never seen."

### Rule-based and statistical milestones
**Formal grammars** compose symbols by rules; **POS tagging** annotates words to
reduce ambiguity. **ELIZA/PARRY** faked conversation with ranked pattern-response
rules (PARRY adding an affective state model). **HMMs** reason over hidden states from
observations. **IBM Model I** learned translation from parallel corpora — "no rules or
linguists," introducing the alignment problem and the "more data is better" ethos.

### Toward neural LMs
**word2vec** operationalized the **distributional hypothesis** as dense embeddings
(CBOW / skip-gram), enabling vector arithmetic on meaning — the bridge to
[[Embeddings in Understanding LLMs]] and the neural era.

## Equations or formal definitions

**Markov ($k$-th order) assumption and n-gram MLE:**
$$ P(w_i\mid w_{1:i-1}) \approx P(w_i\mid w_{i-k:i-1}) = \frac{c(w_{i-k:i})}{c(w_{i-k:i-1})}, $$
where $c(\cdot)$ is a corpus count and $n=k+1$.

**Add-$\alpha$ (Laplace) smoothing** (vocabulary size $V$, total count $N$):
$$ \hat p(w_i) = \frac{c(w_i) + \alpha}{N + V\alpha}. $$
$\alpha$ is a pseudo-count added to every event ($\alpha=1$ = add-one); it removes
zero probabilities while preserving the order of seen vs. unseen events.

**HMM components:** hidden states $Q=\{q_1,\dots,q_N\}$, transitions $A=\{a_{ij}\}$,
emissions $B=\{b_i(o_t)\}$, initial distribution $\Pi$, observations
$O=\{o_1,\dots,o_T\}$.

## Local relevance

This lecture is the **organizing map** for the class: each later session fills in one
era of this timeline (formal LMs → ANNs/LSTMs → transformers → benchmarking →
interpretability → finetuning/RLHF → alternative architectures). The
training/behavior/mechanism distinction recurs in
[[Mechanistic Interpretability in Understanding LLMs]] and
[[Behavioral Assessment and Calibration in Understanding LLMs]].

## Exam or project relevance

- **Treat** language modeling as sequence-probability estimation; place transformers
  and RLHF in the broader NLP history.
- **Explain** why count-based models need smoothing (Zipf → sparsity) and have limited
  context (Markov truncation); state the n-gram MLE and add-$\alpha$ formulas.
- **Distinguish** training, inference behavior, and internal mechanisms as separate
  explanatory targets.

## Links to global concepts

No `Global Wiki/` page updated at ingestion. Promotion candidates: **n-gram Language
Models**, **Markov Chain / HMM**, **Distributional Semantics**.

## Open questions

- Which course concepts should be promoted to `Global Wiki/` once they recur across
  classes?
- How will the course operationalize "understanding" across behavioral assessment,
  probing, and mechanistic interpretability?
