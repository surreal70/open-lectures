---
author: Andreas Hümmer
title: IO-Grundlagen
tags:
  - content
  - bs
  - io
  - grundlagen
  - dma
  - interrupt
  - polling
created: '2026-10-07'
modified: '2026-10-09'
bereich: BS
---

# IO-Grundlagen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Rolle des I/O-Subsystems im Betriebssystem verstehen
> - Die drei grundlegenden I/O-Techniken (Polling, Interrupts, DMA) erklären können
> - Den Unterschied zwischen blockierenden und nicht-blockierenden I/O kennen
> - Die Schichten der I/O-Software-Architektur benennen können
> - Buffering, Caching und Spooling unterscheiden können

---

## Definition

> [!quote] **Formale Definition**
> **Ein-/Ausgabe (I/O)** bezeichnet die Kommunikation zwischen dem Prozessor und externen Geräten (Peripherie). Das **I/O-Subsystem** des Betriebssystems abstrahiert die Hardware-Details und bietet Anwendungen eine einheitliche Schnittstelle für den Zugriff auf diverse Geräte.

---

## Das I/O-Problem

Warum ist I/O so herausfordernd für Betriebssysteme?

### Geschwindigkeitsunterschiede

| Gerät | Typische Datenrate | Faktor zu CPU |
|-------|-------------------|---------------|
| **CPU-Register** | ~100 GB/s | 1× |
| **L1-Cache** | ~50 GB/s | 2× |
| **RAM** | ~25 GB/s | 4× |
| **NVMe SSD** | ~7 GB/s | 14× |
| **SATA SSD** | ~600 MB/s | 170× |
| **Festplatte (HDD)** | ~200 MB/s | 500× |
| **Gigabit Ethernet** | ~125 MB/s | 800× |
| **USB 3.0** | ~625 MB/s | 160× |
| **Tastatur** | ~100 B/s | 1.000.000.000× |

Die CPU ist um **Größenordnungen schneller** als I/O-Geräte. Ein Betriebssystem muss diese Diskrepanz effizient überbrücken.

### Heterogenität

I/O-Geräte unterscheiden sich fundamental:

| Eigenschaft | Beispiele |
|-------------|-----------|
| **Dateneinheit** | Byte (Tastatur) vs. Block (Festplatte) |
| **Zugriffsart** | Sequentiell (Band) vs. Random Access (SSD) |
| **Timing** | Synchron (RAM) vs. Asynchron (Netzwerk) |
| **Sharing** | Exklusiv (Drucker) vs. Shared (Festplatte) |
| **Richtung** | Nur Eingabe (Maus), nur Ausgabe (Display), beides (NIC) |

---

## Hardware-Grundlagen

### I/O-Controller

Jedes I/O-Gerät besteht aus zwei Komponenten:
1. **Mechanische/elektronische Komponente**: Das physische Gerät
2. **Controller (Adapter)**: Schnittstelle zwischen Gerät und Systembus

![[io-controller.png|center|600]]
*<span class="fig-id">02-06-01-io-controller</span>: Aufbau eines I/O-Controllers mit seinen Registern*

| Register | Funktion |
|----------|----------|
| **Steuerregister (Control)** | CPU schreibt Befehle (z.B. "Sektor lesen", "Motor starten") |
| **Statusregister (Status)** | Controller meldet Zustand (bereit, beschäftigt, Fehler) |
| **Datenregister (Data-In)** | Empfängt Daten vom Gerät zur Weitergabe an CPU |
| **Datenregister (Data-Out)** | Empfängt Daten von CPU zur Weitergabe an Gerät |

### Ansteuerung von Controllern

**Port-Mapped I/O (PMIO)**:
- Separate I/O-Adressräume
- Spezielle CPU-Instruktionen: `IN`, `OUT`
- Typisch für x86-Architektur

```c
// Port-Mapped I/O auf x86
outb(0x60, data);    // Schreibe data an Port 0x60
byte = inb(0x64);    // Lese von Port 0x64
```

**Memory-Mapped I/O (MMIO)**:
- Controller-Register im normalen Adressraum
- Normale Load/Store-Instruktionen
- Moderne Standardmethode

```c
// Memory-Mapped I/O
volatile uint32_t *device_reg = (uint32_t *)0xFE00B000;
*device_reg = 0x01;   // Schreibe ins Geräteregister
status = *device_reg; // Lese Status
```

