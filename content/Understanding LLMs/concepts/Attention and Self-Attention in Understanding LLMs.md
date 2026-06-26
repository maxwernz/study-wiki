---
type: concept
status: active
scope: local
classes:
  - Understanding LLMs
projects:
domains:
  - natural language processing
  - neural networks
sources:
  - Session 03 - Transformers
  - Basic Transformer Architecture Slides
  - Transformer-Based Language Models
created: 2026-05-14
updated: 2026-06-25
---

# Attention and Self-Attention in Understanding LLMs

## Short definition

**Attention** computes an output as a **weighted sum of value vectors**, where the
weights say how relevant each item is to a given query. **Self-attention** applies
this *within a single sequence*, so each token's new representation is a weighted
blend of all tokens in the same sequence — producing **contextualized embeddings**.

## Intuition

Picture each word as a person at a meeting holding three cards. The **query** is
"what am I looking for?"; the **key** is "what do I have to offer?"; the **value**
is "the actual information I'd hand over." To update myself, I compare my query
against everyone's key (including my own), see who matches best, and then take a
**weighted average of their values** — paying most attention to the people whose
keys fit my query. The lecture's pizza analogy: query = what a token wants, key =
what a token advertises, value = what it actually delivers. Do this for every word
simultaneously and each word ends up "knowing about" the words that matter to it —
which is exactly what turns the static embedding of "green" into the right meaning
in "green shirt" vs. "green recruits."

The historical seed (encoder-decoder attention) is just as intuitive: when humans
translate, we don't read the source once and recite — we **keep glancing back** at
different parts of the source while producing each output word. Attention is that
"glancing back," made into math.

## Explanation

**Where it came from — encoder-decoder attention.** Early seq2seq models squeezed
the whole source sentence into one final hidden state (a bottleneck). Attention
fixed this: at each decoding step, score the decoder's current state against
*every* encoder hidden state, softmax the scores into weights, and form a **context
vector** = weighted sum of encoder states. The decoder thus reads a fresh,
focus-shifted summary of the source at every step. A useful side effect: the
weights can be visualized as a soft alignment between source and target words
(Bahdanau et al. 2015) — though such weights are diagnostics, **not** a complete
explanation of the model.

**Self-attention.** Self-attention turns that same machinery inward: there is no
separate encoder/decoder — every token attends to the tokens of *its own*
sequence. Motivation: word meaning is contextual ("the shirt is green" vs. "the
recruits are green"), but a static type embedding gives "green" one fixed vector.
Self-attention recomputes each token's vector as a weighted sum of its neighbors,
so the representation becomes occurrence-specific.

**The five steps (one head).** From the deck, for input vectors $x_1,\dots,x_n$:
1. **Project.** A head has just three weight matrices $W_q, W_k, W_v$. Each token
   gets $q_i = W_q x_i$, $k_i = W_k x_i$, $v_i = W_v x_i$.
2. **Score.** For the token of interest (say $x_1$), compute dot products of its
   query with every key: $s_j = q_1\cdot k_j$.
3. **Scale + softmax.** Divide each score by $\sqrt{d_k}$ (the deck uses
   $\sqrt{\text{len}(k)}$) and softmax so the weights $a_j$ are positive and sum to
   1. Scaling keeps the dot products from getting so large that softmax saturates.
4. **Weight the values.** The weights multiply the **value** vectors, not the
   original $x_i$: $z_1 = \sum_j a_j v_j$.
5. **Repeat** for every token, yielding new representations $z_1,\dots,z_n$ — the
   output of one **self-attention head**.

**Multi-head.** Words relate in many ways, so one head is limiting. **Multi-head
attention** runs $h$ heads in parallel, each with its own $W_q,W_k,W_v$, then
concatenates their outputs (and projects). One head might track syntactic
subject-verb links, another coreference — see
[[Transformer Architecture in Understanding LLMs]].

**Cost and trade-off.** Self-attention is **context-aware** and far more powerful
than static embeddings, and every $z_i$ can be computed **in parallel** (unlike an
RNN/LSTM's sequential recurrence). The price: it cannot be precomputed and it is
$O(n^2)$ in sequence length — the bottleneck later attacked by
[[State Space Models in Understanding LLMs]].

![Query, key, and value intuition](../../outputs/images/03-Transformers/query-key-value-p063.png)
*The pizza analogy for Q/K/V: a token's **query** is what it is looking for, a
**key** is what it advertises, a **value** is what it actually delivers (deck p63).*

![Self-attention softmax](../../outputs/images/03-Transformers/self-attention-softmax-p070.png)
*Scaled scores pass through softmax to give attention weights (.87/.12/.01/0),
which then weight the value vectors (deck p70).*

## Worked example

The deck's numeric example, sentence "The brown dog ran", computing $z_1$ (the new
representation of "The"):

- **Scores** (query $q_1$ dotted with each key): $s_1=q_1\!\cdot\!k_1=112$,
  $s_2=96$, $s_3=16$, $s_4=8$.
- **Scale + softmax** (here $\sqrt{d_k}=8$, so divide by 8 then softmax):
  $a = \mathrm{softmax}(14, 12, 2, 1) \approx (0.87,\,0.12,\,0.01,\,0)$.
- **Weighted sum of values:**
  $z_1 = 0.87\,v_1 + 0.12\,v_2 + 0.01\,v_3 + 0\,v_4$.

So "The" ends up represented mostly by its own value plus a little of "brown".
Recomputing for $x_2$ ("brown") gives different scores ($92,124,22,8$) and weights
$(0.08, 0.91, 0.01, 0)$ — "brown" attends mostly to itself. Each token gets a
context-specific blend. Note the weights **weight the values $v_i$, not the raw
inputs $x_i$** — a common point of confusion.

## Formal definition / equations

**Per-token (single head).** Projections and output:
$$ q_i = W_q x_i,\quad k_i = W_k x_i,\quad v_i = W_v x_i, \qquad z_i = \sum_{j} a_{ij}\, v_j, $$
$$ a_{ij} = \mathrm{softmax}_j\!\left(\frac{q_i\cdot k_j}{\sqrt{d_k}}\right) = \frac{\exp(q_i\cdot k_j/\sqrt{d_k})}{\sum_{j'}\exp(q_i\cdot k_{j'}/\sqrt{d_k})}. $$

