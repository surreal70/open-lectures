---
title: "Festplattendesign"
created: 2026-10-13
modified: 2026-10-13
type: lecture
tags:
  - lf11d
  - server
  - partitionen
  - dateisysteme
  - linux
  - windows
source: proTirone (CC-BY-4.0)
---

# Festplattendesign

> [!info] Lernziele
> - Unterschied zwischen Festplatten, Partitionen und Dateisystemen verstehen
> - Linux- und Windows-Konzepte vergleichen
> - Partitionierungsstrategien für Server kennen

## Grundbegriffe

### Festplattentypen

| Typ | Bezeichnung | Eigenschaften |
|-----|-------------|---------------|
| **HDD** | Hard Disk Drive | Mechanisch, günstig, langsamer |
| **SSD** | Solid State Drive | Elektronisch, schnell |
| **NVMe** | Non-Volatile Memory Express | Sehr schnell, PCIe-Anbindung |

### Gerätenamen unter Linux

```
/dev/
├── sda           ← Erste SATA/SAS-Festplatte
│   ├── sda1      ← Erste Partition
│   ├── sda2      ← Zweite Partition
│   └── sda3      ← Dritte Partition
├── sdb           ← Zweite SATA/SAS-Festplatte
├── nvme0n1       ← Erstes NVMe-Laufwerk
│   ├── nvme0n1p1 ← Erste Partition
│   └── nvme0n1p2 ← Zweite Partition
└── nvme1n1       ← Zweites NVMe-Laufwerk
```

> [!note] Namenskonvention
> - **SATA/SAS**: `sd` + Buchstabe + Partitionsnummer (sda1, sdb2)
> - **NVMe**: `nvme` + Controller + `n` + Namespace + `p` + Partition (nvme0n1p1)

## Dateisysteme

### Windows-Dateisysteme

| Dateisystem | Beschreibung |
|-------------|--------------|
| **NTFS** | Standard für Windows, Journaling, ACLs |
| **FAT32** | Kompatibel, max. 4 GB Dateigröße |
| **exFAT** | Für USB-Sticks, keine 4-GB-Grenze |
| **ReFS** | Resilient File System, für Server |

### Linux-Dateisysteme

| Dateisystem | Beschreibung |
|-------------|--------------|
| **ext4** | Standard, robust, ausgereift |
| **XFS** | Optimiert für große Dateien |
| **Btrfs** | Modern, Snapshots, Copy-on-Write |
| **tmpfs** | Im RAM, für temporäre Dateien |
| **swap** | Auslagerungsspeicher |

> [!tip] Kompatibilität
> Linux kann Windows-Dateisysteme (NTFS, FAT32, exFAT) lesen und schreiben.
> Windows kann Linux-Dateisysteme standardmäßig **nicht** lesen.

## Mountpoints unter Linux

Im Gegensatz zu Windows (Laufwerksbuchstaben C:, D:) werden Partitionen unter Linux in das Dateisystem **eingehängt** (gemountet):

```
/                    ← Root-Partition
├── boot/            ← Boot-Partition (Kernel)
├── home/            ← Home-Partition (Benutzerdaten)
├── var/             ← Var-Partition (Logs, Datenbanken)
└── tmp/             ← tmpfs (RAM)
```

## Partitionierungsstrategien

### Strategie 1: Alles auf einer Partition

```
┌────────────────────────────────────┐
│            /  (root)               │
│         Alles zusammen             │
└────────────────────────────────────┘
```

**Vorteile:**
- Einfach
- Flexible Speichernutzung

**Nachteile:**
- Kein paralleles OS-Update möglich
- Keine Trennung von Daten und System

### Strategie 2: Getrennte Partitionen (Server)

```
┌──────────┬──────────┬──────────┬──────────┬──────────┐
│  /boot   │   swap   │    /     │  /home   │   /var   │
│  512 MB  │  RAM×2   │  20 GB   │ flexibel │ flexibel │
│  ext4    │  swap    │  ext4    │  ext4    │  ext4    │
└──────────┴──────────┴──────────┴──────────┴──────────┘
```

**Partitionen für Server:**

| Partition | Mountpoint | Zweck |
|-----------|------------|-------|
| Boot | `/boot` | Kernel, Bootloader |
| Swap | - | Auslagerung |
| Root | `/` | Betriebssystem |
| Home | `/home` | Benutzerdaten |
| Var | `/var` | Logs, Datenbanken, Webinhalte |
| Root II | - | Für paralleles OS-Update |

## Nützliche Befehle

### Informationen anzeigen

```bash
# Alle Block-Geräte auflisten
lsblk

# Mit Dateisystemtyp und Mountpoint
lsblk -o NAME,FSTYPE,SIZE,MOUNTPOINT

# Detaillierte Partitionsinformationen
sudo fdisk -l

# Speicherplatz pro Dateisystem
df -h
```

### Partitionen verwalten

```bash
# Grafisches Partitionierungstool
sudo gparted

# Partition mounten
sudo mount /dev/sda1 /mnt/daten

# Partition unmounten
sudo umount /mnt/daten
```

## Praxisbeispiel

### USB-Stick mit zwei Partitionen

```bash
# 1. gparted starten
sudo gparted

# 2. USB-Stick auswählen (z.B. /dev/sdb)

# 3. Bestehende Partitionen löschen

# 4. Neue Partitionen erstellen:
#    - Partition 1: FAT32 (Windows-kompatibel)
#    - Partition 2: ext4 (nur Linux)

# 5. Änderungen anwenden
```

> [!warning] Achtung
> Unter Windows wird nur die FAT32-Partition angezeigt, da Windows ext4 nicht unterstützt!

## Prüfungsrelevanz

> [!question] Typische Prüfungsfragen
> - Nennen Sie Unterschiede zwischen Linux- und Windows-Dateisystemen
> - Warum werden Server mit getrennten Partitionen eingerichtet?
> - Was ist ein Mountpoint?
> - Wie heißen NVMe-Geräte unter Linux?

## Querverweise

- → [[01-Konzeption|Serverkonzeption]] – Planungskontext
- → [[../../../02-LF02-Arbeitsplatz/00-LF02-Index|LF02]] – Hardware-Grundlagen
- → [[../../../09-LF09-Netzwerke-Erweitert/04-SSH/01-SSH-Grundlagen|SSH]] – Fernzugriff auf Server

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (CC-BY-4.0).
