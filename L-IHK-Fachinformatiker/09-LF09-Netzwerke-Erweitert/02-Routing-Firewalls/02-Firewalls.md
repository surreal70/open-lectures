---
title: "Firewalls – Konzepte und Strategien"
created: 2026-10-13
modified: 2026-10-13
type: lecture
tags:
  - lf09
  - firewall
  - sicherheit
  - netzwerk
source: proTirone (CC-BY-4.0)
---

# Firewalls – Konzepte und Strategien

> [!info] Lernziele
> - Firewall-Funktionen verstehen
> - Unterschied zwischen Allow- und Deny-Strategie erklären
> - DMZ-Konzepte anwenden können
> - VLAN-Grundlagen kennen

## Firewall-Grundlagen

### Was Firewalls können

Firewalls können (mindestens) filtern nach:

| Layer | Filterkriterium | Beispiel |
|-------|-----------------|----------|
| **III** | IP-Adresse | Zugriff von/auf bestimmte IPs erlauben/blockieren |
| **III** | Netzadresse | Ganzen Subnetzen Zugriff gewähren/verweigern |
| **IV** | Port | Anfragen an bestimmte Ports zulassen/blockieren |
| **III-VII** | Muster | Häufigkeit, Inhalt, Protokoll analysieren |

## Firewall-Strategien

### Default Allow (Whitelist)

> **Erlaube zuerst alles, unterbinde dann das, was nicht erlaubt sein soll**

```
┌─────────────────────────────────────────┐
│     ALLES ERLAUBT (Standard)            │
├─────────────────────────────────────────┤
│  ✗ Blockiere: Bekannte Angriffsmuster   │
│  ✗ Blockiere: Unerwünschte Ports        │
│  ✗ Blockiere: Verdächtige IPs           │
└─────────────────────────────────────────┘
```

| Vorteil | Nachteil |
|---------|----------|
| Einfach zu managen | Eher unsicher |
| "Sonderwünsche" oft schon möglich | Menschenbedingte Schlupflöcher |

### Default Deny (Blacklist)

> **Unterbinde zuerst alles, ermögliche dann das, was erlaubt sein soll**

```
┌─────────────────────────────────────────┐
│     ALLES VERBOTEN (Standard)           │
├─────────────────────────────────────────┤
│  ✓ Erlaube: HTTP/HTTPS (80, 443)        │
│  ✓ Erlaube: SSH (22) von Admin-Netz     │
│  ✓ Erlaube: DNS (53)                    │
└─────────────────────────────────────────┘
```

| Vorteil | Nachteil |
|---------|----------|
| Sicherer (weniger Schlupflöcher) | Aufwendiger zu managen |
| Explizite Kontrolle | "Sonderwünsche" bedeuten Aufwand |

> [!tip] Best Practice
> Für sicherheitskritische Umgebungen: **Default Deny** verwenden!

## DMZ – Demilitarisierte Zone

### Begriff

> [!quote] Ursprung
> "A 'demilitarized zone' is an area [...] which cannot be occupied or used for military purposes by any party to the conflict."

In der IT hat DMZ eine andere Bedeutung:

Eine **DMZ** ist ein Bereich zwischen den Routern ins Internet und den Routern in nachgelagerte Netze (Intranet). Sie ermöglicht unterschiedlich starke Firewall-Regeln für verschiedene Bereiche.

### Einstufige DMZ

```
┌─────────┐     ┌──────────────┐     ┌──────────┐
│Internet │────▶│    Router    │────▶│ Intranet │
└─────────┘     │  + Firewall  │     └──────────┘
                │              │
                │  ┌────────┐  │
                │  │  DMZ   │  │
                │  │Webserver│ │
                │  └────────┘  │
                └──────────────┘
```

### Zweistufige DMZ

```
┌─────────┐     ┌────────────┐     ┌─────────┐     ┌──────────┐
│Internet │────▶│Außenrouter │────▶│   DMZ   │────▶│Intranet- │
└─────────┘     │ (Gateway)  │     │         │     │  Router  │
                └────────────┘     │Webserver│     └──────────┘
                                   │Mailserver│          │
                                   └─────────┘     ┌──────────┐
                                                   │ Intranet │
                                                   └──────────┘
```

### Strategie für zweistufige DMZ

**Außenrouter/Gateway:**
1. Lasse initial alle Anfragen von außen zu
2. Erlaube alle Anfragen von innen nach außen
3. Unterbinde danach nur generell unzulässige Anfragen
4. Verbiete unerwünschte Anfragen von innen nach außen

**Binnenrouter/Intranet:**
1. Verbiete initial alle Zugriffe von außen
2. Erlaube nur explizit gewünschte Services (HTTPS, SMTP, VPN)
3. Erlaube Zugriff für bestimmte feste IP-Adressen

> [!warning] IP-Spoofing
> Vorsicht bei IP-basierten Freigaben – IP-Adressen können gefälscht werden!

## VLAN – Virtual Local Area Network

### Konzept

**VLAN** steht für **Virtual Local Area Network** und erfordert einen Layer-III-Switch.

```
┌─────────────────────────────────────────────────────────────┐
│                    Layer-III-Switch                         │
├───────┬───────┬───────┬───────┬───────┬───────┬───────┬─────┤
│Port 1 │Port 2 │Port 3 │Port 4 │Port 5 │Port 6 │Port 7 │Port8│
├───────┴───────┼───────┴───────┼───────┴───────┴───────┴─────┤
│   VLAN 10     │   VLAN 20     │          VLAN 30            │
│  (Entwicklung)│   (Finanzen)  │        (Management)         │
└───────────────┴───────────────┴─────────────────────────────┘
```

### Eigenschaften

- Alle Rechner sind Teil desselben **physischen** Netzes
- Switch kennt IP-Adresse und Port-Zuordnung jedes Rechners
- Mehrere Ports werden per Konfiguration zu **virtuellen Broadcast-Domänen** zusammengefasst
- Broadcast-Anfragen (ARP) werden nur innerhalb des VLANs propagiert

### Layer-III-Switch Varianten

| Typ | Beschreibung |
|-----|--------------|
| **Einfach** | Erwartet physisch angeschlossene Router für lokales Routing |
| **Komplex** | Emuliert Router als Teil seiner Software |

> [!important] Grundsätze
> 1. Layer-III-Switch routet von einer lokalen BCD in die nächste – oft ohne physischen Router
> 2. Layer-III-Switch routet NICHT von sich aus ins Internet

---

> [!tip] Übung
> 1. Ermitteln Sie, wie viele Firewalls in Ihrem Beispielnetz minimal benötigt werden
> 2. Konzipieren Sie eine DMZ für ein Firmennetz mit Entwicklungs- und Finanzabteilung
> 3. Realisieren Sie drei Abteilungen (FIN, MNG, HR) als VLANs auf einem Layer-III-Switch

## Weiterführende Literatur

- Schreiner: Computernetzwerke, 2014, S. 127 (VLANs)
- [ICRC – Demilitarized Zones](https://casebook.icrc.org/a_to_z/glossary/demilitarized-zones)

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (Karsten Reincke), lizenziert unter CC-BY-4.0.
> Inhalte wurden für das Open-Lectures-Format angepasst.
