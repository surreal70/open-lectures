---
author: Open Lectures
title: Zahlenstrahl und Zahlenmengen
status: final
tags:
  - content
  - mathematik
  - zahlenmengen
  - zahlenstrahl
created: 2026-10-13
modified: 2026-10-16
---

# Zahlenstrahl und Zahlenmengen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Zahlen auf dem Zahlenstrahl darstellen und ablesen können
> - Die verschiedenen Zahlenmengen und ihre Symbole kennen
> - Teilmengenbeziehungen zwischen Zahlenmengen verstehen
> - Zahlen korrekt in Zahlenmengen einordnen können

---

## Überblick

Der Zahlenstrahl ist ein wichtiges Hilfsmittel, um Zahlen zu visualisieren und zu ordnen. Er zeigt anschaulich, wie die verschiedenen Zahlenmengen aufeinander aufbauen und wie sie zusammenhängen.

Die Idee, Zahlen als Punkte auf einer Linie darzustellen, geht auf das 17. Jahrhundert zurück. Der Philosoph und Mathematiker René Descartes (1596–1650) nutzte diese Darstellung, um Geometrie und Algebra zu verbinden – ein revolutionärer Schritt, der zur analytischen Geometrie führte. Heute ist der Zahlenstrahl ein fundamentales Werkzeug in der Mathematik und ein unverzichtbares Hilfsmittel beim Lernen.

---

## Der Zahlenstrahl

Der **Zahlenstrahl** ist eine gerade Linie, auf der Zahlen als Punkte dargestellt werden. Jeder Punkt entspricht genau einer reellen Zahl, und jede reelle Zahl entspricht genau einem Punkt:

![[zahlenstrahl-basis.png]]
*<span class="fig-id">01-01-07-zahlenstrahl-basis</span>: Der Zahlenstrahl – eine gerade Linie mit gleichmäßigen Abständen, 0 als Ursprung, positive Zahlen rechts, negative links.*

### Eigenschaften des Zahlenstrahls

| Eigenschaft | Beschreibung | Bedeutung |
|-------------|--------------|-----------|
| **Ursprung** | Der Punkt 0 (Nullpunkt) | Trennt positive von negativen Zahlen |
| **Richtung** | Positive Zahlen rechts, negative links | Ermöglicht eindeutige Ordnung |
| **Skalierung** | Gleichmäßige Abstände zwischen benachbarten ganzen Zahlen | Der Abstand von 1 zu 2 ist gleich dem von 5 zu 6 |
| **Ausdehnung** | Unendlich in beide Richtungen | Es gibt keine größte und keine kleinste Zahl |

### Der Zahlenstrahl als Modell

Der Zahlenstrahl ist ein mathematisches **Modell** – eine vereinfachte Darstellung der Realität. In der Realität können wir keinen unendlich langen Strahl zeichnen, und die Punkte haben keine echte „Ausdehnung". Trotzdem hilft uns dieses Modell, abstrakte Zahlenbeziehungen zu verstehen.

### Zahlen eintragen

Um eine Zahl auf dem Zahlenstrahl einzutragen:

1. **Orientierung finden:** Bestimme, ob die Zahl positiv (rechts von 0) oder negativ (links von 0) ist
2. **Position abschätzen:** Finde die nächstgelegenen ganzen Zahlen als Anhaltspunkte
3. **Punkt markieren:** Setze den Punkt an die richtige Stelle zwischen den Anhaltspunkten
4. **Beschriften:** Schreibe den Wert dazu (bei Bedarf)

**Beispiel:** Die Zahlen $-1{,}5$, $\frac{1}{2}$ und $2{,}75$ eintragen:

![[zahlenstrahl-beispielpunkte.png]]
*<span class="fig-id">01-01-07-zahlenstrahl-beispielpunkte</span>: Die Zahlen −1,5, ½ und 2,75 auf dem Zahlenstrahl eingetragen – zwischen den ganzzahligen Markierungen positioniert.*

> [!tip] **Hilfstechnik: Intervallhalbierung**
> Um Brüche wie $\frac{1}{4}$ oder $\frac{3}{4}$ einzutragen, halbiere zunächst den Abstand zwischen zwei ganzen Zahlen (das ergibt $\frac{1}{2}$), dann halbiere erneut (das ergibt $\frac{1}{4}$ und $\frac{3}{4}$).

