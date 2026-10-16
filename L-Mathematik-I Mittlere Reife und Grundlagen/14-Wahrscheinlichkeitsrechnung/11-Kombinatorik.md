---
title: Einfache kombinatorische Aufgaben
chapter: "14"
section: "14.11"
type: lecture
created: 2026-10-13
modified: 2025-01-20
status: draft - review pending
tags:
  - mathematik/wahrscheinlichkeit
  - kombinatorik
---

# Einfache kombinatorische Aufgaben

## Einführung

> [!info] **Lernziele**
> Nach dieser Lektion können Sie:
> - Die Fakultät berechnen
> - Anordnungsprobleme lösen
> - Auswahlprobleme unterscheiden

---

## Überblick

Die Kombinatorik ist die Kunst des systematischen Zählens. Sie beantwortet Fragen wie: „Auf wie viele Arten kann ich fünf Bücher in ein Regal stellen?" oder „Wie viele verschiedene Sechser-Kombinationen gibt es beim Lotto?" 

Diese Zählprobleme sind eng mit der Wahrscheinlichkeitsrechnung verbunden: Um die Laplace-Formel $P(E) = \frac{|E|}{|\Omega|}$ anzuwenden, müssen wir oft |E| und |Ω| berechnen – und genau das leistet die Kombinatorik.

Die Kombinatorik hat eine lange Geschichte. Schon im 12. Jahrhundert beschäftigten sich indische Mathematiker mit Anordnungsproblemen. Im 17. Jahrhundert entwickelten Blaise Pascal und Pierre de Fermat die Grundlagen der modernen Kombinatorik im Zusammenhang mit Glücksspielen.

---

## Fakultät

> [!note] **Definition**
> $$n! = n \cdot (n-1) \cdot (n-2) \cdot \ldots \cdot 2 \cdot 1$$
> Sprich: „n Fakultät"

Die Fakultät gibt an, auf wie viele Arten man $n$ verschiedene Objekte anordnen kann.

### Werte der Fakultät

| n | n! | Berechnung |
|---|-----|------------|
| 0 | 1 | Per Definition |
| 1 | 1 | 1 |
| 2 | 2 | 2 × 1 |
| 3 | 6 | 3 × 2 × 1 |
| 4 | 24 | 4 × 3 × 2 × 1 |
| 5 | 120 | 5 × 4 × 3 × 2 × 1 |
| 6 | 720 | 6! |
| 10 | 3.628.800 | 10! |

> [!tip] **Warum ist 0! = 1?**
> Diese Definition erscheint zunächst seltsam, macht aber mathematisch Sinn: Es gibt genau eine Möglichkeit, null Objekte anzuordnen – nämlich „gar nichts tun". Außerdem funktionieren so viele Formeln der Kombinatorik konsistent.

### Schnelles Wachstum

Die Fakultät wächst extrem schnell:
- 10! ≈ 3,6 Millionen
- 15! ≈ 1,3 Billionen
- 20! ≈ 2,4 Trillionen

> [!warning] **Häufiger Fehler**
> Die Fakultät wird oft unterschätzt. Bei 52 Karten gibt es 52! ≈ 8 × 10⁶⁷ verschiedene Reihenfolgen – mehr als es Atome im beobachtbaren Universum gibt!

---

## Anordnungen (Permutationen)

Bei einer **Permutation** werden alle Objekte angeordnet – die Reihenfolge zählt.

$n$ verschiedene Objekte anordnen: **$n!$ Möglichkeiten**

> [!example] **4 Personen auf 4 Stühle**
> - 1. Stuhl: 4 Möglichkeiten (jede der 4 Personen)
> - 2. Stuhl: 3 Möglichkeiten (die verbliebenen 3)
> - 3. Stuhl: 2 Möglichkeiten
> - 4. Stuhl: 1 Möglichkeit (die letzte Person)
> 
> Gesamt: $4! = 4 \cdot 3 \cdot 2 \cdot 1 = 24$ Möglichkeiten

### Anschauliche Erklärung

