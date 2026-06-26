---
type: concept
status: active
scope: local
classes:
  - Understanding LLMs
projects:
domains:
  - natural language processing
  - representation learning
sources:
  - Session 01 - Introduction
  - Session 02 - PyTorch, Optimization, ANNs, LMs, RNNs, LSTMs
  - Transformer-Based Language Models
created: 2026-05-14
updated: 2026-06-25
---

# Embeddings in Understanding LLMs

## Short definition

An **embedding** is a dense, continuous vector that represents a discrete token (or
a whole sequence). It converts symbols the network can't do arithmetic on (word
IDs) into points in a space where similarity and structure are encoded as geometry.

## Intuition

A neural network only does arithmetic on numbers, but words are symbols. The naive
fix — number the vocabulary 1, 2, 3, … — is terrible, because the numbers imply a
meaningless order (is "cat" really halfway between "car" and "cup"?). The next fix,
**one-hot vectors** (a 1 in the word's slot, 0 everywhere else), removes the false
order but makes every word equidistant from every other — "cat" is no closer to
"dog" than to "bureaucracy." An **embedding** replaces that with a learned dense
vector, *positioned so that geometry carries meaning*: words used in similar
contexts land near each other. The famous illustration is that directions become
meaningful — $\text{king}-\text{man}+\text{woman}\approx\text{queen}$.

## Explanation

**Distributed representations.** An embedding is a **distributed representation**:
information about a token is spread across all coordinates of a dense vector rather
than localized in one slot (as in one-hot). The guiding principle is the
**distributional hypothesis** — "you shall know a word by the company it keeps" —
so the training signal that shapes embeddings is *which words co-occur*.

**Type vs. token (static vs. contextualized).** This is the key distinction the
deck draws:
- **Word (type) embeddings** assign *one* fixed vector per word type (word2vec,
  GloVe). "bank" gets a single vector that blends the river-bank and money-bank
  senses — a *type-based* representation.
- **Contextualized (token) embeddings** assign a vector to each *occurrence*,
  computed from the surrounding sequence. In a transformer, "bank" in "river bank"
  and "bank loan" get *different* vectors because self-attention mixes in the
  neighbors. These are *token-based* representations and are what make transformers
  powerful (see [[Attention and Self-Attention in Understanding LLMs]]).

**Where embeddings live in the pipeline.** At the input, an **embedding matrix**
$E$ maps each one-hot token to its dense vector ($x = E w$). The network then
transforms these vectors layer by layer; in a transformer, **positional**
information is added so order is preserved, and each layer produces increasingly
contextualized representations. At the output, an **unembedding** (often the
transpose of $E$, "weight tying") maps the final hidden vector back to a logit per
vocabulary item, which softmax turns into the next-token distribution. The
**embedding dimension** $d$ — the width of these vectors — is the main number meant
by a model's "hidden size."

**Sequence embeddings.** Beyond single tokens, a whole sequence can be summarized
into one vector (e.g. the final hidden state, or a pooled/[CLS] representation) for
classification or retrieval — the basis for the retrieval step in
[[Retrieval-Augmented Generation in Understanding LLMs]].

## Worked example

Suppose $d=4$ and the learned embeddings are
$E_{\text{cat}}=[0.9,0.1,-0.2,0.3]$, $E_{\text{dog}}=[0.8,0.2,-0.1,0.4]$,
$E_{\text{car}}=[-0.3,0.7,0.5,-0.6]$. Cosine similarity puts "cat" and "dog" close
(both animals, similar contexts) and both far from "car." A static embedding stops
here — "bank" would have one vector forever. A **contextualized** model instead
starts from $E_{\text{bank}}$ and, after attention over "river bank," shifts it
toward a cluster near "water, shore," while in "bank loan" it shifts toward
"money, finance" — the same input embedding, two different output vectors,
depending on neighbors.

## Formal definition / equations

**Embedding lookup.** With one-hot token $w\in\{0,1\}^{|\mathcal V|}$ and embedding
matrix $E\in\mathbb R^{d\times|\mathcal V|}$:
$$ x = E w \in \mathbb R^{d}, $$
which simply selects the column of $E$ for that token. $d$ is the embedding
dimension; $|\mathcal V|$ the vocabulary size.

**Unembedding (output projection).** Final hidden vector $h\in\mathbb R^d$ →
vocabulary logits → distribution:
$$ \text{logits} = W_U\, h \in\mathbb R^{|\mathcal V|}, \qquad P(\cdot) = \mathrm{softmax}(W_U h), $$
where $W_U\in\mathbb R^{|\mathcal V|\times d}$ is the unembedding matrix (often
$W_U = E^\top$, *weight tying*).

**Similarity** between two embeddings (how "alike" two tokens are):
$$ \cos(u,v) = \frac{u\cdot v}{\|u\|\,\|v\|}. $$

## Role in this class or project

Embeddings are the **representational substrate** of every model in the course —
the input to RNNs/LSTMs ([[Neural Sequence Models in Understanding LLMs]]) and
transformers ([[Transformer Architecture in Understanding LLMs]]), the thing
self-attention *contextualizes*, and the object that interpretability methods read
(the residual stream in
[[Mechanistic Interpretability in Understanding LLMs]] is a running sum of
embedding-space updates; the logit lens decodes intermediate embeddings through the
unembedding).

## Exam, assignment, or project relevance

- **Distinguish** one-hot indices, static word embeddings, and contextualized token
  embeddings — and say why each step is an improvement.
- **Explain** the embedding lookup ($x=Ew$) and unembedding/weight-tying.
- **Connect** "model size / hidden dimension" to embedding dimension $d$.
- **Explain** how contextualization makes "bank" polysemy-aware.

## Related global concepts

- Promotion candidates: **Word Embeddings / Distributed Representations**,
  **Distributional Hypothesis**.

## Related local pages

- [[Language Models in Understanding LLMs]]
- [[Neural Sequence Models in Understanding LLMs]]
- [[Attention and Self-Attention in Understanding LLMs]]
- [[Transformer Architecture in Understanding LLMs]]

## Common confusions

- **Embeddings are not meanings.** They are coordinates learned to serve the
  training objective; they correlate with meaning but aren't definitions.
- **Static embeddings conflate senses.** One vector per type can't separate "river
  bank" from "bank loan"; only contextualized embeddings can.
- **Embedding dimension ≠ vocabulary size.** $d$ (vector width, e.g. 768) is
  unrelated to $|\mathcal V|$ (number of tokens, e.g. 50k); the embedding matrix is
  $d\times|\mathcal V|$.

## Sources

- [[Session 01 - Introduction]]
- [[Session 02 - PyTorch, Optimization, ANNs, LMs, RNNs, LSTMs]]
- [[Session 03 - Transformers]]
- [[Transformer-Based Language Models]]
