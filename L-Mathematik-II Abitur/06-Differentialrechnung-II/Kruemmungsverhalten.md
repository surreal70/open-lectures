---
author: Andreas Hümmer
title: Krümmungsverhalten
tags:
  - content
  - mathe
  - differentialrechnung
  - kruemmung
  - analysis
created: 2025-06-20
modified: 2025-06-20
---

# Krümmungsverhalten

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Links- und Rechtskrümmung anhand der zweiten Ableitung bestimmen können
> - Den Zusammenhang zwischen Krümmung und Monotonie von $f'$ verstehen
> - Krümmungsintervalle systematisch bestimmen können
> - Die Krümmungsformel kennen und anwenden können

---

## Überblick

Das **Krümmungsverhalten** beschreibt, wie sich die Steigung einer Funktion ändert – ob sie zunimmt oder abnimmt. Während die erste Ableitung angibt, ob die Funktion steigt oder fällt, zeigt die zweite Ableitung, wie sich diese Steigung verändert. Geometrisch bedeutet dies, ob der Graph nach oben oder nach unten gebogen ist.

## Arten der Krümmung

### Linkskrümmung (konvex)

Eine Funktion ist **linksgekrümmt** (konvex, nach oben geöffnet), wenn:
- Die Tangenten unterhalb des Graphen verlaufen
- Die Steigung zunimmt (Funktion „biegt nach oben")
- $f''(x) > 0$

**Merkhilfe:** Die Kurve sieht aus wie ein Tal oder eine nach oben geöffnete Schale.

### Rechtskrümmung (konkav)

Eine Funktion ist **rechtsgekrümmt** (konkav, nach unten geöffnet), wenn:
- Die Tangenten oberhalb des Graphen verlaufen
- Die Steigung abnimmt (Funktion „biegt nach unten")
- $f''(x) < 0$

**Merkhilfe:** Die Kurve sieht aus wie ein Berg oder eine nach unten geöffnete Schale.

## Krümmungskriterium

> [!note] **Satz: Krümmungskriterium**
> Sei $f$ zweimal differenzierbar auf einem Intervall $I$. Dann gilt:
> - $f''(x) > 0$ für alle $x \in I$ $\Rightarrow$ $f$ ist auf $I$ linksgekrümmt
> - $f''(x) < 0$ für alle $x \in I$ $\Rightarrow$ $f$ ist auf $I$ rechtsgekrümmt

**Zusammenhang mit der ersten Ableitung:**

| $f''(x)$ | $f'$ ist... | Graph ist... |
|----------|-------------|--------------|
| $> 0$ | streng monoton steigend | linksgekrümmt |
| $< 0$ | streng monoton fallend | rechtsgekrümmt |
| $= 0$ | stationär | mögl. Wendepunkt |

## Bestimmung der Krümmungsintervalle

### Vorgehensweise

**Schritt 1:** Berechne $f''(x)$

**Schritt 2:** Bestimme Nullstellen von $f''(x)$

**Schritt 3:** Berücksichtige Definitionslücken

**Schritt 4:** Untersuche das Vorzeichen von $f''$ in den Intervallen

**Schritt 5:** Gib Krümmungsintervalle an

### Beispiel 1: Ganzrationale Funktion

Gegeben: $f(x) = x^4 - 6x^2$

**Ableitungen:**
$$f'(x) = 4x^3 - 12x$$
$$f''(x) = 12x^2 - 12 = 12(x^2 - 1) = 12(x-1)(x+1)$$

**Nullstellen von f'':**
$$f''(x) = 0 \implies x_1 = -1, \quad x_2 = 1$$

**Vorzeichenuntersuchung:**

| Intervall | $(-\infty, -1)$ | $(-1, 1)$ | $(1, \infty)$ |
|-----------|-----------------|-----------|----------------|
| $f''(x)$ | $+$ | $-$ | $+$ |
| Krümmung | links | rechts | links |

**Ergebnis:**
- Linksgekrümmt auf $(-\infty, -1)$ und $(1, \infty)$
- Rechtsgekrümmt auf $(-1, 1)$
- Wendepunkte bei $x = -1$ und $x = 1$

### Beispiel 2: Exponentialfunktion

Gegeben: $f(x) = e^{-x^2}$

**Ableitungen (Kettenregel):**
$$f'(x) = e^{-x^2} \cdot (-2x) = -2x \cdot e^{-x^2}$$

$$f''(x) = -2 \cdot e^{-x^2} + (-2x) \cdot (-2x) \cdot e^{-x^2} = e^{-x^2}(4x^2 - 2) = 2e^{-x^2}(2x^2 - 1)$$

**Nullstellen von f'':**
$$f''(x) = 0 \implies 2x^2 - 1 = 0 \implies x = \pm\frac{1}{\sqrt{2}} = \pm\frac{\sqrt{2}}{2}$$

Da $e^{-x^2} > 0$ immer, hängt das Vorzeichen nur von $(2x^2 - 1)$ ab:

| Intervall | $\left(-\infty, -\frac{\sqrt{2}}{2}\right)$ | $\left(-\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2}\right)$ | $\left(\frac{\sqrt{2}}{2}, \infty\right)$ |
|-----------|---------------------------|---------------------------|---------------------------|
| $2x^2 - 1$ | $+$ | $-$ | $+$ |
| Krümmung | links | rechts | links |

## Die Krümmungsformel

Die **Krümmung** $\kappa$ (Kappa) einer Kurve an der Stelle $x$ ist definiert als:

$$\kappa(x) = \frac{|f''(x)|}{(1 + (f'(x))^2)^{3/2}}$$

Der **Krümmungsradius** ist der Kehrwert:

$$r(x) = \frac{1}{\kappa(x)} = \frac{(1 + (f'(x))^2)^{3/2}}{|f''(x)|}$$

**Hinweis:** Im Abitur wird meist nur das Vorzeichen von $f''$ zur Krümmungsbestimmung verwendet, nicht die vollständige Krümmungsformel.

### Beispiel: Krümmung einer Parabel

Für $f(x) = x^2$ im Scheitelpunkt $(0|0)$:

$$f'(x) = 2x \implies f'(0) = 0$$
$$f''(x) = 2 \implies f''(0) = 2$$

$$\kappa(0) = \frac{|2|}{(1 + 0)^{3/2}} = 2$$

$$r(0) = \frac{1}{2} = 0{,}5$$

Der Krümmungskreis im Scheitelpunkt hat Radius $0{,}5$.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Hoehere-Ableitungen]] – Zweite Ableitung als Grundlage
- → [[Wendepunkte]] – Krümmungswechsel
- → [[Extremstellen]] – Krümmung zur Klassifikation
- → [[Monotonieverhalten]] – Monotonie von $f'$ und Krümmung
- → [[Vollstaendige-Kurvendiskussion]] – Einbettung in die Analyse

> [!warning] **Prüfungsrelevant**
> - $f''(x) > 0$ → linksgekrümmt (konvex)
> - $f''(x) < 0$ → rechtsgekrümmt (konkav)
> - Nullstellen von $f''$ sind potenzielle Wendestellen
> - Linkskrümmung = Steigung nimmt zu, Rechtskrümmung = Steigung nimmt ab
> - Die vollständige Krümmungsformel ist im Abitur selten gefragt

> [!question] **Typische Prüfungsfragen**
> - Bestimmen Sie die Intervalle, in denen der Graph links- bzw. rechtsgekrümmt ist
> - Begründen Sie anhand von $f''$, dass der Graph eine Linkskurve beschreibt
> - Wie hängt das Krümmungsverhalten mit den Wendepunkten zusammen?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020
- ISB Bayern: Lehrplan Mathematik Gymnasium (LehrplanPLUS)

> [!tip] **Weiterführende Links**
> - [[Wendepunkte]] – Stellen des Krümmungswechsels
> - [[Anwendungen-in-Physik-und-Technik]] – Krümmung bei Bahnkurven
