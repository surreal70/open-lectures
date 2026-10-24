---
author: Andreas Hümmer
title: 'Praxisübung: Netzwerkanalyse mit Shell-Kommandos'
tags:
  - uebung
  - praxis
  - rn
  - netzwerk
  - shell
  - linux
  - windows
  - diagnose
bereich: RN
created: '2026-10-24'
modified: '2026-10-24'
---

# Praxisübung: Netzwerkanalyse mit Shell-Kommandos

**Bereich:** RN – Rechnernetze und Netzwerkdiagnose
**Voraussetzungen:** Terminal/Shell-Zugang (Linux oder Windows), Netzwerkverbindung

---

> [!info] **Lernziele**
> Nach dieser Übung solltest du:
> - Netzwerkkonfiguration anzeigen und verstehen können
> - Konnektivität mit ping und traceroute testen können
> - DNS-Abfragen durchführen und analysieren können
> - Offene Ports und aktive Verbindungen untersuchen können
> - Netzwerkverkehr mit tcpdump/Wireshark erfassen können
> - Firewall-Regeln anzeigen und verstehen können

---

## Vorbereitung

### Linux

Öffne ein Terminal. Einige Kommandos benötigen Root-Rechte (`sudo`).

Installiere ggf. fehlende Tools:
```bash
# Debian/Ubuntu
sudo apt install net-tools dnsutils traceroute tcpdump nmap

# RHEL/CentOS/Fedora
sudo dnf install net-tools bind-utils traceroute tcpdump nmap
```

### Windows

Öffne **PowerShell** oder **cmd.exe** (als Administrator für manche Aufgaben).

> [!tip] **WSL-Nutzer**
> Für Linux-Kommandos kannst du WSL verwenden. Netzwerk-Tools greifen dann auf die WSL-Netzwerkkonfiguration zu.

---

## Teil 1: Netzwerkkonfiguration anzeigen

### Aufgabe 1.1: IP-Konfiguration (Linux)

**Führe folgende Kommandos aus und dokumentiere die Ergebnisse:**

```bash
# 1. Alle Interfaces mit IP-Adressen (modern)
ip addr show

# 2. Nur IPv4-Adressen
ip -4 addr show

# 3. Kurze Übersicht
ip -br addr

# 4. Routing-Tabelle anzeigen
ip route show

# 5. Default-Gateway ermitteln
ip route | grep default

# 6. DNS-Konfiguration
cat /etc/resolv.conf
```

**Fragen:**

a) Wie lautet deine IPv4-Adresse und Subnetzmaske?

_IP:_ __________________ _Maske:_ __________________

b) Wie lautet dein Default-Gateway?

_Gateway:_ __________________

c) Welche DNS-Server sind konfiguriert?

_DNS:_ __________________

---

### Aufgabe 1.2: IP-Konfiguration (Windows)

```powershell
# 1. Alle Netzwerkadapter
Get-NetIPAddress | Format-Table InterfaceAlias, IPAddress, PrefixLength

# 2. Detaillierte Konfiguration
Get-NetIPConfiguration

# 3. DNS-Server anzeigen
Get-DnsClientServerAddress

# 4. Routing-Tabelle
Get-NetRoute | Where-Object {$_.DestinationPrefix -eq "0.0.0.0/0"}

# 5. Klassisch (cmd)
ipconfig /all
```

**Oder mit cmd.exe:**
```cmd
ipconfig /all
route print
```

---

### Aufgabe 1.3: MAC-Adressen und ARP (Linux)

```bash
# 1. MAC-Adressen der eigenen Interfaces
ip link show

# 2. ARP-Cache anzeigen (bekannte MAC-Adressen im Netzwerk)
ip neigh show

# 3. Oder klassisch
arp -a

# 4. MAC-Adresse eines Hosts im LAN ermitteln
ping -c 1 192.168.1.1   # Zuerst anpingen
ip neigh show | grep 192.168.1.1
```

**Frage:** Welche MAC-Adresse hat dein Default-Gateway?

_MAC:_ __________________

---

## Teil 2: Konnektivitätstests

### Aufgabe 2.1: Ping (Linux & Windows)

