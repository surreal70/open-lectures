---
author: Andreas Hümmer
title: MPLS - Multiprotocol Label Switching
tags:
  - content
  - rn
  - wan
  - mpls
  - carrier
  - label-switching
created: '2026-10-13'
modified: '2026-10-24'
bereich: RN
---

# MPLS - Multiprotocol Label Switching

> [!info] Lernziele
> - Verstehen des Label-basierten Forwarding-Konzepts bei MPLS
> - Kennenlernen des MPLS-Headers (Shim Header) und seiner Felder
> - Unterscheiden zwischen CE, PE und P-Routern im MPLS-Netzwerk
> - Verstehen der Label-Operationen (Push, Swap, Pop)
> - Kennen typischer Einsatzszenarien (Provider-Backbones, VPNs)

## Definition

> [!quote] Definition
> **MPLS (Multiprotocol Label Switching)** ist eine Technologie zur effizienten Weiterleitung von Paketen in Provider-Netzwerken. Statt IP-basiertem Routing werden kurze Labels für schnelles Forwarding verwendet.
## Eigenschaften

| Eigenschaft | Wert |
|-------------|------|
| **Layer** | Zwischen 2 und 3 ("Layer 2.5") |
| **Label-Größe** | 32 Bit (4 Bytes) |
| **Forwarding** | Label-basiert (nicht IP-basiert) |
| **Protokoll** | LDP (Label Distribution Protocol) |
| **Anwendung** | Provider-Backbones, VPNs |

## MPLS-Header (Shim Header)

![[mpls-header.png]]
*<span class="fig-id">03-06-01-mpls-header</span>: MPLS Shim Header mit Label (20 Bit), Traffic Class, Bottom-of-Stack-Bit und TTL.*

## Funktionsprinzip

![[mpls-label-switching.png]]
*<span class="fig-id">03-06-01-mpls-label-switching</span>: MPLS Label Switching mit CE/PE/P-Routern und Label-Operationen (Push, Swap, Pop).*

## Label-Operationen

MPLS verwendet drei grundlegende Operationen zur Label-Verarbeitung:

| Operation | Router | Beschreibung |
|-----------|--------|--------------|
| **Push** | PE (Ingress) | Label wird auf das IP-Paket aufgesetzt |
| **Swap** | P | Label wird durch neues Label ersetzt |
| **Pop** | PE (Egress) | Label wird entfernt, IP-Paket weitergeleitet |

### Push (Label Imposition)

Der **Ingress PE-Router** empfängt ein IP-Paket vom Kunden und fügt einen MPLS-Header hinzu:

```
[IP-Paket] → PE → [Label | IP-Paket]
```

Das Label wird basierend auf der **FEC (Forwarding Equivalence Class)** bestimmt – typischerweise das Ziel-Präfix.

### Swap (Label Switching)

**P-Router** im Backbone tauschen das eingehende Label gegen ein ausgehendes Label:

```
[Label_in | IP] → P → [Label_out | IP]
```

Die Lookup-Tabelle heißt **LFIB (Label Forwarding Information Base)**. Der P-Router sieht nie den IP-Header – nur das Label.

### Pop (Label Disposition)

Der **Egress PE-Router** entfernt das Label und leitet das ursprüngliche IP-Paket an den Kunden weiter:

```
[Label | IP-Paket] → PE → [IP-Paket]
```

### PHP (Penultimate Hop Popping)

Eine Optimierung, bei der das Label bereits am **vorletzten** Router (Penultimate Hop) entfernt wird:

```
[Label | IP] → P (vorletzte) → [IP] → PE (Egress) → CE
```

**Vorteil:** Der Egress-PE muss nur noch IP-Routing durchführen, nicht Label-Lookup + IP-Lookup. Das spart einen Lookup-Vorgang.

> [!info] PHP-Signalisierung
> PHP wird über LDP signalisiert: Der Egress-PE teilt dem vorletzten Router mit, dass er das Label "poppen" soll, indem er das **Implicit Null Label (3)** ankündigt.

## MPLS VPN (L3VPN)

MPLS ermöglicht die Bereitstellung von **Virtual Private Networks** über eine gemeinsame Provider-Infrastruktur.

### VRF (Virtual Routing and Forwarding)

Jeder Kunde erhält eine eigene, isolierte Routing-Tabelle auf dem PE-Router:

| Komponente | Beschreibung |
|------------|--------------|
| **VRF** | Virtuelle Routing-Instanz pro Kunde |
| **RD** | Route Distinguisher – macht Präfixe eindeutig |
| **RT** | Route Target – steuert Import/Export von Routen |

> [!example] Beispiel: Überlappende Adressräume
> - Kunde A: 10.0.0.0/24 → VRF_A mit RD 65000:100
> - Kunde B: 10.0.0.0/24 → VRF_B mit RD 65000:200
> 
> Beide Kunden nutzen denselben IP-Bereich, aber durch unterschiedliche RDs sind die Routen im Provider-Netz eindeutig unterscheidbar.

### Route Distinguisher (RD)

Der RD ist ein 8-Byte-Präfix, das an jede VPN-Route angehängt wird:

```
VPN-IPv4-Adresse = RD (8 Byte) + IPv4-Präfix (4 Byte)

Beispiel: 65000:100:10.0.0.0/24
          ─────────  ──────────
             RD        Präfix
```

