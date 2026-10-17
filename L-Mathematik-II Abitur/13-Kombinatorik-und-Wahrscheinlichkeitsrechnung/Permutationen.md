---
author: Andreas Hümmer
title: Permutationen
tags:
  - content
  - mathe
  - kombinatorik
  - permutation
  - anordnung
created: 2025-07-01
modified: 2025-07-01
---

# Permutationen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Begriff Permutation verstehen und erklären können
> - Permutationen ohne und mit Wiederholung berechnen können
> - Praktische Probleme als Permutationsprobleme erkennen
> - Zirkuläre Permutationen (Kreisanordnungen) bestimmen können

---

## Überblick

Eine Permutation ist eine Anordnung von Objekten in einer bestimmten Reihenfolge. Der Begriff stammt vom lateinischen „permutare" (vertauschen). Permutationen spielen eine zentrale Rolle in der Kombinatorik und bilden die Grundlage für viele Berechnungen in der Wahrscheinlichkeitsrechnung.

## Permutationen ohne Wiederholung

### Definition

Eine **Permutation ohne Wiederholung** ist eine Anordnung von $n$ verschiedenen Objekten, bei der jedes Objekt genau einmal vorkommt.

Die Anzahl aller Permutationen von $n$ verschiedenen Objekten ist:

$$P_n = n!$$

### Herleitung

Bei der Anordnung von $n$ verschiedenen Objekten:
- Für die 1. Position gibt es $n$ Möglichkeiten
- Für die 2. Position gibt es $n-1$ Möglichkeiten
- ...
- Für die $n$-te Position gibt es 1 Möglichkeit

Nach der Produktregel: $n \cdot (n-1) \cdot \ldots \cdot 2 \cdot 1 = n!$

### Beispiel: Anordnung von Buchstaben

Wie viele verschiedene „Wörter" kann man aus den Buchstaben A, B, C, D bilden?

**Lösung:**
$$P_4 = 4! = 24$$

Die 24 Anordnungen sind:
```
ABCD  ABDC  ACBD  ACDB  ADBC  ADCB
BACD  BADC  BCAD  BCDA  BDAC  BDCA
CABD  CADB  CBAD  CBDA  CDAB  CDBA
DABC  DACB  DBAC  DBCA  DCAB  DCBA
```

## Permutationen mit Wiederholung

### Definition

Eine **Permutation mit Wiederholung** liegt vor, wenn unter den $n$ Objekten mehrere gleiche sind.

Gibt es $n$ Objekte, von denen:
- $k_1$ Objekte vom Typ 1 sind
- $k_2$ Objekte vom Typ 2 sind
- ...
- $k_r$ Objekte vom Typ $r$ sind

mit $k_1 + k_2 + \ldots + k_r = n$, dann ist die Anzahl der verschiedenen Anordnungen:

$$P_n^{k_1, k_2, \ldots, k_r} = \frac{n!}{k_1! \cdot k_2! \cdot \ldots \cdot k_r!}$$

### Herleitung

Wären alle $n$ Objekte verschieden, gäbe es $n!$ Anordnungen. Da aber je $k_i$ Objekte ununterscheidbar sind, werden die Anordnungen, die sich nur durch Vertauschung gleicher Objekte unterscheiden, mehrfach gezählt. Division durch $k_i!$ korrigiert diese Mehrfachzählung.

### Beispiel: Wort MISSISSIPPI

Wie viele verschiedene Anordnungen der Buchstaben des Wortes MISSISSIPPI gibt es?

**Analyse:**
- Gesamtzahl der Buchstaben: $n = 11$
- M: 1-mal ($k_1 = 1$)
- I: 4-mal ($k_2 = 4$)
- S: 4-mal ($k_3 = 4$)
- P: 2-mal ($k_4 = 2$)

**Lösung:**
$$P_{11}^{1,4,4,2} = \frac{11!}{1! \cdot 4! \cdot 4! \cdot 2!} = \frac{39916800}{1 \cdot 24 \cdot 24 \cdot 2} = \frac{39916800}{1152} = 34650$$

### Beispiel: Binärfolgen

Wie viele verschiedene Binärfolgen der Länge 8 mit genau drei Einsen gibt es?

