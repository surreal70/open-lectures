---
author: Andreas Hümmer
title: CPU-Architekturen im Wandel der Zeit
tags:
  - content
- bs
- architektur
- hardware
- cpu
- intel
- amd
created: '2026-10-07'
modified: '2026-10-07'
bereich: BS
---
author: Andreas Hümmer

# CPU-Architekturen im Wandel der Zeit

> [!info] **Übersicht**
> Diese Datei dokumentiert die Entwicklung der x86-CPU-Architektur von den Anfängen (8086/8088) bis zu modernen Designs (Intel Core, AMD Zen).

> [!note] **Zu den Blockdiagrammen**
> Die Blockdiagramme in diesem Kapitel heben vor allem die **relevanten Neuerungen und Änderungen** gegenüber dem jeweiligen Vorgänger hervor – sie zeigen nicht zwingend das vollständige Blockdiagramm der gesamten CPU. Bereits bekannte oder unveränderte Einheiten werden teils weggelassen oder nur verkürzt dargestellt, um den Fokus auf das Wesentliche zu legen.

---
author: Andreas Hümmer

## Intel 8086/8088 (1978/1979)

Der **Beginn der x86-Ära** – diese Prozessoren legten den Grundstein für die dominierende PC-Architektur der nächsten Jahrzehnte.

### Technische Daten

| Eigenschaft | Intel 8086 | Intel 8088 |
|-------------|------------|------------|
| **Erscheinungsjahr** | 1978 | 1979 |
| **Transistoren** | 29.000 | 29.000 |
| **Taktfrequenz** | 5-10 MHz | 5-8 MHz |
| **Adressbus** | 20 Bit (1 MB) | 20 Bit (1 MB) |
| **Datenbus extern** | 16 Bit | 8 Bit |
| **Datenbus intern** | 16 Bit | 16 Bit |
| **Fertigung** | 3 µm | 3 µm |
| **Gehäuse** | DIP-40 | DIP-40 |

> [!note] **Warum 8088 im IBM PC?**
> Der 8088 wurde für den ersten IBM PC (1981) gewählt, weil der 8-Bit externe Datenbus günstigere 8-Bit-Peripheriebausteine ermöglichte – ein Kostenkompromiss.

### Pinbelegung (DIP-40)

![[.assets/intel-8088-pinout.png]]

Die wichtigsten Signalgruppen des DIP-40-Gehäuses:

- **AD0–AD7** – Gemultiplexter Adress-/Datenbus (8 Bit); Daten und untere Adressbits teilen sich dieselben Leitungen
- **A8–A19** – Adressleitungen (obere 12 Bit)
- **CLK** – Takteingang
- **RESET** – Prozessor-Reset
- **INTR** – Interrupt Request (maskierbar)
- **NMI** – Non-Maskable Interrupt

### Blockdiagramm

![[.assets/intel-8088-blockdiagramm.png]]

Der 8088 teilt sich in zwei Einheiten: Die **Execution Unit (EU)** führt Befehle aus und enthält die Allgemein- und Flag-Register sowie die 16-Bit-ALU. Die **Bus Interface Unit (BIU)** kümmert sich um den Speicherzugriff – sie bildet über den Adress-Addierer aus Segment und Offset die physische 20-Bit-Adresse (`Segment × 16 + Offset`) und füllt parallel die 4-Byte-Instruction-Queue vor (Prefetch). Beide Einheiten arbeiten überlappend: Während die EU rechnet, holt die BIU bereits den nächsten Befehl.

---
author: Andreas Hümmer

## Intel 80286 (1982)

Der **erste x86-Prozessor mit Protected Mode** – ein Meilenstein für Speicherschutz und Multitasking.

### Technische Daten

| Eigenschaft | Wert |
|-------------|------|
| **Erscheinungsjahr** | 1982 |
| **Transistoren** | 134.000 |
| **Taktfrequenz** | 6-25 MHz |
| **Adressbus** | 24 Bit (16 MB adressierbar) |
| **Datenbus** | 16 Bit |
| **Fertigung** | 1,5 µm |
| **Gehäuse** | PLCC-68, PGA-68 |

### Wichtige Neuerungen

| Feature | Beschreibung |
|---------|--------------|
| **Protected Mode** | Speicherschutz durch Hardware (aber kein Rückweg zu Real Mode!) |
| **Segmentierung** | Segmente mit Deskriptoren und Zugriffsrechten |
| **Privilege Levels** | 4 Ringe (Ring 0-3) für Rechteverwaltung |
| **Multitasking** | Hardware-Unterstützung durch Task State Segment (TSS) |
| **24-Bit Adressen** | 16 MB adressierbar (statt 1 MB beim 8086) |

> [!warning] **Designfehler**
> Der 80286 konnte zwar in den Protected Mode wechseln, aber **nicht zurück** in den Real Mode – außer durch einen Reset! Dies machte die Nutzung in DOS-Umgebungen problematisch und wurde erst mit dem 80386 korrigiert.

### Vereinfachtes Blockdiagramm

![[.assets/intel-80286-blockdiagramm.png]]

Der 80286 gliedert sich in drei Einheiten. Die eigentliche Neuerung ist die **Protection Unit** innerhalb der Address Unit: Sie prüft bei jedem Speicherzugriff die Descriptor-Tabellen (GDT/LDT), die Privilegstufe (Ring 0–3) und das Segment-Limit – die Grundlage des **Protected Mode**. Die Execution Unit erweitert die 8086-Register um das Machine Status Word (MSW), und die Bus Unit bedient einen 24-Bit-Adressbus (16 MB adressierbar) mit 6-Byte-Prefetch-Queue.

---
author: Andreas Hümmer

## Intel 80386 (1985)

Der **erste echte 32-Bit x86-Prozessor** – ein revolutionärer Sprung, der die Grundlage für moderne Betriebssysteme wie Windows und Linux legte.

### Technische Daten

