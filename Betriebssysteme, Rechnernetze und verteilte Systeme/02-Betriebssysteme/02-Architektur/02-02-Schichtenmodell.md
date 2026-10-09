---
author: Andreas Hümmer
title: Schichtenmodell
tags:
  - content
- bs
- schichten
- architektur
- abstraction
- layering
created: '2026-10-07'
modified: '2026-10-07'
bereich: BS
---
author: Andreas Hümmer

# Schichtenmodell

## Überblick

> [!info] **Lernziele**
> - Das Konzept der Schichtenarchitektur verstehen
> - Die typischen Schichten eines Betriebssystems kennen
> - Vor- und Nachteile des Schichtenmodells beurteilen können
> - Reale Implementierungen (THE, UNIX, Windows) einordnen können
> - CPU-Ringe und Privilegierungsstufen verstehen

Das **Schichtenmodell** (Layered Architecture) organisiert ein Betriebssystem in hierarchische Ebenen. Jede Schicht baut auf der darunterliegenden auf und bietet Dienste für die darüberliegende an - ähnlich wie beim OSI-Modell in Netzwerken.

---
author: Andreas Hümmer

## Das Prinzip der Schichtung

### Grundidee

![[./.assets/schichtenprinzip.png]]

*Grundidee der Schichtung: Jede Schicht N nutzt ausschließlich die Dienste der direkt darunterliegenden Schicht N-1 und bietet selbst Dienste für die Schicht N+1 darüber. Da nur über die definierte Schnittstelle kommuniziert wird, lässt sich eine Schicht austauschen, ohne die anderen zu verändern.*

### Regeln der Schichtung

Damit die Vorteile der Schichtung tatsächlich greifen, muss die Hierarchie bestimmten Regeln folgen. Entscheidend ist, dass eine Schicht nur die direkt darunterliegende kennt und ihre eigene Umsetzung nach außen verbirgt. Erst diese Disziplin erlaubt es, einzelne Schichten unabhängig zu entwickeln, zu testen und auszutauschen.

| Regel | Beschreibung |
|-------|--------------|
| **Abstraktion** | Jede Schicht versteckt Komplexität vor höheren Schichten |
| **Kapselung** | Implementierungsdetails sind unsichtbar |
| **Dienste** | Jede Schicht bietet definierte Dienste nach oben |
| **Abhängigkeit** | Eine Schicht kennt nur die direkt darunterliegende |
| **Austauschbarkeit** | Schichten können ersetzt werden (bei gleicher Schnittstelle) |

---
author: Andreas Hümmer

## Generisches Betriebssystem-Schichtenmodell

Überträgt man das abstrakte Schichtenprinzip auf ein konkretes Betriebssystem, ergibt sich eine typische Staffelung von der nackten Hardware bis zur Benutzeroberfläche. Jede Ebene fügt eine weitere Abstraktion hinzu: Die untersten Schichten machen die Hardware überhaupt ansprechbar, die mittleren verwalten Ressourcen, die obersten stellen dem Benutzer nutzbare Programme bereit.

### 6-Schichten-Modell

![[./.assets/sechs-schichten-modell.png]]

*Das 6-Schichten-Modell ordnet ein Betriebssystem von der Hardware (Schicht 1) bis zu den Benutzeranwendungen (Schicht 6). Die Schichten 2–4 (HAL, Gerätetreiber, Kernel) laufen im privilegierten Kernel-Space, die Schichten 5–6 im User-Space. Zwischen den Ebenen vermitteln definierte Schnittstellen: das Hardware-Interface, die System Calls und die API/Libraries.*

### Beschreibung der Schichten

| Schicht | Name | Funktion |
|---------|------|----------|
| **6** | Benutzeranwendungen | Programme, die der Endbenutzer ausführt |
| **5** | Systemdienste | Shell, GUI, Daemon-Prozesse, Utilities |
| **4** | Betriebssystem-Kern | Prozess-, Speicher-, Dateiverwaltung |
| **3** | Gerätetreiber | Hardware-spezifische Ansteuerung |
| **2** | HAL | Hardware-Abstraktion, Portabilitätsschicht |
| **1** | Hardware | Physische Komponenten (CPU, RAM, I/O) |

---
author: Andreas Hümmer

## CPU-Ringe und Privilegierungsstufen

Die Trennung zwischen privilegiertem Kernel und unprivilegierten Anwendungen ist nicht nur ein Software-Konzept, sondern wird direkt von der Hardware durchgesetzt. Dazu kennt die CPU verschiedene Privilegierungsstufen, die festlegen, welche Befehle ein laufendes Programm ausführen darf. So kann eine fehlerhafte oder bösartige Anwendung nicht einfach auf die Hardware zugreifen oder den Kernel überschreiben.

