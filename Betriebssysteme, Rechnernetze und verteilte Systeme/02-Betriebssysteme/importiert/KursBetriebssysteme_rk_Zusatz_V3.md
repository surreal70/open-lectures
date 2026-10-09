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
quelle: "KursBetriebssysteme_rk_Zusatz_V3.pdf"
seiten: 32
---
author: Andreas Hümmer

# Grosser

> [!info] Dokumentinformationen
> - **Quelle:** KursBetriebssysteme_rk_Zusatz_V3.pdf
> - **Typ:** sonstig
> - **Bereich:** BS
> - **Seiten:** 32
> - **Autor:** Kloos, Reinhold, Dr.

---
author: Andreas Hümmer

## Inhalt

### Seite 1

Prof. Dr. Reinhold Kloos
BETRIEBSSYSTEME, RECHNERNETZE
UND VERTEILTE SYSTEME
ZUSATZ
ZusatzmaterialienDuales Studium
Köln, Virtuell

### Seite 2

ALLES AUF DEM RECHNER SIND DATEN, CODE – FORMALE SPRACHEN
13.11.2023
Beispiel: Gesucht ist ein Codewort zur Erfassung eines Graphen
Alphabet Σ (endliche Menge an Zeichen) für den Code: Σ = 0,1,2,3,4,5,6,7,8,9, #
➢ Code mit Auflistung der Kanten (z.B. Codewort für gewichtete Kante (1,2): 1#2#w(1,2), Kantentrennung: ##):
➢ Code mit Adjazenzliste (z.B. Liste für einen Knoten:                                                                                                Aubau generell:                                                  ):
➢ Code mit Adjazenzmatrix (𝐴 = 𝑎𝑖𝑗 , 𝑎𝑖𝑗 =0 𝑠𝑜𝑛𝑠𝑡
𝑤 𝑖,𝑗  falls 𝑖,𝑗  Kante im Graph , Zeilentrennung: ##):
In der Theorie: Das Code-/Datenwort kommt aus einer formalen Sprache, die
regelt, wie aus Zeichen/Symbole eines Alphabets mit festen Regeln Worte
zusammengestellt werden, die also eine bestimmte Syntax haben. Wegen des
festen Aufbaus kann man den Worten eine Semantik zuordnen, umso
Informationen zu erfassen.
Es werden hier drei Worte vorgestellt, die mit unterschiedlicher Syntax gebildet
sind, aber semantisch jeweils den Graphen als Information erfassen.

### Seite 3

MAßEINHEITEN FÜR SPEICHERGRÖßEN           1 BYTE = 8 BITS (1 BIT ≙ 0/1)
Dezimalpräfixe Unterschied
gerundet

Binärpräfixe gemäß IEC
Name Symbol Anzahl Bytes Name Symbol Anzahl Bytes
Kilobyte kB 1 000 = 103 2,4 % Kibibyte KiB 1 024 = 210
Megabyte MB 1 000 000 = 106 4,9 % Mebibyte MiB 1 048 576 = 220
Gigabyte GB 1 000 000 000 = 109 7,4 % Gibibyte GiB 1 073 741 824 = 230
Terabyte TB 1 000 000 000 000 = 1012 10,0 % Tebibyte TiB 1 099 511 627 776 = 240
Petabyte PB 1 000 000 000 000 000 = 1015 12,6 % Pebibyte PiB 1 125 899 906 842 624 = 250
Exabyte EB 1 000 000 000 000 000 000 = 1018 15,3 % Exbibyte EiB 1 152 921 504 606 846 976 = 260
Zettabyte ZB 1 000 000 000 000 000 000 000 = 10 21 18,1 % Zebibyte ZiB 1 180 591 620 717 411 303 424 = 2 70
Yottabyte YB 1 000 000 000 000 000 000 000 000 = 10 24 20,9 % Yobibyte YiB 1 208 925 819 614 629 174 706 176 = 2 80
16./31.10.2023
Der Rechner kennt im kleinsten nur zwei Zustände, nämlich digital an/aus oder 0/1, mit denen man zwei Informationen erfassen kann.
Das ist die kleinste Informationseinheit, die als Bit bezeichnet wird. Sie kann mit einem Zeichen aus einem Alphabet mit zwei Zeichen
dargestellt werden. Mit 8 Zeichen über einem solchen Alphabet kann ich bis zu 28 = 256 Informationen als Byte mit Datenworten
erfassen, z.B. die Dualzahlen von 0 bis 255. Die folgende Tabelle erfasst Informationseinheiten für bis zu 60 Bits.

### Seite 4

ZAHLEN MIT STELLENWERTSYSTEM
Umrechnung
Z.B.: 19110 in Dualzahl umrechnen:
Reste von unten nach oben
abgelesen ergibt:
19110 = 101111112
16./31.10.2023
101011112 = 2578
Schnelle Umwandlung zwischen
Dualzahl und Oktalzahl bzw.
Hexadezimalzahl
101011112= 𝐴𝐹16
Umwandlung von 0,62510:
notiert von oben nach unten:
0,62510 = 0,1012
63 − 37:
00111111
+ 11011011
00011010
= 26
n-stellige Zahl: 𝑎𝑛−1 … 𝑎1𝑎0 = 𝑎𝑛−1 ∙ 𝑏𝑛−1 ⋯ 𝑎1 ∙ 𝑏1 + 𝑎0 ∙ 𝑏0 = σ𝑖=0
𝑛−1 𝑎𝑖 ∙ 𝑏𝑖, mit 𝑏 als Basis
Zahl mit Vorzeichen bei einem 8-Bit-Wort
(Das MSB ist Vorzeichen):

### Seite 5

GANZZAHLFORMATE ALS DUALZAHL UND ZEICHENCODIERUNG
19110 = 101111112
25.03.2024
−6510= 101111112
Zweierkomplement
Invertierung: 010000002
+  12
6510 = 01000001
66 – 65: (Mit einem Byte als Formatgröße)
01000010
+ 10111111
= 00000001
(Mit einem Byte als Formatgröße)

### Seite 6

IEEE 754 STANDARD FÜR GLEITKOMMAZAHLEN
− Darstellung von Gleitkommazahlen:
𝑥 = (−1)𝑠∙ 𝑚 ∙ 2𝐸 = −1 𝑠 ∙ 1, 𝑓 ∙ 2𝑒−𝑏
− Normierte Mantisse 𝑚 = 1, 𝑓
− Exponent wird dargestellt als 𝐸 = 𝑒 − 𝑏 (Exzessdarstellung)
− Biaswert 𝑏 = 2𝑝−1 − 1
− Einfache Genauigkeit (32 Bit: n = 32, p = 8, k = 23):  𝑏 = 127
− Doppelte Genauigkeit (64 Bit: n = 64, p = 11, k = 52): 𝑏 = 1023
16./31.10.2023
z.B.: 11000000011000100111100000000000
Negative Zahl: 𝑠 = 1
Mantisse: 𝑚 = 1,110001001111 2
Exponent in Exzessdarstellung:
Charakteristik: 𝑒 = 10000000 2 = 27 = 12810
Exponent: E = 𝑒 − 𝑏 = 128 − 127 = 1
−1 ∙ 1,110001001111 2 ∙ 21
= − 11,10001001111 2 = −3,5385742188

### Seite 7

SCHALTNETZ UND SCHALTWERK
16./31.10.2023
Schaltnetz
⋮
𝐸1
𝐸2
𝐸𝑛
𝐴1
𝐴2
𝐴𝑚
⋮
Welche Ausgangswerte ergeben
sich bei welchen
Eingabewerten?
z.B. Schaltnetz für die Addition oder:
Rechenoperationen kann
man mit Schaltnetzen mit
logischen Gattern realisieren.
Mit Flipflops erhält man
Speicherelemente erweitert
man Schaltnetze zu
Schaltwerken. Ein Register
besteht aus Flipflops.
So kann man Zustände
festhalten, die sich (ggf.)
taktgesteuert verändern.
Schaltwerk
(Schaltnetz plus Zustandsspeicherung)
⋮
Mit
Zustand
𝐸1
𝐸2
𝐸𝑛
𝐴1
𝐴2
𝐴𝑚
⋮
Welche Ausgangswerte ergeben
sich bei welchen Eingabewerten
und den Zustand?
z.B. Addierwerk der ALU

### Seite 8

SCHALTUNGSUMFORMUNGEN UND RECHENSCHALTUNGEN
− BCD-Dezimal (getrennte Umsetzer für beide Richtungen)
Umsetzung von den Dezimalziffer 0-9 zu den BCD-Code-Stellen 𝐵3 𝐵2 𝐵1 𝐵0
− 7-Segment Codeumsetzer
− Paritychecker für 8 stellige Dualzahl 𝐵7 𝐵6 𝐵5 𝐵4 𝐵3 𝐵2 𝐵1 𝐵0
− Multiplexer und Demultiplexer (Datenselektoren)
Parallele Datenströme zu einem seriellen – Serieller Datenstrom zu parallelen
− Addierer
Halbaddierer (𝐴 + 𝐵 → (𝑍, 𝐶𝑂𝑢𝑡)) und
Volladdierer (𝐴 + 𝐵 + 𝐶𝐼𝑛 → (𝑍, 𝐶𝑂𝑢𝑡)) )
− Carry-Ripple-Addierer
− Und weitere …
25.03.2024

### Seite 9

VON-NEUMANN-RECHNERARCHITEKTUR - SPEICHERHIERARCHIE
16./31.10.2023
CISC- und RISC-
Prozessoren

### Seite 10

BITOPERATIONEN IN EINER ASSEMBLER-SPRACHE
Einen Rechner kann man programmieren (Programmcode) – Hardware-nah mit einer Assembler-Sprache
Im Kurs wurde die Assembler-Sprache für einen Mips-Prozessor (Simulation mit Mars) angesprochen
− Invertierung einer Dualzahl
Zur Bildung eines Zweierkomplements braucht man die Invertierung einer Dualzahl.
Dafür gibt es Hardware-Bausteine man kann aber auch eine bitweise Logik-Operation mit XOR anwenden:
Sei in einem Prozessor das 16-Bit-Register $t1 wie folgt belegt:    $t1: xFFFF
Der Befehl XOR $t0, $t0, $t1 invertiert die Dualzahl in Register $t0 und speichert das Ergebnis in $t0
$𝑡1 𝑥𝐹𝐹𝐹𝐹 1111 1111 1111 1111
$𝑡0 191 0000 0000 1011 1111
$𝑡0 𝑛𝑎𝑐ℎ 𝑋𝑂𝑅 1111 1111 0100 0000
− Multiplikation/Division mit bitweiser Verschiebung
− Bitweise Verschiebung nach links bedeutet Multiplikation mit 2: 1110 2 = 14 10 ⇝ 11100 2 = 28 10
− Bitweise Verschiebung nach rechts bedeutet Division durch 2: 1110 2 = 14 10 ⇝ 111 2 = 7 10
− Schnelle Realisierung der Multiplikation mit Verschieben und Addition:
− „Ringschieberegister“ werden mit VA für die bitweise Addition genutzt (selber Recherchieren)
16./31.10.2023

### Seite 11

Unterbrechungen

### Seite 12

INTERRUPTS
−Interrupts sind ein globales Kommunikationskonzept für unterschiedliche
Aufgabenbereiche.
−Sie dienen
−zur Ereignis- und Fehlerbehandlung im laufenden Betrieb,
−zum Aufruf von Betriebssystemfunktionen aus dem User-Mode heraus.
−In allen Fällen erhält das Betriebssystem im Kernel-Modus die Kontrolle.
−Hierfür ist Hardwareunterstützung zwingend notwendig.
11.12.2023

### Seite 13

Dateisysteme
Bild: PiPix / pixelio.de
Mit den
Leseköpfen
und ihrer
Position ergibt
sich ein
Zylinder der
übereinander
liegenden
Spuren des
Plattenstapels.

### Seite 14

DATEISYSTEM
− Datenträger sind in adressierbaren Blöcken fester
Größe (aktuell bis 4KiB, früher 512B) organisiert,
− keinerlei Inhaltsverwaltung, aus Sicht des
Datenträgers existieren nur Blöcke,
− Bereitstellen einer geeigneten Verwaltungsstruktur
durch das Betriebssystem notwendig
11.12.2023
− Datenträger adressieren nur auf Blockebene
− Dateisysteme bieten logische Sicht auf Datenträger
− Elemente der Strukturierung: Datei und Verzeichnis
− verschiedene Dateisystemvarianten existieren parallel

### Seite 15

DATEISYSTEM
Datei: Zusammenhängender Datenbestand
− typischerweise Lesen und/oder Schreiben möglich,
− Interpretation des Inhalts durch Software
Verzeichnis: Datei, die aus Verweisen auf Dateien besteht
Dateisystem: Datenstruktur zur Verwaltung von Dateien,
− Zuordnung von Dateien zu Blöcken,
− Verwaltung freier Blöcke
− Metadaten wie Name, Besitzer, Zugriffssrechte,
− Wiederherstellung, Verschlüsselung, Komprimierung, etc.
11.12.2023

### Seite 16

Speicherverwaltung
Grafik: Wikipedia

### Seite 17

SPEICHERHIERARCHIE
19.12.2023
− Primärspeicher
Bereitstellung von Programmcode und Laufzeitdaten für die
Ausführung durch die CPU
− Sekundärspeicher
zur Ablage und zeitnahen Verfügbarmachung des
Programmcodes und seiner persistenten Daten auch ohne
permanente Energieversorgung,
− Tertiärspeicher
zur Langzeitarchivierung und Datensicherung
Speicher ist ein unbedingt notwendiges Betriebsmittel für die Ausführung von
Prozessen.

### Seite 18

ZUSAMMENFASSUNG
−Die Verwaltung des zur Verfügung stehenden Hauptspeichers ist eine wesentliche Aufgabe
des Betriebssystems.
−Das Konzept der Segmentierung ermöglicht geschützte Speicherbereiche für jeden Prozess
und reduziert außerdem die Länge des Programmcodes durch indirekt-relative Adressierung.
−Beim Paging wird virtueller Speicher adressiert, sodass Prozessen wesentlich mehr Freiraum
zur Verfügung steht. Zugriffsschutz und Seitenauslagerung werden von der Hardware
unterstützt.
06.06.2023

### Seite 19

SPEICHERVERWALTUNG (HAUPTSPEICHER)
− Speicherverwaltung ist eine wesentliche Aufgabe des Betriebssystems.
− Zwei Konzepte (alternativ oder zusammen)
− Segmentierung
ermöglicht geschützte Speicherbereiche für jeden Prozess
reduziert die Länge des Programmcodes (indirekt-relative Adressierung)
− Paging (virtueller Speicher)
Zugriffsschutz und Seitenauslagerung vom Primärspeicher auf Sekundärspeicher
verfügbare Speicherraum für Prozesse erhöht sich wesentlich
− feste Länge der Adresse bestimmt durch Anzahl der Leitungen im Adressbus)
− 32 Bit Adressen (z.B. Intel 80486 bis 2007) erlaubten maximal 4GiB adressierbaren Speicher,
− 64 Bit Adressen (aktuell) adressieren 16 EiB.
− Der physikalisch vorhandene Speicher ist typischerweise deutlich kleiner als der theoretisch adressierbare Raum.
Dies ermöglicht u.a. Virtualisierung
19.12.2023

