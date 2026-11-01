---
author: Andreas Hümmer
title: 'Lösung: Rechnernetze (Klausurformat)'
tags:
  - loesung
  - rn
  - klausur
bereich: RN
created: '2026-11-01'
modified: '2025-07-18'
---

# Lösung: Rechnernetze (Klausurformat)

**Zugehörige Übung:** [[UE-RN-Rechnernetze|Übung: Rechnernetze (Klausurformat)]]

---

## Teil 1: Grundlagen (15 Punkte)

### Aufgabe 1.1: Fundamentale Aspekte der Kommunikation (5 Punkte)

**a) Fünf fundamentale Aspekte:**

> [!success] **Musterlösung**
> | Nr. | Aspekt | Kurzbeschreibung | Moderne Entsprechung |
> |-----|--------|------------------|----------------------|
> | 1 | **Gemeinsames Alphabet** | Sender und Empfänger müssen die Zeichen verstehen | Protokolle (TCP/IP, HTTP) |
> | 2 | **Reichweite** | Maximale Distanz für Signalübertragung | LAN < WAN < Satellit |
> | 3 | **Bandbreite** | Informationsmenge pro Zeiteinheit | bps, Mbps, Gbps |
> | 4 | **Kommunikationspartner** | Wer kann mit wem kommunizieren? | Unicast, Broadcast, Multicast |
> | 5 | **Zuverlässigkeit** | Kommt die Nachricht korrekt an? | ARQ, Checksummen, FEC |

---

### Aufgabe 1.2: Netzwerktypen (5 Punkte)

> [!success] **Musterlösung**
> | Netzwerktyp | Ausgeschrieben | Reichweite | Typische Technologie | Bandbreite |
> |-------------|----------------|------------|---------------------|------------|
> | PAN | Personal Area Network | ~10 m | Bluetooth, ZigBee, NFC | kbps – Mbps |
> | LAN | Local Area Network | Haus/Campus | Ethernet, WiFi | Mbps – Gbps |
> | MAN | Metropolitan Area Network | Stadt/Region | Metro-Ethernet, Glasfaser | Gbps |
> | WAN | Wide Area Network | Land/Kontinent | MPLS, Glasfaser, VPN | Gbps |

---

### Aufgabe 1.3: Topologien (5 Punkte)

**a) Stern-Topologie mit zentralem Switch und 4 Endgeräten:**

> [!success] **Musterlösung**
> ```
>            [PC1]
>              │
>              │
> [PC2]───────[SW]───────[PC3]
>              │
>              │
>            [PC4]
> ```
> *SW = zentraler Switch, PC1-PC4 = Endgeräte*

**b) Vorteile und Nachteile der Topologien:**

> [!success] **Musterlösung**
> | Topologie | Vorteile | Nachteile |
> |-----------|----------|-----------|
> | Bus | 1. Einfache Installation <br> 2. Geringer Kabelaufwand | 1. Single Point of Failure (Kabel) <br> 2. Schwierige Fehlersuche |
> | Stern | 1. Einfache Fehlersuche <br> 2. Ausfall eines Endgeräts betrifft nur dieses | 1. Single Point of Failure (Zentrale) <br> 2. Hoher Kabelaufwand |
> | Mesh (vollvermascht) | 1. Hohe Redundanz <br> 2. Kein Single Point of Failure | 1. Sehr hoher Kabelaufwand <br> 2. Komplexe Konfiguration |

---

## Teil 2: Standards und Gremien (10 Punkte)

### Aufgabe 2.1: Standardisierungsgremien (5 Punkte)

> [!success] **Musterlösung**
> | Gremium | Zuständigkeitsbereich | Beispiel-Standard |
> |---------|----------------------|-------------------|
> | IEEE | LAN/WLAN-Technologien | 802.3 (Ethernet), 802.11 (WLAN) |
> | IETF | Internet-Protokolle | TCP/IP, HTTP, DNS (als RFCs) |
> | ISO | Allgemeine internationale Standards | OSI-Modell (ISO/IEC 7498), ISO 27001 |
> | ITU | Telekommunikation | H.264 (Video), G.711 (Audio), xDSL |

---

### Aufgabe 2.2: De-facto vs. De-jure Standards (5 Punkte)

