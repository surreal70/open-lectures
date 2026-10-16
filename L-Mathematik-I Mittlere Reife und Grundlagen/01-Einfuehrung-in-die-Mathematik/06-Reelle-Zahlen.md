---
author: Open Lectures
title: Reelle Zahlen – eine erste Einführung
status: draft - review pending
tags:
  - content
  - mathematik
  - zahlenmengen
  - reelle-zahlen
created: 2026-10-13
modified: 2026-10-13
---

# Reelle Zahlen – eine erste Einführung

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Menge der reellen Zahlen $\mathbb{R}$ kennen
> - Den Unterschied zwischen rationalen und irrationalen Zahlen verstehen
> - Beispiele für irrationale Zahlen nennen können
> - Verstehen, warum $\mathbb{R}$ den Zahlenstrahl „vollständig" füllt

---

## Überblick

Die reellen Zahlen umfassen alle Zahlen, die auf dem Zahlenstrahl liegen. Sie entstehen durch die Erweiterung der rationalen Zahlen um die **irrationalen Zahlen** – Zahlen, die sich nicht als Bruch darstellen lassen. Damit wird der Zahlenstrahl „lückenlos" gefüllt.

---

## Definition der reellen Zahlen

Die **reellen Zahlen** $\mathbb{R}$ umfassen alle Zahlen auf dem Zahlenstrahl:

$$\mathbb{R} = \mathbb{Q} \cup \text{(irrationale Zahlen)}$$

Sie setzen sich zusammen aus:
- **Rationale Zahlen** $\mathbb{Q}$: Alle Brüche (abbrechende oder periodische Dezimalzahlen)
- **Irrationale Zahlen**: Nicht-abbrechende, nicht-periodische Dezimalzahlen

---

## Die Zahlenmengenhierarchie

```
┌─────────────────────────────────────────────────────────┐
│                    Reelle Zahlen ℝ                      │
│  ┌───────────────────────────────────────────────────┐  │
│  │              Rationale Zahlen ℚ                   │  │
│  │  ┌─────────────────────────────────────────────┐  │  │
│  │  │            Ganze Zahlen ℤ                   │  │  │
│  │  │  ┌───────────────────────────────────────┐  │  │  │
│  │  │  │       Natürliche Zahlen ℕ             │  │  │  │
│  │  │  │       1, 2, 3, 4, ...                 │  │  │  │
│  │  │  └───────────────────────────────────────┘  │  │  │
│  │  │  ..., -2, -1, 0, 1, 2, ...                  │  │  │
│  │  └─────────────────────────────────────────────┘  │  │
│  │  ..., -½, ⅓, 0,75, ...                           │  │
│  └───────────────────────────────────────────────────┘  │
│  √2, π, e, ...  (irrationale Zahlen)                    │
└─────────────────────────────────────────────────────────┘
```

$$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$$

---

## Irrationale Zahlen

**Irrationale Zahlen** sind reelle Zahlen, die sich **nicht** als Bruch zweier ganzer Zahlen darstellen lassen.

### Eigenschaften irrationaler Zahlen

- Ihre Dezimaldarstellung bricht **nicht ab**
- Ihre Dezimaldarstellung ist **nicht periodisch**
- Sie können nicht als $\frac{p}{q}$ mit $p, q \in \mathbb{Z}$ geschrieben werden

### Berühmte irrationale Zahlen

| Zahl | Symbol | Ungefährer Wert | Bedeutung |
|------|--------|-----------------|-----------|
| Wurzel aus 2 | $\sqrt{2}$ | $1{,}41421356...$ | Diagonale im Einheitsquadrat |
| Kreiszahl | $\pi$ | $3{,}14159265...$ | Verhältnis Umfang/Durchmesser |
| Eulersche Zahl | $e$ | $2{,}71828182...$ | Basis des natürlichen Logarithmus |
| Goldener Schnitt | $\varphi$ | $1{,}61803398...$ | $\frac{1+\sqrt{5}}{2}$ |

---

## Beweis: $\sqrt{2}$ ist irrational

Der klassische Beweis durch Widerspruch:

> [!example] **Beweis (Widerspruchsbeweis)**
> **Annahme:** $\sqrt{2}$ ist rational, also $\sqrt{2} = \frac{p}{q}$ mit $p, q \in \mathbb{Z}$, $q \neq 0$, und $\frac{p}{q}$ vollständig gekürzt.
>
> **Umformung:**
> $$\sqrt{2} = \frac{p}{q} \implies 2 = \frac{p^2}{q^2} \implies p^2 = 2q^2$$
>
> Also ist $p^2$ gerade, damit auch $p$ gerade: $p = 2k$
>
> Einsetzen: $(2k)^2 = 2q^2 \implies 4k^2 = 2q^2 \implies q^2 = 2k^2$
>
> Also ist auch $q^2$ gerade, damit $q$ gerade.
>
> **Widerspruch:** $p$ und $q$ sind beide gerade, aber der Bruch sollte gekürzt sein!
>
> **Fazit:** Die Annahme war falsch. $\sqrt{2}$ ist irrational.

