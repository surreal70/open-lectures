---
author: Andreas Hümmer
title: Geschichte der Festplatten
tags:
  - content
  - bs
  - dateisystem
  - historie
  - hdd
  - ssd
  - speicher
created: '2026-10-09'
modified: '2026-10-09'
bereich: BS
---

# Geschichte der Festplatten

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Evolution der Speichertechnologie von Lochkarten bis SSDs kennen
> - Den Aufbau und die Funktionsweise von HDDs verstehen
> - Die physischen Parameter (Zylinder, Köpfe, Sektoren) erklären können
> - Den Unterschied zwischen HDD und SSD aus Betriebssystem-Sicht kennen
> - Verstehen, warum diese Historie für moderne Dateisysteme relevant ist

---

## Warum Geschichte?

Die Architektur moderner Dateisysteme ist tief geprägt von den **physischen Eigenschaften** der Speichermedien, für die sie entwickelt wurden. Viele Konzepte (Blöcke, Sektoren, Scheduling-Algorithmen) machen nur Sinn, wenn man die Hardware versteht.

> [!tip] **Merke**
> Selbst auf SSDs verwenden wir Begriffe wie "Sektor" und "Block" – Relikte aus der mechanischen Ära.

---

## Evolution der Speichermedien

### Von Lochkarten zu Random Access

Bevor es Festplatten gab, war Datenspeicherung **sequentiell**. Lochkarten und Magnetbänder mussten von Anfang bis Ende gelesen werden, um einen bestimmten Datensatz zu finden – wie das Vorspulen einer Musikkassette.

Die Entwicklung der Festplatte war ein **Paradigmenwechsel**: Zum ersten Mal konnte der Computer direkt zu beliebigen Daten springen. Dieses "Random Access"-Prinzip ist die Grundlage aller modernen Dateisysteme.

### Zeitleiste

| Jahr | Meilenstein | Bedeutung |
|------|-------------|-----------|
| 1725 | Lochkarten (Jacquard-Webstuhl) | Erste programmierbare Maschine |
| 1890 | Hollerith-Lochkarten | US Census, Gründung von IBM |
| 1928 | Magnetband (Fritz Pfleumer) | Sequentieller Massenspeicher |
| **1956** | **★ IBM RAMAC 305** | **Erste Festplatte** – 5 MB, 1 Tonne |
| 1973 | IBM Winchester (3340) | Sealed Head/Disk Assembly |
| 1980 | Seagate ST-506 | Erste 5.25" HDD für PCs (5 MB) |
| 1983 | 3.5" Formfaktor | Standard für Desktop-PCs |
| 1988 | 2.5" Festplatten | Ermöglicht Laptops |
| 1991 | Erste SSD (SanDisk) | 20 MB für $1000 |
| 2000er | Perpendicular Recording | Kapazitätssprung auf TB-Bereich |
| 2007 | SSDs werden erschwinglich | Consumer-Markt öffnet sich |
| **2020** | **★ NVMe SSDs dominieren** | **HDDs nur noch für Archiv/Server** |

### IBM RAMAC 305 (1956)

Die **erste kommerzielle Festplatte** der Welt markierte den Beginn der Ära des Random-Access-Speichers. Entwickelt von IBM in San Jose, Kalifornien, war sie das Ergebnis von fünf Jahren Forschung unter der Leitung von Rey Johnson.

![[ibmramac305.png|center|500]]
*<span class="fig-id">02-07-01-ibmramac305</span>: IBM RAMAC 305 (1956) – die erste kommerzielle Festplatte der Welt (Quelle: tutorialsprogramacionya.com)*

| Eigenschaft | RAMAC 305 | Moderne HDD (2026) |
|-------------|-----------|-------------------|
| Kapazität | 5 MB | 20 TB |
| Platten | 50 Scheiben (24") | 8-10 Scheiben (3.5") |
| Gewicht | 1 Tonne | 700 g |
| Zugriffszeit | 600 ms | 4 ms |
| Preis | $35.000/Jahr Miete | €50-300 Kauf |
| $/MB | $7.000 | $0,000015 |

