---
author: Andreas Hümmer
title: 'Übung: Rechnernetze (Klausurformat)'
tags:
  - uebung
  - rn
  - klausur
  - osi
  - tcp-ip
  - ip
  - subnetting
  - tcp
  - udp
  - arp
  - dhcp
  - dns
  - http
punkte_gesamt: 120
bearbeitungszeit: 180
bereich: RN
created: '2026-11-01'
modified: '2026-11-01'
---

# Übung: Rechnernetze (Klausurformat)

**Bereich:** RN – Alle Kapitel
**Gesamtpunktzahl:** 120 Punkte
**Bearbeitungszeit:** ca. 180 Minuten

---

> [!info] **Themenübersicht**
> Diese Übung deckt die zentralen Themen des Moduls Rechnernetze ab:
> - Teil 1: Grundlagen (15 Punkte)
> - Teil 2: Standards und Gremien (10 Punkte)
> - Teil 3: Referenzmodelle (20 Punkte)
> - Teil 4: Netzwerkschicht / IP (20 Punkte)
> - Teil 5: Transportschicht (20 Punkte)
> - Teil 6: Basisprotokolle (20 Punkte)
> - Teil 7: Anwendungsschicht (15 Punkte)

---

## Teil 1: Grundlagen (15 Punkte)

### Aufgabe 1.1: Fundamentale Aspekte der Kommunikation (5 Punkte) ⭐

a) **Nennen Sie die fünf fundamentalen Aspekte, die jede Form der Kommunikation (von Rauchzeichen bis Glasfaser) adressieren muss.** (5 Punkte)

| Nr. | Aspekt | Kurzbeschreibung | Moderne Entsprechung |
|-----|--------|------------------|----------------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

---

### Aufgabe 1.2: Netzwerktypen (5 Punkte) ⭐

**Ordnen Sie die folgenden Netzwerktypen nach aufsteigender Reichweite und nennen Sie jeweils eine typische Technologie sowie einen typischen Bandbreitenbereich.**

| Netzwerktyp | Ausgeschrieben | Reichweite | Typische Technologie | Bandbreite |
|-------------|----------------|------------|---------------------|------------|
| PAN | | | | |
| LAN | | | | |
| MAN | | | | |
| WAN | | | | |

---

### Aufgabe 1.3: Topologien (5 Punkte) ⭐⭐

a) **Zeichnen Sie eine Stern-Topologie mit einem zentralen Switch und 4 Endgeräten.** (2 Punkte)

<br><br><br><br><br>

b) **Nennen Sie für jede Topologie zwei Vorteile und zwei Nachteile.** (3 Punkte)

| Topologie | Vorteile | Nachteile |
|-----------|----------|-----------|
| Bus | 1. <br> 2. | 1. <br> 2. |
| Stern | 1. <br> 2. | 1. <br> 2. |
| Mesh (vollvermascht) | 1. <br> 2. | 1. <br> 2. |

---

## Teil 2: Standards und Gremien (10 Punkte)

### Aufgabe 2.1: Standardisierungsgremien (5 Punkte) ⭐

**Ordnen Sie den Standardisierungsgremien ihre Zuständigkeitsbereiche und je ein Beispiel für einen Standard zu.**

| Gremium | Zuständigkeitsbereich | Beispiel-Standard |
|---------|----------------------|-------------------|
| IEEE | | |
| IETF | | |
| ISO | | |
| ITU | | |

---

### Aufgabe 2.2: De-facto vs. De-jure Standards (5 Punkte) ⭐⭐

a) **Erklären Sie den Unterschied zwischen De-facto- und De-jure-Standards.** (3 Punkte)

| Standardtyp | Definition | Entstehungsweg |
|-------------|------------|----------------|
| De-jure | | |
| De-facto | | |

b) **Nennen Sie je zwei Beispiele für De-facto- und De-jure-Standards.** (2 Punkte)

_De-facto:_

<br><br>

_De-jure:_

<br><br>

---

## Teil 3: Referenzmodelle (20 Punkte)

### Aufgabe 3.1: OSI-Modell (8 Punkte) ⭐

**Nennen Sie alle 7 OSI-Schichten in der richtigen Reihenfolge (von unten nach oben) und geben Sie für jede Schicht die Aufgabe, die Dateneinheit (PDU) und ein Beispielprotokoll oder -gerät an.**

