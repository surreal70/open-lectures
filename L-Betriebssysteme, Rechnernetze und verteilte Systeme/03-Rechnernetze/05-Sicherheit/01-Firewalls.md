---
author: Andreas Hümmer
title: Firewalls
tags:
  - content
  - rn
  - sicherheit
  - firewall
  - paketfilter
created: '2026-10-07'
modified: '2026-10-24'
bereich: RN
---

# Firewalls

> [!info] Lernziele
> - Verstehen der Grundfunktion und Einsatzzwecke von Firewalls
> - Unterscheiden zwischen Paketfilter, Stateful Inspection und Application-Level-Gateway
> - Kennenlernen typischer Firewall-Regeln und Regelaufbau
> - Verstehen von Default-Deny vs. Default-Allow Konzepten
> - Wissen über Firewall-Positionierung im Netzwerk

## Definition

> [!quote] Definition
> Eine **Firewall** ist ein Netzwerksicherheitssystem, das den ein- und ausgehenden Datenverkehr anhand definierter Regeln überwacht, filtert und kontrolliert.

## Erklärung

Firewalls bilden eine Sicherheitsbarriere zwischen vertrauenswürdigen (z.B. LAN) und nicht vertrauenswürdigen Netzwerken (z.B. Internet). Sie arbeiten auf verschiedenen OSI-Schichten und haben sich von einfachen Paketfiltern zu komplexen Next-Generation Firewalls entwickelt.

### Evolution der Firewall-Technologien

| Generation | Technologie | OSI-Schicht | Einführung |
|------------|-------------|-------------|------------|
| **1. Generation** | Paketfilter | 3-4 | ~1988 |
| **2. Generation** | Stateful Inspection | 3-4 | ~1994 |
| **3. Generation** | Application Gateway | 7 | ~1990er |
| **4. Generation** | Next-Generation FW | 3-7 | ~2009 |

## Eigenschaften

| Eigenschaft | Beschreibung |
|-------------|--------------|
| **Regelbasiert** | Entscheidungen basieren auf konfigurierten Regeln |
| **Positionierung** | Zwischen Netzwerkzonen (Perimeter, intern) |
| **Default Policy** | Default-Deny (Whitelist) oder Default-Allow (Blacklist) |
| **Logging** | Protokollierung erlaubter/blockierter Verbindungen |

## Firewall-Positionierung

### Typische Netzwerktopologie

![[firewall-topology.png]]
*<span class="fig-id">05-01-firewall-topology</span>: Firewall-Positionierung mit DMZ – Perimeter- und interne Firewall schützen verschiedene Zonen.*

### DMZ (Demilitarized Zone)

Die DMZ ist ein isoliertes Netzwerksegment für öffentlich erreichbare Dienste:

- **Zweck**: Kompromittierte Server gefährden nicht das interne Netz
- **Typische Dienste**: Webserver, Mailserver, DNS
- **Regelbeispiel**: Internet → DMZ erlaubt, DMZ → LAN verboten

---

## 1. Paketfilter (Stateless)

### Funktionsweise

Paketfilter analysieren jedes Paket **isoliert** anhand von Header-Informationen:

- Quell- und Ziel-IP-Adresse (Schicht 3)
- Quell- und Ziel-Port (Schicht 4)
- Protokoll (TCP, UDP, ICMP)
- Interface (eingehend/ausgehend)

> [!warning] Einschränkung
> Paketfilter kennen keinen Verbindungskontext. Jedes Paket wird unabhängig bewertet.

### Regelaufbau

```
[Nummer] [Aktion] [Protokoll] [Quelle] [Ziel] [Port] [Optionen]
```

### Vereinfachtes Regelwerk (Beispiel)

| Nr. | Aktion | Protokoll | Quelle | Ziel | Dest-Port | Beschreibung |
|-----|--------|-----------|--------|------|-----------|--------------|
| 1 | ALLOW | TCP | any | Server | 22 | SSH erlauben |
| 2 | ALLOW | TCP | any | Server | 80, 443 | Web erlauben |
| 3 | ALLOW | ICMP | any | Server | - | Ping erlauben |
| 4 | DENY | TCP | any | Server | 3389 | RDP blockieren |
| 5 | DENY | any | any | any | any | **Default Deny** |

