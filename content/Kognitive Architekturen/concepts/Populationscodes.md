---
type: concept
status: active
scope: local
classes: [Kognitive Architekturen]
projects:
domains: [neural coding, spatial representation]
sources: ["VL10 Multisensorische Interaktion und Räume"]
created: 2026-07-01
updated: 2026-07-01
---

# Populationscodes

## Short definition

Ein Populationscode repräsentiert eine kontinuierliche Größe (z. B. eine Richtung, einen
Ort) nicht durch ein einzelnes Neuron, sondern durch das **gemeinsame Aktivitätsmuster
vieler grob getunter Neuronen mit überlappenden rezeptiven Feldern**.

## Intuition

Stell dir einen Chor vor, in dem jede Sängerin auf eine bevorzugte Tonhöhe „geeicht" ist
und umso lauter singt, je näher der gespielte Ton an ihrer Lieblingstonhöhe liegt. Kein
einzelner Ton wird von genau einer Sängerin gemeldet – aber aus der *Lautstärke­verteilung
über den ganzen Chor* kannst du den gespielten Ton sehr genau ablesen, und du erkennst
zusätzlich, *wie sicher* die Sache ist (scharfer Peak = sicher, breiter Berg = unsicher).
Genau so kodiert eine Neuronenpopulation eine Größe: robust gegen Ausfall einzelner
Neuronen und mitsamt ihrer Unsicherheit.

## Explanation

Ein einzelnes Neuron ist ein schlechter Melder für einen kontinuierlichen Wert: seine
Feuerrate ist mehrdeutig (dieselbe Rate kann von zwei verschiedenen Reizen kommen) und
verrauscht. Ein **Populationscode** löst das, indem viele Neuronen mit jeweils eigener
**Tuningkurve** (rezeptivem Feld) zusammenarbeiten. Jedes Neuron $i$ hat eine
**präferierte Größe** $s_i$ und feuert am stärksten, wenn der Reiz $s$ dort liegt; die
Antwort fällt mit dem Abstand ab (z. B. als rektifizierter Cosinus über dem Winkel
zwischen $s$ und $s_i$, oder als Gauß-Glocke). Weil die rezeptiven Felder **überlappen**,
aktiviert jeder Reiz mehrere Neuronen gleichzeitig.

Drei Eigenschaften machen das mächtig:

1. **Redundanz/Robustheit.** Fällt ein Neuron aus oder rauscht, tragen die Nachbarn die
   Information weiter.
2. **Verteilungen statt Punktschätzungen.** Das gesamte Aktivitätsprofil approximiert eine
   **Wahrscheinlichkeitsverteilung** über der kodierten Größe. Dadurch kann die Population
   nicht nur „wo", sondern auch **Unsicherheit**, **Wettbewerb** zwischen mehreren
   Stimuli und **Sicherheit der Präsenz** eines Stimulus darstellen. Das ist die
   Voraussetzung dafür, dass Populationscodes **Bayes-Prinzipien** umsetzen können (siehe
   [[Multisensorische Informationsfusion]]).
3. **Topographie.** Häufig stimmt **neuronale Nähe mit räumlicher Nähe** überein –
   benachbarte Neuronen kodieren benachbarte Reize. Beispiele: die **retinotope** Karte im
   visuellen Kortex, der **somatosensorische Homunkulus**. Eine wichtige Ausnahme ist der
   **Hippocampus**: dort sind Nachbarzellen im Kortex *nicht* notwendig Nachbarn im
   kodierten Raum, und die Zuordnung ändert sich von Umgebung zu Umgebung (flexible,
   wiederverwendbare Kodierung; siehe [[Kognitive Karten und Hippocampus]]).

**Dekodierung** heißt: aus dem Aktivitätsmuster wieder eine Schätzung $\hat{s}$
gewinnen. Der einfachste Weg ist der **Populationsvektor** – ein feuerraten­gewichtetes
Mittel der präferierten Größen. Verschiedene Dekodierverfahren (Populationsvektor,
Maximum-Likelihood, Bayes) haben je typische, in eine bestimmte Richtung verzerrte
Fehler (Pouget, Dayan & Zemel 2003).

