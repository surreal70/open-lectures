---
author: Andreas Hümmer
title: Variationen
tags:
  - content
  - mathe
  - kombinatorik
  - variation
  - auswahl
created: 2025-07-01
modified: 2025-07-01
---

# Variationen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Unterschied zwischen Variation und Permutation verstehen
> - Variationen ohne und mit Wiederholung berechnen können
> - Praktische Probleme als Variationsprobleme erkennen
> - Die richtige Formel je nach Problemtyp auswählen können

---

## Überblick

Eine Variation ist eine geordnete Auswahl von $k$ Objekten aus einer Menge von $n$ Objekten. Im Gegensatz zur Permutation werden bei der Variation nicht alle Objekte verwendet, sondern nur eine Teilmenge. Der wesentliche Unterschied zur Kombination ist, dass bei Variationen die Reihenfolge der Auswahl eine Rolle spielt.

## Variationen ohne Wiederholung

### Definition

Eine **Variation ohne Wiederholung** ist eine geordnete Auswahl von $k$ Objekten aus $n$ verschiedenen Objekten, wobei jedes Objekt höchstens einmal ausgewählt werden kann.

Die Anzahl der Variationen ohne Wiederholung ist:

$$V_n^k = \frac{n!}{(n-k)!} = n \cdot (n-1) \cdot (n-2) \cdot \ldots \cdot (n-k+1)$$

### Herleitung

Bei der geordneten Auswahl von $k$ aus $n$ Objekten:
- Für die 1. Position gibt es $n$ Möglichkeiten
- Für die 2. Position gibt es $n-1$ Möglichkeiten
- ...
- Für die $k$-te Position gibt es $n-k+1$ Möglichkeiten

Nach der Produktregel:
$$V_n^k = n \cdot (n-1) \cdot \ldots \cdot (n-k+1) = \frac{n!}{(n-k)!}$$

### Beispiel: Medaillengewinner

Bei einem Wettkampf mit 10 Teilnehmern sollen Gold, Silber und Bronze vergeben werden. Auf wie viele Arten können die Medaillen verteilt werden?

**Lösung:**
$$V_{10}^3 = \frac{10!}{7!} = 10 \cdot 9 \cdot 8 = 720$$

### Beispiel: PIN-Code

Ein PIN-Code besteht aus 4 verschiedenen Ziffern (0-9). Wie viele verschiedene PINs gibt es?

**Lösung:**
$$V_{10}^4 = \frac{10!}{6!} = 10 \cdot 9 \cdot 8 \cdot 7 = 5040$$

## Variationen mit Wiederholung

### Definition

Eine **Variation mit Wiederholung** ist eine geordnete Auswahl von $k$ Objekten aus $n$ verschiedenen Objekten, wobei jedes Objekt mehrfach ausgewählt werden kann.

Die Anzahl der Variationen mit Wiederholung ist:

$$V_n^{k,W} = n^k$$

### Herleitung

Bei der geordneten Auswahl mit Zurücklegen:
- Für jede der $k$ Positionen gibt es $n$ Möglichkeiten
- Die Auswahlen sind unabhängig voneinander

Nach der Produktregel:
$$V_n^{k,W} = \underbrace{n \cdot n \cdot \ldots \cdot n}_{k \text{ Faktoren}} = n^k$$

### Beispiel: Zahlenschloss

Ein Zahlenschloss hat 4 Ringe mit je 10 Ziffern (0-9). Wie viele verschiedene Kombinationen gibt es?

**Lösung:**
$$V_{10}^{4,W} = 10^4 = 10000$$

### Beispiel: Binärcode

Wie viele verschiedene 8-Bit-Binärzahlen gibt es?

**Lösung:**
$$V_2^{8,W} = 2^8 = 256$$

## Übersicht und Vergleich

| Auswahltyp | Mit Reihenfolge | Ohne Wiederholung | Mit Wiederholung |
|------------|-----------------|-------------------|------------------|
| Alle $n$ Objekte | Permutation | $n!$ | $\frac{n!}{k_1! \cdot \ldots \cdot k_r!}$ |
| $k$ aus $n$ Objekten | Variation | $\frac{n!}{(n-k)!}$ | $n^k$ |

