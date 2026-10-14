---
author: Andreas Hümmer
title: Signale und Codierung
tags:
  - vorlesung
  - rn
  - layer1
  - codierung
  - modulation
  - signale
created: '2026-10-07'
modified: '2026-10-13'
bereich: RN
---

# Signale und Codierung

## Lernziele

> [!ziel] Nach diesem Kapitel können Sie...
> - Den Unterschied zwischen Leitungs- und Kanalcodierung erklären
> - Die wichtigsten Leitungscodierungen (Manchester, 4B5B, 8B10B) beschreiben
> - Die Begriffe Bandbreite, Baudrate und Bitrate unterscheiden
> - Das Shannon-Theorem anwenden
> - Modulationsverfahren (AM, FM, PM, QAM) erläutern

## Grundbegriffe

### Bandbreite und Datenrate

```
┌─────────────────────────────────────────────────────────────────┐
│                    GRUNDBEGRIFFE                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Bandbreite (B)                                                │
│   • Frequenzbereich eines Übertragungskanals                   │
│   • Einheit: Hertz (Hz)                                        │
│   • Beispiel: Telefonleitung ≈ 3100 Hz (300-3400 Hz)          │
│                                                                 │
│   Baudrate (Symbolrate)                                         │
│   • Anzahl der Signaländerungen pro Sekunde                    │
│   • Einheit: Baud (Bd)                                         │
│   • 1 Symbol kann mehrere Bits kodieren                        │
│                                                                 │
│   Bitrate (Datenrate)                                           │
│   • Anzahl übertragener Bits pro Sekunde                       │
│   • Einheit: bit/s (bps)                                       │
│   • Bitrate = Baudrate × Bits pro Symbol                       │
│                                                                 │
│   Beispiel:                                                     │
│   100 MBaud mit 2 Bit/Symbol = 200 Mbit/s                      │
│   1000BASE-T: 125 MBaud mit PAM-5 → 250 Mbit/s pro Paar       │
│               × 4 Paare × 2 (Vollduplex) = 1000 Mbit/s         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Shannon-Theorem

> [!formel] Kanalkapazität nach Shannon
> $$ C = B \cdot \log_2(1 + SNR) $$
> 
> - **C** = Maximale Kanalkapazität (bit/s)
> - **B** = Bandbreite (Hz)
> - **SNR** = Signal-Rausch-Verhältnis (Signal-to-Noise Ratio)

> [!beispiel] Berechnung
> Telefonleitung mit B = 3100 Hz und SNR = 1000 (30 dB):
> 
> $C = 3100 \cdot \log_2(1001) ≈ 3100 \cdot 10 ≈ 31.000$ bit/s
> 
> Daher waren 56k-Modems das praktische Maximum.

## Leitungscodierung

Die **Leitungscodierung** wandelt digitale Daten in übertragbare Signale um.

### Anforderungen

- **Gleichstromfreiheit**: Kein DC-Anteil (wichtig für Transformator-Kopplung)
- **Taktrückgewinnung**: Empfänger muss Takt aus Signal extrahieren können
- **Fehlertoleranz**: Erkennung von Übertragungsfehlern
- **Effizienz**: Möglichst viele Bits pro Symbol

### Wichtige Codierungsverfahren

```
┌─────────────────────────────────────────────────────────────────┐
│                 LEITUNGSCODIERUNGEN                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   NRZ (Non-Return-to-Zero)                                      │
│   ┌───┐   ┌───────┐       ┌───┐                                │
│   │   │   │       │       │   │                                │
│   ┘   └───┘       └───────┘   └──                              │
│     1   0     1       0     1   0                               │
│   Problem: Keine Taktrückgewinnung bei langen 0/1-Folgen       │
│                                                                 │
│   Manchester (10BASE-T Ethernet)                                │
│   ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐                                     │
│   │ └─┘ └─┘ └─┘ └─┘ └─┘ │                                      │
│   └─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┘                                      │
│     1   0   1   1   0   1                                       │
│   Flanke in der Mitte jedes Bits = Takt + Daten                │
│   0 = High→Low, 1 = Low→High                                   │
│   Nachteil: 2× Bandbreite nötig (50% Effizienz)               │
│                                                                 │
│   4B5B + NRZI (100BASE-TX)                                      │
│   • 4 Datenbits → 5 Codebits                                   │
│   • Garantiert max. 3 aufeinanderfolgende Nullen               │
│   • 80% Effizienz                                              │
│                                                                 │
│   8B10B (1000BASE-X)                                            │
│   • 8 Datenbits → 10 Codebits                                  │
│   • DC-Balance und Taktrückgewinnung                           │
│   • 80% Effizienz                                              │
│                                                                 │
│   PAM-5 (1000BASE-T)                                            │
│   • 5 Spannungspegel: -2, -1, 0, +1, +2                        │
│   • 2 Bit pro Symbol (4 Datenpegel + 1 Fehlererkennung)       │
│   • Alle 4 Adernpaare bidirektional                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Vergleich der Codierungen

| Codierung | Verwendung | Effizienz | Taktrückgewinnung |
|-----------|------------|-----------|-------------------|
| NRZ | Einfache Übertragungen | 100% | Schlecht |
| Manchester | 10BASE-T | 50% | Sehr gut |
| 4B5B+NRZI | 100BASE-TX | 80% | Gut |
| 8B10B | 1000BASE-X, FC | 80% | Sehr gut |
| 64B66B | 10GBASE-R | 97% | Gut |
| PAM-5 | 1000BASE-T | ~80% | Gut |

