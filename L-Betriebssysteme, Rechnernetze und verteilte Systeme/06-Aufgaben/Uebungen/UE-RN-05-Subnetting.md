---
author: Andreas Hümmer
title: Übung - IP-Adressierung und Subnetting
tags:
  - uebung
  - rn
  - ip
  - subnetting
  - cidr
  - netzwerk
created: '2026-10-24'
modified: '2026-10-24'
bereich: RN
---

# Übung: IP-Adressierung und Subnetting

## Ausgangssituation

Ein mittelständisches Unternehmen plant die IP-Adressierung für sein neues Netzwerk. Die IT-Abteilung hat folgende Gerätezahlen ermittelt:

| Gerätegruppe | Aktuelle Anzahl | Mit Reserve (+20%) |
|--------------|-----------------|-------------------|
| **Server** | 46 | ? |
| **Clients** | 132 | ? |
| **IoT-Devices** | 399 | ? |

---

## Anforderungen

### Allgemeine Vorgaben

1. **Adressbereich**: Verwenden Sie einen RFC 1918 Private Address Range
2. **Reserve**: Jedes Subnetz muss die aktuelle Gerätezahl **plus 20% Reserve** aufnehmen können
3. **Supernetting**: Die drei Subnetze sollen zu einem gemeinsamen **Supernet** zusammengefasst werden können
4. **Gateway**: Die **erste nutzbare IP-Adresse** jedes Subnetzes ist für den Router/Firewall reserviert

### RFC 1918 Private Address Ranges

| Klasse | Bereich | CIDR | Anzahl Adressen |
|--------|---------|------|-----------------|
| A | 10.0.0.0 – 10.255.255.255 | 10.0.0.0/8 | 16.777.216 |
| B | 172.16.0.0 – 172.31.255.255 | 172.16.0.0/12 | 1.048.576 |
| C | 192.168.0.0 – 192.168.255.255 | 192.168.0.0/16 | 65.536 |

---

## Aufgaben

### Aufgabe 1: Bedarfsberechnung (4 Punkte)

Berechnen Sie für jede Gerätegruppe:

**a)** Die benötigte Anzahl an IP-Adressen inklusive 20% Reserve (aufrunden!)

**b)** Die minimale Subnetzgröße (nächste Zweierpotenz), die diesen Bedarf abdeckt

**c)** Die entsprechende CIDR-Präfixlänge

> [!tip] Hinweis
> Denken Sie daran: In jedem Subnetz sind **Netzwerk-Adresse** und **Broadcast-Adresse** nicht für Hosts nutzbar!
> 
> Nutzbare Adressen = 2^(32-Präfix) - 2

**Tabelle zum Ausfüllen:**

| Gerätegruppe | Geräte | +20% Reserve | + Gateway | Benötigt gesamt | Subnetzgröße (2^n) | Präfix |
|--------------|--------|--------------|-----------|-----------------|-------------------|--------|
| Server | 46 | ? | +1 | ? | ? | /? |
| Clients | 132 | ? | +1 | ? | ? | /? |
| IoT-Devices | 399 | ? | +1 | ? | ? | /? |

---

### Aufgabe 2: Subnetz-Design (6 Punkte)

Entwerfen Sie drei Subnetze aus dem Bereich **10.100.0.0**, die zu einem Supernet zusammengefasst werden können.

**Anforderungen:**
- Die Subnetze müssen **zusammenhängend** sein (für Supernetting)
- Beginnen Sie mit dem **größten** Subnetz
- Ordnen Sie die Subnetze **lückenlos** hintereinander an

**Für jedes Subnetz angeben:**

| Eigenschaft | Server-Netz | Client-Netz | IoT-Netz |
|-------------|-------------|-------------|----------|
| **Netzwerk-Adresse** | | | |
| **CIDR-Notation** | | | |
| **Subnetzmaske** | | | |
| **Gateway (1. Host)** | | | |
| **Letzter Host** | | | |
| **Broadcast-Adresse** | | | |
| **Nutzbare Adressen** | | | |
| **Belegte Adressen** | | | |
| **Freie Adressen** | | | |

---

### Aufgabe 3: Supernet berechnen (4 Punkte)

**a)** Geben Sie das Supernet an, das alle drei Subnetze zusammenfasst. (2 Punkte)

| Eigenschaft | Wert |
|-------------|------|
| **Supernet (CIDR)** | |
| **Subnetzmaske** | |
| **Adressbereich** | von ________ bis ________ |
| **Gesamtadressen** | |

**b)** Erklären Sie, warum die gewählte Anordnung der Subnetze ein Supernetting ermöglicht. (2 Punkte)

_Dein Antwort:_

<br><br><br>

---

### Aufgabe 4: Verständnisfragen (6 Punkte)

**a)** Warum ist es wichtig, mit dem größten Subnetz zu beginnen und die Netze zusammenhängend anzuordnen? (2 Punkte)

_Dein Antwort:_

<br><br><br>

**b)** Ein Kollege schlägt vor, die Subnetze 10.100.0.0/23, 10.100.4.0/24 und 10.100.8.0/23 zu verwenden. Warum ist das für Supernetting problematisch? (2 Punkte)

_Dein Antwort:_

<br><br><br>

**c)** Wie viele IP-Adressen "verschwendet" Ihr Design im Vergleich zum theoretischen Minimum? Berechnen Sie die Effizienz. (2 Punkte)

```
Theoretisches Minimum: Geräte + Gateways = _____ Adressen
Tatsächlich allokiert: _____ Adressen
Effizienz: _____ %
```

---

## Hilfstabelle: CIDR-Präfixe

| Präfix | Subnetzmaske | Adressen | Nutzbar |
|--------|--------------|----------|---------|
| /20 | 255.255.240.0 | 4096 | 4094 |
| /21 | 255.255.248.0 | 2048 | 2046 |
| /22 | 255.255.252.0 | 1024 | 1022 |
| /23 | 255.255.254.0 | 512 | 510 |
| /24 | 255.255.255.0 | 256 | 254 |
| /25 | 255.255.255.128 | 128 | 126 |
| /26 | 255.255.255.192 | 64 | 62 |
| /27 | 255.255.255.224 | 32 | 30 |
| /28 | 255.255.255.240 | 16 | 14 |

---

## Bewertung

| Aufgabe | Thema | Punkte |
|---------|-------|--------|
| 1 | Bedarfsberechnung | 4 |
| 2 | Subnetz-Design | 6 |
| 3 | Supernet berechnen | 4 |
| 4 | Verständnisfragen | 6 |
| **Gesamt** | | **20** |

---

## Musterlösung

> [!tip] **Für Dozenten**
> Die ausführliche Musterlösung finden Sie hier:
> 
> [[../Loesungen/LOE-UE-RN-05-Subnetting|→ Musterlösung Subnetting]]

---

## Weiterführende Themen

- [[../../03-Rechnernetze/04-Basisprotokolle/01-IP|IP-Protokoll]] – IP-Adressierung
- [[../../03-Rechnernetze/03-Referenzmodelle/06-Vermittlungsschicht/02-Subnetting|Subnetting]] – CIDR und VLSM
- [[../../03-Rechnernetze/05-Sicherheit/01-Firewalls|Firewalls]] – Netzwerksegmentierung
