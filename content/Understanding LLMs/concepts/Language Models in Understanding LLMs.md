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
  - Session 01 - Introduction
  - Session 02 - PyTorch, Optimization, ANNs, LMs, RNNs, LSTMs
  - Transformer-Based Language Models
created: 2026-05-14
updated: 2026-06-25
---

# Language Models in Understanding LLMs

## Short definition

A language model is a **probability distribution over finite token sequences** —
it assigns each possible string a probability. The course argues this is more
honestly called a "**(finite, discrete) sequence model**," because nothing about
the definition requires it to "understand language."

## Intuition

A language model is a machine that answers one question for any piece of text:
*"how likely is this string to occur?"* Show it "the cat sat on the mat" and it
returns a high number; show it "mat the on sat cat the" and it returns a low one.
That is the entire formal content. Everything impressive that LLMs do — answering
questions, writing code — is squeezed out of this single ability to score how
probable a string is, applied **one token at a time** to *generate* the most
probable continuation. Keeping that in view is the antidote to over-reading: the
model is, at bottom, a very good "what comes next?" estimator, not a mind.

## Explanation

**The formal object.** Let $\mathcal V$ be a finite **vocabulary** of tokens
(characters, sub-words, or words) and $S$ the set of all finite sequences built
from $\mathcal V$. A language model is an element of $\Delta(S)$ — a probability
distribution over *all* such sequences. Optionally it can be **conditioned** on an
input $x$ from a set $X$ (an image to caption, a sentence in another language to
translate); then it is a map $\mathrm{LM}_\theta:X\mapsto\Delta(S)$ with parameters
$\theta$. With a single empty input, it is just a distribution over strings.

**Why "sequence model" is the honest name.** The definition mentions probability
and tokens — not meaning, truth, or intent. A model can assign excellent
probabilities to text while being, formally, a **token-index predictor**. The
lecturers stress this because it pre-empts a series of later confusions: a fluent
model can still hallucinate (high-probability ≠ true), can ace a benchmark without
"reasoning" the way a human does (which motivates
[[Mechanistic Interpretability in Understanding LLMs]] and
[[Probing Classifiers in Understanding LLMs]]), and is **not** automatically a
helpful assistant — pretraining optimizes next-token likelihood, not helpfulness,
which is exactly the gap [[Finetuning and RLHF in Understanding LLMs]] closes.

**What it can and can't capture (the deck's "think break").** A model that
perfectly compressed the true probability of strings over *all human language*
would capture an enormous amount of world knowledge and linguistic regularity —
but it would also faithfully reproduce the biases, falsehoods, and frequency
artifacts of its corpus, and it would have no notion of truth beyond "what tends
to be written." The training distribution (a curated corpus vs. the whole
internet) determines what "likely" even means.

**From definition to a working model.** The distribution over whole sequences is
astronomically large, so it is **factored autoregressively** into next-token
predictions (see [[Autoregressive Language Models in Understanding LLMs]]), each
computed by a neural network ([[Neural Sequence Models in Understanding LLMs]],
[[Transformer Architecture in Understanding LLMs]]) and fit by
[[Optimization for Language Models in Understanding LLMs]].

## Worked example

Tiny vocabulary $\mathcal V=\{\text{the, cat, sat}\}$. A language model assigns a
probability to every finite string over these tokens. For the 2-token string "the
cat" it might give $P(\text{the cat}) = 0.18$, while $P(\text{sat sat}) = 0.002$ —
the model has learned "the cat" is a far more typical English fragment. Crucially
these probabilities over *all* strings of a given length **sum to 1**: it is a
genuine distribution, so making one string more probable necessarily makes others
less so. To make the huge space tractable, the model never stores all those
numbers — it *computes* $P(\text{the cat})$ as $P(\text{the})\cdot
P(\text{cat}\mid\text{the})$, two next-token predictions.

## Formal definition / equations

$$ \mathrm{LM}\in\Delta(S), \qquad \mathrm{LM}_\theta : X \mapsto \Delta(S), $$
where $S$ is the set of all finite sequences over a finite vocabulary $\mathcal V$,
$X$ is an (optional) set of input conditions, $\theta\in\Theta$ the parameters, and
$\Delta(\cdot)$ denotes "probability distribution over." A **neural** language
model is one where this map is realized by a neural network. In the autoregressive
case the distribution over sequences is built from next-token factors:
$$ P_{\mathrm{LM}}(w_{1:n}) = \prod_{i=1}^{n} P_{\mathrm{LM}}(w_i \mid w_{1:i-1}). $$

## Role in this class or project

This is **the central object of the course**. Every later topic is a lens on it:
architectures that *implement* it (RNN/LSTM/transformer/SSM), measures that
*evaluate* it (surprisal, perplexity, benchmarks), methods that *inspect* it
(probing, mechanistic interpretability), and procedures that *align* it
(finetuning, RLHF). Getting the definition precise here keeps all of those honest.

## Exam, assignment, or project relevance

- **Define** a language model as a probability distribution over token sequences;
  state why "(finite, discrete) sequence model" is more precise.
- **Explain** the gap between *language-modeling ability* and *assistant behavior*,
  and why pretraining alone optimizes neither truth nor helpfulness.
- **Connect** the abstract distribution to the autoregressive factorization that
  makes it computable.

## Related global concepts

- Promotion candidate: **Language Model** (general definition reusable across
  classes).

## Related local pages

- [[Autoregressive Language Models in Understanding LLMs]]
- [[Neural Sequence Models in Understanding LLMs]]
- [[Transformer Architecture in Understanding LLMs]]
- [[Finetuning and RLHF in Understanding LLMs]]
- [[Benchmarking LLMs in Understanding LLMs]]

## Common confusions

- **A language model is not automatically an assistant.** Helpful, harmless,
  honest behavior is added later (instruction tuning, RLHF), not implied by the
  definition.
- **High-probability text is not true text.** The model scores typicality, not
  truth — the root of hallucination.
- **Better perplexity does not explain the mechanism.** Predicting well says
  nothing about *how* the model does it; that is what interpretability asks.

## Sources

- [[Session 01 - Introduction]]
- [[Session 02 - PyTorch, Optimization, ANNs, LMs, RNNs, LSTMs]]
- [[Transformer-Based Language Models]]
