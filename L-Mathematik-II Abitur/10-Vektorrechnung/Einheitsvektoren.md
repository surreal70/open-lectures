---
author: Andreas Hümmer
title: Einheitsvektoren
tags:
  - content
  - mathe
  - vektorrechnung
  - einheitsvektoren
  - normierung
  - abitur
created: 2025-01-21
modified: 2025-01-21
---

# Einheitsvektoren

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Einheitsvektoren definieren und ihre Bedeutung erklären können
> - Jeden Vektor auf einen Einheitsvektor normieren können
> - Die Standardbasisvektoren $\vec{e}_1, \vec{e}_2, \vec{e}_3$ kennen und verwenden können
> - Richtungsvektoren mit festgelegter Länge berechnen können

---

## Überblick

Ein **Einheitsvektor** ist ein Vektor mit dem Betrag 1. Einheitsvektoren spielen eine zentrale Rolle in der Vektorrechnung: Sie beschreiben reine Richtungen ohne Berücksichtigung einer bestimmten Länge. Die Umwandlung eines beliebigen Vektors in einen Einheitsvektor heißt **Normierung** und ist eine häufig benötigte Operation.

## Definition

Ein Vektor $\vec{e}$ heißt **Einheitsvektor**, wenn gilt:

$$|\vec{e}| = 1$$

Zu jedem Vektor $\vec{a} \neq \vec{0}$ existiert genau ein Einheitsvektor $\vec{e}_a$, der in dieselbe Richtung zeigt.

## Normierung eines Vektors

### Formel

Der Einheitsvektor $\vec{e}_a$ in Richtung von $\vec{a}$ berechnet sich durch:

$$\vec{e}_a = \frac{\vec{a}}{|\vec{a}|} = \frac{1}{|\vec{a}|} \cdot \vec{a}$$

Man dividiert den Vektor durch seinen eigenen Betrag.

### Beispielrechnung 1

Normiere den Vektor $\vec{a} = \begin{pmatrix} 3 \\ 4 \\ 0 \end{pmatrix}$.

**Schritt 1:** Betrag berechnen
$$|\vec{a}| = \sqrt{3^2 + 4^2 + 0^2} = \sqrt{25} = 5$$

**Schritt 2:** Normieren
$$\vec{e}_a = \frac{1}{5} \cdot \begin{pmatrix} 3 \\ 4 \\ 0 \end{pmatrix} = \begin{pmatrix} 0{,}6 \\ 0{,}8 \\ 0 \end{pmatrix}$$

**Probe:**
$$|\vec{e}_a| = \sqrt{0{,}6^2 + 0{,}8^2} = \sqrt{0{,}36 + 0{,}64} = \sqrt{1} = 1 \checkmark$$

### Beispielrechnung 2

Normiere den Vektor $\vec{b} = \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix}$.

**Betrag:** $|\vec{b}| = \sqrt{1 + 4 + 4} = \sqrt{9} = 3$

**Einheitsvektor:**
$$\vec{e}_b = \frac{1}{3} \cdot \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix} = \begin{pmatrix} \frac{1}{3} \\ \frac{2}{3} \\ \frac{2}{3} \end{pmatrix}$$

## Standardbasisvektoren

Die **Standardbasisvektoren** (auch kanonische Basisvektoren) sind die Einheitsvektoren entlang der Koordinatenachsen:

$$\vec{e}_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \quad \vec{e}_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \quad \vec{e}_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$$

### Eigenschaften der Standardbasisvektoren

| Eigenschaft | Formel |
|-------------|--------|
| Betrag | $|\vec{e}_i| = 1$ für $i = 1, 2, 3$ |
| Orthogonalität | $\vec{e}_i \cdot \vec{e}_j = 0$ für $i \neq j$ |
| Skalarprodukt mit sich selbst | $\vec{e}_i \cdot \vec{e}_i = 1$ |

### Darstellung beliebiger Vektoren

Jeder Vektor lässt sich als **Linearkombination** der Standardbasisvektoren schreiben:

$$\vec{a} = \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix} = a_1 \vec{e}_1 + a_2 \vec{e}_2 + a_3 \vec{e}_3$$

