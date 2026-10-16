---
title: Praktische Zufallsexperimente
chapter: "14"
section: "14.12"
type: lecture
created: 2026-10-13
modified: 2025-01-20
status: draft - review pending
tags:
  - mathematik/wahrscheinlichkeit
  - praxis
---

# Praktische Zufallsexperimente

## Einführung

> [!info] **Lernziele**
> Nach dieser Lektion können Sie:
> - Alltagssituationen als Zufallsexperimente modellieren
> - Verschiedene Aufgabentypen lösen

---

## Überblick

In diesem abschließenden Kapitel wenden wir alle gelernten Konzepte auf praktische Situationen an. Die Wahrscheinlichkeitsrechnung ist nicht nur ein abstraktes Gebiet – sie begegnet uns täglich bei Glücksspielen, in der Qualitätskontrolle, bei medizinischen Tests und Wettervorhersagen.

Das Wichtigste bei praktischen Aufgaben ist die **Modellierung**: Wie übersetze ich eine Alltagssituation in die Sprache der Wahrscheinlichkeitsrechnung? Welches mathematische Modell passt? Diese Übersetzungsleistung ist oft der schwierigste Teil – wenn das Modell einmal steht, ist die Berechnung meist Routine.

---

## Glücksspiele

Glücksspiele waren historisch der Ausgangspunkt der Wahrscheinlichkeitsrechnung. Sie eignen sich besonders gut zum Üben, weil die Regeln klar definiert sind.

### Lotto „6 aus 49"

> [!example] **Lotto „6 aus 49"**
> Mögliche Kombinationen: 
> $$\binom{49}{6} = \frac{49!}{6! \cdot 43!} = 13.983.816$$
> 
> **Wahrscheinlichkeiten:**
> | Ereignis | Wahrscheinlichkeit | Etwa |
> |----------|-------------------|------|
> | 6 Richtige | $\frac{1}{13.983.816}$ | 1 : 14 Mio. |
> | 5 Richtige | $\frac{258}{13.983.816}$ | 1 : 54.000 |
> | 4 Richtige | $\frac{13.545}{13.983.816}$ | 1 : 1.000 |
> | 3 Richtige | $\frac{246.820}{13.983.816}$ | 1 : 57 |

> [!warning] **Häufiger Fehler: „Überfällige" Zahlen**
> Manche Spieler wählen Zahlen, die lange nicht gezogen wurden, weil sie „überfällig" seien. Das ist ein Fehlschluss: Jede Ziehung ist unabhängig, jede Kombination ist gleich wahrscheinlich – auch 1, 2, 3, 4, 5, 6!

### Würfelspiele

Bei vielen Würfelspielen (Kniffel, Mäxchen) muss man Wahrscheinlichkeiten abschätzen können.

> [!example] **Zwei Würfel: Wahrscheinlichkeiten der Summen**
> | Summe | Möglichkeiten | Wahrscheinlichkeit |
> |-------|--------------|-------------------|
> | 2 | (1,1) | 2,8% |
> | 3 | (1,2), (2,1) | 5,6% |
> | 7 | (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) | 16,7% |
> | 12 | (6,6) | 2,8% |
> 
> Die Summe 7 ist am wahrscheinlichsten – wichtig für Spiele wie „Craps" oder „Siedler von Catan".

---

## Urnenmodelle

Das **Urnenmodell** ist das zentrale Denkwerkzeug der Wahrscheinlichkeitsrechnung. Viele Situationen lassen sich als „Ziehen aus einer Urne" modellieren.

### Mit Zurücklegen

- Wahrscheinlichkeiten bleiben **konstant**
- Züge sind **unabhängig**
- Pfadregeln: Einfach multiplizieren

> [!example] **Würfel als Urne mit Zurücklegen**
> 3× würfeln entspricht: 3× eine Kugel aus einer Urne mit den Zahlen 1-6 ziehen, wobei nach jedem Zug die Kugel zurückgelegt wird.
> 
> $P(\text{3× Sechs}) = \frac{1}{6} \cdot \frac{1}{6} \cdot \frac{1}{6} = \frac{1}{216}$

### Ohne Zurücklegen

- Wahrscheinlichkeiten **ändern sich** von Zug zu Zug
- Züge sind **abhängig**
- Im Baumdiagramm: Kantengewichte anpassen!

