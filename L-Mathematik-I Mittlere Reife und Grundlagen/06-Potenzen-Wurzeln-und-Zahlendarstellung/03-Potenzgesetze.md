---
title: "Potenzgesetze"
chapter: "06"
section: "03"
type: topic
status: "draft - review pending"
learning_objectives:
  - "Die fünf Potenzgesetze kennen und anwenden"
  - "Potenzen mit gleicher Basis multiplizieren/dividieren"
  - "Potenzen potenzieren"
  - "Produkte und Quotienten potenzieren"
tags:
  - mathematik
  - potenzen
  - potenzgesetze
  - rechenregeln
created: 2026-10-13
modified: 2025-06-26
---

# Potenzgesetze

> [!info] Lernziele
> - Die fünf Potenzgesetze kennen und anwenden
> - Potenzen mit gleicher Basis multiplizieren/dividieren
> - Potenzen potenzieren
> - Produkte und Quotienten potenzieren

## Überblick

Die **Potenzgesetze** sind fundamentale Rechenregeln, die das Arbeiten mit Potenzen systematisch ermöglichen.

Diese Gesetze sind keine willkürlichen Vereinbarungen, sondern ergeben sich logisch aus der Definition der Potenz als wiederholte Multiplikation. Wenn man versteht, **warum** die Regeln so lauten, braucht man sie nicht auswendig zu lernen – man kann sie jederzeit selbst herleiten.

Die Potenzgesetze wurden im 17. Jahrhundert systematisiert, als die Algebra sich zu einer exakten Wissenschaft entwickelte. **John Wallis** (1616–1703) und später **Leonhard Euler** (1707–1783) erweiterten die Regeln auf gebrochene und negative Exponenten. Heute bilden die Potenzgesetze das Fundament für höhere Mathematik, Physik und Technik.

## Die fünf Potenzgesetze

### 1. Multiplikation (gleiche Basis)

$$a^m \cdot a^n = a^{m+n}$$

**Beispiel:** $2^3 \cdot 2^4 = 2^{3+4} = 2^7 = 128$

**Merkregel:** Gleiche Basis → Exponenten addieren

> [!tip] **Warum addiert man die Exponenten?**
> Schreibe die Potenzen aus:
> $$2^3 \cdot 2^4 = (2 \cdot 2 \cdot 2) \cdot (2 \cdot 2 \cdot 2 \cdot 2) = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 = 2^7$$
> Die Anzahl der Faktoren (Exponenten) addiert sich: $3 + 4 = 7$.

### 2. Division (gleiche Basis)

$$\frac{a^m}{a^n} = a^{m-n}$$

**Beispiel:** $\frac{5^6}{5^2} = 5^{6-2} = 5^4 = 625$

**Merkregel:** Gleiche Basis → Exponenten subtrahieren

### 3. Potenz einer Potenz

$$(a^m)^n = a^{m \cdot n}$$

**Beispiel:** $(3^2)^4 = 3^{2 \cdot 4} = 3^8 = 6561$

**Merkregel:** Exponenten multiplizieren

### 4. Potenz eines Produkts

$$(a \cdot b)^n = a^n \cdot b^n$$

**Beispiel:** $(2 \cdot 5)^3 = 2^3 \cdot 5^3 = 8 \cdot 125 = 1000$

### 5. Potenz eines Quotienten

$$\left(\frac{a}{b}\right)^n = \frac{a^n}{b^n}$$

**Beispiel:** $\left(\frac{3}{2}\right)^2 = \frac{3^2}{2^2} = \frac{9}{4}$

## Übersicht

| Gesetz | Formel | Beispiel |
|--------|--------|----------|
| Multiplikation | $a^m \cdot a^n = a^{m+n}$ | $x^3 \cdot x^5 = x^8$ |
| Division | $a^m : a^n = a^{m-n}$ | $x^7 : x^2 = x^5$ |
| Potenz von Potenz | $(a^m)^n = a^{m \cdot n}$ | $(x^3)^2 = x^6$ |
| Produkt | $(ab)^n = a^n b^n$ | $(2x)^3 = 8x^3$ |
| Quotient | $(a/b)^n = a^n/b^n$ | $(x/3)^2 = x^2/9$ |

## Häufige Fehler

> [!warning] **Häufiger Fehler: Die drei gefährlichsten Verwechslungen**

| Falsch | Richtig | Erklärung |
|--------|---------|-----------|
| $a^m \cdot a^n = a^{m \cdot n}$ | $a^m \cdot a^n = a^{m+n}$ | Exponenten werden **addiert**, nicht multipliziert! |
| $a^m + a^n = a^{m+n}$ | Nicht vereinfachbar! | Potenzgesetze gelten nur bei Multiplikation/Division |
| $(a + b)^2 = a^2 + b^2$ | $(a + b)^2 = a^2 + 2ab + b^2$ | Das ist die 1. binomische Formel! |

> [!tip] **Merkregel: Gleiche Basis prüfen**
> Die ersten beiden Potenzgesetze (Multiplikation und Division) funktionieren **nur bei gleicher Basis**:
> - $2^3 \cdot 2^5 = 2^8$ ✓ (gleiche Basis 2)
> - $2^3 \cdot 3^5 = ?$ ✗ (verschiedene Basen – nicht vereinfachbar!)
>
> Bei Gesetz 4 und 5 muss dagegen der **Exponent gleich** sein.

## Zusammenhänge

### Voraussetzungen

- [[01-Potenzschreibweise]]
- [[02-Potenzen-mit-natuerlichen-Exponenten]]

## Prüfungsrelevanz

> [!warning] Prüfungsrelevanz: Sehr hoch
> Die Potenzgesetze müssen sicher beherrscht werden!

## Typische Prüfungsfragen

1. Vereinfache: $x^4 \cdot x^3$
2. Berechne: $\frac{2^8}{2^5}$
3. Vereinfache: $(a^2)^5$
4. Vereinfache: $(3x)^2$

## Quellen

- Lambacher Schweizer Mathematik 8

## Weiterführende Links

- [[04-Potenzen-mit-negativen-Exponenten]]
- [[08-Wurzelgesetze]]
