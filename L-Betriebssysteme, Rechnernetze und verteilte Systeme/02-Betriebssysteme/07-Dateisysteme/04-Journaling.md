---
author: Andreas Hümmer
title: Journaling-Dateisysteme
tags:
  - content
  - bs
  - dateisystem
  - journaling
  - crash-recovery
  - konsistenz
  - ext4
  - ntfs
created: '2026-10-07'
modified: '2026-10-09'
bereich: BS
---

# Journaling-Dateisysteme

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das Problem der Dateisystem-Inkonsistenz verstehen
> - Das Prinzip des Journaling erklären können
> - Verschiedene Journaling-Modi (Metadata-Only, Full Data) unterscheiden
> - Den Ablauf einer journaled Transaction beschreiben können
> - Die Trade-offs zwischen Sicherheit und Performance kennen

---

## Definition

> [!quote] **Formale Definition**
> Ein **Journaling-Dateisystem** protokolliert geplante Änderungen in einem separaten **Journal** (Log), bevor sie auf das eigentliche Dateisystem angewendet werden. Bei einem Systemabsturz kann das Journal verwendet werden, um das Dateisystem schnell und konsistent wiederherzustellen.

Das Konzept stammt aus der Welt der Datenbanken, wo Transaktions-Logs seit den 1970er Jahren Standard sind. Die Idee wurde in den 1990er Jahren auf Dateisysteme übertragen, als Festplatten immer größer wurden und die traditionelle Konsistenzprüfung nach einem Absturz untragbar lange dauerte. Heute ist Journaling in praktisch allen modernen Dateisystemen implementiert – von ext4 über NTFS bis hin zu APFS.

---

## Das Problem: Inkonsistenz nach Absturz

### Warum sind Abstürze problematisch?

Ein Dateisystem ist kein monolithischer Block, sondern ein komplexes Geflecht aus miteinander verknüpften Datenstrukturen: Superblock, Inode-Tabellen, Datenblöcke, Verzeichniseinträge und Bitmaps für die Freispeicherverwaltung. Diese Strukturen müssen stets konsistent zueinander sein – ein Verzeichniseintrag muss auf einen gültigen Inode zeigen, ein Inode muss auf tatsächlich allozierte Blöcke verweisen, und die Bitmap muss den tatsächlichen Belegungszustand widerspiegeln.

Das Problem: Eine scheinbar einfache Operation wie "Datei erstellen" erfordert Änderungen an mehreren dieser Strukturen. Wenn der Strom ausfällt oder der Kernel abstürzt, während diese Änderungen nur teilweise durchgeführt wurden, bleibt das Dateisystem in einem inkonsistenten Zustand zurück.

Eine Dateisystem-Operation besteht oft aus **mehreren Schritten**, die zusammengehören:

**Beispiel: Neue Datei "report.txt" erstellen**

| Schritt | Operation | Betroffene Struktur |
|---------|-----------|---------------------|
| 1 | Freien Inode finden und reservieren | Inode-Bitmap |
| 2 | Inode mit Metadaten initialisieren | Inode-Tabelle |
| 3 | Datenblöcke allozieren und schreiben | Block-Bitmap, Datenbereich |
| 4 | Verzeichniseintrag hinzufügen | Verzeichnisblock |
| 5 | Superblock aktualisieren (freie Inodes) | Superblock |
| 6 | Bitmap aktualisieren (belegte Blöcke) | Block-Bitmap |

> [!danger] **Crash-Szenarien**
> 
> **⚡ Absturz zwischen Schritt 3 und 4:**
> - Inode existiert und zeigt auf Datenblöcke
> - Aber: Kein Verzeichniseintrag verweist darauf!
> - → **"Orphan Inode"** – Speicher belegt, aber für Benutzer nicht erreichbar
> 
> **⚡ Absturz zwischen Schritt 4 und 6:**
> - Verzeichnis verweist auf Inode
> - Aber: Bitmap zeigt Blöcke noch als "frei"!
> - → **Doppelte Allokation möglich** – andere Dateien könnten dieselben Blöcke bekommen → Datenverlust

