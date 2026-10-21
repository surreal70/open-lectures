---
author: Andreas Hümmer
title: TCP - Transmission Control Protocol
tags:
  - content
  - rn
  - transport-layer
  - tcp
  - verbindungsorientiert
  - handshake
created: '2026-10-07'
modified: '2026-10-21'
bereich: RN
---

# TCP - Transmission Control Protocol

## Definition

Das **Transmission Control Protocol (TCP)** ist ein verbindungsorientiertes, zuverlässiges Transportprotokoll, das eine vollständige und geordnete Datenübertragung zwischen Anwendungen gewährleistet.

## Eigenschaften

| Eigenschaft | Beschreibung |
|-------------|--------------|
| **Verbindungsorientiert** | 3-Way-Handshake vor Datentransfer |
| **Zuverlässig** | Bestätigungen (ACK) für empfangene Daten |
| **Geordnet** | Sequenznummern garantieren Reihenfolge |
| **Vollduplex** | Bidirektionale Kommunikation gleichzeitig |
| **Flusskontrolle** | Sliding Window verhindert Empfänger-Überlastung |
| **Staukontrolle** | Congestion Control schützt das Netzwerk |

## TCP-Header

Der TCP-Header ist mindestens **20 Bytes** lang:

![[tcp-header.png]]
*<span class="fig-id">03-07-01-tcp-header</span>: TCP-Header Struktur mit 32-Bit Feldaufteilung*

### Header-Felder im Detail

| Feld | Bits | Beschreibung |
|------|------|--------------|
| **Source Port** | 16 | Quell-Portnummer |
| **Destination Port** | 16 | Ziel-Portnummer |
| **Sequence Number** | 32 | Position des ersten Datenbytes |
| **Acknowledgment Number** | 32 | Nächstes erwartetes Byte |
| **Data Offset** | 4 | Header-Länge in 32-Bit-Worten |
| **Flags** | 9 | Steuerungsflags (siehe unten) |
| **Window** | 16 | Empfangsfenstergröße |
| **Checksum** | 16 | Prüfsumme (Header + Daten) |
| **Urgent Pointer** | 16 | Zeiger auf dringende Daten |

### TCP-Flags

| Flag | Name | Beschreibung |
|------|------|--------------|
| **SYN** | Synchronize | Verbindungsaufbau initiieren |
| **ACK** | Acknowledgment | Bestätigung |
| **FIN** | Finish | Verbindungsabbau initiieren |
| **RST** | Reset | Verbindung abbrechen |
| **PSH** | Push | Daten sofort an Anwendung übergeben |
| **URG** | Urgent | Dringende Daten vorhanden |
| **ECE** | ECN-Echo | Explicit Congestion Notification |
| **CWR** | Congestion Window Reduced | Staufenster reduziert |

## TCP-Verbindungsaufbau (3-Way-Handshake)

Der Verbindungsaufbau erfolgt in drei Schritten:

![[tcp-3way-handshake.png]]
*<span class="fig-id">03-07-01-tcp-3way-handshake</span>: TCP 3-Way-Handshake für den Verbindungsaufbau*

> [!tip] Merkhilfe: SYN → SYN-ACK → ACK
> "**S**ie **S**ind **A**ngenommen" oder einfach "**SSA**"

### Warum 3-Way?

1. **Synchronisation:** Beide Seiten tauschen initiale Sequenznummern aus
2. **Gegenseitige Bestätigung:** Jede Seite bestätigt die Sequenznummer der anderen
3. **Verbindungsbereitschaft:** Beide Seiten signalisieren Bereitschaft

## TCP-Verbindungsabbau (4-Way-Handshake)

Der Verbindungsabbau erfolgt in vier Schritten (Halbduplex-Close):

![[tcp-4way-handshake.png]]
*<span class="fig-id">03-07-01-tcp-4way-handshake</span>: TCP 4-Way-Handshake für den Verbindungsabbau*

> [!info] TIME_WAIT
> Der TIME_WAIT-Zustand dauert 2×MSL (Maximum Segment Lifetime, typisch 60 Sekunden). Dies stellt sicher, dass verspätete Pakete nicht eine neue Verbindung stören.

## TCP-Zustandsdiagramm

![[tcp-state-diagram.png]]
*<span class="fig-id">03-07-01-tcp-state-diagram</span>: TCP Zustandsdiagramm mit allen Verbindungszuständen*

## Sequenznummern und Bestätigungen

### Funktionsweise

![[tcp-seq-ack.png]]
*<span class="fig-id">03-07-01-tcp-seq-ack</span>: TCP Sequenznummern und Bestätigungsmechanismus*

