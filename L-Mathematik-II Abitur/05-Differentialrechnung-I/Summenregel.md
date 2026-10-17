---
author: Andreas Hümmer
title: Summenregel
tags:
  - content
  - mathe
  - differentialrechnung
  - ableitung
  - summenregel
  - analysis
created: 2026-10-17
modified: 2026-10-17
---

# Summenregel

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Summenregel für Ableitungen formulieren und anwenden können
> - Verstehen, warum die Ableitung einer Summe die Summe der Ableitungen ist
> - Die Summenregel auf Polynome und andere zusammengesetzte Funktionen anwenden können
> - Die Differenzregel als Spezialfall einordnen können

---

## Überblick

Die Summenregel ist eine der grundlegenden Ableitungsregeln. Sie besagt, dass die Ableitung einer Summe gleich der Summe der Ableitungen ist. In Kombination mit der [[Potenzregel|Potenzregel]] und der Faktorregel ermöglicht sie das Ableiten beliebiger Polynome.

## Die Summenregel

> [!note] **Satz: Summenregel**
> Sind $u$ und $v$ differenzierbare Funktionen, so ist auch $f = u + v$ differenzierbar, und es gilt:
> $$(u + v)'(x) = u'(x) + v'(x)$$
> oder kurz:
> $$[u(x) + v(x)]' = u'(x) + v'(x)$$

**Merkregel:** "Die Ableitung einer Summe ist die Summe der Ableitungen."

## Herleitung

Die Herleitung folgt direkt aus der Definition der Ableitung und den Rechenregeln für Grenzwerte:

$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$
$$= \lim_{h \to 0} \frac{[u(x+h) + v(x+h)] - [u(x) + v(x)]}{h}$$
$$= \lim_{h \to 0} \frac{[u(x+h) - u(x)] + [v(x+h) - v(x)]}{h}$$
$$= \lim_{h \to 0} \frac{u(x+h) - u(x)}{h} + \lim_{h \to 0} \frac{v(x+h) - v(x)}{h}$$
$$= u'(x) + v'(x)$$

## Differenzregel

Die Differenzregel ist ein Spezialfall der Summenregel (mit negativem Faktor):

> [!note] **Satz: Differenzregel**
> $$(u - v)'(x) = u'(x) - v'(x)$$

**Begründung:** $u - v = u + (-1) \cdot v$, und mit der Faktorregel ist $(-v)' = -v'$.

## Verallgemeinerung auf mehrere Summanden

Die Summenregel lässt sich auf beliebig viele Summanden erweitern:

$$[f_1(x) + f_2(x) + \ldots + f_n(x)]' = f_1'(x) + f_2'(x) + \ldots + f_n'(x)$$

In Summennotation:
$$\left[\sum_{i=1}^{n} f_i(x)\right]' = \sum_{i=1}^{n} f_i'(x)$$

## Beispiele

### Beispiel 1: Einfache Summe

$f(x) = x^3 + x^2$

**Lösung:**
$$f'(x) = (x^3)' + (x^2)' = 3x^2 + 2x$$

### Beispiel 2: Polynom

$f(x) = 2x^4 - 3x^3 + 5x^2 - x + 7$

**Lösung:** Summen-/Differenzregel und Potenzregel:
$$f'(x) = 2 \cdot 4x^3 - 3 \cdot 3x^2 + 5 \cdot 2x - 1 + 0$$
$$= 8x^3 - 9x^2 + 10x - 1$$

### Beispiel 3: Mit Brüchen und Wurzeln

$f(x) = \frac{1}{x} + \sqrt{x}$

**Umschreiben:**
$$f(x) = x^{-1} + x^{1/2}$$

**Ableiten:**
$$f'(x) = -x^{-2} + \frac{1}{2}x^{-1/2} = -\frac{1}{x^2} + \frac{1}{2\sqrt{x}}$$

### Beispiel 4: Trigonometrische Funktionen