---

## Übersicht der Zahlenmengen

Die Mathematik kennt verschiedene Zahlenmengen, die systematisch aufeinander aufbauen. Jede Erweiterung ermöglicht neue Rechenoperationen.

### Die wichtigsten Zahlenmengen im Überblick

| Symbol | Name | Elemente | Neu möglich |
|--------|------|----------|-------------|
| $\mathbb{N}$ | Natürliche Zahlen | $1, 2, 3, 4, 5, \ldots$ | Zählen |
| $\mathbb{N}_0$ | Natürliche Zahlen mit Null | $0, 1, 2, 3, 4, \ldots$ | „Nichts" ausdrücken |
| $\mathbb{Z}$ | Ganze Zahlen | $\ldots, -2, -1, 0, 1, 2, \ldots$ | Subtraktion immer möglich |
| $\mathbb{Q}$ | Rationale Zahlen | Alle Brüche $\frac{p}{q}$ | Division immer möglich |
| $\mathbb{R}$ | Reelle Zahlen | Alle Zahlen auf dem Strahl | Zahlenstrahl ist „lückenlos" |

### Teilmengenbeziehungen

Die Zahlenmengen sind wie ineinander geschachtelte Behälter angeordnet. Jede kleinere Menge ist vollständig in der größeren enthalten:

$$\mathbb{N} \subset \mathbb{N}_0 \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$$

Das Symbol $\subset$ bedeutet „ist Teilmenge von" oder „ist enthalten in".

**Was bedeutet das konkret?**
- Jede natürliche Zahl ist auch eine ganze Zahl: $5 \in \mathbb{N} \Rightarrow 5 \in \mathbb{Z}$
- Jede ganze Zahl ist auch eine rationale Zahl: $-3 \in \mathbb{Z} \Rightarrow -3 \in \mathbb{Q}$
- Jede rationale Zahl ist auch eine reelle Zahl: $\frac{1}{2} \in \mathbb{Q} \Rightarrow \frac{1}{2} \in \mathbb{R}$

Umgekehrt gilt das nicht: $\sqrt{2}$ ist reell, aber nicht rational; $-3$ ist ganz, aber nicht natürlich.

---

## Visualisierung auf dem Zahlenstrahl

Jede Zahlenmenge hat eine charakteristische Art, wie sie auf dem Zahlenstrahl erscheint.

### Natürliche Zahlen $\mathbb{N}$: Isolierte Punkte

![[mengen-n.png]]
*<span class="fig-id">01-01-07-mengen-n</span>: Die natürlichen Zahlen ℕ bilden isolierte Punkte mit Lücken dazwischen; die Null ist nicht enthalten (leerer Kreis).*

Die natürlichen Zahlen bilden **isolierte Punkte** mit Lücken dazwischen. Zwischen 2 und 3 gibt es keine natürliche Zahl.

### Ganze Zahlen $\mathbb{Z}$: Punkte auf beiden Seiten

![[mengen-z.png]]
*<span class="fig-id">01-01-07-mengen-z</span>: Die ganzen Zahlen ℤ erweitern ℕ um die Null und die negativen Zahlen – weiterhin isolierte Punkte, nun auch links der Null.*

Die ganzen Zahlen erweitern die natürlichen um die Null und die negativen Zahlen. Trotzdem sind es immer noch isolierte Punkte mit Lücken.

### Rationale Zahlen $\mathbb{Q}$: Dicht, aber mit Lücken

![[mengen-q.png]]
*<span class="fig-id">01-01-07-mengen-q</span>: Die rationalen Zahlen ℚ liegen dicht – zwischen je zwei rationalen Zahlen liegt immer eine weitere; trotzdem bleiben „unsichtbare Lücken" (z. B. √2).*

Die rationalen Zahlen liegen **dicht**: Zwischen je zwei rationalen Zahlen liegt immer eine weitere. Trotzdem gibt es „unsichtbare Lücken" – Punkte wie $\sqrt{2}$, die von keiner rationalen Zahl getroffen werden.

### Reelle Zahlen $\mathbb{R}$: Durchgezogene Linie

