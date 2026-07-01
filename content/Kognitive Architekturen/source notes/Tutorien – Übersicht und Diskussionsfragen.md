---
type: source_note
status: processed
scope: local
class: Kognitive Architekturen
project:
source_type: tutorial_materials
raw_path: "raw/Tutorien/CogArchTut_1..9.pdf"
created: 2026-06-09
updated: 2026-07-01
---

# Tutorien – Übersicht und Diskussionsfragen

> Konsolidierte Notiz für die neun Tutoriums-PDFs (`raw/Tutorien/CogArchTut_1..9.pdf`).
> Die Tutorien sind bildbasierte Foliensätze des Tutors (Mudar Adas & Laurens Löst)
> und mischen: **Paper-Diskussionsfragen**, **Recaps**, **praktische Aufgaben** und
> Organisatorisches/Feedback. Sie wurden zu PNG gerendert und gelesen.
>
> **Wichtig:** Hier werden nur die *Themen* und die *Diskussionsfragen* festgehalten
> (diese sind hervorragende Lern-/Prüfungsleitfragen). Inhalte der **Übungsblätter**
> bzw. Lösungswege werden bewusst **nicht** übernommen.

## Hochwertiger Fund: Formelsammlung

Tutorium 1 enthält eine **offizielle Formelsammlung** der Vorlesung (Schematheorie,
RL inkl. Eligibility Traces, optischer Fluss, Informations-Fusion, Wahrscheinlichkeit/
Bayes, Varianz/Kovarianz). Sie ist separat aufbereitet:
→ [[Formelsammlung (Tutorium)]].

## Kursfahrplan (aus Tutorium 7)

Tutorium 7 enthält den vollständigen **Semesterplan**: Datum, Vorlesung, Thema,
Diskussionspaper, Übungsblatt und Tutoriumsthema je Woche. Sehr nützlich als Landkarte –
er bestätigt u. a. die Paper-Zuordnung (VL08 ↔ Stevens 2012), die praktischen
Tutoriumsthemen (optischer Fluss, Bayessches Schließen, Informationsfusion,
Kovarianzmatrizen) und den **Klausurtermin 29.07.2026 (18–19 Uhr)**.

![[course-schedule-tut7-p1.png]]
*Semesterfahrplan (Tutorium 7, S. 1): Wochenraster mit Vorlesung, Thema, Paper,
Übungsblatt und Tutoriumsthema – die kompakteste Gesamtübersicht des Kurses.*

## Tutorium-für-Tutorium

### Tutorium 1 — Übung 0 (Dennett & Turing) + Grundlagen
- **Diskussionsfragen zu [[Dennett (1984) Cognitive Wheels The Frame Problem of AI|Dennett]]**:
  Was unterscheidet die drei Roboter R1/R1D1/R2D1? Warum müssen intelligente Agenten
  ihre Handlungen *im Voraus* planen, und wie testet man das? Was bedeutet die
  Metapher „Cognitive Wheels", mit Vor-/Nachteilen?
- **Diskussionsfragen zu [[Turing (1950) Computing Machinery and Intelligence|Turing]]**:
  Warum ersetzt das Imitation Game die Frage „Können Maschinen denken?", und welche
  Grenzen hat es als Test? Welche der neun Einwände überzeugen? Ist der Test angesichts
  von LLMs heute noch gültig?
- **Praktische Aufgaben** (Themen): Verhalten und Konzeption von Braitenberg-Fahrzeugen,
  Braitenberg-Parcours, optischer Fluss (Biene zwischen zwei Wänden / Landung).
  Siehe [[Emergenz und Attraktoren]].
- Illustrationen: ARC-AGI-Aufgabe (Intelligenzdebatte), Braitenberg-Skizzen.

### Tutorium 2 — Übung 1 (Brooks) + Evolutionäre Algorithmen
- **Diskussionsfragen zu [[Brooks (1990) Elephants Dont Play Chess|Brooks]]**:
  Symbol System Hypothesis – was behauptet sie, ist sie „notwendig und hinreichend"?
  Physical Grounding Hypothesis und der Bottom-up-Ansatz; Subsumptionsarchitektur und
  ihre Prinzipien.
- **Aufgabenthemen**: evolutionäre Bit-Strings (Fitness, Selektion, Crossover),
  Take-Over Time, Schematheorie. Siehe [[Evolutionäre Algorithmen]].

### Tutorium 3 — Recap EA + Zwei-Systeme + Übung 2 (Goldberg)
- **Recap**: Schematheorie/Take-Over Time.
- **Aufgabenthema**: Zwei-Systeme-Modell (Objekt-Daten-File vs.
  Interaktionsverarbeitung) am Kollisions-Szenario. Siehe
  [[Kernwissen und Zwei-Systeme-Modell]].
- **Diskussionsfragen zu [[Goldberg (1998) The Race the Hurdle and the Sweet Spot|Goldberg]]**:
  Wie verteilt Selektion Überleben? Wie wirken Selektion/Rekombination/Mutation
  zusammen, und warum ist keiner allein effektiv? Was ist das „Race"?

### Tutorium 4 — Feedback + Übung 3 (Lin) + RL
- **Diskussionsfragen zu [[Lin et al. (2022) Infants Physical Reasoning|Lin et al.]]**:
  Core-Knowledge-Hypothese – Prinzipien vs. Konzepte; wann treten *errors of omission*
  und *commission* auf; Unterschied und Interaktion von OF- und PR-System.
- **Aufgabenthemen**: MDP-Formalisierung & Werteberechnung; Q-Learning-Update;
  Exploration-Exploitation. Siehe [[Reinforcement Learning]].

