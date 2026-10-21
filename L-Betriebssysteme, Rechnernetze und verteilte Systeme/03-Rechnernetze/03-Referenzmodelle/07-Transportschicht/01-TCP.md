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

> [!info] Lernziele
> Nach diesem Kapitel können Sie...
> - Die Eigenschaften von TCP (verbindungsorientiert, zuverlässig) erklären
> - Den 3-Way-Handshake und 4-Way-Handshake beschreiben
> - Das TCP-Zustandsdiagramm interpretieren
> - Sequenznummern und Bestätigungen (ACK) verstehen
> - Sliding Window und Flusskontrolle erläutern
> - Congestion Control (Slow Start, Congestion Avoidance) beschreiben

## Definition

> [!quote] Definition
> Das **Transmission Control Protocol (TCP)** ist ein verbindungsorientiertes, zuverlässiges Transportprotokoll, das eine vollständige und geordnete Datenübertragung zwischen Anwendungen gewährleistet.
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

Eine TCP-Verbindung durchläuft verschiedene **Zustände** während ihres Lebenszyklus. Das Zustandsdiagramm zeigt alle möglichen Übergänge zwischen diesen Zuständen.

![[tcp-state-diagram.png]]
*<span class="fig-id">03-07-01-tcp-state-diagram</span>: TCP Zustandsdiagramm mit allen Verbindungszuständen*

### Die TCP-Zustände im Überblick

| Zustand | Beschreibung | Typische Situation |
|---------|--------------|-------------------|
| **CLOSED** | Keine Verbindung | Ausgangszustand |
| **LISTEN** | Wartet auf Verbindungsanfragen | Server wartet auf Clients |
| **SYN_SENT** | SYN gesendet, warte auf SYN-ACK | Client hat Verbindung initiiert |
| **SYN_RCVD** | SYN empfangen, SYN-ACK gesendet | Server hat SYN vom Client erhalten |
| **ESTABLISHED** | Verbindung aufgebaut | Datenübertragung möglich |
| **FIN_WAIT_1** | FIN gesendet, warte auf ACK | Active Close initiiert |
| **FIN_WAIT_2** | FIN-ACK erhalten, warte auf FIN | Hälfte der Verbindung geschlossen |
| **CLOSE_WAIT** | FIN empfangen, warte auf Close | Passive Close, Anwendung muss schließen |
| **LAST_ACK** | FIN gesendet, warte auf letztes ACK | Verbindungsabbau fast abgeschlossen |
| **TIME_WAIT** | Warte auf verspätete Segmente | 2×MSL bevor CLOSED |

### Verbindungsaufbau (Active vs. Passive Open)

Der Verbindungsaufbau unterscheidet zwischen der **aktiven** (initiierenden) und **passiven** (wartenden) Seite.

#### Passive Open (Server)

Der Server bereitet sich auf eingehende Verbindungen vor, ohne selbst eine zu initiieren:

1. **Anwendung ruft `listen()` auf** → Socket wechselt in LISTEN-Zustand
2. **Server wartet passiv** auf eingehende SYN-Pakete
3. **Bei SYN-Empfang:** Wechsel zu SYN_RCVD, SYN-ACK wird gesendet
4. **Bei ACK-Empfang:** Wechsel zu ESTABLISHED

```
Zustandsfolge: CLOSED → LISTEN → SYN_RCVD → ESTABLISHED
```

**Typische Anwendungen:** Webserver (Port 80/443), Mailserver (Port 25), SSH-Server (Port 22)

#### Active Open (Client)

Der Client initiiert aktiv eine Verbindung zu einem wartenden Server:

1. **Anwendung ruft `connect()` auf** → Socket wechselt in SYN_SENT
2. **Client sendet SYN** mit initialer Sequenznummer
3. **Bei SYN-ACK-Empfang:** Wechsel zu ESTABLISHED, ACK wird gesendet

```
Zustandsfolge: CLOSED → SYN_SENT → ESTABLISHED
```

**Typische Anwendungen:** Webbrowser, E-Mail-Client, SSH-Client

#### Vergleich

