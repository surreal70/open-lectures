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
quelle: "13-iu-Betriebssysteme, Rechnernetze und verteilte Systeme-BETRIEBSSYSTEME-Teil3-v2.0 - Exkurs Rechnerarchitekturen.pdf"
seiten: 14
---
author: Andreas Hümmer

# Betriebssysteme, Rechnernetze und verteilte Systeme

> [!info] Dokumentinformationen
> - **Quelle:** 13-iu-Betriebssysteme, Rechnernetze und verteilte Systeme-BETRIEBSSYSTEME-Teil3-v2.0 - Exkurs Rechnerarchitekturen.pdf
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
Sommersemester 2025
Andreas Hümmer
V 2.0
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE

### Seite 2

iu © 2023 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Einstieg in die Betriebsysteme und deren Strukturen
Fragerunde 
. .www menti com

### Seite 3

iu © 2023 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Welche Betriebssysteme kennen Sie?
https://de.wikipedia.org/wiki/
Liste_von_Betriebssystemen

### Seite 4

iu © 2023 Andreas Hümmer iu INTERNATIONALE
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

### Seite 5

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

### Seite 6

iu © 2023 Andreas Hümmer iu INTERNATIONALE
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

### Seite 7

Betriebssysteme
Exkurs Rechnerarchitekturen
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme

### Seite 8

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Exkurs: Rechnerarchitekturen
Von Neumann- vs Harvard-Architektur
Von Neuman Harvard
Programm- und Datenspeicher sind eins Programmspeicher ist vom Datenspeicher
getrennt
General Purpose – einfach und günstig Special Purpose – aufwändiger und meist
teurer
Begrenzung durch „nur einen“ Speicherbus Geschwindigkeitsvorteilt durch Trennung
von Daten- und Programmspeicherzugriff
BSP: x86 Familie, general purpose CPU Bsp.: Embedded Controller, DSP, special
purpose CPUHeute oft
Mischformen
Bild:
Wikimedia

### Seite 9

iu © 2025  Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Exkurs: Rechnerarchitekturen
Von Neumann-Architektur
Computer
Modul
Funktion
Prozessor Ausführung von Programmen und Berechnung von Daten
Hauptspeich
er
Zwischenspeichern des Programcodes und der
erforderlichen Daten
Ein-/Ausgabe Austausch von Adress,- Daten- und Steuerinformationen
mit externen Einheiten
Bussystem Ermöglicht die Kommunikation und den Datenaustausch
zwischen den Modulen
Bild:
Wikimedia

### Seite 10

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Exkurs: Rechnerarchitekturen
RISC vs CISC

### Seite 11

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Exkurs: Rechnerarchitekturen
RISC vs CISC
RISC CISC
Reduced Instruction Set Computer Complex Instruction Set Computer
Einfache Befehle die in einem Zyklus
abgearbeitet werden
Komplexe Instruktionen, die mehrere
Zyklen benötigen
Sehr wenige Instruktionen referenzieren
den Speicher
Viele Instruktionen referenzieren den
Speicher
Instruktionen werden durch Hardware
ausgeführt
Instruktionen werden durch Microcode
ausgeführt
Festes Befehlsformat Variables Befehlsformat
Komplexe Adressierungsmethoden werden
via Software realisiert
Komplexe Adressierungsmethoden werden
direkt unterstützt
Mehrere Registersätze Ein Registersatz
Pipeling Wenig oder kein Pipelinig
Komplexität im Compiler Komplextät im Microcode
Heute oft
Mischformen

### Seite 12

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Exkurs: Rechnerarchitekturen

### Seite 13

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Exkurs: Rechnerarchitekturen

### Seite 14

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Exkurs: Rechnerarchitekturen
