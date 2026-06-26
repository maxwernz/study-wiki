---
type: method
status: active
scope: local
classes:
  - Understanding LLMs
projects:
domains:
  - machine learning
  - alignment
sources:
  - Session 05 - Finetuning and RLHF
created: 2026-05-14
updated: 2026-06-25
---

# Finetuning and RLHF in Understanding LLMs

## Short definition

**Finetuning** continues training a pretrained model on new data to change its
behavior. **RLHF** (Reinforcement Learning from Human Feedback) aligns a model with
human preferences by (1) supervised finetuning, (2) training a **reward model** from
human comparisons, and (3) optimizing the model as a **policy** to maximize that
reward while staying close to its starting point.

## Intuition

A pretrained model is a brilliant autocompleter that has read the internet — but it
completes text, it doesn't *help you*. Ask "how do I make an omelet?" and a base
model might continue with more questions, because that's a statistically plausible
continuation. **Finetuning** is the etiquette school that teaches it to answer
instead of ramble. The cheapest lesson is **supervised finetuning**: show it
thousands of good question→answer demonstrations and have it imitate them
(behavioral cloning). But you can't write a demonstration for everything, and "good"
is subjective. **RLHF** solves this by learning from *judgments* rather than
demonstrations: humans find it hard to score an answer 7.3/10 but easy to say "A is
better than B." So we collect comparisons, distill them into a **reward model** (an
automatic judge), and then let the model practice against that judge — with a leash
(the **KL penalty**) so it doesn't wander off into weird high-reward gibberish.

## Explanation

