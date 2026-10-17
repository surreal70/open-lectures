---
author: Andreas Hümmer
title: Satz von Bayes
tags:
  - content
  - mathe
  - stochastik
  - bayes
  - bedingte-wahrscheinlichkeit
created: 2025-07-01
modified: 2025-07-01
---

# Satz von Bayes

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Satz von Bayes formulieren und herleiten können
> - Die Begriffe Priori- und Posteriori-Wahrscheinlichkeit verstehen
> - Den Satz von Bayes auf praktische Probleme anwenden können
> - Die Grenzen und Fallstricke bei der Interpretation kennen

---

## Überblick

Der Satz von Bayes ermöglicht es, bedingte Wahrscheinlichkeiten „umzukehren": Wenn wir $P(B|A)$ kennen, können wir daraus $P(A|B)$ berechnen. Dieser nach Thomas Bayes (1702–1761) benannte Satz ist fundamental für die statistische Inferenz, medizinische Diagnostik, maschinelles Lernen und viele weitere Anwendungen.

## Der Satz von Bayes

### Grundform

Für zwei Ereignisse $A$ und $B$ mit $P(A) > 0$ und $P(B) > 0$ gilt:

$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$

### Herleitung

Aus der Definition der bedingten Wahrscheinlichkeit:
$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

Nach dem Multiplikationssatz gilt:
$$P(A \cap B) = P(B|A) \cdot P(A)$$

Einsetzen ergibt den Satz von Bayes.

### Erweiterte Form

Mit dem Satz der totalen Wahrscheinlichkeit für eine vollständige Zerlegung $A_1, \ldots, A_n$:

$$P(A_i|B) = \frac{P(B|A_i) \cdot P(A_i)}{\sum_{j=1}^{n} P(B|A_j) \cdot P(A_j)}$$

## Terminologie

### Priori-Wahrscheinlichkeit (a priori)

$P(A)$ — Die Wahrscheinlichkeit von $A$ **vor** der Beobachtung von $B$.
Dies ist unser „Vorwissen" über $A$.

### Likelihood (Beobachtungswahrscheinlichkeit)

$P(B|A)$ — Die Wahrscheinlichkeit, $B$ zu beobachten, **gegeben** dass $A$ wahr ist.

### Posteriori-Wahrscheinlichkeit (a posteriori)

$P(A|B)$ — Die aktualisierte Wahrscheinlichkeit von $A$ **nach** der Beobachtung von $B$.

### Bayessche Formel in Worten

$$\text{Posteriori} = \frac{\text{Likelihood} \times \text{Priori}}{\text{Normierungskonstante}}$$

## Beispiel 1: Medizinischer Test

Ein Test auf eine seltene Krankheit hat:
- **Sensitivität:** $P(T^+|K) = 0{,}99$ (99% der Kranken werden erkannt)
- **Spezifität:** $P(T^-|G) = 0{,}95$ (95% der Gesunden testen negativ)
- **Prävalenz:** $P(K) = 0{,}01$ (1% der Bevölkerung ist krank)

**Frage:** Wie groß ist die Wahrscheinlichkeit, tatsächlich krank zu sein, wenn der Test positiv ist?

### Lösung

Gesucht: $P(K|T^+)$

**Schritt 1:** Berechne $P(T^+)$ (totale Wahrscheinlichkeit)
$$P(T^+) = P(K) \cdot P(T^+|K) + P(G) \cdot P(T^+|G)$$
$$= 0{,}01 \cdot 0{,}99 + 0{,}99 \cdot 0{,}05$$
$$= 0{,}0099 + 0{,}0495 = 0{,}0594$$

**Schritt 2:** Wende Bayes an
$$P(K|T^+) = \frac{P(T^+|K) \cdot P(K)}{P(T^+)} = \frac{0{,}99 \cdot 0{,}01}{0{,}0594} \approx 0{,}167$$

**Interpretation:** Nur etwa **16,7%** der positiv Getesteten sind tatsächlich krank!

### Das Bayes-Paradoxon erklärt

Obwohl der Test eine hohe Sensitivität (99%) hat, ist die Wahrscheinlichkeit einer Erkrankung bei positivem Test nur 16,7%. Der Grund:
- Bei 10.000 Personen sind etwa 100 krank und 9.900 gesund
- Von 100 Kranken testen 99 positiv (richtig-positiv)
- Von 9.900 Gesunden testen 495 positiv (falsch-positiv)
- Insgesamt: 594 positive Tests, davon nur 99 wirklich krank

## Beispiel 2: Produktion und Qualitätskontrolle

Ein Unternehmen hat drei Maschinen:
- Maschine A: 50% der Produktion, 2% Ausschuss
- Maschine B: 30% der Produktion, 3% Ausschuss
- Maschine C: 20% der Produktion, 5% Ausschuss

