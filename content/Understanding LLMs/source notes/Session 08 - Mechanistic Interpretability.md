---
type: source_note
status: processed
scope: local
class: Understanding LLMs
project:
source_type: lecture slides
raw_path: raw/08-Mechanistic-Interpretability.pdf
created: 2026-06-17
updated: 2026-06-17
---

# Session 08 - Mechanistic Interpretability

## Summary

Where Session 07 asked "*which* inputs/layers correlate with the output?", this lecture asks the harder question: "*how* does the network actually compute the answer, step by step, inside its weights?" That is **mechanistic interpretability (MI)** — reverse-engineering a trained Transformer into human-understandable algorithms, the way you might reverse-engineer a compiled binary back into source code. The previous methods (what-if, SHAP, probing) are framed as the starting point and their limits motivate going deeper: probing tells you a property is *present* but not how it is *used*, and a null probing result is hard to interpret.

The lecture walks up a ladder of increasingly mechanistic tools. **Early decoding / logit lens**: project a model's *intermediate* hidden states through the output (unembedding) matrix to read "what each layer already wants to say" — e.g. watching the answer "Warsaw" crystallise across layers for "the capital of Poland is". **Residual stream**: re-derive the Transformer (following Elhage et al.'s "Mathematical Framework") as a central communication bus that every attention head and MLP *reads from and writes to* additively; this view exposes QK (query-key) and OV (output-value) circuits and specialised **head types** like induction heads. **Activation patching**: a causal-intervention method — run the model on a clean and a corrupted input, then copy ("patch") activations from one run into the other to find which components are *causally* responsible for a behaviour. **Circuit analysis**: assemble these located components into a wiring diagram (the IOI circuit) and test the hypothesis rigorously with **causal scrubbing**. Finally, **superposition** (models pack more concepts than they have neurons, so neurons are *polysemantic*) motivates **sparse autoencoders (SAEs)** and **transcoders** that decompose activations into many sparse, monosemantic, interpretable features.

The throughline: MI tries to move from *correlation* to *mechanism* and ultimately to *causal*, testable claims about the algorithm a model implements — while honestly flagging that every tool here (SAEs, transcoders) is an approximation, not a silver bullet.

## Key points

- **Mechanistic interpretability = reverse-engineering the model's internal computation** into human-understandable parts, going beyond the post-hoc attribution of Session 07.
- The recap explicitly lists the limits of prior methods that MI tries to overcome: hard-to-interpret negatives, absence of signal, and low probe performance don't tell you *how* the model works.
- **Logit lens (early decoding):** because the residual stream keeps a constant shape across layers and the final unembedding $W_U$ maps it to vocabulary, you can apply $W_U$ to *intermediate* layers and decode their "current best guess." Early/middle layers often surface the subject or a generic token; the final answer appears only in later layers.
- The Transformer can be **rewritten to expose its linear structure**: token embedding writes to a residual stream; each attention head and each MLP *adds* its output back to the stream; the unembedding reads the final stream. Heads communicate through this stream via implicit **virtual weights**.
- The residual stream is **high-dimensional (100s–10,000s of dims)** but each head reads/writes only small **subspaces**; computational bandwidth far exceeds communication bandwidth ("bottleneck activations"), and some heads act as **memory managers**.
- Attention heads factor into a **QK circuit** (where to attend) and an **OV circuit** (what to copy/write). **Most Transformer operations are achieved via copying.**
- **Induction heads** are a canonical learned head type: if the current token was seen earlier, attend to the token that *followed* it last time and copy it (pattern completion `[A][B]…[A]→[B]`); otherwise dump attention on the first token.
- **Activation patching** is a *causal* method: take a clean run and a corrupted run, patch an activation from one into the other, and see whether the output flips. Components whose patch strongly changes the output are causally implicated (e.g. localising factual knowledge or gender bias).
- Choose an **expressive metric** for the patch effect: **logit difference** (correct − incorrect) is preferred; alternatives are raw correct-class logit, log-prob, raw prob, or binary accuracy/rank.
- **Patch direction matters:** per the slides, corrupted→clean patching tests whether activations are **necessary** ("noising"); clean→corrupted patching tests whether they are **sufficient** ("denoising").
- **Circuit analysis** assembles located heads into a mechanism. The **IOI** ("Indirect Object Identification") circuit (Wang et al. 2023) uses Previous-Token, Duplicate-Token, Induction, S-Inhibition, and (Negative/Backup) Name-Mover heads. **Causal scrubbing** rigorously tests a circuit hypothesis by recursively replacing components that should be invariant.
- **Superposition & polysemanticity:** a single neuron (the famous "Neuron 83") can fire on academic citations, English dialogue, HTTP requests, *and* Korean text. Models represent more concepts than they have neurons by encoding each as a linear combination across many neurons.
- **Sparse autoencoders (SAEs)** learn an **overcomplete** (e.g. 4×–256× wider), **L1-sparse** representation that pulls these tangled features apart into compact, monosemantic features. For GPT-3 scale this means millions of features per layer.
- **Transcoders** replace an MLP with a single-layer, overcomplete, L1-sparse ReLU MLP trained to *reproduce the layer's output* (not just reconstruct activations), so they are interpretable feature maps *and* drop-in MLP replacements — enabling **input-invariant circuit discovery**. **Cross-layer transcoders (CLTs)** read one layer and write to all following ones, supporting attribution graphs across layers.
- Honest caveats: SAEs struggle with dense MLP computation; transcoders are approximations and expensive (though pretrained ones increasingly ship with open-weight models).

