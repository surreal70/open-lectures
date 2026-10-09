---
author: Andreas Hümmer
title: "Betriebssysteme, Rechnernetze und verteilte Systeme"
tags:
  - content
  - importiert
  - bs
created: '2026-10-07'
modified: '2026-10-07'
bereich: BS
typ: sonstig
quelle: "12-iu-Betriebssysteme, Rechnernetze und verteilte Systeme-BETRIEBSSYSTEME-Teil4-v2.0 - Übersicht Architektur Definitionen.pdf"
seiten: 14
---
author: Andreas Hümmer

# Betriebssysteme, Rechnernetze und verteilte Systeme

> [!info] Dokumentinformationen
> - **Quelle:** 12-iu-Betriebssysteme, Rechnernetze und verteilte Systeme-BETRIEBSSYSTEME-Teil4-v2.0 - Übersicht Architektur Definitionen.pdf
> - **Typ:** sonstig
> - **Bereich:** BS
> - **Seiten:** 14
> - **Autor:** Andreas Hümmer

---
author: Andreas Hümmer

## Inhalt

### Seite 1

Betriebssysteme,
Rechnernetze und
verteilte Systeme
Sommersemester 2024
Andreas Hümmer
V 1.1
iu © 2023 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE

### Seite 2

Betriebssysteme
Übersicht
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme

### Seite 3

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Einstieg in die Betriebsysteme und deren Strukturen
Fragerunde 
. .www menti com
100n

### Seite 4

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Welche Betriebssysteme kennen Sie?
https://de.wikipedia.org/wiki/
Liste_von_Betriebssystemen

### Seite 5

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
In welchen Geräten befinden sich Betriebssysteme
und welcher Art? (Auszug)
Gerät „vollwertiges“
Betriebssystem
Resident Monitor (RM)
PC/Server Windows, Unix
Mobile Geräte iOS, Android, Symbian
Smartcards TCOS
Mainframe zOS, BS2000
Embedded Systems RTOS Ja auch
Industriesteuerung/
Automotive
Ja auch

### Seite 6

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
A brief history of…Evolution in Aktion, die ganze
Geschichte
 Geschichte der Unix Betriebssysteme als PDF zum
Ausdrucken :
https://www.levenez.com/unix/redirect_unix_pdf.html
 Geschichte der Windows Betriebssysteme als PDF zum
Ausdrucken :
https://www.levenez.com/windows/windows.pdf
 Es gibt noch mehr, viel mehr:
http://shannon.usu.edu.ru/History/oshistory/

### Seite 7

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Wie viele Betriebssysteme hat dieses System?
Mehrer
e!
Bild: Dell
inc.
Netzwerkkarte: Realtime OS oder
RM
Baseboard Management: Intel
Manageengine/Minix
Storagecontroller: Realtime OS oder
RM
PrimärOS: Windows oder Unix oder
Hypervisor

### Seite 8

Betriebssysteme
Architektur und Definition
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme

### Seite 9

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Betriebssystemarchitekturen – Unix *)
Benutzer
Programme Bibliotheken
API -Interface
Prozesskontrolle
Gerätetreiber
IPC
Interprozess-
kommunikati
on
Speicher-
verwaltungScheduler
Buffers
Dateisystem
DateiverwaltungNetzwerk
IO-Subsystem / HAL
Hardware
Network Character Block
Hardwa
re
Supervis
or
(Kernel)
Use
r
*) exemplarisch für einen monolithischen
Kernel

### Seite 10

Windows Executive
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Betriebssystemarchitekturen - Windows
WOW
Security
Subsystem
HAL
Hardware Hardwa
re
Supervis
or
Use
r
E/A
Manager
Treiber
Graphik-
Subsyste
m
Treiber
Microkernel
Objekt
Manager
Prozess
Manager
Virtueller
Speicher
Manager
Sicherheit
s Monitor
Local
Procdure
Call
Interface
Systemdienste
OS/2 Subsystem
Win32/64
Subsystem
Posix Subsystem

### Seite 11

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Betriebssystemarchitekturen - Kernelvariationen

### Seite 12

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Betriebssystem -  abstrakt
HARDWARE (Prozessor, Speicher,
Ein-/Ausgabe)
Hardware-Abstraktionsschicht
Geräte-Treiber, Dateisystem,
Hardwaresteuerung (Kernel)
Systemschnittstelle
Prozessor- und Ressourcenmanagement
Anwendungsprogamme
Systemaufrufe für
Anwendungsprogramme (API )
Betriebssyst
em
Einheitliche Aufrufe als Schnittstelle
zwischen Anwendungsprogramm
und
Betriebssystem
Privilegierte Zugriffe auf die
Hardware
Koordinierung der Zugriffe auf
Prozessor,
Speicher und Ein-/Ausgabe
Ansteuerung der wichtigsten
Geräte,
Datenleitungen und
Speichermedien
Kapselung der spezifischen
Hardware-
Plattform, damit dass
Betriebssystem
auf unterschiedlicher Hardware
lauffähig ist.

### Seite 13

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Was ist also die Aufgabe eines Betriebssystems?
 Bildet die Schnittstelle zwischen Anwendungsprogrammen und
den Hardware-Komponenten
 Interagiert über privilegierte Zugriffe, sogenannte
Systemaufrufe, mit der Hardware
 Organisiert das Laden, Starten und Beenden von
Anwendungsprogrammen einschließlich ihrer Daten in den
Hauptspeicher
 Priorisiert und verteilt die Prozessor- , Speicher- und
Schnittstellen-Ressourcen
 Gewährleistet die Systemsicherheit und
Schnittstellenüberwachung
 Steuert mittels spezieller Gerätetreiber sämtliche Bestandteile
der Hardware
 Verschlüsselt, komprimiert und verwaltet sämtliche extern zu
speichernden Daten

### Seite 14

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Definitionen
"Ein Programm, das als Vermittler zwischen Anwender und Hardware
fungiert. Der Sinn des Betriebssystems ist eine Umgebung bereitzustellen,
in der der Anwender bequem und effizient Programme ausführen kann"
[Silberschatz]
"Eine Softwareschicht, die alle Teile des Systems verwaltet und dem
Benutzer eine Schnittstelle oder virtuelle Maschine anbietet, die leichter zu
verstehen und zu programmieren ist (als die zugrundeliegende reale
Hardware/Maschine)." [Tanenbaum]
„Das Betriebssystem wird gebildet durch die Programme eines digitalen
Rechensystems, die zusammen mit den Eigenschaften der Rechenanlage
die Grundlage der möglichen Betriebsarten des digitalen Rechensystems
bilden und insbesondere die Ausführung von Programmen steuern und
überwachen.“  [DIN 44300]
