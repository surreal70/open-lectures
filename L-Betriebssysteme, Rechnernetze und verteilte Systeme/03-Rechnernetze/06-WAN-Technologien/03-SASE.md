---
author: Andreas Hümmer
title: SASE - Secure Access Service Edge
tags:
  - content
  - rn
  - wan
  - sase
  - zero-trust
  - cloud
  - ztna
created: '2026-10-13'
modified: '2026-10-24'
bereich: RN
---

# SASE - Secure Access Service Edge

> [!info] Lernziele
> - Verstehen des SASE-Konzepts als Kombination von Netzwerk und Sicherheit
> - Kennenlernen der SASE-Komponenten (ZTNA, SWG, CASB, FWaaS)
> - Unterscheiden zwischen SSE (Security Service Edge) und SD-WAN als SASE-Bausteine
> - Verstehen des Zero-Trust-Prinzips bei SASE
> - Kennen der Vorteile Cloud-nativer Sicherheitsarchitekturen

## Definition

> [!quote] Definition
> **SASE (Secure Access Service Edge)**, ausgesprochen "sassy", ist ein von Gartner 2019 definiertes Cloud-Architekturmodell, das Netzwerk- und Sicherheitsfunktionen in einem einheitlichen, Cloud-nativen Service kombiniert.
## Komponenten

![[sase-components.png]]
*<span class="fig-id">03-06-03-sase-components</span>: SASE kombiniert Netzwerk (WAN Edge/SD-WAN) mit Sicherheit (SSE) in einer Cloud-nativen Plattform.*

## Komponenten erklärt

| Abkürzung | Name | Funktion |
|-----------|------|----------|
| **ZTNA** | Zero Trust Network Access | Identity-basierter Zugriff, ersetzt VPN |
| **SWG** | Secure Web Gateway | Web-Filterung, Malware-Schutz |
| **CASB** | Cloud Access Security Broker | Sicherheit für Cloud-Apps (SaaS) |
| **FWaaS** | Firewall as a Service | Cloud-basierte Firewall |
| **DLP** | Data Loss Prevention | Schutz vor Datenverlust |

## ZTNA - Zero Trust Network Access

![[ztna-vs-vpn.png]]
*<span class="fig-id">03-06-03-ztna-vs-vpn</span>: Vergleich Traditional VPN (vollständiger Netzwerkzugriff) mit ZTNA (anwendungsbasierter Zugriff nach "Never trust, always verify").*

## Architekturprinzipien

### Identity-Centric

Zugriff basiert auf **Identität**, nicht auf Netzwerkstandort:

- Benutzeridentität (SSO, MFA)
- Geräteidentität (Zertifikate, MDM-Status)
- Anwendungsidentität
- Kontextbewertung (Zeit, Ort, Risiko)

### Cloud-Native

SASE ist von Grund auf für die Cloud konzipiert:

| Aspekt | Traditionell | Cloud-Native |
|--------|--------------|--------------|
| Deployment | Hardware-Appliances | Software/Container |
| Skalierung | Manuell, Wochen | Automatisch, Minuten |
| Updates | Wartungsfenster | Continuous |
| Verfügbarkeit | Aktiv/Passiv | Multi-Region HA |

### Globale Edge-Präsenz

SASE-Anbieter betreiben **Points of Presence (PoPs)** weltweit:

- Benutzer verbinden sich zum nächsten PoP
- Geringe Latenz durch Nähe
- Security-Funktionen werden am Edge ausgeführt
- Typisch: 50-150+ PoPs weltweit (Zscaler: 150+, Cloudflare: 300+)

### Single-Pass Architecture

Alle Security-Funktionen in **einem Durchlauf**:

```
Traffic → [ZTNA + SWG + CASB + FWaaS + DLP] → Ziel
                    ↓
              Single Pass
         (nicht nacheinander)
```

**Vorteil:** Geringere Latenz, da nicht mehrere Appliances nacheinander durchlaufen werden.

## Anbieter

