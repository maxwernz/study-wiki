---
type: source_note
status: processed
scope: local
class: Understanding LLMs
project:
source_type: technical slide deck
raw_path: raw/04-TransforMechInterp-slides.pdf
created: 2026-05-14
updated: 2026-06-25
---

# Basic Transformer Architecture Slides

## Summary

This technical slide deck is the **presentation companion** to the formal handout
[[Transformer-Based Language Models]] — same notation, same objects, in slide form.
It formalizes transformer-based language models: tokens, vocabularies, indexing,
finite token sequences, the autoregressive vs. masked factorizations, the
transformer block as a typed function, zero-layer (lexical + positional)
embeddings, unembedding to logits, the four block components (attention, FFN,
LayerNorm, residual), and the attention head's key/query/value scoring with
masking. Use this deck for the visual version; cite the handout note for the
fully-unpacked equations.

## Key points

- A **vocabulary** is a finite set of tokens with a bijective **indexing function**
  $\mathrm{Ind}:\mathcal V\to\{1,\dots,n_V\}$ — emphasizing the model operates on
  token *indices*, not "meanings."
- A **generative LM** maps inputs to a probability distribution over finite token
  sequences; **autoregressive** = predict the next token, **masked** = predict
  selected tokens inside the sequence.
- Transformers process **all positions in parallel** through a stack of blocks;
  layer $\ell$ uses the same parameters at every position.
- **Zero-layer embeddings** combine the lexical token embedding ($W_E\,\mathrm{Ind}(i)$)
  with **positional** information; **final-layer** embeddings are **unembedded**
  ($W_U x^{(n_L)}$) into logits, then softmaxed.
- A **transformer block** = attention + FFN + residual connections + LayerNorm.
- An **attention head** uses query-key **scores**, a **mask** (score $=-\infty$ for
  inaccessible positions), **softmax** weights, and a weighted sum of **value**
  vectors.

## Important concepts

- [[Language Models in Understanding LLMs]]
- [[Autoregressive Language Models in Understanding LLMs]]
- [[Transformer Architecture in Understanding LLMs]]
- [[Attention and Self-Attention in Understanding LLMs]]
- [[Embeddings in Understanding LLMs]]

## Methods, models, or theories

- Autoregressive next-token prediction; masked (bidirectional) language modeling.
- Positional embeddings; unembedding + softmax decoding.
- Multi-head attention; residual connections; layer normalization.

## Equations or formal definitions

**Transformer block as a typed function** (layer $\ell$, position $i$, context size
$n_C$):
$$ T^{(\ell)}:\ \big\langle\, i,\ \langle x_1^{(\ell-1)},\dots,x_{n_C}^{(\ell-1)}\rangle\,\big\rangle \ \mapsto\ x_i^{(\ell)}. $$
It maps a token index plus all previous-layer embeddings to that token's new
embedding.

**Masked attention score and weight:**
$$ \mathrm{Score}(x_i,x_j) = \begin{cases}-\infty & j \text{ masked for } i \\ \mathrm{Query}(x_i)\cdot\mathrm{Key}(x_j) & \text{otherwise,}\end{cases}\qquad \mathrm{Weight}(x_i,x_j) = \mathrm{softmax}_j\!\Big(\tfrac{\mathrm{Score}(x_i,x_j)}{\sqrt{d_k}}\Big). $$

**Unembedding → next-token probability:**
$$ \mathrm{logits}_i = W_U\,x_i^{(n_L)},\qquad P_M(t\mid\mathbf t,i)=\mathrm{softmax}(\mathrm{logits}_i)[\mathrm{Ind}(t)]. $$

The full block anatomy (LayerNorm + FFN equations, multi-head concatenation,
Value/Key/Query definitions) is unpacked symbol-by-symbol in
[[Transformer-Based Language Models]] and conceptually in
[[Transformer Architecture in Understanding LLMs]] — not duplicated here.

## Local relevance

This deck and its handout give the **precise mathematical notation** behind the
intuitive [[Session 03 - Transformers]] lecture, and fix the computational objects
that [[Mechanistic Interpretability in Understanding LLMs]] later interprets.

## Exam or project relevance

- Distinguish **autoregressive vs. masked** language modeling formally.
- Identify the **components of a transformer block** and their order.
- Connect token embeddings → positional embeddings → final logits → softmax
  probabilities.
- Explain **masking** (score $=-\infty$) as the control on which positions a
  prediction may use.

## Links to global concepts

No `Global Wiki/` page updated. Promotion candidate: **Transformer**.

## Open questions

- Which parts of this formal notation are required at equation level for the exam
  vs. for conceptual recognition only?