## Kanalcodierung

Die **Kanalcodierung** fügt Redundanz hinzu, um Fehler zu erkennen und zu korrigieren.

### Verfahren

| Verfahren | Funktion | Anwendung |
|-----------|----------|-----------|
| **Parität** | Erkennung von 1-Bit-Fehlern | Seriell |
| **CRC** | Erkennung von Burst-Fehlern | Ethernet, USB |
| **Hamming** | Korrektur von 1-Bit-Fehlern | ECC-RAM |
| **Reed-Solomon** | Korrektur mehrerer Fehler | CDs, DVDs, QR |
| **LDPC** | Fehlerkorrektur | WiFi, SSD |

> [!info] CRC in Ethernet
> Ethernet verwendet CRC-32 (Cyclic Redundancy Check) zur Fehlererkennung im Frame Check Sequence (FCS) Feld. CRC kann Fehler erkennen, aber nicht korrigieren.

## Modulation

Bei der **Modulation** wird ein hochfrequenter Träger durch das Nutzsignal verändert.

```
┌─────────────────────────────────────────────────────────────────┐
│                    MODULATIONSARTEN                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Träger:  ∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿                            │
│                                                                 │
│   AM (Amplitudenmodulation)                                     │
│   • Amplitude des Trägers wird verändert                       │
│   • Einfach, aber störanfällig                                 │
│   ∿∿∿∿∿∿                  ∿∿∿∿∿∿                               │
│   klein (0)              groß (1)                               │
│                                                                 │
│   FM (Frequenzmodulation)                                       │
│   • Frequenz des Trägers wird verändert                        │
│   • Robuster als AM                                            │
│   ∿∿∿∿∿∿∿∿∿∿             ∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿                      │
│   niedrig (0)            hoch (1)                               │
│                                                                 │
│   PM (Phasenmodulation)                                         │
│   • Phase des Trägers wird verändert                           │
│   • Basis für digitale Modulation                              │
│   ∿∿∿∿│∿∿∿∿              Phasensprung = Bitwechsel             │
│                                                                 │
│   QAM (Quadrature Amplitude Modulation)                         │
│   • Kombination aus AM und PM                                  │
│   • Mehrere Bits pro Symbol möglich                            │
│   • QAM-16 = 4 Bit/Symbol, QAM-256 = 8 Bit/Symbol             │
│   • Verwendet in DSL, Kabel, WLAN                              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Digitale Modulationsverfahren

| Verfahren | Bits/Symbol | Anwendung |
|-----------|-------------|-----------|
| BPSK | 1 | Robust, langsam |
| QPSK | 2 | WLAN, Satellit |
| 16-QAM | 4 | DSL, WLAN |
| 64-QAM | 6 | Kabel, WLAN |
| 256-QAM | 8 | DOCSIS, LTE |
| 1024-QAM | 10 | WiFi 6 |
| 4096-QAM | 12 | WiFi 7 |

## Duplex-Verfahren

```
┌─────────────────────────────────────────────────────────────────┐
│                    DUPLEX-VERFAHREN                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Simplex                                                       │
│   ────────────────────────────►                                │
│   Nur in eine Richtung (z.B. Radio)                            │
│                                                                 │
│   Half-Duplex (HDX)                                             │
│   ◄───────────────────────────►                                │
│   Abwechselnd in beide Richtungen (z.B. Walkie-Talkie)        │
│   Früher: Ethernet über Koax, Hub                              │
│                                                                 │
│   Full-Duplex (FDX)                                             │
│   ────────────────────────────►                                │
│   ◄────────────────────────────                                │
│   Gleichzeitig in beide Richtungen                             │
│   Heute: Ethernet über Switch mit Twisted Pair                 │
│                                                                 │
│   Technische Umsetzung:                                         │
│   • Separate Leitungen (100BASE-TX: 2 Paare)                   │
│   • Echo-Cancellation (1000BASE-T: 4 Paare bidirektional)     │
│   • Frequenztrennung (FDD)                                     │
│   • Zeitmultiplex (TDD)                                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Zusammenfassung

> [!zusammenfassung] Kernpunkte
> - **Leitungscodierung** wandelt Bits in Signale (Manchester, 4B5B, 8B10B, PAM-5)
> - **Kanalcodierung** fügt Redundanz zur Fehlererkennung hinzu (CRC)
> - **Modulation** moduliert einen Träger für Funkübertragung (AM, FM, QAM)
> - **Bandbreite** × **Bits/Symbol** = **Datenrate**
> - **Shannon-Theorem** bestimmt maximale Kanalkapazität
> - **Full-Duplex** ermöglicht gleichzeitiges Senden und Empfangen

## Prüfungsrelevanz

> [!pruefung] Prüfungstipps
> - Verstehen Sie den Unterschied zwischen Leitungs- und Kanalcodierung
> - Kennen Sie die Manchester-Codierung und warum sie verwendet wird
> - Können Sie das Shannon-Theorem erklären
> - Wissen Sie, was QAM ist und wozu es verwendet wird

## Verwandte Themen

- [[01-Uebertragungsmedien]] – Physikalische Medien
- [[../05-Sicherungsschicht/02-Fehlererkennung|Fehlererkennung]] – CRC im Detail
- [[../../02-Standards-und-Gremien/02-IEEE-Standards|IEEE Standards]] – Ethernet-Codierungen

## Quellen

- Vorlesungsskript „Betriebssysteme, Rechnernetze und verteilte Systeme", Andreas Hümmer, IU 2025
- Tanenbaum, A. S.: Computer Networks, 5th Edition
