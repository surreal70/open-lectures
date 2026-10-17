---
author: Andreas Hümmer
title: Anwendungen von Matrizen
tags:
  - content
  - mathe
  - lineare-algebra
  - matrizen
  - anwendungen
created: 2025-07-01
modified: 2025-07-01
---

# Anwendungen von Matrizen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Praktische Anwendungen von Matrizen in verschiedenen Bereichen kennen
> - Verstehen, wie Verflechtungsaufgaben mit Matrizen modelliert werden
> - Die Anwendung von Matrizen in der Computergrafik nachvollziehen können
> - Übergangsmatrizen bei Markov-Ketten verstehen
> - Den Nutzen der linearen Algebra in realen Problemstellungen erkennen

---

## Überblick

Matrizen sind nicht nur abstrakte mathematische Objekte, sondern finden vielfältige Anwendungen in Wirtschaft, Technik, Naturwissenschaften und Informatik. Von der Produktionsplanung über Computergrafik bis hin zu Suchmaschinen — die lineare Algebra liefert das mathematische Fundament für zahlreiche moderne Technologien.

## Verflechtungsaufgaben (Leontief-Modell)

### Problemstellung

Ein Unternehmen produziert mehrere Produkte, wobei zur Herstellung eines Produkts auch andere Produkte als Vorleistungen benötigt werden. Die Matrix beschreibt diese Verflechtung.

### Modell

Die **Technologiematrix** $A$ enthält die Produktionskoeffizienten $a_{ij}$: Wie viele Einheiten von Produkt $i$ werden benötigt, um eine Einheit von Produkt $j$ herzustellen?

$$
\vec{x} = A \cdot \vec{x} + \vec{y}
$$

- $\vec{x}$: Bruttoproduktion
- $\vec{y}$: Endnachfrage (Nettoabsatz)

Die Lösung ist:

$$
\vec{x} = (I - A)^{-1} \cdot \vec{y}
$$

### Beispiel

Zwei Sektoren (Energie, Stahl) mit Technologiematrix:

$$
A = \begin{pmatrix} 0{,}2 & 0{,}3 \\ 0{,}4 & 0{,}1 \end{pmatrix}
$$

Energie benötigt 20% Energie und 40% Stahl zur Produktion.
Stahl benötigt 30% Energie und 10% Stahl zur Produktion.

Bei Endnachfrage $\vec{y} = \begin{pmatrix} 100 \\ 80 \end{pmatrix}$:

$$
(I - A) = \begin{pmatrix} 0{,}8 & -0{,}3 \\ -0{,}4 & 0{,}9 \end{pmatrix}
$$

Nach Invertierung erhält man die erforderliche Bruttoproduktion.

## Computergrafik und Bildverarbeitung

### 2D-Transformationen

Grafikprogramme verwenden Matrizen für geometrische Transformationen:

| Transformation | Matrix |
|----------------|--------|
| Verschiebung | Homogene Koordinaten |
| Drehung um $\varphi$ | $\begin{pmatrix} \cos\varphi & -\sin\varphi \\ \sin\varphi & \cos\varphi \end{pmatrix}$ |
| Skalierung | $\begin{pmatrix} s_x & 0 \\ 0 & s_y \end{pmatrix}$ |
| Spiegelung (y-Achse) | $\begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$ |

### Homogene Koordinaten

Um auch Verschiebungen durch Matrixmultiplikation darstellen zu können, erweitert man auf **homogene Koordinaten**:

$$
\begin{pmatrix} x' \\ y' \\ 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 & t_x \\ 0 & 1 & t_y \\ 0 & 0 & 1 \end{pmatrix} \cdot \begin{pmatrix} x \\ y \\ 1 \end{pmatrix}
$$

Verschiebung um $(t_x, t_y)$.

### 3D-Grafik

In 3D-Anwendungen (Spiele, CAD) werden 4×4-Matrizen verwendet:

$$
\begin{pmatrix} x' \\ y' \\ z' \\ 1 \end{pmatrix} = M \cdot \begin{pmatrix} x \\ y \\ z \\ 1 \end{pmatrix}
$$

Die Matrix $M$ kombiniert Rotation, Skalierung, Translation und Projektion.

## Markov-Ketten und Übergangsmatrizen

### Problemstellung

Ein System kann sich in verschiedenen Zuständen befinden. Die Wahrscheinlichkeit, von einem Zustand in einen anderen zu wechseln, ist konstant.

### Übergangsmatrix

Die **Übergangsmatrix** (oder stochastische Matrix) $P$ enthält die Übergangswahrscheinlichkeiten $p_{ij}$:

$$
P = \begin{pmatrix} p_{11} & p_{12} & \cdots \\ p_{21} & p_{22} & \cdots \\ \vdots & \vdots & \ddots \end{pmatrix}
$$