### Seite 20

ADRESSIERUNGSVARIANTEN – BEISPIELE
Absolute Adressierung Relative Adressierung

### Seite 21

ADRESSIERUNG
− feste Länge der Adresse bestimmt durch Anzahl der Leitungen im
Adressbus)
− 32 Bit Adressen (z.B. Intel 80486 bis 2007) erlaubten maximal 4GiB
adressierbaren Speicher,
− 64 Bit Adressen (aktuell) adressieren 16 EiB.
Der physikalisch vorhandene Speicher (Primärspeicher) ist typischerweise deutlich kleiner als der adressierbare Raum.
Dies ermöglicht u.a. Virtualisierung per Paging

### Seite 22

SEGMENTIERUNG
− Adresse besteht aus einem Segmentteil (Segmentnummer) und einem Offset
(Position innerhalb des Segmentes), z.B.:
− bei 32-Bit-Adressen: 16 Bit Segment, 16 Bit Offset
− bei 64-Bit-Adressen: 32 Bit Segment, 32 Bit Offset
− Segmentnummer bestimmt über Segmenttabelle die Startadresse
− Die Segmentlänge ist durch das maximal mögliche Offset begrenzt. Bei 16 Bit sind
maximal 64KiB große Segmente zulässig, bei 32 Bit 4GiB.

