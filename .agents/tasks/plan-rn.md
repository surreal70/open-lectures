# Plan: Übungsklausur Rechnernetze (UE-RN)

**Autor:** Andreas Hümmer  
**Bereich:** RN  
**Erstellt:** 2025-01-21  
**Gesamtpunktzahl:** 120 Punkte  
**Bearbeitungszeit:** 180 Minuten  

---

## Themenübersicht

Die Übungsklausur deckt alle Hauptkapitel des Bereichs Rechnernetze ab:

| Teil | Thema | Punkte | Schwerpunkte |
|------|-------|--------|--------------|
| 1 | Grundlagen | 15 | Historie, Netzwerktypen, Topologien |
| 2 | Standards und Gremien | 10 | IEEE, IETF, De-facto vs. De-jure |
| 3 | Referenzmodelle | 20 | OSI, TCP/IP, Schichtenvergleich, Einkapselung |
| 4 | Netzwerkschicht / IP | 20 | IPv4-Adressierung, Subnetting, NAT, ICMP |
| 5 | Transportschicht | 20 | TCP vs. UDP, 3-Way-Handshake, Flusskontrolle |
| 6 | Basisprotokolle | 20 | ARP, DHCP, DNS |
| 7 | Anwendungsschicht | 15 | HTTP, Statuscodes, REST |
| **Gesamt** | | **120** | |

---

## Teil 1: Grundlagen (15 Punkte)

### Aufgabe 1.1: Fundamentale Aspekte der Kommunikation (5 Punkte) ⭐
- Nennen Sie die fünf fundamentalen Aspekte jeder Kommunikation
- Tabelle: Aspekt + Beschreibung + moderne Entsprechung

### Aufgabe 1.2: Netzwerktypen (5 Punkte) ⭐
- Ordnen Sie Netzwerktypen nach Reichweite (PAN, LAN, MAN, WAN)
- Tabelle: Netzwerktyp + Reichweite + typische Technologie + Bandbreite

### Aufgabe 1.3: Topologien (5 Punkte) ⭐⭐
- Zeichnen Sie eine Stern-Topologie
- Tabelle: Topologie + 2 Vorteile + 2 Nachteile
- Berechnungsaufgabe: Wie viele Verbindungen bei vollvermaschtem Netz mit n Knoten?

---

## Teil 2: Standards und Gremien (10 Punkte)

### Aufgabe 2.1: Standardisierungsgremien (5 Punkte) ⭐
- Tabelle: Gremium (IEEE, IETF, ISO, ITU) + Zuständigkeit + Beispiel-Standard

### Aufgabe 2.2: De-facto vs. De-jure Standards (5 Punkte) ⭐⭐
- Erklären Sie den Unterschied
- Nennen Sie je 2 Beispiele

---

## Teil 3: Referenzmodelle (20 Punkte)

### Aufgabe 3.1: OSI-Modell (8 Punkte) ⭐
- Nennen Sie alle 7 OSI-Schichten in der richtigen Reihenfolge
- Tabelle: Schicht + Aufgabe + PDU-Bezeichnung + Beispielprotokoll

### Aufgabe 3.2: TCP/IP-Modell (6 Punkte) ⭐⭐
- Nennen Sie die 4 TCP/IP-Schichten
- Ordnen Sie folgende Protokolle den Schichten zu: HTTP, TCP, IP, Ethernet

### Aufgabe 3.3: Einkapselung und Paketfluss (6 Punkte) ⭐⭐
- Beschreiben Sie den Weg eines Pakets durch die Schichten (Encapsulation)
- Was ändert sich beim Durchgang durch einen Router?
- Welche Schichten verarbeitet ein Router?

---

## Teil 4: Netzwerkschicht / IP (20 Punkte)

### Aufgabe 4.1: IPv4-Adressierung (6 Punkte) ⭐
- Erklären Sie Netzwerk- und Hostanteil einer IP-Adresse
- Private vs. öffentliche Adressen: Nennen Sie die drei RFC-1918-Bereiche

### Aufgabe 4.2: Subnetting (8 Punkte) ⭐⭐⭐
- Berechnungsaufgabe: Gegeben Netzwerk X.X.X.X/Y
  - Netzwerkadresse berechnen
  - Broadcast-Adresse berechnen
  - Hostbereich angeben
  - Anzahl nutzbarer Hosts berechnen

### Aufgabe 4.3: ICMP und Diagnose (6 Punkte) ⭐⭐
- Welche ICMP-Typen werden bei Ping verwendet?
- Wie ermittelt Traceroute den Pfad durch das Netzwerk? (TTL-Trick)
- Was passiert, wenn TTL=0 erreicht wird?

---

## Teil 5: Transportschicht (20 Punkte)

### Aufgabe 5.1: TCP vs. UDP Vergleich (8 Punkte) ⭐⭐
- Tabelle mit Vergleichskriterien:
  - Verbindungsaufbau
  - Zuverlässigkeit
  - Reihenfolgegarantie
  - Header-Größe
  - Anwendungsbeispiele

