---
title: "FMEA – Fehlermöglichkeits- und Einflussanalyse"
created: 2026-10-13
modified: 2026-10-13
type: lecture
tags:
  - lf11c
  - prozessanalyse
  - fmea
  - qualitaetsmanagement
  - risikobewertung
source: proTirone (CC-BY-4.0)
---

# FMEA – Fehlermöglichkeits- und Einflussanalyse

> [!info] Lernziele
> - FMEA-Verfahren verstehen und anwenden
> - Risiko-Prioritätszahl (RPZ) berechnen
> - Verschiedene FMEA-Typen unterscheiden

## Definition

**FMEA** steht für *Failure Mode and Effects Analysis* (deutsch: *Fehlermöglichkeits- und Einflussanalyse*).

> [!note] Kernidee
> FMEA ist ein systematisches Verfahren, um möglichen Produktfehlern eine Kennzahl zuzuordnen, anhand derer die Dringlichkeit der Bearbeitung im Vergleich zu anderen Fehlern erkennbar wird.

## FMEA-Prozess

### Schritte der Durchführung

1. **Team bilden**: Interdisziplinäres Expertenteam aus:
   - Konstruktion und Entwicklung
   - Versuch und Fertigungsplanung
   - Fertigungsausführung
   - Qualitätsmanagement

2. **System beschreiben**: Struktur und Funktion der Elemente dokumentieren

3. **Fehler identifizieren**: Für jedes Subsystem potenzielle Fehler auflisten:
   - Fehlerort
   - Fehlerart
   - Fehlerfolge
   - Fehlerursache

4. **Fehler bewerten**: Drei Dimensionen (Wert 1–10):
   - **B** = **S**everity (Bedeutung der Fehlerfolge)
   - **A** = **O**ccurrence (Auftretenswahrscheinlichkeit)
   - **E** = **D**etection (Entdeckungswahrscheinlichkeit)

5. **RPZ berechnen**: Risiko-Prioritätszahl = B × A × E

## Bewertungsdimensionen

### Bedeutung (B / Severity)
Je gewichtiger die Auswirkungen eines Fehlers, desto wichtiger ist die Beseitigung seiner Ursache.

### Auftretenswahrscheinlichkeit (A / Occurrence)
Je häufiger ein Fehler auftritt, desto wichtiger ist die Beseitigung seiner Ursache.

### Entdeckungswahrscheinlichkeit (E / Detection)

> [!warning] Interpretation variiert
> - **Pekuniärer Standpunkt**: Schwer entdeckbare Fehler brauchen weniger Aufmerksamkeit
> - **Moralischer Standpunkt**: Gerade schwer entdeckbare Fehler erfordern mehr Aufmerksamkeit (Imageschutz)

Jede Bewertung muss eine auf den Firmenethos ausgerichtete Systematik zugrunde legen.

## FMEA-Typen

| Typ | Fokus | Anwendung |
|-----|-------|-----------|
| **Design-FMEA** (D-FMEA) | Produktfehler | Während der Konstruktionsphase |
| **Prozess-FMEA** (P-FMEA) | Herstellungsprozess | Qualitätssteigerung in der Fertigung |
| **Präventive FMEA** | Proaktive Identifikation | Frühe Designphase (Antizipation) |
| **Korrektive FMEA** | Reaktive Analyse | Spätere Produktlebenszyklusphasen |

### Prozess-FMEA Mängel

Bei der Prozess-FMEA gelten als Mängel:
- Zu langsame Produktion
- Zu teure Produktion
- Zu fehlerbehafteter Output

## Beispiel: Risikobewertung

```
Fehler: Softwarefehler in Benutzeroberfläche
├── Bedeutung (B):     7 (mittlere Auswirkung auf Nutzer)
├── Auftreten (A):     4 (gelegentlich)
├── Entdeckung (E):    3 (meist im Test gefunden)
└── RPZ:               7 × 4 × 3 = 84
```

> [!tip] RPZ-Interpretation
> - RPZ < 40: Geringes Risiko
> - RPZ 40–100: Mittleres Risiko, Maßnahmen prüfen
> - RPZ > 100: Hohes Risiko, Maßnahmen erforderlich
> - RPZ > 200: Kritisch, sofortige Maßnahmen

## Prüfungsrelevanz

> [!question] Typische Prüfungsfragen
> - Was bedeutet die Abkürzung FMEA?
> - Welche drei Faktoren bilden die RPZ?
> - Unterschied zwischen Design-FMEA und Prozess-FMEA?
> - Wann wird eine präventive, wann eine korrektive FMEA eingesetzt?

## Querverweise

- → [[02-ABC-Analyse|ABC-Analyse]] – Alternative Priorisierungsmethode
- → [[03-Ishikawa|Ursache-Wirkungsdiagramm]] – Ursachenanalyse
- → [[../03-Datenqualitaet/01-Qualitaetskriterien|Qualitätskriterien]] – Qualitätsmerkmale

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (CC-BY-4.0).