Stellen Sie sich vor, Sie vergeben Plätze nacheinander:
- Für den ersten Platz haben Sie volle Auswahl (n Möglichkeiten)
- Für den zweiten Platz ist eine Person schon vergeben (n-1)
- Und so weiter...

---

## Auswahl (Kombination vs. Variation)

Bei Auswahlproblemen wird nur ein Teil der Objekte ausgewählt. Die entscheidende Frage ist: **Spielt die Reihenfolge eine Rolle?**

| Typ | Reihenfolge | Formel | Beispiel |
|-----|-------------|--------|----------|
| **Variation** | wichtig | $\frac{n!}{(n-k)!}$ | PIN-Code, Platzierung |
| **Kombination** | unwichtig | $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ | Lotto, Team auswählen |

### Mit Reihenfolge (Variation)

„Wie viele Möglichkeiten gibt es, aus n Objekten k auszuwählen, wenn die Reihenfolge zählt?"

> [!example] **Podiumsplätze: 3 von 10 Läufern**
> Gold, Silber, Bronze sind verschieden! (1., 2., 3. Platz)
> 
> $10 \cdot 9 \cdot 8 = 720$ Möglichkeiten

### Ohne Reihenfolge (Kombination)

„Wie viele Möglichkeiten gibt es, aus n Objekten k auszuwählen, wenn die Reihenfolge egal ist?"

> [!example] **Team auswählen: 3 aus 5 Personen**
> **Mit Reihenfolge:** $5 \cdot 4 \cdot 3 = 60$ (als würden wir Plätze vergeben)
> 
> **Ohne Reihenfolge:** Jede 3er-Gruppe wurde 3! = 6-mal gezählt (alle Reihenfolgen)
> 
> Also: $\frac{60}{3!} = \frac{60}{6} = 10$ Teams

> [!tip] **Merkregel: Wann ist Reihenfolge wichtig?**
> - **Wichtig:** Wenn verschiedene Positionen/Plätze vergeben werden (1. Platz, 2. Platz, ... oder verschiedene Aufgaben)
> - **Unwichtig:** Wenn nur eine Gruppe/Menge gebildet wird (Lotto: 6 Richtige, egal in welcher Reihenfolge gezogen)

---

## Lotto als Anwendung

> [!example] **Lotto „6 aus 49"**
> Wie viele Kombinationen gibt es?
> 
> - Reihenfolge ist egal (nur die 6 Zahlen zählen, nicht wann sie gezogen wurden)
> - Also eine Kombination: $\binom{49}{6}$
> 
> $$\binom{49}{6} = \frac{49!}{6! \cdot 43!} = \frac{49 \cdot 48 \cdot 47 \cdot 46 \cdot 45 \cdot 44}{6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1} = 13.983.816$$
> 
> Die Wahrscheinlichkeit für 6 Richtige:
> $P = \frac{1}{13.983.816} \approx 0{,}000007\% \approx 1:14$ Millionen

---

## Zusammenfassung: Welche Formel wann?

| Situation | Formel |
|-----------|--------|
| Alle n Objekte anordnen | $n!$ |
| k aus n auswählen, Reihenfolge wichtig | $\frac{n!}{(n-k)!}$ |
| k aus n auswählen, Reihenfolge egal | $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ |

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[05-Laplace-Experimente|Laplace-Experimente]] – Kombinatorik liefert |E| und |Ω|
- → [[02-Ergebnismengen|Ergebnismengen]] – Die Mächtigkeit |Ω| bestimmen
- → [[12-Praktische-Zufallsexperimente|Praktische Zufallsexperimente]] – Anwendung auf Lotto, Urnen etc.
- → [[../06-Potenzen-Wurzeln-und-Zahlendarstellung/01-Potenzschreibweise|Potenzschreibweise]] – Für Formeln wie $k^n$

---

**Navigation:** [[10-Unabhaengige-Ereignisse|← Unabhängigkeit]] | [[12-Praktische-Zufallsexperimente|Praxis →]]
