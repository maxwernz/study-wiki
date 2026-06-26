---
type: method
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

# Prompt Engineering in Understanding LLMs

## Short definition

Prompt engineering is the design of input prompts that steer a language model toward a desired task behavior, reasoning pattern, format, or output distribution.

## Intuition

A frozen model contains many possible "behaviors"; the prompt is the dial that selects
one. You can't change the model, but you can change what you *ask* and *how* — and
because the model is an autoregressive continuer, the wording, examples, and demanded
format dramatically change the continuation. The deeper trick is about **computation
per token**: a model answering "what is 17×24?" in one token has to guess, but a model
told "think step by step" *spends* tokens doing intermediate arithmetic, and those
intermediate tokens become context the final answer can read. So chain-of-thought
isn't mysticism — it literally gives the model more serial computation and a scratchpad.
Prompt engineering at its best is choosing how to spend the model's "thinking budget."

## Role in this class or project

The class presents prompt engineering as the bridge from simple prompting to LM-based applications. It matters most when the model is used through a fixed prompt interface and its weights cannot be updated.

## Explanation

Prompting strategies range from direct task instructions to structured reasoning procedures. The lecture covers:

- Zero-shot prompting: an instruction and target input without examples.
- Few-shot prompting: demonstrations plus a target input.
- Chain-of-thought prompting: examples or instructions that elicit intermediate reasoning steps.
- Zero-shot chain-of-thought prompting: adding a phrase such as "Let's think step by step."
- Self-consistency: sampling multiple reasoning paths and aggregating the final answers.
- Generated-knowledge prompting: generating useful knowledge statements before answering.
- Tree of Thought: decomposing a problem into thought states, generating continuations, evaluating states, and searching through the resulting tree.

![Tree of Thought](../../outputs/images/06-ICL-Agents/tree-of-thought-p029.png)

Tree of Thought is important because it turns prompting into a modular search process: thought decomposition, thought generation, state evaluation, and tree traversal.

## Worked example

Question: *"Roger has 5 tennis balls. He buys 2 cans of 3 balls each. How many now?"*

- **Zero-shot (direct):** the model may blurt "11" or "8" — one token, no scratchpad.
- **Zero-shot CoT** ("Let's think step by step"): it generates "He starts with 5. Two
  cans × 3 balls = 6. 5 + 6 = 11." — the intermediate tokens carry the arithmetic, and
  the final "11" is read off them.
- **Self-consistency:** sample the CoT 5 times; suppose 4 paths end in "11" and 1 in
  "8". Take the **majority vote** → "11". Averaging over reasoning paths cancels
  individual slips.
- **Tree of Thought:** branch at each step, *evaluate* partial states ("is this
  arithmetic on track?"), prune bad branches, and search — overkill here, but decisive
  on puzzles where a single linear chain easily goes wrong.

## Formal definition / equations

**Self-consistency** marginalizes over $m$ sampled reasoning paths $r^{(j)}$ and takes
the most frequent answer:
$$ \hat y = \arg\max_{y}\ \sum_{j=1}^{m}\mathbb{1}\big[a(r^{(j)}) = y\big],\qquad r^{(j)}\sim P_\theta(\cdot\mid \text{prompt}), $$
where $a(r^{(j)})$ extracts the final answer from path $j$. It trades extra samples
(compute) for accuracy by voting, exploiting that correct reasoning paths agree more
often than wrong ones diverge.

## Exam, assignment, or project relevance

- Compare zero-shot prompting, few-shot prompting, and chain-of-thought prompting.
- Explain why chain-of-thought helps mainly on tasks where intermediate reasoning structure matters.
- Describe self-consistency as answer aggregation over multiple stochastic generations.
- Explain how Tree of Thought differs from a single linear chain-of-thought completion.
- Relate prompting to [[In-Context Learning in Understanding LLMs]].

## Related global concepts

No global concept page exists yet for this term.

## Related local pages

- [[In-Context Learning in Understanding LLMs]]
- [[Language Models in Understanding LLMs]]
- [[LLM Agents in Understanding LLMs]]

## Common confusions

- Prompt engineering does not require weight updates; it changes inputs and procedures around model calls.
- Chain-of-thought is not the same as guaranteed correct reasoning.
- Tree of Thought is not just "longer prompting"; it adds explicit generation, evaluation, and search structure.

## Sources

- [[Session 06 - In-Context Learning, Tool Use, Applications, and Agents]]
