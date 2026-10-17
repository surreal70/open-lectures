---
author: Andreas Hümmer
title: Kombinationen
tags:
  - content
  - mathe
  - kombinatorik
  - kombination
  - auswahl
created: 2025-07-01
modified: 2025-07-01
---

# Kombinationen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Unterschied zwischen Kombination und Variation verstehen
> - Kombinationen ohne und mit Wiederholung berechnen können
> - Den Zusammenhang zwischen Kombinationen und Binomialkoeffizienten kennen
> - Praktische Probleme als Kombinationsprobleme erkennen

---

## Überblick

Eine Kombination ist eine ungeordnete Auswahl von $k$ Objekten aus einer Menge von $n$ Objekten. Im Gegensatz zur Variation spielt bei Kombinationen die Reihenfolge keine Rolle – es zählt nur, welche Objekte ausgewählt wurden, nicht in welcher Reihenfolge. Kombinationen sind eines der wichtigsten Werkzeuge in der Wahrscheinlichkeitsrechnung.

## Kombinationen ohne Wiederholung

### Definition

Eine **Kombination ohne Wiederholung** ist eine ungeordnete Auswahl von $k$ Objekten aus $n$ verschiedenen Objekten, wobei jedes Objekt höchstens einmal ausgewählt werden kann.

Die Anzahl der Kombinationen ohne Wiederholung ist:

$$C_n^k = \binom{n}{k} = \frac{n!}{k! \cdot (n-k)!}$$

### Herleitung

Die Anzahl der geordneten Auswahlen (Variationen) von $k$ aus $n$ Objekten ist $\frac{n!}{(n-k)!}$.

Da bei Kombinationen die Reihenfolge egal ist, entsprechen je $k!$ verschiedene Variationen derselben Kombination (die $k$ ausgewählten Objekte können auf $k!$ Arten angeordnet werden).

Also:
$$C_n^k = \frac{V_n^k}{k!} = \frac{n!}{(n-k)! \cdot k!} = \binom{n}{k}$$

### Beispiel: Lottozahlen

Beim deutschen Lotto werden 6 aus 49 Zahlen gezogen. Wie viele verschiedene Tipps gibt es?

**Lösung:**
$$\binom{49}{6} = \frac{49!}{6! \cdot 43!} = \frac{49 \cdot 48 \cdot 47 \cdot 46 \cdot 45 \cdot 44}{6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1} = 13.983.816$$

### Beispiel: Handkarten

Aus einem Skatblatt mit 32 Karten erhält ein Spieler 10 Karten. Wie viele verschiedene Blätter sind möglich?

**Lösung:**
$$\binom{32}{10} = \frac{32!}{10! \cdot 22!} = 64.512.240$$

## Kombinationen mit Wiederholung

### Definition

Eine **Kombination mit Wiederholung** ist eine ungeordnete Auswahl von $k$ Objekten aus $n$ verschiedenen Objekten, wobei jedes Objekt beliebig oft ausgewählt werden kann.

Die Anzahl der Kombinationen mit Wiederholung ist:

$$C_n^{k,W} = \binom{n+k-1}{k} = \frac{(n+k-1)!}{k! \cdot (n-1)!}$$

### Herleitung (Sterne-und-Balken-Methode)

Man kann die Auswahl als Verteilungsproblem darstellen: $k$ identische Objekte (Sterne) werden auf $n$ Kategorien verteilt, getrennt durch $n-1$ Trennstriche (Balken).

Die Gesamtzahl der Symbole ist $k + (n-1) = n + k - 1$.
Davon müssen $k$ Positionen für Sterne gewählt werden:
$$\binom{n+k-1}{k}$$

### Beispiel: Obstkauf

In einem Laden gibt es 4 Obstsorten (Äpfel, Birnen, Kirschen, Orangen). Du möchtest 7 Früchte kaufen. Wie viele verschiedene Zusammenstellungen gibt es?

**Lösung:**
$$\binom{4+7-1}{7} = \binom{10}{7} = \frac{10!}{7! \cdot 3!} = 120$$

### Beispiel: Würfelsummen

