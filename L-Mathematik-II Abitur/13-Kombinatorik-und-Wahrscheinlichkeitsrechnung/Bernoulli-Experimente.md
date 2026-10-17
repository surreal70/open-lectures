---
author: Andreas Hümmer
title: Bernoulli-Experimente
tags:
  - content
  - mathe
  - stochastik
  - bernoulli
  - zufallsexperiment
created: 2025-07-01
modified: 2025-07-01
---

# Bernoulli-Experimente

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Ein Bernoulli-Experiment definieren und erkennen können
> - Die charakteristischen Eigenschaften von Bernoulli-Experimenten kennen
> - Beispiele aus dem Alltag als Bernoulli-Experimente modellieren können
> - Den Zusammenhang zu Bernoulli-Ketten verstehen

---

## Überblick

Ein Bernoulli-Experiment (benannt nach dem Schweizer Mathematiker Jacob Bernoulli, 1654–1705) ist ein Zufallsexperiment mit genau zwei möglichen Ausgängen: Erfolg oder Misserfolg. Diese einfache Struktur macht Bernoulli-Experimente zum Grundbaustein vieler stochastischer Modelle und ist Ausgangspunkt für die wichtige Binomialverteilung.

## Definition

Ein **Bernoulli-Experiment** ist ein Zufallsexperiment mit genau zwei möglichen Ausgängen:

- **Erfolg** (E) mit Wahrscheinlichkeit $p$
- **Misserfolg** (M) mit Wahrscheinlichkeit $q = 1 - p$

### Eigenschaften

1. Genau zwei mögliche Ergebnisse
2. Die Wahrscheinlichkeiten $p$ und $q$ sind konstant und bekannt
3. $p + q = 1$

### Notation

| Symbol | Bedeutung |
|--------|-----------|
| $p$ | Erfolgswahrscheinlichkeit |
| $q = 1-p$ | Misserfolgswahrscheinlichkeit |
| $n$ | Anzahl der Wiederholungen (bei Ketten) |
| $k$ | Anzahl der Erfolge |

## Beispiele für Bernoulli-Experimente

### Klassische Beispiele

| Experiment | Erfolg | Misserfolg | $p$ |
|------------|--------|------------|-----|
| Münzwurf | Kopf | Zahl | 0,5 |
| Würfelwurf (6 gewinnt) | 6 | 1–5 | $\frac{1}{6}$ |
| Freiwurf (Basketball) | Treffer | Fehlwurf | variabel |
| Multiple-Choice (4 Optionen) | richtig | falsch | 0,25 |
| Qualitätskontrolle | defekt | in Ordnung | variabel |

### Beispiel 1: Münzwurf

Beim Werfen einer fairen Münze:
- Erfolg: Kopf, $p = 0{,}5$
- Misserfolg: Zahl, $q = 0{,}5$

### Beispiel 2: Würfelwurf

Beim Würfeln mit dem Ziel „eine 6 werfen":
- Erfolg: 6, $p = \frac{1}{6}$
- Misserfolg: 1, 2, 3, 4, 5, $q = \frac{5}{6}$

### Beispiel 3: Medizinische Behandlung

Eine Behandlung wirkt bei 80% der Patienten:
- Erfolg: Heilung, $p = 0{,}8$
- Misserfolg: keine Heilung, $q = 0{,}2$

## Nicht-Bernoulli-Experimente

Folgende Experimente sind **keine** Bernoulli-Experimente:

- Würfelwurf mit Interesse an der genauen Augenzahl (6 Ausgänge)
- Ziehen aus einer Urne ohne Zurücklegen (Wahrscheinlichkeiten ändern sich)
- Kartenspiel mit verschiedenen Gewinnklassen (mehr als 2 Ausgänge)

### Umformung möglich

Manchmal kann ein komplexeres Experiment zu einem Bernoulli-Experiment reduziert werden:

**Beispiel:** Würfelwurf
- Als Nicht-Bernoulli: Ergebnisse 1, 2, 3, 4, 5, 6
- Als Bernoulli: „gerade" vs. „ungerade"

## Das Bernoulli-Schema

### Einzelnes Bernoulli-Experiment

Das einfachste probabilistische Modell:

```
         ┌─── E    mit P(E) = p
Start ───┤
         └─── M    mit P(M) = q = 1-p
```

### Wahrscheinlichkeitsverteilung

Für eine Bernoulli-Zufallsvariable $X$ mit $X = 1$ bei Erfolg und $X = 0$ bei Misserfolg:

$$P(X = k) = \begin{cases} p & \text{falls } k = 1 \\ 1-p & \text{falls } k = 0 \end{cases}$$

Oder kompakt:
$$P(X = k) = p^k \cdot (1-p)^{1-k} \quad \text{für } k \in \{0, 1\}$$

### Kenngrößen

**Erwartungswert:**
$$E(X) = 0 \cdot (1-p) + 1 \cdot p = p$$

**Varianz:**
$$\text{Var}(X) = E(X^2) - [E(X)]^2 = p - p^2 = p(1-p) = pq$$

