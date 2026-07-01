---
type: method
status: active
scope: local
classes: [Kognitive Architekturen]
projects:
domains: [Bayesian inference, multisensory integration]
sources: ["VL10 Multisensorische Interaktion und Räume", "Tutorien – Übersicht und Diskussionsfragen"]
created: 2026-07-01
updated: 2026-07-01
---

# Multisensorische Informationsfusion

## Short definition

Das **präzisionsgewichtete (Bayes-optimale) Kombinieren** mehrerer unabhängiger,
verrauschter Schätzungen derselben Größe zu einer einzigen Schätzung, die *präziser* ist
als jede Einzelquelle – wobei sichere Quellen (kleine Varianz) stärker zählen.

## Intuition

Zwei Freunde schätzen die Entfernung eines Autos: der eine hat scharfe Augen (sehr
sicher), der andere ist kurzsichtig (unsicher). Du glaubst natürlich mehr dem
Scharfsichtigen – aber du ignorierst den anderen nicht ganz. Optimal ist ein
**gewichteter Mittelwert**, bei dem das Gewicht die *Sicherheit* jeder Person ist. Und:
Zwei Meinungen zusammen sind sicherer als jede einzelne. Genau das macht das Gehirn mit
Auge, Ohr, Tastsinn – es gewichtet jede Modalität nach ihrer Zuverlässigkeit.

## Explanation

Meist stehen mehrere Informationsquellen bereit, um *wo* und *was* etwas ist (Sehen,
Hören, Tasten, …). Sind diese Quellen (näherungsweise) **unabhängig**, lassen sie sich
**Bayesianisch optimal** fusionieren. Der Schlüsselbegriff ist **Präzision** = inverse
Varianz $1/\sigma^2$: Sie misst, wie sicher eine Quelle ist. Die fusionierte Schätzung ist
das mit den Präzisionen gewichtete Mittel der Einzelschätzungen; die fusionierte
**Varianz** ist der Kehrwert der Summe aller Präzisionen – d. h. mehr Quellen ergeben
immer eine kleinere Varianz (mehr Sicherheit).

Zwei praktische Komplikationen behandelt die Vorlesung:

1. **Unterschiedliche Referenzrahmen/Einheiten.** Bevor man Quellen kombiniert, muss man
   sie per **Mappingfunktion** $f_i$ in einen gemeinsamen Raum $L$ projizieren (z. B. cm
   in eine neuronale Skala, retinale in körperrelative Koordinaten). Diese Mappings
   müssen auch die *Varianzen* transformieren und hängen von der aktuellen Körperstellung
   ab (**posturales Körperschema**). Neuronaler Kandidat: **gain-field Neuronen** im
   posterioren Parietalkortex, die zwei Quellen *multiplikativ* in einen dritten
   Referenzrahmen überführen.

2. **Integration über die Zeit.** Ortsschätzungen sollen über Zeit erhalten bleiben. Ein
   **Vorwärtsmodell** $g$ projiziert die letzte Schätzung anhand der Motorsignale in den
   nächsten Zeitschritt und liefert so eine **a-priori-Schätzung**, die als (fast)
   unabhängige zusätzliche Quelle in die Fusion eingeht. Entscheidend: die **Unsicherheit
   muss dabei wachsen** ($\sigma$ erhöhen), sonst überschätzt das System seine Sicherheit
   und es entstehen **Illusionen/Halluzinationen**. Erwartet das interne Modell keine
   Bewegung, wird die alte Schätzung unverändert weitergetragen.

Die Rechnung ist **exakt**, wenn (a) alle Quellen Gauß-verteilt sind und (b) die
Mappingfunktionen die Gauß-Form erhalten. Bleibt beim Bayes-Update die Verteilungsfamilie
gleich (Gauß → Gauß), spricht man von einem **conjugate prior**.

## Worked example

Aus **Tutorium 9, Aufgabe 1a** (beide Quellen im selben Referenzraum, $f_i(x)=x$):
visuell $s_1=30$, $\sigma_1^2=2$; auditiv $s_2=10$, $\sigma_2^2=8$. Präzisionen:
$1/2=0{,}5$ und $1/8=0{,}125$.

$$\hat{L}=\frac{\frac{30}{2}+\frac{10}{8}}{\frac{1}{2}+\frac{1}{8}}
=\frac{15+1{,}25}{0{,}625}=\frac{16{,}25}{0{,}625}=26$$

Die Fusion liegt bei $26$ – deutlich näher an der **sichereren** visuellen Quelle ($30$)
als an der unsicheren auditiven ($10$), aber nicht ganz bei $30$. Die fusionierte Varianz
wäre $\sigma_L^2=1/(0{,}5+0{,}125)=1{,}6$ – **kleiner als die beste Einzelvarianz** ($2$),
also sicherer als jede Quelle allein.