### Seite 23

SEGMENTTABELLE
Hauptspeicher Segmenttabelle
Speicher wird in Speicherbereiche (Segmente) aufgeteilt, Segmente werden den Prozessen zugeordnet.
Segmente festgelegt durch Startadresse (Basis) und Länge, sie haben Zugriffsrechte und Privilegierungsstufen
Die Segmentinformationen werden in einer
Segmenttabelle durch das Betriebssystem verwaltet
und von der CPU (Speicherverwaltungseinheit)
ausgewertet.
Adresse besteht aus einem Segmentteil (Segmentnummer)
und einem Offset (Position innerhalb des Segmentes), z.B.:
bei 32-Bit-Adressen: 16 Bit Segment, 16 Bit Offset
bei 64-Bit-Adressen: 32 Bit Segment, 32 Bit Offset
Segmentnummer bestimmt via Segmenttabelle die
Startadresse
Die Segmentlänge ist durch das maximal mögliche Offset begrenzt.
Bei 16 Bit sind maximal 64KiB große Segmente zulässig, bei 32 Bit 4GiB.

### Seite 24

VIRTUELLER SPEICHER DURCH PAGING
Im Skript
heißen die
Rahmen
Kacheln

### Seite 25

VIRTUELLER SPEICHER DURCH PAGING

