---
author: Andreas Hümmer
title: Potenzregel
tags:
  - content
  - mathe
  - differentialrechnung
  - ableitung
  - potenzregel
  - analysis
created: 2026-10-17
modified: 2026-10-17
---

# Potenzregel

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Potenzregel für beliebige reelle Exponenten anwenden können
> - Wurzeln und Brüche als Potenzen umschreiben und ableiten können
> - Die Herleitung der Potenzregel für natürliche Exponenten nachvollziehen können
> - Die Faktorregel in Kombination mit der Potenzregel verwenden können

---

## Überblick

Die Potenzregel ist die grundlegendste aller Ableitungsregeln. Sie erlaubt die Ableitung von Potenzfunktionen $f(x) = x^n$ für beliebige reelle Exponenten $n$. In Kombination mit der Faktor- und Summenregel ermöglicht sie das Ableiten aller Polynome und vieler weiterer Funktionen.

## Die Potenzregel

> [!note] **Satz: Potenzregel**
> Für $f(x) = x^n$ mit $n \in \mathbb{R}$ gilt:
> $$f'(x) = n \cdot x^{n-1}$$

**Merkregel:** "Exponent nach vorne, Exponent um 1 verringern"

### Ergänzung: Faktorregel

Für $f(x) = c \cdot x^n$ mit einer Konstanten $c$:
$$f'(x) = c \cdot n \cdot x^{n-1}$$

## Herleitung für natürliche Exponenten

Für $n \in \mathbb{N}$ können wir die Potenzregel mithilfe der Definition der Ableitung beweisen:

$$f'(x) = \lim_{h \to 0} \frac{(x+h)^n - x^n}{h}$$

Mit dem binomischen Lehrsatz:
$$(x+h)^n = \sum_{k=0}^{n} \binom{n}{k} x^{n-k} h^k = x^n + n x^{n-1} h + \binom{n}{2} x^{n-2} h^2 + \ldots + h^n$$

Einsetzen und $x^n$ subtrahieren:
$$\frac{(x+h)^n - x^n}{h} = \frac{n x^{n-1} h + \binom{n}{2} x^{n-2} h^2 + \ldots + h^n}{h}$$
$$= n x^{n-1} + \binom{n}{2} x^{n-2} h + \ldots + h^{n-1}$$

Für $h \to 0$ verschwinden alle Terme mit $h$:
$$f'(x) = n x^{n-1}$$

## Beispiele für verschiedene Exponenten

### Natürliche Exponenten

| $f(x)$ | $f'(x)$ |
|--------|---------|
| $x$ | $1$ |
| $x^2$ | $2x$ |
| $x^3$ | $3x^2$ |
| $x^4$ | $4x^3$ |
| $x^{10}$ | $10x^9$ |

### Negative Exponenten

Brüche werden als negative Potenzen geschrieben:

| $f(x)$ | Umgeschrieben | $f'(x)$ | Vereinfacht |
|--------|---------------|---------|-------------|
| $\frac{1}{x}$ | $x^{-1}$ | $-1 \cdot x^{-2}$ | $-\frac{1}{x^2}$ |
| $\frac{1}{x^2}$ | $x^{-2}$ | $-2 \cdot x^{-3}$ | $-\frac{2}{x^3}$ |
| $\frac{1}{x^3}$ | $x^{-3}$ | $-3 \cdot x^{-4}$ | $-\frac{3}{x^4}$ |
| $\frac{1}{x^n}$ | $x^{-n}$ | $-n \cdot x^{-n-1}$ | $-\frac{n}{x^{n+1}}$ |

### Rationale Exponenten (Wurzeln)

Wurzeln werden als Bruchpotenzen geschrieben:

| $f(x)$ | Umgeschrieben | $f'(x)$ | Vereinfacht |
|--------|---------------|---------|-------------|
| $\sqrt{x}$ | $x^{1/2}$ | $\frac{1}{2} x^{-1/2}$ | $\frac{1}{2\sqrt{x}}$ |
| $\sqrt[3]{x}$ | $x^{1/3}$ | $\frac{1}{3} x^{-2/3}$ | $\frac{1}{3\sqrt[3]{x^2}}$ |
| $\sqrt[n]{x}$ | $x^{1/n}$ | $\frac{1}{n} x^{(1-n)/n}$ | $\frac{1}{n\sqrt[n]{x^{n-1}}}$ |
| $\sqrt{x^3}$ | $x^{3/2}$ | $\frac{3}{2} x^{1/2}$ | $\frac{3}{2}\sqrt{x}$ |

### Die Konstante

Beachte: $f(x) = 1 = x^0$
$$f'(x) = 0 \cdot x^{-1} = 0$$

Allgemein: Die Ableitung jeder Konstanten ist 0.

## Ausführliche Beispiele

### Beispiel 1: Polynom

