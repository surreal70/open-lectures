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

**Bandbreite (B)**
- Frequenzbereich eines Übertragungskanals
- Einheit: Hertz (Hz)
- Beispiel: Telefonleitung ≈ 3100 Hz (300–3400 Hz)

**Baudrate (Symbolrate)**
- Anzahl der Signaländerungen pro Sekunde
- Einheit: Baud (Bd)
- 1 Symbol kann mehrere Bits kodieren

**Bitrate (Datenrate)**
- Anzahl übertragener Bits pro Sekunde
- Einheit: bit/s (bps)
- Bitrate = Baudrate × Bits pro Symbol

> [!beispiel] Rechenbeispiel
> - 100 MBaud mit 2 Bit/Symbol = 200 Mbit/s
> - 1000BASE-T: 125 MBaud mit PAM-5 → 250 Mbit/s pro Paar × 4 Paare × 2 (Vollduplex) = 1000 Mbit/s

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

![[leitungscodierung-nrz-manchester.png]]
*<span class="fig-id">03-03-04-02-leitungscodierung</span>: NRZ- und Manchester-Codierung im Vergleich. Bei NRZ fehlt die Taktrückgewinnung bei langen 0/1-Folgen. Manchester codiert den Takt durch eine Flanke in der Bitmitte.*

**4B5B + NRZI (100BASE-TX)**
- 4 Datenbits → 5 Codebits
- Garantiert max. 3 aufeinanderfolgende Nullen
- 80% Effizienz

**8B10B (1000BASE-X, Fibre Channel)**
- 8 Datenbits → 10 Codebits
- DC-Balance und Taktrückgewinnung
- 80% Effizienz

**PAM-5 (1000BASE-T)**
- 5 Spannungspegel: −2, −1, 0, +1, +2
- 2 Bit pro Symbol (4 Datenpegel + 1 Fehlererkennung)
- Alle 4 Adernpaare bidirektional

> [!info] Gleichstromfreiheit (DC-Balance)
> Ein wichtiges Ziel vieler Leitungscodierungen ist die **Gleichstromfreiheit** – das Signal enthält keinen DC-Anteil (Mittelwert = 0). Dies ist notwendig, weil:
> - **Transformatorkopplung**: Übertrager (z.B. in Ethernet-Buchsen) können keinen Gleichstrom übertragen
> - **Kapazitive Kopplung**: Kondensatoren blockieren DC-Anteile
> - **Baseline Wander**: Ein DC-Anteil verschiebt den Referenzpegel und erschwert die Dekodierung
> 
> Manchester erreicht dies durch garantierte Flanken, 8B10B durch spezielle Codeworte mit ausgeglichener Anzahl von Einsen und Nullen.

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

![[modulationsarten.png]]
*<span class="fig-id">03-03-04-02-modulationsarten</span>: Modulationsarten im Vergleich – AM, FM, PM und QAM-Konstellationsdiagramme.*

**AM (Amplitudenmodulation)**
- Amplitude des Trägers wird verändert
- Einfach zu implementieren, aber störanfällig
- Anwendung: Rundfunk (Mittelwelle)

**FM (Frequenzmodulation)**
- Frequenz des Trägers wird verändert
- Robuster gegenüber Störungen als AM
- Anwendung: UKW-Radio, analoges TV-Audio

**PM (Phasenmodulation)**
- Phase des Trägers wird verändert
- Basis für digitale Modulationsverfahren
- Anwendung: BPSK, QPSK in WLAN und Satellit

**QAM (Quadrature Amplitude Modulation)**
- Kombination aus Amplituden- und Phasenmodulation
- Mehrere Bits pro Symbol durch verschiedene Signalpunkte im I/Q-Diagramm
- Je mehr Punkte im Konstellationsdiagramm, desto mehr Bits/Symbol – aber auch höhere Fehleranfälligkeit
- Anwendung: DSL, Kabel-Internet, WLAN, LTE/5G

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

![[duplex-verfahren.png]]
*<span class="fig-id">03-03-04-02-duplex</span>: Duplex-Verfahren – Simplex, Half-Duplex und Full-Duplex im Vergleich.*

**Simplex**
- Übertragung nur in eine Richtung
- Beispiele: Radio, TV-Broadcast, Sensordaten

**Half-Duplex (HDX)**
- Abwechselnd in beide Richtungen
- Zu einem Zeitpunkt kann nur eine Station senden
- Beispiele: Walkie-Talkie, frühere Ethernet-Netze über Koax/Hub

**Full-Duplex (FDX)**
- Gleichzeitig in beide Richtungen
- Beide Stationen können simultan senden und empfangen
- Beispiele: Telefon, Ethernet über Switch mit Twisted Pair

**Technische Umsetzung von Full-Duplex:**
- **Separate Leitungen**: 100BASE-TX nutzt 2 Adernpaare (je eins pro Richtung)
- **Echo-Cancellation**: 1000BASE-T nutzt alle 4 Paare bidirektional und filtert das eigene Signal heraus
- **Frequenztrennung (FDD)**: Unterschiedliche Frequenzbänder für Senden/Empfangen (z.B. LTE)
- **Zeitmultiplex (TDD)**: Schneller Wechsel zwischen Senden und Empfangen (z.B. WLAN)

## Zusammenfassung

> [!zusammenfassung] Kernpunkte
> - **Leitungscodierung** wandelt Bits in Signale (Manchester, 4B5B, 8B10B, PAM-5)
> - **Kanalcodierung** fügt Redundanz zur Fehlererkennung hinzu (CRC)
> - **Modulation** moduliert einen Träger für Funkübertragung (AM, FM, QAM)
> - **Bandbreite** × **Bits/Symbol** = **Datenrate**
> - **Shannon-Theorem** bestimmt maximale Kanalkapazität
> - **Full-Duplex** ermöglicht gleichzeitiges Senden und Empfangen

## Prüfungsrelevanz

> [!warning] **Prüfungsrelevant**
> - Unterschied Leitungscodierung (Bits→Signale) vs. Kanalcodierung (Fehlerschutz)

> [!question] **Typische Prüfungsfragen**
> - Was ist der Unterschied zwischen Leitungs- und Kanalcodierung?
> - Warum wird bei 10BASE-T Manchester-Codierung verwendet?
> - Was bedeutet Gleichstromfreiheit und warum ist sie wichtig?

## Verwandte Themen

- [[01-Uebertragungsmedien]] – Physikalische Medien
- [[../05-Sicherungsschicht/02-Fehlererkennung|Fehlererkennung]] – CRC im Detail
- [[../../02-Standards-und-Gremien/02-IEEE-Standards|IEEE Standards]] – Ethernet-Codierungen

## Quellen

- Vorlesungsskript „Betriebssysteme, Rechnernetze und verteilte Systeme", Andreas Hümmer, IU 2025
- Tanenbaum, A. S.: Computer Networks, 5th Edition
