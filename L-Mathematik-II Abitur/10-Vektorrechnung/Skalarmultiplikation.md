---
author: Andreas Hümmer
title: Skalarmultiplikation
tags:
  - content
  - mathe
  - vektorrechnung
  - skalarmultiplikation
  - streckung
  - abitur
created: 2025-01-21
modified: 2025-01-21
---

# Skalarmultiplikation

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Einen Vektor mit einem Skalar multiplizieren können
> - Die geometrische Auswirkung der Skalarmultiplikation verstehen
> - Die Rechengesetze der Skalarmultiplikation kennen und anwenden können
> - Kollinearität von Vektoren über die Skalarmultiplikation prüfen können

---

## Überblick

Die **Skalarmultiplikation** (auch S-Multiplikation genannt) ist die Multiplikation eines Vektors mit einer reellen Zahl (einem Skalar). Diese Operation ändert die Länge des Vektors und kann seine Richtung umkehren, ohne jedoch die Orientierung der Geraden zu verändern, auf der der Vektor liegt.

## Definition

Ein Vektor $\vec{a}$ wird mit einem Skalar $k \in \mathbb{R}$ multipliziert, indem jede Komponente mit $k$ multipliziert wird:

$$k \cdot \vec{a} = k \cdot \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix} = \begin{pmatrix} k \cdot a_1 \\ k \cdot a_2 \\ k \cdot a_3 \end{pmatrix}$$

### Beispielrechnung

$$3 \cdot \begin{pmatrix} 2 \\ -1 \\ 4 \end{pmatrix} = \begin{pmatrix} 3 \cdot 2 \\ 3 \cdot (-1) \\ 3 \cdot 4 \end{pmatrix} = \begin{pmatrix} 6 \\ -3 \\ 12 \end{pmatrix}$$

$$-2 \cdot \begin{pmatrix} 1 \\ 3 \\ -2 \end{pmatrix} = \begin{pmatrix} -2 \\ -6 \\ 4 \end{pmatrix}$$

## Geometrische Bedeutung

Die Skalarmultiplikation bewirkt eine **Streckung** oder **Stauchung** des Vektors:

| Wert von $k$ | Auswirkung |
|--------------|------------|
| $k > 1$ | Streckung (Vektor wird länger) |
| $0 < k < 1$ | Stauchung (Vektor wird kürzer) |
| $k = 1$ | Keine Änderung |
| $k = 0$ | Ergibt den Nullvektor |
| $-1 < k < 0$ | Stauchung und Richtungsumkehr |
| $k < -1$ | Streckung und Richtungsumkehr |
| $k = -1$ | Gegenvektor (nur Richtungsumkehr) |

### Visualisierung

```
    k = 2:     ────────────────→  (doppelt so lang)
    k = 1:     ────────→          (Originalvektor)
    k = 0.5:   ────→              (halb so lang)
    k = -1:    ←────────          (Gegenvektor)
    k = -0.5:  ←────              (halb so lang, umgekehrt)
```

## Rechengesetze

Die Skalarmultiplikation erfüllt folgende Gesetze:

| Gesetz | Formel |
|--------|--------|
| **Assoziativgesetz** | $(rs) \cdot \vec{a} = r \cdot (s \cdot \vec{a})$ |
| **Distributivgesetz I** | $r \cdot (\vec{a} + \vec{b}) = r \cdot \vec{a} + r \cdot \vec{b}$ |
| **Distributivgesetz II** | $(r + s) \cdot \vec{a} = r \cdot \vec{a} + s \cdot \vec{a}$ |
| **Neutrales Element** | $1 \cdot \vec{a} = \vec{a}$ |
| **Nullelement** | $0 \cdot \vec{a} = \vec{0}$ |

### Beweis des Distributivgesetzes I

$$r \cdot (\vec{a} + \vec{b}) = r \cdot \begin{pmatrix} a_1 + b_1 \\ a_2 + b_2 \\ a_3 + b_3 \end{pmatrix} = \begin{pmatrix} r(a_1 + b_1) \\ r(a_2 + b_2) \\ r(a_3 + b_3) \end{pmatrix}$$

$$= \begin{pmatrix} ra_1 + rb_1 \\ ra_2 + rb_2 \\ ra_3 + rb_3 \end{pmatrix} = \begin{pmatrix} ra_1 \\ ra_2 \\ ra_3 \end{pmatrix} + \begin{pmatrix} rb_1 \\ rb_2 \\ rb_3 \end{pmatrix} = r \cdot \vec{a} + r \cdot \vec{b}$$

## Auswirkung auf den Betrag

Der Betrag des skalierten Vektors ergibt sich zu:

$$|k \cdot \vec{a}| = |k| \cdot |\vec{a}|$$

**Achtung:** Der Betrag des Skalars $|k|$ geht ein, nicht $k$ selbst!

### Beispiel