### Aufgabe 5.2: TCP 3-Way-Handshake (6 Punkte) ⭐⭐
- Beschreiben Sie die drei Schritte (SYN, SYN-ACK, ACK)
- Sequenznummern-Berechnung: Gegeben initial SEQ, berechnen Sie ACK

### Aufgabe 5.3: Flusskontrolle und Sliding Window (6 Punkte) ⭐⭐⭐
- Erklären Sie das Sliding-Window-Verfahren
- Was ist der Unterschied zwischen Flusskontrolle und Staukontrolle?
- Was passiert bei Window=0?

---

## Teil 6: Basisprotokolle (20 Punkte)

### Aufgabe 6.1: ARP (6 Punkte) ⭐⭐
- Erklären Sie den Zweck von ARP (Brücke Layer 2/3)
- Warum ist ARP Request ein Broadcast, ARP Reply ein Unicast?
- Was ist ARP-Spoofing und wie schützt man sich dagegen?

### Aufgabe 6.2: DHCP (8 Punkte) ⭐⭐
- Beschreiben Sie den DORA-Prozess (4 Schritte)
- Warum ist DHCPREQUEST ein Broadcast?
- Erklären Sie T1 (50%) und T2 (87.5%) bei Lease-Erneuerung

### Aufgabe 6.3: DNS (6 Punkte) ⭐⭐
- Beschreiben Sie die DNS-Hierarchie (Root, TLD, SLD)
- Tabelle: Record-Typ (A, AAAA, MX, CNAME, NS, PTR) + Beschreibung
- Was ist der Unterschied zwischen rekursiver und iterativer Auflösung?

---

## Teil 7: Anwendungsschicht (15 Punkte)

### Aufgabe 7.1: HTTP-Grundlagen (7 Punkte) ⭐⭐
- Nennen Sie die wichtigsten HTTP-Methoden (GET, POST, PUT, DELETE) und deren Verwendung
- Erklären Sie den Aufbau einer HTTP-Anfrage (Request-Line, Header, Body)
- Tabelle: HTTP-Statuscode + Bedeutung (200, 301, 404, 500)

### Aufgabe 7.2: HTTP vs. HTTPS (4 Punkte) ⭐
- Was ist der Unterschied zwischen HTTP und HTTPS?
- Welche Schicht fügt HTTPS hinzu?

### Aufgabe 7.3: Cookies und Session-Management (4 Punkte) ⭐⭐
- Warum sind Cookies notwendig (HTTP ist zustandslos)?
- Nennen Sie 3 Sicherheitsattribute für Cookies (HttpOnly, Secure, SameSite)

---

## Schwierigkeitsverteilung

| Schwierigkeit | Symbol | Punkte | Anteil |
|---------------|--------|--------|--------|
| Leicht | ⭐ | 40 | 33% |
| Mittel | ⭐⭐ | 55 | 46% |
| Schwer | ⭐⭐⭐ | 25 | 21% |
| **Gesamt** | | **120** | **100%** |

---

## Verifizierte Quellen-Wiki-Links

Die folgenden Dateien existieren im Verzeichnis `03-Rechnernetze` und werden als Quellen verlinkt:

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
- [[02-Routing|Routing]]
- [[03-IPv6|IPv6]]
- [[05-ICMP|ICMP]]

### Transportschicht
- [[01-TCP|TCP – Transmission Control Protocol]]
- [[02-UDP|UDP – User Datagram Protocol]]
- [[03-Ports|Ports]]

### Basisprotokolle
- [[01-ARP|ARP – Address Resolution Protocol]]
- [[02-DHCP|DHCP – Dynamic Host Configuration Protocol]]
- [[03-DNS|DNS – Domain Name System]]
- [[04-NTP|NTP – Network Time Protocol]]

### Anwendungsschicht
- [[02-HTTP|HTTP – Hypertext Transfer Protocol]]
- [[03-SMTP|SMTP – Simple Mail Transfer Protocol]]

---

## Hinweise zur Umsetzung

1. **Aufgabenformat:** Orientierung an der Vorlage UE-BS-Betriebssysteme.md
   - YAML-Frontmatter mit: author, title, tags, punkte_gesamt, bearbeitungszeit, bereich, created, modified
   - Themenübersicht als [!info] Callout
   - Teile mit Aufgaben, Punkten und Schwierigkeitsmarkierungen
   - Tabellen zum Ausfüllen durch Studierende
   - Selbsteinschätzungs-Tabelle am Ende
   - Quellen-Sektion mit Wiki-Links

2. **Inhaltliche Anforderungen:**
   - Alle Aufgaben basieren auf den Inhalten der Vorlesungsnotizen
   - Prüfungsrelevante Themen aus den [!warning]-Callouts berücksichtigen
   - Mix aus Definitions-, Verständnis- und Anwendungsaufgaben
   - Berechnungsaufgaben für Subnetting und Sequenznummern

3. **Tags für Frontmatter:**
   - uebung, rn, klausur
   - osi, tcp-ip, ip, subnetting, tcp, udp, arp, dhcp, dns, http
