---
author: Andreas Hümmer
title: Konvergenz
tags:
  - content
  - mathe
  - folgen
  - konvergenz
  - grenzwert
  - analysis
created: 2025-06-17
modified: 2025-06-17
---

# Konvergenz

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Begriff der Konvergenz anschaulich und formal verstehen
> - Die Epsilon-Definition des Grenzwerts kennen und anwenden können
> - Konvergenzkriterien anwenden können
> - Den Unterschied zwischen Konvergenz und Divergenz verstehen
> - Wichtige konvergente Folgen und ihre Grenzwerte kennen

---

## Überblick

Der Begriff der **Konvergenz** ist eines der fundamentalsten Konzepte der Analysis. Eine Folge heißt konvergent, wenn sich ihre Glieder einem bestimmten Wert beliebig nähern. Dieser Wert heißt **Grenzwert** oder **Limes** der Folge. Das Konzept der Konvergenz ermöglicht es uns, über "unendliche Prozesse" rigoros zu sprechen und bildet die Grundlage für Differentialrechnung, Integralrechnung und viele weitere Bereiche der Mathematik.

## Anschauliche Definition

### Intuitive Beschreibung

Eine Folge $(a_n)$ **konvergiert** gegen einen Wert $L$, wenn sich die Folgenglieder $a_n$ für große $n$ dem Wert $L$ beliebig annähern und dort "bleiben".

**Schreibweise:**
$$\lim_{n \to \infty} a_n = L \quad \text{oder} \quad a_n \to L \text{ für } n \to \infty$$

**Sprechweise:** "Der Limes von $a_n$ für $n$ gegen unendlich ist $L$" oder "$a_n$ konvergiert gegen $L$".

### Beispiel: Die Folge $a_n = \frac{1}{n}$

| $n$ | $a_n = \frac{1}{n}$ |
|-----|---------------------|
| 1 | 1 |
| 10 | 0,1 |
| 100 | 0,01 |
| 1.000 | 0,001 |
| 10.000 | 0,0001 |

Die Werte nähern sich beliebig der 0 an: $\lim_{n \to \infty} \frac{1}{n} = 0$

## Die Epsilon-Definition (Cauchy)

### Formale Definition

Eine Folge $(a_n)$ **konvergiert gegen $L$**, wenn gilt:

$$\boxed{\forall \varepsilon > 0 \; \exists N \in \mathbb{N} : \forall n \geq N : |a_n - L| < \varepsilon}$$

**In Worten:** Zu jeder noch so kleinen positiven Zahl $\varepsilon$ gibt es einen Index $N$, sodass alle Folgenglieder ab diesem Index weniger als $\varepsilon$ von $L$ entfernt sind.

### Interpretation

- $\varepsilon$ ist eine "Toleranz" oder "Schlauchbreite" um $L$
- $N$ ist der Index, ab dem alle Glieder im $\varepsilon$-Schlauch liegen
- Je kleiner $\varepsilon$, desto größer muss $N$ sein

### Beispiel: Beweis für $\lim_{n \to \infty} \frac{1}{n} = 0$

**Zu zeigen:** $\forall \varepsilon > 0 \; \exists N : \forall n \geq N : \left|\frac{1}{n} - 0\right| < \varepsilon$

**Beweis:**
Sei $\varepsilon > 0$ beliebig gegeben.

Wir brauchen: $\frac{1}{n} < \varepsilon \quad \Leftrightarrow \quad n > \frac{1}{\varepsilon}$

Wähle $N = \lceil \frac{1}{\varepsilon} \rceil + 1$ (nächste ganze Zahl größer als $\frac{1}{\varepsilon}$).

Für alle $n \geq N$ gilt dann: $n > \frac{1}{\varepsilon}$, also $\frac{1}{n} < \varepsilon$. ∎

## Konvergenzkriterien

### Monotoniekriterium

> Jede **monotone und beschränkte** Folge ist konvergent.

**Präziser:**
- Monoton wachsend und nach oben beschränkt → konvergent gegen das Supremum
- Monoton fallend und nach unten beschränkt → konvergent gegen das Infimum

**Beispiel:** $a_n = \frac{n}{n+1}$
- Monoton wachsend: $\frac{a_{n+1}}{a_n} = \frac{(n+1)^2}{n(n+2)} > 1$ ✓
- Beschränkt durch 1: $a_n < 1$ für alle $n$ ✓
- Also konvergent, Grenzwert: $\lim_{n \to \infty} \frac{n}{n+1} = 1$

