---
author: Andreas Hümmer
title: Geometrische Folgen
tags:
  - content
  - mathe
  - folgen
  - geometrische-folge
  - exponentielles-wachstum
  - analysis
created: 2025-06-17
modified: 2025-06-17
---

# Geometrische Folgen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Definition einer geometrischen Folge verstehen und anwenden können
> - Das explizite Bildungsgesetz und die rekursive Darstellung beherrschen
> - Die Summenformel für geometrische Reihen herleiten und anwenden können
> - Geometrische Folgen von arithmetischen Folgen unterscheiden können
> - Anwendungen in Zinseszins- und Wachstumsproblemen lösen können

---

## Überblick

Eine **geometrische Folge** ist eine Zahlenfolge, bei der der Quotient aufeinanderfolgender Glieder konstant ist. Diese Konstante heißt **Quotient** $q$. Geometrische Folgen modellieren exponentielles Wachstum oder exponentiellen Zerfall und sind das diskrete Pendant zu Exponentialfunktionen.

Geometrische Folgen finden sich in zahlreichen Anwendungen: Zinseszinsrechnung, radioaktiver Zerfall, Populationsdynamik, Kettenreaktionen oder die geometrische Perspektive in der Kunst.

## Definition und Eigenschaften

### Definition

Eine Folge $(a_n)$ heißt **geometrische Folge**, wenn für alle $n \in \mathbb{N}$ gilt:

$$\frac{a_{n+1}}{a_n} = q \quad \text{(konstanter Quotient, } a_n \neq 0 \text{)}$$

Äquivalent: Der Quotient $q = \frac{a_{n+1}}{a_n}$ ist unabhängig von $n$.

### Charakteristische Größen

| Größe | Symbol | Bedeutung |
|-------|--------|-----------|
| Anfangsglied | $a_1$ | Erster Wert der Folge |
| Quotient | $q$ | Konstanter Wachstumsfaktor |
| $n$-tes Glied | $a_n$ | Wert an Position $n$ |

### Darstellungsformen

**Explizite Darstellung:**
$$a_n = a_1 \cdot q^{n-1}$$

**Rekursive Darstellung:**
$$a_{n+1} = a_n \cdot q \quad \text{mit Startwert } a_1$$

**Beispiel:** Geometrische Folge mit $a_1 = 2$ und $q = 3$

$$a_n = 2 \cdot 3^{n-1}$$

Die Folge lautet: $(2, 6, 18, 54, 162, \ldots)$

## Verhalten der Folge

Das Verhalten einer geometrischen Folge hängt vom Quotienten $q$ ab (bei $a_1 > 0$):

| Quotient | Verhalten | Beispiel |
|----------|-----------|----------|
| $q > 1$ | Unbeschränktes Wachstum | $(2, 4, 8, 16, \ldots)$ |
| $q = 1$ | Konstante Folge | $(3, 3, 3, 3, \ldots)$ |
| $0 < q < 1$ | Konvergenz gegen 0 | $(1, 0.5, 0.25, \ldots)$ |
| $q = 0$ | Nullfolge ab $n = 2$ | $(5, 0, 0, 0, \ldots)$ |
| $-1 < q < 0$ | Alternierende Konvergenz gegen 0 | $(1, -0.5, 0.25, \ldots)$ |
| $q = -1$ | Alternierende, beschränkte Folge | $(1, -1, 1, -1, \ldots)$ |
| $q < -1$ | Alternierende, unbeschränkte Folge | $(1, -2, 4, -8, \ldots)$ |

## Die geometrische Summenformel

### Herleitung

Die Summe der ersten $n$ Glieder einer geometrischen Folge heißt **geometrische Reihe**:

$$S_n = a_1 + a_1 q + a_1 q^2 + \ldots + a_1 q^{n-1} = \sum_{k=0}^{n-1} a_1 q^k$$

**Trick:** Multipliziere mit $q$ und subtrahiere:

$$\begin{align}
S_n &= a_1 + a_1 q + a_1 q^2 + \ldots + a_1 q^{n-1} \\
q \cdot S_n &= \phantom{a_1 +} a_1 q + a_1 q^2 + \ldots + a_1 q^{n-1} + a_1 q^n
\end{align}$$

Subtraktion ergibt:
$$S_n - q \cdot S_n = a_1 - a_1 q^n$$
$$S_n (1 - q) = a_1 (1 - q^n)$$

### Summenformel (für $q \neq 1$)

$$\boxed{S_n = a_1 \cdot \frac{1 - q^n}{1 - q} = a_1 \cdot \frac{q^n - 1}{q - 1}}$$

**Sonderfall $q = 1$:** $S_n = n \cdot a_1$

### Beispiel: Potenzreihe

Berechne $S_6 = 1 + 2 + 4 + 8 + 16 + 32$

Mit $a_1 = 1$, $q = 2$, $n = 6$:

$$S_6 = 1 \cdot \frac{2^6 - 1}{2 - 1} = \frac{64 - 1}{1} = 63$$

