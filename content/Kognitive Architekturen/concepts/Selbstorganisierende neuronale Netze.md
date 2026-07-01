---
type: method
status: active
scope: local
classes: [Kognitive Architekturen]
projects:
domains: [unsupervised learning, self-organization]
sources: ["VL10 Multisensorische Interaktion und Räume"]
created: 2026-07-01
updated: 2026-07-01
---

# Selbstorganisierende neuronale Netze

## Short definition

Unüberwachte, **online lernende** Netze, deren Knoten sich so anordnen, dass sie die
Struktur (das „Manifold") der Eingabedaten abbilden – von starrer Gitterstruktur
(Kohonen/SOM) über frei bewegliche Knoten (Neural Gas) bis zu wachsenden, topologie-
lernenden Netzen (Growing Neural Gas).

## Intuition

Stell dir vor, du streust Reißnägel auf eine Landkarte und ziehst jeden Nagel immer ein
kleines Stück dorthin, wo gerade eine Stadt aufleuchtet. Nach vielen Städten sitzen die
Nägel dicht in besiedelten Regionen und dünn in der Wildnis – die Nägel haben die
*Verteilung* der Städte „gelernt", ohne dass jemand ihnen die Karte gezeigt hat. Genau so
verteilen selbstorganisierende Netze ihre Knoten dorthin, wo die Daten sind.

## Explanation

Gemeinsames Prinzip: Für jeden neuen Eingabepunkt wird der/die **nächstgelegene(n)
Knoten** bestimmt und Richtung Eingabe verschoben (plus, je nach Verfahren, Nachbarn). Das
Netz passt sich **iterativ und online** an, ohne Ziellabels. Drei prominente Varianten,
die die Vorlesung vergleicht:

- **Kohonen-Netz / Self-Organizing Map (SOM).** *Feste* $n$-dimensionale Gitterstruktur
  (kein Knotenwachstum). Der „Gewinnerknoten" und seine Gitternachbarn (Gauß-/Max-
  Nachbarschaft) werden zum Input gezogen. Ergebnis: eine topologie-erhaltende Projektion
  hochdimensionaler Daten auf ein festes Gitter.
- **Neural Gas.** *Freie* Struktur ohne feste Dimensionalität und **ohne Verknüpfungen**.
  Knoten werden nach dem **Rang ihrer Nähe** zum Input verschoben (der nächste am
  stärksten, der zweitnächste weniger usw.). Die Dimensionalität entsteht implizit aus
  den Daten.
- **Growing Neural Gas (GNG, Fritzke 1995).** Wie Neural Gas (rangbasierte Anpassung),
  **plus Verknüpfungen plus Wachstum nach Bedarf**: Zwischen den zwei input-nächsten
  Knoten entsteht eine Kante; überschreitet der akkumulierte Fehler eine Schranke, wird
  ein neuer Knoten eingefügt. GNG lernt so *auch die Topologie* explizit mit.

**Time Growing Neural Gas** (Butz, Reif & Herbort 2008) erweitert GNG um eine **zeitliche
/ sensomotorische** Komponente, um eine **hippocampusähnliche Karte** zu lernen (siehe
[[Kognitive Karten und Hippocampus]]):

- **Knoten** entstehen „on demand" beim Erreichen neuer Umgebungen und repräsentieren
  Orte (rezeptive Felder, [[Populationscodes]]).
- **Kanten** entstehen zwischen *zeitlich nacheinander* besuchten Knoten (zeitliches
  Hebbsches Lernen) und **speichern den Motorvektor**, der den Übergang bewirkt hat.

Auf dieser gelernten Karte wird Verhalten via **model-basiertem RL** erzeugt: ein
aktiviertes Ziel propagiert per Bellman-Gleichung einen **Aktivierungsgradienten** über
die Knoten; an jeder Position zeigt der Gradient (zusammen mit den in den Kanten
gespeicherten Motorvektoren) den besten nächsten Schritt. So entsteht flexible,
zielgerichtete Navigation – demonstriert an einem Agenten mit acht Distanzsensoren, der
ein Labyrinth (inkl. Teleportern) kartiert und Ziele effizient erreicht.

## Worked example

GNG in einem 2D-Gebiet: Punkte werden zufällig im schattierten Bereich erzeugt. Anfangs
zwei Knoten. Bei jedem Punkt: nächsten und zweitnächsten Knoten finden, Kante zwischen
ihnen setzen, nächsten Knoten (und seine Kanten-Nachbarn) Richtung Punkt ziehen,
Fehlerzähler des nächsten Knotens erhöhen. Periodisch: am Knoten mit dem größten
akkumulierten Fehler einen neuen Knoten einfügen. Nach vielen Punkten überzieht ein
Knoten-Kanten-Netz genau die Form des schattierten Gebiets – das Netz hat dessen Topologie
gelernt. (Kohonen würde dieselbe Punktwolke auf ein *festes* Gitter abbilden, Neural Gas
ohne Kanten.)

## Formal definition / equations

Diese Seite ist konzeptuell; die genutzte Formalik ist die Karten-Auswertung per
model-basiertem RL. Kern ist die Bellman-Aktualisierung
$V(s)=\max_a\big[r(s,a)+\gamma\,V(s')\big]$, mit Diskontfaktor $\gamma$, deren Größen in
[[Reinforcement Learning]] definiert und hergeleitet sind. Der resultierende
$V$-Gradient über die GNG-Knoten liefert die Bewegungsrichtung.

## Role in this class or project

Vierter Baustein von [[VL10 Multisensorische Interaktion und Räume]]: der *Lern-*
Mechanismus, mit dem eine kognitive Karte selbstorganisierend entsteht – die
konstruktive Antwort auf „Wie kommt die Karte in den Kopf?".

## Exam, assignment, or project relevance

**Vergleich SOM ↔ Neural Gas ↔ GNG** entlang: feste vs. freie Struktur, mit/ohne Kanten,
mit/ohne Wachstum, Topologie-Lernen. Time-GNG: Rolle von Knoten (Orte) und Kanten
(Motorvektoren) und die Kopplung mit model-basiertem RL/Bellman.

## Related global concepts

[[Reinforcement Learning]] (model-basierte Planung auf der Karte),
[[Encoding and Decoding]] (rezeptive Felder/Populationskodierung der Knoten).

## Related local pages

[[Kognitive Karten und Hippocampus]], [[Populationscodes]],
[[Multisensorische Informationsfusion]].

## Common confusions

- **SOM ≠ Neural Gas ≠ GNG.** Häufigster Fehler: nur „selbstorganisierend" zu sagen. Die
  Klausur will die Unterschiede (Struktur/Kanten/Wachstum).
- **GNG-Wachstum ist fehlergetrieben**, nicht zeitgetrieben: Knoten kommen dort dazu, wo
  der Repräsentationsfehler hoch ist.
- **Time-GNG-Kanten sind gerichtet und tragen Motorinformation** – sie sind nicht bloße
  Nachbarschaftslinks, sondern die Grundlage der Bewegungsauswahl.

## Sources

[[VL10 Multisensorische Interaktion und Räume]] (Folien 27–36); Fritzke (1995), *A
growing neural gas network learns topologies*; Butz, Reif & Herbort (2008), *Bridging the
Gap: Learning Sensorimotor-Linked Population Codes for Planning and Motor Control*, ICCS.
