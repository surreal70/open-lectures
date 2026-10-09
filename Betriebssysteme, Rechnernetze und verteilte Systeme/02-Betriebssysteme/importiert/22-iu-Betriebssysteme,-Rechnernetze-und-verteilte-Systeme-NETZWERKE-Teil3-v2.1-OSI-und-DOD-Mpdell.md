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
quelle: "22-iu-Betriebssysteme, Rechnernetze und verteilte Systeme-NETZWERKE-Teil3-v2.1 - OSI und DOD Mpdell.pdf"
seiten: 60
---
author: Andreas Hümmer

# Betriebssysteme, Rechnernetze und verteilte Systeme

> [!info] Dokumentinformationen
> - **Quelle:** 22-iu-Betriebssysteme, Rechnernetze und verteilte Systeme-NETZWERKE-Teil3-v2.1 - OSI und DOD Mpdell.pdf
> - **Typ:** sonstig
> - **Bereich:** BS
> - **Seiten:** 60
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
Protokoll und Kommunikations-Formen
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
Was ist ein Protokoll?
Definition: Ein Protokoll definiert das Format und die
Reihenfolge, in der Nachrichten von Systemen in Netzwerken
gesendet und empfangen werden, so wie die Aktion, welche
durch die Nachricht ausgelöst wird.
Diese Aussage ist universell und gilt für jede Ebene der
Netzwerkkommunikation, wie wir in den Schichtmodellen
sehen werden.
Betrachtet man die Kommunikation, den eine Nachricht
durchlaufen muss von einer Anwendung zur anderen, so kann
man sagen, dass das verwendete Applikationsprotokoll
mehrere Unterprotokolle (pro Ebene eines) hat. Man spricht
hier von einem Protokoll Stack.

### Seite 4

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Kommunikationsarten
Anhand der Beteiligten und ihrer Kommunikation lassen sich
folgende Gruppen bilden, die auf allen Ebenen der
Kommunikation anwendung finden:
Art der
Beziehung
Beschreibung Strukturelement
das für die
Verteilung
maßgeblich ist
Terminus
Technicus
1:n one to all Topologie Broadcast
1:m one to many Topologie Netcast
1:1 one to one Adresse Unicast
1:l one to many Abonement Multicast

### Seite 5

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Topologie
Grafik: Wikimedia

### Seite 6

Rechnernetze
OSI/DOD Stack
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme

### Seite 7

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
OSI vs. DOD (TCP/IP)
OSI OSI
Einordnung
Protokoll-
beispiele
Einheiten Kopplun
gseleme
nte
DOD
Einordnung
DOD/TCP/
IP
7 Anwendung
(application)
Anwendung
s-orientiert
DNS
HTTPS
Daten
Applicati
on Level
Gateway,
Proxy Ende zu
Ende
Anwendun
g
6 Darstellung
(presentation)
5 Sitzung
(session)
4 Transport
(transport)
Transport-
orientiert
TCP
UDP
TCP=Segmente,
UDP=Datagram
me
Transport
3 Vermittlung
(network)
ICMP
IGMP
IP
IPSec
Pakete Router Internet
2 Sicherung
(data link)
IEEE 802.3
IEEE 802.5
IEEE 802.11
Rahmen
(frames)
Bridges,
Switches
Punkt zu
Punkt Netzzugriff
1 Bitübertragung
(physical) 1000BaseT
Token Ring Symbole
Kabel,
Hub,
Repeater

### Seite 8

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Geträte(klassen)
Gerätet
yp4
Eigenschaften Collision
Domain
Broadcas
t Domain
Arbeitet
auf
Layer
Leistungslimit
Hub Bus -> nur HDX 1 1 1 (2) Shared Wirespeed
Repeate
r
Signalverstärk
ung
1 1 2 Wirespeed
Bridge Trennt
Collision
Domains
2 1 2 Wirespeed
Switch *) Crossbar Port VLAN 2 CPU/Backplane
Bandbreite
Router Port/IP Port/
VLAN/
Subnet
3 CPU/Paket routing
engine
(App)
Gateway
Applicaito
n
Applicatio
n
7 CPU*) Switches können je nach Klasse/Ausbaustufe auch als Layer 3, Layer 7
Geräte arbeiten

