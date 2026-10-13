---
author: Andreas Hümmer
title: Dateisystem-Implementierung
tags:
  - content
  - bs
  - dateisystem
  - implementierung
  - inode
  - blockallokation
  - fat
  - ext4
created: '2026-10-07'
modified: '2026-10-09'
bereich: BS
---

# Dateisystem-Implementierung

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die physische Struktur eines Dateisystems verstehen
> - Verschiedene Blockallokations-Strategien erklären können
> - Die Inode-Struktur und ihre Bedeutung kennen
> - Freispeicherverwaltung mit Bitmaps und Free Lists verstehen
> - Den Buffer Cache und seine Rolle erklären können

---

## Definition

> [!quote] **Formale Definition**
> Die **Dateisystem-Implementierung** definiert, wie Dateien, Verzeichnisse und Metadaten physisch auf dem Speichermedium organisiert werden. Sie umfasst die Datenstrukturen zur Blockallokation, Freispeicherverwaltung und Metadatenspeicherung.

Die Implementierung eines Dateisystems ist das Bindeglied zwischen der abstrakten Sicht (Dateien und Verzeichnisse) und der physischen Realität (Blöcke auf einer Festplatte oder SSD). Während Benutzer und Anwendungen mit Dateinamen und Pfaden arbeiten, muss das Dateisystem diese in konkrete Blockadressen übersetzen und dabei Effizienz, Zuverlässigkeit und Konsistenz gewährleisten.

---

## Physische Struktur eines Dateisystems

### Disk-Layout

Ein Speichermedium wird typischerweise in Bereiche aufgeteilt. Diese Aufteilung ist bei der Formatierung festgelegt und bestimmt maßgeblich die Eigenschaften des Dateisystems:

![[disk-layout.png|center|700]]
*<span class="fig-id">02-07-03-disk-layout</span>: Typische Aufteilung eines Speichermediums in funktionale Bereiche*

### Der Superblock

Der **Superblock** enthält kritische Metadaten über das gesamte Dateisystem:

| Feld | Beschreibung |
|------|--------------|
| **Magic Number** | Identifiziert den Dateisystem-Typ |
| **Blockgröße** | Größe eines Blocks (z.B. 4096 Bytes) |
| **Anzahl Blöcke** | Gesamtzahl der Blöcke |
| **Freie Blöcke** | Anzahl verfügbarer Blöcke |
| **Anzahl Inodes** | Gesamtzahl der Inodes |
| **Freie Inodes** | Anzahl verfügbarer Inodes |
| **Mount-Count** | Wie oft wurde das FS gemountet? |
| **Last Mount Time** | Wann zuletzt gemountet? |
| **FS State** | Clean / Dirty (sauber beendet?) |

> [!warning] **Wichtig**
> Der Superblock ist so kritisch, dass Dateisysteme ihn mehrfach als Backup speichern (z.B. ext4: Kopien in Blockgruppen).

Bei ext4 werden Superblock-Kopien standardmäßig in den Blockgruppen 0, 1 und bei Potenzen von 3, 5 und 7 gespeichert (also Blockgruppen 3, 5, 7, 9, 25, 27, ...). Mit dem Befehl `dumpe2fs` kann man diese Backup-Positionen anzeigen:

```bash
# Superblock-Backups anzeigen
$ sudo dumpe2fs /dev/sda1 | grep -i superblock
Primary superblock at 0, Group descriptors at 1-1
Backup superblock at 32768, Group descriptors at 32769-32769
Backup superblock at 98304, Group descriptors at 98305-98305
```

---

## Blockallokation

Die zentrale Frage der Dateisystem-Implementierung lautet: **Wie werden Datenblöcke einer Datei zugeordnet?** Die Wahl der Allokationsstrategie hat fundamentale Auswirkungen auf Performance, Fragmentierung und maximale Dateigröße. Im Laufe der Jahrzehnte haben sich verschiedene Ansätze entwickelt, jeder mit spezifischen Stärken und Schwächen.

