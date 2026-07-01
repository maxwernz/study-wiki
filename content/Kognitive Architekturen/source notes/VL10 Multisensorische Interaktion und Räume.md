---
type: source_note
status: processed
scope: local
class: Kognitive Architekturen
project:
source_type: lecture_slides
raw_path: "raw/VL Folien/KogArch_10_MultisensorischeInteraktionUndRaeume.pdf"
created: 2026-07-01
updated: 2026-07-01
---

# VL10 – Multisensorische Interaktion & Räume

## Summary

Die Vorlesung fragt: **Wie repräsentiert das Gehirn den Raum, und wie fusioniert es
mehrere Sinnesquellen zu einer robusten, handlungsleitenden Schätzung?** Die zentrale
These lautet: Der Geist hält den Raum **redundant** in vielen verschiedenen
**Referenzrahmen** gleichzeitig vor (körperzentriert, augenzentriert, umwelt-relativ) und
kann so hochflexibel und zielgerichtet handeln. Kein einzelner „Weltkoordinaten"-Raum,
sondern viele überlappende, aufgabenangepasste Karten.

Vier Bausteine tragen die Vorlesung:

1. **Peripersonale Räume** – körpernahe Räume (um Hand, Arm, Gesicht), die taktile,
   visuelle und motorische Information integrieren und *Erreichbarkeit* und *Relevanz*
   (z. B. Gefahr) kodieren.
2. **Populationscodes** – der neuronale Repräsentationsmechanismus: viele Neuronen mit
   überlappenden rezeptiven Feldern kodieren gemeinsam eine räumliche Größe *und* deren
   Unsicherheit; sie approximieren eine Wahrscheinlichkeitsverteilung.
3. **Multisensorische Informationsfusion** – wie unabhängige Sinnesquellen
   **Bayes-optimal** (per inverser Varianz gewichtet) und über die Zeit (mittels
   Vorwärtsmodell) kombiniert werden.
4. **Kognitive Karten & Hippocampus** – allozentrische (umwelt-relative)
   Raum- und Ereignisrepräsentationen; und ein konkretes Modell (Time Growing Neural
   Gas), das eine hippocampusähnliche Karte selbstorganisierend *erlernt* und via
   model-basiertem RL für zielgerichtetes Verhalten nutzt.

Roter Faden: **Wahrnehmung, Handlung und Gedächtnis teilen sich dieselben
raum-repräsentierenden Mechanismen.** Fusion dient nicht nur der Perzeption, sondern wird
**antizipativ** schon *vor* der Handlung eingesetzt, um zukünftige kritische Situationen
vorzubereiten.

## Key points

- Raum wird in **mehreren Referenzrahmen redundant** repräsentiert: direktionale Felder,
  körperrelative Felder, allozentrische (umwelt-relative) Karten. Redundanz = Robustheit
  und Flexibilität.
- **Peripersonaler Raum** = körpernaher Interaktionsraum. Je Körperteil ein Paar aus
  einer **intraparietalen** und einer **prämotorischen** Region (Arm/Hand: AIP & F4/PMVc;
  Gesicht: VIP & PZ). Rezeptive Felder reagieren auf Berührung, Blickfokus und
  Objektnähe – also *pro-aktiv* auf mögliche Interaktionen, nicht nur reaktiv auf Reize.
- Stimulationsbefunde (Graziano 2006; Desmurget et al. 2009): Reizung im Motor-/
  Prämotorkortex löst *typische Zielstellungen* der Hand bzw. unbemerkte Bewegungs-
  ausführung aus; Reizung im Parietalkortex erzeugt eine *Bewegungsintention*. Der Raum
  ist also aktions- und zielkodiert.
- **Populationscode**: Jedes Neuron hat ein rezeptives Feld (z. B. rektifizierter
  Cosinus über der präferierten Richtung); überlappende Aktivitäten kodieren zusammen
  eine Verortung *und* die Sicherheit. Neuronale Nähe ≈ räumliche Nähe (retinotope Karte,
  somatosensorischer Homunkulus) – **außer im Hippocampus**.
- **Dekodierung** eines Populationscodes: gewichtetes Mittel der präferierten Richtungen
  $\hat{s}=\sum_i f_i(s)\,s_i$; bei zyklischen Größen (Winkel) **Umweg über
  Einheitsvektoren**, sonst systematische Fehler.
- **Bayes-optimale Fusion**: unabhängige Ortsschätzungen werden mit ihrer **inversen
  Varianz** (Präzision) gewichtet gemittelt → präzisere Schätzung als jede Einzelquelle.
