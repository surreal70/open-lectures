---
author: Andreas Hümmer
title: Differentialquotient
tags:
  - content
  - mathe
  - differentialrechnung
  - differentialquotient
  - grenzwert
  - ableitung
  - analysis
created: 2026-10-17
modified: 2026-10-17
---

# Differentialquotient

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Differentialquotienten als Grenzwert des Differenzenquotienten verstehen
> - Die verschiedenen Notationen für den Differentialquotienten kennen und anwenden können
> - Den Grenzprozess bei einfachen Funktionen durchführen können
> - Die Bedeutung des Differentialquotienten als Ableitung erkennen

---

## Überblick

Der **Differentialquotient** ist der zentrale Begriff der Differentialrechnung. Er entsteht aus dem [[Differenzenquotient|Differenzenquotienten]] durch einen Grenzprozess: Wir lassen die Schrittweite $h$ gegen Null gehen. Während der Differenzenquotient die durchschnittliche Änderungsrate über ein Intervall beschreibt, gibt der Differentialquotient die momentane Änderungsrate an einem einzelnen Punkt an.

Der Differentialquotient ist identisch mit der **Ableitung** der Funktion an der betrachteten Stelle.

## Definition

> [!note] **Definition: Differentialquotient**
> Sei $f$ eine Funktion, die in einer Umgebung von $x_0$ definiert ist. Der **Differentialquotient** von $f$ an der Stelle $x_0$ ist der Grenzwert:
> $$\frac{df}{dx}\bigg|_{x=x_0} = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}$$
> falls dieser Grenzwert existiert.

Der Grenzübergang verwandelt den Differenzenquotienten $\frac{\Delta f}{\Delta x}$ in den Differentialquotienten $\frac{df}{dx}$:

$$\frac{\Delta f}{\Delta x} \xrightarrow{h \to 0} \frac{df}{dx}$$

## Notationen

Für den Differentialquotienten haben sich verschiedene gleichwertige Schreibweisen etabliert:

| Notation | Name | Verwendung |
|----------|------|------------|
| $f'(x_0)$ | Lagrange-Notation | Einfach, kompakt |
| $\frac{df}{dx}\big|_{x=x_0}$ | Leibniz-Notation | Betont die Variable |
| $\frac{dy}{dx}$ | Leibniz (mit $y = f(x)$) | Bei Kurvendiskussion |
| $\dot{f}(t)$ | Newton-Notation | Bei Zeitabhängigkeit |
| $D_x f(x_0)$ | Operator-Notation | Funktionalanalysis |

Die **Leibniz-Notation** $\frac{df}{dx}$ ist besonders anschaulich:
- $df$ steht für ein "unendlich kleines" Änderungsstück der Funktion
- $dx$ steht für ein "unendlich kleines" Änderungsstück des Arguments
- Der Quotient gibt die "Steigung im Unendlich-Kleinen" an

## Der Grenzprozess

### Vom Differenzenquotienten zum Differentialquotienten

```
    Differenzenquotient           Differentialquotient
    
    f(x₀ + h) - f(x₀)      h→0        df
    ─────────────────    ──────►    ────
           h                         dx
    
    Durchschnittliche              Momentane
    Änderungsrate                  Änderungsrate
    
    Sekantensteigung               Tangentensteigung
```

### Visualisierung des Grenzprozesses

Sei $f(x) = x^2$ und $x_0 = 1$. Der Differenzenquotient für verschiedene $h$:

| $h$ | Differenzenquotient $\frac{(1+h)^2 - 1}{h}$ | Wert |
|-----|---------------------------------------------|------|
| 1 | $\frac{4 - 1}{1}$ | 3 |
| 0,5 | $\frac{2{,}25 - 1}{0{,}5}$ | 2,5 |
| 0,1 | $\frac{1{,}21 - 1}{0{,}1}$ | 2,1 |
| 0,01 | $\frac{1{,}0201 - 1}{0{,}01}$ | 2,01 |
| 0,001 | $\frac{1{,}002001 - 1}{0{,}001}$ | 2,001 |

Der Grenzwert ist $f'(1) = 2$.

## Berechnungsbeispiele

### Beispiel 1: Potenzfunktion $f(x) = x^2$

Berechne den Differentialquotienten an einer beliebigen Stelle $x_0$:

$$\frac{df}{dx} = \lim_{h \to 0} \frac{(x_0 + h)^2 - x_0^2}{h}$$
$$= \lim_{h \to 0} \frac{x_0^2 + 2x_0 h + h^2 - x_0^2}{h}$$
$$= \lim_{h \to 0} \frac{2x_0 h + h^2}{h}$$
$$= \lim_{h \to 0} (2x_0 + h) = 2x_0$$

Also: $f'(x) = 2x$

### Beispiel 2: Potenzfunktion $f(x) = x^3$

$$\frac{df}{dx} = \lim_{h \to 0} \frac{(x_0 + h)^3 - x_0^3}{h}$$

Mit $(x_0 + h)^3 = x_0^3 + 3x_0^2 h + 3x_0 h^2 + h^3$:

$$= \lim_{h \to 0} \frac{3x_0^2 h + 3x_0 h^2 + h^3}{h}$$
$$= \lim_{h \to 0} (3x_0^2 + 3x_0 h + h^2) = 3x_0^2$$