| Aspekt | Port-Mapped I/O | Memory-Mapped I/O |
|--------|-----------------|-------------------|
| **Adressraum** | Separater I/O-Raum | Teil des RAM-Adressraums |
| **Instruktionen** | Spezielle (`IN`, `OUT`) | Normale (`MOV`, `LDR`) |
| **Schutz** | Privilegiert (Ring 0) | Über Paging/MMU |
| **Caching** | Kein Problem | Muss deaktiviert werden |
| **Verbreitung** | Legacy x86 | ARM, moderne Geräte |

---

## I/O-Techniken

Das Betriebssystem kennt drei grundlegende Methoden, um mit I/O-Geräten zu kommunizieren:

### 1. Programmed I/O (Polling / Busy Waiting)

Die CPU fragt das Gerät in einer Schleife ab, bis es bereit ist.

![[polling-busy-waiting.png|center|600]]
*<span class="fig-id">02-06-01-polling-busy-waiting</span>: Polling – CPU fragt wiederholt den Gerätestatus ab, bis es bereit ist*

**Pseudocode:**
```c
void print_string(char *s) {
    while (*s != '\0') {
        // Warte bis Drucker bereit
        while ((inb(PRINTER_STATUS) & READY) == 0) {
            // Busy waiting - CPU macht nichts Nützliches
        }
        // Sende Zeichen
        outb(PRINTER_DATA, *s);
        s++;
    }
}
```

| Vorteile | Nachteile |
|----------|-----------|
| Einfach zu implementieren | CPU-Zeit wird verschwendet |
| Keine Interrupt-Handler nötig | Andere Prozesse müssen warten |
| Deterministisches Timing | Nicht skalierbar |

**Anwendungsfall:** Kurze, vorhersagbare Wartezeiten (z.B. Spin-Locks im Kernel)

---

### 2. Interrupt-Driven I/O

Die CPU startet die I/O-Operation und arbeitet andere Aufgaben ab. Das Gerät signalisiert per **Interrupt**, wenn es fertig ist.

![[interrupt-driven-io.png|center|600]]
*<span class="fig-id">02-06-01-interrupt-driven-io</span>: Interrupt-gesteuertes I/O – CPU arbeitet weiter, bis das Gerät per Interrupt meldet*

**Ablauf eines Interrupts:**
1. CPU programmiert Controller und startet Operation
2. CPU führt andere Prozesse aus
3. Controller beendet Operation und löst Interrupt aus
4. CPU unterbricht aktuellen Prozess
5. **Interrupt-Handler** wird ausgeführt
6. Handler verarbeitet Daten und weckt wartenden Prozess
7. CPU kehrt zum unterbrochenen Prozess zurück

| Vorteile | Nachteile |
|----------|-----------|
| CPU-Zeit wird effizient genutzt | Overhead durch Kontextwechsel |
| Gut für langsame Geräte | Interrupt-Handler-Entwicklung komplex |
| Multiprogramming möglich | Bei vielen Interrupts: Livelock-Gefahr |

---

### 3. Direct Memory Access (DMA)

Bei DMA übernimmt ein spezieller **DMA-Controller** die Datenübertragung direkt zwischen Gerät und RAM – **ohne CPU-Beteiligung**.

![[dma-transfer.png|center|650]]
*<span class="fig-id">02-06-01-dma-transfer</span>: DMA – Daten werden ohne CPU-Beteiligung zwischen Gerät und RAM übertragen*

**DMA-Modi:**

| Modus | Beschreibung |
|-------|--------------|
| **Burst Mode** | DMA übernimmt Bus komplett bis Transfer fertig |
| **Cycle Stealing** | DMA "stiehlt" einzelne Bus-Zyklen von der CPU |
| **Transparent** | DMA nutzt nur Bus-Zyklen, die CPU nicht braucht |

**Vorteile von DMA:**
- CPU-Entlastung bei großen Datenmengen
- Höherer Durchsatz (keine Byte-für-Byte-Kopie durch CPU)
- Unverzichtbar für Hochgeschwindigkeits-I/O (NVMe, Netzwerk, GPU)

**Nachteile:**
- Zusätzliche Hardware (DMA-Controller)
- Cache-Kohärenz-Probleme (CPU-Cache vs. DMA)
- Komplexere Programmierung

---

## Vergleich der I/O-Techniken

| Kriterium | Polling | Interrupts | DMA |
|-----------|---------|------------|-----|
| **CPU-Last während I/O** | 100% | Niedrig | Minimal |
| **Latenz** | Niedrig | Mittel (Interrupt-Overhead) | Mittel |
| **Durchsatz** | Niedrig | Mittel | Hoch |
| **Komplexität** | Gering | Mittel | Hoch |
| **Hardware-Aufwand** | Keiner | Interrupt-Controller | DMA-Controller |
| **Typische Anwendung** | Einfache Embedded | Tastatur, Maus | Festplatte, Netzwerk, GPU |

