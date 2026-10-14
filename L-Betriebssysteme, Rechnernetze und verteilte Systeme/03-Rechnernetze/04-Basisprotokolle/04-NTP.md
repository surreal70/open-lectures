---
author: Andreas Hümmer
title: NTP - Network Time Protocol
tags:
  - content
  - rn
  - protokolle
  - ntp
  - layer7
  - zeitsynchronisation
  - netzwerkdienst
created: '2026-10-13'
modified: '2026-10-13'
bereich: RN
---

# NTP – Network Time Protocol

## Definition

Das **Network Time Protocol (NTP)** synchronisiert Systemuhren über Netzwerke hinweg. Präzise Zeitsynchronisation ist kritisch für Logging, Authentifizierung (Kerberos), Zertifikate (TLS), Datenbankreplikation und verteilte Systeme.

> [!info] Schichtzuordnung
> NTP ist ein **Layer-7-Protokoll** (Anwendungsschicht), das **UDP Port 123** verwendet. Für die neue NTS-Erweiterung (Network Time Security) wird zusätzlich **TCP Port 4460** genutzt.

## Warum Zeitsynchronisation?

```
┌─────────────────────────────────────────────────────────────────┐
│              Warum ist genaue Zeit wichtig?                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ✓ Logging & Forensik                                         │
│     → Ereignisse verschiedener Systeme korrelieren             │
│     → "Was passierte zuerst?"                                  │
│                                                                  │
│   ✓ Authentifizierung (Kerberos)                               │
│     → Tickets haben Zeitstempel                                │
│     → Max. 5 Minuten Abweichung erlaubt                        │
│                                                                  │
│   ✓ TLS-Zertifikate                                            │
│     → "Not Before" / "Not After" Zeitstempel                   │
│     → Falsche Uhr → Zertifikat ungültig!                       │
│                                                                  │
│   ✓ Datenbank-Replikation                                      │
│     → Konfliktauflösung basiert auf Zeitstempeln               │
│                                                                  │
│   ✓ Verteilte Systeme                                          │
│     → Lamport-Uhren, Vektoruhren                               │
│     → Konsistenzgarantien                                      │
│                                                                  │
│   ✓ Finanzsektor / Compliance                                  │
│     → MiFID II: Zeitstempel auf 1ms genau                      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## NTP-Stratum-Hierarchie

> [!info] RFC-Referenz
> - NTPv4: [[A-RFC-Index#RFC 5905|RFC 5905]]
> - SNTP: [[A-RFC-Index#RFC 4330|RFC 4330]]
> - NTS: [[A-RFC-Index#RFC 8915|RFC 8915]]

```
┌─────────────────────────────────────────────────────────────────┐
│                    NTP-Stratum-Hierarchie                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Stratum 0    ┌─────────────────────────────────────────────┐  │
│   (Referenz)   │  GPS  │  Atomuhr  │  DCF77  │  PPS  │ GLONASS│ │
│                │       │ (Caesium) │ (77.5kHz)│       │       │  │
│                └────────────────────┬────────────────────────┘  │
│                                     │                           │
│                                     │ Direkte Verbindung        │
│                                     │ (seriell, PPS-Signal)     │
│                                     │                           │
│   Stratum 1    ┌────────────────────┴────────────────────────┐  │
│   (Primary)    │        Primäre NTP-Server                   │  │
│                │  time.google.com, time.windows.com          │  │
│                │  PTB (ptbtime1.ptb.de)                      │  │
│                └────────────────────┬────────────────────────┘  │
│                                     │                           │
│   Stratum 2    ┌────────────────────┴────────────────────────┐  │
│   (Secondary)  │       Sekundäre NTP-Server                  │  │
│                │  ISP-Server, Unternehmens-Server            │  │
│                └────────────────────┬────────────────────────┘  │
│                                     │                           │
│   Stratum 3+   ┌────────────────────┴────────────────────────┐  │
│                │    Clients, weitere Server                  │  │
│                │    (Desktop, Server, IoT-Geräte)           │  │
│                └─────────────────────────────────────────────┘  │
│                                                                  │
│   Stratum 16 = unsynchronisiert (ungültig)                     │
│   Stratum 15 = maximale Entfernung von Stratum 0               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Stratum-Regeln

| Stratum | Beschreibung | Genauigkeit |
|---------|--------------|-------------|
| **0** | Referenzuhren (GPS, Atomuhr, DCF77) | Nanosekunden |
| **1** | Direkt an Stratum 0 angeschlossen | Mikrosekunden |
| **2** | Synchronisiert mit Stratum 1 | < 10 ms |
| **3-15** | Weitere Hierarchiestufen | Zunehmend ungenauer |
| **16** | Unsynchronisiert | Ungültig |

> [!tip] Stratum-Berechnung
> Der Stratum-Wert eines Servers ist immer **Stratum des Upstreams + 1**.
> Ein Client, der sich mit einem Stratum-2-Server synchronisiert, wird selbst zu Stratum 3.

## Zeitmessung und Offset-Berechnung

