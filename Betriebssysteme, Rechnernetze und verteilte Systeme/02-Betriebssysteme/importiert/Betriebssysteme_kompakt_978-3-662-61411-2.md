---
author: Andreas Hümmer
title: "429734_2_De_Print.indd"
tags:
  - content
  - importiert
  - bs
created: '2026-10-07'
modified: '2026-10-07'
bereich: BS
typ: sonstig
quelle: "Betriebssysteme_kompakt_978-3-662-61411-2.pdf"
seiten: 298
---

# 429734_2_De_Print.indd

> [!info] Dokumentinformationen
> - **Quelle:** Betriebssysteme_kompakt_978-3-662-61411-2.pdf
> - **Typ:** sonstig
> - **Bereich:** BS
> - **Seiten:** 298
> - **Autor:** 0012149

---

## Inhalt

### Seite 1

Betriebssysteme
kompakt
Christian Baun
Grundlagen, Daten, Speicher, Dateien,
Prozesse und Kommunikation
2. Auflage
IT kompakt

### Seite 2

IT kompakt

### Seite 3

Die Bücher der Reihe „IT kompakt“ zu wichtigen Konzepten und
Technologien der IT:
• ermöglichen einen raschen Einstieg,
• bieten einen fundierten Überblick,
• eignen sich für Selbststudium und Lehre,
• sind praxisorientiert, aktuell und immer ihren Preis wert.
Weitere Bände in der Reihe http://www.springer.com/series/8297

### Seite 4

Christian Baun
Betriebssysteme
kompakt
Grundlagen, Daten, Speicher,
Dateien, Prozesse und
Kommunikation
2., aktualisierte Auflage

### Seite 5

Christian Baun
Fachbereich 2: Informatik
und Ingenieurwissenschaften
Frankfurt University of
Applied Sciences
Frankfurt, Hessen, Deutschland
ISSN 2195-3651 ISSN 2195-366X (electronic)
IT kompakt
ISBN 978-3-662-61410-5  ISBN 978-3-662-61411-2 (eBook)
https://doi.org/10.1007/978-3-662-61411-2
Die Deutsche Nationalbibliothek verzeichnet diese Publikation in der Deutschen
Nationalbibliografie; detaillierte bibliografische Daten sind im Internet über
http://dnb.d-nb.de abrufbar.
© Springer-Verlag GmbH Deutschland, ein Teil von Springer Nature 2017, 2020
Das Werk einschließlich aller seiner Teile ist urheberrechtlich geschützt. Jede
Verwertung, die nicht ausdrücklich vom Urheberrechtsgesetz zugelassen ist,
bedarf der vorherigen Zustimmung des Verlags. Das gilt insbesondere für
Vervielfältigungen, Bearbeitungen, Übersetzungen, Mikroverfilmungen und die
Einspeicherung und Verarbeitung in elektronischen Systemen.
Die Wiedergabe von allgemein beschreibenden Bezeichnungen, Marken,
Unternehmensnamen etc. in diesem Werk bedeutet nicht, dass diese frei durch
jedermann benutzt werden dürfen. Die Berechtigung zur Benutzung unterliegt,
auch ohne gesonderten Hinweis hierzu, den Regeln des Markenrechts. Die Rechte
des jeweiligen Zeicheninhabers sind zu beachten.
Der Verlag, die Autoren und die Herausgeber gehen davon aus, dass die
Angaben und Informationen in diesem Werk zum Zeitpunkt der Veröffentlichung
vollständig und korrekt sind. Weder der Verlag, noch die Autoren oder die
Herausgeber übernehmen, ausdrücklich oder implizit, Gewähr für den Inhalt
des Werkes, etwaige Fehler oder Äußerungen. Der Verlag bleibt im Hinblick auf
geografische Zuordnungen und Gebietsbezeichnungen in veröffentlichten Karten
und Institutionsadressen neutral.
Planung: Sybille Thelen
Springer Vieweg ist ein Imprint der eingetragenen Gesellschaft Springer-Verlag
GmbH, DE und ist ein Teil von Springer Nature.
Die Anschrift der Gesellschaft ist: Heidelberger Platz 3, 14197 Berlin, Germany

### Seite 6

V
Vorwort zur 2. Auflage
Aufgrund der positiven Rückmeldungen und Verbesserungsvor -
schläge enthält diese Auflage außer neuen Inhalten auch zahl-
reiche sprachliche und didaktische Verbesserungen.
Neu hinzugekommen ist unter anderem eine Beschreibung
des Unterschieds von harten und weichen Seitenfehlern in
Kap. 5. Zudem wurde die Darstellung der Arbeitsweise der
Seitenersetzungsstrategie LRU in Kap. 5 verbessert.
Wenn Ihnen bei der Arbeit mit diesem Werk Kritikpunkte
auffallen, oder Sie Verbesserungsvorschläge für zukünftige Auf-
lagen haben, würde ich mich über eine Email von Ihnen sehr
freuen: christianbaun@gmail.com
An dieser Stelle möchte ich meiner Lektorin Sybille
Thelen für ihre Unterstützung danken. Zudem danke ich Jens
Liebehenschel und Torsten Wiens für das Korrekturlesen.
Meinen Eltern Dr. Marianne Baun und Karl-Gustav Baun sowie
meinen Schwiegereltern Anette Jost und Hans Jost und ganz
besonders meiner Frau Katrin Baun danke ich für die Motivation
und Unterstützung in guten und in schwierigen Zeiten.
Frankfurt am Main
März 2020
Prof. Dr. Christian Baun

### Seite 7

VII
Vorwort zur 1. Auflage
Betriebssysteme sind ein wichtiges Thema der praktischen
Informatik und zum geringeren Teil auch der technischen
Informatik. Sie sind die Schnittstelle zwischen der Hardware
eines Computers und seinen Benutzern und deren Software-
prozessen. Zudem verwalten Betriebssysteme die Hardware-
komponenten eines Computers und die gespeicherten Daten.
Dieses kompakte Werk über das breite Thema Betriebssysteme
wurde mit dem Ziel geschrieben, dem Leser einen Überblick
über die wichtigsten Aufgabenbereiche und Kernfunktionali-
täten von Betriebssystemen zu verschaffen und so das Verständnis
dafür zu wecken, wie Betriebssysteme funktionieren, wie sie die
wichtigsten Funktionalitäten erbringen und wie sie die wichtigsten
Hardwarekomponenten eines Computers nutzen und steuern.
Die Programmbeispiele in diesem Werk wurden alle in
der Programmiersprache C geschrieben und unter dem freien
Betriebssystem Debian GNU/Linux getestet. Prinzipiell sollten
sie unter jedem anderen Unix-(ähnlichen) Betriebssystem laufen.
Die Programmbeispiele und eine Errata-Liste sind auf meiner
Webseite1 verfügbar.
Für das Korrekturlesen danke ich Henry Cocos, Samuel
Dietz, Maximilian Hoecker, Rosa Maria Spanou, Michael
Stapelberg und Torsten Wiens.
1http://www.christianbaun.de

### Seite 8

Vorwort zur 1. AuflageVIII
An dieser Stelle möchte ich ganz besonders meiner Familie
danken, die mich auch bei diesem Werk so viel unterstützt hat.
Frankfurt am Main
Februar 2017
Prof. Dr. Christian Baun

### Seite 9

IX
Inhaltsverzeichnis
1 Einleitung ...................................  1
2 Grundlagen der Informationstechnik ............  3
2.1 Bit ...................................  3
2.2 Repräsentation von Zahlen ................  4
2.2.1 Dezimalsystem ..................  5
2.2.2 Dualsystem .....................  5
2.2.3 Oktalsystem  ....................  6
2.2.4 Hexadezimalsystem  ..............  7
2.3 Datei- und Speichergrößen ................  8
2.4 Informationsdarstellung ..................  9
2.4.1 ASCII-Kodierung ................  10
2.4.2 Unicode  .......................  12
2.4.3 Darstellung von Zeichenketten  .....  13
3 Grundlagen der Betriebssysteme ................  15
3.1 Einordnung der Betriebssysteme in die
Informatik  ............................  15
3.2 Positionierung und Kernfunktionalitäten
von Betriebssystemen  ...................  16
3.3 Entwicklung der Betriebssysteme ..........  19
3.3.1 Zweite Generation von
Computern .....................  20
3.3.2 Dritte Generation von Computern ...  21
3.3.3 Vierte Generation von Computern ...  22
3.4 Betriebsarten  ..........................  23
3.4.1 Stapelbetrieb und Dialogbetrieb .....  23

### Seite 10

InhaltsverzeichnisX
3.4.2 Einzelprogrammbetrieb und
Mehrprogrammbetrieb ............  25
3.4.3 Einzelbenutzerbetrieb und
Mehrbenutzerbetrieb  .............  26
3.5 8/16/32/64 Bit-Betriebssysteme ............  27
3.6 Echtzeitbetriebssysteme ..................  28
3.6.1 Harte und weiche
Echtzeitbetriebssysteme ...........  28
3.6.2 Architekturen von
Echtzeitbetriebssystemen ..........  29
3.7 Verteilte Betriebssysteme .................  30
3.8 Architektur des Betriebssystemkerns ........  33
3.8.1 Monolithische Kerne .............  33
3.8.2 Minimale Kerne .................  35
3.8.3 Hybride Kerne ..................  36
3.9 Schichtenmodell ........................  36
4 Grundlagen der Rechnerarchitektur  ............  39
4.1 V on-Neumann-Architektur ................  39
4.1.1 Hauptprozessor ..................  40
4.1.2 V on-Neumann-Zyklus  ............  41
4.1.3 Busleitungen ....................  42
4.2 Ein-/Ausgabegeräte  .....................  46
4.3 Digitale Datenspeicher ...................  49
4.4 Speicherhierarchie  ......................  51
4.4.1 Register  .......................  52
4.4.2 Cache  .........................  53
4.4.3 Hauptspeicher ...................  55
4.4.4 Festplatten  .....................  56
4.4.5 Solid State Drives ................  59
4.5 RAID  ................................  65
4.5.1 RAID 0 ........................  68
4.5.2 RAID 1 ........................  69
4.5.3 RAID 2 ........................  70
4.5.4 RAID 3 ........................  71
4.5.5 RAID 4 ........................  71
4.5.6 RAID 5 ........................  73

### Seite 11

