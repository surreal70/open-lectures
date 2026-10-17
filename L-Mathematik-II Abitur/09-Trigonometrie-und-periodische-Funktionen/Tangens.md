---
author: Andreas Hümmer
title: Tangens
tags:
  - content
  - mathe
  - trigonometrie
  - tangens
  - kotangens
  - winkelfunktionen
created: 2025-06-20
modified: 2025-06-20
---

# Tangens

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Tangens als Quotient von Sinus und Kosinus definieren können
> - Den Graphen der Tangensfunktion mit Polstellen skizzieren können
> - Die Periode und Symmetrie des Tangens kennen
> - Tangenswerte besonderer Winkel berechnen können

---

## Überblick

Der **Tangens** ist die dritte wichtige trigonometrische Funktion neben Sinus und Kosinus. Er ist definiert als der Quotient aus Sinus und Kosinus und hat im Gegensatz zu diesen **keine beschränkten Funktionswerte**. Der Tangens ist besonders wichtig für die Beschreibung von Steigungen und spielt in der Analysis und Physik eine zentrale Rolle.

## Definition

### Als Quotient

Der Tangens ist definiert als:

$$\tan(\alpha) = \frac{\sin(\alpha)}{\cos(\alpha)}$$

Diese Definition gilt für alle $\alpha$, bei denen $\cos(\alpha) \neq 0$.

### Im rechtwinkligen Dreieck

Für spitze Winkel $\alpha$ gilt:

$$\tan(\alpha) = \frac{\text{Gegenkathete}}{\text{Ankathete}} = \frac{a}{b}$$

### Am Einheitskreis

Am Einheitskreis entspricht der Tangens der **Länge des Tangentenabschnitts**:

```
     y
     |     /P(cos α, sin α)
     |    /
     |   /
     |  / tan α
     | /__|
     |/   |
     +----+-------- x
         1
```

Genauer: Verlängert man den Strahl vom Ursprung durch $P$ bis zur Tangente $x = 1$, ist die $y$-Koordinate des Schnittpunkts gleich $\tan(\alpha)$.

## Funktionsgraph

### Charakteristika

```
   y
   |           |           |
   |     *     |     *     |
   |    *      |    *      |
   |   *       |   *       |
   +---*-------+---*-------+---> x
   |   *       |   *       |
   |    *      |    *      |
   |     *     |     *     |
   |           |           |
  -π/2        π/2        3π/2
```

Der Graph:
- Hat **senkrechte Asymptoten** (Polstellen) bei $x = \frac{\pi}{2} + k\pi$
- Ist **streng monoton steigend** zwischen den Polstellen
- Geht durch den Ursprung

### Polstellen

Der Tangens ist **nicht definiert** für:

$$x = \frac{\pi}{2} + k\pi, \quad k \in \mathbb{Z}$$

Das sind die Stellen, an denen $\cos(x) = 0$.

In der Nähe der Polstellen gilt:
$$\lim_{x \to \frac{\pi}{2}^-} \tan(x) = +\infty$$
$$\lim_{x \to \frac{\pi}{2}^+} \tan(x) = -\infty$$

## Eigenschaften

### Definitionsbereich und Wertebereich

| Eigenschaft | Wert |
|-------------|------|
| Definitionsbereich | $\mathbb{R} \setminus \left\{\frac{\pi}{2} + k\pi \mid k \in \mathbb{Z}\right\}$ |
| Wertebereich | $\mathbb{R}$ (alle reellen Zahlen) |

### Periodizität

Der Tangens hat die **Periode $\pi$** (nicht $2\pi$ wie Sinus und Kosinus):

$$\tan(x + \pi) = \tan(x)$$

### Symmetrie

Der Tangens ist eine **ungerade Funktion** (punktsymmetrisch zum Ursprung):

$$\tan(-x) = -\tan(x)$$

### Nullstellen

$$\tan(x) = 0 \quad \Leftrightarrow \quad x = k\pi, \quad k \in \mathbb{Z}$$

Die Nullstellen des Tangens sind genau die Nullstellen des Sinus.

## Wichtige Funktionswerte

| $x$ (rad) | $x$ (Grad) | $\tan(x)$ |
|-----------|------------|-----------|
| $0$ | $0°$ | $0$ |
| $\frac{\pi}{6}$ | $30°$ | $\frac{1}{\sqrt{3}} = \frac{\sqrt{3}}{3}$ |
| $\frac{\pi}{4}$ | $45°$ | $1$ |
| $\frac{\pi}{3}$ | $60°$ | $\sqrt{3}$ |
| $\frac{\pi}{2}$ | $90°$ | nicht definiert |
| $\frac{3\pi}{4}$ | $135°$ | $-1$ |
| $\pi$ | $180°$ | $0$ |

### Merkregel

$$\tan(45°) = 1$$

Das liegt daran, dass bei $45°$ Gegenkathete und Ankathete gleich lang sind.

## Tangens und Steigung

### Steigungswinkel einer Geraden

Für eine Gerade mit Steigung $m$ gilt:

$$m = \tan(\alpha)$$

wobei $\alpha$ der **Steigungswinkel** ist (Winkel zur positiven $x$-Achse).

### Beispiel

Eine Gerade mit Steigung $m = 1$ hat den Steigungswinkel:
$$\alpha = \arctan(1) = 45°$$

Eine Gerade mit Steigung $m = \sqrt{3}$ hat den Steigungswinkel:
$$\alpha = \arctan(\sqrt{3}) = 60°$$

## Ableitung und Stammfunktion

Die Ableitung des Tangens:

$$\frac{d}{dx}\tan(x) = \frac{1}{\cos^2(x)} = 1 + \tan^2(x)$$

Die Stammfunktion:

$$\int \tan(x) \, dx = -\ln|\cos(x)| + C = \ln|\sec(x)| + C$$

## Der Kotangens

### Definition

Der **Kotangens** ist der Kehrwert des Tangens:

$$\cot(\alpha) = \frac{1}{\tan(\alpha)} = \frac{\cos(\alpha)}{\sin(\alpha)}$$

### Eigenschaften

- Polstellen bei $x = k\pi$ (wo $\sin(x) = 0$)
- Periode: $\pi$
- Ungerade Funktion

Im Abitur spielt der Kotangens eine untergeordnete Rolle.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Sinus-und-Kosinus]] – Grundlage für die Tangensdefinition
- → [[Einheitskreis]] – Geometrische Interpretation
- → [[Trigonometrische-Identitaeten]] – Beziehungen mit Tangens
- → [[Trigonometrische-Gleichungen]] – Gleichungen mit Tangens lösen

> [!warning] **Prüfungsrelevant**
> - Definition als Quotient: $\tan(x) = \frac{\sin(x)}{\cos(x)}$
> - Die Polstellen bei $x = \frac{\pi}{2} + k\pi$ kennen
> - Die Periode $\pi$ (nicht $2\pi$!)
> - Zusammenhang mit Geradensteigung: $m = \tan(\alpha)$

> [!question] **Typische Prüfungsfragen**
> - Bestimmen Sie den Definitionsbereich von $f(x) = \tan(2x)$.
> - Eine Gerade hat die Steigung $m = -1$. Welchen Winkel schließt sie mit der positiven $x$-Achse ein?
> - Berechnen Sie $\tan(120°)$ ohne Taschenrechner.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020.
- Lambacher Schweizer: Mathematik für Gymnasien, Oberstufe. Klett Verlag, 2019.

> [!tip] **Weiterführende Links**
> - [[Trigonometrische-Gleichungen]] – Tangens in Gleichungen
> - [[05-Differentialrechnung-I-Index]] – Ableitung des Tangens