| Eigenschaft | Wert |
|-------------|------|
| **Erscheinungsjahr** | 1985 |
| **Transistoren** | 275.000 |
| **Taktfrequenz** | 16-40 MHz |
| **Adressbus** | 32 Bit (4 GB adressierbar) |
| **Datenbus** | 32 Bit |
| **Fertigung** | 1,5 µm → 1,0 µm |
| **Gehäuse** | PGA-132 |

### Wichtige Neuerungen

| Feature | Beschreibung |
|---------|--------------|
| **32-Bit Architektur** | Volle 32-Bit Register (EAX, EBX, ECX, EDX, etc.) |
| **Paging** | 4 KB Seiten ermöglichen virtuellen Speicher |
| **Virtual 8086 Mode** | DOS-Programme im Protected Mode ausführen |
| **Mode-Wechsel** | Rückkehr von Protected zu Real Mode möglich (80286-Fix!) |
| **Debug-Register** | Hardware-Unterstützung für Debugging (DR0-DR7) |
| **Neue Segmentregister** | FS und GS zusätzlich zu CS, DS, SS, ES |

> [!tip] **Meilenstein für Betriebssysteme**
> Der 80386 mit Paging ermöglichte erstmals echten virtuellen Speicher und Speicherschutz auf x86. Linux, Windows NT und OS/2 basierten alle auf dieser Architektur.

### Blockdiagramm

![[.assets/intel-80386-blockdiagramm.png]]

Der 80386 ist der erste vollwertige 32-Bit-x86-Prozessor und bringt zwei Neuerungen, die bis heute das Fundament moderner Betriebssysteme bilden: die **Control-Register** (CR0/CR2/CR3) und vor allem die **Paging Unit**. Eine lineare 32-Bit-Adresse wird in Directory (10 Bit), Table (10 Bit) und Offset (12 Bit) zerlegt und über zwei Tabellenstufen in einen physischen Frame übersetzt; der TLB cached die letzten Übersetzungen. Erst dieses hardwaregestützte Paging macht echten virtuellen Speicher mit Demand Paging praktikabel.

---
author: Andreas Hümmer

## Intel 80486 (1989)

Die **Integration von FPU und Cache auf dem Die** – ein entscheidender Schritt zur modernen CPU-Architektur.

### Technische Daten

| Eigenschaft | Wert |
|-------------|------|
| **Erscheinungsjahr** | 1989 |
| **Transistoren** | 1,2 Millionen |
| **Taktfrequenz** | 25-100 MHz |
| **Adressbus** | 32 Bit (4 GB) |
| **Datenbus** | 32 Bit |
| **Fertigung** | 1,0 µm → 0,6 µm |
| **Gehäuse** | PGA-168 |

### Wichtige Neuerungen

| Feature | Beschreibung |
|---------|--------------|
| **Integrierte FPU** | x87-Koprozessor erstmals auf dem CPU-Die (vorher separater 80387) |
| **On-Die L1 Cache** | 8 KB unified Cache direkt auf dem Chip |
| **5-stufige Pipeline** | RISC-ähnliche Pipeline für höheren Durchsatz |
| **Burst Mode** | Schnellere Speicherzugriffe für Cache-Fills |

> [!note] **Performance-Sprung**
> Durch Pipeline und On-Die Cache erreichte der 486 etwa **doppelte Performance pro MHz** im Vergleich zum 386. Dies war der erste x86-Prozessor mit echtem Pipelining.

> [!info] **486SX vs. 486DX**
> Der günstigere **486SX** hatte die FPU deaktiviert (oder defekt) – ein früher Vorläufer des "Binning" bei modernen CPUs.

### Pipeline-Struktur (5 Stufen)

Die 80486-Pipeline war die erste echte Pipeline in der x86-Familie:

| Stufe | Kürzel | Funktion |
|-------|--------|----------|
| 1 | **IF** | Instruction Fetch – Befehl aus L1 Cache oder Bus holen |
| 2 | **D1** | Decode 1 – Befehl dekodieren |
| 3 | **D2** | Decode 2 – Operanden holen |
| 4 | **EX** | Execute – ALU/FPU Operation ausführen |
| 5 | **WB** | Write Back – Ergebnis zurückschreiben |

**Pipeline-Ablauf (Beispiel):**

| Takt | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|------|---|---|---|---|---|---|---|---|---|
| Befehl 1 | IF | D1 | D2 | EX | WB | | | | |
| Befehl 2 | | IF | D1 | D2 | EX | WB | | | |
| Befehl 3 | | | IF | D1 | D2 | EX | WB | | |
| Befehl 4 | | | | IF | D1 | D2 | EX | WB | |
| Befehl 5 | | | | | IF | D1 | D2 | EX | WB |

> [!tip] **Idealer Durchsatz**
> Im Idealfall: **1 Befehl pro Takt** (CPI = 1). In der Praxis reduzieren Pipeline-Stalls durch Datenabhängigkeiten und Cache-Misses den Durchsatz.

### Blockdiagramm

![[.assets/intel-80486-blockdiagramm.png]]

Der 80486 integriert erstmals mehrere bisher getrennte Bausteine auf einem Die: einen **8-KB-L1-Cache**, die **FPU** (der externe 80387-Coprozessor entfällt) und die oben gezeigte fünfstufige Integer-Pipeline. Durch Pipelining und On-Chip-Cache erreicht der 486 bei gleicher Taktfrequenz etwa die doppelte Leistung des 80386.

---
author: Andreas Hümmer

## Intel Pentium (1993)

Die **erste superskalare x86-Architektur** – zwei Befehle gleichzeitig in parallelen Pipelines.

### Technische Daten

| Eigenschaft | Wert |
|-------------|------|
| **Erscheinungsjahr** | 1993 |
| **Transistoren** | 3,1 Millionen |
| **Taktfrequenz** | 60-300 MHz |
| **Adressbus** | 32 Bit |
| **Datenbus** | 64 Bit (extern) |
| **Fertigung** | 0,8 µm → 0,35 µm |
| **Gehäuse** | PGA-273, SPGA-296 |

### Wichtige Neuerungen