## Important concepts

- [[Mechanistic Interpretability in Understanding LLMs]]
- [[Activation Patching in Understanding LLMs]]
- [[Sparse Autoencoders and Superposition in Understanding LLMs]]
- [[Probing Classifiers in Understanding LLMs]]
- [[Feature Attribution in Understanding LLMs]]
- [[Transformer Architecture in Understanding LLMs]]
- [[Attention and Self-Attention in Understanding LLMs]]

## Methods, models, or theories

- **Logit lens / early decoding** — decode intermediate residual states with the unembedding to inspect layer-wise predictions.
- **Residual-stream view of the Transformer** (Elhage et al. 2021) — additive read/write bus; QK and OV circuits; virtual weights; subspaces.
- **Induction heads** — pattern-completion attention heads.
- **Activation patching** (a.k.a. causal tracing / causal mediation) — clean/corrupted runs, patch location, metric choice, noising vs. denoising. See [[Activation Patching in Understanding LLMs]].
- **Circuit analysis** — IOI circuit (Wang et al. 2023); **causal scrubbing** (Chan et al. 2022).
- **Sparse autoencoders, transcoders, cross-layer transcoders** — dictionary learning of interpretable features. See [[Sparse Autoencoders and Superposition in Understanding LLMs]].

## Equations or formal definitions

**The residual-stream rewrite of the Transformer** (Elhage et al. 2021), the formal backbone of the whole lecture:

$$x_0 = W_E\, t \quad\text{(token embedding writes to the stream)}$$
$$x_{i+1} = x_i + \sum_{h \in H_i} h(x_i) \quad\text{(each attention head adds its output back)}$$
$$x_{i+2} = x_{i+1} + m(x_{i+1}) \quad\text{(the MLP adds its output back)}$$
$$T(t) = W_U\, x_{-1} \quad\text{(unembedding reads the final stream to logits)}$$

- $t$ — the input token (one-hot); $W_E$ — embedding matrix; $x_0$ — its vector in the residual stream.
- $x_i$ — the residual stream state at depth $i$; the key idea is that every block *adds* to $x_i$ rather than replacing it, so the stream is a running sum that all components read from and write to.
- $H_i$ — the set of attention heads at layer $i$; $h(x_i)$ — one head's contribution; $m(\cdot)$ — the MLP.
- $x_{-1}$ — the final residual state; $W_U$ — the unembedding matrix; $T(t)$ — output logits.
- *In words:* the Transformer is a sequence of additive edits to a shared vector bus. This linearity is what lets MI talk about "virtual weights" $W_O^{(2)}W_O^{(1)}$ connecting non-adjacent layers, and what makes the **logit lens** valid: applying $W_U$ to an *intermediate* $x_i$ asks "what would the model say if it stopped here?"

**Logit lens.** Decode any intermediate state: $\text{logits}_i = W_U\, x_i$, then read the top token. Because the stream's geometry is constant across depth, the same $W_U$ is meaningful at every layer.

**Activation-patching metric — logit difference.** The recommended effect metric is

$$\Delta = \text{logit}(\text{correct}) - \text{logit}(\text{incorrect}),$$

measured before vs. after patching a component, because it isolates the behaviour of interest better than raw probability (which is squashed by the softmax). Symbols and the full method are unpacked in [[Activation Patching in Understanding LLMs]].

## Local relevance

This is the deep companion to [[Session 07 - Probing and Attribution]] and the payoff for the formal Transformer machinery from [[Session 03 - Transformers]] / [[Transformer Architecture in Understanding LLMs]] and [[Attention and Self-Attention in Understanding LLMs]] (the QK/OV decomposition is exactly the $W_Q,W_K,W_V,W_O$ matrices seen there). It directly upgrades the previously thin [[Mechanistic Interpretability in Understanding LLMs]] page into a full account, and it sets up Session 09's pivot to *behavioural* assessment by contrasting internal-mechanism analysis with black-box behavioural testing.

## Exam or project relevance

High-yield and conceptually central. Likely targets: define MI vs. attribution/probing; explain the **logit lens** and why the residual-stream constancy makes it work; write the **residual-stream equations** and explain "read/write/add"; describe **QK vs. OV** and **induction heads**; explain **activation patching** end-to-end including the **necessity/sufficiency (noising/denoising)** distinction and why **logit difference** is the metric; sketch the **IOI circuit** idea and **causal scrubbing**; and explain **superposition → SAEs → transcoders/CLTs** (why overcompleteness + L1 sparsity yields monosemantic features, and why transcoders enable input-invariant circuits). For projects, note that pretrained SAEs/transcoders increasingly ship with open-weight models.

## Links to global concepts

No `Global Wiki/` pages created or modified. Promotion candidates if they recur across classes: a general **Mechanistic Interpretability** page and a **Sparse Autoencoder / dictionary learning** page. Tracked as candidates, not yet promoted.

## Open questions

- The slides simplify to "toy Transformers" (decoder-only, no MLP/biases/LayerNorm) for the residual-stream math; how much of the messy full-model detail will the exam expect?
- Causal scrubbing was presented at a high level; the recursive testing procedure's details are not fully on the slides.
- The exact training objective/loss for SAEs and transcoders (reconstruction + L1 weighting) is stated qualitatively, not with the full loss function.