| Nr. | Schicht (deutsch) | Schicht (englisch) | Aufgabe | PDU | Beispiel |
|-----|-------------------|-------------------|---------|-----|----------|
| 7 | | | | | |
| 6 | | | | | |
| 5 | | | | | |
| 4 | | | | | |
| 3 | | | | | |
| 2 | | | | | |
| 1 | | | | | |

---

### Aufgabe 3.2: TCP/IP-Modell (6 Punkte) ⭐⭐

a) **Nennen Sie die 4 Schichten des TCP/IP-Modells und ordnen Sie sie den entsprechenden OSI-Schichten zu.** (4 Punkte)

| TCP/IP-Schicht | Entsprechende OSI-Schicht(en) |
|----------------|-------------------------------|
| | |
| | |
| | |
| | |

b) **Ordnen Sie die folgenden Protokolle der richtigen TCP/IP-Schicht zu:** HTTP, TCP, IP, Ethernet, UDP, DNS, ARP (2 Punkte)

| Anwendungsschicht | Transportschicht | Internetschicht | Netzzugangsschicht |
|-------------------|-----------------|-----------------|-------------------|
| | | | |

---

### Aufgabe 3.3: Datenkapselung und Paketfluss (6 Punkte) ⭐⭐

a) **Beschreiben Sie den Prozess der Datenkapselung (Encapsulation) beim Durchlaufen der TCP/IP-Schichten.** (3 Punkte)

_Dein Antwort:_

<br><br><br>

b) **Ein Paket durchläuft einen Router auf dem Weg vom Sender zum Empfänger. Welche Schichten verarbeitet der Router und was ändert sich dabei an dem Paket?** (3 Punkte)

_Dein Antwort:_

<br><br><br>

---

## Teil 4: Netzwerkschicht / IP (20 Punkte)

### Aufgabe 4.1: IPv4-Adressierung (6 Punkte) ⭐

a) **Erklären Sie den Unterschied zwischen dem Netzwerkanteil und dem Hostanteil einer IP-Adresse.** (2 Punkte)

_Dein Antwort:_

<br><br><br>

b) **Nennen Sie die drei privaten IPv4-Adressbereiche nach RFC 1918.** (2 Punkte)

| Bereich | CIDR-Notation | Anzahl Adressen |
|---------|---------------|-----------------|
| Klasse A | | |
| Klasse B | | |
| Klasse C | | |

c) **Warum sind private IP-Adressen nicht im Internet routbar?** (2 Punkte)

_Dein Antwort:_

<br><br><br>

---

### Aufgabe 4.2: Subnetting (8 Punkte) ⭐⭐⭐

**Gegeben ist das Netzwerk 192.168.10.0/24. Dieses soll in 4 gleich große Subnetze aufgeteilt werden.**

a) **Welche Subnetzmaske wird für die 4 Subnetze benötigt? Geben Sie die Maske in CIDR- und Dezimalschreibweise an.** (2 Punkte)

_Dein Antwort:_

<br><br>

b) **Füllen Sie die folgende Tabelle für alle 4 Subnetze aus.** (6 Punkte)

| Subnetz | Netzwerkadresse | Erste Host-IP | Letzte Host-IP | Broadcast-Adresse | Anzahl Hosts |
|---------|-----------------|---------------|----------------|-------------------|--------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |

---

### Aufgabe 4.3: ICMP und Diagnose (6 Punkte) ⭐⭐

a) **Welche ICMP-Nachrichtentypen werden bei einem Ping verwendet?** (2 Punkte)

| Richtung | ICMP-Typ | Typ-Nummer |
|----------|----------|------------|
| Anfrage | | |
| Antwort | | |

b) **Erklären Sie, wie Traceroute den Pfad durch das Netzwerk ermittelt. Welche Rolle spielt dabei der TTL-Wert?** (3 Punkte)

_Dein Antwort:_

<br><br><br>

c) **Was passiert, wenn der TTL-Wert eines Pakets auf 0 fällt?** (1 Punkt)

_Dein Antwort:_

<br><br>

---

## Teil 5: Transportschicht (20 Punkte)

### Aufgabe 5.1: TCP vs. UDP Vergleich (8 Punkte) ⭐⭐

**Vergleichen Sie TCP und UDP anhand der folgenden Kriterien.**

| Kriterium | TCP | UDP |
|-----------|-----|-----|
| Verbindungsaufbau | | |
| Zuverlässigkeit | | |
| Reihenfolgegarantie | | |
| Flusskontrolle | | |
| Header-Größe | | |
| Typische Anwendung (2 Beispiele) | | |

---

