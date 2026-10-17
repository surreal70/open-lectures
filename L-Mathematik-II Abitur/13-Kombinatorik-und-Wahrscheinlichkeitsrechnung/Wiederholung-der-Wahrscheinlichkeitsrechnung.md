---
author: Andreas Hümmer
title: Wiederholung der Wahrscheinlichkeitsrechnung
tags:
  - content
  - mathe
  - stochastik
  - wahrscheinlichkeit
  - grundlagen
created: 2025-07-01
modified: 2025-07-01
---

# Wiederholung der Wahrscheinlichkeitsrechnung

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Grundbegriffe der Wahrscheinlichkeitsrechnung sicher beherrschen
> - Wahrscheinlichkeiten mit dem Laplace-Modell berechnen können
> - Rechenregeln für Wahrscheinlichkeiten anwenden können
> - Den Unterschied zwischen theoretischer und empirischer Wahrscheinlichkeit verstehen

---

## Überblick

Die Wahrscheinlichkeitsrechnung (Stochastik) beschäftigt sich mit der mathematischen Beschreibung und Analyse von Zufallsexperimenten. Sie bildet die Grundlage für die weiterführenden Themen dieses Moduls und ist ein zentraler Bestandteil der Abiturprüfung. In diesem Kapitel wiederholen wir die fundamentalen Konzepte, die du aus der Mittelstufe bereits kennst.

## Grundbegriffe der Wahrscheinlichkeitsrechnung

### Zufallsexperiment

Ein **Zufallsexperiment** ist ein Vorgang, der:
- unter gleichen Bedingungen beliebig oft wiederholbar ist
- mehrere mögliche Ergebnisse hat
- dessen Ausgang nicht vorhersagbar ist

**Beispiele:**
- Werfen eines Würfels
- Werfen einer Münze
- Ziehen einer Kugel aus einer Urne
- Roulettespiel

### Ergebnisraum und Ereignisse

Der **Ergebnisraum** $\Omega$ (Omega) ist die Menge aller möglichen Ergebnisse eines Zufallsexperiments.

**Beispiel Würfelwurf:**
$$\Omega = \{1, 2, 3, 4, 5, 6\}$$

Ein **Ereignis** $A$ ist eine Teilmenge des Ergebnisraums: $A \subseteq \Omega$

| Bezeichnung | Symbol | Bedeutung |
|-------------|--------|-----------|
| Elementarereignis | $\{\omega\}$ | Menge mit genau einem Element |
| Sicheres Ereignis | $\Omega$ | Tritt immer ein |
| Unmögliches Ereignis | $\emptyset$ | Tritt nie ein |
| Gegenereignis | $\bar{A}$ oder $A^c$ | Alle Ergebnisse, die nicht in $A$ liegen |

### Beispiel: Würfelwurf

Beim Werfen eines fairen Würfels definieren wir:
- $A = \{2, 4, 6\}$ — „Es fällt eine gerade Zahl"
- $B = \{1, 2, 3\}$ — „Es fällt höchstens eine 3"
- $\bar{A} = \{1, 3, 5\}$ — „Es fällt eine ungerade Zahl"

## Das Laplace-Modell

Bei einem **Laplace-Experiment** sind alle Elementarereignisse gleich wahrscheinlich. Die Wahrscheinlichkeit eines Ereignisses $A$ berechnet sich dann als:

$$P(A) = \frac{|A|}{|\Omega|} = \frac{\text{Anzahl der günstigen Ergebnisse}}{\text{Anzahl aller möglichen Ergebnisse}}$$

### Beispiel: Gerade Zahl beim Würfeln

Für das Ereignis $A = \{2, 4, 6\}$ (gerade Zahl) gilt:
$$P(A) = \frac{|A|}{|\Omega|} = \frac{3}{6} = \frac{1}{2} = 0{,}5 = 50\%$$

### Eigenschaften von Wahrscheinlichkeiten

Für jede Wahrscheinlichkeit $P(A)$ gilt:

1. **Nichtnegativität:** $0 \le P(A) \le 1$
2. **Normierung:** $P(\Omega) = 1$ und $P(\emptyset) = 0$
3. **Gegenereignis:** $P(\bar{A}) = 1 - P(A)$

## Rechenregeln für Wahrscheinlichkeiten

### Vereinigung von Ereignissen

Für die Wahrscheinlichkeit, dass mindestens eines der Ereignisse $A$ oder $B$ eintritt:

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

