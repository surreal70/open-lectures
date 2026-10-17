---
author: Andreas Hümmer
title: Ableitungsregeln
tags:
  - content
  - mathe
  - differentialrechnung
  - ableitung
  - ableitungsregeln
  - analysis
created: 2026-10-17
modified: 2026-10-17
---

# Ableitungsregeln

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Einen Überblick über alle grundlegenden Ableitungsregeln haben
> - Die richtige Regel für eine gegebene Funktion auswählen können
> - Mehrere Regeln in Kombination anwenden können
> - Die Ableitungen elementarer Funktionen kennen

---

## Überblick

Die Ableitungsregeln erlauben es, Ableitungen effizient zu berechnen, ohne jedes Mal auf die Definition über den Grenzwert zurückgreifen zu müssen. Sie bauen auf grundlegenden Ableitungen auf und zeigen, wie sich die Ableitung zusammengesetzter Funktionen aus den Ableitungen ihrer Bausteine ergibt.

## Grundlegende Ableitungen

### Ableitungen elementarer Funktionen

| Funktion $f(x)$ | Ableitung $f'(x)$ | Bemerkung |
|-----------------|-------------------|-----------|
| $c$ (Konstante) | $0$ | |
| $x^n$ | $n \cdot x^{n-1}$ | [[Potenzregel\|Potenzregel]] |
| $\sqrt{x} = x^{1/2}$ | $\frac{1}{2\sqrt{x}}$ | Spezialfall der Potenzregel |
| $\frac{1}{x} = x^{-1}$ | $-\frac{1}{x^2}$ | Spezialfall der Potenzregel |
| $e^x$ | $e^x$ | Exponentialfunktion |
| $a^x$ $(a > 0)$ | $a^x \cdot \ln(a)$ | Allgemeine Exponentialfunktion |
| $\ln(x)$ | $\frac{1}{x}$ | Natürlicher Logarithmus |
| $\log_a(x)$ | $\frac{1}{x \cdot \ln(a)}$ | Allgemeiner Logarithmus |
| $\sin(x)$ | $\cos(x)$ | Trigonometrisch |
| $\cos(x)$ | $-\sin(x)$ | Trigonometrisch |
| $\tan(x)$ | $\frac{1}{\cos^2(x)}$ | Trigonometrisch |

## Übersicht der Rechenregeln

### Faktorregel

Für $f(x) = c \cdot g(x)$ mit einer Konstanten $c$:

$$f'(x) = c \cdot g'(x)$$

**Beispiel:** $f(x) = 5x^3 \Rightarrow f'(x) = 5 \cdot 3x^2 = 15x^2$

### Summenregel

Für $f(x) = g(x) + h(x)$:

$$f'(x) = g'(x) + h'(x)$$

Ausführlich: → [[Summenregel|Summenregel]]

**Beispiel:** $f(x) = x^3 + 2x^2 - 5x + 1$
$$f'(x) = 3x^2 + 4x - 5$$

### Potenzregel

Für $f(x) = x^n$ mit $n \in \mathbb{R}$:

$$f'(x) = n \cdot x^{n-1}$$

Ausführlich: → [[Potenzregel|Potenzregel]]

**Beispiele:**
- $f(x) = x^5 \Rightarrow f'(x) = 5x^4$
- $f(x) = x^{-2} = \frac{1}{x^2} \Rightarrow f'(x) = -2x^{-3} = -\frac{2}{x^3}$
- $f(x) = x^{1/3} = \sqrt[3]{x} \Rightarrow f'(x) = \frac{1}{3}x^{-2/3} = \frac{1}{3\sqrt[3]{x^2}}$

### Produktregel

Für $f(x) = u(x) \cdot v(x)$:

$$f'(x) = u'(x) \cdot v(x) + u(x) \cdot v'(x)$$

Ausführlich: → [[Produktregel|Produktregel]]

**Beispiel:** $f(x) = x^2 \cdot e^x$
$$f'(x) = 2x \cdot e^x + x^2 \cdot e^x = e^x(2x + x^2)$$

### Quotientenregel

Für $f(x) = \frac{u(x)}{v(x)}$ mit $v(x) \neq 0$:

$$f'(x) = \frac{u'(x) \cdot v(x) - u(x) \cdot v'(x)}{[v(x)]^2}$$

Ausführlich: → [[Quotientenregel|Quotientenregel]]

**Beispiel:** $f(x) = \frac{x^2}{x + 1}$
$$f'(x) = \frac{2x \cdot (x+1) - x^2 \cdot 1}{(x+1)^2} = \frac{2x^2 + 2x - x^2}{(x+1)^2} = \frac{x^2 + 2x}{(x+1)^2}$$

### Kettenregel

Für $f(x) = g(h(x))$ (Verkettung):

$$f'(x) = g'(h(x)) \cdot h'(x)$$

Kurz: "Äußere Ableitung mal innere Ableitung"

Ausführlich: → [[Kettenregel|Kettenregel]]

