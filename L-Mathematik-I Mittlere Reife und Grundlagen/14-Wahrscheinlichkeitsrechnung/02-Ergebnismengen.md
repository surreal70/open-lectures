---
title: Ergebnismengen
chapter: "14"
section: "14.2"
type: lecture
created: 2026-10-13
modified: 2025-01-20
status: draft - review pending
tags:
  - mathematik/wahrscheinlichkeit
  - ergebnismenge
---

# Ergebnismengen

## Einführung

> [!info] **Lernziele**
> Nach dieser Lektion können Sie:
> - Die Ergebnismenge eines Experiments angeben
> - Die Anzahl der Ergebnisse bestimmen

---

## Überblick

Bevor wir Wahrscheinlichkeiten berechnen können, müssen wir wissen, welche Ergebnisse überhaupt möglich sind. Die systematische Erfassung aller möglichen Ergebnisse ist der erste Schritt bei jeder Wahrscheinlichkeitsaufgabe. Diese Sammlung nennt man die **Ergebnismenge**.

Die korrekte Bestimmung der Ergebnismenge ist entscheidend: Vergessen wir ein Ergebnis oder zählen eines doppelt, werden alle weiteren Berechnungen falsch. Daher lohnt es sich, hier besonders sorgfältig vorzugehen.

---

## Definition

> [!note] **Definition**
> Die **Ergebnismenge Ω** (Omega) enthält alle möglichen Ergebnisse eines Zufallsexperiments.

Das griechische Symbol Ω (großes Omega) ist die internationale Standardbezeichnung für die Ergebnismenge. Die einzelnen Elemente von Ω heißen **Elementarereignisse** – sie sind die „Atome" der Wahrscheinlichkeitsrechnung, die nicht weiter zerlegbaren Grundbausteine.

---

## Beispiele

| Experiment | Ergebnismenge Ω | |Ω| |
|------------|-----------------|-----|
| Würfel | {1, 2, 3, 4, 5, 6} | 6 |
| Münze | {Kopf, Zahl} | 2 |
| Zweimal Münze | {KK, KZ, ZK, ZZ} | 4 |
| Ampel | {Rot, Gelb, Grün} | 3 |

> [!tip] **Systematisches Aufzählen**
> Bei komplexeren Experimenten hilft es, die Ergebnisse systematisch aufzulisten. Bei zweimal Münze werfen: Erst alle Möglichkeiten mit K als erstem Wurf (KK, KZ), dann alle mit Z (ZK, ZZ).

### Wichtig: Vollständigkeit und Überschneidungsfreiheit

Eine korrekte Ergebnismenge muss zwei Eigenschaften erfüllen:

1. **Vollständig:** Jedes mögliche Ergebnis des Experiments ist enthalten
2. **Überschneidungsfrei:** Kein Ergebnis kommt doppelt vor

> [!warning] **Häufiger Fehler**
> Beim zweimaligen Münzwurf werden oft nur drei Ergebnisse genannt: „beide Kopf", „beide Zahl", „einmal Kopf und einmal Zahl". Das ist falsch! KZ und ZK sind verschiedene Ergebnisse (die Reihenfolge ist unterschiedlich). Richtig sind vier Ergebnisse.

---

## Mehrstufige Experimente

Bei mehrstufigen Experimenten wächst die Ergebnismenge schnell an. Die Anzahl lässt sich mit einer einfachen Formel berechnen:

Bei $n$ Stufen mit je $k$ Ergebnissen:
$$|Ω| = k^n$$

Diese Formel gilt, wenn jede Stufe unabhängig von den vorherigen ist und immer gleich viele Möglichkeiten bietet.

> [!example] **Beispiele zur Formel**
> - Dreimal Münze werfen: $|Ω| = 2^3 = 8$
> - Zweimal würfeln: $|Ω| = 6^2 = 36$
> - Viermal Münze werfen: $|Ω| = 2^4 = 16$
> - PIN-Code (4 Ziffern): $|Ω| = 10^4 = 10.000$

### Visualisierung: Baumdiagramm

Bei mehrstufigen Experimenten hilft ein Baumdiagramm, alle Ergebnisse systematisch zu erfassen:

```
Zweimal Münze:
           Start
          /     \
        K         Z
       / \       / \
      K   Z     K   Z
      
Ergebnisse: KK  KZ  ZK  ZZ
```

Die Ergebnismenge liest man ab, indem man jeden Pfad vom Start bis zum Ende verfolgt.

---

## Praktische Anwendung

Die richtige Bestimmung der Ergebnismenge ist besonders wichtig bei:

- **Glücksspielen:** Wie viele Möglichkeiten gibt es beim Lotto?
- **Sicherheit:** Wie viele mögliche Passwörter gibt es?
- **Qualitätskontrolle:** Wie viele Stichproben-Kombinationen sind möglich?

> [!example] **Beispiel: Passwort-Sicherheit**
> Ein Passwort aus 4 Kleinbuchstaben (26 Möglichkeiten pro Stelle):
> $|Ω| = 26^4 = 456.976$ mögliche Passwörter
> 
> Mit Groß- und Kleinbuchstaben (52 Möglichkeiten):
> $|Ω| = 52^4 = 7.311.616$ – über 16-mal so viele!

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[01-Zufallsexperimente|Zufallsexperimente]] – Die Vorgänge, deren Ergebnisse wir sammeln
- → [[03-Ereignisse|Ereignisse]] – Teilmengen der Ergebnismenge
- → [[05-Laplace-Experimente|Laplace-Experimente]] – Wenn alle Ergebnisse gleich wahrscheinlich sind
- → [[11-Kombinatorik|Kombinatorik]] – Systematisches Zählen von Möglichkeiten

---

**Navigation:** [[01-Zufallsexperimente|← Zufallsexperimente]] | [[03-Ereignisse|Ereignisse →]]