Also: $f'(x) = 3x^2$

### Beispiel 3: Wurzelfunktion $f(x) = \sqrt{x}$

$$\frac{df}{dx} = \lim_{h \to 0} \frac{\sqrt{x_0 + h} - \sqrt{x_0}}{h}$$

Erweitern mit konjugierter Wurzel:
$$= \lim_{h \to 0} \frac{(\sqrt{x_0 + h} - \sqrt{x_0})(\sqrt{x_0 + h} + \sqrt{x_0})}{h(\sqrt{x_0 + h} + \sqrt{x_0})}$$
$$= \lim_{h \to 0} \frac{(x_0 + h) - x_0}{h(\sqrt{x_0 + h} + \sqrt{x_0})}$$
$$= \lim_{h \to 0} \frac{1}{\sqrt{x_0 + h} + \sqrt{x_0}} = \frac{1}{2\sqrt{x_0}}$$

Also: $f'(x) = \frac{1}{2\sqrt{x}}$

### Beispiel 4: Kehrwertfunktion $f(x) = \frac{1}{x}$

$$\frac{df}{dx} = \lim_{h \to 0} \frac{\frac{1}{x_0 + h} - \frac{1}{x_0}}{h}$$
$$= \lim_{h \to 0} \frac{\frac{x_0 - (x_0 + h)}{(x_0 + h) \cdot x_0}}{h}$$
$$= \lim_{h \to 0} \frac{-h}{h(x_0 + h) x_0}$$
$$= \lim_{h \to 0} \frac{-1}{(x_0 + h) x_0} = -\frac{1}{x_0^2}$$

Also: $f'(x) = -\frac{1}{x^2}$

## Existenz des Differentialquotienten

Der Differentialquotient existiert an einer Stelle $x_0$, wenn:

1. Die Funktion in einer Umgebung von $x_0$ definiert ist
2. Der Grenzwert $\lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}$ existiert und endlich ist

> [!warning] **Nicht-Existenz**
> Der Differentialquotient existiert **nicht**, wenn:
> - Die Funktion an $x_0$ nicht stetig ist (Sprungstelle)
> - Die Funktion einen "Knick" hat (links- und rechtsseitiger Grenzwert verschieden)
> - Die Tangente senkrecht ist (Grenzwert $\pm \infty$)

### Beispiel: Betragsfunktion

Für $f(x) = |x|$ an der Stelle $x_0 = 0$:

- Linksseitiger Grenzwert: $\lim_{h \to 0^-} \frac{|h| - 0}{h} = \lim_{h \to 0^-} \frac{-h}{h} = -1$
- Rechtsseitiger Grenzwert: $\lim_{h \to 0^+} \frac{|h| - 0}{h} = \lim_{h \to 0^+} \frac{h}{h} = 1$

Da die einseitigen Grenzwerte verschieden sind, existiert $f'(0)$ nicht.

## Zusammenhang mit der Ableitung

Der Differentialquotient an der Stelle $x_0$ ist **definitionsgemäß** die Ableitung $f'(x_0)$.

Wenn wir den Differentialquotienten für alle $x$ berechnen, erhalten wir die **Ableitungsfunktion** $f'$:

$$f'(x) = \frac{df}{dx} = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Differenzenquotient|Differenzenquotient]] – Der Ausgangspunkt vor dem Grenzübergang
- → [[Definition-der-Ableitung|Definition der Ableitung]] – Formale Einführung
- → [[Momentane-aenderungsrate|Momentane Änderungsrate]] – Physikalische Interpretation
- → [[Geometrische-Bedeutung-der-Ableitung|Geometrische Bedeutung]] – Visualisierung
- → [[Grenzwerte-von-Funktionen|Grenzwerte von Funktionen]] – Mathematische Grundlage

> [!warning] **Prüfungsrelevant**
> - Die Grenzwertdefinition $\lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}$ muss sicher beherrscht werden
> - Das Durchführen des Grenzübergangs bei einfachen Funktionen (Polynome, Wurzel, Kehrwert) ist Standardaufgabe
> - Die verschiedenen Notationen müssen erkannt und verstanden werden
> - Das Erkennen von Stellen, an denen der Differentialquotient nicht existiert

> [!question] **Typische Prüfungsfragen**
> - "Berechnen Sie die Ableitung von $f$ an der Stelle $x_0$ mithilfe der Definition."
> - "Zeigen Sie mithilfe des Differentialquotienten, dass $f'(x) = ...$"
> - "An welchen Stellen existiert der Differentialquotient nicht? Begründen Sie."

## Quellen

- Bronstein, I.N., Semendjajew, K.A. (2012): *Taschenbuch der Mathematik*. Verlag Europa-Lehrmittel.
- Papula, L. (2018): *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1. Springer Vieweg.
- Griesel, H., Postel, H., Suhr, F. (2019): *Elemente der Mathematik – Qualifikationsphase*. Schroedel Verlag.

> [!tip] **Weiterführende Links**
> - [[Ableitungsregeln|Ableitungsregeln]] – Effizientes Ableiten ohne Grenzwertberechnung
> - [[Potenzregel|Potenzregel]] – Erste wichtige Ableitungsregel