### Abarbeitungsreihenfolge (First Match Wins)

> [!important] Reihenfolge ist entscheidend!
> Firewall-Regeln werden **von oben nach unten** abgearbeitet. Die **erste passende Regel** entscheidet – nachfolgende Regeln werden ignoriert.

**Beispiel der Auswertung:**

```
Eingehendes Paket: TCP, Quelle: 203.0.113.50, Ziel: Server:443

Regel 1: SSH (Port 22) → passt nicht → weiter
Regel 2: Web (Port 80, 443) → PASST! → ALLOW → ENDE

Ergebnis: Paket erlaubt (Regel 2)
```

**Häufiger Fehler – falsche Reihenfolge:**

| Nr. | Aktion | Protokoll | Quelle | Ziel | Port | Problem |
|-----|--------|-----------|--------|------|------|---------|
| 1 | DENY | any | any | any | any | ⚠️ Blockiert ALLES! |
| 2 | ALLOW | TCP | any | Server | 22 | ❌ Wird nie erreicht |
| 3 | ALLOW | TCP | any | Server | 443 | ❌ Wird nie erreicht |

> [!tip] Best Practice
> - Spezifische Regeln **vor** allgemeinen Regeln
> - DENY-Regeln für bekannte Bedrohungen **vor** ALLOW-Regeln
> - Default-Deny-Regel **immer am Ende**

### Beispiel: Linux iptables (Legacy)

```bash
# Default Policy: Alles verbieten
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# Loopback erlauben
iptables -A INPUT -i lo -j ACCEPT

# SSH von überall erlauben
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# HTTP/HTTPS erlauben
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# ICMP (Ping) erlauben
iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT

# Etablierte Verbindungen erlauben (pseudo-stateful)
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
```

### Beispiel: Linux nftables (Modern)

```bash
#!/usr/sbin/nft -f

table inet filter {
    chain input {
        type filter hook input priority 0; policy drop;
        
        # Loopback
        iif lo accept
        
        # Established connections
        ct state established,related accept
        
        # SSH
        tcp dport 22 accept
        
        # Web
        tcp dport { 80, 443 } accept
        
        # ICMP
        icmp type echo-request accept
        icmpv6 type echo-request accept
    }
    
    chain forward {
        type filter hook forward priority 0; policy drop;
    }
    
    chain output {
        type filter hook output priority 0; policy accept;
    }
}
```

### Beispiel: Windows Firewall (netsh)

```cmd
REM Eingehend: RDP nur aus internem Netz
netsh advfirewall firewall add rule name="RDP intern" ^
    dir=in action=allow protocol=tcp localport=3389 ^
    remoteip=192.168.1.0/24

REM Eingehend: HTTP/HTTPS für alle
netsh advfirewall firewall add rule name="Webserver" ^
    dir=in action=allow protocol=tcp localport=80,443

REM Ausgehend: DNS erlauben
netsh advfirewall firewall add rule name="DNS out" ^
    dir=out action=allow protocol=udp remoteport=53
```

### Vor- und Nachteile Paketfilter

| Vorteile | Nachteile |
|----------|-----------|
| ✓ Schnell (wenig Overhead) | ✗ Kein Verbindungskontext |
| ✓ Einfach zu verstehen | ✗ Keine Anwendungserkennung |
| ✓ Transparent für Anwendungen | ✗ Anfällig für IP-Spoofing |
| ✓ Kernel-Level (effizient) | ✗ Komplexe Regeln für Antwortpakete |

### Problem: Antwortpakete

Bei reinen Paketfiltern muss man Antwortpakete explizit erlauben:

```bash
# Ohne Stateful: Explizite Regel für Rückverkehr nötig
iptables -A INPUT -p tcp --sport 80 -j ACCEPT  # Unsicher!

# Problem: Angreifer kann Pakete mit sport 80 senden
```

---

## 2. Stateful Inspection (Stateful Firewall)

### Funktionsweise

