---
author: Andreas Hümmer
title: Kettenregel
tags:
  - content
  - mathe
  - differentialrechnung
  - ableitung
  - kettenregel
  - verkettung
  - analysis
created: 2026-10-17
modified: 2026-10-17
---

# Kettenregel

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Kettenregel formulieren und anwenden können
> - Verkettete Funktionen erkennen und in innere und äußere Funktion zerlegen können
> - Die Kettenregel in Kombination mit anderen Ableitungsregeln nutzen können
> - Typische Anwendungsfälle (Exponential-, trigonometrische, Potenzfunktionen) sicher beherrschen

---

## Überblick

Die Kettenregel ist die wichtigste Ableitungsregel für zusammengesetzte (verkettete) Funktionen. Sie ermöglicht die Ableitung von Funktionen wie $(2x + 1)^5$, $e^{x^2}$ oder $\sin(3x)$, bei denen eine Funktion als "Eingabe" in eine andere eingesetzt wird. Die Kettenregel besagt im Wesentlichen: **Äußere Ableitung mal innere Ableitung**.

## Die Kettenregel

> [!note] **Satz: Kettenregel**
> Sei $f(x) = g(h(x))$ eine verkettete Funktion, wobei $h$ die **innere** und $g$ die **äußere** Funktion ist. Sind $g$ und $h$ differenzierbar, so gilt:
> $$f'(x) = g'(h(x)) \cdot h'(x)$$

**Kurzform:** $(g \circ h)'(x) = g'(h(x)) \cdot h'(x)$

**Merkregel:** "Äußere ableiten, Inneres stehen lassen, mal innere Ableitung"

### In Leibniz-Notation

Mit $y = g(u)$ und $u = h(x)$:
$$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$$

Diese Schreibweise ist besonders einprägsam: Die $du$ "kürzen sich weg" (formal ist dies natürlich kein Kürzen, aber eine hilfreiche Eselsbrücke).

## Erkennen verketteter Funktionen

### Innere und äußere Funktion identifizieren

| Funktion $f(x)$ | Äußere $g(u)$ | Innere $h(x) = u$ |
|-----------------|---------------|-------------------|
| $(3x + 1)^5$ | $u^5$ | $3x + 1$ |
| $\sqrt{x^2 + 1}$ | $\sqrt{u}$ | $x^2 + 1$ |
| $e^{x^2}$ | $e^u$ | $x^2$ |
| $\sin(2x)$ | $\sin(u)$ | $2x$ |
| $\ln(x^3 - 1)$ | $\ln(u)$ | $x^3 - 1$ |
| $(e^x + 1)^3$ | $u^3$ | $e^x + 1$ |

**Faustregel:** Die innere Funktion ist das, was "im Argument" steht – also das, was nicht direkt $x$ ist.

## Wichtige Spezialfälle

### Potenzfunktion mit linearem Argument

Für $f(x) = (ax + b)^n$:
$$f'(x) = n(ax + b)^{n-1} \cdot a$$

**Beispiel:** $f(x) = (2x + 3)^4$
$$f'(x) = 4(2x + 3)^3 \cdot 2 = 8(2x + 3)^3$$

### Exponentialfunktion mit beliebigem Exponenten

Für $f(x) = e^{h(x)}$:
$$f'(x) = e^{h(x)} \cdot h'(x)$$

**Beispiel:** $f(x) = e^{3x^2 - x}$
$$f'(x) = e^{3x^2 - x} \cdot (6x - 1)$$

### Allgemeine Exponentialfunktion

Für $f(x) = a^{h(x)}$ mit $a > 0$:
$$f'(x) = a^{h(x)} \cdot \ln(a) \cdot h'(x)$$

### Logarithmusfunktion mit Argument

Für $f(x) = \ln(h(x))$:
$$f'(x) = \frac{h'(x)}{h(x)}$$

**Beispiel:** $f(x) = \ln(x^2 + 1)$
$$f'(x) = \frac{2x}{x^2 + 1}$$

### Trigonometrische Funktionen

Für $f(x) = \sin(h(x))$:
$$f'(x) = \cos(h(x)) \cdot h'(x)$$

Für $f(x) = \cos(h(x))$:
$$f'(x) = -\sin(h(x)) \cdot h'(x)$$

**Beispiel:** $f(x) = \sin(3x)$
$$f'(x) = \cos(3x) \cdot 3 = 3\cos(3x)$$

## Ausführliche Beispiele

### Beispiel 1: Potenz mit Polynom

$f(x) = (x^3 - 2x + 1)^4$

**Lösung:**
- Äußere Funktion: $g(u) = u^4$, also $g'(u) = 4u^3$
- Innere Funktion: $h(x) = x^3 - 2x + 1$, also $h'(x) = 3x^2 - 2$