### 1. Zusammenhängende Allokation (Contiguous)

Die einfachste Strategie: Alle Blöcke einer Datei liegen physisch hintereinander auf dem Medium. Das Verzeichnis speichert nur den Startblock und die Länge – mehr Informationen sind nicht nötig, da alle weiteren Blöcke direkt aufeinander folgen.

![[contiguous-alloc.png|center|650]]
*<span class="fig-id">02-07-03-contiguous-alloc</span>: Zusammenhängende Blockallokation – Dateien belegen aufeinanderfolgende Blöcke*

| Vorteile | Nachteile |
|----------|-----------|
| Schneller sequentieller Zugriff | Externe Fragmentierung |
| Einfache Implementierung | Dateigröße muss bekannt sein |
| Random Access effizient | Wachsen schwierig |

**Anwendung:** CD-ROMs, DVDs (Dateien ändern sich nicht)

Das Problem der externen Fragmentierung wird hier besonders deutlich: Nach mehrfachem Löschen und Anlegen von Dateien entstehen "Löcher", die möglicherweise zu klein für neue Dateien sind. Eine Defragmentierung kann helfen, ist aber zeitaufwändig und bei SSDs sogar schädlich.

### 2. Verkettete Allokation (Linked List)

Um die Fragmentierungsprobleme zu lösen, kann jeder Block einen Zeiger auf seinen Nachfolger enthalten. Dadurch können Dateien beliebig über das Medium verstreut sein:

![[linked-alloc.png|center|700]]
*<span class="fig-id">02-07-03-linked-alloc</span>: Verkettete Blockallokation – jeder Block enthält einen Zeiger auf den nächsten*

| Vorteile | Nachteile |
|----------|-----------|
| Keine externe Fragmentierung | Langsamer Random Access (Kette durchlaufen) |
| Dateien können beliebig wachsen | Speicherplatz für Pointer |
| Einfache Freispeicherverwaltung | Pointer-Verlust = Datenverlust |

Der größte Nachteil zeigt sich beim wahlfreien Zugriff: Um Block 1000 einer Datei zu lesen, müssen erst alle 999 vorherigen Blöcke durchlaufen werden, um den Zeigern zu folgen. Dies macht die verkettete Allokation für Datenbanken oder andere Anwendungen mit häufigem Random Access unbrauchbar.

### 3. File Allocation Table (FAT)

Microsoft löste das Random-Access-Problem elegant: Alle Zeiger werden aus den Datenblöcken herausgenommen und in einer zentralen Tabelle – der **File Allocation Table** – gespeichert. Diese Tabelle wird beim Booten komplett in den RAM geladen:

![[fat-alloc.png|center|750]]
*<span class="fig-id">02-07-03-fat-alloc</span>: File Allocation Table – zentrale Tabelle im RAM mit Verkettungsinformationen*

| Vorteile | Nachteile |
|----------|-----------|
| Random Access schneller (FAT im RAM) | FAT kann sehr groß werden |
| Keine Zeiger in Datenblöcken | FAT-Korruption = Totalverlust |
| Einfach zu implementieren | Nicht gut skalierbar |

**Anwendung:** MS-DOS, USB-Sticks (FAT32), SD-Karten

Die 4-GB-Grenze von FAT32 erklärt sich aus der Verwendung von 32-Bit-Einträgen für die Dateigröße im Verzeichniseintrag (2³² Bytes = 4 GB). exFAT wurde später entwickelt, um diese Limitierung für Flash-Speicher zu überwinden.

### 4. Indizierte Allokation (Inodes)

Unix-Systeme verwenden einen anderen Ansatz: Jede Datei erhält einen eigenen Index-Block – den **Inode** (Index Node). Dieser enthält alle Metadaten sowie die Adressen der Datenblöcke. Der entscheidende Trick ist das mehrstufige Indirektionssystem:

![[inode-alloc.png|center|750]]
*<span class="fig-id">02-07-03-inode-alloc</span>: Inode-Struktur mit Direct Blocks und mehrstufiger Indirektion*

