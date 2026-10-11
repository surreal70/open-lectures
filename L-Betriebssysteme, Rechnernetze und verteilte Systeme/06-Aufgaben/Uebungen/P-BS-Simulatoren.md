---
author: Andreas Hümmer
title: 'Praxisübung: Betriebssysteme mit Simulatoren'
tags:
  - uebung
  - praxis
  - bs
  - simulator
  - deadlock
  - cpu
  - von-neumann
bereich: BS
created: '2026-10-09'
modified: '2026-10-09'
---

# Praxisübung: Betriebssysteme mit Simulatoren

**Bereich:** BS – Systemarchitektur und Konzepte
**Voraussetzungen:** Webbrowser, ggf. Java Runtime

---

> [!info] **Lernziele**
> Nach dieser Übung solltest du:
> - Deadlock-Situationen in einem Simulator erkennen und analysieren können
> - Die Von-Neumann-Architektur praktisch verstehen
> - CPU-Zyklen (Fetch-Decode-Execute) beobachten können
> - Assembler-Grundlagen in einer simulierten Umgebung anwenden können

---

## Teil 1: Deadlock-Simulation mit MOSS

**MOSS** (Modern Operating Systems Simulators) ist eine Sammlung von Lehrsimulatoren, entwickelt für das Lehrbuch von Andrew S. Tanenbaum.

> [!tip] **Simulator-Link**
> **[MOSS Deadlock Simulator](http://www.ontko.com/moss/deadlock/user_guide.html)**

### Aufgabe 1.1: Installation und Einrichtung

1. Lade den MOSS Deadlock Simulator herunter
2. Stelle sicher, dass Java installiert ist
3. Starte den Simulator

```bash
# Download (falls verfügbar)
# Oder direkt über die Website

# Java-Version prüfen
java -version

# Simulator starten
java -jar deadlock.jar
```

### Aufgabe 1.2: Deadlock-Erkennung

**Experiment 1: Einen Deadlock erzeugen**

Konfiguriere den Simulator mit:
- 3 Prozesse (P0, P1, P2)
- 3 Ressourcentypen (R0, R1, R2)
- Jeweils 1 Instanz pro Ressourcentyp

Erstelle folgende Anforderungssequenz:

| Schritt | Prozess | Aktion | Ressource |
|---------|---------|--------|-----------|
| 1 | P0 | Request | R0 |
| 2 | P1 | Request | R1 |
| 3 | P2 | Request | R2 |
| 4 | P0 | Request | R1 |
| 5 | P1 | Request | R2 |
| 6 | P2 | Request | R0 |

**Fragen:**

a) Bei welchem Schritt tritt der Deadlock auf?

_Dein Antwort:_

<br><br>

b) Zeichne den Resource Allocation Graph für den Deadlock-Zustand:

<br><br><br><br>

c) Welche Coffman-Bedingungen sind erfüllt?

_Dein Antwort:_

<br><br>

### Aufgabe 1.3: Deadlock-Vermeidung

**Experiment 2: Banker's Algorithm**

Konfiguriere den Simulator für den Banker's Algorithm mit:
- Ressourcen: A=10, B=5, C=7
- 5 Prozesse mit folgenden maximalen Anforderungen:

| Prozess | Max A | Max B | Max C | Belegt A | Belegt B | Belegt C |
|---------|-------|-------|-------|----------|----------|----------|
| P0 | 7 | 5 | 3 | 0 | 1 | 0 |
| P1 | 3 | 2 | 2 | 2 | 0 | 0 |
| P2 | 9 | 0 | 2 | 3 | 0 | 2 |
| P3 | 2 | 2 | 2 | 2 | 1 | 1 |
| P4 | 4 | 3 | 3 | 0 | 0 | 2 |

**Aufgaben:**

a) Berechne die verfügbaren Ressourcen (Available):

| A | B | C |
|---|---|---|
| ? | ? | ? |

b) Ist der aktuelle Zustand sicher? Finde eine sichere Sequenz!

_Dein Antwort:_

<br><br><br>

c) P1 fordert (1, 0, 2) an. Soll das System die Anforderung gewähren?

_Dein Antwort:_

<br><br>

---

## Teil 2: Von-Neumann-Architektur mit Johnny Simulator

**Johnny** ist ein Simulator für einen einfachen Von-Neumann-Rechner, entwickelt an deutschen Universitäten.

> [!tip] **Simulator-Link**
> **[Johnny Simulator Download](https://sourceforge.net/projects/johnnysimulator/files/latest/download)**

### Aufgabe 2.1: Installation

1. Lade Johnny herunter
2. Entpacke das Archiv
3. Starte den Simulator

### Aufgabe 2.2: Von-Neumann-Zyklus beobachten

Johnny zeigt den klassischen Fetch-Decode-Execute-Zyklus:

1. **Fetch**: Befehl aus dem Speicher holen
2. **Decode**: Befehl interpretieren
3. **Execute**: Befehl ausführen

**Experiment: Einfaches Additionsprogramm**

Gib folgendes Programm ein:

```
Adresse | Befehl
--------|--------
   0    | TAKE 10    ; Lade Wert von Adresse 10 in Akkumulator
   1    | ADD 11     ; Addiere Wert von Adresse 11
   2    | SAVE 12    ; Speichere Ergebnis an Adresse 12
   3    | STOP       ; Programm beenden

  10    | 5          ; Erster Operand
  11    | 7          ; Zweiter Operand
  12    | 0          ; Platz für Ergebnis
```

**Aufgaben:**

a) Führe das Programm Schritt für Schritt aus und beobachte:
- Den Programmzähler (PC)
- Den Akkumulator
- Den Speicherinhalt

b) Was steht nach der Ausführung an Adresse 12?