**a) Unterschied:**

> [!success] **Musterlösung**
> | Standardtyp | Definition | Entstehungsweg |
> |-------------|------------|----------------|
> | De-jure | Offiziell durch Gremien verabschiedet ("nach Recht") | Formeller Prozess durch IEEE, ISO, IETF etc. mit Abstimmung und Genehmigung |
> | De-facto | Durch Marktdominanz zum Standard geworden ("nach Tatsache") | Weite Verbreitung durch einen Hersteller oder eine Technologie ohne formelles Verfahren |

**b) Beispiele:**

> [!success] **Musterlösung**
> _De-facto:_
> - TCP/IP (vor der RFC-Standardisierung)
> - Windows-Betriebssystem
> 
> _De-jure:_
> - IEEE 802.3 (Ethernet)
> - ISO/IEC 7498 (OSI-Modell)

---

## Teil 3: Referenzmodelle (20 Punkte)

### Aufgabe 3.1: OSI-Modell (8 Punkte)

> [!success] **Musterlösung**
> | Nr. | Schicht (deutsch) | Schicht (englisch) | Aufgabe | PDU | Beispiel |
> |-----|-------------------|-------------------|---------|-----|----------|
> | 7 | Anwendung | Application | Schnittstelle für Anwendungsprozesse | Daten | HTTP, SMTP, DNS |
> | 6 | Darstellung | Presentation | Datenformatierung, Verschlüsselung | Daten | SSL/TLS, JPEG, ASCII |
> | 5 | Sitzung | Session | Dialogsteuerung, Sitzungsverwaltung | Daten | RPC, NetBIOS |
> | 4 | Transport | Transport | Ende-zu-Ende-Kommunikation, Flusskontrolle | Segment | TCP, UDP |
> | 3 | Vermittlung | Network | Logische Adressierung, Routing | Paket | IP, ICMP, Router |
> | 2 | Sicherung | Data Link | Rahmenbildung, MAC-Adressierung | Frame | Ethernet, Switch |
> | 1 | Bitübertragung | Physical | Physikalische Signalübertragung | Bit | Hub, Repeater, Kabel |

---

### Aufgabe 3.2: TCP/IP-Modell (6 Punkte)

**a) Schichten und OSI-Zuordnung:**

> [!success] **Musterlösung**
> | TCP/IP-Schicht | Entsprechende OSI-Schicht(en) |
> |----------------|-------------------------------|
> | Anwendung | 7 (Anwendung) + 6 (Darstellung) + 5 (Sitzung) |
> | Transport | 4 (Transport) |
> | Internet | 3 (Vermittlung) |
> | Netzzugang | 2 (Sicherung) + 1 (Bitübertragung) |

**b) Protokollzuordnung:**

> [!success] **Musterlösung**
> | Anwendungsschicht | Transportschicht | Internetschicht | Netzzugangsschicht |
> |-------------------|-----------------|-----------------|-------------------|
> | HTTP, DNS | TCP, UDP | IP | Ethernet, ARP |

---

### Aufgabe 3.3: Datenkapselung und Paketfluss (6 Punkte)

**a) Prozess der Datenkapselung (Encapsulation):**

> [!success] **Musterlösung**
> Beim Durchlaufen der TCP/IP-Schichten werden die Daten von oben nach unten **gekapselt** – jede Schicht fügt ihren eigenen Header (und ggf. Trailer) hinzu:
> 
> 1. **Anwendungsschicht:** Erzeugt die Anwendungsdaten (z.B. HTTP-Request)
> 2. **Transportschicht:** Fügt TCP/UDP-Header hinzu → **Segment** (bei TCP) oder **Datagramm** (bei UDP)
> 3. **Internetschicht:** Fügt IP-Header hinzu → **Paket**
> 4. **Netzzugangsschicht:** Fügt Ethernet-Header und Trailer (FCS) hinzu → **Frame**
> 
> Beim Empfänger wird dieser Prozess umgekehrt durchlaufen (Decapsulation).

**b) Router und Paketverarbeitung:**

