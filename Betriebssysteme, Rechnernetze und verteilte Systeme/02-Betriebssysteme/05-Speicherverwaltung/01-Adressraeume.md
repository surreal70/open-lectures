---
author: Andreas Hümmer
title: Adressräume
tags:
  - content
  - bs
  - speicher
  - adressraum
  - mmu
  - allokierung
created: '2026-10-07'
modified: '2026-10-07'
bereich: BS
---

# Adressräume

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Unterschied zwischen physischer und logischer Adresse kennen
> - Die Aufgaben der Speicherverwaltung verstehen
> - Die Funktion der MMU (Memory Management Unit) erklären können
> - Die typische Aufteilung eines Adressraums kennen
> - Belegungsstrategien (First-Fit, Best-Fit, etc.) unterscheiden können

---

## Definition

> [!quote] **Formale Definition**
> Ein **Adressraum** ist der Bereich von Speicheradressen, die einem Prozess zur Verfügung stehen. Das Betriebssystem verwaltet die Zuteilung von Speicherbereichen im Hauptspeicher (RAM).

---

## Aufgaben der Speicherverwaltung

```
┌─────────────────────────────────────────────────────────────┐
│              SPEICHERVERWALTUNG                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  1. ADRESSMAPPING                                   │   │
│  │     Logische Adressen → Physikalische Adressen      │   │
│  │     Seiten (Pages) → Bereiche im Hauptspeicher      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  2. BELEGUNGSSTRATEGIE                              │   │
│  │     In welcher Lücke soll Speicher reserviert werden│   │
│  │     Minimierung von Fragmentierung                  │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  3. ERSETZUNGSSTRATEGIE                             │   │
│  │     Welcher Speicherbereich kann sinnvoll           │   │
│  │     ausgelagert werden?                             │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Speicherallokierung

> [!quote] **Definition**
> Das **Reservieren von Speicherbereichen** im Hauptspeicher durch das Betriebssystem nennt man **Allokieren**.

### Eigenschaften

- Jedem Prozess werden während der Ausführung Daten- und Codebereiche zugeteilt
- Die Speicherbereiche eines Prozesses sind **nicht zusammenhängend** im Hauptspeicher verteilt
- Die Speicherbereiche quasi-gleichzeitiger Prozesse sind **voneinander isoliert**
- Allokierung erfolgt beim Programmstart und kann **dynamisch** angepasst werden

```
┌─────────────────────────────────────────────────────────────┐
│                     ARBEITSSPEICHER                         │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────────────┐                                    │
│  │   Betriebssystem    │  ← Reserviert für Kernel          │
│  ├─────────────────────┤                                    │
│  │       frei          │                                    │
│  ├─────────────────────┤                                    │
│  │    Programm A       │  ← Allokiert für Prozess A        │
│  ├─────────────────────┤                                    │
│  │       frei          │  ← Lücke (Fragmentierung)         │
│  ├─────────────────────┤                                    │
│  │    Programm B       │                                    │
│  ├─────────────────────┤                                    │
│  │       frei          │                                    │
│  ├─────────────────────┤                                    │
│  │    Programm C       │                                    │
│  ├─────────────────────┤                                    │
│  │    Programm D       │                                    │
│  └─────────────────────┘                                    │
└─────────────────────────────────────────────────────────────┘
```

---

## Physische vs. Logische Adresse

```
┌─────────────────────────────────────────────────────────────┐
│              ADRESSUMRECHNUNG                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Programm                                                  │
│   ┌─────────────────┐                                       │
│   │  Logische       │     MMU        Physischer            │
│   │  Adresse        │──────────────▶ Speicher              │
│   │  (virtuell)     │   (Memory     ┌─────────────────┐    │
│   │                 │   Management  │  Physische      │    │
│   │  z.B. 0x1000    │   Unit)       │  Adresse        │    │
│   └─────────────────┘               │  z.B. 0x5A000   │    │
│                                     └─────────────────┘    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

| Adresstyp | Beschreibung |
|-----------|--------------|
| **Physische Adresse** | Reale, am Adressbus anliegende Adresse der Speicherzelle |
| **Logische Adresse** | Virtuelle, auf Startpunkt 0 bezogene Adresse, wird durch MMU in physische Adresse umgerechnet |

---

## Belegungsstrategien

Durch ständiges Allokieren und Freigeben entstehen **Lücken** (Fragmentierung).