**Standardabweichung:**
$$\sigma = \sqrt{p(1-p)}$$

## Vom Bernoulli-Experiment zur Bernoulli-Kette

### Wiederholung von Bernoulli-Experimenten

Wenn ein Bernoulli-Experiment $n$-mal unabhängig wiederholt wird, entsteht eine **Bernoulli-Kette** der Länge $n$.

### Beispiel: Dreimaliger Münzwurf

```
                            ┌─ E (EEE)  p³
              ┌─ E ─────────┤
              │   p         └─ M (EEM)  p²q
    ┌─ E ─────┤
    │   p     │             ┌─ E (EME)  p²q
    │         └─ M ─────────┤
    │             q         └─ M (EMM)  pq²
────┤
    │                       ┌─ E (MEE)  p²q
    │         ┌─ E ─────────┤
    │         │   p         └─ M (MEM)  pq²
    └─ M ─────┤
        q     │             ┌─ E (MME)  pq²
              └─ M ─────────┤
                  q         └─ M (MMM)  q³
```

### Wahrscheinlichkeit für genau $k$ Erfolge

Bei $n$ Wiederholungen mit Erfolgswahrscheinlichkeit $p$:

$$P(X = k) = \binom{n}{k} \cdot p^k \cdot (1-p)^{n-k}$$

Diese Formel definiert die **Binomialverteilung**.

## Modellierung realer Situationen

### Schritte zur Modellierung

1. **Identifiziere** das Zufallsexperiment
2. **Definiere** Erfolg und Misserfolg
3. **Bestimme** die Erfolgswahrscheinlichkeit $p$
4. **Prüfe**, ob die Voraussetzungen erfüllt sind:
   - Genau zwei Ausgänge?
   - Konstante Wahrscheinlichkeit?
   - Unabhängige Wiederholungen?

### Beispiel: Qualitätskontrolle

Eine Maschine produziert Schrauben mit einer Ausschussquote von 3%.

**Modellierung:**
- Bernoulli-Experiment: Prüfung einer Schraube
- Erfolg: Schraube ist defekt (interessierendes Ereignis)
- $p = 0{,}03$, $q = 0{,}97$

**Frage:** Bei 100 Schrauben, wie viele sind voraussichtlich defekt?
$$E(X) = n \cdot p = 100 \cdot 0{,}03 = 3$$

### Beispiel: Geburtstage

Die Wahrscheinlichkeit, an einem bestimmten Wochentag geboren zu sein (bei Gleichverteilung):

**Modellierung:**
- Erfolg: Geburt am Montag
- $p = \frac{1}{7}$

## Voraussetzungen und Grenzen

### Wann ist das Bernoulli-Modell anwendbar?

✅ **Geeignet:**
- Münzwurf, Würfelwurf
- Wiederholte unabhängige Ziehungen mit Zurücklegen
- Produktionsprozesse mit konstanter Fehlerrate

❌ **Nicht geeignet:**
- Ziehen ohne Zurücklegen (bei kleiner Grundgesamtheit)
- Sich ändernde Wahrscheinlichkeiten (z.B. Ermüdung)
- Abhängige Experimente

### Approximation bei großen Grundgesamtheiten

Bei sehr großen Grundgesamtheiten kann auch Ziehen ohne Zurücklegen näherungsweise als Bernoulli-Experiment modelliert werden, da sich die Wahrscheinlichkeiten kaum ändern.

**Faustregel:** Wenn die Stichprobe weniger als 5% der Grundgesamtheit ausmacht.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Bernoulli-Ketten]] — Wiederholung von Bernoulli-Experimenten
- → [[Binomialkoeffizienten]] — Kombinatorik der Bernoulli-Ketten
- → [[Unabhaengigkeit-von-Ereignissen]] — Voraussetzung für Wiederholung
- → [[Baumdiagramme]] — Visualisierung

> [!warning] **Prüfungsrelevant**
> - Definition: genau zwei Ausgänge mit $p$ und $q = 1-p$
> - Erkennen, ob ein Experiment ein Bernoulli-Experiment ist
> - Voraussetzungen für die Anwendbarkeit prüfen
> - Erwartungswert und Varianz einer Bernoulli-Verteilung

> [!question] **Typische Prüfungsfragen**
> - Erkläre, was ein Bernoulli-Experiment ist, und gib drei Beispiele.
> - Warum ist das Ziehen ohne Zurücklegen kein Bernoulli-Experiment?
> - Bei einem Glücksrad mit 8 gleichen Sektoren gewinnt man bei Sektor 1. Bestimme $p$ und $q$.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3, Springer Vieweg, 2016
- Bronstein, I.N. et al.: Taschenbuch der Mathematik, Verlag Europa-Lehrmittel, 2020
- ISB Bayern: Lehrplan Mathematik Gymnasium, Stochastik

> [!tip] **Weiterführende Links**
> - [[Bernoulli-Ketten]] — Die Binomialverteilung
> - [[14-Wahrscheinlichkeitsverteilungen/Binomialverteilung|Binomialverteilung]] — Ausführliche Behandlung
