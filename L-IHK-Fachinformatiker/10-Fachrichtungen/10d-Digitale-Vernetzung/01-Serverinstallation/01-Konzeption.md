---
title: "Serverkonzeption"
created: 2026-10-13
modified: 2026-10-13
type: lecture
tags:
  - lf11d
  - server
  - installation
  - konzeption
  - planung
source: proTirone (CC-BY-4.0)
---

# Serverkonzeption

> [!info] Lernziele
> - Planungsbereiche einer Serverinstallation kennen
> - Abhängigkeiten zwischen Entscheidungen verstehen
> - Systematische Vorgehensweise bei der Konzeption anwenden

## Wissensbereiche (Knowledge Areas)

Bei der Planung einer Serverinstallation müssen folgende Bereiche berücksichtigt werden:

### 1. Betriebssystem

**Fragen:**
- Welches Betriebssystem soll installiert werden?
- Linux-Distribution oder Windows Server?
- 32-bit oder 64-bit?

**Optionen:**
| Typ | Beispiele | Einsatzgebiet |
|-----|-----------|---------------|
| Linux (Debian-basiert) | Ubuntu Server, Debian | Webserver, Container |
| Linux (RHEL-basiert) | Rocky Linux, AlmaLinux | Enterprise |
| Windows Server | 2019, 2022 | Active Directory, .NET |

### 2. Festplattendesign

→ Siehe [[02-Festplattendesign|Festplattendesign]]

**Fragen:**
- Wie sollen die Festplatten partitioniert werden?
- Welche Dateisysteme werden verwendet?
- RAID-Konfiguration?

### 3. Dateizugriffsregeln

**Fragen:**
- Welche Benutzer und Gruppen werden benötigt?
- Welche Berechtigungen auf Verzeichnisebene?
- ACLs oder Standard-Unix-Rechte?

### 4. Installationsmedium

**Optionen:**
- USB-Stick (bootfähig)
- DVD/CD
- Netzwerk-Installation (PXE)
- Cloud-Images

### 5. Systemweite Einstellungen

**Fragen:**
- Tastaturlayout?
- Betriebssprache?
- Zeitzone und Zeitserver (NTP)?
- Hostname und Domain?

### 6. Services (Serverdienste)

**Fragen:**
- Welche Serverprogramme werden benötigt?
- Webserver (Apache, Nginx)?
- Datenbank (MySQL, PostgreSQL)?
- Mail-Server?

### 7. Backup-Strategie

**Fragen:**
- Vollbackup oder inkrementell?
- Backup-Medium (lokal, NAS, Cloud)?
- Backup-Intervall?
- Retention-Policy?

### 8. Netzwerkintegration

**Fragen:**
- IP-Adresse (statisch/DHCP)?
- Subnetz und Gateway?
- DNS-Server?
- Firewall-Regeln?

## Vorgehensweise

```
┌──────────────────────────────────────────────────────────┐
│                    1. ANALYSE                            │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│  │ Anforderungen│  │Restriktionen│  │  Ressourcen │      │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘      │
└─────────┼────────────────┼────────────────┼─────────────┘
          └────────────────┼────────────────┘
                           ↓
┌──────────────────────────────────────────────────────────┐
│                    2. DESIGN                             │
│  Entscheidungen zu allen 8 Wissensbereichen treffen      │
│  Abhängigkeiten berücksichtigen                          │
└───────────────────────────┬──────────────────────────────┘
                           ↓
┌──────────────────────────────────────────────────────────┐
│                    3. DOKUMENTATION                      │
│  Alle Entscheidungen schriftlich festhalten              │
│  Begründungen dokumentieren                              │
└───────────────────────────┬──────────────────────────────┘
                           ↓
┌──────────────────────────────────────────────────────────┐
│                    4. UMSETZUNG                          │
│  Installation durchführen                                │
│  Konfiguration gemäß Dokumentation                       │
└──────────────────────────────────────────────────────────┘
```

## Abhängigkeiten zwischen Entscheidungen

> [!warning] Wichtig
> Die Entscheidungen in den verschiedenen Bereichen sind **nicht unabhängig** voneinander!

| Entscheidung | Beeinflusst |
|--------------|-------------|
| Betriebssystem | Dateisysteme, Services, Backup-Tools |
| Services | Festplattendesign, Netzwerkports |
| Backup-Strategie | Festplattendesign, Netzwerk |
| Netzwerk | Firewall, Services |

## Empfehlung: Minimalinstallation

> [!tip] Best Practice
> Beginnen Sie mit einer **Minimalinstallation** und erweitern Sie das System sukzessive:
> 1. Grundsystem ohne GUI installieren
> 2. Netzwerk konfigurieren
> 3. SSH aktivieren (Fernzugriff)
> 4. Services einzeln hinzufügen und testen

## Prüfungsrelevanz

> [!question] Typische Prüfungsfragen
> - Welche Bereiche müssen bei der Serverplanung berücksichtigt werden?
> - Nennen Sie Abhängigkeiten zwischen Planungsentscheidungen
> - Warum ist eine Minimalinstallation empfehlenswert?

## Querverweise

- → [[02-Festplattendesign|Festplattendesign]] – Partitionierung
- → [[../02-IoT-Protokolle/01-MQTT|MQTT]] – Serverdienst-Beispiel
- → [[../../../09-LF09-Netzwerke-Erweitert/04-SSH/01-SSH-Grundlagen|SSH]] – Fernzugriff

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (CC-BY-4.0).
