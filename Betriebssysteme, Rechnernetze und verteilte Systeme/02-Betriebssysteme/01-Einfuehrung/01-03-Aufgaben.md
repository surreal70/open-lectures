---
author: Andreas Hümmer
title: Aufgaben eines Betriebssystems
tags:
  - content
- bs
- aufgaben
- einfuehrung
- ressourcen
created: '2026-10-07'
modified: '2026-10-07'
bereich: BS
---
author: Andreas Hümmer

# Aufgaben eines Betriebssystems

## Überblick

Ein Betriebssystem erfüllt zwei fundamentale Rollen:

1. **Erweiterte Maschine (Extended Machine)**: Abstraktion der komplexen Hardware in eine einfach nutzbare Schnittstelle
2. **Ressourcenverwalter (Resource Manager)**: Koordination und Zuteilung der Hardware-Ressourcen

Diese duale Sichtweise geht auf Andrew S. Tanenbaum zurück und bildet die Grundlage für das Verständnis aller BS-Funktionen.

---
author: Andreas Hümmer

## Kernfunktionalitäten

Die Aufgabenbereiche eines Betriebssystems lassen sich in vier Hauptkategorien gliedern:

| Kategorie | Verwaltete Elemente |
|-----------|---------------------|
| **Hardware** | CPU, Speicher, E/A-Geräte, Netzwerk |
| **Daten** | Cache, RAM, Swap, Festplatte |
| **Prozesse** | Erzeugung, Scheduling, IPC, Synchronisation |
| **Benutzer** | Accounts, Gruppen, Rechte |

> Nach Baun (2020): "Betriebssysteme kompakt", Springer

---
author: Andreas Hümmer

## Konkrete Aufgaben im Detail

### 1. Schnittstelle zur Hardware

Das Betriebssystem bildet die **Schnittstelle zwischen Anwendungsprogrammen und Hardware**:

![[./.assets/bs-schnittstelle.png]]

*Das Betriebssystem liegt zwischen Anwendungen und Hardware: Nach oben stellt es den Programmen Systemaufrufe (API) bereit, nach unten greift es privilegiert auf die Hardware zu.*

### 2. Ressourcenverwaltung

Als Ressourcenverwalter koordiniert das Betriebssystem den Zugriff mehrerer konkurrierender Prozesse auf die begrenzten Hardware-Ressourcen. Ohne diese zentrale Instanz würden sich Programme gegenseitig behindern oder überschreiben. Das BS entscheidet, welcher Prozess wann wie viel von welcher Ressource erhält – zeitlich (Multiplexing der CPU) und räumlich (Aufteilung des Speichers).

| Ressource | Verwaltungsaufgaben |
|-----------|---------------------|
| **CPU** | Prozesse, CPU-Zuteilung, Synchronisation, Interprozesskommunikation |
| **Speicher** | Speicherverwaltung, Speicherschutz, Mapping (logisch → physisch) |
| **E/A-Geräte** | Gerätetreiber, Pufferung, Interrupt-Handling |

> **Hinweis**: CPU-Verwaltung umfasst auch mehrere Prozessoren, Kerne und Hardware-Threads.

### 3. Programmverwaltung

Damit ein auf der Festplatte liegendes Programm ausgeführt werden kann, muss es zunächst in den Hauptspeicher geladen und als Prozess gestartet werden. Das Betriebssystem übernimmt den gesamten Lebenszyklus: Es reserviert Speicher, lädt den Programmcode, richtet den Prozesskontext ein und gibt beim Beenden alle belegten Ressourcen wieder frei.

- **Laden** von Programmen und Daten in den Hauptspeicher
- **Starten** von Anwendungsprogrammen
- **Beenden** und Ressourcenfreigabe

### 4. Priorisierung und Verteilung

Da mehrere Prozesse gleichzeitig um dieselben Ressourcen konkurrieren, muss das Betriebssystem fair und effizient priorisieren. Zeitkritische Prozesse erhalten dabei Vorrang, während im Hintergrund laufende Aufgaben weniger häufig an die Reihe kommen. Diese Entscheidungen trifft der Scheduler nach definierten Strategien.

