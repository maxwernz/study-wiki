---
type: source_note
status: processed
scope: local
class: Understanding LLMs
project:
source_type: lecture slides
raw_path: raw/07-Probing-Attribution.pdf
created: 2026-06-17
updated: 2026-06-17
---

# Session 07 - Probing and Attribution

## Summary

This lecture is about **interpretability**: once you have a trained language (or vision) model, how do you figure out *why* it makes the predictions it does, and how do you debug it when it fails? The plain-language framing is "the model gave an answer — was it right for the right reason, or right for the wrong reason?" A famous example is a visual-question-answering model that answers "how symmetric are the white bricks?" with "very" — but gives the same "very" to "how *fast* are the bricks *speaking*?", revealing it never understood the question and is exploiting answer priors.

The session organises interpretability along two axes that recur throughout: **global vs. local** (do you want to understand the whole model's behaviour, or one specific prediction?) and **who the explanation is for** (a developer debugging, a strategic buyer, an end user, a journalist) — there is no single "best" explanation, only one *suitable* for an audience and purpose. Against that backdrop it surveys a toolbox of concrete techniques, moving from cheap-and-shallow to expensive-and-deep: practical **model debugging**, **what-if exploration**, **Shapley values / SHAP** (game-theoretic feature attribution), **attention visualization** (and the debate over whether attention is even an explanation), **gradient tracing** (integrated gradients, Grad-CAM), and **probing classifiers** (training small classifiers on frozen representations to ask "is this linguistic property encoded in here?"), ending with **knowledge editing** of facts stored in representations.

The unifying message: these are mostly **post-hoc, behavioural** lenses on the model. They tell you *what* correlates with the output (which input features, which layers, which heads) but generally **not the internal mechanism** — that gap is what the next lecture, mechanistic interpretability, sets out to close.

## Key points

- Interpretability serves two questions that should not be conflated: **global** explanations describe the whole model's decision surface; **local** explanations justify one individual prediction. Most of the techniques here are *local* (Shapley, gradient tracing, attention maps) and can only be *aggregated* into something global.
- An explanation is only good *relative to an audience and a goal* — "tailored explanations": a developer debugging, an expert buyer, a layperson user, and the press all need different things. Local vs. global × expert vs. layperson is the design grid.
- **What-if exploration** ("replace *he* with *she*", "add a period") is the most intuitive interpretability tool and underlies many others: most attribution methods are just summaries of what-if behaviour.
- **Debugging order matters**: don't debug everything at once. Work top-down through likely causes — training-time problems (too little capacity, bad optimization, training bugs) → test-time problems (train/test code disconnects, search failures) → overfitting → **loss/metric mismatch**.
- A classic, counterintuitive failure: you optimise **maximum likelihood**, the likelihood keeps improving, yet **accuracy gets worse**. Fixes: train directly on the metric (e.g. RL) or, more cheaply, **early-stop on the evaluation metric** rather than the loss.
- **Error analysis** is half the job: do *qualitative* analysis (read 100–200 errors, group them into a typology) and *quantitative* analysis (is the specific phenomenon you targeted — low-frequency words, long-distance syntax, search errors — actually improving?).
- **Shapley values** give a theoretically principled, model-agnostic, *directional* attribution of a prediction to input features, by averaging each feature's marginal contribution over all orderings. The cost is **factorial** in the number of features; **SHAP** is the NLP-friendly approximation (tokens = players).
- **Attention weights are tempting but contested as explanations.** Several 2019 papers (Jain & Wallace; Serrano & Smith) argue *no* — alternative attention weights give near-identical predictions and attention often fails to track the tokens that actually drive the decision; others (Wiegreffe & Pinter; Zhong et al.) argue *maybe*, under tests.
- **Gradient tracing** attributes a prediction to inputs via gradients. Naïve feature×gradient is noisy and suffers **gradient saturation**; **Integrated Gradients** fixes this by integrating gradients along a straight path from an informationless **baseline** to the input. **Grad-CAM** localises which regions a CNN used.
- **Probing classifiers** test whether a linguistic property is *encoded* in a model's representations: freeze the encoder, train a small classifier on its vectors to predict the property. High accuracy ⇒ the property is decodable from the representation.
- A probe can succeed for the wrong reason — a powerful probe can *learn the task itself*. **Control tasks** (Hewitt et al. 2019) and **selectivity** (probe accuracy minus control-task accuracy) separate "the representation encodes this" from "the probe is just strong."
- Empirically (Peters et al. 2018), **early layers capture local syntax, later layers capture content/semantics** — a robust, exam-worthy finding.
- **Knowledge editing** (e.g. REMEDI) edits *facts* by modifying an entity's representation with an edit vector, changing what the LM generates without retraining.

## Important concepts

- [[Probing Classifiers in Understanding LLMs]]
- [[Feature Attribution in Understanding LLMs]]
- [[Mechanistic Interpretability in Understanding LLMs]]
- [[Attention and Self-Attention in Understanding LLMs]]
- [[Benchmarking LLMs in Understanding LLMs]]

## Methods, models, or theories

This is a survey of interpretability/attribution methods. For each: what it does, how it works, when to use it.

**Model debugging (engineering practice).** Identify *where* a model fails before *why*. Check the training loss first (does it go to ~0 on the full data in 20–30 epochs? on a tiny dataset?). If not, suspect capacity or optimization (optimizer = an Adam variant, learning-rate/decay, initialization range, batch size). Then suspect **train/test disconnects** — loss and prediction are usually different code paths (especially for encoder-decoders), and *duplicated code is a source of bugs*; loss is typically minibatched while generation is not. Use when your model trains but underperforms or makes incomprehensible errors.

**What-if exploration.** Probe the model by perturbing inputs and watching outputs. Intuitive ("what you see is what you get") and highly expressive. Used for model understanding/debugging, algorithmic recourse, and prompt design.

**Shapley values / SHAP.** Game-theoretic feature attribution. Treat input features as "players" cooperating to produce the prediction (the "gain"); fairly split credit by averaging each player's marginal contribution across all join orders. **SHAP** applies this to NLP with tokens as players and signed (positive/negative) contributions. Model-agnostic and directional; factorial cost unless approximated; gives **no mechanistic** account. → [[Feature Attribution in Understanding LLMs]]

**Attention visualization.** Read off the attention weights (encoder-decoder or self-attention heads) as a heatmap of "what the model looked at." Cheap and ubiquitous, but its status as an *explanation* is disputed (see Equations / the "attention is [not] explanation" debate). Some heads are interpretable (relation-specific); head importance can be scored by gradient-based measures (Michel et al. 2019).

**Gradient tracing.** Attribute predictions to input features via gradients. Variants: **feature×gradient** ($x_i \cdot \partial y/\partial x_i$), **Integrated Gradients** (path integral from a baseline), **Grad-CAM** (gradient-weighted activation maps for CNNs). Model-specific, scales to complex models; weaknesses are input dependence and **gradient saturation**. Tooling: `captum.ai`. → [[Feature Attribution in Understanding LLMs]]

**Probing classifiers.** Freeze a pretrained encoder, train a small supervised classifier on its representations to predict a linguistic property (POS, constituency, coreference). Tests *encoding*, not *use*. Guard against an over-powerful probe with **control tasks** and **selectivity**. → [[Probing Classifiers in Understanding LLMs]]

**Knowledge editing (REMEDI).** Edit stored facts by computing an edit vector $z = h_{entity} + W h_{attr} + b$ from a "representation editor" and substituting it into the entity's encoding, steering generation to a new target without retraining.

## Equations or formal definitions

**Shapley value.** For player (feature) $i$ and a set-function $v(S)$ giving the gain of any coalition $S \subseteq \{1,\dots,M\}$:

$$\phi_i(v) = \mathbb{E}_{O \sim \pi(M)}\big[\, v(\mathrm{pre}_i(O)\cup\{i\}) - v(\mathrm{pre}_i(O)) \,\big]$$

- $\pi(M)$ — the uniform distribution over all $M!$ orderings (permutations) of the players.
- $O$ — one such ordering; $\mathrm{pre}_i(O)$ — the set of players that come *before* $i$ in ordering $O$.
- $v(\mathrm{pre}_i(O)\cup\{i\}) - v(\mathrm{pre}_i(O))$ — player $i$'s **marginal contribution**: how much the gain increases when $i$ joins the coalition already present.
- In words: *line the features up in a random order, ask how much $i$ adds when it steps in, and average that over every possible order.* The $M!$ orderings are why the exact computation is factorial.

**Integrated Gradients.** Attribution of prediction $F$ to the input relative to a baseline:

$$\mathrm{IG}(\text{input},\text{base}) = (\text{input}-\text{base}) \cdot \int_{0}^{1} \nabla F\big(\alpha\cdot\text{input} + (1-\alpha)\cdot\text{base}\big)\, d\alpha$$

- $\text{base}$ — an **informationless** reference input (black image; empty text / zero embedding).
- $\alpha \in [0,1]$ — interpolation parameter sweeping the straight-line path from baseline to input.
- $\nabla F(\cdot)$ — the model's gradient evaluated at each interpolated point along the path.
- In words: *the noisy gradient at the single input point misses contributions where the function has already saturated; integrating the gradient all along the path from a blank baseline recovers them.* IG explains the difference $F(\text{input}) - F(\text{base})$ in terms of input features. Saturation (flat gradients near the input) is exactly the failure it repairs.

**Selectivity (probing).** $\text{selectivity} = (\text{probe accuracy on the real task}) - (\text{probe accuracy on the control task})$. High accuracy with high selectivity ⇒ the *representation* carries the property; high accuracy with low selectivity ⇒ the *probe itself* is doing the work.

## Local relevance

This session sits between Session 04 (which first introduced interpretability and foundation models) and Session 08 (mechanistic interpretability). It supplies the vocabulary — local/global, attribution, probing, saturation, selectivity — that Session 08 then deepens with circuits and causal interventions. The attention material connects directly to [[Attention and Self-Attention in Understanding LLMs]], and the "attention is not explanation" debate is a useful corrective to over-reading the attention animations from earlier sessions.

## Exam or project relevance

Likely exam targets: the **global vs. local** distinction and the audience-tailoring grid; why **loss can improve while the metric worsens** and the early-stopping fix; the **Shapley intuition + Alice/Bob computation**; **why naïve gradients fail (saturation) and how Integrated Gradients fixes it** (define the baseline); the **probing setup** (frozen encoder, trained classifier) and especially **control tasks + selectivity** (a favourite "gotcha"); and the **early-layers-syntax / later-layers-content** finding. For projects, `captum.ai` (gradient methods) and SHAP are the practical libraries.

## Links to global concepts

No `Global Wiki/` pages were created or modified. Candidate for promotion once it recurs across classes: a general **Feature Attribution / Shapley value** page (Shapley values also appear in cooperative game theory and ML explainability broadly). Tracked as a promotion candidate, not yet promoted.

## Open questions

- How much of the probing/control-task formalism will the exam expect quantitatively vs. conceptually?
- Will the course require hands-on use of `captum` or SHAP in the tutorial/assignment, or only conceptual understanding?
- REMEDI knowledge editing was shown at a high level only; the exact training of the representation editor is not on the slides.