| Anbieter | Produkt | Stärken |
|----------|---------|---------|
| **Zscaler** | ZIA, ZPA | Marktführer SSE, größtes Edge-Netzwerk |
| **Palo Alto** | Prisma Access | Starke NGFW-Integration, Cortex XDR |
| **Cisco** | Umbrella + SD-WAN | Breites Portfolio, Meraki-Integration |
| **Cloudflare** | Cloudflare One | Größtes Anycast-Netzwerk, Developer-freundlich |
| **Netskope** | Netskope One | Starke CASB-Funktionen, DLP |
| **Fortinet** | FortiSASE | Integriert mit FortiGate, günstig |

> [!info] Gartner Magic Quadrant
> **SSE Leaders (2023):** Zscaler, Netskope, Palo Alto
> **SD-WAN Leaders:** Cisco, VMware, Fortinet, Palo Alto

## SASE vs. SSE

Gartner hat 2021 **SSE (Security Service Edge)** als separate Kategorie eingeführt:

| Aspekt | SSE | SASE |
|--------|-----|------|
| **Komponenten** | ZTNA, SWG, CASB, FWaaS | SSE + SD-WAN |
| **Fokus** | Security | Security + Networking |
| **Typischer Anbieter** | Zscaler, Netskope | Cisco, Fortinet, Palo Alto |
| **Use Case** | Remote User Security | Komplettes Branch-Office |

```
SASE = SSE + SD-WAN

┌─────────────────────────────────────────────────┐
│                    SASE                         │
│  ┌─────────────────────┐  ┌─────────────────┐  │
│  │        SSE          │  │     SD-WAN      │  │
│  │  • ZTNA             │  │  • Path Select  │  │
│  │  • SWG              │  │  • WAN Opt      │  │
│  │  • CASB             │  │  • QoS          │  │
│  │  • FWaaS            │  │  • ZTP          │  │
│  └─────────────────────┘  └─────────────────┘  │
└─────────────────────────────────────────────────┘
```

> [!tip] Praxisempfehlung
> Unternehmen mit reinen Remote-Usern können mit **SSE** starten. Für Branch-Offices mit lokaler Infrastruktur ist **vollständiges SASE** (inkl. SD-WAN) sinnvoller.

## Prüfungsrelevanz

> [!warning] **Prüfungsrelevant**
NA

---

## Prüfungstipps

> [!warning] Häufige Fehler
NA

> [!question] Typische Prüfungsfragen
> - Was sind die Kernkomponenten von SASE?
> - Erklären Sie das Zero-Trust-Prinzip
> - Worin unterscheidet sich ZTNA von einem klassischen VPN?
> - Was ist der Unterschied zwischen SASE und SSE?
> - Was versteht man unter "Single-Pass Architecture"?

> [!tip] Lernstrategie
> - Die fünf Hauptkomponenten auswendig lernen: ZTNA, SWG, CASB, FWaaS, DLP
> - "Never trust, always verify" als Mantra für Zero Trust
> - SASE = SD-WAN + SSE als einfache Formel

---

## Weiterführende Ressourcen

- [Gartner: The Future of Network Security Is in the Cloud](https://www.gartner.com/en/documents/sase) - Original SASE Paper (2019)
- [Gartner Magic Quadrant for SSE](https://www.gartner.com/en/documents/sse)
- [Zscaler: What is SASE?](https://www.zscaler.com/resources/security-terms-glossary/what-is-sase)

---

## Zusammenhänge

- [[00-WAN-Index]] - WAN-Übersicht
- [[02-SD-WAN]] - Netzwerk-Komponente von SASE
- [[../05-Sicherheit/02-VPN/00-VPN-Index|VPN]] - ZTNA ersetzt VPN teilweise
- [[../05-Sicherheit/01-Firewalls|Firewalls]] - FWaaS als Cloud-basierte Firewall

---

## Quellen

- Gartner (2019). *The Future of Network Security Is in the Cloud*. (SASE-Definition)
- Gartner (2021). *Magic Quadrant for Security Service Edge*.
- NIST SP 800-207: *Zero Trust Architecture*.

