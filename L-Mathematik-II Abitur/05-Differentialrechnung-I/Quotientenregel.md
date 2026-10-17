---
author: Andreas Hümmer
title: Quotientenregel
tags:
  - content
  - mathe
  - differentialrechnung
  - ableitung
  - quotientenregel
  - analysis
created: 2026-10-17
modified: 2026-10-17
---

# Quotientenregel

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Quotientenregel formulieren und anwenden können
> - Brüche aus Funktionen sicher ableiten können
> - Den Zusammenhang zur Produktregel verstehen
> - Die Quotientenregel in Kombination mit anderen Regeln nutzen können

---

## Überblick

Die Quotientenregel ermöglicht das Ableiten von Funktionen, die als Quotient (Bruch) zweier differenzierbarer Funktionen geschrieben sind. Sie ist die "Schwester" der [[Produktregel|Produktregel]] und wird überall dort benötigt, wo der Nenner keine Konstante ist und sich der Bruch nicht sinnvoll umschreiben lässt.

## Die Quotientenregel

> [!note] **Satz: Quotientenregel**
> Sind $u$ und $v$ differenzierbare Funktionen mit $v(x) \neq 0$, so ist auch $f = \frac{u}{v}$ differenzierbar, und es gilt:
> $$\left(\frac{u}{v}\right)'(x) = \frac{u'(x) \cdot v(x) - u(x) \cdot v'(x)}{[v(x)]^2}$$

**Kurzform:**
$$\left(\frac{u}{v}\right)' = \frac{u' \cdot v - u \cdot v'}{v^2}$$

**Merkspruch:** "NAZ – ZAN durch N²"
- **N**enner mal **A**bleitung **Z**ähler
- minus **Z**ähler mal **A**bleitung **N**enner
- durch **N**enner zum **Q**uadrat

Alternative: "Nenner mal Ableitung Zähler minus Zähler mal Ableitung Nenner, das Ganze durch Nenner zum Quadrat"

## Herleitung aus der Produktregel

Wir schreiben $\frac{u}{v} = u \cdot v^{-1}$ und wenden die Produktregel an:

$$\left(\frac{u}{v}\right)' = (u \cdot v^{-1})' = u' \cdot v^{-1} + u \cdot (v^{-1})'$$

