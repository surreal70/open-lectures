---
title: Zufallsexperimente
chapter: "14"
section: "14.1"
type: lecture
created: 2026-10-13
modified: 2025-01-20
status: draft - review pending
tags:
  - mathematik/wahrscheinlichkeit
  - zufallsexperiment
---

# Zufallsexperimente

## Einführung

> [!info] **Lernziele**
> Nach dieser Lektion können Sie:
> - Zufallsexperimente erkennen und beschreiben
> - Zwischen ein- und mehrstufigen Experimenten unterscheiden

---

## Überblick

Der Zufall begegnet uns täglich: beim Wetter, beim Würfelspiel, bei der Frage, ob der Bus pünktlich kommt. Lange Zeit galt der Zufall als etwas, das sich der Mathematik entzieht – wie sollte man etwas Unvorhersehbares berechnen? Diese Sichtweise änderte sich im 17. Jahrhundert, als Mathematiker erkannten, dass der Zufall zwar im Einzelfall unberechenbar ist, aber in der Masse durchaus Gesetzmäßigkeiten folgt.

Der Ausgangspunkt für jede wahrscheinlichkeitstheoretische Überlegung ist das **Zufallsexperiment**. Es beschreibt den Vorgang, dessen Ausgang wir untersuchen möchten. Ein präzises Verständnis dieses Begriffs ist entscheidend für alles Weitere.

---

## Definition

> [!note] **Definition**
> Ein **Zufallsexperiment** ist ein Vorgang, der:
> - unter gleichen Bedingungen beliebig oft wiederholbar ist
> - mehrere mögliche Ergebnisse hat
> - dessen Ausgang nicht vorhersagbar ist

### Erläuterung der drei Bedingungen

**1. Wiederholbarkeit:** Wir müssen das Experiment (zumindest gedanklich) beliebig oft durchführen können. Ein Würfelwurf lässt sich millionenfach wiederholen, immer unter denselben Bedingungen.

**2. Mehrere Ergebnisse:** Es muss mindestens zwei verschiedene Ausgänge geben. Beim Würfeln sind es sechs, beim Münzwurf zwei.

**3. Unvorhersagbarkeit:** Wir können vor der Durchführung nicht mit Sicherheit sagen, welches Ergebnis eintreten wird. Dies unterscheidet Zufallsexperimente von deterministischen Vorgängen wie dem Berechnen einer Summe.

---

## Beispiele

| Zufallsexperiment | Kein Zufallsexperiment |
|-------------------|------------------------|
| Würfeln | Wasser kochen (Ergebnis vorhersagbar) |
| Münze werfen | Tag nach Montag bestimmen |
| Lotto spielen | 2 + 3 berechnen |
| Karte ziehen | Sonnenaufgang morgen früh |

> [!tip] **Erkennungsmerkmal**
> Fragen Sie sich: „Könnte das Ergebnis auch anders ausfallen, selbst wenn ich alles genau gleich mache?" Wenn ja, handelt es sich um ein Zufallsexperiment.

### Alltagsbeispiele für Zufallsexperimente

- **Glücksspiele:** Roulette, Lotto, Kartenspiele
- **Wetter:** Wird es morgen regnen?
- **Qualitätskontrolle:** Ist ein zufällig gezogenes Produkt fehlerfrei?
- **Medizin:** Wirkt ein Medikament bei einem bestimmten Patienten?
- **Verkehr:** Welche Ampelphase zeigt die nächste Kreuzung?

---

## Einstufig vs. Mehrstufig

Zufallsexperimente können aus einer oder mehreren Stufen bestehen:

- **Einstufig:** Einmal würfeln, eine Karte ziehen
- **Mehrstufig:** Zweimal würfeln, dreimal Münze werfen, erst würfeln und dann eine Karte ziehen

Bei **mehrstufigen Experimenten** führen wir mehrere Zufallsexperimente nacheinander durch. Die Gesamtzahl der möglichen Ergebnisse wächst dabei schnell an – ein wichtiger Aspekt, den wir später mit Baumdiagrammen übersichtlich darstellen werden.

> [!example] **Beispiel: Zweimal Münze werfen**
> - 1. Stufe: Kopf oder Zahl (2 Möglichkeiten)
> - 2. Stufe: Wieder Kopf oder Zahl (2 Möglichkeiten)
> - Gesamt: $2 \times 2 = 4$ mögliche Ergebnisse (KK, KZ, ZK, ZZ)

---

## Historischer Hintergrund

Die mathematische Untersuchung von Zufallsexperimenten begann im Jahr 1654 mit einem Briefwechsel zwischen Blaise Pascal und Pierre de Fermat. Der Anlass war eine Frage des Chevalier de Méré, eines leidenschaftlichen Spielers: Wie teilt man den Einsatz gerecht auf, wenn ein Würfelspiel vorzeitig abgebrochen werden muss?

Diese scheinbar einfache Frage führte zur Entwicklung der gesamten Wahrscheinlichkeitstheorie. Pascal und Fermat erkannten, dass man auch über zukünftige, unsichere Ereignisse mathematisch fundierte Aussagen treffen kann – nicht über den Einzelfall, aber über die Verteilung bei vielen Wiederholungen.

> [!warning] **Häufiger Fehler**
> Verwechseln Sie nicht „unvorhersagbar" mit „ohne Muster". Obwohl wir das einzelne Ergebnis nicht vorhersagen können, folgen die Häufigkeiten bei vielen Wiederholungen festen Gesetzmäßigkeiten. Ein fairer Würfel zeigt auf lange Sicht jede Zahl etwa gleich oft.

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[02-Ergebnismengen|Ergebnismengen]] – Wie man alle möglichen Ergebnisse systematisch erfasst
- → [[04-Haeufigkeit-und-Wahrscheinlichkeit|Häufigkeit und Wahrscheinlichkeit]] – Der Zusammenhang zwischen beobachteten Häufigkeiten und theoretischen Wahrscheinlichkeiten
- → [[08-Baumdiagramme|Baumdiagramme]] – Visualisierung mehrstufiger Experimente

---

**Navigation:** [[00-Wahrscheinlichkeit-Index|← Übersicht]] | [[02-Ergebnismengen|Ergebnismengen →]]
