---
author: Andreas Hümmer
title: RISC vs. CISC Architekturen
tags:
  - content
- bs
- architektur
- hardware
- cpu
- risc
- cisc
created: '2026-10-07'
modified: '2026-10-07'
bereich: BS
---
author: Andreas Hümmer

# RISC vs. CISC Architekturen

> [!info] **Lernziele**
> Nach dem Durcharbeiten dieses Kapitels sollten Sie:
> 1. **Verstehen**, was RISC und CISC bedeutet und worin die Philosophie-Unterschiede liegen
> 2. **Erklären** können, warum RISC-Prozessoren mehr Register haben als CISC
> 3. **Unterscheiden** können zwischen Load/Store-Architektur (RISC) und Speicher-zu-Speicher-Operationen (CISC)
> 4. **Beschreiben** können, wie moderne x86-CPUs intern RISC-artig arbeiten (µOp-Zerlegung)
> 5. **Kennen** der wichtigsten Vertreter beider Architekturen (x86, ARM, RISC-V, MIPS)
> 6. **Bewerten** können, warum RISC und CISC heute konvergieren

---
author: Andreas Hümmer

## Überblick

### Die zwei Philosophien

| Aspekt | CISC | RISC |
|--------|------|------|
| **Name** | Complex Instruction Set Computing | Reduced Instruction Set Computing |
| **Philosophie** | "Mache komplexe Dinge mit EINEM Befehl" | "Mache einfache Dinge SEHR SCHNELL" |
| **Befehle** | Wenige, aber mächtige | Viele einfache, schnelle |
| **Takte pro Befehl** | Mehrere (variabel) | Meist 1 (konstant) |

### Beispiel: Multiplikation mit Speicherzugriff

**CISC (1 komplexer Befehl):**
```asm
MULT A, [B+C*4]    ; Adresse berechnen, laden, multiplizieren, speichern
```

**RISC (8 einfache Befehle, je 1 Takt):**
```asm
LOAD  R1, [B]      ; B laden
LOAD  R2, [C]      ; C laden
SHL   R2, 2        ; C * 4
ADD   R1, R2       ; Adresse berechnen
LOAD  R3, [R1]     ; Wert von Adresse laden
LOAD  R4, [A]      ; A laden
MUL   R4, R3       ; Multiplizieren
STORE [A], R4      ; Ergebnis speichern
```

### Bekannte Architekturen

| CISC | RISC |
|------|------|
| Intel x86 | ARM |
| AMD x86-64 | MIPS |
| Motorola 68000 | RISC-V |
| VAX | SPARC |
| IBM System/360 | PowerPC |

---
author: Andreas Hümmer

## Historischer Hintergrund

### 1960er–1970er: Aufstieg von CISC

| Faktor | Auswirkung |
|--------|------------|
| **Speicher war teuer** | Weniger Befehle = weniger Speicherverbrauch |
| **Compiler waren primitiv** | Hardware musste Komplexität übernehmen |
| **Assembler-Programmierung üblich** | Komplexe Befehle = einfacherer Code für Entwickler |

**Beispiel: VAX (1977)**

| Eigenschaft | Details |
|-------------|---------|
| **Spezial-Befehle** | POLY (Polynomauswertung in Hardware!), String-Operationen, BCD-Arithmetik, Queue-Operationen |
| **Befehlsanzahl** | Über 300 verschiedene Befehle |

---
author: Andreas Hümmer

### 1980er: Die RISC-Revolution

**Forschung an Berkeley (Patterson) und Stanford (Hennessy)**

> [!warning] **Zentrale Erkenntnis**
> *"80% der Ausführungszeit entfällt auf 20% der Befehle"*
> 
> - Die meisten komplexen CISC-Befehle werden **selten** genutzt
> - Compiler erzeugen hauptsächlich einfache Befehle
> - Komplexe Befehle sind schwer zu optimieren

**Erste RISC-Prozessoren**

| Prozessor | Jahr | Besonderheiten |
|-----------|------|----------------|
| **Berkeley RISC I** | 1982 | 32 Befehle, 1 Takt pro Befehl |
| **Stanford MIPS** | 1983 | Minimalist Instruction Set Processor |

---
author: Andreas Hümmer

