---
type: concept
status: active
scope: local
classes: Neuropsychology
projects:
domains: [neuropsychology, cognitive neuroscience]
sources:
  - "Lit_Kerns et al 2004"
  - "Lit_Shenhav et al 2013"
created: 2026-06-11
updated: 2026-06-11
---

# Conflict Monitoring and the Anterior Cingulate Cortex

## Short definition

The **dorsal anterior cingulate cortex (dACC)**, on the **medial** wall of the frontal lobe,
**monitors** for situations that need more control — especially **response conflict** — and
signals the lateral PFC to **adjust control**. A broader theory recasts this as the dACC
**deciding how much control is worth allocating**.

## Intuition

The dACC is a **smoke detector for your behaviour**. It doesn't fight the fire (that's the
DLPFC's job) — it **detects trouble and sounds the alarm**. When two responses compete (you
almost said the wrong thing), the detector blares; that alarm makes the "firefighter" (lateral
PFC) turn up focus, so the *next* moment you're more careful. The richer version: a good
detector doesn't just scream at every wisp of smoke — it **weighs whether responding is worth
the effort** (a burnt-toast wisp vs a real fire). That cost–benefit calculation is the
"expected value of control."

## Explanation

**The conflict-monitoring hypothesis.** The medial frontal/dACC is reliably active in tasks
where a **prepotent (habitual) response competes with the correct one** — Stroop, Eriksen
flanker, go/no-go. The hypothesis (Botvinick, Cohen, Carter): dACC **detects response
conflict** (simultaneous activation of incompatible responses) and uses it as a signal that
**control should be increased**, recruiting lateral PFC to bias processing toward the goal.

**Kerns et al. (2004): the causal-sequence test.** It had been *questioned* whether conflict
actually drives subsequent control adjustments. Kerns used the Stroop task with fMRI and the
**Gratton (conflict-adaptation) effect**: people are **faster and more accurate on a
high-conflict trial that follows another high-conflict trial** (post-conflict adjustment).
The elegant result chain: **dACC conflict-related activity on trial *n*** predicted **(a)
greater DLPFC activity** and **(b)** greater behavioural adjustment (slowing + accuracy gain)
**on trial *n+1***. This is the missing link — it shows the predicted **monitor → adjust**
sequence in real data: dACC monitors, lateral PFC implements, behaviour improves. (See the
loop figure below.)

**Shenhav et al. (2013): the Expected Value of Control (EVC).** The dACC has been tied to a
*bewildering* range of functions — pain, reward, error, effort, value, motivation. Rather than
pick one or oversimplify, Shenhav, Botvinick & Cohen propose a **single integrative function**:
the dACC computes the **Expected Value of Control** and uses it to decide **whether, where, and
how much control to allocate**. EVC integrates three quantities:

- the **expected payoff** of a controlled process (how much reward/benefit if it succeeds),
- **how much control** must be invested to get that payoff,
- the **cost of cognitive effort** itself (control is intrinsically aversive/costly).

On this view conflict monitoring is **one input** to EVC, not the whole story: conflict is one
cue that more control would pay off. EVC explains why dACC tracks reward *and* effort *and*
errors — they are all terms in the same control-allocation calculation.

## Worked example — a Stroop sequence, as a loop

![[acc-conflict-control-loop.pdf]]
*The monitor→adjust loop. An incongruent Stroop trial creates response conflict; dACC detects
it and (per EVC) evaluates whether control is worth its effort cost; if so it specifies how
much control; DLPFC implements it by biasing the task-relevant representation; the result is a
behavioural adjustment (the post-conflict Gratton effect), which feeds back to reduce conflict.
Conflict monitoring (Kerns 2004) is thus one input to the broader EVC computation (Shenhav 2013).*

Step through it: trial *n* = the word **GREEN** in red ink, rule "name the ink." Word-reading
(say "green") competes with the goal (say "red") → **conflict**. dACC fires. On trial *n+1*,
DLPFC has turned up control, so you're slower but more accurate — and a control-demanding
trial that follows conflict is handled better than one that follows an easy trial.

## Formal definition / equations

The EVC of allocating a control signal is, schematically, the expected payoff of the
controlled outcome minus the cost of the control invested:

$$\mathrm{EVC}(\text{signal}, \text{state}) = \Big[\sum_{\text{outcomes}} P(\text{outcome}\mid \text{signal},\text{state})\, V(\text{outcome})\Big] - \mathrm{Cost}(\text{signal})$$

- $V(\text{outcome})$ — the value (reward) of each possible outcome.
- $P(\cdot\mid\text{signal},\text{state})$ — how the chosen control signal changes the
  probability of each outcome in the current state.
- $\mathrm{Cost}(\text{signal})$ — the intrinsic effort cost of that much control.

In words: **allocate the control signal that buys the most expected reward per unit of effort.**
The dACC's job is to find and specify that signal.

## Role in this class or project

This is the lecture's **medial-frontal monitoring/allocation** system, complementing the
**lateral** implementation system in [[Hierarchical Cognitive Control]] and feeding the
**ventromedial** value system in [[Value-Based Decision Making and the vmPFC]]. Together
they form the regulate-and-decide core of [[Executive Functions]]. Note the medial frontal
cortex overlap with social cognition ([[Medial Frontal Cortex and Social Cognition]]).

## Exam, assignment, or project relevance

Know: **dACC = monitor, DLPFC = implement**; the **conflict-monitoring hypothesis** and the
**Gratton/post-conflict adjustment** effect; **Kerns et al. 2004** as the demonstration that
trial-*n* dACC conflict predicts trial-*n+1* DLPFC activity and behavioural adjustment; and
the **EVC theory** (the three ingredients: payoff, required control, effort cost) as an
integrative account of dACC's many roles.

## Related global concepts

Promotion candidates: **Anterior Cingulate Cortex**, **Cognitive control / conflict
monitoring**, **Expected Value of Control**, **Cost of cognitive effort**.

## Related local pages

- [[Executive Functions]]
- [[Hierarchical Cognitive Control]]
- [[Value-Based Decision Making and the vmPFC]]
- [[Medial Frontal Cortex and Social Cognition]]

## Common confusions

- **dACC does not *exert* control** — it monitors/allocates; the **lateral PFC** does the
  biasing. Reversing these is a common error.
- **"dACC = error detection only."** Error and conflict are *related* signals, but the modern
  EVC view is broader: dACC allocates control based on cost–benefit, of which conflict/error
  are inputs.
- **Conflict ≠ difficulty per se** — it specifically means **co-activation of incompatible
  responses**, not just a hard problem.
- **dorsal vs ventral ACC** — the monitoring/control role is **dorsal** ACC; ventral/subgenual
  ACC is more affective.

## Sources

- [[Anterior cingulate conflict monitoring - Kerns et al 2004]]
- [[The expected value of control - Shenhav et al 2013]]
