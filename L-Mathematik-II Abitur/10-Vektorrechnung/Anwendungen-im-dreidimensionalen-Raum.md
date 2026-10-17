---
author: Andreas Hümmer
title: Anwendungen im dreidimensionalen Raum
tags:
  - content
  - mathe
  - vektorrechnung
  - anwendungen
  - raumgeometrie
  - abitur
created: 2025-01-21
modified: 2025-01-21
---

# Anwendungen im dreidimensionalen Raum

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Flächeninhalte von Dreiecken und Parallelogrammen mit Vektoren berechnen können
> - Volumen von Parallelepipeden und Tetraedern bestimmen können
> - Das Spatprodukt anwenden können
> - Geometrische Probleme systematisch mit Vektormethoden lösen können

---

## Überblick

Die Vektorrechnung entfaltet ihre volle Stärke bei der Lösung geometrischer Probleme im dreidimensionalen Raum. Dieses Kapitel fasst die wichtigsten Anwendungen zusammen: von der Flächenberechnung über Volumenbestimmungen bis hin zu praktischen Problemlösungsstrategien.

## Flächenberechnungen

### Flächeninhalt eines Parallelogramms

Das Parallelogramm, das von zwei Vektoren $\vec{a}$ und $\vec{b}$ aufgespannt wird, hat den Flächeninhalt:

$$A_{\text{Parallelogramm}} = |\vec{a} \times \vec{b}|$$

**Herleitung:** Der Betrag des Kreuzprodukts entspricht $|\vec{a}| \cdot |\vec{b}| \cdot \sin\varphi$, was genau die Formel für die Parallelogrammfläche ist.

### Flächeninhalt eines Dreiecks

Ein Dreieck ist die Hälfte eines Parallelogramms:

$$A_{\triangle} = \frac{1}{2} |\vec{a} \times \vec{b}|$$

wobei $\vec{a}$ und $\vec{b}$ zwei Seitenvektoren des Dreiecks sind.

### Beispielrechnung: Dreiecksflächeninhalt

Berechne den Flächeninhalt des Dreiecks $ABC$ mit $A(1|0|0)$, $B(0|2|0)$, $C(0|0|3)$.

**Schritt 1:** Seitenvektoren bestimmen
$$\vec{AB} = \begin{pmatrix} -1 \\ 2 \\ 0 \end{pmatrix}, \quad \vec{AC} = \begin{pmatrix} -1 \\ 0 \\ 3 \end{pmatrix}$$

**Schritt 2:** Kreuzprodukt berechnen
$$\vec{AB} \times \vec{AC} = \begin{pmatrix} 2 \cdot 3 - 0 \cdot 0 \\ 0 \cdot (-1) - (-1) \cdot 3 \\ (-1) \cdot 0 - 2 \cdot (-1) \end{pmatrix} = \begin{pmatrix} 6 \\ 3 \\ 2 \end{pmatrix}$$

**Schritt 3:** Betrag berechnen
$$|\vec{AB} \times \vec{AC}| = \sqrt{36 + 9 + 4} = \sqrt{49} = 7$$

**Schritt 4:** Dreiecksfläche
$$A_{\triangle} = \frac{1}{2} \cdot 7 = 3{,}5 \text{ FE}$$

## Das Spatprodukt

Das **Spatprodukt** (auch gemischtes Produkt oder Tripel-Skalarprodukt) ist definiert als:

$$[\vec{a}, \vec{b}, \vec{c}] = \vec{a} \cdot (\vec{b} \times \vec{c})$$

Es kann auch als Determinante geschrieben werden:

$$[\vec{a}, \vec{b}, \vec{c}] = \begin{vmatrix} a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \\ c_1 & c_2 & c_3 \end{vmatrix}$$

### Eigenschaften des Spatprodukts

