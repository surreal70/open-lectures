---
author: Andreas Hümmer
title: Wendepunkte
tags:
  - content
  - mathe
  - differentialrechnung
  - wendepunkte
  - kruemmung
created: 2025-06-20
modified: 2025-06-20
---

# Wendepunkte

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Wendepunkte als Stellen des Krümmungswechsels verstehen
> - Die notwendige und hinreichende Bedingung für Wendepunkte kennen
> - Wendepunkte systematisch berechnen können
> - Wendestellen von Sattelpunkten unterscheiden können

---

## Überblick

Ein **Wendepunkt** ist ein Punkt auf dem Graphen einer Funktion, an dem sich das Krümmungsverhalten ändert – die Kurve wechselt von einer Links- in eine Rechtskrümmung oder umgekehrt. Wendepunkte sind charakteristische Punkte, die wesentliche Informationen über den Funktionsverlauf liefern. An einem Wendepunkt ändert die erste Ableitung ihr Monotonieverhalten, hat also selbst ein Extremum.

## Definition

> [!note] **Definition: Wendepunkt**
> Ein Punkt $W(x_0 | f(x_0))$ heißt **Wendepunkt** der Funktion $f$, wenn sich an der Stelle $x_0$ das Krümmungsverhalten ändert.

**Äquivalente Beschreibungen:**
- Die Tangente „durchstößt" den Graphen am Wendepunkt
- Die erste Ableitung $f'$ hat an $x_0$ ein lokales Extremum
- Das Vorzeichen von $f''$ wechselt an $x_0$

## Bedingungen für Wendepunkte

### Notwendige Bedingung

Ist $x_0$ eine Wendestelle von $f$ und ist $f''(x_0)$ definiert, dann gilt:

$$f''(x_0) = 0$$

**Achtung:** Aus $f''(x_0) = 0$ folgt nicht automatisch ein Wendepunkt!

### Hinreichende Bedingungen

**Variante 1: Vorzeichenwechsel von f''**

$x_0$ ist Wendestelle, wenn $f''(x_0) = 0$ und $f''$ bei $x_0$ einen Vorzeichenwechsel hat.

**Variante 2: Mit der dritten Ableitung**

$x_0$ ist Wendestelle, wenn $f''(x_0) = 0$ und $f'''(x_0) \neq 0$.

**Variante 3: Allgemeines Kriterium**

Ist $n \geq 2$ die kleinste Zahl mit $f^{(n)}(x_0) \neq 0$:
- $n$ ungerade → Wendestelle
- $n$ gerade → kein Wendepunkt

## Berechnung von Wendepunkten

### Systematisches Vorgehen

**Schritt 1:** Berechne $f''(x)$

**Schritt 2:** Löse $f''(x) = 0$ → Wendekandidaten $x_1, x_2, \ldots$

**Schritt 3:** Prüfe hinreichende Bedingung (Vorzeichenwechsel oder $f'''$)

**Schritt 4:** Berechne $y$-Koordinaten: $f(x_i)$

**Schritt 5:** Gib Wendepunkte als Koordinaten an

### Beispiel 1: Polynomfunktion

Gegeben: $f(x) = x^3 - 6x^2 + 9x + 1$

**Ableitungen:**
$$f'(x) = 3x^2 - 12x + 9$$
$$f''(x) = 6x - 12$$
$$f'''(x) = 6$$

**Notwendige Bedingung:**
$$f''(x) = 0 \implies 6x - 12 = 0 \implies x_W = 2$$

**Hinreichende Bedingung:**
$$f'''(2) = 6 \neq 0 \quad \checkmark$$

**Wendepunkt:**
$$f(2) = 8 - 24 + 18 + 1 = 3$$
$$W(2 | 3)$$

### Beispiel 2: Funktion mit e-Term

Gegeben: $f(x) = x \cdot e^{-x}$

**Ableitungen (Produktregel):**
$$f'(x) = e^{-x} - x \cdot e^{-x} = (1-x) \cdot e^{-x}$$
$$f''(x) = -e^{-x} - (1-x) \cdot e^{-x} = (x-2) \cdot e^{-x}$$
$$f'''(x) = e^{-x} + (x-2) \cdot (-e^{-x}) = (3-x) \cdot e^{-x}$$

**Notwendige Bedingung:**
$$f''(x) = 0 \implies (x-2) \cdot e^{-x} = 0$$

Da $e^{-x} > 0$ für alle $x$: $x_W = 2$

**Hinreichende Bedingung:**
$$f'''(2) = (3-2) \cdot e^{-2} = e^{-2} \neq 0 \quad \checkmark$$

**Wendepunkt:**
$$f(2) = 2 \cdot e^{-2} = \frac{2}{e^2}$$
$$W\left(2 \,\middle|\, \frac{2}{e^2}\right) \approx W(2 | 0{,}27)$$

## Sattelpunkt (Terrassenpunkt)

Ein **Sattelpunkt** ist ein spezieller Wendepunkt, bei dem die Tangente waagerecht verläuft:

$$f'(x_0) = 0 \quad \text{und} \quad f''(x_0) = 0 \quad \text{und} \quad f'''(x_0) \neq 0$$

**Beispiel:** $f(x) = x^3$

- $f'(x) = 3x^2$, $f'(0) = 0$ ✓
- $f''(x) = 6x$, $f''(0) = 0$ ✓
- $f'''(x) = 6$, $f'''(0) = 6 \neq 0$ ✓

Der Ursprung $(0|0)$ ist ein Sattelpunkt.

## Wendetangente

Die **Wendetangente** ist die Tangente im Wendepunkt. Ihre Gleichung lautet:

$$t(x) = f(x_W) + f'(x_W) \cdot (x - x_W)$$

**Beispiel:** Für $f(x) = x^3 - 6x^2 + 9x + 1$ mit $W(2|3)$:

$$f'(2) = 3 \cdot 4 - 12 \cdot 2 + 9 = 12 - 24 + 9 = -3$$

Wendetangente:
$$t(x) = 3 + (-3)(x - 2) = 3 - 3x + 6 = -3x + 9$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Hoehere-Ableitungen]] – Berechnung von $f''$ und $f'''$
- → [[Kruemmungsverhalten]] – Krümmung und Wendepunkte
- → [[Extremstellen]] – Wendepunkte sind Extrema von $f'$
- → [[Tangenten-und-Normalen]] – Gleichung der Wendetangente
- → [[Vollstaendige-Kurvendiskussion]] – Einbettung in die Analyse

> [!warning] **Prüfungsrelevant**
> - Notwendige Bedingung: $f''(x_0) = 0$
> - Hinreichend: Vorzeichenwechsel von $f''$ ODER $f'''(x_0) \neq 0$
> - Sattelpunkt: zusätzlich $f'(x_0) = 0$
> - Wendepunkt als Koordinatenpaar $(x_W | y_W)$ angeben
> - Wendetangente oft gefragt

> [!question] **Typische Prüfungsfragen**
> - Bestimmen Sie alle Wendepunkte der Funktion $f$
> - Zeigen Sie, dass der Graph von $f$ genau einen Wendepunkt besitzt
> - Ermitteln Sie die Gleichung der Wendetangente
> - Hat die Funktion einen Sattelpunkt? Begründen Sie.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020
- ISB Bayern: Lehrplan Mathematik Gymnasium (LehrplanPLUS)

> [!tip] **Weiterführende Links**
> - [[Kruemmungsverhalten]] – Vertiefung zur Krümmungsanalyse
> - [[Vollstaendige-Kurvendiskussion]] – Einordnung in die Gesamtanalyse
