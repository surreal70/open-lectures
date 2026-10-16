---
title: Laplace-Experimente
chapter: "14"
section: "14.5"
type: lecture
created: 2026-10-13
modified: 2025-01-20
status: draft - review pending
tags:
  - mathematik/wahrscheinlichkeit
  - laplace
---

# Laplace-Experimente

## Einführung

> [!info] **Lernziele**
> Nach dieser Lektion können Sie:
> - Laplace-Experimente erkennen
> - Die Laplace-Formel anwenden

---

## Überblick

Die einfachste und wichtigste Methode zur Berechnung von Wahrscheinlichkeiten geht auf den französischen Mathematiker Pierre-Simon Laplace (1749–1827) zurück. Seine Idee war so simpel wie genial: Wenn alle Ergebnisse gleich wahrscheinlich sind, dann ist die Wahrscheinlichkeit eines Ereignisses einfach das Verhältnis der günstigen zu den möglichen Ergebnissen.

Laplace formulierte diese Idee in seinem berühmten Werk „Théorie analytique des probabilités" (1812). Obwohl die Wahrscheinlichkeitsrechnung schon über 150 Jahre alt war, brachte Laplace sie erstmals in eine systematische Form und machte sie zu einem mächtigen Werkzeug für Wissenschaft und Alltag.

---

## Definition

> [!note] **Definition**
> Ein **Laplace-Experiment** ist ein Zufallsexperiment, bei dem alle Ergebnisse **gleich wahrscheinlich** sind.

### Beispiele für Laplace-Experimente

| Experiment | Ergebnisse | Warum gleich wahrscheinlich? |
|------------|------------|------------------------------|
| Fairer Würfel | 1, 2, 3, 4, 5, 6 | Symmetrischer Körper |
| Faire Münze | Kopf, Zahl | Symmetrische Form |
| Gut gemischte Karten | Jede Karte | Zufällige Anordnung |
| Lostrommel | Jedes Los | Zufällige Auswahl |

### Gegenbeispiele (keine Laplace-Experimente)

- **Gezinkter Würfel:** Manche Zahlen erscheinen häufiger
- **Reißzwecke werfen:** „Auf der Spitze" vs. „auf dem Kopf" nicht gleich wahrscheinlich
- **Wetter morgen:** „Regen" und „kein Regen" nicht gleich wahrscheinlich

---

## Laplace-Formel

> [!note] **Formel**
> $$P(E) = \frac{\text{Anzahl günstiger Ergebnisse}}{\text{Anzahl möglicher Ergebnisse}} = \frac{|E|}{|Ω|}$$

### Anwendungsschritte

1. Prüfen, ob ein Laplace-Experiment vorliegt (alle Ergebnisse gleich wahrscheinlich?)
2. Ergebnismenge Ω bestimmen und Anzahl |Ω| zählen
3. Günstige Ergebnisse für das Ereignis E sammeln und Anzahl |E| zählen
4. Formel anwenden: $P(E) = \frac{|E|}{|Ω|}$

> [!tip] **Merkregel: „Günstig durch möglich"**
> Die Laplace-Formel lässt sich leicht merken:
> - Zähler: Wie viele Ergebnisse sind „günstig" (führen zum gewünschten Ereignis)?
> - Nenner: Wie viele Ergebnisse sind insgesamt möglich?

---

## Beispiele

> [!example] **Würfel: Gerade Zahl**
> Ereignis E = „gerade Zahl" = {2, 4, 6}
> 
> $P(\text{gerade}) = \frac{|\{2,4,6\}|}{|\{1,2,3,4,5,6\}|} = \frac{3}{6} = \frac{1}{2} = 50\%$

> [!example] **Kartenspiel (32 Karten)**
> - P(Herz-Ass) = $\frac{1}{32}$ (nur eine Karte ist das Herz-Ass)
> - P(Ass) = $\frac{4}{32} = \frac{1}{8}$ (vier Asse: Herz, Karo, Pik, Kreuz)
> - P(Herz) = $\frac{8}{32} = \frac{1}{4}$ (acht Herz-Karten)

> [!example] **Zweimal Würfeln: Summe 7**
> Ergebnismenge: Alle Paare (1. Wurf, 2. Wurf) → |Ω| = 36
> 
> Günstige Ergebnisse für Summe 7:
> (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) → |E| = 6
> 
> $P(\text{Summe 7}) = \frac{6}{36} = \frac{1}{6} \approx 16{,}7\%$

---

## Wann ist die Laplace-Formel anwendbar?

> [!warning] **Häufiger Fehler**
> Die Laplace-Formel darf **nur** angewendet werden, wenn alle Ergebnisse gleich wahrscheinlich sind!
> 
> **Falsch:** „Morgen regnet es oder nicht, also P(Regen) = ½"
> 
> Zwei Möglichkeiten bedeuten nicht automatisch gleiche Wahrscheinlichkeiten. Das Wetter ist kein Laplace-Experiment.

### Checkliste für Laplace-Experimente

Vor Anwendung der Formel fragen:
- [ ] Sind die Ergebnisse symmetrisch? (Würfel, Münze)
- [ ] Wird zufällig und fair ausgewählt? (Lostrommel, gemischte Karten)
- [ ] Gibt es keine Bevorzugung einzelner Ergebnisse?

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[02-Ergebnismengen|Ergebnismengen]] – Die Menge Ω, deren Größe wir für den Nenner brauchen
- → [[03-Ereignisse|Ereignisse]] – Die Teilmenge E, deren Größe wir für den Zähler brauchen
- → [[06-Wahrscheinlichkeiten-berechnen|Wahrscheinlichkeiten berechnen]] – Weitere Berechnungsmethoden
- → [[11-Kombinatorik|Kombinatorik]] – Hilfsmittel zum Abzählen von |E| und |Ω|

---

**Navigation:** [[04-Haeufigkeit-und-Wahrscheinlichkeit|← Häufigkeit]] | [[06-Wahrscheinlichkeiten-berechnen|Berechnung →]]
