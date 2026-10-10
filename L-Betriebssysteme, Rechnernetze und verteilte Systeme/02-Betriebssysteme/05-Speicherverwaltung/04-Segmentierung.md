---
author: Andreas Hümmer
title: Segmentierung
tags:
  - content
  - bs
  - speicher
  - segmentierung
  - segment-table
created: '2026-10-07'
modified: '2026-10-07'
bereich: BS
---

# Segmentierung

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das Konzept der Segmentierung verstehen und von Paging unterscheiden können
> - Wissen, wie Segmente den logischen Programmaufbau widerspiegeln
> - Die Adressumrechnung bei Segmentierung erklären können
> - Vor- und Nachteile gegenüber Paging kennen
> - Das Konzept der kombinierten Segmentierung mit Paging verstehen

---

## Definition

> [!quote] **Formale Definition**
> **Segmentierung** unterteilt den Adressraum in logische Einheiten (**Segmente**) unterschiedlicher Größe. Jedes Segment repräsentiert eine logische Einheit des Programms (Code, Daten, Stack, etc.).

---

## Grundkonzept

```
┌─────────────────────────────────────────────────────────────┐
│              SEGMENTIERUNG – KONZEPT                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Programmsicht                    Physischer Speicher      │
│   (logische Segmente)              (beliebige Platzierung)  │
│                                                             │
│   ┌─────────────────┐              ┌─────────────────────┐  │
│   │ Segment 0: Code │──────────────│█████████████████████│  │
│   │    (4 KB)       │              ├─────────────────────┤  │
│   ├─────────────────┤              │                     │  │
│   │ Segment 1: Daten│───────┐      ├─────────────────────┤  │
│   │    (2 KB)       │       └─────▶│███████████          │  │
│   ├─────────────────┤              ├─────────────────────┤  │
│   │ Segment 2: Stack│──────┐       │                     │  │
│   │    (1 KB)       │      │       ├─────────────────────┤  │
│   ├─────────────────┤      └──────▶│█████                │  │
│   │ Segment 3: Heap │───┐          ├─────────────────────┤  │
│   │    (8 KB)       │   └─────────▶│█████████████████████│  │
│   └─────────────────┘              │█████████████████████│  │
│                                    └─────────────────────┘  │
│                                                             │
│   Jedes Segment hat VARIABLE Größe (anders als bei Paging!) │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Segmentierung vs. Paging

| Eigenschaft | Segmentierung | Paging |
|-------------|---------------|--------|
| **Einheitsgröße** | Variabel | Fest (z.B. 4 KB) |
| **Sichtbarkeit** | Dem Programmierer bekannt | Für Programmierer transparent |
| **Logische Struktur** | Spiegelt Programmaufbau wider | Keine logische Bedeutung |
| **Fragmentierung** | Extern (zwischen Segmenten) | Intern (innerhalb Pages) |
| **Schutz** | Pro Segment (logisch sinnvoll) | Pro Page |
| **Sharing** | Einfach (ganze Segmente) | Komplex (einzelne Pages) |

---

## Adressumrechnung

Eine **logische Adresse** bei Segmentierung besteht aus:
- **Segmentnummer** (s)
- **Offset** innerhalb des Segments (d)

```
┌─────────────────────────────────────────────────────────────┐
│              ADRESSUMRECHNUNG BEI SEGMENTIERUNG             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Logische Adresse:                                         │
│   ┌───────────────┬────────────────┐                        │
│   │ Segment (s)   │   Offset (d)   │                        │
│   └───────┬───────┴────────┬───────┘                        │
│           │                │                                │
│           ▼                │                                │
│   ┌───────────────────┐    │                                │
│   │  SEGMENT TABLE    │    │                                │
│   ├───────┬───────────┤    │                                │
│   │ Seg 0 │Base│Limit │    │                                │
│   │ Seg 1 │Base│Limit │◀───┘                                │
│   │ Seg 2 │Base│Limit │                                     │
│   └───────┴──┬────┬───┘                                     │
│              │    │                                         │
│         Base │    │ Limit                                   │
│              │    │                                         │
│              ▼    ▼                                         │
│         ┌────────────┐                                      │
│         │ d < Limit? │──── NEIN ──▶ TRAP (Speicherfehler)   │
│         └─────┬──────┘                                      │
│               │ JA                                          │
│               ▼                                             │
│   Physische Adresse = Base + d                              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Segment Table

