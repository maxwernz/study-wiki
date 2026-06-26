---
type: source_note
status: processed
scope: local
class: Understanding LLMs
project:
source_type: lecture slides
raw_path: raw/09-behaveAssess-CogSciLing.pdf
created: 2026-06-17
updated: 2026-06-17
---

# Session 09 - Behavioral Assessment and Cognitive Language Sciences

## Summary

This capstone lecture has two halves. It opens with two more **architectural flavours** of LMs — **Mixture-of-Experts (MoE)** models (sparse layers of expert sub-networks plus a router that sends each token to a few experts, buying capacity without proportional compute) and **Large Reasoning Models** (LLMs trained, often via RL, to "think step by step", e.g. DeepSeek-R1, sometimes hiding their reasoning tokens). The bulk of the session, however, is methodological: **how do we assess what a language model can actually do**, and how does that relate to what *humans* do?

The conceptual spine is the **"common-sense axiom" of behavioral assessment**: if you want to know how a system will perform in some application context, you must test it under *the same circumstances* in which it will be used. The lecture then shows how standard practice often *violates* this axiom and surveys assessment methods along a ladder of rigour: **tale-telling by example** (single anecdotes — fine for refutation or motivation, weak for positive claims), **benchmarks** (standardised task batteries — scalable but individual tests can be low-quality and a benchmark named "X" need not actually test ability "X"), and quantitative metrics: **accuracy** (and the subtle argMax-vs-softMax distinction that breaks the common-sense axiom), **calibration** (Brier score, expected calibration error), and **bias corrections** (length, prompt-order/contextual calibration, surface-form competition).

The second half pivots to **machine psychology** and **computational psycholinguistics**: treating LMs as a new "natural kind" to be studied with the experimental methods of behavioral psychology (cognitive reflection tests, semantic illusions, deep/shallow processing via the logit lens), and comparing LM behaviour to **human language processing** — grammaticality judgements (and why **grammaticality ≠ string probability**, and why *how* you ask the model matters: meta-prompting fails where surprisal comparison succeeds), and **surprisal theory** linking a word's processing difficulty to its negative log-probability, validated against reading times, eye-tracking, and the N400 ERP — including the striking **inverse-scaling** result that bigger, "better" LMs can predict human reading times *worse*.

## Key points

