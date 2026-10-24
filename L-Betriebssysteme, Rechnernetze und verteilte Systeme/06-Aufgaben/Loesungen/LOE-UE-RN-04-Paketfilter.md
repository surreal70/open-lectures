---
author: Andreas Hümmer
title: Lösung - Paketfilter-Regelwerk
tags:
  - loesung
  - rn
  - sicherheit
  - firewall
  - paketfilter
created: '2026-10-24'
modified: '2026-10-24'
bereich: RN
---

# Lösung: Paketfilter-Regelwerk

> [!info] Zugehörige Übung
> [[../Uebungen/UE-RN-04-Paketfilter|→ Übung Paketfilter-Regelwerk]]

---

## Aufgabe 1: Regelwerk-Tabelle (10 Punkte)

### Musterlösung

| Nr. | Aktion | Protokoll | Quelle | Ziel | Dest-Port | NAT | Beschreibung |
|-----|--------|-----------|--------|------|-----------|-----|--------------|
| 1 | ALLOW | UDP | LAN | DNS-Server | 53 | - | DNS-Anfragen Clients → DNS-Server |
| 2 | ALLOW | TCP | LAN | DNS-Server | 53 | - | DNS über TCP (große Antworten) |
| 3 | ALLOW | UDP | DNS-Server | Internet | 53 | SNAT | DNS-Forwarding ins Internet |
| 4 | ALLOW | TCP | DNS-Server | Internet | 53 | SNAT | DNS-Forwarding TCP |
| 5 | ALLOW | TCP | LAN | Internet | 80 | SNAT | HTTP Clients → Internet |
| 6 | ALLOW | TCP | LAN | Internet | 443 | SNAT | HTTPS Clients → Internet |
| 7 | ALLOW | TCP | Internet | Webserver | 80 | DNAT | HTTP Internet → Webserver |
| 8 | ALLOW | TCP | Internet | Webserver | 443 | DNAT | HTTPS Internet → Webserver |
| 9 | ALLOW | TCP | Internet | Mailserver | 25 | DNAT | SMTP Internet → Mailserver |
| 10 | DENY | any | DMZ | LAN | any | - | **DMZ → LAN blockiert** |
| 11 | DENY | any | Internet | LAN | any | - | **Internet → LAN blockiert** |
| 12 | DENY | any | any | any | any | - | **Default Deny** |

### NAT-Erklärung

| NAT-Typ | Richtung | Funktion | Beispiel |
|---------|----------|----------|----------|
| **SNAT** | LAN/DMZ → Internet | Quell-IP wird auf 203.0.113.1 umgeschrieben | Client 192.168.1.150 → erscheint als 203.0.113.1 |
| **DNAT** | Internet → DMZ | Ziel-IP wird auf private DMZ-IP umgeschrieben | 203.0.113.10 → wird zu 192.168.10.10 |
| **-** | Intern | Kein NAT, private IPs bleiben unverändert | LAN ↔ DMZ, LAN intern |

### Bewertungshinweise

**Volle Punktzahl (10 Punkte):**
- Alle notwendigen ALLOW-Regeln vorhanden (Regeln 1-9)
- Korrekte NAT-Zuordnung (SNAT für ausgehend, DNAT für eingehend zur DMZ)
- Explizite DENY-Regeln für DMZ→LAN und Internet→LAN
- Default-Deny am Ende
- Korrekte Reihenfolge (spezifisch vor allgemein)

**Punktabzug:**
- -1 Punkt: DNS-Regeln fehlen oder unvollständig
- -1 Punkt: NAT falsch oder fehlend bei Internet-Kommunikation
- -1 Punkt: Trennung DMZ/LAN fehlt (Regel 10)
- -2 Punkte: Default-Deny fehlt
- -1 Punkt: Falsche Reihenfolge (Default-Deny nicht am Ende)

### Erklärung der Regelreihenfolge

```
Regeln 1-2:  DNS intern (LAN → DNS-Server)
Regeln 3-4:  DNS extern (DNS-Server → Internet)
Regeln 5-6:  Web-Browsing (LAN → Internet)
Regeln 7-9:  DMZ-Dienste (Internet → DMZ)
Regeln 10-11: Explizite Blockierungen
Regel 12:    Default Deny (Catch-All)
```

> [!tip] Warum diese Reihenfolge?
> - **Spezifische Regeln zuerst**: DNS-Server hat eigene Regel vor der allgemeinen LAN-Regel
> - **ALLOW vor DENY**: Erlaubte Verbindungen werden erkannt, bevor die Blockierungen greifen
> - **Default-Deny am Ende**: Alles, was nicht explizit erlaubt wurde, wird blockiert

---

## Aufgabe 2: Abarbeitungsreihenfolge (4 Punkte)

### Gegebenes Paket

