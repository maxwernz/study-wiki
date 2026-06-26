---
type: concept
status: active
scope: local
classes:
  - Understanding LLMs
projects:
domains:
  - natural language processing
  - machine learning
sources:
  - Session 06 - In-Context Learning, Tool Use, Applications, and Agents
created: 2026-05-19
updated: 2026-05-19
---

# In-Context Learning in Understanding LLMs

## Short definition

In-context learning is the ability of a language model to use examples or demonstrations inside the prompt to produce the desired output for a new input without changing model parameters.

## Intuition

Normally "learning" means changing the model's weights with gradient descent. ICL is
weirder: you hand the *frozen* model a few worked examples in the prompt — "cat → 🐱,
dog → 🐶, fish → ?" — and it completes the pattern, as if it had "learned" the task on
the spot. Nothing inside the network changed; the only thing that changed is what's in
the context window. The mental picture: the model isn't a student who studied, it's an
incredibly well-read improviser who, shown the shape of a task, recognizes "ah, this is
that kind of text" and continues it. That reframing matters because it explains the
big caveat — if the model is *pattern-matching the format* rather than *understanding
the labels*, then few-shot success can survive even nonsensical labels, which is
exactly what some studies find.

## Role in this class or project

The class uses in-context learning to explain why large autoregressive LMs can appear to adapt to a task at inference time. It also treats ICL as a disputed phenomenon: the behavior may look like learning, but it can often be explained by prompt structure, similarity, and pretrained task knowledge.

## Explanation

In $k$-shot prompting, the prompt contains $k$ demonstrations $(x_i, y_i)$ and then a target input $x_t$. The model continues the text by producing an output candidate $y_t$.

$$
(x_1, y_1), \ldots, (x_k, y_k), x_t \mapsto y_t
$$

The lecture emphasizes that ICL does not require gradient updates. The model's weights remain fixed; only the context changes. Brown et al. (2020) made this behavior prominent for GPT-3, but later work complicates a simple meta-learning interpretation.

Several factors influence ICL performance:

- Demonstration format and input-label structure.
- Similarity between demonstrations and the target input.
- Coverage of possible labels in the prompt.
- Explanations supplied alongside demonstrations.
- Model scale.

The lecture's main caution is that correct input-label mapping can matter less than expected. If performance survives shuffled or semantically odd labels, then the model may be exploiting format and distributional cues rather than "understanding" the prompt in a human-like way.

**Is ICL "really" learning?** One influential theoretical line argues that a
transformer doing ICL is *implicitly* running an optimization step: the forward pass
over the demonstrations behaves like an implicit gradient-descent update on an internal
linear model, so the model "fits" the in-context examples without any weight change.
This is a hypothesis, not settled fact — but it's why ICL is taken seriously as a form
of learning rather than mere retrieval.

## Worked example

Sentiment classification, 2-shot. Prompt:

```
Review: "Loved every minute." Sentiment: positive
Review: "A complete waste of time." Sentiment: negative
Review: "I couldn't stop smiling." Sentiment:
```

The frozen model continues with " positive". No weights moved — the two demonstrations
fixed the *format* (Review → Sentiment label) and the *label set* (positive/negative),
and the model's pretrained knowledge supplies the mapping. The unsettling finding
(Min et al. 2022): replace the demonstration labels with **random** ones ("Loved every
minute." → negative) and accuracy often barely drops — evidence that much of ICL's gain
comes from learning the *format and label distribution*, not the input→label
correspondence.

## Formal definition / equations

$k$-shot ICL maps a prompt of $k$ demonstrations plus a target to an output:
$$ (x_1,y_1),\,\dots,\,(x_k,y_k),\,x_t \ \mapsto\ y_t, $$
computed as ordinary autoregressive generation
$y_t \sim P_\theta(\cdot \mid x_1,y_1,\dots,x_k,y_k,x_t)$ with $\theta$ **fixed**.
$k=0$ is zero-shot (instruction only), $k=1$ one-shot, $k>1$ few-shot. The implicit-GD
hypothesis writes the effect of the demonstrations as an implicit update to an internal
predictor, $W \to W + \Delta W(\text{demos})$, realized entirely within the forward
pass.

## Exam, assignment, or project relevance

- Define zero-shot, one-shot, few-shot, and $k$-shot prompting.
- Explain why ICL can improve performance without parameter updates.
- Know why ICL is not automatically evidence of genuine meta-learning.
- Mention findings from Reynolds and McDonell, Min et al., Webson and Pavlick, and Lampinen et al.
- Relate ICL to [[Prompt Engineering in Understanding LLMs]] and [[Autoregressive Language Models in Understanding LLMs]].

## Related global concepts

No global concept page exists yet for this term.

## Related local pages

- [[Prompt Engineering in Understanding LLMs]]
- [[Language Models in Understanding LLMs]]
- [[Autoregressive Language Models in Understanding LLMs]]
- [[Transformer Architecture in Understanding LLMs]]

## Common confusions

- In-context learning changes the prompt, not the model weights.
- Few-shot prompting can work even when labels are not semantically natural, so success is not always prompt understanding.
- A model can benefit from examples because the prompt makes the continuation look like familiar text-generation structure.

## Sources

- [[Session 06 - In-Context Learning, Tool Use, Applications, and Agents]]
