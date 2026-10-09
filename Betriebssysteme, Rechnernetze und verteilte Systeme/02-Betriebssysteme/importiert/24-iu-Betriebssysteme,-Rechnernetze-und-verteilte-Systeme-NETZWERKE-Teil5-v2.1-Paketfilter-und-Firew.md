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
quelle: "24-iu-Betriebssysteme, Rechnernetze und verteilte Systeme-NETZWERKE-Teil5-v2.1 - Paketfilter und Firewalls.pdf"
seiten: 15
---

# Betriebssysteme, Rechnernetze und verteilte Systeme

> [!info] Dokumentinformationen
> - **Quelle:** 24-iu-Betriebssysteme, Rechnernetze und verteilte Systeme-NETZWERKE-Teil5-v2.1 - Paketfilter und Firewalls.pdf
> - **Typ:** sonstig
> - **Bereich:** BS
> - **Seiten:** 15
> - **Autor:** Andreas Hümmer

---

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
Netzwerksicherheit – Ein Einstieg
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme

### Seite 3

iu © 2023 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Firewall - Paketfilter
 Ein Paketfilter besteht aus Regeln, die
 die Richtung des Datenverkehrs
 die Adresse des Ziels
 die Adresse der Quelle
berücksichtigen.
 Für diese Regeln werden Aktionen definiert:
 Erlauben, Verbieten
 Überwachen
 DNAT, SNAT
 Statefull Paketfilter erweitern diese Funktion um eine
so genannte Zustandstabelle für jede Verbindung
geführt wird in den bereits bekannten Verbindungen
(siehe z.B. TCP) gemerkt werden. Als weitere Funktion
lassen sich damit Protokolle, die aus mehreren
Kommunikationskanälen bestehen (FTP, RPC,…)

### Seite 4

iu © 2023 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Firewall - Paketfilter
 Eine Regeltabelle hat (vereinfacht) die Form:
 Diese Tabelle wird für jedes Paket von oben nach
unten abgearbeitet
 Das Durchlaufen der Regeltabelle wird beendet,
sobald eine Regel erreicht wird, die auf das Paket
zutrifft. Diese Regel wird angewandt und die
Verarbeitung dan abgebrochen
 Die letzte Regel ist die so genannte Cach-All, in der alle
Pakete, die keiner Regel genügen gedropt oder
rejected werden
Quelle Quellport Ziel Zielport Protokoll Aktion
Quell IP 1 Any Dest IP 1 HTTP TCP Erlauben
Quell IP 2 Any Dest IP 2 DNS UDP Erlauben
Quell IP 3 Any Any/Internet HTTP TCP SNAT
Erlauben
Any/Internet Any Dest IP 3 HTTP TCP DNAT
Erlauben
Any Any Any Any Any DROP/
REJECT

### Seite 5

iu © 2023 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
NAT
Destination NAT (Port Forwarding)
 Die Adresse des Zielsystems wird umgeschrieben
 Beispiel: Zugriff auf Systeme mit privater Adresse aus
dem Internet
Source NAT (Masquerading)
 Die Adresse des verbindungssaufbauenden Systems
wird umgeschrieben
 Beispiel: RFC1918 Adressen -> Internet
Quelle Ziel Aktion Quelle Ziel
Private IP:49701 18.158.120.91:443 SNAT Externe Adresse
der
FW/Router:49701
18.158.120.91:443
Quelle Ziel Aktion Quelle Ziel
18.158.120.91:2323
4
Externe Adresse
der FW/Router:443
DNAT 18.158.120.91:2323
4
Private IP:443

### Seite 6

iu © 2023 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Hostbasierte Firewalls
 Kontrollieren das
Netzwerkinterface (TCPIP Stack)
eine Hostsystems (Desktop,
Leptop, Server, etc)
 Von Außen eingehender
Netzwerkverkehr wird
beschränkt/überwacht
 Unerwünschter ausgehender
Verkehr wird ebenfalls
beschränkt/überwacht
 Teilweise starke Integration ins
Betriebsystem

### Seite 7

iu © 2023 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Netzwerkfirewalls
• Kontrollieren und können den
Netzwerkverkehr an
Netzübergangspunkten
beschränken und
Überwachen.
• Vereinfachte Sichtweise:
Hostbasierte Firewall mit
mehreren Interfaces und
aktiviertem Routing

### Seite 8

iu © 2023 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Weiterführende Themen
• IDS – Intrusion Detection System
• IPS – Intrusion Prevention System
• NG Firewalls – Next Generation Firewalls
• XDR – Extended Detection and Response
• SIEM – Security Information and Event
Management
• SOAR – Security Orchestration Automation
and Response
• WAF – Web Application Firewall
 Statische Regelsätze -> Definitions-/Pattern
Dateien
 Dynamische Regelsätze -> Adaptive
Pattern/Machine Learning/Crowd Inteligence

### Seite 9

Rechnernetze
Zusammenfassung
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme

### Seite 10

iu © 2023 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Zusammenfassung
Rechnernetze sorgen für einen wohldefinierten
Datenaustausch und Kommunikation der
Teilnehmer. Sie bilden die Grundlage für nahezu
jedes moderne System und durchdringen
unseren gesamten Lebensalltag.

### Seite 11

iu © 2023 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Rechnernet
ze
Weiterführende Literatur (optional)
TCP/IP Illustrated Vol. 1-3
 TCP/IP Illustrated Volume 1: The Protocols (Addison-Wesley
Professional Computing, Band 1) von Kevin R. Fall
 TCP/IP Illustrated, Volume 2 (paperback): The Implementation
(Addison-Wesley Professional Computing, Band 2) von Gary R. Wright
 Tcp/Ip Illustrated: Tcp for Transactions, Http, Nntp, and the Unix
Domain Protocols (3) (Addison-wesley Professional Computing, Band
3) von W. Richard Stevens

### Seite 12

iu © 2023 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssysteme -
Praxisteil
Ein bisschen Praxis … auf der Kommandozeile
Netzwerk in Unix(Linux)
ifconfig, siehe auch ip
netstat –lnpt
route oder ip route
arp –a
Iptables -L
Netzwerk in Windows
ipconfig /all
netstat – anop tcp
route print
arp

### Seite 13

iu © 2022 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssysteme -
Praxisteil
Wireshark

### Seite 14

iu © 2022 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssysteme -
Praxisteil
GNS3

### Seite 15

iu © 2022 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssysteme -
Praxisteil
Aufgabe
Zwei Gebäude, Abstand 300m. Gefordert Gigabit
Verkabelung zwischen den Gebäuden. Welche Kabel
und Komponenten werden benötigt?
Gebäude A Gebäude B
300
m
MM: 1000SX od
SM:1000LX
CAT
7
100
m WIF
I
