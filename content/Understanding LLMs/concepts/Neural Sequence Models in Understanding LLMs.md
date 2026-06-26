---
type: concept
status: active
scope: local
classes:
  - Understanding LLMs
projects:
domains:
  - neural networks
  - natural language processing
sources:
  - Session 02 - PyTorch, Optimization, ANNs, LMs, RNNs, LSTMs
  - Session 03 - Transformers
created: 2026-05-14
updated: 2026-06-25
---

# Neural Sequence Models in Understanding LLMs

## Short definition

A neural sequence model uses a neural network to model an **ordered** sequence of
tokens — usually by predicting the next token from the ones before it. The course
covers three generations: **RNNs**, **LSTMs**, and **transformers**.

## Intuition

Reading a sentence word by word, you keep a running "gist" in your head and update
it at each word. An **RNN** is exactly that: a single mental notepad (the hidden
state) rewritten at every step. The trouble is the notepad has to do two jobs at
once — *remember* everything relevant from far back *and* decide what to output
now — and rewriting it every word tends to smear out old information. An **LSTM**
adds a second, protected notepad (the **memory cell**) with **gates** that decide
what to erase, what to write, and what to reveal — so important facts from early in
the sentence can survive untouched until needed. A **transformer** throws out the
single notepad entirely: instead of passing one summary forward, every word gets
to *look directly* at every other word (attention), in parallel.

## Explanation

**RNNs.** A recurrent network threads a hidden state $h_t$ through time, reusing
the *same* weight matrices at every step. At each token it combines the previous
state $h_{t-1}$ with the current embedding $x_t$ and emits a next-token
distribution. This makes it a natural language model, but the hidden state's
**dual role** (memory + current decision) is a conceptual bottleneck, and training
is technically hard.

**Why training is hard.** RNNs are trained by **backpropagation through time
(BPTT)**: unroll the recurrence across the whole sequence and apply the chain rule
backward. The gradient reaching an early step is a **product of many Jacobians**;
that product tends to shrink to zero (**vanishing gradients** — the model can't
learn long-range dependencies, far context is "forgotten") or blow up
(**exploding gradients** — unstable training, recency bias). This is the central
limitation that motivates everything after.

**LSTMs.** The LSTM (Hochreiter & Schmidhuber 1997) keeps the hidden state $h_t$
but adds a dedicated **memory cell** $c_t$ updated through three **gates**:
- **forget gate** $f_t$ — how much of the old cell to keep;
- **input gate** $i_t$ — how much new candidate information to write;
- **output gate** $o_t$ — how much of the cell to expose as the hidden state.

Because the cell update is **near-additive** (you add a gated candidate rather than
fully overwriting), gradients can flow back through many steps without being
repeatedly multiplied down — directly mitigating the vanishing-gradient problem.

**Transformers.** Transformers (Session 03) drop recurrence altogether. Each layer
computes **contextualized** representations using **self-attention**: every token
attends to every other token in parallel, so there is no single hidden state to
bottleneck information and no long sequential gradient path. This trades the RNN's
$O(1)$-memory streaming for $O(n^2)$ attention cost, but it removes the
vanishing-gradient and parallelization problems at a stroke. See
[[Attention and Self-Attention in Understanding LLMs]].

**Other RNN variants in the deck.** *Stacked* RNNs add depth (higher layers hold
more abstract "meaning"). *Bidirectional* RNNs run a left-to-right and a
right-to-left pass and concatenate the hidden states for richer contextual
embeddings — better for representation tasks, but they need the full sequence up
front and so cannot do left-to-right generation.

## Worked example

