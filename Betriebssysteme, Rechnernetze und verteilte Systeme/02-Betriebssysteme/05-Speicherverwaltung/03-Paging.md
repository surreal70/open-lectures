---
author: Andreas Hümmer
title: Paging
tags:
  - content
  - bs
  - speicher
  - paging
  - page-table
  - tlb
created: '2026-10-07'
modified: '2026-10-07'
bereich: BS
---

# Paging

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das Paging-Konzept mit Pages und Frames verstehen
> - Die Funktion der Page Table erklären können
> - Den TLB (Translation Lookaside Buffer) kennen
> - Page-Ersetzungsalgorithmen verstehen (FIFO, LRU, etc.)
> - Die Adressumrechnung bei Paging nachvollziehen können

---

## Definition

> [!quote] **Formale Definition**
> **Paging** ist eine Speicherverwaltungstechnik, bei der der virtuelle Adressraum in gleich große Blöcke (**Pages**) und der physische Speicher in gleich große Blöcke (**Frames/Kacheln**) unterteilt wird.

---

## Grundkonzept

```
┌─────────────────────────────────────────────────────────────┐
│                    PAGING-KONZEPT                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Virtueller Adressraum         Physischer Speicher         │
│   (eines Prozesses)             (RAM)                       │
│                                                             │
│   ┌─────────────┐               ┌─────────────┐             │
│   │   Page 0    │───────────────│   Frame 2   │             │
│   ├─────────────┤               ├─────────────┤             │
│   │   Page 1    │───────┐       │   Frame 1   │             │
│   ├─────────────┤       │       ├─────────────┤             │
│   │   Page 2    │──┐    │       │   Frame 5   │             │
│   ├─────────────┤  │    │       ├─────────────┤             │
│   │   Page 3    │──┼────┼──┐    │   Frame 0   │             │
│   ├─────────────┤  │    │  │    ├─────────────┤             │
│   │   Page 4    │──┼────┼──┼───▶│   Frame 3   │             │
│   └─────────────┘  │    │  │    ├─────────────┤             │
│                    │    │  └───▶│   Frame 4   │             │
│                    │    └──────▶├─────────────┤             │
│                    └───────────▶│   Frame 6   │             │
│                                 └─────────────┘             │
│                                                             │
│   Typische Page-Größe: 4 KB                                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

| Begriff | Beschreibung |
|---------|--------------|
| **Page** | Block im virtuellen Adressraum |
| **Frame (Kachel)** | Block im physischen Speicher |
| **Page Table** | Tabelle, die Pages auf Frames abbildet |
| **Page Size** | Typisch 4 KB (kann auch 4 MB, 1 GB sein) |

---

## Page Table

Jeder Prozess hat eine eigene **Page Table**, die die Zuordnung von Pages zu Frames speichert.

```
┌─────────────────────────────────────────────────────────────┐
│                    PAGE TABLE                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Page │ Valid │ Frame │ Modified │ Referenced │ Protection │
│   ─────┼───────┼───────┼──────────┼────────────┼─────────── │
│     0  │   1   │   2   │    0     │     1      │   R/W      │
│     1  │   1   │   5   │    1     │     1      │   R/W      │
│     2  │   0   │   -   │    -     │     -      │    -       │  ← nicht im RAM
│     3  │   1   │   1   │    0     │     0      │   R        │
│     4  │   1   │   3   │    1     │     1      │   R/W      │
│                                                             │
│   Valid Bit:    1 = Page ist im RAM, 0 = auf Festplatte     │
│   Modified Bit: 1 = Page wurde verändert (Dirty Bit)        │
│   Referenced:   1 = Page wurde kürzlich zugegriffen         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Adressumrechnung

Eine virtuelle Adresse besteht aus **Page Number** und **Offset**:

```
┌─────────────────────────────────────────────────────────────┐
│              ADRESSUMRECHNUNG BEI PAGING                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Virtuelle Adresse (z.B. 32 Bit):                           │
│  ┌────────────────────────┬───────────────────┐             │
│  │     Page Number        │      Offset       │             │
│  │      (20 Bit)          │     (12 Bit)      │             │
│  └──────────┬─────────────┴────────┬──────────┘             │
│             │                      │                        │
│             ▼                      │                        │
│      ┌────────────┐                │                        │
│      │ Page Table │                │                        │
│      │  Lookup    │                │                        │
│      └─────┬──────┘                │                        │
│            │                       │                        │
│            ▼                       │                        │
│  Physische Adresse:                │                        │
│  ┌────────────────────────┬────────┴──────────┐             │
│  │     Frame Number       │      Offset       │             │
│  │      (20 Bit)          │     (12 Bit)      │             │
│  └────────────────────────┴───────────────────┘             │
│                                                             │
│  Bei 4 KB Pages: Offset = 12 Bit (2^12 = 4096 Bytes)        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Rechenbeispiel

```
Page-Größe: 4 KB = 4096 Bytes = 2^12 → 12 Bit Offset

Virtuelle Adresse: 0x00001234
  Page Number: 0x00001 = 1
  Offset:      0x234   = 564

Page Table: Page 1 → Frame 5

Physische Adresse:
  Frame Number: 5 = 0x005
  Offset: 0x234 (unverändert)
  → 0x00005234