> [!example] **5 Kugeln (3 rot, 2 blau) – 2 Züge ohne Zurücklegen**
> 
> $P(\text{beide rot}) = \frac{3}{5} \cdot \frac{2}{4} = \frac{6}{20} = \frac{3}{10} = 30\%$
> 
> Beachte: Nach dem 1. Zug sind nur noch 4 Kugeln in der Urne!

> [!tip] **Erkennungsmerkmal im Aufgabentext**
> - „mit Zurücklegen" → unabhängig, konstante Wahrscheinlichkeiten
> - „ohne Zurücklegen" → abhängig, Wahrscheinlichkeiten ändern sich
> - „nacheinander ziehen" → ohne Kontext meist „ohne Zurücklegen"

---

## Alltagsanwendungen

Die Wahrscheinlichkeitsrechnung hat zahlreiche praktische Anwendungen jenseits von Glücksspielen:

### Qualitätskontrolle

In der Industrie werden Stichproben gezogen, um die Qualität einer Produktion zu prüfen.

> [!example] **Stichprobe**
> Eine Lieferung von 100 Teilen enthält 5 defekte. Bei zufälliger Entnahme von 3 Teilen:
> 
> $P(\text{alle 3 in Ordnung}) = \frac{95}{100} \cdot \frac{94}{99} \cdot \frac{93}{98} \approx 85{,}7\%$

### Versicherungen

Versicherungen basieren auf Wahrscheinlichkeitsrechnung: Sie berechnen, wie wahrscheinlich ein Schaden ist, und legen danach die Prämien fest.

### Medizinische Tests

> [!example] **Sensitivität und Spezifität**
> Ein Test erkennt 95% der Kranken (Sensitivität) und 90% der Gesunden (Spezifität).
> 
> Wenn 1% der Bevölkerung krank ist:
> - Von 10.000 Personen sind 100 krank und 9.900 gesund
> - Der Test erkennt 95 Kranke richtig (richtig positiv)
> - Aber auch 990 Gesunde werden fälschlich als krank erkannt (falsch positiv)
> 
> $P(\text{wirklich krank | positiver Test}) = \frac{95}{95 + 990} \approx 8{,}8\%$
> 
> Überraschend niedrig! Bei seltenen Krankheiten sind falsch-positive Ergebnisse häufig.

### Wettervorhersage

„30% Regenwahrscheinlichkeit" bedeutet: Bei ähnlichen Wetterlagen hat es in der Vergangenheit in etwa 30% der Fälle geregnet.

---

## Problemlösungsstrategien

> [!tip] **Systematisches Vorgehen bei Wahrscheinlichkeitsaufgaben**
> 1. **Verstehen:** Was genau ist gefragt? Welches Ereignis?
> 2. **Modellieren:** Welches Modell passt? (Laplace? Baumdiagramm? Gegenereignis?)
> 3. **Ergebnismenge:** Was ist Ω? Wie groß ist |Ω|?
> 4. **Günstige Fälle:** Was ist E? Wie groß ist |E|?
> 5. **Berechnen:** Formel anwenden
> 6. **Prüfen:** Ist das Ergebnis plausibel? (0 ≤ P ≤ 1)

### Wann welche Methode?

| Situation | Empfohlene Methode |
|-----------|-------------------|
| Alle gleich wahrscheinlich | Laplace-Formel |
| Mehrstufig, übersichtlich | Baumdiagramm + Pfadregeln |
| „Mindestens einmal" | Gegenereignis |
| Viele Möglichkeiten zählen | Kombinatorik |

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[05-Laplace-Experimente|Laplace-Experimente]] – Grundformel für faire Zufallsexperimente
- → [[08-Baumdiagramme|Baumdiagramme]] – Visualisierung mehrstufiger Experimente
- → [[07-Gegenereignisse|Gegenereignisse]] – Trick bei „mindestens einmal"
- → [[11-Kombinatorik|Kombinatorik]] – Systematisches Abzählen
- → [[../13-Statistik-und-Datenanalyse/00-Statistik-Index|Statistik und Datenanalyse]] – Verwandtes Gebiet der Datenauswertung

---

**Navigation:** [[11-Kombinatorik|← Kombinatorik]] | [[../15-Praktische-Mathematik-und-Abschlussprojekt/00-Praktische-Mathematik-Index|Praktische Mathematik →]]
