---
author: Andreas Hümmer
title: Uneigentliche Integrale – Einführung
tags:
  - content
  - mathe
  - integralrechnung
  - uneigentliche-integrale
  - grenzwerte
created: 2025-06-26
modified: 2025-06-26
---

# Uneigentliche Integrale – Einführung

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Verstehen, was uneigentliche Integrale sind und wann sie auftreten
> - Uneigentliche Integrale 1. Art (unbeschränkte Intervalle) berechnen können
> - Uneigentliche Integrale 2. Art (unbeschränkte Integranden) erkennen können
> - Konvergenz und Divergenz von uneigentlichen Integralen beurteilen können

---

## Überblick

Bisher haben wir **bestimmte Integrale** nur über beschränkte Intervalle $[a, b]$ mit stetigen Integranden betrachtet. **Uneigentliche Integrale** erweitern dieses Konzept auf:

1. **Unbeschränkte Integrationsintervalle** (z.B. $[a, \infty)$) – **Typ I**
2. **Unbeschränkte Integranden** (z.B. Polstellen) – **Typ II**

Diese Integrale werden als **Grenzwerte** definiert und können entweder einen endlichen Wert (konvergent) oder keinen endlichen Wert (divergent) haben.

---

## Uneigentliche Integrale 1. Art (unbeschränktes Intervall)

### Definition

Ist $f$ auf $[a, \infty)$ stetig, so definiert man:

$$\int_a^{\infty} f(x) \, dx = \lim_{b \to \infty} \int_a^b f(x) \, dx$$

Falls der Grenzwert existiert und endlich ist, heißt das Integral **konvergent**, sonst **divergent**.

Analog für $(-\infty, b]$:

$$\int_{-\infty}^b f(x) \, dx = \lim_{a \to -\infty} \int_a^b f(x) \, dx$$

Und für $(-\infty, \infty)$:

$$\int_{-\infty}^{\infty} f(x) \, dx = \int_{-\infty}^c f(x) \, dx + \int_c^{\infty} f(x) \, dx$$

(Beide Teilintegrale müssen konvergieren.)

---

## Beispiele für Typ I

### Beispiel 1: Konvergentes Integral

Berechne $\int_1^{\infty} \frac{1}{x^2} \, dx$

**Lösung:**

$$\int_1^{\infty} \frac{1}{x^2} \, dx = \lim_{b \to \infty} \int_1^b x^{-2} \, dx = \lim_{b \to \infty} \left[-x^{-1}\right]_1^b$$

$$= \lim_{b \to \infty} \left(-\frac{1}{b} + 1\right) = 0 + 1 = 1$$

Das Integral **konvergiert** mit Wert 1.

> [!tip] **Anschauung**
> Obwohl die Fläche unter der Kurve bis ins Unendliche reicht, ist sie endlich! Die Funktion fällt schnell genug gegen 0.

### Beispiel 2: Divergentes Integral

Berechne $\int_1^{\infty} \frac{1}{x} \, dx$

**Lösung:**

$$\int_1^{\infty} \frac{1}{x} \, dx = \lim_{b \to \infty} \int_1^b \frac{1}{x} \, dx = \lim_{b \to \infty} [\ln x]_1^b$$

$$= \lim_{b \to \infty} (\ln b - \ln 1) = \lim_{b \to \infty} \ln b = \infty$$

Das Integral **divergiert** – die Fläche ist unendlich groß.

### Beispiel 3: Exponentialfunktion

Berechne $\int_0^{\infty} e^{-x} \, dx$

**Lösung:**

$$\int_0^{\infty} e^{-x} \, dx = \lim_{b \to \infty} \int_0^b e^{-x} \, dx = \lim_{b \to \infty} \left[-e^{-x}\right]_0^b$$

$$= \lim_{b \to \infty} (-e^{-b} + e^0) = 0 + 1 = 1$$

Das Integral konvergiert mit Wert 1.

---

## Das p-Integral (Konvergenzkriterium)

Ein wichtiges Referenzintegral ist:

$$\int_1^{\infty} \frac{1}{x^p} \, dx$$

### Konvergenzverhalten

| Exponent $p$ | Verhalten | Wert (falls konvergent) |
|--------------|-----------|-------------------------|
| $p > 1$ | konvergent | $\frac{1}{p-1}$ |
| $p = 1$ | divergent | – |
| $p < 1$ | divergent | – |

**Merkregel:** Das Integral $\int_1^{\infty} \frac{1}{x^p} \, dx$ konvergiert genau dann, wenn $p > 1$.

### Herleitung für $p \neq 1$

$$\int_1^{\infty} x^{-p} \, dx = \lim_{b \to \infty} \left[\frac{x^{-p+1}}{-p+1}\right]_1^b = \lim_{b \to \infty} \frac{1}{1-p}\left(b^{1-p} - 1\right)$$

- Für $p > 1$: $1-p < 0$, also $b^{1-p} \to 0$ für $b \to \infty$ → konvergent
- Für $p < 1$: $1-p > 0$, also $b^{1-p} \to \infty$ für $b \to \infty$ → divergent

