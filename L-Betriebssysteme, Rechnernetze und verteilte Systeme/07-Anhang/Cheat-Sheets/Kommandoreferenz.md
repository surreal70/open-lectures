---
author: Andreas Hümmer
title: "Kommandoreferenz"
tags:
  - kommandos
  - referenz
  - befehle
  - cli
created: 2026-10-07
modified: 2026-10-07
---

# Kommandoreferenz

Diese Übersicht enthält wichtige Kommandos und Befehle für die Arbeit mit **Betriebssystemen** und **Netzwerken**.

---

## Linux/Unix Grundkommandos

### Dateisystem-Navigation

| Kommando | Beschreibung | Beispiel |
|----------|--------------|----------|
| `ls` | Verzeichnisinhalt anzeigen | `ls -la /home` |
| `cd` | Verzeichnis wechseln | `cd /var/log` |
| `pwd` | Aktuelles Verzeichnis anzeigen | `pwd` |
| `mkdir` | Verzeichnis erstellen | `mkdir -p projekt/src` |
| `rmdir` | Leeres Verzeichnis löschen | `rmdir temp` |
| `tree` | Verzeichnisbaum anzeigen | `tree -L 2` |

### Dateioperationen

| Kommando | Beschreibung | Beispiel |
|----------|--------------|----------|
| `cp` | Dateien kopieren | `cp datei.txt backup/` |
| `mv` | Dateien verschieben/umbenennen | `mv alt.txt neu.txt` |
| `rm` | Dateien löschen | `rm -rf temp/` |
| `touch` | Datei erstellen/Zeitstempel ändern | `touch neue_datei.txt` |
| `cat` | Dateiinhalt anzeigen | `cat /etc/passwd` |
| `less` | Datei seitenweise anzeigen | `less logfile.log` |
| `head` | Erste Zeilen anzeigen | `head -n 20 datei.txt` |
| `tail` | Letzte Zeilen anzeigen | `tail -f /var/log/syslog` |

### Suchen und Filtern

| Kommando | Beschreibung | Beispiel |
|----------|--------------|----------|
| `find` | Dateien suchen | `find /home -name "*.txt"` |
| `grep` | In Dateien suchen | `grep -r "error" /var/log/` |
| `locate` | Schnelle Dateisuche | `locate config.json` |
| `which` | Pfad eines Befehls finden | `which python` |

### Berechtigungen

| Kommando | Beschreibung | Beispiel |
|----------|--------------|----------|
| `chmod` | Berechtigungen ändern | `chmod 755 script.sh` |
| `chown` | Eigentümer ändern | `chown user:group datei.txt` |
| `chgrp` | Gruppe ändern | `chgrp developers projekt/` |

---

## Prozessverwaltung

| Kommando | Beschreibung | Beispiel |
|----------|--------------|----------|
| `ps` | Prozesse anzeigen | `ps aux` |
| `top` | Prozesse live überwachen | `top` |
| `htop` | Erweiterte Prozessübersicht | `htop` |
| `kill` | Prozess beenden | `kill -9 1234` |
| `killall` | Prozesse nach Namen beenden | `killall firefox` |
| `bg` | Prozess in den Hintergrund | `bg %1` |
| `fg` | Prozess in den Vordergrund | `fg %1` |
| `jobs` | Hintergrundjobs anzeigen | `jobs -l` |
| `nohup` | Prozess unabhängig von Terminal | `nohup script.sh &` |
| `nice` | Priorität setzen | `nice -n 10 command` |
| `renice` | Priorität ändern | `renice -n 5 -p 1234` |

---

## Speicherverwaltung

| Kommando | Beschreibung | Beispiel |
|----------|--------------|----------|
| `free` | Speichernutzung anzeigen | `free -h` |
| `df` | Festplattenplatz anzeigen | `df -h` |
| `du` | Verzeichnisgröße anzeigen | `du -sh *` |
| `vmstat` | Virtuelle Speicherstatistik | `vmstat 1` |

---

## Netzwerk-Kommandos

### Netzwerkdiagnose

| Kommando | Beschreibung | Beispiel |
|----------|--------------|----------|
| `ping` | Erreichbarkeit testen | `ping -c 4 google.com` |
| `traceroute` | Route zu einem Host anzeigen | `traceroute google.com` |
| `nslookup` | DNS-Abfrage | `nslookup example.com` |
| `dig` | Erweiterte DNS-Abfrage | `dig example.com MX` |
| `host` | DNS-Lookup | `host google.com` |

### Netzwerkkonfiguration

