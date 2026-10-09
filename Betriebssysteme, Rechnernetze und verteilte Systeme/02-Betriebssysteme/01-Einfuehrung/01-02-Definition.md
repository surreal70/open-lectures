---
author: Andreas Hümmer
title: Definition eines Betriebssystems
tags:
  - content
- bs
- definition
- einfuehrung
- architektur
created: '2026-10-07'
modified: '2026-10-07'
bereich: BS
---
author: Andreas Hümmer

# Definition eines Betriebssystems

## Überblick

Ein **Betriebssystem** (englisch: Operating System, OS) ist die fundamentale Software, die als Vermittler zwischen Anwendungsprogrammen und der Computer-Hardware fungiert. Es verwaltet alle Hardware-Ressourcen und stellt eine einheitliche Schnittstelle für Programme und Benutzer bereit.

> [!info] **Lernziele**
> - Die verschiedenen Definitionen eines Betriebssystems kennen
> - Die Schichtenarchitektur eines Betriebssystems verstehen
> - Die Kernaufgaben eines Betriebssystems benennen können
> - Den Unterschied zwischen Kernel- und User-Mode verstehen

---
author: Andreas Hümmer

## Definitionen aus der Literatur

### Silberschatz (Operating System Concepts)

> [!quote] Definition nach Silberschatz
> *"Ein Programm, das als Vermittler zwischen Anwender und Hardware fungiert. Der Sinn des Betriebssystems ist eine Umgebung bereitzustellen, in der der Anwender bequem und effizient Programme ausführen kann."*
> — Silberschatz, Galvin, Gagne: Operating System Concepts

Diese Definition betont die **Benutzerorientierung**: Das Betriebssystem soll dem Anwender die Arbeit erleichtern.

### Tanenbaum (Modern Operating Systems)

> [!quote] Definition nach Tanenbaum
> *"Eine Softwareschicht, die alle Teile des Systems verwaltet und dem Benutzer eine Schnittstelle oder virtuelle Maschine anbietet, die leichter zu verstehen und zu programmieren ist (als die zugrundeliegende reale Hardware/Maschine)."*
> — Tanenbaum, Bos: Modern Operating Systems

Diese Definition betont die **Abstraktion**: Das Betriebssystem verbirgt die Komplexität der Hardware.

### DIN 44300 (Deutsche Norm)

> [!quote] Definition nach DIN 44300
> *"Das Betriebssystem wird gebildet durch die Programme eines digitalen Rechensystems, die zusammen mit den Eigenschaften der Rechenanlage die Grundlage der möglichen Betriebsarten des digitalen Rechensystems bilden und insbesondere die Ausführung von Programmen steuern und überwachen."*
> — DIN 44300

Diese formale Definition betont die **Steuerungs- und Überwachungsfunktion** des Betriebssystems.

---
author: Andreas Hümmer

## Zwei Sichtweisen auf Betriebssysteme

### 1. Top-Down: Erweiterung der Maschine (Abstraktion)

Aus Sicht des **Anwendungsprogrammierers** erweitert das Betriebssystem die nackte Hardware zu einer komfortableren "virtuellen Maschine":

| Reale Hardware | Virtuelle Maschine (OS) |
|----------------|-------------------------|
| Komplizierte Register | Einfache Systemaufrufe |
| Bit-Level-Programmierung | Abstrakte Konzepte |
| Geräte-spezifische Codes | Einheitliche APIs |
| Keine Fehlerbehandlung | Fehlerbehandlung |

> [!example] Beispiel: Festplattenzugriff
> **Hardware-Sicht:** Zylinder, Köpfe, Sektoren, DMA, Interrupts
> **OS-Sicht:** `open()`, `read()`, `write()`, `close()` – einfache Aufrufe!

### 2. Bottom-Up: Ressourcenmanager (Verwaltung)

