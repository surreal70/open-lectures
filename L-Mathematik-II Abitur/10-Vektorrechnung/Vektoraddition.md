---
author: Andreas Hümmer
title: Vektoraddition
tags:
  - content
  - mathe
  - vektorrechnung
  - addition
  - subtraktion
  - abitur
created: 2025-01-21
modified: 2025-01-21
---

# Vektoraddition

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Vektoren komponentenweise addieren und subtrahieren können
> - Die geometrische Bedeutung der Vektoraddition verstehen (Parallelogrammregel, Kettenregel)
> - Vektorgleichungen aufstellen und lösen können
> - Die Rechengesetze der Vektoraddition anwenden können

---

## Überblick

Die **Addition von Vektoren** ist eine der fundamentalen Operationen der Vektorrechnung. Sie ermöglicht es, mehrere Verschiebungen, Kräfte oder andere vektorielle Größen zu einer resultierenden Größe zusammenzufassen. Die Vektoraddition kann sowohl geometrisch als auch algebraisch durchgeführt werden.

## Komponentenweise Addition

Zwei Vektoren werden addiert, indem ihre entsprechenden Komponenten addiert werden:

$$\vec{a} + \vec{b} = \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix} + \begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix} = \begin{pmatrix} a_1 + b_1 \\ a_2 + b_2 \\ a_3 + b_3 \end{pmatrix}$$

### Beispielrechnung

$$\begin{pmatrix} 3 \\ -2 \\ 5 \end{pmatrix} + \begin{pmatrix} 1 \\ 4 \\ -1 \end{pmatrix} = \begin{pmatrix} 3 + 1 \\ -2 + 4 \\ 5 + (-1) \end{pmatrix} = \begin{pmatrix} 4 \\ 2 \\ 4 \end{pmatrix}$$

## Geometrische Interpretation

### Die Parallelogrammregel

Wenn zwei Vektoren $\vec{a}$ und $\vec{b}$ vom selben Punkt aus angetragen werden, bilden sie zwei Seiten eines Parallelogramms. Die **Diagonale** dieses Parallelogramms ist der Summenvektor $\vec{a} + \vec{b}$.

```
           B ─────────── C
          /            /
         /            /
        / → b        / → a + b
       /            /
      A ─────────── D
          → a
```

### Die Kettenregel (Spitze-an-Fuß-Regel)

Die Vektoren werden „hintereinandergehängt": Der Endpunkt des ersten Vektors ist der Anfangspunkt des zweiten Vektors. Der Summenvektor führt vom Anfangspunkt des ersten zum Endpunkt des zweiten Vektors.

```
      → a        → b
    A ────── B ────── C
    
    |__________________|
           → a + b
```

Diese Regel gilt für beliebig viele Vektoren:

$$\vec{AB} + \vec{BC} + \vec{CD} = \vec{AD}$$

## Vektorsubtraktion

Die **Subtraktion** wird auf die Addition des Gegenvektors zurückgeführt:

$$\vec{a} - \vec{b} = \vec{a} + (-\vec{b}) = \begin{pmatrix} a_1 - b_1 \\ a_2 - b_2 \\ a_3 - b_3 \end{pmatrix}$$

### Beispielrechnung

$$\begin{pmatrix} 5 \\ 3 \\ 7 \end{pmatrix} - \begin{pmatrix} 2 \\ 4 \\ 1 \end{pmatrix} = \begin{pmatrix} 5 - 2 \\ 3 - 4 \\ 7 - 1 \end{pmatrix} = \begin{pmatrix} 3 \\ -1 \\ 6 \end{pmatrix}$$

### Geometrische Interpretation der Subtraktion

Der Differenzvektor $\vec{a} - \vec{b}$ zeigt von der Spitze von $\vec{b}$ zur Spitze von $\vec{a}$, wenn beide Vektoren vom selben Punkt aus angetragen werden.

```
        → a
    A ────────── C
     \          ↑
      \        /
       \      / → a - b
        \    /
         \  /
    → b   \/
           B
```

## Rechengesetze der Vektoraddition

Die Vektoraddition erfüllt wichtige algebraische Gesetze:

| Gesetz | Formel | Bedeutung |
|--------|--------|-----------|
| **Kommutativgesetz** | $\vec{a} + \vec{b} = \vec{b} + \vec{a}$ | Reihenfolge ist egal |
| **Assoziativgesetz** | $(\vec{a} + \vec{b}) + \vec{c} = \vec{a} + (\vec{b} + \vec{c})$ | Klammerung ist egal |
| **Neutrales Element** | $\vec{a} + \vec{0} = \vec{a}$ | Nullvektor ändert nichts |
| **Inverses Element** | $\vec{a} + (-\vec{a}) = \vec{0}$ | Gegenvektor ergibt Nullvektor |

