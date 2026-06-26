---
type: source_note
status: processed
scope: local
class: Understanding LLMs
project:
source_type: lecture slides
raw_path: raw/04-Transformers-02.pdf
created: 2026-05-14
updated: 2026-06-25
---

# Session 04 - Transformer-based LMs, Benchmarking, Interpretability, Foundation Models

## Summary

This lecture zooms out from "how a transformer works" to "how we *frame, measure,
and instantiate* trained LMs." It opens with **conceptual calibration** — LMs are
**adapted systems** (shaped by an optimization process) rather than top-down
engineered ones, though the *architecture* is designed to make them adapt a certain
way. It gives a **teaser of mechanistic interpretability** (reverse-engineering the
forward pass; the **residual stream** as a sequence of additive updates, decodable
mid-stream by the logit lens — "memory of working memory"). It then surveys
**evaluation**: predictive-accuracy metrics (cross-entropy, surprisal, perplexity),
generation metrics (BLEU, ROUGE, METEOR) and their weaknesses, and **benchmarks**
(GLUE, SuperGLUE, BIG-Bench, HELM). Finally it does **SOTA close-ups**: the three
kinds of LLMs (core/foundation, assistant, application), the **LLaMA** family as a
study in engineering choices, and **BERT** as the bidirectional, masked-LM
counterpoint to autoregressive models.

## Key points

- **Adapted vs. engineered systems.** A trained LM is *adapted* (shaped by training)
  — you design the architecture and objective, not the learned behavior directly.
- **Mechanistic interpretability** = finding concepts/tools to describe how a
  trained LM processes information; the **residual stream** is a sequence of
  **additive** updates where old info is often more important than new, and any
  intermediate stage can be unembedded (**logit lens / early decoding**).
- **Predictive accuracy**: cross-entropy / average surprisal / perplexity on
  held-out text — the same family from Session 02, now as evaluation.
- **Generation metrics** (BLEU-n, ROUGE-n, METEOR) compare output to references;
  all depend on the reference corpus and tokenizer and may misalign with human
  judgment.
- **Benchmarks** standardize tasks + evaluation to track capability and compare
  systems: GLUE (9 tasks), SuperGLUE (8), BIG-Bench (204+), HELM (51 tasks, broad
  metrics incl. calibration, robustness, fairness, toxicity, efficiency).
- **Three kinds of LLM**: **core/foundation** (predict likely next token, e.g.
  GPT-2, LLaMA), **assistant** (finetuned/RLHF, predict tokens that *please the
  user*), **application** (algorithms *using* LLMs — tools, agents, reasoners).
- **LLaMA**: publicly-trained, smaller-model-more-data philosophy (cheaper
  inference); architecture tweaks = **pre-normalization**, **SwiGLU**, **rotary
  positional embeddings**; AdamW; 1.4T BPE tokens; 13B LLaMA ≈ 175B GPT-3.
- **BERT**: bidirectional encoder, 12 layers, hidden 768, ~110M params; trained by
  **masked LM** (15% of tokens: 80% masked / 10% random / 10% unchanged) +
  **next-sentence prediction**; great for representations, not generation.
- **WEIRD/WYOMING** caveat: typical LLM training data is skewed (Western, young,
  opinionated, non-marginalized internet text — Bender et al. 2021).

## Important concepts

- [[Transformer Architecture in Understanding LLMs]]
- [[Mechanistic Interpretability in Understanding LLMs]]
- [[Benchmarking LLMs in Understanding LLMs]]
- [[Language Models in Understanding LLMs]]
- [[Autoregressive Language Models in Understanding LLMs]]

## Methods, models, or theories

### Conceptual calibration
The "trinity (+L)" of computational modeling: an **Idea**, expressed in **Math**,
realized in **Code**, communicated via **Language**. LMs are **adapted systems** —
the analogy to human memory/attention (retrieve relevance when cued, filter by
relevance) frames why attention is a natural design.

