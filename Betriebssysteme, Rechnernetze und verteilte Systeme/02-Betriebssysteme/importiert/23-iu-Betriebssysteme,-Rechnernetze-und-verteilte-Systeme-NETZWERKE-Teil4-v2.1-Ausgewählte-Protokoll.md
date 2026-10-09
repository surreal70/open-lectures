---
author: Andreas Hümmer
title: "Betriebssysteme, Rechnernetze und verteilte Systeme"
tags:
  - content
  - importiert
  - bs
created: '2026-10-07'
modified: '2026-10-07'
bereich: BS
typ: sonstig
quelle: "23-iu-Betriebssysteme, Rechnernetze und verteilte Systeme-NETZWERKE-Teil4-v2.1 - Ausgewählte Protokolle.pdf"
seiten: 14
---
author: Andreas Hümmer

# Betriebssysteme, Rechnernetze und verteilte Systeme

> [!info] Dokumentinformationen
> - **Quelle:** 23-iu-Betriebssysteme, Rechnernetze und verteilte Systeme-NETZWERKE-Teil4-v2.1 - Ausgewählte Protokolle.pdf
> - **Typ:** sonstig
> - **Bereich:** BS
> - **Seiten:** 14
> - **Autor:** Andreas Hümmer

---
author: Andreas Hümmer

## Inhalt

### Seite 1

Betriebssysteme,
Rechnernetze und
verteilte Systeme
Sommersemester 2025
Andreas Hümmer
V 2.1
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE

### Seite 2

Rechnernetze
Ausgewählte Protokolle
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme

### Seite 3

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
ARP – Address Resolution Protcol – RFC 826
 ARP arbeitet auf Layer 2
 ARP ist für die Auflösung der MAC Adressen im lokalen Netz
zuständig (IP-Adresse zu MAC-Adresse)
Bild:
Cisco

### Seite 4

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
NBDP - Neighbor Discovery Protocol – RFC ???
 IPv6 Ersatz für das ARP
 …tbd
Bild:
Cisco

### Seite 5

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
DHCP – Dynamic Host Configuration Protocol – RFC
2131
DHCP (Dynamic Host Configuration Protocol) ist ein Dienst, der
den Teilnehmern in einem lokalen Netz Konfigurationsdaten
und vor allem die IP-Adresse zuteilt, über die er mit anderen
Netzteilnehmern kommunizieren kann
IP-Adresse-Bestätigung
DHCPACKNOWLEDGEMENT
IP-Adresse-Annahme
DHCPRECOVER oder DHCPREQUEST
IP-Adresse-Angebot
DHCPOFFER
DHCP-Client
IP-Adresse-Anfrage
DHCPDISCOVER
DHCP-Server

### Seite 6

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
DHCP – DHCP Nachrichten
 DHCPDISCOVER: Ein Client ohne IP-Adresse sendet eine Broadcast-Anfrage
nach Adress-Angeboten an alle DHCP-Server im lokalen Netz.
 DHCPOFFER: Die DHCP-Server antworten mit entsprechenden Werten auf eine
DHCPDISCOVER-Anfrage.
 DHCPREQUEST: Der Client fordert eine der angebotenen IP-Adressen, weitere
Daten sowie Verlängerung der Lease-Zeit von einem der antwortenden DHCP-
Server.
 DHCPACK: Bestätigung des DHCP-Servers zu einer DHCPREQUEST-Anforderung
oder die Übermittlung von Konfigurationsparametern, die vorher durch
DHCPINFORM vom Client angefordert wurden.
 DHCPNAK: Ablehnung einer DHCPREQUEST-Anforderung durch den DHCP-
Server.
 DHCPDECLINE: Ablehnung durch den Client, da die IP-Adresse schon
verwendet wird.
 DHCPRELEASE: Der Client gibt die eigene Konfiguration frei, damit die
Parameter wieder für andere Clients zur Verfügung stehen.
 DHCPINFORM: Anfrage eines Clients nach weiteren Konfigurationsparametern,
z. B. weil der Client eine statische IP-Adresse besitzt.

### Seite 7

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
DHCP – Dynamic Host Configuration Protocol – RFC
2131
Verwendete Portnummern:
 67 UDP – IPv4 Server oder Relay Agent
 68 UDP – IPv4 Client
 547 UDP – IPv6 Server oder Relay Agent
 546 UDP – IPv6 Client
Mögliche Serveroptionen (Auszug):
 Time Server (RFC 868) und NTP-Server
 Name Server
 Router

### Seite 8

iu © 2023 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
DNS – Domain Name System -  RFC 1034, 1035
 DNS arbeitet auf Layer 7
 DNS ist für die Auflösung von Namen zu IP Adressen
zuständig
 Exemplarische Einträge in der DNS Datenbank:
