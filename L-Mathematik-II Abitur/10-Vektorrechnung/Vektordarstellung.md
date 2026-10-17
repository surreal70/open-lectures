---
author: Andreas Hümmer
title: Vektordarstellung
tags:
  - content
  - mathe
  - vektorrechnung
  - koordinaten
  - komponenten
  - abitur
created: 2025-01-21
modified: 2025-01-21
---

# Vektordarstellung

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Vektoren in Koordinatendarstellung (Spaltenschreibweise) angeben können
> - Die Komponenten eines Vektors interpretieren und berechnen können
> - Zwischen zwei- und dreidimensionaler Darstellung unterscheiden können
> - Den Verbindungsvektor zweier Punkte berechnen können

---

## Überblick

Um mit Vektoren rechnen zu können, benötigen wir eine präzise numerische Darstellung. Die **Koordinatendarstellung** ermöglicht es, Vektoren durch ihre Komponenten bezüglich eines gewählten Koordinatensystems eindeutig zu beschreiben. Diese algebraische Form ist die Grundlage für alle weiteren Vektoroperationen.

## Koordinatendarstellung in der Ebene

In der Ebene $\mathbb{R}^2$ wird ein Vektor durch zwei Komponenten dargestellt:

$$\vec{a} = \begin{pmatrix} a_1 \\ a_2 \end{pmatrix}$$

Dabei gibt $a_1$ die Verschiebung in $x$-Richtung und $a_2$ die Verschiebung in $y$-Richtung an.

**Beispiel:** Der Vektor $\vec{v} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$ beschreibt eine Verschiebung um 3 Einheiten nach rechts und 4 Einheiten nach oben.

```
    y
    ↑
  4 +     ● Endpunkt
    |    /
    |   /
    |  /  → v
    | /
    +---+---+---→ x
        1   2   3
```

## Koordinatendarstellung im Raum

Im dreidimensionalen Raum $\mathbb{R}^3$ hat ein Vektor drei Komponenten:

$$\vec{a} = \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix}$$

Die Komponenten beschreiben die Verschiebungen entlang der drei Koordinatenachsen:
- $a_1$: Verschiebung in $x$-Richtung
- $a_2$: Verschiebung in $y$-Richtung
- $a_3$: Verschiebung in $z$-Richtung

**Beispiel:** Der Vektor $\vec{w} = \begin{pmatrix} 2 \\ -1 \\ 5 \end{pmatrix}$ beschreibt eine Verschiebung um 2 Einheiten in $x$-Richtung, 1 Einheit entgegen der $y$-Richtung und 5 Einheiten in $z$-Richtung.

## Verbindungsvektor zweier Punkte

Der **Verbindungsvektor** $\vec{AB}$ vom Punkt $A$ zum Punkt $B$ berechnet sich durch:

$$\vec{AB} = \begin{pmatrix} b_1 - a_1 \\ b_2 - a_2 \\ b_3 - a_3 \end{pmatrix}$$

Kurz: **„Spitze minus Fuß"** oder **„Endpunkt minus Anfangspunkt"**.

### Beispielrechnung

Gegeben sind die Punkte $A(1|3|2)$ und $B(4|1|7)$.

Der Verbindungsvektor $\vec{AB}$ ist:

$$\vec{AB} = \begin{pmatrix} 4 - 1 \\ 1 - 3 \\ 7 - 2 \end{pmatrix} = \begin{pmatrix} 3 \\ -2 \\ 5 \end{pmatrix}$$

Der Gegenvektor $\vec{BA}$ ergibt sich zu:

$$\vec{BA} = \begin{pmatrix} 1 - 4 \\ 3 - 1 \\ 2 - 7 \end{pmatrix} = \begin{pmatrix} -3 \\ 2 \\ -5 \end{pmatrix} = -\vec{AB}$$

## Gleichheit von Vektoren

Zwei Vektoren sind genau dann gleich, wenn alle ihre Komponenten übereinstimmen:

$$\vec{a} = \vec{b} \Leftrightarrow a_1 = b_1 \land a_2 = b_2 \land a_3 = b_3$$

Diese Definition folgt aus der Idee, dass Vektoren durch Parallelverschiebung ineinander überführt werden können.

## Nullvektor und Gegenvektor in Koordinaten

### Nullvektor

$$\vec{0} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$$

### Gegenvektor

Für $\vec{a} = \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix}$ gilt:

$$-\vec{a} = \begin{pmatrix} -a_1 \\ -a_2 \\ -a_3 \end{pmatrix}$$

## Standardbasisvektoren

Die **Standardbasisvektoren** (auch Einheitsvektoren der Koordinatenachsen) sind:

$$\vec{e}_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \quad \vec{e}_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \quad \vec{e}_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$$

Jeder Vektor lässt sich als Linearkombination dieser Basisvektoren schreiben:

$$\vec{a} = \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix} = a_1 \cdot \vec{e}_1 + a_2 \cdot \vec{e}_2 + a_3 \cdot \vec{e}_3$$

## Zeilen- und Spaltenschreibweise

In der Mathematik unterscheidet man:

| Schreibweise | Form | Verwendung |
|--------------|------|------------|
| **Spaltenvektor** | $\begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix}$ | Standard für Vektoren |
| **Zeilenvektor** | $(a_1, a_2, a_3)$ | Transponiert, für Matrixrechnung |

Die Transposition wandelt einen Spaltenvektor in einen Zeilenvektor um:

$$\vec{a}^T = (a_1, a_2, a_3)$$

## Praktische Anwendung: Punkte und Vektoren

In der analytischen Geometrie werden Punkte und Vektoren oft verwechselt. Hier die wichtige Unterscheidung:

| Konzept | Schreibweise | Bedeutung |
|---------|--------------|-----------|
| **Punkt** | $P(3|2|5)$ | Feste Position im Raum |
| **Ortsvektor** | $\vec{OP} = \begin{pmatrix} 3 \\ 2 \\ 5 \end{pmatrix}$ | Vektor vom Ursprung zu $P$ |
| **Freier Vektor** | $\vec{v} = \begin{pmatrix} 3 \\ 2 \\ 5 \end{pmatrix}$ | Verschiebung, nicht ortsgebunden |

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Grundlagen-der-Vektoren]] — Geometrische Grundlagen
- → [[Ortsvektoren]] — Spezielle Vektordarstellung für Punkte
- → [[Vektoraddition]] — Rechnen mit Vektoren in Koordinatenform
- → [[Betrag-eines-Vektors]] — Längenberechnung aus Komponenten

> [!warning] **Prüfungsrelevant**
> - Berechnung von Verbindungsvektoren („Spitze minus Fuß")
> - Gleichheit von Vektoren über Komponentenvergleich prüfen
> - Umrechnung zwischen Punkt- und Vektorschreibweise
> - Standardbasisvektoren und Linearkombinationen

> [!question] **Typische Prüfungsfragen**
> - Berechne den Verbindungsvektor $\vec{AB}$ für $A(2|1|4)$ und $B(-1|3|0)$.
> - Für welchen Wert von $t$ gilt $\begin{pmatrix} t+1 \\ 3 \\ 2t \end{pmatrix} = \begin{pmatrix} 4 \\ 3 \\ 6 \end{pmatrix}$?
> - Stelle den Vektor $\vec{v} = \begin{pmatrix} 5 \\ -2 \\ 3 \end{pmatrix}$ als Linearkombination der Standardbasisvektoren dar.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018
- Bigalke/Köhler: Mathematik – Analytische Geometrie und Lineare Algebra. Cornelsen, 2022
- Lambacher Schweizer: Mathematik für Gymnasien – Analytische Geometrie. Klett, 2023

> [!tip] **Weiterführende Links**
> - [[Einheitsvektoren]] — Normierte Vektoren der Länge 1
> - [[12-Einfuehrung-in-die-lineare-Algebra-Index|Lineare Algebra]] — Vektoren als Elemente von Vektorräumen