**Berechnung der maximalen Dateigröße (4KB Blöcke, 4 Byte Pointer):**

| Ebene | Blöcke | Bei 4KB Blockgröße |
|-------|--------|-------------------|
| 12 Direct | 12 | 48 KB |
| 1 Single Indirect | 1024 | 4 MB |
| 1 Double Indirect | 1024² = 1M | 4 GB |
| 1 Triple Indirect | 1024³ = 1G | 4 TB |
| **Gesamt** | | **~4 TB** |

| Vorteile | Nachteile |
|----------|-----------|
| Schneller Random Access | Overhead für kleine Dateien |
| Kleine Dateien effizient (Direct) | Indirektion kostet Zugriffe |
| Große Dateien möglich | Maximalgröße begrenzt |

**Anwendung:** Unix/Linux (ext2/3/4), macOS (HFS+)

> [!tip] **Praktische Beobachtung**
> Die meisten Dateien auf einem typischen System sind klein (unter 48 KB). Durch die 12 Direct Blocks können diese Dateien ohne jegliche Indirektion gelesen werden – mit nur einem zusätzlichen Disk-Zugriff für den Inode selbst.

Moderne Dateisysteme wie ext4 verwenden zusätzlich **Extents** statt einzelner Blockadressen. Ein Extent beschreibt zusammenhängende Blöcke als (Startblock, Länge)-Paar, was den Overhead für große, nicht-fragmentierte Dateien drastisch reduziert.

```bash
# Inode-Informationen einer Datei anzeigen
$ stat /etc/passwd
  File: /etc/passwd
  Size: 2847        Blocks: 8          IO Block: 4096   regular file
Device: 8,1   Inode: 131074      Links: 1

# Alle Inodes eines Dateisystems anzeigen
$ df -i
Filesystem      Inodes  IUsed   IFree IUse% Mounted on
/dev/sda1      6553600 245789 6307811    4% /
```

---

## Verzeichnis-Implementierung

Verzeichnisse sind letztlich nur spezielle Dateien, die Zuordnungen von Namen zu Inodes (oder bei FAT: zu Startclustern) speichern. Die Art, wie diese Zuordnungen organisiert werden, hat erheblichen Einfluss auf die Performance bei Verzeichnisoperationen.

### Lineare Liste

Die einfachste Implementierung speichert Einträge als Liste von (Name, Inode)-Paaren. Bei einer Suche muss diese Liste sequentiell durchlaufen werden:

![[dir-linear.png|center|650]]
*<span class="fig-id">02-07-03-dir-linear</span>: Verzeichnis als lineare Liste mit Name-Inode-Zuordnungen*

| Vorteile | Nachteile |
|----------|-----------|
| Einfach zu implementieren | Suche O(n) |
| Wenig Overhead | Langsam bei vielen Dateien |

Für typische Home-Verzeichnisse mit wenigen hundert Dateien ist die lineare Suche akzeptabel. Problematisch wird es bei Verzeichnissen mit tausenden Einträgen – etwa Mail-Verzeichnisse im Maildir-Format oder Build-Verzeichnisse großer Projekte.

### Hash-Tabelle

Um die Suchzeit zu verbessern, kann eine Hash-Tabelle über den Dateinamen gelegt werden. Der Hash des Namens bestimmt den Bucket, innerhalb dessen nur noch wenige Einträge linear durchsucht werden müssen:

![[dir-hash.png|center|700]]
*<span class="fig-id">02-07-03-dir-hash</span>: Verzeichnis mit Hash-Tabelle und Kollisionsbehandlung durch Verkettung*

### B-Baum

Für sehr große Verzeichnisse (z.B. NTFS, ext4 mit dir_index) werden B-Bäume verwendet. Diese garantieren logarithmische Suchzeit und sind besonders effizient für sortierte Auflistungen:

| Struktur | Suchzeit | Anwendung |
|----------|----------|-----------|
| Lineare Liste | O(n) | Kleine Verzeichnisse |
| Hash-Tabelle | O(1) avg | Mittlere Verzeichnisse |
| B-Baum | O(log n) | Sehr große Verzeichnisse |

ext4 aktiviert die dir_index-Funktion automatisch bei der Formatierung mit `mkfs.ext4`. Sie kann mit `tune2fs -l /dev/sdXX | grep dir_index` überprüft werden.

---

## Freispeicherverwaltung

Das Dateisystem muss jederzeit wissen, welche Blöcke frei und welche belegt sind. Zwei grundlegende Ansätze haben sich etabliert:

### Bitmap (Bit Vector)

Die eleganteste Lösung: Ein Bit pro Block zeigt den Belegungszustand an (1 = belegt, 0 = frei). Die Bitmap ist kompakt und ermöglicht effiziente Suche nach zusammenhängenden freien Bereichen:

![[bitmap-free.png|center|700]]
*<span class="fig-id">02-07-03-bitmap-free</span>: Bitmap-basierte Freispeicherverwaltung – ein Bit pro Block*

Mit Bit-Operationen können moderne CPUs sehr schnell zusammenhängende Nullen (freie Blöcke) finden. Die Funktion `__builtin_clz` (Count Leading Zeros) oder die SSE-Instruktion `POPCNT` beschleunigen diese Suche erheblich.

### Verkettete Freispeicherliste

Eine Alternative zur Bitmap: Freie Blöcke bilden selbst eine verkettete Liste. Der erste freie Block enthält einen Zeiger auf den nächsten freien Block:

![[freelist.png|center|700]]
*<span class="fig-id">02-07-03-freelist</span>: Verkettete Freispeicherliste – freie Blöcke zeigen auf den nächsten freien Block*

### Grouping und Counting

Optimierungen für Free Lists:

| Methode | Beschreibung |
|---------|--------------|
| **Grouping** | Freie Blöcke speichern Adressen weiterer freier Blöcke |
| **Counting** | (Startblock, Anzahl) statt einzelner Adressen |

Moderne Dateisysteme wie ext4 kombinieren mehrere Ansätze: Bitmaps für die Grundverwaltung, aber mit zusätzlichen Datenstrukturen zur Optimierung der Allokation (z.B. Multi-Block Allocator).

---

## Buffer Cache

### Konzept

Festplatten sind um Größenordnungen langsamer als RAM. Um diese Lücke zu überbrücken, hält der Kernel häufig genutzte Disk-Blöcke im Hauptspeicher – dem **Buffer Cache** (auch Page Cache genannt). Dies ist einer der wichtigsten Performance-Mechanismen moderner Betriebssysteme:

![[buffer-cache.png|center|650]]
*<span class="fig-id">02-07-03-buffer-cache</span>: Buffer Cache als Vermittler zwischen Anwendung und Festplatte*

### Write-Strategien

Die Wahl der Write-Strategie ist ein klassischer Trade-off zwischen Performance und Datensicherheit:

| Strategie | Beschreibung | Trade-off |
|-----------|--------------|-----------|
| **Write-Through** | Sofort auf Disk schreiben | Sicher, aber langsam |
| **Write-Back** | Verzögert schreiben (bei Cache-Eviction) | Schnell, aber Datenverlust-Risiko |
| **Write-Behind** | Asynchron im Hintergrund schreiben | Kompromiss |

Linux verwendet standardmäßig Write-Back mit periodischem Zurückschreiben (alle 5 Sekunden durch den `pdflush`/`writeback`-Kernel-Thread). Bei einem Stromausfall können bis zu 5 Sekunden an Änderungen verloren gehen – daher die Wichtigkeit von [[04-Journaling|Journaling]].

```bash
# Linux: Dirty Pages manuell auf Disk schreiben
$ sync

# Dirty Page Statistics
$ cat /proc/meminfo | grep -i dirty
Dirty:               1024 kB
Writeback:              0 kB
```

### Cache-Ersetzungsstrategien

