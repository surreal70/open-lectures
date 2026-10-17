---
author: Andreas Hümmer
title: Verkettung von Funktionen
tags:
  - content
  - mathe
  - funktionen
  - verkettung
  - komposition
created: 2025-01-22
modified: 2025-01-22
---

# Verkettung von Funktionen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Verkettung (Komposition) von Funktionen definieren und berechnen können
> - Verkettete Funktionen in ihre Bestandteile zerlegen können
> - Den Definitionsbereich verketteter Funktionen bestimmen können
> - Die Kettenregel als Ableitung verketteter Funktionen kennen

---

## Überblick

Die **Verkettung** (oder Komposition) von Funktionen erzeugt aus zwei Funktionen eine neue, indem der Funktionswert der einen als Argument der anderen verwendet wird. Dieses Konzept ist fundamental für das Verständnis komplexer Funktionen und bildet die Grundlage für die Kettenregel der Differentialrechnung.

## Definition

### Formale Definition

Seien $f: D_f \to W_f$ und $g: D_g \to W_g$ zwei Funktionen. Die **Verkettung** (oder Komposition) $g \circ f$ ist definiert als:

$$(g \circ f)(x) = g(f(x))$$

**Lies:** „$g$ nach $f$" oder „$g$ von $f$ von $x$"

### Definitionsbereich der Verkettung

$$D_{g \circ f} = \{x \in D_f \mid f(x) \in D_g\}$$

Das heißt: $x$ muss im Definitionsbereich von $f$ liegen, und $f(x)$ muss im Definitionsbereich von $g$ liegen.

### Schematische Darstellung

```
   x  ──f──>  f(x)  ──g──>  g(f(x))
   
   D_f        W_f ∩ D_g      W_g
```

## Beispiele

### Beispiel 1: Einfache Verkettung

Seien $f(x) = x^2$ und $g(x) = x + 1$.

$$(g \circ f)(x) = g(f(x)) = g(x^2) = x^2 + 1$$

$$(f \circ g)(x) = f(g(x)) = f(x+1) = (x+1)^2 = x^2 + 2x + 1$$

**Beachte:** $g \circ f \neq f \circ g$ im Allgemeinen!

### Beispiel 2: Mit Definitionsbereichseinschränkung

Seien $f(x) = x - 2$ und $g(x) = \sqrt{x}$.

$$(g \circ f)(x) = g(f(x)) = g(x-2) = \sqrt{x-2}$$

**Definitionsbereich:**
- $D_f = \mathbb{R}$
- $D_g = [0, \infty)$
- $D_{g \circ f} = \{x \in \mathbb{R} \mid x - 2 \geq 0\} = [2, \infty)$

### Beispiel 3: Dreifache Verkettung

Sei $h(x) = \sin(e^{x^2})$.

Diese Funktion ist eine dreifache Verkettung:
$$h = \sin \circ \exp \circ q$$

mit $q(x) = x^2$, $\exp(x) = e^x$, $\sin(x) = \sin(x)$.

Berechnung von innen nach außen:
$$x \xrightarrow{q} x^2 \xrightarrow{\exp} e^{x^2} \xrightarrow{\sin} \sin(e^{x^2})$$

## Zerlegung verketteter Funktionen

Das Erkennen der Zerlegung ist wichtig für die Anwendung der Kettenregel.

### Strategie

Identifiziere die „innere" und „äußere" Funktion:
- **Innere Funktion:** Was steht „innen" (im Argument)?
- **Äußere Funktion:** Was wird auf dieses Argument angewandt?

### Beispiele

| Funktion $h(x)$ | Äußere $g(u)$ | Innere $f(x)$ |
|-----------------|---------------|---------------|
| $\sqrt{x^2+1}$ | $\sqrt{u}$ | $x^2+1$ |
| $e^{3x}$ | $e^u$ | $3x$ |
| $\sin^2(x)$ | $u^2$ | $\sin(x)$ |
| $\ln(\cos(x))$ | $\ln(u)$ | $\cos(x)$ |
| $(2x+1)^5$ | $u^5$ | $2x+1$ |

**Merke:** Bei $\sin^2(x) = (\sin(x))^2$ ist das Quadrieren die äußere Funktion!

## Eigenschaften der Verkettung

### Nicht-Kommutativität

Im Allgemeinen gilt $g \circ f \neq f \circ g$.