Type IPv4 IPv6 Beispiel
Name to Address A AAAA foo.nowhere.org.                  IN   A          192.168.1.2
Adress to Name PTR 2.1.168.192.in-addr.arpa.    IN   PTR
foo.nowhere.org.
Alias for Name CNAME www                                       IN   CNAME
foo.nowhere.org.
Pointer  to
Nameserver (for
Domain)
NS nowhere.org.                         IN   NS
foo.nowhere.org.
Pointer to
Mailserver (for
Domain)
MX nowhere.org.             10        IN   MX
foo.nowhere.org.

### Seite 9

iu © 2023 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
DNS – Client zu Server
 Ein Client fragt bei einem Server eine Namensauflösung an
 Folgende Fälle können auftreten:
1
Cache Hit
in lokalem
DNS
Cache
DNS request:
Server:53
(udp)
1
3
2
DNS reply
Bei Cache
Miss
Cache Hit
in lokalem
DNS
Cache
5 4
DNS reply Ist
authorativ
e DNS für
die
angefragt
e zone
Bei Cache
Miss
DNS request:
Server:53
(udp)
5
6
DNS reply
Forwarding
NS7
Not
authorativ
e
Not
authorativ
e, no
Forwarder
s
DNS request:
Server:53
(udp)
6
Root
NS
5
ACHTUNG:
Auch negative
Caching!

### Seite 10

iu © 2023 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
DNS – Server zu Server
 Server tauschen Statusupdates und Daten aus
 Ausgewählte DNS Zonenkonfigurationen:
 Stub Zone
Eine Stub Zone enthält einen direkten Verweis
aud den/die authorative Nameserver für eine
DNS Zone
 Delegate
Benennt einen authorative Nameserver für eine
DNS Zone
 Secondary
Ein authorative DNS Server, der eine Kopie der
Zonendaten führt. Die Kopie bezieht er vom
Primary DNs Server für diese Zone. Die
Zonendaten müssen also nur an einer Stelle
gepflegt werden.
 Hidden Primary
Die Zonendaten auf diesem DNS Server zeigen
auf „andere“ authorative DNS Server für
diese Zone.
DNS Zone
request:
Server:53 (tdp)
4
3
DNS Zone
data:
DNS Update
ACK
1
2
Secondary
Primary DNS Update
Notify

### Seite 11

iu © 2023 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
NTP – Network Time Protocol -  RFC 5905
NTP, kurz für Network Time
Protocol, ist ein
Netzwerkprotokoll, das die
Synchronisation von
Computeruhren über das
Internet ermöglicht. Es sorgt
dafür, dass Geräte in einem
Netzwerk eine einheitliche
Zeit verwenden
Verwendete Ports: 123 UDP
und TCP

### Seite 12

iu © 2023 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
L2 – Spanning Tree
Das Spanning Tree Protocol verhindert
Broadcast-Stürme und andere Störungen der
Kommunikation in einem Netzwerk. Die
vergleichsweise lange Ausfallzeit, die durch die
Neustrukturierung des namensgebenden
Spannbaums entsteht, macht das Verfahren
allerdings anfällig für Angriffe
Im ersten Schritt wird beim Spanning Tree
Protocol eine Root Bridge ausgewählt, die als
Ausgangspunkt für den Spannbaum fungiert.
Von dort werden dann die einzelnen Pfade
ausgebaut, indem der Algorithmus Ports aktiviert
oder deaktiviert. Nur über die Root Bridge
können auch Einstellungen verändert und die
folgenden Timer neu justiert werden.
1
2
2
3
3
3
4
4
5
5
5
L2 ohne Sp...
Text is not SVG - cannot display

### Seite 13

iu © 2023 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
L2 – Spanning Tree
Portstati beim Spanning Tree
 Forwarding: Ports, die als forwarding gelistet sind, können Frames
weiterleiten, Adressen lernen und Bridge Protocol Data Units
empfangen, verarbeiten und übertragen.
 Blocking: Ports, die auf blocking stehen, verwerfen zwar Frames und
lernen keine Adressen, empfangen und verarbeiten dafür aber Bridge
Protocol Data Units.
 Listening: Listening Ports verwerfen Frames, lernen keine Adressen,
empfangen, verarbeiten und übertragen allerdings Bridge Protocol
Data Units.
 Learning: Learning Ports verwerfen zwar Frames, lernen aber
Adressen und empfangen, verarbeiten und übertragen Bridge
Protocol Data Units.
 Disabled: Ports, die auf disabled gestellt sind, verwerfen Frames,
lernen keine Adressen und können Bridge Protocol Data Units weder
empfangen noch verarbeiten.

### Seite 14

iu © 2023 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
L2 – Spanning Tree
https://www.cs.usfca.edu/~ga
lles/visualization/Prim.html
https://
algorithms.discrete.ma.tum.d
e/graph-algorithms/mst-
kruskal/index_en.html
