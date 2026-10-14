---
author: Andreas Hümmer
title: Fehlererkennung
tags:
  - vorlesung
  - rn
  - layer2
  - crc
  - fcs
  - fehlererkennung
created: '2026-10-07'
modified: '2026-10-13'
bereich: RN
---

# Fehlererkennung

## Lernziele

> [!ziel] Nach diesem Kapitel können Sie...
> - Den Unterschied zwischen Fehlererkennung und Fehlerkorrektur erklären
> - Das CRC-Verfahren in Grundzügen beschreiben
> - Die Funktion der Frame Check Sequence (FCS) erläutern
> - Weitere Prüfsummenverfahren benennen

## Fehlerarten

Bei der Datenübertragung können verschiedene Fehler auftreten:

| Fehlerart | Beschreibung | Ursache |
|-----------|--------------|---------|
| **Einzelbitfehler** | Ein Bit wird verfälscht | Rauschen, Störung |
| **Burst-Fehler** | Mehrere aufeinanderfolgende Bits | Blitzschlag, Interferenz |
| **Verlust** | Frame kommt nicht an | Kollision, Überlastung |

## Fehlererkennung vs. Fehlerkorrektur

```
┌─────────────────────────────────────────────────────────────────┐
│          FEHLERERKENNUNG vs. FEHLERKORREKTUR                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   FEHLERERKENNUNG (Error Detection)                            │
│   ─────────────────────────────────                            │
│   • Erkennt, DASS ein Fehler aufgetreten ist                   │
│   • Frame wird verworfen                                       │
│   • Neuübertragung durch höhere Schicht (z.B. TCP)            │
│   • Weniger Redundanz nötig                                    │
│   • Beispiel: CRC, Prüfsumme                                   │
│                                                                 │
│   FEHLERKORREKTUR (Error Correction / FEC)                     │
│   ────────────────────────────────────────                     │
│   • Erkennt UND korrigiert Fehler                              │
│   • Keine Neuübertragung nötig                                 │
│   • Mehr Redundanz erforderlich                                │
│   • Beispiel: Hamming-Code, Reed-Solomon                       │
│   • Einsatz: Speicher (ECC-RAM), CDs, Satellit                │
│                                                                 │
│   Ethernet verwendet Fehlererkennung (CRC) –                   │
│   Korrektur übernimmt TCP durch Retransmission                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## CRC – Cyclic Redundancy Check

### Funktionsweise

CRC behandelt die Daten als großes Polynom und dividiert durch ein Generator-Polynom. Der Rest dieser Division ist die Prüfsumme.

```
┌─────────────────────────────────────────────────────────────────┐
│                    CRC PRINZIP                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   1. Sender                                                     │
│      • Daten als Polynom D(x) interpretieren                   │
│      • Mit x^n multiplizieren (n Nullbits anhängen)            │
│      • Division durch Generator G(x) mittels XOR               │
│      • Rest R(x) = CRC-Wert                                    │
│      • Übertragen: D(x) · x^n + R(x)                          │
│                                                                 │
│   2. Empfänger                                                  │
│      • Empfangene Daten durch G(x) dividieren                  │
│      • Rest = 0 → Kein Fehler erkannt                          │
│      • Rest ≠ 0 → Fehler erkannt, Frame verwerfen             │
│                                                                 │
│   Beispiel mit CRC-4 (vereinfacht):                            │
│   ─────────────────────────────────                            │
│   Daten:     1101011                                           │
│   Generator: 10011 (CRC-4 Polynom)                             │
│                                                                 │
│   11010110000 ÷ 10011                                          │
│   = ... (XOR-Division)                                         │
│   Rest: 1110 → CRC                                             │
│                                                                 │
│   Übertragen: 11010111110                                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### CRC-Varianten

| CRC | Bits | Generator-Polynom | Anwendung |
|-----|------|-------------------|-----------|
| CRC-8 | 8 | 0x07 | ATM, I²C |
| CRC-16 | 16 | 0x8005 | USB, Modbus |
| CRC-32 | 32 | 0x04C11DB7 | **Ethernet**, ZIP |
| CRC-64 | 64 | diverse | HDLC |