wobei $p_{ij}$ die Wahrscheinlichkeit ist, von Zustand $j$ nach Zustand $i$ zu wechseln.

**Eigenschaft:** Jede Spalte summiert sich zu 1.

### Beispiel: Wettermodell

Zustände: Sonnig (S), Regnerisch (R)

$$
P = \begin{pmatrix} 0{,}8 & 0{,}4 \\ 0{,}2 & 0{,}6 \end{pmatrix}
$$

- Nach einem sonnigen Tag: 80% Sonne, 20% Regen
- Nach einem regnerischen Tag: 40% Sonne, 60% Regen

Zustandsvektor nach $n$ Tagen:

$$
\vec{p}^{(n)} = P^n \cdot \vec{p}^{(0)}
$$

## Netzwerkanalyse und PageRank

### Prinzip

Der Google-PageRank-Algorithmus bewertet Webseiten anhand ihrer Verlinkungsstruktur. Die Idee: Eine Seite ist wichtig, wenn viele wichtige Seiten auf sie verlinken.

### Mathematisches Modell

Die Linkstruktur wird als **Adjazenzmatrix** dargestellt. Der PageRank-Vektor ist der dominante Eigenvektor der modifizierten Übergangsmatrix.

$$
\vec{r} = P \cdot \vec{r}
$$

Der Vektor $\vec{r}$ ist ein Eigenvektor zum Eigenwert 1.

## Bildkompression mit SVD

Die **Singulärwertzerlegung (SVD)** zerlegt eine Matrix in:

$$
A = U \cdot \Sigma \cdot V^T
$$

Für Bildkompression:
- Behalte nur die $k$ größten Singulärwerte
- Approximiere: $A_k = U_k \cdot \Sigma_k \cdot V_k^T$
- Reduziert Speicherbedarf erheblich

## Kryptographie

### Hill-Chiffre

Verschlüsselung mit einer invertierbaren Matrix $K$:

**Verschlüsseln:** $\vec{c} = K \cdot \vec{m} \mod 26$

**Entschlüsseln:** $\vec{m} = K^{-1} \cdot \vec{c} \mod 26$

wobei $\vec{m}$ der Klartext und $\vec{c}$ der Geheimtext als Zahlenvektoren ist.

## Lösung von Differentialgleichungssystemen

Systeme linearer Differentialgleichungen:

$$
\vec{x}'(t) = A \cdot \vec{x}(t)
$$

Die Lösung hängt von den **Eigenwerten und Eigenvektoren** von $A$ ab:

$$
\vec{x}(t) = c_1 \cdot e^{\lambda_1 t} \cdot \vec{v}_1 + c_2 \cdot e^{\lambda_2 t} \cdot \vec{v}_2 + \ldots
$$

Anwendung: Schwingungssysteme, Populationsdynamik, elektrische Schaltkreise.

## Zusammenfassung der Anwendungsbereiche

| Bereich | Anwendung |
|---------|-----------|
| Wirtschaft | Verflechtungsanalyse, Optimierung |
| Informatik | Computergrafik, Suchmaschinen, Machine Learning |
| Physik | Quantenmechanik, Schwingungen |
| Technik | Regelungstechnik, Signalverarbeitung |
| Biologie | Populationsmodelle, Genetik |
| Statistik | Hauptkomponentenanalyse, Regression |

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Matrizenmultiplikation]] — Grundlage aller Anwendungen
- → [[Inverse-Matrizen]] — Lösung von Verflechtungsaufgaben
- → [[Einfuehrung-in-Eigenwerte-und-Eigenvektoren]] — PageRank, Differentialgleichungen
- → [[Lineare-Abbildungen]] — Geometrische Transformationen

> [!warning] **Prüfungsrelevant**
> - Verflechtungsaufgaben mit $(I - A)^{-1}$ lösen
> - Matrizen für geometrische Transformationen aufstellen
> - Übergangsmatrizen bei Markov-Ketten anwenden
> - Zustandsvektoren nach mehreren Schritten berechnen
> - Interpretation der Ergebnisse im Sachkontext

> [!question] **Typische Prüfungsfragen**
> - Modellieren Sie die Produktionsverflechtung als Matrixgleichung.
> - Berechnen Sie die Wahrscheinlichkeitsverteilung nach 3 Schritten.
> - Welche Matrix beschreibt die Hintereinanderausführung von Drehung und Spiegelung?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 2, Springer Vieweg
- Strang, G.: Lineare Algebra, Springer
- Leontief, W.: Input-Output Economics, Oxford University Press

> [!tip] **Weiterführende Links**
> - [[Exponentialfunktionen]] — Wachstumsprozesse in Markov-Ketten
> - [[Wachstumsprozesse]] — Anwendungen in der Modellierung
