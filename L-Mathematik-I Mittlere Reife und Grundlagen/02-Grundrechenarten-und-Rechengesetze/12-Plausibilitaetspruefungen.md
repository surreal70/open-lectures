---
author: Open Lectures
title: Plausibilitätsprüfungen
status: draft - review pending
tags:
  - content
  - mathematik
  - rechengesetze
created: 2026-10-13
modified: 2026-10-13
---

# Plausibilitätsprüfungen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Ergebnisse auf Sinnhaftigkeit prüfen können
> - Typische Fehler durch Plausibilitätsprüfung erkennen
> - Verschiedene Prüfmethoden anwenden können

---

## Überblick

**Plausibilitätsprüfungen** helfen zu erkennen, ob ein Rechenergebnis überhaupt sinnvoll sein kann. Sie ersetzen nicht die genaue Rechnung, aber sie decken grobe Fehler auf.

---

## Methoden der Plausibilitätsprüfung

### 1. Größenordnung prüfen

*„Liegt das Ergebnis in einem realistischen Bereich?"*

**Beispiel:** 
- Berechnung ergibt: Alter einer Person = 350 Jahre → **unmöglich**
- Preis eines Brötchens = 0,003 € → **unrealistisch**

### 2. Überschlagsrechnung

Vergleiche das exakte Ergebnis mit dem Überschlag.

**Beispiel:** $47 \cdot 23$
- Überschlag: $50 \cdot 20 = 1000$
- Wenn Ergebnis 10810 lautet → **Fehler** (eine Stelle zu viel)

### 3. Probe

Umkehroperation anwenden:

**Bei Division:** $144 : 12 = 12$ → Probe: $12 \cdot 12 = 144$ ✓

**Bei Gleichungen:** Lösung einsetzen und prüfen

### 4. Vorzeichen prüfen

- Produkt zweier negativer Zahlen muss positiv sein
- Summe positiver Zahlen muss positiv sein

### 5. Quersummenprobe (bei Multiplikation)

Die Quersumme des Ergebnisses muss zum Produkt der Quersummen passen (modulo 9).

---

## Beispiele

### Beispiel 1: Textaufgabe

*„Ein Zug fährt 3 Stunden mit 120 km/h. Wie weit kommt er?"*

Ergebnis: 40 km → **Fehler!** (3 · 120 = 360 km)

### Beispiel 2: Bruchrechnung

$\frac{3}{4} + \frac{1}{2}$

Ergebnis: $\frac{4}{6}$ → **Verdächtig!** (sollte > 1 sein, da $\frac{3}{4} + \frac{1}{2} = \frac{5}{4}$)

### Beispiel 3: Prozentrechnung

*„20% von 80"*

Ergebnis: 160 → **Fehler!** (20% von etwas muss kleiner als das Ganze sein)

---

## Zusammenhänge

- → [[11-Ueberschlagsrechnung|Überschlagsrechnung]]

> [!warning] **Prüfungsrelevant**
> - Ergebnisse immer auf Plausibilität prüfen
> - Überschlag als Kontrollmittel
> - Probe durch Umkehroperation

> [!question] **Typische Prüfungsfragen**
> - Welches Ergebnis kann nicht stimmen: $(-5) \cdot (-3) = -15$?
> - Prüfe durch Probe: $156 : 12 = 13$
> - Ein Ergebnis von 0,5 Personen – was ist falsch?

## Quellen

- Padberg, Friedhelm: *Didaktik der Arithmetik*. Springer, 2017.