### Seite 26

VIRTUELLER SPEICHER DURCH PAGING
Programmierung - VE526
HS bis zu 2 GiB
Virtueller Speicher bis zu
16 GiB
Beispiel
Bild aus dem
Skript
Seitengröße 64 KiB
= 64 ∙ 210 B
= 26 ∙ 210 B
Speicherwort 4 B = 22 B
(Tiefe einer adressierbaren
Speicherzelle)
𝑩𝟏 𝑩𝟐 𝑩𝟑 𝑩𝟒
Datenbus: 4 ∙ 8 𝐵𝑖𝑡 = 32 𝐵𝑖𝑡

### Seite 27

VIRTUELLER SPEICHER DURCH PAGING
Programmierung - VE527
HS bis zu 2 GiB
Virtueller Speicher bis zu
16 GiB
Beispiel
Seitengröße 64 KiB
= 64 ∙ 210 B
= 26 ∙ 210 B
Speicherwort 4 B = 22 B
(Tiefe einer adressierbaren
Speicherzelle)
𝑩𝟏 𝑩𝟐 𝑩𝟑 𝑩𝟒
Datenbus: 22𝐵 = 4 ∙ 8 𝐵𝑖𝑡 = 32 𝐵𝑖𝑡
Offset-Adresse für eine Seite 14 Bit:
26 ∙ 210 B = 214 ∙ 22 B
Virtuelle-Adresse 32 Bit:
16 GiB = 24 ∙ 230 B = 232 ∙ 22 B
Seitennummer-Adresse 18 Bit:
32 Bit – 14 Bit = 18 Bit
Physische-Adresse 29 Bit:
2 GiB = 21 ∙ 230 B = 229 ∙ 22 B
Kachelnummer-Adresse 15 Bit:
29 Bit – 14 Bit = 15 Bit
(Rahmennummer)
Aus geg. Fakten ergibt sich:
Seitengröße 64 KiB
Rahmen ist im Skript Kachel

