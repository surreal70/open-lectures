---
author: Open Lectures
title: Rationale Zahlen
status: draft - review pending
tags:
  - content
  - mathematik
  - zahlenmengen
  - rationale-zahlen
created: 2026-10-13
modified: 2026-10-13
---

# Rationale Zahlen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Menge der rationalen Zahlen $\mathbb{Q}$ definieren können
> - Brüche als rationale Zahlen verstehen
> - Rationale Zahlen auf dem Zahlenstrahl darstellen können
> - Wissen, warum Division durch rationale Zahlen erweitert werden musste

---

## Überblick

Die rationalen Zahlen erweitern die ganzen Zahlen um alle Brüche. Damit wird die Division (außer durch Null) immer möglich. Der Name „rational" kommt vom lateinischen Wort „ratio" (Verhältnis), denn jede rationale Zahl lässt sich als Verhältnis zweier ganzer Zahlen schreiben.

Die Einführung der Brüche war ein wichtiger Schritt in der Geschichte der Mathematik. Schon die alten Ägypter verwendeten Brüche, um Längen und Flächen zu messen, die nicht genau einer ganzen Zahl von Einheiten entsprachen. Wenn ein Stück Land 3,5 Ellen lang ist, braucht man eine Möglichkeit, diese „halbe Elle" auszudrücken – und genau das leisten die rationalen Zahlen.

---

## Definition der rationalen Zahlen

Die **rationalen Zahlen** sind alle Zahlen, die sich als Bruch zweier ganzer Zahlen darstellen lassen:

$$\mathbb{Q} = \left\{ \frac{p}{q} \,\middle|\, p \in \mathbb{Z}, \, q \in \mathbb{Z}, \, q \neq 0 \right\}$$

Das Symbol $\mathbb{Q}$ kommt von „Quotient" (lat. für „wie oft enthalten"), denn ein Bruch $\frac{p}{q}$ gibt an, wie oft $q$ in $p$ enthalten ist.

### Bedeutung der Definition

Die Definition sagt:
- $p$ kann jede ganze Zahl sein (positiv, negativ oder null)
- $q$ kann jede ganze Zahl außer Null sein (denn durch Null darf man nicht teilen)
- Die Schreibweise $\frac{p}{q}$ bedeutet „$p$ geteilt durch $q$"

### Beispiele für rationale Zahlen

| Darstellung | Bruchform | Dezimalform | Erklärung |
|-------------|-----------|-------------|-----------|
| Ein Halb | $\frac{1}{2}$ | $0{,}5$ | Ein Ganzes in zwei Teile geteilt, einen davon nehmen |
| Drei Viertel | $\frac{3}{4}$ | $0{,}75$ | Ein Ganzes in vier Teile geteilt, drei davon nehmen |
| Minus zwei Drittel | $-\frac{2}{3}$ | $-0{,}\overline{6}$ | Negative rationale Zahl |
| Fünf | $\frac{5}{1}$ | $5{,}0$ | Jede ganze Zahl ist auch rational |
| Null | $\frac{0}{1}$ | $0{,}0$ | Null geteilt durch jede Zahl ergibt Null |

> [!note] **Ganze Zahlen sind rational**
> Jede ganze Zahl ist auch eine rationale Zahl:
> $$\mathbb{Z} \subset \mathbb{Q}$$
> Denn jede ganze Zahl $n$ lässt sich als Bruch schreiben: $n = \frac{n}{1}$. Zum Beispiel: $5 = \frac{5}{1}$ oder $-3 = \frac{-3}{1}$.

---

## Brüche und ihre Bestandteile

Ein Bruch besteht aus drei Teilen, die jeweils eine eigene Bedeutung haben:

```
       Zähler (Dividend)      ← „Wie viele Teile nehme ich?"
      ─────────────────       ← Bruchstrich (= Divisionszeichen)
       Nenner (Divisor)       ← „In wie viele Teile ist das Ganze geteilt?"
```

| Begriff | Symbol | Bedeutung | Beispiel bei $\frac{3}{4}$ |
|---------|--------|-----------|---------------------------|
| **Zähler** | $p$ | Gibt an, wie viele Teile genommen werden | 3 Teile werden genommen |
| **Nenner** | $q$ | Gibt an, in wie viele Teile das Ganze geteilt wird | Das Ganze ist in 4 Teile geteilt |
| **Bruchstrich** | — | Entspricht dem Divisionszeichen | $3 : 4$ |

