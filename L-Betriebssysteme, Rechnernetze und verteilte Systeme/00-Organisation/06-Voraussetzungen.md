---
author: Andreas Hümmer
title: "Technische Voraussetzungen"
tags:
  - organisation
  - orga
  - voraussetzungen
  - tools
  - lab
  - vm
created: 2026-10-07
modified: 2026-10-07
---

# Technische Voraussetzungen

## Übersicht

Für die Bearbeitung der praktischen Aufgaben in diesem Kurs benötigen Sie einige Werkzeuge. Diese Seite beschreibt die Einrichtung der Lab-Umgebung.

## Hypervisor (Virtualisierungssoftware)

Sie benötigen einen Hypervisor Ihrer Wahl:

| Hypervisor | Plattform | Link |
|------------|-----------|------|
| **VMware Workstation** | Windows, Linux | [vmware.com](https://www.vmware.com/products/workstation-pro.html) |
| **VirtualBox** | Windows, macOS, Linux | [virtualbox.org](https://www.virtualbox.org/) |
| **ProxMox** | Linux (Server) | [proxmox.com](https://www.proxmox.com/) |
| **Parallels** / **UTM** | macOS (inkl. Apple Silicon) | Alternative für Mac |

## Virtuelle Maschinen

Folgende VMs werden für das Lab benötigt:

### Ubuntu 26.04 Server

| | |
|---|---|
| **Download** | [ubuntu.com](https://ubuntu.com/) |
| **Version** | Ubuntu 26.04 LTS (Server) |
| **Netzwerk** | **Bridge-Mode** |
| **Empfohlene Ressourcen** | 2 CPU, 2-4 GB RAM, 20 GB Disk |

### Windows Desktop (oder Linux Desktop)

| | |
|---|---|
| **Download** | [Microsoft Windows 10 ISO](https://www.microsoft.com/de-de/software-download/windows10ISO) |
| **Alternative** | Linux Desktop (z.B. Ubuntu Desktop) |
| **Netzwerk** | **Bridge-Mode** |
| **Empfohlene Ressourcen** | 2 CPU, 4 GB RAM, 40 GB Disk |

> [!info] Warum Bridge-Mode?
> Im Bridge-Mode erhalten die VMs eigene IP-Adressen im lokalen Netzwerk und können wie physische Rechner kommunizieren. Dies ist wichtig für die Netzwerk-Übungen.

## Tools

Machen Sie sich mit folgenden Werkzeugen vertraut:

### Netzwerkanalyse

| Tool | Beschreibung | Link |
|------|--------------|------|
| **Wireshark** | Netzwerk-Protokoll-Analyzer | [wireshark.org](https://www.wireshark.org/) |
| **Nmap** | Netzwerk-Scanner und Security Auditing | [nmap.org](https://nmap.org/) |

### Betriebssystem-Tools (in jedem OS enthalten)

| Tool | Beschreibung |
|------|--------------|
| **ping** | Erreichbarkeit von Hosts prüfen (ICMP) |
| **traceroute** / **tracert** | Netzwerkpfad zu einem Ziel anzeigen |
| **netstat** | Netzwerkverbindungen und Statistiken anzeigen |
| **route** | Routing-Tabelle anzeigen und bearbeiten |

## Checkliste zur Einrichtung

- [ ] Hypervisor installiert (VMware/VirtualBox/ProxMox)
- [ ] Ubuntu 26.04 Server VM erstellt
  - [ ] Netzwerk auf Bridge-Mode gesetzt
  - [ ] SSH-Zugang eingerichtet
- [ ] Windows 10/11 oder Linux Desktop VM erstellt
  - [ ] Netzwerk auf Bridge-Mode gesetzt
- [ ] Wireshark installiert
- [ ] Nmap installiert
- [ ] Netzwerkverbindung zwischen VMs getestet (ping)

## Tipps zur Installation

### Ubuntu Server

```bash
# Nach der Installation: System aktualisieren
sudo apt update && sudo apt upgrade -y

# SSH-Server installieren (falls nicht vorhanden)
sudo apt install openssh-server

# Netzwerk-Tools installieren
sudo apt install net-tools traceroute nmap
```

### Wireshark unter Ubuntu

```bash
sudo apt install wireshark
# Benutzer zur wireshark-Gruppe hinzufügen (für Capture ohne root)
sudo usermod -aG wireshark $USER
```

## Verwandte Seiten

- [[01-Kursueberblick]]
- [[03-Zeitplan]]
- [[04-Kontakt]]
