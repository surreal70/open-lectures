---
author: Andreas Hümmer
title: Paging
tags:
  - content
  - bs
  - speicher
  - paging
  - page-table
  - tlb
created: '2026-10-07'
modified: '2026-10-09'
bereich: BS
---

# Paging

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das Paging-Konzept mit Pages und Frames verstehen
> - Die Funktion der Page Table erklären können
> - Den TLB (Translation Lookaside Buffer) kennen
> - Page-Ersetzungsalgorithmen verstehen (FIFO, LRU, etc.)
> - Die Adressumrechnung bei Paging nachvollziehen können

---

## Überblick

Paging ist die Standardtechnik moderner Betriebssysteme zur Implementierung von virtuellem Speicher. Die Idee ist bestechend einfach: Statt den Speicher in variable Segmente aufzuteilen, wird er in gleich große Blöcke unterteilt – sowohl auf der virtuellen als auch auf der physischen Seite.

Die Technik wurde erstmals im **Atlas Computer** (1962) eingesetzt und hat sich seitdem als Standard etabliert. Der entscheidende Vorteil: Durch die feste Blockgröße entsteht **keine externe Fragmentierung** – jeder freie Frame kann jede Page aufnehmen.

Moderne Prozessoren unterstützen Paging direkt in Hardware (MMU), und das Betriebssystem muss nur die Page Tables verwalten. Diese enge Hardware-Software-Kooperation macht Paging extrem effizient.

---

## Definition

> [!quote] **Formale Definition**
> **Paging** ist eine Speicherverwaltungstechnik, bei der der virtuelle Adressraum in gleich große Blöcke (**Pages**) und der physische Speicher in gleich große Blöcke (**Frames/Kacheln**) unterteilt wird.

### Zentrale Begriffe

| Begriff | Beschreibung | Beispiel |
|---------|--------------|----------|
| **Page** | Block im virtuellen Adressraum | Virtuelle Page 5 eines Prozesses |
| **Frame (Kachel)** | Block im physischen Speicher | RAM-Adresse 0x1000-0x1FFF |
| **Page Table** | Tabelle, die Pages auf Frames abbildet | Page 5 → Frame 12 |
| **Page Size** | Größe einer Page/eines Frames | 4 KB, 2 MB, 1 GB |
| **Page Table Entry (PTE)** | Ein Eintrag in der Page Table | Frame-Nummer + Flags |

---

## Grundkonzept

Das Paging-Konzept trennt die logische Sicht (Pages) von der physischen Realität (Frames). Jede Page eines Prozesses kann in einem beliebigen freien Frame liegen:

![[02-05-03-paging-konzept.png]]
*<span class="fig-id">02-05-03-paging-konzept</span>: Paging-Konzept: Der virtuelle Adressraum wird in Pages unterteilt, der physische Speicher in Frames. Die Page Table ordnet jede Page einem Frame zu – die Zuordnung muss nicht zusammenhängend sein.*

### Warum gleich große Blöcke?

| Vorteil | Beschreibung |
|---------|--------------|
| **Keine externe Fragmentierung** | Jeder freie Frame passt für jede Page – keine "Lücken" |
| **Einfache Verwaltung** | Frame-Liste statt komplexer Lückenverwaltung |
| **Schnelle Allokation** | O(1) – einfach den ersten freien Frame nehmen |
| **Hardware-Unterstützung** | Adressübersetzung kann effizient in Hardware erfolgen |

### Page-Größen in der Praxis

| System | Standard Page Size | Huge Pages |
|--------|-------------------|------------|
| x86 (32-Bit) | 4 KB | 4 MB (PSE) |
| x86-64 | 4 KB | 2 MB, 1 GB |
| ARM (64-Bit) | 4 KB, 16 KB, 64 KB | 2 MB, 1 GB |
| RISC-V | 4 KB | 2 MB, 1 GB |

