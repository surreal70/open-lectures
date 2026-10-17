---
author: Andreas Hümmer
title: Kumulative Wahrscheinlichkeiten
tags:
  - content
  - mathe
  - stochastik
  - verteilungsfunktion
  - kumulativ
  - binomialverteilung
created: 2026-10-17
modified: 2026-10-17
---

# Kumulative Wahrscheinlichkeiten

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Kumulative Wahrscheinlichkeiten berechnen und interpretieren
> - Die Verteilungsfunktion $F(k) = P(X \leq k)$ anwenden
> - Beliebige Wahrscheinlichkeiten auf kumulative zurückführen
> - Tabellen der kumulativen Binomialverteilung effizient nutzen

---

## Überblick

Kumulative Wahrscheinlichkeiten summieren Einzelwahrscheinlichkeiten auf und beantworten die Frage: „Mit welcher Wahrscheinlichkeit ist das Ergebnis höchstens $k$?" Die Verteilungsfunktion $F(k)$ ist das zentrale Werkzeug für effiziente Berechnungen, insbesondere bei der [[Binomialverteilung]].

## Definition der Verteilungsfunktion

Die **kumulative Verteilungsfunktion** (Verteilungsfunktion) einer diskreten Zufallsvariablen $X$ ist:

$$F(k) = P(X \leq k) = \sum_{i=0}^{k} P(X = i)$$

### Beispiel: Binomialverteilung

Für $X \sim B(5, 0{,}3)$:

| $k$ | $P(X = k)$ | $F(k) = P(X \leq k)$ |
|-----|------------|---------------------|
| 0 | $0{,}1681$ | $0{,}1681$ |
| 1 | $0{,}3602$ | $0{,}5283$ |
| 2 | $0{,}3087$ | $0{,}8370$ |
| 3 | $0{,}1323$ | $0{,}9693$ |
| 4 | $0{,}0284$ | $0{,}9977$ |
| 5 | $0{,}0024$ | $1{,}0000$ |

## Umrechnung verschiedener Wahrscheinlichkeiten

### Grundformeln

Alle Wahrscheinlichkeiten lassen sich durch $F(k)$ ausdrücken:

| Wahrscheinlichkeit | Berechnung mit $F$ |
|-------------------|-------------------|
| $P(X \leq k)$ | $F(k)$ |
| $P(X < k)$ | $F(k-1)$ |
| $P(X \geq k)$ | $1 - F(k-1)$ |
| $P(X > k)$ | $1 - F(k)$ |
| $P(X = k)$ | $F(k) - F(k-1)$ |
| $P(a \leq X \leq b)$ | $F(b) - F(a-1)$ |

### Beispiele mit $X \sim B(5, 0{,}3)$

**a) $P(X \geq 2)$**:

$$P(X \geq 2) = 1 - P(X \leq 1) = 1 - F(1) = 1 - 0{,}5283 = 0{,}4717$$

**b) $P(X > 3)$**:

$$P(X > 3) = 1 - P(X \leq 3) = 1 - F(3) = 1 - 0{,}9693 = 0{,}0307$$

**c) $P(1 \leq X \leq 3)$**:

$$P(1 \leq X \leq 3) = F(3) - F(0) = 0{,}9693 - 0{,}1681 = 0{,}8012$$

## Grafische Darstellung

Die Verteilungsfunktion ist eine **Treppenfunktion**:

```
F(k) für B(5, 0,3)
  |
1,0 +                          ●────
    |                    ●─────○
0,9 +                    │
    |              ●─────○
0,8 +              │
    |        ●─────○
0,5 +        │
    |  ●─────○
0,2 +  │
    +──○─────┼─────┼─────┼─────┼────
       0     1     2     3     4     5  k
```

### Ablesen aus dem Graphen

- **$P(X \leq k)$**: Höhe der Stufe bei $k$
- **$P(X = k)$**: Sprunghöhe bei $k$
- **$P(X > k)$**: Abstand von der Stufe zur Linie 1

## Arbeit mit Tabellen

### Aufbau von Binomialtabellen

Tabellen der kumulativen Binomialverteilung zeigen $F(k) = P(X \leq k)$ für verschiedene $n$ und $p$:

**Ausschnitt: $n = 10$**