Stateful Firewalls führen eine **Verbindungstabelle** (State Table), die den Status jeder Verbindung verfolgt:

| Feld | Beschreibung |
|------|--------------|
| **Source IP/Port** | Absender der Verbindung |
| **Dest IP/Port** | Ziel der Verbindung |
| **Protocol** | TCP, UDP, ICMP |
| **State** | NEW, ESTABLISHED, RELATED, INVALID |
| **Timeout** | Ablaufzeit des Eintrags |

### Verbindungsstatus (Connection Tracking)

| Status | Bedeutung |
|--------|-----------|
| **NEW** | Erstes Paket einer neuen Verbindung |
| **ESTABLISHED** | Antwort auf NEW empfangen, Verbindung aktiv |
| **RELATED** | Neue Verbindung, die zu bestehender gehört (z.B. FTP-Data) |
| **INVALID** | Paket gehört zu keiner bekannten Verbindung |

### Beispiel: TCP-Verbindung in State Table

![[state-table.png]]
*<span class="fig-id">05-01-state-table</span>: Connection State Table einer Stateful Firewall – verfolgt alle aktiven Verbindungen mit Status und Timeout.*

### Beispiel: Stateful iptables-Konfiguration

```bash
# Default Policy
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT DROP

# Loopback
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT

# Connection Tracking - der Schlüssel zu Stateful!
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
iptables -A OUTPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Ungültige Pakete verwerfen
iptables -A INPUT -m conntrack --ctstate INVALID -j DROP

# Neue ausgehende Verbindungen erlauben
iptables -A OUTPUT -m conntrack --ctstate NEW -j ACCEPT

# Eingehend: Nur spezifische neue Verbindungen
iptables -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -m conntrack --ctstate NEW -j ACCEPT
```

### Beispiel: nftables mit Connection Tracking

```bash
table inet filter {
    chain input {
        type filter hook input priority 0; policy drop;
        
        # Connection Tracking
        ct state invalid drop
        ct state established,related accept
        
        # Neue Verbindungen
        tcp dport 22 ct state new accept
        tcp dport 443 ct state new accept
    }
    
    chain output {
        type filter hook output priority 0; policy drop;
        
        ct state established,related accept
        ct state new accept
    }
}
```

### Beispiel: pfSense/OPNsense Regel

```
Action: Pass
Interface: WAN
Protocol: TCP
Source: any
Destination: WAN address
Dest Port: 443
State Type: keep state    ← Stateful!
Description: HTTPS to Webserver
```

### FTP und RELATED-Verbindungen

FTP nutzt zwei Verbindungen: Control (21) und Data (20 oder dynamisch):

```bash
# FTP-Modul laden (für RELATED-Tracking)
modprobe nf_conntrack_ftp

# FTP Control erlauben
iptables -A INPUT -p tcp --dport 21 -m conntrack --ctstate NEW -j ACCEPT

# FTP Data wird automatisch als RELATED erkannt
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
```

### Vor- und Nachteile Stateful Firewall

| Vorteile | Nachteile |
|----------|-----------|
| ✓ Einfachere Regeln | ✗ Speicherverbrauch (State Table) |
| ✓ Antwortpakete automatisch erlaubt | ✗ DoS gegen State Table möglich |
| ✓ Besserer Schutz gegen Spoofing | ✗ Keine Anwendungserkennung |
| ✓ RELATED für komplexe Protokolle | ✗ Verschlüsselter Traffic opak |

---

## 3. Application-Level Gateway (ALG/Proxy)

### Funktionsweise

Application-Level Gateways arbeiten auf **Schicht 7** und verstehen Anwendungsprotokolle:

- Terminiert Verbindungen (Client ↔ Proxy ↔ Server)
- Analysiert Protokollinhalte (HTTP-Header, SQL-Queries, etc.)
- Kann Inhalte modifizieren oder filtern

### Beispiel: HTTP-Proxy-Regeln

```
# Squid Proxy ACLs
acl blocklist dstdomain .facebook.com .tiktok.com
acl malware url_regex -i \.exe$ \.bat$ \.scr$
acl worktime time MTWHF 08:00-18:00

http_access deny blocklist
http_access deny malware
http_access allow worktime
http_access deny all
```