## Mittelwert-Eigenschaft

### Geometrisches Mittel

In einer geometrischen Folge ist jedes Glied (außer dem ersten und letzten) das **geometrische Mittel** seiner beiden Nachbarn:

$$a_n = \sqrt{a_{n-1} \cdot a_{n+1}}$$

**Beweis:** Mit $a_{n-1} = \frac{a_n}{q}$ und $a_{n+1} = a_n \cdot q$:

$$\sqrt{a_{n-1} \cdot a_{n+1}} = \sqrt{\frac{a_n}{q} \cdot a_n \cdot q} = \sqrt{a_n^2} = |a_n| = a_n \quad \text{(für } a_n > 0\text{)}$$

## Anwendungsbeispiele

### Beispiel 1: Zinseszins

Ein Kapital von 5.000 € wird zu einem jährlichen Zinssatz von 3% angelegt.

**Kapitalentwicklung:**
- $a_1 = 5000$ (Anfangskapital)
- $q = 1,03$ (Wachstumsfaktor = 1 + Zinssatz)
- $a_n = 5000 \cdot 1,03^{n-1}$

**Nach 10 Jahren:** $a_{10} = 5000 \cdot 1,03^9 \approx 6523,87$ €

### Beispiel 2: Radioaktiver Zerfall

Eine radioaktive Substanz hat eine Halbwertszeit von 5 Jahren. Anfangs sind 200 g vorhanden.

**Masseentwicklung:**
- $a_1 = 200$
- Nach 5 Jahren: $a_2 = 100$ (Halbierung)
- $q = 0,5$

**Nach $n \cdot 5$ Jahren:** $a_n = 200 \cdot 0,5^{n-1}$

**Nach 20 Jahren ($n = 5$):** $a_5 = 200 \cdot 0,5^4 = 12,5$ g

### Beispiel 3: Wöchentliche Verdopplung

Eine Bakterienkultur verdoppelt sich wöchentlich. Anfangs sind 100 Bakterien vorhanden. Wie viele sind nach 8 Wochen vorhanden, und wie viele Bakterien wurden insgesamt "produziert"?

**Anzahl nach 8 Wochen:**
$$a_9 = 100 \cdot 2^8 = 25.600$$

**Gesamtsumme (alle Generationen):**
$$S_9 = 100 \cdot \frac{2^9 - 1}{2 - 1} = 100 \cdot 511 = 51.100$$

## Vergleich: Arithmetisch vs. Geometrisch

| Eigenschaft | Arithmetische Folge | Geometrische Folge |
|-------------|---------------------|---------------------|
| Bildungsgesetz | $a_n = a_1 + (n-1) \cdot d$ | $a_n = a_1 \cdot q^{n-1}$ |
| Rekursion | $a_{n+1} = a_n + d$ | $a_{n+1} = a_n \cdot q$ |
| Kennzahl | Differenz $d$ | Quotient $q$ |
| Wachstum | linear | exponentiell |
| Graph | Gerade | Exponentialkurve |
| Mittelwert | arithmetisches Mittel | geometrisches Mittel |

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Zahlenfolgen]] – Allgemeiner Folgenbegriff
- → [[Arithmetische-Folgen]] – Vergleich: konstante Differenz statt konstantem Quotienten
- → [[Unendliche-geometrische-Reihen]] – Konvergenz für $|q| < 1$
- → [[Exponentialfunktionen]] – Kontinuierliches Pendant
- → [[Wachstumsprozesse]] – Anwendungen in der Modellierung

> [!warning] **Prüfungsrelevant**
> - Explizite Formel $a_n = a_1 \cdot q^{n-1}$ muss sicher beherrscht werden
> - Summenformel $S_n = a_1 \cdot \frac{q^n - 1}{q - 1}$ ist Standardwissen
> - Zinseszinsaufgaben sind ein Klassiker im Abitur
> - Unterscheidung zu arithmetischen Folgen wird häufig abgefragt
> - Prozentuale Änderungen bedeuten $q = 1 + p$ (Zunahme) bzw. $q = 1 - p$ (Abnahme)

> [!question] **Typische Prüfungsfragen**
> - Ein Kapital verdreifacht sich in 10 Jahren. Bestimme den jährlichen Zinssatz.
> - Eine geometrische Folge hat $a_2 = 12$ und $a_5 = 324$. Bestimme $a_1$ und $q$.
> - Nach wie vielen Halbwertszeiten ist von einer radioaktiven Substanz weniger als 1% der Ausgangsmenge übrig?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I. N. et al.: Taschenbuch der Mathematik. Europa-Lehrmittel, 2020.
- Tietze, J.: Einführung in die angewandte Wirtschaftsmathematik. Springer Spektrum, 2019.

> [!tip] **Weiterführende Links**
> - [[Konvergenz]] – Wann konvergiert eine geometrische Folge?
> - [[Logarithmusfunktionen]] – Umkehrung der Exponentialfunktion für Lösungen nach $n$
