---
author: Andreas Hümmer
title: Segmentierung
tags:
  - content
  - bs
  - speicher
  - segmentierung
  - segment-table
created: '2026-10-07'
modified: '2026-10-09'
bereich: BS
---

# Segmentierung

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das Konzept der Segmentierung verstehen und von Paging unterscheiden können
> - Wissen, wie Segmente den logischen Programmaufbau widerspiegeln
> - Die Adressumrechnung bei Segmentierung erklären können
> - Vor- und Nachteile gegenüber Paging kennen
> - Das Konzept der kombinierten Segmentierung mit Paging verstehen

---

## Definition

> [!quote] **Formale Definition**
> **Segmentierung** unterteilt den Adressraum in logische Einheiten (**Segmente**) unterschiedlicher Größe. Jedes Segment repräsentiert eine logische Einheit des Programms (Code, Daten, Stack, etc.).

---

## Historischer Kontext

Die Segmentierung entstand in den 1960er Jahren als Antwort auf die Frage: *Wie kann der Speicher so organisiert werden, dass er die logische Struktur eines Programms widerspiegelt?*

Frühe Systeme wie **Multics** (1965) setzten Segmentierung konsequent um – jede Prozedur, jedes Datenfeld war ein eigenes Segment. Dies ermöglichte:

- **Natürlichen Schutz**: Code-Segmente nur lesbar/ausführbar
- **Einfaches Sharing**: Bibliotheken als geteilte Segmente
- **Dynamisches Wachstum**: Segmente können zur Laufzeit wachsen

Die Intel 8086-Architektur (1978) übernahm Segmentierung aus einem anderen Grund: Sie ermöglichte das Adressieren von 1 MB Speicher mit nur 16-Bit-Registern durch die Kombination von Segment- und Offset-Register.

---

## Grundkonzept

Der fundamentale Unterschied zu Paging: Bei Segmentierung bestimmt die **logische Struktur** des Programms die Aufteilung, nicht eine feste Blockgröße.

![[segmentierung-konzept.png]]
*<span class="fig-id">05-04-01-segmentierung-konzept</span>: Segmente werden aus der logischen Programmsicht an beliebige Positionen im physischen Speicher abgebildet.*

### Typische Segmente eines Prozesses

| Segment | Inhalt | Typische Zugriffsrechte | Wachstumsrichtung |
|---------|--------|-------------------------|-------------------|
| **Code (Text)** | Maschinencode | Read + Execute | Statisch |
| **Data** | Initialisierte globale Variablen | Read + Write | Statisch |
| **BSS** | Nicht-initialisierte globale Variablen | Read + Write | Statisch |
| **Heap** | Dynamisch allozierter Speicher | Read + Write | Aufwärts ↑ |
| **Stack** | Lokale Variablen, Rücksprungadressen | Read + Write | Abwärts ↓ |

---

## Segmentierung vs. Paging

| Eigenschaft | Segmentierung | Paging |
|-------------|---------------|--------|
| **Einheitsgröße** | Variabel | Fest (z.B. 4 KB) |
| **Sichtbarkeit** | Dem Programmierer bekannt | Für Programmierer transparent |
| **Logische Struktur** | Spiegelt Programmaufbau wider | Keine logische Bedeutung |
| **Fragmentierung** | Extern (zwischen Segmenten) | Intern (innerhalb Pages) |
| **Schutz** | Pro Segment (logisch sinnvoll) | Pro Page |
| **Sharing** | Einfach (ganze Segmente) | Komplex (einzelne Pages) |
| **Adressformat** | (Segment, Offset) | (Page, Offset) |
| **Hardware** | Segment Table | Page Table + TLB |

### Wann ist welcher Ansatz besser?

**Segmentierung eignet sich besser für:**
- Bibliotheken-Sharing (eine Shared Library = ein Segment)
- Sprachkonstrukte mit variabler Größe (Arrays, Objekte)
- Feingranularen Schutz basierend auf Semantik