### 1990er–heute: Konvergenz

| Entwicklung | Beschreibung |
|-------------|--------------|
| **CISC wird intern RISC** | x86-Prozessoren übersetzen zu RISC-ähnlichen µOps |
| **RISC wird komplexer** | SIMD-Erweiterungen, Krypto-Befehle |
| **Marktaufteilung** | ARM dominiert Mobile, x86 dominiert Desktop/Server |
| **Apple-Wechsel (2020)** | Von Intel (CISC) zu ARM (RISC) |

**Timeline der x86-Entwicklung**

| Jahr | Prozessor | Architektur-Meilenstein |
|------|-----------|------------------------|
| 1971 | 4004 | 4-Bit, erster Mikroprozessor |
| 1978 | 8086 | 16-Bit CISC |
| 1985 | 80386 | 32-Bit CISC |
| 1989 | i486 | Integrierte FPU |
| 1993 | Pentium | Superskalare CISC |
| 2006 | Core | x86 mit RISC-Kern intern |
| 2020 | Apple M1 | RISC (ARM) für Desktop |
| heute | — | ARM überall (Server, Desktop, Mobile)

---
author: Andreas Hümmer

## CISC im Detail

### Charakteristiken

#### 1. Viele und komplexe Befehle

| Eigenschaft | Details |
|-------------|---------|
| **Befehlsanzahl** | Hunderte verschiedener Befehle |
| **Spezialisierung** | Spezial-Befehle für viele Situationen |
| **Befehlslänge** | Variabel (x86: 1–15 Bytes!) |

**x86-Beispiele komplexer Befehle:**

| Befehl | Funktion |
|--------|----------|
| `MOVSB` | Byte kopieren, Pointer automatisch anpassen |
| `REP MOVSB` | Ganze Blöcke kopieren (Loop in Hardware) |
| `ENTER` | Stack-Frame aufbauen (komplexe Operation) |
| `CPUID` | CPU-Informationen abfragen |
| `AESENC` | AES-Verschlüsselungsrunde |

---
author: Andreas Hümmer

#### 2. Speicher-zu-Speicher Operationen

- Befehle können **direkt auf Speicher** arbeiten
- Weniger explizite LOAD/STORE nötig

```asm
ADD [mem1], [mem2]   ; Direkte Speicheraddition
```

---
author: Andreas Hümmer

#### 3. Komplexe Adressierungsarten

**x86 Adressierungsmodi:**

| Syntax | Modus | Anwendung |
|--------|-------|-----------|
| `[EAX]` | Register indirekt | Pointer-Zugriff |
| `[EAX + 4]` | Basis + Displacement | Struct-Felder |
| `[EAX + EBX]` | Basis + Index | Array mit Index |
| `[EAX + EBX*4]` | Basis + skalierter Index | Array mit int-Index |
| `[EAX + EBX*4 + 8]` | Alles kombiniert | `array[i].field` |

> [!tip] **Praxisnutzen**
> Die komplexe Adressierung `[EAX + EBX*4 + 8]` entspricht direkt dem C-Ausdruck `array[i].field` – ein Befehl statt mehrerer!

---
author: Andreas Hümmer

#### 4. Mikrocode

| Aspekt | Beschreibung |
|--------|--------------|
| **Funktion** | Komplexe Befehle werden in Mikrooperationen (µOps) zerlegt |
| **Speicherung** | Mikrocode im ROM der CPU gespeichert |
| **Updatefähig** | Kann durch Firmware-Updates gepatcht werden |

**Beispiel: ENTER-Befehl**

```asm
ENTER 16, 0          ; Komplexer Befehl
```

Wird intern zerlegt in:

| µOp | Operation |
|-----|-----------|
| µOp1 | `PUSH EBP` |
| µOp2 | `MOV EBP, ESP` |
| µOp3 | `SUB ESP, 16` |

→ Ausführungseinheiten verarbeiten dann die einfachen µOps

### x86 Befehlsformat

**Aufbau (variable Länge: 1–15 Bytes)**