> [!success] **Musterlösung**
> Ein Router arbeitet auf **Schicht 3 (Netzwerkschicht)** und verarbeitet auch **Schicht 2 (Sicherungsschicht)**:
> 
> 1. Der Router entfernt den **Ethernet-Frame-Header** (Layer 2) beim Empfang
> 2. Er liest den **IP-Header** (Layer 3) und trifft eine Routing-Entscheidung
> 3. Der **TTL-Wert** im IP-Header wird um 1 dekrementiert
> 4. Die **Header-Checksum** wird neu berechnet
> 5. Ein **neuer Layer-2-Header** wird für das ausgehende Interface erstellt (neue Quell- und Ziel-MAC-Adressen)
> 
> **Was sich ändert:** Layer-2-Adressen (MAC), TTL, IP-Header-Checksum
> **Was gleich bleibt:** Quell- und Ziel-IP-Adressen (bei normalem Routing ohne NAT)

---

## Teil 4: Netzwerkschicht / IP (20 Punkte)

### Aufgabe 4.1: IPv4-Adressierung (6 Punkte)

**a) Netzwerkanteil vs. Hostanteil:**

> [!success] **Musterlösung**
> Eine IP-Adresse besteht aus zwei Teilen:
> 
> - **Netzwerkanteil:** Identifiziert das Netzwerk, in dem sich der Host befindet. Alle Geräte im selben Netzwerk haben denselben Netzwerkanteil. Dieser Teil wird für das Routing verwendet.
> - **Hostanteil:** Identifiziert das einzelne Gerät innerhalb des Netzwerks. Jedes Gerät im Netzwerk muss einen eindeutigen Hostanteil haben.
> 
> Die **Subnetzmaske** definiert die Grenze zwischen Netzwerk- und Hostanteil.

**b) Private IPv4-Adressbereiche:**

> [!success] **Musterlösung**
> | Bereich | CIDR-Notation | Anzahl Adressen |
> |---------|---------------|-----------------|
> | Klasse A | 10.0.0.0/8 | 16.777.216 (ca. 16,7 Mio.) |
> | Klasse B | 172.16.0.0/12 | 1.048.576 (ca. 1 Mio.) |
> | Klasse C | 192.168.0.0/16 | 65.536 |

**c) Warum private IP-Adressen nicht routbar:**

> [!success] **Musterlösung**
> Private IP-Adressen nach RFC 1918 sind **nicht im Internet routbar**, weil:
> 
> 1. Internet-Router haben keine Routen für diese Adressbereiche in ihren Routing-Tabellen
> 2. Diese Adressen können in **vielen verschiedenen Netzwerken gleichzeitig** verwendet werden (keine globale Eindeutigkeit)
> 3. Ein Router im Internet könnte nicht wissen, an welches der tausenden Netzwerke mit z.B. 192.168.1.0/24 ein Paket weitergeleitet werden soll
> 
> Für die Kommunikation mit dem Internet wird **NAT (Network Address Translation)** benötigt, das die private Adresse in eine öffentliche übersetzt.

---

### Aufgabe 4.2: Subnetting (8 Punkte)

**a) Subnetzmaske für 4 Subnetze:**

> [!success] **Musterlösung**
> Um 4 Subnetze zu erstellen, benötigt man 2 zusätzliche Bits für die Netzwerkadresse (2² = 4).
> 
> - **CIDR-Notation:** /26
> - **Dezimalschreibweise:** 255.255.255.192
> 
> Erklärung: /24 + 2 Bits = /26

**b) Die 4 Subnetze:**

> [!success] **Musterlösung**
> | Subnetz | Netzwerkadresse | Erste Host-IP | Letzte Host-IP | Broadcast-Adresse | Anzahl Hosts |
> |---------|-----------------|---------------|----------------|-------------------|--------------|
> | 1 | 192.168.10.0/26 | 192.168.10.1 | 192.168.10.62 | 192.168.10.63 | 62 |
> | 2 | 192.168.10.64/26 | 192.168.10.65 | 192.168.10.126 | 192.168.10.127 | 62 |
> | 3 | 192.168.10.128/26 | 192.168.10.129 | 192.168.10.190 | 192.168.10.191 | 62 |
> | 4 | 192.168.10.192/26 | 192.168.10.193 | 192.168.10.254 | 192.168.10.255 | 62 |
> 
> **Berechnung:** Bei /26 bleiben 6 Bits für Hosts → 2⁶ - 2 = 62 nutzbare Host-Adressen pro Subnetz

