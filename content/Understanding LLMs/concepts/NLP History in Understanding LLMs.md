---
type: synthesis
status: active
scope: local
classes:
  - Understanding LLMs
projects:
domains:
  - natural language processing
sources:
  - Session 01 - Introduction
created: 2026-05-14
updated: 2026-06-25
---

# NLP History in Understanding LLMs

## Short definition

The arc of NLP from **rule-based** systems (formal grammars, ELIZA) through
**statistical** methods (n-grams, HMMs, IBM translation) to **neural** representation
learning (word2vec, LSTMs) and finally **transformers** and aligned assistants — each
era trading differently between rules, statistics, scale, and transparency.

## Intuition

The history is *not* "wrong ideas replaced by right ones." It is a pendulum between
two ways of getting a machine to handle language: **write the rules yourself**
(grammars, hand-coded patterns) versus **let data set the rules** (count things,
then learn representations, then learn at scale). Each swing was driven by a
bottleneck of the last: rules don't scale to real language → count statistics; counts
are sparse and context-blind → learn dense representations; representations need
context and depth → transformers. Today's LLMs inherit the *oldest* goal (machines
that converse, the Turing test) with the *newest* tools (scale + attention), which is
exactly why the course pairs capability with "critical distrust."

## Explanation

**Foundations (information theory + Markov).** Shannon (1950) reframed language as a
**signal stream** — predict the next character from history — sidestepping the need to
define linguistic "units." Full history is unwieldy, so the **Markov assumption**
truncates it to the previous $k$ symbols, giving **$n$-gram models** ($n=k+1$:
unigram, bigram, trigram). Probabilities are estimated from **counts**.

**Two problems counts create.** **Zipf's law** — a few words are very frequent, most
are extremely rare — means most $n$-grams are never seen, so counts assign them
probability 0. **Smoothing** (Laplace's old "sunrise problem") fixes this by adding a
small $\alpha$ to every count, keeping a gap between "seen once" and "never seen."

**Rules era.** **Formal grammars** (1950s) compose symbols by rules ($C\to A\,B$);
**POS tagging** annotates words to reduce ambiguity (tag sets grew from 8 to 148).
**ELIZA** (1966) faked conversation by reflecting keywords back via ranked
pattern-response rules; **PARRY** (1971) added an affective state model (anger, fear,
mistrust) and reportedly passed a Turing-style test with psychiatrists.

**Statistical era.** **Hidden Markov Models** (1989) reason over *hidden* states from
observations (transition + emission probabilities) — used for tagging, speech, etc.
**IBM Model I** (1990) learned translation from **parallel corpora** with no
linguists, introducing the **word-alignment** problem — "the more data, the better,"
a foreshadowing of scale.

**Neural era.** **word2vec** (2013) turned the **distributional hypothesis** ("a word
is known by its company") into dense vectors (CBOW / skip-gram), enabling vector
arithmetic on meaning ($\text{king}-\text{man}+\text{woman}\approx\text{queen}$). See
[[Embeddings in Understanding LLMs]]. **RNNs/LSTMs** (1985/1997) modeled sequences with
recurrence (see [[Neural Sequence Models in Understanding LLMs]]).

**Transformer era.** **Transformers** (2017) replaced recurrence with attention; then
**BERT** (2019, bidirectional), **GPT-2/3** (2019/2020, autoregressive scale),
**RLHF** (2022, alignment), **GPT-4** (2023), **Mamba** (2023), and the
interpretability subfields (**probing** 2019, **mechanistic interpretability** 2022).
The course's own place ("ULMs, 2026") sits at the end of this line.

## Worked example

A **bigram** model on the toy corpus "the cat sat. the cat ran." Counts:
$c(\text{the cat})=2$, $c(\text{cat sat})=1$, $c(\text{cat ran})=1$. The MLE estimate
$P(\text{sat}\mid\text{cat}) = c(\text{cat sat})/c(\text{cat}) = 1/2$. But
$P(\text{slept}\mid\text{cat}) = 0/2 = 0$ — the model is *certain* "cat slept" is
impossible, purely because it wasn't seen. **Add-$\alpha$ smoothing** with $\alpha=1$
and vocabulary size $V$ gives $P(\text{slept}\mid\text{cat}) = (0+1)/(2+V)$ — small but
nonzero. This single fix is why count-based models can handle unseen text at all, and
it foreshadows the generalization that neural models achieve far better.

## Formal definition / equations

**Markov ($k$-th order) assumption:**
$$ P(w_i\mid w_1,\dots,w_{i-1}) \approx P(w_i\mid w_{i-k},\dots,w_{i-1}). $$
Only the previous $k$ symbols matter — the basis of $n$-gram models ($n=k+1$).

**$n$-gram MLE estimate** (from counts $c$):
$$ \hat P(w_i\mid w_{i-k:i-1}) = \frac{c(w_{i-k:i})}{c(w_{i-k:i-1})}. $$

**Add-$\alpha$ (Laplace) smoothing** (vocabulary size $V$, total count $N$):
$$ \hat p(w_i) = \frac{c(w_i) + \alpha}{N + V\alpha}. $$
$\alpha$ is the pseudo-count added to every event; it removes zero probabilities while
preserving the gap between seen and unseen events. $\alpha=1$ is "add-one."

**Hidden Markov Model** components: hidden states $Q=\{q_1,\dots,q_N\}$, transition
probabilities $A=\{a_{ij}\}$, emission likelihoods $B=\{b_i(o_t)\}$, initial
distribution $\Pi$, observations $O=\{o_1,\dots,o_T\}$.

## Role in this class or project

This page is the **map for the whole course**: every later technical session fills in
one era — [[Language Models in Understanding LLMs]] (the formal object the timeline
builds toward), [[Neural Sequence Models in Understanding LLMs]],
[[Transformer Architecture in Understanding LLMs]],
[[Finetuning and RLHF in Understanding LLMs]],
[[Mechanistic Interpretability in Understanding LLMs]]. Session 01 also fixes the
three explanatory targets the course keeps separate: **training**, **inference
behavior**, and **internal mechanisms**.

## Exam, assignment, or project relevance

- **Place** transformers, BERT/GPT, and RLHF in the timeline (rules → stats → neural →
  transformers).
- **Explain** why count-based models need **smoothing** (Zipf → sparsity → zero
  probabilities) and have limited context (Markov truncation).
- **State** the $n$-gram MLE and add-$\alpha$ smoothing formulas.
- **Distinguish** rule-based, statistical, and neural approaches as answers to
  different parts of the problem.

## Related global concepts

- Promotion candidates: **n-gram Language Models**, **Markov Chain / HMM**,
  **Distributional Semantics**.

## Related local pages

- [[Language Models in Understanding LLMs]]
- [[Embeddings in Understanding LLMs]]
- [[Neural Sequence Models in Understanding LLMs]]
- [[Transformer Architecture in Understanding LLMs]]
- [[Mechanistic Interpretability in Understanding LLMs]]
- [[Finetuning and RLHF in Understanding LLMs]]

## Common confusions

- **Not a straight line of replacement.** Old ideas reappear: attention echoes
  alignment from IBM Model I; the Turing-test goal is older than every method here.
- **Symbolic ≠ statistical ≠ neural as competitors.** They answer different parts of
  the modeling problem (structure vs. frequency vs. learned representation).
- **n-grams aren't "just small transformers."** They are count tables with a hard
  context window and no generalization beyond seen sequences — smoothing only patches
  zeros, it doesn't add understanding.

## Sources

- [[Session 01 - Introduction]]