| Algorithmus | Beschreibung |
|-------------|--------------|
| **LRU** | Least Recently Used - Ältester Zugriff wird verdrängt |
| **LFU** | Least Frequently Used - Seltenster Zugriff wird verdrängt |
| **Clock** | Approximation von LRU (effizienter) |

Linux verwendet eine Variante namens **2Q** (Two-Queue), die zwischen einmalig und mehrfach zugegriffenen Seiten unterscheidet. Dies verhindert, dass ein einmaliger großer Dateiscan den gesamten Cache verdrängt.

```bash
# Cache-Statistiken anzeigen
$ free -h
              total        used        free      shared  buff/cache   available
Mem:           15Gi       4.2Gi       2.1Gi       512Mi       9.1Gi        10Gi

# Die 9.1 GB "buff/cache" sind der Buffer/Page Cache
# "available" zeigt, wieviel RAM inkl. Cache verfügbar wäre
```

---

## Vergleich: FAT vs. ext4 vs. NTFS

Die folgende Tabelle fasst die wichtigsten Unterschiede der drei verbreitetsten Dateisysteme zusammen. Die Wahl des richtigen Dateisystems hängt vom Einsatzzweck ab:

| Aspekt | FAT32 | ext4 | NTFS |
|--------|-------|------|------|
| **Blockallokation** | FAT-Tabelle | Inodes + Extents | MFT + Runs |
| **Max. Dateigröße** | 4 GB | 16 TB | 16 TB |
| **Max. Volumegröße** | 2 TB | 1 EB | 256 TB |
| **Journaling** | Nein | Ja | Ja |
| **Berechtigungen** | Keine | Unix rwx + ACL | ACL |
| **Fragmentierung** | Hoch | Niedrig (Extents) | Mittel |
| **Anwendung** | USB-Sticks, SD | Linux | Windows |

> [!tip] **Praxistipp: Dateisystemwahl**
> - **FAT32/exFAT**: Für Wechselmedien, die zwischen verschiedenen Betriebssystemen ausgetauscht werden
> - **ext4**: Für Linux-Systeme, Server, und überall wo Zuverlässigkeit und Performance wichtig sind
> - **NTFS**: Für Windows-Systeme und Dual-Boot-Konfigurationen (Linux kann NTFS lesen/schreiben via ntfs-3g)

### Übersicht gängiger Dateisysteme

Die folgende Tabelle gibt einen umfassenden Überblick über die wichtigsten Dateisysteme, ihre technischen Grenzen und typischen Einsatzgebiete:

| Dateisystem | Max. Dateigröße | Max. Volumegröße | Journaling | Typische Anwendung |
|-------------|-----------------|------------------|------------|-------------------|
| **FAT16** | 2 GB | 2 GB | Nein | Legacy-Systeme, kleine Speicherkarten |
| **FAT32** | 4 GB | 2 TB | Nein | USB-Sticks, SD-Karten, Spielekonsolen |
| **exFAT** | 16 EB | 128 PB | Nein | Große SD-Karten (SDXC), Kamera-Speicher |
| **NTFS** | 16 TB | 256 TB | Ja | Windows-Systeme, externe Festplatten |
| **ReFS** | 35 PB | 35 PB | Ja | Windows Server, Hyper-V, Speicherpools |
| **ext2** | 2 TB | 32 TB | Nein | Boot-Partitionen, Flash-Speicher (wenig Writes) |
| **ext3** | 2 TB | 32 TB | Ja | Ältere Linux-Systeme |
| **ext4** | 16 TB | 1 EB | Ja | Standard-Linux, Server, Desktops |
| **XFS** | 8 EB | 8 EB | Ja | Große Dateien, Medienserver, Enterprise |
| **Btrfs** | 16 EB | 16 EB | Ja (CoW) | Snapshots, RAID, Container-Hosts |
| **ZFS** | 16 EB | 256 ZB | Ja (CoW) | NAS, Datenspeicher, Deduplizierung |
| **HFS+** | 8 EB | 8 EB | Ja | macOS (bis Mojave), Time Machine |
| **APFS** | 8 EB | 8 EB | Ja (CoW) | macOS (ab High Sierra), iOS, SSDs |
| **F2FS** | 4 TB | 16 TB | Ja | Android, Flash-Speicher, SSDs |
| **ISO 9660** | 4 GB | 8 TB | Nein | CD-ROMs, DVD-ROMs |
| **UDF** | 16 EB | 2 TB | Nein | DVDs, Blu-rays, Wechselmedien |

