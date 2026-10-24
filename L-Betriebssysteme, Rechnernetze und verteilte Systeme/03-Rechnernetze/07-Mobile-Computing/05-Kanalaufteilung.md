---
author: Andreas Hümmer
title: Kanalaufteilung im Funkbereich
tags:
  - content
  - rn
  - mobile-computing
  - multiplexing
  - fdma
  - tdma
  - cdma
  - ofdma
created: '2026-10-24'
modified: '2026-10-24'
bereich: RN
---

# Kanalaufteilung im Funkbereich

## Lernziele

> [!ziel] Lernziele
> Nach diesem Kapitel können Sie:
> - Das Problem der Kanalaufteilung im Funk erklären
> - Die vier Multiplexing-Verfahren (FDMA, TDMA, CDMA, SDMA) unterscheiden
> - OFDMA als moderne Kombination verstehen
> - Verfahren den Mobilfunkgenerationen zuordnen

## Das Problem: Shared Medium

> [!important] Geteiltes Medium
> Bei Funknetzen teilen sich **alle Teilnehmer denselben Frequenzbereich**. Anders als bei Kabeln kann nicht jeder Teilnehmer seine eigene physische Leitung haben.

**Frage:** Wie können mehrere Kanäle im selben Funkbereich realisiert werden?

**Lösung:** Multiplexing – Aufteilung der Ressourcen nach verschiedenen Dimensionen:

```
┌─────────────────────────────────────────────────────────────┐
│              Dimensionen der Kanalaufteilung                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐      │
│   │Frequenz │  │  Zeit   │  │  Code   │  │  Raum   │      │
│   │ (FDMA)  │  │ (TDMA)  │  │ (CDMA)  │  │ (SDMA)  │      │
│   └─────────┘  └─────────┘  └─────────┘  └─────────┘      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## FDMA – Frequency Division Multiple Access

> [!quote] Definition
> Bei **FDMA** erhält jeder Teilnehmer einen eigenen Frequenzbereich (Kanal), der exklusiv für ihn reserviert ist.

### Prinzip

```
Frequenz ▲
         │
    f4   │  ████████████████████████  Teilnehmer D
         │
    f3   │  ████████████████████████  Teilnehmer C
         │
    f2   │  ████████████████████████  Teilnehmer B
         │
    f1   │  ████████████████████████  Teilnehmer A
         │
         └──────────────────────────────────────► Zeit
```

### Eigenschaften

| Vorteil | Nachteil |
|---------|----------|
| Einfache Implementierung | Ineffizient bei geringer Auslastung |
| Keine Synchronisation nötig | Feste Bandbreitenzuweisung |
| Kontinuierliche Übertragung | Schutzabstände zwischen Kanälen nötig |

### Anwendung

- Analoges Radio/TV (UKW, DVB-T)
- Erstes Mobilfunknetz (1G/AMPS)
- Kombiniert mit anderen Verfahren (z.B. GSM: FDMA + TDMA)

## TDMA – Time Division Multiple Access

> [!quote] Definition
> Bei **TDMA** teilen sich alle Teilnehmer dieselbe Frequenz, aber jeder bekommt **Zeitschlitze (Time Slots)** zugewiesen, in denen er senden darf.

### Prinzip

```
Frequenz ▲
         │
         │  ┌──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┐
    f    │  │A │B │C │D │A │B │C │D │A │B │C │D │
         │  └──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┘
         │
         └──────────────────────────────────────► Zeit
              Frame 1    Frame 2    Frame 3