```bash
# 1. Einfacher Ping
ping -c 4 8.8.8.8

# 2. Ping mit Statistik (10 Pakete)
ping -c 10 google.com

# 3. Ping mit Zeitstempel
ping -D -c 4 google.com

# 4. Ping mit bestimmter Paketgröße
ping -c 4 -s 1400 google.com

# 5. Ping an Broadcast (wer ist im Netz?)
ping -b -c 3 192.168.1.255  # Funktioniert oft nicht mehr
```

**Windows:**
```cmd
ping -n 4 8.8.8.8
ping -n 10 google.com
```

**Analyse der Ping-Ausgabe:**
```
64 bytes from 8.8.8.8: icmp_seq=1 ttl=118 time=12.3 ms
```

| Feld | Bedeutung |
|------|-----------|
| `64 bytes` | Antwortgröße |
| `icmp_seq` | Sequenznummer |
| `ttl=118` | Time-to-Live (Hops bis Ziel) |
| `time=12.3 ms` | Round-Trip-Time (RTT) |

**Frage:** Was bedeutet ein TTL von 118, wenn das Maximum 255 ist?

_Dein Antwort:_

<br><br>

---

### Aufgabe 2.2: Traceroute (Linux)

```bash
# 1. Standard-Traceroute (ICMP)
traceroute google.com

# 2. Mit TCP (Port 80) – umgeht oft Firewalls
traceroute -T -p 80 google.com

# 3. Mit UDP (Standard auf Linux)
traceroute -U google.com

# 4. Schneller mit weniger Wartezeit
traceroute -w 1 -q 1 google.com

# 5. Maximum 15 Hops
traceroute -m 15 google.com
```

**Windows:**
```cmd
tracert google.com
tracert -d google.com   # Ohne DNS-Auflösung (schneller)
```

**Frage:** Wie viele Hops sind es bis zu google.com? Bei welchem Hop verlässt das Paket dein Netzwerk?

_Hops:_ ____  _Letzter lokaler Hop:_ ____

---

### Aufgabe 2.3: MTU und Fragmentierung (Linux)

```bash
# 1. MTU der Interfaces anzeigen
ip link show | grep mtu

# 2. Path MTU Discovery – größtes Paket ohne Fragmentierung finden
ping -c 1 -M do -s 1472 google.com   # 1472 + 28 Header = 1500

# 3. Wenn "Frag needed" kommt, verkleinern
ping -c 1 -M do -s 1400 google.com
```

**Experiment:** Finde die maximale Paketgröße zu google.com ohne Fragmentierung.

_Maximale Payload-Größe:_ ______ Bytes

---

## Teil 3: DNS-Diagnose

### Aufgabe 3.1: DNS-Abfragen (Linux)

```bash
# 1. Einfache DNS-Abfrage
nslookup google.com

# 2. Mit dig (detaillierter)
dig google.com

# 3. Nur A-Records
dig google.com A +short

# 4. MX-Records (Mailserver)
dig google.com MX

# 5. NS-Records (Nameserver)
dig google.com NS

# 6. Reverse DNS (IP → Name)
dig -x 8.8.8.8

# 7. Bestimmten DNS-Server befragen
dig @8.8.8.8 google.com

# 8. DNS-Trace (komplette Auflösung von Root an)
dig +trace google.com
```

**Windows:**
```cmd
nslookup google.com
nslookup -type=MX google.com
nslookup google.com 8.8.8.8
```

```powershell
Resolve-DnsName google.com
Resolve-DnsName -Name google.com -Type MX
Resolve-DnsName -Name google.com -Server 8.8.8.8
```

**Aufgabe:** Ermittle die folgenden DNS-Informationen für `example.com`:

| Record-Typ | Wert |
|------------|------|
| A (IPv4) | |
| AAAA (IPv6) | |
| MX (Mail) | |
| NS (Nameserver) | |
| TXT | |

---

### Aufgabe 3.2: DNS-Cache (Linux & Windows)

```bash
# Linux: systemd-resolved Cache
resolvectl statistics
resolvectl flush-caches
```

**Windows:**
```cmd
# DNS-Cache anzeigen
ipconfig /displaydns

# DNS-Cache leeren
ipconfig /flushdns
```

```powershell
Get-DnsClientCache
Clear-DnsClientCache
```

---

## Teil 4: Ports und Verbindungen

### Aufgabe 4.1: Offene Ports und Verbindungen (Linux)

