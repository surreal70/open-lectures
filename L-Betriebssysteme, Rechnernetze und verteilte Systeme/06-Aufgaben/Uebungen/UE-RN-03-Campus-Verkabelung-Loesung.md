---
author: Andreas Hümmer
title: Musterlösung - Campus-Netzwerkverkabelung
tags:
  - loesung
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

# Musterlösung: Campus-Netzwerkverkabelung

Diese Musterlösung präsentiert drei verschiedene Lösungsansätze für die Campus-Verkabelungsaufgabe:

1. **Variante A: Optimale Lösung** – Maximale Performance und Zukunftssicherheit
2. **Variante B: Kostenoptimierte Lösung** – Wirtschaftlich mit gutem Preis-Leistungs-Verhältnis
3. **Variante C: WLAN-Hybrid-Lösung** – Kombination aus kabelgebundener Infrastruktur und Wireless

---

## Aufgabe 1: Medienanalyse für Trasse 1 und 2 (2 Punkte)

### Ausgangsdaten

| Trasse | Luftlinie | Geschätzte Kabellänge |
|--------|-----------|----------------------|
| T1 | 120m | ca. 150m |
| T2 | 180m | ca. 220m |

### Reasoning

**Kupfer-Analyse:**
- 10GBASE-T über Cat 6a: max. 100m → **Trasse 1 und 2 überschreiten dies deutlich**
- 1000BASE-T über Cat 5e/6: max. 100m → ebenfalls überschritten
- Selbst mit Repeatern wäre Kupfer problematisch (Latenz, zusätzliche Fehlerquellen)

**LWL-Analyse:**
- 10GBASE-SR über OM3: max. 300m → **Beide Trassen geeignet**
- 10GBASE-SR über OM4: max. 400m → **Beide Trassen geeignet**
- Multimode ausreichend, da < 400m

### Antwort

| Variante | Trasse 1 (150m) | Trasse 2 (220m) | Begründung |
|----------|-----------------|-----------------|------------|
| **A (Optimal)** | LWL OM4 | LWL OM4 | Maximale Reserve für 40G-Upgrade |
| **B (Kosten)** | LWL OM3 | LWL OM3 | OM3 günstiger, für 10G ausreichend |
| **C (WLAN)** | LWL OM3 | LWL OM3 | Backbone-Kapazität auch für WLAN nötig |

> [!info] **Zusatzinfo für Aufgabe 3**
> Die Medienauswahl hier bestimmt die möglichen Ethernet-Standards. OM4 ermöglicht längere Strecken bei 40G/100G und bietet mehr Zukunftssicherheit.

---

## Aufgabe 2: Medienauswahl für Trasse 3 (2 Punkte)

### Ausgangsdaten

- Trasse 3: 280m Luftlinie, ca. 350m Kabellänge
- Gebäude C: Separater Stromanschluss, keine gemeinsame Erdung

### Reasoning

**Das Problem der Potentialtrennung:**

1. **Unterschiedliche Erdpotentiale**: Gebäude A/B und C haben getrennte Erdungssysteme. Zwischen diesen können Spannungsdifferenzen von mehreren Volt bis zu hunderten Volt entstehen (bei Blitzeinschlag oder Netzfehlern).

2. **Kupferkabel als Brücke**: Bei Kupferverkabelung (auch geschirmte wie Cat 7) verbindet der Kabelschirm die Erdungssysteme galvanisch. Folge:
   - **Ausgleichsströme** fließen über die Schirmung
   - **Störungen** auf den Datenleitungen
   - **Brandgefahr** durch Überhitzung
   - **Geräteschäden** an Netzwerkkarten und Switches

3. **Glasfaser als Lösung**: LWL ist elektrisch nicht leitend → automatische galvanische Trennung, keine Ausgleichsströme möglich.

### Antwort

**Alle drei Varianten: Zwingend Glasfaser (LWL)**

| Aspekt | Kupfer | Glasfaser |
|--------|--------|-----------|
| Galvanische Trennung | ❌ Nein | ✅ Ja |
| Ausgleichsströme | ⚠️ Gefahr | ✅ Unmöglich |
| Blitzschutz | ❌ Überspannung möglich | ✅ Immun |
| Länge 350m mit 10G | ❌ Nicht möglich | ✅ Kein Problem |