**Anschauliche Interpretation:** Der Bruch $\frac{3}{4}$ bedeutet:
> „Teile ein Ganzes (z.B. einen Kuchen) in 4 gleiche Teile und nimm 3 davon."

Diese Vorstellung hilft, Brüche zu verstehen und miteinander zu vergleichen. Ein Viertel ($\frac{1}{4}$) ist offensichtlich kleiner als drei Viertel ($\frac{3}{4}$) – denn man nimmt weniger Stücke vom gleichen Kuchen.

---

## Warum brauchen wir rationale Zahlen?

### Motivation: Division ohne Einschränkungen

In den ganzen Zahlen ist nicht jede Division möglich. Die Division $a : b$ ergibt nur dann eine ganze Zahl, wenn $a$ ein Vielfaches von $b$ ist:

| Rechnung | Ergebnis in $\mathbb{Z}$? | Ergebnis in $\mathbb{Q}$ | Erklärung |
|----------|---------------------------|--------------------------|-----------|
| $6 : 3$ | ✓ Ja: $2$ | $2$ | 6 ist Vielfaches von 3 |
| $5 : 2$ | ✗ Nein | $\frac{5}{2} = 2{,}5$ | 5 ist kein Vielfaches von 2 |
| $1 : 4$ | ✗ Nein | $\frac{1}{4} = 0{,}25$ | 1 ist kein Vielfaches von 4 |
| $7 : 3$ | ✗ Nein | $\frac{7}{3} = 2{,}\overline{3}$ | 7 ist kein Vielfaches von 3 |

Mit den rationalen Zahlen ist die Division (außer durch 0) **immer möglich**. Das war die Hauptmotivation für die Erweiterung der Zahlenmengen.

### Alltagsbeispiele für Brüche

Brüche begegnen uns im Alltag ständig:

| Bereich | Beispiel | Bedeutung |
|---------|----------|-----------|
| **Kochen** | $\frac{3}{4}$ Liter Milch | 750 ml = dreiviertel Liter |
| **Backen** | $\frac{1}{2}$ Teelöffel Salz | Ein halber Teelöffel |
| **Zeit** | $\frac{1}{4}$ Stunde | 15 Minuten = eine Viertelstunde |
| **Geld** | $\frac{1}{2}$ Euro | 50 Cent = ein halber Euro |
| **Sport** | $\frac{2}{3}$ des Spiels vorbei | Zwei Drittel der Spielzeit sind um |
| **Tanken** | Tank ist $\frac{3}{4}$ voll | Dreiviertel des Tanks sind gefüllt |

---

## Dezimaldarstellung rationaler Zahlen

Jede rationale Zahl hat eine **abbrechende** oder **periodische** Dezimaldarstellung. Dies ist ein fundamentales Kennzeichen rationaler Zahlen.

### Abbrechende Dezimalzahlen

Bei manchen Brüchen bricht die Dezimalentwicklung nach endlich vielen Stellen ab:

| Bruch | Dezimalzahl | Warum abbrechend? |
|-------|-------------|-------------------|
| $\frac{1}{2}$ | $0{,}5$ | Nenner ist $2 = 2^1$ |
| $\frac{3}{4}$ | $0{,}75$ | Nenner ist $4 = 2^2$ |
| $\frac{7}{8}$ | $0{,}875$ | Nenner ist $8 = 2^3$ |
| $\frac{1}{5}$ | $0{,}2$ | Nenner ist $5 = 5^1$ |
| $\frac{3}{20}$ | $0{,}15$ | Nenner ist $20 = 2^2 \cdot 5$ |

> [!note] **Wann bricht die Dezimalentwicklung ab?**
> Ein vollständig gekürzter Bruch $\frac{p}{q}$ hat genau dann eine abbrechende Dezimaldarstellung, wenn der Nenner $q$ nur die Primfaktoren 2 und/oder 5 enthält.

### Periodische Dezimalzahlen

