---
title: "Scrum-Grundlagen"
created: 2026-10-13
modified: 2026-10-13
type: lecture
tags:
  - lf12
  - scrum
  - agil
  - projektmanagement
  - sprint
source: proTirone (CC-BY-4.0)
---

# Scrum-Grundlagen

> [!info] Lernziele
> - Scrum-Rollen kennen
> - Scrum-Artefakte verstehen
> - Unterschied zum Wasserfallmodell erklären

## Was ist Scrum?

**Scrum** ist ein agiles Framework für die iterative Produktentwicklung.

> [!note] Herkunft
> Scrum entstand aus dem Unwohlsein von Web-Entwicklern mit dem traditionellen Projektmanagement. Es ist im Kern ein **Time & Material**-Beauftragungsmodell.

### Kernprinzipien

- **Iterativ**: Kleine Feedbackschleifen (Sprints)
- **Inkrementell**: Funktionsfähiges Produkt nach jedem Sprint
- **Selbstorganisiert**: Team entscheidet über Arbeitsweise
- **Transparent**: Alle Informationen sind sichtbar

## Die drei Scrum-Rollen

```
┌─────────────────────────────────────────────────────────┐
│                    SCRUM-TEAM                           │
├─────────────────┬─────────────────┬─────────────────────┤
│  PRODUCT OWNER  │  SCRUM MASTER   │   DEVELOPERS        │
├─────────────────┼─────────────────┼─────────────────────┤
│ • Definiert     │ • Überwacht     │ • Setzen Tasks um   │
│   Anforderungen │   Scrum-Regeln  │ • Organisieren sich │
│ • Priorisiert   │ • Pflegt        │   selbst            │
│   Backlog       │   Kanban-Board  │ • Entscheiden       │
│ • Definiert     │ • Entfernt      │   technische        │
│   "Done"        │   Hindernisse   │   Umsetzung         │
│                 │ • Sorgt für     │ • Schätzen Aufwand  │
│                 │   Informations- │                     │
│                 │   fluss         │                     │
└─────────────────┴─────────────────┴─────────────────────┘
```

### Product Owner

- **Verantwortlich für**: Produktvision, Anforderungen
- **Pflegt**: Product Backlog
- **Definiert**: Definition of Done (messbar an lauffähiger Software)
- **Priorisiert**: Backlog-Einträge
- **Bestimmt NICHT**: Wer wann was tut

### Scrum Master

- **Verantwortlich für**: Einhaltung der Scrum-Regeln
- **Pflegt**: Kanban-Board, Impediment-Log
- **Sorgt für**: Informationsfluss, Beseitigung von Hindernissen
- **Bestimmt NICHT**: Wer wann was tut

### Development Team (Developers)

- **Selbstorganisiert**: Entscheiden Arbeitsweise und Aufteilung
- **Technische Verantwortung**: Entscheiden Art der Umsetzung
- **Commitment**: Nehmen so viele Tasks, wie sie schaffen können

## Scrum-Artefakte

### Product Backlog

- **Was**: Priorisierte Liste aller Anforderungen
- **Wer pflegt**: Product Owner
- **Inhalt**: User Stories, Features, Bugs, technische Schulden

### Sprint Backlog

- **Was**: Tasks für den aktuellen Sprint
- **Wer pflegt**: Development Team
- **Inhalt**: Von oben aus dem Product Backlog entnommene Items

### Increment

- **Was**: Funktionsfähiges Produktinkrement
- **Wann**: Am Ende jedes Sprints
- **Qualität**: Muss Definition of Done erfüllen

## Definition of Done (DoD)

> [!tip] Wichtig
> Die **Definition of Done** ist ein gemeinsames Verständnis darüber, wann ein Backlog-Item „fertig" ist.

**Beispiel DoD:**
- [ ] Code geschrieben und committed
- [ ] Unit-Tests vorhanden und grün
- [ ] Code-Review durchgeführt
- [ ] Dokumentation aktualisiert
- [ ] Auf Testumgebung deployed
- [ ] Vom PO abgenommen

## Scrum vs. Wasserfall

| Aspekt | Wasserfall | Scrum |
|--------|------------|-------|
| **Planung** | Vorab komplett | Iterativ |
| **Anforderungen** | Fest | Änderbar |
| **Feedback** | Am Ende | Nach jedem Sprint |
| **Teams** | Wechselnd pro Phase | Stabil |
| **Dokumentation** | Umfangreich | Minimal notwendig |
| **Lieferung** | Am Ende | Inkrementell |

## Prüfungsrelevanz

> [!question] Typische Prüfungsfragen
> - Welche drei Rollen gibt es in Scrum?
> - Was ist der Unterschied zwischen Product Backlog und Sprint Backlog?
> - Was ist die Definition of Done?
> - Wer entscheidet über die technische Umsetzung?

## Querverweise

- → [[02-Scrum-Prozess|Scrum-Prozess]] – Sprint-Ablauf, Events
- → [[../01-Projektmanagement/01-Grundlagen|Projektmanagement-Grundlagen]] – Wasserfall
- → [[../03-Dokumentation/01-Projektdokumentation|Projektdokumentation]] – IHK-Anforderungen

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (CC-BY-4.0).