| Aspekt | Active Open (Client) | Passive Open (Server) |
|--------|---------------------|----------------------|
| **Initiiert durch** | `connect()` | `listen()` + `accept()` |
| **Sendet zuerst** | SYN | SYN-ACK (als Antwort) |
| **Wartet auf** | SYN-ACK | SYN |
| **Zustandsanzahl** | 2 (SYN_SENT → ESTABLISHED) | 3 (LISTEN → SYN_RCVD → ESTABLISHED) |
| **Port** | Ephemeral (zufällig, >1024) | Well-known (fest, z.B. 80) |

> [!info] Backlog-Queue
> Ein Server im LISTEN-Zustand hat eine **Backlog-Queue** für halboffene Verbindungen (SYN empfangen, aber noch kein ACK). Die Größe wird bei `listen(sockfd, backlog)` festgelegt. Bei SYN-Flood-Angriffen wird diese Queue gezielt überflutet.

### Verbindungsabbau (Active vs. Passive Close)

**Active Close (initiiert Abbau):**
```
ESTABLISHED → FIN_WAIT_1 → FIN_WAIT_2 → TIME_WAIT → CLOSED
```

**Passive Close (reagiert auf Abbau):**
```
ESTABLISHED → CLOSE_WAIT → LAST_ACK → CLOSED
```

### Wichtige Sonderfälle

#### Simultaneous Open
Beide Seiten senden gleichzeitig SYN:
```
SYN_SENT → SYN_RCVD → ESTABLISHED
```

#### Simultaneous Close
Beide Seiten senden gleichzeitig FIN:
```
FIN_WAIT_1 → CLOSING → TIME_WAIT → CLOSED
```

> [!warning] TIME_WAIT und Port-Erschöpfung
> Ein Socket im TIME_WAIT-Zustand belegt weiterhin den Port (typisch 60-120 Sekunden). Bei vielen kurzlebigen Verbindungen (z.B. HTTP ohne Keep-Alive) können Ports knapp werden. Linux-Option `SO_REUSEADDR` erlaubt Wiederverwendung.

## Sequenznummern und Bestätigungen

TCP nummeriert jeden gesendeten Byte-Strom mit **Sequenznummern**. Der Empfänger bestätigt den Empfang mit **Acknowledgment Numbers (ACK)**, die angeben, welches Byte als nächstes erwartet wird.

### Funktionsweise

![[tcp-seq-ack.png]]
*<span class="fig-id">03-07-01-tcp-seq-ack</span>: TCP Sequenznummern und Bestätigungsmechanismus*

Die Grafik zeigt den Ablauf einer typischen Datenübertragung:

1. **Sender schickt Segment** mit SEQ=1000 und 500 Bytes Nutzdaten (Bytes 1000-1499)
2. **Empfänger bestätigt** mit ACK=1500 – das bedeutet „Alle Bytes bis 1499 erhalten, erwarte Byte 1500"
3. **Sender schickt nächstes Segment** mit SEQ=1500 und 300 Bytes (Bytes 1500-1799)
4. **Empfänger bestätigt** mit ACK=1800

**Berechnungsformel:**
```
ACK-Nummer = Sequenznummer + Anzahl empfangener Bytes
```

> [!tip] Kumulative Bestätigungen
> TCP verwendet **kumulative ACKs**: Ein ACK=1800 bestätigt implizit alle Bytes bis 1799 – auch wenn vorherige ACKs verloren gingen.

### Retransmission (Neuübertragung)

Wenn ein Segment verloren geht, muss es erneut gesendet werden. TCP erkennt Verluste durch zwei Mechanismen:

![[tcp-retransmission.png]]
*<span class="fig-id">03-07-01-tcp-retransmission</span>: TCP Retransmission bei Paketverlust*

Die Grafik illustriert einen typischen Paketverlust:

1. **SEQ=1000** kommt an → Empfänger bestätigt (ACK=1500)
2. **SEQ=1500 geht verloren** auf dem Weg zum Empfänger
3. **SEQ=2000** kommt an → Empfänger erkennt Lücke (1500-1999 fehlt)
4. **Empfänger sendet Duplikat-ACK** (ACK=1500) – „Ich erwarte immer noch Byte 1500"
5. **Sender erkennt Problem** durch Timeout oder 3 Duplikat-ACKs
6. **Retransmission:** Sender wiederholt SEQ=1500
7. **Empfänger kann Lücke füllen** und bestätigt alle Daten (ACK=2500)

#### Auslöser für Retransmission