Bei anderen Brüchen wiederholt sich eine Ziffernfolge (die „Periode") unendlich oft:

| Bruch | Dezimalzahl | Periode | Periodenlänge |
|-------|-------------|---------|---------------|
| $\frac{1}{3}$ | $0{,}\overline{3} = 0{,}333...$ | $3$ | 1 |
| $\frac{2}{3}$ | $0{,}\overline{6} = 0{,}666...$ | $6$ | 1 |
| $\frac{1}{7}$ | $0{,}\overline{142857}$ | $142857$ | 6 |
| $\frac{1}{6}$ | $0{,}1\overline{6} = 0{,}1666...$ | $6$ | 1 |
| $\frac{1}{11}$ | $0{,}\overline{09}$ | $09$ | 2 |

Der Überstrich markiert die sich wiederholende Ziffernfolge.

> [!tip] **Merkregel: Rationale Zahlen erkennen**
> Eine Dezimalzahl ist genau dann rational, wenn sie:
> - **abbricht** (z.B. $0{,}25$), oder
> - **periodisch wird** (z.B. $0{,}\overline{3}$)
>
> Nicht-abbrechende, nicht-periodische Dezimalzahlen sind **irrational** (z.B. $\pi = 3{,}14159...$, $\sqrt{2} = 1{,}41421...$).

---

## Darstellung auf dem Zahlenstrahl

Rationale Zahlen liegen **dicht** auf dem Zahlenstrahl – das bedeutet, zwischen je zwei verschiedenen rationalen Zahlen liegt immer mindestens eine weitere:

```
    ←──┬────┬────┬────┬────┬────┬────┬────┬────┬──→
      -1  -½    0   ¼   ½   ¾    1   1¼  1½   2
           │         │   │   │        │
          -0,5      0,25 0,5 0,75    1,25
```

### Die Dichtheit der rationalen Zahlen

> [!note] **Mathematische Eigenschaft: Dichtheit**
> Zwischen je zwei verschiedenen rationalen Zahlen $a$ und $b$ liegt immer eine weitere rationale Zahl.
> 
> **Beweis:** Wenn $a < b$, dann liegt der Mittelwert $\frac{a+b}{2}$ genau zwischen $a$ und $b$:
> $$a < \frac{a+b}{2} < b$$
> 
> Der Mittelwert zweier rationaler Zahlen ist wieder rational (Summe und Division sind in $\mathbb{Q}$ definiert).

Diese Eigenschaft bedeutet: Es gibt keine „Nachbarn" unter den rationalen Zahlen. Zu jeder rationalen Zahl kann man eine beliebig nahe andere finden – aber nie die „nächste".

---

## Kürzen und Erweitern

Brüche lassen sich in verschiedenen Formen darstellen, die denselben Wert repräsentieren.

### Kürzen: Gemeinsame Faktoren entfernen

Beim Kürzen teilt man Zähler und Nenner durch denselben Faktor:

$$\frac{6}{8} = \frac{6:2}{8:2} = \frac{3}{4}$$

Ein Bruch ist **vollständig gekürzt**, wenn Zähler und Nenner keinen gemeinsamen Teiler mehr haben (außer 1).

**Beispiel:**
$$\frac{24}{36} = \frac{24:12}{36:12} = \frac{2}{3}$$

### Erweitern: Zähler und Nenner vervielfachen

Beim Erweitern multipliziert man Zähler und Nenner mit demselben Faktor:

$$\frac{3}{4} = \frac{3 \cdot 2}{4 \cdot 2} = \frac{6}{8} = \frac{3 \cdot 3}{4 \cdot 3} = \frac{9}{12}$$

> [!warning] **Wichtig: Der Wert ändert sich nicht!**
> Kürzen und Erweitern ändern nur die **Darstellung** des Bruchs, nicht seinen **Wert**:
> $$\frac{a}{b} = \frac{a \cdot c}{b \cdot c} \quad \text{für } c \neq 0$$
>
> Der Bruch $\frac{1}{2}$ ist derselbe Wert wie $\frac{2}{4}$ oder $\frac{50}{100}$ – nur anders geschrieben.

Das Erweitern ist besonders wichtig, wenn man Brüche mit verschiedenen Nennern addieren möchte.

---

## Rechenoperationen in $\mathbb{Q}$

### Abgeschlossenheit: Alle Grundrechenarten möglich

| Operation | Abgeschlossen in $\mathbb{Q}$? | Begründung | Beispiel |
|-----------|--------------------------------|------------|----------|
| Addition | ✓ Ja | Summe zweier Brüche ist ein Bruch | $\frac{1}{2} + \frac{1}{3} = \frac{5}{6} \in \mathbb{Q}$ |
| Subtraktion | ✓ Ja | Differenz zweier Brüche ist ein Bruch | $\frac{1}{2} - \frac{2}{3} = -\frac{1}{6} \in \mathbb{Q}$ |
| Multiplikation | ✓ Ja | Produkt zweier Brüche ist ein Bruch | $\frac{2}{3} \cdot \frac{3}{4} = \frac{1}{2} \in \mathbb{Q}$ |
| Division | ✓ Ja (außer durch 0) | Quotient zweier Brüche ist ein Bruch | $\frac{2}{3} : \frac{4}{5} = \frac{5}{6} \in \mathbb{Q}$ |

> [!note] **$\mathbb{Q}$ ist ein Körper**
> In $\mathbb{Q}$ sind alle vier Grundrechenarten (außer Division durch 0) uneingeschränkt möglich. Eine Zahlenmenge mit dieser Eigenschaft nennt man einen **Körper**. Die natürlichen und ganzen Zahlen sind keine Körper, weil dort nicht jede Division möglich ist.

### Kurzregeln für Bruchrechnung

| Operation | Regel | Beispiel |
|-----------|-------|----------|
| **Addition** (gleicher Nenner) | $\frac{a}{c} + \frac{b}{c} = \frac{a+b}{c}$ | $\frac{2}{5} + \frac{1}{5} = \frac{3}{5}$ |
| **Multiplikation** | $\frac{a}{b} \cdot \frac{c}{d} = \frac{a \cdot c}{b \cdot d}$ | $\frac{2}{3} \cdot \frac{4}{5} = \frac{8}{15}$ |
| **Division** | $\frac{a}{b} : \frac{c}{d} = \frac{a}{b} \cdot \frac{d}{c}$ | $\frac{3}{4} : \frac{2}{5} = \frac{3}{4} \cdot \frac{5}{2} = \frac{15}{8}$ |

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[04-Ganze-Zahlen|Ganze Zahlen]] – Die Grundlage: $\mathbb{Z} \subset \mathbb{Q}$
- → [[06-Reelle-Zahlen|Reelle Zahlen]] – Nächste Erweiterung: $\mathbb{Q} \subset \mathbb{R}$
- → [[07-Zahlenstrahl-und-Zahlenmengen|Zahlenstrahl und Zahlenmengen]] – Visualisierung