Die Komponenten sind die Koeffizienten der Linearkombination.

## Vektor mit vorgegebener Länge und Richtung

Häufige Aufgabe: Finde einen Vektor mit Richtung $\vec{a}$ und vorgegebener Länge $\ell$.

### Formel

$$\vec{v} = \ell \cdot \frac{\vec{a}}{|\vec{a}|} = \ell \cdot \vec{e}_a$$

### Beispiel

Gesucht ist ein Vektor mit Länge 10 in Richtung von $\vec{a} = \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix}$.

**Lösung:**
$$|\vec{a}| = 3$$

$$\vec{v} = 10 \cdot \frac{1}{3} \cdot \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix} = \begin{pmatrix} \frac{10}{3} \\ \frac{20}{3} \\ \frac{20}{3} \end{pmatrix}$$

**Probe:** $|\vec{v}| = \frac{10}{3} \cdot \sqrt{1 + 4 + 4} = \frac{10}{3} \cdot 3 = 10 \checkmark$

## Anwendungen von Einheitsvektoren

### 1. Richtungsangaben in der Physik

Kräfte, Geschwindigkeiten und andere vektorielle Größen werden oft in Betrag und Richtung zerlegt:

$$\vec{F} = F \cdot \vec{e}_F$$

wobei $F = |\vec{F}|$ der Betrag und $\vec{e}_F$ der Richtungseinheitsvektor ist.

### 2. Normalenvektoren

In der analytischen Geometrie werden Normalenvektoren von Ebenen oft normiert, um einheitliche Abstandsformeln zu erhalten.

### 3. Richtungskosinus

Die Komponenten eines Einheitsvektors heißen **Richtungskosinus**:

$$\vec{e}_a = \begin{pmatrix} \cos\alpha \\ \cos\beta \\ \cos\gamma \end{pmatrix}$$

wobei $\alpha, \beta, \gamma$ die Winkel zur $x$-, $y$- bzw. $z$-Achse sind.

Es gilt: $\cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1$

## Einheitsvektoren in der Ebene

In $\mathbb{R}^2$ kann man alle Einheitsvektoren durch einen Winkel $\varphi$ parametrisieren:

$$\vec{e}(\varphi) = \begin{pmatrix} \cos\varphi \\ \sin\varphi \end{pmatrix}$$

```
              90°
               ↑
         135°  |  45°
           \   |   /
            \  |  /
             \ | /
    180° ←────●────→ 0°
             / | \
            /  |  \
           /   |   \
         225°  |  315°
               ↓
              270°
```

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Betrag-eines-Vektors]] — Betragsberechnung für die Normierung
- → [[Skalarmultiplikation]] — Streckung auf gewünschte Länge
- → [[Vektordarstellung]] — Standardbasisvektoren als Darstellungsgrundlage
- → [[Skalarprodukt]] — Orthogonalität der Standardbasisvektoren

> [!warning] **Prüfungsrelevant**
> - Normierungsformel: $\vec{e}_a = \frac{\vec{a}}{|\vec{a}|}$
> - Berechnung von Einheitsvektoren (mit Probe)
> - Standardbasisvektoren und ihre Eigenschaften
> - Konstruktion von Vektoren mit vorgegebener Länge und Richtung
> - Richtungskosinus bei Einheitsvektoren

> [!question] **Typische Prüfungsfragen**
> - Bestimme den Einheitsvektor in Richtung von $\vec{a} = \begin{pmatrix} 2 \\ -1 \\ 2 \end{pmatrix}$.
> - Berechne einen Vektor der Länge 6, der in Richtung von $\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$ zeigt.
> - Erkläre, warum die Standardbasisvektoren paarweise orthogonal sind.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018
- Lambacher Schweizer: Mathematik für Gymnasien – Analytische Geometrie. Klett, 2023
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020

> [!tip] **Weiterführende Links**
> - [[Orthogonalitaet]] — Orthonormalsysteme aus Einheitsvektoren
> - [[11-Analytische-Geometrie-Index|Analytische Geometrie]] — Normaleneinheitsvektoren bei Ebenen
