---
author: Andreas Hümmer
title: Produktregel
tags:
  - content
  - mathe
  - differentialrechnung
  - ableitung
  - produktregel
  - analysis
created: 2026-10-17
modified: 2026-10-17
---

# Produktregel

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Produktregel formulieren und begründen können
> - Produkte von Funktionen sicher ableiten können
> - Die Produktregel in Kombination mit anderen Regeln anwenden können
> - Verstehen, warum $(u \cdot v)' \neq u' \cdot v'$

---

## Überblick

Die Produktregel ermöglicht das Ableiten von Funktionen, die als Produkt zweier differenzierbarer Funktionen geschrieben werden können. Sie ist unverzichtbar, wenn weder Umformen noch andere Regeln anwendbar sind. Eine wichtige Erkenntnis: Die Ableitung eines Produkts ist **nicht** einfach das Produkt der Ableitungen!

## Die Produktregel

> [!note] **Satz: Produktregel**
> Sind $u$ und $v$ differenzierbare Funktionen, so ist auch $f = u \cdot v$ differenzierbar, und es gilt:
> $$(u \cdot v)'(x) = u'(x) \cdot v(x) + u(x) \cdot v'(x)$$

**Kurzform:**
$$(u \cdot v)' = u' \cdot v + u \cdot v'$$

**Merkregel:** "Erste mal Ableitung der Zweiten plus Zweite mal Ableitung der Ersten"

Oder: "Ableitung der Ersten mal Zweite plus Erste mal Ableitung der Zweiten"

## Warum nicht einfach $(u \cdot v)' = u' \cdot v'$?

Ein Gegenbeispiel zeigt, dass dies falsch wäre:

Sei $f(x) = x \cdot x = x^2$.
- Nach der richtigen Regel: $f'(x) = 2x$ ✓
- Nach der falschen Regel: $f'(x) = 1 \cdot 1 = 1$ ✗

## Herleitung

Aus der Definition der Ableitung:

$$f'(x) = \lim_{h \to 0} \frac{u(x+h) \cdot v(x+h) - u(x) \cdot v(x)}{h}$$

**Trick:** Wir addieren und subtrahieren $u(x+h) \cdot v(x)$:

$$= \lim_{h \to 0} \frac{u(x+h) \cdot v(x+h) - u(x+h) \cdot v(x) + u(x+h) \cdot v(x) - u(x) \cdot v(x)}{h}$$

$$= \lim_{h \to 0} \left[ u(x+h) \cdot \frac{v(x+h) - v(x)}{h} + v(x) \cdot \frac{u(x+h) - u(x)}{h} \right]$$

Mit $\lim_{h \to 0} u(x+h) = u(x)$ (wegen Stetigkeit):

$$= u(x) \cdot v'(x) + v(x) \cdot u'(x)$$

## Beispiele

### Beispiel 1: Polynom mal Polynom

$f(x) = (x^2 + 1)(x^3 - 2x)$

**Lösung:**
- $u = x^2 + 1$, $u' = 2x$
- $v = x^3 - 2x$, $v' = 3x^2 - 2$

$$f'(x) = 2x \cdot (x^3 - 2x) + (x^2 + 1) \cdot (3x^2 - 2)$$
$$= 2x^4 - 4x^2 + 3x^4 - 2x^2 + 3x^2 - 2$$
$$= 5x^4 - 3x^2 - 2$$

**Kontrolle:** Ausmultiplizieren und dann ableiten:
$$f(x) = x^5 - 2x^3 + x^3 - 2x = x^5 - x^3 - 2x$$
$$f'(x) = 5x^4 - 3x^2 - 2$$ ✓

### Beispiel 2: Polynom mal Exponentialfunktion

$f(x) = x^2 \cdot e^x$

**Lösung:**
- $u = x^2$, $u' = 2x$
- $v = e^x$, $v' = e^x$

$$f'(x) = 2x \cdot e^x + x^2 \cdot e^x = e^x(2x + x^2) = e^x \cdot x(2 + x)$$

### Beispiel 3: Wurzel mal trigonometrische Funktion

$f(x) = \sqrt{x} \cdot \sin(x)$

**Lösung:**
- $u = \sqrt{x} = x^{1/2}$, $u' = \frac{1}{2}x^{-1/2} = \frac{1}{2\sqrt{x}}$
- $v = \sin(x)$, $v' = \cos(x)$

$$f'(x) = \frac{1}{2\sqrt{x}} \cdot \sin(x) + \sqrt{x} \cdot \cos(x)$$
$$= \frac{\sin(x)}{2\sqrt{x}} + \sqrt{x} \cos(x)$$