### Vor- und Nachteile ALG

| Vorteile | Nachteile |
|----------|-----------|
| ✓ Tiefe Paketinspektion | ✗ Hohe Latenz |
| ✓ Protokollvalidierung | ✗ Jedes Protokoll braucht eigenen Proxy |
| ✓ Caching möglich | ✗ Skaliert schlecht |
| ✓ Benutzer-Authentifizierung | ✗ Ende-zu-Ende-Verschlüsselung bricht |

---

## 4. Next-Generation Firewall (NGFW)

### Definition

> [!quote] NGFW
> Next-Generation Firewalls kombinieren traditionelle Firewall-Funktionen mit erweiterten Sicherheitsfunktionen wie Deep Packet Inspection, IPS und Application Awareness.

### Kernfunktionen

| Funktion | Beschreibung |
|----------|--------------|
| **Stateful Inspection** | Basis-Firewall-Funktionalität |
| **Application Awareness** | Erkennung von Anwendungen unabhängig von Port |
| **Deep Packet Inspection** | Analyse des Paketinhalts |
| **Intrusion Prevention (IPS)** | Erkennung und Blockierung von Angriffen |
| **TLS Inspection** | Aufbrechen verschlüsselter Verbindungen |
| **User Identity** | Regeln basierend auf Benutzer, nicht nur IP |
| **Threat Intelligence** | Integration von Bedrohungsdatenbanken |
| **URL Filtering** | Kategoriebasierte Webfilterung |
| **Sandboxing** | Analyse verdächtiger Dateien in Isolation |

### Application Awareness

NGFWs erkennen Anwendungen anhand von Signaturen, nicht nur Ports:

```
# Traditionelle Firewall
ALLOW tcp/443    → Erlaubt HTTPS, aber auch:
                    - HTTPS-VPNs
                    - Tunneling über HTTPS
                    - Malware-C2 über HTTPS

# NGFW mit Application Awareness
ALLOW app=web-browsing
ALLOW app=ssl
DENY  app=tunnel
DENY  app=unknown-tcp
```

### Beispiel: Palo Alto Networks NGFW-Regel

```
Rule: Allow Office 365
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Source Zone:        Trust
Source User:        domain\employees
Destination Zone:   Untrust
Application:        ms-office365-base
                    ms-teams
                    ms-sharepoint-online
Service:            application-default
Action:             Allow
Profile:            antivirus=default
                    vulnerability=strict
                    url-filtering=corporate
Logging:            At session end
```

### Beispiel: Fortinet FortiGate Policy

```
config firewall policy
    edit 1
        set name "Allow-Web-Users"
        set srcintf "internal"
        set dstintf "wan1"
        set srcaddr "User-Group-Employees"
        set dstaddr "all"
        set action accept
        set schedule "business-hours"
        set service "HTTP" "HTTPS"
        set application "Facebook" "YouTube" "Twitter"
        set application-action deny
        set utm-status enable
        set av-profile "av-strict"
        set webfilter-profile "corporate"
        set ips-sensor "high-security"
        set ssl-ssh-profile "deep-inspection"
        set logtraffic all
    next
end
```

### TLS/SSL Inspection (HTTPS-Aufbrechen)

```
Client ←──TLS──→ NGFW ←──TLS──→ Server
                  │
              Entschlüsselt,
              inspiziert,
              neu verschlüsselt
```

**Voraussetzungen:**
- NGFW-CA-Zertifikat auf Clients verteilt
- Datenschutz-/Compliance-Überlegungen
- Ausnahmen für Banking, Healthcare, etc.

### IPS-Signaturen

```
# Beispiel: SQL Injection Detection
alert tcp any any -> any 80 (
    msg:"SQL Injection Attempt";
    flow:to_server,established;
    content:"SELECT"; nocase;
    content:"FROM"; nocase;
    content:"WHERE"; nocase;
    pcre:"/(\%27)|(\')|(\-\-)|(\%23)|(#)/i";
    sid:100001;
    rev:1;
)
```

