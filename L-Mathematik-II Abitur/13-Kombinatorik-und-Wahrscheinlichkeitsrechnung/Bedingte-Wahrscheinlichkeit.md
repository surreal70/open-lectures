---
author: Andreas Hümmer
title: Bedingte Wahrscheinlichkeit
tags:
  - content
  - mathe
  - stochastik
  - bedingte-wahrscheinlichkeit
  - abhängigkeit
created: 2025-07-01
modified: 2025-07-01
---

# Bedingte Wahrscheinlichkeit

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die bedingte Wahrscheinlichkeit definieren und berechnen können
> - Den Multiplikationssatz anwenden können
> - Den Satz der totalen Wahrscheinlichkeit verstehen
> - Bedingte Wahrscheinlichkeiten in Baumdiagrammen erkennen

---

## Überblick

Die bedingte Wahrscheinlichkeit beschreibt, wie sich die Wahrscheinlichkeit eines Ereignisses ändert, wenn wir zusätzliche Information über ein anderes Ereignis haben. Sie ist eines der wichtigsten Konzepte der Stochastik und bildet die Grundlage für den Satz von Bayes und viele Anwendungen in Statistik, Medizin und künstlicher Intelligenz.

## Definition der bedingten Wahrscheinlichkeit

Die **bedingte Wahrscheinlichkeit** von $A$ unter der Bedingung $B$ ist definiert als:

$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

für $P(B) > 0$.

**Sprechweise:** „Die Wahrscheinlichkeit von $A$ gegeben $B$" oder „Die Wahrscheinlichkeit von $A$, wenn $B$ eingetreten ist"

### Interpretation

$P(A|B)$ gibt an, mit welcher Wahrscheinlichkeit $A$ eintritt, wenn wir bereits wissen, dass $B$ eingetreten ist. Durch die Bedingung $B$ wird der Ergebnisraum eingeschränkt.

### Visualisierung

```
┌─────────────────────────────────────┐
│              Ω                      │
│    ┌───────────────┐                │
│    │       B       │                │
│    │   ┌───────┐   │                │
│    │   │ A ∩ B │   │                │
│    │   └───────┘   │                │
│    └───────────────┘                │
└─────────────────────────────────────┘

P(A|B) = Anteil von A∩B an B
```

## Beispiel 1: Würfelwurf

Ein Würfel wird geworfen. Wie groß ist die Wahrscheinlichkeit für eine 6, wenn bekannt ist, dass eine gerade Zahl gefallen ist?

**Lösung:**
- $A = \{6\}$ — „Es fällt eine 6"
- $B = \{2, 4, 6\}$ — „Es fällt eine gerade Zahl"
- $A \cap B = \{6\}$

$$P(A|B) = \frac{P(A \cap B)}{P(B)} = \frac{1/6}{3/6} = \frac{1/6}{1/2} = \frac{1}{3}$$

**Interpretation:** Wenn wir wissen, dass eine gerade Zahl gefallen ist, ist die 6 eine von drei gleichwahrscheinlichen Möglichkeiten.

## Beispiel 2: Urnenziehung

Eine Urne enthält 4 rote und 6 blaue Kugeln. Es werden nacheinander zwei Kugeln ohne Zurücklegen gezogen.

**Gesucht:** P(2. Kugel rot | 1. Kugel rot)

**Lösung:**
Nach dem Ziehen einer roten Kugel sind noch:
- 3 rote Kugeln
- 6 blaue Kugeln
- insgesamt 9 Kugeln

$$P(\text{2. rot} | \text{1. rot}) = \frac{3}{9} = \frac{1}{3}$$

## Der Multiplikationssatz

Durch Umstellen der Definition erhalten wir den **Multiplikationssatz**:

$$P(A \cap B) = P(B) \cdot P(A|B) = P(A) \cdot P(B|A)$$

### Allgemeine Form

Für mehrere Ereignisse $A_1, A_2, \ldots, A_n$:

$$P(A_1 \cap A_2 \cap \ldots \cap A_n) = P(A_1) \cdot P(A_2|A_1) \cdot P(A_3|A_1 \cap A_2) \cdot \ldots$$

### Anwendung im Baumdiagramm

Die Pfadregel „Wahrscheinlichkeiten entlang eines Pfades multiplizieren" ist genau der Multiplikationssatz!

## Beispiel 3: Zwei Karten ziehen

Aus einem Kartenspiel mit 32 Karten werden 2 Karten ohne Zurücklegen gezogen. Wie groß ist die Wahrscheinlichkeit, zwei Asse zu ziehen?

**Lösung:**
- $A_1$: 1. Karte ist ein Ass, $P(A_1) = \frac{4}{32} = \frac{1}{8}$
- $A_2|A_1$: 2. Karte ist ein Ass, gegeben 1. war Ass, $P(A_2|A_1) = \frac{3}{31}$

$$P(A_1 \cap A_2) = P(A_1) \cdot P(A_2|A_1) = \frac{4}{32} \cdot \frac{3}{31} = \frac{12}{992} = \frac{3}{248}$$

## Der Satz der totalen Wahrscheinlichkeit

