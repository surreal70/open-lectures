---
title: "EPK – Ereignisgesteuerte Prozesskette"
created: 2026-10-13
modified: 2026-10-13
type: lecture
tags:
  - lf11c
  - prozessdokumentation
  - epk
  - eepk
  - geschaeftsprozess
  - aris
source: proTirone (CC-BY-4.0)
---

# EPK – Ereignisgesteuerte Prozesskette

> [!info] Lernziele
> - EPK-Grundelemente kennen und anwenden
> - eEPK (erweiterte EPK) verstehen
> - Unterschied zu BPMN und Flussdiagrammen kennen

## Was ist EPK?

Die **Ereignisgesteuerte Prozesskette** (EPK) ist eine grafische Modellierungssprache zur Darstellung von Geschäftsprozessen.

> [!note] Herkunft
> EPK wurde 1992 am Institut für Wirtschaftsinformatik der Universität Saarbrücken entwickelt und ist Teil des ARIS-Konzepts (Architektur integrierter Informationssysteme).

## Grundelemente

### Basiselemente der EPK

```
    ╭─────╮
    │     │     EREIGNIS (sechseckig)
    ╰─────╯     Passiver Zustand, der eintritt
                „Bestellung ist eingegangen"

    ┌─────────┐
    │         │  FUNKTION (rechteckig mit abgerundeten Ecken)
    │         │  Aktive Tätigkeit, die ausgeführt wird
    └─────────┘  „Bestellung prüfen"

        ○       KONNEKTOR (Kreis)
       ╱│╲      Verzweigung/Zusammenführung
      ╱ │ ╲     XOR, AND, OR
```

### Konnektoren im Detail

| Symbol | Name | Bedeutung |
|--------|------|-----------|
| ⊗ | **XOR** | Exklusiv-Oder: Genau EIN Pfad |
| ⊕ | **OR** | Oder: Mindestens ein Pfad |
| ∧ | **AND** | Und: ALLE Pfade parallel |

## Grundregel: Ereignis-Funktion-Wechsel

> [!warning] Wichtige Regel
> In einer EPK wechseln sich Ereignisse und Funktionen **immer** ab!
> - Nach jedem Ereignis folgt eine Funktion
> - Nach jeder Funktion folgt ein Ereignis

```
    ╭─────────────╮
    │ Bestellung  │     ← Ereignis (Start)
    │ eingegangen │
    ╰──────┬──────╯
           │
           ↓
    ┌─────────────┐
    │ Bestellung  │     ← Funktion
    │   prüfen    │
    └──────┬──────┘
           │
           ↓
    ╭─────────────╮
    │ Bestellung  │     ← Ereignis
    │  geprüft    │
    ╰──────┬──────╯
           │
          ⊗ XOR         ← Konnektor
         ╱   ╲
        ↓     ↓
    ╭───────╮ ╭───────╮
    │  OK   │ │Fehler │  ← Ereignisse
    ╰───────╯ ╰───────╯
```

## Erweiterte EPK (eEPK)

Die **erweiterte EPK** (eEPK) ergänzt zusätzliche Elemente:

### Zusätzliche Elemente

| Symbol | Name | Beschreibung |
|--------|------|--------------|
| ▭ | **Organisationseinheit** | Wer führt die Funktion aus? |
| ◇ | **Informationsobjekt** | Welche Daten werden verwendet? |
| □ | **Anwendungssystem** | Welches IT-System unterstützt? |

### eEPK-Beispiel

```
                           ┌──────────────┐
                           │   Vertrieb   │  ← Organisationseinheit
                           └──────┬───────┘
                                  │
    ╭───────────────╮            │
    │   Bestellung  │            │
    │  eingegangen  │ ───────────┘
    ╰───────┬───────╯
            │
            ↓
    ┌───────────────┐      ◇ Kundendaten
    │   Bestellung  │──────◇ Artikeldaten
    │    prüfen     │      □ ERP-System
    └───────┬───────┘
            │
            ↓
    ╭───────────────╮
    │   Bestellung  │
    │    geprüft    │
    ╰───────────────╯
```

## Verzweigungen und Zusammenführungen

### XOR-Verzweigung (Auswahl)

```
    ╭─────────────╮
    │  Prüfung    │
    │ abgeschlossen│
    ╰──────┬──────╯
           │
          ⊗ XOR
         ╱   ╲
        ↓     ↓
    ╭───────╮ ╭───────╮
    │ Zahlung│ │Zahlung│
    │   OK  │ │fehlerhaft│
    ╰───────╯ ╰───────╯
```

### AND-Verzweigung (Parallelität)

```
    ╭─────────────╮
    │ Auftrag     │
    │ angenommen  │
    ╰──────┬──────╯
           │
          ∧ AND
         ╱   ╲
        ↓     ↓
    ┌───────┐ ┌───────┐
    │Lager  │ │Rechnung│
    │prüfen │ │erstellen│
    └───────┘ └───────┘
```

## EPK vs. BPMN

| Aspekt | EPK | BPMN |
|--------|-----|------|
| **Herkunft** | Deutschland (ARIS) | International (OMG) |
| **Standardisierung** | Keine ISO | ISO 19510 |
| **Grundprinzip** | Ereignis-Funktion-Wechsel | Aktivitätsorientiert |
| **Swimlanes** | In eEPK möglich | Nativer Bestandteil |
| **Verbreitung** | DACH-Raum | Weltweit |
| **Tool-Support** | ARIS, Signavio | Sehr viele Tools |

## Best Practices

> [!tip] Empfehlungen
> 1. **Ereignisse**: Als Zustand formulieren („Bestellung ist geprüft")
> 2. **Funktionen**: Als Tätigkeit formulieren („Bestellung prüfen")
> 3. **Konnektoren**: Konsistent verwenden
> 4. **Lesrichtung**: Von oben nach unten
> 5. **Start/Ende**: Mit Ereignis beginnen und enden

## Prüfungsrelevanz

> [!question] Typische Prüfungsfragen
> - Zeichnen Sie den gegebenen Prozess als EPK
> - Welche Grundregel gilt für den Wechsel von Ereignissen und Funktionen?
> - Erklären Sie den Unterschied zwischen XOR, OR und AND
> - Was unterscheidet EPK von eEPK?

## Querverweise

- → [[01-Prozessgrundlagen|Prozessgrundlagen]] – Grundbegriffe
- → [[02-BPMN|BPMN]] – Alternative Notation
- → [[../02-Prozessanalyse/01-FMEA|FMEA]] – Prozessanalyse

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (CC-BY-4.0).
