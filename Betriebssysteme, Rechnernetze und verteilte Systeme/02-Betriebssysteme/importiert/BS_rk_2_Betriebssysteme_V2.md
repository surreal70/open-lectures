---
author: Andreas Hümmer
title: "Grosser"
tags:
  - content
  - importiert
  - bs
created: '2026-10-07'
modified: '2026-10-07'
bereich: BS
typ: sonstig
quelle: "BS_rk_2_Betriebssysteme_V2.pdf"
seiten: 46
---
author: Andreas Hümmer

# Grosser

> [!info] Dokumentinformationen
> - **Quelle:** BS_rk_2_Betriebssysteme_V2.pdf
> - **Typ:** sonstig
> - **Bereich:** BS
> - **Seiten:** 46
> - **Autor:** Kloos, Reinhold, Dr.

---
author: Andreas Hümmer

## Inhalt

### Seite 1

Prof. Dr. Reinhold Kloos
BETRIEBSSYSTEME, RECHNERNETZE
UND VERTEILTE SYSTEME
2-VERBREITETE BETRIEBSSYSTEME
Duales Studium
Nord-Ost Virtueller Campus

### Seite 2

THEMENLANDKARTE
Grundlagen der Betriebssysteme
Verbreitete Betriebssysteme
Dateisysteme und Prozesse
Rechnernetze & TCP/IP und Internet
Architekturen verteilter Systeme
Mobile Computing
1
4
5
6
2
3

### Seite 3

ZWEITE KURSEINHEIT
VERBREITETE BETRIEBSSYSTEME
02

### Seite 4

LERNZIELE
− Geräte, die ein Betriebssystem benötigen
− Liste der verschiedenen Betriebssysteme
− Motivation für die unterschiedlichen Betriebssysteme
− Prinzipielle Unterscheidung der verschiedenen
Betriebssysteme
− Fallstudien zu ausgewählten Betriebssystemen

### Seite 5

EINFACH ERKLÄREN
1. Nennen Sie die grobe Unterteilung der
Einsatzgebiete für ein Betriebssystem. Geben Sie für
die Einsatzgebiete Beispiele an.
2. Inwieweit unterscheiden bzw. gleichen sich die
Betriebssysteme Unix und Linux?
3. Welche Windows-Version ist MS-DOS-basiert?

### Seite 6

GESCHICHTE
Rechnergenerationen:
1. Generation (1945-1960): Röhrenrechner
2. Generation (1960-1970): Transistorrechner
3. Generation (1970-1980): Mikrorechner mit niedrigem
Integrationsgrad
4. Generation (1980-1995): Mikrorechner mit hohen
Integrationsgrad
4.5 Generation (bis heute): Mehrkernsysteme
5. Generation (?): Intelligente Prozessoren

### Seite 7

1. GENERATION (1945-1960)
H. Aiken (Harvard), J. v. Neumann (Princeton) u.a. (USA)
Konrad Zuse (Deutschland)
− Entwurf, Bau, Programmierung, Betrieb und Wartung eines Systems durch
Expertengruppe
− Programmierung durch Verdrahtung, Steckkontakte, Steckkarten, keine höheren
Programmiersprachen
− Nutzung für Anwendungen der numerischen Mathematik
− Ab Anfang der 50er Jahre Einlesen per Lochkarten
− Betriebssysteme unbekannt

### Seite 8

2. GENERATION (1960-1970)
− Nach Einführung von Transistoren wurden Rechner zuverlässiger, Vetrieb wurde
möglich.
− Unterscheidung zwischen Entwicklern, Herstellern, Operateuren, Programmierern und
Wartungspersonal.
− Zunächst Ausführung einzelner Jobs in Form von Lochkartenstapeln mit hohem Anteil
an manuellen Arbeiten.
− Rationalisierung durch Einführung des Stapelbetriebs (Batch-System), in dem
mehrere ähnliche Jobs gruppiert und abgearbeitet wurden.

### Seite 9

