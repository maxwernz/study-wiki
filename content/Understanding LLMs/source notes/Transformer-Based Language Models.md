---
type: source_note
status: processed
scope: local
class: Understanding LLMs
project:
source_type: technical handout
raw_path: raw/TransforMechInterp.pdf
created: 2026-05-14
updated: 2026-06-25
---

# Transformer-Based Language Models

## Summary

This handout (Mohammand-Pour & Franke) is the course's **precise formal
reference** for the transformer. Where Session 03 builds intuition, this fixes
exact notation for every object: vocabulary and token indexing, language as the set
of finite token sequences, the generative/decoder LM as a map to a distribution
over sequences, the autoregressive vs. masked factorizations, and then the full
architecture as a stack of **transformer block functions** $T^{(\ell)}$ — each
composed of attention, FFN, LayerNorm, and residual connections — from zero-layer
embeddings through unembedding to softmax logits. It is the source you cite when an
answer needs to be notationally exact, and the object specification that
mechanistic interpretability later reverse-engineers.

## Key points

- The handout **explicitly warns against over-interpretation**: formally, an
  autoregressive LM just "predicts the next integer in a sequence of integers from
  a finite range $1,\dots,n_V$" — better called a *finite discrete sequence model*.
- **Vocabulary** $\mathcal V$ with bijective index $\mathrm{Ind}:\mathcal V\to\{1,\dots,n_V\}$;
  **language** $L=\{t\in\mathcal V^n\mid n\in\mathbb N\}$ = all finite token sequences.
- A **(decoder) LM** is $M_\theta:X\to\Delta(L)$; the **autoregressive** special
  case is $M_\theta:L\to\Delta(\mathcal V)$ (next-token). **Masked** LMs predict
  tokens *inside* the sequence and are "bidirectional"; next-token is a special
  case of missing-token.
- The model processes the whole context **in parallel** through a chain of $n_L$
  **layers**; the same layer-$\ell$ parameters apply at every position $i$. More
  layers = more iterative processing steps = (tendentially) more capable.
- An **embedding** $x\in\mathbb R^{d_M}$ has dimension $d_M$ = the **model size**.
- A **transformer block** $T^{(\ell)}$ maps a token index $i$ plus all
  previous-layer embeddings to a new embedding $x_i^{(\ell)}$; attention "looks
  back" at the **previous** layer (for parallelism and to avoid circularity).
- The block has four components: **attention**, **FFN**, **LayerNorm**, **residual
  connections**, chained as in Vaswani et al. (2017).
- **Masking** (score $=-\infty$ for inaccessible $j$) is what makes a block respect
  next-token vs. missing-token access.

## Important concepts

- [[Language Models in Understanding LLMs]]
- [[Autoregressive Language Models in Understanding LLMs]]
- [[Transformer Architecture in Understanding LLMs]]
- [[Attention and Self-Attention in Understanding LLMs]]
- [[Embeddings in Understanding LLMs]]
- [[Mechanistic Interpretability in Understanding LLMs]]

## Methods, models, or theories

- **Decoder (generative) LM**, autoregressive and masked factorizations.
- **Transformer block** as a typed function; **zero-layer embedding** (lexical +
  positional); **unembedding** to logits; **softmax** (with temperature/beam-search
  as alternative decoding).
- **LayerNorm** (standardize + learned scale/shift), **FFN** (one hidden layer,
  expand to $d_{FFN}$ then contract), **multi-head attention** (concatenate $n_H$
  heads, output map $W_O$), **Key/Query/Value/Score/Weight** functions.

## Equations or formal definitions

**Transformer block (typed).** For layer $\ell$, position $i$, context size $n_C$:
$$ T^{(\ell)}:\ \big\langle\, i,\ \langle x_1^{(\ell-1)},\dots,x_{n_C}^{(\ell-1)}\rangle\,\big\rangle \ \mapsto\ x_i^{(\ell)}\in\mathbb R^{d_M}. $$
It takes the index of the token plus *all* previous-layer embeddings and returns
that token's new embedding.

**Zero-layer (initial) embedding.** Lexical lookup combined with position:
$$ x_i^{(0)} = F\big(W_E\,\mathrm{Ind}(i),\ \mathrm{PosEmbed}(i)\big), $$
with embedding matrix $W_E\in\mathbb R^{n_V\times d_M}$, positional function
$\mathrm{PosEmbed}(i)\in\mathbb R^{d_M}$ (sinusoidal), and $F$ usually element-wise
addition.

**Block anatomy** (residual + LayerNorm around attention then FFN):
$$ x_i^{(\ell-1,*)} = \mathrm{LayerNorm}^{(\ell,1)}\!\Big(x_i^{(\ell-1)} + \mathrm{Attention}^{(\ell)}\big(i, x_1^{(\ell-1)},\dots,x_{n_C}^{(\ell-1)}\big)\Big), $$
$$ x_i^{(\ell)} = \mathrm{LayerNorm}^{(\ell,2)}\!\Big(x_i^{(\ell-1,*)} + \mathrm{FFN}^{(\ell)}\big(x_i^{(\ell-1,*)}\big)\Big). $$
A residual connection means $G(x)=x+F(x)$.