| Feature | Beschreibung |
|---------|--------------|
| **Superskalar** | 2 Integer Pipelines (U-Pipe und V-Pipe) für parallele Befehlsausführung |
| **Getrennte L1 Caches** | 8 KB Code-Cache + 8 KB Daten-Cache (Harvard-Architektur intern) |
| **64-Bit Datenbus** | Doppelte Speicherbandbreite gegenüber 486 |
| **Branch Prediction** | Sprungvorhersage reduziert Pipeline-Stalls |
| **Pipelined FPU** | Schnellere Gleitkommaoperationen |

> [!tip] **Superskalar = mehrere Befehle pro Takt**
> Der Pentium konnte unter idealen Bedingungen **2 Befehle pro Takt** ausführen (CPI < 1). Die U-Pipe konnte alle Befehle, die V-Pipe nur einfache Integer-Befehle.

> [!warning] **FDIV-Bug**
> Frühe Pentium-CPUs hatten einen Fehler in der Fließkomma-Division, der zu falschen Ergebnissen führte. Intel ersetzte betroffene CPUs kostenlos – ein PR-Desaster, das die Firma ~475 Mio. Dollar kostete.

### Dual-Pipeline Architektur

![[.assets/intel-pentium-blockdiagramm.png]]

Der Pentium ist der erste **superskalare** x86-Prozessor: Er dekodiert zwei Befehle pro Takt und verteilt sie auf zwei parallele Integer-Pipelines (U-Pipe und V-Pipe). Im Idealfall werden so zwei Befehle gleichzeitig ausgeführt (CPI < 1). Nicht jedes Befehlspaar lässt sich jedoch parallelisieren – es gelten strenge **Pairing-Regeln**:

- Keine Datenabhängigkeiten zwischen dem Befehl in U und dem in V
- Die V-Pipe führt nur einfache Befehle aus (ADD, SUB, MOV, …)
- Keine Speicher-Speicher-Operationen in der V-Pipe

Sind diese Bedingungen nicht erfüllt, läuft der zweite Befehl im nächsten Takt – die Pipelines fallen auf skalaren Durchsatz zurück.

---
author: Andreas Hümmer

## Intel Pentium Pro / P6 (1995)

Der *Beginn der modernen x86-Mikroarchitektur** – diese revolutionäre Architektur bildet bis heute die Basis aller Intel Core CPUs.*

### Technische Daten

| Eigenschaft | Wert |
|-------------|------|
| **Erscheinungsjahr** | 1995 |
| **Transistoren** | 5,5 Mio. (+ 15,5 Mio. für L2 Cache) |
| **Taktfrequenz** | 150-200 MHz |
| **Fertigung** | 0,35 µm |
| **Gehäuse** | PGA-387 (Dual-Cavity mit L2 Cache) |

### Revolutionäre Neuerungen

| Feature | Beschreibung |
|---------|--------------|
| **Out-of-Order Execution** | Befehle werden nicht in Programmreihenfolge ausgeführt, sondern sobald Operanden bereit sind |
| **Register Renaming** | Mehr physische als architekturelle Register eliminieren falsche Abhängigkeiten |
| **Speculative Execution** | Befehle werden spekulativ ausgeführt, bevor Sprungentscheidungen feststehen |
| **µOp Decomposition** | CISC-Befehle werden intern in RISC-ähnliche Micro-Ops zerlegt |
| **Integrierter L2 Cache** | 256-512 KB L2 Cache auf dem Package (nicht Die) |
| **3-Way Superscalar** | Bis zu 3 µOps pro Takt ausführbar |

> [!warning] **Architektur-Meilenstein**
> Die P6-Mikroarchitektur war so erfolgreich, dass ihre Grundprinzipien (Out-of-Order, µOps, Register Renaming) in **allen** nachfolgenden Intel-CPUs bis heute verwendet werden: Pentium II, Pentium III, Core, Core 2, Nehalem, Sandy Bridge, Skylake, Alder Lake...

> [!note] **CISC außen, RISC innen**
> Der Pentium Pro erscheint nach außen als CISC-Prozessor (x86-Befehlssatz), arbeitet intern aber wie ein RISC-Prozessor mit einfachen Micro-Operations (µOps).

### P6 Mikroarchitektur

![[.assets/intel-p6-mikroarchitektur.png]]

Die **P6-Mikroarchitektur** ist der tiefgreifendste Umbruch der x86-Geschichte und bildet die Grundlage aller folgenden Intel-Kerne bis heute. Das Frontend arbeitet noch **in-order**: Es holt x86-Befehle, zerlegt sie in RISC-artige **µOps** und benennt über die Register Alias Table die 8 architekturellen auf 40 physische Register um (eliminiert WAR-/WAW-Scheinabhängigkeiten). Das Backend arbeitet **out-of-order**: Der Reorder Buffer verwaltet alle µOps spekulativ, die Reservation Stations geben sie an die Execution Units frei, sobald deren Operanden bereitstehen – unabhängig von der Programmreihenfolge. Erst beim Commit (Retire) wird das Ergebnis in-order sichtbar. So entkoppelt der P6 die Ausführungsreihenfolge von der Programmreihenfolge und hält die Rechenwerke ausgelastet.

---
author: Andreas Hümmer

## AMD K7 / Athlon (1999)

**AMDs erster komplett eigenentwickelter x86-Prozessor** – der Beginn von AMDs Aufstieg zum ernsthaften Intel-Konkurrenten.

### Technische Daten

| Eigenschaft | Wert |
|-------------|------|
| **Erscheinungsjahr** | 1999 |
| **Transistoren** | 22 Millionen |
| **Taktfrequenz** | 500 MHz - 1,4 GHz |
| **Fertigung** | 0,25 µm → 0,18 µm |
| **Gehäuse** | Slot A, später Socket A |

### Wichtige Neuerungen