| Eigenschaft | Formel |
|-------------|--------|
| Zyklische Vertauschung | $[\vec{a}, \vec{b}, \vec{c}] = [\vec{b}, \vec{c}, \vec{a}] = [\vec{c}, \vec{a}, \vec{b}]$ |
| Antizyklische Vertauschung | $[\vec{a}, \vec{b}, \vec{c}] = -[\vec{b}, \vec{a}, \vec{c}]$ |
| Linearität | $[\vec{a}, \vec{b}, k\vec{c}] = k[\vec{a}, \vec{b}, \vec{c}]$ |

## Volumenberechnungen

### Volumen eines Parallelepipeds (Spat)

Das **Parallelepiped** (Spat) ist das dreidimensionale Analogon zum Parallelogramm. Das von drei Vektoren $\vec{a}$, $\vec{b}$, $\vec{c}$ aufgespannte Parallelepiped hat das Volumen:

$$V_{\text{Spat}} = |[\vec{a}, \vec{b}, \vec{c}]| = |\vec{a} \cdot (\vec{b} \times \vec{c})|$$

```
           c
          /
         /________
        /|       /|
       / |      / |
      /__|_____/  |
      |  |_____|__|
    a |  /     |  / b
      | /      | /
      |/_______|/
```

### Volumen eines Tetraeders

Ein **Tetraeder** (dreiseitige Pyramide) mit einer Ecke im Ursprung und Kantenvektoren $\vec{a}$, $\vec{b}$, $\vec{c}$ hat das Volumen:

$$V_{\text{Tetraeder}} = \frac{1}{6} |[\vec{a}, \vec{b}, \vec{c}]|$$

Dies folgt daraus, dass ein Tetraeder ein Sechstel des umgebenden Parallelepipeds ausmacht.

### Beispielrechnung: Tetraedervolumen

Berechne das Volumen des Tetraeders mit den Eckpunkten $O(0|0|0)$, $A(3|0|0)$, $B(0|4|0)$, $C(0|0|2)$.

**Schritt 1:** Kantenvektoren
$$\vec{a} = \begin{pmatrix} 3 \\ 0 \\ 0 \end{pmatrix}, \quad \vec{b} = \begin{pmatrix} 0 \\ 4 \\ 0 \end{pmatrix}, \quad \vec{c} = \begin{pmatrix} 0 \\ 0 \\ 2 \end{pmatrix}$$

**Schritt 2:** Kreuzprodukt $\vec{b} \times \vec{c}$
$$\vec{b} \times \vec{c} = \begin{pmatrix} 4 \cdot 2 - 0 \cdot 0 \\ 0 \cdot 0 - 0 \cdot 2 \\ 0 \cdot 0 - 4 \cdot 0 \end{pmatrix} = \begin{pmatrix} 8 \\ 0 \\ 0 \end{pmatrix}$$

**Schritt 3:** Spatprodukt
$$[\vec{a}, \vec{b}, \vec{c}] = \vec{a} \cdot (\vec{b} \times \vec{c}) = 3 \cdot 8 + 0 + 0 = 24$$

**Schritt 4:** Tetraedervolumen
$$V = \frac{1}{6} \cdot |24| = 4 \text{ VE}$$

## Allgemeines Tetraeder

Für ein Tetraeder mit beliebigen Eckpunkten $P_1$, $P_2$, $P_3$, $P_4$:

$$V = \frac{1}{6} |[\vec{P_1P_2}, \vec{P_1P_3}, \vec{P_1P_4}]|$$

### Beispiel

Tetraeder mit $A(1|2|3)$, $B(4|2|3)$, $C(1|6|3)$, $D(1|2|8)$

Kantenvektoren von $A$ aus:
$$\vec{AB} = \begin{pmatrix} 3 \\ 0 \\ 0 \end{pmatrix}, \quad \vec{AC} = \begin{pmatrix} 0 \\ 4 \\ 0 \end{pmatrix}, \quad \vec{AD} = \begin{pmatrix} 0 \\ 0 \\ 5 \end{pmatrix}$$

$$\vec{AC} \times \vec{AD} = \begin{pmatrix} 20 \\ 0 \\ 0 \end{pmatrix}$$

