---
title: Modalwert (Modus)
chapter: "13"
section: "13.10"
type: lecture
created: 2026-10-13
modified: 2026-10-25
status: final
tags:
  - mathematik/statistik
  - modalwert
  - lageparameter
---

# Modalwert (Modus)

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Den Modalwert bestimmen
> - Multimodale Verteilungen erkennen
> - Alle drei Lageparameter vergleichen

Der Modalwert – auch Modus genannt – ist der einfachste der drei Lageparameter. Er gibt an, welcher Wert am häufigsten vorkommt. Anders als Mittelwert und Median kann der Modalwert auch für **qualitative Daten** (z.B. Lieblingsfarbe, Verkehrsmittel) bestimmt werden.

### Historischer Hintergrund

Der Begriff „Modus" stammt vom lateinischen *modus* (Art, Weise, Maß). In der Statistik bezeichnet er den „typischsten" oder „häufigsten" Wert. Der Begriff wurde im 19. Jahrhundert geprägt, als Statistiker verschiedene Maße entwickelten, um die „zentrale Tendenz" von Daten zu beschreiben.

> [!tip] **Alltagsrelevanz**
> Der Modalwert beantwortet Fragen wie: „Was ist das beliebteste Verkehrsmittel?", „Welche Schuhgröße wird am meisten verkauft?", „Welcher Name ist am häufigsten?" – Fragen, die für Handel und Marketing sehr relevant sind.

## Definition

> [!note] Definition
> Der **Modalwert** (Modus) ist der Wert, der in einer Datenreihe **am häufigsten vorkommt**.

### Besonderheit: Nicht immer eindeutig

Im Gegensatz zu Mittelwert und Median ist der Modalwert nicht immer eindeutig:

- Wenn ein Wert am häufigsten vorkommt: **unimodal** (ein Modalwert)
- Wenn zwei Werte gleich oft am häufigsten vorkommen: **bimodal** (zwei Modalwerte)
- Wenn mehr als zwei Werte gleich oft am häufigsten vorkommen: **multimodal**
- Wenn alle Werte gleich oft vorkommen: **kein Modalwert definiert**

## Beispiele

> [!example] Beispiel 1: Eindeutiger Modalwert (unimodal)
> **Daten:** 2, 3, 3, 4, 3, 5, 2, 3
> 
> **Häufigkeiten auszählen:**
> - 2 kommt 2-mal vor
> - 3 kommt **4-mal** vor ← Maximum
> - 4 kommt 1-mal vor
> - 5 kommt 1-mal vor
> 
> **Modalwert = 3** (kommt am häufigsten vor)

> [!example] Beispiel 2: Zwei Modalwerte (bimodal)
> **Daten:** 1, 2, 2, 3, 3, 4
> 
> **Häufigkeiten:**
> - 1 kommt 1-mal vor
> - 2 kommt **2-mal** vor ← Maximum
> - 3 kommt **2-mal** vor ← Maximum
> - 4 kommt 1-mal vor
> 
> **Modalwerte = 2 und 3** (beide kommen gleich oft am häufigsten vor)
> 
> Diese Verteilung nennt man **bimodal**.

![[modalwert.png]]
*<span class="fig-id">13-10-modalwert</span>: Links eine unimodale Verteilung (ein häufigster Wert), rechts eine bimodale (zwei gleich häufige Gipfel). Die Modalwerte sind dunkel hervorgehoben.*

> [!tip] **Was bedeutet eine bimodale Verteilung?**
> Eine bimodale Verteilung deutet oft darauf hin, dass die Daten aus **zwei verschiedenen Gruppen** stammen.
> 
> Beispiel: Körpergrößen aller Erwachsenen zeigen oft zwei Gipfel – einen für Frauen und einen für Männer.

## Vergleich der drei Lageparameter

| Parameter | Bestimmung | Besonderheit | Datentyp |
|-----------|------------|--------------|----------|
| **Mittelwert** | Summe / Anzahl | Berücksichtigt alle Werte, anfällig für Ausreißer | Nur metrisch |
| **Median** | Mittlerer Wert (geordnet) | Robust gegen Ausreißer | Metrisch und ordinal |
| **Modalwert** | Häufigster Wert | Auch für qualitative Daten, nicht immer eindeutig | Alle Datentypen |

> [!example] **Zusammenfassender Vergleich**
> **Daten:** 1, 2, 2, 2, 3, 4, 10
> 
> | Kennwert | Berechnung | Ergebnis |
> |----------|------------|----------|
> | Mittelwert | $\frac{1+2+2+2+3+4+10}{7} = \frac{24}{7}$ | ≈ 3,4 |
> | Median | Geordnet: 1, 2, 2, **2**, 3, 4, 10 | 2 |
> | Modalwert | 2 kommt 3-mal vor (am häufigsten) | 2 |
> 
> Der Ausreißer (10) beeinflusst den Mittelwert stark, aber Median und Modalwert bleiben davon unbeeinflusst.

## Wann welchen Lageparameter?

> [!tip] **Entscheidungshilfe**
> 
> - **Qualitative Daten** (Lieblingsfarbe, Verkehrsmittel): Nur der **Modalwert** ist sinnvoll
> - **Ordinale Daten** (Schulnoten, Zufriedenheit): **Median** oder Modalwert
> - **Metrische Daten ohne Ausreißer**: **Mittelwert** (nutzt die meiste Information)
> - **Metrische Daten mit Ausreißern**: **Median** (robust)
> - **Frage nach dem „Typischsten"**: **Modalwert**

> [!warning] **Häufiger Fehler: Modalwert bei Messdaten**
> Bei stetigen Messdaten (z.B. Körpergröße auf mm genau) kommt oft jeder Wert nur einmal vor. Dann gibt es keinen sinnvollen Modalwert – hier muss man zuerst Klassen bilden.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[08-Arithmetisches-Mittel|Arithmetisches Mittel]] – Durchschnitt aller Werte
- → [[09-Median|Median]] – Der mittlere Wert
- → [[04-Absolute-und-relative-Haeufigkeiten|Häufigkeiten]] – Grundlage für den Modalwert
- → [[07-Histogramme|Histogramme]] – Multimodale Verteilungen erkennen

> [!warning] **Prüfungsrelevant**
> - Definition: Modalwert = häufigster Wert
> - Bimodale und multimodale Verteilungen erkennen
> - Vergleich: Mittelwert vs. Median vs. Modalwert
> - Wissen, wann welcher Lageparameter geeignet ist

---

**Navigation:** [[09-Median|← Median]] | [[11-Spannweite|Spannweite →]]