| Feld | Größe | Beschreibung |
|------|-------|--------------|
| **Prefixes** | 0–4 Bytes | LOCK, REP, Segment-Override, Operand/Address-Size |
| **Opcode** | 1–3 Bytes | Eigentlicher Befehlscode |
| **ModR/M** | 0–1 Byte | Adressierungsmodus und Register |
| **SIB** | 0–1 Byte | Scale-Index-Base für komplexe Adressierung |
| **Displacement** | 0, 1, 2 oder 4 Bytes | Offset-Wert |
| **Immediate** | 0, 1, 2 oder 4 Bytes | Konstanter Operand |

**Prefix-Typen:**

| Prefix | Funktion |
|--------|----------|
| `LOCK` | Atomarer Speicherzugriff |
| `REP` | Wiederholung für String-Befehle |
| `66h` | Operand-Size Override |
| `67h` | Address-Size Override |
| `REX` | 64-Bit Erweiterung (Zugriff auf R8–R15) |
| `VEX/EVEX` | AVX/AVX-512 Vektorerweiterungen |

**Beispiele verschiedener Befehlslängen:**

| Befehl | Hex-Code | Länge |
|--------|----------|-------|
| `NOP` | `90` | 1 Byte |
| `MOV EAX, EBX` | `89 D8` | 2 Bytes |
| `MOV EAX, [EBX+ECX*4+8]` | `8B 44 8B 08` | 4 Bytes |
| `MOV EAX, 0x12345678` | `B8 78 56 34 12` | 5 Bytes |
| `LOCK ADD [mem], imm32` | `F0 81 05 ...` | 10+ Bytes |
| `VFMADD231PS zmm0,zmm1,[mem]` | `62 ...` | bis 15 Bytes |

> [!warning] **Problem: Dekodierung ist komplex!**
> - **Variable Länge** → schwer vorherzusagen, wo der nächste Befehl beginnt
> - **Viele Prefixes möglich** → aufwendige Dekoder-Logik
> - **Moderne x86-CPUs** benötigen 4–5 parallele Dekoder

---
author: Andreas Hümmer

## RISC im Detail

### Charakteristiken

#### 1. Wenige, einfache Befehle

| Eigenschaft | Details |
|-------------|---------|
| **Befehlsanzahl** | Typisch 50–150 Befehle |
| **Philosophie** | Jeder Befehl macht genau **eine** Sache |
| **Befehlslänge** | Fest (meist 32 Bit) |

**ARM-Beispiele (A64):**

| Befehl | Funktion |
|--------|----------|
| `ADD X0, X1, X2` | X0 = X1 + X2 (nur Register!) |
| `LDR X0, [X1]` | Load von Adresse in X1 |
| `STR X0, [X1]` | Store nach Adresse in X1 |
| `B label` | Unbedingter Sprung |

---
author: Andreas Hümmer

#### 2. Load/Store-Architektur

> [!warning] **Kernprinzip**
> - **NUR** Load/Store-Befehle greifen auf Speicher zu
> - **Alle anderen** Befehle arbeiten **ausschließlich** mit Registern

**Beispiel: Speicheraddition (RISC-Stil)**

```asm
LDR  X1, [X10]      ; Lade Wert A
LDR  X2, [X11]      ; Lade Wert B
ADD  X3, X1, X2     ; Addiere (nur Register!)
STR  X3, [X12]      ; Speichere Ergebnis
```

---
author: Andreas Hümmer

#### 3. Viele Register

| Eigenschaft | Details |
|-------------|---------|
| **Typisch** | 32 oder mehr Universalregister |
| **Vorteil** | Reduziert Speicherzugriffe |
| **Compiler** | Ermöglicht bessere Optimierungen |

**Vergleich der Registeranzahl:**

| Architektur | Universalregister | Bezeichnung |
|-------------|-------------------|-------------|
| x86 (32-bit) | 8 | EAX–EDI |
| x86-64 | 16 | RAX–R15 |
| ARM (32-bit) | 16 | R0–R15 |
| ARM64 (AArch64) | 31 | X0–X30 |
| MIPS | 32 | $0–$31 |
| RISC-V | 32 | x0–x31 |
| SPARC | 32 (128) | Register-Windows |

---
author: Andreas Hümmer

#### 4. Einfache Adressierung