| Feature | Beschreibung |
|---------|--------------|
| **Erster 1 GHz x86** | AMD erreichte als erster Hersteller die 1-GHz-Marke (März 2000) |
| **EV6 Bus** | 200 MHz DDR = 400 MT/s, lizenziert von DECs Alpha-Prozessor |
| **9-stufige Pipeline** | Längere Pipeline für höhere Taktraten |
| **6 Execution Units** | 3 Integer + 3 FP Pipelines (superskalare FPU) |
| **128 KB L1 Cache** | 64 KB I-Cache + 64 KB D-Cache (deutlich mehr als Intel) |
| **Superscalar FPU** | Erste x86-FPU mit mehreren parallelen Pipelines |

> [!tip] **Das GHz-Rennen**
> AMD schlug Intel im "GHz-Rennen" und erreichte am 6. März 2000 als erster Hersteller 1 GHz. Intel folgte nur wenige Tage später. Der Athlon war zu dieser Zeit in vielen Benchmarks schneller als Intels Pentium III.

> [!note] **Alpha-DNA**
> Viele K7-Ingenieure kamen von DEC und brachten Technologien des legendären Alpha-Prozessors mit – darunter den schnellen EV6-Bus und fortschrittliche Out-of-Order-Techniken.

### K7 Blockdiagramm

![[.assets/amd-k7-blockdiagramm.png]]

Der K7/Athlon war 1999 die erste x86-CPU, die Intel bei der Taktfrequenz überholte. Auffällig sind die großzügigen **64-KB-L1-Caches** (doppelt so groß wie beim Pentium III), die drei vollwertigen Decoder (bis zu 6 µOps/Takt) und die **getrennten Scheduler** für Integer und Floating Point mit jeweils eigenen Ausführungseinheiten. Der Systembus übernimmt das leistungsfähige **EV6-Protokoll** aus der DEC-Alpha-Welt und ersetzt den geteilten Bus durch eine Punkt-zu-Punkt-Verbindung.

---
author: Andreas Hümmer

## AMD64 / x86-64 (2003)

**AMD erfindet die 64-Bit Erweiterung für x86** – ein strategischer Coup, der Intel zur Übernahme von AMDs Architektur zwang.

### Einführung

| Prozessor | Jahr | Bedeutung |
|-----------|------|-----------|
| **AMD Opteron** | April 2003 | Erster x86-64 Prozessor (Server) |
| **AMD Athlon 64** | September 2003 | Erster x86-64 für Desktop |
| **Intel Xeon (Nocona)** | Juni 2004 | Intel übernimmt AMD64 als "EM64T" |

### Register-Erweiterungen

| Vorher (32-Bit) | Nachher (64-Bit) | Beschreibung |
|-----------------|------------------|--------------|
| EAX, EBX, ECX, EDX | RAX, RBX, RCX, RDX | Auf 64 Bit erweitert |
| ESI, EDI, ESP, EBP | RSI, RDI, RSP, RBP | Auf 64 Bit erweitert |
| EIP | RIP | + RIP-relative Adressierung |
| – | **R8 - R15** | **8 komplett neue Register!** |

### Register-Layout

![[.assets/amd64-register-layout.png]]

Jedes 64-Bit-Register enthält seine kleineren Vorgänger als **niederwertige Teilregister**: RAX umfasst EAX (untere 32 Bit), darin AX (untere 16 Bit), darin AH und AL (je 8 Bit). Die acht neuen Register R8–R15 folgen demselben Schema mit den Suffixen D (32), W (16) und B (8), besitzen aber kein getrenntes High-Byte wie das historische AH.

### Weitere Neuerungen

| Feature | Beschreibung |
|---------|--------------|
| **8 neue SSE-Register** | XMM8-XMM15 zusätzlich zu XMM0-XMM7 |
| **48-Bit virtuelle Adressen** | 256 TB adressierbarer Speicher |
| **40-52 Bit physische Adressen** | 1 TB bis 4 PB RAM möglich |
| **NX-Bit** | No-Execute Bit für Sicherheit (verhindert Code-Ausführung in Daten) |
| **Neues Calling Convention** | Mehr Argumente in Registern statt auf dem Stack |

> [!warning] **Intel musste AMD folgen**
> Intel hatte mit **Itanium (IA-64)** eine eigene 64-Bit Architektur entwickelt, die nicht x86-kompatibel war. AMDs pragmatischer Ansatz (x86 erweitern statt ersetzen) setzte sich durch. Intel musste AMD64 als "Intel 64" oder "EM64T" übernehmen – eine seltene Situation, in der der Marktführer die Architektur des Konkurrenten lizenziert.

---
author: Andreas Hümmer

## Intel Core (2006)

**Die Ablösung der NetBurst-Architektur (Pentium 4)** – Intel kehrt zu Effizienz statt reiner Taktrate zurück.

### Technische Daten (Core 2 Duo "Conroe")

| Eigenschaft | Wert |
|-------------|------|
| **Erscheinungsjahr** | 2006 |
| **Transistoren** | 291 Millionen (2 Kerne) |
| **Taktfrequenz** | 1,86 - 3,0 GHz |
| **Fertigung** | 65 nm |
| **L1 Cache** | 32 KB I + 32 KB D pro Kern |
| **L2 Cache** | 2-4 MB shared |

### Design-Philosophie

| Aspekt | NetBurst (Pentium 4) | Core |
|--------|---------------------|------|
| **Fokus** | Maximale MHz | Performance per Watt |
| **Pipeline** | 31 Stufen | 14 Stufen |
| **Basis** | Neuentwicklung | Pentium M (Mobile) |
| **Strategie** | Länger & schneller takten | Breiter & effizienter |

### Wichtige Neuerungen

| Feature | Beschreibung |
|---------|--------------|
| **4-fach Dekoder** | 1 komplexer + 3 einfache Decoder |
| **Macro-Op Fusion** | Mehrere x86-Befehle zu einer µOp verschmelzen |
| **128-Bit SSE** | Volle SSE-Operationen in einem Takt |
| **Shared L2 Cache** | Kerne teilen sich L2 Cache dynamisch |

> [!warning] **Das Ende von NetBurst**
> Intels Pentium 4 (NetBurst) war auf hohe Taktraten optimiert, lief aber heiß und ineffizient. Die 31-stufige Pipeline führte zu hohen Branch-Penalties. Intel musste die Architektur aufgeben und griff auf das effiziente **Pentium M Design** aus dem Mobile-Bereich zurück – die Basis für alle modernen Core-Prozessoren.

