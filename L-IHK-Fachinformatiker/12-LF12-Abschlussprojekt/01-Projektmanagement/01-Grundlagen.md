---
title: "Projektmanagement-Grundlagen"
created: 2026-10-13
modified: 2026-10-13
type: lecture
tags:
  - lf12
  - projektmanagement
  - projekt
  - wasserfall
  - stakeholder
source: proTirone (CC-BY-4.0)
---

# Projektmanagement-Grundlagen

> [!info] Lernziele
> - Projekt vs. Linientätigkeit unterscheiden
> - Projektrollen kennen
> - Wasserfallmodell verstehen und kritisieren

## Projekt vs. Linientätigkeit

| Kriterium | Projekt | Linientätigkeit |
|-----------|---------|-----------------|
| **Art** | Vorhaben | Routine |
| **Ende** | Dezidiertes Ende | Wiederholbar |
| **Ziel** | Einzigartig | Gleichartig |
| **Prozess** | Unbekannt | Bekannt |

> [!note] Definition
> Ein **Projekt** ist ein zeitlich begrenztes Vorhaben mit einzigartigem Ziel und unbekanntem Herstellungsprozess.

## Projektrollen

```
┌─────────────────────────────────────────────────────┐
│                 PROJECT GOVERNANCE                   │
├──────────────────┬──────────────────────────────────┤
│  Projekteignerin │ Zielentscheiderin, Gesicht nach  │
│                  │ außen                            │
├──────────────────┼──────────────────────────────────┤
│  Projektsponsorin│ Geldgeberin, Zielentscheiderin   │
├──────────────────┼──────────────────────────────────┤
│  Stakeholder     │ Nachgelagerte Beeinflusser       │
├──────────────────┼──────────────────────────────────┤
│  Steering        │ Formalisierter Einfluss          │
│  Committee       │                                  │
├──────────────────┼──────────────────────────────────┤
│  Projektmanagerin│ Ausführende Leiterin, Gesicht    │
│                  │ nach innen                       │
└──────────────────┴──────────────────────────────────┘
```

### Stakeholder

**Stakeholder** sind alle Personen oder Gruppen, die ein Interesse am Projekt haben:

- **Intern**: Geschäftsführung, Fachabteilungen, IT-Abteilung
- **Extern**: Kunden, Lieferanten, Behörden
- **Positiv**: Unterstützer, Nutznießer
- **Negativ**: Betroffene, Konkurrenz

## Projektmanagement-Standards

### GPM (Deutsche Gesellschaft für Projektmanagement)

- Fokus auf „Wie" und Definitionen
- Kommt vom Wasserfallmodell
- Deutsch ausgerichtet
- [gpm-ipma.de](https://www.gpm-ipma.de/)

### PMI (Project Management Institute)

- Fokus auf Prozesse und Begriffe
- Kommt vom Wasserfallmodell
- International ausgerichtet
- [pmi.org](https://www.pmi.org/)

## Das Wasserfallmodell

### Prinzip

Jede Phase wird abgeschlossen, bevor die nächste beginnt. Ergebnisse werden an die nächste Phase „über den Zaun geworfen".

```
┌──────────────────┐
│ Projektmanagement│
└────────┬─────────┘
         ↓
┌──────────────────┐
│ Funktionales     │
│ Design           │
└────────┬─────────┘
         ↓
┌──────────────────┐
│ Technisches      │
│ Design           │
└────────┬─────────┘
         ↓
┌──────────────────┐
│ Programmierung   │
└────────┬─────────┘
         ↓
┌──────────────────┐
│ Testen           │
└────────┬─────────┘
         ↓
┌──────────────────┐
│ Deployment       │
└──────────────────┘
```

### Nachteile des Wasserfallmodells

> [!warning] Probleme
> - **Lange abgeschlossene Zyklen**: Keine frühe Rückmeldung
> - **Spät erkennbarer Änderungsbedarf**: Fehler werden erst am Ende sichtbar
> - **Formalistisches Wiederansetzen**: Änderungen sind teuer
> - **Aufwendiges Restaffing**: Wechselnde Teams pro Phase
> - **Reibungsverluste**: Viel geht bei Übergabe verloren
> - **Von Wirklichkeit überholt**: Markt ändert sich während des Projekts

## Moderne Alternativen

- **Agile Methoden**: Scrum, Kanban
- **Hybride Ansätze**: Wasserfall + agile Elemente
- **DevOps**: Entwicklung und Betrieb integriert

> [!tip] Empfehlung
> Für IT-Projekte mit unklaren Anforderungen: **Agile Methoden** (→ Scrum)

## Prüfungsrelevanz

> [!question] Typische Prüfungsfragen
> - Was unterscheidet ein Projekt von einer Linientätigkeit?
> - Welche Projektrollen gibt es?
> - Nennen Sie Nachteile des Wasserfallmodells
> - Was sind Stakeholder?

## Querverweise

- → [[../02-Scrum/01-Scrum-Grundlagen|Scrum-Grundlagen]] – Agile Alternative
- → [[../02-Scrum/02-Scrum-Prozess|Scrum-Prozess]] – Sprint-Ablauf
- → [[../03-Dokumentation/01-Projektdokumentation|Projektdokumentation]] – IHK-Anforderungen

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (CC-BY-4.0).