| Modus | Syntax |
|-------|--------|
| Basis | `LDR X0, [X1]` |
| Basis + Offset | `LDR X0, [X1, #8]` |
| Basis + Index | `LDR X0, [X1, X2]` (manchmal) |

→ Wenige Adressierungsmodi = einfachere Hardware

---
author: Andreas Hümmer

#### 5. Feste Befehlslänge

| Eigenschaft | Details |
|-------------|---------|
| **Größe** | Meist 32 Bit (4 Bytes) |
| **Prefetching** | Einfach – immer 4 Bytes pro Befehl |
| **Dekodierung** | Parallelisierung trivial |
| **Branch Target** | Immer an 4-Byte-Grenze

### ARM Befehlsformat (A64)

**Alle Befehle sind exakt 32 Bit (4 Bytes)**

| Bitfeld | Position | Größe | Funktion |
|---------|----------|-------|----------|
| **Opcode** | Bits 31–26 | 6 Bit | Befehlstyp |
| **Rm** | Bits 25–21 | 5 Bit | Quellregister 2 |
| **Opt** | Bits 20–15 | 6 Bit | Optionen/Shift |
| **Rn** | Bits 14–10 | 5 Bit | Quellregister 1 |
| **Rd** | Bits 9–5 | 5 Bit | Zielregister |

**Beispiel: `ADD X0, X1, X2`**

| Feld | Bits | Wert |
|------|------|------|
| Opcode | `10001011` | ADD-Operation |
| Rm | `00010` | X2 |
| Shift | `000000` | Kein Shift |
| Rn | `00001` | X1 |
| Rd | `00000` | X0 |

**Vorteile der festen Länge:**

| Aspekt | Vorteil |
|--------|---------|
| **Dekodierung** | Beginnt immer an 4-Byte-Grenze |
| **Parallelisierung** | Mehrere Befehle trivial parallel dekodierbar |
| **Instruction Fetch** | Immer exakt 4 Bytes pro Befehl |
| **Branch Target** | Immer an 4-Byte-Grenze |

**Nachteil: Konstanten laden**

Das Laden einer 64-Bit-Konstante erfordert mehrere Befehle:

```asm
; 64-Bit Konstante 0x123456789ABCDEF0 laden:
MOVZ X0, #0xDEF0              ; Bits 0-15
MOVK X0, #0x9ABC, LSL #16     ; Bits 16-31
MOVK X0, #0x5678, LSL #32     ; Bits 32-47
MOVK X0, #0x1234, LSL #48     ; Bits 48-63
```

> [!note] **Vergleich mit x86**
> x86 kann dieselbe Konstante in **einem** Befehl laden:
> ```asm
> MOV RAX, 0x123456789ABCDEF0
> ```
> (Dafür ist der Befehl aber 10 Bytes lang!)

---
author: Andreas Hümmer

## Pipeline-Vergleich

### Klassische RISC-Pipeline (5 Stufen)

**Pipeline-Stufen:**

| Stufe | Abkürzung | Funktion |
|-------|-----------|----------|
| 1 | **IF** | Instruction Fetch – Befehl holen |
| 2 | **ID** | Instruction Decode – Dekodieren + Register lesen |
| 3 | **EX** | Execute – ALU-Operation |
| 4 | **MEM** | Memory Access – Speicherzugriff |
| 5 | **WB** | Write Back – Ergebnis schreiben |

**Idealer Pipeline-Ablauf:**

| Takt | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|------|---|---|---|---|---|---|---|---|---|
| Befehl 1 | IF | ID | EX | MEM | WB | | | | |
| Befehl 2 | | IF | ID | EX | MEM | WB | | | |
| Befehl 3 | | | IF | ID | EX | MEM | WB | | |
| Befehl 4 | | | | IF | ID | EX | MEM | WB | |
| Befehl 5 | | | | | IF | ID | EX | MEM | WB |

> [!tip] **Ergebnis bei RISC**
> Nach Pipeline-Füllung: **1 Befehl pro Takt** (CPI = 1)
> Einfache, regelmäßige Pipeline-Struktur

---
author: Andreas Hümmer

### CISC mit Mikrocode (klassisch)

**Problem: Komplexe Befehle verstopfen die Pipeline**

