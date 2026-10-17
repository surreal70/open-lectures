---
author: Andreas Hümmer
title: Einführung in Eigenwerte und Eigenvektoren
tags:
  - content
  - mathe
  - lineare-algebra
  - eigenwerte
  - eigenvektoren
  - matrizen
created: 2025-07-01
modified: 2025-07-01
---

# Einführung in Eigenwerte und Eigenvektoren

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Begriffe Eigenwert und Eigenvektor verstehen
> - Das charakteristische Polynom aufstellen können
> - Eigenwerte einer 2×2-Matrix berechnen können
> - Zu einem Eigenwert den zugehörigen Eigenraum bestimmen können
> - Die geometrische Bedeutung von Eigenvektoren kennen

---

## Überblick

**Eigenwerte** und **Eigenvektoren** sind fundamentale Konzepte der linearen Algebra mit weitreichenden Anwendungen in Physik, Technik und Informatik. Ein Eigenvektor einer Matrix ist ein Vektor, der bei der Matrizenmultiplikation seine Richtung beibehält und nur um einen Faktor (den Eigenwert) gestreckt oder gestaucht wird.

## Definition

### Eigenwert und Eigenvektor

Sei $A$ eine $(n \times n)$-Matrix. Ein Vektor $\vec{v} \neq \vec{0}$ heißt **Eigenvektor** von $A$ zum **Eigenwert** $\lambda$, wenn gilt:

$$
A \cdot \vec{v} = \lambda \cdot \vec{v}
$$

Die Matrix $A$ wirkt auf den Eigenvektor wie eine einfache Skalarmultiplikation.

### Geometrische Deutung

```
Eigenvektor v              Nach Anwendung von A
     │                           │
     │ ↑                         │ ↑ (gestreckt um λ)
     │ │                         │ │
     │ │                         │ │
     ──┼──                       ──┼──
       │                           │
```

- Der Eigenvektor zeigt weiterhin in dieselbe Richtung (oder entgegengesetzt, falls $\lambda < 0$)
- Die Länge ändert sich um den Faktor $|\lambda|$

## Bestimmung der Eigenwerte

### Das charakteristische Polynom

Aus $A \cdot \vec{v} = \lambda \cdot \vec{v}$ folgt:

$$
(A - \lambda I) \cdot \vec{v} = \vec{0}
$$

Damit ein nichttrivialer Eigenvektor existiert, muss gelten:

$$
\det(A - \lambda I) = 0
$$

Dies ist das **charakteristische Polynom** $p(\lambda)$ der Matrix $A$.

### Beispiel: 2×2-Matrix

$$
A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}
$$

**Schritt 1:** $A - \lambda I$ aufstellen

$$
A - \lambda I = \begin{pmatrix} 4 - \lambda & 1 \\ 2 & 3 - \lambda \end{pmatrix}
$$

**Schritt 2:** Charakteristisches Polynom berechnen

$$
\det(A - \lambda I) = (4 - \lambda)(3 - \lambda) - 1 \cdot 2 = 0
$$

$$
\lambda^2 - 7\lambda + 12 - 2 = 0
$$

$$
\lambda^2 - 7\lambda + 10 = 0
$$

**Schritt 3:** Eigenwerte bestimmen (Nullstellen)

Mit der Lösungsformel:

$$
\lambda_{1,2} = \frac{7 \pm \sqrt{49 - 40}}{2} = \frac{7 \pm 3}{2}
$$

$$
\lambda_1 = 5, \quad \lambda_2 = 2
$$

## Bestimmung der Eigenvektoren

Zu jedem Eigenwert $\lambda_i$ bestimmt man den zugehörigen **Eigenraum** durch Lösen des homogenen Systems:

$$
(A - \lambda_i I) \cdot \vec{v} = \vec{0}
$$

### Beispiel (Fortsetzung)

**Für $\lambda_1 = 5$:**

$$
(A - 5I) = \begin{pmatrix} -1 & 1 \\ 2 & -2 \end{pmatrix}
$$

Gleichungssystem: $-x + y = 0 \Rightarrow y = x$

Eigenvektor: $\vec{v}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$ (oder jedes Vielfache davon)

