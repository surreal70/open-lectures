---
author: Andreas Hümmer
title: Virtueller Speicher
tags:
  - content
  - bs
  - speicher
  - virtual-memory
  - swapping
  - demand-paging
created: '2026-10-07'
modified: '2026-10-07'
bereich: BS
---

# Virtueller Speicher

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das Konzept des virtuellen Speichers verstehen
> - Swapping und Demand Paging erklären können
> - Die Speicherhierarchie kennen
> - Verstehen, wie mehr Speicher genutzt werden kann als physisch vorhanden
> - Page Faults und das Working Set Konzept kennen

---

## Definition

> [!quote] **Formale Definition**
> **Virtueller Speicher** ist eine Technik, die den Hauptspeicher durch Auslagern auf die Festplatte erweitert. Mehrere Pages können derselben Kachel entsprechen – aktuell nicht benötigte Pages sind zwischenzeitlich auf die Festplatte ausgelagert.

---

## Grundprinzip

```
┌─────────────────────────────────────────────────────────────┐
│              VIRTUELLER SPEICHER                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Programm sieht:            Realität:                      │
│   ┌───────────────┐          ┌────────────────────────────┐ │
│   │               │          │   RAM (physisch)           │ │
│   │   Virtueller  │          │   ┌─────┬─────┬─────┐      │ │
│   │   Adressraum  │    ┌────▶│   │Page │Page │Page │      │ │
│   │               │    │     │   │ 1   │ 3   │ 5   │      │ │
│   │   (z.B. 8 GB) │    │     │   └─────┴─────┴─────┘      │ │
│   │               │    │     │                            │ │
│   │   Page 1 ─────┼────┘     │   Festplatte (Swap)        │ │
│   │   Page 2 ─────┼─────────▶│   ┌─────┬─────┬─────┐      │ │
│   │   Page 3 ─────┼────┐     │   │Page │Page │Page │      │ │
│   │   ...         │    │     │   │ 2   │ 4   │ 6   │      │ │
│   │               │    └────▶│   └─────┴─────┴─────┘      │ │
│   └───────────────┘          └────────────────────────────┘ │
│                                                             │
│   Vorteil: Programm kann mehr Speicher nutzen als           │
│            physisch vorhanden ist!                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Speicherhierarchie

```
┌─────────────────────────────────────────────────────────────┐
│              SPEICHERHIERARCHIE                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ▲ Geschwindigkeit                      Kapazität ▲         │
│  │                                                │         │
│  │  ┌─────────────────────┐   < 1 ns              │         │
│  │  │     REGISTER        │   (CPU-intern)        │         │
│  │  └──────────┬──────────┘                       │         │
│  │             │                                  │         │
│  │  ┌──────────▼──────────┐   wenige ns           │         │
│  │  │       CACHE         │   (L1, L2, L3)        │         │
│  │  └──────────┬──────────┘                       │         │
│  │             │                                  │         │
│  │  ┌──────────▼──────────┐   ≈ 60 ns             │         │
│  │  │   VORDERGRUNDSPEICHER│   RAM/ROM            │         │
│  │  │   (Hauptspeicher)   │                       │         │
│  │  └──────────┬──────────┘                       │         │
│  │             │                                  │         │
│  │  ┌──────────▼──────────┐   SSD: µs, HDD: ms    │         │
│  │  │   HINTERGRUNDSPEICHER│   HDD, SSD           │         │
│  │  └──────────┬──────────┘                       │         │
│  │             │                                  │         │
│  │  ┌──────────▼──────────┐   Sekunden            │         │
│  │  │   WECHSELSPEICHER   │   Band, DVD, USB      │         │
│  │  └──────────┬──────────┘                       │         │
│  │             │                                  │         │
│  │  ┌──────────▼──────────┐   Sekunden+           │         │
│  │  │   NETZWERKSPEICHER  │   LAN, Cloud          │         │
│  │  └─────────────────────┘                       │         │
│  │                                                ▼         │
│  ▼ Kosten                                   Kosten ▼        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

| Speicherart | Typische Zugriffszeit | Typische Größe |
|-------------|----------------------|----------------|
| Register | < 1 ns | Bytes |
| L1 Cache | 1-2 ns | 32-64 KB |
| L2 Cache | 3-10 ns | 256 KB - 1 MB |
| L3 Cache | 10-20 ns | 4-50 MB |
| RAM | ≈ 60 ns | 8-128 GB |
| SSD | µs | 256 GB - 4 TB |
| HDD | ms | 1-20 TB |

---

## Swapping und Demand Paging

### Swapping

Auslagern ganzer Prozesse auf die Festplatte.