**Lösung:**
$$P_8^{3,5} = \frac{8!}{3! \cdot 5!} = \frac{40320}{6 \cdot 120} = \frac{40320}{720} = 56$$

## Zirkuläre Permutationen (Kreisanordnungen)

### Definition

Bei einer **zirkulären Permutation** werden $n$ Objekte im Kreis angeordnet. Dabei gelten Anordnungen als gleich, wenn sie durch Drehung ineinander überführt werden können.

Die Anzahl der verschiedenen Kreisanordnungen von $n$ verschiedenen Objekten ist:

$$Z_n = (n-1)!$$

### Herleitung

Von den $n!$ linearen Anordnungen entsprechen jeweils $n$ Stück derselben Kreisanordnung (durch $n$ verschiedene Drehungen). Also:
$$Z_n = \frac{n!}{n} = (n-1)!$$

### Beispiel: Runder Tisch

Auf wie viele Arten können sich 6 Personen an einem runden Tisch setzen?

**Lösung:**
$$Z_6 = (6-1)! = 5! = 120$$

### Anmerkung: Unterscheidung der Seiten

Wenn bei einer Kreisanordnung auch die Unterscheidung zwischen „linker" und „rechter Nachbar" wegfällt (z.B. bei Perlen auf einem Armband), halbiert sich die Anzahl nochmals:
$$\frac{(n-1)!}{2}$$

## Übersicht der Permutationsformeln

| Typ | Beschreibung | Formel |
|-----|--------------|--------|
| Ohne Wiederholung | $n$ verschiedene Objekte anordnen | $n!$ |
| Mit Wiederholung | $n$ Objekte mit Gruppen $k_1, \ldots, k_r$ | $\frac{n!}{k_1! \cdot \ldots \cdot k_r!}$ |
| Zirkulär | $n$ Objekte im Kreis | $(n-1)!$ |

## Anwendungsbeispiele

### Beispiel 1: Wartezeiten

In einer Arztpraxis warten 5 Patienten. In wie vielen Reihenfolgen können sie aufgerufen werden?

**Lösung:** $5! = 120$ verschiedene Reihenfolgen

### Beispiel 2: Geheimcode

Ein Tresor hat einen 4-stelligen Code aus den Ziffern 1, 1, 2, 3. Wie viele verschiedene Codes sind möglich?

**Lösung:**
$$P_4^{2,1,1} = \frac{4!}{2! \cdot 1! \cdot 1!} = \frac{24}{2} = 12$$

### Beispiel 3: Sportmannschaften

Ein Trainer muss 8 Spieler in einer bestimmten Reihenfolge zum Elfmeterschießen aufstellen. Wie viele Möglichkeiten gibt es?

**Lösung:** $8! = 40320$ verschiedene Reihenfolgen

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Fakultaeten]] — Mathematische Grundlage für Permutationen
- → [[Variationen]] — Wenn nicht alle Objekte angeordnet werden
- → [[Kombinationen]] — Wenn die Reihenfolge nicht zählt
- → [[Binomialkoeffizienten]] — Permutationen mit Wiederholung als Binomialkoeffizienten

> [!warning] **Prüfungsrelevant**
> - Unterscheidung: Mit oder ohne Wiederholung?
> - Die Formel für Permutationen mit Wiederholung sicher anwenden
> - Kreisanordnungen richtig erkennen und berechnen
> - Systematisches Abzählen bei kleinen Zahlen zur Kontrolle

> [!question] **Typische Prüfungsfragen**
> - Wie viele verschiedene Anordnungen gibt es für die Buchstaben des Wortes BANANE?
> - Auf wie viele Arten können 4 Ehepaare an einem runden Tisch sitzen, wenn jedes Ehepaar nebeneinander sitzt?
> - Wie viele verschiedene Wege gibt es von A nach B in einem Gitter (als Permutationsproblem)?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3, Springer Vieweg, 2016
- Bronstein, I.N. et al.: Taschenbuch der Mathematik, Verlag Europa-Lehrmittel, 2020
- Kemnitz, A.: Mathematik zum Studienbeginn, Springer, 2014

> [!tip] **Weiterführende Links**
> - [[Variationen]] — Auswahl mit Reihenfolge
> - [[Kombinationen]] — Auswahl ohne Reihenfolge
