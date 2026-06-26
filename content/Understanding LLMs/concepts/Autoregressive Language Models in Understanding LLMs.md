---
type: concept
status: active
scope: local
classes:
  - Understanding LLMs
projects:
domains:
  - natural language processing
  - machine learning
sources:
  - Session 02 - PyTorch, Optimization, ANNs, LMs, RNNs, LSTMs
  - Session 03 - Transformers
  - Transformer-Based Language Models
created: 2026-05-14
updated: 2026-06-25
---

# Autoregressive Language Models in Understanding LLMs

## Short definition

An **autoregressive** (left-to-right / causal) language model maps a token
**prefix** $w_{1:n}$ to a probability distribution over the **next** token,
$\mathrm{LM}:w_{1:n}\mapsto\Delta(\mathcal V)$. Whole-sequence probabilities are
built by chaining these one-step predictions.

## Intuition

It is the autocomplete principle taken to its limit. Given everything written so
far, the model produces a probability for every possible next token; you pick one
(the most probable, or a sample), append it, and ask again. Generation is just
this loop run forward; training is the same loop run over real text, checking at
each position whether the model put enough probability on the token that actually
came next. "Autoregressive" literally means *regressing on itself*: each new token
is predicted from the model's own previous outputs.

## Explanation

**The factorization.** Scoring a whole sequence directly is intractable (there are
$|\mathcal V|^n$ sequences of length $n$). The **chain rule of probability** lets
us break it into a product of conditionals — each a single next-token prediction.
This is exact, not an approximation: it always holds for any distribution. What
makes it *useful* is that one neural forward pass computes each factor.

**Training.** Feed real text; at every position the model predicts a distribution
over the next token, and the loss is the **cross-entropy / surprisal** of the
*actual* next token (see
[[Optimization for Language Models in Understanding LLMs]]). With **teacher
forcing**, the conditioning prefix is the *true* preceding text, not the model's
own earlier guesses, so a single bad prediction doesn't derail the rest of the
sequence during learning.

**Generation.** Start from a prompt, sample or argmax the next token from
$P(w_{n+1}\mid w_{1:n})$, append it, and repeat. Because each step conditions on
all previous tokens, the model can produce coherent long text — but it is still
choosing one token at a time, with no explicit lookahead or plan.

**Causal masking (the transformer twist).** A transformer sees the whole sequence
at once, so to stay autoregressive it must be **forbidden from looking at future
tokens**. This is enforced by a **causal mask** in self-attention: position $i$ may
attend only to positions $\le i$. This is how a non-recurrent architecture stays
left-to-right (see [[Attention and Self-Attention in Understanding LLMs]]).

**Contrast: masked LMs (BERT-style).** Instead of predicting the next token,
masked language modeling hides random tokens *inside* the sequence and predicts
them from **both** sides. This gives bidirectional, representation-rich embeddings
(great for classification, retrieval) but is not a natural left-to-right
**generator**. Autoregressive (GPT-style) models are the opposite trade-off:
built for generation, only ever conditioning on the left context.

## Worked example

Prefix "the cat". The model outputs $P(\cdot\mid\text{the cat})$, say
$P(\text{sat})=0.6,\;P(\text{ran})=0.3,\;P(\text{slept})=0.1$. The sequence
probability so far is
$$ P(\text{the cat sat}) = P(\text{the})\cdot P(\text{cat}\mid\text{the})\cdot P(\text{sat}\mid\text{the cat}). $$
If those factors are $0.4,\,0.5,\,0.6$, then $P(\text{the cat sat}) = 0.12$. The
**surprisal** of the realized token "sat" is $-\log 0.6 \approx 0.51$ nats — the
training loss at that position. During generation we'd emit "sat" (the argmax) and
re-query with "the cat sat".

## Formal definition / equations

**Next-token map and chain-rule factorization:**
$$ \mathrm{LM}: w_{1:n}\mapsto \Delta(\mathcal V), \qquad P_{\mathrm{LM}}(w_{1:n}) = \prod_{i=1}^{n} P_{\mathrm{LM}}(w_i \mid w_{1:i-1}). $$
$w_{1:i-1}$ is the prefix conditioning the $i$-th prediction; the first factor uses
the empty prefix.

**Surprisal of the next token:**
$$ \text{surprisal}(w_{n+1}) = -\log P_{\mathrm{LM}}(w_{n+1}\mid w_{1:n}). $$
This is precisely the per-token training loss and the building block of perplexity
and average surprisal (see
[[Session 02 - PyTorch, Optimization, ANNs, LMs, RNNs, LSTMs]]).

**Causal mask** (transformer self-attention, scores $S_{ij}$ before softmax):
$$ S_{ij} \leftarrow -\infty \quad\text{for } j>i, $$
so future positions get zero attention weight after the softmax — enforcing the
left-to-right conditioning.

## Role in this class or project

Autoregression is the *operating mode* of the GPT-style models the course centers
on: it is how they are pretrained and how they generate. It links the abstract
[[Language Models in Understanding LLMs]] distribution to the concrete loss in
[[Optimization for Language Models in Understanding LLMs]], and the causal-masking
mechanism is a recurring detail in
[[Transformer Architecture in Understanding LLMs]] and
[[Attention and Self-Attention in Understanding LLMs]].

## Exam, assignment, or project relevance

- **Derive** sequence probability from the chain rule and define surprisal.
- **Explain** teacher forcing and why it's used in training.
- **Explain** why a transformer needs **causal masking** to be autoregressive.
- **Contrast** GPT-style autoregressive with BERT-style masked modeling and their
  respective strengths (generation vs. representation).

## Related global concepts

- Promotion candidate: **Autoregressive Model / Chain Rule of Probability**.

## Related local pages

- [[Language Models in Understanding LLMs]]
- [[Attention and Self-Attention in Understanding LLMs]]
- [[Transformer Architecture in Understanding LLMs]]
- [[Benchmarking LLMs in Understanding LLMs]]

## Common confusions

- **Autoregressive ≠ recurrent.** Transformers are autoregressive via causal
  masking, with no hidden-state recurrence.
- **Next-token prediction ≠ planning.** Coherent output emerges from greedy/local
  choices; the model does not explicitly plan a whole answer in advance.
- **The chain-rule factorization is exact**, not an approximation — the
  "limitation" of autoregressive models is the *left-only* conditioning, not the
  factorization itself.

## Sources

- [[Session 02 - PyTorch, Optimization, ANNs, LMs, RNNs, LSTMs]]
- [[Session 03 - Transformers]]
- [[Basic Transformer Architecture Slides]]
- [[Transformer-Based Language Models]]
