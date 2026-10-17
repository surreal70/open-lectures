---
author: Andreas Hümmer
title: Einführung in komplexe Zahlen
tags:
  - content
  - mathe
  - algebra
  - komplexe-zahlen
  - imaginaere-einheit
  - gausssche-ebene
created: 2025-01-13
modified: 2025-01-13
---

# Einführung in komplexe Zahlen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die imaginäre Einheit $i$ und komplexe Zahlen verstehen
> - Komplexe Zahlen in der Gaußschen Zahlenebene darstellen können
> - Die Grundrechenarten mit komplexen Zahlen beherrschen
> - Die konjugiert komplexe Zahl und den Betrag bestimmen können

---

## Überblick

Die komplexen Zahlen erweitern den Zahlbereich der reellen Zahlen, sodass auch Gleichungen wie $x^2 + 1 = 0$ lösbar werden. Durch die Einführung der imaginären Einheit $i$ mit der Eigenschaft $i^2 = -1$ entsteht ein algebraisch abgeschlossener Zahlenkörper. Komplexe Zahlen finden vielfältige Anwendungen in der Physik, Elektrotechnik und höheren Mathematik.

## Die imaginäre Einheit

### Motivation

Die Gleichung $x^2 = -1$ hat keine Lösung in $\mathbb{R}$, da das Quadrat einer reellen Zahl stets nicht-negativ ist.

**Lösung:** Man definiert eine neue Zahl $i$ mit der Eigenschaft:

$$i^2 = -1 \quad \text{bzw.} \quad i = \sqrt{-1}$$

Diese Zahl $i$ heißt **imaginäre Einheit**.

### Potenzen von $i$

$$\begin{align}
i^0 &= 1 \\
i^1 &= i \\
i^2 &= -1 \\
i^3 &= i^2 \cdot i = -i \\
i^4 &= i^2 \cdot i^2 = 1 \\
i^5 &= i \quad \text{(Zyklus wiederholt sich)}
\end{align}$$

> [!tip] **Merkhilfe**
> Die Potenzen von $i$ wiederholen sich mit Periode 4: $i^n = i^{n \mod 4}$

## Definition komplexer Zahlen

### Algebraische Form

Eine **komplexe Zahl** $z$ hat die Form:

$$z = a + bi \quad \text{mit } a, b \in \mathbb{R}$$

- $a = \text{Re}(z)$ heißt **Realteil**
- $b = \text{Im}(z)$ heißt **Imaginärteil**

**Beispiele:**
- $z_1 = 3 + 2i$ (Realteil 3, Imaginärteil 2)
- $z_2 = -1 - 4i$ (Realteil -1, Imaginärteil -4)
- $z_3 = 5$ (rein reell, Imaginärteil 0)
- $z_4 = 3i$ (rein imaginär, Realteil 0)

### Die Menge der komplexen Zahlen

$$\mathbb{C} = \{a + bi \mid a, b \in \mathbb{R}\}$$

Es gilt: $\mathbb{R} \subset \mathbb{C}$ (reelle Zahlen sind spezielle komplexe Zahlen mit $b = 0$)

## Die Gaußsche Zahlenebene

Komplexe Zahlen werden in der **Gaußschen Zahlenebene** (komplexe Ebene) dargestellt:

- **x-Achse:** Realteil (reelle Achse)
- **y-Achse:** Imaginärteil (imaginäre Achse)

Die komplexe Zahl $z = a + bi$ entspricht dem Punkt $(a, b)$ bzw. dem Pfeil vom Ursprung zu diesem Punkt.

```
     Im
      ↑
    3 +     • z = 2 + 3i
      |    /
    2 +   /
      |  /
    1 + /
      |/
------+-----→ Re
     0|  1   2   3
```

## Grundrechenarten

### Addition und Subtraktion

Komplexe Zahlen werden **komponentenweise** addiert/subtrahiert:

$$(a + bi) + (c + di) = (a + c) + (b + d)i$$

$$(a + bi) - (c + di) = (a - c) + (b - d)i$$

**Beispiel:** $(3 + 2i) + (1 - 5i) = 4 - 3i$

### Multiplikation

Man multipliziert aus und nutzt $i^2 = -1$:

$$(a + bi)(c + di) = ac + adi + bci + bdi^2 = (ac - bd) + (ad + bc)i$$

**Beispiel:**
$$(2 + 3i)(1 - 2i) = 2 - 4i + 3i - 6i^2 = 2 - i + 6 = 8 - i$$

### Division

Zur Division erweitert man mit der **konjugiert komplexen Zahl** des Nenners:

$$\frac{a + bi}{c + di} = \frac{(a + bi)(c - di)}{(c + di)(c - di)} = \frac{(a + bi)(c - di)}{c^2 + d^2}$$

**Beispiel:**
$$\frac{3 + i}{1 + 2i} = \frac{(3 + i)(1 - 2i)}{(1 + 2i)(1 - 2i)} = \frac{3 - 6i + i - 2i^2}{1 + 4} = \frac{5 - 5i}{5} = 1 - i$$

## Konjugiert komplexe Zahl und Betrag

### Konjugiert komplexe Zahl

Die **konjugiert komplexe Zahl** $\bar{z}$ zu $z = a + bi$ ist:

$$\bar{z} = a - bi$$

Geometrisch: Spiegelung an der reellen Achse.

**Eigenschaften:**
- $z + \bar{z} = 2a = 2 \cdot \text{Re}(z)$
- $z - \bar{z} = 2bi = 2i \cdot \text{Im}(z)$
- $z \cdot \bar{z} = a^2 + b^2 \in \mathbb{R}$
- $\overline{z_1 + z_2} = \bar{z_1} + \bar{z_2}$
- $\overline{z_1 \cdot z_2} = \bar{z_1} \cdot \bar{z_2}$

### Betrag einer komplexen Zahl

Der **Betrag** $|z|$ ist der Abstand vom Ursprung:

$$|z| = |a + bi| = \sqrt{a^2 + b^2}$$

**Eigenschaften:**
- $|z| \geq 0$ und $|z| = 0 \Leftrightarrow z = 0$
- $|z|^2 = z \cdot \bar{z}$
- $|z_1 \cdot z_2| = |z_1| \cdot |z_2|$
- $\left|\frac{z_1}{z_2}\right| = \frac{|z_1|}{|z_2|}$

## Quadratische Gleichungen mit komplexen Lösungen

Die Lösungsformel gilt auch für $D < 0$:

$$x^2 + px + q = 0 \quad \Rightarrow \quad x_{1,2} = -\frac{p}{2} \pm \sqrt{\frac{p^2}{4} - q}$$

**Beispiel:** $x^2 + 2x + 5 = 0$

$$x_{1,2} = -1 \pm \sqrt{1 - 5} = -1 \pm \sqrt{-4} = -1 \pm 2i$$

Die Lösungen sind $x_1 = -1 + 2i$ und $x_2 = -1 - 2i$ (konjugiert komplex).

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Gleichungen-hoeheren-Grades]] – Komplexe Lösungen von Polynomgleichungen
- → [[Faktorisierung-von-Polynomen]] – Fundamentalsatz der Algebra
- → [[Trigonometrische-Funktionen]] – Eulersche Formel (Ausblick)
- → [[Reelle-Zahlen-und-Intervalle]] – Einordnung der Zahlbereiche

> [!warning] **Prüfungsrelevant**
> - Rechnen mit komplexen Zahlen (alle Grundrechenarten)
> - Bestimmung von konjugiert komplexer Zahl und Betrag
> - Lösen quadratischer Gleichungen mit $D < 0$
> - Darstellung in der Gaußschen Zahlenebene

> [!question] **Typische Prüfungsfragen**
> - Berechne $(2 - 3i)(4 + i)$ und gib das Ergebnis in der Form $a + bi$ an.
> - Bestimme alle komplexen Lösungen von $x^2 - 4x + 13 = 0$.
> - Zeige, dass $z \cdot \bar{z} = |z|^2$ für $z = 3 + 4i$ gilt.

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Verlag Europa-Lehrmittel
- ISB Bayern: *Lehrplan Mathematik Gymnasium*

> [!tip] **Weiterführende Links**
> - [[Glossar#Komplexe Zahl|Glossar: Komplexe Zahl]]
> - [[Glossar#Imaginäre Einheit|Glossar: Imaginäre Einheit]]
