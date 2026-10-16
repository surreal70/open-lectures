---
author: Open Lectures
title: Zahlenstrahl und Zahlenmengen
status: draft - review pending
tags:
  - content
  - mathematik
  - zahlenmengen
  - zahlenstrahl
created: 2026-10-13
modified: 2026-10-13
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

---

## Der Zahlenstrahl

Der **Zahlenstrahl** ist eine gerade Linie, auf der Zahlen als Punkte dargestellt werden:

```
    ←──┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬──→
      -3   -2   -1    0    1    2    3    4    5    6    7
```

### Eigenschaften des Zahlenstrahls

| Eigenschaft | Beschreibung |
|-------------|--------------|
| **Ursprung** | Der Punkt 0 (Nullpunkt) |
| **Richtung** | Positive Zahlen rechts, negative links |
| **Skalierung** | Gleichmäßige Abstände zwischen benachbarten Zahlen |
| **Ausdehnung** | Unendlich in beide Richtungen |

### Zahlen eintragen

Um eine Zahl einzutragen:
1. Finde die richtige Position relativ zu bekannten Zahlen
2. Markiere den Punkt
3. Beschrifte ihn bei Bedarf

**Beispiel:** Die Zahlen $-1{,}5$, $\frac{1}{2}$ und $2{,}75$ eingetragen:

```
    ←──┬────┬────┬──┬─┬────┬────┬──┬─┬────┬──→
      -2  -1,5  -1   0  ½   1    2  2,75  3
           ●            ●          ●
```

---

## Übersicht der Zahlenmengen

### Die wichtigsten Zahlenmengen

| Symbol | Name | Elemente | Beispiele |
|--------|------|----------|-----------|
| $\mathbb{N}$ | Natürliche Zahlen | Positive ganze Zahlen | $1, 2, 3, 100$ |
| $\mathbb{N}_0$ | Natürliche Zahlen mit Null | $\mathbb{N} \cup \{0\}$ | $0, 1, 2, 3$ |
| $\mathbb{Z}$ | Ganze Zahlen | Alle ganzen Zahlen | $-5, 0, 7$ |
| $\mathbb{Q}$ | Rationale Zahlen | Alle Brüche | $\frac{1}{2}, -\frac{3}{4}, 5$ |
| $\mathbb{R}$ | Reelle Zahlen | Alle Zahlen auf dem Strahl | $\sqrt{2}, \pi, -3$ |

### Teilmengenbeziehungen

$$\mathbb{N} \subset \mathbb{N}_0 \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$$

Das bedeutet:
- Jede natürliche Zahl ist auch eine ganze Zahl
- Jede ganze Zahl ist auch eine rationale Zahl
- Jede rationale Zahl ist auch eine reelle Zahl

---

## Visualisierung auf dem Zahlenstrahl

### Natürliche Zahlen $\mathbb{N}$

```
    ←──────────────────┬────┬────┬────┬────┬────┬──→
                       0    1    2    3    4    5
                            ●    ●    ●    ●    ●
                            ↑
                       Natürliche Zahlen (diskrete Punkte)
```

### Ganze Zahlen $\mathbb{Z}$

```
    ←──┬────┬────┬────┬────┬────┬────┬────┬──→
      -3   -2   -1    0    1    2    3    4
       ●    ●    ●    ●    ●    ●    ●    ●
                      ↑
                  Null gehört dazu
```

### Rationale Zahlen $\mathbb{Q}$

```
    ←──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──→
      -1 -¾ -½ -¼  0  ¼  ½  ¾  1  ...
       ●  ●  ●  ●  ●  ●  ●  ●  ●
                   ↑
          Unendlich viele zwischen je zwei Punkten
```

### Reelle Zahlen $\mathbb{R}$

```
    ←══════════════════════════════════════════→
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                     ↑
          Durchgezogene Linie (keine Lücken)
```

---

## Zugehörigkeit prüfen

### Entscheidungsbaum