---

### Aufgabe 4.3: ICMP und Diagnose (6 Punkte)

**a) ICMP-Nachrichtentypen bei Ping:**

> [!success] **Musterlösung**
> | Richtung | ICMP-Typ | Typ-Nummer |
> |----------|----------|------------|
> | Anfrage | Echo Request | Type 8 |
> | Antwort | Echo Reply | Type 0 |

**b) Traceroute und TTL:**

> [!success] **Musterlösung**
> Traceroute ermittelt den Pfad durch das Netzwerk mittels **TTL-Manipulation**:
> 
> 1. Traceroute sendet ein Paket mit **TTL=1** an das Ziel
> 2. Der **erste Router** dekrementiert TTL auf 0 und verwirft das Paket
> 3. Der Router sendet eine **ICMP Time Exceeded** (Type 11) Nachricht zurück
> 4. Traceroute notiert die IP-Adresse dieses Routers und die Laufzeit (RTT)
> 5. Nun wird ein Paket mit **TTL=2** gesendet → der zweite Router antwortet
> 6. Dieser Vorgang wird wiederholt, bis das Ziel erreicht ist (Echo Reply)
> 
> So wird Hop für Hop der gesamte Pfad rekonstruiert.

**c) TTL=0:**

> [!success] **Musterlösung**
> Wenn der TTL-Wert eines Pakets auf 0 fällt, wird das Paket vom Router **verworfen** und eine **ICMP Time Exceeded** Nachricht (Type 11, Code 0) an den Absender zurückgeschickt. Dies verhindert **Endlosschleifen** im Netzwerk bei fehlerhaftem Routing.

---

## Teil 5: Transportschicht (20 Punkte)

### Aufgabe 5.1: TCP vs. UDP Vergleich (8 Punkte)

> [!success] **Musterlösung**
> | Kriterium | TCP | UDP |
> |-----------|-----|-----|
> | Verbindungsaufbau | Ja (3-Way-Handshake) | Nein (verbindungslos) |
> | Zuverlässigkeit | Zuverlässig (Bestätigungen, Neuübertragung) | Unzuverlässig (Best-Effort) |
> | Reihenfolgegarantie | Ja (Sequenznummern) | Nein |
> | Flusskontrolle | Ja (Sliding Window) | Nein |
> | Header-Größe | 20-60 Bytes | 8 Bytes |
> | Typische Anwendung | 1. HTTP/HTTPS (Web) <br> 2. SMTP (E-Mail) | 1. DNS (Namensauflösung) <br> 2. VoIP/Streaming |

---

### Aufgabe 5.2: TCP 3-Way-Handshake (6 Punkte)

**a) Die drei Schritte:**

> [!success] **Musterlösung**
> | Schritt | Richtung | Gesetzte Flags | Beschreibung |
> |---------|----------|----------------|--------------|
> | 1 | Client → Server | SYN | Client initiiert Verbindung, sendet initiale Sequenznummer |
> | 2 | Server → Client | SYN, ACK | Server bestätigt und sendet eigene Sequenznummer |
> | 3 | Client → Server | ACK | Client bestätigt Server-Sequenznummer, Verbindung steht |

**b) Sequenznummern-Berechnung:**

> [!success] **Musterlösung**
> | Paket | Sequenznummer | ACK-Nummer |
> |-------|---------------|------------|
> | SYN (Client → Server) | 1000 | – |
> | SYN-ACK (Server → Client) | 5000 | **1001** |
> | ACK (Client → Server) | **1001** | **5001** |
> 
> **Erklärung:**
> - Die ACK-Nummer ist immer die **erwartete nächste Sequenznummer** = empfangene SEQ + 1 (bei SYN) bzw. + Datenlänge
> - SYN-ACK: ACK = 1000 + 1 = **1001** (Client-SYN verbraucht 1 Sequenznummer)
> - Finales ACK: SEQ = **1001** (nächste Client-Sequenznummer), ACK = 5000 + 1 = **5001**

---

### Aufgabe 5.3: Flusskontrolle und Sliding Window (6 Punkte)

**a) Sliding-Window-Verfahren:**