XIInhaltsverzeichnis
4.5.7 RAID 6 ........................  74
4.5.8 RAID-Kombinationen  ............  74
5 Speicherverwaltung  ..........................  77
5.1 Konzepte zur Speicherverwaltung ..........  77
5.1.1 Statische Partitionierung  ..........  78
5.1.2 Dynamische Partitionierung ........  79
5.1.3 Buddy-Speicherverwaltung  ........  82
5.2 Speicheradressierung in der Praxis  .........  86
5.2.1 Real Mode .....................  86
5.2.2 Protected Mode und virtueller
Speicher .......................  90
5.2.3 Seitenorientierter Speicher
(Paging) .......................  93
5.2.4 Segmentorientierter Speicher
(Segmentierung) .................  101
5.2.5 Aktueller Stand beim virtuellen
Speicher .......................  102
5.2.6 Kernelspace und Userspace ........  104
5.3 Seitenersetzungsstrategien ................  105
5.3.1 Optimale Strategie ...............  106
5.3.2 Least Recently Used ..............  107
5.3.3 Least Frequently Used ............  108
5.3.4 First In First Out .................  109
5.3.5 Clock / Second Chance  ...........  110
5.3.6 Random  .......................  111
6 Dateisysteme  ................................  113
6.1 Technische Grundlagen der Dateisysteme ....  114
6.2 Blockadressierung bei Linux-Dateisystemen  .  115
6.2.1 Minix  .........................  117
6.2.2 ext2/3  .........................  119
6.3 Dateisysteme mit Dateizuordnungstabellen ...  121
6.3.1 FAT12 .........................  126
6.3.2 FAT16 .........................  126
6.3.3 FAT32 .........................  128
6.3.4 VFAT  .........................  128
6.4 Journaling-Dateisysteme  .................  129

### Seite 12

InhaltsverzeichnisXII
6.5 Extent-basierte Adressierung ..............  132
6.5.1 ext4 ...........................  133
6.5.2 NTFS  .........................  134
6.6 Copy-on-Write .........................  137
6.7 Datenzugriffe mit einem Cache
beschleunigen ..........................  138
6.8 Defragmentierung  ......................  139
7 Systemaufrufe  ...............................  141
7.1 Benutzermodus und Kernelmodus ..........  141
7.2 Systemaufrufe und Bibliotheken ...........  142
7.3 Ablauf eines Systemaufrufs ...............  146
8 Prozessverwaltung  ...........................  149
8.1 Prozesskontext .........................  149
8.2 Prozesszustände ........................  151
8.3 Struktur eines Prozesses im Speicher  .......  158
8.4 Prozesse erzeugen mit fork  ...............  162
8.5 Prozesse ersetzen mit exec ................  167
8.6 Prozesswechsel und Scheduling von
Prozessen .............................  171
8.6.1 Prioritätengesteuertes Scheduling ...  175
8.6.2 First Come First Served ...........  175
8.6.3 Round Robin  ...................  176
8.6.4 Shortest Job First/Shortest Process
Next ..........................  177
8.6.5 Shortest Remaining Time First  .....  178
8.6.6 Longest Job First ................  178
8.6.7 Longest Remaining Time First ......  179
8.6.8 Highest Response Ratio Next. . . . . . .  179
8.6.9 Earliest Deadline First ............  180
8.6.10 Fair-Share-Scheduling  ............  181
8.6.11 Multilevel-Scheduling  ............  181
9 Interprozesskommunikation  ..................  187
9.1 Kritische Abschnitte und
Wettlaufsituationen .....................  187
9.2 Synchronisation von Prozessen ............  190
9.2.1 Definition der Ausführungsreihen-
folge durch Signalisierung .........  191

### Seite 13

XIIIInhaltsverzeichnis
9.2.2 Schutz kritischer Abschnitte durch
Sperren ........................  193
9.2.3 Verhungern und Deadlock .........  195
9.3 Kommunikation von Prozessen ............  200
9.3.1 Gemeinsamer Speicher (Shared
Memory) .......................  200
9.3.2 Nachrichtenwarteschlangen
(Message Queue) ................  209
9.3.3 Kommunikationskanäle (Pipes) .....  218
9.3.4 Sockets ........................  230
9.4 Kooperation von Prozessen ...............  244
9.4.1 Semaphor ......................  245
9.4.2 Mutex .........................  251
9.4.3 Monitor ........................  251
10 Virtualisierung  ..............................  253
10.1 Partitionierung  .........................  254
10.2 Hardware-Emulation  ....................  255
10.3 Anwendungsvirtualisierung ...............  256
10.4 V ollständige Virtualisierung ...............  257
10.5 Paravirtualisierung ......................  260
10.6 Hardware-Virtualisierung .................  261
10.7 Betriebssystem-Virtualisierung  ............  262
Glossar .........................................  265
Literatur ........................................  273
Stichwortverzeichnis ..............................  277

### Seite 14

1Einleitung
Dieses Buch will einen Überblick über das Thema Betriebssysteme
und deren Komponenten schaffen, ohne dabei den Anspruch auf
V ollständigkeit zu erheben. Das Ziel ist es, den Leserinnen und
Lesern ein grundlegendes Wissen über die Funktionsweise von
Betriebssystemen und deren Komponenten zu vermitteln. Techni-
sche V orkenntnisse sind dabei nicht erforderlich.
In den Kap.2 und 3 ﬁndet eine Einführung in die Grundlagen der
Informationstechnik und der Betriebssysteme statt. Dies ist nötig,
um die Thematik Betriebssysteme und den Inhalt dieses Buchs
verstehen zu können.
Ein V erständnis der notwendigsten Hardwarekomponenten
eines Computers ist elementar, um die Arbeitsweise von Betriebs-
systemen zu verstehen. Darum beschäftigt sich Kap. 4 mit den
Grundlagen der Rechnerarchitektur. Schwerpunkte dieses Kapi-
tels sind die Arbeitsweise des Hauptprozessors, des Speichers und
der Bussysteme.
Kap. 5 beschreibt die grundlegenden Konzepte der Speicherver-
waltung und die Art und Weise, wie moderne Betriebssysteme den
Cache und den Hauptspeicher verwalten.
Eine andere Form der Speicherverwaltung thematisiert Kap. 6.
Dieses Kapitel beschreibt die technischen Grundlagen klassischer
und moderner Dateisysteme anhand ausgewählter Beispiele.
© Springer-V erlag GmbH Deutschland, ein Teil von Springer
Nature 2020
C. Baun, Betriebssysteme kompakt, IT kompakt,
https://doi.org/10.1007/978-3-662-61411-2_1
1

### Seite 15

2 1 Einleitung
Die Interaktion der Benutzerprozesse mit den Funktionen des
Betriebssystemkerns geschieht via Systemaufrufe. Diese können
direkt oder über Bibliotheksfunktionen aufgerufen werden. Eine
Beschreibung der Arbeitsweise von und mit Systemaufrufen ent-
hält Kap. 7.
Der Fokus von Kap.8 liegt auf der Prozessverwaltung. Schwer-
punkte sind einerseits die Art und Weise, wie Prozesse im Betriebs-
system realisiert werden und nach welchen Kriterien diese den
Prozessor zugewiesen bekommen.
Möglichkeiten zum Schutz kritischer Abschnitte und die ver-
schiedenen Aspekte der Interprozesskommunikation beschreibt
Kap. 9.
Abschließend ﬁndet in Kap. 10 eine Einführung in die aus Sicht
der Betriebssysteme relevanten Virtualisierungskonzepte statt.

### Seite 16

2Grundlagen der
Informationstechnik
Um die Funktionsweise von Betriebssystemen zu verstehen, ist
ein grundlegendes Verständnis der Informationstechnik (IT) nötig.
Bei diesen Grundlagen handelt es sich um die Möglichkeiten der
Informationsdarstellung und Repräsentation von Zahlen, Größen-
ordnungen und die Art und Weise, wie Informationen (speziell
Texte) in Rechnern dargestellt werden.
2.1 Bit
Ein Bit ist die kleinstmögliche Einheit der Information und jede
Information ist an einen Informationsträger gebunden [ 20]. Ein
Informationsträger, der sich in genau einem von zwei Zuständen
beﬁnden kann, kann die Datenmenge 1 Bit darstellen. Den Wert
eines oder mehrerer Bits nennt man Zustand. Ein Bit stellt zwei
Zustände dar. Verschiedene Sachverhalte können die Datenmenge
1 Bit darstellen. Beispiele sind:
• Die Stellung eines Schalters mit zwei Zuständen
• Der Schaltzustand eines Transistors
• Das V orhandensein einer elektrischen Spannung oder Ladung
• Das V orhandensein einer Magnetisierung
• Der Wert einer Variable mit den logischen Wahrheitswerten
© Springer-Verlag GmbH Deutschland, ein Teil von Springer
Nature 2020
C. Baun, Betriebssysteme kompakt, IT kompakt,
https://doi.org/10.1007/978-3-662-61411-2_2
3

### Seite 17

4 2 Grundlagen der Informationstechnik
Tab. 2.1 Die Anzahl der darstellbaren Zustände verdoppelt sich mit jedem
zusätzlichen Bit
Bits Zustände Bits Zustände Bits Zustände
1 21 = 2 9 29 = 512 17 217 = 131.072
2 22 = 4 10 210 = 1.024 18 218 = 262.144
3 23 = 8 11 211 = 2.048 19 219 = 524.288
4 24 = 16 12 212 = 4.096 20 220 = 1.048.576
5 25 = 32 13 213 = 8.192 21 221 = 2.097.152
6 26 = 64 14 214 = 16.384 22 222 = 4.194.304
7 27 = 128 15 215 = 32.768 23 223 = 8.388.608
8 28 = 256 16 216 = 65.536 24 224 = 16.777.216
Benötigt man zur Speicherung einer Information mehr als zwei
Zustände, sind Folgen von Bits (Bitfolgen) nötig. Mit n Bits kann
man 2 n verschiedene Zustände darstellen (siehe Tab. 2.1). Also
kann man mit 2 Bits 22 = 4 verschiedene Zustände repräsentieren,
nämlich 00, 01, 10 und 11. Mit 3 Bits kann man schon 2 3 = 8
verschiedene Zustände (000, 001, 010, 011, 100, 101, 110 und
111) repräsentieren. Jedes zusätzliche Bit verdoppelt die Anzahl
der möglichen darstellbaren Zustände (Bitfolgen) [20].
2.2 Repräsentation von Zahlen
Zahlen kann man auf unterschiedliche Arten darstellen. Eine Auf-
gabe der IT ist es, Zahlen aus der realen Welt im Rechner abzu-
bilden. Wichtig ist dabei die Unterscheidung zwischen Wert und
Darstellung.
In der Mathematik unterscheidet man Zahlen als Elemente ver-
schiedener Wertemengen (natürliche Zahlen, ganze Zahlen, reelle
Zahlen, komplexe Zahlen, usw.). Den Wert einer Zahl nennt man
auch abstrakte Zahl und der Wert ist unabhängig von der Darstel-
lung (zum Beispiel 0,5 = 1/2).
Operationen eines Rechners werden aber nicht auf Werten, son-
dern auf Bitfolgen ausgeführt. Darum ist für die IT besonders
die Darstellung der Zahlen interessant. Die Darstellung wird vom