### Das Ring-Modell

Moderne CPUs (x86, ARM) implementieren **Schutzringe** (Protection Rings), die verschiedene Privilegierungsstufen definieren:

![[./.assets/cpu-protection-rings.png]]

*CPU-Schutzringe als konzentrische Privilegstufen: Im Zentrum liegt Ring 0 (Kernel) mit vollem Hardware-Zugriff, außen Ring 3 für Anwendungen mit stark eingeschränkten Rechten. Je weiter innen, desto mehr Privilegien. Die Ringe 1 und 2 waren ursprünglich für Treiber bzw. OS-Dienste gedacht, werden heute aber kaum genutzt.*

### Praktische Verwendung der Ringe

| Ring | Verwendung | Rechte |
|------|------------|--------|
| **Ring 0** | Kernel | Alle CPU-Befehle, direkter Hardware-Zugriff |
| **Ring 1** | (meist ungenutzt) | Ursprünglich für Treiber vorgesehen |
| **Ring 2** | (meist ungenutzt) | Ursprünglich für privilegierte Utilities |
| **Ring 3** | Anwendungen | Eingeschränkt, keine privilegierten Befehle |

> [!note] Praxis: Nur Ring 0 und Ring 3
> Die meisten modernen Betriebssysteme ([[07-Anhang/Betriebssysteme/Linux|Linux]], [[07-Anhang/Betriebssysteme/Windows-NT|Windows]]) verwenden nur **Ring 0** (Kernel) und **Ring 3** (User). Die Ringe 1 und 2 werden ignoriert.

### Ring-Wechsel (Mode Switch)

Da Anwendungen in Ring 3 keine privilegierten Operationen ausführen dürfen, benötigen sie für jeden Hardware- oder Kernel-Dienst einen kontrollierten Übergang nach Ring 0. Dieser Wechsel – der *Mode Switch* – ist der einzige legale Weg vom User- in den Kernel-Mode und wird über Systemaufrufe ausgelöst. Er ist bewusst teuer und streng kontrolliert, denn an dieser Stelle entscheidet sich die Sicherheit des gesamten Systems.

![[./.assets/ring-wechsel-mode-switch.png]]

*Beim Mode Switch wechselt die CPU zwischen User Mode (Ring 3) und Kernel Mode (Ring 0): Ein Anwendungsaufruf wie `read()` löst über eine SYSCALL-/INT-Instruktion den Übergang in den Kernel aus, der die eigentliche Funktion `sys_read()` ausführt. Mit SYSRET/IRET kehrt die Ausführung anschließend in den User Mode zurück.*

**Ablauf im Detail:**

1. User-Programm ruft `read()` auf (über die libc)
2. libc legt die Parameter in Register
3. `SYSCALL` / `INT 0x80` → CPU wechselt in Ring 0
4. Kernel führt `sys_read()` aus
5. Ergebnis in Register, `SYSRET` / `IRET` → zurück in Ring 3

---
author: Andreas Hümmer

## Historisches Beispiel: THE-System (1968)

### Dijkstras THE Multiprogramming System

Das **THE-System** (Technische Hogeschool Eindhoven) von **Edsger Dijkstra** (1968) war das erste konsequent geschichtete Betriebssystem.

Das System war in sechs Schichten (0–5) über der Hardware organisiert – von unten nach oben:

| Schicht | Funktion | Details |
|---------|----------|---------|
| **Schicht 5** | Benutzerprogramme | Operator-Interface |
| **Schicht 4** | Benutzer-Prozesse | Unabhängige Programme |
| **Schicht 3** | I/O-Management | Ein-/Ausgabe-Puffer |
| **Schicht 2** | Operator-Konsole-Kommunikation | Message Passing |
| **Schicht 1** | Speicherverwaltung | Segmentierung, virtueller Speicher |
| **Schicht 0** | Prozessor-Scheduling | CPU-Zuweisung, Semaphoren |
| *(Hardware)* | Electrologica X8 | Zielrechner von 1968 |

### Bedeutung des THE-Systems

| Innovation             | Beschreibung                                                 |
| ---------------------- | ------------------------------------------------------------ |
| **Semaphoren**         | Dijkstra erfand hier das Konzept zur Prozess-Synchronisation |
| **Strenge Schichtung** | Erste konsequente Anwendung des Layering-Prinzips            |
| **Beweisbarkeit**      | System konnte formal verifiziert werden                      |
| **Einfluss**           | Grundlage für alle modernen OS-Architekturen                 |

---
author: Andreas Hümmer

## Unix/Linux Schichtenmodell