- Zuteilung von **Prozessorzeit**
- Vergabe von **Speicherbereichen**
- Reservierung von **Schnittstellen**

### 5. Sicherheit

Das Betriebssystem ist die letzte Verteidigungslinie gegen unbefugten Zugriff und fehlerhafte Programme. Es trennt die Adressräume der Prozesse voneinander, überwacht alle Zugriffe über seine Schnittstellen und setzt Benutzer- und Gruppenrechte durch. So wird verhindert, dass ein Programm Daten eines anderen liest oder das System zum Absturz bringt.

- **Systemsicherheit** gewährleisten
- **Schnittstellenüberwachung**
- **Zugriffsrechte** verwalten

### 6. Geräteansteuerung

Jedes Hardware-Gerät – von der Grafikkarte bis zum USB-Stick – spricht sein eigenes "Protokoll". Das Betriebssystem kapselt diese Unterschiede in Gerätetreibern und bietet Anwendungen eine einheitliche Schnittstelle. Ein Programm muss daher nicht wissen, welcher konkrete Festplattentyp verbaut ist, sondern nutzt dieselben Aufrufe für jedes Speichermedium.

- Steuerung **sämtlicher Hardware** mittels Gerätetreiber
- **Abstraktion** der Hardware-Unterschiede

### 7. Datenverwaltung

Persistente Daten müssen strukturiert, geschützt und effizient gespeichert werden. Das Betriebssystem organisiert dies über das Dateisystem und kann Daten bei Bedarf verschlüsseln oder komprimieren. So bleiben Informationen auch nach dem Ausschalten erhalten und sind gegen unbefugten Zugriff abgesichert.

- **Verschlüsselung** von Daten
- **Komprimierung** bei Bedarf
- **Dateisystemverwaltung** für externe Speicherung

---
author: Andreas Hümmer

## Aufgabenliste (Zusammenfassung)

Nach der IU-Vorlesung erfüllt ein Betriebssystem folgende konkrete Aufgaben:

> [!summary] Die 7 Kernaufgaben
> 1. Schnittstelle zwischen Anwendungen und Hardware
> 2. Privilegierte Systemaufrufe zur Hardware
> 3. Laden, Starten und Beenden von Programmen
> 4. Priorisierung und Verteilung der Ressourcen
> 5. Systemsicherheit und Schnittstellenüberwachung
> 6. Hardwaresteuerung mittels Gerätetreibern
> 7. Datenverwaltung (Verschlüsselung, Komprimierung, Speicherung)

---
author: Andreas Hümmer

## Sichtweisen auf das Betriebssystem

### Top-Down-Sicht (Benutzerperspektive)

Aus Sicht des Benutzers bietet das BS eine **virtuelle Maschine**:
- Einheitliche Schnittstellen (API)
- Abstraktion von Hardware-Details
- Komfortable Programmierumgebung

### Bottom-Up-Sicht (Systemperspektive)

Aus Sicht der Hardware ist das BS ein **Ressourcenmanager**:
- Multiplexing der CPU (zeitlich)
- Multiplexing des Speichers (räumlich)
- Koordination von E/A-Zugriffen

![[./.assets/bs-zwei-sichtweisen.png]]

*Dasselbe Betriebssystem lässt sich aus zwei Blickwinkeln betrachten: Die **Top-Down-Sicht** (Benutzerperspektive) sieht eine virtuelle Maschine mit komfortabler API; die **Bottom-Up-Sicht** (Systemperspektive) sieht einen Ressourcenmanager, der die Hardware verwaltet.*

---
author: Andreas Hümmer

## Abgrenzung: Was gehört NICHT zum Betriebssystem?

Nicht zum Betriebssystem im engeren Sinne gehören:

- **Anwendungsprogramme** (Word, Browser, Spiele)
- **Compiler und Interpreter** (auch wenn oft mitgeliefert)
- **Shell/GUI** (kann als Systemprogramm betrachtet werden)
- **Dienstprogramme** (Utilities wie `ls`, `copy`)

> Die Grenze ist fließend – [[07-Anhang/Betriebssysteme/Windows-10|Windows]] betrachtet den Explorer als Teil des BS, während [[07-Anhang/Betriebssysteme/UNIX|Unix]] die Shell als austauschbares Programm sieht.

