---
author: Andreas Hümmer
title: Grenzwerte von Folgen
tags:
  - content
  - mathe
  - folgen
  - grenzwert
  - limes
  - analysis
created: 2025-06-17
modified: 2025-06-17
---

# Grenzwerte von Folgen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Grenzwerte von Folgen mit algebraischen Methoden berechnen können
> - Die Grenzwertsätze sicher anwenden können
> - Standardgrenzwerte kennen und einsetzen können
> - Unbestimmte Ausdrücke durch Umformung auflösen können
> - Rationale Folgen und Wurzelfolgen behandeln können

---

## Überblick

Die **Berechnung von Grenzwerten** ist eine zentrale Fähigkeit in der Analysis. Während die Definition des Grenzwerts (Epsilon-Kriterium) für das Verständnis wichtig ist, erfolgt die praktische Berechnung meist über algebraische Umformungen und Rechenregeln. In diesem Kapitel werden die wichtigsten Techniken zur Grenzwertberechnung vorgestellt.

## Grenzwertsätze

### Rechenregeln für konvergente Folgen

Seien $(a_n)$ und $(b_n)$ konvergente Folgen mit $\lim_{n \to \infty} a_n = a$ und $\lim_{n \to \infty} b_n = b$. Dann gilt:

| Regel | Formel |
|-------|--------|
| **Summenregel** | $\lim_{n \to \infty} (a_n + b_n) = a + b$ |
| **Differenzregel** | $\lim_{n \to \infty} (a_n - b_n) = a - b$ |
| **Produktregel** | $\lim_{n \to \infty} (a_n \cdot b_n) = a \cdot b$ |
| **Quotientenregel** | $\lim_{n \to \infty} \frac{a_n}{b_n} = \frac{a}{b}$ (falls $b \neq 0$) |
| **Potenzregel** | $\lim_{n \to \infty} a_n^k = a^k$ |
| **Wurzelregel** | $\lim_{n \to \infty} \sqrt[k]{a_n} = \sqrt[k]{a}$ (falls $a_n \geq 0$) |
| **Faktorregel** | $\lim_{n \to \infty} (c \cdot a_n) = c \cdot a$ |

### Wichtig: Voraussetzungen beachten!

Die Regeln gelten nur, wenn beide Folgen konvergieren und keine Division durch Null auftritt.

## Standardgrenzwerte

Diese Grenzwerte solltest du auswendig kennen:

| Folge | Grenzwert | Bedingung |
|-------|-----------|-----------|
| $\frac{1}{n}$ | $0$ | — |
| $\frac{1}{n^k}$ | $0$ | $k > 0$ |
| $q^n$ | $0$ | $\|q\| < 1$ |
| $\sqrt[n]{n}$ | $1$ | — |
| $\sqrt[n]{a}$ | $1$ | $a > 0$ |
| $\left(1 + \frac{1}{n}\right)^n$ | $e$ | — |
| $\left(1 + \frac{x}{n}\right)^n$ | $e^x$ | — |
| $\frac{a^n}{n!}$ | $0$ | $a > 0$ beliebig |
| $\frac{n^k}{a^n}$ | $0$ | $a > 1$, $k$ beliebig |

**Merkregel für Wachstumsvergleich:**
$$n! \gg a^n \gg n^k \gg \ln(n)$$
("Fakultät schlägt Exponential schlägt Polynom schlägt Logarithmus")

## Grenzwerte rationaler Folgen

### Standardmethode: Ausklammern der höchsten Potenz

Für rationale Folgen der Form $a_n = \frac{P(n)}{Q(n)}$ (Polynome im Zähler und Nenner):

**Strategie:** Klammere im Zähler und Nenner die höchste Potenz von $n$ aus.

### Fall 1: Grad Zähler < Grad Nenner → Grenzwert 0

$$\lim_{n \to \infty} \frac{3n + 1}{n^2 + 2} = \lim_{n \to \infty} \frac{n(3 + \frac{1}{n})}{n^2(1 + \frac{2}{n^2})} = \lim_{n \to \infty} \frac{3 + \frac{1}{n}}{n(1 + \frac{2}{n^2})} = \frac{3}{+\infty} = 0$$

### Fall 2: Grad Zähler = Grad Nenner → Quotient der Leitkoeffizienten

$$\lim_{n \to \infty} \frac{5n^2 + 3n}{2n^2 + 1} = \lim_{n \to \infty} \frac{n^2(5 + \frac{3}{n})}{n^2(2 + \frac{1}{n^2})} = \frac{5 + 0}{2 + 0} = \frac{5}{2}$$

### Fall 3: Grad Zähler > Grad Nenner → bestimmte Divergenz

$$\lim_{n \to \infty} \frac{n^3 + 1}{n^2 + 1} = \lim_{n \to \infty} \frac{n^3(1 + \frac{1}{n^3})}{n^2(1 + \frac{1}{n^2})} = \lim_{n \to \infty} n \cdot \frac{1 + 0}{1 + 0} = +\infty$$

### Merkregel