**Beispiel:** $f(x) = x^2$, $g(x) = x + 1$
- $(g \circ f)(x) = x^2 + 1$
- $(f \circ g)(x) = x^2 + 2x + 1$

### Assoziativität

$$(h \circ g) \circ f = h \circ (g \circ f)$$

Daher kann man ohne Klammern schreiben: $h \circ g \circ f$.

### Identität

Die Identitätsfunktion $\text{id}(x) = x$ ist das neutrale Element:
$$f \circ \text{id} = \text{id} \circ f = f$$

### Umkehrfunktion als Inverse

Für eine bijektive Funktion $f$ gilt:
$$f \circ f^{-1} = f^{-1} \circ f = \text{id}$$

## Verkettung und Ableitungen: Die Kettenregel

### Satz (Kettenregel)

Ist $f$ differenzierbar bei $x$ und $g$ differenzierbar bei $f(x)$, so ist $g \circ f$ differenzierbar bei $x$ mit:

$$(g \circ f)'(x) = g'(f(x)) \cdot f'(x)$$

**Merksatz:** „Äußere Ableitung mal innere Ableitung"

### Beispiel zur Kettenregel

$$h(x) = (3x^2 + 1)^4$$

**Zerlegung:** $g(u) = u^4$, $f(x) = 3x^2 + 1$

**Ableitungen:** $g'(u) = 4u^3$, $f'(x) = 6x$

**Kettenregel:**
$$h'(x) = g'(f(x)) \cdot f'(x) = 4(3x^2+1)^3 \cdot 6x = 24x(3x^2+1)^3$$

## Rechenregeln für Verkettungen

### Monotonie

| $f$ | $g$ | $g \circ f$ |
|-----|-----|-------------|
| streng mon. wachsend | streng mon. wachsend | streng mon. wachsend |
| streng mon. wachsend | streng mon. fallend | streng mon. fallend |
| streng mon. fallend | streng mon. wachsend | streng mon. fallend |
| streng mon. fallend | streng mon. fallend | streng mon. wachsend |

**Merkregel:** Wie bei der Vorzeichenmultiplikation.

### Symmetrie

| $f$ | $g$ | $g \circ f$ |
|-----|-----|-------------|
| gerade | gerade | gerade |
| gerade | ungerade | gerade |
| ungerade | gerade | gerade |
| ungerade | ungerade | ungerade |

## Anwendungen

### Substitution bei Integralen

Bei der Substitutionsregel wird die Verkettung „rückgängig gemacht":

$$\int g(f(x)) \cdot f'(x) \, dx = \int g(u) \, du \quad \text{mit } u = f(x)$$

### Implizite Differentiation

Bei implizit definierten Funktionen ist $y = y(x)$ eine Funktion von $x$:
$$\frac{d}{dx}[y^2] = 2y \cdot y' \quad \text{(Kettenregel!)}$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Umkehrfunktionen]] – Inverse bezüglich der Verkettung
- → [[Wiederholung-des-Funktionsbegriffs]] – Funktion als Zuordnung
- → [[05-Differentialrechnung-I|Differentialrechnung I]] – Kettenregel
- → [[Monotonie]] – Monotonie verketteter Funktionen

> [!warning] **Prüfungsrelevant**
> - Definition und Berechnung von Verkettungen
> - Zerlegung verketteter Funktionen (für Kettenregel!)
> - Bestimmung des Definitionsbereichs
> - Nicht-Kommutativität: $g \circ f \neq f \circ g$

> [!question] **Typische Prüfungsfragen**
> - Zerlege $h(x) = e^{\sin(x^2)}$ in innere und äußere Funktionen.
> - Berechne $(f \circ g)(x)$ und $(g \circ f)(x)$ für $f(x) = \frac{1}{x}$ und $g(x) = x^2 + 1$.
> - Bestimme den Definitionsbereich von $h(x) = \ln(\sqrt{x} - 1)$.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I. N. et al.: Taschenbuch der Mathematik. Verlag Harri Deutsch, 2012.
- ISB Bayern: Lehrplan Mathematik Gymnasium.

> [!tip] **Weiterführende Links**
> - [[07-Integralrechnung-I|Integralrechnung I]] – Substitutionsregel
> - [[Transformationen]] – Verkettung mit linearen Funktionen
> - [[Exponentialfunktionen]] – Verkettungen mit $e^x$