Mit $(v^{-1})' = -v^{-2} \cdot v' = -\frac{v'}{v^2}$ (Kettenregel):

$$= \frac{u'}{v} - \frac{u \cdot v'}{v^2} = \frac{u' \cdot v - u \cdot v'}{v^2}$$

## Beispiele

### Beispiel 1: Einfacher Bruch

$f(x) = \frac{x^2}{x + 1}$

**Lösung:**
- $u = x^2$, $u' = 2x$
- $v = x + 1$, $v' = 1$

$$f'(x) = \frac{2x \cdot (x + 1) - x^2 \cdot 1}{(x + 1)^2}$$
$$= \frac{2x^2 + 2x - x^2}{(x + 1)^2} = \frac{x^2 + 2x}{(x + 1)^2} = \frac{x(x + 2)}{(x + 1)^2}$$

### Beispiel 2: Polynome im Zähler und Nenner

$f(x) = \frac{x^3 - 1}{x^2 + 1}$

**Lösung:**
- $u = x^3 - 1$, $u' = 3x^2$
- $v = x^2 + 1$, $v' = 2x$

$$f'(x) = \frac{3x^2 \cdot (x^2 + 1) - (x^3 - 1) \cdot 2x}{(x^2 + 1)^2}$$
$$= \frac{3x^4 + 3x^2 - 2x^4 + 2x}{(x^2 + 1)^2}$$
$$= \frac{x^4 + 3x^2 + 2x}{(x^2 + 1)^2} = \frac{x(x^3 + 3x + 2)}{(x^2 + 1)^2}$$

### Beispiel 3: Exponentialfunktion im Nenner

$f(x) = \frac{x}{e^x}$

**Lösung:**
- $u = x$, $u' = 1$
- $v = e^x$, $v' = e^x$

$$f'(x) = \frac{1 \cdot e^x - x \cdot e^x}{(e^x)^2} = \frac{e^x(1 - x)}{e^{2x}} = \frac{1 - x}{e^x}$$

### Beispiel 4: Trigonometrischer Bruch

$f(x) = \frac{\sin(x)}{\cos(x)} = \tan(x)$

**Lösung:**
- $u = \sin(x)$, $u' = \cos(x)$
- $v = \cos(x)$, $v' = -\sin(x)$

$$f'(x) = \frac{\cos(x) \cdot \cos(x) - \sin(x) \cdot (-\sin(x))}{\cos^2(x)}$$
$$= \frac{\cos^2(x) + \sin^2(x)}{\cos^2(x)} = \frac{1}{\cos^2(x)}$$

Dies beweist: $(\tan x)' = \frac{1}{\cos^2(x)}$

### Beispiel 5: Wurzel im Bruch

$f(x) = \frac{\sqrt{x}}{x - 2}$

**Lösung:**
- $u = \sqrt{x}$, $u' = \frac{1}{2\sqrt{x}}$
- $v = x - 2$, $v' = 1$

$$f'(x) = \frac{\frac{1}{2\sqrt{x}} \cdot (x - 2) - \sqrt{x} \cdot 1}{(x - 2)^2}$$
$$= \frac{\frac{x - 2}{2\sqrt{x}} - \sqrt{x}}{(x - 2)^2}$$

Hauptnenner im Zähler: $\sqrt{x}$ wird zu $\frac{2x}{2\sqrt{x}}$:
$$= \frac{\frac{x - 2 - 2x}{2\sqrt{x}}}{(x - 2)^2} = \frac{-x - 2}{2\sqrt{x}(x - 2)^2}$$

## Kombination mit der Kettenregel

$f(x) = \frac{x}{(2x + 1)^3}$

**Lösung:**
- $u = x$, $u' = 1$
- $v = (2x + 1)^3$, $v' = 3(2x + 1)^2 \cdot 2 = 6(2x + 1)^2$ (Kettenregel!)

$$f'(x) = \frac{1 \cdot (2x + 1)^3 - x \cdot 6(2x + 1)^2}{(2x + 1)^6}$$
$$= \frac{(2x + 1)^2 [(2x + 1) - 6x]}{(2x + 1)^6}$$
$$= \frac{1 - 4x}{(2x + 1)^4}$$

## Spezialfall: Kehrwertfunktion

Für $f(x) = \frac{1}{v(x)}$ vereinfacht sich die Quotientenregel:

$$\left(\frac{1}{v}\right)' = \frac{0 \cdot v - 1 \cdot v'}{v^2} = -\frac{v'}{v^2}$$

**Beispiel:** $f(x) = \frac{1}{x^2 + 1}$
$$f'(x) = -\frac{2x}{(x^2 + 1)^2}$$

## Wann Quotientenregel anwenden?

**Quotientenregel nötig:**
- Nenner enthält die Variable $x$ und ist keine Potenz von $x$
- Bruch lässt sich nicht sinnvoll umschreiben

**Quotientenregel nicht nötig:**
- Nenner ist konstant → Faktorregel
- Bruch lässt sich als Produkt schreiben, z.B. $\frac{x^2}{x^3} = x^{-1}$
- Nur negative Potenz von $x$ im Nenner → Potenzregel

**Beispiel:** $\frac{3x^2}{5}$ braucht keine Quotientenregel, sondern nur $\frac{3}{5} \cdot 2x = \frac{6x}{5}$

## Typische Fehler

> [!warning] **Häufige Fehler**
> 1. **Reihenfolge vertauscht:** Es ist $u'v - uv'$, nicht $uv' - u'v$
> 2. **Quadrat vergessen:** Der Nenner muss quadriert werden: $v^2$
> 3. **Vereinfachung vergessen:** Das Ergebnis sollte wenn möglich faktorisiert werden

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Ableitungsregeln|Ableitungsregeln]] – Übersicht aller Regeln
- → [[Produktregel|Produktregel]] – Die "Schwester" der Quotientenregel
- → [[Kettenregel|Kettenregel]] – Oft kombiniert
- → [[Gebrochenrationale-Funktionen|Gebrochenrationale Funktionen]] – Hauptanwendungsgebiet
- → [[Potenzregel|Potenzregel]] – Alternative bei einfachen Brüchen

> [!warning] **Prüfungsrelevant**
> - Die Quotientenregel muss absolut sicher beherrscht werden
> - Der Merkspruch "NAZ – ZAN durch N²" hilft bei der Reihenfolge
> - Die Kombination mit der Kettenregel ist Standard
> - Ergebnisse faktorisieren und wenn möglich kürzen

> [!question] **Typische Prüfungsfragen**
> - "Bestimmen Sie die Ableitung von $f(x) = \frac{...}{...}$"
> - "Für welche $x$ gilt $f'(x) = 0$?" (Nullstellen nur im Zähler suchen!)
> - "Zeigen Sie mithilfe der Quotientenregel, dass $(\tan x)' = \frac{1}{\cos^2 x}$"

## Quellen

- Bronstein, I.N., Semendjajew, K.A. (2012): *Taschenbuch der Mathematik*. Verlag Europa-Lehrmittel.
- Bigalke, A., Köhler, N. (2015): *Mathematik – Qualifikationsphase*. Cornelsen Verlag.
- Papula, L. (2018): *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1. Springer Vieweg.

> [!tip] **Weiterführende Links**
> - [[Kettenregel|Kettenregel]] – Die dritte wichtige Ableitungsregel
> - [[Tangenten-und-Normalen|Tangenten und Normalen]] – Anwendung der Ableitung