- **Mixture-of-Experts (MoE):** sparse layers contain $N$ expert networks (often FFNs); a **router** sends each token to one/few experts, so only a fraction of parameters activate per token — more capacity, roughly constant compute. → [[Mixture-of-Experts in Understanding LLMs]]
- **Large Reasoning Models:** LLMs prone to "think step by step", extending zero-shot CoT ("Let's think step by step"); DeepSeek-R1 is trained (RL + SFT/distillation) for *accurate* answers on math/engineering, **not** for logically consistent reasoning, and hides reasoning tokens.
- **Common-sense axiom:** to predict performance in context $C$, test the system under the exact circumstances of $C$. Much standard benchmarking violates it.
- **Three lenses on "what LMs know/can do":** probing (encoding), intervention (mechanism, cf. Session 08), and **behavioral tests** (I/O behaviour) — this lecture is about the third, plus comparison to humans.
- **Tale-telling by example:** good for motivation or for *refuting* universal claims (one counterexample suffices), but positive claims need systematic testing (many items, models, methods; ideally antagonistic/severe testing).
- **Benchmarks:** standardised tasks with fixed evaluation; enable scaling comparisons and a shared agenda, but individual items can be poor and a "test for X" may not isolate X. Examples: BIG-Bench causal-judgement and empirical-judgement tasks.
- **Accuracy, argMax vs softMax:** scoring an option by $s(y)=\log P(y\mid x)$ and choosing by **arg-max** gives the usual accuracy; choosing **stochastically** (softmax, as a human sampling an answer would) can give very different numbers — the worked example yields 80% argMax vs ~40% softMax accuracy. ArgMax accuracy **violates the common-sense axiom** because the model is never actually sampled that way in use.
- **Calibration:** predicted probabilities should match empirical correctness. Measured by the **Brier score** (mean squared error vs one-hot truth) and **expected calibration error (ECE)** (gap between confidence and accuracy), visualised with **reliability diagrams**. → [[Behavioral Assessment and Calibration in Understanding LLMs]]
- **Bias corrections:** raw scores are biased by **answer length** (fix: average per-token log-prob), by **prompt properties** in k-shot learning (majority-label, recency, common-token biases; fix: contextual calibration against a null prompt — Zhao et al. 2021), and by **surface-form competition** among near-synonyms (fix: domain-conditional PMI — Holtzman et al. 2021).
- **Machine psychology:** study LMs as a new natural kind using behavioral-psychology experiments (Binz & Schulz 2023 on GPT-3; semantic illusions like "How many animals did *Moses* take on the Ark?"; cognitive reflection test; Hu & Franke 2024 using the logit lens to show early layers prefer the intuitive/shallow answer).
- **Targeted linguistic assessment:** curated test suites from theoretical linguistics/psycholinguistics (Marvin & Linzen 2018; BLiMP) test whether an LM matches human **grammaticality judgements**; an LM "predicts the right judgement" iff it assigns higher probability to the grammatical member of a minimal pair. → [[Targeted Linguistic Assessment in Understanding LLMs]]
- **Grammaticality ≠ string probability** (Chomsky 1957; Wilcox et al. 2023): a meaningful ungrammatical string can be *more* probable than a grammatical one; and **manner of assessment matters** — LMs *fail* grammaticality via meta-prompting ("Is this grammatical?") but *succeed* via **surprisal comparison** of minimal pairs.
- **Surprisal theory:** processing effort for a word ∝ its surprisal $-\log P(w\mid \text{context})$; compatible with prediction-error and integration mechanisms; validated by cloze, eye-tracking, self-paced reading, EEG/N400, maze tasks. **Inverse scaling:** larger/lower-perplexity LMs can fit human reading times *worse* (Oh & Schuler 2023). → [[Surprisal Theory in Understanding LLMs]]
- **Best practice for machine psychology:** control measurement variability (prompt sensitivity, aggregation), know LM biases (token frequency, position), state a clear hypothesis, do **severe (not confirmatory) testing**, preregister, run statistics, avoid overselling, and beware **training-data contamination** (use new material).

## Important concepts

- [[Mixture-of-Experts in Understanding LLMs]]
- [[Behavioral Assessment and Calibration in Understanding LLMs]]
- [[Targeted Linguistic Assessment in Understanding LLMs]]
- [[Surprisal Theory in Understanding LLMs]]
- [[Benchmarking LLMs in Understanding LLMs]]
- [[Mechanistic Interpretability in Understanding LLMs]]
- [[Probing Classifiers in Understanding LLMs]]
- [[In-Context Learning in Understanding LLMs]]

## Methods, models, or theories

- **Mixture-of-Experts** architecture (sparse expert layers + router).
- **Large Reasoning Models** / RL-trained step-by-step reasoning (DeepSeek-R1).
- **Behavioral assessment hierarchy:** tale-telling → benchmarks → quantitative metrics.
- **Accuracy** (argMax vs softMax / stochastic choice).
- **Calibration metrics:** Brier score, expected calibration error, reliability diagrams.
- **Bias corrections:** length normalisation, contextual calibration (null-prompt affine transform), domain-conditional PMI (surface-form competition).
- **Machine psychology:** experimental-psychology methods applied to LMs.
- **Targeted syntactic evaluation:** minimal-pair test suites (Marvin & Linzen, BLiMP); grammaticality-as-probability-comparison.
- **Surprisal theory** of human sentence processing.

## Equations or formal definitions

**Option scoring and accuracy.** For item $i$ with input $x_i$, options $y_{i1},\dots,y_{ik}$, and true option $t_i$:

$$s(y_{ij}) = \log P(y_{ij}\mid x_i),\qquad c_i = \arg\max_j s(y_{ij}),\qquad \text{accuracy} = \mathbb{E}_{i\sim I}\,\delta_{c_i = t_i}$$

- $s(\cdot)$ — the option's log-probability under the model; $c_i$ — the chosen option; $\delta$ — indicator (1 if the choice equals the truth). **Stochastic (softmax) choice** replaces the arg-max: $P(c_i=j)\propto \exp(\alpha\, s(y_{ij}))$, and accuracy becomes $\mathbb{E}_{i}\mathbb{E}_{c_i\sim P}\,\delta_{c_i=t_i}$ — a function of the temperature $\alpha$. These two can disagree sharply (80% vs ~40% in the slides' example).