> [!warning] **Prüfungsrelevant**
> - Definition: $\mathbb{Q} = \{ \frac{p}{q} \mid p, q \in \mathbb{Z}, q \neq 0 \}$
> - $\mathbb{Z} \subset \mathbb{Q}$ (jede ganze Zahl ist rational)
> - Rationale Zahlen haben abbrechende oder periodische Dezimaldarstellung
> - In $\mathbb{Q}$ sind alle vier Grundrechenarten möglich (außer Division durch 0)
> - Brüche kürzen: Zähler und Nenner durch gleichen Faktor teilen
> - Division durch Bruch = Multiplikation mit Kehrwert

> [!question] **Typische Prüfungsfragen**
> - Ist $0{,}75$ eine rationale Zahl? Stelle sie als vollständig gekürzten Bruch dar.
> - Warum ist $\sqrt{2}$ keine rationale Zahl?
> - Kürze den Bruch $\frac{24}{36}$ vollständig.
> - Finde eine rationale Zahl zwischen $\frac{1}{3}$ und $\frac{1}{2}$.
> - Berechne: $\frac{2}{3} + \frac{3}{4}$

## Quellen

- Scheid, Harald; Schwarz, Wolfgang: *Elemente der Arithmetik und Algebra*. Springer, 2016.
- Padberg, Friedhelm: *Didaktik der Bruchrechnung*. Springer, 2009.
- Ifrah, Georges: *Universalgeschichte der Zahlen*. Campus, 1991.

> [!tip] **Weiterführende Links**
> - [Mathebibel: Rationale Zahlen](https://www.mathebibel.de/rationale-zahlen)
> - [[06-Reelle-Zahlen|Nächstes Kapitel: Reelle Zahlen]]