| Mechanismus | Beschreibung | Reaktionszeit |
|-------------|--------------|---------------|
| **Timeout (RTO)** | Retransmission Timeout läuft ab | Langsam (RTT + Sicherheit) |
| **Fast Retransmit** | 3 identische Duplikat-ACKs empfangen | Schnell (sofort nach 3. Dup-ACK) |

> [!info] Selective Acknowledgment (SACK)
> Mit SACK (RFC 2018) kann der Empfänger mitteilen, welche Segmente angekommen sind – auch wenn eine Lücke besteht. Der Sender muss dann nur die fehlenden Segmente wiederholen, nicht alle nachfolgenden.

## Flusskontrolle (Flow Control)

Die Flusskontrolle verhindert, dass ein schneller Sender einen langsamen Empfänger überlastet. TCP implementiert dies mit dem **Sliding Window Protokoll**.

### Sliding Window

Das Sliding Window unterteilt den Sendepuffer in drei Bereiche:

![[tcp-sliding-window.png]]
*<span class="fig-id">03-07-01-tcp-sliding-window</span>: TCP Sliding Window Mechanismus*

#### Die drei Pufferbereiche

| Bereich | Beschreibung | Status |
|---------|--------------|--------|
| **Gesendet + ACK** | Bytes wurden gesendet und bestätigt | Können aus dem Puffer entfernt werden |
| **Sendefenster** | Bytes dürfen gesendet werden | Warten auf ACK oder noch nicht gesendet |
| **Noch nicht gesendet** | Bytes außerhalb des Fensters | Müssen warten, bis Fenster gleitet |

#### Funktionsweise

1. **Sender darf nur Daten innerhalb des Fensters senden** – maximal so viele Bytes, wie das Window erlaubt
2. **Bei ACK-Empfang gleitet das Fenster nach rechts** – neue Bytes werden sendbar
3. **Empfänger steuert Fenstergroße** – über das Window-Feld im ACK

#### Beispiel

```
Fenstergroße: 4 Segmente
Sendepuffer:  [1][2][3][4][5][6][7][8][9][10]
                   └─────────┘
                   Sendefenster

Nach ACK für Segment 1-2:
Sendepuffer:  [1][2][3][4][5][6][7][8][9][10]
                         └─────────┘
                         Fenster gleitet →
```

> [!tip] Effizienz durch Pipelining
> Ohne Sliding Window müsste der Sender nach jedem Segment auf ein ACK warten (Stop-and-Wait). Mit Sliding Window können mehrere Segmente gleichzeitig „unterwegs" sein – das erhöht den Durchsatz erheblich, besonders bei hoher Latenz.

### Window-Size-Ankündigung

Der Empfänger teilt dem Sender über das **Window-Feld** im TCP-Header mit, wie viel Pufferplatz noch verfügbar ist. Dieser Wert wird mit jedem ACK aktualisiert.

![[tcp-window-size.png]]
*<span class="fig-id">03-07-01-tcp-window-size</span>: TCP Window Size Ankündigung durch den Empfänger*

#### Funktionsweise

| Situation | Auswirkung |
|-----------|------------|
| Anwendung liest Daten | Puffer wird frei → Window vergrößert sich |
| Daten treffen ein | Puffer füllt sich → Window verkleinert sich |
| Puffer voll | Window = 0 (Zero Window) |

#### Zero Window

Wenn der Empfänger ein **Window = 0** sendet, muss der Sender die Übertragung pausieren:

1. Sender stoppt Datenübertragung
2. Sender startet **Persist Timer**
3. Sender sendet periodisch **Window Probes** (1 Byte)
4. Empfänger antwortet mit aktuellem Window-Wert
5. Bei Window > 0: Übertragung wird fortgesetzt

> [!warning] Silly Window Syndrome
> Häufiges Senden kleiner Window-Updates führt zu ineffizienter Übertragung. **Nagle-Algorithmus** (Sender) und **Clark's Solution** (Empfänger) verhindern dies durch Aggregation kleiner Segmente.

#### Window Scaling (RFC 7323)

Das 16-Bit Window-Feld begrenzt die Fenstergröße auf 65.535 Bytes. Für Hochgeschwindigkeitsnetze ist das zu klein:

| Verbindung | Problem bei 64 KB Window |
|------------|--------------------------|
| 1 Gbit/s, 100 ms RTT | Nur 5,2 Mbit/s nutzbar |
| 10 Gbit/s, 100 ms RTT | Nur 0,5% Auslastung |