| Takt | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|------|---|---|---|---|---|---|---|---|---|---|
| Befehl 1 | IF | ID | µ1 | µ2 | µ3 | WB | | | | |
| Befehl 2 | | IF | — | WAIT | — | — | ID | µ1 | µ2 | WB |
| Befehl 3 | | | IF | — | — | WAIT | — | — | ID | ... |

> [!warning] **Pipeline-Stalls**
> Komplexe Befehle mit mehreren Mikrooperationen blockieren nachfolgende Befehle!

---
author: Andreas Hümmer

### Moderner x86 (mit µOp-Zerlegung)

**Lösung: CISC-Befehle werden zu RISC-ähnlichen µOps zerlegt**

| Schritt | Beschreibung |
|---------|--------------|
| 1. Fetch | x86-Befehl holen |
| 2. Decode | Zerlegung in µOps (Micro-Operations) |
| 3. Execute | µOps durchlaufen Out-of-Order Engine |
| 4. Retire | Ergebnisse in Programmreihenfolge committen |

**Beispiel: `ADD [mem], EAX`**

| µOp | Operation | Beschreibung |
|-----|-----------|--------------|
| µOp1 | `LOAD temp, [mem]` | Wert aus Speicher laden |
| µOp2 | `ADD temp, EAX` | Addition durchführen |
| µOp3 | `STORE [mem], temp` | Ergebnis zurückschreiben |

> [!info] **Kernaussage**
> **Moderne x86-CPUs sind intern RISC-Maschinen!**
> 
> Die komplexen CISC-Befehle werden vom Decoder in einfache µOps zerlegt, die dann wie RISC-Befehle durch eine Out-of-Order-Pipeline laufen.

---
author: Andreas Hümmer

## Direkter Vergleich

| Merkmal | CISC | RISC |
|---------|------|------|
| **Befehlsanzahl** | Viele (200–1000+) | Wenige (50–150) |
| **Befehlslänge** | Variabel (x86: 1–15 Bytes) | Fest (meist 32 Bit) |
| **Befehlskomplexität** | Komplex (mehrere Operationen) | Einfach (1 Op pro Befehl) |
| **Speicherzugriff** | In vielen Befehlen | Nur LOAD/STORE |
| **Adressierungsmodi** | Viele, komplex | Wenige, einfach |
| **Register** | Wenige (8–16) | Viele (32+) |
| **Takte pro Befehl (CPI)** | Variabel (1–100+) | Meist 1 |
| **Codedichte** | Hoch (kompakter Code) | Niedriger (mehr Befehle nötig) |
| **Dekodierung** | Komplex | Einfach |
| **Pipeline-Optimierung** | Schwer | Einfach |
| **Chipfläche** | Groß (komplexe Logik) | Klein (einfache Logik) |
| **Stromverbrauch** | Höher | Niedriger |
| **Compiler-Aufwand** | Niedriger (Hardware hilft) | Höher (Software muss optimieren) |

---
author: Andreas Hümmer

## Performance-Gleichung

### Die CPU-Performance-Formel

$$\text{Ausführungszeit} = \frac{\text{Befehle}}{\text{Programm}} \times \frac{\text{Takte}}{\text{Befehl}} \times \frac{\text{Sekunden}}{\text{Takt}}$$

| Faktor | Beeinflusst durch |
|--------|-------------------|
| **Befehle/Programm** | ISA + Compiler |
| **Takte/Befehl (CPI)** | Architektur + Hardware |
| **Sekunden/Takt** | Taktfrequenz (Hardware) |

### Vergleich der Ansätze

| Aspekt | CISC-Ansatz | RISC-Ansatz |
|--------|-------------|-------------|
| **Befehle/Programm** | Weniger | Mehr |
| **CPI** | Höher (variabel) | ≈ 1 |
| **Hardware** | Komplex | Einfach |
| **Taktfrequenz** | Durch Komplexität begrenzt | Höhere möglich |

### Beispielrechnung (vereinfacht)

| Architektur | Befehle | × CPI | × Taktzeit | = Ausführungszeit |
|-------------|---------|-------|------------|-------------------|
| CISC | 100 | × 4 | × 1 ns | = **400 ns** |
| RISC | 200 | × 1 | × 1 ns | = **200 ns** ← Schneller! |