- **Zeitliche Integration** braucht ein **Vorwärtsmodell** $g$: Es projiziert Schätzung
  und Unsicherheit in den nächsten Zeitschritt (a-priori-Schätzung) und **erhöht dabei
  die Unsicherheit**. Wird die Unsicherheit unterschätzt → Illusionen/Halluzinationen.
- **Gain-Field-Neuronen** (posteriorer Parietalkortex) multiplizieren zwei
  Informationsquellen (z. B. Körperstellung × Retinotopie) und überführen sie in einen
  dritten Referenzrahmen (hand-relativ). Vermuteter neuronaler Mechanismus der
  Referenzrahmen-Transformation.
- **Antizipative Raumkodierung** (Belardinelli et al. 2018, „Mental space maps into the
  future"): Der peripersonale Handraum wird *aufgabenspezifisch in die Zukunft projiziert*
  – schon *bevor* die Bewegung ausgeführt wird. Nachweis über cross-modalen
  Kongruenzeffekt und Augenfixation.
- **Hippocampus**: Aufbau **episodischen Gedächtnisses**; **place cells** (Orte),
  **head-direction cells** (globale Richtung), **view cells** (Blick zu Landmarke). Kodiert
  allgemeine **raum-zeitliche** Zusammenhänge und **Ereignisepisoden** → Brücke zur
  ereignis-prädiktiven Kognition und zu Reflektion/hypothetischem Denken.
- **Selbstorganisierende neuronale Netze** (SOM/Kohonen, Neural Gas, Growing Neural Gas)
  können solche Karten **online erlernen**. Butz' **Time Growing Neural Gas** baut eine
  sensomotorische Karte auf (Knoten = Orte, Kanten speichern Motorvektoren) und erzeugt
  über **model-basiertes RL** (Bellman-Gleichung) einen Aktivierungsgradienten für
  zielgerichtetes Verhalten.

## Important concepts

- [[Populationscodes]] (volle Tiefe) – Kodierung/Dekodierung, rezeptive Felder, Bezug
  zu Wahrscheinlichkeitsverteilungen und Bayes.
- [[Multisensorische Informationsfusion]] (volle Tiefe) – inverse-Varianz-Gewichtung,
  Mappingfunktionen, zeitliche Integration mit Vorwärtsmodell, Voraussetzungen.
- [[Kognitive Karten und Hippocampus]] (volle Tiefe) – place/head-direction/view cells,
  allozentrische Karten, Ereignisgedächtnis.
- [[Selbstorganisierende neuronale Netze]] (volle Tiefe) – SOM, Neural Gas, Growing
  Neural Gas, Time-GNG als Kartenlern-Mechanismus.
- Kandidatenbegriffe (als Klartext, keine eigene Seite): peripersonaler Raum, Körperschema,
  Referenzrahmen, gain-field Neuronen, direktionale/körperrelative/allozentrische Felder,
  McGurk-Effekt, Spiegelneuronen, sharp waves, Theta-Rhythmus, POMDP, Kalman-Filter.

## Methods, models, or theories

**Populationskodierung/-dekodierung.** *Was:* Repräsentation einer kontinuierlichen Größe
durch die verteilte Aktivität vieler grob getunter Neuronen. *Wie:* Jedes Neuron $i$
feuert gemäß seiner Tuningkurve $f_i(s)$ am stärksten nahe seiner präferierten Größe
$s_i$; die Population als Ganzes approximiert eine Wahrscheinlichkeitsverteilung über $s$.
*Wann:* immer, wenn Unsicherheit, Wettbewerb konkurrierender Stimuli oder Verteilungen
mitrepräsentiert werden sollen. Siehe [[Populationscodes]].

**Bayes-optimale Informationsfusion.** *Was:* Kombination mehrerer unabhängiger,
verrauschter Schätzungen derselben Größe zu einer optimalen Schätzung. *Wie:* jede
Quelle wird mit ihrer Präzision (inverse Varianz) gewichtet; Quellen werden per
Mappingfunktion $f_i$ in einen gemeinsamen Referenzrahmen projiziert. Über die Zeit sorgt
ein Vorwärtsmodell für die a-priori-Schätzung. *Wann:* multisensorische Wahrnehmung,
Objekterkennung, Sensor-Fusion. Siehe [[Multisensorische Informationsfusion]].

**Time Growing Neural Gas (Butz, Reif & Herbort 2008).** *Was:* selbstorganisierendes,
wachsendes Netz, das eine sensomotorisch verankerte, hippocampusähnliche Karte lernt.
*Wie:* Knoten entstehen „on demand" beim Erreichen neuer Umgebungsteile (rezeptive
Felder = Orte); Kanten entstehen zwischen zeitlich aufeinanderfolgend besuchten Knoten
(zeitliches Hebbsches Lernen) und speichern den zugehörigen Motorvektor. Zielgerichtetes
Verhalten via **model-basiertem RL** (Bellman-Gleichung liefert Aktivierungsgradienten).
*Wann:* Kartenaufbau, Navigation, Planung. Siehe [[Selbstorganisierende neuronale Netze]]
und [[Reinforcement Learning]].