> [!warning] **Prüfungsrelevant**
> Die Potentialtrennung ist ein **K.O.-Kriterium**. Auch wenn theoretisch Medienkonverter mit galvanischer Trennung existieren, ist LWL die einzig sinnvolle Lösung für diese Strecke.

---

## Aufgabe 3: Ethernet-Standards für Backbone (2 Punkte)

### Reasoning

**Anforderungen:**
- Mindestens 10 Gbit/s, wünschenswert 40 Gbit/s
- Strecken: 150m, 220m, 350m
- Bei Redundanz: zusätzliche Direktverbindung B↔C nötig (ca. 200m)

**Multimode vs. Singlemode:**
- Multimode (OM3/OM4): Günstiger, einfachere Stecker, ausreichend für < 400m
- Singlemode (OS2): Teurer, aber unbegrenzte Upgrade-Möglichkeit (100G+)

### Antwort

#### Variante A: Optimal (40 Gbit/s)

| Verbindung | Standard | Reichweite | LWL-Typ | Begründung |
|------------|----------|------------|---------|------------|
| V-A → V-B | 40GBASE-SR4 | 150m (max) | OM4 | Maximale Bandbreite |
| V-A → V-C | 40GBASE-LR4 | 10km | OS2 | Singlemode für Zukunft |
| V-B → V-C | 40GBASE-SR4 | 150m | OM4 | Redundanzstrecke |

**Reasoning**: OM4 für kurze Strecken (kostengünstig), OS2 für lange Strecke zu Rechenzentrum (Zukunftssicherheit für 100G+).

#### Variante B: Kostenoptimiert (10 Gbit/s)

| Verbindung | Standard | Reichweite | LWL-Typ | Begründung |
|------------|----------|------------|---------|------------|
| V-A → V-B | 10GBASE-SR | 300m | OM3 | Günstig, ausreichend |
| V-A → V-C | 10GBASE-LR | 10km | OS2 | Muss Singlemode sein |
| V-B → V-C | 10GBASE-SR | 300m | OM3 | Redundanzstrecke |

**Reasoning**: 10G erfüllt Mindestanforderung, OM3 reicht für die Strecken, OS2 nur wo technisch nötig.

#### Variante C: WLAN-Hybrid (10 Gbit/s)

| Verbindung | Standard | Reichweite | LWL-Typ | Begründung |
|------------|----------|------------|---------|------------|
| V-A → V-B | 10GBASE-SR | 300m | OM3 | WLAN-Traffic berücksichtigt |
| V-A → V-C | 10GBASE-LR | 10km | OS2 | Server-Anbindung kritisch |
| V-B → V-C | 10GBASE-SR | 300m | OM3 | Redundanz |

**Reasoning**: WLAN reduziert Client-Dichte am Kabel, aber Backbone muss Spitzenlast aller APs verkraften.

> [!tip] **SFP-Module für Aufgabe 5**
> - 10GBASE-SR: SFP+ mit LC-Duplex-Stecker
> - 10GBASE-LR: SFP+ mit LC-Duplex-Stecker (andere Wellenlänge)
> - 40GBASE-SR4: QSFP+ mit MPO/MTP-Stecker (12 Fasern)

---

## Aufgabe 4: Ethernet-Standards für Client-Anbindung (2 Punkte)

### Reasoning

**Anforderungen:**
- Mindestens 1 Gbit/s, wünschenswert 2,5 Gbit/s
- Innerhalb von Gebäuden → max. 90m Installationskabel + 10m Patchkabel = 100m
- Zukunftssicherheit für 10 Jahre

**Kabelkategorien im Vergleich:**

| Kategorie | Max. Frequenz | 1G | 2.5G | 5G | 10G | Kosten |
|-----------|---------------|----|----- |----|-----|--------|
| Cat 5e | 100 MHz | ✅ | ✅ | ❌ | ❌ | € |
| Cat 6 | 250 MHz | ✅ | ✅ | ✅ | ❌ | €€ |
| Cat 6a | 500 MHz | ✅ | ✅ | ✅ | ✅ | €€€ |
| Cat 7 | 600 MHz | ✅ | ✅ | ✅ | ✅ | €€€€ |

### Antwort

#### Variante A: Optimal

**Cat 6a** für alle Gebäude