### Traditionelle Lösung: fsck

Ohne Journaling muss nach einem Absturz das gesamte Dateisystem überprüft werden. Das Programm `fsck` (File System Consistency Check) durchsucht systematisch alle Datenstrukturen und versucht, Inkonsistenzen zu finden und zu reparieren. Bei einem 1-TB-Dateisystem mit Millionen von Dateien kann dieser Prozess leicht mehrere Stunden dauern – während dieser Zeit ist das System unbenutzbar.

```bash
# Filesystem Check (kann Stunden dauern!)
$ fsck /dev/sda1
```

In Serverumgebungen ist solche Downtime inakzeptabel. Ein Datenbankserver, der nach einem Stromausfall stundenlang offline ist, verursacht erhebliche Kosten. Dies war der Hauptantrieb für die Entwicklung von Journaling-Dateisystemen.

| Problem mit fsck | Auswirkung |
|------------------|------------|
| Scannt gesamte Disk | Sehr langsam (TB-Größe = Stunden) |
| Inkonsistenzen finden | Komplexe Heuristiken |
| Reparatur unsicher | Daten können verloren gehen |
| Downtime | System unbenutzbar während Check |

> [!tip] **Praxis: fsck bei ext4**
> Bei ext4 mit Journaling wird fsck normalerweise nur alle paar Monate oder nach einer bestimmten Anzahl von Mounts durchgeführt – als präventive Maßnahme, nicht als Notfallreparatur. Die eigentliche Crash-Recovery übernimmt das Journal.

---

## Die Lösung: Journaling

### Grundprinzip: Write-Ahead Logging

**Idee:** Bevor eine Änderung durchgeführt wird, wird sie im Journal protokolliert.

Das Prinzip ist simpel, aber elegant: Statt Änderungen direkt auf das Dateisystem zu schreiben, werden sie zunächst in einem separaten Bereich – dem Journal – protokolliert. Erst nachdem das Journal erfolgreich geschrieben wurde (der "Commit"), werden die Änderungen auf das eigentliche Dateisystem angewendet.

Der entscheidende Vorteil: Das Journal ist klein und sequentiell organisiert. Nach einem Absturz muss nur das Journal gelesen werden (Millisekunden bis Sekunden), nicht das gesamte Dateisystem (Minuten bis Stunden). Aus dem Journal lässt sich eindeutig ableiten, welche Transaktionen vollständig waren und welche nicht.

![[journaling-prinzip.png|center|700]]
*<span class="fig-id">02-07-04-journaling-prinzip</span>: Vergleich – ohne vs. mit Journaling bei einem Systemabsturz*

### Transaktionsablauf

Eine Transaktion im Dateisystem-Journal folgt dem klassischen ACID-Prinzip aus der Datenbankwelt: Die Änderungen sind atomar (ganz oder gar nicht), konsistent (Invarianten bleiben erhalten), isoliert (andere Operationen sehen nur den Endzustand) und dauerhaft (nach dem Commit sind sie persistent).

Der Ablauf einer typischen Journal-Transaktion:

![[journal-transaktion.png|center|700]]
*<span class="fig-id">02-07-04-journal-transaktion</span>: Ablauf einer Journal-Transaktion mit den 5 Phasen*

**Crash-Szenarien und Recovery-Verhalten:**

| Szenario | Zeitpunkt | Recovery-Aktion |
|----------|-----------|-----------------|
| **A** | Crash vor Commit | Transaktion verwerfen (undo) – keine Änderungen wurden bestätigt |
| **B** | Crash nach Commit | Transaktion wiederholen (redo) – Änderungen waren bestätigt, aber evtl. noch nicht angewendet |
| **C** | Crash nach Apply | Alles OK – Journal aufräumen, Transaktion war vollständig |

---

## Journaling-Modi