| Kommando | Beschreibung | Beispiel |
|----------|--------------|----------|
| `ip addr` | IP-Adressen anzeigen | `ip addr show` |
| `ip route` | Routing-Tabelle anzeigen | `ip route` |
| `ifconfig` | Netzwerkschnittstellen (veraltet) | `ifconfig eth0` |
| `netstat` | Netzwerkstatistiken | `netstat -tulpn` |
| `ss` | Socket-Statistiken | `ss -tulpn` |

### Netzwerkübertragung

| Kommando | Beschreibung | Beispiel |
|----------|--------------|----------|
| `curl` | URL abrufen | `curl -O https://example.com/file` |
| `wget` | Dateien herunterladen | `wget https://example.com/file.zip` |
| `scp` | Sichere Dateiübertragung | `scp file.txt user@host:/path/` |
| `rsync` | Synchronisation | `rsync -avz src/ dest/` |
| `ssh` | Sichere Shell-Verbindung | `ssh user@server.com` |
| `ftp` | FTP-Verbindung | `ftp server.com` |

### Firewall

| Kommando | Beschreibung | Beispiel |
|----------|--------------|----------|
| `iptables` | Firewall-Regeln verwalten | `iptables -L -n` |
| `ufw` | Einfache Firewall (Ubuntu) | `ufw status` |
| `firewall-cmd` | Firewall (CentOS/RHEL) | `firewall-cmd --list-all` |

---

## Paketverwaltung

### Debian/Ubuntu (apt)

| Kommando | Beschreibung | Beispiel |
|----------|--------------|----------|
| `apt update` | Paketliste aktualisieren | `sudo apt update` |
| `apt upgrade` | Pakete aktualisieren | `sudo apt upgrade` |
| `apt install` | Paket installieren | `sudo apt install vim` |
| `apt remove` | Paket entfernen | `sudo apt remove vim` |
| `apt search` | Pakete suchen | `apt search python` |

### Red Hat/CentOS (yum/dnf)

| Kommando | Beschreibung | Beispiel |
|----------|--------------|----------|
| `dnf install` | Paket installieren | `sudo dnf install httpd` |
| `dnf update` | Pakete aktualisieren | `sudo dnf update` |
| `dnf search` | Pakete suchen | `dnf search nginx` |

---

## Systemverwaltung

| Kommando | Beschreibung | Beispiel |
|----------|--------------|----------|
| `systemctl` | Dienste verwalten | `systemctl status nginx` |
| `journalctl` | System-Logs anzeigen | `journalctl -xe` |
| `dmesg` | Kernel-Meldungen | `dmesg | tail` |
| `uptime` | Systemlaufzeit | `uptime` |
| `uname` | Systeminformationen | `uname -a` |
| `hostname` | Hostname anzeigen/setzen | `hostname` |
| `date` | Datum und Uhrzeit | `date` |
| `shutdown` | System herunterfahren | `shutdown -h now` |
| `reboot` | System neustarten | `reboot` |

---

## Benutzer- und Gruppenverwaltung

| Kommando | Beschreibung | Beispiel |
|----------|--------------|----------|
| `useradd` | Benutzer erstellen | `useradd -m neueruser` |
| `userdel` | Benutzer löschen | `userdel -r altuser` |
| `usermod` | Benutzer ändern | `usermod -aG sudo user` |
| `passwd` | Passwort ändern | `passwd username` |
| `groupadd` | Gruppe erstellen | `groupadd developers` |
| `groups` | Gruppen eines Benutzers | `groups username` |
| `id` | Benutzer-/Gruppen-IDs | `id username` |
| `who` | Eingeloggte Benutzer | `who` |
| `w` | Detaillierte Benutzerinfo | `w` |

---

## Archivierung und Komprimierung

| Kommando | Beschreibung | Beispiel |
|----------|--------------|----------|
| `tar` | Archivieren | `tar -czvf archiv.tar.gz ordner/` |
| `zip` | ZIP erstellen | `zip -r archiv.zip ordner/` |
| `unzip` | ZIP entpacken | `unzip archiv.zip` |
| `gzip` | Komprimieren | `gzip datei.txt` |
| `gunzip` | Dekomprimieren | `gunzip datei.txt.gz` |

---

> **Hinweis**: Diese Referenz enthält eine Auswahl häufig verwendeter Kommandos. Für detaillierte Informationen nutzen Sie `man <kommando>` oder `<kommando> --help`.

## Verwandte Seiten

- [[Glossar]]
- [[Abkuerzungen|Abkürzungsverzeichnis]]