$$[\vec{AB}, \vec{AC}, \vec{AD}] = 3 \cdot 20 = 60$$

$$V = \frac{1}{6} \cdot 60 = 10 \text{ VE}$$

## Prüfung auf Komplanarität

Drei Vektoren $\vec{a}$, $\vec{b}$, $\vec{c}$ liegen genau dann in einer Ebene (sind komplanar), wenn:

$$[\vec{a}, \vec{b}, \vec{c}] = 0$$

Dies bedeutet: Das aufgespannte Parallelepiped hat kein Volumen – die Vektoren sind linear abhängig.

### Anwendung: Punktprüfung

Vier Punkte $A$, $B$, $C$, $D$ liegen genau dann in einer Ebene, wenn:

$$[\vec{AB}, \vec{AC}, \vec{AD}] = 0$$

## Zusammenfassung der Formeln

| Objekt | Formel |
|--------|--------|
| Dreiecksflächeninhalt | $A = \frac{1}{2}|\vec{a} \times \vec{b}|$ |
| Parallelogrammfläche | $A = |\vec{a} \times \vec{b}|$ |
| Tetraedervolumen | $V = \frac{1}{6}|[\vec{a}, \vec{b}, \vec{c}]|$ |
| Spatvolumen | $V = |[\vec{a}, \vec{b}, \vec{c}]|$ |
| Pyramidenvolumen (allg.) | $V = \frac{1}{3} \cdot A_{\text{Grundfläche}} \cdot h$ |

## Problemlösungsstrategie

Bei räumlichen Geometrieaufgaben:

1. **Koordinatensystem wählen** – günstig: Ein Punkt im Ursprung, Kanten entlang der Achsen
2. **Punkte als Ortsvektoren** notieren
3. **Verbindungsvektoren** berechnen (Spitze minus Fuß)
4. **Passende Operationen** auswählen:
   - Länge → Betrag
   - Winkel → Skalarprodukt
   - Senkrechter Vektor → Kreuzprodukt
   - Fläche → Kreuzprodukt-Betrag
   - Volumen → Spatprodukt
5. **Ergebnis interpretieren** und auf Plausibilität prüfen

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Kreuzprodukt]] — Grundlage für Flächenberechnungen
- → [[Skalarprodukt]] — Für Winkel und Projektionen
- → [[Betrag-eines-Vektors]] — Längen- und Abstandsberechnungen
- → [[11-Analytische-Geometrie-Index|Analytische Geometrie]] — Weiterführende Anwendungen

> [!warning] **Prüfungsrelevant**
> - Dreiecksfläche: $A = \frac{1}{2}|\vec{a} \times \vec{b}|$
> - Tetraedervolumen: $V = \frac{1}{6}|[\vec{a}, \vec{b}, \vec{c}]|$
> - Spatprodukt berechnen und interpretieren
> - Komplanarität über $[\vec{a}, \vec{b}, \vec{c}] = 0$ prüfen
> - Systematische Vorgehensweise bei räumlichen Aufgaben

> [!question] **Typische Prüfungsfragen**
> - Berechne den Flächeninhalt des Dreiecks mit den Eckpunkten $A(1|1|0)$, $B(3|0|0)$, $C(0|2|2)$.
> - Bestimme das Volumen des Tetraeders $ABCD$ mit $A(0|0|0)$, $B(2|0|0)$, $C(0|3|0)$, $D(0|0|4)$.
> - Prüfe, ob die vier Punkte $P(1|0|0)$, $Q(0|1|0)$, $R(0|0|1)$, $S(1|1|1)$ in einer Ebene liegen.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018
- Lambacher Schweizer: Mathematik für Gymnasien – Analytische Geometrie. Klett, 2023
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020

> [!tip] **Weiterführende Links**
> - [[11-Analytische-Geometrie-Index|Analytische Geometrie]] — Geraden, Ebenen und ihre Lagebeziehungen
> - [[12-Einfuehrung-in-die-lineare-Algebra-Index|Lineare Algebra]] — Determinanten und lineare Abhängigkeit
