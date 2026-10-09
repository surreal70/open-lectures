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
quelle: "14-iu-Betriebssysteme, Rechnernetze und verteilte Systeme-BETRIEBSSYSTEME-Teil5-v2.1 - Ressourcen.pdf"
seiten: 54
---
author: Andreas Hümmer

# Betriebssysteme, Rechnernetze und verteilte Systeme

> [!info] Dokumentinformationen
> - **Quelle:** 14-iu-Betriebssysteme, Rechnernetze und verteilte Systeme-BETRIEBSSYSTEME-Teil5-v2.1 - Ressourcen.pdf
> - **Typ:** sonstig
> - **Bereich:** BS
> - **Seiten:** 54
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
V 2.1
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE

### Seite 2

Betriebssysteme
Ressoucenverwaltung
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
Verwaltung der Hardware (Ressourcen)
 CPU *)
 Prozesse
 CPU-Zuteilung
 Synchronisation
 Interprozesskommunikation
 Speicher (zusammen mit der MMU) **)
 Speicherverwaltung
 Speicherschutz
 Speicher Mapping (logisch auf physisch)
 E/A Geräte
*) Auch mehrere, auch Cores oder Thread
Units
**) Arbeitsspeicher und
Hintergrundspeicher

### Seite 4

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Interrupt
Definition: Ein Interrupt ist ein Hardware-Signal an den
Prozessor, um die sequenzielle Abarbeitung der
Befehlszyklen zu unterbrechen.
 Dieses Signal kann von einem Systemprogramm
(privilegierte Zugriffsrechte) ausgelöst werden.
 Ein Interrupt wird benötigt, um in Echtzeit eine
Systemantwort erhalten zu können, obwohl die CPU gerade
ein anderes Programm abarbeitet.
 Der Interrupt Handler sichert den aktuellen
Programmzustand, reagiert auf den jeweiligen Interrupt und
sorgt dafür, dass im Anschluss das unterbrochene Programm
wieder ordnungsgemäß fortgesetzt wird.
 Ein Interrupt wird z. B. bei einer Unterbrechung durch eine
Tastatur-Eingabe genutzt.

### Seite 5

Betriebssysteme
Prozesse
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme

### Seite 6

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Prozesse
Definition: Ein Prozess ist ein Programm, das ausgeführt
wird.
Ein Prozess hat einen Prozesskontext: PCB – Process Control
Block
 Speicher: Code, Daten, Stack
 Prozessorregister: Instruktionszeiger, Stapelzeiger,
Mehrzweckregister,
Prozessorstatusregister
 Benutzer, Zugriffsrechte
 Belegte Betriebsmittel: z.B. Dateien, Geräte, etc.
 …
Prozesse benötigen Betriebsmittel haben einen Zustand und
unterliegen der Kontrolle des Betriebssystems. Prozesse sind
ein Strukturkonzept für Systemaktivitäten und bilden eine
Prozesshirarchie.

### Seite 7

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Prozesse und (System)prioritäten
Systemprozesse
Interaktive Prozesse
Batchprozesse
Benutzerprozesse
Priorit
ät

### Seite 8

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Prozessverhalten und Prozesszustände
Running
Blocked
Ready
Prozessszustände:
Running:
Der Prozess wird gerade
ausgeführt
Ready:
Prozess ist rechenbereit und
wartet
auf die CPU
Blocked:
Prozess wartet auf die
Beendigung
einer E/A Aktivität

### Seite 9

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Scheduling
Warteschlange CPU
Neue
Aufträge/
Prozesse
fertige
Aufträg
e/
Prozess
e
Verdrängte Aufträge /
Prozesse

### Seite 10

Betriebssysteme
Prozess Scheduling
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme

### Seite 11

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Scheduling - Grundlegendes
 Basisziel: Geordneter Ablauf konkurrierender Prozesse
Was führt zu Veränderungen in der Zuteilung, welche
Ereignisse lösen Veränderungen aus?
Welche Kriterien gibt es für die Reihenfolge mit der
Prozesse ablaufen (sollen)?
 …weitere Ziele des Scheduling Algorithmus:
 Kurze Antwortzeiten
 Optimale CPU Auslastung
 Echtzeitverhalten, …
 Zielsetzungen müssen für jedes System individuell
