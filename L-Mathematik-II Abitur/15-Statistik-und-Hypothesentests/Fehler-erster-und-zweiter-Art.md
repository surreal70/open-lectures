---
author: Andreas Hümmer
title: Fehler erster und zweiter Art
tags:
  - content
  - mathe
  - statistik
  - hypothesentest
  - fehler
  - alpha
  - beta
created: 2025-06-26
modified: 2025-06-26
---

# Fehler erster und zweiter Art

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Fehler erster und zweiter Art unterscheiden und definieren können
> - Die Wahrscheinlichkeiten $\alpha$ und $\beta$ berechnen und interpretieren können
> - Den Zusammenhang zwischen beiden Fehlerarten verstehen
> - Die Gütefunktion und den Begriff der Macht eines Tests kennen

---

## Überblick

Bei einem Hypothesentest kann man zwei Arten von Fehlentscheidungen treffen: Man kann $H_0$ ablehnen, obwohl sie wahr ist (Fehler 1. Art), oder $H_0$ beibehalten, obwohl sie falsch ist (Fehler 2. Art). Beide Fehler haben unterschiedliche Konsequenzen und können nicht gleichzeitig minimiert werden.

---

## Die vier möglichen Ausgänge

Ein Hypothesentest hat vier mögliche Kombinationen aus Realität und Entscheidung:

|  | **$H_0$ ist wahr** | **$H_0$ ist falsch** |
|---|:---:|:---:|
| **$H_0$ nicht ablehnen** | ✓ Richtige Entscheidung | ✗ Fehler 2. Art ($\beta$) |
| **$H_0$ ablehnen** | ✗ Fehler 1. Art ($\alpha$) | ✓ Richtige Entscheidung |

### Fehler erster Art (α-Fehler)

Der **Fehler erster Art** tritt auf, wenn $H_0$ abgelehnt wird, obwohl sie wahr ist.

$$\alpha = P(\text{Ablehnung von } H_0 \mid H_0 \text{ ist wahr})$$

**Andere Bezeichnungen:** 
- Falsch-positiv-Rate
- Irrtum der ersten Art
- Überspezifischer Fehler

### Fehler zweiter Art (β-Fehler)

Der **Fehler zweiter Art** tritt auf, wenn $H_0$ nicht abgelehnt wird, obwohl sie falsch ist (d.h. $H_1$ wahr ist).

$$\beta = P(\text{Keine Ablehnung von } H_0 \mid H_1 \text{ ist wahr})$$

**Andere Bezeichnungen:**
- Falsch-negativ-Rate
- Irrtum der zweiten Art
- Unspezifischer Fehler

---

## Anschauliche Beispiele

### Gerichtsverfahren

| Statistik | Gerichtsanalogie |
|-----------|------------------|
| $H_0$: unschuldig | Unschuldsvermutung |
| $H_1$: schuldig | Anklage |
| Fehler 1. Art | Unschuldiger wird verurteilt |
| Fehler 2. Art | Schuldiger wird freigesprochen |