> [!info] **Moderne CISC erreichen auch CPI < 1**
> Durch fortgeschrittene Techniken:
> - Superskalar-Ausführung (mehrere Befehle parallel)
> - Out-of-Order Execution
> - Spekulative Ausführung
> - Branch Prediction

---
author: Andreas Hümmer

## Moderne Entwicklung

### Konvergenz: CISC außen, RISC innen

**Aufbau eines modernen x86-Prozessors (Intel/AMD):**

#### Frontend (CISC-Interface)

| Komponente | Funktion |
|------------|----------|
| **Instruction Fetch** | Bis zu 16 Bytes/Takt holen |
| **Predecode** | Befehlsgrenzen erkennen (bei variabler Länge!) |
| **Decoder** | 4–5 parallele Dekoder |

**Decoder-Verhalten:**

| Befehlstyp | Dekodierung |
|------------|-------------|
| Einfache Befehle | 1 µOp direkt |
| Komplexe Befehle | 2–4 µOps |
| Sehr komplexe | Microcode-ROM |

→ Ausgabe: µOp Queue / µOp Cache

#### Backend (RISC-artig!)

| Komponente | Funktion |
|------------|----------|
| **Register Renaming** | >100 physische Register (statt 16 architekturelle) |
| **Reorder Buffer (ROB)** | 200+ Einträge für Out-of-Order |
| **Scheduler** | Reservation Stations verteilen µOps |
| **Execution Units** | 6–8 parallele Einheiten (ALU, FPU, Load, Store) |

> [!tip] **Ergebnis**
> Moderne x86-CPUs erreichen **4–6 IPC** (Instructions Per Cycle) trotz CISC-ISA!

---
author: Andreas Hümmer

### RISC-Erweiterungen

Moderne RISC-Prozessoren werden komplexer und haben CISC-ähnliche Erweiterungen:

**ARM:**

| Erweiterung | Funktion |
|-------------|----------|
| **NEON (SIMD)** | 128-Bit Vektoroperationen |
| **SVE/SVE2** | Skalierbare Vektoren bis 2048 Bit |
| **Krypto** | AES, SHA in Hardware |
| **Thumb/Thumb-2** | 16-Bit Befehle für Codedichte |
| **Mikroarchitektur** | Branch Prediction, Out-of-Order, Speculation |

**RISC-V:**

| Erweiterung | Beschreibung |
|-------------|--------------|
| **Basis** | ~50 Befehle (sehr RISC) |
| **M** | Multiplikation/Division |
| **A** | Atomare Operationen |
| **F/D** | Fließkomma (32/64 Bit) |
| **C** | Komprimierte Befehle (16 Bit) |
| **V** | Vektor-Erweiterung |
| **B** | Bit-Manipulation |
| **Zicbom** | Cache-Management |

**Apple Silicon (M1/M2/M3/M4):**

| Merkmal | Details |
|---------|---------|
| **Basis** | ARM-basiert (RISC) |
| **Decoder** | 8 Decoder (mehr als viele x86!) |
| **OoO-Engine** | Massive Out-of-Order Execution |
| **ROB** | Riesiger Reorder Buffer |
| **Spekulation** | Aggressive Speculation |
| **Beschleuniger** | Neural Engine, GPU, Media Engine |

> [!warning] **Fazit: Die Grenze verschwimmt!**
> - **RISC-ISA + komplexe Mikroarchitektur** (Apple M-Serie)
> - **CISC-ISA + RISC-artige Ausführung** (Intel/AMD x86)
> - Beide Ansätze erreichen ähnliche Performance
> - Hauptunterschied: **Energieeffizienz** (RISC oft besser)

---
author: Andreas Hümmer

## Bekannte Vertreter

### CISC-Architekturen

#### x86 / x86-64 (Intel, AMD)

| Aspekt | Details |
|--------|---------|
| **Markt** | Dominiert Desktop, Laptop, Server |
| **Vorteil** | Riesiges Software-Ökosystem |
| **Stärke** | Höchste Single-Thread-Performance |
| **Beispiele** | Core i9, Ryzen 9, Xeon, EPYC |

#### Motorola 68000 (historisch)