```

### Eigenschaften

| Vorteil | Nachteil |
|---------|----------|
| Effizientere Frequenznutzung | Synchronisation erforderlich |
| Dynamische Slot-Zuweisung möglich | Burst-Übertragung (nicht kontinuierlich) |
| Weniger Hardware (ein Transceiver) | Guard Times zwischen Slots nötig |

### GSM-Beispiel

GSM kombiniert FDMA und TDMA:

```
┌─────────────────────────────────────────────────────────────┐
│                  GSM: FDMA + TDMA                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Frequenz ▲                                                 │
│           │  ┌──┬──┬──┬──┬──┬──┬──┬──┐                     │
│  Kanal 3  │  │1 │2 │3 │4 │5 │6 │7 │8 │  8 Zeitschlitze    │
│           │  └──┴──┴──┴──┴──┴──┴──┴──┘                     │
│           │  ┌──┬──┬──┬──┬──┬──┬──┬──┐                     │
│  Kanal 2  │  │1 │2 │3 │4 │5 │6 │7 │8 │                     │
│           │  └──┴──┴──┴──┴──┴──┴──┴──┘                     │
│           │  ┌──┬──┬──┬──┬──┬──┬──┬──┐                     │
│  Kanal 1  │  │1 │2 │3 │4 │5 │6 │7 │8 │                     │
│           │  └──┴──┴──┴──┴──┴──┴──┴──┘                     │
│           └──────────────────────────────────────► Zeit     │
│                                                             │
│  Jeder GSM-Kanal hat 200 kHz Bandbreite                    │
│  8 Zeitschlitze pro Frame (4,615 ms)                       │
│  1 Teilnehmer = 1 Frequenz + 1 Zeitschlitz                 │
└─────────────────────────────────────────────────────────────┘
```

## CDMA – Code Division Multiple Access

> [!quote] Definition
> Bei **CDMA** senden alle Teilnehmer gleichzeitig auf derselben Frequenz. Die Unterscheidung erfolgt durch **eindeutige Codes** (Spreizsequenzen), mit denen das Signal moduliert wird.

### Prinzip

```
┌─────────────────────────────────────────────────────────────┐
│                      CDMA-Prinzip                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Sender A: Daten × Code_A ──────┐                          │
│                                  │                          │
│  Sender B: Daten × Code_B ──────┼──► Überlagertes Signal   │
│                                  │       im Funkkanal       │
│  Sender C: Daten × Code_C ──────┘                          │
│                                                             │
│                        │                                    │
│                        ▼                                    │
│                                                             │
│  Empfänger: Signal × Code_A ──► Nur Daten von A            │
│             (Korrelation)                                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Spreizspektrum-Verfahren

**Direct Sequence Spread Spectrum (DSSS):**
- Jedes Datenbit wird mit einem Chip-Code (z.B. 64 Chips) multipliziert
- Signal wird über breites Frequenzband "gespreizt"
- Empfänger kennt Code und kann Signal "entspreizen"

```
Datenbit:     1
Chip-Code:    1 0 1 1 0 1 0 0 (8 Chips)
Gesendetes:   1 0 1 1 0 1 0 0

→ Bandbreite wird um Faktor 8 erhöht
→ Andere Codes erscheinen als Rauschen
```

### Eigenschaften

| Vorteil | Nachteil |
|---------|----------|
| Hohe Kapazität | Komplexe Signalverarbeitung |
| Inherente Verschlüsselung | Near-Far-Problem |
| Soft Handover möglich | Präzise Leistungsregelung nötig |
| Robust gegen Interferenzen | |

### Near-Far-Problem

> [!warning] Near-Far-Problem
> Ein naher, starker Sender kann das Signal eines fernen, schwachen Senders überlagern. Lösung: Dynamische Leistungsregelung.

### Anwendung

- UMTS (3G) – W-CDMA
- GPS – Alle Satelliten senden auf gleicher Frequenz
- IS-95 (cdmaOne)

## SDMA – Space Division Multiple Access

> [!quote] Definition
> Bei **SDMA** werden die Sendebereiche in **räumliche Zellen** unterteilt. Zellen mit ausreichendem Abstand können dieselbe Frequenz wiederverwenden.

### Prinzip: Frequenzwiederverwendung