Auf wie viele Arten kann man mit 3 ununterscheidbaren Würfeln eine Augensumme erreichen? (Hier fragen wir nach der Anzahl verschiedener „Würfelbilder".)

**Lösung:**
$$\binom{6+3-1}{3} = \binom{8}{3} = 56$$

## Übersicht der Kombinationsformeln

| Typ | Formel | Beispiel |
|-----|--------|----------|
| Ohne Wiederholung | $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ | Lotto: 6 aus 49 |
| Mit Wiederholung | $\binom{n+k-1}{k}$ | 7 Früchte aus 4 Sorten |

## Vergleich: Variation vs. Kombination

| | Variation | Kombination |
|---|-----------|-------------|
| Reihenfolge | wichtig | egal |
| Ohne Wdh. | $\frac{n!}{(n-k)!}$ | $\binom{n}{k}$ |
| Mit Wdh. | $n^k$ | $\binom{n+k-1}{k}$ |
| Beispiel (ohne Wdh.) | Podiumsplätze | Lotterie |
| Beispiel (mit Wdh.) | PIN-Code | Obstauswahl |

### Zusammenhang

$$\binom{n}{k} = \frac{V_n^k}{k!}$$

Die Kombination ist die Variation geteilt durch die Anzahl der möglichen Anordnungen.

## Praktische Anwendungen

### Beispiel 1: Arbeitsgruppe bilden

Aus einer Klasse mit 25 Schülern soll eine Arbeitsgruppe mit 4 Mitgliedern gebildet werden. Wie viele Möglichkeiten gibt es?

**Analyse:** 
- Auswahl von 4 aus 25
- Reihenfolge egal (alle sind gleichberechtigte Mitglieder)
- Ohne Wiederholung

**Lösung:**
$$\binom{25}{4} = \frac{25!}{4! \cdot 21!} = \frac{25 \cdot 24 \cdot 23 \cdot 22}{24} = 12650$$

### Beispiel 2: Multiple-Choice-Test

Bei einem Test mit 20 Fragen sollen 5 Fragen ausgewählt werden, die der Lehrer besonders genau korrigiert. Wie viele Auswahlmöglichkeiten gibt es?

**Lösung:**
$$\binom{20}{5} = \frac{20!}{5! \cdot 15!} = 15504$$

### Beispiel 3: Händeschütteln

Bei einem Treffen von 12 Personen begrüßt jede Person jede andere mit Handschlag. Wie viele Handschläge finden statt?

**Analyse:** Ein Handschlag ist eine ungeordnete Auswahl von 2 Personen aus 12.

**Lösung:**
$$\binom{12}{2} = \frac{12!}{2! \cdot 10!} = \frac{12 \cdot 11}{2} = 66$$

### Beispiel 4: Eiskugeln wählen

Eine Eisdiele hat 8 Sorten. Du bestellst 3 Kugeln und darfst Sorten wiederholen. Wie viele verschiedene Bestellungen gibt es?

**Lösung:**
$$\binom{8+3-1}{3} = \binom{10}{3} = 120$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Binomialkoeffizienten]] — Mathematische Eigenschaften von $\binom{n}{k}$
- → [[Variationen]] — Geordnete Auswahl
- → [[Fakultaeten]] — Grundlage der Berechnungen
- → [[Bernoulli-Ketten]] — Kombinationen in Wahrscheinlichkeitsberechnungen

> [!warning] **Prüfungsrelevant**
> - Erkennen, ob die Reihenfolge relevant ist (Variation oder Kombination?)
> - Die Formel $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ sicher anwenden
> - Kombinationen mit Wiederholung: $\binom{n+k-1}{k}$
> - Typische Anwendungen: Lotto, Gruppenbildung, Verteilungsprobleme

> [!question] **Typische Prüfungsfragen**
> - Auf wie viele Arten kann man aus 10 Büchern 3 für eine Reise auswählen?
> - Bei einer Prüfung müssen 4 von 8 Aufgaben bearbeitet werden. Wie viele Kombinationen gibt es?
> - Eine Firma hat 15 Bewerber und 4 Stellen. Auf wie viele Arten können die Stellen besetzt werden, wenn alle Stellen gleichwertig sind?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3, Springer Vieweg, 2016
- Bronstein, I.N. et al.: Taschenbuch der Mathematik, Verlag Europa-Lehrmittel, 2020
- Tietze, J.: Einführung in die angewandte Wirtschaftsmathematik, Springer, 2019

> [!tip] **Weiterführende Links**
> - [[Binomialkoeffizienten]] — Vertiefung der mathematischen Eigenschaften
> - [[Wiederholung-der-Wahrscheinlichkeitsrechnung]] — Anwendung in Wahrscheinlichkeiten