```
┌─────────────────────────────────────────────────────────────┐
│                    SEGMENT TABLE                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Segment │  Base   │  Limit  │ Protection │ Present        │
│   ────────┼─────────┼─────────┼────────────┼──────────      │
│      0    │ 0x4000  │  4096   │   R/X      │    1           │
│      1    │ 0x6000  │  2048   │   R/W      │    1           │
│      2    │ 0x8800  │  1024   │   R/W      │    1           │
│      3    │ 0xA000  │  8192   │   R/W      │    1           │
│                                                             │
│   Base:       Startadresse im physischen Speicher           │
│   Limit:      Maximale Größe des Segments                   │
│   Protection: Zugriffsrechte (Read/Write/Execute)           │
│   Present:    Segment im Speicher geladen?                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Externe Fragmentierung

Das Hauptproblem der Segmentierung:

```
┌─────────────────────────────────────────────────────────────┐
│              EXTERNE FRAGMENTIERUNG                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Nach mehrmaligem Laden/Entladen von Segmenten:            │
│                                                             │
│   ┌─────────────────────────────────────────────────────┐   │
│   │████████│      │███│        │██████│    │████│       │   │
│   │ Seg A  │ frei │ B │  frei  │ Seg C│frei│ D  │ frei  │   │
│   │  8 KB  │ 3 KB │2KB│  6 KB  │ 5 KB │2KB │3KB │ 4 KB  │   │
│   └─────────────────────────────────────────────────────┘   │
│                                                             │
│   Neues Segment E mit 10 KB:                                │
│   → Kein zusammenhängender Block frei!                      │
│   → Aber: 3+6+2+4 = 15 KB freier Speicher insgesamt         │
│                                                             │
│   Lösung: KOMPAKTIERUNG (Defragmentierung)                  │
│   ┌─────────────────────────────────────────────────────┐   │
│   │████████│███│██████│████│                            │   │
│   │ Seg A  │ B │ Seg C│ D  │         FREI               │   │
│   └─────────────────────────────────────────────────────┘   │
│                                                             │
│   Problem: Kompaktierung ist teuer (alle Segmente kopieren) │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Kombination: Segmentierung mit Paging

Moderne Systeme kombinieren oft beide Ansätze:

```
┌─────────────────────────────────────────────────────────────┐
│              SEGMENTIERUNG + PAGING                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Logische Adresse:                                         │
│   ┌─────────┬───────────┬────────────┐                      │
│   │ Segment │ Page Nr.  │   Offset   │                      │
│   └────┬────┴─────┬─────┴──────┬─────┘                      │
│        │          │            │                            │
│        ▼          │            │                            │
│   ┌──────────┐    │            │                            │
│   │ Segment  │    │            │                            │
│   │  Table   │    │            │                            │
│   └────┬─────┘    │            │                            │
│        │          │            │                            │
│        ▼          ▼            │                            │
│   ┌──────────────────┐         │                            │
│   │    Page Table    │         │                            │
│   │  (pro Segment)   │         │                            │
│   └────────┬─────────┘         │                            │
│            │                   │                            │
│            ▼                   ▼                            │
│   ┌─────────────────────────────────┐                       │
│   │      Physische Adresse          │                       │
│   │     Frame + Offset              │                       │
│   └─────────────────────────────────┘                       │
│                                                             │
│   Vorteile:                                                 │
│   • Logische Struktur durch Segmente                        │
│   • Keine externe Fragmentierung durch Paging               │
│   • Schutz auf Segment- UND Page-Ebene                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Intel x86 Segmentierung

Die x86-Architektur nutzt Segmentierung historisch bedingt:

```
┌─────────────────────────────────────────────────────────────┐
│              x86 SEGMENTREGISTER                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   CS  - Code Segment      (für Programmcode)                │
│   DS  - Data Segment      (für Daten)                       │
│   SS  - Stack Segment     (für Stack)                       │
│   ES  - Extra Segment     (zusätzliches Datensegment)       │
│   FS  - (ab 386)          (Thread-Local Storage)            │
│   GS  - (ab 386)          (Thread-Local Storage)            │
│                                                             │
│   Moderne Betriebssysteme (Linux, Windows):                 │
│   → Nutzen "Flat Memory Model" (alle Segmente = 0 bis 4GB)  │
│   → Segmentierung wird effektiv umgangen                    │
│   → Paging übernimmt die Speicherverwaltung                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Zusammenhänge

- [[03-Paging|Paging]] → Alternative/Ergänzung zur Segmentierung
- [[01-Adressraeume|Adressräume]] → Segmente strukturieren den Adressraum
- [[02-Virtueller-Speicher|Virtueller Speicher]] → Segmente können ausgelagert werden

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - Unterschied Segmentierung vs. Paging
> - Adressumrechnung bei Segmentierung (Base + Offset)
> - Externe vs. interne Fragmentierung
> - Aufbau der Segment Table
> - Kombination von Segmentierung und Paging

> [!question] **Häufige Prüfungsfragen**
> 1. Was ist der Unterschied zwischen Segmentierung und Paging?
> 2. Wie erfolgt die Adressumrechnung bei Segmentierung?
> 3. Was ist externe Fragmentierung und warum tritt sie bei Segmentierung auf?
> 4. Welche Informationen enthält ein Segment-Table-Eintrag?
> 5. Warum kombinieren moderne Systeme Segmentierung mit Paging?

> [!tip] **Merkhilfen**
> - **Segment** = "Kapitel eines Buches" (logische Einheit, variable Länge)
> - **Page** = "Buchseite" (feste Größe, keine logische Bedeutung)
> - **Externe Fragmentierung** = "Lücken zwischen Büchern im Regal"
> - **Interne Fragmentierung** = "Leere Seiten am Ende eines Kapitels"

---

## Weiterführende Ressourcen

> [!note] **Videos (YouTube)**
>
> | | Video | Beschreibung |
> |---|-------|--------------|
> | 🎬 | [CoreDumped – Memory Access](https://www.youtube.com/watch?v=A9WLYbE0p-I) | Speicherorganisation und Adressierung |

---

## Quellen

- Tanenbaum: Modern Operating Systems
- Intel x86 Architecture Manual