---
author: Andreas Hümmer

## Zusammenhänge

- [[01-02-Definition]] – Was ist ein Betriebssystem?
- [[01-01-Historie]] – Historische Entwicklung
- [[02-01-Kerneltypen]] – Kernel-Architekturen
- [[02-02-Schichtenmodell]] – Schichtenaufbau
- [[03-01-Prozessmodell]] – Prozessverwaltung im Detail
- [[05-01-Adressraeume]] – Speicherverwaltung im Detail

---
author: Andreas Hümmer

## Prüfungstipps

> [!warning] Prüfungsrelevant
> - **Zwei Sichtweisen** (Erweiterte Maschine vs. Ressourcenverwalter) erklären können
> - **Die 7 Kernaufgaben** aufzählen und beschreiben
> - **Unterschied** zwischen Betriebssystem und Anwendungsprogramm
> - **Ressourcentypen** (CPU, Speicher, E/A) und deren Verwaltung

---
author: Andreas Hümmer

## Quellen

- Hümmer, A. (2025): *Betriebssysteme, Rechnernetze und verteilte Systeme*, IU Internationale Hochschule, Teil 4 + 5
- Baun, C. (2020): *Betriebssysteme kompakt*, 2. Aufl., Springer
- Tanenbaum, A.S. & Bos, H. (2015): *Modern Operating Systems*, 4th ed., Pearson

### Direkte Quellenreferenzen

**Tanenbaum, A. S. & Bos, H.: Modern Operating Systems (5th Edition)**
- Kapitel 1: Introduction
  - 1.1 What Is an Operating System?
    - 1.1.1 The Operating System as an Extended Machine (→ Erweiterte Maschine)
    - 1.1.2 The Operating System as a Resource Manager (→ Ressourcenverwalter)
  - 1.5 Operating System Concepts
    - 1.5.1 Processes (→ Prozessverwaltung)
    - 1.5.2 Address Spaces (→ Speicherverwaltung)
    - 1.5.3 Files (→ Dateiverwaltung)
    - 1.5.4 Input/Output (→ E/A-Geräteverwaltung)
    - 1.5.5 Security (→ Sicherheit)
- Kapitel 2: Processes and Threads
  - 2.1 Processes (→ Programmverwaltung: Laden, Starten, Beenden)

**Silberschatz, A., Galvin, P. B. & Gagne, G.: Operating System Concepts (10th Edition)**
- Chapter 1: Introduction
  - 1.1 What Operating Systems Do
    - 1.1.1 User View (→ Top-Down-Sicht)
    - 1.1.2 System View (→ Bottom-Up-Sicht)
  - 1.4 Operating-System Structure
- Chapter 2: Operating-System Structures
  - 2.1 Operating-System Services (→ Die 7 Kernaufgaben)
    - User Interface
    - Program Execution (→ Programmverwaltung)
    - I/O Operations (→ E/A-Verwaltung)
    - File-System Manipulation (→ Datenverwaltung)
    - Communications (→ Interprozesskommunikation)
    - Error Detection (→ Fehlerbehandlung)
    - Resource Allocation (→ Ressourcenverwaltung)
    - Logging/Accounting
    - Protection and Security (→ Sicherheit)

**Baun, C.: Betriebssysteme kompakt (2. Auflage, 2020)**
- Kapitel 3: Grundlagen der Betriebssysteme
  - 3.2 Positionierung und Kernfunktionalitäten von Betriebssystemen
    - Abb. 3.3 Kernfunktionalitäten (→ Kernfunktionalitäten-Diagramm)
  - Hardware-Verwaltung (→ CPU, Speicher, E/A)
  - Daten-Verwaltung (→ Dateisystem)
  - Prozess-Verwaltung (→ Scheduling, IPC)
  - Benutzer-Verwaltung (→ Accounts, Rechte)

### Weiterführende Literatur

- Stallings, W.: Operating Systems: Internals and Design Principles
  - Chapter 2: Operating System Overview
    - 2.3 Operating System Design (→ Schnittstellen-Konzept)
    - 2.4 Operating System Structure (→ Schichtenarchitektur)
