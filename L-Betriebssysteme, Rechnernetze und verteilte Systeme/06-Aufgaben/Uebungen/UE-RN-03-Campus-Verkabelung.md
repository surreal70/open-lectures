---
author: Andreas Hümmer
title: Übung - Campus-Netzwerkverkabelung
tags:
  - uebung
  - rn
  - verkabelung
  - layer1
  - layer2
  - lwl
  - kupfer
  - strukturierte-verkabelung
created: '2026-10-13'
modified: '2026-10-13'
bereich: RN
---

# Übung: Campus-Netzwerkverkabelung

## Ausgangssituation

Ein mittelständisches Unternehmen plant die Netzwerkinfrastruktur für seinen neuen Campus mit drei Gebäuden. Sie sind als Netzwerkplaner beauftragt, eine geeignete Verkabelungslösung zu entwerfen.

---

## Campus-Lageplan

![[campus-lageplan.png]]
*<span class="fig-id">06-UE-03-campus-lageplan</span>: Campus-Lageplan mit drei Gebäuden und Kabeltrassen (Maßstab: 2 Pixel = 1 Meter)*

---

## Gebäudedaten

| Gebäude | Funktion | Grundfläche | Etagen | Arbeitsplätze | Verteiler |
|---------|----------|-------------|--------|---------------|-----------|
| **A** | Verwaltung | 60m × 30m | 3 | 150 | V-A |
| **B** | Produktion | 80m × 40m | 2 | 80 | V-B |
| **C** | Rechenzentrum | 50m × 50m | 1 | 20 + Server | V-C |

---

## Kabeltrassenlängen

| Trasse | Von | Nach | Länge (Luftlinie) | Geschätzte Kabellänge* |
|--------|-----|------|-------------------|------------------------|
| **1** | V-A (Geb. A) | V-B (Geb. B) | 120m | ca. 150m |
| **2** | Verbindung | Geb. B Eingang | 180m | ca. 220m |
| **3** | V-A (Geb. A) | V-C (Geb. C) | 280m | ca. 350m |

*Geschätzte Kabellänge berücksichtigt: Verlegereserve, Steigzonen, Kabelführung in Gebäuden (+20-25%)

---

## Anforderungen

### Bandbreite

| Verbindung | Mindestbandbreite | Wünschenswert |
|------------|-------------------|---------------|
| **Backbone** (zwischen Gebäuden) | 10 Gbit/s | 40 Gbit/s |
| **Client-Anbindung** (Arbeitsplätze) | 1 Gbit/s | 2,5 Gbit/s |
| **Server-Anbindung** (Geb. C) | 10 Gbit/s | 25 Gbit/s |

### Ausfallsicherheit

- **Backbone**: Redundante Verbindungen zwischen allen Gebäuden
- **Keine Single-Point-of-Failure** für die Anbindung von Gebäude C (Rechenzentrum)
- **Maximale Ausfallzeit** bei Kabelbruch: < 50ms (Umschaltzeit)

### Besondere Bedingung: Gebäude C

> [!warning] **Potentialtrennung erforderlich!**
> Gebäude C verfügt über einen **separaten Stromanschluss ohne gemeinsame Erdung** mit Gebäude A und B. Dies ist typisch für Rechenzentren mit USV und Notstromversorgung.
> 
> **Problem**: Bei Kupferverkabelung können **Ausgleichsströme** über die Kabelschirmung fließen und:
> - Störungen verursachen
> - Brandgefahr darstellen
> - Geräte beschädigen

---

## Aufgaben

### Aufgabe 1: Medienanalyse für Trasse 1 und 2 (2 Punkte)

Analysieren Sie die Trassenlängen für die Verbindungen zwischen Gebäude A und B. Bestimmen Sie, welche Übertragungsmedien (Kupfer oder LWL) für diese Strecken geeignet sind. Berücksichtigen Sie dabei die maximalen Segmentlängen der verschiedenen Ethernet-Standards und die geforderten Bandbreiten.

---

### Aufgabe 2: Medienauswahl für Trasse 3 (2 Punkte)

Begründen Sie, warum für die Verbindung zu Gebäude C (Rechenzentrum) **zwingend Glasfaser** verwendet werden muss. Erklären Sie das Problem der Potentialtrennung und welche Gefahren bei Kupferverkabelung entstehen würden.

---

### Aufgabe 3: Ethernet-Standards für Backbone (2 Punkte)

Wählen Sie geeignete Ethernet-Standards für die Backbone-Verbindungen zwischen den Gebäuden. Geben Sie jeweils an:
- IEEE-Bezeichnung (z.B. 10GBASE-SR)
- Maximale Reichweite
- Benötigter LWL-Typ (OM3, OM4 oder OS2)

---

### Aufgabe 4: Ethernet-Standards für Client-Anbindung (2 Punkte)

Wählen Sie geeignete Ethernet-Standards für die Client-Anbindung in den Gebäuden. Begründen Sie Ihre Wahl der Kabelkategorie (Cat 5e, Cat 6, Cat 6a oder Cat 7) unter Berücksichtigung der Zukunftssicherheit.

---

### Aufgabe 5: Core-Switch im Verteiler A (2 Punkte)

Beschreiben Sie die Anforderungen an den Core-Switch im Verteiler A (Gebäude A):
- Layer 2 oder Layer 3?
- Welche Port-Typen werden benötigt?
- Welche SFP/SFP+-Module für die LWL-Strecken?