---

## Wo begegnen uns irrationale Zahlen?

### In der Geometrie

| Figur | Irrationale Länge |
|-------|-------------------|
| Einheitsquadrat | Diagonale: $\sqrt{2}$ |
| Gleichseitiges Dreieck (Seite 2) | Höhe: $\sqrt{3}$ |
| Kreis (Durchmesser 1) | Umfang: $\pi$ |
| Goldenes Rechteck | Seitenverhältnis: $\varphi$ |

### In der Natur

- **Spiralen**: Schneckenhäuser, Galaxien (goldener Schnitt)
- **Kreise**: Räder, Planeten, Wellen ($\pi$)
- **Wachstum**: Exponentielles Wachstum ($e$)

---

## Vollständigkeit der reellen Zahlen

Ein wichtiger Unterschied zu $\mathbb{Q}$:

> [!note] **Vollständigkeit**
> Die reellen Zahlen „füllen" den Zahlenstrahl lückenlos aus.
> 
> In $\mathbb{Q}$ gibt es „Lücken": Die Stelle $\sqrt{2}$ auf dem Zahlenstrahl wird von keiner rationalen Zahl getroffen.
>
> In $\mathbb{R}$ gibt es keine Lücken: Jeder Punkt auf dem Zahlenstrahl entspricht genau einer reellen Zahl.

### Visualisierung

```
Zahlenstrahl:
←────────┼────────┼────────┼────────┼────────┼────────→
         0        1       √2       2        3

         ↑                 ↑
    Rationale          Irrationale
      Zahl                Zahl
    (in ℚ und ℝ)        (nur in ℝ)
```

---

## Intervallschreibweise

Für Teilmengen von $\mathbb{R}$ verwendet man **Intervalle**:

| Notation | Bedeutung | Beispiel |
|----------|-----------|----------|
| $[a, b]$ | Alle $x$ mit $a \leq x \leq b$ | $[0, 1] = \{x \in \mathbb{R} \mid 0 \leq x \leq 1\}$ |
| $(a, b)$ | Alle $x$ mit $a < x < b$ | $(0, 1)$ enthält nicht 0 und 1 |
| $[a, b)$ | Alle $x$ mit $a \leq x < b$ | Halb-offen rechts |
| $(a, b]$ | Alle $x$ mit $a < x \leq b$ | Halb-offen links |
| $[a, \infty)$ | Alle $x$ mit $x \geq a$ | $[0, \infty)$ = nicht-negative Zahlen |

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[05-Rationale-Zahlen|Rationale Zahlen]] – Die Grundlage: $\mathbb{Q} \subset \mathbb{R}$
- → [[07-Zahlenstrahl-und-Zahlenmengen|Zahlenstrahl und Zahlenmengen]] – Visualisierung aller Mengen
- → [[02-Mathematische-Symbole|Mathematische Symbole]] – Intervallnotation

> [!warning] **Prüfungsrelevant**
> - $\mathbb{R} = \mathbb{Q} \cup$ (irrationale Zahlen)
> - Irrationale Zahlen: nicht-abbrechend, nicht-periodisch
> - Beispiele: $\sqrt{2}$, $\pi$, $e$
> - $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$
> - $\mathbb{R}$ ist vollständig (keine Lücken im Zahlenstrahl)

> [!question] **Typische Prüfungsfragen**
> - Ist $\sqrt{9}$ rational oder irrational? Begründe.
> - Nenne drei irrationale Zahlen.
> - Was bedeutet es, dass $\mathbb{R}$ „vollständig" ist?
> - Ordne die Zahlenmengen: $\mathbb{Q}$, $\mathbb{N}$, $\mathbb{R}$, $\mathbb{Z}$

## Quellen

- Heuser, Harro: *Lehrbuch der Analysis, Teil 1*. Teubner, 2009.
- Beutelspacher, Albrecht: *Zahlen*. Rowohlt, 2013.

> [!tip] **Weiterführende Links**
> - [Mathebibel: Reelle Zahlen](https://www.mathebibel.de/reelle-zahlen)
> - [[07-Zahlenstrahl-und-Zahlenmengen|Nächstes Kapitel: Zahlenstrahl und Zahlenmengen]]