| Einsatzgebiet | Systeme |
|---------------|---------|
| Computer | Apple Macintosh (1984–1994), Amiga, Atari ST |
| Konsolen | Sega Genesis/Mega Drive |

#### IBM System/360/370/z (Mainframes)

| Aspekt | Details |
|--------|---------|
| **Einsatz** | Bankenwesen, Versicherungen |
| **Stärke** | Extrem hohe Zuverlässigkeit |
| **Besonderheit** | Abwärtskompatibilität seit 1964! |

---
author: Andreas Hümmer

### RISC-Architekturen

#### ARM (Arm Ltd.)

| Einsatzgebiet | Beispiele |
|---------------|-----------|
| **Smartphones** | ~95% aller Geräte (iPhone, Android) |
| **Tablets** | iPad, Android-Tablets |
| **Desktop** | Apple Silicon (M1, M2, M3, M4) |
| **Server** | AWS Graviton, Ampere Altra |
| **Embedded** | Raspberry Pi, IoT-Geräte |

#### RISC-V (Open Source!)

| Aspekt | Details |
|--------|---------|
| **Lizenz** | Freie ISA ohne Lizenzgebühren |
| **Wachstum** | Stark (China, Europa, USA) |
| **Hersteller** | SiFive, Alibaba T-Head, etc. |
| **Spektrum** | Embedded bis Hochleistung |

#### MIPS (historisch wichtig)

| Einsatzgebiet | Systeme |
|---------------|---------|
| **Konsolen** | PlayStation 1/2, Nintendo 64 |
| **Netzwerk** | Router (Cisco) |
| **Lehre** | Klassisches Lehrbeispiel für RISC |

#### SPARC (Sun/Oracle)

| Aspekt | Details |
|--------|---------|
| **Markt** | High-End Server |
| **Besonderheit** | Register Windows |
| **OS** | Solaris |

#### PowerPC (IBM/Apple/Freescale)

| Einsatzgebiet | Systeme |
|---------------|---------|
| **Computer** | Apple Mac (1994–2006) |
| **Konsolen** | PlayStation 3, Xbox 360, Wii |
| **Server** | IBM POWER Server |

---
author: Andreas Hümmer

## Auswirkungen auf Betriebssysteme

### Kontextwechsel

| Aspekt | CISC (x86-64) | RISC (ARM64) |
|--------|---------------|--------------|
| **Universalregister** | 16 | 31 |
| **Zu sichern** | Weniger Basisregister | Mehr Basisregister |
| **Aber** | Viele Spezialregister (FPU, SSE, AVX-512) | Einheitliches Format (NEON/SVE) |

### Syscall-Mechanismus

| Architektur | Evolution |
|-------------|-----------|
| **x86** | `INT 0x80` → `SYSENTER` → `SYSCALL` (historisch gewachsen) |
| **ARM** | `SVC` (Supervisor Call) – von Anfang an optimiert |

### Memory Model

| Aspekt | x86 | ARM |
|--------|-----|-----|
| **Ordnung** | Stark (Sequential Consistency ähnlich) | Schwach (Relaxed) |
| **Für Programmierer** | Einfacher | Mehr Memory Barriers nötig |
| **Für Hardware** | Muss Ordnung erzwingen | Kann mehr umsortieren → schneller |

**Beispiel: Spinlock-Implementierung**

x86 (einfacher):
```asm
spin_lock:
    lock bts [mutex], 0    ; LOCK-Präfix reicht
    jc spin_lock
    ret
```

ARM (explizite Barriers):
```asm
spin_lock:
    sevl
1:  wfe
    ldaxr w1, [x0]         ; Load-Acquire
    cbnz  w1, 1b
    stxr  w1, w2, [x0]     ; Store-Exclusive
    cbnz  w1, 1b
    ret
```

### Portabilität

**Linux:**
- Architektur-spezifischer Code in `arch/x86` und `arch/arm64`
- Gemeinsamer Kern-Code: >95%
- Abstraktionsschichten für Hardware-Unterschiede

**Windows:**

| Architektur | Unterstützung |
|-------------|---------------|
| x86/x64 | Nativ |
| ARM64 | Mit x86-Emulation (langsamer) |
| Trend | Native ARM64-Apps werden häufiger |

