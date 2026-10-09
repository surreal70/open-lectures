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
quelle: "20-iu-Betriebssysteme, Rechnernetze und verteilte Systeme-NETZWERKE-Teil1-v2.1 - Einführung und Historie.pdf"
seiten: 13
---
author: Andreas Hümmer

# Betriebssysteme, Rechnernetze und verteilte Systeme

> [!info] Dokumentinformationen
> - **Quelle:** 20-iu-Betriebssysteme, Rechnernetze und verteilte Systeme-NETZWERKE-Teil1-v2.1 - Einführung und Historie.pdf
> - **Typ:** sonstig
> - **Bereich:** BS
> - **Seiten:** 13
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
Einführung
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme

### Seite 3

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Was betrachten wir hier?
Hardware
BIOS/UEFI
Betriebssystem
Benutzersoftware
Netzwerk

### Seite 4

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
„Wat is e Netzwerk? … in det ene End vom Kabel gehen die
Daten rin und det andere kriegen mer später…*)
„… it´s complicated …“
„42“
*) frei nach „Die Feuerzangenbowle“

### Seite 5

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Verschiedene Aspekte
Kommunikationsnetzwerke sind heute allgegenwärtig,
kommen in vielen Ausprägungen vor, erfüllen verschiedenste
Zwecke, was die Beschreibung und Durchdringung nicht leicht
macht
Um diese Komplexität aufzulösen, werden wir Rechnernetze
aus verschieden Sichtweisen beleuchten. U.a. werden wir
folgendes Betrachten:
 Physische Ausprägung – Kabel/Leitungen/Medien
 Physische Datenübertragung – Codierung der Signale
 Topologieformen
 Logische Kommunikation: Aufteilung nach Layern
 Logische Kommunikation bei einigen ausgewählten
Protokollen

### Seite 6

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Dimension von Netzwerken
Bezeichnung Dimension Typische
Komponenten
CN/NOC ChipNet/Network on a Chip µm Chipintegriert oder
auf Platine, I2C, SPI
SN/CN SystemNet/ClusterNet Wenige Meter High Perfomance
Netzwerksysteme
(z.B. Infiniband)
PAN Personal Area Network Persönlicher
Wirkbereich
Bluetooth, WiFi
LAN Local Area Network Haus/Campus Switch/Router
MAN Metropolitan Area
Network
Urbaner Bereich Switch/Router
WAN Wide Area Network Region/Land Switch/Router
GAN /
Internet
Global Area Network Die Erde Switch/Router/
Satelliten
SAN Solar Area Network Das Sonnensystem Richtlaser im P2P
Betrieb, Richtfunk
VPN

### Seite 7

Rechnernetze
Ein bisschen Geschichte
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme

### Seite 8

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
A brief history… ganz am Anfang
 Sprache – Reichweite: einige Meter – Erfordert gleiche
Sprache bei den Beteiligten – Kommunikationsmatrix: 1:1,
1:n, n:n – Inhalte: Komplex
 Gesten – Reichweite: ein paar Meter mehr – Erfordert
Abstimmung darüber, was die Gesten bedeuten sollen – 1:1,
1:n - Einfach
 Trommeln oder Blasinstrumente – Reichweite: noch ein
bischen weiter – Erfordert Abstimmung was die Beat-Folgen
oder Melodien bedeuten – 1:n – Sehr einfach
 Rauchzeichen – 1:n – Ganz, ganz einfach

### Seite 9

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
A brief history… ergo…
Bedingungen und Aspekte für eine erfolgreiche
Kommunikation sind also:
 Gemeinsames Alphabet
 Reichweite
 Anzahl der Kommunikationspartner
 Bandbreite
 Informationstiefe

### Seite 10

iu © 2023 Andreas Hümmer iu INTERNATIONALE
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

### Seite 11

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
A brief history… moderne Zeiten
Art der
Kommunikati
on
Ab
ca.
Bandbreit
e
(ca.)
Reichweit
e
Signalalphabet
Optische
Telegraphie
Ende
18.
Jhd
2-4
Signale/s
mehrere
km
Codewörter über
Signalalphabet
Kabelgebunde
ne el.
Telegraphie
Mitte
19.
Jhd
2-3
Signale/s
mehrere
km*)
Morse
Funk
Telegraphie
Anfan
g 20.
Jhd
1-2
Signale/s
mehrere
km *)
Morse
Telefonie Mitte
19.
Jhd
Bis 8
Signale/s
mehrere
km *)
Sprache
*) später mehr…mehrere hundert oder gar tausende km – Bilder:
Wikimedia

### Seite 12

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
A brief history… serielle Kommunikation
 „Erste“ serielle Kommunikation
Terminals an den ersten elektronischen Rechnern
 RS-232 Standard (1964) - Spannungsschnittstelle‚ RS-485
Standard () - Stromschnittstelle
Art der
Kommunikation
Ab ca. Bandbreite
(ca.)
Reichweit
e
Signalalphab
et
Seriell Terminal to
Host
1950 Einige Baud wenige m Binärcode
RS-232
ITU V.22, V.24,
DIN66020-1, ISO
2110
1964 Längenabh.
siehe Tab.
Längenab
h.
siehe Tab
Binärcode
RS-485, ITU V.11,
X.27
1960 Max 10Mbps 1200m Binärcode

### Seite 13

iu © 2023 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
A brief history… „echte Rechnernetzwerke“
 Erstes Funk-Rechnernetz: ALOHA (1970)
Einer der Väter des Ethernet
 ARPANET (1969)
Erstes Modem
Erstes Weitverkehrsnetzwerk
Urvater des TCP/IP und des Internets
 Ethernet (1977)
XEROX „Distributed Packet Switching)
Art der
Kommunikation
Ab ca. Bandbreite
(ca.)
Reichweit
e
Standard
ALOHA 1970 9600bit/s
ARPANET 1969 X.25
Paketvermitt
elt
Ethernet 1977 1-20Mbit/s
