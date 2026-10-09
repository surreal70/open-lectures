---
author: Andreas Hümmer
title: Von-Neumann- vs. Harvard-Architektur
tags:
  - content
- bs
- architektur
- hardware
- cpu
- speicher
created: '2026-10-07'
modified: '2026-10-07'
bereich: BS
---
author: Andreas Hümmer

# Von-Neumann- vs. Harvard-Architektur

> [!info] **Lernziele**
> Nach dem Durcharbeiten dieses Kapitels sollten Sie:
> 1. **Verstehen**, was die Von-Neumann-Architektur auszeichnet und welche Prinzipien ihr zugrunde liegen
> 2. **Erklären** können, was der Von-Neumann-Flaschenhals ist und welche Lösungen es gibt
> 3. **Unterscheiden** können zwischen Von-Neumann- und Harvard-Architektur
> 4. **Beschreiben** können, wie die Modified Harvard Architecture funktioniert
> 5. **Kennen** der typischen Anwendungsgebiete beider Architekturen

---
author: Andreas Hümmer

## Überblick

![[./.assets/von-neumann-vs-harvard-ueberblick.png]]

*Die beiden grundlegenden Rechnerarchitekturen im Vergleich: Die **Von-Neumann-Architektur** verbindet die CPU über einen einzigen gemeinsamen Bus mit einem einzigen Speicher, in dem Befehle und Daten zusammenliegen. Die **Harvard-Architektur** trennt beides – ein eigener Befehlsbus und -speicher für den Code, ein eigener Datenbus und -speicher für die Daten.*

---
author: Andreas Hümmer

## Von-Neumann-Architektur

### Historischer Hintergrund

Die Von-Neumann-Architektur wurde 1945 von **John von Neumann** im "First Draft of a Report on the EDVAC" beschrieben. Sie basiert auf Ideen von Turing, Eckert und Mauchly und definierte das Konzept des **speicherprogrammierten Computers**.

### Kernprinzipien

#### 1. Speicherprogrammierung

Programme werden wie Daten im Hauptspeicher abgelegt und können dort auch modifiziert werden.

#### 2. Einheitlicher Adressraum

Befehle und Daten teilen sich denselben Adressraum.

#### 3. Sequentielle Befehlsausführung

Befehle werden der Reihe nach aus dem Speicher geholt und ausgeführt (gesteuert durch Programmzähler).

#### 4. Binäre Kodierung

Alle Informationen (Daten + Befehle) werden binär codiert.

#### 5. Fünf Funktionseinheiten

| Einheit | Funktion |
|---------|----------|
| **Rechenwerk (ALU)** | Arithmetische und logische Operationen |
| **Steuerwerk (Control Unit)** | Befehlsausführung koordinieren |
| **Speicher (Memory)** | Programme und Daten speichern |
| **Eingabewerk (Input)** | Daten von außen aufnehmen |
| **Ausgabewerk (Output)** | Ergebnisse nach außen geben |

### Detaillierte Architektur

![[./.assets/von-neumann-detail.png]]

*Die Von-Neumann-Architektur im Detail: Die CPU besteht aus Steuerwerk (Befehlsregister, Programmzähler, Dekoder) und Rechenwerk (ALU, Register, Statusregister). Über den Systembus – unterteilt in Adress-, Daten- und Steuerbus – ist sie mit den Ein-/Ausgabewerken und dem gemeinsamen Speicher verbunden, in dem Befehle und Daten gemeinsam liegen.*

### Der Von-Neumann-Flaschenhals

#### Das Problem

> [!warning] **Kernproblem**
> CPU und Speicher teilen sich **einen** Bus – nur **ein** Zugriff gleichzeitig möglich!

| Komponente | Geschwindigkeit |
|------------|-----------------|
| **CPU** | Sehr schnell |
| **Bus** | Begrenzte Bandbreite |
| **Speicher** | Relativ langsam |

**Auswirkung:** Die CPU muss **warten**, bis Befehle/Daten über den Bus geladen sind!

#### Zeitlicher Ablauf (vereinfacht)