```
Situation: Neuer Prozess benötigt 15 KB

┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  Lücke 1: 20 KB    Lücke 2: 15 KB    Lücke 3: 30 KB        │
│  ┌──────────┐      ┌──────────┐      ┌──────────────┐      │
│  │          │      │          │      │              │      │
│  │  20 KB   │      │  15 KB   │      │    30 KB     │      │
│  │          │      │          │      │              │      │
│  └──────────┘      └──────────┘      └──────────────┘      │
│       ▲                 ▲                   ▲               │
│  First-Fit         Best-Fit           Worst-Fit            │
│  (erste passende)  (genau passend)    (größte Lücke)       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

| Strategie | Beschreibung | Vor-/Nachteile |
|-----------|--------------|----------------|
| **First-Fit** | Erste passende Lücke | Schnell, aber Fragmentierung am Anfang |
| **Next-Fit** | Nächste passende Lücke (ab letzter Position) | Verteilt Fragmentierung |
| **Best-Fit** | Kleinste passende Lücke | Minimale Verschwendung, aber langsam |
| **Worst-Fit** | Größte Lücke | Große Reste bleiben nutzbar |

---

## Speicherschutz

> [!danger] **Wichtig**
> Es muss sichergestellt werden, dass Prozesse **nicht auf den Speicherbereich anderer Prozesse** zugreifen können!

Der Speicherschutz wird gewährleistet durch:
- **MMU** (Memory Management Unit) in der CPU
- **Grenzregister** (Base & Limit Register)

```
┌─────────────────────────────────────────────────────────────┐
│              SPEICHERSCHUTZ MIT GRENZREGISTERN              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Prozess will auf Adresse 0x1234 zugreifen:                │
│                                                             │
│  ┌────────────┐    Prüfung:                                 │
│  │   Base     │    Adresse >= Base?                         │
│  │  0x1000    │    Adresse < Base + Limit?                  │
│  ├────────────┤                                             │
│  │   Limit    │    Wenn ja → Zugriff erlaubt               │
│  │  0x2000    │    Wenn nein → Trap (Speicherverletzung)   │
│  └────────────┘                                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Typischer Adressraum eines Prozesses

```
┌─────────────────────────────────────────────────────────────┐
│                  PROZESS-ADRESSRAUM                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Hohe Adressen ──────────────────────────────────▶         │
│                                                             │
│   ┌─────────────────────────────────────────────────┐      │
│   │              STACK                               │      │
│   │         (wächst nach unten ↓)                    │      │
│   │    Lokale Variablen, Rücksprungadressen         │      │
│   ├─────────────────────────────────────────────────┤      │
│   │                                                 │      │
│   │              (freier Bereich)                   │      │
│   │                                                 │      │
│   ├─────────────────────────────────────────────────┤      │
│   │              HEAP                               │      │
│   │         (wächst nach oben ↑)                    │      │
│   │    Dynamisch allokierter Speicher (malloc)     │      │
│   ├─────────────────────────────────────────────────┤      │
│   │              BSS                                │      │
│   │    Uninitialisierte globale Variablen          │      │
│   ├─────────────────────────────────────────────────┤      │
│   │              DATA                               │      │
│   │    Initialisierte globale Variablen            │      │
│   ├─────────────────────────────────────────────────┤      │
│   │              TEXT (CODE)                        │      │
│   │    Programmcode (read-only)                    │      │
│   └─────────────────────────────────────────────────┘      │
│                                                             │
│   Niedrige Adressen ──────────────────────────────▶        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Speichergrößen – Historischer Überblick

| System | Typischer Speicher |
|--------|-------------------|
| C64 | 64 KB |
| Arduino (ATMEL) | 128 KB |
| IBM PC/XT | 512 KB – 640 KB |
| 32-Bit CPU (adressierbar) | 4 GB (2³²) |
| Moderne Desktop (64-Bit) | 8 – 128 GB |
| Moderne Server | 2 – 8 TB |
| 64-Bit CPU (theoretisch) | 18 Millionen TB (2⁶⁴) |

---

## Zusammenhänge

- [[02-Virtueller-Speicher|Virtueller Speicher]] → Erweiterung des Adressraums
- [[03-Paging|Paging]] → Speicheraufteilung in Pages
- [[04-Segmentierung|Segmentierung]] → Alternative Speicherorganisation

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - Unterschied physische vs. logische Adresse
> - Aufgaben der Speicherverwaltung
> - Belegungsstrategien (First-Fit, Best-Fit, Worst-Fit)
> - Funktion der MMU
> - Speicherschutz und Grenzregister

> [!question] **Häufige Prüfungsfragen**
> 1. Was ist der Unterschied zwischen physischer und logischer Adresse?
> 2. Erklären Sie die Funktion der MMU!
> 3. Vergleichen Sie die Belegungsstrategien First-Fit und Best-Fit!
> 4. Wie wird der Speicherschutz zwischen Prozessen gewährleistet?
> 5. Was versteht man unter Fragmentierung?

> [!tip] **Merkhilfen**
> - **First-Fit** = "Erste freie Parklücke nehmen"
> - **Best-Fit** = "Perfekt passende Parklücke suchen"
> - **Worst-Fit** = "Größte Parklücke nehmen"
> - **MMU** = "Übersetzer" zwischen virtuell und physisch

---

## Weiterführende Ressourcen

> [!note] **Videos (YouTube)**
> - CoreDumped – Memory Access

---

## Quellen

- IU Skript: Betriebssysteme, Rechnernetze und verteilte Systeme - Teil 5 (Ressourcen)
- Tanenbaum: Modern Operating Systems