Aus Sicht des **Systems** ist das Betriebssystem ein Verwalter, der die begrenzten Hardware-Ressourcen fair und effizient verteilt:

| Ressource | Verwaltungsaufgabe |
|-----------|--------------------|
| **CPU** | Scheduling, Prozesswechsel |
| **Hauptspeicher** | Zuteilung, Schutz, Virtual Memory |
| **Festplatten** | Dateisystem, Caching, Defragmentierung |
| **Netzwerk** | Protokolle, Pufferung, Routing |
| **Peripherie** | Treiber, Interrupt-Handling |

> [!tip] Warum braucht man das?
> **Ohne OS:** Chaos – Programme überschreiben sich gegenseitig.
> **Mit OS:** Geordneter, fairer Zugriff auf alle Ressourcen.

---
author: Andreas Hümmer

## Abstrakte Schichtenarchitektur

Das folgende Diagramm zeigt die typische Schichtenarchitektur eines Betriebssystems:

![[.assets/schichtenarchitektur.png]]

*Das Betriebssystem liegt als Schichtenstapel zwischen den Anwendungsprogrammen und der Hardware. Nach oben bildet die **System-Call-API** die Schnittstelle zu den Anwendungen, nach unten greift der **Kernel-Mode** privilegiert auf die Hardware zu. Dazwischen koordinieren Ressourcenmanagement, Gerätetreiber/Dateisystem und die Hardware-Abstraktionsschicht (HAL) den Betrieb.*

---
author: Andreas Hümmer

## Aufgaben eines Betriebssystems

Zusammenfassend hat ein Betriebssystem folgende Kernaufgaben:

| Aufgabe | Beschreibung |
|---------|--------------|
| **Schnittstelle** | Bildet die Schnittstelle zwischen Anwendungsprogrammen und den Hardware-Komponenten |
| **Systemaufrufe** | Interagiert über privilegierte Zugriffe (Systemaufrufe) mit der Hardware |
| **Programmverwaltung** | Organisiert das Laden, Starten und Beenden von Anwendungsprogrammen einschließlich ihrer Daten in den Hauptspeicher |
| **Ressourcenverwaltung** | Priorisiert und verteilt die Prozessor-, Speicher- und Schnittstellen-Ressourcen |
| **Sicherheit** | Gewährleistet die Systemsicherheit und Schnittstellenüberwachung |
| **Gerätesteuerung** | Steuert mittels spezieller Gerätetreiber sämtliche Bestandteile der Hardware |
| **Datenverwaltung** | Verschlüsselt, komprimiert und verwaltet sämtliche extern zu speichernden Daten |

---
author: Andreas Hümmer

## Wo finden wir Betriebssysteme?

Betriebssysteme sind nicht nur auf PCs zu finden, sondern in praktisch jedem elektronischen Gerät:

| Gerät | "Vollwertiges" Betriebssystem | Resident Monitor (RM) / RTOS |
|-------|------------------------------|------------------------------|
| **PC/Server** | [[07-Anhang/Betriebssysteme/Windows-10\|Windows]], [[07-Anhang/Betriebssysteme/Linux\|Linux]], [[07-Anhang/Betriebssysteme/macOS\|macOS]], [[07-Anhang/Betriebssysteme/UNIX\|Unix]] | - |
| **Mobile Geräte** | [[07-Anhang/Betriebssysteme/iOS\|iOS]], [[07-Anhang/Betriebssysteme/Android\|Android]], ([[07-Anhang/Betriebssysteme/Symbian\|Symbian]]†) | - |
| **Smartcards** | [[07-Anhang/Betriebssysteme/TCOS\|TCOS]], [[07-Anhang/Betriebssysteme/JavaCard\|JavaCard]] | ✓ |
| **Mainframes** | [[07-Anhang/Betriebssysteme/z-OS\|z/OS]], [[07-Anhang/Betriebssysteme/BS2000\|BS2000]] | - |
| **Embedded Systems** | [[07-Anhang/Betriebssysteme/Linux\|Linux]] Embedded | RTOS, [[07-Anhang/Betriebssysteme/FreeRTOS\|FreeRTOS]] |
| **Industriesteuerung** | - | RTOS, [[07-Anhang/Betriebssysteme/VxWorks\|VxWorks]] |
| **Automotive** | Android Auto, [[07-Anhang/Betriebssysteme/QNX\|QNX]] | [[07-Anhang/Betriebssysteme/AUTOSAR\|AUTOSAR]], RTOS |
| **Netzwerkgeräte** | - | Firmware, RTOS |