> [!info] **Trade-off bei der Page-Größe**
> - **Kleine Pages (4 KB):** Weniger interne Fragmentierung, aber große Page Tables
> - **Große Pages (2 MB, 1 GB):** Kleinere Page Tables, weniger TLB-Misses, aber mehr Verschwendung pro Page

---

## Page Table

Jeder Prozess hat eine eigene **Page Table**, die die Zuordnung von Pages zu Frames speichert. Die Page Table liegt im RAM und wird vom Betriebssystem verwaltet.

> [!example] **Beispiel: Page Table**
> 
> | Page | Valid | Frame | Modified | Referenced | Protection |
> |:----:|:-----:|:-----:|:--------:|:----------:|:----------:|
> | 0 | 1 | 2 | 0 | 1 | R/W |
> | 1 | 1 | 5 | 1 | 1 | R/W |
> | 2 | 0 | - | - | - | - |
> | 3 | 1 | 1 | 0 | 0 | R |
> | 4 | 1 | 3 | 1 | 1 | R/W |
> 
> - **Valid Bit:** 1 = Page ist im RAM, 0 = auf Festplatte (Page 2)
> - **Modified Bit:** 1 = Page wurde verändert (Dirty Bit)
> - **Referenced:** 1 = Page wurde kürzlich zugegriffen

### Page Table Entry (PTE) im Detail

Ein Page Table Entry enthält mehr als nur die Frame-Nummer:

| Feld | Bits (typisch) | Beschreibung |
|------|----------------|--------------|
| **Frame Number** | 20-40 Bit | Physische Frame-Adresse |
| **Valid/Present (V)** | 1 Bit | Page ist im RAM (1) oder ausgelagert (0) |
| **Modified/Dirty (M)** | 1 Bit | Page wurde seit dem Laden verändert |
| **Referenced/Accessed (R)** | 1 Bit | Page wurde kürzlich zugegriffen |
| **Protection** | 2-3 Bit | Zugriffsrechte (R/W/X) |
| **User/Supervisor (U)** | 1 Bit | User-Mode (1) oder Kernel-Mode (0) Zugriff |
| **No-Execute (NX)** | 1 Bit | Code-Ausführung verboten (Sicherheit) |
| **Cache Disable** | 1 Bit | Caching für diese Page deaktivieren |

### Bedeutung der Flags

| Flag | Wenn gesetzt (1) | Wenn nicht gesetzt (0) |
|------|------------------|------------------------|
| **Valid** | Page im RAM, Zugriff erlaubt | Page Fault → von Disk laden |
| **Modified** | Bei Ersetzung auf Disk schreiben | Einfach verwerfen (Kopie auf Disk aktuell) |
| **Referenced** | Kürzlich benutzt (Clock-Algo) | Kandidat für Ersetzung |
| **NX** | Daten, kein Code | Code darf ausgeführt werden |

> [!tip] **Dirty Bit spart I/O**
> Wenn eine Page nur gelesen wurde (Dirty = 0), muss sie bei der Ersetzung nicht zurückgeschrieben werden – die Kopie auf der Festplatte ist noch aktuell. Das spart teure Schreiboperationen.

---

## Adressumrechnung

Eine virtuelle Adresse besteht aus **Page Number** und **Offset**. Der Offset bleibt bei der Übersetzung unverändert – nur die Page Number wird durch die Frame Number ersetzt:

![[02-05-03-adressumrechnung.png]]
*<span class="fig-id">02-05-03-adressumrechnung</span>: Adressumrechnung bei Paging: Die Page Number wird über die Page Table in eine Frame Number übersetzt. Der Offset (Position innerhalb der Page) bleibt unverändert.*

### Berechnung der Bit-Aufteilung

Die Offset-Größe ergibt sich aus der Page-Größe:

| Page-Größe | Offset-Bits | Berechnung |
|------------|-------------|------------|
| 4 KB | 12 Bit | log₂(4096) = 12 |
| 2 MB | 21 Bit | log₂(2.097.152) = 21 |
| 1 GB | 30 Bit | log₂(1.073.741.824) = 30 |