- **Standard**: 2.5GBASE-T (aktuell), Upgrade-Pfad zu 5GBASE-T und 10GBASE-T
- **Begründung**: 
  - Unterstützt alle Standards bis 10 Gbit/s über volle 100m
  - Bessere Schirmung gegen Übersprechen (Alien Crosstalk)
  - Mehrpreis zu Cat 6 rechtfertigt sich durch 10+ Jahre Nutzungsdauer
  - Im Rechenzentrum (Geb. C) ohnehin erforderlich für Server

#### Variante B: Kostenoptimiert

**Cat 6** für Gebäude A und B, **Cat 6a** nur für Gebäude C

- **Standard**: 1000BASE-T (Geb. A/B), 10GBASE-T (Geb. C)
- **Begründung**:
  - Cat 6 unterstützt 1G und 2.5G problemlos
  - Cat 6 unterstützt 5G bis ca. 55m (für zentrale Bereiche nutzbar)
  - Nur Rechenzentrum benötigt zwingend 10G-Fähigkeit
  - Kostenersparnis ca. 30% bei der Verkabelung

#### Variante C: WLAN-Hybrid

**Cat 6** für alle Gebäude, **Cat 6a** nur für AP-Anschlüsse und Server

- **Standard**: 1000BASE-T (Clients), 2.5GBASE-T (Access Points)
- **Begründung**:
  - Weniger kabelgebundene Clients → geringere Anforderungen
  - WiFi 6/6E Access Points benötigen mindestens 2.5G Uplink
  - APs mit PoE++ (802.3bt) profitieren von Cat 6a (bessere Stromübertragung)

> [!info] **Hinweis zu PoE**
> Cat 6a ist für Power over Ethernet (PoE++) besser geeignet, da dickere Leiter weniger Wärme entwickeln. Relevant für Aufgabe 6 (Switches mit PoE).

---

## Aufgabe 5: Core-Switch im Verteiler A (2 Punkte)

### Reasoning

**Anforderungen an den Core-Switch:**
1. Zentrale Routing-Instanz für drei Gebäude → Layer 3 sinnvoll
2. Uplinks zu V-B und V-C → LWL-Ports (SFP+/QSFP+)
3. Lokale Anbindung in Gebäude A → Kupfer-Ports oder weitere SFP+
4. Redundanz → Stack-fähig oder modulares Chassis
5. Management → Out-of-Band-Management-Port

### Antwort

#### Variante A: Optimal

**Layer 3 Modular Chassis Switch**

| Anforderung | Spezifikation |
|-------------|---------------|
| Layer | Layer 3 (Routing zwischen VLANs/Subnetzen) |
| Uplink-Ports | 4× QSFP+ (40G) für Backbone |
| LWL-Module | 2× QSFP+ SR4 (OM4), 1× QSFP+ LR4 (OS2) |
| Downlink-Ports | 48× 10GBASE-T oder 24× SFP+ |
| Redundanz | Dual Power Supply, Stack-fähig |
| Features | OSPF/BGP, VRRP, LACP, QoS, 802.1X |

**SFP/QSFP-Module:**
- QSFP+ SR4 für OM4-Strecken (V-A→V-B, Redundanz)
- QSFP+ LR4 für OS2-Strecke (V-A→V-C)

#### Variante B: Kostenoptimiert

**Layer 3 Stackable Switch**

| Anforderung | Spezifikation |
|-------------|---------------|
| Layer | Layer 3 (statisches Routing, evtl. OSPF) |
| Uplink-Ports | 4× SFP+ (10G) |
| LWL-Module | 2× SFP+ SR (OM3), 1× SFP+ LR (OS2) |
| Downlink-Ports | 24-48× 1GBASE-T |
| Redundanz | Stack mit zweitem Switch |
| Features | Inter-VLAN-Routing, LACP, STP |

**Reasoning**: Stackable Switches sind deutlich günstiger als modulare Chassis, erfüllen aber die Grundanforderungen.

#### Variante C: WLAN-Hybrid

**Layer 3 Switch mit WLAN-Controller-Funktion**

| Anforderung | Spezifikation |
|-------------|---------------|
| Layer | Layer 3 mit integriertem WLAN-Controller |
| Uplink-Ports | 4× SFP+ (10G) |
| LWL-Module | 2× SFP+ SR (OM3), 1× SFP+ LR (OS2) |
| Downlink-Ports | 24× PoE++ (802.3bt) für APs |
| WLAN-Features | Zentrale AP-Verwaltung, Roaming, Band-Steering |
| Redundanz | Controller-Redundanz (Active/Standby) |