### Beispiel 4: Logarithmus mal Polynom

$f(x) = \ln(x) \cdot (x^2 + 3)$

**Lösung:**
- $u = \ln(x)$, $u' = \frac{1}{x}$
- $v = x^2 + 3$, $v' = 2x$

$$f'(x) = \frac{1}{x} \cdot (x^2 + 3) + \ln(x) \cdot 2x$$
$$= \frac{x^2 + 3}{x} + 2x \ln(x) = x + \frac{3}{x} + 2x \ln(x)$$

## Produkt von drei Faktoren

Für $f = u \cdot v \cdot w$ wenden wir die Produktregel zweimal an:

$$f' = (u \cdot v)' \cdot w + (u \cdot v) \cdot w'$$
$$= (u' v + u v') \cdot w + u v w'$$
$$= u' v w + u v' w + u v w'$$

> [!note] **Verallgemeinerte Produktregel**
> $$(u \cdot v \cdot w)' = u' v w + u v' w + u v w'$$
> Jeder Faktor wird einmal abgeleitet, die anderen bleiben stehen.

### Beispiel

$f(x) = x \cdot e^x \cdot \sin(x)$

$$f'(x) = 1 \cdot e^x \cdot \sin(x) + x \cdot e^x \cdot \sin(x) + x \cdot e^x \cdot \cos(x)$$
$$= e^x \sin(x) + x e^x \sin(x) + x e^x \cos(x)$$
$$= e^x [\sin(x) + x \sin(x) + x \cos(x)]$$
$$= e^x [(1 + x)\sin(x) + x \cos(x)]$$

## Kombination mit der Kettenregel

Oft tritt die Produktregel zusammen mit der [[Kettenregel|Kettenregel]] auf:

$f(x) = x^2 \cdot (3x - 1)^4$

**Lösung:**
- $u = x^2$, $u' = 2x$
- $v = (3x - 1)^4$, $v' = 4(3x - 1)^3 \cdot 3 = 12(3x - 1)^3$ (Kettenregel!)

$$f'(x) = 2x \cdot (3x - 1)^4 + x^2 \cdot 12(3x - 1)^3$$
$$= 2x(3x - 1)^3 [(3x - 1) + 6x]$$
$$= 2x(3x - 1)^3 (9x - 1)$$

## Wann Produktregel anwenden?

Die Produktregel ist nötig, wenn:
- Eine Funktion als Produkt zweier nicht-konstanter Funktionen vorliegt
- Ausmultiplizieren nicht möglich oder zu aufwendig ist

Die Produktregel ist **nicht** nötig, wenn:
- Ein Faktor konstant ist → Faktorregel genügt
- Das Produkt sich leicht ausmultiplizieren lässt

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Ableitungsregeln|Ableitungsregeln]] – Übersicht aller Regeln
- → [[Quotientenregel|Quotientenregel]] – Eng verwandt, für Brüche
- → [[Kettenregel|Kettenregel]] – Oft kombiniert
- → [[Exponentialfunktionen|Exponentialfunktionen]] – Häufiges Anwendungsgebiet
- → [[Polynomfunktionen|Polynomfunktionen]] – Kontrolle durch Ausmultiplizieren

> [!warning] **Prüfungsrelevant**
> - Die Produktregel $(uv)' = u'v + uv'$ muss absolut sicher sitzen
> - Typischer Fehler: $(uv)' = u' \cdot v'$ ist **falsch**!
> - Die Kombination mit der Kettenregel ist Standardaufgabe
> - Ergebnisse sollten wenn möglich faktorisiert werden

> [!question] **Typische Prüfungsfragen**
> - "Bestimmen Sie die Ableitung von $f(x) = ...$" (Produkt zweier Funktionen)
> - "Zeigen Sie, dass $f'(x) = ...$" (mit Produktregel)
> - "Für welche $x$ gilt $f'(x) = 0$?" (nach Faktorisierung)

## Quellen

- Bronstein, I.N., Semendjajew, K.A. (2012): *Taschenbuch der Mathematik*. Verlag Europa-Lehrmittel.
- Bigalke, A., Köhler, N. (2015): *Mathematik – Qualifikationsphase*. Cornelsen Verlag.
- Papula, L. (2018): *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1. Springer Vieweg.

> [!tip] **Weiterführende Links**
> - [[Quotientenregel|Quotientenregel]] – Die "Schwester" der Produktregel
> - [[Tangenten-und-Normalen|Tangenten und Normalen]] – Anwendung der Ableitung