```bash
# 1. Alle lauschenden Ports (TCP)
ss -tlnp

# 2. Alle lauschenden Ports (UDP)
ss -ulnp

# 3. Alle aktiven TCP-Verbindungen
ss -tnp

# 4. Verbindungen zu einem bestimmten Port
ss -tnp | grep :443

# 5. Statistiken
ss -s

# 6. Mit netstat (klassisch)
netstat -tlnp
netstat -an
```

**Erklärung der ss-Ausgabe:**
```
State    Recv-Q  Send-Q  Local Address:Port   Peer Address:Port  Process
ESTAB    0       0       192.168.1.100:52431  93.184.216.34:443  users:(("firefox",pid=1234,fd=42))
```

| Feld | Bedeutung |
|------|-----------|
| `State` | Verbindungsstatus (ESTAB, LISTEN, TIME-WAIT...) |
| `Local Address:Port` | Eigene IP und Port |
| `Peer Address:Port` | Gegenstelle IP und Port |
| `Process` | Zugehöriger Prozess |

**Aufgabe:** Finde heraus, welche Prozesse auf deinem System auf Netzwerkverbindungen warten.

| Port | Protokoll | Prozess | Beschreibung |
|------|-----------|---------|--------------|
| | | | |
| | | | |
| | | | |

---

### Aufgabe 4.2: Ports und Verbindungen (Windows)

```cmd
# Alle lauschenden Ports
netstat -an | findstr LISTENING

# Mit Prozess-ID
netstat -ano | findstr LISTENING

# Bestimmten Port finden
netstat -ano | findstr :443
```

```powershell
# TCP-Verbindungen
Get-NetTCPConnection | Where-Object State -eq Listen

# Mit Prozessnamen
Get-NetTCPConnection -State Listen | 
    Select-Object LocalPort, OwningProcess, @{n='Process';e={(Get-Process -Id $_.OwningProcess).Name}}
```

---

### Aufgabe 4.3: Port-Scanning mit nmap (Linux)

> [!warning] **Nur im eigenen Netzwerk!**
> Port-Scanning fremder Systeme ohne Erlaubnis kann illegal sein!

```bash
# 1. Schneller Scan der häufigsten Ports (eigenes System)
nmap localhost

# 2. Alle Ports scannen
nmap -p- localhost

# 3. Bestimmte Ports
nmap -p 22,80,443 localhost

# 4. Service-Version erkennen
nmap -sV localhost

# 5. Ping-Scan im lokalen Netz (wer ist online?)
nmap -sn 192.168.1.0/24

# 6. OS-Erkennung (root nötig)
sudo nmap -O localhost
```

**Aufgabe:** Scanne dein eigenes System und dokumentiere die offenen Ports:

```bash
nmap -sV localhost
```

| Port | Service | Version |
|------|---------|---------|
| | | |
| | | |
| | | |

---

## Teil 5: Netzwerkverkehr erfassen

### Aufgabe 5.1: tcpdump Grundlagen (Linux)

> [!info] **Root-Rechte erforderlich**
> `tcpdump` benötigt Root-Rechte zum Erfassen von Paketen.

```bash
# 1. Alle Pakete auf Interface eth0 (erste 10)
sudo tcpdump -i eth0 -c 10

# 2. Nur ICMP (Ping)
sudo tcpdump -i any icmp -c 5

# 3. Nur Traffic zu/von bestimmter IP
sudo tcpdump -i any host 8.8.8.8 -c 10

# 4. Nur TCP Port 80
sudo tcpdump -i any tcp port 80 -c 10

# 5. Nur DNS (UDP Port 53)
sudo tcpdump -i any udp port 53 -c 5

# 6. Mit Paketinhalt (Hex + ASCII)
sudo tcpdump -i any -X -c 3 port 80

# 7. In Datei speichern (für Wireshark)
sudo tcpdump -i any -w capture.pcap -c 100
```

**Experiment:** Erfasse einen DNS-Lookup:

```bash
# Terminal 1: tcpdump starten
sudo tcpdump -i any udp port 53 -c 4

# Terminal 2: DNS-Abfrage auslösen
dig example.com
```

**Frage:** Welche zwei Pakete siehst du bei einer DNS-Abfrage?

_Dein Antwort:_

<br><br>

---