2. GENERATION (1960-1970) - BATCHSYSTEME
− Nutzten oft höhere Programmiersprachen wie FORTRAN.
− Jobs wurden nach Art der verwendeten Programmiersprache gruppiert.
− Anwender geben Lochkartenstapel mit auszuführendem Programm an
(menschlichen) Operator. Dieser gruppiert die Jobs und startet den Einlesevorgang.
− Ein fest installiertes Programm, der Resident Monitor, steuert die Ausführung des
Jobstapels.
Vorläufer heutiger Betriebssysteme!
Batch-System (Beispiel)
− IBM 7094 als Hauptrechner, IBM 1401 für Ein- und Ausgabe
− Eingabe per Lochkarten, Transfer auf Magnetband
− Später ersetzt durch direktgekoppeltes System 7094/7044

### Seite 10

2. GENERATION (1960-1970) - BATCHSYSTEME
Eigene Kommandosprache (Job Control Language) zur
Beschreibung und Steuerung eines einzelnen Jobs
Vorläufer heutiger Kommandozeileninterpreter

### Seite 11

3. GENERATION (1970-1980)
− Sequentielle Jobausführung ineffizient, sobald Ein-/Ausgabeoperationen durchgeführt
werden
− Lösung: Mehrere Jobs parallel im Speicher vorhalten. Sobald einer dieser Jobs auf
Ein-/Ausgabe wartet, wird der nächste Job bedient (Multiprogramming/ Multitasking).
− Betriebssystem organisert unter anderem
− Umschaltung zwischen den Jobs
− Speicherzuteilung
Job 2
Job 1
Job 3
Betriebs-
system
Speicher-
organisation

### Seite 12

4. GENERATION (1980 – 1990)
−Vom Mainzframe zum Personal Computer
−Lokale Netzwerke zur Kommunikation und Kooperation
−Graphische Ein-/Ausgabe führt zu bedienfreundlicheren Benutzerschnittstellen
Mit diesen Möglichkeiten wächst auch der Aufgabenbereich von Betriebssystemen
stetig

### Seite 13

4.5 GENERATION (BIS HEUTE)
Steigende Komplexität und neue Funktionalitäten:
− Verteiltheit (Client/Server),
− Heterogenität,
− Skalierbarkeit
− Mehrkernsysteme,
− Sicherheit (Datenschutz, Integrität)
− Fehlertoleranz / Robustheit
− Multimedia
Aktuelle Entwicklungsrichtungen:
− Verteilte Betriebssysteme
− Massives Multiprocessing
− Standardisierung von Schnittstellen
− Virtualisierung
− Konfigurierbarkeit
− Sicherheit

### Seite 14

KLASSIFIKATION NACH AUFGABEN
(Beispielbetriebssysteme in Klammern)
− Mainzframe-Betriebssysteme (OS2200)
− Server-Betriebssysteme (SCO OpenServer)
− Endanwender-Betriebssysteme (Windows 8-11)
− Smartphone-Betriebssysteme (Android)
− Echtzeit-Betriebssysteme (IOS)1
− Betriebssysteme für eingebettete Systeme (Nucleus)
− Chipkartenbetriebssysteme (TCOS)
1) Internet Operating System von Cisco, nicht zu verwechseln mit iOS von Apple

### Seite 15

Auf welchen Geräten ist ein Betriebssystem erforderlich?
Da das Betriebssystem die Schnittstelle zwischen Hardware und Anwender-Software bildet, benötigen alle
Geräte, auf denen variierende Anwender-Software laufen soll, ein Betriebssystem.
Beispiele für Geräte mit einem Betriebssystem:
− Server, Großrechner
− Desktop-PC, Laptop
− Smartphone, Tablet
− Spielcomputer, Navigationssysteme
− Eingebettete Systeme (embedded system) in Haushaltsgeräten, Unterhaltungselektronik,
Fahrzeugtechnik, Medizintechnik, Routern etc.
VERBREITETEBETRIEBSSYSTEME

### Seite 16

EINTEILUNGSKRITERIEN DER VERSCHIEDENEN BETRIEBSSYSTEME
Herstellerfirma
Einsatzgebiet (Gerätetechnik)
Komplexität und technische Anforderungen
Prinzipieller Aufbau des Kernels
Generell hat das Betriebssystem die Aufgabe, die Computer-Hardware
zu abstrahieren und für die Interaktion mit der Hardware
entsprechende Systemfunktionen zur Verfügung zu stellen.

### Seite 17

Verbreitete Hersteller für Betriebssysteme sind:
− Microsoft
− Apple
− AT&T
− SUN Microsystems (heute Oracle)
− Google
− Huawei
Betriebssysteme werden aber auch als Freeware bereitgestellt.
EINTEILUNGSKRITERIEN DER VERSCHIEDENEN BETRIEBSSYSTEME
Herstellerfirma