### Smartcard-Betriebssysteme

Auch Chipkarten (Smartcards) enthalten vollständige Betriebssysteme - nur eben extrem miniaturisiert.

![[.assets/smartcard.png]]
*Smartcard mit sichtbarem Chip-Modul und Kontaktflächen*

#### Aufbau einer Smartcard

Eine Smartcard enthält einen kompletten Mikrocontroller mit Kontaktflächen nach **ISO 7816**:

![[.assets/smartcard-kontakte.png]]

*Kontaktbelegung des Chip-Moduls nach ISO 7816-2: fünf Kontakte in der oberen, drei in der unteren Reihe. Aktive Kontakte (amber) übernehmen Spannung, Reset, Takt, Masse, Programmierspannung und Datenein-/ausgabe; die Kontakte 4 und 8 sind reserviert (RFU).*

**Interner Aufbau des Chip-Moduls:**

![[.assets/smartcard-chip-aufbau.png]]

*Interner Aufbau des Chip-Moduls: Der Rechenkern (CPU, RAM, ROM mit dem Betriebssystem) ist über einen gemeinsamen Bus mit dem EEPROM/Flash (Anwendungsdaten und Schlüssel), einem optionalen Krypto-Coprozessor (RSA, ECC, AES, SHA) und dem I/O-Interface (kontaktbehaftet nach ISO 7816 oder kontaktlos über NFC) verbunden.*

#### Wichtige Smartcard-Betriebssysteme

| Betriebssystem | Hersteller | Einsatzgebiet |
|----------------|------------|---------------|
| **[[07-Anhang/Betriebssysteme/TCOS\|TCOS]]** | Deutsche Telekom (TeleSec) | Personalausweis, Reisepass, Signaturkarten |
| **JCOP** | IBM/NXP | Bankkarten, Zugangskarten, eID |
| **[[07-Anhang/Betriebssysteme/JavaCard\|JavaCard]]** | Oracle (Spezifikation) | Plattform für portable Applets |
| **MULTOS** | MULTOS Consortium | Hochsicherheits-Bankkarten |
| **BasicCard** | ZeitControl | Entwicklung, Prototypen |

#### [[07-Anhang/Betriebssysteme/TCOS|TCOS]] (Telekom Chipcard Operating System)

**[[07-Anhang/Betriebssysteme/TCOS|TCOS]]** ist das deutsche Smartcard-Betriebssystem der Telekom Security:
- **BSI-zertifiziert** nach Common Criteria (EAL4+/EAL5+)
- Eingesetzt im **deutschen Personalausweis** und **Reisepass**
- Unterstützt PKI, digitale Signaturen, Verschlüsselung
- Kontakt- und kontaktlos (Dual Interface)

#### JavaCard / JCOP

**JavaCard** ist eine Plattform, die Java-Applets auf Smartcards ausführt:
- **Portabilität**: Applets laufen auf verschiedenen Karten
- **Multi-Application**: Mehrere Anwendungen auf einer Karte
- **JCOP** (Java Card OpenPlatform): Implementierung von IBM/NXP
- Eingesetzt in: Bankkarten, SIM-Karten, Firmenausweise

#### Besonderheiten von Smartcard-OS

Smartcard-Betriebssysteme unterscheiden sich grundlegend von Desktop- oder Server-Systemen: Sie laufen auf extrem begrenzter Hardware und stellen Sicherheit über Komfort.