Wenn $B_1, B_2, \ldots, B_n$ eine **vollständige Zerlegung** von $\Omega$ bilden (d.h. paarweise disjunkt und $\bigcup B_i = \Omega$), dann gilt:

$$P(A) = \sum_{i=1}^{n} P(B_i) \cdot P(A|B_i)$$

### Visualisierung

```
┌────────────────────────────────────────┐
│                  Ω                     │
│  ┌────────┬────────┬────────┐          │
│  │   B₁   │   B₂   │   B₃   │          │
│  │  ╔═══╗ │ ╔════╗ │ ╔═══╗  │          │
│  │  ║ A ║ │ ║ A  ║ │ ║ A ║  │          │
│  │  ╚═══╝ │ ╚════╝ │ ╚═══╝  │          │
│  └────────┴────────┴────────┘          │
└────────────────────────────────────────┘

P(A) = P(B₁)·P(A|B₁) + P(B₂)·P(A|B₂) + P(B₃)·P(A|B₃)
```

## Beispiel 4: Produktion in drei Werken

Ein Unternehmen produziert in drei Werken:
- Werk 1: 50% der Produktion, Ausschussquote 2%
- Werk 2: 30% der Produktion, Ausschussquote 3%
- Werk 3: 20% der Produktion, Ausschussquote 5%

Wie groß ist die Gesamtausschussquote?

**Lösung:**
- $B_1, B_2, B_3$: Produkt stammt aus Werk 1, 2 bzw. 3
- $A$: Produkt ist Ausschuss

$$P(A) = P(B_1) \cdot P(A|B_1) + P(B_2) \cdot P(A|B_2) + P(B_3) \cdot P(A|B_3)$$
$$= 0{,}50 \cdot 0{,}02 + 0{,}30 \cdot 0{,}03 + 0{,}20 \cdot 0{,}05$$
$$= 0{,}010 + 0{,}009 + 0{,}010 = 0{,}029 = 2{,}9\%$$

## Beispiel 5: Medizinischer Test

Ein Test auf eine Krankheit hat folgende Eigenschaften:
- Sensitivität: 99% (Test positiv bei Kranken)
- Spezifität: 95% (Test negativ bei Gesunden)
- Prävalenz: 1% (Anteil Kranker in der Bevölkerung)

Wie groß ist die Wahrscheinlichkeit für einen positiven Test?

**Notation:**
- $K$: Person ist krank, $P(K) = 0{,}01$
- $G$: Person ist gesund, $P(G) = 0{,}99$
- $T^+$: Test positiv

$$P(T^+) = P(K) \cdot P(T^+|K) + P(G) \cdot P(T^+|G)$$
$$= 0{,}01 \cdot 0{,}99 + 0{,}99 \cdot 0{,}05$$
$$= 0{,}0099 + 0{,}0495 = 0{,}0594 \approx 5{,}9\%$$

## Bedingte Wahrscheinlichkeit im Baumdiagramm

### Vorwärts lesen

```
              ┌─ A     P(A|B₁)
    ┌─ B₁ ────┤
    │   p₁    └─ Ā     P(Ā|B₁)
────┤
    │         ┌─ A     P(A|B₂)
    └─ B₂ ────┤
        p₂    └─ Ā     P(Ā|B₂)
```

Die Wahrscheinlichkeiten an den Kanten der 2. Stufe sind bedingte Wahrscheinlichkeiten!

### Rückwärts rechnen

Um $P(B_1|A)$ zu berechnen (die „umgekehrte" Richtung), benötigt man den Satz von Bayes.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Wiederholung-der-Wahrscheinlichkeitsrechnung]] — Grundlagen
- → [[Baumdiagramme]] — Visualisierung bedingter Wahrscheinlichkeiten
- → [[Satz-von-Bayes]] — „Umkehrung" der bedingten Wahrscheinlichkeit
- → [[Unabhaengigkeit-von-Ereignissen]] — Wann $P(A|B) = P(A)$

> [!warning] **Prüfungsrelevant**
> - Definition und Formel für $P(A|B)$
> - Der Multiplikationssatz und seine Anwendung
> - Der Satz der totalen Wahrscheinlichkeit
> - Unterscheidung zwischen $P(A|B)$ und $P(B|A)$

> [!question] **Typische Prüfungsfragen**
> - Ein Würfel wird geworfen. Berechne P(Augenzahl > 4 | Augenzahl gerade).
> - Aus einer Urne mit 5 weißen und 3 schwarzen Kugeln werden 2 Kugeln ohne Zurücklegen gezogen. Berechne P(2. weiß | 1. schwarz).
> - Ein Unternehmen bezieht Bauteile von zwei Zulieferern. Berechne die Gesamtfehlerquote.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3, Springer Vieweg, 2016
- Bronstein, I.N. et al.: Taschenbuch der Mathematik, Verlag Europa-Lehrmittel, 2020
- ISB Bayern: Lehrplan Mathematik Gymnasium, Stochastik

> [!tip] **Weiterführende Links**
> - [[Satz-von-Bayes]] — Berechnung von $P(B|A)$ aus $P(A|B)$
> - [[Unabhaengigkeit-von-Ereignissen]] — Spezialfall: keine Abhängigkeit
