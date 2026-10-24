---
author: Andreas Hümmer
title: Lösung - IP-Adressierung und Subnetting
tags:
  - loesung
  - rn
  - ip
  - subnetting
  - cidr
  - netzwerk
created: '2026-10-24'
modified: '2026-10-24'
bereich: RN
---

# Lösung: IP-Adressierung und Subnetting

> [!info] Zugehörige Übung
> [[../Uebungen/UE-RN-05-Subnetting|→ Übung IP-Adressierung und Subnetting]]

---

## Aufgabe 1: Bedarfsberechnung (4 Punkte)

### Berechnung der Reserve (+20%)

| Gerätegruppe | Geräte | × 1,2 | Aufgerundet |
|--------------|--------|-------|-------------|
| Server | 46 | 55,2 | **56** |
| Clients | 132 | 158,4 | **159** |
| IoT-Devices | 399 | 478,8 | **479** |

### Berechnung der Subnetzgröße

Benötigte Adressen = Geräte + Gateway + Netzwerk-Adresse + Broadcast

| Gerätegruppe | Geräte (mit Reserve) | + Gateway | Benötigt nutzbar | + Netz/Broadcast | Nächste 2^n | Präfix |
|--------------|---------------------|-----------|------------------|------------------|-------------|--------|
| **Server** | 56 | +1 | 57 | +2 = 59 | **64** (2^6) | **/26** |
| **Clients** | 159 | +1 | 160 | +2 = 162 | **256** (2^8) | **/24** |
| **IoT-Devices** | 479 | +1 | 480 | +2 = 482 | **512** (2^9) | **/23** |

### Musterlösung Tabelle

| Gerätegruppe | Geräte | +20% Reserve | + Gateway | Benötigt gesamt | Subnetzgröße (2^n) | Präfix |
|--------------|--------|--------------|-----------|-----------------|-------------------|--------|
| Server | 46 | 56 | +1 | 59 | 64 | **/26** |
| Clients | 132 | 159 | +1 | 162 | 256 | **/24** |
| IoT-Devices | 399 | 479 | +1 | 482 | 512 | **/23** |

---

## Aufgabe 2: Subnetz-Design (6 Punkte)

### Strategie: Größtes Subnetz zuerst

Um Supernetting zu ermöglichen, müssen die Netze:
1. **Zusammenhängend** sein (keine Lücken)
2. An einer **durch die Subnetzgröße teilbaren Adresse** beginnen
3. **Größte zuerst** angeordnet werden

### Reihenfolge nach Größe

1. **IoT-Netz**: /23 = 512 Adressen (größtes)
2. **Client-Netz**: /24 = 256 Adressen
3. **Server-Netz**: /26 = 64 Adressen (kleinstes)

### Berechnung der Subnetze

Startadresse: **10.100.0.0**

#### IoT-Netz (/23 = 512 Adressen)

```
Netzwerk:    10.100.0.0/23
Bereich:     10.100.0.0 – 10.100.1.255
Nächstes:    10.100.2.0
```

#### Client-Netz (/24 = 256 Adressen)

```
Netzwerk:    10.100.2.0/24
Bereich:     10.100.2.0 – 10.100.2.255
Nächstes:    10.100.3.0
```

#### Server-Netz (/26 = 64 Adressen)

```
Netzwerk:    10.100.3.0/26
Bereich:     10.100.3.0 – 10.100.3.63
Nächstes:    10.100.3.64
```

### Musterlösung Tabelle

| Eigenschaft | IoT-Netz | Client-Netz | Server-Netz |
|-------------|----------|-------------|-------------|
| **Netzwerk-Adresse** | 10.100.0.0 | 10.100.2.0 | 10.100.3.0 |
| **CIDR-Notation** | 10.100.0.0/23 | 10.100.2.0/24 | 10.100.3.0/26 |
| **Subnetzmaske** | 255.255.254.0 | 255.255.255.0 | 255.255.255.192 |
| **Gateway (1. Host)** | 10.100.0.1 | 10.100.2.1 | 10.100.3.1 |
| **Letzter Host** | 10.100.1.254 | 10.100.2.254 | 10.100.3.62 |
| **Broadcast-Adresse** | 10.100.1.255 | 10.100.2.255 | 10.100.3.63 |
| **Nutzbare Adressen** | 510 | 254 | 62 |
| **Belegte Adressen** | 479 + 1 = 480 | 159 + 1 = 160 | 56 + 1 = 57 |
| **Freie Adressen** | 30 | 94 | 5 |

### Visuelle Darstellung

```
10.100.0.0                                                    10.100.3.63
    |←─────────── IoT /23 ───────────→|←── Clients /24 ──→|←─ Server /26 ─→|
    |                                  |                   |                |
10.100.0.0                      10.100.2.0           10.100.3.0      10.100.3.63
    ├──────────────────────────────────┼───────────────────┼────────────────┤
    │        512 Adressen              │   256 Adressen    │  64 Adressen   │
    │      (10.100.0.0-1.255)          │ (10.100.2.0-2.255)│(10.100.3.0-.63)│
    └──────────────────────────────────┴───────────────────┴────────────────┘
```

---

## Aufgabe 3: Supernet berechnen (4 Punkte)

### a) Supernet-Berechnung

Die drei Subnetze belegen:
- IoT: 10.100.0.0 – 10.100.1.255 (512)
- Clients: 10.100.2.0 – 10.100.2.255 (256)
- Server: 10.100.3.0 – 10.100.3.63 (64)

**Gesamtbereich**: 10.100.0.0 – 10.100.3.63 = 832 Adressen

