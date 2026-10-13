---
author: Andreas Hümmer
title: Dateisystem-Grundlagen
tags:
  - content
  - bs
  - dateisystem
  - grundlagen
  - datei
  - verzeichnis
  - inode
created: '2026-10-07'
modified: '2026-10-09'
bereich: BS
---

# Dateisystem-Grundlagen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Aufgaben eines Dateisystems aus Betriebssystem-Sicht verstehen
> - Die Konzepte Datei, Verzeichnis und Pfad erklären können
> - Den Unterschied zwischen logischer und physischer Sicht kennen
> - Dateiattribute und Zugriffsrechte beschreiben können
> - Die wichtigsten Dateisystem-Operationen kennen

---

## Definition

> [!quote] **Formale Definition**
> Ein **Dateisystem** ist die Komponente des Betriebssystems, die persistente Daten auf Speichermedien organisiert und verwaltet. Es bietet eine abstrakte, logische Sicht auf den Speicher in Form von **Dateien** und **Verzeichnissen** und versteckt die physischen Details des Speichermediums.

---

## Warum Dateisysteme?

### Das Problem ohne Dateisysteme

Ohne Dateisysteme müssten Anwendungen:
- Direkt Sektoren/Blöcke auf der Festplatte adressieren
- Selbst verwalten, welche Blöcke frei oder belegt sind
- Eigene Datenstrukturen für Metadaten implementieren
- Sich gegenseitig vor Überschreibungen schützen

### Die Lösung: Abstraktion

Das Dateisystem bietet eine mehrschichtige Abstraktion, die die Komplexität der physischen Speicherung vollständig vor den Anwendungen verbirgt. Diese Schichtenarchitektur ist ein klassisches Beispiel für das Prinzip der **Information Hiding** in der Systemsoftware.

| Abstraktion | Versteckt |
|-------------|-----------|
| **Datei** | Zusammenhängende Byte-Sequenz statt verstreuter Blöcke |
| **Verzeichnis** | Benannte Container für Dateien |
| **Pfad** | Hierarchische Adressierung statt Block-Nummern |
| **Zugriffsrechte** | Schutz vor unberechtigtem Zugriff |

![[dateisystem-abstraktion.png|center|600]]
*<span class="fig-id">02-07-02-dateisystem-abstraktion</span>: Die drei Abstraktionsebenen eines Dateisystems*

Die Abbildung zeigt, wie ein einfacher `open()`-Aufruf durch mehrere Schichten übersetzt wird: Das VFS (Virtual File System) bietet eine einheitliche Schnittstelle, der konkrete Dateisystem-Treiber (ext4, NTFS, etc.) übersetzt in Blockoperationen, und der Buffer Cache optimiert den Zugriff auf die physischen Blöcke.

---

## Das Datei-Konzept

### Was ist eine Datei?

Eine **Datei** ist aus Betriebssystem-Sicht:
- Eine benannte Sammlung zusammengehöriger Daten
- Eine Abstraktion für persistenten Speicher
- Die kleinste Einheit, die auf Sekundärspeicher geschrieben werden kann

> [!tip] **Merkhilfe**
> Eine Datei ist wie ein Aktenordner: Sie hat einen Namen, einen Inhalt, und Metadaten (Erstellungsdatum, Besitzer, etc.) – aber wie die Papiere darin physisch gelagert werden, ist für den Benutzer unsichtbar.

### Dateistrukturen

| Struktur | Beschreibung | Beispiel |
|----------|--------------|----------|
| **Byte-Sequenz** | Unstrukturierter Byte-Strom | Unix/Linux, Windows |
| **Record-Sequenz** | Folge von Datensätzen fester Länge | Historische Mainframes |
| **B-Baum** | Datei mit internem Schlüsselbaum | IBM VSAM |

**Unix/Linux-Philosophie:** Alles ist eine Byte-Sequenz. Das Betriebssystem interpretiert den Inhalt nicht – das ist Aufgabe der Anwendung.

### Dateitypen

| Typ | Beschreibung | Beispiel (Linux) |
|-----|--------------|------------------|
| **Reguläre Datei** | Enthält Benutzerdaten | Text, Binär, Bilder |
| **Verzeichnis** | Enthält Verweise auf andere Dateien | `/home/user/` |
| **Gerätedatei (Block)** | Blockorientiertes Gerät | `/dev/sda` |
| **Gerätedatei (Char)** | Zeichenorientiertes Gerät | `/dev/tty` |
| **Symbolischer Link** | Verweis auf andere Datei | Shortcut |
| **Socket** | IPC-Kommunikationsendpunkt | `/var/run/*.sock` |
| **Named Pipe (FIFO)** | Benannte Pipe für IPC | `/tmp/myfifo` |