![[mengen-r.png]]
*<span class="fig-id">01-01-07-mengen-r</span>: Die reellen Zahlen ℝ füllen den Zahlenstrahl vollständig aus – eine durchgezogene Linie ohne Lücken; jeder Punkt entspricht genau einer Zahl.*

Die reellen Zahlen „füllen" den Zahlenstrahl vollständig aus. Es gibt keine Lücken – zu jedem Punkt gehört genau eine Zahl.

---

## Zugehörigkeit prüfen: In welcher Menge liegt eine Zahl?

### Entscheidungsbaum

Um zu bestimmen, in welchen Zahlenmengen eine Zahl liegt, kann man systematisch vorgehen:

![[entscheidungsbaum.png]]
*<span class="fig-id">01-01-07-entscheidungsbaum</span>: Entscheidungsbaum zur systematischen Einordnung einer Zahl x in die passende Zahlenmenge – jede „ja"-Antwort führt zum Ergebnis, jede „nein"-Antwort zur nächsten Prüfung.*

### Praktische Übungstabelle

| Zahl | $\in \mathbb{N}$? | $\in \mathbb{Z}$? | $\in \mathbb{Q}$? | $\in \mathbb{R}$? | Begründung |
|------|-------------------|-------------------|-------------------|-------------------|------------|
| $5$ | ✓ | ✓ | ✓ | ✓ | Positive ganze Zahl |
| $-3$ | ✗ | ✓ | ✓ | ✓ | Negative ganze Zahl |
| $0$ | ✗ | ✓ | ✓ | ✓ | Null (nicht in $\mathbb{N}$) |
| $\frac{2}{3}$ | ✗ | ✗ | ✓ | ✓ | Bruch, keine ganze Zahl |
| $0{,}5$ | ✗ | ✗ | ✓ | ✓ | $= \frac{1}{2}$, abbrechende Dezimalzahl |
| $0{,}\overline{3}$ | ✗ | ✗ | ✓ | ✓ | $= \frac{1}{3}$, periodische Dezimalzahl |
| $\sqrt{2}$ | ✗ | ✗ | ✗ | ✓ | Irrational (nicht als Bruch darstellbar) |
| $\pi$ | ✗ | ✗ | ✗ | ✓ | Irrational (weder abbrechend noch periodisch) |
| $\sqrt{9}$ | ✓ | ✓ | ✓ | ✓ | $= 3$, also natürliche Zahl! |

> [!tip] **Vorsicht bei Wurzeln!**
> Nicht jede Wurzel ist irrational. $\sqrt{9} = 3$ ist sogar eine natürliche Zahl. Immer erst ausrechnen, dann einordnen!

---

## Mengenoperationen

Manchmal arbeiten wir mit Kombinationen von Mengen. Die wichtigsten Operationen:

### Schnittmenge ($\cap$): „sowohl als auch"

Die Schnittmenge enthält alle Elemente, die in **beiden** Mengen liegen:

$$A \cap B = \{x \mid x \in A \text{ und } x \in B\}$$

![[venn-schnittmenge.png]]
*<span class="fig-id">01-01-07-venn-schnittmenge</span>: Die Schnittmenge A ∩ B (hervorgehoben) umfasst nur die Elemente, die sowohl zu A als auch zu B gehören.*

**Beispiele:**
- $\mathbb{N} \cap \mathbb{Z}^- = \emptyset$ (Natürliche Zahlen und negative ganze Zahlen haben keine gemeinsamen Elemente)
- $\mathbb{Z} \cap \mathbb{Q} = \mathbb{Z}$ (Alle ganzen Zahlen sind auch rational)

### Vereinigung ($\cup$): „oder"

Die Vereinigung enthält alle Elemente, die in **mindestens einer** der Mengen liegen:

$$A \cup B = \{x \mid x \in A \text{ oder } x \in B\}$$

![[venn-vereinigung.png]]
*<span class="fig-id">01-01-07-venn-vereinigung</span>: Die Vereinigung A ∪ B (hervorgehoben) umfasst alle Elemente, die zu A oder zu B (oder zu beiden) gehören.*

**Beispiel:**
$$\mathbb{Z}^+ \cup \mathbb{Z}^- \cup \{0\} = \mathbb{Z}$$
(Positive, negative ganze Zahlen und Null ergeben zusammen alle ganzen Zahlen)

### Differenz ($\setminus$): „ohne"