| Phase | CPU | Bus | Speicher |
|-------|-----|-----|----------|
| Fetch | FETCH | BELEGT | Zugriff |
| Decode | DECODE | frei | — |
| Execute | EXEC | frei | — |
| Fetch | FETCH | BELEGT | Zugriff |
| ... | ... | ... | ... |

**Visuelle Timeline:**

```
Zeit ──────────────────────────────────────────────────────────────►

CPU:      [FETCH]     [DECODE] [EXEC]      [FETCH]     [DECODE] [EXEC]
              │                                │
              ▼                                ▼
Bus:      ═══════                          ═══════
          │BELEGT│        frei             │BELEGT│        frei
              │                                │
              ▼                                ▼
Speicher: [Zugriff]    [warten...]         [Zugriff]    [warten...]

          ◄────── Befehl 1 ──────►         ◄────── Befehl 2 ──────►
```

> [!warning] **Problem**
> Die CPU muss bei jedem FETCH **warten**, bis der Bus frei ist und der Speicher geantwortet hat!

---
author: Andreas Hümmer

#### Moderne Lösungsansätze

Da der Von-Neumann-Flaschenhals ein fundamentales Designproblem ist, haben sich über Jahrzehnte mehrere komplementäre Strategien entwickelt. Keine einzelne Lösung beseitigt ihn vollständig – erst ihre Kombination ermöglicht die Performance moderner Prozessoren.

##### 1. Cache-Speicher (L1, L2, L3)

Der wirkungsvollste Ansatz ist ein mehrstufiger Cache direkt auf dem Prozessorchip. Häufig benötigte Befehle und Daten werden in schnellem SRAM gehalten, der mit CPU-Taktgeschwindigkeit läuft – ohne Wartezyklen. Der L1-Cache ist am schnellsten und kleinsten, L2 und L3 sind größer aber etwas langsamer. Nur bei einem Cache-Miss muss auf den deutlich langsameren Hauptspeicher zugegriffen werden.

| Ebene | Latenz | Typische Größe |
|-------|--------|----------------|
| **L1** | ~1 ns | 32–64 KB |
| **L2** | ~4 ns | 256–512 KB |
| **L3** | ~12 ns | 4–32 MB |
| **RAM** | ~100 ns | 8–128 GB |

```
CPU ◄──► [L1] ◄──► [L2] ◄──► [L3] ◄──► RAM
```

##### 2. Pipelining

Statt einen Befehl vollständig abzuarbeiten, bevor der nächste beginnt, werden mehrere Befehle gleichzeitig in verschiedenen Ausführungsstufen gehalten – ähnlich einem Fließband. Während Befehl 1 in der Ausführungsphase (EXEC) ist, wird Befehl 2 bereits dekodiert und Befehl 3 aus dem Speicher geholt. So kann der Bus für FETCH genutzt werden, während die ALU gleichzeitig rechnet.

| Takt | 1 | 2 | 3 | 4 | 5 |
|------|---|---|---|---|---|
| Befehl 1 | FETCH | DECODE | EXEC | WRITE | — |
| Befehl 2 | — | FETCH | DECODE | EXEC | WRITE |
| Befehl 3 | — | — | FETCH | DECODE | EXEC |

##### 3. Mehrere Busse (Split-Bus)

Durch die Einführung separater Busse für Befehle und Daten – wie es die Harvard-Architektur vorsieht – können Befehls-Fetch und Datenzugriff parallel stattfinden. Moderne Prozessoren setzen dies auf Cache-Ebene konsequent um (Modified Harvard): L1-I-Cache und L1-D-Cache haben jeweils eigene Verbindungen zur CPU.

##### 4. Prefetching

Der Prozessor lädt Befehle und Daten vorausschauend in den Cache, noch bevor sie tatsächlich benötigt werden. Branch-Prediction hilft dabei vorherzusagen, welcher Codepfad als nächstes ausgeführt wird. Moderne CPUs können so den Flaschenhals oft vollständig verbergen, solange die Vorhersagen korrekt sind.

### Befehlszyklus (Instruction Cycle)

![[./.assets/von-neumann-befehlszyklus.png]]