**Für $\lambda_2 = 2$:**

$$
(A - 2I) = \begin{pmatrix} 2 & 1 \\ 2 & 1 \end{pmatrix}
$$

Gleichungssystem: $2x + y = 0 \Rightarrow y = -2x$

Eigenvektor: $\vec{v}_2 = \begin{pmatrix} 1 \\ -2 \end{pmatrix}$

### Probe

$$
A \cdot \vec{v}_1 = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix} \cdot \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 5 \\ 5 \end{pmatrix} = 5 \cdot \begin{pmatrix} 1 \\ 1 \end{pmatrix} \checkmark
$$

## Eigenschaften von Eigenwerten

### Spur und Determinante

Für eine $(n \times n)$-Matrix mit Eigenwerten $\lambda_1, \lambda_2, \ldots, \lambda_n$ gilt:

- **Spur:** $\text{tr}(A) = a_{11} + a_{22} + \ldots + a_{nn} = \lambda_1 + \lambda_2 + \ldots + \lambda_n$
- **Determinante:** $\det(A) = \lambda_1 \cdot \lambda_2 \cdot \ldots \cdot \lambda_n$

### Für 2×2-Matrizen

$$
\lambda_1 + \lambda_2 = a_{11} + a_{22} = \text{tr}(A)
$$

$$
\lambda_1 \cdot \lambda_2 = \det(A)
$$

Dies ermöglicht eine Schnellprüfung der Ergebnisse.

### Beispiel (Kontrolle)

$\lambda_1 + \lambda_2 = 5 + 2 = 7 = 4 + 3 = \text{tr}(A)$ ✓

$\lambda_1 \cdot \lambda_2 = 5 \cdot 2 = 10 = 4 \cdot 3 - 1 \cdot 2 = \det(A)$ ✓

## Spezialfälle

### Keine reellen Eigenwerte

Das charakteristische Polynom kann komplexe Nullstellen haben:

$$
A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}
$$

$\det(A - \lambda I) = \lambda^2 + 1 = 0 \Rightarrow \lambda = \pm i$

Diese Drehmatrix (90°) hat keine reellen Eigenwerte.

### Mehrfache Eigenwerte

Ein Eigenwert kann mehrfach als Nullstelle auftreten. Die **algebraische Vielfachheit** ist die Vielfachheit als Nullstelle, die **geometrische Vielfachheit** ist die Dimension des Eigenraums.

## Anwendungen

| Bereich | Anwendung |
|---------|-----------|
| Physik | Schwingungen, Hauptachsen |
| Statistik | Hauptkomponentenanalyse (PCA) |
| Informatik | Google PageRank, Bildkompression |
| Technik | Stabilität von Systemen |

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Determinanten]] — Charakteristisches Polynom
- → [[Matrizen]] — Grundlagen
- → [[Lineare-Abbildungen]] — Eigenvektoren und Transformationen
- → [[Quadratische-Funktionen]] — Lösen quadratischer Gleichungen

> [!warning] **Prüfungsrelevant**
> - Aufstellen des charakteristischen Polynoms
> - Berechnung der Eigenwerte für 2×2-Matrizen
> - Bestimmung der Eigenvektoren durch Lösen homogener Systeme
> - Kontrolle über Spur und Determinante
> - Geometrische Interpretation

> [!question] **Typische Prüfungsfragen**
> - Bestimmen Sie die Eigenwerte und Eigenvektoren der gegebenen Matrix.
> - Überprüfen Sie, ob der gegebene Vektor ein Eigenvektor ist.
> - Welche geometrische Bedeutung hat ein Eigenwert $\lambda = 1$ bzw. $\lambda = -1$?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 2, Springer Vieweg
- Bronstein, I.N. et al.: Taschenbuch der Mathematik, Verlag Harri Deutsch
- Strang, G.: Lineare Algebra, Springer

> [!tip] **Weiterführende Links**
> - [[Anwendungen-von-Matrizen]] — Praktische Anwendungen von Eigenwerten
> - [[Lineare-Abbildungen]] — Eigenvektoren bei geometrischen Transformationen
