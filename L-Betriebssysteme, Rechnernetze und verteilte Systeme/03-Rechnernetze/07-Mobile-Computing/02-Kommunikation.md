---
author: Andreas Hümmer
title: Kommunikationsanforderungen Mobile Computing
tags:
  - content
  - rn
  - mobile-computing
  - wireless
  - communication
  - tcp
  - quic
created: '2026-10-24'
modified: '2026-10-29'
bereich: RN
---

# Kommunikationsanforderungen Mobile Computing

## Lernziele

> [!ziel] Lernziele
> Nach diesem Kapitel können Sie:
> - Die besonderen Anforderungen mobiler Kommunikation erklären
> - Kompensationsmaßnahmen für Verbindungsunterbrechungen benennen
> - Die Rolle von Proxies und VPNs verstehen
> - Moderne Protokolle wie QUIC/HTTP/3 einordnen

## Herausforderungen mobiler Kommunikation

### Verbindungsunterbrechungen

> [!important] Ziel
> Für den Benutzer soll die Kommunikation auch bei Unterbrechung **fehlerfrei weiter bestehen**.

Mobile Verbindungen sind inhärent unzuverlässig:

| Problem | Ursache | Häufigkeit |
|---------|---------|------------|
| **Funkloch** | Keine Netzabdeckung | Häufig in ländlichen Gebieten |
| **Handover-Latenz** | Wechsel zwischen Funkzellen | Bei Bewegung |
| **Signalschwächung** | Gebäude, Tunnel, Wetter | Situationsabhängig |
| **Netzüberlastung** | Zu viele Teilnehmer | Events, Rush Hour |
| **Energiesparmodus** | Gerät schaltet Funk ab | Bei niedrigem Akku |

### Abkopplungen (Disconnection)

Zwei Arten von Abkopplungen:

1. **Geplante Abkopplung**: Benutzer aktiviert Flugmodus, spart Akku
2. **Ungeplante Abkopplung**: Verbindungsverlust durch externe Faktoren

## Kompensationsmaßnahmen

### 1. Fehlerkorrektur auf Protokollebene (TCP)

TCP bietet bereits Mechanismen zur Fehlerbehebung:

![[tcp-retransmission.png]]
*<span class="fig-id">03-07-02-tcp-retransmission</span>: TCP-Retransmission bei Verbindungsunterbrechung – das verlorene Segment wird nach Timeout erneut gesendet.*

**Probleme von TCP bei mobilen Verbindungen:**
- Interpretiert Paketverlust als Stau → reduziert Sendefenster
- Lange Timeouts bei Funkunterbrechungen
- Head-of-Line Blocking bei Paketverlusten

### 2. Einsatz von Stellvertreter-Systemen (Proxies)

Proxies können mobile Verbindungen optimieren:

![[proxy-architecture.png]]
*<span class="fig-id">03-07-02-proxy-architecture</span>: Proxy als stabiler Vermittler zwischen instabiler Funkverbindung und kabelgebundenem Server.*

**Proxy-Funktionen:**

| Funktion | Beschreibung |
|----------|--------------|
| **Caching** | Speichert häufig angefragte Daten |
| **Compression** | Komprimiert Daten für schmalbandige Verbindungen |
| **Protocol Conversion** | Optimiert Protokolle für mobile Nutzung |
| **Connection Persistence** | Hält Server-Verbindung trotz Client-Unterbrechung |
| **Prefetching** | Lädt wahrscheinlich benötigte Daten vorab |

### 3. Resiliente VPN-Verbindungen

Klassische VPNs (IPsec, OpenVPN) haben Probleme bei IP-Wechseln:

> [!warning] Problem klassischer VPNs
> Bei Wechsel der IP-Adresse (z.B. WLAN → Mobilfunk) bricht die VPN-Verbindung ab und muss neu aufgebaut werden.

**Moderne Lösungen:**