### Seite 18

Grob lassen sich die Einsatzgebiete in vier Kategorien einteilen:
Die Komplexität und die Anforderung an die Systemfunktionen unterscheidet sich je nach Einsatzgebiet.
Auch die Ansprüche an Ressourcenverwaltung und Sicherheit sind unterschiedlich.
EINTEILUNGSKRITERIEN DER VERSCHIEDENEN BETRIEBSSYSTEME
Großrechner,
Server
Personal-
Computer
Mobile Geräte, wie
z. B. Smartphones
Eingebettete
Systeme
Einsatzgebiet (Gerätetechnik)

### Seite 19

Mögliche technische Anforderungen können sein:
− Echtzeitfähigkeit
− 16-Bit-/32-Bit-/64-Bit-Verarbeitungsbreite
− Multitasking-Unterstützung
− Graphische Benutzerschnittstelle (GUI)
− Unterstützte Dateisysteme (z. B. NTFS, FAT, VFAT)
− Vielfalt der Hardware-Treiber
− Schnittstelle für Anwenderprogrammierung
− Sicherheitskonzepte
EINTEILUNGSKRITERIEN DER VERSCHIEDENEN BETRIEBSSYSTEME
Komplexität und technische Anforderungen

### Seite 20

Einige wichtige Kernels:
− Windows-NT-Kernel
− Linux-Kernel
− XNU-Kernel (Darwin)
− Minix-Kernel
EINTEILUNGSKRITERIEN DER VERSCHIEDENEN BETRIEBSSYSTEME
Der Kernel ist das Kernstück des Betriebssystems, das die
unmittelbare Schnittstelle zur Hardware darstellt.
Er ist für die Prozess- und Speicherverwaltung verantwortlich.
Prinzipieller Aufbau des Kernels

### Seite 21

− Windows
− Unix
− Sun OS (Solaris)
− Linux
− Android
− Mac OS
− iOS
− Fuchsia OS
− Harmony OS
AUFLISTUNG VERBREITETER BETRIEBSSYSTEME
Übung:
Ermitteln Sie zu den aufgeführten Betriebssystemen die
Hersteller und auf welchen Systemen sie vorrangig zum
Einsatz kommen.

### Seite 22

SCHICHTENMODELL
Benutzer
Anwendung
Betriebssystem
Hardware
User 1 User 2 User 3
Browser D3 Textverarbeitung…
Betriebssystem
Hardware

### Seite 23

ABSTRAKTION
Schnittstelle zu einem Gerät wird durch sogenannten Gerätetreiber als Teil des Betriebssystems bereitgestellt. Dieser kennt
die interne Implementierung des Gerätes.
Abstraktionsstufen:
− Logisches Gerät – Schnittstellenrepräsentation eines realen (dinglichen) Gerätes. Kommunikation über Gerätetreiber
− Virtuelles Gerät – Abstrakte Schnittstellenrepräsentation einer Funktionalität, unabhängig davon, ob diese dinglich oder
virtuell implementiert ist. Kommunikation über Softwareschnittstelle.

### Seite 24

PROZESSE
− Ein Prozess ist ein eindeutig identifizierbarer Ablauf eines Programms, d.h. ein Programm in Ausführung mit allen
dazu notwendigen Daten.
− Der Prozessor (engl.: Central Processing Unit, CPU) führt die Anweisungen eines Prozesses nacheinander aus. Er
kann aus mehreren Kernen bestehen, je Kern kann genau ein Prozess ausgeführt werden.
Prozesse können selbst neue Prozesse erzeugen (Kindprozesse).
Beim Start des Betriebssystems existiert nur ein einziger Prozess
(root process).
Dieser erzeugt schrittweise Kindprozesse, die wiederum
selbst Kindprozesse erzeugen können, es entsteht ein Prozessbaum*).
*) Windows kennt keine solche Prozesshierarchie

### Seite 25