festgelegt werden – es gibt kein „one fits all“

### Seite 12

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Scheduling - Zuteilungsstrategien
 Einfache
FCFS – Fist come first serve
 Zeitscheibenbasiert
RR – Round Robin, VRR – Virtual Round Robin
 Vorhersagebasiert
SPN (SJF), SRTF, HRRN
 Prioritätenbasiert
FB (MLQ, MLFQ)
Weitere Strategien für Mehrprozessorbetrieb, Echtzeitbetrieb,
etc.
Interaktives Tool der Universität Osnabrück:
https://ess.cs.uni-osnabrueck.de/software/AnimOS/

### Seite 13

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Scheduling – Zuteilungsstrategien - Workshop
Interaktives Tool der Universität Osnabrück:
https://ess.cs.uni-osnabrueck.de/software/AnimOS/

### Seite 14

Betriebssysteme
Threads
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme

### Seite 15

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Threads (Leichtgewichtige Prozesse)
 Die direkte Beziehung zwischen Kontrollfluss und
Adressraum wird aufgehoben.
 Kooperierende Threads können sich einen Adressraum
teilen (aber nicht den Stack)
 Vorteile:
 Aktivitäten (Programme) können von Hyperthreding
profitieren, wenn sie aus mehreren unabhängigen
Kontrollflüssen bestehen.
 Aufgrund des selben Adressraums: Schneller
Kontextwechsel möglich
 Nachteil:
 Programmierung wird aufwändiger und Zugriff auf
Betriebsmittel muss koordiniert werden.

### Seite 16

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Benutzer vs Kernel Threads
Kernelthread Userethread
Vorteile • Ausnutzung von
mehr
Prozessorresourcen
möglich
• Ggf. mehr
Rechenzeit
• Sehr schneller
Kontextwechsel
Nachteile • Nur im
Supervisormode
möglich
• Blockierung eines
Threads führt zu
Blockierung des
ganzen Programms
• „Kein zusätzlicher
Rechenzeitanteil“ –
Die Zuteilung an den
User bleibt
unverändert

### Seite 17

Prozess
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Prozesse und Threads im Kontext
Globale und
statische Daten
Stack 1 Stack 2 Stack 3 Stack n
Thread 1 Thread 2 Thread 3 Thread n

### Seite 18

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Multithredding, -tasking, -processing
Multithreadding Multitasking Multiprocessing
Quasi-gleichzeitiges
Abarbeiten mehrer
Threads des selben
Prozesses
Quasi-gleichzeitiges
Abarbeiten mehrere
Prozesse
Echtes gleichzeitiges
Abarbeiten mehrere
Prozesse oder Threads
auf mehreren
Prozessoren (Kernen)
Zielsetzung: Optimale Ausnutzung der Ressourcen und schnellerer Ablauf
der Programme

### Seite 19

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssysteme -
Praxisteil
Ein bisschen Praxis … auf der Kommandozeile
Prozesse in Unix(Linux)
ps –eax
Priorität ändern: nice, renice
GUI: top, htop, glances, btop
Siehe man signal(2)
pstree
kill
…more to come 
Prozesse in Windows
TASKLIST
Priorität ändern: start … /B /WAIT
GUI: Taskmanager, Perfmon
Sysinternals: Processmon

### Seite 20

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssysteme -
Praxisteil
Visualisierungen
YouTube
Enlisch:
- CoreDumped – A Programm is not a Process  https://www.youtube.com/watch?v=7ge7u5V
USbE
- CoreDumped – Processes https://www.youtube.com/watch?v=7ge7u5VUSbE
- CoreDumped – Threads on a single core Processor  https://www.youtube.com/watch?v=M9
HHWFp84f0
- Core Dumped – Threads on Multicoresystems  https://www.youtube.com/watch?v=5sw9XJo
kAqw&list=PL9vTTBa7QaQPdvEuMTqS9McY-ieaweU8M&index=7
- CoreDumped – Concurrency   https://www.youtube.com/watch?v=3X93PnKRNUo
- Core Dumped – Scheduling   https://www.youtube.com/watch?v=O2tV9q6784k

### Seite 21