**macOS:**

| Technologie | Funktion |
|-------------|----------|
| **Rosetta 2** | x86 → ARM Übersetzung |
| **Universal Binaries** | Beide Architekturen in einer App |
| **Ergebnis** | Transition Intel → Apple Silicon erfolgreich |

---
author: Andreas Hümmer

## Zusammenfassung

| Aspekt | CISC | RISC |
|--------|------|------|
| **Philosophie** | Komplexe Befehle | Einfache Befehle |
| **Befehlsanzahl** | Viele (200+) | Wenige (50-150) |
| **Befehlslänge** | Variabel | Fest (meist 32 Bit) |
| **CPI** | Variabel (1-100+) | ≈ 1 |
| **Register** | Wenige (8-16) | Viele (32+) |
| **Speicherzugriff** | In vielen Befehlen | Nur LOAD/STORE |
| **Energieeffizienz** | Geringer | Höher |
| **Codedichte** | Hoch | Niedriger |
| **Beispiele** | x86, 68k, VAX | ARM, RISC-V, MIPS |

**Moderne Realität:** Die Unterschiede verschwimmen - x86 ist intern RISC-artig, ARM wird komplexer.

---
author: Andreas Hümmer

## Zusammenhänge

- → [[02-01-Kerneltypen|Kerneltypen]] - Kernel-Design unabhängig von RISC/CISC
- → [[02-02-Schichtenmodell|Schichtenmodell]] - Hardware-Abstraktion
- → [[02-03-Systemaufrufe|Systemaufrufe]] - Syscall-Mechanismus architekturabhängig
- → [[02-04-Von-Neumann-vs-Harvard|Von-Neumann vs. Harvard]] - Speicherarchitektur
- → [[03-01-Prozessmodell|Prozessmodell]] - Kontextwechsel architekturabhängig

### Betriebssystem-Referenzen

- → [[07-Anhang/Betriebssysteme/Linux|Linux]] - Unterstützt beide (x86, ARM, RISC-V, ...)
- → [[07-Anhang/Betriebssysteme/Windows-NT|Windows NT]] - Hauptsächlich x86, zunehmend ARM
- → [[07-Anhang/Betriebssysteme/macOS|macOS]] - Von x86 zu ARM (Apple Silicon)
- → [[07-Anhang/Betriebssysteme/iOS|iOS]] - ARM-basiert
- → [[07-Anhang/Betriebssysteme/Android|Android]] - ARM-basiert (auch x86)

---
author: Andreas Hümmer

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - Unterschiede zwischen RISC und CISC verstehen
> - Vor- und Nachteile beider Ansätze
> - Typische Vertreter (x86 = CISC, ARM = RISC)
> - Moderne Entwicklung: CISC außen, RISC innen

> [!question] **Häufige Prüfungsfragen**
> 1. Nennen Sie die Hauptunterschiede zwischen RISC und CISC
> 2. Warum haben RISC-Prozessoren meist mehr Register?
> 3. Was bedeutet "Load/Store-Architektur"?
> 4. Warum konvergieren moderne CISC und RISC?
> 5. Nennen Sie je 2 Beispiele für RISC- und CISC-Prozessoren
> 6. Welchen Einfluss hat die ISA auf das Betriebssystem?

> [!tip] **Merkhilfen**
> - **CISC** = "Swiss Army Knife" (ein Werkzeug für alles)
> - **RISC** = "Toolbox" (viele spezialisierte Werkzeuge)
> - **Load/Store** = "Erst holen, dann rechnen, dann wegbringen"
> - **Register** = "Schnelle Notizzettel" (RISC hat mehr davon)
> - **x86 intern** = "CISC in Verkleidung, RISC im Herzen"

---
author: Andreas Hümmer

## Quellen

- Patterson, D. & Hennessy, J.: Computer Organization and Design (RISC-V Edition)
- Hennessy, J. & Patterson, D.: Computer Architecture: A Quantitative Approach
- Intel® 64 and IA-32 Architectures Software Developer's Manual
- ARM Architecture Reference Manual (ARMv8-A)
- RISC-V Instruction Set Manual
- Tanenbaum, A. S.: Structured Computer Organization
