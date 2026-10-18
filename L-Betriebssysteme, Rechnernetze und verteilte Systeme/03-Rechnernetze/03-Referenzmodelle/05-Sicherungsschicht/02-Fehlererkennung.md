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

**Fehlererkennung (Error Detection)**
- Erkennt, **dass** ein Fehler aufgetreten ist
- Frame wird verworfen
- Neuübertragung durch höhere Schicht (z.B. TCP)
- Weniger Redundanz nötig
- Beispiele: CRC, Prüfsumme

**Fehlerkorrektur (Error Correction / FEC)**
- Erkennt **und korrigiert** Fehler
- Keine Neuübertragung nötig
- Mehr Redundanz erforderlich
- Beispiele: Hamming-Code, Reed-Solomon
- Einsatz: Speicher (ECC-RAM), CDs, Satellitenkommunikation

> [!info] Ethernet-Strategie
> Ethernet verwendet **Fehlererkennung** (CRC) — die Korrektur übernimmt TCP durch Retransmission.

## CRC – Cyclic Redundancy Check

### Funktionsweise

CRC behandelt die Daten als großes Polynom und dividiert durch ein Generator-Polynom. Der Rest dieser Division ist die Prüfsumme.

**Sender:**
1. Daten als Polynom $D(x)$ interpretieren
2. Mit $x^n$ multiplizieren ($n$ Nullbits anhängen, wobei $n$ = Grad des Generators)
3. Division durch Generator-Polynom $G(x)$ mittels XOR
4. Rest $R(x)$ = CRC-Wert
5. Übertragen: $D(x) \cdot x^n + R(x)$

**Empfänger:**
- Empfangene Daten durch $G(x)$ dividieren
- Rest $= 0$ → Kein Fehler erkannt
- Rest $\neq 0$ → Fehler erkannt, Frame verwerfen

**Beispiel mit CRC-4 (vereinfacht):**

| Schritt | Wert |
|---------|------|
| Daten | `1101011` |
| Generator $G(x)$ | `10011` (Grad 4) |
| Daten × $x^4$ | `11010110000` |
| XOR-Division | Rest: `1110` |
| **Übertragen** | `11010111110` |

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

**Gerade Parität (Even Parity):**
- Anzahl der 1-Bits + Paritätsbit = **gerade**
- Daten: `1101001` (4 Einsen) → Parität: `0` → `11010010`
- Daten: `1101011` (5 Einsen) → Parität: `1` → `11010111`

**Ungerade Parität (Odd Parity):**
- Anzahl der 1-Bits + Paritätsbit = **ungerade**

> [!warning] Einschränkungen
> - Erkennt nur **Einzelbitfehler**
> - Erkennt **keine** geradzahligen Mehrbitfehler
> - Keine Korrektur möglich

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

| Schicht | Prüfung | Bei Fehler |
|---------|---------|------------|
| **L2 (Ethernet)** | CRC-32 (FCS) | Frame verwerfen |
| **L3 (IP)** | Header Checksum (nur Header!) | Paket verwerfen |
| **L4 (TCP)** | Checksum (Header + Daten) | Segment verwerfen, Retransmission anfordern |
| **L4 (UDP)** | Checksum (optional in IPv4) | Datagramm verwerfen (keine Retransmission) |

> [!tip] Mehrfache Prüfung
> Die mehrfache Prüfung auf verschiedenen Schichten erhöht die Zuverlässigkeit der Datenübertragung.

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