*Der Befehlszyklus durchläuft fünf Stufen: **Fetch** (Befehl anhand des Programmzählers aus dem Speicher holen), **Decode** (Opcode und Operanden ermitteln), optional **Fetch Operands** (Operanden laden), **Execute** (ALU-Operation ausführen) und **Write Back** (Ergebnis zurückschreiben). Solange kein HALT erreicht ist, beginnt der Zyklus mit dem nächsten Befehl von vorn.*

---
author: Andreas Hümmer

## Harvard-Architektur

### Historischer Hintergrund

Die Harvard-Architektur wurde nach dem **Harvard Mark I** Computer (1944) benannt, der von Howard Aiken an der Harvard University entwickelt wurde. Sie verwendet physisch getrennte Speicher und Busse für Befehle und Daten.

### Detaillierte Architektur

![[./.assets/harvard-detail.png]]

*Die Harvard-Architektur im Detail: Dieselbe CPU-Struktur wie bei Von-Neumann, aber mit zwei getrennten Pfaden – ein Befehlsbus zum (meist nur lesbaren) Befehlsspeicher (ROM) und ein eigener Datenbus zum les- und schreibbaren Datenspeicher (RAM).*

> [!tip] **Vorteile der Harvard-Architektur**
> - Gleichzeitiger Zugriff auf Befehle **und** Daten möglich
> - Höherer Durchsatz, da keine Bus-Konflikte auftreten
> - Unterschiedliche Wortbreiten für Code und Daten möglich
> - Code kann nicht versehentlich durch Datenzugriffe überschrieben werden

### Paralleler Zugriff

#### Von-Neumann (sequentiell)

Bei der Von-Neumann-Architektur teilen sich Befehls- und Datenzugriffe denselben Bus. Das bedeutet: Während die CPU einen Befehl holt (FETCH), ist der Bus belegt – ein gleichzeitiger Datenzugriff (LOAD/STORE) ist nicht möglich. Die Zugriffe müssen strikt nacheinander erfolgen, was zu Wartezyklen und einem geringeren Durchsatz führt.

| Takt | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|------|---|---|---|---|---|---|---|---|
| **Bus** | FETCH | — | LOAD | — | FETCH | — | STORE | — |
| **CPU** | — | EXEC | — | EXEC | — | EXEC | — | EXEC |

→ **4 Takte pro Befehl** (Bus-Konflikt zwischen Befehls- und Datenzugriff)

```
Zeit ──────────────────────────────────────────────────────────────►

Bus:      [FETCH]  [frei]  [LOAD]  [frei]  [FETCH]  [frei]  [STORE]
CPU:      [wait ]  [EXEC]  [wait]  [EXEC]  [wait ]  [EXEC]  [wait ]

          ◄─────── Befehl 1 ───────►◄─────── Befehl 2 ────────►
```

---
author: Andreas Hümmer

#### Harvard (parallel)

Die Harvard-Architektur beseitigt diesen Konflikt durch physisch getrennte Busse. Der Instruktionsbus (I-Bus) holt permanent den nächsten Befehl, während der Datenbus (D-Bus) gleichzeitig Operanden lädt oder Ergebnisse zurückschreibt. Beide Busse arbeiten vollständig unabhängig voneinander – es gibt keine Wartezyklen durch Bus-Konflikte.

| Takt | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|------|---|---|---|---|---|---|---|---|
| **I-Bus** | FETCH | FETCH | FETCH | FETCH | FETCH | FETCH | FETCH | FETCH |
| **D-Bus** | — | LOAD | STORE | LOAD | STORE | LOAD | STORE | LOAD |
| **CPU** | — | EXEC | EXEC | EXEC | EXEC | EXEC | EXEC | EXEC |

→ **2 Takte pro Befehl** (keine Bus-Konflikte!)

```
Zeit ──────────────────────────────────────────────────────────────►

I-Bus:    [FETCH] [FETCH] [FETCH] [FETCH] [FETCH] [FETCH] [FETCH]
D-Bus:    [     ] [LOAD ] [STORE] [LOAD ] [STORE] [LOAD ] [STORE]
CPU:      [     ] [EXEC ] [EXEC ] [EXEC ] [EXEC ] [EXEC ] [EXEC ]

          ◄─ B1 ─►◄─ B2 ─►◄─ B3 ─►◄─ B4 ─►◄─ B5 ─►◄─ B6 ─►
```