### Rechenbeispiel

> [!example] **Adressumrechnung Schritt für Schritt**
> 
> **Gegeben:**
> - Page-Größe: 4 KB = 4096 Bytes = 2¹² → 12 Bit Offset
> - Virtuelle Adresse: `0x00001234` (hexadezimal)
> - Page Table: Page 1 → Frame 5
> 
> **Schritt 1: Adresse aufteilen**
> ```
> 0x00001234 = 0000 0000 0000 0001 0010 0011 0100 (binär)
>              ├─── Page Number ───┤├── Offset ──┤
>              0x00001 = 1          0x234 = 564
> ```
> 
> **Schritt 2: Page Table Lookup**
> - Page 1 → Frame 5
> 
> **Schritt 3: Physische Adresse zusammensetzen**
> ```
> Frame 5 = 0x005
> Offset  = 0x234
> → Physische Adresse: 0x00005234
> ```

### Formel zur Adressumrechnung

```
Physische Adresse = (Frame_Number × Page_Size) + Offset

Oder equivalänt (für Bit-Operationen):
Physische Adresse = (Frame_Number << Offset_Bits) | Offset
```

---

## TLB – Translation Lookaside Buffer

### Das Problem

Die Page Table liegt im RAM. Ohne Optimierung erfordert **jeder Speicherzugriff zwei RAM-Zugriffe**:
1. Page Table lesen (um Frame-Nummer zu ermitteln)
2. Tatsächliche Daten lesen

Das würde die Speichergeschwindigkeit halbieren – inakzeptabel.

### Die Lösung: TLB

Der **Translation Lookaside Buffer (TLB)** ist ein kleiner, extrem schneller Cache direkt in der CPU, der kürzlich verwendete Page-Table-Einträge speichert.

![[02-05-03-tlb.png]]
*<span class="fig-id">02-05-03-tlb</span>: TLB-Ablauf: Bei einem TLB Hit wird die physische Adresse direkt geliefert. Bei einem TLB Miss muss die Page Table im RAM konsultiert und der TLB aktualisiert werden.*

### TLB-Eigenschaften

| Eigenschaft | Typischer Wert | Beschreibung |
|-------------|----------------|--------------|
| **Größe** | 64-1024 Einträge | Klein, aber sehr schnell |
| **Zugriffszeit** | < 1 ns | Vollständig assoziativ, parallel durchsucht |
| **Hit Rate** | > 99% | Dank Lokalitätsprinzip |
| **Miss Penalty** | 10-100 Zyklen | Page Table Lookup im RAM |

### Zugriffszeiten im Vergleich

| Ereignis | Zugriffszeit | Faktor |
|----------|--------------|--------|
| TLB Hit | ≈ 1 ns | 1× |
| TLB Miss (Page Table im L3-Cache) | ≈ 10-20 ns | 10-20× |
| TLB Miss (Page Table im RAM) | ≈ 60-100 ns | 60-100× |
| Page Fault (SSD) | ≈ 100 µs | 100.000× |
| Page Fault (HDD) | ≈ 10 ms | 10.000.000× |

### TLB und Kontextwechsel

Bei einem Kontextwechsel (Prozesswechsel) muss der TLB in der Regel geleert werden (**TLB Flush**), da jeder Prozess seine eigene Page Table hat. Moderne CPUs verwenden **ASIDs** (Address Space Identifiers), um TLB-Einträge verschiedener Prozesse zu unterscheiden und Flushes zu vermeiden.

> [!info] **PCID / ASID**
> - **PCID** (Process Context ID, Intel) / **ASID** (Address Space ID, ARM)
> - Jeder TLB-Eintrag enthält zusätzlich die Prozess-ID
> - Bei Kontextwechsel bleibt der TLB erhalten
> - Enormer Performance-Gewinn bei häufigen Kontextwechseln

---

## Mehrstufige Page Tables