### NGFW vs. Traditionelle Firewall

| Merkmal | Paketfilter | Stateful | NGFW |
|---------|-------------|----------|------|
| **OSI-Schicht** | 3-4 | 3-4 | 3-7 |
| **Port-basiert** | ✓ | ✓ | ✓ |
| **Connection Tracking** | ✗ | ✓ | ✓ |
| **App-Erkennung** | ✗ | ✗ | ✓ |
| **User-Identität** | ✗ | ✗ | ✓ |
| **IPS** | ✗ | ✗ | ✓ |
| **TLS Inspection** | ✗ | ✗ | ✓ |
| **URL-Kategorien** | ✗ | ✗ | ✓ |
| **Performance** | Hoch | Hoch | Mittel |
| **Komplexität** | Niedrig | Mittel | Hoch |

---

## Default-Deny vs. Default-Allow

### Default-Deny (Whitelist)

```bash
# Alles verbieten, explizit erlauben
iptables -P INPUT DROP
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT
# Alles andere wird gedroppt
```

**Prinzip**: Was nicht explizit erlaubt ist, ist verboten.
**Empfohlen für**: Eingehenden Traffic, Server

### Default-Allow (Blacklist)

```bash
# Alles erlauben, explizit verbieten
iptables -P INPUT ACCEPT
iptables -A INPUT -p tcp --dport 23 -j DROP   # Telnet
iptables -A INPUT -s 10.0.0.0/8 -j DROP       # Private IPs von außen
# Alles andere wird erlaubt
```

**Prinzip**: Was nicht explizit verboten ist, ist erlaubt.
**Risiko**: Unbekannte Bedrohungen passieren

> [!tip] Best Practice
> **Default-Deny** ist das empfohlene Sicherheitsprinzip. Starte mit allem blockiert und öffne nur das Nötige.

---

## Beispiele

### Komplettes iptables-Skript für Webserver

```bash
#!/bin/bash
# Firewall-Skript für Webserver

# Alle Regeln löschen
iptables -F
iptables -X
iptables -t nat -F

# Default Policy: DROP
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT DROP

# Loopback erlauben
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT

# Connection Tracking
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
iptables -A OUTPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
iptables -A INPUT -m conntrack --ctstate INVALID -j DROP

# Anti-Spoofing
iptables -A INPUT -s 127.0.0.0/8 ! -i lo -j DROP
iptables -A INPUT -s 0.0.0.0/8 -j DROP
iptables -A INPUT -s 224.0.0.0/4 -j DROP
iptables -A INPUT -s 240.0.0.0/5 -j DROP

# Rate Limiting für SSH (Brute-Force-Schutz)
iptables -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW \
    -m recent --set --name SSH
iptables -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW \
    -m recent --update --seconds 60 --hitcount 4 --name SSH -j DROP
iptables -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW -j ACCEPT

# Webserver
iptables -A INPUT -p tcp --dport 80 -m conntrack --ctstate NEW -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -m conntrack --ctstate NEW -j ACCEPT

# ICMP (Ping) mit Rate Limit
iptables -A INPUT -p icmp --icmp-type echo-request -m limit \
    --limit 1/second --limit-burst 4 -j ACCEPT

# Ausgehend: DNS, HTTP, HTTPS, NTP
iptables -A OUTPUT -p udp --dport 53 -m conntrack --ctstate NEW -j ACCEPT
iptables -A OUTPUT -p tcp --dport 80 -m conntrack --ctstate NEW -j ACCEPT
iptables -A OUTPUT -p tcp --dport 443 -m conntrack --ctstate NEW -j ACCEPT
iptables -A OUTPUT -p udp --dport 123 -m conntrack --ctstate NEW -j ACCEPT

# Logging für gedroppte Pakete
iptables -A INPUT -j LOG --log-prefix "FW-DROP-IN: " --log-level 4
iptables -A OUTPUT -j LOG --log-prefix "FW-DROP-OUT: " --log-level 4

echo "Firewall aktiviert."
```

### Windows Firewall via PowerShell