### Aufgabe 5.2: TCP 3-Way-Handshake (6 Punkte) ⭐⭐

a) **Beschreiben Sie die drei Schritte des TCP-Verbindungsaufbaus (3-Way-Handshake). Nennen Sie für jeden Schritt die gesetzten Flags.** (3 Punkte)

| Schritt | Richtung | Gesetzte Flags | Beschreibung |
|---------|----------|----------------|--------------|
| 1 | Client → Server | | |
| 2 | Server → Client | | |
| 3 | Client → Server | | |

b) **Berechnung der Sequenznummern:** Der Client sendet ein SYN mit Sequenznummer 1000. Der Server antwortet mit einem SYN-ACK mit Sequenznummer 5000. Welche Werte haben die ACK-Felder in den jeweiligen Paketen? (3 Punkte)

| Paket | Sequenznummer | ACK-Nummer |
|-------|---------------|------------|
| SYN (Client → Server) | 1000 | – |
| SYN-ACK (Server → Client) | 5000 | |
| ACK (Client → Server) | | |

---

### Aufgabe 5.3: Flusskontrolle und Sliding Window (6 Punkte) ⭐⭐⭐

a) **Erklären Sie das Sliding-Window-Verfahren bei TCP.** (3 Punkte)

_Dein Antwort:_

<br><br><br>

b) **Was ist der Unterschied zwischen Flusskontrolle und Staukontrolle?** (2 Punkte)

| Mechanismus | Schützt vor | Ziel |
|-------------|-------------|------|
| Flusskontrolle | | |
| Staukontrolle | | |

c) **Was passiert, wenn der Empfänger ein Window von 0 ankündigt?** (1 Punkt)

_Dein Antwort:_

<br><br>

---

## Teil 6: Basisprotokolle (20 Punkte)

### Aufgabe 6.1: ARP (6 Punkte) ⭐⭐

a) **Erklären Sie den Zweck von ARP. Warum wird es als "Brücke zwischen Layer 2 und Layer 3" bezeichnet?** (2 Punkte)

_Dein Antwort:_

<br><br><br>

b) **Warum wird der ARP-Request als Broadcast und der ARP-Reply als Unicast gesendet?** (2 Punkte)

| Nachrichtentyp | Übertragungsart | Begründung |
|----------------|-----------------|------------|
| ARP Request | Broadcast | |
| ARP Reply | Unicast | |

c) **Was ist ARP-Spoofing und wie kann man sich dagegen schützen?** (2 Punkte)

_ARP-Spoofing:_

<br><br>

_Schutzmaßnahme:_

<br><br>

---

### Aufgabe 6.2: DHCP (8 Punkte) ⭐⭐

a) **Beschreiben Sie die vier Schritte des DORA-Prozesses.** (4 Punkte)

| Schritt | Name | Richtung | Übertragungsart | Beschreibung |
|---------|------|----------|-----------------|--------------|
| D | | | | |
| O | | | | |
| R | | | | |
| A | | | | |

b) **Warum wird DHCPREQUEST als Broadcast gesendet, obwohl der Client bereits weiß, welchen Server er wählt?** (2 Punkte)

_Dein Antwort:_

<br><br><br>

c) **Erklären Sie die Bedeutung von T1 (50%) und T2 (87,5%) bei der DHCP-Lease-Erneuerung.** (2 Punkte)

| Zeitpunkt | Prozent der Lease | Verhalten des Clients |
|-----------|-------------------|----------------------|
| T1 | 50% | |
| T2 | 87,5% | |

---

### Aufgabe 6.3: DNS (6 Punkte) ⭐⭐

a) **Beschreiben Sie die DNS-Hierarchie. Nennen Sie die Ebenen von der Wurzel bis zum Host.** (2 Punkte)

| Ebene | Name | Beispiel |
|-------|------|----------|
| 0 | | |
| 1 | | |
| 2 | | |
| 3+ | | |

b) **Füllen Sie die folgende Tabelle mit den wichtigsten DNS-Record-Typen aus.** (2 Punkte)

| Record-Typ | Zweck | Beispiel |
|------------|-------|----------|
| A | | |
| AAAA | | |
| MX | | |
| CNAME | | |
| NS | | |
| PTR | | |

c) **Was ist der Unterschied zwischen rekursiver und iterativer DNS-Auflösung?** (2 Punkte)

| Auflösungsart | Client-Perspektive | Server-Verhalten |
|---------------|-------------------|------------------|
| Rekursiv | | |
| Iterativ | | |