> [!success] **Musterlösung**
> Das **Sliding-Window-Verfahren** ist ein Mechanismus zur Flusskontrolle bei TCP:
> 
> 1. Der **Empfänger** teilt dem Sender über das Window-Feld im TCP-Header mit, wie viel Pufferplatz noch verfügbar ist
> 2. Der **Sender** darf nur so viele Bytes senden, wie das Fenster erlaubt, ohne auf eine Bestätigung zu warten
> 3. Bei Empfang eines **ACK** gleitet das Fenster nach rechts – neue Bytes werden sendbar
> 4. Das Fenster kann **dynamisch** angepasst werden (vergrößern bei freiem Puffer, verkleinern bei vollem Puffer)
> 
> **Vorteil:** Ermöglicht effizientes **Pipelining** – mehrere Segmente gleichzeitig unterwegs, statt Stop-and-Wait.

**b) Flusskontrolle vs. Staukontrolle:**

> [!success] **Musterlösung**
> | Mechanismus | Schützt vor | Ziel |
> |-------------|-------------|------|
> | Flusskontrolle | Überlastung des **Empfängers** | Anpassung der Senderate an die Verarbeitungsgeschwindigkeit des Empfängers (Receiver Window) |
> | Staukontrolle | Überlastung des **Netzwerks** | Anpassung der Senderate an die verfügbare Netzwerkkapazität (Congestion Window) |

**c) Window = 0:**

> [!success] **Musterlösung**
> Wenn der Empfänger ein **Window = 0** sendet, muss der Sender die Datenübertragung **pausieren**. Der Sender startet einen **Persist Timer** und sendet periodisch kleine **Window Probes** (1 Byte), um zu erfahren, wann wieder Pufferplatz verfügbar ist. Erst wenn der Empfänger ein Window > 0 ankündigt, wird die Übertragung fortgesetzt.

---

## Teil 6: Basisprotokolle (20 Punkte)

### Aufgabe 6.1: ARP (6 Punkte)

**a) Zweck von ARP:**

> [!success] **Musterlösung**
> Das **Address Resolution Protocol (ARP)** löst IP-Adressen in MAC-Adressen auf. Es wird als **"Brücke zwischen Layer 2 und Layer 3"** bezeichnet, weil:
> 
> - **Layer 3 (IP)** arbeitet mit logischen IP-Adressen für das Routing über Netzwerkgrenzen hinweg
> - **Layer 2 (Ethernet)** arbeitet mit physischen MAC-Adressen für die lokale Zustellung
> - ARP **übersetzt** zwischen beiden Adresstypen: Ein Host kennt die Ziel-IP, benötigt aber die Ziel-MAC für den Ethernet-Frame

**b) Broadcast vs. Unicast:**

> [!success] **Musterlösung**
> | Nachrichtentyp | Übertragungsart | Begründung |
> |----------------|-----------------|------------|
> | ARP Request | Broadcast | Der anfragende Host kennt die gesuchte MAC-Adresse nicht und muss daher **alle Hosts** im lokalen Netzwerk fragen ("Wer hat IP x.x.x.x?") |
> | ARP Reply | Unicast | Der antwortende Host kennt jetzt die MAC-Adresse des Anfragenden (aus dem Request) und kann **direkt** antworten – ein Broadcast wäre unnötig |

**c) ARP-Spoofing und Schutz:**

> [!success] **Musterlösung**
> _ARP-Spoofing:_
> Ein Angreifer sendet gefälschte ARP-Replies, um seine eigene MAC-Adresse mit der IP-Adresse eines anderen Hosts (z.B. Gateway) zu verknüpfen. Dadurch wird der Traffic zum Angreifer umgeleitet (**Man-in-the-Middle-Angriff**).
> 
> _Schutzmaßnahme:_
> **Dynamic ARP Inspection (DAI)** auf dem Switch: Der Switch prüft ARP-Pakete gegen eine vertrauenswürdige Datenbank (DHCP-Snooping-Tabelle) und blockiert gefälschte ARP-Nachrichten.

---

### Aufgabe 6.2: DHCP (8 Punkte)

**a) Der DORA-Prozess:**