Für $\vec{a} = \begin{pmatrix} 3 \\ 4 \\ 0 \end{pmatrix}$ gilt $|\vec{a}| = \sqrt{9 + 16 + 0} = 5$.

Dann: $|-2 \cdot \vec{a}| = |-2| \cdot 5 = 2 \cdot 5 = 10$

## Kollinearität (Parallelität)

Zwei Vektoren $\vec{a}$ und $\vec{b}$ (mit $\vec{a}, \vec{b} \neq \vec{0}$) sind genau dann **kollinear** (parallel), wenn einer ein Vielfaches des anderen ist:

$$\vec{a} \parallel \vec{b} \Leftrightarrow \exists k \in \mathbb{R}: \vec{a} = k \cdot \vec{b}$$

### Prüfung auf Kollinearität

**Methode:** Die Verhältnisse der entsprechenden Komponenten müssen gleich sein:

$$\frac{a_1}{b_1} = \frac{a_2}{b_2} = \frac{a_3}{b_3} = k$$

(Falls eine Komponente von $\vec{b}$ null ist, muss die entsprechende Komponente von $\vec{a}$ ebenfalls null sein.)

### Beispiel: Kollinearitätsprüfung

Sind $\vec{a} = \begin{pmatrix} 6 \\ -4 \\ 10 \end{pmatrix}$ und $\vec{b} = \begin{pmatrix} 3 \\ -2 \\ 5 \end{pmatrix}$ kollinear?

$$\frac{6}{3} = 2, \quad \frac{-4}{-2} = 2, \quad \frac{10}{5} = 2$$

Alle Verhältnisse sind gleich, also: $\vec{a} = 2 \cdot \vec{b}$ → **kollinear**.

### Gegenbeispiel

Sind $\vec{c} = \begin{pmatrix} 2 \\ 4 \\ 3 \end{pmatrix}$ und $\vec{d} = \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix}$ kollinear?

$$\frac{2}{1} = 2, \quad \frac{4}{2} = 2, \quad \frac{3}{2} = 1{,}5$$

Die Verhältnisse sind nicht alle gleich → **nicht kollinear**.

## Linearkombinationen

Eine **Linearkombination** von Vektoren entsteht durch Addition skalierter Vektoren:

$$\vec{v} = r \cdot \vec{a} + s \cdot \vec{b} + t \cdot \vec{c}$$

Diese Schreibweise ist fundamental für:
- Parameterdarstellungen von Geraden und Ebenen
- Basisdarstellungen in der linearen Algebra
- Beschreibung von Teilpunkten

### Beispiel: Geradengleichung

Die Parameterform einer Geraden durch Punkt $A$ mit Richtungsvektor $\vec{v}$:

$$\vec{x} = \vec{a} + t \cdot \vec{v}, \quad t \in \mathbb{R}$$

Hier ist $t \cdot \vec{v}$ die Skalarmultiplikation.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Grundlagen-der-Vektoren]] — Gegenvektor als Spezialfall ($k = -1$)
- → [[Vektoraddition]] — Zusammenspiel mit der Addition
- → [[Einheitsvektoren]] — Normierung durch Skalarmultiplikation
- → [[Betrag-eines-Vektors]] — Längenänderung bei Skalierung

> [!warning] **Prüfungsrelevant**
> - Komponentenweise Berechnung der Skalarmultiplikation
> - Geometrische Interpretation: Streckung, Stauchung, Richtungsumkehr
> - Rechengesetze (insbesondere Distributivgesetze)
> - Kollinearitätsprüfung über Komponentenverhältnisse
> - Aufstellen von Linearkombinationen

> [!question] **Typische Prüfungsfragen**
> - Berechne $3\vec{a} - 2\vec{b}$ für $\vec{a} = \begin{pmatrix} 1 \\ -2 \\ 4 \end{pmatrix}$ und $\vec{b} = \begin{pmatrix} 3 \\ 1 \\ -1 \end{pmatrix}$.
> - Prüfe, ob die Vektoren $\vec{p} = \begin{pmatrix} 4 \\ -6 \\ 2 \end{pmatrix}$ und $\vec{q} = \begin{pmatrix} -2 \\ 3 \\ -1 \end{pmatrix}$ kollinear sind.
> - Für welchen Wert von $k$ sind $\begin{pmatrix} k \\ 6 \\ -3 \end{pmatrix}$ und $\begin{pmatrix} 4 \\ -8 \\ 4 \end{pmatrix}$ kollinear?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018
- Lambacher Schweizer: Mathematik für Gymnasien – Analytische Geometrie. Klett, 2023
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020

> [!tip] **Weiterführende Links**
> - [[11-Analytische-Geometrie-Index|Analytische Geometrie]] — Parameterdarstellungen mit Skalarmultiplikation
> - [[12-Einfuehrung-in-die-lineare-Algebra-Index|Lineare Algebra]] — Lineare Unabhängigkeit von Vektoren