**Formate:**
- Typ 0: `ASN:nn` (z.B. 65000:100)
- Typ 1: `IP:nn` (z.B. 192.168.1.1:100)

### Route Target (RT)

Route Targets steuern, welche Routen zwischen VRFs ausgetauscht werden:

- **Export RT:** Markiert Routen beim Verlassen einer VRF
- **Import RT:** Filtert, welche Routen in eine VRF importiert werden

```
VRF Kunde-A                          VRF Kunde-B
┌──────────────┐                     ┌──────────────┐
│ Export: 100  │ ────────────────→   │ Import: 100  │
│ Import: 200  │ ←────────────────   │ Export: 200  │
└──────────────┘                     └──────────────┘
```

### MP-BGP für VPN-Routen

**Multiprotocol BGP** transportiert VPN-Routen zwischen PE-Routern:

- Address Family: **VPNv4** (AFI=1, SAFI=128)
- Trägt RD + Präfix + RT als Extended Community
- PE-Router peeren untereinander (iBGP Full Mesh oder Route Reflector)

```
PE1 ──── MP-BGP (VPNv4) ────── PE2
         [RD:Präfix + RT]
```

## Vor- und Nachteile

### Vorteile

| Vorteil | Beschreibung |
|---------|--------------|
| **QoS-Garantien** | Traffic Class (TC) im Label ermöglicht priorisierte Weiterleitung |
| **Traffic Engineering** | MPLS-TE erlaubt explizite Pfadsteuerung (Constraint-Based Routing) |
| **Schnelles Forwarding** | Label-Lookup schneller als IP-Longest-Prefix-Match |
| **VPN-Unterstützung** | Native L2VPN und L3VPN-Dienste |
| **Zuverlässigkeit** | Fast Reroute (FRR) für sub-50ms Failover |
| **Multiprotokoll** | Kann IPv4, IPv6, Ethernet und andere Protokolle transportieren |

### Nachteile

| Nachteil | Beschreibung |
|----------|--------------|
| **Hohe Kosten** | Dedizierte Leitungen, teure Provider-Verträge |
| **Inflexibilität** | Änderungen (neue Standorte, Bandbreite) dauern Wochen |
| **Provider-Abhängigkeit** | Kein Multi-Provider ohne zusätzliche Komplexität |
| **Keine Internet-Integration** | Cloud-Dienste nicht nativ erreichbar |
| **Komplexität** | LDP, MP-BGP, VRF – hoher Konfigurationsaufwand |

> [!warning] MPLS vs. SD-WAN
> Diese Nachteile sind der Hauptgrund, warum viele Unternehmen von MPLS zu SD-WAN migrieren. SD-WAN bietet Flexibilität und Kostenersparnis durch Nutzung von Internet-Leitungen.

## Prüfungsrelevanz

> [!warning] **Prüfungsrelevant**
> NA

---

## Prüfungstipps

> [!warning] Häufige Fehler
> - CE und PE verwechseln: CE gehört dem Kunden, PE dem Provider
> - RD und RT verwechseln: RD macht Routen eindeutig, RT steuert den Austausch
> - "Layer 2.5" nicht erklären können: MPLS sitzt zwischen Layer 2 (Ethernet) und Layer 3 (IP)

> [!question] Typische Prüfungsfragen
> - Erklären Sie die drei Label-Operationen Push, Swap und Pop
> - Was ist der Unterschied zwischen CE, PE und P-Routern?
> - Warum wird MPLS als "Layer 2.5" bezeichnet?
> - Was ist PHP (Penultimate Hop Popping) und welchen Vorteil bietet es?
> - Wie ermöglicht MPLS überlappende Kundenadressräume?

> [!tip] Lernstrategie
> - Die Paketreise durch das MPLS-Netz nachvollziehen (Push → Swap → Swap → Pop)
> - VRF/RD/RT-Konzept mit konkretem Beispiel durchspielen
> - Vergleich MPLS vs. SD-WAN für Diskussionsfragen vorbereiten

---

## Weiterführende Ressourcen

- [Cisco MPLS Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/mp_l3_vpns/configuration/xe-16/mp-l3-vpns-xe-16-book.html)
- [MPLS Fundamentals (Cisco Press)](https://www.ciscopress.com/store/mpls-fundamentals-9781587051975)
- [RFC 3031 - MPLS Architecture](https://datatracker.ietf.org/doc/html/rfc3031)

---

## Zusammenhänge

- [[00-WAN-Index]] - WAN-Übersicht
- [[02-SD-WAN]] - Nachfolger/Ergänzung
- [[../03-Referenzmodelle/06-Netzwerkschicht/02-Routing|Routing]] - IP-Routing vs. Label-Switching
- [[../05-Sicherheit/02-VPN/00-VPN-Index|VPN]] - VPN-Grundlagen

---

## Quellen

- RFC 3031 - MPLS Architecture (Rosen et al., 2001)
- RFC 3032 - MPLS Label Stack Encoding
- RFC 4364 - BGP/MPLS IP Virtual Private Networks (VPNs)
- Tanenbaum, A. S., & Wetherall, D. J. (2021). *Computer Networks* (6th ed.). Pearson.