```
Protokoll: TCP
Quell-IP: 192.168.1.150 (LAN-Client)
Ziel-IP: 93.184.216.34 (Internet)
Quell-Port: 52431
Ziel-Port: 443
```

### Lösung a) Prüfung gegen Regelwerk (2 Punkte)

Die Firewall prüft das Paket **sequenziell** gegen jede Regel:

| Regel | Prüfung | Ergebnis |
|-------|---------|----------|
| 1 | UDP, Port 53 → TCP, Port 443 | ❌ Passt nicht |
| 2 | TCP, Port 53 → TCP, Port 443 | ❌ Passt nicht |
| 3 | Quelle DNS-Server → Quelle LAN | ❌ Passt nicht |
| 4 | Quelle DNS-Server → Quelle LAN | ❌ Passt nicht |
| 5 | TCP, LAN→Internet, Port 80 → Port 443 | ❌ Passt nicht |
| **6** | **TCP, LAN→Internet, Port 443** | **✅ MATCH!** |

**Abbruch bei Regel 6** – nachfolgende Regeln werden nicht mehr geprüft.

### Lösung b) Ergebnis (2 Punkte)

**Regel 6 greift: ALLOW TCP LAN → Internet Port 443**

Das Paket wird **erlaubt** und an das Ziel (93.184.216.34:443) weitergeleitet.

---

## Aufgabe 3: Antwortpaket-Problem (4 Punkte)

### Lösung a) Problem beschreiben (2 Punkte)

Wenn der Client (192.168.1.150) eine HTTPS-Verbindung zu einem Webserver im Internet aufbaut:

1. **Ausgehendes Paket** (Client → Server):
   - Quell-IP: 192.168.1.150, Quell-Port: 52431
   - Ziel-IP: 93.184.216.34, Ziel-Port: 443
   - → **Wird durch Regel 6 erlaubt** ✅

2. **Antwortpaket** (Server → Client):
   - Quell-IP: 93.184.216.34, **Quell-Port: 443**
   - Ziel-IP: 192.168.1.150, Ziel-Port: 52431
   - → **Wird durch Regel 11 blockiert!** ❌
   
   (Internet → LAN ist verboten)

**Problem**: Die Antwort des Webservers kommt nicht beim Client an, obwohl die ursprüngliche Anfrage erlaubt wurde.

### Lösung b) Zusätzliche Regel und Risiko (2 Punkte)

**Zusätzliche Regel für Stateless-Filter:**

| Nr. | Aktion | Protokoll | Quelle | Ziel | Src-Port | Beschreibung |
|-----|--------|-----------|--------|------|----------|--------------|
| ? | ALLOW | TCP | Internet | LAN | 80, 443 | Antworten von Webservern |

Diese Regel müsste **vor** Regel 11 eingefügt werden.

**Sicherheitsrisiko:**

> [!danger] Erhebliches Sicherheitsrisiko!
> Ein Angreifer könnte Pakete mit **gefälschtem Quell-Port 443** senden:
> ```
> Angreifer sendet:
> Quell-IP: Angreifer-IP
> Quell-Port: 443 (gefälscht!)
> Ziel-IP: 192.168.1.150
> Ziel-Port: beliebig
> ```
> Diese Pakete würden durch die Regel erlaubt, obwohl keine legitime Verbindung besteht.

---

## Aufgabe 4: Stateful vs. Stateless (2 Punkte)

### Musterlösung

Eine **Stateful Firewall** führt eine **Connection State Table**, die alle aktiven Verbindungen verfolgt. Wenn ein Client eine ausgehende Verbindung aufbaut, wird diese in der State Table als "ESTABLISHED" markiert. Eingehende Pakete werden automatisch erlaubt, wenn sie zu einer bekannten, aktiven Verbindung gehören – ohne explizite Regel für Antwortpakete.

**Vorteile:**
- Keine Regel für Antwortpakete nötig
- Kein Risiko durch gefälschte Quell-Ports
- Einfachere Konfiguration

**Beispiel-Eintrag in State Table:**

```
Proto  Source              Destination         State
TCP    192.168.1.150:52431 93.184.216.34:443   ESTABLISHED
```

Antwortpakete von 93.184.216.34:443 an 192.168.1.150:52431 werden automatisch als "gehört zu bestehender Verbindung" erkannt und erlaubt.

---

## Erweiterung: iptables-Umsetzung (Bonus)

Für fortgeschrittene Studierende: So würde das Regelwerk mit Linux iptables aussehen:

```bash
#!/bin/bash
# Paketfilter für LAN/DMZ/Internet Szenario mit NAT

# Variablen
LAN="192.168.1.0/24"
DMZ="192.168.10.0/24"
DNS_SERVER="192.168.1.10"
WEBSERVER="192.168.10.10"
MAILSERVER="192.168.10.20"
PUBLIC_IP="203.0.113.1"
PUBLIC_WEB="203.0.113.10"
PUBLIC_MAIL="203.0.113.20"
WAN_IF="eth0"

# Alle Regeln löschen
iptables -F
iptables -X
iptables -t nat -F

# Default Policy: DROP (Default-Deny)
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# Connection Tracking (macht es zur Stateful Firewall!)
iptables -A FORWARD -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# ============================================
# NAT-Regeln (in der nat-Tabelle)
# ============================================

# SNAT: LAN/DMZ → Internet (Masquerading)
iptables -t nat -A POSTROUTING -s $LAN -o $WAN_IF -j MASQUERADE
iptables -t nat -A POSTROUTING -s $DMZ -o $WAN_IF -j MASQUERADE

# DNAT: Internet → Webserver (Port-Forwarding)
iptables -t nat -A PREROUTING -d $PUBLIC_WEB -p tcp --dport 80 -j DNAT --to-destination $WEBSERVER
iptables -t nat -A PREROUTING -d $PUBLIC_WEB -p tcp --dport 443 -j DNAT --to-destination $WEBSERVER

# DNAT: Internet → Mailserver
iptables -t nat -A PREROUTING -d $PUBLIC_MAIL -p tcp --dport 25 -j DNAT --to-destination $MAILSERVER

# ============================================
# Filter-Regeln (in der filter-Tabelle)
# ============================================

# DNS: LAN → DNS-Server (intern, kein NAT)
iptables -A FORWARD -s $LAN -d $DNS_SERVER -p udp --dport 53 -j ACCEPT
iptables -A FORWARD -s $LAN -d $DNS_SERVER -p tcp --dport 53 -j ACCEPT

# DNS: DNS-Server → Internet (Forwarding, wird per SNAT maskiert)
iptables -A FORWARD -s $DNS_SERVER -p udp --dport 53 -j ACCEPT
iptables -A FORWARD -s $DNS_SERVER -p tcp --dport 53 -j ACCEPT

# Web: LAN → Internet (wird per SNAT maskiert)
iptables -A FORWARD -s $LAN -p tcp --dport 80 -j ACCEPT
iptables -A FORWARD -s $LAN -p tcp --dport 443 -j ACCEPT

# DMZ: Internet → Webserver (nach DNAT-Umsetzung!)
iptables -A FORWARD -d $WEBSERVER -p tcp --dport 80 -j ACCEPT
iptables -A FORWARD -d $WEBSERVER -p tcp --dport 443 -j ACCEPT

# DMZ: Internet → Mailserver (nach DNAT-Umsetzung!)
iptables -A FORWARD -d $MAILSERVER -p tcp --dport 25 -j ACCEPT

# Explizit: DMZ → LAN blockieren
iptables -A FORWARD -s $DMZ -d $LAN -j DROP

# Logging für verworfene Pakete
iptables -A FORWARD -j LOG --log-prefix "FW-DROP: "

echo "Firewall mit NAT aktiviert."
```

> [!info] NAT-Verarbeitung in iptables
> Die Reihenfolge der Verarbeitung ist wichtig:
> 1. **PREROUTING** (DNAT): Ziel-IP wird umgeschrieben, *bevor* die Filter-Regeln greifen
> 2. **FORWARD** (Filter): Entscheidung ALLOW/DENY basierend auf der *umgeschriebenen* Adresse
> 3. **POSTROUTING** (SNAT): Quell-IP wird umgeschrieben, *nachdem* die Filter-Regeln erlaubt haben
>
> Daher prüft `iptables -A FORWARD -d $WEBSERVER` die *private* IP 192.168.10.10, obwohl das Paket ursprünglich an 203.0.113.10 adressiert war.

---

## Zusammenfassung der Lernziele

| Lernziel | Aufgabe | Kernkonzept |
|----------|---------|-------------|
| Regelwerk erstellen | 1 | Strukturierte Tabelle mit Aktion, Protokoll, Quelle, Ziel, Port |
| First-Match-Wins | 2 | Sequenzielle Abarbeitung, erste passende Regel entscheidet |
| Stateless-Limitierung | 3 | Antwortpakete müssen explizit erlaubt werden |
| Stateful-Vorteil | 4 | Connection Tracking löst das Antwortpaket-Problem |

---

## Weiterführende Themen

- [[../../03-Rechnernetze/05-Sicherheit/01-Firewalls|Firewalls]] – Theorie zu Paketfilter, Stateful, NGFW
- [[../../03-Rechnernetze/05-Sicherheit/03-TLS|TLS]] – Warum HTTPS wichtig ist
- [[../../03-Rechnernetze/05-Sicherheit/00-Sicherheit-Index|Sicherheit]] – Übersicht Netzwerksicherheit
