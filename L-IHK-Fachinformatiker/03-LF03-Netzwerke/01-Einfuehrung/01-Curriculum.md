---
author: Andreas Hümmer
created: 2026-10-13
modified: 2026-10-13
tags:
  - content
  - lf03
  - curriculum
source: proTirone (CC-BY-4.0), Karsten Reincke
---

# LF03 Curriculum: Clients in Netzwerke einbinden

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Struktur und Ziele von Lernfeld 03 kennen
> - Die Kompetenzanforderungen des Rahmenlehrplans verstehen
> - Den Zusammenhang zu anderen Lernfeldern erkennen
> - Wissen, welche Werkzeuge für die Netzwerkarbeit benötigt werden

---

## Überblick

Lernfeld 03 ist eines der zentralen technischen Lernfelder im ersten Ausbildungsjahr. Es legt die Grundlagen für das Verständnis von Netzwerken, die in späteren Lernfeldern (insbesondere LF09) vertieft werden.

## Kompetenzbeschreibung (Rahmenlehrplan)

> [!quote] **Offizielle Kompetenzbeschreibung**
> Die Schülerinnen und Schüler verfügen über die Kompetenz, eine Netzwerkinfrastruktur zu analysieren sowie Clients in bestehende Netzwerke einzubinden.

### Handlungsfelder

Die Schülerinnen und Schüler:

1. **Analysieren** Netzwerkinfrastrukturen hinsichtlich der eingesetzten Komponenten und Protokolle
2. **Planen** die Integration von Clients unter Berücksichtigung von Adressierungsschemata
3. **Konfigurieren** Netzwerkschnittstellen und überprüfen die Konnektivität
4. **Dokumentieren** ihre Arbeit und erstellen Netzwerkpläne

## Themenübersicht

| Woche | Thema | Schwerpunkt |
|-------|-------|-------------|
| 1-2 | Grundbegriffe | Terminologie, Netzwerkkomponenten |
| 3-4 | Architekturen | OSI-Modell, TCP/IP, Topologien |
| 5-6 | Adressierung | MAC, IPv4, IPv6 |
| 7-8 | Protokolle | ARP, DHCP, DNS |
| 9-10 | Praxis | Konfiguration, Troubleshooting |

## Werkzeuge und Tools

Für die praktische Arbeit in LF03 werden folgende Werkzeuge benötigt:

### Diagnosewerkzeuge (Kommandozeile)

| Befehl | Zweck |
|--------|-------|
| `ping` | Erreichbarkeit testen |
| `ipconfig` / `ip addr` | IP-Konfiguration anzeigen |
| `arp -a` | ARP-Cache anzeigen |
| `tracert` / `traceroute` | Route zu Ziel verfolgen |
| `nslookup` / `dig` | DNS-Abfragen |
| `netstat` | Netzwerkverbindungen anzeigen |

### Dokumentationswerkzeuge

- **draw.io** — Netzwerkdiagramme erstellen
- **Freeplane** — Mindmaps für Begriffsstrukturen
- **Wireshark** — Netzwerkverkehr analysieren (fortgeschritten)

> [!tip] **Übung: Werkzeuge installieren**
> - [ ] Installiere draw.io auf deinem Rechner
> - [ ] Installiere Freeplane für Mindmaps
> - [ ] Teste `ping 8.8.8.8` in der Kommandozeile

## Zusammenhang mit anderen Lernfeldern

```
LF01 ──────┐
           │
LF02 ──────┼──→ LF03 (Netzwerke) ──→ LF09 (Vertiefung)
           │          │
LF04 ◄─────┘          └──→ LF06 (Serviceanfragen)
(Sicherheit)
```

- **LF01/02**: Betriebliche Grundlagen, Hardware-Kenntnisse
- **LF03**: Netzwerk-Grundlagen (dieses Lernfeld)
- **LF04**: Baut auf Netzwerkwissen auf (Sicherheitskonzepte)
- **LF06**: Serviceanfragen erfordern Netzwerk-Diagnose
- **LF09**: Vertiefung der Netzwerkthemen

## Zusammenhänge

- → [[02-Grundbegriffe|Nächstes Kapitel: Grundbegriffe]]
- → [[00-LF03-Index|Zurück zur LF03-Übersicht]]
- → [[Glossar|Begriffsdefinitionen]]

> [!warning] **Prüfungsrelevant**
> - Kenntnis der Rahmenlehrplan-Kompetenzen
> - Umgang mit Diagnose-Tools (ping, ipconfig, tracert)
> - Verständnis der Lernfeld-Zusammenhänge

> [!question] **Typische Prüfungsfragen**
> - Welche Werkzeuge verwenden Sie zur Netzwerkdiagnose?
> - Wie überprüfen Sie die Erreichbarkeit eines Hosts?
> - Welche Informationen liefert der Befehl `ipconfig /all`?

## Quellen

- Rahmenlehrplan für Fachinformatiker (KMK, 2020)
- proTirone: LF03 Curriculum (Karsten Reincke, CC-BY-4.0)

> [!tip] **Weiterführende Links**
> - [[02-Grundbegriffe|Grundbegriffe der Netzwerktechnik]]
> - [Rahmenlehrplan PDF](https://www.kmk.org)