**Paging eignet sich besser für:**
- Effiziente Speicherverwaltung ohne externe Fragmentierung
- Demand Paging und Swapping
- Hardwareunterstützung (TLB-Caching)

---

## Adressumrechnung

Eine **logische Adresse** bei Segmentierung besteht aus zwei Komponenten:
- **Segmentnummer (s)**: Identifiziert das Segment
- **Offset (d)**: Position innerhalb des Segments

Die Hardware prüft bei jedem Zugriff:
1. Ist das Segment vorhanden (Present-Bit)?
2. Liegt der Offset innerhalb der Segmentgrenzen (d < Limit)?
3. Ist der Zugriffstyp erlaubt (Read/Write/Execute)?

![[segmentierung-adressumrechnung.png]]
*<span class="fig-id">05-04-02-segmentierung-adressumrechnung</span>: Adressumrechnung bei Segmentierung mit Grenzprüfung.*

### Berechnungsbeispiel

Gegeben:
- Segment 2 mit Base = `0x5000`, Limit = `4096` Bytes
- Logische Adresse: Segment 2, Offset `0x100` (256)

Berechnung:
1. Prüfung: `0x100` (256) < 4096 ✓
2. Physische Adresse = `0x5000` + `0x100` = `0x5100`

Würde der Offset `0x2000` (8192) sein → **Segmentation Fault**, da 8192 > 4096!

---

## Segment Table

Die Segment Table ist das zentrale Verwaltungselement. Jeder Prozess hat seine eigene Segment Table.

| Segment | Base | Limit | Protection | Present |
|---------|------|-------|------------|---------|
| 0 | `0x4000` | 4096 | R/X | 1 |
| 1 | `0x6000` | 2048 | R/W | 1 |
| 2 | `0x8800` | 1024 | R/W | 1 |
| 3 | `0xA000` | 8192 | R/W | 1 |

*<span class="fig-id">05-04-01</span>: Beispiel einer Segment Table mit vier Segmenten.*

### Felder eines Segment-Table-Eintrags

| Feld | Bedeutung |
|------|-----------|
| **Base** | Startadresse des Segments im physischen Speicher |
| **Limit** | Maximale Größe des Segments in Bytes |
| **Protection** | Zugriffsrechte (Read, Write, Execute) |
| **Present** | Segment aktuell im RAM geladen? |
| **Dirty** | Segment seit dem Laden verändert? |
| **Accessed** | Segment kürzlich zugegriffen? |

### Segment Table Base Register (STBR)

Die CPU enthält ein Register, das auf die Segment Table des aktuellen Prozesses zeigt:
- **STBR** (Segment Table Base Register): Basisadresse der Tabelle
- **STLR** (Segment Table Length Register): Anzahl der Segmente

Bei einem Kontextwechsel werden diese Register mit den Werten des neuen Prozesses geladen.

---

## Externe Fragmentierung

Das Hauptproblem der Segmentierung ist die **externe Fragmentierung**: Durch wiederholtes Laden und Entladen von Segmenten unterschiedlicher Größe entstehen "Löcher" im Speicher, die einzeln zu klein für neue Segmente sind.

![[segmentierung-fragmentierung.png]]
*<span class="fig-id">05-04-03-segmentierung-fragmentierung</span>: Externe Fragmentierung und Lösung durch Kompaktierung.*

### Strategien zur Speicherzuweisung

Um externe Fragmentierung zu minimieren, gibt es verschiedene Algorithmen:

| Strategie | Beschreibung | Vor-/Nachteile |
|-----------|--------------|----------------|
| **First Fit** | Erstes passendes Loch verwenden | Schnell, aber fragmentiert am Anfang |
| **Best Fit** | Kleinstes passendes Loch verwenden | Minimiert Verschnitt, aber langsam |
| **Worst Fit** | Größtes Loch verwenden | Lässt große Restlöcher, praktisch selten gut |
| **Next Fit** | Ab letzter Position suchen | Verteilt Fragmentierung gleichmäßiger |