Das Rechtssystem legt hohen Wert darauf, Fehler 1. Art zu vermeiden („Im Zweifel für den Angeklagten").

### Medizinischer Test

| Statistik | Medizinische Diagnose |
|-----------|----------------------|
| $H_0$: gesund | Patient hat keine Krankheit |
| $H_1$: krank | Patient hat die Krankheit |
| Fehler 1. Art | Gesunder wird als krank diagnostiziert |
| Fehler 2. Art | Kranker wird als gesund diagnostiziert |

### Qualitätskontrolle

| Statistik | Produktionskontrolle |
|-----------|---------------------|
| $H_0$: Charge in Ordnung | Ausschussquote im Rahmen |
| $H_1$: Charge fehlerhaft | Ausschussquote zu hoch |
| Fehler 1. Art | Gute Charge wird aussortiert |
| Fehler 2. Art | Schlechte Charge wird ausgeliefert |

---

## Berechnung der Fehlerwahrscheinlichkeiten

### Fehler 1. Art ($\alpha$)

Der Fehler 1. Art ist direkt durch das Signifikanzniveau festgelegt:

$$\alpha = P(X \in \text{Ablehnungsbereich} \mid H_0)$$

**Beispiel:** Binomialtest mit $n = 20$, $p_0 = 0{,}5$, Ablehnungsbereich $\{15, 16, \ldots, 20\}$

$$\alpha = P(X \geq 15 \mid p = 0{,}5) = \sum_{k=15}^{20} \binom{20}{k} \cdot 0{,}5^k \cdot 0{,}5^{20-k}$$

$$\alpha \approx 0{,}0207$$

### Fehler 2. Art ($\beta$)

Der Fehler 2. Art hängt vom wahren (aber unbekannten) Parameter ab:

$$\beta(p) = P(X \notin \text{Ablehnungsbereich} \mid p)$$

**Beispiel:** Für denselben Test, wenn der wahre Wert $p_1 = 0{,}7$ ist:

$$\beta(0{,}7) = P(X < 15 \mid p = 0{,}7) = P(X \leq 14 \mid p = 0{,}7)$$

$$\beta(0{,}7) = \sum_{k=0}^{14} \binom{20}{k} \cdot 0{,}7^k \cdot 0{,}3^{20-k} \approx 0{,}5836$$

Das bedeutet: Selbst wenn der wahre Anteil 0,7 beträgt, erkennt der Test dies in 58% der Fälle nicht!

---

## Die Gütefunktion

Die **Gütefunktion** (Power Function) gibt für jeden möglichen Parameterwert die Wahrscheinlichkeit an, $H_0$ abzulehnen:

$$G(p) = P(\text{Ablehnung von } H_0 \mid p)$$

### Eigenschaften

- Für $p = p_0$ (unter $H_0$): $G(p_0) = \alpha$
- Für $p \neq p_0$ (unter $H_1$): $G(p) = 1 - \beta(p)$

### Die Macht (Power) eines Tests

Die **Macht** (Power) ist die Wahrscheinlichkeit, $H_0$ korrekt abzulehnen, wenn $H_1$ wahr ist:

$$\text{Macht} = 1 - \beta$$

Ein Test mit hoher Macht erkennt Abweichungen von $H_0$ zuverlässig.

---

## Zusammenhang zwischen $\alpha$ und $\beta$

### Das Dilemma

Bei festem Stichprobenumfang $n$ stehen $\alpha$ und $\beta$ in Konkurrenz:

- **Kleineres $\alpha$** → Ablehnungsbereich wird kleiner → **$\beta$ wird größer**
- **Größeres $\alpha$** → Ablehnungsbereich wird größer → **$\beta$ wird kleiner**

Man kann nicht beide Fehler gleichzeitig minimieren!

### Visualisierung

```
         H₀ wahr                    H₁ wahr (z.B. p₁ > p₀)
         
    │                           │
    │    ┌─────┐               │         ┌─────┐
    │    │     │               │         │     │
    │   ╱│     │╲             │        ╱│     │╲
    │  ╱ │     │ ╲            │       ╱ │     │ ╲
    │ ╱  │     │  ╲           │      ╱  │     │  ╲
    │╱   │     │   ╲          │     ╱   │     │   ╲
    ├────┴─────┴────┼─────────┼────┴────┴─────┴────
                    │krit. Wert│
         
         ──α──                        ──β──
      (Fehler 1. Art)             (Fehler 2. Art)
```

### Lösung: Stichprobenumfang erhöhen

Durch Vergrößerung von $n$ können beide Fehlerwahrscheinlichkeiten reduziert werden. Die Verteilungen werden schmaler, und der Überlappungsbereich wird kleiner.

---

## Praktische Konsequenzen

### Welchen Fehler minimieren?

Die Wahl hängt von den Konsequenzen ab:

| Situation | Priorität | Begründung |
|-----------|-----------|------------|
| Medikamentenzulassung | $\alpha$ klein | Unwirksames Medikament schadet Patienten |
| Krankheitsscreening | $\beta$ klein | Übersehene Krankheit ist gefährlich |
| Gerichtsverfahren | $\alpha$ klein | Unschuldige schützen |
| Qualitätskontrolle | Abwägung | Kosten für beide Fehler vergleichen |

### Typische Werte

- $\alpha$: wird festgelegt (meist 0,05 oder 0,01)
- $\beta$: wird berechnet oder durch $n$ gesteuert
- Übliches Ziel: $\beta \leq 0{,}2$ (Macht $\geq 0{,}8$)

---

## Beispiel: Vollständige Fehleranalyse

**Situation:** Ein Hersteller behauptet $p \leq 0{,}10$ Ausschuss. Test mit $n = 50$, $\alpha = 0{,}05$.

**1. Hypothesen:**
$$H_0: p \leq 0{,}10 \quad H_1: p > 0{,}10$$

**2. Ablehnungsbereich bestimmen:**
Unter $H_0$ mit $p_0 = 0{,}10$: $X \sim B(50, 0{,}1)$

Gesucht: kleinstes $k$ mit $P(X \geq k) \leq 0{,}05$

$P(X \geq 9) \approx 0{,}0402 \leq 0{,}05$ ✓

Ablehnungsbereich: $\{9, 10, \ldots, 50\}$

**3. Tatsächliches $\alpha$:**
$$\alpha = P(X \geq 9 \mid p = 0{,}1) \approx 0{,}0402$$

**4. Fehler 2. Art für $p_1 = 0{,}20$:**
$$\beta(0{,}2) = P(X \leq 8 \mid p = 0{,}2)$$

Mit $X \sim B(50, 0{,}2)$: $\beta(0{,}2) \approx 0{,}3073$

**Interpretation:** Wenn der wahre Ausschuss 20% beträgt, erkennt der Test dies nur in ca. 70% der Fälle.

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Signifikanzniveau]] – Festlegung von $\alpha$
- → [[Nullhypothese-und-Alternativhypothese]] – Grundlage für Fehlerdefinitionen
- → [[Binomialtests]] – Konkrete Berechnung der Fehlerwahrscheinlichkeiten
- → [[Stichproben]] – Einfluss des Stichprobenumfangs