### Das Problem der Page-Table-Größe

Bei einem 32-Bit-Adressraum mit 4 KB Pages:
- Anzahl Pages: 2³² / 2¹² = 2²⁰ = ca. 1 Million
- Page Table Größe: 1M × 4 Bytes = **4 MB pro Prozess**

Bei 64-Bit-Adressräumen wäre eine flache Page Table astronomisch groß.

### Lösung: Hierarchische Page Tables

Statt einer flachen Tabelle werden mehrere Ebenen verwendet. Nicht benötigte Teile der Page Table müssen gar nicht existieren.

![[02-05-03-zweistufig.png]]
*<span class="fig-id">02-05-03-zweistufig</span>: Zweistufige Page Table: Der Dir Index wählt einen Eintrag im Page Directory, der auf eine von 1024 Page Tables zeigt. Der Page Index wählt dort den Frame aus.*

### Page-Table-Ebenen in verschiedenen Architekturen

| Architektur | Ebenen | Adressbreite | Page Größe |
|-------------|--------|--------------|------------|
| x86 (32-Bit) | 2 | 32 Bit | 4 KB |
| x86 PAE | 3 | 36 Bit | 4 KB |
| x86-64 | 4 | 48 Bit | 4 KB |
| x86-64 (5-Level) | 5 | 57 Bit | 4 KB |
| ARM64 | 4 | 48 Bit | 4/16/64 KB |

### x86-64: 4-Level Paging

![[02-05-03-x86-64-paging.png]]
*<span class="fig-id">02-05-03-x86-64-paging</span>: x86-64 verwendet vier Page-Table-Ebenen, um 48-Bit-Adressen (256 TB) zu unterstützen. Jede Ebene verwendet 9 Bit als Index.*

| Abkürzung | Name | Funktion |
|-----------|------|----------|
| **PML4** | Page Map Level 4 | Oberste Ebene, 512 Einträge |
| **PDPT** | Page Directory Pointer Table | Zeigt auf Page Directories |
| **PD** | Page Directory | Zeigt auf Page Tables |
| **PT** | Page Table | Enthält Frame-Nummern |

> [!note] **Warum nur 48 Bit?**
> Obwohl x86-64 Register 64 Bit breit sind, werden nur 48 Bit für Adressen genutzt (256 TB). Die oberen 16 Bit müssen mit Bit 47 übereinstimmen (Sign Extension). Dies ist eine bewusste Designentscheidung, um Page Tables kompakt zu halten.

---

## Page-Ersetzungsalgorithmen

Wenn alle Frames belegt sind und eine neue Page geladen werden muss, entscheidet der Ersetzungsalgorithmus, welche Page weichen muss.

### Übersicht der Algorithmen

| Algorithmus | Beschreibung | Vorteile | Nachteile |
|-------------|--------------|----------|-----------|
| **OPT** | Ersetze Page, die am längsten nicht benötigt wird | Theoretisch optimal | Nicht implementierbar (Zukunft unbekannt) |
| **FIFO** | First In, First Out | Einfach zu implementieren | Belady-Anomalie möglich |
| **LRU** | Least Recently Used | Gute Ergebnisse | Aufwendig (Zeitstempel/Stack) |
| **LFU** | Least Frequently Used | Berücksichtigt Häufigkeit | Zähler-Overhead, "Altlasten" |
| **Clock** | FIFO + Second Chance | Guter Kompromiss | Approximation von LRU |
| **NRU** | Not Recently Used | Sehr einfach | Grobe Approximation |

### Clock-Algorithmus (Second Chance)

Der Clock-Algorithmus ist die praktische Wahl für die meisten Betriebssysteme. Er kombiniert die Einfachheit von FIFO mit der Berücksichtigung des Referenced-Bits:

![[02-05-03-clock-algorithmus.png]]
*<span class="fig-id">02-05-03-clock-algorithmus</span>: Clock-Algorithmus: Der Zeiger wandert im Kreis. Pages mit R=1 bekommen eine zweite Chance (R wird auf 0 gesetzt). Die erste Page mit R=0 wird ersetzt.*