```
┌─────────────────────────────────────────────────────────────────┐
│              NTP-Zeitmessung (Algorithmus)                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Client                                             Server     │
│      │                                                  │       │
│   t1 │ ──────────── NTP Request ────────────────────► │ t2     │
│      │              (Zeitstempel t1)                    │       │
│      │                                                  │       │
│   t4 │ ◄─────────── NTP Response ─────────────────── │ t3     │
│      │              (Zeitstempel t1, t2, t3)           │       │
│      │                                                  │       │
│                                                                  │
│   Berechnung:                                                   │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │                                                          │  │
│   │   Offset (θ) = ((t2 - t1) + (t3 - t4)) / 2              │  │
│   │                                                          │  │
│   │   → Wie weit geht die Client-Uhr falsch?                │  │
│   │                                                          │  │
│   │   Delay (δ) = (t4 - t1) - (t3 - t2)                     │  │
│   │                                                          │  │
│   │   → Round-Trip-Zeit (ohne Server-Verarbeitung)          │  │
│   │                                                          │  │
│   └─────────────────────────────────────────────────────────┘  │
│                                                                  │
│   t1 = Client-Sendezeit       t2 = Server-Empfangszeit         │
│   t3 = Server-Sendezeit       t4 = Client-Empfangszeit         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### NTP-Algorithmen

| Algorithmus | Funktion |
|-------------|----------|
| **Clock Filter** | Wählt beste Samples aus mehreren Messungen |
| **Clock Selection** | Wählt beste Server aus mehreren Quellen |
| **Clock Clustering** | Eliminiert Ausreißer (Falsetickers) |
| **Clock Discipline** | Steuert Uhr sanft nach (keine Sprünge) |

> [!warning] Zeitsprünge vermeiden
> NTP passt die Uhr schrittweise an (**Slewing**), nicht sprunghaft. Bei großen Abweichungen (>128ms) kann ein **Step** nötig sein, was Anwendungen stören kann.

## NTP-Paketformat

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│LI │ VN  │Mode │    Stratum    │     Poll      │   Precision   │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│                         Root Delay                            │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│                       Root Dispersion                         │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│                     Reference Identifier                      │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│                   Reference Timestamp (64 Bit)                │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│                   Originate Timestamp (64 Bit)                │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│                    Receive Timestamp (64 Bit)                 │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
│                   Transmit Timestamp (64 Bit)                 │
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

| Feld | Bits | Beschreibung |
|------|------|--------------|
| **LI** | 2 | Leap Indicator (Schaltsekunde) |
| **VN** | 3 | Version Number (aktuell: 4) |
| **Mode** | 3 | 3=Client, 4=Server, 5=Broadcast |
| **Stratum** | 8 | Stratum-Level (0-16) |
| **Poll** | 8 | Poll-Intervall (2^n Sekunden) |
| **Precision** | 8 | Präzision der Uhr (2^n Sekunden) |
| **Root Delay** | 32 | Delay zur Referenzuhr |
| **Root Dispersion** | 32 | Maximaler Fehler zur Referenzuhr |
| **Reference ID** | 32 | Referenzuhr-Identifier |
| **Timestamps** | 4×64 | Zeitstempel (t1-t4) |

## NTP vs. SNTP vs. PTP

| Aspekt | NTP | SNTP | PTP (IEEE 1588) |
|--------|-----|------|-----------------|
| **Genauigkeit** | 1-10 ms | 100+ ms | < 1 µs |
| **Komplexität** | Hoch | Niedrig | Sehr hoch |
| **Hardware** | Software | Software | Hardware-Support |
| **Algorithmen** | Clock Filter, Clustering | Vereinfacht | Best Master Clock |
| **Einsatz** | Allgemein | Embedded, IoT | Industrie, Finanz |
| **Port** | UDP 123 | UDP 123 | UDP 319, 320 |

## Sicherheit

### NTP-Amplification-Angriffe

```
┌─────────────────────────────────────────────────────────────────┐
│              NTP Amplification Attack (DDoS)                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Angreifer           NTP-Server             Opfer             │
│      │                    │                    │               │
│      │  Kleine Anfrage    │                    │               │
│      │  (Source IP =      │                    │               │
│      │   Opfer-IP!)       │                    │               │
│      │────────────────────►│                    │               │
│      │                    │                    │               │
│      │                    │  Große Antwort    │               │
│      │                    │  (z.B. monlist)   │               │
│      │                    │───────────────────►│               │
│      │                    │                    │               │
│                                                                  │
│   Amplification-Faktor: bis zu 556x!                           │
│                                                                  │
│   Gegenmaßnahmen:                                               │
│   • monlist deaktivieren (ntpd: "disable monitor")             │
│   • Rate Limiting                                              │
│   • BCP38 (Ingress Filtering)                                  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### NTS (Network Time Security)