### Seite 18

2.2 Repräsentation von Zahlen 5
verwendeten Stellenwertsystem (Positionssystem) bestimmt. Die
für die IT wichtigen Stellenwertsysteme sind das Dezimalsystem,
das Dualsystem, das Oktalsystem und das Hexadezimalsystem.
2.2.1 Dezimalsystem
Das Dezimalsystem verwendet als Basis die Zahl 10. Jede ZifferD
an der Stelle i hat den Wert D × 10i . Ein Beispiel ist:
2013 = 2 × 103 + 0 × 102 + 1 × 101 + 3 × 100
Computer-Systeme unterscheiden prinzipiell zwischen zwei
elektrischen Zuständen. Darum ist aus Sicht der IT als Basis die
Zahl 2 und damit das Dualsystem optimal geeignet.
2.2.2 Dualsystem
Das Dualsystem verwendet als Basis die Zahl 2. Zahlen werden
nur mit den Ziffern der Werte Null und Eins dargestellt. Zahldar-
stellungen im Dualsystem heißen Dualzahlen oder Binärzahlen.
Alle positiven natürlichen Zahlen inklusive der Null können durch
Folgen von Symbolen aus der Menge {0, 1} repräsentiert werden.
Wenn n der Anzahl der Bits entspricht, ist x0 das niederwertigste
Bit (Least Signiﬁcant Bit – LSB) und xn−1 das höchstwertigste Bit
(Most Signiﬁcant Bit – MSB).
Da lange Reihen von Nullen und Einsen für Menschen schnell
unübersichtlich werden, verwendet man zur Darstellung von Bit-
folgen häuﬁg das Oktalsystem oder das Hexadezimalsystem.
Die Umrechnung der Stellenwertsysteme ist einfach möglich.
Zur Verdeutlichung ist das Stellenwertsystem der jeweiligen Zahl
in den folgenden Beispielen tiefgestellt beigefügt.
Bei der Umwandlung von Dualzahlen in Dezimalzahlen werden
die Ziffern mit ihren Stellenwertigkeiten ausmultipliziert und die
Ergebnisse addiert.
101001002 = 27 + 25 + 22 = 16410

### Seite 19

6 2 Grundlagen der Informationstechnik
Tab. 2.2 Die Dezimalzahl 16410 in die Dualzahl 101001002 umwandeln
k Quotient Rest
k DIV 2 k MODULO 2
164 82 0 = x1
82 41 0 = x2
41 20 1 = x3
20 10 0 = x4
10 5 0 = x5
5 2 1 = x6
2 1 0 = x7
1 0 1 = x8
Die Umwandlung von Dezimalzahlen in Dualzahlen ist unter
anderem mit dem in Tab.2.2 gezeigten Verfahren möglich. Dabei
wird die Dezimalzahl durch die Basis 2 dividiert und das Ergebnis
und der Rest (Wert Null oder Eins) werden notiert. Das Ergeb-
nis der Division wird in der nächsten Runde (Zeile der Tabelle)
erneut durch die Basis dividiert und erneut werden das Ergebnis
und der Rest notiert. Dieser Restwertalgorithmus wird so lange
weitergeführt, bis das Ergebnis der Division Null ist.
2.2.3 Oktalsystem
Das Oktalsystem verwendet als Basis die Zahl 8 und kann Gruppen
von 3 Bits mit einem Zeichen darstellen.
Bei der Umwandlung von Dualzahlen in Oktalzahlen wird die
Bitkette vom niederwertigsten Bit beginnend in Dreiergruppen
unterteilt. Jede Dreiergruppe entspricht einer Stelle der Oktalzahl.
16410 = 10|100|1002 = 2448
Die Umwandlung von Oktalzahlen in Dualzahlen erfolgt ana-
log. Eine Stelle im Oktalsystem entspricht drei Stellen im Dual-
system.

### Seite 20

2.2 Repräsentation von Zahlen 7
2.2.4 Hexadezimalsystem
Das Hexadezimalsystem verwendet als Basis die Zahl 16. Die Dar-
stellung positiver natürlicher Zahlen erfolgt mit den 16 Ziffern und
Buchstaben aus der Menge {0, 1,... 8, 9, A, B, C, D, E, F}. Ein
Zeichen kann eine Gruppe von 4 Bits (Tetrade oder Nibble) dar-
stellen.
Bei der Umwandlung von Dualzahlen in Hexadezimalzahlen
wird die Bitkette vom niederwertigsten Bit beginnend in Tetraden
unterteilt. Jede Tetrade entspricht einer Stelle der Hexadezimal-
zahl.
16410 = 1010|01002 = A416
Die Umwandlung von Hexadezimalzahlen in Dualzahlen
geschieht analog. Eine Stelle im Hexadezimalsystem entspricht
vier Stellen im Dualsystem.
Tab. 2.3 Verschiedene Darstellungen positiver natürlicher Zahlen
Dezimale
Darstellung
Binäre
Darstellung
Oktale
Darstellung
Hexadezimale
Darstellung
00 0000 00 0
01 0001 01 1
02 0010 02 2
03 0011 03 3
04 0100 04 4
05 0101 05 5
06 0110 06 6
07 0111 07 7
08 1000 10 8
09 1001 11 9
10 1010 12 A
11 1011 13 B
12 1100 14 C
13 1101 15 D
14 1110 16 E
15 1111 17 F

### Seite 21

8 2 Grundlagen der Informationstechnik
Tab.2.3 enthält eine Übersicht der verschiedenen Darstellun-
gen der ersten 16 positiven natürlichen Zahlen im Dezimalsystem,
Dualsystem, Oktalsystem und Hexadezimalsystem.
2.3 Datei- und Speichergrößen
Computer lesen und schreiben aus Geschwindigkeitsgründen meist
nicht einzelne Bits, sondern arbeiten mit Bitfolgen, deren Längen
Vielfache von Acht sind. Eine Gruppe von 8 Bits nennt manByte.
Den Wert eines Bytes kann man entweder durch 8 Bits oder zwei
Hexadezimalziffern darstellen.
Eine Datei ist eine beliebig lange Folge von Bytes und enthält
inhaltlich zusammengehörende Daten. Alle Informationen (Zah-
len, Texte, Musik, Programme, usw.), mit denen ein Computer
arbeiten soll, müssen als Folge von Bytes repräsentiert werden
können und als Datei gespeichert werden [20].
Da sich die Größenordnungen der meisten Dateien im Bereich
mehrerer Tausend oder Millionen Bytes beﬁnden, gibt es ver-
schiedene Größeneinheiten zur verkürzten Zahlendarstellung. Für
Datenspeicher mit binärer Adressierung ergeben sich Speicherka-
pazitäten von 2n Byte, also Zweierpotenzen (siehe Tab.2.4).
Die Maßeinheiten in Tab. 2.4 haben sich für die Größenan-
gabe von Hauptspeicher und Speichermedien in Betriebssyste-
men eingebürgert. Die Hersteller von Festplatten, CD/DVDs und
Tab. 2.4 Datei- und Speichergrößen
Name Symbol Bytes
Kilobyte kB 210 = 1.024
Megabyte MB 220 = 1.048.576
Gigabyte GB 230 = 1.073.741.824
Terabyte TB 240 = 1.099.511.627.776
Petabyte PB 250 = 1.125.899.906.842.624
Exabyte EB 260 = 1.152.921.504.606.846.976
Zettabyte ZB 270 = 1.180.591.620.717.411.303.424
Yottabyte YB 280 = 1.208.925.819.614.629.174.706.176

### Seite 22

2.4 Informationsdarstellung 9
USB-Speichermedien bevorzugen zur Berechnung der Kapazität
und zur Angabe auf der Verpackung aber lieber Dezimal-Präﬁxe,
also zum Beispiel den Faktor 10 9 anstatt 2 30 für GB und 10 12
anstatt 2 40 für TB. Aus diesem Grund wird zum Beispiel bei
einem DVD-Rohling mit einer angegebenen Kapazität von 4,7 GB
in vielen Anwendungen korrekterweise nur die Kapazität 4,38 GB
angezeigt.
109 = 1.000.000.000 , 230 = 1.073.741.824
Der Kapazitätsunterschied zwischen Zweierpotenz und Zehner-
potenz ist in diesem Fall ca. 7,37 %.
Bei größeren Speichern ist der Unterschied noch größer. So
können von einer Festplatte mit angeblich 1 TB Speicherkapazität
tatsächlich nur etwa 930 GB verwendet werden.
1012 = 1.000.000.000.000 , 240 = 1.099.511.627.776
Der Kapazitätsunterschied zwischen Zweierpotenz und Zehner-
potenz ist in diesem Fall schon ca. 9,95 % und mit jeder weiteren
Maßeinheit (PB, EB, ZB, usw.) wächst der Kapazitätsunterschied
zwischen Zweierpotenzen und Zehnerpotenzen weiter.
Die International Electrotechnical Commission (IEC) schlug
1996 vor, die populären Größenfaktoren, die auf den Zweierpoten-
zen basieren, mit einem kleinen „i“ zu kennzeichnen und die eta-
blierten Bezeichnungen der Maßeinheiten für die Zehnerpotenzen
zu reservieren. Dieser V orschlag konnte sich bislang nicht durch-
setzen und die daraus resultierenden alternativen Bezeichnungen
Kibibyte (KiB), Mebibyte (MiB), Gibibyte (GiB), Tebibyte (TiB),
Pebibyte (PiB), Exbibyte (EiB) und Zebibyte (ZiB) sind außerhalb
des akademischen Bereichs nicht besonders populär.
2.4 Informationsdarstellung
Daten sind Folgen von Nullen und Einsen, die beliebige Infor-
mationen repräsentieren. Um Texte und Zahlen durch Daten dar-
zustellen, kodiert man die Zeichen des Alphabets (Groß- und

### Seite 23

10 2 Grundlagen der Informationstechnik
Kleinschreibung), Satzzeichen wie Punkt, Komma und Semiko-
lon, sowie einige Spezialzeichen wie zum Beispiel +, %, & und
$ in Bitfolgen. Zudem sind Sonderzeichen wie Leerzeichen (SP),
Wagenrücklauf (CR) und Tabulator (TAB) nötig. Die am besten eta-
blierte Kodierung ist derAmerican Standard Code for Information
Interchange (ASCII).
2.4.1 ASCII-Kodierung
Die ASCII-Kodierung, häuﬁg auch US-ASCII genannt, ist eine
7-Bit-Zeichenkodierung. Das heißt, dass jedem Zeichen eine Bit-
folge aus 7 Bits zugeordnet ist. Es existieren also 2 7 = 128 ver-
schiedene Bitfolgen und exakt so viele Zeichen deﬁniert die Zei-
chenkodierung (siehe Tab.2.5). V on den 128 Zeichen sind 95 Zei-
chen druckbar und 33 Zeichen nicht druckbar. Die druckbaren Zei-
chen sind (beginnend mit dem Leerzeichen):
!"#$%&’()*+,-./0123456789:;<=>?
@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]ˆ_
‘abcdefghijklmnopqrstuvwxyz{|}˜
Die nicht druckbaren Zeichen 0016 bis 2016 und 7F16, zum Beispiel
Backspace ( BS) und Carriage Return ( CR), sind Steuerzeichen,
die ursprünglich zur Steuerung eines Fernschreibers verwendet
wurden. ASCII ist also nicht nur ein Standard zur Datenablage,
sondern auch zur Datenübertragung geeignet. Den Anfang und
das Ende einer Datenübertragung markiert man mit Start of Text
(STX) bzw. End of Text ( ETX). Die Steuerung der Übertragung
ist mit nicht druckbaren Zeichen wie Acknowledge ( ACK) und
negative Acknowledge (NAK) möglich. Mit Bell ( BEL) kann ein
Sender, zum Beispiel bei einem Fehler, ein Alarmsignal an den
Empfänger senden.
Das 8. Bit kann als Paritätsbit zur Fehlererkennung verwendet
werden. In diesem Fall hat es den Wert 0, wenn die Anzahl der Ein-
sen an den übrigen sieben Bitpositionen gerade ist und ansonsten
den Wert 1.