> [!tip] **Ergebnis**
> Harvard-Architektur ermöglicht **doppelten Durchsatz** durch parallelen Zugriff auf Befehle und Daten!

---
author: Andreas Hümmer

## Modified Harvard Architecture

### Das Beste aus beiden Welten

![[./.assets/modified-harvard.png]]

*Modified Harvard: **intern** arbeitet die CPU nach dem Harvard-Prinzip (getrennte L1-Caches für Befehle und Daten), während der **externe** Zugriff auf den gemeinsamen Hauptspeicher dem Von-Neumann-Modell folgt. Ab dem vereinheitlichten L2-Cache fließen Code und Daten über einen gemeinsamen Pfad.*

### Warum Modified Harvard?

Die Modified Harvard Architecture entstand als pragmatische Antwort auf die Grenzen beider Reinformen. Sie kombiniert die innere Effizienz der Harvard-Architektur mit der äußeren Einfachheit des Von-Neumann-Modells und ist heute in praktisch allen modernen Hochleistungsprozessoren zu finden.

#### 1. Performance

Die getrennte L1-Cache-Ebene (I-Cache für Befehle, D-Cache für Daten) beseitigt den Von-Neumann-Flaschenhals dort, wo er am stärksten wirkt: in der innersten Schleife des Prozessors. Während die CPU einen Befehl ausführt, kann der I-Cache bereits den nächsten Befehl holen – gleichzeitig kann der D-Cache Operanden laden oder Ergebnisse schreiben.

| Aspekt | Vorteil |
|--------|---------|
| **L1-Cache getrennt** | Paralleler Zugriff auf Befehle + Daten |
| **Kein Flaschenhals** | Auf Cache-Ebene kein Von-Neumann-Problem |
| **Pipeline** | Kann optimal gefüllt werden |

#### 2. Flexibilität

Ab der L2-Cache-Ebene wird der Speicher wieder vereint. Das ermöglicht selbstmodifizierenden Code – eine Voraussetzung für JIT-Compiler (Java, .NET, JavaScript), die zur Laufzeit nativen Maschinencode erzeugen und sofort ausführen. In einer strikten Harvard-Architektur wäre dies nicht möglich, da Daten nie als Befehle ausgeführt werden können.

| Aspekt | Vorteil |
|--------|---------|
| **Einheitlicher RAM** | Einfaches Speichermodell |
| **Selbstmod. Code** | JIT-Compiler, dynamisches Patching möglich |
| **Dynamisches Laden** | Code zur Laufzeit nachladen |

#### 3. Kompatibilität

Für Software ist der Unterschied zur reinen Von-Neumann-Architektur vollständig transparent. Programme sehen einen gemeinsamen, linearen Adressraum – Betriebssysteme können Code und Daten frei darin platzieren, ohne sich um getrennte Speicherbereiche kümmern zu müssen. Das gesamte bestehende Software-Ökosystem läuft ohne Änderungen.

| Aspekt | Vorteil |
|--------|---------|
| **Software-Sicht** | Sieht Von-Neumann-Modell (gemeinsamer Adressraum) |
| **Bestehende Programme** | Funktionieren ohne Änderung |
| **Betriebssystem** | Kann Code/Daten frei platzieren |

#### 4. Kosteneffizienz

Im Vergleich zur strikten Harvard-Architektur benötigt Modified Harvard nur einen Speichercontroller und einen einheitlichen Hauptspeicher. Der verfügbare RAM kann dynamisch zwischen Code und Daten aufgeteilt werden – je nach Bedarf der laufenden Anwendung. Keine feste Partitionierung bedeutet keine Verschwendung.

| Aspekt | Vorteil |
|--------|---------|
| **Speichercontroller** | Nur einer nötig |
| **Speicheraufteilung** | Dynamisch zwischen Code/Daten |
| **Keine Verschwendung** | Keine feste Partitionierung |

> [!tip] **Zusammenfassung**
> Modified Harvard kombiniert die **Performance von Harvard** (getrennte Caches) mit der **Flexibilität von Von-Neumann** (gemeinsamer Hauptspeicher). Alle modernen CPUs – von Intel Core bis Apple M-Serie – basieren auf diesem Prinzip.