**Reasoning**: Integrierter WLAN-Controller vereinfacht Management, PoE-Ports für Access Points direkt am Core.

---

## Aufgabe 6: Switches Verteiler B und C (2 Punkte)

### Reasoning

**V-B (Produktion):**
- 80 Arbeitsplätze auf 2 Etagen → ca. 40 Ports/Etage
- Industrie-Umgebung → evtl. robustere Hardware
- Uplink zum V-A und Redundanzlink zu V-C

**V-C (Rechenzentrum):**
- 20 Arbeitsplätze + Server
- Höchste Anforderungen an Bandbreite und Zuverlässigkeit
- Server benötigen 10G-Anbindung
- Möglicherweise ToR-Switches (Top of Rack) für Server-Racks

### Antwort

#### Variante A: Optimal

**V-B (Produktion):**

| Komponente | Spezifikation |
|------------|---------------|
| Switch-Typ | 2× Layer 2/3 Stackable (einer pro Etage) |
| Uplink-Ports | 2× SFP+ pro Switch (LACP zum V-A) |
| Access-Ports | 48× 1G/2.5G PoE+ pro Switch |
| LWL-Module | SFP+ SR (OM4) |
| Features | 802.1X, VLAN, QoS, IGMP Snooping |

**V-C (Rechenzentrum):**

| Komponente | Spezifikation |
|------------|---------------|
| Switch-Typ | 2× Layer 2/3 ToR-Switch (redundant) |
| Uplink-Ports | 4× QSFP+ (2× zum V-A, 2× zu V-B) |
| Server-Ports | 24× SFP+ (10G) oder 10GBASE-T |
| Client-Ports | 24× 1G/2.5G |
| Features | MLAG/VPC, Jumbo Frames, DCB (Data Center Bridging) |
| Besonderheit | Lüfterrichtung front-to-back, Dual PSU |

#### Variante B: Kostenoptimiert

**V-B (Produktion):**

| Komponente | Spezifikation |
|------------|---------------|
| Switch-Typ | 2× Layer 2 Managed Switch |
| Uplink-Ports | 2× SFP+ (10G) |
| Access-Ports | 48× 1GBASE-T |
| LWL-Module | SFP+ SR (OM3) |

**V-C (Rechenzentrum):**

| Komponente | Spezifikation |
|------------|---------------|
| Switch-Typ | 1× Layer 2/3 Switch + 1× Standby |
| Uplink-Ports | 2× SFP+ (10G) |
| Server-Ports | 12× 10GBASE-T |
| Client-Ports | 24× 1GBASE-T |

#### Variante C: WLAN-Hybrid

**V-B (Produktion):**

| Komponente | Spezifikation |
|------------|---------------|
| Switch-Typ | 1× PoE++ Switch pro Etage |
| Uplink-Ports | 2× SFP+ (10G) |
| Access-Ports | 24× PoE++ (für APs + wenige Kabel-Clients) |
| AP-Anbindung | 802.3bt (bis 90W für WiFi 6E APs) |

**V-C (Rechenzentrum):**

| Komponente | Spezifikation |
|------------|---------------|
| Switch-Typ | 1× Layer 3 Switch mit 10G |
| Uplink-Ports | 2× SFP+ (10G) |
| Server-Ports | 12× 10GBASE-T |
| AP-Ports | 4× PoE+ für Rechenzentrums-WLAN |

> [!warning] **Besonderheit Rechenzentrum**
> - Separate Erdung → Alle LWL-Verbindungen nach außen
> - USV-geschützte Stromversorgung
> - Klimatisierung beachten (Switch-Abwärme)
> - Redundante Netzteile zwingend erforderlich

---

## Aufgabe 7: Redundante Backbone-Topologie (2 Punkte)

### Reasoning

**Anforderungen:**
- Kein Single-Point-of-Failure für Gebäude C
- Ausfall einer Leitung → Kommunikation weiterhin möglich
- Maximale Ausfallzeit < 50ms

**Topologie-Optionen:**

1. **Stern**: Alle zu V-A → Kein Ausfall-Schutz für V-A
2. **Ring**: A→B→C→A → Eine Leitung kann ausfallen
3. **Vollvermaschung**: A↔B, A↔C, B↔C → Maximale Redundanz
4. **Stern + Ring**: V-A als Zentrum mit Bypass B↔C