Die verschiedenen Journaling-Modi repräsentieren unterschiedliche Kompromisse zwischen Datensicherheit und Performance. Je mehr Daten ins Journal geschrieben werden, desto sicherer, aber auch desto langsamer wird das System.

### 1. Metadata-Only Journaling (Writeback Mode)

Nur **Metadaten** werden ins Journal geschrieben:

**Was wird geloggt:**
- ✓ Inode-Änderungen
- ✓ Verzeichniseinträge
- ✓ Bitmap-Änderungen
- ✓ Superblock-Änderungen
- ✗ Dateiinhalte (Datenblöcke)

![[metadata-journaling.png|center|650]]
*<span class="fig-id">02-07-04-metadata-journaling</span>: Metadata-Only Journaling – nur Metadaten werden geloggt, Daten gehen direkt auf die Disk*

| Vorteile | Nachteile |
|----------|-----------|
| Schneller (weniger I/O) | Daten können nach Crash inkonsistent sein |
| Dateisystem-Struktur immer konsistent | "Stale Data" möglich |
| Standard bei ext4 | Nicht für kritische Daten |

> [!warning] **Stale Data Problem**
> Nach einem Absturz kann eine Datei alte Daten enthalten, wenn der neue Inode bereits geschrieben wurde, aber die neuen Datenblöcke noch nicht.

### 2. Ordered Mode (ext4 Default)

Metadaten werden geloggt, Daten werden **vor** den Metadaten geschrieben:

Der Ordered Mode ist der clevere Kompromiss, der in ext4 standardmäßig verwendet wird. Die Idee: Datenblöcke müssen nicht ins Journal, solange garantiert ist, dass sie auf der Disk sind, bevor die zugehörigen Metadaten committet werden. So zeigen Metadaten niemals auf Blöcke, die noch nicht geschrieben wurden.

![[ordered-mode.png|center|700]]
*<span class="fig-id">02-07-04-ordered-mode</span>: Ordered Mode – Reihenfolge garantiert: Daten vor Metadaten*

| Vorteile | Nachteile |
|----------|-----------|
| Kein Stale Data Problem | Langsamer als Writeback |
| Guter Kompromiss | Daten können verloren gehen |
| ext4 Default | (Aber: Struktur bleibt konsistent) |

### 3. Full Data Journaling (Journal Mode)

**Alle Daten und Metadaten** werden ins Journal geschrieben:

Dies ist der sicherste, aber auch langsamste Modus. Jedes Byte wird zweimal geschrieben: erst ins Journal, dann an seinen endgültigen Platz. Für normale Desktopanwendungen ist dieser Overhead unnötig, aber für Datenbanken oder andere kritische Anwendungen kann er sich lohnen – die Garantie, dass keine Daten verloren gehen, ist den Performance-Verlust wert.

![[full-data-journaling.png|center|700]]
*<span class="fig-id">02-07-04-full-data-journaling</span>: Full Data Journaling – alle Daten werden zweimal geschrieben*

| Vorteile | Nachteile |
|----------|-----------|
| Maximale Sicherheit | Doppelte Schreiblast |
| Alle Daten wiederherstellbar | Deutlich langsamer |
| Für kritische Anwendungen | Mehr Journal-Platz nötig |

### Vergleich der Modi

| Modus | Sicherheit | Performance | Anwendung |
|-------|------------|-------------|-----------|
| **Writeback** | Metadaten | Schnell | Temporäre Daten |
| **Ordered** | Metadaten + Datenreihenfolge | Mittel | Allgemein (ext4 Default) |
| **Journal** | Alles | Langsam | Datenbanken, kritische Systeme |

```bash
# ext4: Journaling-Modus setzen
$ mount -o data=journal /dev/sda1 /mnt      # Full Data
$ mount -o data=ordered /dev/sda1 /mnt      # Ordered (Default)
$ mount -o data=writeback /dev/sda1 /mnt    # Metadata only

# Aktuellen Modus prüfen
$ cat /proc/mounts | grep /dev/sda1

# Bei der Formatierung kann auch die Journal-Größe festgelegt werden
$ mkfs.ext4 -J size=256 /dev/sda1           # 256 MB Journal
```