> [!tip] **Performance-Sprung**
> Der Core 2 Duo war bei gleichem Takt oft **40-50% schneller** als ein Pentium 4 und verbrauchte dabei deutlich weniger Strom.

### Core 2 Duo Blockdiagramm

![[.assets/intel-core2duo-blockdiagramm.png]]

Mit dem Core 2 Duo wird **Mehrkern-Technik** im Mainstream Standard: Zwei vollständige, identische Kerne sitzen auf einem Die. Jeder Kern besitzt eigene L1-Caches und eine komplette Out-of-Order-Pipeline, teilt sich aber mit dem anderen Kern einen gemeinsamen **L2-Cache** (4 MB). Der geteilte L2 erlaubt es, Daten zwischen den Kernen ohne Umweg über den Hauptspeicher auszutauschen. Nach außen führt noch der klassische **Front Side Bus** zum Chipsatz – ein Flaschenhals, den AMD mit integriertem Speichercontroller zu diesem Zeitpunkt bereits umgangen hatte.

---
author: Andreas Hümmer

## AMD Zen Architektur (2017-)

**Die Renaissance von AMD** – nach Jahren der Intel-Dominanz kehrt AMD mit einer komplett neuen Architektur an die Spitze zurück.

### Zen Generationen

| Generation | Jahr | Fertigung | Produkte | Highlights |
|------------|------|-----------|----------|------------|
| **Zen 1** | 2017 | 14nm | Ryzen 1000, EPYC Naples | Neue Architektur, IPC +52% vs. Excavator |
| **Zen+** | 2018 | 12nm | Ryzen 2000 | Optimiertes Zen 1, höhere Taktraten |
| **Zen 2** | 2019 | 7nm | Ryzen 3000, EPYC Rome | Chiplet-Design, verdoppelte Kerne |
| **Zen 3** | 2020 | 7nm | Ryzen 5000, EPYC Milan | Unified L3, +19% IPC |
| **Zen 4** | 2022 | 5nm | Ryzen 7000, EPYC Genoa | AVX-512, DDR5, PCIe 5.0 |
| **Zen 5** | 2024 | 4nm | Ryzen 9000 | Breitere Ausführung, +16% IPC |

### Wichtige Eigenschaften

| Feature | Beschreibung |
|---------|--------------|
| **SMT** | Simultaneous Multithreading – 2 Threads pro Kern |
| **CCX Design** | Core Complex – Kerne gruppiert mit geteiltem L3 Cache |
| **Chiplet-Architektur** | CPU-Dies (CCD) getrennt von I/O-Die (ab Zen 2) |
| **Infinity Fabric** | Schneller Interconnect zwischen Chiplets |
| **Große L3 Caches** | Bis zu 32 MB pro CCX, 96 MB+ pro CPU |

> [!tip] **Das Chiplet-Geheimnis**
> Ab Zen 2 trennte AMD die CPU-Kerne (CCD) vom I/O-Controller (IOD). Die CCDs werden im neuesten Prozess gefertigt (7nm/5nm), der IOD im älteren, günstigeren Prozess (14nm/12nm). Das ermöglicht mehr Kerne bei niedrigeren Kosten und besseren Yields.

> [!warning] **Comeback-Story**
> Nach den schwachen "Bulldozer"-Jahren (2011-2017) galt AMD als abgeschlagen. Zen änderte alles: Der Ryzen 1800X war 2017 der erste AMD-Prozessor seit Jahren, der mit Intels High-End konkurrieren konnte – zum halben Preis. Mit Zen 3 überholte AMD Intel erstmals auch bei der Single-Thread-Performance.

### Zen 3 CCX (Core Complex)

```
┌───────────────────────────────────────────────────────────────────────────────┐
│                    ZEN 3 CORE COMPLEX (CCX)                                   │
│                    (8 Kerne mit Unified L3)                                   │
├───────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│  ┌─────────────────────────────────────────────────────────────────────────┐  │
│  │                         8 ZEN 3 KERNE                                   │  │
│  │                                                                         │  │
│  │  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐│  │
│  │  │Core 0│ │Core 1│ │Core 2│ │Core 3│ │Core 4│ │Core 5│ │Core 6│ │Core 7││  │
│  │  │      │ │      │ │      │ │      │ │      │ │      │ │      │ │      ││  │
│  │  │L1 I$ │ │L1 I$ │ │L1 I$ │ │L1 I$ │ │L1 I$ │ │L1 I$ │ │L1 I$ │ │L1 I$ ││  │
│  │  │32 KB │ │32 KB │ │32 KB │ │32 KB │ │32 KB │ │32 KB │ │32 KB │ │32 KB ││  │
│  │  │      │ │      │ │      │ │      │ │      │ │      │ │      │ │      ││  │
│  │  │L1 D$ │ │L1 D$ │ │L1 D$ │ │L1 D$ │ │L1 D$ │ │L1 D$ │ │L1 D$ │ │L1 D$ ││  │
│  │  │32 KB │ │32 KB │ │32 KB │ │32 KB │ │32 KB │ │32 KB │ │32 KB │ │32 KB ││  │
│  │  │      │ │      │ │      │ │      │ │      │ │      │ │      │ │      ││  │
│  │  │ L2$  │ │ L2$  │ │ L2$  │ │ L2$  │ │ L2$  │ │ L2$  │ │ L2$  │ │ L2$  ││  │
│  │  │512 KB│ │512 KB│ │512 KB│ │512 KB│ │512 KB│ │512 KB│ │512 KB│ │512 KB││  │
│  │  └──┬───┘ └──┬───┘ └──┬───┘ └──┬───┘ └──┬───┘ └──┬───┘ └──┬───┘ └──┬───┘│  │
│  │     │        │        │        │        │        │        │        │    │  │
│  │     └────────┴────────┴────────┴────────┴────────┴────────┴────────┘    │  │
│  │                               │                                         │  │
│  │                               ▼                                         │  │
│  │  ┌──────────────────────────────────────────────────────────────┐       │  │
│  │  │               UNIFIED L3 CACHE (32 MB)                       │       │  │
│  │  │                                                              │       │  │
│  │  │   Alle 8 Kerne teilen sich den gesamten L3 Cache             │       │  │
│  │  │   (Zen 2 hatte 2×4 Kerne mit je 16 MB = nicht unified)       │       │  │
│  │  │                                                              │       │  │
│  │  │   16-Way Set Associative                                     │       │  │
│  │  │   64 Byte Cache Lines                                        │       │  │
│  │  └──────────────────────────────────────────────────────────────┘       │  │
│  │                               │                                         │  │
│  └───────────────────────────────┼─────────────────────────────────────────┘  │
│                                  │                                            │
│                                  ▼                                            |
│  ┌──────────────────────────────────────────────────────────────────┐         │
│  │                    INFINITY FABRIC                               │         │
│  │                                                                  │         │
│  │   • Verbindet CCX mit Memory Controller (I/O Die)                │         │
│  │   • Verbindet mehrere CCDs in Multi-Chiplet Designs              │         │
│  │   • Skaliert von 1 CCD (8 Kerne) bis 8 CCDs (64 Kerne, EPYC)     │         │
│  └──────────────────────────────────────────────────────────────────┘         │
│                                                                               │
└───────────────────────────────────────────────────────────────────────────────┘
```

