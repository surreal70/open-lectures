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
modified: '2026-10-13'
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

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|          Source Port          |       Destination Port        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                        Sequence Number                        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Acknowledgment Number                      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Data |       |C|E|U|A|P|R|S|F|                               |
| Offset| Rsrvd |W|C|R|C|S|S|Y|I|            Window             |
|       |       |R|E|G|K|H|T|N|N|                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|           Checksum            |         Urgent Pointer        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Options (falls vorhanden)                  |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

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

```
┌──────────────────────────────────────────────────────────────────┐
│                     TCP 3-Way-Handshake                          │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│    Client                                          Server        │
│    (CLOSED)                                        (LISTEN)      │
│       │                                               │          │
│       │         1. SYN (seq=x)                        │          │
│       │  ─────────────────────────────────────────►   │          │
│       │                                               │          │
│    (SYN_SENT)                                    (SYN_RCVD)      │
│       │                                               │          │
│       │         2. SYN-ACK (seq=y, ack=x+1)          │          │
│       │  ◄─────────────────────────────────────────   │          │
│       │                                               │          │
│       │         3. ACK (seq=x+1, ack=y+1)            │          │
│       │  ─────────────────────────────────────────►   │          │
│       │                                               │          │
│    (ESTABLISHED)                               (ESTABLISHED)     │
│       │                                               │          │
│       │  ◄════════ Datenübertragung ════════════►    │          │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

> [!tip] Merkhilfe: SYN → SYN-ACK → ACK
> "**S**ie **S**ind **A**ngenommen" oder einfach "**SSA**"

### Warum 3-Way?

1. **Synchronisation:** Beide Seiten tauschen initiale Sequenznummern aus
2. **Gegenseitige Bestätigung:** Jede Seite bestätigt die Sequenznummer der anderen
3. **Verbindungsbereitschaft:** Beide Seiten signalisieren Bereitschaft

## TCP-Verbindungsabbau (4-Way-Handshake)

Der Verbindungsabbau erfolgt in vier Schritten (Halbduplex-Close):

```
┌──────────────────────────────────────────────────────────────────┐
│                     TCP 4-Way-Handshake                          │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│    Client                                          Server        │
│    (ESTABLISHED)                               (ESTABLISHED)     │
│       │                                               │          │
│       │         1. FIN (seq=u)                        │          │
│       │  ─────────────────────────────────────────►   │          │
│       │                                               │          │
│    (FIN_WAIT_1)                                  (CLOSE_WAIT)    │
│       │                                               │          │
│       │         2. ACK (ack=u+1)                      │          │
│       │  ◄─────────────────────────────────────────   │          │
│       │                                               │          │
│    (FIN_WAIT_2)                                  (CLOSE_WAIT)    │
│       │                                               │          │
│       │         3. FIN (seq=v)                        │          │
│       │  ◄─────────────────────────────────────────   │          │
│       │                                               │          │
│    (TIME_WAIT)                                   (LAST_ACK)      │
│       │                                               │          │
│       │         4. ACK (ack=v+1)                      │          │
│       │  ─────────────────────────────────────────►   │          │
│       │                                               │          │
│    (TIME_WAIT)                                   (CLOSED)        │
│       │                                               │          │
│    ~~~ 2*MSL ~~~                                                 │
│       │                                                          │
│    (CLOSED)                                                      │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

> [!info] TIME_WAIT
> Der TIME_WAIT-Zustand dauert 2×MSL (Maximum Segment Lifetime, typisch 60 Sekunden). Dies stellt sicher, dass verspätete Pakete nicht eine neue Verbindung stören.

## TCP-Zustandsdiagramm

```
                              ┌─────────────┐
                              │   CLOSED    │
                              └──────┬──────┘
                     Active Open     │     Passive Open
                     send SYN        │     
                    ┌────────────────┴────────────────┐
                    ▼                                 ▼
             ┌─────────────┐                   ┌─────────────┐
             │  SYN_SENT   │                   │   LISTEN    │
             └──────┬──────┘                   └──────┬──────┘
        rcv SYN-ACK │                     rcv SYN    │
        send ACK    │                     send SYN-ACK
                    ▼                                 ▼
             ┌─────────────┐                   ┌─────────────┐
             │             │◄──────────────────│  SYN_RCVD   │
             │ ESTABLISHED │   rcv ACK         └─────────────┘
             │             │
             └──────┬──────┘
                    │
        Close       │       rcv FIN
        send FIN    │       send ACK
           ┌────────┴────────┐
           ▼                 ▼
    ┌─────────────┐   ┌─────────────┐
    │ FIN_WAIT_1  │   │ CLOSE_WAIT  │
    └──────┬──────┘   └──────┬──────┘
           │                 │ Close
           │                 │ send FIN
           ▼                 ▼
    ┌─────────────┐   ┌─────────────┐
    │ FIN_WAIT_2  │   │  LAST_ACK   │
    └──────┬──────┘   └──────┬──────┘
   rcv FIN │                 │ rcv ACK
   send ACK│                 │
           ▼                 ▼
    ┌─────────────┐   ┌─────────────┐
    │  TIME_WAIT  │   │   CLOSED    │
    └──────┬──────┘   └─────────────┘
           │ 2*MSL Timeout
           ▼
    ┌─────────────┐
    │   CLOSED    │
    └─────────────┘
```