$$\lim_{n \to \infty} \frac{a_m n^m + \ldots}{b_k n^k + \ldots} = \begin{cases} 0 & \text{falls } m < k \\ \frac{a_m}{b_k} & \text{falls } m = k \\ \pm\infty & \text{falls } m > k \end{cases}$$

## Grenzwerte mit Wurzeln

### Methode: Rationalisieren (Erweitern mit konjugiertem Ausdruck)

**Beispiel:** $\lim_{n \to \infty} \left(\sqrt{n+1} - \sqrt{n}\right)$

Erweitere mit $(\sqrt{n+1} + \sqrt{n})$:

$$\begin{align}
\sqrt{n+1} - \sqrt{n} &= \frac{(\sqrt{n+1} - \sqrt{n})(\sqrt{n+1} + \sqrt{n})}{\sqrt{n+1} + \sqrt{n}} \\
&= \frac{(n+1) - n}{\sqrt{n+1} + \sqrt{n}} \\
&= \frac{1}{\sqrt{n+1} + \sqrt{n}}
\end{align}$$

Da $\sqrt{n+1} + \sqrt{n} \to +\infty$, folgt:

$$\lim_{n \to \infty} \left(\sqrt{n+1} - \sqrt{n}\right) = 0$$

### Beispiel mit quadratischem Ausdruck

$$\lim_{n \to \infty} \left(\sqrt{n^2 + n} - n\right)$$

$$= \lim_{n \to \infty} \frac{(n^2 + n) - n^2}{\sqrt{n^2 + n} + n} = \lim_{n \to \infty} \frac{n}{\sqrt{n^2 + n} + n}$$

Ausklammern von $n$:
$$= \lim_{n \to \infty} \frac{n}{n(\sqrt{1 + \frac{1}{n}} + 1)} = \frac{1}{\sqrt{1} + 1} = \frac{1}{2}$$

## Unbestimmte Ausdrücke

### Die "unbestimmten Formen"

Folgende Kombinationen erfordern genauere Analyse:

| Form | Beispiel |
|------|----------|
| $\frac{0}{0}$ | $\frac{\sin(1/n)}{1/n}$ |
| $\frac{\infty}{\infty}$ | $\frac{n^2}{n^2+1}$ |
| $0 \cdot \infty$ | $n \cdot \frac{1}{n}$ |
| $\infty - \infty$ | $\sqrt{n+1} - \sqrt{n}$ |
| $1^\infty$ | $\left(1 + \frac{1}{n}\right)^n$ |
| $0^0$ | — |
| $\infty^0$ | — |

**Lösungsstrategie:** Umformung, sodass die Grenzwertsätze anwendbar werden.

## Praktische Beispiele

### Beispiel 1

$$\lim_{n \to \infty} \frac{3n^2 - 2n + 5}{4n^2 + n - 1}$$

Grad Zähler = Grad Nenner = 2, also:

$$= \frac{3}{4}$$

### Beispiel 2

$$\lim_{n \to \infty} \frac{(2n+1)^3}{n^3 + 1}$$

Ausmultiplizieren: $(2n+1)^3 = 8n^3 + 12n^2 + 6n + 1$

$$= \lim_{n \to \infty} \frac{8n^3 + 12n^2 + 6n + 1}{n^3 + 1} = \frac{8}{1} = 8$$

### Beispiel 3

$$\lim_{n \to \infty} \left(1 + \frac{3}{n}\right)^{2n}$$

Umschreiben: $= \left[\left(1 + \frac{3}{n}\right)^n\right]^2 = (e^3)^2 = e^6$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Konvergenz]] – Definition und Kriterien
- → [[Divergenz]] – Wenn kein endlicher Grenzwert existiert
- → [[Grenzwerte-von-Funktionen]] – Übertragung auf kontinuierliche Funktionen
- → [[Rekursive-Folgen]] – Grenzwerte rekursiv definierter Folgen
- → [[Definition-der-Ableitung]] – Grenzwerte zur Definition der Ableitung

> [!warning] **Prüfungsrelevant**
> - Grenzwertsätze müssen sicher angewendet werden können
> - Die Standardgrenzwerte sind auswendig zu lernen
> - Rationale Folgen: Methode des Ausklammerns ist Standard
> - Wurzelausdrücke: Rationalisieren durch Erweitern ist häufig
> - Die "Hierarchie des Wachstums" (Fakultät > Exponential > Polynom > Log) ist wichtig

> [!question] **Typische Prüfungsfragen**
> - Berechne $\lim_{n \to \infty} \frac{(n+2)^2 - n^2}{3n + 1}$.
> - Bestimme $\lim_{n \to \infty} \left(\sqrt{4n^2 + 3n} - 2n\right)$.
> - Zeige: $\lim_{n \to \infty} \frac{2^n}{n!} = 0$.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Forster, O.: Analysis 1. Springer Spektrum, 2016.
- Bronstein, I. N. et al.: Taschenbuch der Mathematik. Europa-Lehrmittel, 2020.

> [!tip] **Weiterführende Links**
> - [[Unendliche-geometrische-Reihen]] – Summenbildung und Konvergenz
> - [[Stetigkeit]] – Grenzwerte und Funktionsverhalten