### Seite 24

2.4 Informationsdarstellung 11
Tab. 2.5 Tabelle der ASCII-Zeichenkodierung (US-ASCII)
Dez Hex Zeichen Dez Hex Zeichen Dez Hex Zeichen Dez Hex Zeichen
000 00 NUL 032 20 Space 064 40 @ 096 60 ‘
001 01 SOH 033 21 ! 065 41 A 097 61 a
002 02 STX 034 22 " 066 42 B 098 62 b
003 03 ETX 035 23 # 067 43 C 099 63 c
004 04 EOT 036 24 $ 068 44 D 100 64 d
005 05 ENQ 037 25 % 069 45 E 101 65 e
006 06 ACK 038 26 & 070 46 F 102 66 f
007 07 BEL 039 27 ' 071 47 G 103 67 g
008 08 BS 040 28 ( 072 48 H 104 68 h
009 09 TAB 041 29 ) 073 49 I 105 69 i
010 0A LF 042 2A * 074 4A J 106 6A j
011 0B VT 043 2B + 075 4B K 107 6B k
012 0C FF 044 2C , 076 4C L 108 6C l
013 0D CR 045 2D − 077 4D M 109 6D m
014 0E SO 046 2E . 078 4E N 110 6E n
015 0F SI 047 2F / 079 4F O 111 6F o
016 10 DLE 048 30 0 080 50 P 112 70 p
017 11 DC1 049 31 1 081 51 Q 113 71 q
018 12 DC2 050 32 2 082 52 R 114 72 r
019 13 DC3 051 33 3 083 53 S 115 73 s
020 14 DC4 052 34 4 084 54 T 116 74 t
021 15 NAK 053 35 5 085 55 U 117 75 u
022 16 SYN 054 36 6 086 56 V 118 76 v
023 17 ETB 055 37 7 087 57 W 119 77 w
024 18 CAN 056 38 8 088 58 X 120 78 x
025 19 EM 057 39 9 089 59 Y 121 79 y
026 1A SUB 058 3A : 090 5A Z 122 7A z
027 1B ESC 059 3B ; 091 5B [ 123 7B {
028 1C FS 060 3C < 092 5C \ 124 7C |
029 1D GS 061 3D = 093 5D ] 125 7D }
030 1E RS 062 3E > 094 5E ^ 126 7E ~
031 1F US 063 3F ? 095 5F _ 127 7F DEL

### Seite 25

12 2 Grundlagen der Informationstechnik
Durch verbesserte Protokolle zur Datenübertragung benötigt
man das 8. Bit bei der Datenübertragung von ASCII-kodierten Tex-
ten nicht mehr zur Fehlererkennung. Darum wurde, um zusätzliche
Zeichen kodieren zu können, US-ASCII mit zahlreichen Erwei-
terungen zu einer 8-Bit-Zeichenkodierung erweitert. Wird jedem
Zeichen eine Bitfolge aus 8 Bits zugeordnet, sind 2 8 = 256 ver-
schiedene Bitfolgen verfügbar. Es sind also 128 Zeichen mehr
verfügbar, als bei US-ASCII. Da diese 128 zusätzlichen Zeichen
nicht ausreichen, um alle international benötigten Sonderzeichen
zu kodieren, existieren verschiedene ASCII-Erweiterungen für die
verschiedenen Sprachen und Regionen.
Die Erweiterungen sind mit dem ursprünglichen US-ASCII
kompatibel. Alle im US-ASCII deﬁnierten Zeichen werden in
den verschiedenen Erweiterungen durch die gleichen Bitfolgen
kodiert. Die ersten 128 Zeichen einer ASCII-Erweiterung sind
also mit der ursprünglichen ASCII-Tabelle identisch. Die Erwei-
terungen wie zum Beispiel ISO Latin 9 (ISO 8859-15) enthalten
sprachspeziﬁsche Zeichen (zum Beispiel Umlaute) und Sonderzei-
chen (zum Beispiel das Euro-SymbolC), die nicht im lateinischen
Grundalphabet enthalten sind.
Ein Nachteil der ASCII-Erweiterungen ist, dass nicht in allen
Betriebssystemen alle Erweiterungen verfügbar sind. Wenn zwei
Kommunikationspartner nicht die identische Erweiterung verwen-
den, werden unter anderem die Sonderzeichen im Text falsch ange-
zeigt.
2.4.2 Unicode
Um die Probleme durch unterschiedliche Zeichenkodierungen in
Zukunft zu vermeiden, wurde die Mehrbyte-Kodierung Unicode
(ISO 10646) entwickelt. Diese wird laufend erweitert und soll in
Zukunft alle bekannten Schriftzeichen enthalten.
Es existieren verschiedene Unicode-Standards. Am populärsten
ist UTF-8. Die ersten 128 Zeichen werden mit einem Byte codiert
und sind mit US-ASCII identisch. Die Kodierungen aller anderen
Zeichen verwenden zwischen 2 und 6 Bytes. Aktuell enthält UTF-8
über 100.000 Zeichen.

### Seite 26

2.4 Informationsdarstellung 13
Tab. 2.6 Mehrbyte-Zeichenkodierung mit UTF-8
Codelänge Bits für die
Zeichenkodierung
Format
1B y t e 7 Bits 0xxxxxxx
2B y t e s 11 Bits 110xxxxx
10xxxxxx
3B y t e s 16 Bits 1110xxxx
10xxxxxx
10xxxxxx
4B y t e s 21 Bits 11110xxx
10xxxxxx
10xxxxxx
10xxxxxx
5B y t e s 26 Bits 111110xx
10xxxxxx
10xxxxxx
10xxxxxx
10xxxxxx
6B y t e s 31 Bits 1111110x
10xxxxxx
10xxxxxx
10xxxxxx
10xxxxxx
10xxxxxx
Bei UTF-8 entspricht jedes mit 0 beginnende Byte einem 7-
Bit US-ASCII-Zeichen. Jedes mit 1 beginnende Byte gehört zu
einem aus mehreren Bytes kodierten Zeichen. Besteht ein mit UTF-
8 kodiertes Zeichen aus n≥2 Bytes, beginnt das erste Byte mit n
Einsen und jedes der n − 1 folgenden Bytes mit der Bitfolge 10
(siehe Tab.2.6).
2.4.3 Darstellung von Zeichenketten
Um einen fortlaufenden Text zu kodieren, werden die einzelnen
Zeichen zu einer Zeichenkette(String) aneinandergefügt. Der Text
„Betriebssysteme kompakt.“ wird zur nachstehenden Zei-
chenfolge.

### Seite 27

14 2 Grundlagen der Informationstechnik
B, e, t, r, i, e, b, s, s, y, s, t,
e ,m ,e , ,k ,o ,m ,p ,a ,k ,t ,.
Alle Zeichen (auch das Leerzeichen) werden durch die dezimalen
Zeichennummern der ASCII-Tabelle ersetzt.
066 101 116 114 105 101 098 115 115 121 115 116
101 109 101 000 107 111 109 112 097 107 116 046
Alternativ kann man die hexadezimalen Zeichennummern der
ASCII-Tabelle angeben.
42 65 74 72 69 65 62 73 73 79 73 74
65 6D 65 00 6B 6F 6D 70 61 6B 74 2E
Konvertiert man die Zeichennummern in Dualzahlen, erhält man
die Repräsentation als Bitfolge.
01000010 01100101 01110100 01110010
01101001 01100101 01100010 01110011
01110011 01111001 01110011 01110100
01100101 01101101 01100101 00000000
01101011 01101111 01101101 01110000
01100001 01101011 01110100 00101110

### Seite 28

3Grundlagen der
Betriebssysteme
Nach einer Einordnung des Themas Betriebssysteme in die Infor-
matik behandelt dieses Kapitel grundlegende Begriffe und Unter-
scheidungskriterien der Betriebssysteme. Dazu gehören die unter-
schiedlichen Betriebsarten Stapelbetrieb und Dialogbetrieb sowie
Einzel- und Mehrprogrammbetrieb. Es folgt eine Beschreibung der
wichtigsten Eigenschaften von Echtzeitbetriebssystemen sowie
von verteilten Betriebssystemen. Im weiteren Verlauf des Kapitels
werden die unterschiedlichen Architekturkonzepte von Betriebs-
systemkernen gegenübergestellt und der prinzipielle Aufbau der
Betriebssysteme anhand eines Schichtenmodells dargestellt.
3.1 Einordnung der Betriebssysteme in die
Informatik
Die Informatik gliedert sich in die vier Teilgebiete praktische,
technische und theoretische Informatik sowie Mathematik. Wie
jedes Fachgebiet ist auch die Informatik beeinﬂusst von ande-
ren Fachgebieten. Ein Studium der Informatik oder eine ver-
gleichbare Ausbildung berücksichtigen daher auch immer min-
destens ein Nebenfach, um den persönlichen Neigungen und dem
© Springer-Verlag GmbH Deutschland, ein Teil von Springer
Nature 2020
C. Baun, Betriebssysteme kompakt, IT kompakt,
https://doi.org/10.1007/978-3-662-61411-2_3
15