---
author: Andreas Hümmer

## Direkter Vergleich

| Merkmal | Von-Neumann | Harvard |
|---------|-------------|---------|
| **Speicher** | Gemeinsam (Code + Daten) | Getrennt (Code ≠ Daten) |
| **Bus-System** | Ein Bus | Zwei Busse |
| **Parallelität** | Sequentiell (Flaschenhals) | Parallel möglich |
| **Durchsatz** | Niedriger | Höher (bis 2×) |
| **Flexibilität** | Hoch (selbstmod. Code) | Eingeschränkt |
| **Komplexität** | Einfacher | Komplexer |
| **Kosten** | Günstiger (weniger Hardware) | Teurer (mehr Busse) |
| **Sicherheit** | Geringer (Code überschreibbar) | Höher (Code geschützt) |
| **Wortbreite** | Einheitlich | Kann unterschiedlich sein |

---
author: Andreas Hümmer

## Anwendungsgebiete

### Von-Neumann-Architektur

| Einsatzgebiet | Beispiele |
|---------------|-----------|
| Desktop-PCs & Laptops | x86, x86-64 |
| Server | Intel Xeon, AMD EPYC |
| Smartphones | ARM-basiert (aber Modified Harvard) |
| Mainframes | IBM z/Series |
| JIT-Systeme | Java, .NET, JavaScript |

**Prozessor-Beispiele:**
- Intel Core i-Serie
- AMD Ryzen
- Apple M-Serie (Modified Harvard)

---
author: Andreas Hümmer

### Harvard-Architektur (strikt)

| Einsatzgebiet | Beispiele |
|---------------|-----------|
| Mikrocontroller | AVR, PIC, 8051 |
| Digitale Signalprozessoren | TI C6000 DSPs |
| Embedded Systems | Festes Programm in ROM |
| Steuergeräte | Automotive, Industrie |
| IoT-Devices | Sensoren, Aktoren |
| Echtzeitsysteme | Deterministische Anforderungen |

**Prozessor-Beispiele:**
- Arduino (ATmega328P – AVR)
- PIC-Mikrocontroller
- Texas Instruments C6000 DSP
- ARM Cortex-M (Modified Harvard)

---
author: Andreas Hümmer

### Modified Harvard (Hybrid)

| Einsatzgebiet | Beispiele |
|---------------|-----------|
| High-Performance CPUs | Desktop, Server |
| Mobile Prozessoren | ARM Cortex-A |
| Moderne x86-64 | Intel Core, AMD Ryzen |
| RISC-V mit Cache | SiFive |
| Apple Silicon | M1, M2, M3, M4 |

---
author: Andreas Hümmer

## Implikationen für Betriebssysteme

Die Wahl der Speicherarchitektur hat weitreichende Auswirkungen auf das Design und die Implementierung von Betriebssystemen. Von-Neumann und Modified Harvard stellen dabei andere Anforderungen als die strikte Harvard-Architektur, die vor allem in eingebetteten Systemen und Echtzeitsystemen anzutreffen ist.

### Von-Neumann / Modified Harvard

#### 1. Virtueller Speicher

Da Code und Daten denselben Adressraum teilen, kann das Betriebssystem virtuellen Speicher einheitlich verwalten. Seiten werden unabhängig von ihrem Inhalt (Code oder Daten) durch dieselbe Paging-Mechanik verwaltet. Das Execute-Disable-Bit (NX bei AMD, XD bei Intel) erlaubt es dem Betriebssystem, einzelne Seiten explizit als nicht ausführbar zu markieren – eine wichtige Sicherheitsfunktion.

| Aspekt | Beschreibung |
|--------|--------------|
| **Adressraum** | Einheitlich für Code und Daten |
| **Paging** | Code- und Daten-Seiten gleich behandelt |
| **Sicherheit** | Execute-Disable (NX/XD) Bit verfügbar |

#### 2. Prozessladen