### Dateiattribute (Metadaten)

Jede Datei hat Metadaten, die vom Dateisystem verwaltet werden:

| Attribut | Beschreibung | Beispiel |
|----------|--------------|----------|
| **Name** | Menschenlesbarer Bezeichner | `report.pdf` |
| **Typ** | Art der Datei | Regulär, Verzeichnis, Link |
| **Größe** | Anzahl der Bytes | 4096 Bytes |
| **Erstellt** | Zeitstempel der Erstellung | 2026-10-01 14:30 |
| **Geändert** | Letzte Inhaltsänderung | 2026-10-09 09:15 |
| **Zugegriffen** | Letzter Lesezugriff | 2026-10-09 10:00 |
| **Besitzer** | Benutzer-ID (UID) | 1000 |
| **Gruppe** | Gruppen-ID (GID) | 1000 |
| **Rechte** | Zugriffsberechtigungen | `rwxr-xr--` |
| **Speicherort** | Physische Blöcke | Inode-Verweis |

```bash
# Dateiattribute unter Linux anzeigen
$ stat /etc/passwd
  File: /etc/passwd
  Size: 2847        Blocks: 8          IO Block: 4096   regular file
Device: 8,1   Inode: 131074      Links: 1
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2026-10-09 08:00:00.000000000 +0200
Modify: 2026-09-15 10:30:00.000000000 +0200
Change: 2026-09-15 10:30:00.000000000 +0200
 Birth: 2026-01-01 00:00:00.000000000 +0100
```

---

## Verzeichnisse

### Verzeichnisstruktur

Ein **Verzeichnis** (Directory) ist eine spezielle Datei, die Verweise auf andere Dateien und Verzeichnisse enthält.

**Historische Entwicklung:**

Die Verzeichnisstruktur hat sich über Jahrzehnte weiterentwickelt, um den wachsenden Anforderungen an Organisation und gemeinsame Nutzung von Dateien gerecht zu werden:

![[verzeichnis-evolution.png|center|700]]
*<span class="fig-id">02-07-02-verzeichnis-evolution</span>: Evolution der Verzeichnisstruktur – von flach bis zum azyklischen Graphen*

| Struktur | Vorteile | Nachteile |
|----------|----------|-----------|
| **Flach** | Einfach zu implementieren | Namenskollisionen, keine Organisation |
| **Zweistufig** | Benutzerisolation | Keine Unterverzeichnisse |
| **Hierarchisch** | Beliebige Tiefe, gute Organisation | Keine gemeinsamen Dateien |
| **Azyklischer Graph** | Gemeinsame Dateien via Links | Komplexere Verwaltung |

### Absolute vs. Relative Pfade

| Pfadtyp | Beschreibung | Beispiel |
|---------|--------------|----------|
| **Absolut** | Beginnt bei Root (`/`) | `/home/user/docs/file.txt` |
| **Relativ** | Relativ zum aktuellen Verzeichnis | `docs/file.txt` oder `../file.txt` |

**Spezielle Verzeichniseinträge:**
- `.` (Punkt) – das aktuelle Verzeichnis
- `..` (Punkt-Punkt) – das übergeordnete Verzeichnis

### Hard Links vs. Soft Links

Unix-Dateisysteme bieten zwei Mechanismen, um mehrere Namen auf dieselbe Datei verweisen zu lassen. Das Verständnis dieser Unterschiede ist wichtig für die Arbeit mit Dateisystemen und erklärt auch, warum `rm` eine Datei nicht immer sofort löscht.

![[hard-vs-soft-links.png|center|700]]
*<span class="fig-id">02-07-02-hard-vs-soft-links</span>: Hard Links vs. Symbolic Links – zwei Wege zur gemeinsamen Dateinutzung*

| Eigenschaft | Hard Link | Symbolic Link (Symlink) |
|-------------|-----------|------------------------|
| **Mechanismus** | Beide Namen → selber Inode | Symlink enthält Pfad als Text |
| **Datei-Existenz** | Datei existiert bis Link Count = 0 | Kann "dangling" sein (Ziel gelöscht) |
| **Dateisystem-Grenzen** | Nur im selben Dateisystem | Kann über FS-Grenzen zeigen |
| **Verzeichnisse** | Nicht erlaubt (außer `.` und `..`) | Kann auf Verzeichnisse zeigen |
| **Eigener Inode** | Nein (teilt Inode mit Original) | Ja (eigene kleine Datei) |