**Matrix form (the canonical equation).** Stack queries/keys/values into matrices
$Q,K,V$:
$$ \mathrm{Attention}(Q,K,V) = \mathrm{softmax}\!\left(\frac{QK^{\top}}{\sqrt{d_k}}\right)V. $$
- $Q\in\mathbb R^{n\times d_k}$: queries (one row per token).
- $K\in\mathbb R^{n\times d_k}$: keys; $QK^\top\in\mathbb R^{n\times n}$ is the
  matrix of all query-key scores.
- $\sqrt{d_k}$: scaling by the square root of the key dimension, so large dot
  products don't push softmax into vanishing gradients.
- $V\in\mathbb R^{n\times d_v}$: values; the softmax'd weight matrix times $V$ is
  the weighted sum.

**Multi-head:** with heads $\text{head}_m=\mathrm{Attention}(QW_m^Q,KW_m^K,VW_m^V)$,
$$ \mathrm{MultiHead}(Q,K,V) = \mathrm{Concat}(\text{head}_1,\dots,\text{head}_h)\,W^O. $$

**Causal (masked) self-attention:** set $S_{ij}=-\infty$ for $j>i$ before softmax,
so a position attends only to itself and earlier positions — required for
autoregressive decoding (see
[[Autoregressive Language Models in Understanding LLMs]]).

## Animation

A rendered walkthrough of self-attention on the sentence *"the cat sat down"*
with query token **sat**: each token becomes a query/key/value; the query scans
every key via the scaled dot product (scores $0.5, 3.0, 2.2, 1.4$); softmax turns
those into attention weights ($0.05, 0.58, 0.26, 0.12$) so "sat" attends most to
its subject "cat"; the output is the weighted sum of values — a contextualized
embedding. Ends on $\mathrm{Attention}(Q,K,V)=\mathrm{softmax}(QK^{\top}/\sqrt{d_k})V$.

![[self-attention.mp4]]

For slides, a transparent version (alpha, drops onto any light deck with no box)
lives at `outputs/images/attention-self-attention/self-attention.mov`. Source
scene: `outputs/images/attention-self-attention/scripts/self_attention.py`.

## Role in this class or project

Self-attention is the **core computational primitive** of the whole course: it is
the engine inside [[Transformer Architecture in Understanding LLMs]], the source of
the contextualized [[Embeddings in Understanding LLMs]] that everything downstream
reads, the object that [[Mechanistic Interpretability in Understanding LLMs]]
dissects (QK/OV circuits, induction heads), and the $O(n^2)$ cost that motivates
the efficient architectures of [[State Space Models in Understanding LLMs]].

## Exam, assignment, or project relevance

- **State the Q/K/V roles** and the five computation steps.
- **Write** $\mathrm{softmax}(QK^\top/\sqrt{d_k})V$ and explain *why* the $\sqrt{d_k}$
  scaling is there.
- **Work the numeric example** (scores → scale → softmax → weighted sum of values).
- **Explain** why attention weights weight the *values* and why they are diagnostics,
  not faithful explanations.
- **Explain** multi-head attention and causal masking.

## Related global concepts

- Promotion candidate: **Attention Mechanism / Scaled Dot-Product Attention**.

## Related local pages

- [[Transformer Architecture in Understanding LLMs]]
- [[Embeddings in Understanding LLMs]]
- [[Autoregressive Language Models in Understanding LLMs]]
- [[Neural Sequence Models in Understanding LLMs]]
- [[Mechanistic Interpretability in Understanding LLMs]]
- [[State Space Models in Understanding LLMs]]

## Common confusions

- **Weights weight the values, not the inputs.** $z_i=\sum_j a_{ij}v_j$, not
  $\sum_j a_{ij}x_j$.
- **Attention weights ≠ explanation.** A high weight is suggestive but not a
  faithful account of the full computation (the value and downstream layers matter).
- **Self-attention ≠ RNN recurrence.** It mixes information across all positions
  *within one layer, in parallel*, with no sequential hidden state.
- **Attention ≠ human attention.** The name is a loose analogy, not a cognitive
  claim.

## Sources

- [[Session 03 - Transformers]]
- [[Basic Transformer Architecture Slides]]
- [[Transformer-Based Language Models]]