### Seite 9

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Edge Connectors – Clientanbindung (physisch)
 Einwahl per Modem
Eigentlich heute eher selten, aber durchaus
noch in Verwendung im Industrieumfeld oder
für OoBM – Out of Band Management
 DSL – Digital Subscriber Line
 Breitbandkabel
 FTTH/FTTB – Fibre to the Home/Basement
 Ethernet (Kupfer und Glas)
 Token Ring
 WLAN
Verwenden
von Layer3
Tunnelproto
-kollen,
z.B. PPPoE
oder L2TP
direkt oder
mittelbar via
Router
Direkter
Layer2
Zugang zum
Netzwerk
mittels
Netzwerkkar
te

### Seite 10

Rechnernetze
Layer 1 – Bitübertragung/Physik
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme

### Seite 11

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Layer 1
MAU
Twisted
Pair
WiF
i
Gla
s
Coa
x
Signalwandlung
Date
n
Leitungscodierun
g
Physik
Aufbereitung der
Daten für
Gleichstromfreie
Übertragung und
Taktrückgewinnun
g
z.B. Manchester
Codierung

### Seite 12

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Layer 1
 Kabel und Stecker RJ45
Bilder: Wikimedia, Amazon,
et al.

### Seite 13

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Layer 1 … way back in time…Ethernet yellow cable
MAU (Media Access Unit) für yellow cable
Bilder: Wikimedia, Amazon,
et al.

### Seite 14

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Layer 1
 Kabel und Stecker optisch
Bilder: Wikimedia, Amazon,
et al.

### Seite 15

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Layer 1
 Kabel und Stecker Sonstige
Bilder: Wikimedia, Amazon, Reichelt, Aruba,
et al.

### Seite 16

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Ethernet aus der Praxis
 Weit verbreitet
 Viele Variationen
 Im Serverbereich:
Aktive Netzwerkkarten mit
eigenem Prozessor
 Zunehmend immer mehr
„Offloading“ in die
Hochintegrierten ASICS
U.a. Prüfsummenkalkulation auf
Frame-, IP-, TCP/UDP- Ebene
ASIC (Layer 2-
4)
MAU (Layer
1)
RJ45 (Layer
1)

### Seite 17

Rechnernetze
Layer 2 – Sicherung/Data Link
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme

### Seite 18

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Layer 2
Logical Link Layer
(802.3/4/…)
MAC (802.2)
Media Access
Control *)
Date
n
Date
n
*) bei CSMA/CD auch in
Layer 1
Generierung von
Prüfsummen
Padding
MAC-Adressen
Frame Codierung
Preambel Dest
Address
Src
Address
Type Data Pad Checksum

### Seite 19

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Layer 2 - Frame
Es sind vier Frametypes definiert, heute gebräuchlich sind noch
zwei:
Ehternet II und IEEE 802.3, wir beziehen und hier nur auf 802.3.
Präambel und Start-Frame Delimiter
Die Präambel besteht 7 Bytes mit der Bitfolge „10101010“ gefolgt
vom Frame-Delimiter mit der Bitfolge „10101011“, also:
10101010  10101010  10101010  10101010  10101010  10101010  10101010
10101011
Dest. Address und Src Address
Hier finden sich die MAC-Adressen der Kommunikationspartner
(später mehr zu MAC Adressen)

### Seite 20

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Layer 2 – Frame II
Type
Type gib das Protokol an, welches in der darüber
liegenden Schicht verwendet wird. Typische Werte sind in
nebenstehender Tabelle angegeben.

