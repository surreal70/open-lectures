---
author: Andreas Hümmer
title: Baumdiagramme
tags:
  - content
  - mathe
  - stochastik
  - baumdiagramm
  - visualisierung
created: 2025-07-01
modified: 2025-07-01
---

# Baumdiagramme

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Mehrstufige Zufallsexperimente als Baumdiagramm darstellen können
> - Die Pfadregeln (Multiplikations- und Additionsregel) anwenden können
> - Wahrscheinlichkeiten systematisch berechnen können
> - Rückwärts im Baum arbeiten können (für bedingte Wahrscheinlichkeiten)

---

## Überblick

Baumdiagramme sind ein zentrales Werkzeug zur Visualisierung und Berechnung von Wahrscheinlichkeiten bei mehrstufigen Zufallsexperimenten. Sie stellen die zeitliche Abfolge von Ereignissen und deren Wahrscheinlichkeiten übersichtlich dar und ermöglichen die systematische Anwendung der Pfadregeln.

## Aufbau eines Baumdiagramms

### Grundstruktur

Ein Baumdiagramm besteht aus:
- **Startknoten** (Wurzel): Ausgangspunkt des Experiments
- **Verzweigungen** (Kanten): Mögliche Ausgänge einer Stufe
- **Knoten**: Zwischenzustände nach einer Stufe
- **Endknoten** (Blätter): Endergebnisse des gesamten Experiments

```
                    ┌─── A₁ ─── Ergebnis (A₁, B₁)
           ┌── A ───┤
           │   p(A) └─── A₂ ─── Ergebnis (A₁, B₂)
    Start ─┤
           │        ┌─── B₁ ─── Ergebnis (A₂, B₁)
           └── B ───┤
               p(B) └─── B₂ ─── Ergebnis (A₂, B₂)
```

### Beschriftung

- An jeder Kante steht die (bedingte) Wahrscheinlichkeit für diesen Übergang
- Die Summe der Wahrscheinlichkeiten aller von einem Knoten ausgehenden Kanten ist immer 1

## Die Pfadregeln

### 1. Multiplikationsregel (Produktregel)

Die Wahrscheinlichkeit eines Pfades ist das **Produkt** der Wahrscheinlichkeiten entlang des Pfades.

$$P(\text{Pfad}) = P(E_1) \cdot P(E_2|E_1) \cdot P(E_3|E_1 \cap E_2) \cdot \ldots$$

Bei unabhängigen Stufen vereinfacht sich dies zu:
$$P(\text{Pfad}) = P(E_1) \cdot P(E_2) \cdot P(E_3) \cdot \ldots$$

### 2. Additionsregel (Summenregel)

Die Wahrscheinlichkeit eines Ereignisses, das durch **mehrere Pfade** erreicht werden kann, ist die **Summe** der einzelnen Pfadwahrscheinlichkeiten.

$$P(A) = \sum_{\text{alle Pfade zu } A} P(\text{Pfad})$$

## Beispiel 1: Zweimaliges Würfeln

Wir würfeln zweimal und interessieren uns für das Ereignis „mindestens einmal eine 6".

### Baumdiagramm

```
                        ┌─ 6     P = 1/6 · 1/6 = 1/36
              ┌─ 6 ─────┤
              │   1/6   └─ k.6   P = 1/6 · 5/6 = 5/36
    Start ────┤
              │         ┌─ 6     P = 5/6 · 1/6 = 5/36
              └─ k.6 ───┤
                  5/6   └─ k.6   P = 5/6 · 5/6 = 25/36
```

(k.6 = keine 6)

### Berechnung

**Mindestens eine 6:** Pfade 1, 2 oder 3
$$P(\text{mind. eine 6}) = \frac{1}{36} + \frac{5}{36} + \frac{5}{36} = \frac{11}{36}$$

**Alternative über Gegenereignis:**
$$P(\text{mind. eine 6}) = 1 - P(\text{keine 6}) = 1 - \frac{25}{36} = \frac{11}{36}$$

## Beispiel 2: Urnenziehung ohne Zurücklegen

Eine Urne enthält 3 rote und 2 blaue Kugeln. Es wird zweimal ohne Zurücklegen gezogen.

### Baumdiagramm

```
                        ┌─ R     P = 3/5 · 2/4 = 6/20 = 3/10
              ┌─ R ─────┤   2/4
              │   3/5   └─ B     P = 3/5 · 2/4 = 6/20 = 3/10
    Start ────┤             2/4
              │         ┌─ R     P = 2/5 · 3/4 = 6/20 = 3/10
              └─ B ─────┤   3/4
                  2/5   └─ B     P = 2/5 · 1/4 = 2/20 = 1/10
                            1/4
```

### Berechnungen

**P(beide rot):**
$$P(R, R) = \frac{3}{5} \cdot \frac{2}{4} = \frac{6}{20} = \frac{3}{10}$$

**P(verschiedene Farben):**
$$P(\text{versch.}) = P(R, B) + P(B, R) = \frac{3}{10} + \frac{3}{10} = \frac{6}{10} = \frac{3}{5}$$