**Lösung:** Window Scale Option multipliziert Window-Wert mit 2^n (n = 0-14)

```
Effektives Window = Window-Feld × 2^(Scale Factor)
Maximum: 65.535 × 2^14 = 1 GB
```

## Staukontrolle (Congestion Control)

Die Staukontrolle schützt das **Netzwerk** vor Überlastung (im Gegensatz zur Flusskontrolle, die den Empfänger schützt). Ohne Staukontrolle würde ein Sender bei Paketverlust einfach neu senden – was die Stausituation verschlimmert.

### Grundprinzip

TCP verwendet ein **Congestion Window (cwnd)**, das die maximale Menge an Daten begrenzt, die ohne Bestätigung unterwegs sein darf:

```
Effektives Sendefenster = min(cwnd, Empfänger-Window)
```

### Algorithmen

TCP verwendet mehrere Mechanismen zur Staukontrolle:

![[tcp-congestion-control.png]]
*<span class="fig-id">03-07-01-tcp-congestion-control</span>: TCP Congestion Control mit Slow Start und Congestion Avoidance*

### Phasen der Staukontrolle

1. **Slow Start:**
   - Start mit cwnd = 1 MSS (oder IW = 10 MSS bei modernen Implementierungen)
   - Exponentielles Wachstum (cwnd × 2 pro RTT)
   - Bis ssthresh erreicht

2. **Congestion Avoidance:**
   - Lineares Wachstum (cwnd + 1 MSS pro RTT)
   - Vorsichtiges Abtasten der verfügbaren Kapazität
   - Bis Paketverlust erkannt

3. **Bei Paketverlust:**
   - **Timeout:** ssthresh = cwnd/2, cwnd = 1, Slow Start
   - **3 Duplikat-ACKs:** ssthresh = cwnd/2, cwnd = ssthresh (Fast Recovery)

### Verlusterkennung

| Methode | Interpretation | Reaktion |
|---------|----------------|----------|
| **Timeout** | Schwere Stausituation | Aggressiver Reset (cwnd = 1) |
| **3 Duplikat-ACKs** | Leichte Stausituation | Moderater Reset (Fast Recovery) |

### TCP-Varianten

Verschiedene Congestion-Control-Algorithmen wurden entwickelt:

| Variante | Besonderheit | Einsatzgebiet |
|----------|--------------|---------------|
| **TCP Tahoe** | Ursprünglicher Algorithmus | Historisch |
| **TCP Reno** | Fast Recovery | Standard |
| **TCP NewReno** | Verbessertes Fast Recovery | Weit verbreitet |
| **TCP CUBIC** | Kubische Wachstumsfunktion | Linux Default |
| **TCP BBR** | Bandbreitenbasiert | Google, YouTube |

> [!info] TCP CUBIC vs. BBR
> **CUBIC** reagiert auf Paketverlust (loss-based), während **BBR** die verfügbare Bandbreite aktiv misst (model-based). BBR erreicht bessere Auslastung bei langen Latenzen, ist aber in bestimmten Szenarien weniger fair zu anderen Verbindungen.

### Explicit Congestion Notification (ECN)

Statt auf Paketverlust zu warten, können Router Stau explizit signalisieren:

1. Router markiert Paket mit CE (Congestion Experienced) im IP-Header
2. Empfänger setzt ECE-Flag im TCP-ACK
3. Sender reduziert cwnd und setzt CWR-Flag

**Vorteil:** Staureaktion ohne Paketverlust → geringere Latenz

### Berechnungsbeispiel

> [!example] Slow Start Berechnung
> **Gegeben:** MSS = 1460 Bytes, ssthresh = 64 KB, cwnd initial = 1 MSS
> 
> | RTT | cwnd | Gesendete Daten |
> |-----|------|-----------------|
> | 1 | 1 MSS | 1.460 Bytes |
> | 2 | 2 MSS | 2.920 Bytes |
> | 3 | 4 MSS | 5.840 Bytes |
> | 4 | 8 MSS | 11.680 Bytes |
> | 5 | 16 MSS | 23.360 Bytes |
> | 6 | 32 MSS | 46.720 Bytes |
> | 7 | 44 MSS | 64.240 Bytes (≈ ssthresh) |
> 
> Ab RTT 7: Wechsel zu Congestion Avoidance (lineares Wachstum)

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