---

## I/O-Software-Schichten

Das I/O-Subsystem ist in mehrere Schichten organisiert, die jeweils spezifische Aufgaben übernehmen:

![[io-software-schichten.png|center|500]]
*<span class="fig-id">02-06-01-io-software-schichten</span>: Die Schichten der I/O-Software von User-Space bis Hardware*

### Schicht 1: Interrupt-Handler

- Wird bei Hardware-Interrupt aufgerufen
- Speichert Zustand, bestätigt Interrupt
- Weckt wartenden Treiber-Thread
- Sollte so kurz wie möglich sein

### Schicht 2: Gerätetreiber

- Kennt die spezifische Hardware
- Übersetzt abstrakte Befehle in Geräte-Kommandos
- Verwaltet Geräte-Register

### Schicht 3: Geräteunabhängige I/O-Software

Diese Schicht bietet einheitliche Funktionen für alle Geräte:

| Funktion | Beschreibung |
|----------|--------------|
| **Naming** | `/dev/sda`, `/dev/tty0` – einheitliche Benennung |
| **Protection** | Zugriffsrechte (rwx) auf Geräte |
| **Buffering** | Pufferung zwischen User-Space und Gerät |
| **Error Handling** | Einheitliche Fehlerbehandlung |
| **Block Size** | Abstraktion unterschiedlicher Blockgrößen |
| **Allocation** | Dedizierte Geräte (Drucker) vs. Shared (Disk) |

### Schicht 4: User-Space I/O

- Standard-Bibliotheken (libc): `printf()`, `fread()`, `fwrite()`
- Spooling-Systeme (z.B. CUPS für Drucker)
- Abstraktion für Anwendungsprogrammierer

---

## Buffering, Caching und Spooling

### Buffering (Pufferung)

Buffering überbrückt Geschwindigkeits- und Größenunterschiede zwischen Produzent und Konsument.

**Buffering-Strategien:**

| Strategie | Beschreibung | Anwendung |
|-----------|--------------|-----------|
| **Unbuffered** | Direkte Übertragung | Echtzeitanwendungen |
| **Single Buffer** | Ein Puffer im Kernel | Einfache Geräte |
| **Double Buffer** | Zwei Puffer abwechselnd | Audio, Video |
| **Circular Buffer** | Ring-Puffer | Netzwerk, Tastatur |

**Double Buffering:**
![[double-buffering.png|center|550]]
*<span class="fig-id">02-06-01-double-buffering</span>: Double Buffering – zwei Puffer werden abwechselnd gefüllt und verarbeitet*

### Caching

**Cache** speichert Kopien häufig genutzter Daten für schnelleren Zugriff.

| Unterschied | Buffering | Caching |
|-------------|-----------|---------|
| **Zweck** | Geschwindigkeitsanpassung | Schneller Wiederzugriff |
| **Kopie** | Einzige Kopie der Daten | Zusätzliche Kopie |
| **Lebensdauer** | Kurz (Transfer) | Länger (bis Verdrängung) |

**I/O-Caches:**
- **Page Cache**: Cacht Datei-Blöcke im RAM
- **Disk Cache**: Controller-interner Cache
- **Write-Back Cache**: Schreibt verzögert (Risiko bei Stromausfall)
- **Write-Through Cache**: Schreibt sofort durch (sicherer, langsamer)

### Spooling

**Spool** = Simultaneous Peripheral Operations On-Line

Spooling ermöglicht mehreren Prozessen die Nutzung eines exklusiven Geräts durch Warteschlangen.

![[spooling.png|center|550]]
*<span class="fig-id">02-06-01-spooling</span>: Spooling – Jobs werden in einer Warteschlange gesammelt und nacheinander abgearbeitet*

**Typische Spooling-Systeme:**
- **Druckerspooler** (CUPS, Windows Print Spooler)
- **E-Mail-Queues** (sendmail, postfix)
- **Batch-Job-Systeme**

---

## Blockierende vs. Nicht-blockierende I/O

### Blockierende I/O (Synchron)

Der aufrufende Prozess wird **suspendiert**, bis die I/O-Operation abgeschlossen ist.

```c
// Blockierender Aufruf
int n = read(fd, buffer, 1024);
// Prozess wartet hier, bis Daten verfügbar
printf("Gelesen: %d Bytes\n", n);
```

**Eigenschaften:**
- Einfaches Programmiermodell
- Prozess verbraucht keine CPU während des Wartens
- Standard für die meisten Anwendungen

