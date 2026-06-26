---
type: method
status: active
scope: local
classes:
  - Understanding LLMs
projects:
domains:
  - machine learning
  - model adaptation
sources:
  - Session 05 - Finetuning and RLHF
created: 2026-05-14
updated: 2026-06-25
---

# Parameter-Efficient Finetuning in Understanding LLMs

## Short definition

**Parameter-efficient finetuning (PEFT)** adapts a large pretrained model by
training only a **small** number of parameters — added or selected — while keeping
the vast majority of the original weights **frozen**. **LoRA** is the headline
method: it injects small low-rank adapter matrices instead of updating the full
weight matrices.

## Intuition

Full finetuning of a 70-billion-parameter model means computing and storing a
gradient and optimizer state for *every* weight, and saving a complete 70B copy for
each task — wildly expensive. PEFT asks: do we really need to move all 70B weights to
teach the model one new task? Empirically, no — the *change* needed is small and
"low-dimensional." LoRA's bet is that the weight update has **low rank**: you can
write it as the product of two skinny matrices with very few entries. So you **freeze
the big model** and train only those few entries — like editing a giant document by
attaching a short sticky note rather than rewriting every page. Result: a fraction of
a percent of the parameters trained, one frozen base shared across many tasks, and a
tiny adapter file per task.

## Explanation

**Why full finetuning hurts at scale.** Updating all weights needs gradients +
optimizer moments for billions of parameters (memory), and a full model checkpoint
per task (storage). PEFT methods avoid one or both.

**LoRA (Low-Rank Adaptation).** For a pretrained weight matrix
$W_0\in\mathbb R^{d\times k}$, LoRA freezes $W_0$ and learns a **low-rank update**
$\Delta W = BA$, where $B\in\mathbb R^{d\times r}$ and $A\in\mathbb R^{r\times k}$ with
rank $r \ll \min(d,k)$. The adapted layer computes $h = W_0 x + BA\,x$. Only $A,B$ are
trained: instead of $d\times k$ parameters you train $r(d+k)$ — often <1%. At
inference you can **merge** $BA$ back into $W_0$, so there is no added latency.

**QLoRA.** Combines LoRA with **quantization**: the frozen base is stored in 4-bit
(see [[Model Compression in Understanding LLMs]]), drastically cutting memory, while
the small LoRA adapters are trained in higher precision. This lets a single consumer
GPU finetune very large models.

**Prompt tuning / soft prompts.** Instead of touching weights at all, learn a small
set of **continuous "prompt" vectors** prepended to the input embeddings. The frozen
model is steered by these learned vectors. Crucially, these are *learned parameters*,
not hand-written text — distinct from prompt *engineering* (see
[[Prompt Engineering in Understanding LLMs]]).

**Selective finetuning.** Simply choose a subset of existing parameters to update
(e.g. only the top layers, or only bias terms) and freeze the rest — the simplest
PEFT family.

![LoRA adapter: frozen W₀ plus trainable low-rank B·A](../../outputs/images/05-Finetuning-RLHF-2026/lora-p024.png)
*LoRA freezes the pretrained weight $W_0$ and learns a low-rank bypass $\Delta W=BA$
($r\ll d,k$); only $A,B$ are trained (deck p24).*

## Worked example

Take one weight matrix of size $d=4096$, $k=4096$ (≈16.8M parameters).

- **Full finetuning:** train all $4096\times4096 = 16{,}777{,}216$ parameters for
  this matrix alone.
- **LoRA with rank $r=8$:** train $A$ ($8\times4096$) and $B$ ($4096\times8$) =
  $2\times8\times4096 = 65{,}536$ parameters — about **0.39%** of the full count,
  for a matrix whose adapted output is $W_0 x + B(Ax)$.
- Multiply across all layers and the saving is enormous; the per-task artifact is the
  few-MB $A,B$ set, not a multi-GB model copy. **QLoRA** further stores $W_0$ in 4-bit
  so the frozen base barely uses memory while you train those 65k numbers.

## Formal definition / equations

**LoRA-adapted layer.** With frozen $W_0\in\mathbb R^{d\times k}$ and rank
$r\ll\min(d,k)$:
$$ h = W_0 x + \Delta W\,x = W_0 x + B A\,x,\qquad B\in\mathbb R^{d\times r},\ A\in\mathbb R^{r\times k}. $$
$W_0$ is not updated; only $A,B$ receive gradients. Trainable count
$r(d+k)$ vs. full $d\cdot k$ — the ratio $\tfrac{r(d+k)}{dk}$ is tiny for small $r$.
(Often scaled by $\alpha/r$: $h = W_0x + \tfrac{\alpha}{r}BAx$.) Typically $A$ is
initialized random and $B=0$, so $\Delta W=0$ at the start (training begins from the
pretrained model).

## Role in this class or project

PEFT is the *practical enabler* of [[Finetuning and RLHF in Understanding LLMs]]:
SFT, instruction tuning, and even RLHF policies are routinely trained with LoRA so
they fit realistic compute budgets. It operates on the weight matrices of the
[[Transformer Architecture in Understanding LLMs]] and shares the quantization idea
with [[Model Compression in Understanding LLMs]] — together they are the course's two
efficiency levers (training-side and inference-side).

## Exam, assignment, or project relevance

- **Explain why full finetuning is expensive** (gradients/optimizer state per
  parameter; a full checkpoint per task).
- **Write the LoRA decomposition** $\Delta W = BA$ and compute the parameter saving.
- **Say what QLoRA adds** (4-bit frozen base) and what prompt tuning learns (soft
  prompt vectors, not text).
- **Distinguish** PEFT (learned parameters) from prompt *engineering* (hand-written
  prompts).

## Related global concepts

- Promotion candidates: **LoRA / Low-Rank Adaptation**, **Parameter-Efficient
  Finetuning**.

## Related local pages

- [[Finetuning and RLHF in Understanding LLMs]]
- [[Optimization for Language Models in Understanding LLMs]]
- [[Transformer Architecture in Understanding LLMs]]
- [[Model Compression in Understanding LLMs]]
- [[Prompt Engineering in Understanding LLMs]]

## Common confusions

- **LoRA is not a new architecture** — it's an adaptation method bolted onto an
  existing model's weight matrices.
- **Prompt tuning ≠ prompt engineering.** Prompt tuning *learns* continuous vectors
  by gradient descent; prompt engineering *writes* discrete text by hand.
- **"Low-rank" refers to the update, not the model.** The base weights are full-rank
  and frozen; only the trained *delta* is constrained to be low-rank.

## Sources

- [[Session 05 - Finetuning and RLHF]]