### Zen 3 Kern-Architektur

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ZEN 3 EINZELNER KERN                                 │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌───────────────────────────────────────────────────────────────────┐  │
│  │                         FRONTEND                                  │  │
│  │                                                                   │  │
│  │   ┌─────────────────────────────────────────────────────────┐     │  │
│  │   │  Branch Prediction                                      │     │  │
│  │   │  • TAGE Predictor                                       │     │  │
│  │   │  • 6.5K BTB Entries                                     │     │  │
│  │   │  • 512 Indirect Target Array                            │     │  │
│  │   └─────────────────────────────────────────────────────────┘     │  │
│  │                              │                                    │  │
│  │   ┌─────────────────────────────────────────────────────────┐     │  │
│  │   │  L1 Instruction Cache: 32 KB, 8-Way                     │     │  │
│  │   └─────────────────────────────────────────────────────────┘     │  │
│  │                              │                                    │  │
│  │   ┌─────────────────────────────────────────────────────────┐     │  │
│  │   │  Op Cache: 4K µOps (Decoded Instruction Cache)          │     │  │
│  │   │  Bypass für häufig genutzte Befehlssequenzen            │     │  │
│  │   └─────────────────────────────────────────────────────────┘     │  │
│  │                              │                                    │  │
│  │   ┌─────────────────────────────────────────────────────────┐     │  │
│  │   │  4 Decoder (bis zu 8 µOps/Takt)                         │     │  │
│  │   │  Macro-Op Fusion (CMP+JCC, TEST+JCC)                    │     │  │
│  │   └─────────────────────────────────────────────────────────┘     │  │
│  └───────────────────────────────────────────────────────────────────┘  │
│                              │                                          │
│  ┌───────────────────────────────────────────────────────────────────┐  │
│  │                         EXECUTION                                 │  │
│  │                                                                   │  │
│  │   ┌─────────────────────────────────────────────────────────┐     │  │
│  │   │  Integer Scheduler: 4 × 24 Entries = 96                 │     │  │
│  │   │                                                         │     │  │
│  │   │   ┌────┐ ┌────┐ ┌────┐ ┌────┐                           │     │  │
│  │   │   │ALU │ │ALU │ │ALU │ │ALU │   4× Integer ALU          │     │  │
│  │   │   └────┘ └────┘ └────┘ └────┘                           │     │  │
│  │   │   ┌─────────┐ ┌─────────┐                               │     │  │
│  │   │   │  AGU    │ │  AGU    │ │  AGU    │   3× Address Gen  │     │  │
│  │   │   └─────────┘ └─────────┘ └─────────┘                   │     │  │
│  │   │   ┌─────────┐                                           │     │  │
│  │   │   │ Branch  │                        1× Branch Unit     │     │  │
│  │   │   └─────────┘                                           │     │  │
│  │   └─────────────────────────────────────────────────────────┘     │  │
│  │                                                                   │  │
│  │   ┌─────────────────────────────────────────────────────────┐     │  │
│  │   │  Floating Point / SIMD Scheduler: 2 × 32 = 64 Entries   │     │  │
│  │   │                                                         │     │  │
│  │   │   ┌──────────────────────────────────────────────────┐  │     │  │
│  │   │   │  4× 256-Bit FMA (AVX2)                           │  │     │  │
│  │   │   │  = 2× 256-Bit FP MUL + 2× 256-Bit FP ADD         │  │     │  │
│  │   │   │  oder 4× 128-Bit                                 │  │     │  │
│  │   │   └──────────────────────────────────────────────────┘  │     │  │
│  │   │   ┌──────────────────────────────────────────────────┐  │     │  │
│  │   │   │  2× FP Store (256-Bit)                           │  │     │  │
│  │   │   └──────────────────────────────────────────────────┘  │     │  │
│  │   └─────────────────────────────────────────────────────────┘     │  │
│  │                                                                   │  │
│  │   Reorder Buffer: 256 Entries                                     │  │
│  │   Retire Width: 8 µOps/Takt                                       │  │
│  └───────────────────────────────────────────────────────────────────┘  │
│                              │                                          │
│  ┌───────────────────────────────────────────────────────────────────┐  │
│  │                       LOAD/STORE                                  │  │
│  │                                                                   │  │
│  │   L1 Data Cache: 32 KB, 8-Way                                     │  │
│  │   Load Queue: 72 Entries                                          │  │
│  │   Store Queue: 64 Entries                                         │  │
│  │   3 Loads + 2 Stores pro Takt                                     │  │
│  │                                                                   │  │
│  │   L2 Cache: 512 KB, 8-Way (privat pro Kern)                       │  │
│  └───────────────────────────────────────────────────────────────────┘  │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### Chiplet-Design (Zen 2+)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    AMD CHIPLET-ARCHITEKTUR                              │
│                    (am Beispiel Ryzen 9 5950X)                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │                     AM4 PACKAGE                                 │    │
│  │                                                                 │    │
│  │   ┌─────────────────────┐         ┌─────────────────────┐       │    │
│  │   │    CCD 0 (7nm)      │         │    CCD 1 (7nm)      │       │    │
│  │   │                     │         │                     │       │    │
│  │   │  ┌───────────────┐  │         │  ┌───────────────┐  │       │    │
│  │   │  │   CCX (8C)    │  │         │  │   CCX (8C)    │  │       │    │
│  │   │  │   32 MB L3    │  │         │  │   32 MB L3    │  │       │    │
│  │   │  └───────────────┘  │         │  └───────────────┘  │       │    │
│  │   │                     │         │                     │       │    │
│  │   └──────────┬──────────┘         └──────────┬──────────┘       │    │
│  │              │                               │                  │    │
│  │              │      INFINITY FABRIC          │                  │    │
│  │              │◄─────────────────────────────►│                  │    │
│  │              │                               │                  │    │
│  │              └───────────────┬───────────────┘                  │    │
│  │                              │                                  │    │
│  │   ┌──────────────────────────┴──────────────────────────┐       │    │
│  │   │                   I/O DIE (12nm)                    │       │    │
│  │   │                                                     │       │    │
│  │   │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  │       │    │
│  │   │  │   Memory    │  │   PCIe 4.0  │  │    USB      │  │       │    │
│  │   │  │ Controller  │  │  24 Lanes   │  │   SATA      │  │       │    │
│  │   │  │  DDR4-3200  │  │             │  │   etc.      │  │       │    │
│  │   │  └─────────────┘  └─────────────┘  └─────────────┘  │       │    │
│  │   │                                                     │       │    │
│  │   └─────────────────────────────────────────────────────┘       │    │
│  │                                                                 │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                         │
│  VORTEILE:                                                              │
│  • CCDs auf modernstem Prozess (7nm/5nm/4nm)                            │
│  • I/O Die auf günstigerem Prozess (12nm/6nm)                           │
│  • Bessere Yields (kleinere Dies)                                       │
│  • Skalierbar von 8 bis 64 Kerne (EPYC: 8 CCDs)                         │
│  • Konsistente Architektur über Desktop/Server                          │
│                                                                         │
│  EPYC (Server): Bis zu 8 CCDs + 1 I/O Die = 64 Kerne                    │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---
author: Andreas Hümmer