> [!success] **Musterlösung**
> | Schritt | Name | Richtung | Übertragungsart | Beschreibung |
> |---------|------|----------|-----------------|--------------|
> | D | DHCPDISCOVER | Client → Server | Broadcast | Client sucht DHCP-Server im Netzwerk |
> | O | DHCPOFFER | Server → Client | Broadcast/Unicast | Server bietet IP-Adresse und Konfiguration an |
> | R | DHCPREQUEST | Client → Server | Broadcast | Client akzeptiert ein Angebot (informiert alle Server) |
> | A | DHCPACK | Server → Client | Broadcast/Unicast | Server bestätigt die Zuweisung, Client nutzt IP |

**b) DHCPREQUEST als Broadcast:**

> [!success] **Musterlösung**
> Der Client sendet DHCPREQUEST als **Broadcast**, damit **alle** DHCP-Server im Netzwerk erfahren, welchen Server der Client gewählt hat. Server, deren Angebot nicht angenommen wurde, können ihre reservierten IP-Adressen dann wieder freigeben und für andere Clients verfügbar machen.

**c) T1 und T2 bei der Lease-Erneuerung:**

> [!success] **Musterlösung**
> | Zeitpunkt | Prozent der Lease | Verhalten des Clients |
> |-----------|-------------------|----------------------|
> | T1 | 50% | Client versucht **Renewal**: sendet DHCPREQUEST direkt an den ursprünglichen Server (Unicast) |
> | T2 | 87,5% | Client versucht **Rebinding**: sendet DHCPREQUEST als Broadcast an alle Server (falls ursprünglicher Server nicht erreichbar) |

---

### Aufgabe 6.3: DNS (6 Punkte)

**a) DNS-Hierarchie:**

> [!success] **Musterlösung**
> | Ebene | Name | Beispiel |
> |-------|------|----------|
> | 0 | Root-Zone | `.` (13 Root-Server: a-m.root-servers.net) |
> | 1 | Top-Level-Domain (TLD) | `.de`, `.com`, `.org` |
> | 2 | Second-Level-Domain (SLD) | `example.de`, `google.com` |
> | 3+ | Subdomain / Host | `www.example.de`, `mail.google.com` |

**b) DNS-Record-Typen:**

> [!success] **Musterlösung**
> | Record-Typ | Zweck | Beispiel |
> |------------|-------|----------|
> | A | Name → IPv4-Adresse | `www IN A 192.168.1.2` |
> | AAAA | Name → IPv6-Adresse | `www IN AAAA 2001:db8::1` |
> | MX | Mailserver für Domain (mit Priorität) | `example.de IN MX 10 mail.example.de` |
> | CNAME | Alias für anderen Namen | `www IN CNAME webserver.example.de` |
> | NS | Nameserver für Zone | `example.de IN NS ns1.example.de` |
> | PTR | IP → Name (Reverse Lookup) | `2.1.168.192.in-addr.arpa IN PTR www` |

**c) Rekursive vs. iterative Auflösung:**

> [!success] **Musterlösung**
> | Auflösungsart | Client-Perspektive | Server-Verhalten |
> |---------------|-------------------|------------------|
> | Rekursiv | Client stellt eine Anfrage und erwartet die **vollständige Antwort** | Server übernimmt die gesamte Auflösung und fragt selbst weitere Server, bis das Ergebnis vorliegt |
> | Iterativ | Client muss ggf. **mehrere Server** selbst befragen | Server antwortet mit **Verweis** auf den nächsten zuständigen Server, ohne selbst weiterzufragen |

---

## Teil 7: Anwendungsschicht (15 Punkte)

### Aufgabe 7.1: HTTP-Grundlagen (7 Punkte)

**a) HTTP-Methoden:**

> [!success] **Musterlösung**
> | Methode | Verwendung |
> |---------|-----------|
> | GET | Ressource abrufen (ohne Seiteneffekte) |
> | POST | Daten an Server senden, neue Ressource erstellen |
> | PUT | Ressource vollständig ersetzen/aktualisieren |
> | DELETE | Ressource löschen |

**b) Aufbau einer HTTP-Anfrage:**

> [!success] **Musterlösung**
> Eine HTTP-Anfrage (Request) besteht aus drei Teilen:
> 
> 1. **Request-Line:** Methode, Pfad/URI und HTTP-Version (z.B. `GET /index.html HTTP/1.1`)
> 2. **Header:** Key-Value-Paare mit Metadaten (z.B. `Host: www.example.com`, `User-Agent: ...`, `Accept: text/html`)
> 3. **Body:** Optionaler Nachrichtentext mit Nutzdaten (bei POST/PUT, leer bei GET)
> 
> Zwischen Header und Body steht eine Leerzeile.