> [!warning] **Prüfungsrelevant**
> - Definition und Unterscheidung beider Fehlerarten
> - Berechnung von $\alpha$ aus dem Ablehnungsbereich
> - Berechnung von $\beta$ für gegebenes alternatives $p_1$
> - Zusammenhang: $\alpha$ senken → $\beta$ steigt (bei festem $n$)
> - Macht = $1 - \beta$ = Wahrscheinlichkeit, $H_0$ korrekt abzulehnen
> - Praktische Interpretation: Welcher Fehler wiegt schwerer?

> [!question] **Typische Prüfungsfragen**
> - Erkläre den Unterschied zwischen Fehler erster und zweiter Art an einem Beispiel aus der Qualitätskontrolle.
> - Ein Test hat Ablehnungsbereich $\{12, 13, \ldots, 20\}$ bei $n=20$, $p_0=0{,}3$. Berechne $\alpha$ und $\beta(0{,}5)$.
> - Wie kann man bei gegebenem $\alpha$ den Fehler 2. Art reduzieren?

---

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3. Springer Vieweg, 2016.
- Fahrmeir, L. et al.: Statistik – Der Weg zur Datenanalyse. Springer, 2016.
- ISB Bayern: Abiturprüfungen Mathematik.

> [!tip] **Weiterführende Links**
> - [[Binomialtests]] – Praktische Anwendung der Fehlerberechnung
> - [[Interpretation-statistischer-Ergebnisse]] – Kommunikation von Testergebnissen