### Aufgabe 5.2: tcpdump Filter-Beispiele

```bash
# TCP SYN-Pakete (Verbindungsaufbau)
sudo tcpdump -i any 'tcp[tcpflags] & tcp-syn != 0' -c 5

# HTTP GET-Requests
sudo tcpdump -i any -A 'tcp port 80 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)' | grep -i "GET"

# HTTPS (nur Handshake sichtbar, Inhalt verschlüsselt)
sudo tcpdump -i any tcp port 443 -c 10

# ARP-Pakete
sudo tcpdump -i any arp -c 5
```

---

### Aufgabe 5.3: Paketanalyse (Windows)

Windows hat kein eingebautes tcpdump. Alternativen:

```powershell
# 1. Netzwerk-Trace starten (Admin-PowerShell)
netsh trace start capture=yes tracefile=C:\temp\trace.etl

# 2. Traffic generieren (z.B. Webseite aufrufen)

# 3. Trace stoppen
netsh trace stop

# 4. Mit Microsoft Message Analyzer oder Wireshark öffnen
```

> [!tip] **Empfehlung: Wireshark**
> Für grafische Paketanalyse ist Wireshark das Standardtool (Linux & Windows).
> Download: https://www.wireshark.org/

---

## Teil 6: Firewall-Status

### Aufgabe 6.1: iptables/nftables anzeigen (Linux)

```bash
# 1. iptables-Regeln anzeigen
sudo iptables -L -n -v

# 2. Mit Zeilennummern
sudo iptables -L -n --line-numbers

# 3. NAT-Tabelle
sudo iptables -t nat -L -n -v

# 4. nftables (moderner)
sudo nft list ruleset

# 5. Firewalld-Status (RHEL/Fedora)
sudo firewall-cmd --list-all

# 6. ufw-Status (Ubuntu)
sudo ufw status verbose
```

**Aufgabe:** Zeige die aktuellen Firewall-Regeln deines Systems und identifiziere:

- Default Policy für INPUT: __________
- Default Policy für OUTPUT: __________
- Erlaubte eingehende Ports: __________

---

### Aufgabe 6.2: Windows Firewall

```powershell
# 1. Firewall-Status
Get-NetFirewallProfile | Select-Object Name, Enabled

# 2. Eingehende Regeln (Erlaubt)
Get-NetFirewallRule -Direction Inbound -Enabled True | 
    Select-Object DisplayName, Action | Format-Table

# 3. Regeln für bestimmten Port
Get-NetFirewallPortFilter | Where-Object LocalPort -eq 80

# 4. Firewall-Regel erstellen (Test)
# New-NetFirewallRule -DisplayName "Test HTTP" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 8080
```

```cmd
# Klassisch
netsh advfirewall show allprofiles
netsh advfirewall firewall show rule name=all
```

---

## Teil 7: Netzwerkdienste testen

### Aufgabe 7.1: HTTP/HTTPS testen

```bash
# 1. Einfacher HTTP-Request
curl -v http://example.com

# 2. Nur Header anzeigen
curl -I https://google.com

# 3. HTTPS mit Zertifikatsinfo
curl -v https://google.com 2>&1 | grep -A5 "Server certificate"

# 4. HTTP-Statuscode
curl -o /dev/null -s -w "%{http_code}\n" https://google.com

# 5. Download-Geschwindigkeit messen
curl -o /dev/null -s -w "Time: %{time_total}s\nSpeed: %{speed_download} bytes/s\n" https://google.com

# 6. Mit wget
wget --spider https://google.com
```

**Windows PowerShell:**
```powershell
Invoke-WebRequest -Uri https://google.com -Method Head
(Invoke-WebRequest -Uri https://google.com).StatusCode
```

---

### Aufgabe 7.2: TLS/SSL-Zertifikate prüfen

```bash
# 1. Zertifikat anzeigen
openssl s_client -connect google.com:443 -servername google.com < /dev/null 2>/dev/null | openssl x509 -text -noout | head -30

# 2. Ablaufdatum prüfen
echo | openssl s_client -connect google.com:443 -servername google.com 2>/dev/null | openssl x509 -noout -dates

# 3. Zertifikatskette anzeigen
openssl s_client -connect google.com:443 -servername google.com -showcerts < /dev/null 2>/dev/null

# 4. TLS-Version und Cipher
openssl s_client -connect google.com:443 -servername google.com < /dev/null 2>/dev/null | grep -E "(Protocol|Cipher)"
```