**Beispiel:** $f(x) = (3x + 1)^5$
- Äußere Funktion: $g(u) = u^5$, also $g'(u) = 5u^4$
- Innere Funktion: $h(x) = 3x + 1$, also $h'(x) = 3$
$$f'(x) = 5(3x+1)^4 \cdot 3 = 15(3x+1)^4$$

## Anwendungsstrategie

### Schritt 1: Funktionstyp erkennen

Analysiere die Struktur der Funktion:
- Ist es eine Summe/Differenz? → Summenregel
- Ist es ein Produkt? → Produktregel
- Ist es ein Quotient? → Quotientenregel
- Ist es eine Verkettung? → Kettenregel

### Schritt 2: Teilfunktionen identifizieren

Bei zusammengesetzten Regeln die Teile klar benennen:
- Produktregel: $u$ und $v$ festlegen
- Quotientenregel: Zähler $u$ und Nenner $v$
- Kettenregel: Innere und äußere Funktion

### Schritt 3: Systematisch berechnen

Die Regeln sorgfältig anwenden und das Ergebnis vereinfachen.

## Kombinierte Beispiele

### Beispiel 1: Produkt mit Potenz

$f(x) = x^3 \cdot (2x - 1)^4$

**Lösung:** Produktregel mit Kettenregel
- $u = x^3$, $u' = 3x^2$
- $v = (2x-1)^4$, $v' = 4(2x-1)^3 \cdot 2 = 8(2x-1)^3$ (Kettenregel)

$$f'(x) = 3x^2 \cdot (2x-1)^4 + x^3 \cdot 8(2x-1)^3$$
$$= x^2(2x-1)^3 \cdot [3(2x-1) + 8x]$$
$$= x^2(2x-1)^3(6x - 3 + 8x) = x^2(2x-1)^3(14x - 3)$$

### Beispiel 2: Quotient mit Wurzel

$f(x) = \frac{\sqrt{x}}{x + 1}$

**Lösung:** Quotientenregel
- $u = \sqrt{x}$, $u' = \frac{1}{2\sqrt{x}}$
- $v = x + 1$, $v' = 1$

$$f'(x) = \frac{\frac{1}{2\sqrt{x}} \cdot (x+1) - \sqrt{x} \cdot 1}{(x+1)^2}$$
$$= \frac{\frac{x+1}{2\sqrt{x}} - \sqrt{x}}{(x+1)^2}$$
$$= \frac{\frac{x+1 - 2x}{2\sqrt{x}}}{(x+1)^2} = \frac{1-x}{2\sqrt{x}(x+1)^2}$$

### Beispiel 3: Exponentialfunktion mit Polynom

$f(x) = e^{x^2 - 3x}$

**Lösung:** Kettenregel
- Äußere Funktion: $e^u$, Ableitung: $e^u$
- Innere Funktion: $u = x^2 - 3x$, Ableitung: $2x - 3$

$$f'(x) = e^{x^2 - 3x} \cdot (2x - 3)$$

## Merkhilfen

> [!tip] **Merksprüche**
> - **Produktregel**: "Erste mal Ableitung der Zweiten plus Zweite mal Ableitung der Ersten"
> - **Quotientenregel**: "NAZ – ZAN durch N²" (Nenner mal Ableitung Zähler minus Zähler mal Ableitung Nenner, durch Nenner zum Quadrat)
> - **Kettenregel**: "Außen ableiten, Inneres stehen lassen, mal innere Ableitung"

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Potenzregel|Potenzregel]] – Grundlage für Polynome
- → [[Summenregel|Summenregel]] – Ableitung von Summen
- → [[Produktregel|Produktregel]] – Ableitung von Produkten
- → [[Quotientenregel|Quotientenregel]] – Ableitung von Brüchen
- → [[Kettenregel|Kettenregel]] – Ableitung verketteter Funktionen
- → [[Verkettung-von-Funktionen|Verkettung von Funktionen]] – Grundlage für Kettenregel

> [!warning] **Prüfungsrelevant**
> - Alle Ableitungsregeln müssen sicher beherrscht werden
> - Die Ableitungen der elementaren Funktionen müssen auswendig gekonnt werden
> - Kombinationen mehrerer Regeln sind Standardaufgaben
> - Ergebnisse sollten wenn möglich vereinfacht/faktorisiert werden

> [!question] **Typische Prüfungsfragen**
> - "Bestimmen Sie die Ableitung von $f$."
> - "Geben Sie an, welche Ableitungsregel(n) Sie für die Funktion $f$ benötigen."
> - "Berechnen Sie $f'(x)$ und vereinfachen Sie das Ergebnis."

## Quellen

- Bronstein, I.N., Semendjajew, K.A. (2012): *Taschenbuch der Mathematik*. Verlag Europa-Lehrmittel.
- Bigalke, A., Köhler, N. (2015): *Mathematik – Qualifikationsphase*. Cornelsen Verlag.
- Papula, L. (2018): *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1. Springer Vieweg.

> [!tip] **Weiterführende Links**
> - [[Tangenten-und-Normalen|Tangenten und Normalen]] – Anwendung der Ableitungsregeln
> - [[Exponentialfunktionen|Exponentialfunktionen]] – Spezielle Ableitungen