_Dein Antwort:_

<br><br>

c) Wie viele Speicherzugriffe werden für den `ADD 11`-Befehl benötigt?

_Dein Antwort:_

<br><br>

### Aufgabe 2.3: Schleife programmieren

Schreibe ein Programm, das die Zahlen 1 bis 5 aufsummiert (Ergebnis: 15).

**Hinweis:** Du brauchst:
- Einen Zähler
- Eine Schleife mit bedingtem Sprung
- Eine Summen-Variable

```
Adresse | Befehl
--------|--------
   0    | ???
   1    | ???
   ...
```

---

## Teil 3: CPU-Simulation mit Visual 6502

Die **Visual 6502** Projekte zeigen die tatsächliche Funktionsweise historischer CPUs auf Transistor-Ebene.

> [!tip] **Simulator-Links**
> - **[6502 CPU (Apple II, C64)](http://www.visual6502.org/JSSim/index.html)**
> - **[6800 CPU (Motorola)](http://www.visual6502.org/JSSim/expert-6800.html)**
> - **[ARM1 CPU](http://www.visual6502.org/sim/varm/armgl.html)**

### Aufgabe 3.1: 6502 CPU erkunden

Die 6502 CPU war in vielen historischen Computern verbaut (Apple II, Commodore 64, NES).

1. Öffne den 6502 Simulator
2. Beobachte die Chip-Visualisierung (Transistoren!)
3. Führe ein einfaches Programm aus

**Experimente:**

a) Beobachte, wie sich die "aktiven" Transistoren (hervorgehoben) während der Ausführung ändern.

b) Identifiziere den Akkumulator (A), die Index-Register (X, Y) und den Stack-Pointer (S).

c) Wie viele Taktzyklen benötigt ein `LDA #$42` (Load Accumulator Immediate)?

_Dein Antwort:_

<br><br>

### Aufgabe 3.2: ARM1 CPU

Die ARM1 war der erste ARM-Prozessor (1985) – Vorfahre der CPUs in heutigen Smartphones.

1. Öffne den ARM1 Simulator
2. Vergleiche die Komplexität mit der 6502

**Frage:** Wie unterscheidet sich die ARM-Architektur (RISC) von der 6502 (CISC) visuell?

_Dein Antwort:_

<br><br>

---

## Teil 4: MIPS-Simulation mit EduMIPS64

**EduMIPS64** ist ein Simulator für die MIPS64-Architektur, entwickelt für Bildungszwecke.

> [!tip] **Simulator-Link**
> **[EduMIPS64 Download](https://sourceforge.net/projects/edumips64/)**

### Aufgabe 4.1: MIPS-Grundlagen

MIPS ist eine klassische RISC-Architektur, die in vielen Lehrbüchern verwendet wird.

**Experiment: Einfaches MIPS-Programm**

```mips
; Zwei Zahlen addieren
.data
    num1:  .word 10
    num2:  .word 20
    result: .word 0

.text
    lw $t0, num1($zero)    ; Lade num1 in $t0
    lw $t1, num2($zero)    ; Lade num2 in $t1
    add $t2, $t0, $t1      ; $t2 = $t0 + $t1
    sw $t2, result($zero)  ; Speichere Ergebnis
    syscall                 ; Beenden
```

**Aufgaben:**

a) Beobachte die Pipeline-Stages (IF, ID, EX, MEM, WB)

b) Identifiziere Pipeline-Stalls (Hazards)

c) Was ist der Unterschied zwischen `lw` (Load Word) und `add`?

_Dein Antwort:_

<br><br>

---

## Teil 5: x86-Simulation mit jSim8086

**jSim8086** simuliert den Intel 8086 Prozessor.

> [!tip] **Simulator-Link**
> **[jSim8086 Download](https://sourceforge.net/projects/jsim8086/)**

### Aufgabe 5.1: x86 Assembler-Grundlagen

```asm
; Einfaches 8086 Programm
mov ax, 5      ; AX = 5
mov bx, 3      ; BX = 3
add ax, bx     ; AX = AX + BX = 8
```

**Aufgaben:**

a) Führe das Programm aus und beobachte die Register

b) Welche Flags werden durch die `add`-Operation beeinflusst?

_Dein Antwort:_

<br><br>

---

## Bonus: IBM Mainframe mit Hercules

**Hercules** emuliert IBM Mainframe-Systeme (S/370, S/390, z/Architecture).

> [!tip] **Simulator-Link**
> **[SDL Hercules 390](https://sdl-hercules-390.github.io/html/)**

> [!warning] **Komplexität**
> Dies ist ein fortgeschrittenes Projekt. Die Installation und Konfiguration erfordert Einarbeitung.

**Optionale Aufgabe:** Installiere Hercules und starte ein minimales MVS-System.

---

## Zusammenfassung: Simulator-Übersicht

| Simulator | Fokus | Schwierigkeit | Plattform |
|-----------|-------|---------------|-----------|
| **MOSS Deadlock** | Deadlock-Erkennung | ⭐ Einfach | Java |
| **Johnny** | Von-Neumann | ⭐ Einfach | Java |
| **Visual 6502** | CPU-Transistoren | ⭐⭐ Mittel | Browser |
| **EduMIPS64** | RISC-Pipeline | ⭐⭐ Mittel | Java |
| **jSim8086** | x86 Assembler | ⭐⭐ Mittel | Java |
| **Hercules** | IBM Mainframe | ⭐⭐⭐ Schwer | Native |

---

## Quellen

- [[04-Deadlocks|Deadlocks]]
- [[01-Prozessmodell|Prozessmodell]]
- MOSS Project: http://www.ontko.com/moss/
- Visual 6502: http://www.visual6502.org/
- Tanenbaum: Modern Operating Systems