```powershell
# Alle eingehenden Verbindungen blockieren
Set-NetFirewallProfile -Profile Domain,Public,Private -DefaultInboundAction Block
Set-NetFirewallProfile -Profile Domain,Public,Private -DefaultOutboundAction Allow

# RDP nur aus internem Netz
New-NetFirewallRule -DisplayName "RDP Internal" `
    -Direction Inbound -Action Allow `
    -Protocol TCP -LocalPort 3389 `
    -RemoteAddress 192.168.0.0/16

# Webserver-Ports
New-NetFirewallRule -DisplayName "HTTP" `
    -Direction Inbound -Action Allow `
    -Protocol TCP -LocalPort 80

New-NetFirewallRule -DisplayName "HTTPS" `
    -Direction Inbound -Action Allow `
    -Protocol TCP -LocalPort 443

# Ping erlauben
New-NetFirewallRule -DisplayName "ICMP Allow" `
    -Direction Inbound -Action Allow `
    -Protocol ICMPv4 -IcmpType 8
```

## Prüfungsrelevanz

> [!warning] **Prüfungsrelevant**
> - Evolution: Paketfilter → Stateful Inspection → NGFW
> - Paketfilter: Filterung auf Schicht 3/4 (IP, Port)
> - Stateful Inspection: Connection Tracking, State Table
> - NGFW: Deep Packet Inspection, Application Awareness
> - Verbindungszustände: NEW, ESTABLISHED, RELATED
> - Default Deny vs. Default Allow
> - DMZ-Konzept

---

## Prüfungstipps

> [!warning] Häufige Klausurfehler
> - Verwechslung von Paketfilter und Stateful Firewall
> - Annahme, dass NGFWs nur auf Schicht 7 arbeiten – sie kombinieren alle Schichten
> - Vergessen, dass Stateful Firewalls eine State Table führen
> - Default-Allow mit Default-Deny verwechseln

> [!question] Typische Prüfungsfragen
> - Was ist der Unterschied zwischen Paketfilter und Stateful Inspection?
> - Erklären Sie die Verbindungszustände NEW, ESTABLISHED und RELATED
> - Was bedeutet "Default Deny" und warum wird es empfohlen?
> - Welche zusätzlichen Funktionen bietet eine NGFW gegenüber einer Stateful Firewall?
> - Warum ist TLS Inspection bei NGFWs kontrovers?
> - Was ist eine DMZ und welchen Zweck erfüllt sie?

> [!tip] Prüfungsvorbereitung
> - Verstehe die **Evolution**: Paketfilter → Stateful → ALG → NGFW
> - Kenne die **OSI-Schichten** jeder Technologie
> - Merke: Stateful = Connection Tracking, NGFW = Application Awareness
> - Lerne ein einfaches iptables/nftables-Beispiel auswendig

---

## Weiterführende Ressourcen

- [Netfilter/iptables Dokumentation](https://netfilter.org/documentation/) – Offizielle Linux-Firewall-Docs
- [nftables Wiki](https://wiki.nftables.org/) – Moderne Linux-Firewall
- [pfSense Dokumentation](https://docs.netgate.com/pfsense/en/latest/) – Open-Source-Firewall
- [NIST SP 800-41: Firewall Guidelines](https://csrc.nist.gov/publications/detail/sp/800-41/rev-1/final) – Best Practices

---

## Zusammenhänge

- [[00-Sicherheit-Index]] – Sicherheit Übersicht
- [[02-VPN/01-IPsec]] – IPsec wird oft auf Firewalls terminiert
- [[03-TLS]] – TLS Inspection bei NGFWs
- [[../03-Referenzmodelle/01-OSI-Modell]] – Schichten und Firewall-Typen
- [[../02-Standards-und-Gremien/03-Ports]] – Port-basierte Filterung

---

## Quellen

- Cheswick, W., Bellovin, S., Rubin, A.: "Firewalls and Internet Security"
- NIST SP 800-41 Rev. 1: Guidelines on Firewalls and Firewall Policy
- RFC 2979: Behavior of and Requirements for Internet Firewalls
- https://netfilter.org/
- https://www.paloaltonetworks.com/
- https://www.fortinet.com/
