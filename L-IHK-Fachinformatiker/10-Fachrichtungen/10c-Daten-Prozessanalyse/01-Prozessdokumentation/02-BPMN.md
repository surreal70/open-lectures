---
title: "BPMN – Business Process Model and Notation"
created: 2026-10-13
modified: 2026-10-13
type: lecture
tags:
  - lf11c
  - prozessdokumentation
  - bpmn
  - geschaeftsprozess
  - modellierung
source: proTirone (CC-BY-4.0)
---

# BPMN – Business Process Model and Notation

> [!info] Lernziele
> - BPMN-Grundelemente kennen und anwenden
> - Geschäftsprozesse in BPMN modellieren
> - Unterschied zu EPK und Flussdiagrammen verstehen

## Was ist BPMN?

**BPMN** (Business Process Model and Notation) ist eine grafische Spezifikationssprache zur Modellierung von Geschäftsprozessen und Arbeitsabläufen.

> [!note] Standardisierung
> BPMN ist ein ISO-Standard (ISO/IEC 19510:2013) und wird von der Object Management Group (OMG) gepflegt.

## Grundelemente

### Flussobjekte

| Symbol | Name | Beschreibung |
|--------|------|--------------|
| ○ | **Startereignis** | Beginn des Prozesses |
| ◎ | **Zwischenereignis** | Ereignis während des Prozesses |
| ◉ | **Endereignis** | Ende des Prozesses |
| ▭ | **Aktivität/Task** | Auszuführende Tätigkeit |
| ◇ | **Gateway** | Verzweigung/Zusammenführung |

### Gateway-Typen

```
    ◇        Exklusives Gateway (XOR)
   ╱ ╲       Nur EIN Pfad wird gewählt
  ╱ X ╲      
  ╲   ╱
   ╲ ╱

    ◇        Paralleles Gateway (AND)
   ╱ ╲       ALLE Pfade werden parallel ausgeführt
  ╱ + ╲      
  ╲   ╱
   ╲ ╱

    ◇        Inklusives Gateway (OR)
   ╱ ╲       MINDESTENS ein Pfad wird gewählt
  ╱ O ╲      
  ╲   ╱
   ╲ ╱
```

### Verbindungsobjekte

| Symbol | Name | Beschreibung |
|--------|------|--------------|
| ──→ | **Sequenzfluss** | Reihenfolge der Aktivitäten |
| - - → | **Nachrichtenfluss** | Kommunikation zwischen Pools |
| ····→ | **Assoziation** | Verknüpfung mit Artefakten |

### Swimlanes

```
┌─────────────────────────────────────────────────┐
│  Pool: Organisation                              │
├─────────────────────────────────────────────────┤
│ Lane: Abteilung A                                │
│  ○──→ ▭──→ ◇                                    │
├─────────────────────────────────────────────────┤
│ Lane: Abteilung B                                │
│           ↓                                      │
│        ▭──→ ◉                                   │
└─────────────────────────────────────────────────┘
```

- **Pool**: Repräsentiert einen Teilnehmer/Organisation
- **Lane**: Unterteilt einen Pool in Verantwortungsbereiche

## Beispiel: Einkaufsprozess

```
┌─────────────────────────────────────────────────────────────┐
│ Einkaufsprozess                                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ○──→ ▭ Einkaufszettel ──→ ◇ Reinigung?                     │
│       prüfen              ╱ ╲                                │
│                          ╱   ╲                               │
│                    ja  ╱       ╲ nein                        │
│                       ↓         ↓                            │
│              ▭ Nach Herborn  ◇ Drogerie?                     │
│              fahren         ╱ ╲                              │
│                 │      ja ╱   ╲ nein                         │
│                 │        ↓     ↓                             │
│                 │   ▭ Nach   ▭ Nach                          │
│                 │   Erda     Niederweidbach                  │
│                 │     │         │                            │
│                 └─────┴────┬────┘                            │
│                            ↓                                 │
│                       ▭ Einkaufen                            │
│                            │                                 │
│                            ↓                                 │
│                           ◉                                  │
└─────────────────────────────────────────────────────────────┘
```

## Artefakte

| Element | Beschreibung |
|---------|--------------|
| **Datenobjekt** | Daten, die im Prozess verwendet werden |
| **Gruppe** | Visuelle Gruppierung von Elementen |
| **Anmerkung** | Textuelle Kommentare |

## BPMN vs. andere Notationen

| Aspekt | BPMN | EPK | Flussdiagramm |
|--------|------|-----|---------------|
| Standardisierung | ISO | Keine | Keine |
| Komplexität | Hoch | Mittel | Niedrig |
| Swimlanes | Ja | Möglich | Selten |
| Ereignisse | Vielfältig | Ja | Nein |
| Tool-Unterstützung | Sehr gut | Gut | Universal |

## Werkzeuge

- **Camunda Modeler** (Open Source)
- **Signavio** (kommerziell)
- **Bizagi Modeler** (kostenlos für Grundfunktionen)
- **draw.io** (kostenlos, webbasiert)

## Best Practices

> [!tip] Empfehlungen
> 1. **Lesrichtung**: Von links nach rechts, von oben nach unten
> 2. **Benennung**: Aktivitäten im Imperativ („Bestellung prüfen")
> 3. **Swimlanes**: Für klare Verantwortungszuordnung
> 4. **Gateways**: Immer mit Bedingungen beschriften
> 5. **Detailgrad**: Konsistent innerhalb eines Diagramms

## Prüfungsrelevanz

> [!question] Typische Prüfungsfragen
> - Zeichnen Sie den gegebenen Prozess als BPMN-Diagramm
> - Welche Gateway-Typen gibt es und wann werden sie verwendet?
> - Was ist der Unterschied zwischen Pool und Lane?
> - Erklären Sie den Unterschied zwischen Sequenz- und Nachrichtenfluss

## Querverweise

- → [[01-Prozessgrundlagen|Prozessgrundlagen]] – Grundbegriffe
- → [[03-EPK|EPK]] – Alternative Notation
- → [[../02-Prozessanalyse/03-Ishikawa|Ishikawa]] – Ursachenanalyse

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (CC-BY-4.0).