$f(x) = \sin(x) + \cos(x)$

**Lösung:**
$$f'(x) = \cos(x) + (-\sin(x)) = \cos(x) - \sin(x)$$

### Beispiel 5: Exponential- und Logarithmusfunktion

$f(x) = e^x + \ln(x)$

**Lösung:**
$$f'(x) = e^x + \frac{1}{x}$$

## Zusammenspiel mit anderen Regeln

### Mit der Faktorregel

Die Faktorregel $(c \cdot u)' = c \cdot u'$ und die Summenregel zusammen:

$f(x) = 3x^2 + 5x - 2$

$$f'(x) = 3 \cdot 2x + 5 \cdot 1 - 0 = 6x + 5$$

### Allgemeines Polynom

Für das allgemeine Polynom
$$p(x) = a_n x^n + a_{n-1} x^{n-1} + \ldots + a_1 x + a_0$$

ist die Ableitung:
$$p'(x) = n a_n x^{n-1} + (n-1) a_{n-1} x^{n-2} + \ldots + a_1$$

### Mit Produkt- und Kettenregel

Bei komplexeren Funktionen wird die Summenregel oft mit anderen Regeln kombiniert:

$f(x) = x^2 e^x + \sin(x)$

**Lösung:**
- Erster Summand: Produktregel → $(x^2 e^x)' = 2x e^x + x^2 e^x$
- Zweiter Summand: $(\sin x)' = \cos x$
$$f'(x) = 2x e^x + x^2 e^x + \cos(x) = e^x(2x + x^2) + \cos(x)$$

## Geometrische Interpretation

Die Summenregel hat eine anschauliche geometrische Bedeutung:

Wenn $f(x) = u(x) + v(x)$, dann wird der Graph von $f$ an jeder Stelle aus den Graphen von $u$ und $v$ zusammengesetzt. Die Steigung der Tangente an $f$ ist dann die Summe der Steigungen der Tangenten an $u$ und $v$.

```
      y
      |        f = u + v
      |       /
      |      /  u
      |     /  /
      |    / /
      |   //   v
      |  /   /
      | /  /
      |/ /
      +--------------> x
```

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Ableitungsregeln|Ableitungsregeln]] – Übersicht aller Regeln
- → [[Potenzregel|Potenzregel]] – Oft gemeinsam angewendet
- → [[Polynomfunktionen|Polynomfunktionen]] – Hauptanwendungsgebiet
- → [[Produktregel|Produktregel]] – Wenn Faktoren nicht konstant sind
- → [[Definition-der-Ableitung|Definition der Ableitung]] – Grundlage der Herleitung

> [!warning] **Prüfungsrelevant**
> - Die Summenregel ist bei **jeder** Polynomableitung nötig
> - "Ableitung einer Summe = Summe der Ableitungen" muss sofort abrufbar sein
> - Die Kombination mit Potenz- und Faktorregel ist Standardwerkzeug
> - Auch bei komplexeren Funktionen (trigonometrisch, exponentiell) anwendbar

> [!question] **Typische Prüfungsfragen**
> - "Bestimmen Sie die Ableitung des Polynoms $p(x) = ...$"
> - "Leiten Sie $f(x) = ...$ ab." (mit verschiedenen Funktionstypen in der Summe)
> - "Welche Ableitungsregeln benötigen Sie für $f(x) = ...$?"

## Quellen

- Bronstein, I.N., Semendjajew, K.A. (2012): *Taschenbuch der Mathematik*. Verlag Europa-Lehrmittel.
- Bigalke, A., Köhler, N. (2015): *Mathematik – Qualifikationsphase*. Cornelsen Verlag.
- Papula, L. (2018): *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1. Springer Vieweg.

> [!tip] **Weiterführende Links**
> - [[Produktregel|Produktregel]] – Für Produkte statt Summen
> - [[Tangenten-und-Normalen|Tangenten und Normalen]] – Anwendung der Ableitung