---

### Aufgabe 6: Switches in Verteiler B und C (2 Punkte)

Bestimmen Sie die Anforderungen an die Switches in den Verteilern B und C:
- Anzahl und Typ der Uplink-Ports
- Anzahl der Access-Ports für Clients
- Besonderheiten für den Switch im Rechenzentrum (Gebäude C)

---

### Aufgabe 7: Redundante Backbone-Topologie (2 Punkte)

Entwerfen Sie eine redundante Verkabelungstopologie für die Backbone-Verbindungen. Skizzieren Sie, wie die drei Gebäude so verbunden werden können, dass beim Ausfall einer Leitung die Kommunikation weiterhin möglich ist.

---

### Aufgabe 8: Spanning Tree Protocol (2 Punkte)

Erklären Sie, welches Layer-2-Protokoll bei der redundanten Topologie Schleifen verhindert. Vergleichen Sie STP, RSTP und MSTP hinsichtlich ihrer Konvergenzzeit und begründen Sie, welche Variante hier eingesetzt werden sollte, um die geforderte Umschaltzeit < 50ms zu erreichen.

---

### Aufgabe 9: Strukturierte Verkabelung – Ebenen (2 Punkte)

Ordnen Sie Ihre Verkabelungslösung in das Konzept der strukturierten Verkabelung ein. Beschreiben Sie, welche Komponenten zur Primär-, Sekundär- und Tertiärverkabelung gehören.

---

### Aufgabe 10: Normen und Standards (2 Punkte)

Nennen Sie mindestens drei relevante Normen für die strukturierte Verkabelung und erklären Sie kurz deren Anwendungsbereich:
- Eine internationale Norm (ISO/IEC)
- Eine europäische Norm (EN)
- Eine amerikanische Norm (TIA/EIA)

---

## Hinweise und Grenzwerte

### Maximale Segmentlängen Ethernet über Kupfer

| Standard | Bezeichnung | Bandbreite | Max. Länge | Kabeltyp |
|----------|-------------|------------|------------|----------|
| 1000BASE-T | Gigabit Ethernet | 1 Gbit/s | 100m | Cat 5e/6 |
| 2.5GBASE-T | 2.5G Ethernet | 2,5 Gbit/s | 100m | Cat 5e/6 |
| 5GBASE-T | 5G Ethernet | 5 Gbit/s | 100m | Cat 6 |
| 10GBASE-T | 10G Ethernet | 10 Gbit/s | 55-100m | Cat 6a/7 |

### Maximale Segmentlängen Ethernet über LWL

| Standard | Bandbreite | Multimode (OM3) | Multimode (OM4) | Singlemode (OS2) |
|----------|------------|-----------------|-----------------|------------------|
| 1000BASE-SX | 1 Gbit/s | 300m | 400m | - |
| 1000BASE-LX | 1 Gbit/s | 550m | 550m | 5km |
| 10GBASE-SR | 10 Gbit/s | 300m | 400m | - |
| 10GBASE-LR | 10 Gbit/s | - | - | 10km |
| 40GBASE-SR4 | 40 Gbit/s | 100m | 150m | - |
| 40GBASE-LR4 | 40 Gbit/s | - | - | 10km |

### Potentialtrennung

> [!info] **Warum LWL bei getrennter Erdung?**
> - Glasfaser ist **elektrisch nicht leitend**
> - Keine Ausgleichsströme möglich
> - Galvanische Trennung automatisch gegeben
> - Bei Kupfer: Medienkonverter mit galvanischer Trennung oder LWL verwenden

---

## Bewertung

| Aufgabe | Thema | Punkte |
|---------|-------|--------|
| 1 | Medienanalyse Trasse 1+2 | 2 |
| 2 | Medienauswahl Trasse 3 (Potentialtrennung) | 2 |
| 3 | Ethernet-Standards Backbone | 2 |
| 4 | Ethernet-Standards Client | 2 |
| 5 | Core-Switch Verteiler A | 2 |
| 6 | Switches Verteiler B und C | 2 |
| 7 | Redundante Topologie | 2 |
| 8 | Spanning Tree Protocol | 2 |
| 9 | Strukturierte Verkabelung | 2 |
| 10 | Normen und Standards | 2 |
| **Gesamt** | | **20** |

---

## Musterlösung

> [!tip] **Für Dozenten**
> Die ausführliche Musterlösung mit drei Varianten (optimal, kostenoptimiert, WLAN-Hybrid) sowie vollständigem Reasoning finden Sie hier:
> 
> [[../Loesungen/LOE-UE-RN-03-Campus-Verkabelung|→ Musterlösung Campus-Verkabelung]]

---

## Weiterführende Themen

- [[../../03-Rechnernetze/03-Referenzmodelle/04-Physikalische-Schicht/01-Uebertragungsmedien|Übertragungsmedien]] - Kupfer vs. Glasfaser
- [[../../03-Rechnernetze/03-Referenzmodelle/04-Physikalische-Schicht/02-Signale|Signale]] - Signalübertragung und Dämpfung
- [[../../03-Rechnernetze/04-Basisprotokolle/05-Spanning-Tree|Spanning Tree Protocol]] - Loop-Vermeidung
- [[../../03-Rechnernetze/03-Referenzmodelle/05-Sicherungsschicht/00-Sicherungsschicht-Index|Sicherungsschicht]] - Layer 2