### Seite 21

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Layer 2 – Frame III
Padding
Padding-Bytes werden benötigt, wenn der Frame weniger als 46
Bytes Nutzdaten hat und somit kleiner als die Minimalgröße von
64 Bytes betragen würde
FCS (Frame Check Sequence)
Eine 32-Bit lange Prüfsumme die über den Frame ohne Präambel
und SFD berechnet wird. Die Berechnung erfolgt mittels CRC
(Cycly Redundancy Check) Verfahren.

### Seite 22

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Data Link Layer
Die OSI-Layer-2-Codierung, auch bekannt als
Datenverbindungsschicht oder Sicherungsschicht, ist für die
zuverlässige und fehlerfreie Datenübertragung zwischen
benachbarten Netzwerkgeräten zuständig. Sie kapselt die Daten
der höheren Schichten in Frames und verwendet MAC-Adressen,
um die Daten an das richtige Ziel zu leiten.
Aufgabe der Sicherungsschicht ist es der Vermittlungsschicht
einen übertragungsfehlerfreien Datenkanal zur Verfügung zu
stellen. Hierzu werden die Daten in Data Frames aufgeteilt und
sequenziell übertragen. War die Übertragung erfolgreich erfolgt
eine Bestätigung des Empfängers in Form eines
Acknowledgement Frames, der an den Sender zurück gesendet
wird.

### Seite 23

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Leitungs- und Kanalcodierung
Leitungskodierung:
Leitungscodierung bezieht sich auf die Verarbeitung der Daten, bevor sie über eine
Übertragungsleitung gesendet werden. Das Ziel der Leitungscodierung ist es, die
Übertragung von Signalen über eine physikalische Leitung zu optimieren, um Fehler durch
Rauschen und andere Störungen zu minimieren. Ein Beispiel für eine Leitungscodierung ist
die Differentielle Manchester-Codierung (DMC), die in Ethernet-Netzwerken verwendet wird.
DMC kodiert jedes Bit durch Veränderungen des Signalzustands, was es ermöglicht, dass das
Signal leicht erkannt und rekonstruiert werden kann, auch wenn das Signal durch Rauschen
gestört wird
Kanalkodierung:
Kanalcodierung hingegen bezieht sich auf die Verarbeitung der Daten, nachdem sie die
Leitung verlassen haben. Das Ziel der Kanalcodierung ist es, Fehler zu erkennen und zu
korrigieren, die während der Übertragung aufgetreten sind. Ein Beispiel für Kanalcodierung
ist die Cyclic Redundancy Check (CRC), die häufig bei der Übertragung von Daten in drahtlosen
Netzwerken verwendet wird. CRC fügt dem Datenstrom zusätzliche Informationen hinzu, die
es dem Empfänger ermöglichen, Übertragungsfehler zu erkennen und zu korrigieren.
Zusammen tragen Leitungscodierung und Kanalcodierung dazu bei, die Zuverlässigkeit der
Datenübertragung zu erhöhen und sicherzustellen, dass die übertragenen Daten korrekt und
vollständig empfangen werden

### Seite 24

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Punkt zu Punkt Verbindungen
Punkt zu Punkt Verbindungen stellen eine Verbingung zwischen
zwei Endpunkten her.
Typische Protokolle für P2P Verbindungen sind:
 HDLC – High Level Datalink Protocol, ISO/IEC 13239:2002.
Synchrones, bit-orientiertes Protokoll
 SLIP – Serial Line Internet Protocol. Keine Fehlererkennung,
keine Authtentifizierung, keine Adressierung (muss via höherer
Protokollschicht implementiert werden)
 PPP – Point to Point Protocol, RFC 1661, oft in Verbindung mit