```
Ist die Zahl...
├── ... eine positive ganze Zahl (1, 2, 3, ...)?
│   └── Ja → ℕ (und damit auch ℤ, ℚ, ℝ)
│
├── ... eine ganze Zahl (..., -2, -1, 0, 1, 2, ...)?
│   └── Ja → ℤ (und damit auch ℚ, ℝ)
│
├── ... ein Bruch oder abbrechende/periodische Dezimalzahl?
│   └── Ja → ℚ (und damit auch ℝ)
│
└── ... eine nicht-abbrechende, nicht-periodische Dezimalzahl?
    └── Ja → ℝ \ ℚ (irrational, nur in ℝ)
```

### Übungstabelle

| Zahl | $\in \mathbb{N}$? | $\in \mathbb{Z}$? | $\in \mathbb{Q}$? | $\in \mathbb{R}$? |
|------|-------------------|-------------------|-------------------|-------------------|
| $5$ | ✓ | ✓ | ✓ | ✓ |
| $-3$ | ✗ | ✓ | ✓ | ✓ |
| $0$ | ✗ | ✓ | ✓ | ✓ |
| $\frac{2}{3}$ | ✗ | ✗ | ✓ | ✓ |
| $0{,}5$ | ✗ | ✗ | ✓ | ✓ |
| $\sqrt{2}$ | ✗ | ✗ | ✗ | ✓ |
| $\pi$ | ✗ | ✗ | ✗ | ✓ |

---

## Mengenoperationen

### Schnittmenge ($\cap$)

Elemente, die in **beiden** Mengen liegen:

$$\mathbb{N} \cap \mathbb{Z}^- = \emptyset$$
(Natürliche Zahlen und negative ganze Zahlen haben keine gemeinsamen Elemente)

### Vereinigung ($\cup$)

Elemente, die in **mindestens einer** Menge liegen:

$$\mathbb{Z}^+ \cup \mathbb{Z}^- \cup \{0\} = \mathbb{Z}$$
(Positive, negative und Null ergeben zusammen alle ganzen Zahlen)

### Differenz ($\setminus$)

Elemente der ersten Menge, die **nicht** in der zweiten liegen:

$$\mathbb{R} \setminus \mathbb{Q} = \text{irrationale Zahlen}$$

---

## Wichtige Teilmengen

| Notation | Bedeutung | Elemente |
|----------|-----------|----------|
| $\mathbb{Z}^+$ | Positive ganze Zahlen | $1, 2, 3, \ldots$ (= $\mathbb{N}$) |
| $\mathbb{Z}^-$ | Negative ganze Zahlen | $-1, -2, -3, \ldots$ |
| $\mathbb{Q}^+$ | Positive rationale Zahlen | $\frac{1}{2}, 3, \frac{7}{4}, \ldots$ |
| $\mathbb{R}^+$ | Positive reelle Zahlen | $(0, \infty)$ |
| $\mathbb{R}^+_0$ | Nicht-negative reelle Zahlen | $[0, \infty)$ |

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

> [!question] **Typische Prüfungsfragen**
> - In welchen Zahlenmengen liegt die Zahl $-\frac{5}{2}$?
> - Zeichne die Zahlen $-2$, $0{,}5$, $\sqrt{4}$ auf einem Zahlenstrahl ein.
> - Was ist $\mathbb{Z} \cap \mathbb{Q}$?
> - Nenne eine Zahl, die in $\mathbb{R}$, aber nicht in $\mathbb{Q}$ liegt.

## Quellen

- Papula, Lothar: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1. Springer, 2018.
- Beutelspacher, Albrecht: *Zahlen*. Rowohlt, 2013.

> [!tip] **Weiterführende Links**
> - [Mathebibel: Zahlenmengen](https://www.mathebibel.de/zahlenmengen)
> - [[08-Positive-und-negative-Zahlen|Nächstes Kapitel: Positive und negative Zahlen]]