### Retransmission (Neuübertragung)

![[tcp-retransmission.png]]
*<span class="fig-id">03-07-01-tcp-retransmission</span>: TCP Retransmission bei Paketverlust*

## Flusskontrolle (Flow Control)

### Sliding Window

Das Sliding Window verhindert, dass der Sender den Empfänger überlastet:

![[tcp-sliding-window.png]]
*<span class="fig-id">03-07-01-tcp-sliding-window</span>: TCP Sliding Window Mechanismus*

### Window-Size-Ankündigung

![[tcp-window-size.png]]
*<span class="fig-id">03-07-01-tcp-window-size</span>: TCP Window Size Ankündigung durch den Empfänger*

## Staukontrolle (Congestion Control)

### Algorithmen

TCP verwendet mehrere Mechanismen zur Staukontrolle:

![[tcp-congestion-control.png]]
*<span class="fig-id">03-07-01-tcp-congestion-control</span>: TCP Congestion Control mit Slow Start und Congestion Avoidance*

### Phasen der Staukontrolle

1. **Slow Start:**
   - Start mit cwnd = 1 MSS
   - Exponentielles Wachstum (cwnd × 2 pro RTT)
   - Bis ssthresh erreicht

2. **Congestion Avoidance:**
   - Lineares Wachstum (cwnd + 1 MSS pro RTT)
   - Bis Paketverlust erkannt

3. **Bei Paketverlust:**
   - **Timeout:** ssthresh = cwnd/2, cwnd = 1, Slow Start
   - **3 Duplikat-ACKs:** ssthresh = cwnd/2, cwnd = ssthresh (Fast Recovery)

## TCP-Optionen

| Option | Länge | Beschreibung |
|--------|-------|--------------|
| MSS | 4 | Maximum Segment Size |
| Window Scale | 3 | Erlaubt Fenster > 65535 |
| SACK | variabel | Selective Acknowledgment |
| Timestamp | 10 | RTT-Messung, PAWS |
| NOP | 1 | Padding |
| EOL | 1 | Ende der Optionsliste |

> [!info] MSS (Maximum Segment Size)
> Die MSS wird beim Verbindungsaufbau ausgehandelt. Typisch: 1460 Bytes (1500 MTU - 20 IP - 20 TCP)

## Typische Anwendungen

| Anwendung | Warum TCP? |
|-----------|------------|
| **HTTP/HTTPS** | Webseiten müssen vollständig und korrekt übertragen werden |
| **SMTP/IMAP** | E-Mails dürfen nicht verstümmelt ankommen |
| **FTP** | Dateien müssen intakt bleiben |
| **SSH** | Interaktive Sitzung erfordert Zuverlässigkeit |
| **Datenbanken** | Transaktionen müssen vollständig sein |

## Prüfungsrelevante Themen

> [!warning] Klausurrelevanz: Sehr hoch
>
> **Häufige Prüfungsthemen:**
> 1. TCP-Header-Aufbau und Flags
> 2. 3-Way-Handshake (SYN, SYN-ACK, ACK)
> 3. Sequenznummern und ACK-Berechnung
> 4. Sliding Window und Flusskontrolle
> 5. Slow Start und Congestion Control

### Berechnungsbeispiel

> [!example] Sequenznummer-Berechnung
> **Gegeben:** Client sendet SYN mit seq=1000
> 
> **Ablauf:**
> 1. Client → Server: SYN, seq=1000
> 2. Server → Client: SYN-ACK, seq=5000, ack=1001
> 3. Client → Server: ACK, seq=1001, ack=5001
> 
> **Nach Verbindungsaufbau:**
> - Client-Sequenz: 1001 (nächstes zu sendende Byte)
> - Server-Sequenz: 5001

## Zusammenhänge

- [[02-UDP]] - Vergleichsprotokoll (verbindungslos)
- [[03-Ports]] - Portnummern für Multiplexing
- [[06-Netzwerkschicht/01-IP-Protokoll|IP-Protokoll]] - Darunterliegende Schicht
- [[08-Anwendungsschicht/00-Anwendungsschicht-Index|Anwendungsschicht]] - Nutzt TCP

## Quellen

- [[A-RFC-Index|RFC 9293]] - TCP Specification (aktualisiert RFC 793)
- [[A-RFC-Index|RFC 5681]] - TCP Congestion Control
- [[A-RFC-Index|RFC 7323]] - TCP Extensions (Window Scale, Timestamps)
- Tanenbaum, A. S.: Computernetzwerke, Kap. 6