> [!info] **Wann welchen Modus verwenden?**
> - **Ordered** (Default): Für die meisten Anwendungsfälle die beste Wahl
> - **Journal**: Für Datenbanken auf Dateisystemebene (PostgreSQL auf ext4), Mailserver, oder wenn absolute Datensicherheit kritisch ist
> - **Writeback**: Nur für temporäre Daten oder wenn die Anwendung selbst für Konsistenz sorgt (z.B. Datenbanken mit eigenem WAL)

---

## Recovery-Prozess

Der Recovery-Prozess nach einem Absturz ist der eigentliche Grund, warum sich der Overhead des Journaling lohnt. Statt das gesamte Dateisystem zu scannen, muss nur ein kleines, sequentiell organisiertes Journal durchgelesen werden.

### Ablauf nach Systemstart

![[crash-recovery.png|center|700]]
*<span class="fig-id">02-07-04-crash-recovery</span>: Ablauf der Crash Recovery nach einem Systemabsturz*

> [!success] **Dauer: Sekunden statt Minuten/Stunden**
> Im Vergleich zu `fsck` ist die Journal-basierte Recovery extrem schnell, da nur das kleine Journal gelesen werden muss – nicht das gesamte Dateisystem.

---

## Journaling in der Praxis

### ext4 Journal-Struktur

Das Journal von ext4 wird durch das JBD2 (Journaling Block Device 2) Subsystem verwaltet. Es ist als Ringpuffer organisiert: Neue Transaktionen werden am Ende angefügt, und sobald eine Transaktion vollständig auf das Dateisystem angewendet wurde (Checkpoint), kann ihr Platz im Journal für neue Transaktionen wiederverwendet werden.

![[ext4-journal.png|center|700]]
*<span class="fig-id">02-07-04-ext4-journal</span>: Struktur des ext4 Journals (JBD2) als Ring Buffer*

| Konzept | Beschreibung |
|---------|--------------|
| **Ring Buffer** | Älteste Transaktionen werden überschrieben, wenn Platz benötigt wird |
| **Checkpoint** | Nach einem Checkpoint sind Transaktionen nicht mehr nötig → Platz wird frei |

```bash
# ext4 Journal-Info anzeigen
$ dumpe2fs /dev/sda1 | grep -i journal
Journal inode:            8
Journal backup:           inode blocks
Journal features:         journal_incompat_revoke
Journal size:             128M
Journal length:           32768
Journal sequence:         0x00012345

# Journal-Statistiken in Echtzeit
$ cat /proc/fs/jbd2/sda1-8/info
```

Die typische Journalgröße liegt zwischen 64 MB und 256 MB – winzig im Vergleich zu modernen Festplatten, aber groß genug, um mehrere Sekunden an Transaktionen zu puffern.

### NTFS Journaling

NTFS verwendet zwei Log-Mechanismen:

| Log | Zweck |
|-----|-------|
| **$LogFile** | Transaktions-Log für Metadaten (ähnlich ext4 Journal) |
| **$UsnJrnl** | Change Journal (protokolliert alle Änderungen für Anwendungen) |

Das NTFS-$LogFile funktioniert konzeptionell sehr ähnlich wie das ext4-Journal: Metadaten-Änderungen werden protokolliert, bevor sie angewendet werden. Das $UsnJrnl (Update Sequence Number Journal) hat einen anderen Zweck: Es protokolliert alle Dateiänderungen chronologisch, sodass Anwendungen wie Backup-Software oder Virenscanner effizient erkennen können, welche Dateien sich seit dem letzten Scan geändert haben.

```powershell
# Windows: NTFS Journal-Status prüfen
fsutil usn queryjournal C:

# Letzten 10 Journal-Einträge anzeigen
fsutil usn readjournal C: | head -100
```