| $k$ | $p=0{,}1$ | $p=0{,}2$ | $p=0{,}3$ | $p=0{,}5$ |
|-----|-----------|-----------|-----------|-----------|
| 0 | 0,3487 | 0,1074 | 0,0282 | 0,0010 |
| 1 | 0,7361 | 0,3758 | 0,1493 | 0,0107 |
| 2 | 0,9298 | 0,6778 | 0,3828 | 0,0547 |
| 3 | 0,9872 | 0,8791 | 0,6496 | 0,1719 |
| 4 | 0,9984 | 0,9672 | 0,8497 | 0,3770 |
| 5 | 0,9999 | 0,9936 | 0,9527 | 0,6230 |

### Nutzung der Tabelle

**Beispiel**: $X \sim B(10, 0{,}3)$

a) $P(X \leq 3)$: Ablesen → $0{,}6496$

b) $P(X = 3) = F(3) - F(2) = 0{,}6496 - 0{,}3828 = 0{,}2668$

c) $P(X \geq 4) = 1 - F(3) = 1 - 0{,}6496 = 0{,}3504$

## Komplementregel

Die wichtigste Regel für „mindestens"-Aufgaben:

$$P(X \geq k) = 1 - P(X \leq k-1) = 1 - F(k-1)$$

### Beispiel: Qualitätskontrolle

Bei 20 Produkten mit Ausschussrate 10% ($X \sim B(20, 0{,}1)$):

„Wahrscheinlichkeit für **mindestens 3** Ausschussstücke?"

$$P(X \geq 3) = 1 - P(X \leq 2) = 1 - F(2)$$

Mit Tabelle oder Rechner: $F(2) \approx 0{,}6769$

$$P(X \geq 3) = 1 - 0{,}6769 = 0{,}3231$$

## Bereichswahrscheinlichkeiten

$$P(a \leq X \leq b) = F(b) - F(a-1)$$

### Beispiel

Für $X \sim B(10, 0{,}3)$: $P(2 \leq X \leq 5)$

$$P(2 \leq X \leq 5) = F(5) - F(1) = 0{,}9527 - 0{,}1493 = 0{,}8034$$

## Typische Fehlerquellen

> [!warning] **Achtung bei Ungleichungen**
> - $P(X < k)$ ist **nicht** $F(k)$, sondern $F(k-1)$
> - $P(X \geq k)$ ist **nicht** $1 - F(k)$, sondern $1 - F(k-1)$
> - Bei „weniger als" oder „mehr als" muss der Grenzwert **nicht** eingeschlossen sein

### Merkhilfe

| Formulierung | Mathematisch | Berechnung |
|--------------|--------------|------------|
| höchstens $k$ | $X \leq k$ | $F(k)$ |
| weniger als $k$ | $X < k$ | $F(k-1)$ |
| mindestens $k$ | $X \geq k$ | $1 - F(k-1)$ |
| mehr als $k$ | $X > k$ | $1 - F(k)$ |

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Wahrscheinlichkeitsverteilungen]] — Verteilungsfunktion allgemein
- → [[Binomialverteilung]] — Wichtigste Anwendung
- → [[Diskrete-Zufallsvariablen]] — Summation über Einzelwahrscheinlichkeiten
- → [[Normalverteilung]] — Verteilungsfunktion Φ bei stetigen Verteilungen
- → [[Standardnormalverteilung]] — Tabelle für Φ(z)

> [!warning] **Prüfungsrelevant**
> - Umrechnung: $P(X \geq k) = 1 - F(k-1)$
> - Bereichswahrscheinlichkeiten: $P(a \leq X \leq b) = F(b) - F(a-1)$
> - Ablesen aus kumulativen Tabellen
> - Unterscheidung von $\leq$, $<$, $\geq$, $>$

> [!question] **Typische Prüfungsfragen**
> - Berechne die Wahrscheinlichkeit, dass mindestens $k$ Treffer erzielt werden.
> - Lies aus der Tabelle ab: $P(3 \leq X \leq 7)$ für $X \sim B(n, p)$.
> - Bestimme mithilfe der Verteilungsfunktion, ob das Ereignis ungewöhnlich ist.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3. Springer Vieweg, 2016.
- Bosch, K.: Elementare Einführung in die Wahrscheinlichkeitsrechnung. Springer Spektrum, 2011.
- ISB Bayern: Lehrplan Mathematik, Gymnasium, Oberstufe.

> [!tip] **Weiterführende Links**
> - [[Normalverteilung]] — Stetige Verteilungsfunktion
> - [[Standardnormalverteilung]] — Tabelle für die Standardnormalverteilung