### Seite 29

16 3 Grundlagen der Betriebssysteme
Abb. 3.1 Einordnung der Betriebssysteme in die Informatik
Arbeitsmarkt gerecht zu werden. Nebenfächer 1 sind häuﬁg E-
Technik, BWL/VWL oder Medizin, seltener Geographie oder
Sprachwissenschaften.
Bei Betriebssystemen handelt es sich ausschließlich um Soft-
ware. Darum umfasst das Thema Betriebssysteme primär Inhalte
aus der praktischen Informatik. Da eine der Hauptaufgaben von
Betriebssystemen die Steuerung der jeweiligen Computer ist, gehö-
ren zum Thema Betriebssysteme auch immer Inhalte der techni-
schen Informatik.
Abb.3.1 zeigt eine Übersicht über die Teilgebiete der Informatik
und dazugehöriger Themen.
3.2 Positionierung und Kernfunktionalitäten
von Betriebssystemen
Auf jedem 2 Computer ist direkt über der Hardware-Ebene ein
Betriebssystem (siehe Abb. 3.2) installiert, das mit Hilfe des
1Die an dieser Stelle präsentierte Auﬂistung der Nebenfächer hat keinen
Anspruch auf V ollständigkeit. Das gleiche gilt für die in Abb. 3.1 gezeigten
Themen der Informatik.
2Eine Ausnahme vom Grundsatz, dass direkt über der Hardware-Ebene
ein Betriebssystem läuft, ist das Virtualisierungskonzept Paravirtualisierung

### Seite 30

3.2 Positionierung und Kernfunktionalitäten von Betriebssystemen 17
Abb. 3.2 Positionierung des Betriebssystems
Betriebssystemkerns (englisch:Kernel) und verschiedener System-
prozesse3 die grundlegenden Kernfunktionalitäten anbietet. Aus
hierarchischer Sicht über dem Betriebssystem beﬁnden sich die
Benutzerprozesse, die die Aufträge der Benutzer abarbeiten.
Eine Übersicht über die Kernfunktionalitäten (Aufgabenberei-
che) der Betriebssysteme zeigt Abb.3.3. Diese sind die Verwaltung
der…
• Hardwarekomponenten eines Computers.
• Daten in den unterschiedlichen Datenspeichern (Cache, Haupt-
speicher, Auslagerungsspeicher und Speicherlaufwerke) des
Computers.
• Prozesse und die Bereitstellung von Funktionalitäten zur Inter-
prozesskommunikation.
• unterschiedlichen Benutzer und Benutzergruppen.
Konsequenterweise sind die allermeisten in diesem Abschnitt
beschriebenen und in Abb.3.3 gezeigten Kernfunktionalitäten der
Betriebssysteme auch die Themen, die dieses Werk vermitteln
will. Grundlegendes Wissen zu den Hardwarekomponenten, die
(siehe Abschn. 10.5). Dort läuft direkt auf der Hardware ein Hypervisor, der
die Hardwareressourcen unter den Gastsystemen verteilt.
3Systemprozesse sind Prozesse, die Dienstleistungen für das Betriebssystem
erbringen.

### Seite 31

18 3 Grundlagen der Betriebssysteme
Abb. 3.3 Kernfunktionalitäten von Betriebssystemen

### Seite 32

3.3 Entwicklung der Betriebssysteme 19
Tab. 3.1 Generationen von Computersystemen
Generation Zeitraum Technologischer
Fortschritt
0 bis 1940 (Elektro-)mechanische
Rechenmaschinen
1 1940–1955 Elektronenröhren,
Relais, Steckfelder
2 1955–1965 Transistoren,
Stapelverarbeitung
3 1965–1980 Integrierte Schaltungen,
Dialogbetrieb
4 1980–2000 Hochintegrierte
Schaltungen,
PCs/Workstations
5 2000 bis ? Verteilte Systeme,
Mobile Systeme
durch die Betriebssysteme verwaltet werden, vermittelt Kap.4. Die
verschiedenen Formen der Speicherverwaltung sind die Inhalte
der Kap. 5 und 6. Die Verwaltung der Prozesse und die unter-
schiedlichen Formen der Interprozesskommunikation vermitteln
die Kap. 7, 8 und 9.
3.3 Entwicklung der Betriebssysteme
Die Auﬂistung der Generationen von Computersystemen, deren
zeitliche Grenzen unschärfer sind, als es Tab. 3.1 vermuten lässt,
macht deutlich, warum es erst ab den 1950er Jahren erste Entwick-
lungen im Bereich Betriebssysteme gab.
Die erste Generation von Computersystemen entstand wäh-
rend des zweiten Weltkriegs. Konrad Zuse konstruierte 1941 in
Deutschland mit der Z3 den ersten funktionsfähigen Computer 4
4Zu den Anforderungen an einen Computer, also an eine universelle, elektro-
nische Rechenmaschine gehören: Gespeicherte Programme, bedingte Sprünge
und die Trennung von Speicher und Prozessor.

### Seite 33

20 3 Grundlagen der Betriebssysteme
der Welt. Andere frühe Computer der ersten Generation entstanden
im weiteren Verlauf der 1940er Jahre in den USA (z. B. Atanasoff-
Berry-Computer, Mark I, ENIAC) sowie in England (Colossus).
Computer dieser Generation waren Maschinen mit teilweise mehr
als 10.000 Röhren oder Relais, die im Vergleich zu modernen
Computern langsam und fehleranfällig arbeiteten. Computer dieser
Generation wurden aus den genannten Gründen nicht für univer-
selle Zwecke, sondern nur für spezielle Aufgaben wie zum Bei-
spiel Flugbahnberechnungen oder zur Kryptoanalyse verwendet.
Betriebssysteme und auch Programmiersprachen waren zu jener
Zeit noch unbekannt5 und die Programme wurden von den Benut-
zer (Programmierern) über Steckfelder gesteckt, also direkt in der
Hardware implementiert.
3.3.1 Zweite Generation von Computern
Ab Anfang der 1950er Jahre lösten Lochkarten 6 (siehe Abb. 3.4)
die Steckfelder ab und durch die Einführung der Transistoren
ab Mitte der 1950er Jahre wurden die Computersysteme zuver-
lässiger. Auf Computern dieser zweiten Generation wurden Pro-
gramme in den Programmiersprachen Fortran oder COBOL von
Programmierern auf Formblätter aufgeschrieben, von Eingebern
bzw. Codierern in Lochkarten gestanzt und anschließend einem
Operator übergeben. Der Operator koordinierte die Reihenfolge
der Programme, bestückte den Computer mit den Lochkarten,
sorge dafür, dass der Compiler von einem Magnetband geladen
5In den 1940er Jahren entwickelte Konrad Zuse zusätzlich zu seinen Com-
putern die Programmiersprache Plankalkül. Da die Sprache praktisch nicht
eingesetzt wurde (Compiler dafür wurden erst Jahrzehnte später entwickelt),
hat sie primär historische Bedeutung.
6Jede Lochkarte stellt üblicherweise eine Zeile Programmtext mit 80 Zeichen
oder entsprechend viele binäre Daten dar. Das die Zeilenlänge von E-Mails
und Textdateien heute noch typischerweise 80 Zeichen beträgt, geht auf die
Lochkarte zurück. 12 Lochpositionen stehen für die Kodierung jedes Zeichens
zur Verfügung. Ziffern kodiert man mit einem einzelnen Loch in der entspre-
chenden Zeile. Buchstaben und Sonderzeichen kodiert man, indem mehrere
Löcher in die Spalte gestanzt werden.

### Seite 34

3.3 Entwicklung der Betriebssysteme 21
Abb. 3.4 Beispiel einer Lochkarte
wurde und übergab die Programmausgabe als Ausdruck an den
Auftraggeber. Diese Form der Softwareentwicklung und Program-
mausführung war bedingt durch die zahlreichen Zwischenschritte
und den beim Benutzer- und Prozesswechsel entstehenden Leer-
lauf inefﬁzient.
Das Sammeln der Programme auf Magnetbändern führte zu
einer efﬁzienteren Programmausführung, weil so das Einlesen
beschleunigt wurde. Betriebssysteme, die in dieser zweiten Gene-
ration verwendet wurden, ermöglichten ausschließlich Stapelver-
arbeitung (siehe Abschn.3.4.1) undEinzelprogrammbetrieb(siehe
Abschn. 3.4.2).
3.3.2 Dritte Generation von Computern
Ab den frühen 1960er Jahren ermöglichten integrierte Schaltun-
gen leistungsfähigere, kleinere und auch in der Herstellung billi-
gere Computer. Die Betriebssysteme zur Stapelverarbeitung wur-
den in den 1960er Jahren dahingehend erweitert, dass sie mehrere
Aufträge gleichzeitig abarbeiten konnten. Diese Fähigkeit heißt
Mehrprogrammbetrieb (siehe Abschn. 3.4.2) und erforderte erst-
mals eine einfache Speicherverwaltung (siehe Kap. 5).
Eine Aufgabe der Speicherverwaltung ist der sogenannte Spei-
cherschutz (siehe Abschn. 5.2.2). Dabei wird der Arbeitsspei-
cher aufgeteilt, um laufende Programme voneinander zu trennen.

### Seite 35

22 3 Grundlagen der Betriebssysteme
Dadurch beeinträchtigen Programmierfehler oder der Absturz ein-
zelner Programme nicht die Stabilität anderer Programme oder des
Gesamtsystems.
Weitere wichtige Funktionalitäten von Betriebssystemen, die
für die dritte Generation von Computersystemen entwickelt wur-
den, sind:
• Dateisysteme (siehe Kap. 6), die quasi-gleichzeitige Dateizu-
griffe erlauben und die Art und Weise der Datenspeicherung
auf den Laufwerken organisieren.
• Swapping (siehe Kap. 7), also das Ein- und Auslagern von
Daten in den/vom Arbeitsspeicher vom/in den Auslagerungs-
speicher (meist auf Festplatten oder SSDs).
• Scheduling (siehe Abschn. 8.6), also die automatische Erstel-
lung eines Ablaufplanes (englisch: Schedule), der Benutzern
bzw. Prozessen zeitlich begrenzte Ressourcen zuteilt.
Während der 1970er Jahre wurden die Computer dahingehend aus-
gebaut, dass mehrere Benutzer gleichzeitig über Dialogstationen
(Terminals) an einem Großrechner arbeiten konnten. Diese Form
der Arbeit heißt Dialogbetrieb (siehe Abschn. 3.4.1).
Die Entwicklung des Mikroprozessors Ende der 1970er Jahre
führte in den frühen 1980er Jahren zur Entwicklung der Heim-
computer (z. B. Apple II) und des IBM Personal Computers (PC).
Weitere bekannte Vertreter der dritten Generation sind CDC 6600,
IBM System/360, DEC PDP-8 und CRAY 1.
Einige Betriebssysteme aus der dritten Generation von Compu-
tersystemen sind IBM OS/360, Multics (der V orgänger von Unix),
Unics (später Unix) aus den Bell Laboratories, DEC VMS für DEC
V AX-Rechner und Version 6/7 Unix.
3.3.3 Vierte Generation von Computern
Die zunehmende Leistungsfähigkeit der Prozessoren und zuneh-
mende Speicherkapazität bei sinkenden Anschaffungskosten führ-
ten ab den frühen 1980er Jahren zu einer Etablierung der Personal