Der Loader des Betriebssystems platziert beim Programmstart sowohl Code- als auch Datensegmente in denselben Adressraum des Prozesses. Dynamisches Linken – also das Einbinden von Shared Libraries erst zur Laufzeit – ist nur möglich, weil Code und Daten im selben Speicher liegen. Eine Shared Library wie `libc.so` wird einmal in den physischen Speicher geladen und dann in die Adressräume aller nutzenden Prozesse eingeblendet.

| Aspekt | Beschreibung |
|--------|--------------|
| **Laden** | Code und Daten in gemeinsamen Speicher |
| **Linking** | Dynamisches Linken zur Laufzeit möglich |
| **Shared Libraries** | Einmal laden, mehrfach nutzen |

#### 3. Cache-Kohärenz

Selbstmodifizierender Code – wie er von JIT-Compilern erzeugt wird – stellt das Betriebssystem vor ein Kohärenzproblem: Der erzeugte Maschinencode landet zunächst als Daten im D-Cache. Damit die CPU ihn als Befehle ausführen kann, muss sichergestellt sein, dass der I-Cache diese Änderungen sieht. Auf ARM-Systemen ist dafür ein expliziter Cache-Flush nötig; auf x86 ist die Kohärenz zwischen I-Cache und D-Cache hardwareseitig garantiert.

| Schritt | Aktion |
|---------|--------|
| 1 | JIT generiert Code → D-Cache |
| 2 | D-Cache → RAM (Write-Back) |
| 3 | **I-Cache invalidieren!** |
| 4 | Neuer Code → I-Cache |
| 5 | Ausführung |

> [!warning] **Wichtig**
> JIT-Compiler müssen explizit Cache-Synchronisation durchführen – auf ARM über `__clear_cache()`, auf x86 ist dies hardwareseitig garantiert.

#### 4. Speicherschutz

Das W⊕X-Prinzip (Write XOR Execute) ist eine direkte Konsequenz der Von-Neumann-Architektur: Da Code und Daten denselben Speicher teilen, muss das Betriebssystem durch Seitenattribute sicherstellen, dass eine Seite nie gleichzeitig beschreibbar und ausführbar ist. Dies verhindert klassische Code-Injection-Angriffe, bei denen Angreifer schadhaften Code in Datenbereiche (z.B. den Stack) schreiben und dann zur Ausführung bringen.

| Mechanismus | Beschreibung |
|-------------|--------------|
| **W⊕X** | Write XOR Execute: Seite ist ENTWEDER schreibbar ODER ausführbar |
| **DEP** | Data Execution Prevention (Windows) |
| **NX-Bit** | Stack nicht ausführbar |
| **Zweck** | Verhindert Code-Injection-Angriffe |

---
author: Andreas Hümmer

### Strikte Harvard (Embedded/RTOS)

Auf Mikrocontrollern und in Echtzeitsystemen mit strikter Harvard-Architektur vereinfacht sich das Betriebssystemdesign erheblich – auf Kosten der Flexibilität.

#### 1. Speicherlayout

Das Programm wird zur Compile-Zeit fest in Flash oder ROM gebrannt; Variablen und Stack liegen im RAM. Es gibt keine Möglichkeit, zur Laufzeit neuen Code zu laden oder bestehenden Code zu verändern. Dieses Modell ist einfach, deterministisch und robust.

| Bereich | Speichertyp | Eigenschaften |
|---------|-------------|---------------|
| **Code** | Flash/ROM | Nicht änderbar |
| **Daten** | RAM | Lesen + Schreiben |
| **Zuordnung** | — | Fest zur Compile-Zeit |

#### 2. Einfacheres Speichermanagement

Ohne gemeinsamen Adressraum entfallen viele Komplexitäten moderner Betriebssysteme: kein Paging, kein Swapping, kein dynamischer Linker. Speicherzugriffe haben dadurch vollständig deterministische Laufzeiten – eine zentrale Anforderung für harte Echtzeitsysteme wie Motorsteuerungen oder medizinische Geräte.

| Aspekt | Vorteil |
|--------|---------|
| **Virtueller Speicher** | Nicht nötig |
| **Paging/Swapping** | Nicht nötig |
| **Zugriffszeiten** | Deterministisch (wichtig für Echtzeit!) |

#### 3. Sicherheit