> [!info] **Legende**
> - **EB** = Exabyte (10¹⁸ Bytes), **PB** = Petabyte (10¹⁵ Bytes), **ZB** = Zettabyte (10²¹ Bytes)
> - **CoW** = Copy-on-Write (Daten werden nie überschrieben, sondern neu geschrieben)

#### Besondere Merkmale ausgewählter Dateisysteme

| Dateisystem | Besondere Features |
|-------------|-------------------|
| **Btrfs** | Snapshots, Subvolumes, transparente Kompression, integriertes RAID, Online-Defragmentierung |
| **ZFS** | Prüfsummen für alle Daten, Deduplizierung, Snapshots, RAID-Z, Self-Healing |
| **APFS** | Space Sharing zwischen Volumes, native Verschlüsselung, Clones, optimiert für Flash |
| **XFS** | Excellent für sehr große Dateien, parallele I/O, Online-Vergrößerung |
| **F2FS** | Flash-Friendly, Log-structured, minimiert Write Amplification |
| **ReFS** | Integrity Streams, automatische Fehlerkorrektur mit Storage Spaces |

---

## Zusammenhänge

- [[01-Historie-Festplatten|Geschichte der Festplatten]] → Hardware-Grundlagen verstehen
- [[02-Grundlagen|Grundlagen]] → Logische Sicht auf Dateisysteme
- [[04-Journaling|Journaling]] → Absicherung der Datenstrukturen
- [[../06-Ein-Ausgabe/01-IO-Grundlagen|I/O-Grundlagen]] → Block-I/O und Caching
- [[../05-Speicherverwaltung/03-Paging|Paging]] → Page Cache nutzt Paging-Infrastruktur

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
>N/A

> [!question] **Häufige Prüfungsfragen**
> 1. Vergleichen Sie zusammenhängende, verkettete und indizierte Blockallokation!
> 2. Berechnen Sie die maximale Dateigröße bei gegebener Inode-Struktur!
> 3. Warum ist FAT für große Dateisysteme problematisch?
> 4. Erklären Sie die Vor- und Nachteile von Bitmap vs. Free List!
> 5. Was ist der Unterschied zwischen Write-Through und Write-Back?

> [!tip] **Merkhilfen**
> - **FAT** = "Inhaltsverzeichnis eines Buches" (zentrale Tabelle)
> - **Inode** = "Karteikarte mit allen Infos außer dem Namen"
> - **Bitmap** = "Sitzplan im Kino" (belegt/frei auf einen Blick)
> - **Buffer Cache** = "Schreibtisch" (Arbeitskopien im schnellen Zugriff)

---

## Weiterführende Ressourcen

> [!note] **Videos (YouTube)**
>
> | | Video | Beschreibung |
> |---|-------|--------------|
> | 🎬 | [Neso Academy – File Allocation Methods](https://www.youtube.com/watch?v=mzUyMy7Ihk0) | Allokationsstrategien |
> | 🎬 | [Linux Filesystem - inodes](https://www.youtube.com/watch?v=tMVj22EWg6A) | Inode-Struktur erklärt |

---

## Quellen

- Tanenbaum, A. S.: Modern Operating Systems, Kapitel 4.3-4.4
- Silberschatz, Galvin, Gagne: Operating System Concepts, Kapitel 14
- Love, R.: Linux Kernel Development, Kapitel 13
- ext4 Documentation: https://www.kernel.org/doc/html/latest/filesystems/ext4/