### Tutorium 5 — Recap RL + RL II (Übung 4)
- Organisatorisches (Raumänderung 22.07.; Discord), Feedback-Auswertung.
- **Recap**: Q-Learning.
- **Aufgabenthemen**: Eligibility Traces (akkumulierende vs. ersetzende Spur);
  hierarchisches RL / 4-Räume-Gridworld. Siehe [[Reinforcement Learning]].

### Tutorium 6 — Recap RL II + Antizipation (Übung 5/Blakemore)
- Organisatorisches/Feedback; Korrektur der Q-Learning-Formel (Klammerung).
- **Recap**: Eligibility Traces (Schritt-für-Schritt), Semi-MDPs.
- **Reafferenzprinzip**-Grafik (Efferenz/Efferenzkopie/Reafferenz/Exafferenz) als
  Brücke zu [[Blakemore et al. (2000) Why cant you tickle yourself|Blakemore]] und
  [[Ideomotorik und Antizipation]].

### Tutorium 7 — Optischer Fluss (Übung 7) + Blakemore-Fragen
- Enthält den **Kursfahrplan** (oben) und die **Blakemore-Begleitfragen** (Forward
  Model: wie unterscheiden Efferenzkopien selbst- von fremdverursachten Reizen; Symptom
  „meine Finger nehmen den Stift, aber ich steuere sie nicht“ = Defizit des
  Vorwärtsmodells; Delay-Experiment erklärt das Nicht-sich-selbst-kitzeln-Können).
- **Aufgabenthema – [[Optischer Fluss]]**: visual translation $v_x,v_y$ an einem
  Bildpunkt berechnen; **Fokusexpansionspunkt** $(-T_x/T_z,-T_y/T_z)$ bestimmen;
  **Zeit bis zur Landung** $t=Z/T_z$ für Insekten. Gehört zu
  [[VL08 Visuelle Wahrnehmung Bottom-Up]].

### Tutorium 8 — Bayessches Schließen (Übung 8)
- **Feedback-Auswertung** (quantitative Bewertungen Vorlesung/Tutorium/Übung/Paper).
- **Formel-Recap**: bedingte/gemeinsame Wahrscheinlichkeit, Faktorisierung
  $p(x_1,\dots,x_n)=\prod_i p(x_i\mid\text{parents}(x_i))$, Bayes-Regel (auch
  konditioniert $p(y\mid x,z)$), Marginalisierung.
- **Recap-Beispiel**: das **Tassen-Netz** $A,B\to O\to C,N$ und die **d-Separation**
  (fork/chain/collider) aus der Vorlesung. Siehe [[Bayes-Netzwerke]].
- **Aufgabenthema – Bayes-Netz „Alarm“**: Einbruch (E) und starker Wind (W) → Alarm (A)
  → Hund bellt (H) / Polizei (P). Teilaufgaben: (Un-)Abhängigkeiten via d-Separation
  bestimmen; $p(E,W,A)$ für alle 8 Kombinationen; $p(A\mid E)$, generelles $p(A)$,
  diagnostisch $p(A\mid H)$. Gehört zu [[VL09 Visuelle Wahrnehmung Top-Down]].

### Tutorium 9 — Informationsfusion (zu VL10)

Reines **Aufgaben-Tutorium** zur multisensorischen [[Multisensorische Informationsfusion|Informationsfusion]]
(keine Paper-Diskussionsfragen). Drei Aufgabentypen – hier nur die **Themen**, keine
Lösungen:

- **Aufgabe 1 – Fusion ohne interne Schätzung**: zwei Quellen (visuell/auditiv). (a) beide
  im selben Referenzraum ($f_i(x)=x$); (b) mit **Mappingfunktionen** in unterschiedlichen
  Einheiten ($f_1(x)=x/5$, $f_2(x)=2x$) – erst Quellen und Varianzen mappen, dann
  fusionieren.
- **Aufgabe 2 – Fusion mit drei Modalitäten und interner Schätzung**: a-priori-Schätzung
  wird als weitere Quelle einbezogen; berechnet werden fusionierte Schätzung $\hat{L}$
  *und* Varianz $\sigma_L^2$.
- **Aufgabe 3 – Fusion über zwei Zeitschritte**: iterative Anwendung mit **Vorwärtsmodell**
  (Projektion $\hat{L}'(t)=\hat{L}(t-1)+f(t)$, $\sigma_L^{2\prime}(t)=\sigma_L^2(t-1)+g(t)$;
  hier ohne zusätzliche Varianzerhöhung, „keine Bewegung erwartet").

Gehört zu [[VL10 Multisensorische Interaktion und Räume]]; die Formeln stehen in
[[Multisensorische Informationsfusion]] und der [[Formelsammlung (Tutorium)]]. Direkter
Klausur-Rechendrill.

## Local relevance

Die Tutorien sind die „praktische" Spiegelung der Vorlesung und der direkte
Prüfungs-Drill (die Klausur hat einen praktischen Teil). Die Diskussionsfragen eignen
sich exzellent als Selbsttest pro Paper.

## Exam or project relevance

Sehr hoch: Die Tutoriumsthemen (EA-Rechnungen, MDP/Q-Learning/Eligibility-Traces-
Berechnungen, Zwei-Systeme-Modell, Reafferenzprinzip) decken sich mit dem praktischen
Klausurteil. Die Diskussionsfragen sind ideale Wiederholungsfragen.

## Links to global concepts

[[Marr's Levels of Analysis]], [[Predictive Coding]], [[Bayesian Inference]].

## Open questions

Tutorien 1–9 sind erfasst (Tut 9 = Informationsfusion zu VL10). Spätere Tutorien (zu
Abstraktion, Aufmerksamkeit, Sprache) liegen noch nicht vor.
