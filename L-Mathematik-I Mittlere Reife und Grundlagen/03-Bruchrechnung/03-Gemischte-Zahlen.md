---
author: Andreas Hümmer
title: Gemischte Zahlen
status: draft - review pending
tags:
  - content
  - mathematik
  - bruchrechnung
created: 2026-10-13
modified: 2026-10-16
---

# Gemischte Zahlen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Gemischte Zahlen lesen und schreiben können
> - Gemischte Zahlen in unechte Brüche umwandeln können
> - Unechte Brüche in gemischte Zahlen umwandeln können

---

## Überblick

Eine **gemischte Zahl** besteht aus einem ganzzahligen Anteil und einem echten Bruch. Sie ist eine alternative Darstellung für unechte Brüche und wird oft im Alltag verwendet (z.B. „anderthalb Liter" = $1\frac{1}{2}$ Liter).

Im täglichen Leben begegnen uns gemischte Zahlen ständig: Wenn jemand sagt „Ich bin eineinhalb Stunden gelaufen", meint er $1\frac{1}{2}$ Stunden. Rezepte verlangen oft „zweieinhalb Tassen Mehl" ($2\frac{1}{2}$). Auch Maße wie „drei und drei Viertel Meter" ($3\frac{3}{4}$ m) sind typische Beispiele.

Mathematisch gesehen sind gemischte Zahlen und unechte Brüche vollkommen gleichwertig – sie beschreiben dieselbe Menge. Die gemischte Zahl ist jedoch **leichter zu lesen und zu verstehen**, während der unechte Bruch sich **besser zum Rechnen** eignet.

---

## Definition

$$\text{Gemischte Zahl} = \text{Ganze Zahl} + \text{echter Bruch}$$

$$a\frac{b}{c} = a + \frac{b}{c}$$

**Beispiel:** $2\frac{3}{4} = 2 + \frac{3}{4}$

> [!note] **Wichtig: Das versteckte Pluszeichen**
> Bei gemischten Zahlen steht zwischen der ganzen Zahl und dem Bruch ein **unsichtbares Plus**:
> 
> $2\frac{3}{4}$ bedeutet $2 + \frac{3}{4}$, nicht $2 \cdot \frac{3}{4}$!
>
> Im Englischen schreibt man manchmal $2 + \frac{3}{4}$ oder $2\ \frac{3}{4}$ (mit Leerzeichen), um Verwechslungen zu vermeiden.

---

## Umwandlungen

### Gemischte Zahl → Unechter Bruch

$$a\frac{b}{c} = \frac{a \cdot c + b}{c}$$

> [!note] **Warum funktioniert diese Formel?**
> Wir zerlegen die gemischte Zahl in ihre Teile:
> - $a$ ganze Einheiten = $a \cdot c$ Bruchteile (jede Einheit hat $c$ Teile)
> - Plus die $b$ zusätzlichen Bruchteile
> - Alles zusammen: $\frac{a \cdot c + b}{c}$

**Beispiel:** $3\frac{2}{5}$

$$= \frac{3 \cdot 5 + 2}{5} = \frac{15 + 2}{5} = \frac{17}{5}$$

**Schritt für Schritt gedacht:**
- 3 Ganze = 3 × 5 Fünftel = 15 Fünftel
- Plus 2 Fünftel = 17 Fünftel

| Gemischte Zahl | Rechnung | Unechter Bruch |
|----------------|----------|----------------|
| $2\frac{1}{3}$ | $\frac{2 \cdot 3 + 1}{3}$ | $\frac{7}{3}$ |
| $4\frac{3}{4}$ | $\frac{4 \cdot 4 + 3}{4}$ | $\frac{19}{4}$ |
| $1\frac{1}{2}$ | $\frac{1 \cdot 2 + 1}{2}$ | $\frac{3}{2}$ |

> [!tip] **Merkregel: „Nenner mal Ganze plus Zähler"**
> Um schnell umzuwandeln: Multipliziere den Nenner mit der ganzen Zahl und addiere den Zähler. Das Ergebnis ist der neue Zähler, der Nenner bleibt gleich.
>
> Bei $3\frac{2}{5}$: Nenner (5) mal Ganze (3) = 15, plus Zähler (2) = 17 → $\frac{17}{5}$

### Unechter Bruch → Gemischte Zahl

Division mit Rest (siehe voriges Kapitel):

$$\frac{17}{5} = 17 : 5 = 3 \text{ Rest } 2 = 3\frac{2}{5}$$

> [!warning] **Häufiger Fehler**
> Beim Umwandeln von gemischten Zahlen wird oft falsch multipliziert:
>
> **Falsch:** $2\frac{3}{4} = \frac{2 \cdot 3}{4} = \frac{6}{4}$ ✗
>
> **Richtig:** $2\frac{3}{4} = \frac{2 \cdot 4 + 3}{4} = \frac{11}{4}$ ✓
>
> Der Nenner wird mit der ganzen Zahl multipliziert, nicht der Zähler!

---

## Visualisierung

$2\frac{1}{4}$:

![[gemischte-zahl.png]]
*<span class="fig-id">01-03-03-gemischte-zahl</span>: Die gemischte Zahl 2¼ – zwei ganze Einheiten plus ein Viertel: 1 + 1 + ¼ = 2¼.*

Die Visualisierung zeigt klar: Eine gemischte Zahl besteht aus vollständigen Einheiten plus einem Bruchteil. Bei $2\frac{1}{4}$ haben wir zwei ganze Rechtecke und zusätzlich noch ein Viertel eines dritten.

---

## Rechenhinweise

> [!tip] **Beim Rechnen**
> Für Rechnungen mit gemischten Zahlen ist es oft einfacher, sie zuerst in unechte Brüche umzuwandeln:
>
> $2\frac{1}{2} + 1\frac{3}{4} = \frac{5}{2} + \frac{7}{4} = \frac{10}{4} + \frac{7}{4} = \frac{17}{4} = 4\frac{1}{4}$

### Warum unechte Brüche beim Rechnen?

Mit gemischten Zahlen direkt zu rechnen ist fehleranfällig, besonders bei Multiplikation und Division:

**Beispiel Multiplikation:**
- $2\frac{1}{2} \cdot 3$ ≠ $(2 \cdot 3)\frac{1}{2}$ ← Falsch!
- Richtig: $\frac{5}{2} \cdot 3 = \frac{15}{2} = 7\frac{1}{2}$

**Strategie:** Immer erst in unechte Brüche umwandeln, dann rechnen, am Ende wieder in gemischte Zahl umwandeln.

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[02-Echte-und-unechte-Brueche|Echte und unechte Brüche]] – Wann ist ein Bruch unecht?
- → [[07-Addition-von-Bruechen|Addition von Brüchen]] – Gemischte Zahlen addieren
- → [[09-Multiplikation-von-Bruechen|Multiplikation von Brüchen]] – Mit gemischten Zahlen multiplizieren

> [!warning] **Prüfungsrelevant**
> - Gemischte Zahl = Ganzzahl + echter Bruch
> - Umwandlung: $a\frac{b}{c} = \frac{a \cdot c + b}{c}$
> - Zum Rechnen meist in unechte Brüche umwandeln

> [!question] **Typische Prüfungsfragen**
> - Wandle $5\frac{2}{3}$ in einen unechten Bruch um.
> - Wandle $\frac{23}{6}$ in eine gemischte Zahl um.

## Quellen

- Padberg, Friedhelm: *Didaktik der Bruchrechnung*. Springer, 2009.