Die Differenz $A \setminus B$ enthält alle Elemente von $A$, die **nicht** in $B$ liegen:

$$A \setminus B = \{x \mid x \in A \text{ und } x \notin B\}$$

![[venn-differenz.png]]
*<span class="fig-id">01-01-07-venn-differenz</span>: Die Differenz A ∖ B (hervorgehoben) umfasst die Elemente von A, die nicht gleichzeitig in B liegen.*

**Wichtiges Beispiel:**
$$\mathbb{R} \setminus \mathbb{Q} = \text{irrationale Zahlen}$$
(Alle reellen Zahlen, die nicht rational sind)

---

## Wichtige Teilmengen mit Spezialnotation

Für häufig verwendete Teilmengen gibt es spezielle Schreibweisen:

| Notation | Bedeutung | Elemente | Beispiel |
|----------|-----------|----------|----------|
| $\mathbb{Z}^+$ | Positive ganze Zahlen | $1, 2, 3, \ldots$ (= $\mathbb{N}$) | $7 \in \mathbb{Z}^+$ |
| $\mathbb{Z}^-$ | Negative ganze Zahlen | $-1, -2, -3, \ldots$ | $-5 \in \mathbb{Z}^-$ |
| $\mathbb{Q}^+$ | Positive rationale Zahlen | Alle positiven Brüche | $\frac{3}{4} \in \mathbb{Q}^+$ |
| $\mathbb{R}^+$ | Positive reelle Zahlen | $(0, \infty)$ | $\sqrt{2} \in \mathbb{R}^+$ |
| $\mathbb{R}^+_0$ | Nicht-negative reelle Zahlen | $[0, \infty)$ | $0 \in \mathbb{R}^+_0$ |
| $\mathbb{R}^*$ | Reelle Zahlen ohne Null | $\mathbb{R} \setminus \{0\}$ | Für Division wichtig |

> [!note] **Warum diese Notationen?**
> Diese Schreibweisen sind kompakt und werden in der höheren Mathematik häufig verwendet. Sie sparen Platz und vermeiden Missverständnisse. Statt zu schreiben „alle positiven reellen Zahlen" schreibt man einfach $\mathbb{R}^+$.

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[03-Natuerliche-Zahlen|Natürliche Zahlen]] – Die Grundmenge $\mathbb{N}$
- → [[04-Ganze-Zahlen|Ganze Zahlen]] – Die Menge $\mathbb{Z}$
- → [[05-Rationale-Zahlen|Rationale Zahlen]] – Die Menge $\mathbb{Q}$
- → [[06-Reelle-Zahlen|Reelle Zahlen]] – Die Menge $\mathbb{R}$
- → [[02-Mathematische-Symbole|Mathematische Symbole]] – Mengennotation

> [!warning] **Prüfungsrelevant**
> - Symbole: $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$
> - Teilmengenbeziehung: $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$
> - Zahlen korrekt in Mengen einordnen können
> - Zahlen auf dem Zahlenstrahl darstellen können
> - Schnittmenge ($\cap$), Vereinigung ($\cup$), Differenz ($\setminus$)

> [!question] **Typische Prüfungsfragen**
> - In welchen Zahlenmengen liegt die Zahl $-\frac{5}{2}$?
> - Zeichne die Zahlen $-2$, $0{,}5$, $\sqrt{4}$ auf einem Zahlenstrahl ein.
> - Was ist $\mathbb{Z} \cap \mathbb{Q}$?
> - Nenne eine Zahl, die in $\mathbb{R}$, aber nicht in $\mathbb{Q}$ liegt.
> - Ordne die Zahlenmengen $\mathbb{N}$, $\mathbb{R}$, $\mathbb{Q}$, $\mathbb{Z}$ nach Inklusionsbeziehung.

## Quellen

- Papula, Lothar: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1. Springer, 2018.
- Beutelspacher, Albrecht: *Zahlen*. Rowohlt, 2013.
- Ebbinghaus, H.-D. et al.: *Zahlen*. Springer, 1992.

> [!tip] **Weiterführende Links**
> - [Mathebibel: Zahlenmengen](https://www.mathebibel.de/zahlenmengen)
> - [[08-Positive-und-negative-Zahlen|Nächstes Kapitel: Positive und negative Zahlen]]
