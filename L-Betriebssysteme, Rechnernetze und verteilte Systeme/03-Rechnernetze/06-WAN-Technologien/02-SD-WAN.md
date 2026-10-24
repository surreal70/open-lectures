---
author: Andreas Hümmer
title: SD-WAN - Software-Defined WAN
tags:
  - content
  - rn
  - wan
  - sd-wan
  - sdn
  - overlay
created: '2026-10-13'
modified: '2026-10-24'
bereich: RN
---

# SD-WAN - Software-Defined WAN

> [!info] Lernziele
> - Verstehen des Overlay/Underlay-Konzepts bei SD-WAN
> - Kennenlernen der zentralen Steuerung über den SD-WAN Controller
> - Verstehen der Vorteile gegenüber traditionellem WAN (MPLS)
> - Kennen der unterstützten Transporttypen (MPLS, Internet, LTE/5G)
> - Verstehen von Application-aware Routing und QoS-Funktionen

## Definition

> [!quote] Definition
> **SD-WAN (Software-Defined Wide Area Network)** ist eine Architektur, die Software-Defined-Networking-Konzepte auf WAN-Verbindungen anwendet. Es abstrahiert die Transportschicht und ermöglicht zentrale Steuerung über verschiedene Verbindungstypen hinweg.
## Eigenschaften

| Eigenschaft | Beschreibung |
|-------------|--------------|
| **Architektur** | Overlay über beliebige Underlay-Netze |
| **Steuerung** | Zentraler Controller (Orchestrator) |
| **Transport** | MPLS, Internet, LTE/5G, Satellit, ... |
| **Verschlüsselung** | IPsec oder proprietär |
| **Management** | Cloud-basiert oder On-Premise |

## Architektur

![[sdwan-architecture.png]]
*<span class="fig-id">03-06-02-sdwan-architecture</span>: SD-WAN-Architektur mit zentralem Controller, Edge Devices und verschiedenen Underlay-Transportoptionen.*

## Kernfunktionen

### Dynamic Path Selection

SD-WAN wählt automatisch den optimalen Pfad basierend auf Echtzeit-Metriken:

| Metrik | Beschreibung |
|--------|--------------|
| **Latenz** | Verzögerung in Millisekunden |
| **Jitter** | Schwankung der Latenz |
| **Packet Loss** | Paketverlustrate |
| **Bandbreite** | Verfügbare Kapazität |

Bei Verschlechterung eines Pfads (z.B. Internet-Leitung) wird Traffic automatisch auf einen besseren Pfad (z.B. MPLS oder LTE) umgeleitet – oft in unter einer Sekunde.

### Application-Aware Routing

SD-WAN erkennt Anwendungen durch **Deep Packet Inspection (DPI)** und routet sie intelligent:

| Anwendung | Priorität | Bevorzugter Pfad |
|-----------|-----------|------------------|
| Voice/Video (Teams, Zoom) | Kritisch | MPLS oder Pfad mit niedrigster Latenz |
| ERP, CRM | Hoch | Zuverlässiger Pfad |
| Web-Browsing | Normal | Internet |
| Backup, Updates | Niedrig | Günstigster Pfad |

> [!example] Beispiel
> Ein Zoom-Call wird automatisch über die MPLS-Leitung geroutet, während gleichzeitige Windows-Updates über die günstigere Internet-Leitung laufen.

### WAN Optimization

Techniken zur Bandbreitenoptimierung:

- **Deduplikation:** Gleiche Datenblöcke werden nur einmal übertragen
- **Kompression:** Daten werden vor der Übertragung komprimiert
- **Caching:** Häufig abgerufene Inhalte werden lokal zwischengespeichert
- **TCP-Optimierung:** Anpassung von Window-Size und Congestion Control

### Zero-Touch Provisioning (ZTP)

Neue Standorte können ohne manuelle Konfiguration vor Ort eingerichtet werden:

1. Edge-Device wird an Standort geliefert
2. Device wird mit Internet verbunden und eingeschaltet
3. Device kontaktiert Cloud-Controller automatisch
4. Controller pusht Konfiguration zum Device
5. VPN-Tunnel werden automatisch aufgebaut

