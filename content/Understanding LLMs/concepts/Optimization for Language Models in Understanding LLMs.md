---
type: method
status: active
scope: local
classes:
  - Understanding LLMs
projects:
domains:
  - machine learning
  - optimization
sources:
  - Session 02 - PyTorch, Optimization, ANNs, LMs, RNNs, LSTMs
created: 2026-05-14
updated: 2026-06-25
---

# Optimization for Language Models in Understanding LLMs

## Short definition

Optimization is the process of adjusting a model's parameters $\theta$ to minimize
a **loss function** — for language models, the **negative log likelihood**
(equivalently cross-entropy) of the training data — by repeatedly stepping the
parameters in the direction the **gradient** says reduces loss fastest.

## Intuition

Picture the loss as a hilly landscape whose horizontal coordinates are the
millions of parameters and whose height is "how wrong the model is." Training is a
blindfolded hiker trying to reach a valley. At each step the hiker can feel the
**slope** under their feet (the gradient) and takes a small step downhill (the
size of the step is the **learning rate**). Do this millions of times and you
settle into a low valley — a parameter setting that assigns high probability to
the training text. "Stochastic" just means the hiker estimates the slope from a
small random sample of the data each step instead of surveying the whole terrain,
which is noisier but far cheaper.

## Explanation

**What is being minimized.** A probabilistic language model defines
$P_{M(\theta)}(y\mid x)$ — a probability for output $y$ given input $x$. Good
parameters make the *observed* data probable. We turn "make data probable" into
"minimize a loss" by taking the **negative log likelihood (NLL)**: maximizing
likelihood = minimizing $-\log$ likelihood. For next-token prediction with a
one-hot target, NLL coincides exactly with **cross-entropy** and with the token's
**surprisal** — three names for the same number (see
[[Autoregressive Language Models in Understanding LLMs]]).

**How the gradient is obtained.** The loss is a deeply nested function of the
parameters (layers feeding layers). **Backpropagation** applies the chain rule
*backwards* through the computation graph to get $\partial L/\partial\theta$ for
every parameter in one efficient pass. PyTorch builds the graph automatically
(**autodiff**) so you never differentiate by hand.

**How the step is taken.** **Stochastic gradient descent (SGD)** nudges each
parameter against its gradient, scaled by the learning rate $\eta$. Plain SGD uses
the raw gradient; practical optimizers add refinements — **momentum** (average
recent gradients to push through small bumps and speed up consistent directions)
and **Adam** (per-parameter adaptive step sizes from running estimates of the
gradient's mean and variance), which is the default for training LMs because it
handles the very different scales of different parameters gracefully.

**The five-step training loop** (the deck's "anatomy of a training step"):
1. **Compute predictions** — forward pass: what does the model say now?
2. **Compute the loss** — how wrong is that, on this batch?
3. **Backpropagate** — in which direction should each parameter change?
4. **Update parameters** — step by the learning rate in that direction.
5. **Zero the gradients** — reset, so the next batch's gradients don't accumulate
   onto this one's.

Forgetting step 5 is a classic bug: PyTorch *accumulates* gradients by default, so
without zeroing them you'd sum gradients across batches.

## Worked example

Predict the next token over a 3-word vocabulary {a, b, c}. The true next token is
**a** (one-hot $y=[1,0,0]$). The model currently predicts $\hat y=[0.2,0.5,0.3]$.

- **Loss (cross-entropy / surprisal):**
  $L = -\sum_w y^w\log\hat y^w = -\log(0.2) \approx 1.61$ nats.
  Only the correct token's probability matters because $y$ is one-hot.
- Had the model predicted $\hat y=[0.7,0.2,0.1]$, the loss would be
  $-\log(0.7)\approx 0.36$ — much lower, because it put more mass on the right
  token. So minimizing this loss literally means **pushing probability toward the
  observed token**.
- **One SGD step:** if for some parameter $\theta_k$ we have
  $\partial L/\partial\theta_k = -4$ and $\eta = 0.1$, then
  $\theta_k \leftarrow \theta_k - 0.1\cdot(-4) = \theta_k + 0.4$ — we move $\theta_k$
  *up* because increasing it lowers the loss.

## Formal definition / equations

**Objective.** Given data $D=\langle X,Y\rangle$ and per-example loss $L$,
$$ \hat\theta = \arg\min_{\theta\in\Theta}\ \sum_{(x,y)\in D} L(\theta,x,y), \qquad L(\theta,x,y) = -\log P_{M(\theta)}(y\mid x). $$
$\theta$ = parameters; $\Theta$ = parameter space; $L$ = negative log likelihood.

**Cross-entropy form** (categorical target with one-hot $y^w$, predicted
distribution $\hat y^w$):
$$ L = -\sum_{w\in\mathcal V} y^w \log \hat y^w \;=\; -\log \hat y^{\,w^*}, $$
where $w^*$ is the true token. The sum collapses to a single term — the surprisal
of the correct token.

**SGD update** (learning rate $\eta$, mini-batch gradient $\nabla_\theta L$):
$$ \theta \leftarrow \theta - \eta\,\nabla_\theta L. $$

**With momentum** (velocity $v$, coefficient $\beta$):
$$ v \leftarrow \beta v + \nabla_\theta L, \qquad \theta \leftarrow \theta - \eta\,v. $$
Momentum accumulates a running velocity so consistent gradient directions build
speed and noisy ones cancel. **Adam** extends this with separate first- and
second-moment estimates to give each parameter its own effective step size.

## Role in this class or project

This page is the bridge from *what a language model is* (a probability
distribution, [[Language Models in Understanding LLMs]]) to *how you actually
build one*. The same machinery — loss, gradients, optimizer — is reused at every
later stage: it is the inner loop of pretraining, of supervised finetuning, and of
the policy-gradient updates in [[Finetuning and RLHF in Understanding LLMs]], and
it is what [[Parameter-Efficient Finetuning in Understanding LLMs]] makes cheaper.

## Exam, assignment, or project relevance

- **Recite the five-step loop** and explain *why* gradients must be zeroed.
- **Show** that NLL = cross-entropy = surprisal for a one-hot next-token target.
- **Write the SGD update** and explain the role of the learning rate.
- **Explain** why we minimize *negative log* likelihood rather than likelihood
  directly (numerical stability + turns a product into a sum).

## Related global concepts

- Promotion candidates: **Maximum Likelihood Estimation**, **Stochastic Gradient
  Descent / Numerical Optimization**, **Cross-Entropy**.

## Related local pages

- [[Language Models in Understanding LLMs]]
- [[Autoregressive Language Models in Understanding LLMs]]
- [[Neural Sequence Models in Understanding LLMs]]
- [[Finetuning and RLHF in Understanding LLMs]]

## Common confusions

- **Minimizing loss ≠ maximizing usefulness.** The model optimizes whatever the
  loss encodes — next-token likelihood, not helpfulness or truth. This gap is the
  whole reason RLHF exists.
- **Lower training loss ≠ better generalization.** Pushed too far, the model
  overfits — it memorizes training text without predicting new text better.
- **"Gradient descent finds the global minimum."** In these non-convex landscapes
  it finds *a* good-enough valley, not provably the best one; that is fine in
  practice.

## Sources

- [[Session 02 - PyTorch, Optimization, ANNs, LMs, RNNs, LSTMs]]