Unix und seine Nachfolger setzen das Schichtenmodell pragmatisch um: Oberhalb der strikten Grenze zwischen User- und Kernel-Space ist die Hierarchie klar, innerhalb des Kernels wird sie dagegen bewusst gelockert, um Leistung zu gewinnen. Das Ergebnis ist ein überwiegend monolithischer Kernel, dessen Subsysteme dennoch sauber voneinander abgegrenzt sind.

### Traditionelle Unix-Architektur

![[./.assets/unix-linux-architektur.png]]

*Die Unix/Linux-Architektur gliedert sich in User-Space (Anwendungen über die libc) und Kernel-Space, getrennt durch das System Call Interface. Im Kernel verteilt der System-Call-Dispatcher die Aufrufe an die Subsysteme (Prozess-, Speicherverwaltung, VFS, Netzwerk-Stack, Security). Darunter liegen die Gerätetreiber und der architekturabhängige Code, der die konkrete Hardware anspricht.*

### Das Virtual File System (VFS)

Eine Schlüsselabstraktion in Unix/Linux ist das **VFS**, das verschiedene Dateisysteme hinter einer einheitlichen Schnittstelle vereint:

![[./.assets/virtual-file-system.png]]

*Das VFS bietet Anwendungen eine einheitliche Schnittstelle (`open`, `read`, `write`, `close`, `stat`), unabhängig davon, welches Dateisystem tatsächlich dahintersteckt. So landet ein `open()` je nach Pfad transparent bei ext4, btrfs, procfs, NFS oder FAT – und damit auf lokaler SSD, in Kernel-Daten, auf einem Remote-Server oder einem USB-Stick.*

---
author: Andreas Hümmer

## Windows NT Schichtenmodell

Windows NT wurde von Anfang an stärker geschichtet entworfen als klassisches Unix. Ein zentrales Gestaltungsziel war die Portabilität über verschiedene Prozessorarchitekturen hinweg sowie die gleichzeitige Unterstützung mehrerer API-Umgebungen. Deshalb trennt NT die Umgebungs-Subsysteme sauber vom Kern und kapselt die Hardware explizit in einer eigenen Abstraktionsschicht.

### Die NT-Architektur

![[./.assets/windows-nt-architektur.png]]

*Windows NT trennt User Mode (Ring 3) und Kernel Mode (Ring 0): Anwendungen rufen über Subsystem-DLLs und `ntdll` die Native API auf; Environment-Subsysteme bieten verschiedene API-Umgebungen (Windows, POSIX/WSL). Im Kernel-Mode liegt die große Executive mit ihren Managern über dem Low-Level-Kernel, den Gerätetreibern und dem HAL, der die konkrete Hardware kapselt.*

### Windows-spezifische Schichten

| Schicht | Komponente | Funktion |
|---------|------------|----------|
| **Subsystem DLLs** | kernel32.dll, user32.dll | Win32-API-Implementierung |
| **ntdll.dll** | Native API | Syscall-Stubs, User-Kernel-Übergang |
| **Executive** | ntoskrnl.exe | Kernelfunktionen, Manager |
| **Kernel** | ntoskrnl.exe (Teil) | Low-Level: Scheduling, Interrupts |
| **HAL** | hal.dll | Hardware-Abstraktion |

---
author: Andreas Hümmer

## Vor- und Nachteile des Schichtenmodells

Das Schichtenmodell ist kein Selbstzweck, sondern ein Kompromiss. Es erkauft seine Klarheit und Wartbarkeit mit einem gewissen Leistungsverlust, weil jeder Schichtübergang Aufwand bedeutet. In der Praxis wägen Betriebssysteme deshalb ständig ab, wie streng sie die Hierarchie durchhalten.

### Vorteile

| Vorteil | Erklärung |
|---------|-----------|
| ✅ **Modularität** | Klare Trennung ermöglicht unabhängige Entwicklung |
| ✅ **Abstraktion** | Komplexität wird versteckt |
| ✅ **Wartbarkeit** | Änderungen in einer Schicht betreffen andere nicht |
| ✅ **Testbarkeit** | Jede Schicht kann isoliert getestet werden |
| ✅ **Verständlichkeit** | Einfacher zu verstehen und dokumentieren |
| ✅ **Portierbarkeit** | Hardware-Abhängigkeiten auf untere Schichten begrenzt |

### Nachteile

| Nachteil | Erklärung |
|----------|-----------|
| ❌ **Performance-Overhead** | Jede Schicht kostet Zeit (Funktionsaufrufe) |
| ❌ **Schichtendefinition** | Schwierig, optimale Aufteilung zu finden |
| ❌ **Strenge Hierarchie** | Manchmal ineffizient (z.B. Treiber braucht VFS und umgekehrt) |
| ❌ **Durchbrechungen** | In Praxis oft "Layer Violations" für Performance |

### Strenge vs. Relaxierte Schichtung

![[./.assets/strenge-vs-relaxierte-schichtung.png]]