$f(x) = 3x^4 - 2x^3 + 5x^2 - 7x + 4$

**Lösung:** Jeder Term einzeln nach der Potenzregel:
$$f'(x) = 3 \cdot 4x^3 - 2 \cdot 3x^2 + 5 \cdot 2x - 7 \cdot 1 + 0$$
$$= 12x^3 - 6x^2 + 10x - 7$$

### Beispiel 2: Bruchfunktion

$f(x) = \frac{5}{x^3} - \frac{2}{x}$

**Umschreiben:**
$$f(x) = 5x^{-3} - 2x^{-1}$$

**Ableiten:**
$$f'(x) = 5 \cdot (-3) x^{-4} - 2 \cdot (-1) x^{-2} = -15x^{-4} + 2x^{-2}$$

**Zurückschreiben:**
$$f'(x) = -\frac{15}{x^4} + \frac{2}{x^2}$$

### Beispiel 3: Wurzelfunktion

$f(x) = 4\sqrt{x} - 3\sqrt[3]{x^2}$

**Umschreiben:**
$$f(x) = 4x^{1/2} - 3x^{2/3}$$

**Ableiten:**
$$f'(x) = 4 \cdot \frac{1}{2} x^{-1/2} - 3 \cdot \frac{2}{3} x^{-1/3}$$
$$= 2x^{-1/2} - 2x^{-1/3}$$

**Zurückschreiben:**
$$f'(x) = \frac{2}{\sqrt{x}} - \frac{2}{\sqrt[3]{x}}$$

### Beispiel 4: Gemischte Funktion

$f(x) = x^2 + \frac{1}{x} - \sqrt{x}$

**Umschreiben:**
$$f(x) = x^2 + x^{-1} - x^{1/2}$$

**Ableiten:**
$$f'(x) = 2x - x^{-2} - \frac{1}{2}x^{-1/2}$$
$$= 2x - \frac{1}{x^2} - \frac{1}{2\sqrt{x}}$$

## Definitionsbereiche beachten

Bei negativen und gebrochenen Exponenten muss der Definitionsbereich beachtet werden:

| Funktion | Definitionsbereich von $f$ | Definitionsbereich von $f'$ |
|----------|---------------------------|----------------------------|
| $x^{-1} = \frac{1}{x}$ | $\mathbb{R} \setminus \{0\}$ | $\mathbb{R} \setminus \{0\}$ |
| $x^{1/2} = \sqrt{x}$ | $[0, \infty)$ | $(0, \infty)$ |
| $x^{-1/2} = \frac{1}{\sqrt{x}}$ | $(0, \infty)$ | $(0, \infty)$ |

> [!warning] **Achtung**
> Bei $f(x) = \sqrt{x}$ ist $f'(x) = \frac{1}{2\sqrt{x}}$ an der Stelle $x = 0$ nicht definiert, obwohl $f(0) = 0$ existiert. Die Tangente an $f$ in $(0|0)$ ist senkrecht.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Ableitungsregeln|Ableitungsregeln]] – Übersicht aller Regeln
- → [[Summenregel|Summenregel]] – Ableitung von Summen
- → [[Potenzfunktionen|Potenzfunktionen]] – Eigenschaften der Grundfunktionen
- → [[Polynomfunktionen|Polynomfunktionen]] – Anwendung auf Polynome
- → [[Potenzen-mit-rationalen-Exponenten|Potenzen mit rationalen Exponenten]] – Vorwissen

> [!warning] **Prüfungsrelevant**
> - Die Potenzregel $f(x) = x^n \Rightarrow f'(x) = n \cdot x^{n-1}$ muss absolut sicher beherrscht werden
> - Umschreiben von Wurzeln und Brüchen als Potenzen ist Voraussetzung
> - Definitionsbereiche bei negativen/gebrochenen Exponenten beachten
> - Die Kombination mit der Faktorregel ist Standard

> [!question] **Typische Prüfungsfragen**
> - "Bestimmen Sie die Ableitung von $f(x) = ...$" (Polynome, Brüche, Wurzeln)
> - "Schreiben Sie die Funktion als Potenz und leiten Sie ab."
> - "Geben Sie den Definitionsbereich der Ableitungsfunktion an."

## Quellen

- Bronstein, I.N., Semendjajew, K.A. (2012): *Taschenbuch der Mathematik*. Verlag Europa-Lehrmittel.
- Bigalke, A., Köhler, N. (2015): *Mathematik – Qualifikationsphase*. Cornelsen Verlag.
- Griesel, H., Postel, H., Suhr, F. (2019): *Elemente der Mathematik – Qualifikationsphase*. Schroedel Verlag.

> [!tip] **Weiterführende Links**
> - [[Produktregel|Produktregel]] – Wenn Potenzen multipliziert werden
> - [[Kettenregel|Kettenregel]] – Wenn die Basis selbst eine Funktion ist