**Brier score.** For $N$ items, $K$ categories, predicted probability $p_{ij}$ and one-hot truth $o_{ij}$:

$$\text{BS} = \frac{1}{N}\sum_{i=1}^{N}\sum_{j=1}^{K}(p_{ij}-o_{ij})^2$$

- Mean squared error between predicted probabilities and the one-hot true label; **lower is better**. It rewards being both accurate *and* well-calibrated.

**Expected calibration error.**

$$\text{ECE} = \mathbb{E}_{i\in I}\big[\,p_i - \mathbb{E}_{i'\in I}(t_{i'}=c_{i'}\mid p_{i'}=p_i)\,\big]$$

- $p_i$ — the model's confidence in its choice for item $i$; the inner expectation is the **actual fraction correct** among all items with that confidence. ECE is the average gap between stated confidence and realised accuracy; reliability diagrams plot accuracy vs confidence per bin.

**Length-corrected score.** Replace total log-prob with the **average per-token** log-prob:

$$s(y_{ij}) = \frac{1}{|y_{ij}|}\sum_{l=0}^{|y_{ij}|}\log P(y_{ij}\mid x_i)$$

- Divides out the systematic bias against longer options; often the implicit default (Brown et al. 2020).

**Grammaticality prediction.** For a minimal pair (grammatical $w_{1:n}$, ungrammatical $v_{1:m}$), the LM predicts the right judgement iff $P_M(w_{1:n}) > P_M(v_{1:m})$.

**Surprisal theory.**

$$\text{Effort}(w_i, w_{1:i-1}, C) \;\propto\; \text{Surprisal}(w_i\mid w_{1:i-1}, C) = -\log P(w_i\mid w_{1:i-1}, C)$$

- Processing effort for word $w_i$ is proportional to its negative log-probability given prior context $w_{1:i-1}$ and situation $C$; high-surprisal (unexpected) words are read more slowly and elicit larger N400s. Fully unpacked in [[Surprisal Theory in Understanding LLMs]].

## Local relevance

This session ties the course together. It reuses the **logit lens** from [[Session 08 - Mechanistic Interpretability]] (machine-psychology deep/shallow study; early-decoding of processing measures), contrasts behavioral assessment with the probing/intervention lenses ([[Probing Classifiers in Understanding LLMs]]), extends [[Benchmarking LLMs in Understanding LLMs]] with a critical, methodology-aware view, and connects in-context-learning prompt sensitivity ([[In-Context Learning in Understanding LLMs]]) to the contextual-calibration bias correction. MoE and reasoning models extend the architecture line from [[Transformer Architecture in Understanding LLMs]] and the CoT material from [[Prompt Engineering in Understanding LLMs]].

## Exam or project relevance

Very high-yield and broad. Likely targets: state and apply the **common-sense axiom**; rank the assessment methods (tale-telling vs benchmark vs metric) and their proper use; the **argMax-vs-softMax** accuracy example and *why it violates the axiom*; **Brier score and ECE** definitions + a reliability-diagram reading; the three **bias corrections** (length, contextual/prompt, surface-form) with their fixes; **grammaticality ≠ probability** and the **meta-prompt-fails / surprisal-succeeds** contrast; **surprisal theory** ($-\log P$) with its human-processing evidence and the **inverse-scaling** twist; and the **machine-psychology best practices** (severe testing, preregistration, contamination). MoE (router + sparse experts) and DeepSeek-R1 (RL for accuracy, not reasoning consistency) are likely short-answer items.

## Links to global concepts

No `Global Wiki/` pages created or modified. Promotion candidates: **Mixture-of-Experts**, **Model Calibration (Brier / ECE)**, and **Surprisal Theory** are all reusable beyond this class (calibration is general ML; surprisal is core psycholinguistics). Tracked as candidates, not yet promoted.

## Open questions

- The MoE and reasoning-model sections are brief (recap-level); load-balancing losses and the full DeepSeek-R1 training pipeline are not detailed on the slides.
- The contextual-calibration affine transform (Zhao et al. 2021) is stated with a max-entropy criterion but the exact fitting is not fully derived.
- Several psycholinguistic results are model-dependent (Hu & Franke: effect only for some 7B models); the exam framing of these mixed results is unclear.