Betriebssysteme
Prozess- und Threadsynchronisation
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme

### Seite 22

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Prozesssynchronisation
 Zugriff auf Ressourcen muss koordiniert und wohldefiniert
ablaufen, insbesondere bei nebenläufigen Prozessen
 Programmabschnitte, in welchen es zu Konflikten kommen
kann, werden als kritische Abschnitte bezeichnet. Kritische
Abschnitte dürfen nur von einem Prozess zur gegebenen
Zeit  durchlaufen werden
 Lösung: Prozesse müssen sich gegenseitig ausschließen
(Mutex). Realisiert werden kann dies über „Locks“ oder
Semaphoren
 ABER: Gefahr von Deadlocks oder Race Conditions!

### Seite 23

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Verklemmungen (Deadlocks)
Definition: Eine Menge von Prozessen befindet sich in einem
Deadlock Zustand, wenn jeder Prozess aus der Menge auf ein
Ereignis wartet, das nur ein anderer Prozess aus der Menge
auslösen kann.
Verklemmungen können
auftreten aufgrund von:
 Mutual Exclusion
(Betriebsmittel nur unteilbar
benutzbar)
 Hold and Wait
(Betriebsmittel nur
schrittweise belegbar)
 No Preemption
(Betriebsmittel nicht
entziehbar)

### Seite 24

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Verklemmungen (Deadlocks) – weitere klassische
Probleme

### Seite 25

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Gruppenübung
Lösen des Verklemmungsproblems mittels Semaphore.
Gegeben:
Ein Waschraum, in diesen Waschraum passen 6 Personen. In
dem Waschraum befinden sich vier Toiletten, in jede Toilette
passt eine Person.
Stellen Sie sicher, das sich sowohl im Waschraum als auch in
den Toiletten nie mehr als die angegebene Personenzahl
befindet.

### Seite 26

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Gruppenübung
Lösen des Verklemmungsproblems mittels Semaphore.
SW=6
 SW - -
<- SW + +
ST=4
-> ST - -
<- ST ++ Toiletten
Max=
6
Max=
4
<- ST -- ; SW ++
 ST ++; SW –
 Does not
work!!

### Seite 27

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Workshop MOSS Deadlock Simulator
This document is a user guide for the MOSS Deadlock Simulator. It explains how to
use the simulator and describes the display and the various input files used by and
output files produced by the simulator. The MOSS software is designed for use wi
th Andrew S. Tanenbaum, Modern Operating Systems, 2nd Edition (Prentice Ha
ll, 2001). The Deadlock Simulator and this user guide were written by Ray Ontk
o  (rayo@ontko.com).
http://www.ontko.com/moss/deadlock/user_guide.html
Beispielcode
https://github.com/KR-Ravindra/Deadlock-Simulation
-> Mal selber ausprobieren, gerne auch in der Gruppe.
Präsentation der Ergebnisse dann in der nächsten Session.

### Seite 28

iu © 2023 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Race Conditions (Wettlaufsituation)
Race Conditions können auftreten, wenn nebenläufige Prozese
auf gemeinsame Daten zugreifen und mindestens einer davon
schreibend zugreift.
In diesem Fall ist das Ergebnis nicht vorhersagbar und kann
ggf. inkorrekt sein.

### Seite 29

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Race Conditions Workshops - Beispielcode
https://dextutor.com/program-to-simulate-race-condition/
https://www.educative.io/answers/how-to-simulate-a-race-con
dition-in-c
https://www.javatpoint.com/race-condition-in-java
Vertiefung:
https://jenkov.com/tutorials/java-concurrency/race-conditions-
and-critical-sections.html

### Seite 30

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssysteme -
Praxisteil
Visualisierungen
YouTube
Deutsch:
- Vfhcap eduloop – Racecondiitons  https://www.youtube.com/watch?v=dlOg4Dz-bgM
Betriebssysteme -
Visualisierung

### Seite 31

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Lösungsansätze für Synchronisationsprobleme
 Aktives Warten
 Mit Hardwareunterstützung
Unterbrechungssperre
Atomare Operation
 Mit Betriebssystemunterstützung
Semaphore
 Mit Sprachunterstützung
Monitore