Ein defektes Teil wird gefunden. Von welcher Maschine stammt es am wahrscheinlichsten?

### Lösung

Gesucht: $P(A|D)$, $P(B|D)$, $P(C|D)$

**Schritt 1:** $P(D)$ (totale Wahrscheinlichkeit)
$$P(D) = 0{,}50 \cdot 0{,}02 + 0{,}30 \cdot 0{,}03 + 0{,}20 \cdot 0{,}05 = 0{,}029$$

**Schritt 2:** Bayes für jede Maschine
$$P(A|D) = \frac{0{,}02 \cdot 0{,}50}{0{,}029} = \frac{0{,}01}{0{,}029} \approx 0{,}345$$

$$P(B|D) = \frac{0{,}03 \cdot 0{,}30}{0{,}029} = \frac{0{,}009}{0{,}029} \approx 0{,}310$$

$$P(C|D) = \frac{0{,}05 \cdot 0{,}20}{0{,}029} = \frac{0{,}01}{0{,}029} \approx 0{,}345$$

**Ergebnis:** Maschinen A und C sind gleich wahrscheinlich (je 34,5%), Maschine B etwas weniger (31%).

## Bayes im Baumdiagramm

### Vorwärtsrichtung (gegeben)

```
              ┌─ D     P(D|A) = 0,02
    ┌─ A ─────┤
    │   0,50  └─ D̄     P(D̄|A) = 0,98
────┤
    │         ┌─ D     P(D|B) = 0,03
    ├─ B ─────┤
    │   0,30  └─ D̄     P(D̄|B) = 0,97
    │
    │         ┌─ D     P(D|C) = 0,05
    └─ C ─────┤
        0,20  └─ D̄     P(D̄|C) = 0,95
```

### Rückwärtsrichtung (gesucht)

Wir „laufen rückwärts" durch den Baum:
- Gegeben: Wir sind bei einem D-Blatt
- Gesucht: Von welcher Wurzelkante kamen wir?

## Sequentielle Anwendung von Bayes

Bayes kann mehrfach angewendet werden, wenn neue Informationen eintreffen:

$$P(A|B_1) \quad \rightarrow \quad P(A|B_1 \cap B_2) \quad \rightarrow \quad \ldots$$

Die Posteriori-Wahrscheinlichkeit nach einer Beobachtung wird zur Priori-Wahrscheinlichkeit für die nächste.

## Häufige Fehler

### Verwechslung von $P(A|B)$ und $P(B|A)$

❌ $P(\text{krank}|\text{Test positiv}) = P(\text{Test positiv}|\text{krank})$

Diese beiden Wahrscheinlichkeiten können sehr unterschiedlich sein!

### Vernachlässigung der Prävalenz

Die Basisrate (Priori-Wahrscheinlichkeit) hat einen enormen Einfluss auf das Ergebnis.

### Base-Rate-Fallacy

Menschen neigen dazu, Basisraten zu ignorieren und sich zu sehr auf die Likelihood zu konzentrieren.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Bedingte-Wahrscheinlichkeit]] — Grundlage für den Satz von Bayes
- → [[Baumdiagramme]] — Visualisierung der Rechnung
- → [[Unabhaengigkeit-von-Ereignissen]] — Spezialfall: $P(A|B) = P(A)$
- → [[Wiederholung-der-Wahrscheinlichkeitsrechnung]] — Grundbegriffe

> [!warning] **Prüfungsrelevant**
> - Die Formel des Satzes von Bayes sicher anwenden
> - Berechnung von $P(B)$ über die totale Wahrscheinlichkeit
> - Interpretation der Ergebnisse (insbes. bei medizinischen Tests)
> - Unterscheidung von Priori und Posteriori

> [!question] **Typische Prüfungsfragen**
> - Ein medizinischer Test hat Sensitivität 95% und Spezifität 90%. Bei einer Prävalenz von 2%: Wie groß ist P(krank|positiv)?
> - Zwei Urnen: Urne A (3 rote, 2 blaue), Urne B (1 rote, 4 blaue). Eine Urne wird zufällig gewählt, eine Kugel gezogen. Sie ist rot. Wie groß ist die Wahrscheinlichkeit, dass sie aus Urne A stammt?
> - Erkläre, warum bei seltenen Krankheiten auch bei guten Tests viele falsch-positive Ergebnisse auftreten.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3, Springer Vieweg, 2016
- Bronstein, I.N. et al.: Taschenbuch der Mathematik, Verlag Europa-Lehrmittel, 2020
- Gigerenzer, G.: Das Einmaleins der Skepsis, Piper, 2015

> [!tip] **Weiterführende Links**
> - [[Bedingte-Wahrscheinlichkeit]] — Vertiefung der Grundlagen
> - [[Bernoulli-Experimente]] — Anwendung bei wiederholten Tests
