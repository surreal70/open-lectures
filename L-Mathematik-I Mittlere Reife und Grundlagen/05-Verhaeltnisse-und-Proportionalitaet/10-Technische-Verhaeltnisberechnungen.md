---
title: "Technische Verhältnisberechnungen"
chapter: "05"
section: "10"
type: topic
status: "draft - review pending"
learning_objectives:
  - "Mischungsrechnungen durchführen"
  - "Übersetzungsverhältnisse bei Zahnrädern berechnen"
  - "Hebelgesetze anwenden"
  - "Technische Verhältnisse interpretieren"
tags:
  - mathematik
  - technik
  - mischung
  - uebersetzung
  - hebel
created: 2026-10-13
modified: 2026-10-16
---

# Technische Verhältnisberechnungen

> [!info] Lernziele
> - Mischungsrechnungen durchführen
> - Übersetzungsverhältnisse bei Zahnrädern berechnen
> - Hebelgesetze anwenden
> - Technische Verhältnisse interpretieren

## Überblick

Verhältnisse spielen in vielen technischen Anwendungen eine zentrale Rolle: bei Mischungen, Getrieben und Hebeln.

### Historischer Hintergrund

Die technische Anwendung von Verhältnissen reicht bis in die Antike zurück. **Archimedes** (ca. 287–212 v. Chr.) formulierte das **Hebelgesetz** und soll gesagt haben: „Gebt mir einen festen Punkt, und ich werde die Erde aus den Angeln heben." Damit beschrieb er die enorme Kraft, die durch geschickte Verhältnisse von Hebelarmen entsteht.

Die **Zahnradübersetzung** ist seit der Antike bekannt und wurde im **Antikythera-Mechanismus** (ca. 100 v. Chr.) – einem antiken griechischen Analogrechner – bereits in erstaunlicher Komplexität verwendet. Dieser Mechanismus enthielt über 30 Zahnräder und konnte astronomische Ereignisse vorhersagen.

### Technische Verhältnisse im Alltag

Wir begegnen diesen Verhältnissen täglich:

- **Fahrradschaltung**: Das Übersetzungsverhältnis zwischen Kettenblatt und Ritzel bestimmt, wie schwer oder leicht man treten muss
- **Automotor**: Das Getriebe wandelt die Motordrehzahl in verschiedene Geschwindigkeiten um
- **Schraubenzieher**: Ein Hebel – je länger der Griff, desto mehr Kraft übertragen wir
- **Farben mischen**: Verhältnis der Grundfarben bestimmt den Farbton
- **Cocktails**: Das Mischungsverhältnis macht den Unterschied zwischen gut und perfekt

## Mischungsrechnung

### Prinzip

Bei Mischungen bleibt die Gesamtmenge der Inhaltsstoffe erhalten.

> [!note] **Das Grundprinzip verstehen**
> Wenn du zwei Flüssigkeiten mischst, kann die Konzentration der Mischung nie höher sein als die höchste Einzelkonzentration und nie niedriger als die niedrigste. Die Mischung liegt immer „dazwischen" – gewichtet nach den Mengen.

### Beispiel

**Aufgabe:** 2 Liter 20%-ige Lösung mit 3 Liter 60%-iger mischen.

**Inhaltsstoff:**
- Lösung 1: 2 × 0,20 = 0,4 L
- Lösung 2: 3 × 0,60 = 1,8 L
- Gesamt: 2,2 L in 5 L

**Konzentration:** 2,2 ÷ 5 = 0,44 = **44%**

> [!tip] **Plausibilitätsprüfung bei Mischungen**
> Das Ergebnis (44%) muss zwischen den Ausgangskonzentrationen liegen (20% und 60%). ✓
> Außerdem: Da mehr von der stärkeren Lösung (3 L von 60%) verwendet wird, muss das Ergebnis näher an 60% als an 20% liegen. ✓

> [!warning] **Häufiger Fehler: Konzentrationen mitteln**
> **Falsch:** (20% + 60%) ÷ 2 = 40% (Das stimmt nur, wenn GLEICHE Mengen gemischt werden!)
> **Richtig:** Die Mengen berücksichtigen – hier ist es 44%, weil mehr von der stärkeren Lösung dabei ist.

## Zahnradübersetzung

### Formel

$$\frac{n_1}{n_2} = \frac{z_2}{z_1}$$

n = Drehzahl, z = Zähnezahl

> [!note] **Warum ist das Verhältnis umgekehrt?**
> Die Zähnezahl und die Drehzahl sind **indirekt proportional**. Ein großes Zahnrad mit vielen Zähnen dreht sich langsamer, ein kleines mit wenigen Zähnen dreht sich schneller.
> 
> Denk an ein Fahrrad: Wenn du vorne ein großes Kettenblatt und hinten ein kleines Ritzel hast, musst du weniger treten, fährst aber schneller – das große Rad „treibt" das kleine an.

### Beispiel

Antriebsrad: 20 Zähne, 100 U/min
Abtriebsrad: 40 Zähne

$$n_2 = \frac{20 \times 100}{40} = 50 \text{ U/min}$$

> [!tip] **Merkregel für Zahnräder**
> - **Mehr Zähne = weniger Drehzahl** (aber mehr Kraft!)
> - **Weniger Zähne = mehr Drehzahl** (aber weniger Kraft!)
> 
> Das ist das Grundprinzip jedes Getriebes: Du tauschst Geschwindigkeit gegen Kraft oder umgekehrt.

## Hebelgesetz

$$F_1 \times l_1 = F_2 \times l_2$$

> [!note] **Das Hebelgesetz verstehen**
> Archimedes erkannte: Kraft mal Hebelarm ist auf beiden Seiten gleich. Mit einem langen Hebelarm kannst du mit wenig Kraft viel bewegen. Das nutzen wir bei:
> - **Brechstange**: Langer Griff, kurzer Lastarm
> - **Wippe**: Gleiche Armlängen → gleiche Gewichte balancieren
> - **Schere**: Kurze Klingen, lange Griffe für mehr Kraft

### Beispiel

Kraft 200 N bei 30 cm. Last bei 20 cm?

$$\text{Last} = \frac{200 \times 30}{20} = 300 \text{ N}$$

Mit 200 N Kraft und dem richtigen Hebelarm kannst du also 300 N Last bewegen!

## Zusammenhänge

### Voraussetzungen

- [[01-Verhaeltnisse]] – Grundbegriff für alle technischen Verhältnisse
- [[04-Direkte-Proportionalitaet]] – Mischungsrechnung
- [[05-Indirekte-Proportionalitaet]] – Zahnräder und Hebel

### Weiterführende Themen

- [[03-Dreisatz]] – Universalmethode für viele dieser Aufgaben
- [[09-Dichte-und-Masse]] – Weitere physikalische Anwendung

## Prüfungsrelevanz

> [!warning] Prüfungsrelevanz: Mittel
> Mischungsaufgaben sind häufiger als Getriebe- oder Hebelaufgaben.

## Typische Prüfungsfragen

1. Mische 4 L mit 30% und 6 L mit 50%. Ergebnis?
2. Zahnrad mit 15 Zähnen treibt eines mit 45 Zähnen. Übersetzung?

## Quellen

- Lambacher Schweizer Mathematik 7
- Technische Mathematik

## Weiterführende Links

- [[01-Verhaeltnisse]]
- [[03-Dreisatz]]