## Equations or formal definitions

**1) Dekodierung eines Populationscodes (Populationsvektor).** Die geschätzte Größe ist
das mit den Feuerraten gewichtete Mittel der präferierten Größen der Neuronen:

$$\hat{s}_{\text{tot}} = \sum_{i=1}^{N} f_i(s)\, s_i$$

- $\hat{s}_{\text{tot}}$: dekodierte Schätzung (z. B. Richtung, Ort).
- $f_i(s)$: normierte Feuerrate / Tuning-Antwort von Neuron $i$ auf den Reiz $s$
  (z. B. rektifizierter Cosinus über dem Winkel zwischen $s$ und der präferierten
  Richtung).
- $s_i$: präferierte Größe von Neuron $i$ (bei Richtungen: Einheitsvektor).
- *In Worten:* „Frage jedes Neuron, wie stark es feuert, und mittle die von ihm
  bevorzugten Richtungen mit diesem Gewicht." **Vorsicht bei zyklischen Größen (0°/360°):**
  nur die Vektorsumme der Einheitsvektoren liefert das korrekte Ergebnis; ein naives
  Mitteln der Winkelzahlen erzeugt systematische Fehler.

**2) Multisensorische Fusion mehrerer Ortsquellen (ohne interne a-priori-Schätzung).**

$$\hat{L}(t) = \frac{\displaystyle\sum_{i\in I} \frac{f_i(s_i(t))}{f_i(\sigma_i^2(t))}}
{\displaystyle\sum_{j\in I} \frac{1}{f_j(\sigma_j^2(t))}}$$

- $\hat{L}(t)$: fusionierte a-posteriori-Ortsschätzung im gemeinsamen Referenzrahmen $L$.
- $s_i(t)$: Rohschätzung der Quelle $i$; $\sigma_i^2(t)$: deren Varianz (Unsicherheit).
- $f_i$: Mappingfunktion, die Quelle $i$ in den gemeinsamen Referenzrahmen projiziert
  (z. B. $f(x)=x/5$ oder $f(x)=2x$ bei unterschiedlichen Einheiten).
- $\tfrac{1}{f_i(\sigma_i^2)}$: **Präzision** (inverse Varianz) der Quelle im gemeinsamen
  Raum – das Gewicht der Quelle.
- *In Worten:* präzisionsgewichtetes Mittel; sichere Quellen (kleine Varianz) zählen mehr.
  Der Nenner normiert die Gewichte. Dies ist genau die in **Tutorium 9** geübte Formel.

**3) Fusion mit interner a-priori-Schätzung (aus dem Vorwärtsmodell).** Die zeitlich
propagierte Schätzung $\hat{L}'(t)$ mit Varianz $\sigma_L^{2\prime}(t)$ wird wie eine
weitere Quelle einbezogen:

$$\hat{L}(t)=\frac{\dfrac{\hat{L}'(t)}{\sigma_L^{2\prime}(t)}+\displaystyle\sum_{i\in I}\dfrac{f_i(s_i(t))}{f_i(\sigma_i^2(t))}}
{\dfrac{1}{\sigma_L^{2\prime}(t)}+\displaystyle\sum_{j\in I}\dfrac{1}{f_j(\sigma_j^2(t))}}
\qquad
\sigma_L^{2}(t)=\frac{1}{\dfrac{1}{\sigma_L^{2\prime}(t)}+\displaystyle\sum_{i\in I}\dfrac{1}{f_i(\sigma_i^2(t))}}$$

- Die fusionierte **Varianz** ist der Kehrwert der Summe aller Präzisionen: mehr Quellen
  → kleinere Varianz → sicherere Schätzung. Das ist die Kernaussage der Präzisions-
  gewichtung.

**4) Zeitliche Projektion (Vorwärtsmodell $g$).** Zwischen zwei Zeitschritten wird die
a-priori-Schätzung fortgeschrieben:

$$\hat{L}'(t)=\hat{L}(t-1)+g_f(t), \qquad
\sigma_L^{2\prime}(t)=\sigma_L^{2}(t-1)+g_\sigma(t)$$

- $g_f$: vom Vorwärtsmodell vorhergesagte Änderung der Ortsschätzung (aus Motorsignalen $M$).
- $g_\sigma$: Zuwachs der Unsicherheit (motorische Unsicherheit + Kodierungsunsicherheit).
- *In Worten:* „Sag mit dem Bewegungswissen voraus, wo das Objekt als Nächstes ist – und
  gib zu, dass du dabei unsicherer wirst." Erwartet das interne Modell **keine Bewegung**,
  ist $g_f=0$ und (je nach Aufgabe) $g_\sigma=0$; die alte Schätzung wird nur weiter-
  getragen. **Exakt** ist die ganze Rechnung, wenn alle Quellen Gauß-verteilt sind und die
  Mappingfunktionen die Gauß-Form erhalten (Stichwort **conjugate prior**: a-priori und
  a-posteriori aus derselben Verteilungsfamilie).

## Local relevance

Diese Vorlesung bündelt und formalisiert Fäden aus dem ganzen Semester:

- Sie liefert den **neuronalen Repräsentationsmechanismus** (Populationscodes) hinter der
  körpergrundierten Kognition ([[Körpergrundierte Kognition]]) und dem peripersonalen
  Raum.
- Die **Bayes-Fusion** knüpft direkt an [[Bayes-Netzwerke]],
  [[Generative und diskriminative Modelle]] und [[Gaußsche Mischmodelle]] (multivariate
  Gauß, Kovarianz) an – jetzt in der Anwendung auf sensorische Integration.
- Das **Vorwärtsmodell** verbindet die Fusion mit [[Ideomotorik und Antizipation]]
  (Reafferenzprinzip, antizipative Verhaltenskontrolle).
- Das **Kartenlernmodell** verwendet [[Reinforcement Learning]] (model-basiert,
  Bellman-Gleichung) und schlägt die Brücke zum Hippocampus.
- Der Hippocampus-Teil (Ereignisepisoden, ereignis-prädiktive Kognition) ist die direkte
  theoretische Klammer zum Diskussionspaper [[Zacks (2020) Event Perception and Memory]] –
  inklusive Butz' eigenem Modell **REPRISE**, das Zacks explizit bespricht.

## Exam or project relevance

Sehr hoch und **rechenlastig**. Klausur-typische Aufgaben (vgl. **Tutorium 9**):

- **Informationsfusion berechnen** – mit und ohne Mappingfunktionen $f_i$, mit und ohne
  interne a-priori-Schätzung, über mehrere Zeitschritte (Vorwärtsmodell). Fusionierte
  Schätzung *und* fusionierte Varianz angeben.
- **Populationscode dekodieren** – gewichtetes Mittel; Fallstrick zyklischer Winkel
  (Einheitsvektoren).
- **Konzeptfragen**: Warum redundante Referenzrahmen? Was leisten gain-field Neuronen?
  Warum darf die Unsicherheit im Vorwärtsmodell nicht unterschätzt werden (Illusionen)?
  Rolle des Hippocampus über reine Ortskodierung hinaus.
- Vergleich **SOM vs. Neural Gas vs. Growing Neural Gas** (Struktur, Wachstum,
  Topologie).

## Links to global concepts

[[Encoding and Decoding]] · [[Tuning Curve]] · [[Neural Coding]] (Populationscodes);
[[Bayesian Inference]] · [[Bayes' Theorem]] (Fusion); [[Predictive Coding]]
(Vorwärtsmodell/Antizipation); [[Reinforcement Learning]] (model-basierte Planung auf der
Karte).

## Open questions

- Wie genau realisiert das Gehirn die Referenzrahmen-Transformation? Gain-field Neuronen
  sind ein Kandidat, der Mechanismus ist aber offen (Folie 14).
- Wie werden die selektiv aktivierbaren Mappings *zwischen* Populationscodes gelernt? Die
  Vorlesung verschiebt das auf die spätere VL „Aufmerksamkeit".
- Herausforderungen des Kartenmodells: POMDPs, Dynamik (Trägheit), Zeitverzögerungen,
  Integration antizipativer Quellen (Folie 36) – noch ungelöst.
- Folien 8/9/12/13 enthalten im PDF **vergarbelte Formelsatz-Fragmente** (Textextraktion
  unbrauchbar); die Gleichungen oben wurden aus dem Kontext und Tutorium 9 rekonstruiert
  und sollten bei Gelegenheit gegen die Originalfolien geprüft werden.