```
┌─────────────────────────────────────────────────────────────────┐
│              NTS - Network Time Security                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Problem: NTP ist unverschlüsselt und unauthentifiziert       │
│   → Man-in-the-Middle kann Zeit manipulieren                   │
│   → Zertifikate können "ungültig" gemacht werden               │
│                                                                  │
│   Lösung: NTS (RFC 8915)                                       │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │ 1. NTS-KE (Key Exchange) über TLS (TCP 4460)           │  │
│   │    → Authentifizierung, Schlüsselaustausch             │  │
│   │                                                          │  │
│   │ 2. NTP mit AEAD (Authenticated Encryption)              │  │
│   │    → Integrität und Authentizität der Zeitdaten        │  │
│   └─────────────────────────────────────────────────────────┘  │
│                                                                  │
│   Unterstützung:                                                │
│   • time.cloudflare.com (NTS)                                  │
│   • Chrony (ab Version 4.0)                                    │
│   • NTPsec                                                     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Praxisbeispiele

> [!example] NTP-Befehle
> 
> **Linux (ntpq):**
> ```bash
> $ ntpq -p
>      remote           refid      st t when poll reach   delay   offset  jitter
> ==============================================================================
> *time.google.com .GOOG.           1 u   23   64  377   12.345   -0.123   0.456
> +ptbtime1.ptb.de .PTB.            1 u   45   64  377   25.678    0.234   0.789
> ```
> 
> **Linux (chronyc):**
> ```bash
> $ chronyc sources
> MS Name/IP address         Stratum Poll Reach LastRx Last sample
> ===============================================================
> ^* time.google.com               1   6   377    23   -123us[ -456us] +/-   12ms
> ```
> 
> **Windows:**
> ```cmd
> C:\> w32tm /query /status
> Leap Indicator: 0(no warning)
> Stratum: 3
> Source: time.windows.com
> 
> C:\> w32tm /resync
> Sending resync command to local computer...
> The command completed successfully.
> ```

### Öffentliche NTP-Server

| Server | Anbieter | Stratum |
|--------|----------|---------|
| `time.google.com` | Google | 1 |
| `time.cloudflare.com` | Cloudflare | 3 (NTS!) |
| `time.windows.com` | Microsoft | 2 |
| `ptbtime1.ptb.de` | PTB Deutschland | 1 |
| `pool.ntp.org` | NTP Pool Project | variiert |

## Prüfungsrelevante Themen

> [!warning] Klausurrelevanz: Mittel
>
> **Häufige Prüfungsthemen:**
> 1. Stratum-Hierarchie (0-16)
> 2. Warum ist Zeitsynchronisation wichtig?
> 3. Offset-Berechnung (Grundprinzip)
> 4. NTP vs. SNTP vs. PTP
> 5. Sicherheitsrisiken (Amplification)

### Typische Prüfungsfragen

> [!question] Übungsfragen
> 1. Was bedeutet Stratum 2?
> 2. Warum nutzt NTP UDP statt TCP?
> 3. Wie berechnet NTP den Offset?
> 4. Welche Probleme entstehen ohne Zeitsynchronisation?
> 5. Was ist ein NTP-Amplification-Angriff?

### Merkhilfen

> [!tip] Merkregeln
> - **Stratum 0** = Referenzuhren (GPS, Atomuhr)
> - **Stratum 1** = Direkt angeschlossen
> - **Stratum 16** = Unsynchronisiert
> - **Port 123** = NTP
> - **Offset** = Wie weit geht die Uhr falsch

## Zusammenfassung

```
┌─────────────────────────────────────────────────────────────────┐
│                    NTP auf einen Blick                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Zweck:      Zeitsynchronisation über Netzwerke               │
│   Schicht:    Layer 7 (Anwendungsschicht)                      │
│   Port:       UDP 123 (NTS zusätzlich TCP 4460)                │
│   Standard:   RFC 5905 (NTPv4)                                 │
│   Genauigkeit: 1-10 Millisekunden (typisch)                    │
│                                                                  │
│   Hierarchie:                                                   │
│   Stratum 0 (Referenz) → Stratum 1 → ... → Stratum 15         │
│   Stratum 16 = unsynchronisiert                                │
│                                                                  │
│   Berechnung:                                                   │
│   Offset = ((t2-t1) + (t3-t4)) / 2                             │
│   Delay = (t4-t1) - (t3-t2)                                    │
│                                                                  │
│   Sicherheit: NTS für Authentifizierung und Integrität        │
│   Alternativen: PTP (IEEE 1588) für Sub-µs Genauigkeit        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Querverweise

- [[../05-Sicherheit/03-TLS|TLS]] – Zertifikate benötigen korrekte Zeit
- [[02-DHCP|DHCP]] – Kann NTP-Server-Adresse liefern (Option 42)
- [[03-DNS|DNS]] – NTP-Server werden oft per DNS aufgelöst
- [[../../02-Betriebssysteme/04-Synchronisation/00-Synchronisation-Index|Synchronisation (BS)]] – Uhren in verteilten Systemen

## Quellen

- [[A-RFC-Index#RFC 5905|RFC 5905]] - Network Time Protocol Version 4
- [[A-RFC-Index#RFC 4330|RFC 4330]] - Simple Network Time Protocol (SNTP)
- [[A-RFC-Index#RFC 8915|RFC 8915]] - Network Time Security for NTP
