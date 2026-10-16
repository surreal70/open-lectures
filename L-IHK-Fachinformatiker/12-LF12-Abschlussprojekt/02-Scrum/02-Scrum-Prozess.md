---
title: "Scrum-Prozess"
created: 2026-10-13
modified: 2026-10-13
type: lecture
tags:
  - lf12
  - scrum
  - sprint
  - daily
  - planning-poker
  - retrospektive
source: proTirone (CC-BY-4.0)
---

# Scrum-Prozess

> [!info] Lernziele
> - Sprint-Ablauf verstehen
> - Scrum-Events kennen und erklären
> - Planning Poker durchführen können

## Der Sprint

Ein **Sprint** ist eine zeitlich begrenzte Iteration (typisch: 1-4 Wochen).

```
┌────────────────────────────────────────────────────────┐
│                      SPRINT (2 Wochen)                  │
├────────┬──────────────────────────────┬────────────────┤
│Sprint  │         Entwicklung          │Review + Retro  │
│Planning│  Daily ─ Daily ─ Daily ─ ... │                │
└────────┴──────────────────────────────┴────────────────┘
    ↑                                           ↓
    │                                           │
    └───────── Product Backlog ←────────────────┘
```

## Scrum-Events

### 1. Sprint Planning

**Wann**: Am Anfang jedes Sprints
**Dauer**: Max. 8h für 4-Wochen-Sprint

**Ablauf:**

1. Product Owner hat Backlog repriorisiert
2. PO erläutert funktionale Wünsche
3. **Planning Poker** für Aufwandsschätzung
4. Team einigt sich auf Sprint-Kapazität
5. Team nimmt Tasks von oben ins Sprint Backlog

### Planning Poker

> [!tip] Methode
> Jeder Entwickler schätzt **still** die Komplexität eines Items.
> Dann zeigen alle gleichzeitig ihre Karten.

**Fibonacci-Zahlen**: 1, 2, 3, 5, 8, 13, 20, 40, ?, ☕

```
Ablauf:
1. PO erklärt Anforderung
2. Jeder wählt verdeckt eine Karte
3. Alle decken gleichzeitig auf
4. Ausreißer erklären ihre Einschätzung
5. Diskussion bis Einigung
6. Komplexitätszahl wird notiert
```

> [!note] Warum stilles Zeigen?
> Damit jeder **unbeeinflusst** seine Meinung zeigt. Sonst orientieren sich alle am Lautesten.

> [!note] Warum keine konkreten Stunden?
> Damit das Team seine **Intuition** ausbildet. Formalisierung führt zu Streit, Intuition pendelt sich ein.

### 2. Daily Scrum (Standup)

**Wann**: Täglich, gleiche Zeit, gleicher Ort
**Dauer**: Max. 15 Minuten
**Format**: Im Stehen, im Kreis

**Jeder beantwortet drei Fragen:**

1. Was habe ich **gestern** getan/erreicht?
2. Welche **Hindernisse** gab es? (→ Impediment-Log)
3. Was mache ich **heute**?

> [!warning] Wichtig
> Das Daily dient der **gegenseitigen Information**, nicht der Statusabfrage durch einen Chef!

### 3. Sprint Review

**Wann**: Am Ende des Sprints
**Dauer**: Max. 4h für 4-Wochen-Sprint
**Teilnehmer**: Team + Stakeholder

**Inhalt:**
- **Demo** der lauffähigen Software
- Feedback der Stakeholder
- Anpassung des Product Backlogs

> [!tip] Kernprinzip
> Nur **lauffähige Software** wird vorgeführt, keine PowerPoints!

### 4. Sprint Retrospektive

**Wann**: Nach dem Review, vor dem nächsten Planning
**Dauer**: Max. 3h für 4-Wochen-Sprint
**Teilnehmer**: Nur das Scrum-Team

**Fragen:**
- Was lief **gut**?
- Was können wir **verbessern**?
- Was brauchen wir **zusätzlich**?

**Methoden:**
- Start-Stop-Continue
- Mad-Sad-Glad
- Segelboot-Retrospektive

## Sprint-Zyklus Übersicht

```
            ┌──────────────────┐
            │  Product Backlog │
            │  (priorisiert)   │
            └────────┬─────────┘
                     │
        ┌────────────▼────────────┐
        │    SPRINT PLANNING      │
        │  • Planning Poker       │
        │  • Sprint Backlog       │
        └────────────┬────────────┘
                     │
        ┌────────────▼────────────┐
        │       SPRINT            │
        │  ┌──────────────────┐   │
        │  │  Daily Scrum     │   │
        │  │  (täglich)       │   │
        │  └──────────────────┘   │
        │  Entwicklung...         │
        └────────────┬────────────┘
                     │
        ┌────────────▼────────────┐
        │    SPRINT REVIEW        │
        │  • Demo lauffähiger SW  │
        │  • Stakeholder-Feedback │
        └────────────┬────────────┘
                     │
        ┌────────────▼────────────┐
        │  SPRINT RETROSPEKTIVE   │
        │  • Was war gut?         │
        │  • Was verbessern?      │
        └────────────┬────────────┘
                     │
                     └──────▶ Nächster Sprint
```

## Kanban-Board

```
┌─────────────┬─────────────┬─────────────┬─────────────┐
│   TO DO     │  IN PROGRESS│   REVIEW    │    DONE     │
├─────────────┼─────────────┼─────────────┼─────────────┤
│  ┌───────┐  │  ┌───────┐  │  ┌───────┐  │  ┌───────┐  │
│  │Task 1 │  │  │Task 2 │  │  │Task 4 │  │  │Task 6 │  │
│  └───────┘  │  └───────┘  │  └───────┘  │  └───────┘  │
│  ┌───────┐  │  ┌───────┐  │             │  ┌───────┐  │
│  │Task 3 │  │  │Task 5 │  │             │  │Task 7 │  │
│  └───────┘  │  └───────┘  │             │  └───────┘  │
└─────────────┴─────────────┴─────────────┴─────────────┘
```

## Prüfungsrelevanz

> [!question] Typische Prüfungsfragen
> - Welche Events gibt es in Scrum?
> - Was ist Planning Poker und warum wird es verwendet?
> - Was sind die drei Fragen im Daily?
> - Was ist der Unterschied zwischen Review und Retrospektive?

## Querverweise

- → [[01-Scrum-Grundlagen|Scrum-Grundlagen]] – Rollen, Artefakte
- → [[../01-Projektmanagement/01-Grundlagen|Projektmanagement-Grundlagen]] – Kontext
- → [[../03-Dokumentation/01-Projektdokumentation|Projektdokumentation]] – IHK-Anforderungen

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (CC-BY-4.0).