### Nicht-blockierende I/O (Asynchron)

Der Aufruf kehrt **sofort** zurück, auch wenn keine Daten verfügbar sind.

```c
// Nicht-blockierender Aufruf
fcntl(fd, F_SETFL, O_NONBLOCK);
int n = read(fd, buffer, 1024);
if (n == -1 && errno == EAGAIN) {
    // Keine Daten verfügbar - später erneut versuchen
}
```

**Eigenschaften:**
- Prozess kann andere Aufgaben erledigen
- Komplexeres Programmiermodell
- Typisch für Server (Event-Loop, select/poll/epoll)

### I/O-Multiplexing

Ermöglicht das gleichzeitige Warten auf mehrere I/O-Quellen:

| Mechanismus | Beschreibung | Skalierbarkeit |
|-------------|--------------|----------------|
| **select()** | Prüft Menge von File-Descriptors | O(n) – schlecht bei vielen FDs |
| **poll()** | Wie select, ohne FD-Limit | O(n) |
| **epoll()** (Linux) | Event-basiert | O(1) – sehr gut |
| **kqueue()** (BSD) | Event-basiert | O(1) – sehr gut |
| **io_uring** (Linux 5.1+) | Asynchron, Kernel-Queue | Sehr hoch |

---

## I/O-Scheduling

Bei mehreren gleichzeitigen I/O-Anfragen muss das Betriebssystem entscheiden, welche zuerst bearbeitet wird.

### Disk-Scheduling-Algorithmen

| Algorithmus | Beschreibung | Vor-/Nachteile |
|-------------|--------------|----------------|
| **FCFS** | First Come, First Served | Einfach, aber ineffizient |
| **SSTF** | Shortest Seek Time First | Besser, aber Starvation möglich |
| **SCAN (Elevator)** | Arm bewegt sich in eine Richtung | Fair, guter Durchsatz |
| **C-SCAN** | Wie SCAN, aber nur eine Richtung | Gleichmäßigere Wartezeiten |
| **LOOK / C-LOOK** | Wie SCAN, stoppt am letzten Request | Effizienter |

> [!info] **Nicht prüfungsrelevant: Moderne SSDs**
> Bei SSDs ohne mechanische Teile ist Disk-Scheduling weniger relevant. Moderne Systeme nutzen oft einfache Queues oder I/O-Prioritäten statt komplexer Algorithmen.

---

## Zusammenhänge

- [[../02-Architektur/02-Schichtenmodell|Schichtenmodell]] → I/O als Teil der BS-Architektur
- [[../03-Prozesse/01-Prozessmodell|Prozessmodell]] → Prozesse warten auf I/O (blockiert-Zustand)
- [[../04-Synchronisation/01-Einfuehrung-Synchronisation|Synchronisation]] → I/O erfordert Synchronisation (Buffer-Zugriff)

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - Unterschied Polling vs. Interrupts vs. DMA

> [!question] **Häufige Prüfungsfragen**
> 1. Erklären Sie den Unterschied zwischen Polling und Interrupt-driven I/O!
> 2. Warum ist DMA bei großen Datenmengen effizienter als Interrupt-driven I/O?
> 3. Welche Aufgaben hat die geräteunabhängige I/O-Software?
> 4. Was ist der Unterschied zwischen Buffering und Caching?
> 5. Wann verwendet man blockierende, wann nicht-blockierende I/O?

> [!tip] **Merkhilfen**
> - **Polling** = "Ich frage ständig: Bist du fertig?" (CPU wartet aktiv)
> - **Interrupt** = "Ruf mich an, wenn du fertig bist!" (CPU macht anderes)
> - **DMA** = "Mach das unter euch aus, ich hab Besseres zu tun!" (CPU unbeteiligt)
> - **Buffer** = Übergabestation (temporär), **Cache** = Kopie für schnellen Zugriff

---

## Weiterführende Ressourcen

> [!note] **Videos (YouTube)**
>
> | | Video | Beschreibung |
> |---|-------|--------------|
> | 🎬 | [Neso Academy – I/O Systems](https://www.youtube.com/watch?v=F18RiREDkwE) | Grundlagen der I/O-Systeme |
> | 🎬 | [Jacob Sorber – Blocking vs Non-Blocking I/O](https://www.youtube.com/watch?v=wB9tIg209-8) | Praktische Unterschiede in C |

---

## Quellen

- Tanenbaum, A. S.: Modern Operating Systems, Kapitel 5
- Silberschatz, Galvin, Gagne: Operating System Concepts, Kapitel 13
- Love, R.: Linux Kernel Development, Kapitel 14