**The alignment gap.** Pretraining optimizes next-token likelihood; it does not
optimize helpfulness, honesty, or harmlessness ("language modeling ≠ assisting
users," Ouyang et al. 2022). Everything in this lecture closes that gap.

**Supervised finetuning (SFT).** Train on demonstration pairs (prompt → desired
output) with the ordinary cross-entropy loss (see
[[Optimization for Language Models in Understanding LLMs]]). This **shifts** the
model's output distribution from the broad pretraining distribution $\Delta(S)$ to a
task-specific $\Delta'(S)$. **Instruction finetuning** is SFT on a *broad* mix of
instruction-following tasks, so the model generalizes to unseen instructions. SFT
also produces the **reference policy** $\pi_{\mathrm{ref}}$ used later as the RLHF
anchor.

**RLHF as an RL problem.** Frame the LM as a **policy** $\pi_\theta(a\mid s)$: the
state $s$ is the conversation so far, the action $a$ is the next token, and the
reward measures how good the output is. Because asking humans for a reward at every
step is too slow/expensive, we **learn a reward model** $r_\phi(x,y)$ from human
preference data, then optimize the policy against it. The three practical stages
(OpenAI 2022; Ouyang et al. 2022):

1. **SFT** → produces $\pi_{\mathrm{ref}}$.
2. **Reward model.** Collect preference pairs (a prompt $x$ with a preferred
   completion $y_w$ and a dispreferred $y_l$) and fit $r_\phi$ with the
   **Bradley–Terry** loss so it scores $y_w$ above $y_l$.
3. **Policy optimization.** Optimize $\pi_\theta$ to maximize $r_\phi$ with a
   **per-token KL penalty** to $\pi_{\mathrm{ref}}$, typically via **PPO**.

**Why the KL leash.** Without the $\beta\,D_{\mathrm{KL}}(\pi_\theta\Vert\pi_{\mathrm{ref}})$
term, the policy drifts into **reward-hacked**, degenerate regions: text that scores
high under the imperfect $r_\phi$ but that humans would hate (mode collapse,
gibberish). The penalty says "improve reward, but pay for moving away from the
sensible SFT model."

**PPO vs. DPO.** **PPO** learns $r_\phi$ explicitly and does online RL (sampling
fresh rollouts), keeping **four models** in memory (policy, frozen reference, reward
model, value head) — powerful but hyperparameter-sensitive and reward-hackable.
**DPO** (Direct Preference Optimization) exploits a closed-form solution of the
KL-constrained objective to **skip the reward model entirely**, turning preference
optimization into a single **supervised loss** on $\pi_\theta$ (just policy +
reference). DPO is stabler and cheaper (good for academic budgets) but is offline by
default and bounded by the fixed preference dataset.

**Types of human feedback** (Casper et al. 2023): pairwise **comparison**, full
**ranking**, **scalar** rating, free-text feedback (reward inferred — inverse RL),
**correction**, and **label**. Comparisons dominate because humans are reliable at
them.

![RLHF step 1 — supervised finetuning (behavioral cloning)](../../outputs/images/05-Finetuning-RLHF-2026/rlhf-step-1-p069.png)
*Step 1: SFT on demonstrations shifts the pretraining distribution to a
task-specific one and yields $\pi_{\mathrm{ref}}$ (deck p69).*

![RLHF step 2 — reward model from human preferences](../../outputs/images/05-Finetuning-RLHF-2026/rlhf-step-2-p070.png)
*Step 2: humans compare outputs; a reward model $r_\phi$ is trained to score
preferred completions above dispreferred ones (deck p70).*

![RLHF step 3 — policy optimization against the reward model](../../outputs/images/05-Finetuning-RLHF-2026/rlhf-step-3-p071.png)
*Step 3: the policy is optimized (PPO) to maximize $r_\phi$ with a KL penalty to
$\pi_{\mathrm{ref}}$ (deck p71).*

## Worked example

Prompt $x$ = "How do I make an omelet?", with completions $y_w$ (a clear recipe) and
$y_l$ ("1) buy a stove 2) pay the electricity bill"). A human marks $y_w \succ y_l$.

- **Reward model:** Bradley–Terry says the probability the human prefers $y_w$ is
  $\sigma(r(x,y_w)-r(x,y_l))$. Training pushes $r_\phi(x,y_w)$ above $r_\phi(x,y_l)$;
  if it currently scores them $0.4$ and $0.6$, the gradient raises the first and
  lowers the second until the gap has the right sign.
- **DPO update (no reward model):** the loss directly raises
  $\log\pi_\theta(y_w\mid x)$ and lowers $\log\pi_\theta(y_l\mid x)$, weighted by how
  *wrong* the model currently is — large gradient on hard examples, near-zero once it
  already prefers $y_w$. The reference $\pi_{\mathrm{ref}}$ keeps it from overshooting.

## Formal definition / equations

**SFT loss** (cross-entropy on demonstrations $(x,y)$):
$\mathcal L_{\text{SFT}} = -\sum_t \log\pi_\theta(y_t\mid x, y_{<t})$.

**Bradley–Terry preference likelihood** (latent reward $r$, sigmoid $\sigma$):
$$ P(y_w \succ y_l\mid x) = \sigma\big(r(x,y_w) - r(x,y_l)\big). $$
Only reward *differences* matter ($r$ is identifiable up to an additive constant per
prompt). **Reward-model loss:**
$$ \mathcal L(\phi) = -\,\mathbb E_{(x,y_w,y_l)}\big[\log\sigma\big(r_\phi(x,y_w) - r_\phi(x,y_l)\big)\big]. $$

**KL-constrained RLHF objective:**
$$ \max_{\pi_\theta}\ \mathbb E_{x,\,y\sim\pi_\theta}\big[r(x,y)\big] \;-\; \beta\, D_{\mathrm{KL}}\!\big(\pi_\theta \,\Vert\, \pi_{\mathrm{ref}}\big). $$
Maximize reward, penalized by distance from the reference; $\beta$ sets the leash
length.

**PPO clipped objective** (probability ratio $\rho_t=\pi_\theta(a_t\mid s_t)/\pi_{\theta_{old}}(a_t\mid s_t)$,
advantage $A_t$, clip $\varepsilon\approx0.2$):
$$ \mathcal L^{\text{CLIP}}(\theta) = \mathbb E_t\big[\min(\rho_t A_t,\ \mathrm{clip}(\rho_t,1-\varepsilon,1+\varepsilon)A_t)\big] - \beta\,\mathrm{KL}[\pi_\theta\Vert\pi_{\mathrm{ref}}]. $$
Clipping caps how far one update can move the policy.

**DPO loss** (closed-form, no $r_\phi$): the optimal policy satisfies
$\pi^*(y\mid x)\propto\pi_{\mathrm{ref}}(y\mid x)\exp(r(x,y)/\beta)$, so the implicit
reward is $r_\theta(x,y)=\beta\log\frac{\pi_\theta(y\mid x)}{\pi_{\mathrm{ref}}(y\mid x)}$.
Plugging into Bradley–Terry (the partition $Z(x)$ cancels):
$$ \mathcal L_{\text{DPO}}(\theta) = -\,\mathbb E_{(x,y_w,y_l)}\Big[\log\sigma\Big(\beta\log\tfrac{\pi_\theta(y_w\mid x)}{\pi_{\mathrm{ref}}(y_w\mid x)} - \beta\log\tfrac{\pi_\theta(y_l\mid x)}{\pi_{\mathrm{ref}}(y_l\mid x)}\Big)\Big]. $$

## Role in this class or project

This is the course's account of how a **base LM becomes an assistant** — the bridge
from [[Language Models in Understanding LLMs]] (what the model *is*) to its deployed
behavior. It reuses [[Optimization for Language Models in Understanding LLMs]] (SFT
is plain cross-entropy; PPO/DPO are gradient ascent on new objectives) and is made
affordable by [[Parameter-Efficient Finetuning in Understanding LLMs]]. The
helpful/honest/harmless goal connects to
[[Behavioral Assessment and Calibration in Understanding LLMs]].

## Exam, assignment, or project relevance

- **Distinguish** pretraining, SFT, instruction finetuning, and RLHF.
- **Recite the three RLHF stages** and say why a reward model is learned.
- **Write the Bradley–Terry** preference likelihood and reward-model loss.
- **Explain the KL penalty** and reward hacking.
- **Contrast PPO and DPO** (explicit vs. implicit reward, online vs. offline, 4 vs. 2
  models, stability/failure modes).

## Related global concepts

- Promotion candidates: **Reinforcement Learning from Human Feedback**, **Policy
  Gradient / PPO**, **Direct Preference Optimization**, **Bradley–Terry model**.

## Related local pages

- [[Language Models in Understanding LLMs]]
- [[Optimization for Language Models in Understanding LLMs]]
- [[Parameter-Efficient Finetuning in Understanding LLMs]]
- [[Benchmarking LLMs in Understanding LLMs]]
- [[Behavioral Assessment and Calibration in Understanding LLMs]]

## Common confusions

- **RLHF ≠ guaranteed truth/safety.** It optimizes a *learned proxy* for human
  preference; the reward model can be gamed (reward hacking).
- **A reward model is not human judgment**, just a trained approximation that
  extrapolates badly as the policy drifts (distribution shift).
- **Instruction finetuning ≠ RLHF.** The former is supervised imitation; the latter
  optimizes against preferences.
- **DPO has no explicit reward model**, yet still does preference optimization — the
  reward is *implicit* in the policy/reference log-ratio.

## Sources

- [[Session 05 - Finetuning and RLHF]]