### Entscheidungsbaum zur Formelwahl

```
Ist die Reihenfolge wichtig?
├── JA (Variation/Permutation)
│   └── Werden alle n Objekte verwendet?
│       ├── JA → Permutation: n!
│       └── NEIN → Variation
│           └── Darf ein Objekt mehrfach vorkommen?
│               ├── NEIN → V = n!/(n-k)!
│               └── JA → V = n^k
└── NEIN (Kombination)
    └── → siehe Kombinationen
```

## Anwendungsbeispiele

### Beispiel 1: Autorennnummern

Bei einem Autorennen mit 20 Startern sollen die Startnummern 1, 2 und 3 vergeben werden. Auf wie viele Arten ist das möglich?

**Analyse:** 
- 20 Fahrer zur Auswahl
- 3 Startnummern werden vergeben
- Reihenfolge wichtig (Nummer 1 ≠ Nummer 2)
- Ohne Wiederholung (ein Fahrer kann nur eine Nummer haben)

**Lösung:**
$$V_{20}^3 = 20 \cdot 19 \cdot 18 = 6840$$

### Beispiel 2: Passwort aus Buchstaben

Ein Passwort besteht aus 3 Großbuchstaben (A-Z). Wie viele verschiedene Passwörter gibt es, wenn Buchstaben wiederholt werden dürfen?

**Lösung:**
$$V_{26}^{3,W} = 26^3 = 17576$$

### Beispiel 3: Telefonnummern

Wie viele verschiedene 7-stellige Telefonnummern gibt es (mit führenden Nullen)?

**Lösung:**
$$V_{10}^{7,W} = 10^7 = 10.000.000$$

### Beispiel 4: Podiumsplätze

Bei einer Meisterschaft mit 15 Mannschaften: Auf wie viele Arten können die Plätze 1 bis 5 belegt werden?

**Lösung:**
$$V_{15}^5 = 15 \cdot 14 \cdot 13 \cdot 12 \cdot 11 = 360360$$

## Spezialfall: Variation = Permutation

Wenn $k = n$ ist, also alle Objekte ausgewählt werden, gilt:

$$V_n^n = \frac{n!}{(n-n)!} = \frac{n!}{0!} = \frac{n!}{1} = n!$$

Die Variation aller $n$ Elemente entspricht der Permutation – beide Begriffe beschreiben dann dasselbe.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Fakultaeten]] — Grundlage für die Variationsformel ohne Wiederholung
- → [[Permutationen]] — Spezialfall der Variation mit $k = n$
- → [[Kombinationen]] — Auswahl ohne Beachtung der Reihenfolge
- → [[Binomialkoeffizienten]] — Verhältnis zwischen Variation und Kombination

> [!warning] **Prüfungsrelevant**
> - Unterscheidung: Mit oder ohne Wiederholung?
> - Unterscheidung: Ist die Reihenfolge relevant?
> - Die Formel $n^k$ für Variationen mit Wiederholung
> - Korrekte Anwendung von $\frac{n!}{(n-k)!}$

> [!question] **Typische Prüfungsfragen**
> - Wie viele verschiedene dreistellige Zahlen kann man aus den Ziffern 1, 2, 3, 4, 5 bilden, wenn keine Ziffer mehrfach vorkommen darf?
> - Ein Schloss hat 5 Ringe mit je 6 Symbolen. Wie viele Einstellungen sind möglich?
> - Auf wie viele Arten können aus 12 Schülern ein Klassensprecher und ein Stellvertreter gewählt werden?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3, Springer Vieweg, 2016
- Bronstein, I.N. et al.: Taschenbuch der Mathematik, Verlag Europa-Lehrmittel, 2020
- Kemnitz, A.: Mathematik zum Studienbeginn, Springer, 2014

> [!tip] **Weiterführende Links**
> - [[Kombinationen]] — Wenn die Reihenfolge nicht zählt
> - [[Baumdiagramme]] — Visualisierung von Auswahlprozessen