### Antwort

#### Variante A: Optimal – Vollvermaschung (Full Mesh)

![[topologie-fullmesh.png]]
*<span class="fig-id">06-UE-03-topologie-fullmesh</span>: Vollvermaschte Backbone-Topologie mit 40G-Verbindungen*

**Eigenschaften:**
- 3 unabhängige Verbindungen
- Ausfall von 2 Leitungen tolerierbar
- Load-Balancing über alle Pfade möglich (ECMP)
- Höchste Kosten (3× LWL-Trassen)

#### Variante B: Kostenoptimiert – Ring-Topologie

![[topologie-ring.png]]
*<span class="fig-id">06-UE-03-topologie-ring</span>: Ring-Topologie mit 10G-Verbindungen*

**Eigenschaften:**
- Ring: V-A → V-B → V-C → V-A
- Eine Leitung kann ausfallen
- Spanning Tree verhindert Schleifen
- Günstiger als Full Mesh

#### Variante C: WLAN-Hybrid – Stern mit Backup-Ring

![[topologie-wlan.png]]
*<span class="fig-id">06-UE-03-topologie-wlan</span>: WLAN-Hybrid-Topologie mit Stern und Backup-Verbindung*

**Eigenschaften:**
- Primär: Stern zum V-A
- Backup: Ring oder WLAN-Mesh zwischen Gebäuden
- WLAN-Mesh als Not-Backup (geringere Bandbreite)
- Outdoor-APs für Gebäude-zu-Gebäude-Verbindung

> [!tip] **Für Aufgabe 8**
> Die Ring- und Mesh-Topologien erzeugen physikalische Schleifen. Diese müssen durch Spanning Tree oder Link Aggregation aufgelöst werden.

---

## Aufgabe 8: Spanning Tree Protocol (2 Punkte)

### Reasoning

**Warum Loop-Vermeidung nötig?**
- Redundante Topologie = physikalische Schleifen
- Ohne STP: Broadcast-Stürme, MAC-Tabellen-Instabilität
- Mit STP: Logisch schleifenfreie Topologie, Backup-Pfade blockiert

**Vergleich der STP-Varianten:**

| Protokoll | Standard | Konvergenzzeit | Besonderheiten |
|-----------|----------|----------------|----------------|
| STP | 802.1D | 30-50 Sekunden | Veraltet |
| RSTP | 802.1w | 1-3 Sekunden | Schnelle Konvergenz |
| MSTP | 802.1s | 1-3 Sekunden | Multiple Instanzen, VLAN-basiert |

**Anforderung: < 50ms Umschaltzeit**
- Keines der klassischen STP-Protokolle erreicht < 50ms!
- Lösung: **Link Aggregation (LACP)** oder **Routing-Protokolle**

### Antwort

#### Variante A: Optimal – MSTP + Link Aggregation

**Protokoll:** MSTP (802.1s) + LACP (802.3ad)

**Reasoning:**
- MSTP für VLAN-basierte Lastverteilung über redundante Pfade
- LACP für < 50ms Failover bei gebündelten Links
- Bei Linkausfall innerhalb einer LAG: sofortige Umschaltung
- MSTP als Backup für kompletten Pfadausfall

**Konfigurationskonzept:**
```
MST Region: CAMPUS
  Instance 1: VLANs 1-100 (Clients) → Root: V-A
  Instance 2: VLANs 101-200 (Server) → Root: V-C
  
LACP:
  V-A ↔ V-B: 2× 40G gebündelt (Po1)
  V-A ↔ V-C: 2× 40G gebündelt (Po2)
  V-B ↔ V-C: 2× 40G gebündelt (Po3)
```

**Umschaltzeit:**
- Link in LAG fällt aus: < 50ms (LACP Fast)
- Kompletter Pfad fällt aus: 1-3 Sekunden (MSTP)

#### Variante B: Kostenoptimiert – RSTP

**Protokoll:** RSTP (802.1w)

**Reasoning:**
- Einfacher zu konfigurieren als MSTP
- 1-3 Sekunden Konvergenz akzeptabel für Kosten-Lösung
- Keine LAG nötig (nur einzelne 10G-Links)