> [!quote] **50%-Regel**
> Statistische Analysen zeigen: Bei **First Fit** und **Best Fit** ist etwa **ein Drittel** des Speichers durch Fragmentierung verloren – bei N belegten Segmenten gibt es etwa N/2 Löcher (Knuth, 1973).

### Kompaktierung

Bei der **Kompaktierung** werden alle Segmente verschoben, um einen zusammenhängenden freien Bereich zu schaffen:

Vorteile:
- Beseitigt externe Fragmentierung vollständig
- Ermöglicht Allokation großer Segmente

Nachteile:
- **Sehr teuer**: Alle Segmente müssen kopiert werden
- **Prozesse müssen pausieren** während der Kompaktierung
- Alle Basisadressen müssen aktualisiert werden

---

## Kombination: Segmentierung mit Paging

Moderne Systeme kombinieren beide Ansätze, um ihre jeweiligen Vorteile zu nutzen:
- **Segmentierung** für logische Strukturierung und Schutz
- **Paging** für effiziente physische Speicherverwaltung

![[segmentierung-paging.png]]
*<span class="fig-id">05-04-04-segmentierung-paging</span>: Kombinierte Adressumrechnung bei Segmentierung mit Paging.*

| Vorteil | Beschreibung |
|---------|--------------|
| **Logische Struktur** | Segmente spiegeln Programmaufbau wider |
| **Keine externe Fragmentierung** | Paging eliminiert Speicherlöcher |
| **Zweistufiger Schutz** | Zugriffsrechte auf Segment- UND Page-Ebene |

### Multics – Pionier der kombinierten Architektur

**Multics** (1965-2000) war das erste System mit kombinierter Segmentierung und Paging:
- Bis zu 2¹⁸ Segmente pro Prozess
- Jedes Segment bis zu 2⁶⁴ Wörter (später praktisch limitiert)
- Jedes Segment intern gepagest mit 1024-Wort-Pages

Diese Architektur beeinflusste direkt das Design von Intel-Prozessoren.

---

## Intel x86 Segmentierung

Die x86-Architektur nutzt Segmentierung aus historischen Gründen – ursprünglich um mit 16-Bit-Registern mehr als 64 KB adressieren zu können.

### Segmentregister

| Register | Name | Verwendung |
|----------|------|------------|
| **CS** | Code Segment | Programmcode (Instruction Pointer relativ zu CS) |
| **DS** | Data Segment | Standardmäßiges Datensegment |
| **SS** | Stack Segment | Stack-Operationen (PUSH, POP, CALL, RET) |
| **ES** | Extra Segment | String-Operationen (MOVS, CMPS) |
| **FS** | (ab 386) | Thread-Local Storage (z.B. Exception Handling) |
| **GS** | (ab 386) | Thread-Local Storage (z.B. Thread-Kontext) |

### Protected Mode Deskriptoren

Im **Protected Mode** (ab 80286) verweisen die Segmentregister nicht direkt auf Adressen, sondern auf Einträge in Deskriptor-Tabellen:

**Global Descriptor Table (GDT)**: Systemweite Segmente
**Local Descriptor Table (LDT)**: Prozess-spezifische Segmente

Jeder Deskriptor (8 Bytes) enthält:
- **Base** (32 Bit): Startadresse
- **Limit** (20 Bit): Größe (in Bytes oder 4 KB-Blöcken)
- **Type**: Code/Data, Conforming, Expand-down
- **DPL**: Descriptor Privilege Level (Ring 0-3)
- **Present**, **Accessed**, **Granularity**

### Flat Memory Model

Moderne Betriebssysteme (Linux, Windows, macOS) nutzen das **Flat Memory Model**:
- Alle Segmente haben Base = 0 und Limit = 4 GB (bzw. max)
- Effektiv: Segmentierung wird "umgangen"
- Paging übernimmt vollständig die Speicherverwaltung
- Segmente werden nur noch für **Privilege Level** (Ring 0 vs. Ring 3) genutzt