### Copy-on-Write als Alternative

Einige moderne Dateisysteme (ZFS, Btrfs, APFS) verwenden **Copy-on-Write** (CoW) statt klassischem Journaling. Der fundamentale Unterschied: Statt Daten an ihrem ursprünglichen Ort zu überschreiben und die Änderung zu loggen, werden Daten immer an einem neuen Ort geschrieben. Der Pointer zum alten Ort wird erst dann atomar aktualisiert, wenn die neuen Daten vollständig geschrieben sind.

![[copy-on-write.png|center|700]]
*<span class="fig-id">02-07-04-copy-on-write</span>: Vergleich von In-Place Update und Copy-on-Write*

| Vorteile | Nachteile |
|----------|-----------|
| Kein Journal nötig | Fragmentierung |
| Snapshots "kostenlos" | Write Amplification |
| Atomare Updates | |

---

## Performance-Überlegungen

### Write Amplification

Der Begriff "Write Amplification" beschreibt, wie viel mehr Daten tatsächlich geschrieben werden müssen, als die Anwendung angefordert hat. Journaling erhöht diesen Faktor, weil Daten (teilweise) doppelt geschrieben werden.

| Methode | Schreibfaktor | Erklärung |
|---------|---------------|-----------|
| Kein Journaling | 1× | Direkt schreiben |
| Metadata Journaling | ~1.1× | Nur Metadaten doppelt |
| Full Data Journaling | 2× | Alles doppelt |
| Copy-on-Write | ~1.5× | Variiert mit Fragmentierung |

Bei SSDs ist Write Amplification besonders relevant, da Flash-Speicher eine begrenzte Anzahl von Schreibzyklen pro Zelle verkraftet. Ein Dateisystem mit niedriger Write Amplification verlängert die Lebensdauer der SSD.

### Optimierungen

Moderne Journaling-Implementierungen verwenden verschiedene Techniken, um den Performance-Overhead zu minimieren:

- **Barrier-I/O**: Garantiert Schreibreihenfolge bei Write-Caches. Ohne Barriers könnte der Disk-Cache Schreiboperationen umsortieren und das Journal würde nicht mehr zuverlässig funktionieren.
- **Delayed Allocation**: Blöcke werden erst bei Commit tatsächlich alloziert. Dies erlaubt dem Dateisystem, zusammenhängende Bereiche zu finden und Fragmentierung zu vermeiden.
- **Extent-basiertes Journal**: Zusammenhängende Bereiche werden als (Start, Länge)-Paar geloggt statt als Liste einzelner Blöcke.
- **Compound Transactions**: Mehrere kleine Operationen werden zu einer großen Transaktion zusammengefasst, um den Commit-Overhead zu reduzieren.

```bash
# Barrier-I/O Status prüfen (Linux)
$ cat /sys/block/sda/queue/write_cache
write back

# Barrier explizit aktivieren/deaktivieren
$ mount -o barrier=1 /dev/sda1 /mnt    # Aktivieren (default)
$ mount -o barrier=0 /dev/sda1 /mnt    # Deaktivieren (gefährlich!)
```

> [!warning] **Vorsicht bei deaktivierten Barriers**
> Das Deaktivieren von Write-Barriers kann die Performance verbessern, aber gefährdet die Datenintegrität bei einem Absturz. Nur verwenden, wenn das Storage-System eigene Absicherungen bietet (z.B. batteriegepufferter RAID-Controller).

---

## Praktische Szenarien und häufige Probleme

### Journal voll

Wenn das Journal schneller gefüllt wird als Transaktionen abgeschlossen (Checkpoint) werden können, blockiert das Dateisystem neue Schreiboperationen. Dies tritt typischerweise bei sehr hoher I/O-Last auf.