### Beweis des Kommutativgesetzes

$$\vec{a} + \vec{b} = \begin{pmatrix} a_1 + b_1 \\ a_2 + b_2 \\ a_3 + b_3 \end{pmatrix} = \begin{pmatrix} b_1 + a_1 \\ b_2 + a_2 \\ b_3 + a_3 \end{pmatrix} = \vec{b} + \vec{a}$$

Da die Addition reeller Zahlen kommutativ ist, folgt dies direkt.

## Anwendung: Kräfteaddition

In der Physik werden Kräfte als Vektoren dargestellt. Die **resultierende Kraft** ist die Vektorsumme aller Einzelkräfte:

$$\vec{F}_{\text{res}} = \vec{F}_1 + \vec{F}_2 + \ldots + \vec{F}_n$$

### Beispiel: Zwei Kräfte am Seil

Zwei Personen ziehen an einem Seil mit:
- $\vec{F}_1 = \begin{pmatrix} 100 \\ 50 \\ 0 \end{pmatrix}$ N
- $\vec{F}_2 = \begin{pmatrix} 80 \\ -30 \\ 0 \end{pmatrix}$ N

Die resultierende Kraft:
$$\vec{F}_{\text{res}} = \begin{pmatrix} 100 + 80 \\ 50 + (-30) \\ 0 + 0 \end{pmatrix} = \begin{pmatrix} 180 \\ 20 \\ 0 \end{pmatrix} \text{ N}$$

## Vektorgleichungen lösen

Eine häufige Aufgabe ist das Lösen von Gleichungen nach einem unbekannten Vektor.

### Beispiel

Löse nach $\vec{x}$: $\vec{a} + \vec{x} = \vec{b}$

**Lösung:**
$$\vec{x} = \vec{b} - \vec{a}$$

### Komplexeres Beispiel

Gegeben: $\vec{a} = \begin{pmatrix} 2 \\ 3 \\ 1 \end{pmatrix}$, $\vec{b} = \begin{pmatrix} 5 \\ 1 \\ 4 \end{pmatrix}$

Löse: $2\vec{a} + \vec{x} = \vec{b}$

$$\vec{x} = \vec{b} - 2\vec{a} = \begin{pmatrix} 5 \\ 1 \\ 4 \end{pmatrix} - 2 \cdot \begin{pmatrix} 2 \\ 3 \\ 1 \end{pmatrix} = \begin{pmatrix} 5 \\ 1 \\ 4 \end{pmatrix} - \begin{pmatrix} 4 \\ 6 \\ 2 \end{pmatrix} = \begin{pmatrix} 1 \\ -5 \\ 2 \end{pmatrix}$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Grundlagen-der-Vektoren]] — Definition und Eigenschaften von Vektoren
- → [[Vektordarstellung]] — Koordinatenschreibweise
- → [[Skalarmultiplikation]] — Streckung und Stauchung von Vektoren
- → [[Ortsvektoren]] — Verbindungsvektoren über Differenz

> [!warning] **Prüfungsrelevant**
> - Komponentenweise Addition und Subtraktion durchführen
> - Geometrische Konstruktion mit Parallelogramm- und Kettenregel
> - Rechengesetze (Kommutativ-, Assoziativgesetz) benennen und anwenden
> - Vektorgleichungen nach einer Unbekannten auflösen
> - Anwendung: Resultierende von Kräften bestimmen

> [!question] **Typische Prüfungsfragen**
> - Berechne $\vec{a} + \vec{b}$ und $\vec{a} - \vec{b}$ für $\vec{a} = \begin{pmatrix} 4 \\ -1 \\ 3 \end{pmatrix}$ und $\vec{b} = \begin{pmatrix} -2 \\ 5 \\ 1 \end{pmatrix}$.
> - Bestimme den Vektor $\vec{x}$, sodass $\vec{a} + \vec{x} = \vec{0}$ gilt.
> - Welche Kraft ergibt sich aus der Addition von $\vec{F}_1 = \begin{pmatrix} 30 \\ 40 \end{pmatrix}$ N und $\vec{F}_2 = \begin{pmatrix} -10 \\ 20 \end{pmatrix}$ N?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018
- Lambacher Schweizer: Mathematik für Gymnasien – Analytische Geometrie. Klett, 2023
- Tipler, P.A.; Mosca, G.: Physik für Studierende. Springer Spektrum, 2019

> [!tip] **Weiterführende Links**
> - [[Skalarprodukt]] — Eine andere Art der Vektorverknüpfung
> - [[Kreuzprodukt]] — Das Vektorprodukt für räumliche Berechnungen