**c) HTTP-Statuscodes:**

> [!success] **Musterlösung**
> | Statuscode | Kategorie | Bedeutung |
> |------------|-----------|-----------|
> | 200 | 2xx Success | OK – Anfrage erfolgreich |
> | 301 | 3xx Redirection | Moved Permanently – Ressource dauerhaft verschoben |
> | 404 | 4xx Client Error | Not Found – Ressource nicht gefunden |
> | 500 | 5xx Server Error | Internal Server Error – Serverfehler |
> | 401 | 4xx Client Error | Unauthorized – Authentifizierung erforderlich |
> | 503 | 5xx Server Error | Service Unavailable – Dienst nicht verfügbar |

---

### Aufgabe 7.2: HTTP vs. HTTPS (4 Punkte)

**a) Unterschied HTTP und HTTPS:**

> [!success] **Musterlösung**
> - **HTTP** (Port 80) überträgt Daten im **Klartext** – alle Inhalte können von Dritten mitgelesen werden (z.B. bei Man-in-the-Middle-Angriffen)
> - **HTTPS** (Port 443) verschlüsselt die gesamte Kommunikation mittels **TLS (Transport Layer Security)** und bietet:
>   - **Vertraulichkeit:** Daten sind verschlüsselt
>   - **Integrität:** Manipulation wird erkannt
>   - **Authentizität:** Server-Identität wird durch Zertifikate bestätigt

**b) Zusätzliche Schicht:**

> [!success] **Musterlösung**
> | Aspekt | Antwort |
> |--------|---------|
> | Hinzugefügte Schicht | TLS (Transport Layer Security) / SSL |
> | Zweck | Verschlüsselung der Daten, Integritätsprüfung und Authentifizierung des Servers (optional auch des Clients) durch Zertifikate |

---

### Aufgabe 7.3: Cookies und Session-Management (4 Punkte)

**a) Warum Cookies notwendig:**

> [!success] **Musterlösung**
> HTTP ist ein **zustandsloses Protokoll** – jede Anfrage ist unabhängig und der Server "vergisst" den Client nach jeder Antwort. Für Anwendungen, die einen **Zustand über mehrere Anfragen** hinweg benötigen (Login-Status, Warenkorb, Benutzereinstellungen), sind Cookies notwendig. Der Server speichert eine **Session-ID** im Cookie, die bei jeder Anfrage mitgesendet wird und den Client identifiziert.

**b) Sicherheitsattribute für Cookies:**

> [!success] **Musterlösung**
> | Attribut | Funktion |
> |----------|----------|
> | HttpOnly | Cookie ist **nicht per JavaScript** (document.cookie) zugreifbar – schützt vor XSS-Angriffen (Cross-Site Scripting) |
> | Secure | Cookie wird **nur über HTTPS** übertragen – schützt vor Abhören bei unverschlüsselter Verbindung |
> | SameSite | Cookie wird **nicht bei Cross-Site-Requests** gesendet – schützt vor CSRF-Angriffen (Cross-Site Request Forgery) |

---

## Quellen

- [[01-Historie|Historie der Rechnernetze]]
- [[02-Netzwerktypen|Netzwerktypen]]
- [[03-Topologien|Netzwerktopologien]]
- [[01-Uebersicht|Standardisierung – Übersicht]]
- [[01-OSI-Modell|OSI-Referenzmodell]]
- [[02-TCP-IP-Modell|TCP/IP-Modell]]
- [[01-IP-Protokoll|IP-Protokoll (IPv4)]]
- [[05-ICMP|ICMP]]
- [[01-TCP|TCP – Transmission Control Protocol]]
- [[02-UDP|UDP – User Datagram Protocol]]
- [[01-ARP|ARP – Address Resolution Protocol]]
- [[02-DHCP|DHCP – Dynamic Host Configuration Protocol]]
- [[03-DNS|DNS – Domain Name System]]
- [[02-HTTP|HTTP – Hypertext Transfer Protocol]]