**Konfigurationskonzept:**
```
RSTP Bridge Priority:
  V-A:   4096 (Root Bridge)
  V-B: 8192
  V-C: 12288

Port Roles:
  V-A → V-B: Designated
  V-A → V-C: Designated
  V-B → V-C: Alternate (Backup)
```

**Umschaltzeit:** 1-3 Sekunden

> [!warning] **Anforderung nicht erfüllt**
> Die geforderten < 50ms werden mit reinem RSTP nicht erreicht. Für kritische Anwendungen im Rechenzentrum sollte LACP ergänzt werden.

#### Variante C: WLAN-Hybrid – RSTP + Roaming

**Protokoll:** RSTP + WiFi Fast Roaming (802.11r)

**Reasoning:**
- Kabelgebundenes Backbone: RSTP ausreichend
- WLAN-Clients: 802.11r Fast BSS Transition (< 50ms Roaming)
- Kritische Geräte: Kabelgebunden mit LACP

**Konfigurationskonzept:**
```
RSTP für Backbone (1-3s Konvergenz)
802.11r für WLAN-Clients (< 50ms Roaming)
LACP nur für Server-Anbindung in V-C
```

**Umschaltzeit:**
- WLAN-Clients: < 50ms (802.11r)
- Kabel-Clients: 1-3 Sekunden (RSTP)
- Server: < 50ms (LACP)

---

## Aufgabe 9: Strukturierte Verkabelung – Ebenen (2 Punkte)

### Reasoning

**Die drei Ebenen nach EN 50173 / ISO 11801:**

1. **Primärverkabelung (Campus Backbone)**
   - Verbindet Gebäude untereinander
   - Typisch: Singlemode oder Multimode LWL
   - Sternförmig vom Standortverteiler

2. **Sekundärverkabelung (Building Backbone)**
   - Verbindet Etagen innerhalb eines Gebäudes
   - Typisch: Multimode LWL oder Kupfer
   - Sternförmig vom Gebäudeverteiler

3. **Tertiärverkabelung (Horizontal Cabling)**
   - Verbindet Etagenverteiler mit Anschlussdosen
   - Typisch: Kupfer (Cat 6/6a/7)
   - Maximale Länge: 90m + 10m Patchkabel

### Antwort

#### Zuordnung für alle Varianten

| Ebene | Komponenten | Medium | Verteiler |
|-------|-------------|--------|-----------|
| **Primär** | V-A ↔ V-B, V-A ↔ V-C, V-B ↔ V-C | LWL (OM3/OM4/OS2) | V-A (Standortverteiler) |
| **Sekundär** | V-B ↔ Etagenverteiler EG/1.OG | LWL oder Cat 6a | V-B, V-C (Gebäudeverteiler) |
| **Tertiär** | Etagenverteiler ↔ Anschlussdosen | Cat 6/6a | Etagenverteiler (Floor Distributor) |

#### Variante A: Optimal

```
Primärverkabelung:
├── V-A (Geb. A) ──40G OM4──► V-B (Geb. B)
├── V-A (Geb. A) ──40G OS2──► V-C (Geb. C)
└── V-B ──────────40G OM4──► V-C (Redundanz)

Sekundärverkabelung (Beispiel Geb. A):
├── V-A ──10G OM3──► EV-A-EG (Etagenverteiler EG)
├── V-A ──10G OM3──► EV-A-1OG
└── V-A ──10G OM3──► EV-A-2OG

Tertiärverkabelung:
└── EV-A-EG ──Cat 6a──► Anschlussdosen (max. 90m)
```

#### Variante C: WLAN-Hybrid

```
Primärverkabelung: (wie Variante B)

Sekundärverkabelung:
├── Zusätzlich: Kabel für Access Points (Cat 6a mit PoE++)
└── AP-Dichte: 1 AP pro 150-200 m² Bürofläche

Tertiärverkabelung:
├── Weniger Dosen pro Arbeitsplatz (WLAN als Primärzugang)
└── Reservedosen für kritische Geräte (Drucker, VoIP)
```

> [!info] **Norm-Referenz**
> - EN 50173-1: Allgemeine Anforderungen
> - EN 50173-2: Bürogebäude
> - EN 50173-3: Industriegebäude
> - ISO/IEC 11801: Internationale Entsprechung

---

## Aufgabe 10: Normen und Standards (2 Punkte)

### Antwort (alle Varianten gleich)