### Seite 32

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Interprozesskommunikation
 Zusammenarbeit mehrere Prozesse
 Kommunikation zwischen Prozessen
 Via gemeinsamen Speicher (Hauptspeicher, Datei, etc.)
 Via Nachrichtenaustausch (Netzwerk, API Call, etc.)
synchron oder asynchron
Bsp. Unix: Signals, Pipes, Sockets, MessageQueues
Achtung: Mögliche Deadlocks bedenken!
Im System, auf einer
CPU
Im System, auf
mehreren CPUs
Über Systemgrenzen
hinweg
Zwischen Prozessen,
die zu
unterschiedlichen
Zeiten auf der CPU
laufen
Zwischen Prozessen,
die auf
unterschiedlichen
CPUs laufen
Zwischen Prozessen
auf verschiedenen
Systemen

### Seite 33

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssysteme -
Praxisteil
Visualisierungen
YouTube
Enlisch:
- CoreDumped – Inter Process Communication  https://www.youtube.com/watch?v=Y2mDw
W2pMv4
Betriebssysteme -
Visualisierung

### Seite 34

Betriebssysteme
Speicher
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme

### Seite 35

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Speicherverwaltung
 Adressmapping
 Logische Adressen auf physikalische
Adressen
 Seiten (Pages) auf Bereiche im
Hauptspeicher
 Belegungsstrategie
 In welcher Lücke soll Speicher reserviert
werden
 Minimierung von Fragmentierung
 Ersetzungsstrategie
 Welcher Speicherbereich kann sinnvoll
ausgelagert werden?
Betriebssystem
frei
Programm A
frei
Programm B
frei
Programm C
Programm D
Arbeitsspeich
er
?

### Seite 36

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Speicherverwaltung
Das Betriebssystem verwaltet neben der Zuteilung der CPU-Zeit
auch die Speicherbereiche im Hauptspeicher (Arbeitsspeicher, RAM).
 Jedem Prozess werden während der Ausführung Daten- und
Code-Bereiche im Hauptspeicher zugeteilt.
 Das Reservieren von Speicherbereich im Hauptspeicher durch
das Betriebssystem nennt man allokieren.
 Die Speicherbereiche eines Prozesses sind i. d. R. nicht
zusammenhängend sondern abschnittsweise im Hauptspeicher
verteilt.
 Die Speicherbereiche der (quasi-)gleichzeitig ablaufenden
Prozesse sind voneinander völlig eigenständig.
 Das Allokieren erfolgt mit dem Start des Programms und kann
ggf. auch während des Prozesses noch dynamisch angepasst
werden (allokieren von zusätzlichem Speicher, freigeben von
nicht mehr genutztem Speicher).

### Seite 37

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Speicherverwaltung - Belegungsstrategien
Durch das ständige Allokieren und Freigeben von
Speicherabschnitten entstehen ungenutzte Lücken im Speicher.
 Diesen Effekt nennt man Fragmentieren des Speichers.
 Das Betriebssystem versucht, durch eine optimierte
Speicherzuteilung diese Lücken möglichst zu vermeiden.
Folgende Verfahren sind möglich:
  First-Fit
  Next-Fit
  Best-Fit
  Worst-Fit
Es muss sichergestellt werden, dass andere Prozesse nicht auf den
Speicherbereich eines Prozesses (versehentlich) zugreifen können.
 Dieser Speicherschutz wird vom Betriebssystem in Verbindung
mit einer Hardware-Funktionalität (Grenzregister) der CPU
gewährleistet.

### Seite 38

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Speicheradressierung
Beim Adressieren von Speicherbereichen unterscheidet man zwischen:
Physischer Adresse:
 reale am Adressbus anliegende Adresse der Speicherzelle
Logischer Adresse:
 virtuelle auf den Startpunkt 0 bezogene Adresse, die mithilfe einer
Hardware-Einheit (MMU) in die physische Adresse umgerechnet
wird
Paging:
 Der virtuelle Adressraum wird in Seiten (pages) aufgeteilt, die jeweils
einem Bereich des physischen Adressraums entsprechen (Kachel).
 Mehrere Pages können der gleichen Kachel entsprechen, damit wird
