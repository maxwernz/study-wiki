---
type: concept
status: active
scope: local
classes: [Kognitive Architekturen]
projects:
domains: [spatial cognition, episodic memory]
sources: ["VL10 Multisensorische Interaktion und Räume"]
created: 2026-07-01
updated: 2026-07-01
---

# Kognitive Karten und Hippocampus

## Short definition

Eine **kognitive Karte** ist eine allozentrische (umwelt-relative) interne Repräsentation
von Raum – und, weiter gefasst, von raum-zeitlichen Zusammenhängen und Ereignissen. Der
**Hippocampus** ist die Hirnstruktur, die solche Karten und das episodische Gedächtnis
aufbaut.

## Intuition

Wenn du an dein Zuhause denkst, siehst du keine Fotoreihe von deinem Blickwinkel, sondern
eine „Landkarte von oben": wo die Küche relativ zum Bad liegt, unabhängig davon, wo du
gerade stehst. Das ist eine **allozentrische** Karte (welt-bezogen), im Gegensatz zu einer
**egozentrischen** Sicht (was gerade vor *mir* ist). Der Hippocampus baut solche Karten –
und er tut mehr: Er verknüpft Orte mit *Ereignissen* über die Zeit, sodass ein Ort eine
ganze Episode zurückrufen kann („hier habe ich gestern …").

## Explanation

Der Hippocampus ist zentral für den Aufbau **episodischer** Gedächtnisstrukturen. Mehrere
spezialisierte Zelltypen kodieren Raum:

- **Place cells** – feuern, wenn das Tier sich an einem bestimmten Ort befindet (kodieren
  Gebiete im Raum).
- **Head-direction cells** – kodieren die globale Blick-/Kopfrichtung, wie ein interner
  Kompass.
- **View cells** – kodieren die Blickrichtung zu einer markanten Lokation/einem Objekt.

Anders als retinotope oder somatosensorische Karten ist die hippocampale Kodierung **nicht
topographisch**: benachbarte Zellen kodieren nicht zwingend benachbarte Orte, und die
Zuordnung ändert sich von Umgebung zu Umgebung. Das macht sie zu einer **flexiblen,
wiederverwendbaren** Kodierung (dasselbe Neuronenensemble kann in verschiedenen Kontexten
neu „gemappt" werden). Vgl. [[Populationscodes]], wo diese Ausnahme betont wird.

Die Feuereigenschaften verraten eine Rolle in der **Verhaltensplanung**, nicht nur im
Erinnern:

- Vorwärts- und rückwärts gerichtete **sharp waves** „spielen" zukünftige und vergangene
  Wege durch (mentales Vorausschauen/Zurückblicken).
- Die Verschiebung der mittleren Feuerrate im **Theta-Rhythmus** (Phasenpräzession)
  kodiert Annäherung an oder Entfernung vom Feuerfeld.
- Zellen kodieren teils den *geplanten* oder bereits *gegangenen* Weg und feuern in
  **Antizipation** eines interessanten Zielstimulus.

Neuere Sicht: Der Hippocampus kodiert **allgemeine raum-zeitliche Zusammenhänge** – nicht
nur Orte, sondern **Ereignisse über die Zeit**, die Referenzrahmen, in denen sie
stattfinden, und Kontextinformation. Er kodiert **Ereignisepisoden** und steht damit in
enger Relation zur **ereignis-prädiktiven Kognition**. Dadurch unterstützt er nicht nur
Enkodierung/Erinnerung des Erlebten, sondern auch **Reflektion, hypothetisches und
kontrafaktisches Denken, Träumen**. Dieser Ereignis-Bezug ist die direkte Brücke zum
Diskussionspaper [[Zacks (2020) Event Perception and Memory]] (Ereignissegmentierung,
Aktualisierung an Ereignisgrenzen, medialer Temporallappen).

## Worked example

Ein Roboter/Tier erkundet ein Labyrinth. Immer wenn es einen neuen Bereich erreicht,
entsteht eine neue *place-cell-artige* Repräsentation dieses Ortes; läuft es von Ort A
nach B, wird eine gerichtete Verknüpfung A→B gebildet, die auch den ausgeführten
Bewegungsvektor speichert. Nach einiger Exploration existiert ein Graph aus Orten und
begehbaren Übergängen. Aktiviert man nun ein **Ziel**, kann dessen „Wert" entlang der
Kanten rückwärts propagiert werden (model-basiertes RL, Bellman-Gleichung) und liefert an
jedem Ort den besten nächsten Schritt. Genau dieses Prinzip realisiert Butz' Time Growing
Neural Gas – siehe [[Selbstorganisierende neuronale Netze]].

## Formal definition / equations

Diese Seite ist qualitativ; die formale Seite liegt bei der Karten-*Nutzung*: Zielwerte
werden über model-basiertes RL propagiert, z. B. per Bellman-Gleichung
$V(s)=\max_a\big[r(s,a)+\gamma\,V(s')\big]$ (Symbole und Herleitung in
[[Reinforcement Learning]]). Der Aktivierungsgradient über die Karte liefert dann die
Bewegungsrichtung.

## Role in this class or project

Dritter Baustein von [[VL10 Multisensorische Interaktion und Räume]]: der Übergang von
körpernahen (peripersonalen) zu **allozentrischen** Räumen und die Verbindung von Raum,
Gedächtnis und Ereignis. Verbindet die Vorlesung mit dem Ereignis-Paper und mit der
Verhaltenskontrolle.

## Exam, assignment, or project relevance

Zelltypen (place/head-direction/view) und ihre Funktion; warum die Hippocampus-Kodierung
*nicht* topographisch ist; „Hippocampus kodiert mehr als Orte" (Ereignisse, Kontext,
hypothetisches Denken). Verknüpfung zu ereignis-prädiktiver Kognition (Zacks/REPRISE).

## Related global concepts

[[Reinforcement Learning]] (model-basierte Nutzung der Karte), [[Predictive Coding]]
(antizipatives Vorausspielen).

## Related local pages

[[Selbstorganisierende neuronale Netze]], [[Populationscodes]],
[[Zacks (2020) Event Perception and Memory]], [[Ideomotorik und Antizipation]].

## Common confusions

- **Allozentrisch vs. egozentrisch** nicht verwechseln: kognitive Karten sind
  welt-bezogen (Karte von oben), nicht blickpunkt-bezogen.
- **Hippocampus ≠ nur GPS.** Er kodiert Ereignisse und Zeit, nicht bloß Orte; „place
  cells" sind nur ein Teil der Geschichte.
- **Nicht topographisch:** anders als V1/S1 spiegelt die räumliche Anordnung der Zellen
  nicht die des kodierten Raums – das ist Absicht (Flexibilität), kein Mangel.

## Sources

[[VL10 Multisensorische Interaktion und Räume]] (Folien 22–25).
