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

---

## Definition der rationalen Zahlen

Die **rationalen Zahlen** sind alle Zahlen, die sich als Bruch zweier ganzer Zahlen darstellen lassen:

$$\mathbb{Q} = \left\{ \frac{p}{q} \,\middle|\, p \in \mathbb{Z}, \, q \in \mathbb{Z}, \, q \neq 0 \right\}$$

Das Symbol $\mathbb{Q}$ kommt von „Quotient".

### Beispiele für rationale Zahlen

| Darstellung | Bruchform | Dezimalform |
|-------------|-----------|-------------|
| Ein Halb | $\frac{1}{2}$ | $0{,}5$ |
| Drei Viertel | $\frac{3}{4}$ | $0{,}75$ |
| Minus zwei Drittel | $-\frac{2}{3}$ | $-0{,}\overline{6}$ |
| Fünf | $\frac{5}{1}$ | $5{,}0$ |
| Null | $\frac{0}{1}$ | $0{,}0$ |

> [!note] **Ganze Zahlen sind rational**
> Jede ganze Zahl ist auch eine rationale Zahl:
> $$\mathbb{Z} \subset \mathbb{Q}$$
> Denn $n = \frac{n}{1}$ für jedes $n \in \mathbb{Z}$.

---

## Brüche und ihre Bestandteile

Ein Bruch besteht aus:

```
       Zähler (Dividend)
      ─────────────────
       Nenner (Divisor)
```

| Begriff | Symbol | Bedeutung |
|---------|--------|-----------|
| **Zähler** | $p$ | Gibt an, wie viele Teile genommen werden |
| **Nenner** | $q$ | Gibt an, in wie viele Teile das Ganze geteilt wird |
| **Bruchstrich** | — | Entspricht dem Divisionszeichen |

**Beispiel:** $\frac{3}{4}$ bedeutet: Teile ein Ganzes in 4 gleiche Teile und nimm 3 davon.

---

## Warum brauchen wir rationale Zahlen?

### Motivation: Division

In den ganzen Zahlen ist nicht jede Division möglich:

| Rechnung | Ergebnis in $\mathbb{Z}$? | Ergebnis in $\mathbb{Q}$ |
|----------|---------------------------|--------------------------|
| $6 : 3$ | ✓ Ja: $2$ | $2$ |
| $5 : 2$ | ✗ Nein | $\frac{5}{2} = 2{,}5$ |
| $1 : 4$ | ✗ Nein | $\frac{1}{4} = 0{,}25$ |

Mit den rationalen Zahlen ist die Division (außer durch 0) **immer möglich**.

### Alltagsbeispiele

- **Kochen**: $\frac{3}{4}$ Liter Milch, $\frac{1}{2}$ Teelöffel Salz
- **Zeit**: $\frac{1}{4}$ Stunde = 15 Minuten
- **Geld**: $\frac{1}{2}$ Euro = 50 Cent
- **Sport**: $\frac{2}{3}$ des Spiels vorbei

---

## Dezimaldarstellung rationaler Zahlen

Jede rationale Zahl hat eine **abbrechende** oder **periodische** Dezimaldarstellung:

### Abbrechende Dezimalzahlen

| Bruch | Dezimalzahl |
|-------|-------------|
| $\frac{1}{2}$ | $0{,}5$ |
| $\frac{3}{4}$ | $0{,}75$ |
| $\frac{7}{8}$ | $0{,}875$ |
| $\frac{1}{5}$ | $0{,}2$ |

### Periodische Dezimalzahlen

| Bruch | Dezimalzahl | Periode |
|-------|-------------|---------|
| $\frac{1}{3}$ | $0{,}\overline{3} = 0{,}333...$ | $3$ |
| $\frac{2}{3}$ | $0{,}\overline{6} = 0{,}666...$ | $6$ |
| $\frac{1}{7}$ | $0{,}\overline{142857}$ | $142857$ |
| $\frac{1}{6}$ | $0{,}1\overline{6} = 0{,}1666...$ | $6$ |

> [!tip] **Merkregel**
> Eine Dezimalzahl ist genau dann rational, wenn sie abbricht oder periodisch wird.
> Nicht-abbrechende, nicht-periodische Dezimalzahlen sind **irrational** (z.B. $\pi$, $\sqrt{2}$).

---

## Darstellung auf dem Zahlenstrahl

Rationale Zahlen liegen **dicht** auf dem Zahlenstrahl:

```
    ←──┬────┬────┬────┬────┬────┬────┬────┬────┬──→
      -1  -½    0   ¼   ½   ¾    1   1¼  1½   2
           │         │   │   │        │
          -0,5      0,25 0,5 0,75    1,25
```

> [!note] **Dichtheit der rationalen Zahlen**
> Zwischen je zwei verschiedenen rationalen Zahlen liegt immer eine weitere rationale Zahl.
> Beweis: Wenn $a < b$, dann gilt $a < \frac{a+b}{2} < b$.

---

## Kürzen und Erweitern

### Kürzen

Zähler und Nenner durch denselben Faktor teilen:
$$\frac{6}{8} = \frac{6:2}{8:2} = \frac{3}{4}$$

### Erweitern

Zähler und Nenner mit demselben Faktor multiplizieren:
$$\frac{3}{4} = \frac{3 \cdot 2}{4 \cdot 2} = \frac{6}{8}$$

> [!warning] **Wichtig**
> Der Wert des Bruchs ändert sich beim Kürzen und Erweitern nicht!
> $$\frac{a}{b} = \frac{a \cdot c}{b \cdot c} \quad \text{für } c \neq 0$$

---

## Rechenoperationen in $\mathbb{Q}$

### Abgeschlossenheit

| Operation | Abgeschlossen in $\mathbb{Q}$? | Begründung |
|-----------|--------------------------------|------------|
| Addition | ✓ Ja | $\frac{1}{2} + \frac{1}{3} = \frac{5}{6} \in \mathbb{Q}$ |
| Subtraktion | ✓ Ja | $\frac{1}{2} - \frac{2}{3} = -\frac{1}{6} \in \mathbb{Q}$ |
| Multiplikation | ✓ Ja | $\frac{2}{3} \cdot \frac{3}{4} = \frac{1}{2} \in \mathbb{Q}$ |
| Division | ✓ Ja (außer durch 0) | $\frac{2}{3} : \frac{4}{5} = \frac{5}{6} \in \mathbb{Q}$ |

> [!note] **$\mathbb{Q}$ ist ein Körper**
> In $\mathbb{Q}$ sind alle vier Grundrechenarten (außer Division durch 0) uneingeschränkt möglich. Man nennt eine solche Zahlenmenge einen **Körper**.

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

> [!question] **Typische Prüfungsfragen**
> - Ist $0{,}75$ eine rationale Zahl? Stelle sie als Bruch dar.
> - Warum ist $\sqrt{2}$ keine rationale Zahl?
> - Kürze den Bruch $\frac{24}{36}$ vollständig.
> - Finde eine rationale Zahl zwischen $\frac{1}{3}$ und $\frac{1}{2}$.

## Quellen

- Scheid, Harald; Schwarz, Wolfgang: *Elemente der Arithmetik und Algebra*. Springer, 2016.
- Padberg, Friedhelm: *Didaktik der Bruchrechnung*. Springer, 2009.

> [!tip] **Weiterführende Links**
> - [Mathebibel: Rationale Zahlen](https://www.mathebibel.de/rationale-zahlen)
> - [[06-Reelle-Zahlen|Nächstes Kapitel: Reelle Zahlen]]