**LayerNorm** (standardize then affine):
$$ \mathrm{LayerNorm}(x) = \gamma\odot\frac{x-\mu(x)}{\sigma(x)} + \beta, $$
with mean $\mu(x)=\tfrac1{d_M}\sum_i x_i$, std $\sigma(x)=\sqrt{\tfrac1{d_M}\sum_i(x_i-\mu)^2+\epsilon}$,
and learned per-occurrence $\gamma,\beta\in\mathbb R^{d_M}$.

**FFN** (one hidden layer of size $d_{FFN}\approx 2 d_M$):
$$ \mathrm{FFN}^{(\ell)}(x) = W_{out}^{(\ell)}\,\phi\!\big(W_{in}^{(\ell)}x + \beta^{(in,\ell)}\big) + \beta^{(out,\ell)}. $$

**Unembedding → probabilities.** From the final layer $n_L$ at position $i$:
$$ \mathrm{logits}_i = W_U\,x_i^{(n_L)},\qquad P_M(t\mid \mathbf t, i) = \frac{\exp(\mathrm{logits}_i[\mathrm{Ind}(t)])}{\sum_{j=1}^{n_V}\exp(\mathrm{logits}_i[j])}, $$
with unembedding matrix $W_U\in\mathbb R^{n_V\times d_M}$.

**Attention as $n_H$ heads.**
$$ \mathrm{Attention}^{(\ell)}(\cdot) = W_O\,z,\qquad z = \mathrm{AH}_{\ell,1}\,\Vert\cdots\Vert\,\mathrm{AH}_{\ell,n_H}, $$
each head a weighted sum of values:
$$ \mathrm{AH}_{\ell,h}\big(i,\dots\big) = \sum_{j=1}^{n_C}\mathrm{Weight}^{(\ell,h)}(x_i,x_j)\,\mathrm{Value}^{(\ell,h)}(x_j). $$

**Key/Query/Value/Score/Weight.** With $\mathrm{Value}(x)=W_V x$,
$\mathrm{Key}(x)=W_K x$, $\mathrm{Query}(x)=W_Q x$:
$$ \mathrm{Score}^{(\ell,h)}(x_i,x_j) = \begin{cases} -\infty & j \text{ masked for } i \\ \mathrm{Query}(x_i)\cdot \mathrm{Key}(x_j) & \text{otherwise,} \end{cases} $$
$$ \mathrm{Weight}^{(\ell,h)}(x_i,x_j) = \frac{\exp\!\big(d_k^{-1/2}\,\mathrm{Score}(x_i,x_j)\big)}{\sum_{j'=1}^{n_C}\exp\!\big(d_k^{-1/2}\,\mathrm{Score}(x_i,x_{j'})\big)}. $$
Masking $j>i$ with $-\infty$ (and $\exp(-\infty)=0$) is exactly what enforces
left-to-right autoregression.

## Selected visuals

![General transformer architecture](../../outputs/images/TransforMechInterp/transformer-architecture-p001.png)
*The layer stack ($n_L=3$, $n_H=2$, $d_M=8$, $N=4$): the highlighted vertical chain
of blocks computes the last token's embedding from all tokens at the previous
layer (handout Fig. 1).*

![Transformer block anatomy](../../outputs/images/TransforMechInterp/transformer-block-p004.png)
*One block: attention → LayerNorm → FFN → LayerNorm, with residual connections (gray
arrows) around each sublayer (handout Fig. 2).*

## Local relevance

This is the **canonical formal source** for the class: it pins down the objects
([[Transformer Architecture in Understanding LLMs]] is the readable companion) that
[[Mechanistic Interpretability in Understanding LLMs]] later treats as the thing to
reverse-engineer (residual stream, heads, QK/OV). Cite it for exact notation in
assignments and the exam.

## Exam or project relevance

- Reproduce the **block anatomy** equations and the **Score/Weight** definitions.
- Explain **why attention looks back at the previous layer** (parallelism + avoid
  circularity).
- Explain how **masking via $-\infty$ scores** implements autoregression.
- Connect $d_M$ (model size), $d_{FFN}$, $n_L$, $n_H$, $d_k$ to the architecture.

## Links to global concepts

No `Global Wiki/` page updated. Promotion candidate: **Transformer** (this is the
most rigorous local statement of it).

## Open questions

- Which notation from this handout should be standardized across the other local
  notes (e.g. $d_M$ vs. $d$, $W_E$ vs. $E$)? Currently the intuitive notes use
  $E,W,U,V$ and this handout uses $W_E,W_Q,W_K,W_V,W_U$ — worth a notation key.