Da der Codespeicher physisch vom Datenspeicher getrennt ist, kann ein Angreifer durch Buffer Overflows oder andere Speicherfehler keinen Code in den Befehlsspeicher injizieren. Der Programmcode ist strukturell gegen eine ganze Klasse von Angriffen immun – ohne dass das Betriebssystem aktiv schützen muss.

| Aspekt | Beschreibung |
|--------|--------------|
| **Code-Integrität** | Code kann nicht überschrieben werden |
| **Buffer Overflows** | Können keinen Code injizieren |

---
author: Andreas Hümmer

## Zusammenfassung

| Aspekt           | Von-Neumann     | Harvard      | Modified Harvard              |
| ---------------- | --------------- | ------------ | ----------------------------- |
| **Speicher**     | Gemeinsam       | Getrennt     | Cache getrennt, RAM gemeinsam |
| **Performance**  | Flaschenhals    | Höher        | Optimiert                     |
| **Flexibilität** | Hoch            | Gering       | Hoch                          |
| **Komplexität**  | Einfach         | Mittel       | Komplex                       |
| **Einsatz**      | General Purpose | Embedded/DSP | Moderne CPUs                  |

---
author: Andreas Hümmer

## Zusammenhänge

- → [[02-01-Kerneltypen|Kerneltypen]] - Kernel-Design basiert auf Architektur
- → [[02-02-Schichtenmodell|Schichtenmodell]] - Hardware-Abstraktion
- → [[02-03-Systemaufrufe|Systemaufrufe]] - Speicherzugriff über Syscalls
- → [[05-01-Adressraeume|Adressräume]] - Virtueller Speicher auf Von-Neumann
- → [[05-02-Virtueller-Speicher|Virtueller Speicher]] - Paging und Speicherverwaltung
- → [[05-03-Paging|Paging]] - Seitenbasierte Speicherverwaltung

### Betriebssystem-Referenzen

- → [[07-Anhang/Betriebssysteme/Linux|Linux]] - Modified Harvard (x86-64)
- → [[07-Anhang/Betriebssysteme/Windows-NT|Windows NT]] - Modified Harvard
- → [[07-Anhang/Betriebssysteme/FreeRTOS|FreeRTOS]] - Oft auf Harvard-Mikrocontrollern
- → [[07-Anhang/Betriebssysteme/VxWorks|VxWorks]] - Unterstützt beide Architekturen
- → [[07-Anhang/Betriebssysteme/QNX|QNX]] - Echtzeitsystem auf verschiedenen Architekturen

---
author: Andreas Hümmer

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - Unterschiede zwischen Von-Neumann und Harvard-Architektur
> - Von-Neumann-Flaschenhals verstehen
> - Von-Neumann-Befehlszyklus (Fetch-Decode-Execute)
> - Moderne Hybridlösungen (Modified Harvard)
> - Anwendungsgebiete beider Architekturen

> [!question] **Häufige Prüfungsfragen**
> 1. Erklären Sie den Unterschied zwischen Von-Neumann und Harvard-Architektur
> 2. Was ist der Von-Neumann-Flaschenhals und wie wird er gelöst?
> 3. Warum verwenden moderne CPUs die Modified Harvard Architecture?
> 4. Nennen Sie typische Anwendungsgebiete beider Architekturen
> 5. Welche Auswirkungen hat die Architektur auf das Betriebssystem-Design?

> [!tip] **Merkhilfen**
> - **Von-Neumann** = "Alles in einem Topf" (Code + Daten gemischt)
> - **Harvard** = "Getrennte Küchen" (Code ≠ Daten)
> - **Modified Harvard** = "Restaurant mit getrennter Küche, aber gemeinsamer Vorratskammer"
> - **Flaschenhals** = Ein Bus für alles → Stau!

---
author: Andreas Hümmer

## Quellen

- von Neumann, J.: First Draft of a Report on the EDVAC (1945)
- Tanenbaum, A. S.: Structured Computer Organization, 6th Edition
- Patterson, D. & Hennessy, J.: Computer Organization and Design
- Intel® 64 and IA-32 Architectures Optimization Reference Manual
- ARM Architecture Reference Manual