```bash
# Hard Link erstellen
$ ln original.txt hardlink.txt

# Symbolic Link erstellen
$ ln -s original.txt symlink.txt

# Link-Count anzeigen (2. Spalte)
$ ls -l
-rw-r--r-- 2 user user 100 Oct 9 10:00 hardlink.txt
-rw-r--r-- 2 user user 100 Oct 9 10:00 original.txt
lrwxrwxrwx 1 user user  12 Oct 9 10:00 symlink.txt -> original.txt
```

---

## Dateioperationen

Das Betriebssystem bietet Systemaufrufe für Dateioperationen:

### Grundlegende Operationen

| Operation | Beschreibung | Unix System Call |
|-----------|--------------|------------------|
| **Create** | Neue Datei erstellen | `creat()`, `open(O_CREAT)` |
| **Delete** | Datei löschen | `unlink()` |
| **Open** | Datei öffnen, FD erhalten | `open()` |
| **Close** | Datei schließen | `close()` |
| **Read** | Daten lesen | `read()` |
| **Write** | Daten schreiben | `write()` |
| **Seek** | Leseposition setzen | `lseek()` |
| **Get Attributes** | Metadaten lesen | `stat()`, `fstat()` |
| **Set Attributes** | Metadaten ändern | `chmod()`, `chown()` |
| **Rename** | Umbenennen/Verschieben | `rename()` |

### Open File Table

Wenn eine Datei geöffnet wird, legt das Betriebssystem Einträge in mehreren Tabellen an:

![[open-file-tables.png|center|700]]
*<span class="fig-id">02-07-02-open-file-tables</span>: Drei-Ebenen-Struktur der Open File Tables*

| Ebene | Tabelle | Beschreibung |
|-------|---------|--------------|
| **1. Per-Process** | FD-Tabelle | Jeder Prozess hat eigene File Descriptors (0=stdin, 1=stdout, 2=stderr, 3+: geöffnete Dateien) |
| **2. System-wide** | Open File Table | Enthält für jeden offenen File Descriptor: Zugriffsmodus, aktuellen Offset, Verweis auf Inode |
| **3. Inode Cache** | In-Memory Inode Table | Gecachte Inodes aktiver Dateien mit Größe, Blockliste und Reference Count |

> [!info] **Warum drei Ebenen?**
> - **Prozess-Isolation**: Jeder Prozess hat seinen eigenen Namensraum für File Descriptors
> - **Shared State**: Offset wird pro Open-Aufruf gespeichert (nicht pro Prozess) – so können `fork()`-Kinder die Position teilen
> - **Caching**: Inodes werden nur einmal im RAM gehalten, auch wenn mehrere Prozesse dieselbe Datei öffnen

---

## Zugriffsrechte

### Unix-Berechtigungsmodell

Unix/Linux verwendet ein einfaches, aber effektives Berechtigungsmodell:

![[unix-permissions.png|center|600]]
*<span class="fig-id">02-07-02-unix-permissions</span>: Aufbau der Unix-Dateiberechtigungen*

| Zeichen | Dateityp |
|---------|----------|
| `-` | Reguläre Datei |
| `d` | Verzeichnis (Directory) |
| `l` | Symbolischer Link |
| `c` | Character Device |
| `b` | Block Device |
| `s` | Socket |
| `p` | Named Pipe (FIFO) |

> [!example] **Oktal-Berechnung**
> `rwxr-xr-- = (4+2+1)(4+0+1)(4+0+0) = 754`

### Spezielle Bits

| Bit | Name | Oktal | Wirkung |
|-----|------|-------|---------|
| **SUID** | Set User ID | 4000 | Programm läuft mit Rechten des Besitzers |
| **SGID** | Set Group ID | 2000 | Programm läuft mit Rechten der Gruppe |
| **Sticky** | Sticky Bit | 1000 | Nur Besitzer kann Dateien im Verzeichnis löschen |

```bash
# SUID-Beispiel: passwd läuft als root
$ ls -l /usr/bin/passwd
-rwsr-xr-x 1 root root 59976 Oct 9 10:00 /usr/bin/passwd
    ^
    s = SUID gesetzt

# Sticky Bit auf /tmp
$ ls -ld /tmp
drwxrwxrwt 15 root root 4096 Oct 9 10:00 /tmp
         ^
         t = Sticky Bit gesetzt
```