### Seite 36

3.4 Betriebsarten 23
Computer und Workstations im privaten, universitären und unter-
nehmerischen Umfeld. Eine zunehmend wichtige Aufgabe von
Betriebssystemen dieser Generation ist die Bereitstellung intuiti-
ver Benutzeroberﬂächen für die Benutzer, die immer weniger von
der zu Grunde liegenden Hardware wissen wollen.
Einige Betriebssysteme der vierten Generation sind Disk Ope-
rating Systeme wie QDOS (Quick and Dirty Operating System),
MS-DOS, IBM PC-DOS, Apple DOS und Atari DOS. Weitere Bei-
spiele sind Desktop-Betriebssysteme wie AmigaOS, Atari TOS,
Windows und Mac OS sowie Unix-ähnliche Systeme wie Micro-
soft Xenix, SGI IRIX, SunOS, IBM AIX, NeXTSTEP, das GNU-
Projekt und Linux.
3.4 Betriebsarten
Die Betriebssysteme lassen sich anhand der Betriebsarten Stapel-
betrieb und Dialogbetrieb, Einzelprogrammbetrieb und Mehrpro-
grammbetrieb sowie Einzelbenutzerbetrieb und Mehrprogramm-
betrieb klassiﬁzieren.
3.4.1 Stapelbetrieb und Dialogbetrieb
Stapelverarbeitung (englisch: Batch Processing) heißt auch Sta-
pelbetrieb oder Batchbetrieb. Bei dieser Betriebsart muss jedes
Programm mit allen Eingabedaten vollständig vorliegen, bevor die
Abarbeitung beginnen kann. Auch heutige Systeme ermöglichen
Stapelverarbeitung, zum Beispiel in Form von Batch-Dateien oder
Shell-Skripten. Speziell zur Ausführung von Routineaufgaben ist
diese Form des Stapelbetriebs ein nützliches Werkzeug. Üblicher-
weise ist Stapelbetrieb interaktionslos. Nach dem Start eines Pro-
gramms wird dieses bis zum Ende oder Auftreten eines Fehlers
ohne Interaktion mit dem Benutzer abgearbeitet. Ein Ziel des Sta-
pelbetriebs ist die maximale Prozessorausnutzung.
Abb.3.5 zeigt die Beschleunigung durch Automatisierung, die
Stapelbetrieb ermöglicht. Durch den Stapelbetrieb geht keine
Rechenleistung durch Benutzerwechsel verloren. Allerdings wird

### Seite 37

24 3 Grundlagen der Betriebssysteme
Abb. 3.5 Vergleich von Einzelbenutzerbetrieb mit Einzelprogrammbetrieb
ohne Stapelbetrieb und mit Stapelbetrieb [62]
auch bei dieser dargestellten Variante des Stapelbetriebs der Haupt-
prozessor noch nicht optimal ausgenutzt, denn dieser liegt während
der Ein-/Ausgabe brach.
Das in Abb.3.6 dargestellte System ist ein Beispiel für ein kom-
plexes System zur Datenverarbeitung aus den 1960er Jahren mit
Stapelbetrieb und optimaler Ausnutzung der Rechenleistung. In
diesem Szenario unterstützten ein V orrechner und ein Nachrech-
ner den eigentlichen Großrechner (Hauptrechner). Der V orrechner
schreibt die gesammelten Programme der Benutzer auf Magnet-
band. Der Nachrechner liest die gesammelten Ausgaben der Pro-
gramme vom Magnetband und druckt diese aus. V on Band kann
schneller eingelesen werden als von Lochkarten, und auf Band
kann schneller geschrieben werden als auf Papier. V orrechner und
Nachrechner befreien den Großrechner somit von langsamer Ein-/
Abb. 3.6 Beispiel für ein System zur Datenverarbeitung mit Stapelbetrieb und
optimaler Ausnutzung der Rechenleistung [54]

### Seite 38

3.4 Betriebsarten 25
Ausgabearbeit. Die Entlastung des Hauptprozessors durch zusätz-
liche Hardware für Ein-/Ausgabeoperationen ist unter dem Begriff
Spooling bekannt. Durch Spooling geschieht die Ein-/Ausgabe
nebenläuﬁg zur Bearbeitung der übrigen Aufträge.
Auch moderne Computersysteme haben neben dem Hauptpro-
zessor spezielle, DMA-fähige (Direct Memory Access)
Ein-/Ausgabeprozessoren. Diese schreiben Daten direkt in den
Hauptspeicher und holen von dort die Ergebnisse. Zudem exis-
tieren sogenannte Spoolingprozesse zum Drucken.
Bei der BetriebsartDialogbetrieb (englisch: Time Sharing), die
auch Zeitteilbetrieb heißt, arbeiten mehrere Benutzer an einem
Computersystem gleichzeitig und konkurrierend, indem sie sich
die verfügbare Rechenzeit des Hauptprozessors teilen. Eine Her-
ausforderung hierbei ist die faire Verteilung der Rechenzeit. Dieses
geschieht mit Hilfe von Zeitscheiben (englisch: Time Slices). Die
Verteilung der Zeitscheiben an die Programme kann nach unter-
schiedlichen Scheduling-Verfahren (siehe Abschn.8.6) erfolgen.
Obwohl die Benutzer gleichzeitig über Terminals an einem
Computer interaktiv arbeiten, sind deren Programme durch den
Mehrprogrammbetrieb (siehe Abschn. 3.4.2) unabhängig vonein-
ander.
3.4.2 Einzelprogrammbetrieb und
Mehrprogrammbetrieb
Beim Einzelprogrammbetrieb (englisch: Singletasking)7 läuft zu
jedem Zeitpunkt nur ein einziges Programm.
Die quasi-parallele Programm- bzw. Prozessausführung heißt
Mehrprogrammbetrieb (englisch: Multitasking). Mehrere
Programme können gleichzeitig (bei mehreren Prozessoren bzw.
Rechenkernen) oder zeitlich verschachtelt (quasi-parallel) ausge-
führt werden. Die Prozesse werden in kurzen Abständen abwech-
selnd aktiviert. Dadurch entsteht der Eindruck der Gleichzeitigkeit.
7Der Begriff Task ist gleichzusetzen mit Prozess oder aus Anwendersicht Auf-
gabe bzw. Auftrag.

### Seite 39

26 3 Grundlagen der Betriebssysteme
Ein Nachteil des Mehrprogrammbetriebs ist das Umschalten von
Prozessen, welches einen Verwaltungsaufwand (Overhead) verur-
sacht.
Mehrprogrammbetrieb ist trotz des Verwaltungsaufwand sinn-
voll, denn Prozesse müssen häuﬁg auf äußere Ereignisse warten.
Gründe sind zum Beispiel Benutzereingaben, Eingabe/Ausgabe-
Operationen von Peripheriegeräten oder das Warten auf eine Nach-
richt eines anderen Programms. Durch Mehrprogrammbetrieb kön-
nen Prozesse, die auf ankommende E-Mails, erfolgreiche Daten-
bankoperationen, geschriebene Daten auf der Festplatte oder ähn-
liches warten, in den Hintergrund geschickt werden und andere
Prozesse kommen früher zum Einsatz.
Der Verwaltungsaufwand, der bei der quasiparallelen Abarbei-
tung von Programmen durch die Programmwechsel entsteht, ist
im Vergleich zum Geschwindigkeitszuwachs zu vernachlässigen.
3.4.3 Einzelbenutzerbetrieb und
Mehrbenutzerbetrieb
Beim Einzelbenutzerbetrieb (englisch: Single-User Mode ) steht
der Computer immer nur einem einzigen Benutzer zur Verfü-
gung. Es existieren Single-User-Betriebssysteme mit Single- und
mit Multitasking-Funktionalität. Beispiele für Betriebssysteme,
die ausschließlich Einzelbenutzerbetrieb bieten, sind MS-DOS,
Microsoft Windows 3x/95/98 und OS/2.
Beim Mehrbenutzerbetrieb (englisch: Multi-User Mode) kön-
nen mehrere Benutzer gleichzeitig mit dem Computer arbeiten. Die
Benutzer teilen sich hierbei die Systemleistung. Die Systemres-
sourcen müssen mit Hilfe geeigneter Scheduling-Methoden (siehe
Abschn. 8.6) möglichst gerecht verteilt werden. Die verschiedenen
Benutzer müssen (durch Passwörter) identiﬁziert und Zugriffe auf
Daten und Prozesse anderer Benutzer durch das Betriebssystem
verhindert werden. Beispiele für Betriebssysteme, die Mehrpro-
grammbetrieb ermöglichen, sind Linux und andere Unix-ähnliche
Systeme, Mac OS X, sowie die Server-Versionen der Microsoft
Windows NT-Familie. Dazu gehören auch die VersionenTerminal
Server und MultiPoint Server .

### Seite 40

3.5 8/16/32/64 Bit-Betriebssysteme 27
Tab. 3.2 Einordnung bekannter Betriebssysteme in die verschiedenen
Betriebsarten
Single-User Multi-User
Singletasking MS-DOS, Palm OS Unmöglich
Multitasking OS/2, Windows
3x/95/98,
BeOS, Mac OS. 8x/9x,
AmigaOS, Risc OS
Linux/UNIX,
Mac OS X,
Server-Versionen der
Windows NT-Familie
Tab.3.2 enthält eine Einordnung bekannter Betriebssysteme in
die Betriebsarten Einzelprogrammbetrieb und Mehrprogrammbe-
trieb sowie Einzelbenutzerbetrieb und Mehrprogrammbetrieb.
Eine Besonderheit sind die sogenannten halben Multi-User-
Betriebssysteme. Zu dieser Kategorie gehören beispielsweise die
Desktop/Workstation-Versionen von Microsoft Windows
NT/2000/XP/Vista/7/8/10. Bei diesen Betriebssystemen können
verschiedene Benutzer nur nacheinander am System arbeiten, aber
die Daten der verschiedenen Benutzer sind voreinander geschützt.
Mit inofﬁziellen Erweiterungen ist es auch möglich die Desktop/
Workstation-Versionen dahingehend zu erweitern, dass mehrere
Benutzer sich gleichzeitig via Remote Desktop Protocol (RDP)
am System anmelden können.
3.5 8/16/32/64 Bit-Betriebssysteme
Jedes Betriebssystem arbeitet intern mit Speicheradressen einer
bestimmten Länge. Moderne Betriebssysteme werden üblicher-
weise als 64 Bit-Betriebssysteme angeboten. Zahlreiche Linux-
Distributionen sowie Microsoft Windows werden speziell für ältere
Hardware zusätzlich noch als 32 Bit-Betriebssysteme angeboten.
Ein Betriebssystem kann nur so viele Speichereinheiten anspre-
chen, wie der Adressraum zulässt. Darum kann ein 64 Bit-
Betriebssystem mehr Speicher ansprechen als ein 32 Bit-
Betriebssystem. Die Größe des Adressraums hängt Hardwareseitig
allerdings vom Adressbus (siehe Abschn.4.1.3)a b .