**Aufgabe:** Prüfe das TLS-Zertifikat von `example.com`:

| Eigenschaft | Wert |
|-------------|------|
| Subject (CN) | |
| Issuer | |
| Gültig ab | |
| Gültig bis | |
| TLS-Version | |
| Cipher Suite | |

---

### Aufgabe 7.3: Netcat – der Netzwerk-Alleskönner

```bash
# 1. TCP-Verbindung testen (wie telnet)
nc -zv google.com 80
nc -zv google.com 443

# 2. Port-Range scannen
nc -zv localhost 20-25

# 3. Einfacher Server (lauscht auf Port 1234)
nc -l 1234

# 4. Client verbinden (anderes Terminal)
nc localhost 1234
# Jetzt können Nachrichten ausgetauscht werden

# 5. Datei übertragen
# Server: nc -l 1234 > empfangen.txt
# Client: nc localhost 1234 < senden.txt

# 6. Banner Grabbing (Service-Info)
echo "" | nc -v -n -w1 93.184.216.34 80
```

**Experiment:** Erstelle mit netcat einen einfachen Chat zwischen zwei Terminals.

---

## Zusammenfassung: Wichtige Kommandos

### Linux

| Kommando | Beschreibung |
|----------|--------------|
| `ip addr` / `ip a` | IP-Konfiguration anzeigen |
| `ip route` | Routing-Tabelle |
| `ip neigh` | ARP-Cache |
| `ping` | Erreichbarkeit testen |
| `traceroute` | Route zum Ziel anzeigen |
| `dig` / `nslookup` | DNS-Abfragen |
| `ss -tlnp` | Offene TCP-Ports |
| `ss -tnp` | Aktive Verbindungen |
| `tcpdump` | Pakete erfassen |
| `nmap` | Port-Scanner |
| `curl` / `wget` | HTTP-Requests |
| `nc` (netcat) | Netzwerk-Allzwecktool |
| `openssl s_client` | TLS-Verbindungen testen |
| `iptables -L` | Firewall-Regeln |

### Windows

| Kommando | Beschreibung |
|----------|--------------|
| `ipconfig /all` | IP-Konfiguration |
| `route print` | Routing-Tabelle |
| `arp -a` | ARP-Cache |
| `ping` | Erreichbarkeit testen |
| `tracert` | Route zum Ziel |
| `nslookup` | DNS-Abfragen |
| `netstat -an` | Ports und Verbindungen |
| `Get-NetTCPConnection` | PowerShell: TCP-Verbindungen |
| `Test-NetConnection` | PowerShell: Konnektivitätstest |

---

## Checkliste: Netzwerk-Troubleshooting

Bei Netzwerkproblemen systematisch vorgehen:

- [ ] **Schicht 1 (Physisch):** Kabel gesteckt? Link-LED an?
- [ ] **Schicht 2 (Data Link):** `ip link show` – Interface UP?
- [ ] **Schicht 3 (Netzwerk):** `ip addr` – IP-Adresse vorhanden?
- [ ] **Gateway:** `ping <Gateway-IP>` – Gateway erreichbar?
- [ ] **DNS:** `ping 8.8.8.8` vs. `ping google.com` – DNS funktioniert?
- [ ] **Firewall:** `iptables -L` – Traffic blockiert?
- [ ] **Service:** `ss -tlnp` – Dienst läuft und lauscht?
- [ ] **Anwendung:** `curl -v` – Anwendungsprotokoll-Fehler?

---

## Weiterführende Themen

- [[../../03-Rechnernetze/04-Basisprotokolle/01-IP|IP-Protokoll]] – Adressierung und Routing
- [[../../03-Rechnernetze/04-Basisprotokolle/02-TCP-UDP|TCP und UDP]] – Transportprotokolle
- [[../../03-Rechnernetze/04-Basisprotokolle/03-DNS|DNS]] – Domain Name System
- [[../../03-Rechnernetze/05-Sicherheit/01-Firewalls|Firewalls]] – Paketfilter und mehr
- [[../../03-Rechnernetze/05-Sicherheit/03-TLS|TLS]] – Verschlüsselte Kommunikation