## Entwicklungs-Timeline

### Chronologische Übersicht

| Jahr | CPU | Transistoren | Takt | Wichtigste Neuerungen |
|------|-----|-------------|------|----------------------|
| 1978 | Intel 8086 | 29K | 5-10 MHz | 16-Bit, x86-Start |
| 1979 | Intel 8088 | 29K | 5-8 MHz | IBM PC CPU |
| 1982 | Intel 80286 | 134K | 6-25 MHz | Protected Mode |
| 1985 | Intel 80386 | 275K | 16-40 MHz | 32-Bit, Paging |
| 1989 | Intel 80486 | 1,2M | 25-100 MHz | FPU, Cache, Pipeline |
| 1993 | Intel Pentium | 3,1M | 60-300 MHz | Superskalar |
| 1995 | Pentium Pro | 5,5M | 150-200 MHz | Out-of-Order |
| 1997 | Pentium II | 7,5M | 233-450 MHz | MMX, Slot 1 |
| 1999 | Pentium III | 9,5M | 450-1400 MHz | SSE |
| 1999 | AMD Athlon K7 | 22M | 500-1400 MHz | EV6 Bus |
| 2000 | Pentium 4 | 42M | 1,3-3,8 GHz | NetBurst, SSE2 |
| 2003 | AMD Opteron | 106M | 1,4-3,0 GHz | AMD64 |
| 2006 | Intel Core 2 | 291M | 1,86-3,33 GHz | Core-Architektur |
| 2008 | Intel Core i7 | 731M | 2,66-3,33 GHz | Nehalem, IMC |
| 2011 | Intel Sandy Bridge | 1,16B | 2,5-3,5 GHz | AVX |
| 2017 | AMD Zen 1 | 4,8B | 3,0-4,0 GHz | CCX, SMT |
| 2019 | AMD Zen 2 | 39,5B | 3,6-4,7 GHz | Chiplets, PCIe 4 |
| 2020 | AMD Zen 3 | 10,7B | 3,4-4,9 GHz | Unified L3 |
| 2022 | AMD Zen 4 | 6,5B | 4,5-5,7 GHz | AVX-512, DDR5 |
| 2024 | AMD Zen 5 | 8B+ | 4,5-5,7 GHz | Breitere Execution |

*(B = Milliarden, M = Millionen, K = Tausend)*

### Meilensteine der x86-Architektur

| Ära | CPU | Wichtigste Innovation |
|-----|-----|----------------------|
| **1978** | 8086/8088 | x86-Architektur, Segment:Offset |
| **1985** | 80386 | 32-Bit, Paging, Protected Mode |
| **1989** | 80486 | On-Die FPU & Cache, Pipeline |
| **1993** | Pentium | Superskalar (2 Pipelines) |
| **1995** | Pentium Pro | Out-of-Order, µOp Zerlegung |
| **2003** | AMD64 | 64-Bit Erweiterung |
| **2006** | Core 2 | Effiziente Architektur |
| **2017** | Zen | Chiplet-Design, CCX |

---
author: Andreas Hümmer

> [!info] **Nicht prüfungsrelevant**
> Die Details der CPU-Entwicklung sind interessantes Hintergrundwissen, aber für die Prüfung nicht relevant. Wichtig sind die grundlegenden Konzepte wie Protected Mode, Paging und die Unterscheidung RISC/CISC.