```

---

## TLB – Translation Lookaside Buffer

Die Page Table liegt im RAM → jeder Speicherzugriff erfordert zwei RAM-Zugriffe (Page Table + Daten).

**Lösung**: Der **TLB** ist ein schneller Cache für Page-Table-Einträge.

```
┌─────────────────────────────────────────────────────────────┐
│              TLB (TRANSLATION LOOKASIDE BUFFER)             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                   Virtuelle Adresse                         │
│                         │                                   │
│                         ▼                                   │
│                   ┌───────────┐                             │
│                   │    TLB    │  ← Schneller Cache          │
│                   │  (64-1024 │    (in CPU integriert)      │
│                   │  Einträge)│                             │
│                   └─────┬─────┘                             │
│                         │                                   │
│            ┌────────────┼────────────┐                      │
│            │            │            │                      │
│         TLB Hit      TLB Miss                               │
│            │            │                                   │
│            ▼            ▼                                   │
│     Physische     ┌───────────┐                             │
│     Adresse       │Page Table │                             │
│     direkt        │ (im RAM)  │                             │
│                   └─────┬─────┘                             │
│                         │                                   │
│                         ▼                                   │
│                   Physische Adresse                         │
│                   + TLB Update                              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

| Ereignis | Zugriffszeit |
|----------|--------------|
| TLB Hit | ≈ 1 ns (nur TLB) |
| TLB Miss | ≈ 100 ns (RAM + Update) |
| Page Fault | ≈ 10 ms (Festplatte!) |

---

## Mehrstufige Page Tables

Bei großen Adressräumen wird die Page Table selbst sehr groß. Lösung: **Hierarchische Page Tables**.

```
┌─────────────────────────────────────────────────────────────┐
│              ZWEISTUFIGE PAGE TABLE                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Virtuelle Adresse:                                         │
│  ┌────────────┬────────────┬────────────┐                   │
│  │  Dir Index │Page Index  │  Offset    │                   │
│  │   10 Bit   │  10 Bit    │  12 Bit    │                   │
│  └──────┬─────┴──────┬─────┴─────┬──────┘                   │
│         │            │           │                          │
│         ▼            │           │                          │
│   ┌───────────┐      │           │                          │
│   │  Page     │      │           │                          │
│   │ Directory │      │           │                          │
│   └─────┬─────┘      │           │                          │
│         │            │           │                          │
│         ▼            ▼           │                          │
│   ┌───────────────────┐          │                          │
│   │    Page Table     │          │                          │
│   │    (eine von      │          │                          │
│   │     1024)         │          │                          │
│   └─────────┬─────────┘          │                          │
│             │                    │                          │
│             ▼                    ▼                          │
│   ┌──────────────────────────────────┐                      │
│   │        Frame + Offset            │                      │
│   │      = Physische Adresse         │                      │
│   └──────────────────────────────────┘                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Page-Ersetzungsalgorithmen

Wenn alle Frames belegt sind und eine neue Page geladen werden muss:

| Algorithmus | Beschreibung | Eigenschaften |
|-------------|--------------|---------------|
| **FIFO** | First In, First Out | Einfach, aber Belady's Anomalie |
| **LRU** | Least Recently Used | Optimal, aber aufwendig |
| **LFU** | Least Frequently Used | Häufigkeit zählen |
| **Clock/Second Chance** | FIFO mit Referenced-Bit | Guter Kompromiss |
| **OPT** | Optimaler Algorithmus | Theoretisch, nicht praktikabel |

### Clock-Algorithmus

```
┌─────────────────────────────────────────────────────────────┐
│              CLOCK-ALGORITHMUS                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                      ┌─────┐                                │
│                ┌─────│  R  │─────┐                          │
│                │     └──┬──┘     │                          │
│           ┌────┴────┐   │   ┌────┴────┐                     │
│           │ Page 1  │   │   │ Page 2  │                     │
│           │  R=1    │   │   │  R=0    │ ← Opfer             │
│           └────┬────┘   │   └────┬────┘                     │
│                │        │        │                          │
│           ┌────┴────────┴────────┴────┐                     │
│           │         Zeiger            │                     │
│           │            ↓              │                     │
│           └────┬────────────────┬─────┘                     │
│           ┌────┴────┐      ┌────┴────┐                      │
│           │ Page 4  │      │ Page 3  │                      │
│           │  R=1    │      │  R=1    │                      │
│           └─────────┘      └─────────┘                      │
│                                                             │
│   R=1: Referenced (kürzlich benutzt) → R auf 0 setzen       │
│   R=0: Nicht referenced → Opfer für Ersetzung               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Zusammenhänge

- [[01-Adressraeume|Adressräume]] → Paging teilt den Adressraum auf
- [[02-Virtueller-Speicher|Virtueller Speicher]] → Paging ermöglicht virtuellen Speicher
- [[04-Segmentierung|Segmentierung]] → Alternative/Ergänzung zu Paging

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - Page und Frame Konzept
> - Aufbau und Inhalt der Page Table
> - Adressumrechnung bei Paging berechnen
> - TLB und dessen Funktion
> - Page-Ersetzungsalgorithmen (FIFO, LRU, Clock)

> [!question] **Häufige Prüfungsfragen**
> 1. Rechnen Sie eine virtuelle Adresse in eine physische um!
> 2. Was ist der TLB und warum ist er wichtig?
> 3. Erklären Sie den Clock-Algorithmus zur Page-Ersetzung!
> 4. Was ist der Unterschied zwischen einer Page und einem Frame?
> 5. Welche Informationen enthält ein Page-Table-Eintrag?

> [!tip] **Merkhilfen**
> - **Page** = "Buchseite" (virtuell)
> - **Frame** = "Bilderrahmen" (physisch, nimmt Page auf)
> - **TLB** = "Telefonbuch-Cache" (schnelles Nachschlagen)
> - **Clock** = "Uhrzeiger dreht, bis R=0 gefunden"

---

## Quellen

- IU Skript: Betriebssysteme, Rechnernetze und verteilte Systeme - Teil 5 (Ressourcen)
- Tanenbaum: Modern Operating Systems