**Pseudocode:**
```
WHILE (true):
    page = frames[zeiger]
    IF page.R == 0:
        RETURN page           // Opfer gefunden
    ELSE:
        page.R = 0            // Zweite Chance geben
        zeiger = (zeiger + 1) MOD n
```

### Enhanced Clock (NRU)

Berücksichtigt sowohl Referenced (R) als auch Modified (M):

| Klasse | R | M | Priorität | Beschreibung |
|--------|---|---|-----------|--------------|
| 0 | 0 | 0 | Höchste | Nicht benutzt, nicht verändert |
| 1 | 0 | 1 | Hoch | Nicht benutzt, aber verändert |
| 2 | 1 | 0 | Niedrig | Kürzlich benutzt, nicht verändert |
| 3 | 1 | 1 | Niedrigste | Kürzlich benutzt und verändert |

Ersetze Pages aus der niedrigsten vorhandenen Klasse.

> [!tip] **Warum M=1 schlechter als M=0?**
> Eine modifizierte Page muss vor dem Ersetzen auf die Festplatte geschrieben werden (I/O-Operation). Eine unmodifizierte Page kann einfach verworfen werden.

---

## Interne vs. Externe Fragmentierung

Paging eliminiert externe Fragmentierung vollständig, führt aber zu interner Fragmentierung:

| Fragmentierungsart | Bei Paging | Erklärung |
|--------------------|------------|-----------|
| **Externe Fragmentierung** | ✗ Keine | Jeder Frame passt für jede Page |
| **Interne Fragmentierung** | ✓ Vorhanden | Letzte Page eines Prozesses ist teilweise leer |

### Berechnung der internen Fragmentierung

Im Durchschnitt ist die letzte Page eines Prozesses zur Hälfte gefüllt:

```
Durchschnittliche Verschwendung pro Prozess = Page_Size / 2

Bei 4 KB Pages: 2 KB pro Prozess
Bei 2 MB Pages: 1 MB pro Prozess
```

> [!example] **Beispiel**
> Ein Prozess benötigt 10.500 Bytes bei 4 KB Pages:
> - Benötigte Pages: ⌈10.500 / 4.096⌉ = 3 Pages
> - Reservierter Speicher: 3 × 4.096 = 12.288 Bytes
> - Verschwendung: 12.288 - 10.500 = **1.788 Bytes**

---

## Shared Pages

Paging ermöglicht effizientes Sharing von Code und Daten zwischen Prozessen:

### Code Sharing

Wenn mehrere Prozesse dasselbe Programm ausführen (z.B. mehrere Terminal-Fenster), kann der **Text-Bereich** (Code) geteilt werden:

| Prozess A | Prozess B | Physischer Speicher |
|-----------|-----------|---------------------|
| Page 0 (Code) → | ← Page 0 (Code) | Frame 5 (geteilt) |
| Page 1 (Data) → | | Frame 12 |
| | ← Page 1 (Data) | Frame 17 |

### Copy-on-Write (CoW) mit Paging

Bei `fork()` werden alle Pages als **read-only** markiert und geteilt. Erst beim Schreiben wird die betroffene Page kopiert:

1. `fork()`: Kind erhält Kopie der Page Table, alle Pages read-only
2. Lesezugriff: Beide Prozesse lesen dieselbe Page → OK
3. Schreibzugriff: Page Fault → Kernel kopiert die Page → Schreiben erlaubt

---

## Zusammenhänge

- [[01-Adressraeume|Adressräume]] → Paging teilt den Adressraum auf
- [[02-Virtueller-Speicher|Virtueller Speicher]] → Paging ermöglicht virtuellen Speicher
- [[04-Segmentierung|Segmentierung]] → Alternative/Ergänzung zu Paging

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - Page und Frame Konzept
> - Aufbau und Inhalt der Page Table (Flags!)
> - Page-Ersetzungsalgorithmen (FIFO, LRU, Clock)