### Einschließungskriterium (Sandwich-Theorem)

Seien $(a_n)$, $(b_n)$, $(c_n)$ Folgen mit:
- $a_n \leq b_n \leq c_n$ für alle $n \geq N_0$
- $\lim_{n \to \infty} a_n = \lim_{n \to \infty} c_n = L$

Dann gilt: $\lim_{n \to \infty} b_n = L$

**Beispiel:** Zeige $\lim_{n \to \infty} \frac{\sin(n)}{n} = 0$

Da $-1 \leq \sin(n) \leq 1$, gilt:
$$-\frac{1}{n} \leq \frac{\sin(n)}{n} \leq \frac{1}{n}$$

Mit $\lim_{n \to \infty} \left(-\frac{1}{n}\right) = \lim_{n \to \infty} \frac{1}{n} = 0$ folgt: $\lim_{n \to \infty} \frac{\sin(n)}{n} = 0$

## Wichtige konvergente Folgen

| Folge | Grenzwert | Bedingung |
|-------|-----------|-----------|
| $a_n = \frac{1}{n^k}$ | $0$ | $k > 0$ |
| $a_n = q^n$ | $0$ | $\|q\| < 1$ |
| $a_n = \sqrt[n]{n}$ | $1$ | — |
| $a_n = \sqrt[n]{a}$ | $1$ | $a > 0$ |
| $a_n = \left(1 + \frac{1}{n}\right)^n$ | $e$ | — |
| $a_n = \frac{n^k}{a^n}$ | $0$ | $a > 1$, $k$ beliebig |

### Die Eulersche Zahl $e$

Die Folge $a_n = \left(1 + \frac{1}{n}\right)^n$ konvergiert gegen die **Eulersche Zahl**:

$$e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n \approx 2,71828...$$

Diese Zahl ist fundamental für die Exponentialfunktion und den natürlichen Logarithmus.

## Eindeutigkeit des Grenzwerts

> Der Grenzwert einer konvergenten Folge ist **eindeutig**.

**Beweis (Idee):** Angenommen, $(a_n)$ konvergiert gegen $L_1$ und $L_2$ mit $L_1 \neq L_2$. Wähle $\varepsilon = \frac{|L_1 - L_2|}{2}$. Dann müssten alle Glieder ab einem Index sowohl in einem $\varepsilon$-Schlauch um $L_1$ als auch um $L_2$ liegen – ein Widerspruch, da sich diese Schläuche nicht überlappen.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Zahlenfolgen]] – Grundlagen des Folgenbegriffs
- → [[Divergenz]] – Das Gegenteil: nicht-konvergente Folgen
- → [[Grenzwerte-von-Folgen]] – Rechenregeln für Grenzwerte
- → [[Grenzwerte-von-Funktionen]] – Übertragung auf Funktionen
- → [[Geometrische-Folgen]] – Wichtige Klasse konvergenter Folgen ($|q| < 1$)

> [!warning] **Prüfungsrelevant**
> - Die anschauliche Bedeutung von Konvergenz muss verstanden sein
> - Wichtige konvergente Folgen und ihre Grenzwerte sind Grundwissen
> - Das Monotoniekriterium wird häufig in Beweisen verwendet
> - Die Epsilon-Definition kann in Leistungskursen abgefragt werden
> - Die Folge für die Eulersche Zahl $e$ ist ein Klassiker

> [!question] **Typische Prüfungsfragen**
> - Untersuche die Folge $a_n = \frac{2n^2 + 1}{n^2 + 3}$ auf Konvergenz und bestimme ggf. den Grenzwert.
> - Zeige mit dem Monotoniekriterium, dass die Folge $a_n = \frac{n!}{n^n}$ konvergiert.
> - Erkläre anschaulich, was es bedeutet, dass eine Folge gegen einen Grenzwert konvergiert.

## Quellen

- Forster, O.: Analysis 1. Springer Spektrum, 2016.
- Heuser, H.: Lehrbuch der Analysis, Teil 1. Springer Vieweg, 2009.
- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.

> [!tip] **Weiterführende Links**
> - [[Stetigkeit]] – Konvergenz als Grundlage für Stetigkeit
> - [[Einfuehrung-in-die-mathematische-Grenzwertbildung]] – Formale Beweistechniken
