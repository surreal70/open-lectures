---
title: Gegenereignisse
chapter: "14"
section: "14.7"
type: lecture
created: 2026-10-13
modified: 2025-01-20
status: draft - review pending
tags:
  - mathematik/wahrscheinlichkeit
  - gegenereignis
---

# Gegenereignisse

## Einführung

> [!info] **Lernziele**
> Nach dieser Lektion können Sie:
> - Gegenereignisse bestimmen
> - Die Gegenwahrscheinlichkeit berechnen

---

## Überblick

Das Konzept des Gegenereignisses ist eines der mächtigsten Werkzeuge in der Wahrscheinlichkeitsrechnung. Oft ist es viel einfacher, die Wahrscheinlichkeit zu berechnen, dass etwas *nicht* passiert, und daraus dann auf die eigentlich gesuchte Wahrscheinlichkeit zu schließen.

Dieser Trick ist besonders nützlich bei Formulierungen wie „mindestens einmal", „wenigstens einer" oder „nicht alle". In solchen Fällen ist das Gegenereignis oft viel einfacher zu berechnen als das Ereignis selbst.

---

## Definition

> [!note] **Definition**
> Das **Gegenereignis** $\bar{A}$ (auch $A'$ oder $A^c$ geschrieben) enthält alle Ergebnisse, die **nicht** in A liegen.
> 
> Mathematisch: $\bar{A} = Ω \setminus A$ (Omega ohne A)

### Anschaulich

Wenn A eintritt, tritt $\bar{A}$ nicht ein – und umgekehrt. Die beiden Ereignisse schließen sich gegenseitig aus und ergänzen sich zu 100%.

```
┌──────────────────────────────────┐
│              Ω                   │
│   ┌──────────┐                   │
│   │    A     │      Ā            │
│   │          │                   │
│   └──────────┘                   │
└──────────────────────────────────┘

A und Ā zusammen = Ω (alle Möglichkeiten)
```

---

## Formel

> [!note] **Gegenwahrscheinlichkeit**
> $$P(\bar{A}) = 1 - P(A)$$
> 
> Oder umgestellt: $P(A) = 1 - P(\bar{A})$

Diese einfache Formel folgt direkt aus der Tatsache, dass A und $\bar{A}$ zusammen das sichere Ereignis Ω ergeben, dessen Wahrscheinlichkeit 1 ist.

---

## Beispiele

> [!example] **Würfel: Keine Sechs**
> A = "Sechs würfeln" → $\bar{A}$ = "Keine Sechs"
> 
> $P(A) = \frac{1}{6}$ → $P(\bar{A}) = 1 - \frac{1}{6} = \frac{5}{6} \approx 83{,}3\%$

> [!example] **Mindestens einmal Sechs bei 3 Würfen**
> Direkt zu rechnen wäre kompliziert (1×, 2× oder 3× Sechs).
> 
> Das Gegenereignis ist einfacher:
> $\bar{A}$ = "Keine Sechs bei 3 Würfen"
> 
> $P(\bar{A}) = \left(\frac{5}{6}\right)^3 = \frac{125}{216} \approx 57{,}9\%$
> 
> Also: $P(A) = 1 - \frac{125}{216} = \frac{91}{216} \approx 42{,}1\%$

---

## Wann das Gegenereignis nutzen?

> [!tip] **Wann ist das Gegenereignis hilfreich?**
> Bei Formulierungen mit:
> - „**mindestens einmal**" → Gegenereignis: „kein einziges Mal"
> - „**wenigstens einer**" → Gegenereignis: „keiner"
> - „**nicht alle gleich**" → Gegenereignis: „alle gleich"
> 
> In diesen Fällen ist das Gegenereignis meist viel einfacher zu berechnen!

### Beispiel: Das Geburtstagsproblem

Ein berühmtes Beispiel: Wie wahrscheinlich ist es, dass in einer Gruppe von 23 Personen mindestens zwei am gleichen Tag Geburtstag haben?

Direkt wäre das extrem aufwändig (alle Kombinationen von 2, 3, 4, ... Personen mit gleichem Geburtstag).

Das Gegenereignis ist einfacher: „Alle haben an verschiedenen Tagen Geburtstag."

$$P(\bar{A}) = \frac{365}{365} \cdot \frac{364}{365} \cdot \frac{363}{365} \cdot ... \cdot \frac{343}{365} \approx 0{,}493$$

Also: $P(A) = 1 - 0{,}493 \approx 50{,}7\%$

Überraschend: Bei nur 23 Personen ist es wahrscheinlicher, dass zwei am gleichen Tag Geburtstag haben, als dass alle unterschiedliche Geburtstage haben!

---

## Typische Aufgabentypen

| Formulierung | Gegenereignis | Berechnung |
|--------------|---------------|------------|
| Mindestens 1× Treffer | Kein Treffer | $1 - P(\text{kein Treffer})$ |
| Höchstens 2× Sechs | Mehr als 2× Sechs | Oft direkt einfacher |
| Nicht alle gleich | Alle gleich | $1 - P(\text{alle gleich})$ |

> [!warning] **Häufiger Fehler**
> Das Gegenereignis von „mindestens 2" ist **nicht** „höchstens 2", sondern „weniger als 2" (also 0 oder 1).
> 
> - Gegenereignis von „mindestens $k$" ist „weniger als $k$" (also 0 bis $k-1$)
> - Gegenereignis von „höchstens $k$" ist „mehr als $k$" (also $k+1, k+2, ...$)

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[03-Ereignisse|Ereignisse]] – Grundlagen der Mengenlehre bei Ereignissen
- → [[06-Wahrscheinlichkeiten-berechnen|Wahrscheinlichkeiten berechnen]] – Allgemeine Rechenregeln
- → [[09-Pfadregeln|Pfadregeln]] – Kombination mit Baumdiagrammen
- → [[10-Unabhaengige-Ereignisse|Unabhängige Ereignisse]] – Warum wir bei „3× würfeln" multiplizieren dürfen

---

**Navigation:** [[06-Wahrscheinlichkeiten-berechnen|← Berechnung]] | [[08-Baumdiagramme|Baumdiagramme →]]