```bash
# Journal-Auslastung bei ext4 überwachen
$ cat /proc/fs/jbd2/sda1-8/info
# Zeigt u.a. "waiting" Transaktionen

# Wenn das Journal oft voll läuft: Größe erhöhen
# (erfordert Neuformatierung oder tune2fs bei ext4)
$ tune2fs -J size=256 /dev/sda1
```

### Externe Journals

Bei sehr I/O-intensiven Workloads kann das Journal auf ein separates, schnelleres Gerät ausgelagert werden – typischerweise eine NVMe-SSD für das Journal, während die Daten auf günstigeren HDDs liegen.

```bash
# Externes Journal erstellen
$ mke2fs -O journal_dev /dev/nvme0n1p1

# Dateisystem mit externem Journal formatieren
$ mkfs.ext4 -J device=/dev/nvme0n1p1 /dev/sda1
```

### Journaling und SSDs

SSDs haben ihre eigene Komplexität: Der Flash Translation Layer (FTL) in der SSD führt intern ebenfalls eine Art Log-basierte Verwaltung durch. Das Zusammenspiel von Dateisystem-Journal und FTL kann zu unerwarteten Effekten führen:

- **Doppeltes Logging**: Sowohl das Dateisystem als auch die SSD loggen Änderungen
- **TRIM/DISCARD**: Informiert die SSD über gelöschte Blöcke, damit sie intern aufräumen kann
- **Write Amplification**: Addiert sich zwischen Dateisystem und SSD

```bash
# TRIM aktivieren für bessere SSD-Performance
$ mount -o discard /dev/sda1 /mnt

# Oder periodisches TRIM via fstrim
$ fstrim -v /
```

---

## Zusammenhänge

- [[01-Historie-Festplatten|Geschichte der Festplatten]] → Warum Crash-Recovery nötig ist
- [[02-Grundlagen|Grundlagen]] → Warum Konsistenz wichtig ist
- [[03-Implementierung|Implementierung]] → Welche Strukturen geloggt werden
- [[../06-Ein-Ausgabe/01-IO-Grundlagen|I/O-Grundlagen]] → Write-Back Cache und Journaling
- [[../04-Synchronisation/01-Einfuehrung-Synchronisation|Synchronisation]] → Transaktionen als Synchronisationskonzept

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - Warum Journaling nötig ist (Inkonsistenz-Problem)

> [!question] **Häufige Prüfungsfragen**
> 1. Was ist das Problem bei Dateisystem-Updates ohne Journaling?
> 2. Erklären Sie den Unterschied zwischen Ordered Mode und Journal Mode!
> 3. Wie läuft die Crash-Recovery bei einem Journaling-Dateisystem ab?
> 4. Warum ist Full Data Journaling langsamer, aber sicherer?
> 5. Was ist Copy-on-Write und wie unterscheidet es sich von Journaling?

> [!tip] **Merkhilfen**
> - **Journal** = "Flugschreiber" des Dateisystems
> - **Write-Ahead** = "Erst aufschreiben, dann tun" (wie eine Checkliste)
> - **Checkpoint** = "Alles erledigt, Checkliste abhaken"
> - **Recovery** = "Checkliste durchgehen: Was ist noch offen?"

---

## Weiterführende Ressourcen

> [!note] **Videos (YouTube)**
>
> | | Video | Beschreibung |
> |---|-------|--------------|
> | 🎬 | [Computerphile – Journaling File Systems](https://www.youtube.com/watch?v=x3SHYczYOuk) | Verständliche Erklärung |
> | 🎬 | [MIT OCW – Crash Recovery](https://www.youtube.com/watch?v=0jJcS6FkHPU) | Akademische Perspektive |

---

## Quellen

- Tanenbaum, A. S.: Modern Operating Systems, Kapitel 4.3.5
- Silberschatz, Galvin, Gagne: Operating System Concepts, Kapitel 14.7
- Tweedie, S.: Journaling the Linux ext2fs Filesystem
- ext4 Documentation: https://www.kernel.org/doc/html/latest/filesystems/ext4/journal.html
