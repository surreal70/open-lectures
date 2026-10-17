---
author: Andreas Hümmer
title: Zufallsvariablen
tags:
  - content
  - mathe
  - stochastik
  - zufallsvariable
  - grundlagen
created: 2026-10-17
modified: 2026-10-17
---

# Zufallsvariablen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Begriff der Zufallsvariablen als Abbildung vom Ergebnisraum in die reellen Zahlen verstehen
> - Zwischen diskreten und stetigen Zufallsvariablen unterscheiden können
> - Einfache Zufallsvariablen selbst definieren und deren Wertebereich angeben können
> - Ereignisse mithilfe von Zufallsvariablen formal beschreiben

---

## Überblick

Eine Zufallsvariable ist ein zentrales Konzept der Wahrscheinlichkeitstheorie. Sie ordnet jedem Ergebnis eines Zufallsexperiments eine reelle Zahl zu und ermöglicht so die mathematische Behandlung von Zufallsphänomenen. Der Name „Zufallsvariable" ist dabei historisch bedingt — korrekter wäre eigentlich „Zufallsfunktion".

## Definition der Zufallsvariablen

### Formale Definition

Eine **Zufallsvariable** $X$ ist eine Funktion, die jedem Elementarereignis $\omega$ des Ergebnisraums $\Omega$ eine reelle Zahl zuordnet:

$$X: \Omega \to \mathbb{R}$$

Die Menge aller möglichen Werte, die $X$ annehmen kann, heißt **Wertebereich** oder **Bildmenge** von $X$.

### Beispiel: Würfelwurf

Beim zweimaligen Würfelwurf mit dem Ergebnisraum $\Omega = \{(1,1), (1,2), \ldots, (6,6)\}$ könnte man verschiedene Zufallsvariablen definieren:

- **Augensumme**: $X(\omega) = \omega_1 + \omega_2$ mit Wertebereich $\{2, 3, \ldots, 12\}$
- **Maximum**: $Y(\omega) = \max(\omega_1, \omega_2)$ mit Wertebereich $\{1, 2, \ldots, 6\}$
- **Produkt**: $Z(\omega) = \omega_1 \cdot \omega_2$ mit Wertebereich $\{1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 30, 36\}$

## Arten von Zufallsvariablen

### Diskrete Zufallsvariablen

Eine Zufallsvariable heißt **diskret**, wenn ihr Wertebereich endlich oder abzählbar unendlich ist.

Typische Beispiele:
- Anzahl der Sechsen bei 10 Würfelwürfen
- Anzahl der Kunden in einer Warteschlange
- Anzahl der Treffer bei einem Multiple-Choice-Test

### Stetige Zufallsvariablen

Eine Zufallsvariable heißt **stetig**, wenn sie jeden Wert in einem Intervall $[a, b]$ oder in ganz $\mathbb{R}$ annehmen kann.

Typische Beispiele:
- Körpergröße einer zufällig ausgewählten Person
- Lebensdauer eines elektronischen Bauteils
- Messabweichung bei einem physikalischen Experiment

## Notation und Schreibweisen

Für Zufallsvariablen verwendet man folgende Konventionen:

| Schreibweise | Bedeutung |
|--------------|-----------|
| $X$ | Zufallsvariable (Großbuchstabe) |
| $x$ | konkreter Wert (Kleinbuchstabe) |
| $P(X = x)$ | Wahrscheinlichkeit, dass $X$ den Wert $x$ annimmt |
| $P(X \leq x)$ | Wahrscheinlichkeit, dass $X$ höchstens $x$ ist |
| $P(a \leq X \leq b)$ | Wahrscheinlichkeit, dass $X$ zwischen $a$ und $b$ liegt |

### Ereignisse als Mengen

Ein Ereignis wie „$X = 5$" entspricht formal der Menge aller Elementarereignisse, für die $X$ den Wert 5 annimmt:

$$\{X = 5\} = \{\omega \in \Omega : X(\omega) = 5\}$$

## Bestimmung von Wahrscheinlichkeiten

### Beispiel: Münzwurf

Bei dreimaligem Münzwurf sei $X$ die Anzahl der „Kopf"-Ergebnisse.

Der Ergebnisraum ist $\Omega = \{KKK, KKZ, KZK, ZKK, KZZ, ZKZ, ZZK, ZZZ\}$, wobei jedes Elementarereignis die Wahrscheinlichkeit $\frac{1}{8}$ hat.

| $x$ | Elementarereignisse mit $X = x$ | $P(X = x)$ |
|-----|--------------------------------|------------|
| 0 | $\{ZZZ\}$ | $\frac{1}{8}$ |
| 1 | $\{KZZ, ZKZ, ZZK\}$ | $\frac{3}{8}$ |
| 2 | $\{KKZ, KZK, ZKK\}$ | $\frac{3}{8}$ |
| 3 | $\{KKK\}$ | $\frac{1}{8}$ |

Die Summe der Wahrscheinlichkeiten ergibt stets 1:

$$\sum_{x=0}^{3} P(X = x) = \frac{1}{8} + \frac{3}{8} + \frac{3}{8} + \frac{1}{8} = 1$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Diskrete-Zufallsvariablen]] — Vertiefung zu diskreten Zufallsvariablen
- → [[Wahrscheinlichkeitsverteilungen]] — Die Verteilung einer Zufallsvariablen
- → [[Erwartungswert]] — Der „mittlere" Wert einer Zufallsvariablen
- → [[Bernoulli-Experimente]] — Grundlage vieler diskreter Zufallsvariablen
- → [[Wiederholung-des-Funktionsbegriffs]] — Zufallsvariablen als spezielle Funktionen

> [!warning] **Prüfungsrelevant**
> - Definition der Zufallsvariablen als Funktion $X: \Omega \to \mathbb{R}$
> - Unterscheidung zwischen diskreten und stetigen Zufallsvariablen
> - Berechnung von Wahrscheinlichkeiten $P(X = x)$ durch Abzählen
> - Interpretation von Ungleichungen wie $P(X \leq 3)$ oder $P(X > 2)$

> [!question] **Typische Prüfungsfragen**
> - Definiere eine geeignete Zufallsvariable für das beschriebene Zufallsexperiment und gib ihren Wertebereich an.
> - Berechne $P(X = k)$ für alle möglichen Werte $k$ der Zufallsvariablen $X$.
> - Bestimme die Wahrscheinlichkeit $P(2 \leq X \leq 5)$ für die gegebene Zufallsvariable.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3: Vektoranalysis, Wahrscheinlichkeitsrechnung, Mathematische Statistik, Fehler- und Ausgleichsrechnung. Springer Vieweg, 2016.
- Tietze, J.: Einführung in die angewandte Wirtschaftsmathematik. Springer, 2013.
- ISB Bayern: Lehrplan Mathematik, Gymnasium, Oberstufe.

> [!tip] **Weiterführende Links**
> - [[Diskrete-Zufallsvariablen]] — Nächstes Kapitel: Diskrete Zufallsvariablen im Detail
> - [[Normalverteilung]] — Wichtigste stetige Verteilung