## Sequenznummern und Bestätigungen

### Funktionsweise

```
┌────────────────────────────────────────────────────────────────┐
│                 Sequenznummern und ACKs                        │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Sender                                          Empfänger     │
│     │                                               │          │
│     │  SEQ=1000, Daten: 500 Bytes                  │          │
│     │  ───────────────────────────────────────────► │          │
│     │                                               │          │
│     │  ACK=1500 (nächstes erwartetes Byte)         │          │
│     │  ◄─────────────────────────────────────────── │          │
│     │                                               │          │
│     │  SEQ=1500, Daten: 300 Bytes                  │          │
│     │  ───────────────────────────────────────────► │          │
│     │                                               │          │
│     │  ACK=1800                                     │          │
│     │  ◄─────────────────────────────────────────── │          │
│                                                                │
│  ACK-Nummer = Sequenznummer + Datenlänge                      │
│  ACK=1500 bedeutet: "Alle Bytes bis 1499 erhalten"            │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### Retransmission (Neuübertragung)

```
┌────────────────────────────────────────────────────────────────┐
│                    TCP Retransmission                          │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Sender                                          Empfänger     │
│     │                                               │          │
│     │  SEQ=1000, Daten: 500 Bytes                  │          │
│     │  ───────────────────────────────────────────► │          │
│     │                                               │          │
│     │  SEQ=1500, Daten: 500 Bytes                  │          │
│     │  ─────────────X (verloren)                    │          │
│     │                                               │          │
│     │  SEQ=2000, Daten: 500 Bytes                  │          │
│     │  ───────────────────────────────────────────► │          │
│     │                                               │          │
│     │  ACK=1500 (Duplikat-ACK, 1500-1999 fehlt)    │          │
│     │  ◄─────────────────────────────────────────── │          │
│     │                                               │          │
│  Timeout oder 3 Duplikat-ACKs → Retransmit         │          │
│     │                                               │          │
│     │  SEQ=1500, Daten: 500 Bytes (Wiederholung)   │          │
│     │  ───────────────────────────────────────────► │          │
│     │                                               │          │
│     │  ACK=2500 (alle empfangen)                   │          │
│     │  ◄─────────────────────────────────────────── │          │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

## Flusskontrolle (Flow Control)

### Sliding Window

Das Sliding Window verhindert, dass der Sender den Empfänger überlastet:

```
┌────────────────────────────────────────────────────────────────┐
│                      Sliding Window                            │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Sendepuffer:                                                  │
│  ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐           │
│  │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │10 │11 │12 │           │
│  └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘           │
│    ▲           ▲                   ▲                          │
│    │           │                   │                          │
│  Gesendet    Gesendet,           Noch nicht                   │
│  und ACK     warte auf ACK       gesendet                     │
│              └───────────────────┘                            │
│                 Sendefenster                                   │
│                 (Window Size)                                  │
│                                                                │
│  Window Size = vom Empfänger advertised                       │
│  Sender darf max. Window Size Bytes ohne ACK senden           │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### Window-Size-Ankündigung

```
Empfänger teilt verfügbaren Puffer mit:

  Empfängerpuffer (8 KB):
  ┌────────────────────────────────┬────────────────────────────┐
  │  Bereits empfangen (3 KB)      │  Frei (5 KB)               │
  └────────────────────────────────┴────────────────────────────┘
                                    ▲
                                    │
                              Window = 5120
                              (wird im ACK gesendet)

  Wenn Anwendung Daten liest → Fenster vergrößert sich
  Wenn Puffer voll → Window = 0 (Zero Window)
```

## Staukontrolle (Congestion Control)

### Algorithmen

TCP verwendet mehrere Mechanismen zur Staukontrolle:

```
┌────────────────────────────────────────────────────────────────┐
│                   TCP Congestion Control                       │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Congestion Window (cwnd)                                      │
│  ▲                                                             │
│  │         Congestion          ╱                              │
│  │         Avoidance     ─────╱                               │
│  │                      ╱                                      │
│  │              ───────╱                                       │
│  │             ╱                                               │
│  │   Slow    ╱   ← ssthresh (Slow Start Threshold)            │
│  │   Start  ╱                                                  │
│  │        ╱                                                    │
│  │      ╱                                                      │
│  │    ╱                                                        │
│  │  ╱                                                          │
│  │╱                                                            │
│  └─────────────────────────────────────────────────────► Zeit  │
│                                                                │
│  Slow Start:        cwnd verdoppelt pro RTT                   │
│  Congestion Avoid.: cwnd +1 MSS pro RTT                       │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

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