### Seite 41

28 3 Grundlagen der Betriebssysteme
8 Bit-Betriebssysteme können 2 8 Speichereinheiten adressie-
ren. Beispiele für solche Betriebssysteme sind GEOS, Atari DOS
oder Contiki [13].
16 Bit-Betriebssysteme können 216 Speichereinheiten adressie-
ren. Beispiele für solche Betriebssysteme sind MS-DOS, Windows
3x und OS/2 1x.
32 Bit-Betriebssysteme können 232 Speichereinheiten adressie-
ren. Beispiele für solche Betriebssysteme sind Windows 95/98/
NT/Vista/7/8/10, OS/2 2/3/4, eComStation, BeOS, Linux und
Mac OS X bis einschließlich 10.7.
64 Bit-Betriebssysteme können 264 Speichereinheiten adressie-
ren. Beispiele für solche Betriebssysteme sind Windows 7/8/10 (64
Bit), Linux (64 Bit) und Mac OS X (64 Bit).
3.6 Echtzeitbetriebssysteme
Echtzeitbetriebssystemesind Betriebssysteme die Mehrprogramm-
betrieb mit zusätzlichen Echtzeit-Funktionen für die Einhaltung
von Zeitbedingungen bieten. Wesentliche Qualitätskriterien von
Echtzeitbetriebssystemen sind die Reaktionszeit und die Einhal-
tung von Zeitschranken (englisch: Deadlines).
Die existierenden Echtzeitbetriebssysteme können in die bei-
den Gruppen harte Echtzeitbetriebssysteme und weiche Echtzeit-
betriebssysteme unterschieden werden.
3.6.1 Harte und weiche Echtzeitbetriebssysteme
Harte Echtzeitbetriebssysteme müssen Zeitschranken unbedingt
einhalten. Verzögerungen können unter keinen Umständen akzep-
tiert werden, denn sie können zu katastrophalen Folgen und hohen
Kosten führen. Die Ergebnisse einer Prozessausführung sind unter
Umständen nutzlos, wenn die Bearbeitung des Prozesses zu spät
erfolgt. Einige Einsatzbeispiele für harte Echtzeitbetriebssysteme,
bei denen die Notwendigkeit der Einhaltung von Zeitschranken
eindeutig ist, sind Schweißroboter, Systeme in der Reaktorsteue-
rung, Antiblockiersysteme bei Fahrzeugen, Systeme zur Flugzeug-

### Seite 42

3.6 Echtzeitbetriebssysteme 29
steuerung und Überwachungssysteme auf der Intensivstation. Bei-
spiele für harte Echtzeitbetriebssysteme sind QNX4, VxWorks,
LynxOS und die Linux-Erweiterung RTLinux [68]. Dabei handelt
es sich um einen Echtzeit-Mikrokern, der das komplette Linux-
Betriebssystem als einen Prozess neben den Echtzeitprozessen
betreibt.
Bei weichen Echtzeitbetriebssystemen sind gewisse Toleran-
zen bei der Einhaltung von Zeitschranken erlaubt. Verzögerun-
gen führen zu akzeptablen Kosten. Einige Einsatzbeispiele für
weiche Echtzeitbetriebssysteme sind Telefonanlagen, Parkschein-
oder Fahrkartenautomaten oder Multimedia-Anwendungen wie
Audio/Video on Demand.
Weiches Echtzeitverhalten können alle aktuellen Desktop-
Betriebssysteme wie zum Beispiel Microsoft Windows, Apple
Mac OS X oder Linux für Prozesse mit hoher Priorität garan-
tieren. Wegen des unberechenbaren Zeitverhaltens durch Swap-
ping (siehe Abschn.5.2.2), Unterbrechungen (englisch:Interrupts)
durch Hardwarekomponenten, etc. kann von diesen Betriebssys-
temen aber kein hartes Echtzeitverhalten garantiert werden.
3.6.2 Architekturen von Echtzeitbetriebssystemen
Neben der Unterscheidung anhand der Einhaltung von Zeitschran-
ken, können Echtzeitbetriebssysteme auch anhand Ihrer Architek-
tur in verschiedene Gruppe eingeteilt werden.
Bei Echtzeitbetriebssystemen mit der Architektur Thin-Kernel
läuft der Betriebssystemkern selbst als Prozess mit niedrigster
Priorität. Der Echtzeitkern übernimmt das Scheduling. Die
Echtzeit-Prozesse werden mit der höchsten Priorität ausgeführt.
Der Zweck dieses V orgehens ist es, die Reaktionszeit zu minimie-
ren.
Verfügt ein Echtzeitbetriebssystemen über einen sogenannten
Nano-Kernel, bedeutet das, das neben dem Echtzeitkern weitere
Betriebssystemkerne laufen können (siehe Abb.3.7).
Die Fachbegriffe Pico-Kernel, Femto-Kernel und Atto-Kernel
sind Beispiele für Marketingbegriffe der Hersteller von
Echtzeitsystemen, um die geringe Größe ihrer Echtzeitkerne

### Seite 43

30 3 Grundlagen der Betriebssysteme
Abb. 3.7 Architekturen von Echtzeitbetriebssystemen mit Thin-Kernel und
Nano-Kernel
hervorzuheben. Die Größe des Betriebssystemkerns wird allge-
mein als Qualitätskriterium angesehen, da die Reduktion des Echt-
zeitkerns auf die wichtigsten Funktionalitäten die Wahrscheinlich-
keit von Fehlern minimieren soll.
3.7 Verteilte Betriebssysteme
Ein verteiltes Betriebssystem ist ein verteiltes System, das die Pro-
zesse auf mehreren unabhängigen Computern steuert. Die einzel-
nen Knoten bleiben den Benutzern und deren Prozessen verborgen
(siehe Abb. 3.8). Das System erscheint als ein einzelner großer
Computer. Dieses Prinzip ist im Bereich der verteilten Systeme
auch unter dem Fachbegriff des Single System Image [9] bekannt.
Einige Beispiele für verteilte Betriebssysteme sind:
• Amoeba. Dieses Betriebssystem wurde von Mitte der 1980er
Jahre bis Mitte der 1990er Jahre unter der Leitung von Andrew
S. Tanenbaum an der Freien Universität Amsterdam entwi-
ckelt [56]. Besonders hervorzuheben ist, dass die Programmier-
sprache Python ursprünglich für Amoeba entwickelt wurde [59].
• Inferno wurde ursprünglich in den Bell Laboratories entwickelt
und basiert auf dem Unix-Betriebssystem Plan 9. Im Gegensatz
zu anderen verteilten Betriebssystemen ersetzt Inferno nicht
das Betriebssystem, sondern setzt auf einem bereits existieren-
den Host-Betriebssystem auf. Dabei kann es sich um Micro-
soft Windows, Linux oder verschiedene Unix-Betriebssysteme
handeln. Die aktuelle Version (Inferno 4th edition) unterstützt

### Seite 44

3.7 Verteilte Betriebssysteme 31
Abb. 3.8 Architektur verteilter Betriebssysteme
zahlreiche Hardwarearchitekturen und wurde 2005 als freie
Software veröffentlicht. Anwendungen werden in der Sprache
Limbo programmiert. Diese produziert genau wie Java einen
Bytecode, den eine virtuelle Maschine ausführt. Das Betriebs-
system hat nur minimale Anforderungen an die Hardware. So
benötigt das Betriebssystem nur 1 MB Arbeitsspeicher [16].
• Rainbow von der Universität Ulm. Dieses ab Mitte der 2000er
Jahre entwickelte verteilte Betriebssystem realisiert das Kon-
zept eines gemeinsamen Speichers mit einem für alle verbun-
den Computer einheitlichen Adressraum, in dem Datenobjekte
abgelegt werden. Für Anwendungen ist es transparent, auf wel-
chem Computer im Cluster sich Objekte physisch beﬁnden.
Anwendungen können über einheitliche Adressen von jedem
Computer auf gewünschte Objekte zugreifen. Sollte sich das
Objekt physisch im Speicher eines entfernten Computers beﬁn-
den, sorgt Rainbow automatisch und transparent für eine Über-
tragung und lokale Bereitstellung auf dem bearbeitenden Com-
puter [58].
• Sprite, das von Mitte der 1980er Jahre bis Mitte der 1990er Jahre
an der University of California in Berkeley entwickelt wurde.
Dieses Betriebssystem verbindet Workstations in einer Art und
Weise, dass sie für die Benutzer wie ein einzelnes System mit
Dialogbetrieb (siehe Abschn.3.4.1) erscheinen [46]. Interessant

### Seite 45

32 3 Grundlagen der Betriebssysteme
ist auch, dass pmake, eine parallele Version des Werkzeugs
make, ursprünglich für Sprite entwickelt wurde.
Das Konzept der verteilten Betriebssysteme konnte sich nicht
durchsetzen. Die existierenden verteilten Betriebssysteme kamen
nicht über das Stadium von Forschungsprojekten hinaus. Ein
Grund war, dass das Ersetzen der etablierten Betriebssysteme nicht
sinnvoll erschien. Positiv anzumerken sind die zahlreichen Werk-
zeuge und Technologien, die quasi als Nebenprodukte entstanden
sind – wie Adressräume, die sich über mehrere unabhängige Com-
puter verteilen, die Programmiersprache Python oder das Werk-
zeug pmake, die heute in der Informatik einen festen Platz haben.
Um Anwendungen für Verbünde von Computern zu entwickeln,
existieren Bibliotheken wie zum Beispiel das Message Passing
Interface (MPI) [19], OpenSHMEM [11] oder Uniﬁed Parallel C
(UPC) [14]. MPI stellt ein von der Hardware unabhängiges Mes-
sage Passing, also Kommunikation basierend auf dem Versand von
Nachrichten, bereit (siehe Abb.3.9). Die beiden Lösungen OpenS-
HMEM und UPC ermöglichen den Aufbau eines partitionierten
globalen Adressraums über unabhängige Computer. Der Einsatz
solcher Bibliotheken ist eine leichtgewichtigere Lösung als die
Entwicklung und Installation vollständig neuer Betriebssysteme.
Abb. 3.9 Moderne Architektur verteilter Systeme