**Vorteil:** Deployment in Minuten statt Wochen, kein Techniker vor Ort erforderlich.

### Segmentation

Logische Trennung von Traffic für Sicherheit und Compliance:

| Segment | Beispiel-Traffic | Isolation |
|---------|------------------|-----------|
| Corporate | ERP, E-Mail, Intranet | Streng isoliert |
| Guest | Internet für Besucher | Nur Internet-Zugang |
| IoT | Sensoren, Kameras | Eingeschränkt |
| PCI | Zahlungsverkehr | Compliance-konform |

Segmente können unterschiedliche Security-Policies und Routing-Regeln haben.

## SD-WAN vs. MPLS

| Aspekt | MPLS | SD-WAN |
|--------|------|--------|
| **Kosten** | Hoch | Niedriger |
| **Flexibilität** | Gering | Hoch |
| **Deployment-Zeit** | Wochen/Monate | Minuten/Stunden |
| **Multi-Cloud** | Schwierig | Native Unterstützung |
| **Sicherheit** | Provider-abhängig | Integriert |
| **QoS** | Garantiert | Anwendungsbasiert |

## Anbieter

Die wichtigsten SD-WAN-Anbieter im Markt:

| Anbieter | Produkt | Besonderheit |
|----------|---------|--------------|
| **Cisco** | Viptela, Meraki | Marktführer, umfangreiches Portfolio |
| **VMware** | VeloCloud | Cloud-First-Ansatz, starke Multi-Cloud-Integration |
| **Fortinet** | FortiGate SD-WAN | Integrierte Security (NGFW) |
| **Palo Alto** | Prisma SD-WAN | Fokus auf SASE-Integration |
| **Zscaler** | SD-WAN | Cloud-native, Zero-Trust-Fokus |
| **Versa** | Versa SASE | Integrierte SD-WAN + Security |
| **HPE Aruba** | EdgeConnect | Starke WAN-Optimierung |

> [!info] Gartner Magic Quadrant
> Cisco, VMware, Fortinet und Palo Alto sind typischerweise die "Leaders" im Gartner Magic Quadrant für SD-WAN.

## Prüfungsrelevanz

> [!warning] **Prüfungsrelevant**
NA

---

## Prüfungstipps

> [!warning] Häufige Fehler
> - Overlay und Underlay verwechseln: Overlay ist das logische Netz, Underlay der physische Transport
> - SD-WAN als reinen MPLS-Ersatz sehen – es ergänzt oft MPLS statt es zu ersetzen
> - Application-Aware Routing mit QoS verwechseln

> [!question] Typische Prüfungsfragen
> - Was ist der Unterschied zwischen Overlay und Underlay?
> - Warum ist SD-WAN flexibler als traditionelles MPLS?
> - Erklären Sie das Konzept von Application-Aware Routing
> - Was versteht man unter Zero-Touch Provisioning?
> - Welche Metriken nutzt Dynamic Path Selection?

> [!tip] Lernstrategie
> - Die drei Ebenen verstehen: Management Plane (Controller) → Control Plane (Policies) → Data Plane (Traffic)
> - Vergleichstabelle SD-WAN vs. MPLS auswendig lernen
> - Kernfunktionen mit Beispielen verknüpfen (z.B. Zoom-Call über MPLS)

---

## Weiterführende Ressourcen

- [Gartner: Magic Quadrant for SD-WAN](https://www.gartner.com/en/documents/sd-wan)
- [Cisco SD-WAN Documentation](https://www.cisco.com/c/en/us/solutions/enterprise-networks/sd-wan/index.html)
- [MEF SD-WAN Service Definition](https://www.mef.net/service-standards/sd-wan/)

---

## Zusammenhänge

- [[00-WAN-Index]] - WAN-Übersicht
- [[01-MPLS]] - Traditionelle Alternative
- [[03-SASE]] - SD-WAN + Security
- [[../05-Sicherheit/02-VPN/01-IPsec|IPsec]] - Verschlüsselung

---

## Quellen

- Gartner (2023). *Magic Quadrant for SD-WAN*.
- MEF (2020). *SD-WAN Service Attributes and Service Framework*.
- Cisco (2023). *SD-WAN Design Guide*.