---

## Teil 7: Anwendungsschicht (15 Punkte)

### Aufgabe 7.1: HTTP-Grundlagen (7 Punkte) ⭐⭐

a) **Nennen Sie die vier wichtigsten HTTP-Methoden und deren typische Verwendung.** (2 Punkte)

| Methode | Verwendung |
|---------|-----------|
| GET | |
| POST | |
| PUT | |
| DELETE | |

b) **Erklären Sie den Aufbau einer HTTP-Anfrage (Request).** (2 Punkte)

_Dein Antwort:_

<br><br><br>

c) **Ordnen Sie die HTTP-Statuscodes den Kategorien und Bedeutungen zu.** (3 Punkte)

| Statuscode | Kategorie | Bedeutung |
|------------|-----------|-----------|
| 200 | | |
| 301 | | |
| 404 | | |
| 500 | | |
| 401 | | |
| 503 | | |

---

### Aufgabe 7.2: HTTP vs. HTTPS (4 Punkte) ⭐

a) **Was ist der Unterschied zwischen HTTP und HTTPS?** (2 Punkte)

_Dein Antwort:_

<br><br><br>

b) **Welche Schicht fügt HTTPS im Protokollstapel hinzu und welchen Zweck erfüllt sie?** (2 Punkte)

| Aspekt | Antwort |
|--------|---------|
| Hinzugefügte Schicht | |
| Zweck | |

---

### Aufgabe 7.3: Cookies und Session-Management (4 Punkte) ⭐⭐

a) **Warum sind Cookies notwendig, obwohl HTTP zustandslos ist?** (2 Punkte)

_Dein Antwort:_

<br><br><br>

b) **Nennen Sie drei wichtige Sicherheitsattribute für Cookies und erklären Sie deren Funktion.** (2 Punkte)

| Attribut | Funktion |
|----------|----------|
| HttpOnly | |
| Secure | |
| SameSite | |

---

## Selbsteinschätzung

Nach Bearbeitung der Aufgaben:

| Thema | Sicher | Unsicher | Muss wiederholen |
|-------|:------:|:--------:|:----------------:|
| Grundlagen/Netzwerktypen | ☐ | ☐ | ☐ |
| Standards/Gremien | ☐ | ☐ | ☐ |
| OSI-Modell | ☐ | ☐ | ☐ |
| TCP/IP-Modell | ☐ | ☐ | ☐ |
| IPv4-Adressierung | ☐ | ☐ | ☐ |
| Subnetting | ☐ | ☐ | ☐ |
| ICMP/Ping/Traceroute | ☐ | ☐ | ☐ |
| TCP vs. UDP | ☐ | ☐ | ☐ |
| 3-Way-Handshake | ☐ | ☐ | ☐ |
| Flusskontrolle | ☐ | ☐ | ☐ |
| ARP | ☐ | ☐ | ☐ |
| DHCP | ☐ | ☐ | ☐ |
| DNS | ☐ | ☐ | ☐ |
| HTTP/HTTPS | ☐ | ☐ | ☐ |

---

## Quellen

### Grundlagen
- [[01-Historie|Historie der Rechnernetze]]
- [[02-Netzwerktypen|Netzwerktypen]]
- [[03-Topologien|Netzwerktopologien]]

### Standards und Gremien
- [[01-Uebersicht|Standardisierung – Übersicht]]
- [[02-IEEE-Standards|IEEE-Standards]]
- [[03-RFCs|RFCs]]

### Referenzmodelle
- [[01-OSI-Modell|OSI-Referenzmodell]]
- [[02-TCP-IP-Modell|TCP/IP-Modell]]
- [[03-Schichtenvergleich|Schichtenvergleich]]
- [[04-Arbeitsweise-Schichtenmodell|Arbeitsweise des Schichtenmodells]]

### Netzwerkschicht
- [[01-IP-Protokoll|IP-Protokoll (IPv4)]]
- [[05-ICMP|ICMP]]

### Transportschicht
- [[01-TCP|TCP – Transmission Control Protocol]]
- [[02-UDP|UDP – User Datagram Protocol]]
- [[03-Ports|Ports]]

### Basisprotokolle
- [[01-ARP|ARP – Address Resolution Protocol]]
- [[02-DHCP|DHCP – Dynamic Host Configuration Protocol]]
- [[03-DNS|DNS – Domain Name System]]

### Anwendungsschicht
- [[02-HTTP|HTTP – Hypertext Transfer Protocol]]

