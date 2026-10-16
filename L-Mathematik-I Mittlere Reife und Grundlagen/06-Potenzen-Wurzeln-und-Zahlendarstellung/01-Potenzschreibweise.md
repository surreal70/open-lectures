---
title: "Potenzschreibweise"
chapter: "06"
section: "01"
type: topic
status: "draft - review pending"
learning_objectives:
  - "Die Potenzschreibweise als Kurzform verstehen"
  - "Basis und Exponent unterscheiden"
  - "Potenzen richtig lesen und schreiben"
  - "Einfache Potenzen berechnen"
tags:
  - mathematik
  - potenzen
  - basis
  - exponent
created: 2026-10-13
modified: 2025-06-26
---

# Potenzschreibweise

> [!info] Lernziele
> - Die Potenzschreibweise als Kurzform verstehen
> - Basis und Exponent unterscheiden
> - Potenzen richtig lesen und schreiben
> - Einfache Potenzen berechnen

## Überblick

Die **Potenzschreibweise** ist eine Kurzform für wiederholte Multiplikation derselben Zahl mit sich selbst.

Stell dir vor, du möchtest die Zahl $2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2$ aufschreiben – das wäre mühsam und fehleranfällig. Wie oft steht die 2 dort? Zählen kostet Zeit. Mit der Potenzschreibweise wird daraus elegant $2^{10}$ – sofort lesbar und unmissverständlich.

Die moderne Potenzschreibweise verdanken wir dem französischen Philosophen und Mathematiker **René Descartes** (1596–1650). In seiner *Géométrie* von 1637 verwendete er erstmals konsequent hochgestellte Zahlen als Exponenten. Zuvor hatten Mathematiker umständliche Abkürzungen benutzt: $aa$ für $a^2$ oder $aaa$ für $a^3$. Descartes' elegante Notation setzte sich schnell durch und ist bis heute Standard.

Im Alltag begegnen uns Potenzen ständig, oft ohne dass wir es bemerken: Die Fläche eines Zimmers in Quadratmetern ($m^2$), das Volumen eines Aquariums in Kubikzentimetern ($cm^3$) oder die Speicherkapazität eines USB-Sticks (oft $2^{30}$ Bytes = 1 Gigabyte). Auch in der Informatik sind Zweierpotenzen allgegenwärtig, weil Computer im Binärsystem arbeiten.

## Definition

> [!tip] Definition
> Eine **Potenz** besteht aus:
> $$a^n = \underbrace{a \cdot a \cdot a \cdot ... \cdot a}_{n \text{ Faktoren}}$$
> 
> - **a** = Basis (Grundzahl)
> - **n** = Exponent (Hochzahl)

## Begriffe

```
    ┌─ Exponent (Hochzahl)
    │
   2³ = 8
   │    │
   │    └─ Potenzwert
   └─ Basis (Grundzahl)
```

## Sprechweisen

| Potenz | Sprechweise |
|--------|-------------|
| 3² | "drei hoch zwei" oder "drei Quadrat" |
| 5³ | "fünf hoch drei" oder "fünf Kubik" |
| 2⁴ | "zwei hoch vier" |
| aⁿ | "a hoch n" |

## Wichtige Potenzwerte

### Quadratzahlen (n²)

| n | n² |
|---|-----|
| 1 | 1 |
| 2 | 4 |
| 3 | 9 |
| 4 | 16 |
| 5 | 25 |
| 6 | 36 |
| 7 | 49 |
| 8 | 64 |
| 9 | 81 |
| 10 | 100 |

### Kubikzahlen (n³)

| n | n³ |
|---|-----|
| 1 | 1 |
| 2 | 8 |
| 3 | 27 |
| 4 | 64 |
| 5 | 125 |

### Zweierpotenzen

| 2ⁿ | Wert |
|----|------|
| 2¹ | 2 |
| 2² | 4 |
| 2³ | 8 |
| 2⁴ | 16 |
| 2⁵ | 32 |
| 2⁶ | 64 |
| 2⁷ | 128 |
| 2⁸ | 256 |
| 2¹⁰ | 1024 |

> [!tip] **Zweierpotenzen in der Informatik**
> Die Zweierpotenzen sind in der digitalen Welt allgegenwärtig, weil Computer im **Binärsystem** (Basis 2) arbeiten:
> - $2^{10} = 1024 \approx 1000$ → 1 Kilobyte (KB)
> - $2^{20} = 1.048.576 \approx 1$ Million → 1 Megabyte (MB)
> - $2^{30} \approx 1$ Milliarde → 1 Gigabyte (GB)
> 
> Darum hat ein „1-GB-USB-Stick" genau 1.073.741.824 Bytes – nicht exakt eine Milliarde.

## Sonderfälle

| Potenz | Wert | Erklärung |
|--------|------|-----------|
| a¹ | a | Einmal die Basis |
| a⁰ | 1 | Per Definition (a ≠ 0) |
| 0ⁿ | 0 | Null hoch beliebig (n > 0) |
| 1ⁿ | 1 | Eins hoch beliebig |

> [!tip] **Warum ist $a^0 = 1$?**
> Diese Definition erscheint zunächst willkürlich, ergibt aber aus den Potenzgesetzen Sinn: Wenn wir $a^3 : a^3 = a^{3-3} = a^0$ berechnen, muss das Ergebnis 1 sein, denn jede Zahl geteilt durch sich selbst ergibt 1. Daher **muss** $a^0 = 1$ sein, damit die Potenzgesetze konsistent bleiben.

> [!warning] **Häufiger Fehler**
> Viele verwechseln $a^0 = 1$ mit $0^a = 0$. Das sind zwei völlig verschiedene Situationen:
> - **Exponent ist 0:** $5^0 = 1$, $(-3)^0 = 1$, $\pi^0 = 1$ – immer 1!
> - **Basis ist 0:** $0^5 = 0$, $0^{100} = 0$ – immer 0 (für positive Exponenten)
> 
> Der Sonderfall $0^0$ ist mathematisch nicht eindeutig definiert und wird kontextabhängig behandelt.

## Zusammenhänge

### Voraussetzungen

- [[02-Grundrechenarten-und-Rechengesetze/00-Grundrechenarten-Index|Grundrechenarten]]

### Weiterführende Themen

- → [[02-Potenzen-mit-natuerlichen-Exponenten]] – Berechnung und Vorzeichen bei Potenzen
- → [[03-Potenzgesetze]] – Die wichtigen Rechenregeln für Potenzen
- → [[06-Quadratwurzeln]] – Die Umkehroperation der Potenz

## Prüfungsrelevanz

> [!warning] Prüfungsrelevanz: Sehr hoch
> Quadratzahlen bis 15² sollten auswendig bekannt sein.

## Typische Prüfungsfragen

1. Berechne: 4³, 2⁵, 3⁴
2. Schreibe als Potenz: 7 · 7 · 7 · 7
3. Was ist 5⁰? Was ist 10¹?

## Quellen

- Lambacher Schweizer Mathematik 8

## Weiterführende Links

- [[02-Potenzen-mit-natuerlichen-Exponenten]]
- [[03-Potenzgesetze]]