```c
// Typische GDT-Einträge in Linux
// Segment 0: NULL (Intel-Konvention)
// Segment 1: Kernel Code (Ring 0, Base=0, Limit=4GB)
// Segment 2: Kernel Data (Ring 0, Base=0, Limit=4GB)
// Segment 3: User Code   (Ring 3, Base=0, Limit=4GB)
// Segment 4: User Data   (Ring 3, Base=0, Limit=4GB)
```

### Long Mode (x86-64)

Im **64-Bit Long Mode** ist die Segmentierung noch weiter zurückgedrängt:
- CS, DS, ES, SS: Base und Limit werden ignoriert (implizit 0 und unendlich)
- **FS, GS**: Behalten volle Funktionalität für Thread-Local Storage
  - `RDFSBASE`/`WRFSBASE` Instruktionen für schnellen Zugriff
  - Linux nutzt FS für Thread-Kontext (glibc)
  - Windows nutzt GS für Thread Environment Block (TEB)

---

## Segmentierung in der Praxis

Obwohl Segmentierung auf Betriebssystemebene weitgehend durch Paging ersetzt wurde, lebt das Konzept in anderen Formen weiter:

### Compiler und Linker

Der Linker organisiert Programme in **Sections** (ELF) bzw. **Segments** (PE):
- `.text` – Code
- `.data` – initialisierte Daten
- `.bss` – uninitialisierte Daten
- `.rodata` – Read-only Daten (Strings, Konstanten)

Diese werden beim Laden auf Pages mit passenden Zugriffsrechten abgebildet.

### Memory-Mapped Files

Konzeptionell ähnlich wie Segmente:
- Variable Größe
- Können geteilt werden
- Eigene Zugriffsrechte
- Auf Seitenbasis verwaltet (Kombination)

---

## Zusammenhänge

- [[03-Paging|Paging]] → Alternative/Ergänzung zur Segmentierung
- [[01-Adressraeume|Adressräume]] → Segmente strukturieren den Adressraum
- [[02-Virtueller-Speicher|Virtueller Speicher]] → Segmente können ausgelagert werden

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - Unterschied Segmentierung vs. Paging

> [!question] **Häufige Prüfungsfragen**
> 1. Was ist der Unterschied zwischen Segmentierung und Paging?
> 2. Wie erfolgt die Adressumrechnung bei Segmentierung?
> 3. Was ist externe Fragmentierung und warum tritt sie bei Segmentierung auf?
> 4. Welche Informationen enthält ein Segment-Table-Eintrag?
> 5. Warum kombinieren moderne Systeme Segmentierung mit Paging?
> 6. Warum nutzen moderne Betriebssysteme das Flat Memory Model?

> [!tip] **Merkhilfen**
> - **Segment** = "Kapitel eines Buches" (logische Einheit, variable Länge)
> - **Page** = "Buchseite" (feste Größe, keine logische Bedeutung)
> - **Externe Fragmentierung** = "Lücken zwischen Büchern im Regal"
> - **Interne Fragmentierung** = "Leere Seiten am Ende eines Kapitels"
> - **Flat Model** = "Alle Kapitel zu einem riesigen Buch zusammengebunden"

---

## Weiterführende Ressourcen

> [!note] **Videos (YouTube)**
>
> | | Video | Beschreibung |
> |---|-------|--------------|
> | 🎬 | [CoreDumped – Memory Access](https://www.youtube.com/watch?v=A9WLYbE0p-I) | Speicherorganisation und Adressierung |

> [!note] **Weiterführende Literatur**
>
> - Corbató, F. J., & Vyssotsky, V. A. (1965). Introduction and overview of the Multics system.
> - Intel 64 and IA-32 Architectures Software Developer's Manual, Vol. 3A: System Programming Guide

---

## Quellen

- Tanenbaum: Modern Operating Systems
- Intel x86 Architecture Manual
- Silberschatz, Galvin, Gagne: Operating System Concepts