| VPN-Technologie | Handhabung von IP-Wechseln |
|-----------------|---------------------------|
| **WireGuard** | Roaming-fähig durch Peer-Identifikation via Public Key |
| **IKEv2/IPsec** | MOBIKE-Extension für nahtlosen IP-Wechsel |
| **Tailscale** | Automatisches Reconnect, NAT-Traversal |
| **QUIC-basiert** | Connection-ID statt IP-Tupel |

### 4. Spezielle Protokolle: QUIC und HTTP/3

> [!info] QUIC (Quick UDP Internet Connections)
> QUIC ist ein von Google entwickeltes Transportprotokoll, das UDP als Basis nutzt und Probleme von TCP bei mobilen Verbindungen löst.

**QUIC-Vorteile für Mobile Computing:**

| Feature | Vorteil |
|---------|---------|
| **0-RTT Handshake** | Schnellerer Verbindungsaufbau bei bekannten Servern |
| **Connection Migration** | Verbindung überlebt IP-Adresswechsel |
| **Multiplexing ohne HoL-Blocking** | Streams unabhängig voneinander |
| **Integrierte Verschlüsselung** | TLS 1.3 eingebaut |

![[tcp-vs-quic.png]]
*<span class="fig-id">03-07-02-tcp-vs-quic</span>: Vergleich TCP vs. QUIC bei IP-Wechsel – QUIC erhält die Verbindung durch Connection-ID.*

**HTTP/3:**
- Nutzt QUIC als Transportprotokoll
- Ersetzt TCP+TLS durch QUIC
- Standard seit 2022 (RFC 9114)

## Offline-First Architektur

Moderne mobile Anwendungen sollten nach dem **Offline-First-Prinzip** entwickelt werden:

![[offline-first-app.png]]
*<span class="fig-id">03-07-02-offline-first-app</span>: Offline-First Architektur – lokaler Cache ermöglicht Funktion auch ohne Netzwerkverbindung.*

**Prinzipien:**
1. App funktioniert immer – auch ohne Netzwerk
2. Daten werden lokal gespeichert und später synchronisiert
3. Konflikte werden automatisch oder manuell aufgelöst
4. Benutzer wird über Sync-Status informiert

## Synchronisationsstrategien

| Strategie | Beschreibung | Anwendung |
|-----------|--------------|-----------|
| **Last-Write-Wins** | Neueste Änderung überschreibt | Einfache Daten |
| **Merge** | Änderungen werden kombiniert | Dokumente |
| **Conflict Resolution** | Benutzer entscheidet | Kritische Daten |
| **CRDT** | Konfliktfreie replizierte Datentypen | Echtzeit-Kollaboration |

## Prüfungsrelevanz

> [!warning] **Prüfungsrelevant**
> - Herausforderungen mobiler Kommunikation (Unterbrechungen, Abkopplungen)
> - Kompensationsmaßnahmen (TCP-Retransmission, Proxies, VPN)
> - QUIC/HTTP/3 Vorteile für Mobile Computing
> - Offline-First Architektur

> [!question] Typische Prüfungsfragen
> - Warum ist TCP für mobile Verbindungen suboptimal?
> - Welche Vorteile bietet QUIC gegenüber TCP für mobile Geräte?
> - Was versteht man unter Connection Migration?
> - Wie kann ein Proxy mobile Verbindungen verbessern?

## Zusammenhänge

- [[01-Einfuehrung]] – Grundlagen Mobile Computing
- [[03-Standortbestimmung]] – Lokalisierung
- [[04-Funknetze]] – Übertragungstechnologien
- [[../03-Referenzmodelle/07-Transportschicht/01-TCP|TCP]] – Klassisches Transportprotokoll
- [[../05-Sicherheit/02-VPN/02-WireGuard|WireGuard]] – Modernes VPN-Protokoll

## Quellen

- RFC 9000 – QUIC: A UDP-Based Multiplexed and Secure Transport
- RFC 9114 – HTTP/3
- Schiller, J.: Mobile Communications
- Google: QUIC Design Document

---

*Dateiende*