---

## Uneigentliche Integrale 2. Art (unbeschränkter Integrand)

### Definition

Hat $f$ bei $x = a$ eine Polstelle (Definitionslücke), aber ist auf $(a, b]$ stetig, so definiert man:

$$\int_a^b f(x) \, dx = \lim_{\epsilon \to 0^+} \int_{a+\epsilon}^b f(x) \, dx$$

### Beispiel: Polstelle bei $x = 0$

Berechne $\int_0^1 \frac{1}{\sqrt{x}} \, dx$

**Lösung:**

Der Integrand $\frac{1}{\sqrt{x}}$ hat bei $x = 0$ eine Polstelle.

$$\int_0^1 \frac{1}{\sqrt{x}} \, dx = \lim_{\epsilon \to 0^+} \int_{\epsilon}^1 x^{-1/2} \, dx = \lim_{\epsilon \to 0^+} \left[2\sqrt{x}\right]_{\epsilon}^1$$

$$= \lim_{\epsilon \to 0^+} (2 - 2\sqrt{\epsilon}) = 2 - 0 = 2$$

Das Integral **konvergiert** mit Wert 2.

### Beispiel: Divergentes Integral 2. Art

Berechne $\int_0^1 \frac{1}{x} \, dx$

**Lösung:**

$$\int_0^1 \frac{1}{x} \, dx = \lim_{\epsilon \to 0^+} \int_{\epsilon}^1 \frac{1}{x} \, dx = \lim_{\epsilon \to 0^+} [\ln x]_{\epsilon}^1$$

$$= \lim_{\epsilon \to 0^+} (0 - \ln \epsilon) = \lim_{\epsilon \to 0^+} (-\ln \epsilon) = \infty$$

Das Integral **divergiert**.

---

## Konvergenzkriterien

### Vergleichskriterium

Wenn $0 \leq f(x) \leq g(x)$ für alle $x \geq a$:

- Konvergiert $\int_a^{\infty} g(x) \, dx$, so konvergiert auch $\int_a^{\infty} f(x) \, dx$ (Majorantenkriterium)
- Divergiert $\int_a^{\infty} f(x) \, dx$, so divergiert auch $\int_a^{\infty} g(x) \, dx$ (Minorantenkriterium)

### Praktische Faustregel

Für $x \to \infty$:
- Funktionen, die **schneller als** $\frac{1}{x}$ gegen 0 gehen → meist konvergent
- Funktionen, die **langsamer oder gleich schnell wie** $\frac{1}{x}$ gegen 0 gehen → meist divergent

---

## Zusammenfassung

| Typ | Bedingung | Beispiel |
|-----|-----------|----------|
| Typ I | Unbeschränktes Intervall | $\int_1^{\infty} e^{-x} \, dx$ |
| Typ II | Polstelle im/am Intervall | $\int_0^1 \frac{1}{\sqrt{x}} \, dx$ |

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Grenzwerte-von-Funktionen|Grenzwerte von Funktionen]] – Grundlage der Definition
- → [[Bestimmte-Integrale|Bestimmte Integrale]] – Reguläre Integrale als Basis
- → [[Konvergenz|Konvergenz]] – Konvergenzbegriff bei Folgen und Reihen
- → [[Exponentialfunktionen|Exponentialfunktionen]] – Schneller Abfall sichert Konvergenz
- → [[Anwendungen-in-der-Physik|Anwendungen in der Physik]] – Arbeit über unendliche Distanz

> [!warning] **Prüfungsrelevant**
> - Bei uneigentlichen Integralen **immer** den Grenzwert explizit aufschreiben!
> - Das p-Integral: $\int_1^{\infty} \frac{1}{x^p} \, dx$ konvergiert für $p > 1$
> - Bei Polstellen im Integrationsintervall liegt ein uneigentliches Integral 2. Art vor
> - Konvergenz prüfen, bevor man einen "Wert" angibt!

> [!question] **Typische Prüfungsfragen**
> - Untersuche das Integral $\int_1^{\infty} \frac{1}{x^3} \, dx$ auf Konvergenz und berechne ggf. seinen Wert.
> - Erkläre, warum $\int_0^{\infty} e^{-x^2} \, dx$ konvergiert, ohne es zu berechnen.
> - Warum ist $\int_0^1 \ln x \, dx$ ein uneigentliches Integral? Berechne seinen Wert.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1, Springer Vieweg, 2018
- Bronstein, I. N. et al.: Taschenbuch der Mathematik, Europa-Lehrmittel, 2020
- ISB Bayern: Lehrplan Mathematik Gymnasium, Analysis

> [!tip] **Weiterführende Links**
> - [[Grenzwerte-von-Funktionen|Grenzwerte von Funktionen]] – Fundament der uneigentlichen Integrale
> - [[Unendliche-geometrische-Reihen|Unendliche geometrische Reihen]] – Verwandtes Konvergenzkonzept