Das kleinste Supernet, das diesen Bereich abdeckt:

```
10.100.0.0/22 = 1024 Adressen (10.100.0.0 – 10.100.3.255)
```

| Eigenschaft | Wert |
|-------------|------|
| **Supernet (CIDR)** | **10.100.0.0/22** |
| **Subnetzmaske** | **255.255.252.0** |
| **Adressbereich** | von **10.100.0.0** bis **10.100.3.255** |
| **Gesamtadressen** | **1024** |

### b) Warum funktioniert das Supernetting?

Das Supernetting funktioniert, weil:

1. **Ausrichtung**: 10.100.0.0 ist durch 1024 (2^10) teilbar, also eine gültige /22-Netzwerkadresse
2. **Zusammenhängend**: Alle drei Subnetze liegen lückenlos hintereinander
3. **Binäre Grenzen**: Die Subnetzgrenzen fallen auf Zweierpotenzen
   ```
   10.100.0.0   = 00001010.01100100.00000000.00000000
   10.100.3.255 = 00001010.01100100.00000011.11111111
                                    ^^^^^^^^
                                    Die ersten 22 Bits sind identisch!
   ```

---

## Aufgabe 4: Verständnisfragen (6 Punkte)

### a) Warum mit dem größten Subnetz beginnen? (2 Punkte)

**Antwort:**

Größere Subnetze haben **strengere Alignment-Anforderungen**. Ein /23-Netz muss an einer durch 512 teilbaren Adresse beginnen, ein /26-Netz nur an einer durch 64 teilbaren.

Wenn man mit dem kleinsten Netz beginnt und es an einer "ungeraden" Position platziert, kann das größere Netz möglicherweise nicht mehr korrekt ausgerichtet werden.

**Beispiel des Fehlers:**
```
Falsch (klein zuerst):
10.100.0.0/26  (Server)     → endet bei 10.100.0.63
10.100.0.64/24 (Clients)    → FEHLER! /24 muss bei .0 oder .0 beginnen
```

### b) Warum ist 10.100.0.0/23, 10.100.4.0/24, 10.100.8.0/23 problematisch? (2 Punkte)

**Antwort:**

Diese Netze haben **Lücken** dazwischen:

```
10.100.0.0/23  → 10.100.0.0 – 10.100.1.255
[LÜCKE]        → 10.100.2.0 – 10.100.3.255 (ungenutzt)
10.100.4.0/24  → 10.100.4.0 – 10.100.4.255
[LÜCKE]        → 10.100.5.0 – 10.100.7.255 (ungenutzt)
10.100.8.0/23  → 10.100.8.0 – 10.100.9.255
```

Das kleinste Supernet müsste **/20** sein (10.100.0.0/20), um alle abzudecken – das sind 4096 Adressen statt der benötigten ~830. Die Lücken verschwenden Adressraum und erschweren das Routing.

### c) Effizienzberechnung (2 Punkte)

**Berechnung:**

```
Theoretisches Minimum:
  Server:  56 Geräte + 1 Gateway = 57
  Clients: 159 Geräte + 1 Gateway = 160  
  IoT:     479 Geräte + 1 Gateway = 480
  ─────────────────────────────────────
  Summe:                           697 Adressen

Tatsächlich allokiert (nutzbare Adressen):
  Server:  62 (von /26)
  Clients: 254 (von /24)
  IoT:     510 (von /23)
  ─────────────────────────────────────
  Summe:                           826 Adressen

Effizienz: 697 / 826 = 84,4%
```

Oder bezogen auf das Supernet:

```
Supernet /22: 1024 Adressen
Davon nutzbar: 1022 (minus Netz + Broadcast)
Tatsächlich genutzt: 697 Geräte + 3 Gateways = 700

Effizienz: 700 / 1022 = 68,5%
```

> [!info] Bewertung
> Eine Effizienz von 68-84% ist für Subnetting sehr gut. Perfekte Effizienz ist wegen der Zweierpotenz-Beschränkung praktisch unmöglich.

---

## Zusammenfassung

### Finale Netzwerkkonfiguration

```
Supernet: 10.100.0.0/22 (255.255.252.0)
├── IoT-Netz:     10.100.0.0/23   (510 Hosts, Gateway: 10.100.0.1)
├── Client-Netz:  10.100.2.0/24   (254 Hosts, Gateway: 10.100.2.1)
└── Server-Netz:  10.100.3.0/26   (62 Hosts,  Gateway: 10.100.3.1)
    └── [Frei:    10.100.3.64/26] (Reserve für Zukunft)
```

### Routing-Tabelle (Beispiel für Core-Router)

| Zielnetz | Gateway | Interface | Beschreibung |
|----------|---------|-----------|--------------|
| 10.100.0.0/22 | - | eth0 | Supernet (Summary) |
| 10.100.0.0/23 | 10.100.0.1 | vlan10 | IoT-Netz |
| 10.100.2.0/24 | 10.100.2.1 | vlan20 | Client-Netz |
| 10.100.3.0/26 | 10.100.3.1 | vlan30 | Server-Netz |

---

## Weiterführende Themen

- [[../../03-Rechnernetze/04-Basisprotokolle/01-IP|IP-Protokoll]] – IP-Adressierung
- [[../../03-Rechnernetze/03-Referenzmodelle/06-Vermittlungsschicht/02-Subnetting|Subnetting]] – CIDR und VLSM
- [[../../03-Rechnernetze/05-Sicherheit/01-Firewalls|Firewalls]] – Netzwerksegmentierung