Mit **Mappingfunktion** (Aufgabe 1b) rechnet man zuerst $f_i(s_i)$ und $f_i(\sigma_i^2)$
und setzt dann dieselbe Formel an. Über **mehrere Zeitschritte** (Aufgabe 3) fusioniert
man erst die einkommenden Quellen, projiziert das Ergebnis per Vorwärtsmodell auf den
nächsten Schritt (a-priori) und fusioniert dort erneut.

## Formal definition / equations

Fusion **ohne** interne a-priori-Schätzung:

$$\hat{L}(t) = \frac{\sum_{i\in I} \dfrac{f_i(s_i(t))}{f_i(\sigma_i^2(t))}}
{\sum_{j\in I} \dfrac{1}{f_j(\sigma_j^2(t))}}$$

Fusion **mit** interner a-priori-Schätzung $\hat{L}'(t)$ (Varianz $\sigma_L^{2\prime}$):

$$\hat{L}(t)=\frac{\dfrac{\hat{L}'(t)}{\sigma_L^{2\prime}(t)}+\sum_{i\in I}\dfrac{f_i(s_i(t))}{f_i(\sigma_i^2(t))}}
{\dfrac{1}{\sigma_L^{2\prime}(t)}+\sum_{j\in I}\dfrac{1}{f_j(\sigma_j^2(t))}}
\qquad
\sigma_L^{2}(t)=\frac{1}{\dfrac{1}{\sigma_L^{2\prime}(t)}+\sum_{i\in I}\dfrac{1}{f_i(\sigma_i^2(t))}}$$

Zeitliche Projektion (Vorwärtsmodell): $\hat{L}'(t)=\hat{L}(t-1)+g_f(t)$ und
$\sigma_L^{2\prime}(t)=\sigma_L^{2}(t-1)+g_\sigma(t)$.

- $s_i,\sigma_i^2$: Rohschätzung und Varianz der Quelle $i$; $f_i$: Mappingfunktion;
  $1/f_i(\sigma_i^2)$: Präzision (Gewicht). $g_f,g_\sigma$: vorhergesagte Änderung von
  Schätzung bzw. Unsicherheitszuwachs.

![[inverse-variance-fusion.pdf]]
*Zwei Gauß-Quellen (visuell, präzise; auditiv, unsicher) und ihre präzisionsgewichtete
Fusion: die kombinierte Verteilung ist schmaler (sicherer) als beide Quellen und liegt
näher an der präziseren – die Kernaussage der Bayes-Fusion.*

## Role in this class or project

Formaler Kern der zweiten Hälfte von [[VL10 Multisensorische Interaktion und Räume]] und
das rechnerische Rückgrat von **Tutorium 9**. Baut auf [[Populationscodes]] auf (diese
liefern die zu fusionierenden Verteilungen) und auf [[Ideomotorik und Antizipation]] (das
Vorwärtsmodell).

## Exam, assignment, or project relevance

**Kernrechenaufgabe der Klausur.** Muss sicher beherrscht werden: Fusion mit/ohne
Mapping, mit/ohne a-priori-Schätzung, über mehrere Zeitschritte; immer Schätzung *und*
Varianz. Konzeptuell: Warum wächst die Unsicherheit im Vorwärtsmodell (Illusionsgefahr)?
Was ist ein conjugate prior?

## Related global concepts

[[Bayesian Inference]], [[Bayes' Theorem]], [[Gaussian Mixture Model]] (multivariate
Gauß/Kovarianz). **Promotionskandidat:** „Bayesian Cue Integration / inverse-variance
weighting" ist domänenübergreifend (Wahrnehmung, Sensorfusion, Kalman-Filter) und wäre
eine sinnvolle Globalseite bei „sync globally".

## Related local pages

[[Populationscodes]], [[Ideomotorik und Antizipation]], [[Bayes-Netzwerke]],
[[Gaußsche Mischmodelle]], [[Formelsammlung (Tutorium)]].

## Common confusions

- **Gewicht = Varianz?** Nein – das Gewicht ist die **inverse** Varianz (Präzision).
  Kleine Varianz → großes Gewicht.
- **Fusion verschlechtert nie.** Die fusionierte Varianz ist immer ≤ der kleinsten
  Einzelvarianz; Hinzunahme einer weiteren Quelle kann die Sicherheit nur erhöhen.
- **Mapping der Varianz nicht vergessen.** Bei $f_i\neq \text{id}$ muss auch
  $\sigma_i^2$ durch $f_i$ – nicht nur der Messwert.
- **Unsicherheitszuwachs im Vorwärtsmodell** ist kein Fehler, sondern notwendig gegen
  Selbstüberschätzung/Illusionen.

## Sources

[[VL10 Multisensorische Interaktion und Räume]] (Folien 11–15); [[Tutorien – Übersicht und Diskussionsfragen]]
(Tutorium 9); Formeln auch in [[Formelsammlung (Tutorium)]].
