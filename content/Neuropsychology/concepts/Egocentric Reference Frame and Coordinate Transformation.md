---
type: concept
status: active
scope: local
classes: Neuropsychology
projects:
domains: spatial cognition, sensorimotor integration, neuropsychology
sources: Neglect.pdf; Karnath 2015; Karnath & Dieterich 2006
created: 2026-06-11
updated: 2026-06-11
---

# Egocentric Reference Frame and Coordinate Transformation

## Short definition

The **egocentric (body-centred) reference frame** is the brain's internal map that codes
where objects are **relative to the trunk**. To build it, the brain runs a **coordinate
transformation**: it converts the retinal (retinotopic) image into head-centred and then
body-centred coordinates by combining it with eye-, head- and trunk-position signals. In
spatial neglect this transformation works with a systematic error, rotating the frame
toward the ipsilesional side.

## Intuition

Your eyes give you "where things are on my retina," but that is useless for action, because
the retina moves every time your eye or head moves. To grab a cup you need "where the cup
is relative to my body." The brain therefore re-references the image in steps: "the cup is
here on my retina" → (knowing where my eye points) "here relative to my head" → (knowing
where my head sits on my trunk) "here relative to my body." Each step needs an extra
position signal. It is like converting GPS-on-a-spinning-camera into a stable map of the
room. If one of those position signals is mis-weighted, the whole map ends up rotated — and
you don't notice, because the map *is* your sense of "straight ahead."

## Explanation

**The transformation chain (Karnath 1994, "transformation hypothesis").** Visual space is
re-referenced through successive coordinate frames:

- **Retinotopic** (position of the image on the retina)
- → **Head-centred**, by adding **eye-in-head** position. Eye-in-head is itself estimated
  from **eye-muscle proprioception** and **efference copy** (the brain's own copy of the
  motor command sent to the eye).
- → **Body-centred / egocentric**, by adding **head-in-space** and **head-on-trunk**
  position. These come from the **vestibular** organ (head-in-space) and **neck-muscle
  proprioception** (head-on-trunk).
- The egocentric map then drives **space exploration and orienting**; **auditory** input
  also feeds in directly at the body-centred stage.

So the egocentric frame is a **multisensory construction**: retina + eye signals +
vestibular + neck proprioception (+ auditory). The cortical substrate is the right
multisensory/perisylvian network (see [[Perisylvian Network for Spatial Orienting]]).

![[outputs/images/spatial-neglect/coordinate-transformation.pdf]]
*Figure — the coordinate-transformation chain (retinotopic → head-centred → body-centred)
and the position signals feeding each stage; in neglect a systematic error at the
body-centred stage rotates the egocentric frame rightward. (Redrawn from the lecture's
"transformation hypothesis" diagram, Karnath 1994.)*

**How neglect fits.** In neglect this integration carries a **systematic error**: the whole
egocentric frame settles at a new equilibrium ("default position") rotated toward the
ipsilesional right. Spatially-directed action — including the voluntary control of attention
— is organised on this shifted frame, so exploration is biased right and the left is
neglected. Crucially the *top-down control itself* is intact; only the matrix it runs on is
displaced.

**The decisive evidence — manipulate the inputs, move the bias.** Because the frame is built
from these channels, you can push it around:
- **Caloric vestibular stimulation** (cold water in the left ear) and **posterior
  neck-muscle vibration** shift the exploration centre back toward the trunk midline and can
  abolish neglect.
- The **same** stimulation in **healthy** people induces neglect-*like* asymmetric search.
- The bias does **not** track gravity when the body is tilted — confirming it is *body*-
  referenced, not world/gravity-referenced.

## Worked example

A neglect patient searches a surrounding array in darkness. **No stimulation:** their gaze
explores only the right ~two-thirds, centred ~20–46° right of the body midline. **Left neck-
muscle vibration:** the centre slides leftward toward the midline and they now fixate
previously missed left targets. **Left cold-caloric stimulation:** the centre moves even
further left, search becomes roughly symmetric, and contralesional neglect is temporarily
abolished. Mechanistically, the vibration falsifies the **head-on-trunk** signal and the
caloric stimulation falsifies the **head-in-space** signal — both inputs to the egocentric
transformation — so the computed body-midline is dragged back toward true centre.

## Formal definition / equations

No numerical formalism in the lecture, but the chain can be stated compactly:

$$P_{\text{body}} = P_{\text{retina}} \;\oplus\; \underbrace{(\text{eye-in-head})}_{\text{proprioception + efference copy}} \;\oplus\; \underbrace{(\text{head-on-trunk})}_{\text{neck proprioception}} \;\oplus\; \underbrace{(\text{head-in-space})}_{\text{vestibular}}$$

where $P_{\text{retina}}$ is the object's retinal position, each $\oplus$ adds a position
signal that re-references the location into the next frame, and $P_{\text{body}}$ is its
final body-centred location. In words: the body-centred position is the retinal position
corrected successively by eye, neck and vestibular signals. In neglect, the head-on-trunk /
head-in-space terms are effectively biased, so $P_{\text{body}}$ is computed with a constant
rightward offset.

## Role in this class or project

This is the **mechanism** half of the Spatial neglect "What should I know" outline, and the
unifying idea linking neglect's behaviour, its multisensory anatomy, and its modulation by
stimulation. It also underlies the contrast with [[Pusher Syndrome]], which disturbs a
*different* body-orientation computation (upright/roll plane, a second graviceptive system).

## Exam, assignment, or project relevance

Be able to draw the retinotopic → head-centred → body-centred chain and label each input
(eye-muscle proprioception, efference copy, neck proprioception, vestibular, auditory);
explain why neglect is a transformation error; and explain why vestibular and neck-vibration
stimulation modulate the bias while gravity tilt does not.

## Related global concepts

- Promotion candidate: **egocentric vs allocentric spatial reference frames** is a reusable
  concept (appears in spatial cognition, navigation, parietal-cortex coding).

## Related local pages

- [[Spatial Neglect]] · [[Perisylvian Network for Spatial Orienting]] · [[Pusher Syndrome]]

## Common confusions

- **Efference copy vs proprioception:** both estimate eye-in-head, but efference copy is the
  *predicted* eye position from the motor command, while proprioception is the *sensed*
  position from the muscle — complementary, not the same.
- **Egocentric ≠ allocentric.** Egocentric = relative to the body; allocentric = relative to
  external objects/world. Core neglect is egocentric; line-bisection/object-based neglect is
  more allocentric.

## Sources

- [[Spatial Neglect - lecture slides (Karnath)]]
- [[Spatial attention systems in spatial neglect - Karnath 2015]]
- [[Spatial neglect - a vestibular disorder - Karnath & Dieterich 2006]]