PAP (Password Authentication Protocol oder CHAP (Client
Handshake Authentication Protocol)
Note: DSL arbeited mit eiem PPPoE (Point to Point over Ethernet)
Protokoll

### Seite 25

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Vielfachzugriff
Bei Netzen mit Vielfachzugriff erfolgt die Kommunikation nicht
über einen dedizierten Kanal zwischen zwei Endpunkten sondern
mittels eine shared Mediums mit mehreren Endpunkten. Typische
Vertreter sind z.B.:
 CSMA/CD basierte Verfahren, wie Ethernet und WLAN (FDMA)
  GSM, Token Ring (TDMA)
Note: Die Betrachtung des OSI/DOD Modells ist hier auf die L2
mit Vielfachzugriffen beschränkt.

### Seite 26

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
CSMA/CD – Carrier Sense Multiple Access/Collision
AvoidanceBei Netzwerken nach die mit dem CSMA/CD Verfahren arbeiten,
schick eine Station vor dem Senden der Nachricht eine sog.
Notification an die anderen Stationen im Netzwerk und geprüft
ob es zu einer Kollision gekommen ist.*) Ist das Medium belegt
(Kollision wurde detektiert) wird der Sendeversuch um eine
zufällige Zeit vertagt.
CSMA/CD Verfahren: Ethernet over Coax, WLAN.
Aber: Es kommt auch auf die Art und Weise an, wie das Medium
geshared wird (TDM, FDM, SDM)!
*) der Transceiver der Netzwerkkarte gibt das Notification-Signal
auf das Medium wärend der Receiver der Karte gleichzeitig das
Medium abhört. Das gesendete Signal wird mit dem
Empfangenen Signal verglichen. Sind die Signale unterschiedlich
kam es zu einer Kollision.

### Seite 27

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Vertiefung: Kollisionsdomäne und Slot-Time
(vereinfacht)Ein Ethernet-Paket darf minimal 64 Bytes = 512 Bit lang sein. In diesem Beispiel
soll es mit 100 MBit/s gesendet werden. Dann dauert die Aussendung des
gesamten Paketst = 5.12μs. Mit der Ausbreitungsgeschwindigkeit von v = 1.8 ·
108m/s ist das erste vom letzten Bit
s = t · v = 921m
entfernt. Im schlimmsten Fall (worst case) tritt die Kollision dicht bei einer weit
entfernten Staion auf. Die Zeit, die ein Signal braucht bis es dorthin und als
Kollisionssignal wieder zurück läuft, nennt man Round Trip Delay. Dieser Round
Trip Delay muss also immer kleiner sein als die Zeit t = 5.12μs, damit eine Kollision
auch im schlechtesten Fall erkannt wird.
Daraus folgend dürfen die Stationen nicht weiter als 921m/2 = 460m voneinander
entfernt ein.
In der Praxis hat man noch ca. den Faktor 5 als Sicherheit eingebaut: bei
100BaseT
ist die maximale Länge eines Segments 100 m. Unter Segment versteht man hier
den
Teil eines Netzes, in dem Kollisionen erkannt werden müssen. Man nennt diesen
Teil
auch Kollisionsdomäne.
Note: Vgl. Collitiondomain Ethernet TP mit Hub und mit Switch, wo ist die CD, P2P
oder shared Medium

### Seite 28

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Richtungsabhängingkeit (Duplex)
Half-Duplex
Knoten können senden und empfangen. Die Sende- und
Empfangsvorgänge finden hierbei aber NICHT gleichzeitig statt.
Voll-Duplex
Die Übertragung kann gleichzeitig in beide Richtungen erfolgen,
d.h. die Knoten können gleichzeitig sende und Empfangen.
Voll-Duplex ist nur bei Punkt zu Punkt Verbindungen möglich
Vgl. Ethernet over Coax und Ethernet over TP (Switch vs. HUB)!!

### Seite 29

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
MAC
Unicast MAC
 MAC Adressformat:  48 Bit:
a4:bb:6d:ac:ea:1d
Die MAC besteht aus zwei Teilen, dem Hersteller Teil (blau) und dem
Geräte Teil (grün). Hier: a4:bb:6d = Dell inc.  https://macvendors.com/
 Auf der Leitung wird die MAC bei 802.3 und 802.4 LSB first übertragen,