#### Internationale Norm: ISO/IEC 11801

| Aspekt | Details |
|--------|---------|
| **Titel** | Information technology – Generic cabling for customer premises |
| **Anwendung** | Weltweiter Standard für strukturierte Verkabelung |
| **Inhalt** | Kabelkategorien, Topologie, Leistungsklassen, Testverfahren |
| **Aktuelle Version** | ISO/IEC 11801-1:2017 (Edition 3) |
| **Besonderheit** | Definiert Klassen D, E, EA, F, FA für Übertragungsleistung |

#### Europäische Norm: EN 50173

| Aspekt | Details |
|--------|---------|
| **Titel** | Informationstechnik – Anwendungsneutrale Kommunikationskabelanlagen |
| **Anwendung** | Europäische Harmonisierung, in DE als DIN EN 50173 |
| **Inhalt** | Entspricht weitgehend ISO 11801, EU-spezifische Ergänzungen |
| **Teile** | Teil 1: Allgemein, Teil 2: Büro, Teil 3: Industrie, Teil 4: Wohnungen |
| **Besonderheit** | Definiert Primär/Sekundär/Tertiär-Struktur |

#### Amerikanische Norm: TIA-568

| Aspekt | Details |
|--------|---------|
| **Titel** | Commercial Building Telecommunications Cabling Standard |
| **Anwendung** | Nordamerika, oft auch international referenziert |
| **Inhalt** | Verkabelung, Stecker, Pinbelegung, Testmethoden |
| **Aktuelle Version** | TIA-568.2-D (Kupfer), TIA-568.3-D (LWL) |
| **Besonderheit** | Definiert T568A/T568B Pinbelegung für RJ45 |

#### Weitere relevante Normen

| Norm | Anwendungsbereich |
|------|-------------------|
| **EN 50174** | Installation von Kommunikationsverkabelung |
| **EN 50346** | Prüfung installierter Verkabelung |
| **IEEE 802.3** | Ethernet-Standards (physikalische Spezifikationen) |
| **IEC 60793** | Optische Fasern (LWL-Spezifikationen) |

---

## Zusammenfassung der Varianten

### Kostenvergleich (grobe Schätzung)

| Komponente | Variante A (Optimal) | Variante B (Kosten) | Variante C (WLAN) |
|------------|---------------------|---------------------|-------------------|
| LWL-Verkabelung | €€€€ (OM4 + OS2, Mesh) | €€ (OM3, Ring) | €€ (OM3, Stern) |
| Kupfer-Verkabelung | €€€ (Cat 6a überall) | €€ (Cat 6 + 6a) | € (weniger Dosen) |
| Core-Switch | €€€€ (Chassis, 40G) | €€ (Stackable, 10G) | €€€ (mit WLAN-Ctrl) |
| Distribution-Switches | €€€ (10G ToR) | €€ (Managed L2) | €€ (PoE++) |
| WLAN-Infrastruktur | - | - | €€€ (APs, Lizenzen) |
| **Gesamt relativ** | **150-200%** | **100%** (Basis) | **120-140%** |

### Empfehlung nach Anwendungsfall

| Szenario | Empfohlene Variante |
|----------|---------------------|
| Neubau mit hohem Budget, lange Nutzungsdauer | **A (Optimal)** |
| Bestehendes Budget, pragmatischer Ansatz | **B (Kostenoptimiert)** |
| Flexible Arbeitsplätze, BYOD-Kultur | **C (WLAN-Hybrid)** |
| Industrieumgebung mit EMV-Problemen | **A oder B** (kein WLAN) |
| Schnelle Umsetzung gefordert | **C** (weniger Kabel) |

---

## Weiterführende Themen

- [[../../03-Rechnernetze/03-Referenzmodelle/04-Physikalische-Schicht/01-Uebertragungsmedien|Übertragungsmedien]]
- [[../../03-Rechnernetze/03-Referenzmodelle/04-Physikalische-Schicht/02-Signale|Signale]]
- [[../../03-Rechnernetze/04-Basisprotokolle/05-Spanning-Tree|Spanning Tree Protocol]]
- [[../../03-Rechnernetze/03-Referenzmodelle/05-Sicherungsschicht/00-Sicherungsschicht-Index|Sicherungsschicht]]
- [[./UE-RN-03-Campus-Verkabelung|Zurück zur Aufgabe]]