### CRC-32 in Ethernet

> [!info] Ethernet FCS
> Ethernet verwendet **CRC-32** im Frame Check Sequence (FCS) Feld.
> 
> - Länge: 4 Bytes (32 Bit)
> - Berechnet über: Dst MAC, Src MAC, Type/Length, Payload
> - Generator: 0x04C11DB7
> 
> Eigenschaften:
> - Erkennt alle Einzelbitfehler
> - Erkennt alle Doppelbitfehler
> - Erkennt alle Burst-Fehler ≤ 32 Bit
> - Erkennt >99,99% aller längeren Fehler

## Andere Prüfverfahren

### Parität

```
┌─────────────────────────────────────────────────────────────────┐
│                    PARITÄT                                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Gerade Parität (Even Parity):                                │
│   • Anzahl der 1-Bits + Paritätsbit = gerade                   │
│   • Daten: 1101001 → Parität: 0 → 11010010                    │
│   • Daten: 1101011 → Parität: 1 → 11010111                    │
│                                                                 │
│   Ungerade Parität (Odd Parity):                               │
│   • Anzahl der 1-Bits + Paritätsbit = ungerade                 │
│                                                                 │
│   Einschränkungen:                                              │
│   • Erkennt nur Einzelbitfehler                                │
│   • Erkennt keine geradzahligen Mehrbitfehler                  │
│   • Keine Korrektur möglich                                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Prüfsummen (Checksum)

| Verfahren | Beschreibung | Anwendung |
|-----------|--------------|-----------|
| **Internet Checksum** | 16-Bit Einerkomplement-Summe | IP, TCP, UDP |
| **Fletcher** | Verbesserte Prüfsumme | ISO |
| **Adler-32** | Schnelle Prüfsumme | zlib |

> [!warning] Unterschied CRC vs. Checksum
> - **Checksum**: Einfache Summe, schnell zu berechnen
> - **CRC**: Polynomielle Division, erkennt mehr Fehlerarten
> 
> Ethernet (L2) nutzt CRC, IP/TCP (L3/4) nutzen einfache Checksums.

## Fehlererkennung in der Praxis

```
┌─────────────────────────────────────────────────────────────────┐
│          FEHLERBEHANDLUNG IM PROTOKOLL-STACK                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Schicht      Prüfung          Bei Fehler                      │
│   ──────      ────────          ──────────                      │
│                                                                 │
│   L2 (Eth)    CRC-32 (FCS)     Frame verwerfen                 │
│                                                                 │
│   L3 (IP)     Header Checksum   Paket verwerfen                │
│               (nur Header!)                                     │
│                                                                 │
│   L4 (TCP)    Checksum          Segment verwerfen,             │
│               (Header+Daten)    Retransmission anfordern       │
│                                                                 │
│   L4 (UDP)    Checksum          Datagramm verwerfen            │
│               (optional v4)     (keine Retransmission)         │
│                                                                 │
│   Mehrfache Prüfung erhöht Zuverlässigkeit!                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Zusammenfassung

> [!zusammenfassung] Kernpunkte
> - **Fehlererkennung** erkennt Fehler, **Fehlerkorrektur** behebt sie
> - Ethernet nutzt **CRC-32** im FCS-Feld
> - CRC erkennt Einzelbit-, Doppelbit- und Burst-Fehler zuverlässig
> - Bei erkannten Fehlern wird der Frame verworfen
> - Neuübertragung erfolgt durch höhere Schichten (TCP)

## Prüfungsrelevanz

> [!pruefung] Prüfungstipps
> - Verstehen Sie den Unterschied Fehlererkennung vs. -korrektur
> - Wissen Sie, dass Ethernet CRC-32 verwendet
> - Kennen Sie die Position des FCS im Frame (am Ende)

## Verwandte Themen

- [[01-Rahmenbildung]] – Ethernet-Frame mit FCS
- [[../07-Transportschicht/01-TCP|TCP]] – Retransmission bei Fehlern

## Quellen

- Vorlesungsskript „Betriebssysteme, Rechnernetze und verteilte Systeme", Andreas Hümmer, IU 2025