### Access Control Lists (ACLs)

Für feinere Kontrolle bieten moderne Systeme ACLs:

```bash
# ACL anzeigen
$ getfacl file.txt
# file: file.txt
# owner: alice
# group: staff
user::rw-
user:bob:r--          # Bob darf nur lesen
group::r--
group:devs:rw-        # devs-Gruppe darf auch schreiben
mask::rw-
other::---

# ACL setzen
$ setfacl -m u:bob:r file.txt
```

---

## Dateisystem-Schnittstelle

### Das Virtual File System (VFS)

Linux/Unix verwendet VFS als Abstraktionsschicht, um verschiedene Dateisysteme einheitlich anzusprechen:

![[vfs.png|center|650]]
*<span class="fig-id">02-07-02-vfs</span>: Das Virtual File System als einheitliche Abstraktionsschicht*

---

## Mounten von Dateisystemen

### Das Mount-Konzept

In Unix/Linux werden Dateisysteme an Verzeichnisse "gehängt" (mounted):

![[mount-concept.png|center|750]]
*<span class="fig-id">02-07-02-mount-concept</span>: Vor und nach dem Mounten eines USB-Sticks*

```bash
# Dateisystem mounten
$ mount /dev/sdb1 /mnt/usb

# Alle gemounteten Dateisysteme anzeigen
$ mount
/dev/sda1 on / type ext4 (rw,relatime)
/dev/sdb1 on /mnt/usb type vfat (rw,relatime)
tmpfs on /tmp type tmpfs (rw,nosuid,nodev)

# Dateisystem unmounten
$ umount /mnt/usb
```

### /etc/fstab

Die Datei `/etc/fstab` definiert automatische Mounts beim Systemstart:

```
# /etc/fstab
# <device>        <mountpoint>  <type>  <options>        <dump> <pass>
/dev/sda1         /             ext4    defaults         0      1
/dev/sda2         /home         ext4    defaults         0      2
/dev/sda3         swap          swap    defaults         0      0
UUID=abc123...    /mnt/data     ext4    noauto,user      0      0
```

---

## Zusammenhänge

- [[01-Historie-Festplatten|Geschichte der Festplatten]] → Warum Blöcke und Sektoren?
- [[03-Implementierung|Implementierung]] → Wie Dateisysteme intern arbeiten
- [[04-Journaling|Journaling]] → Schutz vor Datenverlust
- [[../06-Ein-Ausgabe/01-IO-Grundlagen|I/O-Grundlagen]] → Dateisystem nutzt Block-I/O
- [[../02-Architektur/02-Schichtenmodell|Schichtenmodell]] → VFS als Abstraktionsschicht

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - VFS-Konzept

> [!question] **Häufige Prüfungsfragen**
> 1. Was ist der Unterschied zwischen einem Hard Link und einem Symbolic Link?
> 2. Erklären Sie die Unix-Berechtigungen `rwxr-x---` in Worten und Oktal!
> 3. Was passiert beim Öffnen einer Datei auf Betriebssystem-Ebene?
> 4. Warum können Hard Links nicht über Dateisystem-Grenzen hinweg erstellt werden?
> 5. Was ist das VFS und welche Vorteile bietet es?

> [!tip] **Merkhilfen**
> - **Hard Link** = "Alias in der Kontaktliste" (zeigt auf dieselbe Person)
> - **Symbolic Link** = "Wegweiser" (kann ins Leere zeigen)
> - **rwx** = 4+2+1 = 7 (Volle Rechte)
> - **VFS** = "Übersetzer" zwischen Anwendung und verschiedenen Dateisystemen

---

## Weiterführende Ressourcen

> [!note] **Videos (YouTube)**
>
> | | Video | Beschreibung |
> |---|-------|--------------|
> | 🎬 | [Neso Academy – File Systems](https://www.youtube.com/watch?v=mzUyMy7Ihk0) | Grundlagen der Dateisysteme |
> | 🎬 | [MIT OCW – File System Concepts](https://www.youtube.com/watch?v=xM1V0zQyJyY) | Akademische Einführung |

---

## Quellen

- Tanenbaum, A. S.: Modern Operating Systems, Kapitel 4
- Silberschatz, Galvin, Gagne: Operating System Concepts, Kapitel 13-15
- Love, R.: Linux Kernel Development, Kapitel 13