KERNEL
− Die zentralen Komponenten des Betriebssystems werden als Betriebssystemkern (engl.: Kernel) bezeichnet.
− Die Aufgaben des Kerns umfassen im Wesentlichen:
− Direkte Kommunikation mit der Hardware (durch Gerätetreiber)
− Reihenfolgeplanung der Ausführung (Scheduling) und Umschalten (Dispatching) von Prozessen
− Speicherverwaltung
Die Verwendung von Betriebssystemen kann durch die Architektur des Rechners unterstützt werden.
So bietet bspw. die CPU verschiedene Priviligierungsstufen für laufende Prozesse. Mindestens sind
dies
− Kernelmodus (kernel mode, system mode): Modus mit Zugriff auf priviligierte Befehle, reserviert für
die Kernelkomponenten des Betriebssystems.
− Benutzermodus (user mode): Gilt für alle anderen Prozesse. Ihnen steht nur ein eingeschränkter
Befehlssatz zur Verfügung.

### Seite 26

PRIVILIGIERUNGSSTUFEN: BEISPIEL X86 ARCHITEKTUR
X86-kompatible CPUs (also faktisch alle gängigen PCs) besitzen insgesamt 4 Priviligierungsstufen
(Ring 0 bis 3) mit absteigendem Umfang des verfügbaren Befehlssatzes.
Kernel-
modus
Ring 0
Ring 1
Ring 2
Ring 3
Benutzer-
modus
Ring 0 entspricht dem Kernel-modus
(supervisor mode, voller Befehlssatz),
Ring 1-3 sind dem Benutzermodus zugeordnet.
In der Praxis werden Ring 1 und 2 selten genutzt
(Ausnahme: Virtualisierung).

### Seite 27

WINDOWS
− Hersteller: Microsoft
− Entwicklungsgeschichte: seit 1985 noch als MS-DOS, bis heute als WINDOWS 10
− Es kommt vorrangig auf Personal-Computern zum Einsatz, aber auch auf Servern,
Smartphones und eingebetteten Systemen.
− Es ist kein Echtzeitbetriebssystem.
− Seine Stärken sind die große Verbreitung, die vielseitige Abdeckung umfang-reicher
Hardware und die hohe Nutzerflexibilität.
− Die Einführung des NT-Kernel und des Modern UI als neue Oberfläche begründen
jeweils eine neue Epoche des Betriebssystems.

### Seite 28

ENTWICKLUNGSGESCHICHTE VON WINDOWS
1985
MS-DOS, Windows
1.0-3.11
MS-DOS
− Später mit
graphischer
Oberfläche
− 16-Bit-Architektur
− Unterstützt später
auch TCP/IP
(Internetprotokoll)
1995
Windows 95, 98,
ME
Epoche 1
− MS-DOS basierend
und mit graphischer
Oberfläche
− 32-Bit-Architektur
− Unterstützt jetzt
präemptives
Multitasking
− Jetzt mit Internet
Explorer
1993
Windows NT, XP,
2000, Vista, 7
Epoche 2
− NT-Kernel
− 64-Bit-Architektur
− Jetzt auch für
verschiedene
Prozessor-
Architekturen
2012
Windows 8, 10
Epoche 3
− Modern UI als neue
graphische
Oberfläche
− Ein einheitliches
Betriebssystem
deckt jetzt alle
Hardware-
Plattformen in
gleicher Weise ab

### Seite 29

WICHTIGE MEILENSTEINE BEI DER ENTWICKLUNG VON WINDOWS
−MS-DOS als Betriebssystem:
− einfaches Einzelnutzer-Betriebssystem mit 16-Bit-Adressraum
− Läuft auf Intel 8088Prozessor
− Textbasierter Kommandozeilen-Interpreter
−MS-DOS-basiertes Windows:
− Textbasierter Kommandozeilen-Interpreter wird durch eine graphische Oberfläche ersetzt
−NT-basiertes Windows:
− NT-Kernel ermöglicht Speicherschutz
− Einführung eines neuen Dateisystems NTFS
−Windows Modern UI:
− Neue Oberfläche, die für alle Hardware-Plattformen einheitlich ist

### Seite 30

STRUKTUR DES WINDOWS-NT-KERNELS
−Die Struktur des NT-Kernel besteht aus
verschiedenen Schichten:
− Der HAL ermöglicht die Kompatibilität zu
den unterschiedlichen Plattformen.
− Die Programmierschnittstelle Win32API
bietet einen standardisierten Zugang zu
den Systemaufrufen.
Quelle Abbildung: in Anlehnung an Tanenbaum & Bos, 2016, S. 1043. HARDWARE
Ausnahme- und Interrupt-Behandlung
CPU-Verwaltung
Programmier-Schnittstelle
Systembibliotheken
Prozess-
Verwaltung
Speicher-
Verwaltung
Ein-/Ausgabe-Manager
Hardware Abstraction Layer (HAL)
Geräte-Treiber:
− E/A-Geräte
− Dateisystem
− Netzwerke
− TCP/IP (Internet)