**P(mind. eine rote):**
$$P(\text{mind. eine R}) = 1 - P(B, B) = 1 - \frac{1}{10} = \frac{9}{10}$$

## Beispiel 3: Mit Zurücklegen

Dieselbe Urne (3 rote, 2 blaue), aber mit Zurücklegen:

### Baumdiagramm

```
                        ┌─ R     P = 3/5 · 3/5 = 9/25
              ┌─ R ─────┤   3/5
              │   3/5   └─ B     P = 3/5 · 2/5 = 6/25
    Start ────┤             2/5
              │         ┌─ R     P = 2/5 · 3/5 = 6/25
              └─ B ─────┤   3/5
                  2/5   └─ B     P = 2/5 · 2/5 = 4/25
                            2/5
```

**Beachte:** Die Wahrscheinlichkeiten der zweiten Stufe sind jetzt unabhängig von der ersten Stufe!

## Dreistufige Experimente

### Beispiel: Dreimaliger Münzwurf

Wie groß ist die Wahrscheinlichkeit für genau zweimal Kopf?

```
                              ┌─ K (KKK)  P = 1/8
                    ┌─ K ─────┤
          ┌─ K ─────┤         └─ Z (KKZ)  P = 1/8  ✓
          │         │         ┌─ K (KZK)  P = 1/8  ✓
          │         └─ Z ─────┤
Start ────┤                   └─ Z (KZZ)  P = 1/8
          │                   ┌─ K (ZKK)  P = 1/8  ✓
          │         ┌─ K ─────┤
          └─ Z ─────┤         └─ Z (ZKZ)  P = 1/8
                    │         ┌─ K (ZZK)  P = 1/8
                    └─ Z ─────┤
                              └─ Z (ZZZ)  P = 1/8
```

**P(genau 2× Kopf):**
$$P = \frac{1}{8} + \frac{1}{8} + \frac{1}{8} = \frac{3}{8}$$

Alternative: $\binom{3}{2} \cdot \left(\frac{1}{2}\right)^3 = 3 \cdot \frac{1}{8} = \frac{3}{8}$

## Reduzierte Baumdiagramme

Bei symmetrischen Experimenten kann man das Baumdiagramm vereinfachen, indem man nur die Anzahl der Erfolge zählt:

### Beispiel: Dreimaliger Münzwurf (reduziert)

```
                    ┌─ 3× K    1 Pfad    P = 1/8
          ┌─ 2× K ──┤
          │         └─ 2× K    3 Pfade   P = 3/8
Start ────┤
          │         ┌─ 1× K    3 Pfade   P = 3/8
          └─ 1× K ──┤
                    └─ 0× K    1 Pfad    P = 1/8
```

## Typische Fehler vermeiden

### Fehler 1: Verwechslung der Pfadregeln

❌ Falsch: Wahrscheinlichkeiten auf verschiedenen Pfaden multiplizieren
✅ Richtig: Entlang eines Pfades multiplizieren, verschiedene Pfade addieren

### Fehler 2: Vergessen der bedingten Wahrscheinlichkeiten

Bei Ziehen ohne Zurücklegen ändern sich die Wahrscheinlichkeiten!

### Fehler 3: Unvollständiges Baumdiagramm

Alle möglichen Ausgänge müssen berücksichtigt werden.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Wiederholung-der-Wahrscheinlichkeitsrechnung]] — Grundlagen
- → [[Bedingte-Wahrscheinlichkeit]] — Vertiefung der Pfadwahrscheinlichkeiten
- → [[Satz-von-Bayes]] — Rückwärtsrechnen im Baum
- → [[Bernoulli-Ketten]] — Spezialfall mit zwei Ausgängen

> [!warning] **Prüfungsrelevant**
> - Korrektes Aufstellen von Baumdiagrammen
> - Sichere Anwendung von Multiplikations- und Additionsregel
> - Unterscheidung: Mit oder ohne Zurücklegen
> - Berechnung von „mindestens"-Wahrscheinlichkeiten über das Gegenereignis

> [!question] **Typische Prüfungsfragen**
> - Stelle ein Baumdiagramm auf für das dreimalige Ziehen aus einer Urne mit 4 roten und 6 blauen Kugeln ohne Zurücklegen.
> - Berechne die Wahrscheinlichkeit, bei vier Würfen mindestens einmal eine 6 zu erhalten.
> - Eine Urne enthält 5 weiße und 3 schwarze Kugeln. Berechne P(genau 2 weiße) bei dreimaligem Ziehen mit Zurücklegen.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3, Springer Vieweg, 2016
- ISB Bayern: Lehrplan Mathematik Gymnasium, Stochastik
- Tietze, J.: Einführung in die angewandte Wirtschaftsmathematik, Springer, 2019

> [!tip] **Weiterführende Links**
> - [[Bedingte-Wahrscheinlichkeit]] — Wenn der Baum komplexer wird
> - [[Bernoulli-Experimente]] — Vereinfachung für wiederholte Ja/Nein-Experimente