Diese Formel heißt **Additionssatz**.

Bei **disjunkten Ereignissen** ($A \cap B = \emptyset$) gilt vereinfacht:
$$P(A \cup B) = P(A) + P(B)$$

### Schnitt von Ereignissen

Die Wahrscheinlichkeit, dass beide Ereignisse $A$ und $B$ eintreten:

$$P(A \cap B) = P(A) \cdot P(B|A)$$

wobei $P(B|A)$ die bedingte Wahrscheinlichkeit von $B$ unter der Bedingung $A$ ist.

Bei **unabhängigen Ereignissen** vereinfacht sich dies zu:
$$P(A \cap B) = P(A) \cdot P(B)$$

### Beispiel: Zwei Würfelwürfe

Wie groß ist die Wahrscheinlichkeit, bei zwei Würfelwürfen mindestens einmal eine 6 zu werfen?

**Lösung über das Gegenereignis:**
- $\bar{A}$: „Keine 6 in zwei Würfen"
- $P(\text{keine 6 bei einem Wurf}) = \frac{5}{6}$
- $P(\bar{A}) = \frac{5}{6} \cdot \frac{5}{6} = \frac{25}{36}$
- $P(A) = 1 - P(\bar{A}) = 1 - \frac{25}{36} = \frac{11}{36} \approx 30{,}6\%$

## Relative Häufigkeit und Wahrscheinlichkeit

### Empirische (relative) Häufigkeit

Bei $n$ Durchführungen eines Experiments und $k$ günstigen Ergebnissen ist die relative Häufigkeit:

$$h_n(A) = \frac{k}{n}$$

### Gesetz der großen Zahlen

Für große $n$ nähert sich die relative Häufigkeit der theoretischen Wahrscheinlichkeit an:

$$\lim_{n \to \infty} h_n(A) = P(A)$$

**Beispiel:** Bei 1000 Münzwürfen erwarten wir etwa 500-mal Kopf, aber nicht exakt. Die Abweichung vom Erwartungswert wird relativ gesehen immer kleiner.

## Mehrstufige Zufallsexperimente

Bei mehrstufigen Experimenten werden nacheinander mehrere Zufallsexperimente durchgeführt.

### Produktregel für unabhängige Experimente

Bei $n$ unabhängigen Experimenten mit Ergebnisräumen $\Omega_1, \Omega_2, \ldots, \Omega_n$ gilt:

$$|\Omega_{\text{gesamt}}| = |\Omega_1| \cdot |\Omega_2| \cdot \ldots \cdot |\Omega_n|$$

**Beispiel:** Zwei Würfel werden geworfen.
- $|\Omega| = 6 \cdot 6 = 36$ mögliche Ergebnisse
- Ergebnis $(2,5)$ bedeutet: erster Würfel zeigt 2, zweiter zeigt 5

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Baumdiagramme]] — Visualisierung mehrstufiger Experimente
- → [[Bedingte-Wahrscheinlichkeit]] — Vertiefung der bedingten Wahrscheinlichkeit
- → [[Unabhaengigkeit-von-Ereignissen]] — Formale Definition der Unabhängigkeit
- → [[Kombinationen]] — Zählprinzipien für die Berechnung von $|A|$ und $|\Omega|$

> [!warning] **Prüfungsrelevant**
> - Das Laplace-Modell und seine korrekte Anwendung (Voraussetzung prüfen!)
> - Berechnung über das Gegenereignis bei „mindestens"-Aufgaben
> - Der Additionssatz für die Vereinigung von Ereignissen
> - Das Erkennen, ob Ereignisse unabhängig oder disjunkt sind

> [!question] **Typische Prüfungsfragen**
> - Berechne die Wahrscheinlichkeit, bei drei Würfelwürfen mindestens eine 6 zu erhalten.
> - Ein Glücksrad ist in Sektoren eingeteilt. Bestimme die Wahrscheinlichkeit für verschiedene Ereignisse.
> - Erkläre den Unterschied zwischen unabhängigen und disjunkten Ereignissen.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3, Springer Vieweg, 2016
- Tietze, J.: Einführung in die angewandte Wirtschaftsmathematik, Springer, 2019
- ISB Bayern: Lehrplan Mathematik Gymnasium, Stochastik

> [!tip] **Weiterführende Links**
> - [[Fakultaeten]] — Für die Berechnung von Anzahlen
> - [[Bernoulli-Experimente]] — Spezielle Zufallsexperimente mit zwei Ausgängen