```
┌─────────────────────────────────────────────────────────────┐
│                      SWAPPING                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│     RAM                           Swap (Festplatte)         │
│  ┌─────────────┐                  ┌─────────────┐           │
│  │  Prozess A  │  ◀── Swap In ─── │  Prozess C  │           │
│  │  Prozess B  │  ─── Swap Out ─▶ │  (wartend)  │           │
│  │  (frei)     │                  │             │           │
│  └─────────────┘                  └─────────────┘           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Demand Paging

Pages werden erst bei Bedarf geladen (Lazy Loading).

```
┌─────────────────────────────────────────────────────────────┐
│                   DEMAND PAGING                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. Prozess greift auf Page zu                              │
│                                                             │
│  2. Page im RAM?                                            │
│        │                                                    │
│        ├── JA  → Zugriff erfolgt                            │
│        │                                                    │
│        └── NEIN → PAGE FAULT!                               │
│                      │                                      │
│                      ▼                                      │
│              ┌───────────────┐                              │
│              │ Page von      │                              │
│              │ Festplatte    │                              │
│              │ laden         │                              │
│              └───────┬───────┘                              │
│                      │                                      │
│                      ▼                                      │
│              Prozess wird fortgesetzt                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Page Fault

> [!quote] **Definition**
> Ein **Page Fault** (Seitenfehler) tritt auf, wenn ein Prozess auf eine Speicherseite zugreift, die sich nicht im physischen Hauptspeicher befindet.

### Ablauf bei Page Fault

1. **Trap** → CPU löst Interrupt aus
2. **Betriebssystem** prüft, ob Zugriff gültig
3. **Freien Frame** finden (ggf. Page ersetzen)
4. **Page einlesen** von Festplatte
5. **Page Table aktualisieren**
6. **Prozess fortsetzen**

> [!warning] **Achtung**
> Page Faults sind **teuer**: Ein Festplattenzugriff dauert Millionen mal länger als ein RAM-Zugriff!

---

## Working Set

> [!quote] **Definition**
> Das **Working Set** eines Prozesses ist die Menge der Seiten, die der Prozess in einem bestimmten Zeitfenster aktiv nutzt.

```
┌─────────────────────────────────────────────────────────────┐
│                    WORKING SET                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Zeit ───────────────────────────────────────────────▶      │
│                                                             │
│  Zugriffe: P1 P2 P1 P3 P2 P1 P4 P5 P4 P5 P6 P5              │
│                                                             │
│  Fenster (Δ=3):                                             │
│            ├───────┤                                        │
│            P1 P2 P1  → Working Set = {P1, P2}               │
│                                                             │
│                    ├───────┤                                │
│                    P4 P5 P4  → Working Set = {P4, P5}       │
│                                                             │
│  Wenn Working Set > verfügbarer RAM → Thrashing!            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Thrashing

Wenn das Working Set aller Prozesse größer ist als der verfügbare RAM, entstehen ständige Page Faults → **Thrashing** (System verbringt mehr Zeit mit Paging als mit Arbeit).

---

## Zusammenhänge

- [[01-Adressraeume|Adressräume]] → Virtueller Speicher erweitert den Adressraum
- [[03-Paging|Paging]] → Umsetzung des virtuellen Speichers
- [[04-Segmentierung|Segmentierung]] → Alternative/Ergänzung zu Paging

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - Konzept des virtuellen Speichers
> - Unterschied Swapping vs. Demand Paging
> - Page Fault und dessen Behandlung
> - Speicherhierarchie (Zugriffszeiten!)
> - Working Set und Thrashing

> [!question] **Häufige Prüfungsfragen**
> 1. Was ist virtueller Speicher und welche Vorteile bietet er?
> 2. Was passiert bei einem Page Fault?
> 3. Erklären Sie die Speicherhierarchie!
> 4. Was versteht man unter Thrashing und wie kann es vermieden werden?
> 5. Was ist der Unterschied zwischen Swapping und Demand Paging?

> [!tip] **Merkhilfen**
> - **Virtueller Speicher** = "Mehr Platz als da ist" (wie Zaubertrick)
> - **Page Fault** = "Seite nicht gefunden – bitte warten"
> - **Thrashing** = "System schwitzt vor Paging"
> - **Working Set** = "Was der Prozess gerade braucht"

---

## Weiterführende Ressourcen

> [!note] **Videos (YouTube)**
> - CoreDumped – Stack
> - CoreDumped – Heap
> - CoreDumped – Memory Access

---

## Quellen

- IU Skript: Betriebssysteme, Rechnernetze und verteilte Systeme - Teil 5 (Ressourcen)
- Tanenbaum: Modern Operating Systems