*Bei strenger Schichtung ruft jede Schicht ausschließlich die direkt darunterliegende auf. Bei relaxierter Schichtung dürfen Schichten auch tiefere Ebenen direkt aufrufen (im Bild überspringt Schicht 3 die Schicht 2) – das verbessert die Performance, lockert aber die saubere Hierarchie auf.*

|  | Strenge Schichtung | Relaxierte Schichtung |
|--|--------------------|------------------------|
| **Prinzip** | Jede Schicht nutzt nur die direkt darunterliegende | Schichten dürfen auch tiefere Ebenen direkt aufrufen |
| **Vorteile** | Sauberes Design, einfach zu verstehen | Bessere Performance, flexibler |
| **Nachteile** | Langsamer, manchmal umständlich | Komplexer, schwerer zu warten |

---
author: Andreas Hümmer

## Vergleich: Unix vs. Windows Schichtung

Beide Systeme verfolgen dasselbe Grundprinzip, treffen aber unterschiedliche Entwurfsentscheidungen. Unix setzt auf eine pragmatische, überwiegend monolithische Struktur mit minimaler Hardware-Abstraktion, während Windows NT stärker modularisiert ist und Portabilität sowie mehrere API-Umgebungen in den Vordergrund stellt. Die folgende Gegenüberstellung fasst die wichtigsten Unterschiede zusammen:

| Aspekt | Unix/Linux | Windows NT |
|--------|------------|------------|
| **User-Space API** | POSIX (libc) | Win32 (kernel32.dll) |
| **Syscall-Mechanismus** | INT 0x80 / SYSCALL | SYSENTER / SYSCALL |
| **Treiber-Integration** | Im Kernel (Module) | Kernel-Mode + User-Mode |
| **HAL** | Arch-spezifischer Code | Explizites hal.dll |
| **Dateisystem-Abstraktion** | VFS | I/O Manager + Filter |
| **Subsysteme** | Native POSIX | Win32, POSIX, (OS/2) |
| **Schichtendurchbrechung** | Selten | Häufiger (Performance) |

---
author: Andreas Hümmer

## Zusammenhänge

- [[02-01-Kerneltypen]] - Wie Kernel-Architekturen das Schichtenmodell beeinflussen
- [[02-03-Systemaufrufe]] - Die Schnittstelle zwischen User- und Kernel-Space
- [[03-01-Prozessmodell]] - Prozesse und Threads in der Schichtung
- [[05-01-Adressraeume]] - Speicherschutz und Adressräume

---
author: Andreas Hümmer

## Prüfungstipps

> [!warning] Prüfungsrelevant
> - **Das Grundprinzip** der Schichtung erklären können (Abstraktion, Kapselung)
> - **CPU-Ringe**: Ring 0 (Kernel) vs. Ring 3 (User) verstehen
> - **Mode Switch**: Wie wechselt ein Programm vom User- in den Kernel-Mode?
> - **THE-System**: Historische Bedeutung (Dijkstra, Semaphoren, erste Schichtung)
> - **Unix-Schichten**: VFS als Abstraktionsschicht kennen
> - **Windows-Schichten**: HAL, Executive, Kernel unterscheiden
> - **Vor-/Nachteile**: Modularität vs. Performance-Overhead

**Typische Prüfungsfragen:**
1. Erklären Sie das Prinzip der Schichtung in Betriebssystemen.
2. Was sind CPU-Ringe und warum werden nur Ring 0 und Ring 3 genutzt?
3. Zeichnen Sie das generische 6-Schichten-Modell eines Betriebssystems.
4. Welche Funktion hat das Virtual File System (VFS) in Unix/Linux?
5. Nennen Sie drei Vorteile und zwei Nachteile des Schichtenmodells.

---
author: Andreas Hümmer

## Quellen

- Tanenbaum, A. S. & Bos, H.: Modern Operating Systems, Kapitel 1.7 "Operating System Structure"
- Silberschatz, Galvin, Gagne: Operating System Concepts, Chapter 2.7 "Operating-System Structure"
- Dijkstra, E. W.: "The Structure of the THE Multiprogramming System", 1968
- Vorlesung: "Betriebssysteme, Rechnernetze und verteilte Systeme" - Teil 4: Architektur (IU)

### Weiterführende Links

- [THE Multiprogramming System (Original Paper)](https://www.cs.utexas.edu/users/EWD/transcriptions/EWD01xx/EWD196.html)
- [Linux Kernel Documentation: Filesystems](https://www.kernel.org/doc/html/latest/filesystems/)
- [Windows Internals (Microsoft)](https://learn.microsoft.com/en-us/sysinternals/resources/windows-internals)
- [Protection Rings (Wikipedia)](https://en.wikipedia.org/wiki/Protection_ring)