A character-level RNN generating a surname (the deck's running demo), vocabulary =
letters. Feed "A": the embedding $x_1 = E w_1$ enters, $h_1 = \tanh(U h_0 + W x_1)$
with $h_0=\mathbf 0$, and $y_1 = \mathrm{softmax}(V h_1)$ gives a distribution over
the next letter — say it favors "n". Feed "n": now
$h_2 = \tanh(U h_1 + W x_2)$ folds the new letter into the *same* state that
already encodes "A", and $y_2$ predicts the next letter conditioned on "An…". The
single state $h_t$ is the only memory of everything typed so far — which is why, by
the time we reach the 8th letter, the influence of "A" may have faded
(vanishing). An LSTM would instead carry "started with A, looks German" in its
protected cell $c_t$ until the end.

## Formal definition / equations

**RNN forward pass** (one-hot token $w_t$, embedding matrix $E$, input-to-hidden
$W$, hidden-to-hidden $U$, hidden-to-vocab $V$, activation $f$):
$$ x_t = E w_t, \qquad h_t = f(U h_{t-1} + W x_t), \qquad y_t = \mathrm{softmax}(V h_t). $$

**Vanishing/exploding gradient.** Across $T$ unrolled steps,
$$ \frac{\partial L_T}{\partial h_1} = \frac{\partial L_T}{\partial h_T}\prod_{t=2}^{T}\frac{\partial h_t}{\partial h_{t-1}}. $$
A product of $T-1$ Jacobians: norms <1 ⇒ decay to 0 (vanishing), norms >1 ⇒
growth (exploding).

**LSTM gates** (sigmoid $\sigma$, elementwise product $\odot$, input $x_t$,
previous hidden $h_{t-1}$):
$$ f_t = \sigma(W_f[h_{t-1},x_t]+b_f), \quad i_t = \sigma(W_i[h_{t-1},x_t]+b_i), \quad o_t = \sigma(W_o[h_{t-1},x_t]+b_o), $$
$$ \tilde c_t = \tanh(W_c[h_{t-1},x_t]+b_c), \quad c_t = f_t\odot c_{t-1} + i_t\odot\tilde c_t, \quad h_t = o_t\odot\tanh(c_t). $$
Each gate is a 0–1 valve (sigmoid). $\tilde c_t$ is the candidate update; the cell
$c_t$ *keeps* a fraction $f_t$ of its old contents and *adds* a fraction $i_t$ of
the candidate — the additive path that protects long-range gradients. $h_t$ is a
gated view of the cell. *(Reconstructed from Jurafsky & Martin; the deck shows the
gated cell as a diagram, p76.)*

## Role in this class or project

This page is the spine connecting the pre-transformer and transformer halves of
the course. It explains *why* the field moved from RNN → LSTM → transformer, and the
vanishing-gradient story it tells is the exact motivation revisited from the other
direction in [[State Space Models in Understanding LLMs]] (a modern linear
recurrence that reclaims the efficiency RNNs had while fixing their weaknesses).

## Exam, assignment, or project relevance

- **Write the RNN forward pass** and explain the hidden state's dual role.
- **Derive** vanishing/exploding gradients from the product-of-Jacobians and say
  which causes "forgetting" vs. "recency bias."
- **Name the three LSTM gates** and state how the additive cell update helps
  gradient flow.
- **Contrast** recurrence (sequential, $O(1)$ memory, gradient bottleneck) with
  attention (parallel, $O(n^2)$, direct access).

## Related global concepts

- Promotion candidate: **Recurrent Neural Networks / Sequence Models**.

## Related local pages

- [[Embeddings in Understanding LLMs]]
- [[Attention and Self-Attention in Understanding LLMs]]
- [[Transformer Architecture in Understanding LLMs]]
- [[Optimization for Language Models in Understanding LLMs]]
- [[State Space Models in Understanding LLMs]]

## Common confusions

- **LSTMs do not "solve" memory.** They *mitigate* vanishing gradients and extend
  usable range, but very long dependencies still degrade — which is why
  transformers (and later SSMs) were needed.
- **Autoregressive ≠ recurrent.** A model can predict left-to-right without a
  recurrence: a transformer is autoregressive via *causal masking*, not a hidden
  state.
- **Bidirectional ≠ better for everything.** Bidirectional models read the whole
  sequence, so they cannot generate left-to-right; they're for representation, not
  generation.

## Sources

- [[Session 02 - PyTorch, Optimization, ANNs, LMs, RNNs, LSTMs]]
- [[Session 03 - Transformers]]