Die 5 MB Kapazität entsprach damals etwa **64.000 Lochkarten** – ein ganzer Raum voller Karten konnte durch einen einzigen Schrank ersetzt werden.

> [!info] Namensherkunft
> RAMAC = **R**andom **A**ccess **M**ethod of **A**ccounting and **C**ontrol. Das "Random Access" war die Revolution: Erstmals konnte man direkt auf beliebige Daten zugreifen, statt wie bei Magnetbändern sequentiell suchen zu müssen.

### IBM Winchester (1973)

Der Begriff "Winchester" wurde zum Synonym für Festplatten. Das IBM 3340 führte zwei entscheidende Innovationen ein:

1. **Sealed Head/Disk Assembly**: Köpfe und Platten in einem luftdichten Gehäuse
2. **Flying Head**: Der Lesekopf "schwebt" auf einem Luftpolster über der rotierenden Platte

![[IBM_1403_printer_and_IBM_3340_HDD's.jpg|center|500]]
*<span class="fig-id">02-07-01-ibm3340</span>: IBM 3340 Winchester Festplatten (1973) – die Technologie wurde zum Standard für alle HDDs (Foto: Marcin Wichary, CC BY 2.0, via Wikimedia Commons)*

Diese Technologie ist bis heute die Grundlage aller HDDs. Der Name "Winchester" entstand intern bei IBM – angeblich wegen der geplanten zwei 30-MB-Module (30-30), die an das Winchester-Gewehr erinnerten.

### Der PC-Boom (1980er)

Mit dem IBM PC (1981) und seinen Klonen entstand der Massenmarkt für Festplatten. Die Formfaktoren schrumpften dabei kontinuierlich von 8" über 5,25" auf 3,5".

![[IBM_old_hdd.jpg|center|500]]
*<span class="fig-id">02-07-01-ibm-old-hdd</span>: IBM-Festplatte aus der frühen PC-Ära – diese Laufwerke waren groß, laut und hatten Kapazitäten im einstelligen MB-Bereich (Foto: Appaloosa, CC BY-SA 3.0, via Wikimedia Commons)*

#### 8-Zoll-Festplatten (1979)

Die ersten Festplatten im PC-kompatiblen Formfaktor wurden 1979 eingeführt. Die Shugart SA1000 war formfaktorkompatibel mit 8-Zoll-Diskettenlaufwerken und ermöglichte erstmals den Einbau von Festplatten in Standard-Gehäuse.

![[Shugart_SA1004_-_8_inch_HDD.jpg|center|500]]
*<span class="fig-id">02-07-01-shugart-sa1004</span>: Shugart SA1004 – 8-Zoll-Festplatte (1982) mit 10 MB Kapazität (Foto: Mister rf, CC BY-SA 4.0, via Wikimedia Commons)*

#### 5,25-Zoll-Festplatten (1980)

Mit der Seagate ST-506 (1980) begann die Ära der 5,25-Zoll-Festplatten, die zum Standard im IBM PC wurden. Anfangs waren diese Laufwerke "Full Height" (volle Bauhöhe), später kamen "Half Height"-Modelle auf den Markt.

![[5.25_inch_MFM_hdd.JPG|center|500]]
*<span class="fig-id">02-07-01-525inch-mfm-hdd</span>: 5,25-Zoll MFM-Festplatte (Full Height) im Größenvergleich mit einer 2,5-Zoll-Festplatte (Foto: Ian Wilson, CC BY-SA 3.0, via Wikimedia Commons)*

![[quantum-bigfoot-525inch-hdd.jpg|center|500]]
*<span class="fig-id">02-07-01-quantum-bigfoot</span>: Quantum Bigfoot – eine der letzten 5,25-Zoll-Festplatten (Half Height), die bis Ende der 1990er produziert wurden (Foto: Bidgee, CC BY-SA 3.0, via Wikimedia Commons)*

#### 3,5-Zoll-Festplatten (1983)

Der 3,5-Zoll-Formfaktor wurde 1983 eingeführt und setzte sich schnell als Standard für Desktop-PCs durch. Er ist bis heute der dominierende Formfaktor für Desktop-Festplatten.

![[35inch-hdd-closed.jpg|center|500]]
*<span class="fig-id">02-07-01-35inch-hdd-closed</span>: 3,5-Zoll-Desktop-Festplatte (geschlossen) mit PATA-Anschluss (Foto: Evan-Amos, Public Domain, via Wikimedia Commons)*

#### Größenvergleich der Formfaktoren

![[Hard_disk_drive_system.jpg|center|600]]
*<span class="fig-id">02-07-01-hdd-formfaktoren</span>: Größenvergleich verschiedener HDD-Formfaktoren – 5,25", 3,5", 2,5" und PCMCIA-HDD (Foto: Marus, Public Domain, via Wikimedia Commons)*

#### Entwicklung im Überblick

| Jahr | Meilenstein | Kapazität | Preis/MB |
|------|-------------|-----------|----------|
| 1979 | Shugart SA1000 (erste 8" HDD für PCs) | 7.5 MB | $150 |
| 1980 | Seagate ST-506 (erste 5.25" HDD) | 5 MB | $100 |
| 1983 | 3.5" Formfaktor eingeführt | 10 MB | $30 |
| 1988 | 2.5" für Laptops | 20 MB | $20 |
| 1991 | Erste HDD über 1 GB | 1 GB | $1 |
| 1998 | UDMA/33 (schnellere Schnittstelle) | 10 GB | $0.10 |
| 2007 | 1 TB Festplatte | 1 TB | $0.001 |

### Kapazitätswachstum: Kryder's Law

Analog zu Moore's Law für Prozessoren formulierte Mark Kryder (Seagate) 2005, dass sich die Festplattenkapazität alle 13 Monate verdoppelt. Tatsächlich gab es mehrere Technologiesprünge:

| Technologie | Einführung | Wirkung |
|-------------|------------|---------|
| **Dünnfilm-Köpfe** | 1979 | Höhere Datendichte |
| **MR-Köpfe** (Magnetoresistive) | 1991 | 10× Empfindlichkeit |
| **GMR-Köpfe** (Giant MR) | 1997 | Weitere 10× Empfindlichkeit |
| **Perpendicular Recording** | 2005 | Bits stehen senkrecht → höhere Dichte |
| **SMR** (Shingled Magnetic) | 2013 | Überlappende Spuren |
| **HAMR** (Heat-Assisted) | 2020er | Laser erhitzt Medium vor Schreiben |

---

## Aufbau einer Festplatte (HDD)

### Physische Komponenten

Eine Festplatte ist ein Präzisionsinstrument mit erstaunlichen Toleranzen. Der Schreib-/Lesekopf schwebt nur **3-10 Nanometer** über der rotierenden Platte – das entspricht dem Verhältnis eines Jumbo-Jets, der in 1 Meter Höhe über dem Boden fliegt.

![[hdd-aufbau.png|center|700]]
*<span class="fig-id">02-07-01-hdd-aufbau</span>: Festplattenaufbau – Draufsicht und Seitenansicht mit Plattenstapel und Aktuator*

| Komponente | Beschreibung |
|------------|--------------|
| **Platter (Scheibe)** | Aluminium oder Glas mit magnetischer Beschichtung, rotiert mit 5400-15000 U/min |
| **Aktuator-Arm** | Bewegt Schreib-/Leseköpfe radial über Platten, Voice Coil Motor für schnelle Positionierung |
| **Schreib-/Lesekopf** | Ein Kopf pro Plattenoberfläche, schwebt 3-10 nm über der Oberfläche |

### CHS-Adressierung (Cylinder, Head, Sector)

Die klassische Methode, einen Block auf der Festplatte zu adressieren, spiegelte direkt die physische Geometrie wider. Das BIOS des PCs verwendete ursprünglich 10 Bits für Zylinder, 8 für Köpfe und 6 für Sektoren – was zur berühmten **504-MB-Grenze** führte (später durch Tricks auf 8 GB erweitert).

![[chs-adressierung.png|center|700]]
*<span class="fig-id">02-07-01-chs-adressierung</span>: CHS-Adressierung – Zylinder (gleiche Spur auf allen Platten) und Sektoren (Datensegmente einer Spur)*

### Moderne LBA-Adressierung

Heute verwendet man **LBA (Logical Block Addressing)**: Blöcke werden einfach von 0 bis n durchnummeriert. Die Übersetzung zur physischen Position übernimmt der Controller der Festplatte – das Betriebssystem muss sich nicht mehr um die Geometrie kümmern.

| Adressierung | Beschreibung | Limitierung |
|--------------|--------------|-------------|
| **CHS** | Cylinder, Head, Sector | 8 GB (BIOS-Limit) |
| **LBA-28** | 28-Bit Blocknummer | 128 GB |
| **LBA-48** | 48-Bit Blocknummer | 128 PB |

Der Festplatten-Controller übersetzt LBA intern auf die physische Position. Moderne Festplatten verwenden intern sogar **Zone Bit Recording**: Äußere Spuren haben mehr Sektoren als innere, weil sie länger sind. Diese Komplexität bleibt dem Betriebssystem verborgen.

### Sektorgröße: 512 Bytes vs. 4 KB

Jahrzehntelang war der Standard-Sektor **512 Bytes** groß – ein Relikt aus den 1980ern. Seit 2010 setzen sich **Advanced Format**-Festplatten mit 4-KB-Sektoren durch:

| Format | Sektorgröße | Vorteile |
|--------|-------------|----------|
| **512n** (native) | 512 Bytes | Maximale Kompatibilität |
| **512e** (emulated) | 4 KB physisch, 512 B logisch | Übergangsformat |
| **4Kn** (native) | 4 KB | Höhere Kapazität, bessere ECC |

> [!warning] **Alignment-Problem**
> Wenn Partitionen nicht an 4-KB-Grenzen ausgerichtet sind, muss die Festplatte bei jedem Schreibvorgang zwei physische Sektoren lesen-ändern-schreiben. Das halbiert die Schreibperformance!

---

## Zeitverhalten einer HDD

### Zugriffszeit-Komponenten

![[hdd-zugriffszeit.png|center|700]]
*<span class="fig-id">02-07-01-hdd-zugriffszeit</span>: Zugriffszeit einer HDD – Seek Time, Rotational Latency und Transfer Time*

### Warum sequentieller Zugriff schneller ist

| Zugriffsmuster | Geschwindigkeit | Grund |
|----------------|-----------------|-------|
| **Sequentiell** | 150-250 MB/s | Kein Seek, minimale Rotation |
| **Random (4KB)** | 0.3-1 MB/s | Jeder Zugriff: Seek + Rotation |

**Faktor 200×** Unterschied! Deshalb sind Dateisystem-Optimierungen wie:
- Zusammenhängende Allokation
- Disk-Scheduling (Elevator/SCAN)
- Read-Ahead Buffering

so wichtig.

---

## Solid State Drives (SSDs)

### Die Flash-Revolution

SSDs markieren den zweiten großen Paradigmenwechsel in der Speichertechnologie. Nach dem Übergang von sequentiell (Band) zu Random Access (HDD) kam nun der Übergang von mechanisch zu rein elektronisch.

![[Bigfoot_TS_size_comparison.jpg|center|500]]
*<span class="fig-id">02-07-01-storage-size-comparison</span>: Evolution der Speichermedien – Größenvergleich zwischen 5,25" HDD, 3,5" HDD, 2,5" SSD und microSD-Karte (Foto: Mothdotmonster, CC BY-SA 4.0, via Wikimedia Commons)*

Die Technologie basiert auf **NAND-Flash-Speicher**, der 1987 bei Toshiba entwickelt wurde. Anfangs nur in Speicherkarten verwendet, wurden SSDs ab 2007 für Computer erschwinglich.

### Grundlegender Unterschied

![[hdd-vs-ssd.png|center|700]]
*<span class="fig-id">02-07-01-hdd-vs-ssd</span>: HDD vs. SSD – mechanischer vs. elektronischer Speicher*

| HDD (Mechanisch) | SSD (Elektronisch) |
|------------------|-------------------|
| Mechanische Teile | Keine beweglichen Teile |
| Empfindlich gegen Stöße | Stoßunempfindlich |
| Seek Time > 0 | Random ≈ Sequentiell |
| Sequentiell viel schneller | Begrenzte Schreibzyklen |

### SSD-Architektur

![[ssd-architektur.png|center|700]]
*<span class="fig-id">02-07-01-ssd-architektur</span>: SSD-Architektur – Host, Controller mit FTL, und NAND Flash Chips*

![[MSATA_SATA_M.2_NVMeSSD.jpg|center|600]]
*<span class="fig-id">02-07-01-ssd-formfaktoren</span>: Moderne SSD-Formfaktoren – von links: mSATA, M.2 SATA (2242), M.2 SATA (2280), M.2 NVMe (2280) (Foto: ガラパリ, CC BY-SA 4.0, via Wikimedia Commons)*

### SSD-spezifische Eigenschaften

Die Physik von NAND-Flash führt zu Eigenschaften, die für Dateisysteme relevant sind:

| Eigenschaft | Auswirkung |
|-------------|------------|
| **Kein Seek** | Random Read so schnell wie Sequential |
| **Erase-before-Write** | Blöcke müssen vor Überschreiben gelöscht werden |
| **Erase-Blöcke groß** | 128KB-512KB müssen zusammen gelöscht werden |
| **Write Amplification** | Mehr physische Schreibvorgänge als logische |
| **Wear Leveling** | Controller verteilt Schreibvorgänge gleichmäßig |
| **TRIM** | OS informiert SSD über freigegebene Blöcke |

**Das Erase-Problem erklärt:**
NAND-Flash kann Bits nur von 1 auf 0 setzen. Um eine 0 zurück auf 1 zu setzen, muss ein ganzer "Erase Block" (128-512 KB) komplett gelöscht werden. Wenn du nur 4 KB überschreiben willst, muss der Controller:

1. Den gesamten Erase Block lesen
2. Die 4 KB im RAM ändern
3. Den Block löschen
4. Den ganzen Block neu schreiben

Das erklärt, warum SSDs ohne TRIM langsamer werden: Der Controller weiß nicht, welche Blöcke wirklich frei sind.

### Performance-Vergleich

Die Unterschiede sind dramatisch – besonders beim Random Access:

| Metrik | HDD (7200 RPM) | SATA SSD | NVMe SSD |
|--------|----------------|----------|----------|
| **Random Read IOPS** | 80 | 90.000 | 500.000+ |
| **Random Write IOPS** | 80 | 80.000 | 400.000+ |
| **Seq. Read (MB/s)** | 200 | 550 | 7.000 |
| **Seq. Write (MB/s)** | 180 | 520 | 5.000 |
| **Latenz** | 5-15 ms | 0.1 ms | 0.02 ms |

**Warum NVMe so viel schneller ist:**
SATA wurde für HDDs entworfen und ist auf eine Warteschlange mit 32 Befehlen limitiert. NVMe (Non-Volatile Memory Express) wurde speziell für SSDs entwickelt und unterstützt 65.535 Warteschlangen mit je 65.536 Befehlen – das ermöglicht massive Parallelität.

### NAND-Typen und Lebensdauer

| Typ | Bits/Zelle | Schreibzyklen | Einsatz |
|-----|------------|---------------|---------|
| **SLC** (Single-Level Cell) | 1 | 100.000+ | Enterprise, Server |
| **MLC** (Multi-Level Cell) | 2 | 10.000 | High-End Consumer |
| **TLC** (Triple-Level Cell) | 3 | 3.000 | Standard Consumer |
| **QLC** (Quad-Level Cell) | 4 | 1.000 | Budget, Read-Heavy |

Mehr Bits pro Zelle = mehr Kapazität, aber weniger Haltbarkeit und langsamere Schreibgeschwindigkeit.

---

## Relevanz für Dateisysteme

### Warum die Geschichte wichtig ist

| HDD-Konzept | Warum es existiert | SSD-Relevanz |
|-------------|-------------------|--------------|
| **Sektoren (512B/4KB)** | Kleinste addressierbare Einheit | Beibehalten für Kompatibilität |
| **Disk Scheduling** | Seek-Zeit minimieren | Nicht mehr nötig (kein Seek) |
| **Defragmentierung** | Zusammenhängende Allokation | Kontraproduktiv (Write Amp.) |
| **Buffer Cache** | RAM schneller als Disk | Weiterhin sinnvoll |
| **Journaling** | Crash-Sicherheit | Weiterhin wichtig |

### Dateisystem-Anpassungen für SSDs

| Anpassung | Grund |
|-----------|-------|
| **TRIM-Support** | SSD weiß, welche Blöcke frei sind |
| **Keine Defragmentierung** | Unnötig und schädlich (Wear) |
| **Alignment** | Schreibvorgänge an Erase-Block-Grenzen |
| **Weniger aggressive Read-Ahead** | Random Read schnell genug |

```bash
# TRIM aktivieren (fstab)
UUID=... /     ext4    discard,noatime   0 1

# Manueller TRIM
$ fstrim -v /
```

---

## Zusammenhänge

- [[02-Grundlagen|Grundlagen]] → Wie Dateisysteme die Hardware abstrahieren
- [[03-Implementierung|Implementierung]] → Blockallokation basiert auf Hardware-Eigenschaften
- [[../06-Ein-Ausgabe/01-IO-Grundlagen|I/O-Grundlagen]] → DMA, Block-I/O

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - Warum sequentieller Zugriff auf HDDs schneller ist
> - Grundlegender Unterschied HDD vs. SSD

> [!question] **Häufige Prüfungsfragen**
> 1. Erklären Sie die drei Komponenten der Zugriffszeit bei einer Festplatte!
> 2. Warum ist sequentieller Zugriff auf HDDs um Größenordnungen schneller als Random Access?
> 3. Warum brauchen SSDs keinen Disk-Scheduler wie SCAN oder C-LOOK?
> 4. Was ist TRIM und warum ist es für SSDs wichtig?

> [!tip] **Merkhilfen**
> - **Seek** = "Arm fährt zur richtigen Spur" (wie Plattenspieler)
> - **Rotation** = "Warten, bis der richtige Sektor vorbeikommt"
> - **SSD** = "Festplatte ohne das Fest" (keine beweglichen Teile)

---

## Weiterführende Ressourcen

> [!note] **Videos (YouTube)**
>
> | | Video | Beschreibung |
> |---|-------|--------------|
> | 🎬 | [Technology Connections – Hard Drives](https://www.youtube.com/watch?v=wteUW2sL7bc) | Wie HDDs funktionieren |
> | 🎬 | [Branch Education – How do SSDs Work?](https://www.youtube.com/watch?v=5Mh3o886qpg) | SSD-Technologie erklärt |

---

## Quellen

- Tanenbaum, A. S.: Modern Operating Systems, Kapitel 5.4
- Patterson, D., Hennessy, J.: Computer Organization and Design, Kapitel 5
- IBM Archives: RAMAC History
- Micron Technology: NAND Flash 101