### Mechanistic interpretability (teaser)
Reverse-engineer the trained forward pass. The **residual stream** (Elhage et al.
2021) is the key object: each block *adds* to a running representation, the same
function applies at every position, only attention moves information *laterally*
across positions, and the final unembedding can be applied to *any* intermediate
stage (**logit lens**). The slides liken this to **working memory**, with "lateral
access to WM at previous stages" — "memory of working memory." Developed fully in
[[Mechanistic Interpretability in Understanding LLMs]].

### Evaluation
**Predictive accuracy** (perplexity/surprisal — see below) measures held-out text
prediction; it can be confounded by decoding method or finetuning. **Generation
metrics** compare to references (BLEU = n-gram co-occurrence; ROUGE = longest
common subsequence; METEOR = harmonic mean of unigram precision/recall with
synonym/stem matching) but inherit reference- and tokenizer-dependence.
**Benchmarks** package tasks (common-sense, QA, NLU, math, code, linguistic,
expert knowledge) with fixed scoring; collections range from GLUE to the holistic
HELM. Detailed in [[Benchmarking LLMs in Understanding LLMs]].

### SOTA close-ups
**LLaMA** illustrates *engineering* a simple idea: trade a bigger model for a
smaller-but-longer-trained one (cheaper at inference), with pre-norm + SwiGLU +
RoPE tweaks. **BERT** illustrates the *masked / bidirectional* alternative to
autoregression — a strong encoder for representations and cloze tasks, not a
generator (contrast in [[Autoregressive Language Models in Understanding LLMs]]).

## Equations or formal definitions

**Predictive accuracy (held-out fit).**
$$ \text{Avg-Surprisal}_{\mathrm{LM}}(w_{1:n}) = -\tfrac{1}{n}\log P_{\mathrm{LM}}(w_{1:n}),\qquad \mathrm{PP}_{\mathrm{LM}}(w_{1:n}) = P_{\mathrm{LM}}(w_{1:n})^{-\frac1n}, $$
so $\log \mathrm{PP} = \text{Avg-Surprisal}$ — perplexity is the exponential of
average per-token surprisal (lower = better prediction). Same quantities as
training cross-entropy (Session 02), now on a **test** set.

**Generation metric (BLEU-$n$, schematic).** Roughly the geometric mean of
modified $n$-gram precisions between candidate and references, times a brevity
penalty:
$$ \mathrm{BLEU} = \mathrm{BP}\cdot\exp\!\Big(\sum_{k=1}^{n} w_k \log p_k\Big), $$
with $p_k$ = clipped $k$-gram precision, $w_k$ = weights, $\mathrm{BP}$ = brevity
penalty. ROUGE and METEOR vary the matching unit; all depend on the reference set.

**Residual stream update** (the interpretability object):
$$ x^{(\ell)} = x^{(\ell-1)} + \text{Attention}^{(\ell)}(\cdot) + \text{FFN}^{(\ell)}(\cdot), $$
an additive accumulation across layers — the basis for logit-lens decoding.

## Local relevance

This lecture is the hinge from *architecture* to *evaluation and interpretation*.
It seeds three later threads: benchmarking ([[Benchmarking LLMs in Understanding LLMs]]),
mechanistic interpretability ([[Mechanistic Interpretability in Understanding LLMs]]),
and the base-vs-assistant distinction that motivates
[[Finetuning and RLHF in Understanding LLMs]].

## Exam or project relevance

- **Explain** why benchmark scores are useful but incomplete (crude summary stats,
  reference/tokenizer dependence, possible human-judgment mismatch).
- **Distinguish** predictive-accuracy metrics from task/generation benchmarks.
- **Distinguish** core LLMs, assistant-tuned LLMs, and LLM-based applications.
- **State** BERT's training regime (MLM 15%/80-10-10 + NSP) and **why it is not a
  generator**.
- **Name** LLaMA's architecture tweaks (pre-norm, SwiGLU, RoPE) and its
  smaller-model-more-data rationale.

## Links to global concepts

No `Global Wiki/` page updated. Promotion candidates: **Perplexity**, **BLEU/ROUGE**,
**Foundation Models**.

## Open questions

- How will later lectures separate **behavioral** benchmarks from **mechanistic**
  explanations?
- Which evaluation metrics are expected at **formula** level vs. recognition level
  for the exam?