```
┌─────────────────────────────────────────────────────────────┐
│              Zelluläres Netz mit SDMA                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│         ╱╲      ╱╲      ╱╲      ╱╲                         │
│        ╱ 1╲    ╱ 2╲    ╱ 3╲    ╱ 1╲                        │
│       ╱    ╲  ╱    ╲  ╱    ╲  ╱    ╲                       │
│       ╲    ╱  ╲    ╱  ╲    ╱  ╲    ╱                       │
│        ╲ 4╱╲ 5╱╲ 6╱╲ 7╱╲ 4╱╲ 5╱                           │
│         ╲╱  ╲╱  ╲╱  ╲╱  ╲╱  ╲╱                            │
│         ╱╲  ╱╲  ╱╲  ╱╲  ╱╲  ╱╲                            │
│        ╱ 2╲╱ 3╲╱ 1╲╱ 2╲╱ 3╲╱ 1╲                           │
│                                                             │
│  Zahlen = Frequenzgruppen                                  │
│  Gleiche Zahlen = gleiche Frequenz (mit räumlichem Abstand)│
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Cluster-Größe

| Cluster-Größe | Frequenzwiederholung | Kapazität | Interferenz |
|---------------|---------------------|-----------|-------------|
| 3 | Hoch | Hoch | Hoch |
| 7 | Mittel | Mittel | Mittel |
| 12 | Gering | Gering | Gering |

### Moderne SDMA: Beamforming

In 5G wird SDMA durch **Beamforming** erweitert:

```
┌─────────────────────────────────────────────────────────────┐
│                    Beamforming (5G)                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                     Antenne (MIMO-Array)                    │
│                          ║║║║                               │
│                         ╱    ╲                              │
│                        ╱      ╲                             │
│                       ╱        ╲                            │
│                      ╱    📱    ╲                           │
│                     ╱   Beam 1   ╲                          │
│                    ╱              ╲                         │
│                   ╱                ╲                        │
│                             📱                              │
│                           Beam 2                            │
│                                                             │
│  Gerichtete Strahlen zu einzelnen Nutzern                  │
│  Gleiche Frequenz, aber räumlich getrennt                  │
└─────────────────────────────────────────────────────────────┘
```

## OFDMA – Orthogonal Frequency Division Multiple Access

> [!info] OFDMA
> OFDMA ist eine moderne Kombination, die in **LTE** und **WLAN (802.11ax)** verwendet wird. Es kombiniert FDMA und TDMA mit orthogonalen Unterträgern.

### Prinzip

```
┌─────────────────────────────────────────────────────────────┐
│                   OFDMA Resource Grid                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Frequenz ▲                                                 │
│           │  ┌──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┐        │
│  Subcarr. │  │A │A │B │B │C │A │A │B │C │C │D │D │        │
│     12    │  ├──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┤        │
│     11    │  │A │A │B │B │C │A │B │B │C │C │D │D │        │
│     10    │  ├──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┤        │
│      9    │  │A │B │B │C │C │A │B │B │C │D │D │D │        │
│      .    │  ├──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┤        │
│      .    │  │  │  │  │  │  │  │  │  │  │  │  │  │        │
│           └──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──► Zeit │
│               Slot 1    Slot 2    Slot 3    Slot 4         │
│                                                             │
│  A, B, C, D = Verschiedene Nutzer                          │
│  Jeder Nutzer bekommt Resource Blocks (RB)                 │
└─────────────────────────────────────────────────────────────┘
```

### Vorteile

- Flexible Ressourcenzuweisung
- Robust gegen Mehrwegausbreitung
- Hohe spektrale Effizienz
- Dynamische Anpassung an Kanalqualität

## Vergleichsübersicht

| Verfahren | Dimension | Synchronisation | Mobilfunk-Einsatz |
|-----------|-----------|-----------------|-------------------|
| **FDMA** | Frequenz | Keine | 1G (AMPS) |
| **TDMA** | Zeit | Erforderlich | 2G (GSM) |
| **CDMA** | Code | Präzise | 3G (UMTS) |
| **SDMA** | Raum | Keine | Alle (Zellen) |
| **OFDMA** | Frequenz + Zeit | Erforderlich | 4G (LTE), 5G |

## Prüfungsrelevanz

> [!warning] **Prüfungsrelevant**
> - Unterschied FDMA, TDMA, CDMA, SDMA
> - Prinzip der Frequenzwiederverwendung (Zellen)
> - GSM nutzt FDMA + TDMA
> - UMTS nutzt W-CDMA
> - LTE nutzt OFDMA

> [!question] Typische Prüfungsfragen
> - Erklären Sie den Unterschied zwischen FDMA und TDMA.
> - Wie funktioniert das Spreizspektrum-Verfahren bei CDMA?
> - Was ist das Near-Far-Problem?
> - Warum können benachbarte Zellen nicht dieselbe Frequenz verwenden?
> - Welches Multiplexing-Verfahren verwendet LTE?

## Zusammenhänge

- [[01-Einfuehrung]] – Grundlagen Mobile Computing
- [[04-Funknetze]] – Mobilfunktechnologien
- [[../04-Bitübertragungsschicht/02-Signale|Signale]] – Signalverarbeitung
- [[../05-Sicherungsschicht/03-MAC-Protokolle|MAC-Protokolle]] – Medienzugriff

## Quellen

- Schiller, J.: Mobile Communications
- Rappaport, T.: Wireless Communications
- 3GPP Specifications
- IEEE 802.11 Standards

---

*Dateiende*