> [!question] **Häufige Prüfungsfragen**
> 1. Rechnen Sie eine virtuelle Adresse in eine physische um!
> 2. Was ist der TLB und warum ist er wichtig?
> 3. Erklären Sie den Clock-Algorithmus zur Page-Ersetzung!
> 4. Was ist der Unterschied zwischen einer Page und einem Frame?
> 5. Welche Informationen enthält ein Page-Table-Eintrag?
> 6. Warum verwendet man mehrstufige Page Tables?
> 7. Was ist der Unterschied zwischen interner und externer Fragmentierung?
> 8. Erklären Sie Copy-on-Write bei fork()!

> [!tip] **Merkhilfen**
> - **Page** = "Buchseite" (virtuell, logisch)
> - **Frame** = "Bilderrahmen" (physisch, nimmt Page auf)
> - **TLB** = "Telefonbuch-Cache" (schnelles Nachschlagen häufiger Nummern)
> - **Clock** = "Uhrzeiger dreht, bis R=0 gefunden"
> - **Valid=0** → Page Fault → "Seite nicht eingelegt"
> - **Dirty=1** → "Seite beschmutzt" → muss beim Ersetzen gespeichert werden

---

## Praktische Werkzeuge

### Linux-Kommandos

```bash
# Page-Größe des Systems anzeigen
$ getconf PAGE_SIZE
4096

# Speicher-Mapping eines Prozesses anzeigen
$ cat /proc/<pid>/maps

# Page-Table-Statistiken
$ cat /proc/<pid>/smaps

# Huge Pages Konfiguration
$ cat /proc/meminfo | grep Huge

# TLB-Statistiken (erfordert perf)
$ perf stat -e dTLB-loads,dTLB-load-misses ./programm
```

---

## Weiterführende Ressourcen

> [!note] **Videos (YouTube)**
>
> | | Video | Beschreibung |
> |---|-------|--------------|
> | 🎬 | [CoreDumped – Memory Access](https://www.youtube.com/watch?v=A9WLYbE0p-I) | Adressübersetzung und Speicherzugriff |
> | 🎬 | [Computerphile – Paging](https://www.youtube.com/watch?v=KNUJhZCQZ9c) | Einführung in Paging |
> | 🎬 | [MIT 6.004 – Virtual Memory](https://www.youtube.com/watch?v=cjZrQDWJZOg) | Akademische Vorlesung zu VM und Paging |

---

## Quellen

- Vorlesung: „Betriebssysteme, Rechnernetze und verteilte Systeme" – IU, Teil 5 (Ressourcen)
- Tanenbaum, A. S. & Bos, H.: Modern Operating Systems, 5th Edition, Kapitel 3
- Silberschatz, A., Galvin, P. B. & Gagne, G.: Operating System Concepts, 10th Edition, Kapitel 8-9
- Intel 64 and IA-32 Architectures Software Developer's Manual, Volume 3A: System Programming Guide

### Direkte Quellenreferenzen

**Tanenbaum, A. S. & Bos, H.: Modern Operating Systems (5th Edition)**
- Kapitel 3: Memory Management
  - 3.3 Virtual Memory
    - 3.3.1 Paging (→ Grundkonzept)
    - 3.3.2 Page Tables (→ Aufbau, mehrstufig)
    - 3.3.3 Speeding Up Paging (→ TLB)
  - 3.4 Page Replacement Algorithms (→ FIFO, LRU, Clock)

**Silberschatz, A., Galvin, P. B. & Gagne, G.: Operating System Concepts (10th Edition)**
- Chapter 8: Main Memory
  - 8.4 Paging (→ Grundkonzept)
  - 8.5 Structure of the Page Table (→ Hierarchisch, Hashed, Inverted)
- Chapter 9: Virtual Memory
  - 9.4 Page Replacement (→ Algorithmen)
