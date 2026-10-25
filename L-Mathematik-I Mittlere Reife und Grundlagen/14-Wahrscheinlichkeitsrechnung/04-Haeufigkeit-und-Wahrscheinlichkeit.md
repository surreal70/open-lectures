---
title: Absolute und relative Häufigkeit
chapter: "14"
section: "14.4"
type: lecture
created: 2026-10-13
modified: 2026-10-25
status: draft - review pending
tags:
  - mathematik/wahrscheinlichkeit
  - haeufigkeit
---

# Absolute und relative Häufigkeit

## Einführung

> [!info] **Lernziele**
> Nach dieser Lektion können Sie:
> - Den Zusammenhang zwischen Häufigkeit und Wahrscheinlichkeit erklären
> - Das Gesetz der großen Zahlen verstehen

---

## Überblick

Wie kommt man eigentlich auf Wahrscheinlichkeiten? Eine Möglichkeit ist die Beobachtung: Wenn wir ein Experiment oft genug wiederholen und zählen, wie häufig ein bestimmtes Ereignis eintritt, können wir daraus auf die Wahrscheinlichkeit schließen. Dieser Ansatz verbindet die beobachtbare Welt mit der mathematischen Theorie.

Historisch war dies der erste Zugang zur Wahrscheinlichkeit. Schon im 17. Jahrhundert erkannten Mathematiker, dass Glücksspiele bei vielen Wiederholungen vorhersagbare Muster zeigen. Jakob Bernoulli (1654–1705) formulierte daraus das „Gesetz der großen Zahlen" – eines der fundamentalen Prinzipien der Wahrscheinlichkeitstheorie.

---

## Definitionen

> [!note] **Formeln**
> **Absolute Häufigkeit:** $H_n(E)$ = Anzahl, wie oft E eintritt (bei $n$ Durchführungen)
> 
> **Relative Häufigkeit:** $h_n(E) = \frac{H_n(E)}{n}$

### Erläuterung

Die **absolute Häufigkeit** zählt einfach, wie oft ein Ereignis eingetreten ist. Wenn Sie 100-mal würfeln und 18-mal eine Sechs erhalten, ist $H_{100}(\text{Sechs}) = 18$.

Die **relative Häufigkeit** setzt diese Anzahl ins Verhältnis zur Gesamtzahl der Versuche. Im obigen Beispiel: $h_{100}(\text{Sechs}) = \frac{18}{100} = 0{,}18 = 18\%$.

> [!tip] **Merkregel**
> - Absolute Häufigkeit: „Wie oft?" → eine ganze Zahl
> - Relative Häufigkeit: „Welcher Anteil?" → eine Zahl zwischen 0 und 1 (oder in Prozent)

---

## Gesetz der großen Zahlen

> [!note] **Prinzip**
> Bei vielen Wiederholungen nähert sich die relative Häufigkeit der Wahrscheinlichkeit an:
> $$h_n(E) \approx P(E) \text{ für große } n$$

Dieses Gesetz erklärt, warum Wahrscheinlichkeiten überhaupt praktisch nützlich sind: Obwohl wir den Ausgang eines einzelnen Experiments nicht vorhersagen können, werden die Häufigkeiten bei vielen Wiederholungen vorhersagbar.

### Anschauliche Erklärung

Stellen Sie sich vor, Sie werfen eine faire Münze:
- Nach 10 Würfen könnte die relative Häufigkeit von „Kopf" bei 0,3 oder 0,7 liegen – große Abweichungen von 0,5 sind möglich.
- Nach 100 Würfen wird sie wahrscheinlich zwischen 0,4 und 0,6 liegen.
- Nach 10.000 Würfen liegt sie sehr wahrscheinlich zwischen 0,49 und 0,51.

Je mehr Versuche, desto stabiler wird die relative Häufigkeit – und desto näher kommt sie der theoretischen Wahrscheinlichkeit.

---

## Beispiel: Münzwurf

> [!example] **Experiment: Münzwurf**
> | Würfe (n) | Kopf $H_n$ | rel. Häufigkeit $h_n$ |
> |-----------|------------|----------------------|
> | 10 | 4 | 0,40 |
> | 100 | 48 | 0,48 |
> | 1000 | 503 | 0,503 |
> | 10000 | 4987 | 0,4987 |
> 
> → Annäherung an P(Kopf) = 0,5

![[grosse-zahlen.png]]
*<span class="fig-id">14-04-grosse-zahlen</span>: Gesetz der großen Zahlen – mit wachsender Anzahl Würfe nähert sich die relative Häufigkeit von „Kopf" dem Wert $P = 0{,}5$ an.*

Die Schwankungen werden immer kleiner, die relative Häufigkeit stabilisiert sich um den Wert 0,5.

---

## Praktische Bedeutung

Das Gesetz der großen Zahlen ist die Grundlage für viele praktische Anwendungen:

- **Versicherungen:** Können Prämien berechnen, weil sie wissen, wie oft Schäden bei vielen Kunden auftreten
- **Casinos:** Können langfristig Gewinne garantieren, auch wenn einzelne Spieler gewinnen
- **Qualitätskontrolle:** Können aus Stichproben auf die Qualität der gesamten Produktion schließen
- **Meinungsforschung:** Können aus Umfragen auf die Meinung der Gesamtbevölkerung schließen

> [!warning] **Häufiger Fehler: Der Spielerfehlschluss**
> Manche glauben: „Die Münze hat 5-mal Kopf gezeigt, jetzt muss Zahl kommen!"
> 
> Das ist **falsch**. Die Münze hat kein Gedächtnis. Jeder Wurf ist unabhängig, die Wahrscheinlichkeit für Kopf bleibt bei jedem Wurf 50%. Das Gesetz der großen Zahlen sagt nur, dass sich die Häufigkeiten *auf lange Sicht* ausgleichen – nicht, dass nach einer Serie von Köpfen nun Zahl „fällig" wäre.

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[../13-Statistik-und-Datenanalyse/04-Absolute-und-relative-Haeufigkeiten|Absolute und relative Häufigkeiten (Statistik)]] – Dieselben Konzepte in der beschreibenden Statistik
- → [[05-Laplace-Experimente|Laplace-Experimente]] – Theoretische Berechnung von Wahrscheinlichkeiten
- → [[10-Unabhaengige-Ereignisse|Unabhängige Ereignisse]] – Warum einzelne Würfe keinen Einfluss aufeinander haben

---

**Navigation:** [[03-Ereignisse|← Ereignisse]] | [[05-Laplace-Experimente|Laplace →]]