### Seite 31

WINDOWS-DATEISYSTEME
FAT32
(File Allocation Table)
− Für Mobile Speichermedien
(USB-Stick, mobile
Festplatten etc.)
− Nachteil: Es sind (aus heutiger
Sicht) nur verhältnismäßig
geringe Dateigrößen (max. 4
Gibibyte) und kleine
Datenträger (max. 2 Tebibyte)
möglich.
NFTS
(New Technology File System)
− Proprietäres Dateisystem von
Microsoft
− Führ sehr große Dateien (max.
16 Tebibyte) und große
Datenträger (max. 256
Tebibyte) geeignet

### Seite 32

UNIX
− Hersteller: Telefongesellschaft AT&T
− Entwicklungsgeschichte:
− Bereits 1969 begann die Entwicklung von Unix.
− Bis 1980 wurde Unix komplett quellenoffen (open source) entwickelt.
− Eigens für die Programmierung von Unix wurde die Programmiersprache C entwickelt.
− Ursprünglich wurde Unix hauptsächlich für Workstations und Server eingesetzt,
inzwischen auch auf vielen anderen Plattformen, wie Personal Computer, Webserver
etc.
− Aufgrund der anfänglichen Open-Source-Entwicklung gibt es inzwischen viele Unix-
Derivate (z. B. die BSD-Systeme, HP-UX (Hewlett-Packard), DG/UX (Data General), AIX
(IBM), IRIX (Silicon Graphics), Solaris (Oracle), macOS (Apple))

### Seite 33

LINUX
−Entwicklungsgeschichte:
− 1987 entwickelte Andrew S. Tanenbaum ein Lehr-Betriebssystem MINIX
− 1991 entwickelte Linus Torvalds einen zu MINIX kompatiblen Kernel, den er als Freie Software (GNU General
Public License) veröffentlichte und Linux nannte
− Linux basiert nicht auf dem ursprünglichen Unix-Quelltext, sondern wurden separat entwickelt.
− Es wird als „unixoides System“ bezeichnet, weil es ausgewählte, für Unix standardisierte
Betriebssystemfunktionen (POSIX) bereitstellt.
− Linux kommt vorrangig auf Servern zum Einsatz, spielt aber eine zunehmende Rolle bei Laptops,
Desktops, mobilen Geräten und eingebetteten Systemen.
− Es kommen sogenannte Linux-Distributionen zum Einsatz. Sie bilden aus dem Linux-Kernel und
anwendungsspezifischer Software ein eigenes Betriebssystem. Ein Beispiel hierfür ist UBUNTU.

### Seite 34

LINUX-MERKMALE
−Programmierschnittstelle:
Die standardisierten Programmierschnittstelle für unixoide Betriebssysteme ist POSIX.
Die Standardisierung dieser Schnittstelle erlaubt eine hohe Kompatibilität für Anwenderprogramme bei
verschiedenen unixoiden Systemen.
−Dateisysteme:
Ein wichtiges Konzept aller unixoiden Betriebssysteme ist, dass alle Hardware-Ressourcen dem Benutzer
abstrahiert in Form einer Datei im Verzeichnis /dev präsentiert wird (Everything-is-a-file-Paradigma).
−Unterstützte Dateisysteme sind:
− FAT32 (USB-Sticks)
− I-Node (Festplatten)
− ext2/ext3
− HFS+
− APFS

### Seite 35

MOBILE BETRIEBSSYSTEME
− Mobile Betriebssysteme sind
speziell für mobile Geräte wie
Smartphone, Tablet, PDA,
Smartwatch etc.
− Mobile Betriebssysteme
haben als Zusatzfunktion,
dass sie die Verbindung zum
Mobilfunk- und Datennetz
sowie den Zugriff auf das
Telefon verwalten.
Wichtige mobile
Betriebssysteme
− Android
(Google)
− iOS
(Apple)
− Windows Phone
(Microsoft)
− Blackberry
(Research in Motion)
Weitere mobile
Betriebssysteme
− Sailfish OS
(Jolla)
− Tizen
(Intel und Samsung)
− Ubuntu
(Canonical)
− Firefox OS
(Mozilla)
− Symbian OS
(Symbian Foundation)
− WebOS (LG)