der Adressraum virtuell vergrößert. Die aktuell nicht benötigten
Pages derselben Kachel sind zwischenzeitlich auf die Festplatte
ausgelagert.
Das Betriebssystem organisiert die Adressierung und die
Bereitstellung der Speicherbereiche und die entsprechende
Auslagerung nicht benötigter Speicherinhalte auf die Festplatte

### Seite 39

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssysteme -
Prasix
Ein bischen Praxis …
Speichergrößen - Beispiele
- 64 kB (z.B. C64), 128 kB (z.B. Microcontroler wie Arduino(ATMEL))
- 512 kB/640 kB (z.B. IBM PC/XT)
- 4 GB (Adressierbarer Hauptspeicher einer 32 Bit CPU – 2^32)
- 8 – 128 GB (realer Hauptspeicher heutiger Desktop Systeme mit einer 64 Bit CPU)
- 18 Millionen TB (möglicher Adressraum einer 64 Bit (CPU) – 2^64)
- Typischer Speicherausbau eine modernen Zweiprozessor-Serversystems: 2 – 8 TB
- Was noch: IBMs z13 mit 144 Kernen und 10 TByte RAM pro Rack https://www.golem.de/ne
ws/mainframe-ibms-z13-mit-144-kernen-und-10-tbyte-ram-pro-rack-1501-111686.html

### Seite 40

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssysteme -
Visualisierung
Visualisierungen
YouTube
Enlisch:
- CoreDumped – Stack  https://www.youtube.com/watch?v=N3o5yHYLviQ
- CoreDumped – Heap  https://www.youtube.com/watch?v=ioJkA7Mw2-U
- CoreDumped – Memory Access  https://www.youtube.com/watch?v=A9WLYbE0p-I

### Seite 41

Betriebssysteme
Speicherhirarchie
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme

### Seite 42

Steige
nde
Zugrif
fszeite
n
Steige
nde
Kapazi
tät
Fallen
de
Koste
n
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Speicherhirarchie
Register
Cache
Vordergrundspeic
her: RAM/ROM
Hintergrundspeicher:
HDD, SSD
Wechselspeicher: Band, DVD,
USB
Netzwerkspeicher lokal
Netzwerkspeicher Cloud
< 1ns
Wenige ns
Um die 60ns
Ssd: us, hdd:
ms
s

### Seite 43

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
A brief history…Festplatten
Die erste
Festplatte:
- IBM 1956
- 3,75 MB

### Seite 44

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
A brief history…Festplatten
8“

### Seite 45

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
A brief history…Festplatten…moderne Zeiten

### Seite 46

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Speicherverwaltung
Bilder:
Wikimedia
Logische Sicht (wird durch das Betriebssystem zur
Verfügung gestellt)
Physikalische
Sicht
Dateisysteme: Dauerhafte
Speicherung (großer)
Datenmengen

### Seite 47

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Speicherverwaltung

### Seite 48

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Betriebssyste
me
Speicherverwaltung
Übersicht über eine Reihe wichtiger Dateisysteme:
https://www.ufsexplorer.com/articles/file-systems-basics/
https://de.wikipedia.org/wiki/Liste_von_Dateisystemen
https://en.wikipedia.org/wiki/Comparison_of_file_systems
https://openbook.rheinwerk-verlag.de/linux/linux_kap28_002.html
https://de.wikibooks.org/wiki/Disk-Forensik/_Beweismittelquellen/_Grundlagen_der_Da
teisysteme
https://www.sblab.de/assets/lectureFS2018.script.pdf
https://www.kingston.com/de/blog/personal-storage/understanding-file-systems

### Seite 49

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Speicherverwaltung…and beyond
Betriebssysteme -
Prasix
Linux
Ls
Cd
Chown
Chmo
d
Tree
Df
Du
Dolphi
n
Mc
Windo
ws
Dir
Cd
Mkdir
Copy
Move
Del
Fc
Rename
attrib
Explorer
MacO
S
Finde
r
Tools
Gparted
Clonezilla
Knoppix
Systemrescue
Ultimate Boot
CD
Finnix
Grml
Ventoy

### Seite 50

Betriebssysteme
Zusammenfassung/Ausklang
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme

*... weitere 4 Seiten nicht angezeigt*
