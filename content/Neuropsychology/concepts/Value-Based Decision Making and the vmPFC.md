---
type: concept
status: active
scope: local
classes: Neuropsychology
projects:
domains: [neuropsychology, cognitive neuroscience, decision neuroscience]
sources:
  - "Lit_Fellows Farah 2007"
  - "Lit_Hare et al 2009"
  - "Lit_Reber et al 2017"
created: 2026-06-11
updated: 2026-06-11
---

# Value-Based Decision Making and the vmPFC

## Short definition

The **ventromedial prefrontal cortex (vmPFC, including orbitofrontal cortex)** computes a
**common value signal** — a common "currency" that lets you compare unlike options — and is
**necessary for goal-directed choice**. Damage to it produces the impulsive, inconsistent,
poor real-world decisions seen in [[Frontal Lobe Syndrome and Phineas Gage]].

## Intuition

The vmPFC is the brain's **price tag printer**. Faced with an apple, a chocolate bar, a job
offer, you need to put every option onto **one scale** ("how good is this *for me, right
now*?") so you can pick the best. The vmPFC prints those subjective price tags in a **common
currency**, so taste, health, money and risk can all be weighed against each other. Lose the
printer and you don't become *unable to act* — you act on **whim**: your choices stop being
consistent (you prefer A>B>C>A), and you chase the immediately tempting option.

## Explanation

**A common-currency value signal.** Single-unit work in monkeys (orbitofrontal "economic
value" neurons, Padoa-Schioppa) and human fMRI converge: vmPFC activity tracks the
**subjective value** of whatever is being evaluated — food, money, social outcomes — on a
common scale. This is what lets qualitatively different options be compared.

**vmPFC is needed for value, not just for uncertainty (Fellows & Farah 2007).** Earlier work
studied vmPFC patients with **gambling tasks**, framing the deficit as poor handling of
*risk/uncertainty* (e.g. Iowa Gambling Task, Bechara). Fellows & Farah asked whether vmPFC is
about uncertainty specifically, or about **value judgement per se**. They gave patients a
**preference task under certainty** — simple pairwise "which do you prefer?" choices with no
risk. Patients with **vmPFC damage made significantly more inconsistent (intransitive)
preferences** (A>B, B>C, yet C>A), while frontal patients *sparing* vmPFC were normal. So
vmPFC is necessary for **basic value-based choice even without any uncertainty** — judgement
*per se*, not just judgement under uncertainty.

**vmPFC is necessary for goal-directed (not habitual) control (Reber et al. 2017).** Behaviour
is steered by two systems: a **goal-directed** system (sensitive to the current value of
outcomes — flexible but slow) and a **habitual** system (stimulus→response, fast but
inflexible). Reber et al. used **outcome devaluation** (a canonical animal test): let people
work for a food, then **devalue** that food by feeding them to satiety, and see whether they
stop working for it. vmPFC-lesion patients **kept choosing the now-devalued outcome** — a
goal-directed deficit — even though they (a) learned the instrumental contingencies normally
(habit intact) and (b) **rated the devalued food as less pleasant normally** (hedonic
experience intact). This dissociates the systems cleanly: **vmPFC is necessary and selective
for goal-directed choice**, reconciling human lesion data with the animal literature and
explaining the real-world decision failures of vmPFC patients.

**Self-control = DLPFC modulating the vmPFC value signal (Hare et al. 2009).** Where does
willpower fit? Hare, Camerer & Rangel scanned **dieters** choosing whether to eat foods
varying in **taste** and **health**. Findings:

- **vmPFC encoded the goal value** of the chosen food in everyone, regardless of self-control.
- In **non-self-controllers**, the vmPFC value signal reflected **taste only**.
- In **successful self-controllers**, it reflected **taste *and* health**.
- **DLPFC activity rose specifically when subjects exercised self-control**, and DLPFC
  activity **correlated with (modulated) the vmPFC signal**.

So self-control is not a separate "value centre"; it is the **DLPFC reaching in and
re-weighting the vmPFC value computation** to incorporate long-term goals (health) over
immediate temptation (taste). This neatly links the **lateral control** system
([[Hierarchical Cognitive Control]], [[Working Memory and the Prefrontal Cortex]]) to the
**ventromedial value** system.

## Worked example — the dieter's choice

![[hare-self-control-design.png]]
*Hare et al. (2009), Fig. 1. (A) Three blocks: rate each food's **health**, then its **taste**,
then make real **decisions** (eat / don't). (B) Self-controllers (SC) chose to eat
liked-but-unhealthy foods far less often than non-self-controllers (NSC). Behaviourally,
self-control = letting health override taste — neurally, DLPFC modulating the vmPFC value
signal.*

Walk it through: a chocolate bar is **liked (tasty)** but **unhealthy**. The vmPFC starts to
print a high "tasty!" price tag. In a successful dieter, **DLPFC engages** and pushes the
health term into the vmPFC computation, lowering the net value below threshold → "don't eat."
In a non-self-controller DLPFC stays quiet, vmPFC prints taste-only value → "eat." Same value
region, different top-down modulation.

## Formal definition / equations

Value-based choice is usually modelled as picking the option with the highest **subjective
value** $V$. A simple self-control version of the vmPFC signal:

$$V(\text{food}) = \beta_{\text{taste}}\,\text{Taste} + \beta_{\text{health}}\,\text{Health}$$

- $\text{Taste}, \text{Health}$ — the rated attributes of the option.
- $\beta_{\text{taste}}, \beta_{\text{health}}$ — weights the brain places on each attribute.

Hare's result, in these terms: everyone has $\beta_{\text{taste}}>0$; **successful self-control
corresponds to a non-zero $\beta_{\text{health}}$**, and DLPFC engagement is what makes
$\beta_{\text{health}}$ count. Choice follows $V$ exceeding a threshold.

## Role in this class or project

This is the lecture's account of the **ventromedial / orbitofrontal** decision system — the
mechanistic content behind the personality/judgement collapse in
[[Frontal Lobe Syndrome and Phineas Gage]]. It connects to the **dACC** value/control
allocation ([[Conflict Monitoring and the Anterior Cingulate Cortex]]) and to **lateral PFC**
as the source of self-control. The broader "choice overload / paradox of choice" papers in the
lecture (Schwartz; Reutskaja & Lindner) extend this value machinery to how *too many* options
degrade value signals.

## Exam, assignment, or project relevance

Know: **vmPFC = common-currency subjective value signal, necessary for goal-directed choice**;
**Fellows & Farah** (inconsistent preferences under certainty → value *per se*, not just
uncertainty); **Reber et al.** (outcome devaluation → vmPFC selectively needed for
goal-directed, not habitual, control, with intact hedonics); **Hare et al.** (self-control =
DLPFC modulation of the vmPFC value signal; health vs taste weighting).

## Related global concepts

Promotion candidates: **Ventromedial Prefrontal Cortex (vmPFC) / Orbitofrontal Cortex**,
**Subjective value / common currency**, **Goal-directed vs habitual control**,
**Outcome devaluation**.

## Related local pages

- [[Frontal Lobe Syndrome and Phineas Gage]]
- [[Executive Functions]]
- [[Working Memory and the Prefrontal Cortex]]
- [[Conflict Monitoring and the Anterior Cingulate Cortex]]

## Common confusions

- **"vmPFC patients can't decide."** They *can* decide — they decide **badly/inconsistently**
  and impulsively; the deficit is value-based choice, not initiation.
- **"vmPFC is only about risk/gambling."** Fellows & Farah show it's needed even **under
  certainty** — it's value judgement *per se*.
- **"Self-control is a separate brain module."** It's **DLPFC modulating** the same vmPFC value
  signal, not an independent system.
- **Goal-directed ≠ habitual.** Reber's devaluation logic is the canonical way to tell them
  apart; vmPFC damage spares habit but breaks goal-directed control.

## Sources

- [[vmPFC in decision making - Fellows & Farah 2007]]
- [[Self-control modulates the vmPFC valuation system - Hare et al 2009]]
- [[Goal-directed decision-making after vmPFC lesions - Reber et al 2017]]