- → [[02-01-Kerneltypen|Kerneltypen]] - OS-Design für verschiedene CPUs
- → [[02-04-Von-Neumann-vs-Harvard|Von-Neumann vs. Harvard]] - Speicherarchitektur
- → [[02-05-RISC-vs-CISC|RISC vs. CISC]] - x86 ist CISC (aber intern RISC)
- → [[05-03-Paging|Paging]] - Eingeführt mit 80386
- → [[04-Synchronisation/04-01-Kritische-Abschnitte|Synchronisation]] - CPU-Features (LOCK, CMPXCHG)

---
author: Andreas Hümmer

## Weiterführende Links

### Offizielle Dokumentation

| Ressource | Link |
|-----------|------|
| **Intel SDM** (Software Developer Manual) | [intel.com/developer/articles/technical/intel-sdm](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html) |
| **Intel SDM Combined Volume** (PDF) | [intel.com/content-details/819723](https://www.intel.com/content/www/us/en/content-details/819723/intel-64-and-ia-32-architectures-software-developer-s-manual-combined-volumes-1-2a-2b-2c-2d-3a-3b-3c-3d-and-4.html) |
| **AMD Developer Documentation** | [amd.com/developer/documentation](https://www.amd.com/en/developer/browse-by-resource-type/documentation.html) |
| **AMD Zen Architecture Overview** | [amd.com/zen](https://www.amd.com/zen) |

### Historische Intel-Dokumentation

| CPU | Link |
|-----|------|
| **8086 Family User's Manual** (PDF) | [archive.org - 8086 Family Manual](https://ia800602.us.archive.org/16/items/programming-the-8086-8088/8086_family_Users_Manual_1__text.pdf) |
| **Intel 8086/8088 History** | [intel.com/virtual-vault - 8086 and IBM PC](https://www.intel.com/content/www/us/en/history/virtual-vault/articles/the-8086-and-the-ibm-pc.html) |
| **80386 Hardware Reference Manual** (PDF) | [ftpmirror - 80386 Manual](http://ftpmirror.your.org/pub/misc/bitsavers/components/intel/_dataBooks/1986_80386_Hardware_Reference_Manual.pdf) |
| **80386 Programmer's Reference** | [Stanford - i386 Manual](https://www.scs.stanford.edu/05au-cs240c/lab/i386/s02_02.htm) |
| **i386 Manual (GitHub)** | [github.com/NJU-ProjectN/i386-manual](https://github.com/NJU-ProjectN/i386-manual) |
| **Pentium Pro P6 Architecture** (PDF) | [chipdb.org - P6 Tour](https://datasheets.chipdb.org/Intel/x86/P6/p6tour.pdf) |
| **Intel Core 2 Duo Whitepaper** (PDF) | [intel.com - Core 2 Duo Whitepaper](http://www.intel.com/pressroom/kits/core2duo/pdf/ICM_whitepaper.pdf) |

### Technische Analysen

| Ressource | Link |
|-----------|------|
| **Agner Fog: Microarchitecture Manual** (PDF) | [utexas.edu - Agner Fog Microarchitecture](https://www.cs.utexas.edu/~hunt/class/2018-spring/cs340d/documents/Agner-Fog/microarchitecture.pdf) |
| **Agner Fog: Instruction Tables** (PDF) | [theswissbay.ch - Instruction Tables](https://theswissbay.ch/pdf/man_doc/Hardware/Instruction%20tables%20for%20Intel,%20AMD%20and%20VIA%20CPUs%20-%20Agner%20Fog.pdf) |
| **Microarchitecture Cheatsheet** (GitHub) | [github.com/akhin/microarchitecture-cheatsheet](https://github.com/akhin/microarchitecture-cheatsheet) |
| **x86-64 Guide (Stanford CS107)** | [stanford.edu - x86-64 Guide](https://web.stanford.edu/class/cs107/guide/x86-64.html) |

### AMD Zen Deep Dives

| Ressource | Link |
|-----------|------|
| **AMD Zen 5 Technical Deep Dive** | [techpowerup.com - Zen 5 Deep Dive](https://www.techpowerup.com/review/amd-zen-5-technical-deep-dive/3.html) |
| **AMD Zen 5 Architecture (Tom's Hardware)** | [tomshardware.com - Zen 5 Architecture](https://www.tomshardware.com/pc-components/cpus/amd-deep-dives-zen-5-ryzen-9000-and-strix-point-cpu-rdna-35-gpu-and-xdna-2-architectures) |
| **Zen Evolution Explained** | [kindatechnical.com - Zen Evolution](https://kindatechnical.com/computer-architecture/amd-zen-architecture-evolution-explained.html) |
| **AMD K7 Paper (ResearchGate)** | [researchgate.net - 7th Gen x86](https://www.researchgate.net/publication/3795936_A_7th-generation_x86_microprocessor) |

### Historische Artikel

| Ressource | Link |
|-----------|------|
| **AMD Athlon K7 Retrospective** | [custompc.com - K7 Retrospective](https://www.custompc.com/amd-athlon-k7-retrospective) |
| **AMD K7 History (Tom's Hardware)** | [tomshardware.com - AMD CPU History](https://www.tomshardware.com/uk/reviews/amd-cpu-history,2008-7.html) |
| **Ars Technica: Pentium Architecture** | [arstechnica.com - Pentium](https://archive.arstechnica.com/cpu/004/pentium-1/pentium-1-pdf.html) |

### Datenblätter & Datasheets

| Ressource                           | Link                                                                                                |
| ----------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Intel 8086/8088 Datasheets**      | [alldatasheet.com - 8086](https://www.alldatasheet.com/datasheet-pdf/pdf/1154708/INTEL/8086-2.html) |
| **Historic Intel Datasheets (FTP)** | [datasheets.chipdb.org/Intel/x86](http://datasheets.chipdb.org/Intel/x86/808x/datashts/)            |

---
author: Andreas Hümmer

## Quellen

- Intel® 64 and IA-32 Architectures Software Developer's Manual
- AMD64 Architecture Programmer's Manual
- Agner Fog: Microarchitecture of Intel, AMD and VIA CPUs
- AnandTech CPU Reviews (archiviert)
- WikiChip CPU Database