| Eigenschaft | Ausprägung |
|-------------|------------|
| **Speicher** | Extrem begrenzt (KB statt GB) |
| **Persistenz** | Kein Dateisystem im klassischen Sinn |
| **Sicherheit** | Hardware-Krypto, Manipulationsschutz |
| **Stromversorgung** | Extern über Kontakte/Induktion |
| **Kommunikation** | APDU-Befehle (Application Protocol Data Unit) |

> [!info] ISO 7816
> Die Norm **[ISO 7816](https://www.iso.org/standard/54089.html)** definiert die physikalischen Eigenschaften, Kontaktbelegung und Kommunikationsprotokolle für Smartcards. Teil 4 definiert die APDU-Struktur für Kommandos und Antworten.
> 
> - [ISO 7816 - Wikipedia](https://en.wikipedia.org/wiki/ISO/IEC_7816)

### Echtzeit-Betriebssysteme (RTOS)

**Echtzeit-Betriebssysteme** (Real-Time Operating Systems, RTOS) garantieren, dass Aufgaben innerhalb definierter Zeitgrenzen abgeschlossen werden.

#### Definition

> [!quote] Echtzeit-Definition
> Ein Echtzeitsystem ist ein System, bei dem die **Korrektheit** nicht nur vom logischen Ergebnis abhängt, sondern auch vom **Zeitpunkt**, zu dem das Ergebnis produziert wird.

#### Harte vs. Weiche Echtzeit

| Typ | Beschreibung | Beispiel |
|-----|--------------|----------|
| **Harte Echtzeit** | Deadline-Verletzung = Systemversagen | Airbag-Auslösung, ABS, Herzschrittmacher |
| **Weiche Echtzeit** | Deadline-Verletzung = Qualitätsverlust | Video-Streaming, Audio-Wiedergabe |
| **Feste Echtzeit** | Verspätete Ergebnisse sind wertlos, aber nicht gefährlich | Finanz-Transaktionen |

#### Eigenschaften eines RTOS

Ein RTOS ist nicht primär auf Durchsatz optimiert, sondern auf **zeitliche Vorhersagbarkeit**. Die folgenden Kerneigenschaften stellen sicher, dass Deadlines zuverlässig eingehalten werden.

| Kerneigenschaft | Beschreibung |
|-----------------|--------------|
| **Determinismus** | Vorhersagbare Ausführungszeit (WCET) |
| **Preemption** | Höher-priore Tasks können unterbrechen |
| **Niedrige Latenz** | Schnelle Interrupt-Reaktion |
| **Prioritäts-Scheduling** | Strikte Prioritäten |
| **Minimaler Footprint** | Wenig RAM/ROM erforderlich |
| **Ressourcen-Management** | Mutex, Semaphore, Priority Inversion |

#### Wichtige RTOS-Systeme

| RTOS | Lizenz | Einsatzgebiet |
|------|--------|---------------|
| **FreeRTOS** | MIT (Open Source) | IoT, Embedded, Amazon AWS |
| **VxWorks** | Proprietär (Wind River) | Aerospace, Militär, Mars Rover |
| **QNX** | Proprietär (BlackBerry) | Automotive, Medizin |
| **RTEMS** | Open Source | Raumfahrt (ESA, NASA) |
| **Zephyr** | Apache 2.0 | IoT, Wearables |
| **µC/OS** | Proprietär/Open | Embedded Systems |
| **AUTOSAR OS** | Standard | Automotive |

#### Scheduling in RTOS

RTOS verwenden spezielle Scheduling-Algorithmen:

| Algorithmus | Beschreibung |
|-------------|--------------|
| **Rate Monotonic (RM)** | Statische Priorität nach Periode (kürzere Periode = höhere Priorität) |
| **Earliest Deadline First (EDF)** | Dynamische Priorität nach Deadline |
| **Fixed Priority Preemptive** | Feste Prioritäten, sofortige Unterbrechung |

#### Vergleich: RTOS vs. General-Purpose OS

| Eigenschaft | RTOS | General-Purpose OS |
|-------------|------|-------------------|
| **Ziel** | Zeitgarantien | Durchsatz, Fairness |
| **Scheduling** | Prioritätsbasiert | Time-Sharing |
| **Latenz** | Mikrosekunden | Millisekunden |
| **Footprint** | KB bis wenige MB | GB |
| **Determinismus** | Garantiert | Best-Effort |

#### Einsatzgebiete

RTOS stecken in unzähligen Geräten des Alltags – meist unsichtbar, aber überall dort, wo Reaktionen zeitlich garantiert sein müssen.

| Einsatzgebiet | Beispiele |
|---------------|-----------|
| **Automotive** | ABS, ESP, Airbag, Motor-ECU, Infotainment |
| **Aerospace** | Flugsteuerung, Satellit, Drohne |
| **Medizin** | Herzschrittmacher, Infusionspumpe |
| **Industrie** | SPS/PLC, Roboter, CNC-Fräse |
| **Consumer** | Drucker, Waschmaschine, Kamera |
| **Telekommunikation** | Router, Basisstation, 5G-Modem |

> [!info] Weiterführende Links
> - [FreeRTOS - Official Site](https://www.freertos.org/)
> - [VxWorks - Wind River](https://www.windriver.com/products/vxworks)
> - [QNX - BlackBerry](https://blackberry.qnx.com/)
> - [Zephyr Project](https://zephyrproject.org/)
> - [RTOS - Wikipedia](https://en.wikipedia.org/wiki/Real-time_operating_system)

### Mehrere Betriebssysteme in einem System

Ein moderner Server kann **mehrere Betriebssysteme gleichzeitig** enthalten:

![Dell PowerEdge Server mit geöffnetem Gehäuse](../../assets/images/dell-poweredge-server-offen.jpg)
*Dell PowerEdge Server - Ansicht von oben mit geöffnetem Gehäuse (Quelle: servershopping.com)*

Das folgende Diagramm zeigt schematisch die Komponenten und ihre jeweiligen Betriebssysteme:

![[.assets/rack-server-betriebssysteme.png]]

*Schematische Darstellung eines Rack-Servers (PowerEdge-Architektur). Auf der Hauptplatine läuft das primäre Betriebssystem – doch die Erweiterungskarten (NIC, RAID, BMC) führen jeweils ihr **eigenes** eingebettetes OS aus. Ein moderner Server besteht also aus vielen kooperierenden Betriebssystemen.*

**Legende – Betriebssysteme im Server:**

| Komponente | Betriebssystem | Funktion |
|------------|----------------|----------|
| CPU / Hauptsystem | Windows / Linux / Hypervisor | Hauptbetriebssystem |
| NIC (Netzwerkkarte) | RTOS / Firmware | Paketverarbeitung |
| RAID-Controller | RTOS / Firmware | Disk-I/O, RAID |
| BMC (iDRAC/iLO) | Minix / ARM-Linux | Remote-Management |

---
author: Andreas Hümmer

## Zusammenfassung

> [!summary] Kerndefinition
> Ein **Betriebssystem** ist eine Softwareschicht, die:
> 1. Die Hardware-Komplexität vor Anwendungen verbirgt (**Abstraktion**)
> 2. Hardware-Ressourcen fair und effizient verteilt (**Ressourcenmanagement**)
> 3. Eine einheitliche Programmierschnittstelle bereitstellt (**API/Systemaufrufe**)
> 4. Die Systemsicherheit gewährleistet (**Schutz**)

---
author: Andreas Hümmer

## Zusammenhänge

- [[01-01-Historie|Historie]] - Historische Entwicklung der Betriebssysteme
- [[01-03-Aufgaben|Aufgaben]] - Detaillierte Beschreibung der BS-Aufgaben
- [[02-01-Kerneltypen|Kerneltypen]] - Monolithisch vs. Mikrokernel
- [[02-02-Schichtenmodell|Schichtenmodell]] - Detaillierte Architektur
- [[02-03-Systemaufrufe|Systemaufrufe]] - API zwischen Anwendung und Kernel

---
author: Andreas Hümmer

## Prüfungstipps

> [!warning] Prüfungsrelevant
> - Die drei Definitionen (Silberschatz, Tanenbaum, DIN 44300) kennen und unterscheiden
> - Die zwei Sichtweisen: Erweiterung der Maschine vs. Ressourcenmanager
> - Die Schichtenarchitektur mit ihren Aufgaben
> - Die Kernaufgaben eines Betriebssystems aufzählen können

---
author: Andreas Hümmer

## Quellen

- Vorlesung: "Betriebssysteme, Rechnernetze und verteilte Systeme" - Teil 4: Übersicht Architektur Definitionen (IU), Version 2.0
- Silberschatz, A., Galvin, P. B. & Gagne, G.: Operating System Concepts (10th Edition), Chapter 1
- Tanenbaum, A. S. & Bos, H.: Modern Operating Systems (5th Edition), Chapter 1
- DIN 44300: Informationsverarbeitung - Begriffe

### Direkte Quellenreferenzen

**Tanenbaum, A. S. & Bos, H.: Modern Operating Systems (5th Edition)**
- Kapitel 1: Introduction
  - 1.1 What Is an Operating System?
    - 1.1.1 The Operating System as an Extended Machine (→ Zwei Sichtweisen)
    - 1.1.2 The Operating System as a Resource Manager (→ Ressourcenmanagement)
  - 1.2 History of Operating Systems (→ Verweise auf Historie)
  - 1.5 Operating System Concepts
    - 1.5.1 Processes (→ Programmverwaltung)
    - 1.5.2 Address Spaces (→ Speicherverwaltung)
    - 1.5.3 Files (→ Dateiverwaltung)
    - 1.5.5 Security (→ Sicherheit)

**Silberschatz, A., Galvin, P. B. & Gagne, G.: Operating System Concepts (10th Edition)**
- Chapter 1: Introduction
  - 1.1 What Operating Systems Do
    - 1.1.1 User View (→ Benutzerperspektive)
    - 1.1.2 System View (→ Systemperspektive/Ressourcenmanager)
    - 1.1.3 Defining Operating Systems (→ Definitionen)
  - 1.2 Computer-System Organization (→ Schichtenarchitektur)
  - 1.4 Operating-System Structure (→ Kerneltypen-Verweis)
  - 1.10 Computing Environments
    - 1.10.2 Mobile Computing (→ Embedded/Mobile BS)
    - 1.10.5 Real-Time Embedded Systems (→ RTOS)

**Baun, C.: Betriebssysteme kompakt (2. Auflage, 2020)**
- Kapitel 3: Grundlagen der Betriebssysteme
  - 3.2 Positionierung und Kernfunktionalitäten von Betriebssystemen (→ Kernfunktionalitäten-Diagramm)
  - Abb. 3.2 Positionierung des Betriebssystems (→ Schichtenarchitektur)
  - Abb. 3.3 Kernfunktionalitäten von Betriebssystemen

**DIN 44300: Informationsverarbeitung - Begriffe**
- Teil 1: Grundbegriffe
  - Definition Betriebssystem (→ DIN-Definition)

### Weiterführende Links

- [Liste von Betriebssystemen - Wikipedia](https://de.wikipedia.org/wiki/Liste_von_Betriebssystemen)
- [Unix History - Levenez](https://www.levenez.com/unix/)
- [Windows History - Levenez](https://www.levenez.com/windows/)
- [Operating System History Collection](http://shannon.usu.edu.ru/History/oshistory/)
