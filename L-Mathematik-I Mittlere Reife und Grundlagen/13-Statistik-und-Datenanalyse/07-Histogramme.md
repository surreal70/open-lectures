---
title: Histogramme
chapter: "13"
section: "13.7"
type: lecture
created: 2026-10-13
modified: 2026-10-25
status: draft - review pending
tags:
  - mathematik/statistik
  - diagramme
  - histogramm
---

# Histogramme

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Den Unterschied zum Balkendiagramm erklären
> - Histogramme für Klassenbildung erstellen
> - Verteilungen erkennen

Das Histogramm ist ein spezieller Diagrammtyp für **stetige** oder **klassierte** Daten. Während Balkendiagramme einzelne Kategorien darstellen, zeigt das Histogramm die Verteilung von Messwerten über einen kontinuierlichen Bereich.

### Historischer Hintergrund

Der Begriff „Histogramm" wurde 1891 vom englischen Statistiker Karl Pearson geprägt, einem Pionier der modernen Statistik. Er brauchte eine Möglichkeit, die Verteilung von Messdaten (wie Körpergrößen oder Lebenserwartungen) anschaulich darzustellen. Das Wort setzt sich aus dem Griechischen *histos* (Mast, Stab) und *gramma* (Schrift, Zeichnung) zusammen.

## Definition

> [!note] Histogramm
> Ein **Histogramm** stellt die Häufigkeitsverteilung von Daten in **Klassen** (Intervallen) dar. Die Säulen grenzen direkt aneinander – es gibt **keine Lücken** zwischen ihnen.

Das Besondere am Histogramm: Die **Fläche** (nicht nur die Höhe!) der Säulen entspricht der Häufigkeit. Bei gleicher Klassenbreite ist das egal, aber bei unterschiedlichen Klassenbreiten macht es einen wichtigen Unterschied.

## Unterschied zum Balkendiagramm

| Merkmal | Balkendiagramm | Histogramm |
|---------|----------------|------------|
| **Datentyp** | Kategorien (diskret, nominal) | Klassen (stetig, intervalliert) |
| **Lücken** | Lücken zwischen Balken | Keine Lücken |
| **Reihenfolge** | Reihenfolge beliebig | Reihenfolge fest (nach Wert) |
| **Beispiel** | Lieblingsfächer, Verkehrsmittel | Körpergrößen, Temperaturen |

> [!tip] **Eselsbrücke**
> - **Balken**diagramm: **B**eliebige Reihenfolge, **B**eabstandete Balken
> - **H**istogramm: **H**intereinander, **H**ückenlos

## Klassenbildung

Bei stetigen Daten (z.B. Körpergröße) gibt es theoretisch unendlich viele mögliche Werte. Um sie übersichtlich darzustellen, fasst man sie zu **Klassen** (Intervallen) zusammen.

> [!example] Beispiel: Körpergrößen von 30 Schülern
> | Klasse | Häufigkeit |
> |--------|------------|
> | 150–159 cm | 3 |
> | 160–169 cm | 8 |
> | 170–179 cm | 12 |
> | 180–189 cm | 5 |
> | 190–199 cm | 2 |
> | **Summe** | **30** |

![[stat-histogramm.png]]
*<span class="fig-id">13-07-histogramm</span>: Histogramm der Körpergrößen – die Säulen grenzen lückenlos aneinander, da die Daten stetig und klassiert sind.*

Das resultierende Histogramm zeigt auf einen Blick: Die meisten Schüler sind zwischen 170 und 179 cm groß.

> [!tip] **Regeln für die Klassenbildung**
> 1. **Gleiche Klassenbreite**: Alle Klassen sollten gleich breit sein (hier: 10 cm)
> 2. **Keine Überlappungen**: Jeder Wert gehört in genau eine Klasse
> 3. **Keine Lücken**: Die Klassen schließen lückenlos aneinander an
> 4. **Sinnvolle Anzahl**: Typischerweise 5–15 Klassen
>    - Zu wenige Klassen → Information geht verloren
>    - Zu viele Klassen → Unübersichtlich, zufällige Schwankungen

> [!warning] **Häufiger Fehler: Klassengrenzen unklar**
> Wohin gehört ein Schüler mit genau 170 cm – in die Klasse 160–170 oder 170–180?
> 
> Lösung: Klassen eindeutig definieren, z.B.:
> - 160 cm ≤ x < 170 cm (170 gehört zur nächsten Klasse)
> - oder: 160,0–169,9 cm

## Verteilungsformen

Histogramme zeigen charakteristische Verteilungsmuster, die wichtige Informationen über die Daten verraten:

![[stat-verteilungsformen.png]]
*<span class="fig-id">13-07-verteilungsformen</span>: Vier typische Verteilungsformen – symmetrisch, rechtsschief, linksschief und bimodal. Der „Schwanz" zeigt in die Richtung der Schiefe.*

- **Symmetrisch (glockenförmig)**: Die Werte verteilen sich gleichmäßig um einen Mittelwert – typisch für viele natürliche Phänomene (Körpergröße, IQ). Dies ist die berühmte **Normalverteilung** oder „Gaußsche Glockenkurve".

- **Rechtsschief (linkssteil)**: Häufung bei kleinen Werten, lange „Schwanz" nach rechts – typisch für Einkommen, Wartezeiten

- **Linksschief (rechtssteil)**: Häufung bei großen Werten, langer „Schwanz" nach links – z.B. Prüfungsnoten (viele gute, wenige schlechte)

- **Bimodal**: Zwei Gipfel – deutet auf zwei verschiedene Gruppen hin

> [!tip] **Merkregel für Schiefe**
> Der „Schwanz" zeigt in die Richtung der Schiefe:
> - **Rechts**schief = Schwanz zeigt nach **rechts**
> - **Links**schief = Schwanz zeigt nach **links**

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[05-Balkendiagramme|Balkendiagramme]] – Für kategoriale Daten
- → [[08-Arithmetisches-Mittel|Arithmetisches Mittel]] – Lageparameter aus klassierten Daten
- → [[12-Standardabweichung|Standardabweichung]] – Streuung der Verteilung
- → [[../14-Wahrscheinlichkeitsrechnung/01-Zufallsexperimente|Zufallsexperimente]] – Verteilungen in der Wahrscheinlichkeitsrechnung

> [!warning] **Prüfungsrelevant**
> - Unterschied Histogramm vs. Balkendiagramm
> - Regeln für Klassenbildung (gleiche Breite, keine Lücken, keine Überlappung)
> - Verteilungsformen erkennen (symmetrisch, links-/rechtsschief)

---

**Navigation:** [[06-Kreisdiagramme|← Kreisdiagramme]] | [[08-Arithmetisches-Mittel|Arithmetisches Mittel →]]