802.5 und 802.6 wird MSB first angewandt
 Die  MAC Adresse ist an die Hardware gekoppelt – Jedes Netzwerkgeräte
(besser Netzwerkschnittstelle) hat eine individuelle, weltweit einzigartige
MAC – Hat eine Netzwerkkarte 4 Ports, so hat jeder Port eine eigene
MAC!
 In einigen Fällen, kann diese Hardware ID auch Softwareseitig geändert
werden.

### Seite 30

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
MAC
Broadcast MAC
Bei der Broadcast MAC wir die Destination Adresse (MAC) auf
ff:ff:ff:ff:ff:ff
gesetzt. Alle Netzwerkteilnehmer, die derlei Frames empfangen bilden eine
so genannt Broadcast-Domäne (vgl. Kommunikationsarten)

### Seite 31

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
MAC
Mulicast MAC
 In einigen Fällen, kann diese Hardware ID auch Softwareseitig geändert
werden. Dies geschieht u.a. wenn eine Multicast IP an die Schnittstelle
gebunden wird, dann erhält diese auch eine Multicast MAC Adresse:
Diese Abbildung ist NICHT eindeutig!
Bild:
Wikimedia

### Seite 32

Rechnernetze
Layer 3 – Vermittlung/Network
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme

### Seite 33

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Layer 3 (IP – RFC 791)
Network Layer
Date
n
Date
n
Frame Codierung
8 Bit 8 Bit 8 Bit 8 Bit
Version IHL Type of Service Total Length
Identification Flags Fragment Offset
Time to Live Protocol Header Checksum
Source Address
Destination Address
Options and Padding (optional)
Parameter Handling
Adress-Managent
Fragmentation
Handling
Checksums and
Padding
IP v4 -
Header:
Data

### Seite 34

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Layer 3 – Aufgaben
Die Hauptaufgaben der Vermittlungsschicht bestehen in der
logischen Adressierung der Kommunikationspartner und der
Wegfindung im Layer-3-Netzwerk. Darüber hinaus erfüllt die
Schicht 3 folgende Aufgaben:
 Paketieren von Daten höherer Schichten und Hinzufügen der
zur Vermittlung erforderlichen Informationen zum Paket-
Header
 Unterteilen der Daten in für den Übertragungsweg geeignete
Datenpakete
 Wiederzusammensetzen fragmentierter Datenpakete
 Aushandeln und Bereitstellen von Dienstgüten auf der
Übertragungsstrecke
 Fehlerbehandlung und Diagnose
 Zwischenspeichern von Daten
 Flusskontrolle zwischen Kommunikationspartnern und
Vermittlungssystem

### Seite 35

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Layer 3 – IP-Header I
Version
Version des IP-Protokolls (4 für IPv4 oder 6 für IPv6)
IHL (IP Header Length)
Länge des IP-Headers in 32-Bit Worten. Erlaubt eine variable
Länge des Optionsfeldes. IHL=5 -> 5 x 4Byte (43-Bit Word) = 20
Bytes.
TOS
Informationen bzgl. QoS (Qualitiy of Service), welches für das
Paket gelten soll. Hilft die Priorität und die Handhabung des
Pakets zu indizieren. Enthält Unterkategorieren (z.B.: congestion
control, deley, etc. … Details siehe Tanenbaum, et. Al.)

