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
modified: '2026-10-29'
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

| Dimension | Verfahren | Beschreibung |
|-----------|-----------|--------------|
| **Frequenz** | FDMA | Jeder Teilnehmer erhält eigenen Frequenzbereich |
| **Zeit** | TDMA | Jeder Teilnehmer erhält Zeitschlitze |
| **Code** | CDMA | Unterscheidung durch eindeutige Codes |
| **Raum** | SDMA | Räumliche Trennung durch Zellen/Beamforming |

## FDMA – Frequency Division Multiple Access

> [!quote] Definition
> Bei **FDMA** erhält jeder Teilnehmer einen eigenen Frequenzbereich (Kanal), der exklusiv für ihn reserviert ist.

### Prinzip

![[fdma-prinzip.png]]
*<span class="fig-id">03-07-05-fdma-prinzip</span>: FDMA – jeder Teilnehmer erhält einen exklusiven Frequenzbereich über die gesamte Zeit.*

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

![[tdma-prinzip.png]]
*<span class="fig-id">03-07-05-tdma-prinzip</span>: TDMA – alle Teilnehmer teilen sich eine Frequenz, aber erhalten periodisch zugewiesene Zeitschlitze.*

### Eigenschaften

| Vorteil | Nachteil |
|---------|----------|
| Effizientere Frequenznutzung | Synchronisation erforderlich |
| Dynamische Slot-Zuweisung möglich | Burst-Übertragung (nicht kontinuierlich) |
| Weniger Hardware (ein Transceiver) | Guard Times zwischen Slots nötig |

### GSM-Beispiel

GSM kombiniert FDMA und TDMA:

![[gsm-fdma-tdma.png]]
*<span class="fig-id">03-07-05-gsm-fdma-tdma</span>: GSM kombiniert FDMA (mehrere Kanäle) mit TDMA (8 Zeitschlitze pro Kanal).*

## CDMA – Code Division Multiple Access

> [!quote] Definition
> Bei **CDMA** senden alle Teilnehmer gleichzeitig auf derselben Frequenz. Die Unterscheidung erfolgt durch **eindeutige Codes** (Spreizsequenzen), mit denen das Signal moduliert wird.

### Prinzip

![[cdma-prinzip.png]]
*<span class="fig-id">03-07-05-cdma-prinzip</span>: CDMA – alle Sender übertragen gleichzeitig auf derselben Frequenz, Unterscheidung durch individuelle Codes.*

### Spreizspektrum-Verfahren

**Direct Sequence Spread Spectrum (DSSS):**

![[dsss-spreading.png]]
*<span class="fig-id">03-07-05-dsss-spreading</span>: DSSS-Verfahren – das Datenbit wird mit einem Chip-Code multipliziert und über ein breiteres Frequenzband gespreizt.*

- Jedes Datenbit wird mit einem Chip-Code (z.B. 64 Chips) multipliziert
- Signal wird über breites Frequenzband "gespreizt"
- Empfänger kennt Code und kann Signal "entspreizen"
- Andere Codes erscheinen als Rauschen

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

![[sdma-cells.png]]
*<span class="fig-id">03-07-05-sdma-cells</span>: SDMA – Frequenzwiederverwendung durch räumliche Trennung in Zellen. Gleiche Frequenzgruppen mit ausreichendem Abstand.*

### Cluster-Größe

| Cluster-Größe | Frequenzwiederholung | Kapazität | Interferenz |
|---------------|---------------------|-----------|-------------|
| 3 | Hoch | Hoch | Hoch |
| 7 | Mittel | Mittel | Mittel |
| 12 | Gering | Gering | Gering |

### Moderne SDMA: Beamforming

In 5G wird SDMA durch **Beamforming** erweitert:

![[beamforming.png]]
*<span class="fig-id">03-07-05-beamforming</span>: Beamforming in 5G – gerichtete Strahlen zu einzelnen Nutzern ermöglichen räumliche Trennung auf derselben Frequenz.*

## OFDMA – Orthogonal Frequency Division Multiple Access

> [!info] OFDMA
> OFDMA ist eine moderne Kombination, die in **LTE** und **WLAN (802.11ax)** verwendet wird. Es kombiniert FDMA und TDMA mit orthogonalen Unterträgern.

### Prinzip

![[ofdma-grid.png]]
*<span class="fig-id">03-07-05-ofdma-grid</span>: OFDMA Resource Grid – flexible Zuweisung von Frequenz-Zeit-Blöcken (Resource Blocks) an verschiedene Nutzer.*

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