### Seite 46

3.8 Architektur des Betriebssystemkerns 33
3.8 Architektur des Betriebssystemkerns
Der Betriebssystemkern (englisch: Kernel) enthält die grundlegen-
den Funktionen des Betriebssystems. Er ist die Schnittstelle zur
Hardware des Computers.
Die grundlegenden Funktionalitäten sind bei allen Betriebssys-
temen gleich. Zu diesen gehört die Bereitstellung von Systemauf-
rufen, Funktionen zur Benutzerverwaltung und Prozessverwaltung
inklusive Festlegung der Ausführungsreihenfolge (englisch:Sche-
duling) und Interprozesskommunikation, ein Prozessumschalter
(englisch: Dispatcher), die nötigen Gerätetreiber, Funktionen zur
Speicherverwaltung und Dateisysteme zur Verwaltung von Dateien
auf Speicherlaufwerken.
Jedes vollständige Betriebssystem muss die genannten Funk-
tionalitäten erbringen. Die Entwickler der Betriebssysteme haben
gewisse Freiheiten bei der Positionierung der entsprechenden
Funktionen. Diese können entweder vom Betriebssystemkern
selbst oder von Prozessen, die in diesem Kontext auchDienst oder
Server heißen, außerhalb des Kerns erbracht werden. Dementspre-
chend werden die drei Architekturen monolithischer Kern, mini-
maler Kern und hybrider Kern unterschieden.
Eine konkrete Auswirkungen der Positionierung ist, dass Funk-
tionen, die sich im Betriebssystemkerns beﬁnden, vollen Hard-
warezugriff haben. Sie laufen im Adressraum des Kerns, dem
sogenannten Kernelmodus(siehe Abschn.7.1). Wird eine Funktion
hingegen außerhalb des Adressraums des Kerns ausgeführt, kann
diese nur auf ihren virtuellen Speicher, den sogenanntenBenutzer-
modus, zugreifen.
3.8.1 Monolithische Kerne
Ein monolithischer Betriebssystemkern enthält alle Funktionen
zur Erbringung der Funktionalitäten eines Betriebssystems (siehe
Abb.3.10).
Ein V orteil dieses Architekturprinzips ist, dass im Vergleich zu
allen anderen Architekturen weniger Prozesswechsel nötig sind.
Dadurch ist die Ausführungsgeschwindigkeit eines Betriebssys-

### Seite 47

34 3 Grundlagen der Betriebssysteme
Abb. 3.10 Architektur monolithischer und minimaler Kerne
tems mit einem monolithischen Kern besser als mit einem mini-
malen oder einem hybriden Kern. Zudem haben Betriebssysteme
mit einem monolithischen Kern häuﬁg eine durch jahrelange Ent-
wicklungstätigkeit gewachsene Stabilität. Dadurch sind Betriebs-
systeme mit einem minimalen Kern in der Praxis nicht zwangsläu-
ﬁg stabiler als diejenigen mit einem monolithische Kern.
Nachteilig ist, dass abgestürzte Komponenten des Kerns nicht
separat neu gestartet werden können und eventuell das gesamte
Betriebssystem zum Absturz bringen. Zudem ist der Entwick-
lungsaufwand für Erweiterungen am Kern höher, da dieser bei
jedem Kompilieren komplett neu übersetzt werden muss. Eine
Möglichkeit, die genannten Nachteile abzumildern, ist die Verwen-
dung von sogenannten Modulen wie beim Linux-
Betriebssystemkern.
Bei Linux können bestimmte Funktionen wie beispielsweise
Hardware- und Dateisystem-Treiber in Module auslagert werden.
Diese werden jedoch im Kernelmodus und nicht im Benutzermo-
dus ausgeführt. Darum ist der Linux-Kern ein monolithischer Kern.
Weitere Beispiele für Betriebssysteme mit monolithischem Kern
sind verschiedene Varianten der Berkeley Software Distribution
(BSD), MS-DOS, FreeDOS, Windows 95/98/ME, Mac OS (bis
Version 8.6) und OS/2.

### Seite 48

3.8 Architektur des Betriebssystemkerns 35
3.8.2 Minimale Kerne
In minimalen Betriebssystemkernen, die auch Mikrokern oder
Mikrokernel heißen, beﬁnden sich üblicherweise nur die nötigs-
ten Funktionen zur Speicher- und Prozessverwaltung sowie zur
Synchronisation und Interprozesskommunikation. Gerätetreiber,
Treiber für Dateisysteme und alle weiteren Funktionalitäten lau-
fen als sogenannte Dienste bzw. Server außerhalb des Kerns im
Benutzermodus (siehe Abb.3.10).
Die V orteile dieses Architekturprinzips sind, dass aus dem Kern
ausgelagerte Funktionalitäten leichter austauschbar sind. Theore-
tisch bietet ein minimaler Kern eine bessere Stabilität und Sicher-
heit, weil weniger Funktionen im Kernelmodus laufen.
Nachteilig ist, dass das Architekturprinzip der minimalen Kerne
im Vergleich zu allen anderen Architekturen die geringste Aus-
führungsgeschwindigkeit bietet, weil es gleichzeitig die größte
Anzahl an benötigten Prozesswechseln aufweist. Zudem ist die
Entwicklung eines neuen Betriebssystemkerns eine komplexe und
zeitintensive Entwicklung die große ﬁnanzielle Ressourcen oder
großen Enthusiasmus freiwilliger Entwickler benötigt. Aus Sicht
der Benutzer oder Kunden eines Betriebssystems ist die Architek-
tur des Betriebssystemkerns auch kaum ein entscheidendes Krite-
rium, da die Architektur keine Auswirkung auf den Funktionsum-
fang hat.
Ein Beispiel, das die Komplexität der Entwicklung eines neuen
minimalen Kerns veranschaulicht, ist der Kernel GNU Hurd, der
seit den frühen 1990er Jahren für das Betriebssystem GNU entwi-
ckelt wird. Letztlich war es auch das Fehlen eines funktionierenden
Hurd-Kerns und die Probleme bei dessen Entwicklung, die 1991
einen ﬁnnischen Studenten der Informatik mit dem Namen Linus
Torvalds dazu motivierten, die Entwicklung an einem eigenen (der
Einfachheit halber monolithischen) Betriebssystemkern und damit
am Betriebssystem Linux zu starten.
Beispiele für Betriebssysteme mit eine minimalen Kern sind
AmigaOS, MorphOS, Tru64, das Echtzeitbetriebssystem QNX
Neutrino, Symbian, Minix, GNU HURD und das verteilte Betriebs-
system Amoeba.

### Seite 49

36 3 Grundlagen der Betriebssysteme
3.8.3 Hybride Kerne
Ein Kompromiss zwischen monolithischen Kernen und minima-
len Kernen sind die hybriden Kerne, die auchMakrokernel heißen.
Diese enthalten aus Geschwindigkeitsgründen Komponenten, die
bei minimalen Kernen außerhalb des Kerns liegen. Es ist nicht spe-
ziﬁziert, welche Komponenten bei Systemen mit hybriden Kernen
zusätzlich in den Kernel einkompiliert sind.
V orteile hybrider Kerne sind, dass sie theoretisch eine höhere
Geschwindigkeit als minimale Kerne ermöglichen und das sie im
Vergleich zu monolithischen Kernen eine höhere Stabilität bieten.
Die V or- und Nachteile hybrider Kerne zeigt das Beispiel von
Windows NT 4. Bei diesem Betriebssystem aus dem Jahr 1996
enthält der Betriebssystemkern das Graﬁksystem [ 41]. Ein posi-
tiver Effekt war eine verbesserte Leistung bei der Graﬁkausgabe.
Nachteilig war allerdings, dass fehlerhafte Graﬁktreiber zu häu-
ﬁgen Abstürzen führen. Da der Marktanteil von NT 4 geringer
war als der von Windows 95/98, lag der Fokus der Hersteller von
Graﬁkkarten auch nicht in der Verbesserung der Graﬁktreiber für
NT 4.
Beispiele für Betriebssysteme mit hybriden Kernen sind Win-
dows seit NT 3.1, ReactOS, Apple Mac OS X, BeOS, ZETA,
Haiku, Plan 9 und DragonFly BSD.
3.9 Schichtenmodell
In der Literatur (z. B. bei [ 54] und bei [ 62]) ist es ein etabliertes
Verfahren, die Komponenten von Betriebssystemen mit Schichten-
modellen zu visualisieren. Dabei werden die Betriebssysteme mit
ineinander liegenden Schichten logisch strukturiert. Die Schichten
umschließen sich gegenseitig und enthalten von innen nach außen
immer abstraktere Funktionen (siehe Abb.3.11).
Das Minimum für eine sinnvolle Darstellung sind drei Schich-
ten. Die innerste Schicht enthält diejenigen Teile des Betriebs-
systems, die abhängig von der Hardware sind. Betriebssysteme
können nur durch Anpassungen in der innersten Schicht an unter-
schiedliche Computerarchitekturen angepasst werden. Die mittlere

### Seite 50

3.9 Schichtenmodell 37
Abb. 3.11 Die Schichten enthalten von innen nach außen immer abstraktere
Funktionen [62]
Schicht enthält grundlegende Ein-/Ausgabe-Dienste für Geräte
und Daten. Dabei handelt es sich um Bibliotheken und Schnittstel-
len [62]. Die äußerste Schicht enthält die Anwendungsprogramme
und die Benutzerschnittstelle. Meist stellt man Betriebssysteme
wie in Abb.3.12 mit mehr als drei logischen Schichten dar.
Jede Schicht kommuniziert mit benachbarten Schichten über
wohldeﬁnierte Schnittstellen, kann Funktionen der nächst inneren
Schicht aufrufen und stellt Funktionen der nächst äußeren Schicht
zur Verfügung. Alle Funktionen (die sogenannten Dienste), die
eine Schicht anbietet, und die Regeln, die dabei einzuhalten sind,
heißen zusammenProtokoll.In der Praxis wird die Einschränkung,
Abb. 3.12 Visuelle Darstellung der Komponenten von Linux und allgemein
Unix-ähnlichen Betriebssystemen mit einem Schichtenmodell

*... weitere 248 Seiten nicht angezeigt*