## Worked example

Drei Richtungsneuronen mit präferierten Richtungen $s_1=0°$, $s_2=90°$, $s_3=180°$. Ein
Reiz kommt aus $60°$. Angenommen die (normierten) Feuerraten sind $f_1=0{,}3$,
$f_2=0{,}6$, $f_3=0{,}1$. Naiv gemittelt:
$0{,}3\cdot 0° + 0{,}6\cdot 90° + 0{,}1\cdot 180° = 54 + 18 = 72°$ – hier zufällig
plausibel. Läge der Reiz aber nahe $0°/360°$ (z. B. Neuronen bei $350°$ und $10°$), würde
das naive Mitteln der Winkelzahlen $180°$ liefern (genau falsch herum!). Deshalb muss man
bei **zyklischen Größen** die präferierten Richtungen als **Einheitsvektoren** darstellen,
gewichtet aufsummieren und aus dem Summenvektor den Winkel zurückrechnen. Diese
Zyklus-Falle ist eine klassische Prüfungsfrage.

## Formal definition / equations

Dekodierung per Populationsvektor:

$$\hat{s}_{\text{tot}} = \sum_{i=1}^{N} f_i(s)\, s_i$$

- $f_i(s)$: normierte Feuerrate von Neuron $i$ beim Reiz $s$ (Tuning-Antwort).
- $s_i$: präferierte Größe von Neuron $i$; bei Richtungen ein **Einheitsvektor**.
- $\hat{s}_{\text{tot}}$: dekodierte Schätzung.

Bei zyklischen Größen wird $\hat{s}_{\text{tot}}$ als Vektorsumme gebildet und
anschließend in einen Winkel zurücktransformiert; das umgeht den 0°/360°-Sprung.

![[population-code-decoding.pdf]]
*Links: überlappende (rektifizierte Cosinus-)Tuningkurven vieler Neuronen; ein Reiz bei
63° aktiviert mehrere davon unterschiedlich stark (orange Punkte). Rechts: das
Aktivitätsprofil über die präferierten Richtungen bildet eine Verteilung, deren
Vektor-Dekodierung den wahren Reiz zurückgewinnt (63°). Kernaussage: die Information liegt
im Muster über der Population, nicht in einer Einzelzelle.*

## Role in this class or project

Populationscodes sind der **gemeinsame Repräsentationsmechanismus** hinter den
peripersonalen Räumen, der multisensorischen Fusion und den selbstorganisierenden Karten
in [[VL10 Multisensorische Interaktion und Räume]]. Sie liefern die neuronale Basis für
körpergrundierte, unsicherheitsbewusste Raumverarbeitung.

## Exam, assignment, or project relevance

Dekodierung (gewichtetes Mittel), Zyklus-Falle bei Winkeln, und die Verbindung
„Populationsaktivität ≈ Wahrscheinlichkeitsverteilung" (Voraussetzung für Fusion) sind
prüfungsrelevant.

## Related global concepts

[[Encoding and Decoding]], [[Tuning Curve]], [[Neural Coding]].

## Related local pages

[[Multisensorische Informationsfusion]], [[Kognitive Karten und Hippocampus]],
[[Selbstorganisierende neuronale Netze]], [[Optischer Fluss]].

## Common confusions

- **„Ein Neuron = ein Wert"** ist falsch: die Information liegt im *Muster* über der
  Population, nicht in einer einzelnen Zelle.
- **Topographie ist nicht universell.** Retinotopie/Homunkulus sind topographisch, der
  Hippocampus ist es *nicht* – das ist gerade sein Vorteil (flexible Neu­zuordnung pro
  Umgebung).
- **Zyklische vs. lineare Größen** beim Dekodieren nicht verwechseln (Einheitsvektoren
  bei Winkeln).

## Sources

[[VL10 Multisensorische Interaktion und Räume]] (Folien 7–10); Pouget, Dayan & Zemel
(2003), *Inference and computation with population codes*, Annu. Rev. Neurosci. 26,
381–410.