### Seite 36

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Layer 3 – IP-Header II
Total Length
Länge des gesamten IP Pakets, inklusive Header und Daten in
Bytes.
ID
Eindeutige Nummer des Pakets (Benötigt für die
Paketrekonstruktion nach ggf. erfolgter Fragmentierung und die
Bestimmung der korrekten Reihenfolge der Pakete
Flags
Kontrollinformationen für die Handhabung von Fragmentierung
(DF – Dont Fragment – indiziert das das Paket nicht fragmentiert
werden soll, MF – More Fragments  - indiziert, dass noch
Fragmente folgen die zu diesem Datenpaket gehören.

### Seite 37

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Layer 3 – IP-Header III
Fragment Offset
Position des Fragments im Gesamtpaket, Offset in Bytes
TTL - Time To Live
Gibt die maximale Anzahl an Hops (Router), die das Paket
passieren kann bevor es verworfen wird. -> vgl. Traceroute
Protocol
Git das Protokoll der höheren Schicht an, das für die Verarbeitung
der Daten verwendet werden soll (z.B.: TCP(6), UDP(17) oder
ICMP(1), et al.)

### Seite 38

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Layer 3 – IP-Header IV
Header Checksum
16Bit Checcksume über den gesamten IP-Header
Source und Destination Address
IPv4 Adresse der Kommunikationsparner, siehe nachfolgende
Folien

### Seite 39

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
IP v4
Adressraum: 232
https://www.subnet-calculator.com/  https://www.calculator.net/ip-subnet-calculator.html
192 . 168 . 178 . 5 / 24
192 . 168 . 178 . 5 / 255.255.255.0
8 bit . 8 bit . 8 bit . 8 bit / Netzmaske
Address: 192.168.178.5
11000000.10101000.10110010 .00000101
Netmask: 255.255.255.0 = 24    11111111.11111111.11111111
.00000000
Wildcard: 0.0.0.255             00000000.00000000.00000000
.11111111
Network: 192.168.178.0/24      11000000.10101000.10110010
.00000000 (Class C)
Broadcast: 192.168.178.255       11000000.10101000.10110010 .11111111
HostMin: 192.168.178.1
11000000.10101000.10110010 .00000001
HostMax: 192.168.178.254       11000000.10101000.10110010 .11111110
Hosts/Net: 254         (Private Internet)

### Seite 40

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
IP v4 – Besondere Netzbereiche (IANA/RIPE)
IP Netz Netzmas
ke
Verwendung Referenz
0.0.0.0 /8 Localhost RFC 5735
10.0.0.0 /8 Private networks RFC 1918
10.64.0.0 /10 GCN, CarrierGrade Nat RFC 6264,
6598
127.0.0.0 /8 Loopback RFC 1700
169.254.0.0 /16 APIPA, Zeroconf RFC 3927
172.16.0.0 /12 Private networks RFC 1918
192.0.0.0 /24 Reserviert RFC 5736
192.0.2.0, 198.51.100.0,
203.0.113.0
/24 Benutzt in Demos und
Dokumentationen
RFC 5737
192.88.99.0 /24 IPv6 über IPv4 (6to4 anycast) RFC 3068
192.168.0.0 /16 Private networks RFC 1918
192.18.0.0 /15 Testbereich für Netzkomponenten RFC 2544
224.0.0.0 /4 Multicast RFC 3171
240.0.0.0 /4 Reserviert RFC 1112
255.255.255.255 /32 Broadcast RFC 1700

### Seite 41

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Vergleich IPv4 Header vs IPv6-Header
Schöne Übersicht: https://www.ibm.com/docs/de/i/7.5.0?topic=set
up-internet-protocol-version-6

### Seite 42

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
IP v6
Adressraum: 2128
https://www.subnet-calculator.com/
Network Identifier Host Identifier
RIPE private Vergabe
200
1
: 0db
8
: 000
0
: 000
0
: 020
9
: 000
0
: 000
0
: ec1f
200
1
: 0db
8
: 0 : 0 : 020
9
: 0 : 0 : ec1f
200
1
: 0db
8
:: 020
9
: 0 : 0 : ec1f
200
1
: 0db
8
: 0 : 0 : 020
9
:: ec1fLink Loca Adressen
Network Identifier Host Identifier
fe08 :: 8bc
7
: 792
a
: a08
9
: 8b0
d
Immer fe08 Zufall oder aus MAC abgeleitet
Jedes Interface hat automatisch eine Link Local Adresse. Link Local heisst, dass
das Paket nicht von Routern weitergeleitet wird, also das lokale Lan nicht
verlassen kann.

### Seite 43

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
IP v6 – Besondere Adresstypen
Adresstyp Verwendung
Fe08::/10 Link Local
FEC0::/10 obsolete Site Local
Fc00::/7 Unique Local
2001:db8::/32 Documentation
2000::/3 Global Unicast
Ff00::/8 Multicast

### Seite 44

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Unterschiede IPv6 / IPv4 bei Fragmentierung
IPv6 IPv4
Nur der Endhost darf
fragmentieren
Jedes Gerät auf dem Weg darf
fragmentieren
Kein „Do not Fragment“ Bit im
Header
Steuerung über „Do not Fragment“
Bit
Router muss zu großes Paket
verwerfen
Router darf zu großes Paket
verwerfen
ICMPv6 Packet too big wird
versandt
ICMP Packet too big wird versandt

### Seite 45

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
IP Routing Protokolle
Routing Protokoll Beschreibung
Next Hop Routing / Statisches
Routing
manuell Die Routing-Tabelle wird manuell
auf den Geräten oder einem
zentralen Router konfiguriert
Link State Routing OSPF – RFC
2328, et al
Jeder Router kennt die vollständige
Topologie und kann selbst die
Routing Tabelle berechnen
(Dijkstra)
Distant Vector Routing RIP-
RFC2543
Router tauschen Informationen
über den besten Weg aus
Path Vector Routing BGP –
RFC4271,
2918
Verallgemeinerte Form des Distant
Vector Routings
Internet Routing Visualisation Tool:
https://folk.universitetetioslo.no/michawe/research/tools/irvtool/in
dex.html

### Seite 46

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernetze -
Praxis
L3 – Hands on
Wireshark
 Ethernet Frame
 IP-Packet
 Filtern nach MAC Adresse
 Filtern nach IP Adresse
Tipp: Darstellung als Bit und als HEX
TTL -> traceroute
MTU (Maximum Transfere Unit), Ethernet Framegrößen – ping abx –s
[framegröße]

### Seite 47

Rechnernetze
Layer 4 – Transport
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme

### Seite 48

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
ICMP – Internet Control Message Protocol – RFC 792
8 Bit 8 Bit 8 Bit 8 Bit
Type Code Checksum
Data (optional)
 Dient dem Austausch von Informations- und Fehlermeldung in IP-
Netzwerken
 ICMP benutzt IP als Basis
 ICMP-Nachrichten werden in IP-Pakete gekapselt
 Gängige Anwendungen:
Ping (Echo Request, Echo Reply)
Traceroute
diverse Router-Nachrichten (Dest unreachable, Router
Advertisements, etc.)

### Seite 49

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
IPSec – RFC 1825, 2401, 4301, et al
IPSec ist der Internet-
Sicherheitsstandards der
Internet Engineering Task Force
(IETF) für die Cyber-Sicherheit
von IP-Paketen auf der
Netzwerk-Ebene. Die
grundsätzliche Idee von IPSec
ist, eine offene, kostengünstige
und weltweit verfügbare
Kommunikationsinfrastruktur,
wie das Internet zu nutzen und
allen Bedrohungen und Risiken
möglichst sinnvoll
entgegenzuwirken.
https://www.bsi.bund.de/SharedDocs/Downloads
/DE/BSI/Publikationen/TechnischeRichtlinien/TR0
2102/BSI-TR-02102-3.pdf?__blob=publicationFile&
v=7

### Seite 50

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
IPSec – AH – Authentication Header
Der Authentication Header sorgt für die Authentizität und
Integrität der übertragenen Daten und die Authentifizierung
des Senders. Dafür wird den Paketen eine digitale Signatur
(siehe Hashfunktion) in Form eines Authentifizierungs-
Headers hinzugefügt, wodurch eine Manipulation durch
Dritte verhindert werden kann.

*... weitere 10 Seiten nicht angezeigt*