$$f'(x) = 4(x^3 - 2x + 1)^3 \cdot (3x^2 - 2)$$

### Beispiel 2: Wurzel mit Quadrat

$f(x) = \sqrt{x^2 + 4}$

**Umschreiben:** $f(x) = (x^2 + 4)^{1/2}$

**Lösung:**
- Äußere: $g(u) = u^{1/2}$, $g'(u) = \frac{1}{2}u^{-1/2}$
- Innere: $h(x) = x^2 + 4$, $h'(x) = 2x$

$$f'(x) = \frac{1}{2}(x^2 + 4)^{-1/2} \cdot 2x = \frac{x}{\sqrt{x^2 + 4}}$$

### Beispiel 3: Exponentialfunktion

$f(x) = e^{-x^2}$

**Lösung:**
- Äußere: $g(u) = e^u$, $g'(u) = e^u$
- Innere: $h(x) = -x^2$, $h'(x) = -2x$

$$f'(x) = e^{-x^2} \cdot (-2x) = -2x \cdot e^{-x^2}$$

### Beispiel 4: Mehrfache Verkettung

$f(x) = \sin^2(x) = (\sin(x))^2$

**Lösung:**
- Äußere: $g(u) = u^2$, $g'(u) = 2u$
- Innere: $h(x) = \sin(x)$, $h'(x) = \cos(x)$

$$f'(x) = 2\sin(x) \cdot \cos(x) = \sin(2x)$$

(unter Verwendung des Doppelwinkelformel)

### Beispiel 5: Dreifache Verkettung

$f(x) = e^{\sin(x^2)}$

**Lösung (von außen nach innen):**
1. Äußerste: $e^u$, Ableitung: $e^u$
2. Mittlere: $\sin(v)$, Ableitung: $\cos(v)$
3. Innerste: $x^2$, Ableitung: $2x$

$$f'(x) = e^{\sin(x^2)} \cdot \cos(x^2) \cdot 2x$$

## Kombination mit Produkt- und Quotientenregel

### Beispiel: Produktregel + Kettenregel

$f(x) = x^2 \cdot e^{3x}$

**Lösung (Produktregel):**
- $u = x^2$, $u' = 2x$
- $v = e^{3x}$, $v' = 3e^{3x}$ (Kettenregel!)

$$f'(x) = 2x \cdot e^{3x} + x^2 \cdot 3e^{3x} = e^{3x}(2x + 3x^2) = e^{3x} \cdot x(2 + 3x)$$

### Beispiel: Quotientenregel + Kettenregel

$f(x) = \frac{e^x}{(x + 1)^2}$

**Lösung:**
- $u = e^x$, $u' = e^x$
- $v = (x + 1)^2$, $v' = 2(x + 1)$ (Kettenregel!)

$$f'(x) = \frac{e^x \cdot (x + 1)^2 - e^x \cdot 2(x + 1)}{(x + 1)^4}$$
$$= \frac{e^x(x + 1)[(x + 1) - 2]}{(x + 1)^4} = \frac{e^x(x - 1)}{(x + 1)^3}$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Ableitungsregeln|Ableitungsregeln]] – Übersicht aller Regeln
- → [[Verkettung-von-Funktionen|Verkettung von Funktionen]] – Mathematische Grundlage
- → [[Produktregel|Produktregel]] – Oft kombiniert
- → [[Quotientenregel|Quotientenregel]] – Oft kombiniert
- → [[Exponentialfunktionen|Exponentialfunktionen]] – Wichtige Anwendung

> [!warning] **Prüfungsrelevant**
> - Die Kettenregel ist **die wichtigste Ableitungsregel** – sie kommt fast überall vor!
> - Innere und äußere Funktion sicher identifizieren können
> - Die innere Ableitung nicht vergessen! (häufigster Fehler)
> - Kombination mit Produkt- und Quotientenregel ist Standard

> [!question] **Typische Prüfungsfragen**
> - "Bestimmen Sie die Ableitung von $f(x) = (...)^n$, $e^{...}$, $\ln(...)$, $\sin(...)$"
> - "Geben Sie an, welche Funktion die innere/äußere ist."
> - "Zeigen Sie, dass $f'(x) = ...$" (mehrstufige Verkettungen)

## Quellen

- Bronstein, I.N., Semendjajew, K.A. (2012): *Taschenbuch der Mathematik*. Verlag Europa-Lehrmittel.
- Bigalke, A., Köhler, N. (2015): *Mathematik – Qualifikationsphase*. Cornelsen Verlag.
- Papula, L. (2018): *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1. Springer Vieweg.

> [!tip] **Weiterführende Links**
> - [[Tangenten-und-Normalen|Tangenten und Normalen]] – Anwendung der Kettenregel
> - [[Trigonometrische-Funktionen|Trigonometrische Funktionen]] – Verkettungen mit Winkelfunktionen