### Seite 28

Frage:
Wie setzt die Memory-Management-Unit (MMU) beim gegebenen
Speicheraufbau die 32-Bit-Adresse 32769 des virtuellen Speichers zum Zugriff
auf dem Hauptspeicher in eine physische Adresse (29 Bit lang) um?
VIRTUELLER SPEICHER DURCH PAGING
Programmierung - VE528
HS bis zu 2 GiB
Virtueller Speicher bis zu
16 GiB
Beispiel
Offset-Adresse für eine Seite 14 Bit:
26 ∙ 210 B = 214 ∙ 22 B
Virtuelle-Adresse 32 Bit:
16 GiB = 24 ∙ 230 B = 232 ∙ 22 B
Seitennummer-Adresse 18 Bit:
32 Bit – 14 Bit = 18 Bit
Physische-Adresse 29 Bit:
2 GiB = 21 ∙ 230 B = 229 ∙ 22 B
Kachelnummer-Adresse 15 Bit:
29 Bit – 14 Bit = 15 Bit
Aus geg. Fakten ergibt sich:
Seitengröße 64 KiB
Rahmen ist im Skript Kachel

### Seite 29

Frage:
Wie setzt die Memory-Management-Unit (MMU) beim gegebenen
Speicheraufbau die 32-Bit-Adresse 32769 des virtuellen Speichers zum Zugriff
auf dem Hauptspeicher in eine physische Adresse (29 Bit lang) um?
VIRTUELLER SPEICHER DURCH PAGING
Programmierung - VE529
HS bis zu 2 GiB
Virtuelle Adresse: 32769 = 0x00008001 = 0b000000000000000010 00000000000001
Seitennummer (18 Bit)
ist 2
Offset (14 Bit)
ist 1
Seite mit Nummer 2 ist laut Seitentabelle aktuell in Kachel (Rahmen) 6 des
Hauptspeichers. Damit sind die 15 Bit der Kachelnummer bestimmt.
Der 14 Bit-Offset für die Adressierung innerhalb der Seite kommt hinzu:
Physische Adresse: 0b000000000000110 00000000000001 = 0x00018001 = 98305
Antwort:
Beim gegebenen Speicheraufbau wird die 32-
Bit-Adresse 32769 des virtuellen Speichers zum
Zugriff auf dem Hauptspeicher in die physische
Adresse (29 Bit lang) 98305 umgesetzt.

### Seite 30

ZUSATZ ZU TCP/IP
Programmierung - VE530

### Seite 31

© 2024 IU Internationale Hochschule GmbH
Diese Inhalte sind urheberrechtlich geschützt. Alle Rechte vorbehalten.
Diese Inhalte dürfen in jeglicher Form ohne vorherige schriftliche Genehmigung der IU Internationale
Hochschule GmbH nicht reproduziert und/oder unter Verwendung elektronischer Systeme verarbeitet,
vervielfältigt oder verbreitet werden.

### Seite 32

Prof. Dr. Reinhold Kloos
Reinhold.Kloos@iu.org
DANKE