### Seite 36

ANDROID
− Hersteller:
Android wurde von der Open Handset Alliance (OHA) entwickelt. Dahinter stehen
Firmen wie z. B. HTC, Motorola, Samsung, T-Mobile, Vodafone und vor allem Google.
− Es kommt auf Smartphones zum Einsatz, aber auch auf Smartwatches.
− Android basiert auf dem Linux-Kernel.
− Die Benutzeroberfläche unterstützt die Fingerbedienung über einen Touchscreen.
− Als Schnittstelle für die Anwenderprogramme (App) stellt Android eine Java
unterstützende virtuelle Maschine (Android Runtime) bereit.
− Android ist zurzeit das meistgenutzte Betriebssystem auf Smartphones und
Smartwatches.

### Seite 37

Folgende Inhalte wurden besprochen:
ZUSAMMENFASSUNG
Betriebssysteme kommen auf
vielen verschiedenen
Geräten unterschiedlichster
Komplexität zum Einsatz.
Die Betriebssysteme
unterscheiden sich vor allem
aufgrund ihrer unterschiedlichen
Einsatzgebiete.
Die Entwicklungsgeschichte der
Betriebssysteme
begleitet die Weiterentwicklung
der Hardware und
Systemanforderungen.
Das Kernstück eines
Betriebssystems ist der
sogenannte Kernel, der vor allem
die Hardware-Abstraktions-
schicht, die Prozess- und
Speicherverwaltung und die
Gerätetreiber realisiert.
Als Fallstudien wurden die
Betriebssysteme Windows, Unix,
Linux und Android betrachtet.

### Seite 38

REVIEW LERNZIELE
− Geräte, die ein Betriebssystem benötigen
− Liste der verschiedenen Betriebssysteme
− Motivation für die unterschiedlichen Betriebssysteme
− Prinzipielle Unterscheidung der verschiedenen
Betriebssysteme
− Fallstudien zu ausgewählten Betriebssystemen

### Seite 39

TRANSFERAUFGABE
EINHEIT 2

### Seite 40

Informieren Sie sich über das neue
Betriebssystem Harmony OS und
beschreiben Sie seine
wesentlichen Eigenschaften.
Gehen Sie auch auf die
Markteinführungsstrategie des
Herstellers ein.
TRANSFERAUFGABE
− Quelle Bild: 200degrees/1995434/Pixabay.

### Seite 41

TRANSFERAUFGABE
PRÄSENTATION DER ERGEBNISSE
Bitte stellen Sie Ihre
Ergebnisse vor.
Im Plenum werden
die Ergebnisse
diskutiert.

### Seite 42

LERNKONTROLLFRAGEN
1. Was versteht man unter dem Kernel eines
Betriebssystems? Welche Hauptaufgaben erfüllt er?
2. Nennen Sie drei wesentliche Meilensteine der
Windows-Entwicklung.
3. Nennen Sie dir vier wichtigsten mobilen
Betriebssysteme.

### Seite 43

EINFACH ERKLÄREN
1. Nennen Sie die grobe Unterteilung der
Einsatzgebiete für ein Betriebssystem. Geben Sie für
die Einsatzgebiete Beispiele an.
2. Inwieweit unterscheiden bzw. gleichen sich die
Betriebssysteme Unix und Linux?
3. Welche Windows-Version ist MS-DOS-basiert?

### Seite 44

QUELLENVERZEICHNIS
Tanenbaum, A. S. & Bos, H. (2016). Moderne Betriebssysteme. 4. Auflage, Pearson Deutschland, Hallbergmoos.

### Seite 45

© 2025 IU Internationale Hochschule GmbH
Diese Inhalte sind urheberrechtlich geschützt. Alle Rechte vorbehalten.
Diese Inhalte dürfen in jeglicher Form ohne vorherige schriftliche Genehmigung der IU Internationale
Hochschule GmbH nicht reproduziert und/oder unter Verwendung elektronischer Systeme verarbeitet,
vervielfältigt oder verbreitet werden.

### Seite 46

Prof. Dr. Reinhold Kloos
Reinhold.Kloos@iu.org
DANKE
WIE HAT DER KURS GEFALLEN?
