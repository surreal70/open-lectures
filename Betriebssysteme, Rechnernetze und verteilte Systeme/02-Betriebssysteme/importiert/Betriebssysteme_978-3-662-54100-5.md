---
author: Andreas Hümmer
title: "Betriebssysteme_978-3-662-54100-5"
tags:
  - content
  - importiert
  - bs
created: '2026-10-07'
modified: '2026-10-07'
bereich: BS
typ: sonstig
quelle: "Betriebssysteme_978-3-662-54100-5.pdf"
seiten: 496
---
author: Andreas Hümmer

# Betriebssysteme_978-3-662-54100-5

> [!info] Dokumentinformationen
> - **Quelle:** Betriebssysteme_978-3-662-54100-5.pdf
> - **Typ:** sonstig
> - **Bereich:** BS
> - **Seiten:** 496

---
author: Andreas Hümmer

## Inhalt

### Seite 2

Betriebssysteme

### Seite 3

Rüdiger Brause
Betriebssysteme
Grundlagen und Konzepte
4., erweiterte Auflage

### Seite 4

Rüdiger Brause
J.W. Goethe-Universität Frankfurt am Main
Frankfurt
Hessen
Deutschland
ISBN 978-3-662-54099-2       ISBN 978-3-662-54100-5 (eBook)
DOI 10.1007/978-3-662-54100-5
Gedruckt auf säurefreiem und chlorfrei gebleichtem Papier
Springer Vieweg ist Teil von Springer Nature
Die eingetragene Gesellschaft ist Springer-Verlag GmbH Deutschland
Die Anschrift der Gesellschaft ist: Heidelberger Platz 3, 14197 Berlin, Germany
Das Werk einschließlich aller seiner Teile ist urheberrechtlich geschützt. Jede Verwertung, die nicht ausdrücklich
vom Urheberrechtsgesetz zugelassen ist, bedarf der vorherigen Zustimmung des Verlags. Das gilt insbesondere
für Vervielfältigungen, Bearbeitungen, Übersetzungen, Mikroverfilmungen und die Einspeicherung und Ver -
arbeitung in elektronischen Systemen.
Die Wiedergabe von Gebrauchsnamen, Handelsnamen, Warenbezeichnungen usw. in diesem Werk berechtigt
auch ohne besondere Kennzeichnung nicht zu der Annahme, dass solche Namen im Sinne der Warenzeichen-
und Markenschutz-Gesetzgebung als frei zu betrachten wären und daher von jedermann benutzt werden dürften.
Der Verlag, die Autoren und die Herausgeber gehen davon aus, dass die Angaben und Informationen in diesem
Werk zum Zeitpunkt der Veröffentlichung vollständig und korrekt sind. Weder der Verlag, noch die Autoren oder
die Herausgeber übernehmen, ausdrücklich oder implizit, Gewähr für den Inhalt des Werkes, etwaige Fehler
oder Äußerungen. Der Verlag bleibt im Hinblick auf geografische Zuordnungen und Gebietsbezeichnungen in
veröffentlichten Karten und Institutionsadressen neutral.
Springer Vieweg
© Springer-Verlag GmbH Deutschland 1998, 2001, 2004, 2017
Die Deutsche Nationalbibliothek verzeichnet diese Publikation in der Deutschen Nationalbibliografie; detail -
lierte bibliografische Daten sind im Internet über http://dnb.d-nb.de abrufbar.
Die Darstellung von manchen Formeln und Strukturelementen war in einigen elektronischen Aus -
gaben nicht korrekt, dies ist nun korrigiert. Wir bitten damit verbundene Unannehmlichkeiten zu
entschuldigen und danken den Lesern für Hinweise.

### Seite 5

V
Vorwort
Betriebssysteme sind sehr, sehr beharrlich – fast kein Systemprogrammierer oder Infor -
matiker wird zeit seines Lebens mit der Aufgabe konfrontiert werden, ein komplett neues
Betriebssystem zu schreiben. Wozu dient dann dieses Buch?
Seine Zielsetzung besteht hauptsächlich darin, Verständnis für die innere Struktur der
heutigen komplexen Betriebssysteme zu wecken. Erst das Wissen um grundsätzliche Auf-
gaben und mögliche Alternativen versetzt Informatiker in die Lage, mögliche leistungs-
hemmende Strukturen ihres Betriebssystems zu erkennen und die Wirkung von Änderun-
gen in den vielen Parametern und Konfigurationen abzuschätzen.
Statt eine komplette analytische Erfassung der Systemleistung vorzugaukeln, die meist
nur über spezielle Simulations- und Leistungsmessprogramme möglich ist, konzentriert
sich das Buch darauf, gedankliche Konzepte und Methoden zu vermitteln, die in der Praxis
wichtig sind und in eigenen Programmen auch angewendet werden können.
Angesichts der vielfältigen Veränderungen der Betriebssystemlandschaft durch die Ver-
netzung der Rechner und die Vielzahl parallel eingesetzter Prozessoren ist es schwierig,
einen klassischen Text über Betriebssysteme zu verfassen, ohne Rechnernetze und Multi-
prozessorsysteme einzubeziehen. Andererseits ist ein Verständnis dieser Funktionen ohne
die klassischen Betriebssystemthemen nicht möglich. Aus diesem Grund geht das Buch
auf beide Seiten ein: Ausgehend von der klassischen Einprozessorsituation über die Mehr-
prozessorproblematik behandelt es die klassischen Themen wie Prozesse, Speicherver -
waltung und Ein-/Ausgabeverwaltung. Über die klassischen Themen hinaus wendet es
sich den Netzwerkdiensten, dem Thema Sicherheit und den Benutzeroberflächen zu; alle
drei gehören zu einem modernen Betriebssystem.
Dabei werden sowohl Einprozessor- als auch Mehrprozessorsysteme betrachtet und die
Konzepte an existierenden Betriebssystemen verdeutlicht. Viele Mechanismen der verteil-
ten Betriebssysteme und Echtzeitsysteme werden bereits in diesem Buch vorgestellt, um
damit eine spätere Vertiefung im Bedarfsfall zu erleichtern.
Im Unterschied zu manch anderen Betriebssystembüchern steht bei den Beispielen
kein eigenes Betriebssystem im V ordergrund; auch die Beispiele in Pseudocode sind
nicht als vollständige Programmoduln eines Betriebssystems gedacht. Bei einem solchen
Ansatz käme entweder die Darstellung der Konzepte zu kurz, oder das Buch müsste
wesentlich länger sein, ohne mehr aussagen zu können. Aus der Fülle der existierenden

### Seite 6

VI Vorwort
experimentellen und kommerziellen Systeme konzentriert sich das Buch deshalb auf die
in der Praxis wichtigsten Systeme wie UNIX und Windows NT und benennt die für das
jeweilige Konzept wesentlichen Prozeduren. Die detaillierte Dokumentation der Benut-
zerschnittstellen bleibt allerdings aus Platzgründen den einschlägigen Handbüchern der
Softwaredokumentation vorbehalten und wurde deshalb hier nicht aufgenommen.
Ein spezieller Aspekt des Buches ist den Lernenden gewidmet: Zusätzlich zu den
Übungs- und Verständnisaufgaben sind Musterlösungen am Ende des Buches enthalten.
Außerdem sind alle wichtigen Begriffe bei der Einführung fett gedruckt, um die Unsicher-
heit beim Aneignen eines fremden Stoffes zu verringern; Fachwörter und englische Ori-
ginalbegriffe sind durch Kursivschrift gekennzeichnet. Wo immer es möglich und nötig
erschien, sollen Zeichnungen das Verständnis des Textes erleichtern.
Dazu kommen noch für den Lernenden und Lehrenden die V orlesungsvideos, Übungs-
fragen, Klausuren und V ortragsfolien, welche die Verwendung des Buches erleichtern
sollen. Sie sind elektronisch direkt unter der URL http://www.asa.cs.uni-frankfurt.de/bs/
herunterladbar.
Ich hoffe, mit den aktuellen Verbesserungen und Ergänzungen der vierten Auflage
alle Interessierte motiviert zu haben, sich mit dem Unterbau unseres Computerzeitalters
genauer zu beschäftigen. Dabei sollen aber nicht die vielen kritischen Anmerkungen und
Hinweise vieler Menschen unterschlagen werden, deren Beiträge dieses Buch erst reifen
ließen. Neben den Tutoren und V orlesungsteilnehmern möchte ich mich dabei besonders
bei Herrn Eric Hutter bedanken, der durch seine ausführlichen Anmerkungen die neueste
Edition entscheidend verbessert hat.
Rüdiger BrauseFrankfurt, im November 2016

### Seite 7

VII
Inhaltsverzeichnis
1 Übersicht  .........................................................  1
1.1 Einleitung: Was ist ein Betriebssystem? .............................  2
1.2 Betriebssystemschichten  .........................................  2
1.3 Betriebssystemaufbau  ...........................................  4
1.3.1 Systemaufrufe  ...........................................  5
1.3.2 Beispiel UNIX ...........................................  6
1.3.3 Beispiel Mach  ...........................................  7
1.3.4 Beispiel Windows NT .....................................  8
1.4 Schnittstellen und virtuelle Maschinen .............................. 11
1.5 Software-Hardware-Migration ..................................... 15
1.6 Virtuelle Betriebssysteme ........................................ 16
1.6.1 Paravirtualisierung ........................................ 18
1.6.2 Virtualisierung mit BS-Containern ........................... 19
1.6.3 V ollständige Virtualisierung ................................. 19
1.6.4 Hardware-Virtualisierung  .................................. 19
1.6.5 Virtualisierungserweiterungen ............................... 20
1.7 Betriebssysteme für eingebettete Systeme ............................ 21
1.8 Betriebssysteme in Mehrprozessorarchitekturen ....................... 22
1.9 Aufgaben  ..................................................... 25
Literatur ........................................................... 26
2 Prozesse  .......................................................... 27
2.1 Prozesszustände ................................................ 29
2.1.1 Beispiel UNIX ........................................... 30
2.1.2 Beispiel Windows NT ..................................... 33
2.1.3 Leichtgewichtsprozesse .................................... 34
2.1.4 Aufgaben  ............................................... 37
2.2 Prozessscheduling  .............................................. 39
2.2.1 Zielkonflikte ............................................. 40
2.2.2 Non-präemptives Scheduling ................................ 41
2.2.3 Präemptives Scheduling .................................... 44

### Seite 8

VIII Inhaltsverzeichnis
2.2.4 Mehrere Warteschlangen und Scheduler ......................  46
2.2.5 Scheduling in Echtzeitbetriebssystemen ......................  47
2.2.6 Scheduling in Multiprozessorsystemen .......................  53
2.2.7 Stochastische Schedulingmodelle ...........................  60
2.2.8 Beispiel UNIX: Scheduling ................................  62
2.2.9 Beispiel: Scheduling in Windows NT ........................  64
2.2.10 Aufgaben  ..............................................  65
2.3 Prozesssynchronisation  .........................................  67
2.3.1 Race conditions und kritische Abschnitte .....................  68
2.3.2 Signale, Semaphore und atomare Aktionen ....................  69
2.3.3 Beispiel UNIX: Semaphore ................................  77
2.3.4 Beispiel Windows NT: Semaphore ..........................  78
2.3.5 Anwendungen  ..........................................  79
2.3.6 Aufgaben zur Prozesssynchronisation ........................  85
2.3.7 Kritische Bereiche und Monitore ............................  88
2.3.8 Verklemmungen .........................................  92
2.3.9 Aufgaben zu Verklemmungen .............................. 101
2.4 Prozesskommunikation  ......................................... 103
2.4.1 Kommunikation mit Nachrichten. . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
2.4.2 Beispiel UNIX: Interprozesskommunikation mit pipes ........... 107
2.4.3 Beispiel Windows NT: Interprozesskommunikation mit pipes ..... 108
2.4.4 Prozesssynchronisation durch Kommunikation ................. 108
2.4.5 Implizite und explizite Kommunikation ...................... 117
2.4.6 Aufgaben zur Prozesskommunikation ........................ 118
Literatur .......................................................... 118
3 Speicherverwaltung  ............................................... 121
3.1 Direkte Speicherbelegung ....................................... 122
3.1.1 Zuordnung durch feste Tabellen  ............................ 123
3.1.2 Zuordnung durch verzeigerte Listen ......................... 123
3.1.3 Belegungsstrategien ...................................... 125
3.1.4 Aufgaben zur Speicherbelegung ............................ 128
3.2 Logische Adressierung und virtueller Speicher ....................... 129
3.2.1 Speicherprobleme und Lösungen ............................ 129
3.2.2 Der virtuelle Speicher  .................................... 130
3.3 Seitenverwaltung (paging) ....................................... 132
3.3.1 Prinzip der Adresskonversion .............................. 132
3.3.2 Adresskonversionsverfahren  ............................... 133
3.3.3 Gemeinsam genutzter Speicher (shared memory) ............... 137
3.3.4 Virtueller Speicher in UNIX und Windows NT ................. 138
3.3.5 Aufgaben zu virtuellem Speicher. . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
3.3.6 Seitenersetzungsstrategien ................................. 144

### Seite 9

Inhaltsverzeichnis IX
3.3.7 Modellierung und Analyse der Seitenersetzung  ................ 151
3.3.8 Beispiel UNIX: Seitenersetzungsstrategien .................... 159
3.3.9 Beispiel Windows NT: Seitenersetzungsstrategien .............. 161
3.3.10 Aufgaben zur Seitenverwaltung ............................. 162
3.4 Segmentierung ................................................ 164
3.5 Cache ....................................................... 167
3.6 Speicherschutzmechanismen ..................................... 170
3.6.1 Speicherschutz in UNIX  .................................. 171
3.6.2 Speicherschutz in Windows NT ............................. 172
3.6.3 Sicherheitsstufen und virtual mode .......................... 173
Literatur .......................................................... 174
4 Dateiverwaltung  .................................................. 175
4.1 Dateisysteme  ................................................. 176
4.2 Dateinamen  .................................................. 178
4.2.1 Dateitypen und Namensbildung ............................. 178
4.2.2 Pfadnamen  ............................................. 182
4.2.3 Beispiel UNIX: Der Namensraum ........................... 183
4.2.4 Beispiel Windows NT: Der Namensraum ..................... 185
4.2.5 Aufgaben  .............................................. 187
4.3 Dateiattribute und Sicherheitsmechanismen ......................... 188
4.3.1 Beispiel UNIX: Zugriffsrechte  ............................. 188
4.3.2 Beispiel Windows NT: Zugriffsrechte ........................ 190
4.3.3 Aufgaben  .............................................. 191
4.4 Dateifunktionen ............................................... 192
4.4.1 Standardfunktionen  ...................................... 192
4.4.2 Beispiel UNIX: Dateizugriffsfunktionen ...................... 193
4.4.3 Beispiel Windows NT: Dateizugriffsfunktionen ................ 194
4.4.4 Strukturierte Zugriffsfunktionen ............................ 195
4.4.5 Gemeinsame Nutzung von Bibliotheksdateien ................. 202
4.4.6 Speicherabbildung von Dateien (memory mapped files) .......... 204
4.4.7 Besondere Dateien (special files) ............................ 206
4.4.8 Aufgaben zu Dateikonzepten ............................... 207
4.5 Implementierung der Dateiorganisation  ............................ 209
4.5.1 Kontinuierliche Speicherzuweisung  ......................... 209
4.5.2 Listenartige Speicherzuweisung  ............................ 210
4.5.3 Zentrale indexbezogene Speicherzuweisung ................... 210
4.5.4 Verteilte indexbezogene Speicherzuweisung ................... 212
4.5.5 Beispiel UNIX: Implementierung des Dateisystems ............. 213
4.5.6 Beispiel Windows NT: Implementierung des Dateisystems ....... 215
4.5.7 Aufgaben zu Dateiimplementierungen  ....................... 219
Literatur .......................................................... 219

### Seite 10

X Inhaltsverzeichnis
5 Ein- und Ausgabeverwaltung ........................................ 221
5.1 Die Aufgabenschichtung ........................................ 222
5.1.1 Beispiel UNIX: I/O-Verarbeitungsschichten ................... 224
5.1.2 Beispiel Windows NT: I/O-Verarbeitungsschichten ............. 227
5.2 Gerätemodelle  ................................................ 229
5.2.1 Geräteschnittstellen  ...................................... 230
5.2.2 Initialisierung der Geräteschnittstellen  ....................... 231
5.2.3 Plattenspeicher .......................................... 231
5.2.4 SSD-RAM-Disks ........................................ 237
5.2.5 Serielle Geräte .......................................... 239
5.2.6 Aufgaben zu I/O ......................................... 240
5.3 Multiple Plattenspeicher: RAIDs .................................. 240
5.3.1 RAID-Ausfallwahrscheinlichkeiten .......................... 246
5.3.2 Aufgaben zu RAID  ...................................... 248
5.4 Modellierung und Implementierung der Treiber ...................... 249
5.4.1 Beispiel UNIX: Treiberschnittstelle .......................... 250
5.4.2 Beispiel Windows NT: Treiberschnittstelle .................... 252
5.4.3 I/O Treiber in Großrechnern  ............................... 255
5.4.4 Aufgaben zu Treibern  .................................... 255
5.5 Optimierungsstrategien für Treiber ................................ 256
5.5.1 Optimierung bei Festplatten ................................ 256
5.5.2 Pufferung  .............................................. 257
5.5.3 Synchrone und asynchrone Ein- und Ausgabe. . . . . . . . . . . . . . . . . . 259
5.5.4 Aufgaben zur Treiberoptimierung ........................... 261
Literatur .......................................................... 261
6 Netzwerkdienste  .................................................. 263
6.1 Das Schichtenmodell für Netzwerkdienste .......................... 269
6.2 Kommunikation im Netz ........................................ 274
6.2.1 Namensgebung im Netz ................................... 275
6.2.2 Kommunikationsanschlüsse ................................ 280
6.2.3 Aufgaben  .............................................. 288
6.3 Dateisysteme im Netz  .......................................... 289
6.3.1 Zugriffssemantik  ........................................ 289
6.3.2 Zustandsbehaftete und zustandslose Server .................... 291
6.3.3 Die Cacheproblematik .................................... 293
6.3.4 Implementationskonzepte  ................................. 295
6.3.5 Die WebDA V-Dienste .................................... 299
6.3.6 Sicherheitskonzepte ...................................... 300
6.3.7 Aufgaben  .............................................. 302
6.4 Massenspeicher im Netz  ........................................ 302
6.5 Arbeitsmodelle im Netz ......................................... 305

### Seite 11

Inhaltsverzeichnis XI
6.5.1 Jobmanagement ......................................... 305
6.5.2 Netzcomputer ........................................... 306
6.5.3 Schattenserver  .......................................... 309
6.5.4 Aufgaben zu Arbeitsmodellen im Netz ....................... 313
6.6 Middleware und SOA  .......................................... 314
6.6.1 Transparenz durch Middleware ............................. 315
6.6.2 Vermittelnde Dienste ..................................... 316
6.6.3 Service-orientierte Architektur  ............................. 318
6.6.4 Aufgaben zu Middleware .................................. 320
Literatur .......................................................... 321
7 Sicherheit ........................................................ 323
7.1 V orgeschichte ................................................. 324
7.2 Passworte .................................................... 324
7.2.1 Passwort erfragen ........................................ 325
7.2.2 Passwort erraten ......................................... 325
7.2.3 Passwort abhören ........................................ 326
7.3 Trojanische Pferde ............................................. 326
7.4 Der buffer overflow-Angriff ...................................... 327
7.5 Viren ........................................................ 328
7.5.1 Wie kann man einen eingeschleppten Virus entdecken? .......... 330
7.5.2  Was kann man dagegen tun, wenn man einen Virus im
System entdeckt hat? ...........................  . . . . . . . . . 330
7.5.3 Aufgaben zu Viren ....................................... 331
7.6 Rootkits  ..................................................... 332
7.6.1 User mode-Rootkits ...................................... 332
7.6.2 Kernel mode-Rootkits .................................... 333
7.6.3 Ring -1, Ring -2, Ring -3 Rootkits ........................... 334
7.6.4 Entdeckung und Bekämpfung der Rootkits .................... 335
7.7 Zugriffsrechte und Rollen ....................................... 336
7.7.1 Zugriffsrechte im Dateisystem .............................. 337
7.7.2 Zugriffsrechte von Systemprogrammen ....................... 337
7.7.3 Zugriffslisten und Fähigkeiten .............................. 338
7.7.4 Aufgaben  .............................................. 339
7.8 Vertrauensketten ............................................... 340
7.9 Sicherheit in Unix und Windows NT ............................... 341
7.10 Sicherheit im Netz: Firewall-Konfigurationen ........................ 343
7.11 Die Kerberos-Authentifizierung ................................... 345
7.11.1 Das Kerberos-Protokoll ................................... 346
7.11.2 Kerberos V or- und Nachteile ............................... 348
7.11.3 Aufgaben zur Netz-Sicherheit .............................. 349
Literatur .......................................................... 350

### Seite 12

XII Inhaltsverzeichnis
8 Benutzeroberflächen ............................................... 351
8.1 Das Design der Benutzeroberfläche ................................ 352
8.2 Die Struktur der Benutzeroberfläche ............................... 355
8.2.1 Eingaben  .............................................. 356
8.2.2 Rastergrafik und Skalierung ................................ 360
8.2.3 Fenstersysteme und Displaymanagement ..................... 362
8.2.4 Virtuelle Realität ........................................ 365
8.2.5 Das Management der Benutzeroberfläche ..................... 365
8.2.6 Aufgaben  .............................................. 367
8.3 Das UNIX-Fenstersystem: Motif und X-Window ..................... 368
8.3.1 Das Client-Server-Konzept von X-Window ................... 369
8.3.2 Das Fensterkonzept von X-Window ......................... 370
8.3.3 Dialogfenster und Widgets ................................. 371
8.3.4 Ereignisbehandlung ...................................... 373
8.3.5 Sicherheitsaspekte  ....................................... 374
8.4 Das Fenstersystem von Windows NT .............................. 375
8.4.1 Das Konzept der Benutzerschnittstelle  ....................... 375
8.4.2 Die Implementierung ..................................... 377
8.4.3 Aufgaben  .............................................. 379
Literatur .......................................................... 380
9 Musterlösungen ................................................... 381
9.1 Lösungen zu Kap. 1 ............................................ 381
9.2 Lösungen zu Kap. 2 ............................................ 386
9.3 Lösungen zu Kap. 3 ............................................ 416
9.4 Lösungen zu Kap. 4 ............................................ 428
9.5 Lösungen zu Kap. 5 ............................................ 439
9.6 Lösungen zu Kap. 6 ............................................ 448
9.7 Lösungen zu Kap. 7 ............................................ 455
9.8 Lösungen zu Kap. 8 ............................................ 460
Literatur .......................................................... 463
10 Anhang .......................................................... 465
10.1 Modellierung von Thrashing ..................................... 465
Weiterführende Literatur .............................................. 473
Stichwortverzeichnis .................................................. 475

### Seite 13

XIII
Über den Autor
Prof. Dr. rer. nat. habil. Rüdiger W. Brause V on 1970–1978 Studium der Physik und
Kybernetik in Saarbrücken und Tübingen mit Abschluß als Diplom-Physiker. 1980–1988
Konzeption und Implementierung des fehlertoleranten, lastverteilten Multi-Mikroprozes-
sorsystems ATTEMPTO in der Arbeitsgruppe von Prof. Dal Cin. 1983 Promotion mit
einer Arbeit zum Thema „Fehlertoleranz in verteilten Systemen“. Ab 1985 Akad. Oberrat
an der Universität Frankfurt. A. M. im Fachbereich Informatik, in dem er sich 1993 habili-
tierte. Ab 2005 Professor für Praktische Informatik. Im Ruhestand seit April 2016.

### Seite 14

XV
Abbildungsverzeichnis
Abb. 1.1 Benutzungsrelationen von Programmteilen . . . . . . . . . . . . . . . . . 3
Abb. 1.2 Schichtenmodell und Zwiebelschalenmodell  . . . . . . . . . . . . . . . . 3
Abb. 1.3 Die Sicherheitsstufen (Ringe) der Intel 80X86-Architektur . . . . . . . . . 4
Abb. 1.4 Überblick über die Rechnersoftwarestruktur. . . . . . . . . . . . . . . . . 4
Abb. 1.5 Befehlsfolge eines Systemaufrufs . . . . . . . . . . . . . . . . . . . . . . 5
Abb. 1.6 UNIX-Schichten . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
Abb. 1.7 Das Mach-Systemmodell. . . . . . . . . . . . . . . . . . . . . . . . . . . 8
Abb. 1.8 Schichtung und Aufrufe bei Windows NT . . . . . . . . . . . . . . . . . . 9
Abb. 1.9 Echte und virtuelle Maschinen . . . . . . . . . . . . . . . . . . . . . . . 11
Abb. 1.10 Hierarchie virtueller Maschinen . . . . . . . . . . . . . . . . . . . . . . 12
Abb. 1.11 Virtuelle, logische und physikalische Geräte. . . . . . . . . . . . . . . . 13
Abb. 1.12  Ein Netzwerk als virtueller Massenspeicher: die asymmetrische
Pool-Lösung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
Abb. 1.13 Software-Hardware-Migration des Java-Codes . . . . . . . . . . . . . . 15
Abb. 1.14 Virtualisierungsarten bei Servern. . . . . . . . . . . . . . . . . . . . . . 17
Abb. 1.15 Schichten bei der Paravirtualisierung  . . . . . . . . . . . . . . . . . . . 18
Abb. 1.16 Schichten bei der vollständigen Virtualisierung . . . . . . . . . . . . . . 20
Abb. 1.17 Hardwareerweiterung für die Virtualisierung . . . . . . . . . . . . . . . 21
Abb. 1.18 Programmentwicklung bei eingebetteten Systemen . . . . . . . . . . . . 22
Abb. 1.19 Ein Einprozessor- oder Mehrkernsystem. . . . . . . . . . . . . . . . . . 23
Abb. 1.20 Multiprozessor system . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
Abb. 1.21 Mehrrechnersystem. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
Abb. 1.22 Rechnernetz. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
Abb. 2.1 Zusammensetzung der Prozessdaten . . . . . . . . . . . . . . . . . . . . 28
Abb. 2.2 Prozesszustände und Übergänge . . . . . . . . . . . . . . . . . . . . . . 30
Abb. 2.3 Prozesszustände und Übergänge bei UNIX . . . . . . . . . . . . . . . . 31
Abb. 2.4 Erzeugung und Vernichten eines Prozesses in UNIX . . . . . . . . . . . 31
Abb. 2.5 Prozesszustände in Windows NT. . . . . . . . . . . . . . . . . . . . . . 33
Abb. 2.6 Ausführung der Prozesse in UNIX und Windows NT . . . . . . . . . . . 34
Abb. 2.7 I/O-Verhalten (a) leichter und (b) schwerer threads . . . . . . . . . . . . 36
Abb. 2.8 Langzeit- und Kurzzeitscheduling . . . . . . . . . . . . . . . . . . . . . 40

### Seite 15

XVI Abbildungsverzeichnis
Abb. 2.9 Job-Reihenfolgen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
Abb. 2.10 Präemptives Scheduling . . . . . . . . . . . . . . . . . . . . . . . . . . 44
Abb. 2.11 Scheduling mit mehreren Warteschlangen . . . . . . . . . . . . . . . . . 46
Abb. 2.12 Multi-level Scheduling . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
Abb. 2.13 Präzedenzgraph. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
Abb. 2.14 Gantt-Diagramm der Betriebsmittel . . . . . . . . . . . . . . . . . . . . 54
Abb. 2.15 Gantt-Diagramm bei der earliest scheduling-Strategie  . . . . . . . . . . 56
Abb. 2.16 Gantt-Diagramm bei latest scheduling-Strategie. . . . . . . . . . . . . . 56
Abb. 2.17 Optimaler Ablaufplan von drei Prozessen auf zwei Prozessoren  . . . . . 57
Abb. 2.18 Asymmetrisches und symmetrisches Multiprocessing . . . . . . . . . . . 59
Abb. 2.19 Multi-level-Warteschlangen in UNIX . . . . . . . . . . . . . . . . . . . 62
Abb. 2.20 Dispatcher ready queue in Windows NT. . . . . . . . . . . . . . . . . . 64
Abb. 2.21 Race conditions in einer Warteschlange . . . . . . . . . . . . . . . . . . 68
Abb. 2.22 Erster Versuch zur Prozesssynchronisation. . . . . . . . . . . . . . . . . 69
Abb. 2.23 Zweiter Versuch zur Prozesssynchronisation. . . . . . . . . . . . . . . . 70
Abb. 2.24 Prozesssynchronisation nach Peterson . . . . . . . . . . . . . . . . . . . 71
Abb. 2.25 Ein Beispiel für das Apartment-Modell in Windows NT. . . . . . . . . . 79
Abb. 2.26 Das Erzeuger-Verbraucher-Problem . . . . . . . . . . . . . . . . . . . . 81
Abb. 2.27 Lösung des Erzeuger-Verbraucher-Problems mit Semaphoren . . . . . . 82
Abb. 2.28 Der Ringpuffer des NYU-Ultracomputers . . . . . . . . . . . . . . . . . 84
Abb. 2.29 Ein- und Aushängen bei der ready-queue . . . . . . . . . . . . . . . . . 85
Abb. 2.30 Lösung des Erzeuger-Verbraucher-Problems mit einem Monitor . . . . . 90
Abb. 2.31 Ein Betriebs mittelgraph  . . . . . . . . . . . . . . . . . . . . . . . . . . 94
Abb. 2.32 Verbindungsarten. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
Abb. 2.33 Ablauf einer verbindungsorientierten Kommunikation . . . . . . . . . 104
Abb. 2.34 Interprozesskommunikation mit pipes in UNIX . . . . . . . . . . . . . 108
Abb. 2.35 POSIX- Signale. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
Abb. 2.36 Datenkonsistenz mit atomic broadcast-Nachrichten . . . . . . . . . . . 112
Abb. 2.37 Das Rendez-vous-Konzept . . . . . . . . . . . . . . . . . . . . . . . . 113
Abb. 2.38 Erzeuger-Verbraucher-Modell mit kommunizierenden Prozessen. . . . 115
Abb. 2.39 Fibonacci-Folge mittels nebenläufiger Berechnung in GO. . . . . . . . 115
Abb. 2.40 Producer-Consumer-System in GO  . . . . . . . . . . . . . . . . . . . 116
Abb. 3.1 Eine direkte Speicherbelegung und ihre Belegungstabelle. . . . . . . . 123
Abb. 3.2 Eine Speicherbelegung und die verzeigerte Belegungsliste . . . . . . . 124
Abb. 3.3 Visualisierung einer Speicherzuteilung im Buddy-System. . . . . . . . 126
Abb. 3.4 Die Abbildung physikalischer Speicherbereiche auf virtuelle
Bereiche  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
Abb. 3.5 Die Umsetzung einer virtuellen Adresse in eine physikalische
Adresse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
Abb. 3.6 Eine zweistufige Adresskonversion. . . . . . . . . . . . . . . . . . . . 135
Abb. 3.7 Zusammenfassung von Seitentabellen zu einer inversen Seitentabelle . 136
Abb. 3.8 Funktion eines assoziativen Tabellencache. . . . . . . . . . . . . . . . 136

### Seite 16

Abbildungsverzeichnis XVII
Abb. 3.9 Die Abbildung auf gemeinsamen Speicher. . . . . . . . . . . . . . . . 138
Abb. 3.10 Die Auslegung des virtuellen Adressraum bei Linux . . . . . . . . . . 139
Abb. 3.11 Die Unterteilung des virtuellen Adressraums in Windows NT 32 Bit . . 139
Abb. 3.12 Die optimale Seitenersetzung  . . . . . . . . . . . . . . . . . . . . . . 145
Abb. 3.13 Die FIFO-Seitenersetzung . . . . . . . . . . . . . . . . . . . . . . . . 145
Abb. 3.14 Der Clock-Algorithmus  . . . . . . . . . . . . . . . . . . . . . . . . . 147
Abb. 3.15 Die LRU-Seitenersetzung  . . . . . . . . . . . . . . . . . . . . . . . . 147
Abb. 3.16 Realisierung von LRU mit Schieberegistern . . . . . . . . . . . . . . . 148
Abb. 3.17 Die working set – Seitenersetzung bei Δt = 3  . . . . . . . . . . . . . . 150
Abb. 3.18 Die FIFO-Seitenersetzung . . . . . . . . . . . . . . . . . . . . . . . . 153
Abb. 3.19 Die FIFO-Seitenersetzung in Reihenfolge-Notation . . . . . . . . . . . 153
Abb. 3.20 Die LRU-Seitenersetzung  . . . . . . . . . . . . . . . . . . . . . . . . 154
Abb. 3.21 Überlappung von Rechen- und Seitentauschphasen bei tS > tw. . . . . . 155
Abb. 3.22 Überlappung von Rechen- und Seitentauschphasen bei tS < tw. . . . . . 155
Abb. 3.23 Das Nutzungsgradmodell. . . . . . . . . . . . . . . . . . . . . . . . . 157
Abb. 3.24 Die logische Unterteilung von Programmen . . . . . . . . . . . . . . . 164
Abb. 3.25 Segment-Speicherverwaltung beim Intel 80286 . . . . . . . . . . . . . 165
Abb. 3.26 Lokale und globale Seitentabellen beim INTEL 80486 . . . . . . . . . 165
Abb. 3.27 Benutzung eines pipeline-burst-Cache .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  167
Abb. 3.28 Adress- und Datenanschluss des Cache . . . . . . . . . . . . . . . . . 167
Abb. 3.29 Dateninkonsistenz bei unabhängigen Einheiten . . . . . . . . . . . . . 168
Abb. 4.1 Dateiorganisation als Tabelle. . . . . . . . . . . . . . . . . . . . . . . 177
Abb. 4.2 Hierarchische Dateiorganisation . . . . . . . . . . . . . . . . . . . . . 177
Abb. 4.3 Querverbindungen in Dateisystemen. . . . . . . . . . . . . . . . . . . 177
Abb. 4.4 Gültigkeit relativer Pfadnamen. . . . . . . . . . . . . . . . . . . . . . 183
Abb. 4.5 Querverbindungen und Probleme in UNIX  . . . . . . . . . . . . . . . 184
Abb. 4.6 Die Erweiterung des Dateisystems unter UNIX . . . . . . . . . . . . . 185
Abb. 4.7 Ergänzung der Namensräume in Windows NT. . . . . . . . . . . . . . 186
Abb. 4.8 Das pipe-System in UNIX . . . . . . . . . . . . . . . . . . . . . . . . 194
Abb. 4.9 Baumstruktur für zweistufigen, index-sequentiellen Dateizugriff . . . . 196
Abb. 4.10 Der Aufbau des B-Baums mit m = 5 . . . . . . . . . . . . . . . . . . . 198
Abb. 4.11 Der fertige Baum des Beispiels mit m = 5 . . . . . . . . . . . . . . . . 198
Abb. 4.12 Einfügen des Schlüssels „41“ im (a) B-Baum und (b) im B*-Baum  . . 201
Abb. 4.13 Mehrfachlisten einer sequentiellen Datei. . . . . . . . . . . . . . . . . 201
Abb. 4.14 Abbildung von Dateibereichen in den virtuellen Adressraum . . . . . . 204
Abb. 4.15 Speicherung von Dateien mittels Listen . . . . . . . . . . . . . . . . . 210
Abb. 4.16 Listenverzeichnis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 211
Abb. 4.17 Verteilung der Dateiindexliste auf die Dateiköpfe . . . . . . . . . . . . 212
Abb. 4.18 Mehrstufige Übersetzung von logischer zu physikalischer
Blocknummer. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 213
Abb. 4.19 Die Struktur einer i-node in UNIX . . . . . . . . . . . . . . . . . . . . 214
Abb. 4.20 Die Reihenfolge der ersten 16 Dateien, der NTFS-Metadata Files  . . . 216

### Seite 17

XVIII Abbildungsverzeichnis
Abb. 4.21 Die Struktur eines MFT-Eintrags. . . . . . . . . . . . . . . . . . . . . 216
Abb. 4.22 Die Dateistruktur des Wurzelverzeichnisses . . . . . . . . . . . . . . . 217
Abb. 4.23 Datenstrukturen für eine NTFS-Datei . . . . . . . . . . . . . . . . . . 218
Abb. 5.1 Grundschichten der Geräteverwaltung . . . . . . . . . . . . . . . . . . 223
Abb. 5.2 Die Schichtung und Schnittstellen des UDI-Treibers . . . . . . . . . . 224
Abb. 5.3 Die Dateisystemschichtung unter Linux . . . . . . . . . . . . . . . . . 224
Abb. 5.4 Beispiel für einen SystemFS-Dateibaum. . . . . . . . . . . . . . . . . 225
Abb. 5.5 Das Stream-System in UNIX. . . . . . . . . . . . . . . . . . . . . . . 226
Abb. 5.6 Einfache und multiple Schichtung in Windows NT . . . . . . . . . . . 227
Abb. 5.7 Ausfall eines Clusters in NTFS. . . . . . . . . . . . . . . . . . . . . . 229
Abb. 5.8 Ersatz eines Clusters in NTFS . . . . . . . . . . . . . . . . . . . . . . 229
Abb. 5.9 Adressraum, Controller und Gerät . . . . . . . . . . . . . . . . . . . . 230
Abb. 5.10 I/O-Port-Adressen der Standardperipherie eines PC . . . . . . . . . . . 230
Abb. 5.11 Plattenspeicheraufbau  . . . . . . . . . . . . . . . . . . . . . . . . . . 232
Abb. 5.12 Modellierungsfehler bei Suchzeit und Transferzeit
(nach Ruemmler 94) . . . . . . . . . . . . . . . . . . . . . . . . . . . 234
Abb. 5.13 Neugruppierung der Plattenbereiche in Streifen . . . . . . . . . . . . . 241
Abb. 5.14 Spiegelplattenkonfiguration zweier Platten  . . . . . . . . . . . . . . . 242
Abb. 5.15 Datenzuweisung beim RAID-2-System . . . . . . . . . . . . . . . . . 244
Abb. 5.16 Wechselseitige Abspeicherung der Fehlertoleranzinformation. . . . . . 245
Abb. 5.17 Die Zustände des Gesamtsystems und seine Einzelzustände  . . . . . . 246
Abb. 5.18 Entwicklung der Ausfallwahrscheinlichkeit eines Geräts . . . . . . . . 247
Abb. 5.19 Die Verbindung von Geräte- und Treiberobjekten . . . . . . . . . . . . 254
Abb. 6.1 Ein typisches lokales Netzwerk  . . . . . . . . . . . . . . . . . . . . . 264
Abb. 6.2 Subnetze und Backbone eines Intranets . . . . . . . . . . . . . . . . . 264
Abb. 6.3 Ein verteiltes Betriebssystem. . . . . . . . . . . . . . . . . . . . . . . 267
Abb. 6.4 Das Open System Interconnect (OSI)-Modell der International
Organization for Standardization (ISO, früher International Standards
Organization) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 270
Abb. 6.5 Die Kapselung der Daten und Kontrollinformationen . . . . . . . . . . 271
Abb. 6.6 Oft benutzte Protokollschichten in UNIX . . . . . . . . . . . . . . . . 272
Abb. 6.7 OSI-Modell und Windows NT-Netzwerkkomponenten . . . . . . . . . 273
Abb. 6.8 Virtual Private Network . . . . . . . . . . . . . . . . . . . . . . . . . 273
Abb. 6.9 Ein homogener Dateibaum im lokalen Netz . . . . . . . . . . . . . . . 278
Abb. 6.10 Lokale, inhomogene Sicht des Dateibaums . . . . . . . . . . . . . . . 279
Abb. 6.11 Auflösung von Netzwerk-Dateianfragen . . . . . . . . . . . . . . . . . 280
Abb. 6.12 Zuordnung von Portnummern und Diensten . . . . . . . . . . . . . . . 281
Abb. 6.13 Kommunikation über Transportendpunkte. . . . . . . . . . . . . . . . 282
Abb. 6.14 Kommunikationsablauf im Socket-Konzept . . . . . . . . . . . . . . . 282
Abb. 6.15 Das Transportschema eines RPC. . . . . . . . . . . . . . . . . . . . . 285
Abb. 6.16 Ablauf eines synchronen RPC . . . . . . . . . . . . . . . . . . . . . . 286
Abb. 6.17 Die big endian- und little endian-Bytefolgen  . . . . . . . . . . . . . . 286

### Seite 18

Abbildungsverzeichnis XIX
Abb. 6.18 Die Schichtung der RPC in Windows NT . . . . . . . . . . . . . . . . 288
Abb. 6.19 Der V organg zum Sperren einer Datei . . . . . . . . . . . . . . . . . . 292
Abb. 6.20 Übertragungsschichten und Pufferorte für Dateizugriffe im Netz . . . . 294
Abb. 6.21 Cachekohärenz bei gleichen und unterschiedlichen Puffern . . . . . . . 294
Abb. 6.22 Implementierung eines Netzdateiservers auf Prozessebene . . . . . . . 296
Abb. 6.23 Implementierung eines Netzdateiservers auf Treiberebene . . . . . . . 296
Abb. 6.24 Die Architektur des NFS-Dateisystems . . . . . . . . . . . . . . . . . 297
Abb. 6.25 Implementierung des Netzdateisystems in Windows NT . . . . . . . . 298
Abb. 6.26 Ein Speicher netzwerk  . . . . . . . . . . . . . . . . . . . . . . . . . . 303
Abb. 6.27 Das SAN Schichtenmodell nach SNIA.org  . . . . . . . . . . . . . . . 303
Abb. 6.28 Das NAS-Modell . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 304
Abb. 6.29 Das Konzept des Schattenservers (shadow server). . . . . . . . . . . . 310
Abb. 6.30 Struktur des Coda-Dateisystems . . . . . . . . . . . . . . . . . . . . . 312
Abb. 6.31 Heterogenität als Problem . . . . . . . . . . . . . . . . . . . . . . . . 314
Abb. 6.32 Middleware als Vermittlungsschicht . . . . . . . . . . . . . . . . . . . 315
Abb. 6.33 Schichtung der Middleware  . . . . . . . . . . . . . . . . . . . . . . . 315
Abb. 6.34 Beispiel Middleware: SAP/R3 3-tiers Architektur . . . . . . . . . . . . 316
Abb. 6.35 Architekturschichten von Jini  . . . . . . . . . . . . . . . . . . . . . . 317
Abb. 6.36 Thin clients/Thick server durch Middleware. . . . . . . . . . . . . . . 317
Abb. 6.37 Gesamtschichtung der .NET-Architektur. . . . . . . . . . . . . . . . . 318
Abb. 6.38 Ablauf einer Bestellung durch enterprise service bus (IBM) . . . . . . 319
Abb. 7.1 Die Infektion eines Programms  . . . . . . . . . . . . . . . . . . . . . 329
Abb. 7.2 Angriff eines user mode-Rootkits unter Windows NT. . . . . . . . . . 333
Abb. 7.3 Der Rootkit-Angriff als Filtertreiber . . . . . . . . . . . . . . . . . . . 334
Abb. 7.4 Die Matrix der Zugriffsrechte . . . . . . . . . . . . . . . . . . . . . . 338
Abb. 7.5 Rollen und Zugriffsrechte . . . . . . . . . . . . . . . . . . . . . . . . 339
Abb. 7.6 Die Vertrauenskette beim Starten. . . . . . . . . . . . . . . . . . . . . 340
Abb. 7.7 Ablauf beim login  . . . . . . . . . . . . . . . . . . . . . . . . . . . . 341
Abb. 7.8 Die klassische fire-wall-Konfiguration . . . . . . . . . . . . . . . . . . 344
Abb. 7.9 Die dual-homed-host-Konfiguration . . . . . . . . . . . . . . . . . . . 345
Abb. 7.10 Sitzungsausweis und Transaktionsausweis. . . . . . . . . . . . . . . . 347
Abb. 7.11 Transaktions- (Service-) durchführung. . . . . . . . . . . . . . . . . . 348
Abb. 8.1 Benutzeroberfläche und Gesamtsystemstruktur . . . . . . . . . . . . . 356
Abb. 8.2 Die ASCII-Buchstabenkodierung  . . . . . . . . . . . . . . . . . . . . 357
Abb. 8.3 Auslegung des Unicodes . . . . . . . . . . . . . . . . . . . . . . . . . 358
Abb. 8.4 Die Pixelkoordinaten der Rastergrafik . . . . . . . . . . . . . . . . . . 360
Abb. 8.5 Farbwertermittlung über eine Color Lookup Table . . . . . . . . . . . 361
Abb. 8.6 Ein Buchstabe (a) im 5×7-Raster und (b) als Umrandung . . . . . . . . 362
Abb. 8.7 Systemstruktur einer traditionellen Benutzeroberfläche . . . . . . . . . 363
Abb. 8.8 Systemstruktur einer fensterorientierten Benutzeroberfläche . . . . . . 363
Abb. 8.9 Die netzübergreifende Darstellung durch das Client-Server-Konzept
von X-Window . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 369

### Seite 19

XX Abbildungsverzeichnis
Abb. 8.10 Beispiel einer fensterorientierten Interaktion in Motif . . . . . . . . . . 370
Abb. 8.11 Fenster und Unterfenster in X-Window . . . . . . . . . . . . . . . . . 370
Abb. 8.12 Der Hierarchiebaum der Fenster aus Abb. 8.11 . . . . . . . . . . . . . 371
Abb. 8.13 Die Schichtung des X-Window-Motif-toolkits. . . . . . . . . . . . . . 372
Abb. 8.14 Ausschnitt aus der Hierarchie der Motif-widget-Primitiven . . . . . . . 373
Abb. 8.15 Beispiel eines  container widgets . . . . . . . . . . . . . . . . . . . . . 373
Abb. 8.16 Beispiel einer fensterorientierten Interaktion in Windows NT. . . . . . 376
Abb. 8.17 Getrennte und verschmolzene MDI-Fenster . . . . . . . . . . . . . . . 377
Abb. 8.18 Die Struktur der Window-Subsystemschicht. . . . . . . . . . . . . . . 378
Abb. 10.1 Wahrscheinlichkeitsverteilung der Seitenreferenzen. . . . . . . . . . . 466
Abb. 10.2 Der Seitenaustauschgrad ρ in Abhängigkeit vom Speicherangebot
σ pro Prozess . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 468
Abb. 10.3 Anstieg der Bearbeitungszeit mit wachsender Prozesszahl bei ρT ≤ ρw  . 470
Abb. 10.4 Anstieg der Bearbeitungszeit mit wachsender Prozesszahl bei ρT ≥ ρw  . 471

### Seite 20

1
© Springer-Verlag GmbH Deutschland 2017
R. Brause, Betriebssysteme,
DOI 10.1007/978-3-662-54100-5_1
Inhaltsverzeichnis
1.1 Einleitung: Was ist ein Betriebssystem? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  2
1.2 Betriebssystemschichten  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  2
1.3 Betriebssystemaufbau  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  4
1.3.1 Systemaufrufe  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  5
1.3.2 Beispiel UNIX . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  6
1.3.3 Beispiel Mach  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  7
1.3.4 Beispiel Windows NT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  8
1.4 Schnittstellen und virtuelle Maschinen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  11
1.5 Software-Hardware-Migration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  15
1.6 Virtuelle Betriebssysteme  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  16
1.6.1 Paravirtualisierung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  18
1.6.2 Virtualisierung mit BS-Containern . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  19
1.6.3 V ollständige Virtualisierung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  19
1.6.4 Hardware-Virtualisierung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  19
1.6.5 Virtualisierungserweiterungen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  20
1.7 Betriebssysteme für eingebettete Systeme . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  21
1.8 Betriebssysteme in Mehrprozessorarchitekturen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  22
1.9 Aufgaben  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  25
Literatur . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  26
Bevor wir die Einzelteile von Betriebssystemen genauer betrachten, wollen wir uns die
einfache Frage stellen: Was ist eigentlich ein Betriebssystem? Naiv betrachtet ist es die
Software, die mit einem neuen Rechner zum Betrieb mitgeliefert wird. So gesehen enthält
also ein Betriebssystem alle Programme und Programmteile, die nötig sind, einen Rechner
für verschiedene Anwendungen zu betreiben. Die Meinungen, was alles in einem Betriebs-
system enthalten sein sollte, gehen allerdings weit auseinander. Benutzt beispielsweise
Übersicht 1

### Seite 21

2 1 Übersicht
jemand einen Rechner nur zur Textverarbeitung, so erwartet er oder sie, dass der Rechner
alle Funktionen der Anwendung „Textverarbeitung“ beherrscht; wird der Rechner zum
Spielen verwendet, so soll er alles Wichtige für den Spielbetrieb enthalten. Was ist wichtig?
1.1 Einleitung: Was ist ein Betriebssystem?
Betrachten wir mehrere Anwendungsprogramme, so finden wir gemeinsame Aufgaben,
die alle Programme mit den entsprechenden Funktionen abdecken müssen. Statt jedes
Mal „das Rad neu zu erfinden“, lassen sich diese gemeinsamen Funktionen auslagern
und als „zum Rechner gehörige“ Standardsoftware ansehen, die bereits beim Kauf mit-
geliefert wird. Dabei beziehen sich die Funktionen sowohl auf Hardwareeinheiten wie
Prozessor, Speicher, Ein- und Ausgabegeräte, als auch auf logische (Software-) Einheiten
wie Dateien, Benutzerprogramme usw.
Bezeichnen wir alle diese Einheiten, die zum Rechnerbetrieb nötig sind, als „Ressourcen“
oder „Betriebsmittel“, so können wir ein Betriebssystem auch definieren als „die Gesamt-
heit der Programmteile, die die Benutzung von Betriebsmitteln steuern und verwalten“.
Diese Definition erhebt keinen Anspruch auf Universalität und V ollständigkeit, sondern
versucht lediglich, den momentanen Zustand eines sich ständig verändernden Begriffs ver-
ständlich zu machen. Im Unterschied zu der ersten Definition, in der Dienstprogramme wie
Compiler und Linker zum Betriebssystem gehören, werden diese in der zweiten Defini-
tion ausgeschlossen. Im Folgenden wollen wir eine historisch orientierte, mittlere Position
einnehmen:
Das Betriebssystem ist die Software (Programmteile), die für den Betrieb eines Rechners
anwendungsunabhängig notwendig ist.
Dabei ist allerdings die Interpretation von „anwendungsunabhängig“ (es gibt keinen anwen-
dungsunabhängigen Rechnerbetrieb: Dies wäre ein nutzloser Rechner) und „notwendig“
sehr subjektiv (sind Fenster und Mäuse notwendig?) und lädt zu neuen Spekulationen ein.
1.2 Betriebssystemschichten
Es gibt nicht das Betriebssystem schlechthin, sondern nur eine den Forderungen der
Anwenderprogramme entsprechende Unterstützung, die von der benutzerdefinierten Kon-
figuration abhängig ist und sich im Laufe der Zeit stark gewandelt hat. Gehörte früher nur
die Prozessor-, Speicher- und Ein-/Ausgabeverwaltung zum Betriebssystem, so werden
heute auch eine grafische Benutzeroberfläche mit verschiedenen Schriftarten und -größen
(Fonts) sowie Netzwerkfunktionen verlangt. Einen guten Hinweis auf den Umfang eines
Betriebssystems bietet die Auslieferungsliste eines anwendungsunabhängigen Rechner -
systems mit allen darauf vermerkten Softwarekomponenten.
Die Beziehungen der Programmteile eines Rechners lassen sich durch das Diagramm
in Abb. 1.1 visualisieren.

### Seite 22

1.2 Betriebssystemschichten 3
Dies lässt sich auch kompakter zeichnen: in Abb. 1.2 links als Schichtensystem und
rechts als System konzentrischer Kreise („Zwiebelschalen“).
Dabei betont die Darstellung als Schichtenmodell den Aspekt der Basis, auf der auf-
gebaut wird, während das Zwiebelschalenmodell eher Aspekte wie „Abgeschlossenheit“
und „Sichtbarkeit“ von „inneren“ und „äußeren“ Schichten visualisieren.
Beispiel: CPU-Ringe und Schichten
Nach der Initialisierung sind bereits beim 80386 vier Sicherheitsstufen für den Zugriff
auf Programme wirksam, siehe Abb. 1.3. Sie lassen sich mit Hilfe von Ringen oder
Schichten modellieren. Benutzerprogramme (Stufe 3, äußerster Ring), gemeinsam
benutzte Bibliotheken (Stufe 2), Systemaufrufe (Stufe 1) und Kernmodus (Stufe 0,
innerster Ring). Die 2 Bits dieser Einstufung werden als Zugriffsinformation in allen
Speicherbeschreibungen mitgeführt und entscheiden über die Legalität des Zugriffs.
Wird der Zugriff verweigert, so erfolgt eine Fehlerunterbrechung.
Auch Programmsprünge und Prozeduraufrufe in Code einer anderen Stufe werden
streng geregelt. Um eine Prozedur einer anderen Stufe aufzurufen, muss eine spezielle
Instruktion CALL benutzt werden, die über eine Datenstruktur (call gate) den Zugriff
überprüft und dann die vorher von der Prozedur eingerichtete Einsprungadresse ver -
wendet. Unkontrollierte Sprünge werden so verhindert.
EHQXW]W
EHQXW]W
EHQXW]W
%HQXW]HU
%HQXW]HUSURJUDPP
0DVFKLQHQKDUGZDUH
%HWULHEVV\VWHP
Abb. 1.1 Benutzungsrelationen von Programmteilen
+:
8VHU
 6SLHOH
%HWULHEVV\VWHPGLHQVWH
+DUGZDUH
8VHU8VHU
(GLWRU&RPSLOHU
Abb. 1.2 Schichtenmodell und Zwiebelschalenmodell

### Seite 23

4 1 Übersicht
1.3 Betriebssystemaufbau
Das Betriebssystem (operating system) als Gesamtheit aller Software, die für den anwen-
dungsunabhängigen Betrieb des Rechners notwendig ist, enthält
• Dienstprogramme, Werkzeuge: oft benutzte Programme wie Editor, …
• Übersetzungsprogramme: Interpreter, Compiler, Translator, …
• Organisationsprogramme: Speicher-, Prozessor-, Geräte-, Netzverwaltung.
• Benutzerschnittstelle: textuelle und graphische Interaktion mit dem Benutzer.
Da ein vollständiges Betriebssystem inzwischen mehrere hundert Megabyte umfassen
kann, werden aus diesem Reservoir nur die sehr oft benutzten Funktionen als Betriebs-
systemkern in den Hauptspeicher geladen. In Abb. 1.4 ist die Lage des Betriebssystem-
kerns innerhalb der Schichtung eines Gesamtsystems gezeigt.
Der Kern umfasst also alle Dienste, die immer präsent sein müssen, wie z. B. große Teile der
Prozessor-, Speicher- und Geräteverwaltung (Treiber) und wichtige Teile der Netzverwaltung.
6\VWHPDXIUXI
0DVFKLQHQFRGH
%HQXW]HUREHUIOlFKH
8VHU,QWHUIDFH0DQDJHPHQW6\VWHP
%HWULHEVV\VWHPNHUQ
2SHUDWLQJ6\VWHP.HUQHO
+DUGZDUH
$QZHQ
GXQJ
'LHQVW
SURJUDPP
:HUN
]HXJ«
%HQXW]HU « %HQXW]HU1Abb. 1.4 Überblick über die
Rechnersoftwarestruktur
^ƚƵĨĞϯсZŝŶŐϯ
^ƚƵĨĞϮсZŝŶŐϮ
^ƚƵĨĞϭсZŝŶŐϭ
^ƚƵĨĞϬсZŝŶŐϬ
ZŝŶŐϯ
ZŝŶŐϮ
ZŝŶŐϭ
ZŝŶŐϬ
Abb. 1.3 Die Sicherheitsstufen (Ringe) der Intel 80X86-Architektur

### Seite 24

1.3 Betriebssystemaufbau 5
1.3.1 Systemaufrufe
Die Dienste des Kerns werden durch einen Betriebssystemaufruf angefordert und folgen
wie ein normaler Prozeduraufruf einem festen Format (Zahl und Typen der Parameter). Da
die Lage des Betriebssystemkerns im Hauptspeicher sich ändern kann und die Anwender-
programme dann immer wieder neu gebunden werden müssten, gibt es bei den meisten
Betriebssystemkernen einen speziellen Aufrufmechanismus (Systemaufruf, system call),
der eine Dienstleistung anfordert, ohne die genaue Adresse der entsprechenden Prozedur
zu kennen. Dieser Aufrufmechanismus besteht daraus, nach dem Abspeichern der Para-
meter des Aufrufs auf dem Stack einen speziellen Maschinenbefehl auszuführen, den
Softwareinterrupt. Wie bei einem Hardwareinterrupt speichert der Prozessor seine augen-
blickliche Instruktionsadresse (program counter PC + 1) und den Prozessorstatus PS auf
dem Stack, entnimmt das neue Statuswort und die Adresse der nächsten Instruktion einer
festen, dem speziellen Interrupt zugeordneten Adresse des Hauptspeichers und setzt mit
der Befehlsausführung an dieser Adresse fort.
Wurde beim Initialisieren des Rechnersystems (bootstrap) auf dem festen Interrupt-
Speicherplatz die Einstiegsadresse des Betriebssystemkerns geschrieben, so findet das
Anwenderprogramm prompt das Betriebssystem, egal ob es inzwischen neu kompiliert
bzw. im Speicher verschoben wurde oder nicht. In Abb. 1.5 ist der Ablauf eines solchen
Systemaufrufs gezeigt. Da nach einem Systemaufruf die nächste Instruktion nicht gleich
ausgeführt wird, sondern die Befehlsfolge an dieser Speicheradresse plötzlich „aufhört“,
wird der Softwareinterrupt auch als Falltür (trap door, kurz trap) bezeichnet.
Dabei wird hardwaremäßig der augenblickliche Wert des Programmzählers PC (um
eins erhöht für die Adresse der nächsten Instruktion nach der Interrupt-Instruktion) sowie
der Status des Programms (Statuswort PS, enthält die Ergebnisbits der CPU und die Infor-
mation, ob im user mode oder kernel mode) auf den Stack gerettet. Anschließend wird
dann der Inhalt eines Tabelleneintrags für diesen Interrupt, der neue Status PS und die
neue Adresse BS des Betriebssystems, in die CPU geladen.
Die Umschaltung vom Benutzerprogramm zum Betriebssystem wird meist zum
Anlass genommen, die Zugriffsrechte und -möglichkeiten des Codes drastisch zu erwei-
tern. Wurden große Teile des Rechners vor der Umschaltung hardwaremäßig vor Fehl-
bedienung durch das Benutzerprogramm geschützt, so sind nun alle Schutzmechanis-
men abgeschaltet, um den Betriebssystemkern nicht zu behindern. Beim Verlassen des
3URJUDPP
LQVWUXNWLRQHQ
%HWULHEVV\VWHP
NHUQGLHQVWH
UHWXUQIURPLQWHUUXSW
VWDFNĺ^3&36 XVHUPRGH`
,QWHUUXSW
^3&36 XVHUPRGH`ĺVWDFN
%6ĺ3&NHUQHOPRGHĺ36
5HJLVWHUODGHQ
3URJUDPP
LQVWUXNWLRQHQ
Abb. 1.5 Befehlsfolge eines
Systemaufrufs

### Seite 25

6 1 Übersicht
Betriebssystemkerns wird automatisch wieder zurückgeschaltet, ohne dass der Benutzer
etwas davon merkt. Die Umschaltung zwischen dem Benutzerstatus (user mode) und
dem Betriebssystemstatus (kernel mode) geschieht meist hardwaremäßig durch den
Prozessor und lässt sich damit vom Benutzer nicht manipulieren. Manche Prozesso-
ren besitzen sogar noch weitere Sicherheitsstufen, die aber den Hardwareaufwand auf
dem Chip erhöhen. Bei der Rückkehr vom Betriebssystemkern werden die erweiterten
Rechte durch das Neuladen der auf dem Stack gespeicherten Werte automatisch wieder
zurückgesetzt.
Auch für die Behandlung von Fehlern in der Fließkommaeinheit (Floating Point Unit
FPU) werden Softwareinterrupts verwendet. Die Fehlerbehandlung ist aber meist anwen-
dungsabhängig und deshalb üblicherweise im Betriebssystem nicht enthalten, sondern
dem Anwenderprogramm oder seiner Laufzeitumgebung überlassen.
1.3.2 Beispiel UNIX
In UNIX gibt es traditionellerweise als Benutzeroberfläche einen Kommandointerpre-
ter, die Shell. V on dort werden alle Benutzerprogramme sowie die Systemprogramme,
die zum Betriebssystem gehören, gestartet. Die Kommunikation zwischen Benutzer und
Betriebssystem geschieht durch Ein- und Ausgabekanäle; im einfachsten Fall sind dies die
Eingabe von Zeichen durch die Tastatur und die Ausgabe auf dem Terminal. In Abb. 1.6
ist das Grundschema gezeigt.
Das UNIX-System wies gegenüber den damals verfügbaren Systemen verschiedene
V orteile auf. So ist es nicht nur ein Betriebssystem, das mehrere Benutzer (Multi-user)
gleichzeitig unterstützt, sondern auch mehrere Programme ( Multiprogramming) gleich-
zeitig ausführen konnte. Zusammen mit der Tatsache, dass die Quellen den Universi-
täten fast kostenlos zur Verfügung gestellt wurden, wurde es bei allen Universitäten
…
…
XVHUPRGH
NHUQHOPRGH
%HQXW]HU
6KHOO
%HQXW]HU
3URJUDPP
6\VWHP
3URJUDPP
6\VWHP
3URJUDPP
%HQXW]HU
6KHOO
hEHUSUIEDUH6FKQLWWVWHOOHXQG)XQNWLRQVYHUWHLOXQJ
6SHLFKHU
YHUZDOWXQJ 6HULHOOH(LQ$XVJDEH 'DWHLV\VWHP 3UR]HVV
PDQDJH
PHQW
'LV
SOD\ 77< 'UXFNHU0 DXV 3ODWWH
)ORSS\ 1HW]
+DUGZDUH
0XOWL8VHU0XOWL8VHU
0XOWL
SURJUDPPLQJ
0XOWL
SURJUDPPLQJ
Abb. 1.6 UNIX-Schichten

### Seite 26

1.3 Betriebssystemaufbau 7
Standard und dort weiterentwickelt. Durch die überwiegende Implementierung mittels
der „höheren“ Programmiersprache „C“ war es leicht veränderbar und konnte schnell
auf eine andere Hardware übertragen (portiert) werden. Diese Faktoren machten es zum
Betriebssystem der Wahl, als für die neuen RISC-Prozessoren schnell ein Betriebssys-
tem benötigt wurde. Hatte man bei einem alten C-Compiler den Codegenerator für den
neuen Instruktionssatz geändert, so war die Hauptarbeit zum Portieren des Betriebs-
systems bereits getan – alle Betriebssystemprogramme sowie große Teile des Kerns
sind in C geschrieben und sind damit nach dem Kompilieren auf dem neuen Rechner
lauffähig.
Allerdings gibt es trotzdem noch genügend Arbeit bei einer solchen Portierung. Die
ersten Versionen von UNIX (Version 6 und 7) waren noch sehr abhängig von der Hard-
ware, vor allem aber von der Wortbreite der CPU. In den folgenden Versionen (System IV
und V sowie Berkeley UNIX) wurde zwar viel gelernt und korrigiert, aber bis heute ist die
Portierbarkeit nicht problemlos.
Die Grundstruktur von UNIX differiert von Implementierung zu Implementierung. So
sind Anzahl und Art der Systemaufrufe sehr variabel, was die Portierbarkeit der Benutzer-
programme zwischen den verschiedenen Versionen ziemlich behindert. Um dem abzu-
helfen, wurden verschiedene Organisationen gegründet. Eine der bekanntesten ist die X/
Open-Gruppe, ein Zusammenschluss verschiedener Firmen und Institutionen, die ver -
schiedene Normen herausgab. Eine der ersten Normen war die Definition der Anforde-
rungen an ein portables UNIX-System (Portable Operating System Interface based on
UNIX: POSIX, genormt als IEEE 1003.1-2013 bzw. ISO/IEC 9945), das als Menge ver -
schiedener verfügbarer Systemdienste definiert wurde. Allerdings sind dabei nur Dienste,
nicht die Systemaufrufe direkt definiert worden. Durch die an dem Namen „UNIX“ auf
X/Open übertragenen Rechte konnte ein Zertifikationsprozess institutionalisiert werden,
der eine bessere Normierung verspricht. Dabei wurde UNIX auch an das Client-Server-
Modell (Seite 27) angepasst: Es gibt eine Spezifikation für UNIX-98 Server und eine für
UNIX-98 Client.
1.3.3 Beispiel Mach
Das Betriebssystem „Mach“ wurde an der Universität Berkeley als ein Nachfolger von
UNIX entwickelt, der auch für Multiprozessorsysteme einsetzbar sein sollte. Das Konzept
von Mach ist radikal verschieden von dem UNIX-Konzept. Statt alle weiteren, als wichtig
angesehenen Dienste im Kern unterzubringen, beschränkten die Designer das Betriebs-
system auf die allernotwendigsten Funktionen: die Verwaltung der Dienste, die selbst aber
aus dem Kern ausgelagert werden, und die Kommunikation zwischen den Diensten. In
Abb. 1.7 ist das prinzipielle Schichtenmodell gezeigt, das so auch auf das bekannte Share-
ware-Amoeba-System von Tanenbaum zutrifft. Beide Systeme besitzen Bibliotheken für
UNIX-kompatible Systemaufrufe, so dass sie vom Benutzerprogramm als UNIX-Systeme
angesehen werden können.

### Seite 27

8 1 Übersicht
Der V orteil einer solchen Lösung, den Kern in einen besonders kleinen, sparsam bemes-
senen Teil (Mikrokern) einerseits und in Systemdienste auf Benutzerebene andererseits
aufzuteilen, liegt auf der Hand: Die verschiedenen Systemdienste sind gekapselt und
leicht austauschbar; es lassen sich sogar mehrere Versionen nebeneinander benutzen. Die
Nachteile sind aber auch klar: Durch die Kapselung als Programme im Benutzerstatus
dauert es relativ lange, bis die verschiedenen Systemdienste mittels Systemaufrufen und
Umschalten zwischen user mode und kernel mode sich abgestimmt haben, um einen Sys-
temaufruf des Benutzerprogramms auszuführen.
1.3.4 Beispiel Windows NT
Das Betriebssystem Windows NT der Firma Microsoft ist ein relativ modernes System;
es wurde unter der Leitung von David Cutler, einem Betriebssystementwickler von VMS,
RSX11-M und MicroVax der Fa. Digital, seit 1988 entwickelt. Das Projekt, mit dem Mic-
rosoft erstmals versuchte, ein professionelles Betriebssystem herzustellen, hatte verschie-
denen V orgaben zu genügen:
• Das Betriebssystem musste zu allen bisherigen Standards (MS-DOS, 16 Bit-Windows,
UNIX, OS/2) kompatibel sein, um überhaupt am Markt akzeptiert zu werden.
• Es musste zuverlässig und robust sein, d. h. Programme dürfen weder sich gegenseitig
noch das Betriebssystem schädigen können; auftretende Fehler dürfen nur begrenzte
Auswirkungen haben.
• Es sollte auf verschiedene Hardwareplattformen leicht zu portieren sein.
• Es sollte nicht perfekt alles abdecken, sondern für die sich wandelnden Ansprüche
leicht erweiterbar und änderbar sein.
• Sehr wichtig: Es sollte auch leistungsstark sein.
Betrachtet man diese Aussagen, so stellen sie eine Forderung nach der „eierlegenden
Wollmilchsau“ dar. Die gleichzeitigen Forderungen von „kompatibel“, „zuverlässig“,
0DFK.HUQ
6FKHGXOHU1DFKULFKWHQEHUPLWWOXQJ%DVLF,26SHLFKHUREMHNWH
6SHLFKHU
0DQDJHU
)LOH
0DQDJHU
7HUPLQDO
,2
%HQXW]HU
SURJUDPP
XVHUPRGH
NHUQHOPRGH
+DUGZDUH
Abb. 1.7 Das Mach-Systemmodell

### Seite 28

1.3 Betriebssystemaufbau 9
„portabel“, „leistungsstark“ sind schon Widersprüche in sich: MS-DOS ist absolut nicht
zuverlässig, portabel oder leistungsstark und überhaupt nicht kompatibel zu UNIX.
Trotzdem erreichten die Entwickler ihr Ziel, indem sie Erfahrungen anderer Betriebs-
systeme nutzten und stark modularisierten. Die Schichtung und die Aufrufbeziehungen
des Kerns in der ursprünglichen Konzeption sind in Abb. 1.8 gezeigt. Der gesamte Kern
trägt den Namen Windows NT Executive und ist der Block unterhalb der user mode/kernel
mode-Umschaltschranke.
Zur Lösung der Designproblematik seien hier einige Stichworte genannt:
• Die Kompatibilität wird erreicht, indem die Besonderheiten jedes der Betriebssys-
teme in ein eigenes Subsystem verlagert werden. Diese setzen als virtuelle Betriebssys-
temmaschinen auf den Dienstleistungen der NT Executive (Systemaufrufe, schwarze
Pfeile in Abb. 1.8) auf. Die zeichenorientierte Ein/Ausgabe wird an die Dienste des
zentralen Win32-Moduls weitergeleitet. Die Dienste der Subsysteme werden durch
Nachrichten (local procedure calls LPC, graue Pfeile in Abb. 1.8) von Benutzerpro-
grammen, ihren Kunden (Clients), angefordert. Als Dienstleister (Server) haben sie
also eine Client-Server-Beziehung.
• Die Robustheit wird durch rigorose Trennung der Programme voneinander und durch
Bereitstellen spezieller Ablaufumgebungen („virtuelle DOS-Maschine VDM“) für die
MS-DOS/Windows Programme erreicht. Die Funktionen sind gleich, aber der direkte
Zugriff auf Hardware wird unterbunden, so dass nur diejenigen alten Programme laufen
können, die die Hardware-Ressourcen nicht aus Effizienzgründen direkt anzusprechen
versuchen. Zusätzliche Maßnahmen wie ein fehlertolerantes Dateisystem und spezielle
Sicherheitsmechanismen zur Zugriffskontrolle von Dateien, Netzwerken und Program-
men unterstützen dieses Ziel.
• Die Portierbarkeit, Wartbarkeit und Erweiterbarkeit wird dadurch unterstützt, dass das
gesamte Betriebssystem bis auf wenige Ausnahmen (z. B. in der Speicherverwaltung)
XVHUPRGH
NHUQHOPRGH
6\VWHPGLHQVWH
2EMHFW
0DQDJHU
3URFHVV
0DQDJHU
/RFDO
3URF&DOOV
0HPRU\
0DQDJHU
6HFXULW\
0RQLWRU
,2
6\VWHP
.HUQHO
+DUGZDUH$ EVWUDFWLRQ/ D\HU+$/
+DUGZDUH
326,;
&OLHQW:LQ'26
&OLHQW
26
&OLHQW
:LQ
6XEV\V
WHP
/RJRQ
6HFXULW\
6XEV\V
WHP
326,;
6XEV\V
WHP
26
6XEV\V
WHP
Abb. 1.8 Schichtung und Aufrufe bei Windows NT

### Seite 29

10 1 Übersicht
in der Sprache C geschrieben, stark modularisiert und von Anfang an geschichtet ist.
Eine spezielle Schicht HAL bildet als virtuelle Maschine allgemeine Hardware nach
und reduziert bei der Portierung auf andere Prozessoren die notwendigen Änderungen
auf wenige Module.
Die detaillierte Diskussion der oben geschilderten Lösungen würde zu weit führen; hier
sei auf das Buch von Helen Custer (1993) verwiesen.
• Obwohl in Windows NT einige wichtige Subsysteme wie z. B. das Sicherheitssystem
nicht als Kernbestandteil, sondern als Prozess im user mode betrieben werden („Integrale
Subsysteme“), ist interessanterweise seit Version 4.0 das Win32-Subsystem aus Effizienz-
gründen in den Kern verlagert worden, um die Zeit für die Systemaufrufe von Win32 zu
NT Executive zu sparen. Auch die Unterstützung anderer Standards wurde eingestellt.
V on den gezeigten Betriebssystem-Subsystemen sind im Laufe der Versionen von NT
nur noch das Windows/Dos-System und das Windows 32Bit-System („windows over
windows“) übrig; zuerst das OS/2-System ab Version NT 4.0 und dann das POSIX-Sys-
tem („Interix“) wurden mit fortschreitender Marktakzeptanz von Windows NT eingestellt.
In Version NT 5.0, erschienen im Februar 2000 („Windows 2000“), wurden zusätzlich
viele Dienstprogramme zur Netzdateiverwaltung und Sicherheit integriert. Dies ließ den
Umfang von 8 Mio. Codezeilen auf über 40 Mio. anschwellen, was an die Zuverlässigkeit
und Testumgebung der Betriebssystemmodule besonders hohe Anforderungen stellt.
Mit den Versionen NT 5.1 („Windows XP“), NT 5.2 („Windows Server 2003“) und
Version 6.0 („Windows Vista“) stiegen die Anforderungen an die Grafikhardware weiter;
ohne Hardware-Grafikbeschleunigung war MS Windows ab Version NT 6 nicht installierbar.
Auch für die Version 6.1 („Windows 7“), Version NT 6.2 („Windows 8“) und Version NT
6.3 („Windows 8.2“) sowie für die zur Zeit (2016) aktuelle Version NT 10.0 („Windows
10“) wurden die Anforderungen immer weiter ausgeweitet. Zwar wurde der Software-
erstellungsprozess komplett umgeändert und auf Module umgestellt, nachdem Windows
Vista zunächst als sehr fehleranfällig und langsam von den Benutzern abgelehnt wurde,
aber Umfang und Komplexität des Codes blieben erhalten. So wuchs zwar die Anzahl
der Codezeilen mit NT 5.2 und 6.0 auf 50 Mio. und wurde nach der Modularisierung
NT 6.1 auf die „meist verwendeten“ 40 Mio. Codezeilen von über 60 Mio. Zeilen redu-
ziert, aber durch die Übernahme zusätzlicher Funktionalität (Hilfsprogramme) wächst die
gesamte Softwarebasis kontinuierlich an. Zum Vergleich: das zurzeit am meisten verwen-
dete Unix, der Linux-Kern 4.2, hat nur ca. 20 Mio. Codezeilen, und die Smartphone-
Variante „Android“ nur 12 Mio. Codezeilen. Das hört sich viel an im Vergleich für das
Windows-Betriebssystem, aber: betrachtet man etwa das aus Unix entwickelte Apple-Be-
triebssystem MAC OS X 10.4 mit ca. 86 Mio. Codezeilen, und vergleicht man dies noch
mit dem Google-Suchdienst („Betriebssystem des Internets“) mit dem Umfang aller auf
den Servern laufenden Programme von über 2000 Mio. Codezeilen (86 TByte!), also 40
mal mehr als Windows, so relativiert sich diese Einschätzung wieder!

### Seite 30

1.4 Schnittstellen und virtuelle Maschinen 11
1.4 Schnittstellen und virtuelle Maschinen
Betrachten wir nun das Schichtenmodell etwas näher und versuchen, daraus zu abstrahie-
ren. Die Relation „A benutzt B“ lässt sich dadurch kennzeichnen, dass B für A Dienstleis-
tungen erbringt. Dies ist beispielsweise bei der Benutzung einer Unterprozedur B in einem
Programm A der Fall. Betrachten wir dazu das Zeichnen einer Figur, etwa eines Vierecks.
Die Dienstleistung DrawRectangle(x0,y0,x1,y1) hat als Argumente die Koordinaten
der linken unteren Ecke und die der rechten oberen. Wir können diesen Aufruf beispiels-
weise direkt an einen Grafikprozessor GPU richten, der dann auf unserem Bildschirm das
Rechteck zeichnet, siehe Abb. 1.9 links. In diesem Fall benutzen wir eine echte Maschine,
um die Dienstleistung ausführen zu lassen.
In vielen Rechnern ist aber kein Grafikprozessor vorhanden. Stattdessen ruft das Pro-
gramm, das diese Funktion ausführen soll, selbst wieder eine Folge von einfachen Befeh-
len (Dienstleistungen) auf, die diese Funktion implementieren sollen, etwa viermal das
Zeichnen einer Linie. Die Dienstleistung DrawRectangle(x0,y0,x1,y1) wird also nicht
wirklich, sondern mit DrawLine() durch den Aufruf einer anderen Maschine erbracht;
das aufgerufene Programm ist eine virtuelle Maschine, in Abb. 1.9 rechts V1 genannt.
Nun kann das Zeichnen einer Linie auch wieder entweder durch einen echten Grafik-
prozessor erledigt werden, oder aber die Funktion arbeitet selbst als virtuelle Maschine V2
und ruft für jedes Zeichnen einer Linie eine Befehlsfolge einfacher Befehle der darunter
liegenden Schicht für das Setzen aller Bildpunkte zwischen den Anfangs- und Endkoor -
dinaten auf. Diese Schicht ist ebenfalls eine virtuelle Maschine V3 und benutzt Befehle
für die CPU, die im Video-RAM Bits setzt. Die endgültige Ausgabe auf den Bildschirm
wird durch eine echte Maschine, die Displayhardware (Displayprozessor), durchgeführt.
Erinnern wir uns in diesem Zusammenhang an die Normierung von UNIX mittels
POSIX. Interessant ist, dass dabei die Bezeichnung „UNIX“ nur für eine Sammlung von
verbindlichen Schnittstellen steht, nicht für eine Implementierung. Dies bedeutet, dass
UNIX eigentlich als eine virtuelle und nicht als reelle Betriebssystemmaschine angesehen
werden kann.
'UDZ5HFWDQJOH[\[\ 'UDZ5HFWDQJOH[\[\ 9
*UDSKLF3URFHVVRU8QLW
*38
'UDZ/LQH[\[\
'UDZ/LQH[\[\
'UDZ/LQH[\[\
'UDZ/LQH[\[\
9
6HW3RLQW[\EODFN
6HW3RLQW[G[\EODFN
…
9
'LVSOD\5$0 'LVSOD\5$0 9
Abb. 1.9 Echte und virtuelle Maschinen

### Seite 31

12 1 Übersicht
Den Gedankengang der Virtualisierung können wir allgemein formulieren. Gehen
wir davon aus, dass alle Dienstleistungen in einer bestimmten Reihenfolge (Sequenz)
angefordert werden, so lassen sich im Schichtenmodell die Anforderungen vom Anwen-
der an das Anwenderprogramm, vom Anwenderprogramm an das Betriebssystem, vom
Betriebssystem an die Hardware usw. auf Zeitachsen darstellen, die untereinander ange-
ordnet sind.
Jede dieser so entstandenen Schichten bildet nicht nur eine Softwareeinheit wie in
Abb. 1.2 links, sondern die Schichtenelemente sind hierarchisch als Untersequenzen
oder Dienstleistungen angeordnet. Bei jeder Dienstleistung interessiert sich die anfor -
dernde, darüber liegende Schicht nur dafür, dass sie überhaupt erbracht wird, und nicht,
auf welche Weise. Die Dienstleistungsfunktionen einer Schicht, also die Prozeduren
bzw. Methoden, Daten und ihre Benutzungsprotokolle, kann man zu einer Schnitt-
stelle zusammenfassen. Das Programm, das diese Dienstleistungen erbringt, kann nun
selbst wieder als Befehlssequenz aufgefasst werden, die darunter liegende, elementarere
Dienstleistungen als eigene Leistungen benutzt. Die allerunterste Schicht, die die Arbeit
nun tatsächlich auch ausführt, wird von der „darunter liegenden“ Maschinenhardware
gebildet. Da sich ihre Funktionen, so wie bei allen Schichten, über Schnittstellen ansteu-
ern lassen, kann man die darüber liegende Einheit ebenfalls als eine Maschine auffassen;
allerdings erbringt sie die Arbeit nicht selbst und wird deshalb als virtuelle Maschine
bezeichnet. Die Abb. 1.10 beschreibt also eine Hierarchie virtueller Maschinen. Das all-
gemeine Schichtenmodell aus Abb. 1.2 zeigt dies ebenfalls, aber ohne Zeitachsen und
damit ohne Reihenfolge. Es ist auch als Übersicht über Aktivitäten auf parallel arbeiten-
den Maschinen geeignet.
Die Funktion der virtuellen Gesamtmaschine ergibt sich aus dem Zusammenwirken
virtueller Einzelmaschinen. In diesem Zusammenhang ist es natürlich von außen ununter-
scheidbar, ob eine Prozedur oder eine Hardwareeinheit eine Funktion innerhalb einer
Sequenz ausführt.
Bisher haben wir zwischen physikalischen und virtuellen Maschinen unterschieden.
Es gibt nun noch eine dritte Sorte: die logischen Maschinen. Für manche Leute sind sie
als Abstraktion einer physikalischen Maschine mit den virtuellen Maschinen identisch,
andere platzieren sie zwischen physikalische und virtuelle Maschinen.
6FKLFKW
6FKLFKW
=HL
6FKLFKW
Abb. 1.10 Hierarchie virtueller
Maschinen

### Seite 32

1.4 Schnittstellen und virtuelle Maschinen 13
Beispiel virtuelle Festplatte
Eine virtuelle Festplatte lässt sich als Feld von Speicherblöcken modellieren, die ein-
heitlich mit einer sequentiellen Blocknummer angesprochen werden können. Im Gegen-
satz dazu modelliert die logische Festplatte alles etwas konkreter und berücksichtigt, dass
eine Festplatte auch unterschiedlich groß sein kann sowie eine Verzögerungszeit und eine
Priorität beim Datentransfer kennt. In Abb. 1.11 ist dies gezeigt. Mit diesen Angaben kann
man eine Verwaltung der Speicherblöcke anlegen, in der der Speicherplatz mehrerer Fest-
platten einheitlich verwaltet wird, ohne dass dies der Schnittstelle der virtuellen Festplatte
bekannt sein muss. In der dritten Konkretisierungsstufe beim tatsächlichen Ansprechen
der logischen Geräte müssen nun alle Feinheiten der Festplatten (Statusregister, Fehler-
information, Schreib-/Lesepufferadressen, …) bekannt sein. Das Verwalten dieser Infor-
mationen und Verbergen vor der nächsthöheren Schicht (der Verwaltung der logischen
Geräte) besorgt dann der gerätespezifische Treiber. Die Definitionen bedeuten dann in
diesem Fall:
virtuelles Gerät = Verwaltungstreiber für logisches Gerät,
logisches Gerät = HW-Treiber für physikalisches Gerät.
Die drei Gerätearten bilden also auch wieder drei Schichten für den Zugriff auf die Daten,
vgl. Abb. 1.11. Die logischen Geräte (LUN) gestatten es, unabhängig vom Hersteller
auf eine Festplatte zuzugreifen; es kann als eine Abstraktion einer Festplatte aufgefasst
werden. Es gibt dabei keinen Unterschied zu einer virtuellen Maschine; der Begriff
„logisches Gerät“ ist eher eine historische Bezeichnung für diese Abstraktionsstufe.
Mit Hilfe des Begriffs der virtuellen Maschine können wir uns virtuelle Massenspeicher
aber auch ganz anderer Art konstruieren.
.RQWUROOH 'DWHQ
9LUWXHOOHV*HUlW
7UHLEHUIUORJ*HUlWH
ORJ*HUlW
SK\V
*HUlW
7UHLEHU
SK\V
*HUlW
7UHLEHU
ORJ*HUlW
Abb. 1.11 Virtuelle, logische und physikalische Geräte

### Seite 33

14 1 Übersicht
Beispiel Disk-to-Disk-Storage
Ein Bandlaufwerk zur Sicherung von Massendaten kann gut mit einer Menge von Fest-
platten simuliert werden. Die Simulation eines billigen Bandlaufwerks durch teure
Festplatten ist dann sinnvoll, wenn für die Datensicherung (backup)
• Kurze Backup-Zeiten
• Kurze Recovery-Zeiten
• Multiple Bandformate
• Hoher Datendurchsatz
gefordert werden. Hier kommen dann kostengünstige Plattenlaufwerke mit großen
Kapazitäten zum Einsatz.
Beispiel Storage Attached Network SAN
Aber wir können auch alle Massenspeicher eines Speichernetzes mit den kontrollierenden
Rechnern zu einem einzigen virtuellem Massenspeicher zusammenfassen. In Abb. 1.12
ist ein solches Storage Attached Network SAN gezeigt.
Der virtuelle Massenspeicher bestehet in diesem Fall aus einem Netzwerk, das nicht
nur die Speicherfunktionen intern organisiert, sondern auch die Zugriffsrechte, die
Datensicherung (backup) und Zugriffsoptimierung (Lastverteilung, Datenmigration)
selbst regelt. Konflikte gibt es dabei mit unabhängigen Untereinheiten, die selbst diese
Funktionen übernehmen wollen (z. B. NAS oder SAN-in-a-box). Es gibt hauptsächlich
zwei verschiedene Konfigurationen:
• Der asymmetrische Pool: Ein Server dient als Metadaten-Server (Wo sind welche
Daten) und gibt Block-I/O Informationen an die anderen
ILOHVHUYHU
PHWDGDWD
VHUYHU
%ORFN,
2
2UWVLQIR
6$1
/XQ
1$6
1HWZRUN
$WWDFKHG
6WRUDJH
Abb. 1.12 Ein Netzwerk als
virtueller Massenspeicher: die
asymmetrische Pool-Lösung

### Seite 34

1.5 Software-Hardware-Migration 15
• Der symmetrische Pool (3-tiers-Lösung): Die Speichergeräte sind nur mit mehreren
Metadaten-Servern über ein extra Netzwerk verbunden; die Metaserver hängen über
das SAN an den anfragenden Rechnern.
1.5 Software-Hardware-Migration
Die Konstruktion von virtuellen Maschinen erlaubt es, analog zu den Moduln die Schnitt-
stelle beizubehalten, die Implementierung aber zu verändern. Damit ist es möglich, die
Implementierung durch eine wechselnde Mischung aus Hardware und Software zu realisie-
ren: Für die angeforderte Dienstleistung ist dies irrelevant. Da die Hardware meist schneller
arbeitet, aber teuer ist, und die Software vergleichsweise langsam abgearbeitet wird, aber (als
Kopie) billig ist und schneller geändert werden kann, versucht der Rechnerarchitekt, bei dem
Entwurf eines Rechensystems eine Lösung zwischen diesen beiden Extremen anzusiedeln.
In Abb. 1.13 ist als Beispiel die Schichtung eines symbolischen Maschinencodes (hier: Java-
Code) zu sehen, der entweder softwaremäßig durch einen Compiler oder Interpreter in einen
realen Maschinencode umgesetzt werden („Java virtual machine“) oder aber auch direkt als
Maschineninstruktion hardwaremäßig ausgeführt werden kann. Im zweiten Fall wurde die
mittlere Schicht in die Hardware (schraffiert in Abb. 1.13 links) migriert, indem für jeden
Java-Code Befehl eine in Mikrocode programmierte Funktion in der CPU ausgeführt wird.
Ein anderes Beispiel für diese Problematik ist die Unterstützung von Netzwerkfunktionen.
In billigen Netzwerkcontrollern ist meist nur ein Standard-Chipset enthalten, das die zeitkri-
tischen Aspekte wie Signalerzeugung und -erfassung durchführt. Dies entspricht den virtu-
ellen Maschinen auf unterster Ebene. Alle höheren Funktionen und Protokolle zum Zusam-
mensetzen der Datenpakete, Finden der Netzwerkrouten und dergleichen (s. Abschn. 6.1)
muss vom Hauptprozessor und entsprechender Software durchgeführt werden, was die
Prozessorleistung für alle anderen Aufgaben (wie Benutzeroberfläche, Textverarbeitung
etc.) drastisch mindert. Aus diesem Grund sind bei teureren Netzwerkcontrollern viele
Funktionen der Netzwerkkontrolle und Datenmanagement auf die Hardwareplatine mig-
riert worden; der Hauptprozessor muss nur wenige Anweisungen ausführen, um auf hohem
Niveau (in den oberen Schichten) Funktionen anzustoßen und Resultate entgegenzunehmen.
Dabei spielt es keine Rolle, ob die von dem Netzwerkcontroller übernommenen Funk-
tionen durch einen eigenen Prozessor mit Speicher und Programm erledigt werden oder
durch einen dedizierten Satz von Chips: Durch die eindeutige Schnittstellendefinition wird
die angeforderte Dienstleistung erbracht, egal wie. Stellt die virtuelle Maschine nicht die
originale Schnittstelle bereit, sondern eine vereinfachte, modifizierte Version davon, so
3URJUDPPLQ-DYD&RGH
-DYD&RGHĺ0DVFKLQHQFRGH
3URJUDPPLQ-DYD&RGH
0LFURFRGH
XQG&38+DUGZDUH&38+DUGZDUH
Abb. 1.13 Software-Hardware-Migration des Java-Codes

### Seite 35

16 1 Übersicht
wird dies „Paravirtualisierung“ genannt. Wird so die darunter liegende Hardware besser
ausgenutzt, kann man damit die Leistungsfähigkeit der virtuellen Maschine verbessern.
Wird für das Hardwaredesign auch eine formale Sprache verwendet (z. B. VHDL), so
spielen die Unterschiede in der Änderbarkeit der migrierten und nicht-migrierten Imple-
mentierungen immer weniger eine Rolle. Entscheidend sind vielmehr andere Aspekte wie
Kosten, Standards, Normen und Kundenwünsche.
1.6 Virtuelle Betriebssysteme
Die Virtualisierung, also das Einziehen einer abstrahierenden Zwischenschicht zwischen
den Geräten und die bedienenden Programme, macht auch vor dem Betriebssystem nicht
Halt. Eine beliebte Maßnahme in Rechenzentren, die Dienstleistungen von Rechnern
(Serverpool) erbringen, besteht darin, die feste Zuordnung von Dienstleitung zu einem
Rechner oder dem Rechner eines Maschinentyps aufzubrechen und die Dienstleistungen
geeignet auf die vorhandenen Rechner und Multiprozessorkerne zu verteilen.
Dies hat verschiedene V orteile:
• Damit ist es möglich, Rechenzentren dynamisch wachsen zu lassen (Skalierbarkeit),
je nach Anforderungen des Betriebs. Es werden nicht mehr Rechner für bestimmte
Betriebssysteme benötigt, sondern man kann alle Anwendungen auf demselben Rech-
nerpool laufen lassen.
• Da ein großer Teil der Betriebskosten auf die verbrauchte Energie für den Rechner -
betrieb und seine Klimatisierung entfällt, kann man erheblich Geld sparen (ca. 30 %),
wenn man die Jobs auf wenige Rechner konzentriert und unbenutzte Kapazitäten dyna-
misch ab oder zuschaltet. V oraussetzung dafür ist, dass mit den Jobs auch der gesamt
Prozesskontext des Betriebssystems verschoben werden kann; am besten gleich das
ganze Betriebssystem.
• Auch ein Lastenausgleich zwischen verschiedenen Rechnern ist dynamisch während
des Betriebs möglich.
• Man kann so auch alte Programme (Legacy-Anwendungen), die nur auf bestimm-
ten veralteten Betriebssystemen (Legacy-Betriebssysteme) oder veralteter Hardware
laufen, problemlos weiterhin betreiben.
• Ein weiterer V orteil einer solchen Serverkonsolidierung liegt in der dazu notwendigen
Modularisierung und Konzentration der Dienste und Bibliotheken auf wenige, ver -
schiebbare Pakete, die überall eingesetzt werden können.
• Ein wichtiges Merkmal wird auch gern bei der Softwareentwicklung ausgenutzt: Möchte
man eine Applikation gleichzeitig für eine Vielzahl von Betriebssystemen und Hard-
warekonfigurationen entwickeln, so ist das Entwickeln und Testen auf so vielen Konfi-
gurationen sehr aufwändig, teuer und zeitraubend. Besser geht es, wenn man alle Kon-
figurationen (z. B. Smartphones) als virtuelle Maschinen auf demselben Rechner laufen
lassen kann. Man spart sich so die Anschaffung der unterschiedlichen Rechner und, für
die Tests auf derselben Hardware, das umständliche Neubooten jeder Konfiguration.

### Seite 36

1.6 Virtuelle Betriebssysteme 17
• Insgesamt ist durch die neuere Entwicklung der Virtualisierung und ihrer Hardware-
unterstützung durch die CPU nur noch ein geringer Leistungsverlust von ca. 5–10 %
gegenüber einer traditionellen Rechnerkonfigurationen zu beobachten (Hardt 2005).
Die Virtualisierung der Rechnerressourcen bedeutet, dass jede Anwendung vollständig
unabhängig von der tatsächlichen Rechnerkonfiguration laufen kann. Dies bedeutet, dass
Rechnerressourcen universell gehandelt werden können. Beispielsweise ist die Deutsche
Börse AG in Frankfurt in den Handel mit Virtuellen Maschinen eingestiegen. Unter dem
Schlagwort „Infrastructure as a Service“ IaaS vermarktet sie die Angebote von Betreibern
großer Rechenzentren wie Amazon. Entscheidend für den Preis einer solchen virtuellen
Maschine sind nicht nur Hardwaredaten wie garantierte CPU-Leistung, Hauptspeicher -
größe und Massenspeicher, sondern auch der Vertragskontext wie Leistungsklasse, War -
tungsart oder der dafür gültige Rechtsrahmen, wie etwa das Staatsgebiet. Hier sind euro-
päische IT-Unternehmen durch das europäische Datenschutzrecht in besserer Position!
Problematisch bei solchen Ansätzen ist die Definition der garantierten Leistungsdaten
(Benchmarks). Die aktuelle Leistung ist meist von vielen Faktoren abhängig, etwa der
Implementierung der virtuellen Maschinen, der Last der parallel laufenden, anderen Auf-
gaben, CPU-Typ und weiterer Kontextfaktoren. Hier ist noch viel Forschung nötig.
Wie funktioniert die Virtualisierung genau? Je nach Sachlage und Anforderungen gibt
es unterschiedliche Virtualisierungsarten für einen Server (virtual server). Allen gemein-
sam ist, dass jeweils eine Zwischenschicht eingezogen wird, die die Funktionalität einer
virtuellen Maschine hat. Da sie alles kontrolliert, was an Funktionalität bei der Schicht
darunter vorhanden ist, wird sie auch virtual machine monitor (VMM) oder Hypervisor
genannt. In Abb. 1.14 sind drei verschiedene Möglichkeiten gezeigt, wobei jeweils die
Grenze zwischen user mode und kernel mode als roter Strich eingezeichnet ist.
Diese Überlegungen werden in den folgenden Abschnitten genauer erklärt.
26&RQWDLQHU
+:9LUWXDOLVLHUXQJ
ƉƉϭ
ƉƉϭƉƉϭ ͘͘͘ ͘͘͘
͘͘͘ ƉƉE
ƉƉEƉƉE ^Ͳ<ĞƌŶ
^Ͳ<ĞƌŶ
^Ͳ<ĞƌŶ ^Ͳ<ĞƌŶ>ĂƵĨǌĞŝƚ
+DUGZDUH+DUGZDUH+DUGZDUH
^ǇƐĐĂůů
^ǇƐĐĂůů ,ǇƉĞƌǀŝƐŽƌdǇƉϮ
,ǇƉĞƌǀŝƐŽƌdǇƉϭ ,ǇƉĞƌǀŝƐŽƌdǇƉϭ
sŝƌƚƵĂůDĂĐŚŝŶĞDŽŶŝƚŽƌsDD
sŝƌƚƵĂůDĂĐŚŝŶĞDŽŶŝƚŽƌsDD
sŝƌƚƵĂůDĂĐŚŝŶĞDŽŶŝƚŽƌsDD
9LUWXDOLVLHUXQJPLW
26&RQWDLQHU3DUDYLUWXDOLVLHUXQJ
26&RQWDLQHU
Abb. 1.14 Virtualisierungsarten bei Servern

### Seite 37

18 1 Übersicht
1.6.1 Paravirtualisierung
Möchte man mehrere verschiedene Betriebssysteme mit den dazu gehörenden Anwendun-
gen auf demselben Rechner gleichzeitig laufen lassen, so kann man den Hypervisor direkt
zwischen traditionellem Betriebssystemkern und der Hardware installieren (bare metal
hypervisor, hypervisor type 1), siehe Abb. 1.14 links. Natürlich müssen die Betriebssys-
temkerne, die darauf ablaufen, Code desselben CPU-Typs enthalten, also beispielsweise
für Intel x86.
Diese Art von Virtualisierung wird auch Paravirtualisierung genannt, wobei sich
Hypervisor und Betriebssystemkern logisch über einander befinden, siehe Abb. 1.15.
Allerdings werden Ring 2 und 3 meist nicht benutzt, so dass in der 64 Bit-Architektur
(x86-64-Architektur) hardwaremäßig auf diese Schichten verzichtet wurde. In solchen
Systemen mit nur zwei Sicherheitsstufen sind Betriebssystem und Hypervisor entweder
nebeneinander in derselben Schicht 0 (Ring 0) im kernel mode, oder das Betriebssystem
wird in einen gesonderten Prozess in den user mode verschoben.
Da das Betriebssystem nur mittels des Hypervisors auf die Hardware zugreifen
sollte, müssen dazu vorher aus dem Betriebssystemcode alle Hardwareinstruktionen
entfernt werden, die problematisch sind. Dies sind nach (Popek und Goldberg 1974)
alle Befehle, die keine Unterbrechung (trap) hervorrufen wie die Systemaufrufe („pri-
vilegierte Befehle“), sondern unüberwacht eine Hardwarekontrolle ausüben („sensitive
Befehle“). Dazu gehört beispielsweise das Setzen oder Löschen von Bits in Controllern
und CPU-Registern. Diese Befehle werden ersetzt durch Aufrufe an den Hypervisor
(Hypercalls), so dass der Hypervisor die volle Kontrolle erhält. In Abb. 1.15 ist dies
visualisiert.
Dabei werden die „normalen“ Betriebssystemaufrufe zunächst in den Hypervisor umge-
leitet, der dann wiederum die Betriebssystemfunktionen aufruft, die dann über Hypercalls
die eigentlichen Hardwarefunktionen bewirken.
Beispiele sind Red Hat Fedora mit XEN, z/VM, VMware ESX, Hyper-V , die open
source SUN VirtualBox.org, Citrix Xenserver, Microsoft Hyper-V und Virtual Iron.
ZŝŶŐϯ ƵƐĞƌŵŽĚĞ
ZŝŶŐϮ
ZŝŶŐϭ ĞƚƌŝĞďƐƐǇƐƚĞŵ
ZŝŶŐϬ <ĞƌŶĞůŵŽĚĞ ŚǇƉĞƌĐĂůůƐ
,ǇƉĞƌǀŝƐŽƌ dǇƉϭ
,ĂƌĚǁĂƌĞ
ƉƉůŝŬĂƚŝŽŶ
Abb. 1.15 Schichten bei der
Paravirtualisierung

### Seite 38

1.6 Virtuelle Betriebssysteme 19
1.6.2 Virtualisierung mit BS-Containern
Bei vielen Anwendungen reicht es auch aus, nur die benötigten Systemfunktionen, also
eine Teilmenge des Kerns, den Anwendungen zur Verfügung zu stellen und sie damit
unabhängig zu machen. Die Anwendungen und die benötigte Laufzeitumgebung zusam-
men werden gekapselt und bilden einen Container (Jail), siehe Abb. 1.14 mitte. Dies hat
den V orteil, dass alle internen Referenzen der Programme, wie offene Dateien, der Pro-
grammzustand, belegte Puffer, andere benötigte Programme usw. nicht gewechselt werden
müssen, wenn die Anwendung gewechselt wird. Der Hypervisor ermöglicht dann die par-
allele Abarbeitung verschiedener Container und damit auch verschiedener Laufzeitanwen-
dungen. Dies wird als Virtualisierung mit BS-Containern bezeichnet. Der Übergang zum
kernel mode geschieht hier erst beim Übergang zum Hypervisor.
Beispiele sind etwa Open Solaris, BSD jails, Mac-on-Linux, OpenVZ, Linux-VServer, …
1.6.3 Vollständige Virtualisierung
Möchte man nicht das gleiche Betriebssystem nutzen, sondern ein anderes, so müssen die
Systemaufrufe für die Verwaltung der Hardware wie CPU, Hauptspeicher, Festplatten-
speicher, Netzwerke usw. in die Aufrufe des aktuellen Betriebssystems übersetzt werden,
das auf der Hardware läuft. Mit anderen Worten, die gesamte Maschinenhardware wird
virtualisiert (Vollständige Virtualisierung). Dies ist die Aufgabe des Hypervisors oder Vir-
tuellen Maschinenmonitors, der eine entsprechende Schnittstelle nach oben anbietet und
dazu nach unten die Schnittstelle des aktuellen Betriebssystems, die Liste der Systemauf-
rufe, nutzt.
Auch hier kann man ihn in einen nicht genutzten Ring legen und damit zwischen die
Anwendungs- und Betriebssystemschicht.
Beispiele VMware, x86 Version von MS Virtual PC, XEN 3 auf Intel VT-x bzw. AMD-V .
1.6.4 Hardware-Virtualisierung
Möchte man auch Rechner und Betriebssystemkern noch weiter entkoppeln und etwa
Betriebssysteme ganz anderer CPU-Typen auf dem Server ablaufen lassen, so dient der
Hypervisor als Vermittler zwischen verschiedenen CPU-Typen und Betriebssystemfunk-
tionen. Dies wird als Hardware-Virtualisierung bezeichnet. Hier gilt die gleiche Schich-
tung wie bei der vollständigen Virtualisierung in Abb. 1.14 rechts und Abb. 1.16, aber
es werden nicht die Systemanforderungen, sondern die Maschineninstruktionen der
anderen CPU emuliert, also aus den echten Instruktionen nachgebildet (hardware emu-
lation). Dabei muss, ebenso wie bei der Paravirtualisierung oder der Virtualisierung mit
Betriebssystemcontainern, das Betriebssystem angepasst werden, um die sensitiven und

### Seite 39

20 1 Übersicht
privilegierten Befehle auch mittels Hypervisor in der Hardware ausführen zu können.
Deshalb sind diese Techniken meist bei quelloffenen Betriebssystemen wie Unix, nicht
aber bei Windows, üblich.
Beispiel sind Pocket PC auf MS Virtual PC oder eingebettete Systeme auf x86, MIPS,
ARM und PowerPC Basis, die emuliert werden.
1.6.5 Virtualisierungserweiterungen
In Absch. 1.2 hatten wir ein Schichten- und Zwiebelschalenmodell für den CPU-Zugriff einge-
führt. Diese CPU-Architektur von konzentrischen Ringen stößt an ihre Grenzen beim Versuch,
zwischen Hardware und Betriebssystem eine weitere Schicht zur Überwachung und Manage-
ment des laufenden Betriebs, einen Hypervisor, einzuziehen. Eine Möglichkeit besteht nun
darin, den Hypervisor in Ring 0 anzusiedeln und das Betriebssystem in Ring 1 („V ollständige
Virtualisierung“). Dazu muss man aber vorher zur Laufzeit alle Systemaufrufe (Traps) zum
Hypervisor umlenken bzw. durch „normale“ Aufrufe zum Betriebssystem im user mode erset-
zen (binary translation). Eine weitere mögliche Lösung nutzt Ring 0 für beide: Betriebssys-
tem und Hypervisor („Paravirtualisierung“). Auch hier müssen im Betriebssystem die Aufrufe
der Hardware durch entsprechende Aufrufe (hyper calls) des Hypervisors ersetzt werden.
Die Ersetzung von Instruktionen im laufenden Betrieb ist umständlich, fehleranfäl-
lig und kostet Zeit. Wesentlich einfacher ist nun, die inzwischen für die Virtualisierung
übliche Lösung: Man führt einfach eine weitere Schicht (Ring −1) in der Hardware ein, in
der der Hypervisor ausgeführt wird (Intel VT, AMD-V), siehe Abb. 1.17.
Damit kann man das unmodifizierte Originalbetriebssystem mittels seiner privilegierten
Aufrufe (system calls) verwenden, ohne deshalb die Kontrolle aufzugeben: Bei jedem
sensitiven oder privilegierten Aufruf wird der Hypervisor angesprungen. Hier gibt es also
neben dem eigentlichen kernel mode noch einen weiteren, noch stärker privilegierten
Modus: den root mode in Ring −1, der zusätzliche, privilegierte Hardwareinstruktionen
bereitstellt und dem Hypervisor vorbehalten ist, siehe (vmware 2007).
In dem neueren Linuxkern ab Version 2.6.20 (2007) ist bereits eine kernel-based virtual
machine (KVM) enthalten, die auf obigen Hardwareerweiterungen basiert.
ZŝŶŐϯ ƵƐĞƌŵŽĚĞ ƉƉůŝŬĂƟŽŶ
ZŝŶŐϮ 'ĂƐƚͲĞƚƌŝĞďƐƐǇƐƚĞŵ
ZŝŶŐϭ ,ǇƉĞƌǀŝƐŽƌdǇƉϮ
ZŝŶŐϬ <ĞƌŶĞůŵŽĚĞ ,ŽƐƚͲĞƚƌŝĞďƐƐǇƐƚĞŵ
,ĂƌĚǁĂƌĞ
Abb. 1.16 Schichten bei der
vollständigen Virtualisierung

### Seite 40

1.7 Betriebssysteme für eingebettete Systeme 21
1.7 Betriebssysteme für eingebettete Systeme
In über 92 % aller Computersysteme werden universelle Betriebssysteme wie Unix oder
Windows nicht benötigt, da sie sehr spezielle Aufgaben zu bewältigen haben, etwa einen
Fahrstuhl zu betätigen oder einen Fahrkartenautomaten zu managen. Üblicherweise laufen
dazu nur wenige, genau festgelegte und gut bekannte Prozesse und Programme, so dass
die Interaktion mit der Umgebung und die benötigten Ressourcen genau festgelegt werden
können.
Solche Systeme heißen „eingebettete Systeme“ (embedded systems) und treten als
Rechnersysteme nach außen hin nicht in Erscheinung: Wer vermutet schon in der Motor-
elektronik, im Handy, im Radio oder in der Waschmaschine eigene Rechnersysteme? Tat-
sächlich kommt die „Intelligenz“ solcher Alltagsmaschinen ohne eigene Rechnersysteme
mit CPU, Speicher, Ein- und Ausgabebausteinen nicht mehr aus. Natürlich hat ein solches
System auch ein Betriebssystem. Es zeichnet sich aus durch
• kleineren Betriebssystemkern
• Eliminierung von Fehlerquellen
• robusteres Gesamtsystem
• Beschleunigung des Systemstarts und -stopps
• Keine Portierung oder Veränderung bestehender Anwendungen nötig
Hier macht eine vollständige Betriebssysteminstallation mit allen Komponenten keinen
Sinn, sondern schafft nur unerwünschte zusätzliche Fehlerquellen. Alle unnötigen Teile
wie Treiber nicht vorhandener Geräte, PnP, Sicherheitsüberprüfungen, unnötige Protokoll-
schichten usw. können weggelassen werden. Durch eine Reduktion des Betriebssystems
auf die tatsächlich erforderlichen Komponenten wird ein System erzeugt, welches erheb-
lich robuster und besser geschützt gegen Fehlbedienungen und Missbrauch ist. Teilweise
kann sogar eines der kritischsten Systemkomponenten, der Festplattenspeicher, einge-
spart werden. Das wesentlich kompaktere System passt auf einen robusten Speicherchip
ZŝŶŐϯ ƵƐĞƌŵŽĚĞ ƉƉůŝŬĂƟŽŶ
ZŝŶŐϮ
ZŝŶŐϭ
ZŝŶŐϬ ŬĞƌŶĞůŵŽĚĞ ĞƚƌŝĞďƐƐǇƐƚĞŵ
ŚǇƉĞƌĐĂůůƐ
ZŝŶŐ-1 ƌŽŽƚŵŽĚĞ ,ǇƉĞƌǀŝƐŽƌ
,ĂƌĚǁĂƌĞ
Abb. 1.17 Hardwareerweiterung für die Virtualisierung

### Seite 41

22 1 Übersicht
(FLASH-Memory). So lassen sich sogar Gesamtsysteme ohne bewegliche Teile realisie-
ren und so die Lebensdauer und Zuverlässigkeit erhöhen.
Das speziell angepasste eingebettete Betriebssystem startet in erheblich kürzerer Zeit, als
eine Standard-Installation des Betriebssystems. Es existieren auch Embedded-Versionen,
die ohne BIOS auskommen. Innerhalb weniger, meist einzelner Sekunden ist das System
dann voll einsatzbereit. Genauso einfach kann das System abgeschaltet werden. Ein geord-
netes „Herunterfahren“, Dogma der Standard-Betriebssysteminstallationen, entfällt voll-
kommen. Ein Beispiel dafür ist ein Microsystems für Roboter (Koubaa 2017).
Die Programmentwicklung für ein solches System ist nicht ganz unproblematisch. Ver-
wenden wir Betriebssysteme, welche die gleichen Schnittstellen zum Kern anbieten wie
die vorhandenen V ollversionen, etwa das kostenlose embedded Linux oder lizenzpflichtige
Windows CE, so können wir unsere auf den V ollversionen entwickelten Programme auch
auf dem eingebetteten System einsetzen. Zwar müssen nicht alle eingebetteten Systeme
harte Echtzeitbedingungen erfüllen und benötigen deshalb nicht unbedingt die Scheduler
aus Kap. 2, aber alle Programme müssen auf dem Zielsystem getestet werden, bevor sie in
ROM oder EPROM gebrannt und dort fest eingesetzt werden. In Abb. 1.18 ist dazu eine
Skizze gezeigt, wie die Programmentwicklung üblicherweise durchgeführt wird.
Nach jedem Kompilieren und Binden wird das fertige Programm über eine Kommuni-
kationsleitung in das eingebettete System geladen und dort getestet. Spezielle Kommu-
nikationsprogramme bewirken das Übermitteln des Codes an einen Stellvertreterprozess
im eingebetteten System, der diesen Kindprozess in den Speicher lädt und dann startet.
Erfolgt ein Fehlerabbruch oder das „normale“ Ende des Kindes, so erhält der Stellvertre-
terprozess die Kontrolle zurück und teilt dieses seinem Pendant auf dem Entwicklungs-
rechner mit. Kommunikationsprogramme und Stellvertreterprozesse sind üblicherweise
Teil einer Entwicklungsumgebung auf dem Entwicklungsrechner, die entweder vom Her-
steller des eingebetteten Systems (z. B. Motorola, Intel) oder vom Hersteller des eingebet-
teten Betriebssystems (z. B. Microsoft) angeboten werden.
1.8 Betriebssysteme in Mehrprozessorarchitekturen
Für die Verwaltung von Betriebsmitteln ist es ziemlich wichtig, welche Beziehungen und
Abhängigkeiten zwischen ihnen bestehen. Unabhängig von dem benutzten Prozessortyp,
&38
5$0
520
$'
'$
6HULHOO
SDUDOOHO
,2
(LQJHEHWWHWHV6\VWHP (QWZLFNOXQJVUHFKQHUAbb. 1.18 Programment-
wicklung bei eingebetteten
Systemen

### Seite 42

1.8 Betriebssysteme in Mehrprozessorarchitekturen 23
Bustyp oder Speicherplattenfabrikat muss man einige grundsätzliche Konfigurationen unter-
scheiden. Im einfachsten, klassischen Fall gibt es nur einen Prozessor, der Haupt- und Massen-
speicher benutzt, um das Betriebssystem (BS) und die Programme der Benutzer auszuführen,
siehe Abb. 1.19. Die Ein- und Ausgabe (Bildschirm, Tastatur, Maus) ist dabei nicht gezeigt.
Ein solches Einprozessorsystem (single processor) kann man mit mehreren Prozesso-
ren (meist bis zu 16 Stück) aufrüsten. Je nachdem, wie man die Prozessoren miteinander
koppelt, ergeben sich unterschiedliche Architekturen.
Im einfachsten Fall kann man nur multiple Prozessoren an die Stelle des einzelnen Pro-
zessor setzen, etwa durch Anreicherung mit mehreren Kernen wie sie bereits in einfachen
PCs anzutreffen sind. Hierbei ändert sich aber nichts weiter an der Hauptarchitektur, so
dass die multiplen Kerne sich die Datenwege zum Hauptspeicher und Ein-/Ausgabe zum
Massenspeicher teilen müssen. Dies begrenzt die Leistung des Gesamtsystems stark.
Die nächste Stufe sieht Replikationen der CPU vor, die parallel an einem besonderen
Verbindungsnetzwerk (z. B. an einem Multi-Master-Systembus) hängen. In Abb. 1.20 ist
ein solches Multiprozessorsystem abgebildet.
Die Prozessormodule sind auf der einen Seite des Netzwerks und die Speichermo-
dule auf der anderen lokalisiert. Für jeden Daten- und Programmcodezugriff wird zwi-
schen ihnen eine Verbindung hergestellt, die während der Anforderungszeit bestehen
bleibt. Diese Architektur wird deshalb auch „Tanzsaal“-Konzept genannt. Sie ist bei den
0DVVHQ
VSHLFKHU
3URJUDPPH
'DWHQ
%6
.HUQ
1XW]HU
3URJUDPP
 1XW]HUQ
3URJUDPP
+DXSWVSHLFKHU
3UR]HVV
Abb. 1.19 Ein Einprozessor- oder Mehrkernsystem
Verbindungsnetzwerk
„Tanzsaal“
BS-
Kern
Nutzer 1
Programm
.. Nutzern
Programm
P1  P2 … Pn
Abb. 1.20 Multiprozessor system

### Seite 43

24 1 Übersicht
Großrechner (main frames, ab 250.000$) weit verbreitet, wobei die Anzahl der Prozesso-
ren >16 (bis einige tausend CPUs), die Hauptspeichergröße einige tausend GByte und die
Anzahl der I/O-Einheiten mehrere hundert bis tausend beträgt.
Eine derartige Architektur ermöglicht zwar einen parallelen Zugriff der Prozessoren auf
den Hauptspeicher, führt aber auch leicht zu Leistungs- (Performance)-Einbußen, da ein-
zelne Netzwerkknoten für Speicherzugriffe bestimmter, oft benutzter Teile des Betriebs-
systems stark belastet werden („hot spots“) und sich dort Warteschlangen ausbilden.
Abhilfe kommt in diesem Fall aus der Beobachtung, dass die Prozessoren meist nur einen
eng begrenzten Programmteil referenzieren. Der Speicher kann deshalb aufgeteilt und der
relevante Teil „dichter“ an den jeweiligen Prozessor herangebracht werden (Abb. 1.21).
Die feste Aufteilung muss natürlich auch durch den Compiler unterstützt werden, der das
Anwenderprogramm auf die Rechner entsprechend aufteilt, siehe Abschn. 6.4. Ein solches
Mehrrechnersystem ist auch als „V orzimmer“-Architektur bekannt.
Als dritte Möglichkeit der Anordnung der Verbindungen existiert das Rechnernetz.
Hier sind vollkommen unabhängige Rechner mit jeweils eigenem (nicht notwendig glei-
chem!) Betriebssystem lose miteinander über ein Netzwerk gekoppelt, s. Abb. 1.22. Ist das
Netzwerk sehr schnell und sind die Rechner räumlich dicht beieinander, so spricht man
auch von einem Cluster.
9HUELQGXQJVQHW]ZHUN
Ä9RU]LPPHU³
%6
.HUQ
%6
.HUQ
1XW]HU
3URJUDPP
3 3Q«
1XW]HUQ
3URJUDPP
Abb. 1.21 Mehrrechnersystem
9HUELQGXQJVQHW]ZHUN
/$1
3 3Q«
%6
.HUQ
1XW]HU
3URJUDPP
%6
.HUQ
1XW]HUQ
3URJUDPP
Abb. 1.22 Rechnernetz

### Seite 44

1.9 Aufgaben 25
Ist eine Software auf einem Rechner installiert, so dass der Rechner als Dienstleister
(Server) Aufträge für einen anderen Rechner (Kunden, Client) ausführen kann, so spricht
man von einer Client-Server-Architektur. Beispiele für Dienstleistungen sind numeri-
sche Rechnungen mit Supercomputern (number cruncher), Ausdruck von Dateien (print
server) oder das Bereithalten von Dateien (file server).
Jede der vorgestellten Rechnerarchitekturen besitzt ihre V or- und Nachteile. Für uns ist
dabei wichtig: Jede benötigt spezielle Mechanismen, um einer Interprozessorkommuni-
kation und Zugriffssynchronisation bei den Betriebsmitteln zu erreichen. Im kommenden
Kapitel wird darauf näher eingegangen.
1.9 Aufgaben
Aufgabe 1-1 Betriebssystem
Der Zweck eines Betriebssystems besteht beispielsweise in der Verteilung von Betriebs-
mitteln auf die sich bewerbenden Benutzer.1
a) Wie ist der grobe Aufbau eines Betriebssystems?
b) Welche Betriebsmittel kennen Sie?
c) Welche Benutzer könnten sich bewerben? (Dabei ist der Begriff„Benutzer“ allge-
mein gefasst!)
d) Welche Anforderungen stellt ein menschlicher Benutzer an das Betriebssystem?
Aufgabe 1-2 UNIX System calls
a) Finden Sie heraus, wie viele System Calls auf einem aktuellen x86_64-Linux-Sys-
tem definiert sind. Beispielsweise können Sie dazu die entsprechenden Head-
er-Dateien, mit denen der Kernel übersetzt wurde, inspizieren. Auf vielen Rechnern
finden Sie diese im Verzeichnis /lib/modules/[aktuelle Kernelversion]/build, wobei
Sie die [aktuelle Kernelversion] in einem Terminalfenster mit den Befehl uname -r
herausfinden können.
Alternativ können Sie auch eine aktuelle Linux-Distribution in der 64-Bit-Variante,
wie beispielsweise Ubuntu (http://www.ubuntu.com/) in einer virtuellen Maschine
installieren. Beachten Sie jedoch, dass unter Umständen das Paket linux-headers-ge-
neric installiert werden muss, damit die Header-Dateien bereitstehen.
Geben Sie die Zahl der definierten Systemaufrufe an und erläutern Sie, wie Sie
auf diese gekommen sind.
b) In welche Funktionsgruppen lassen sie sich einteilen?
1verkürzt für Benutzerinnen und Benutzer.

### Seite 45

26 1 Übersicht
c) Welcher Assemblerbefehl sorgt bei x86-Prozessoren für die Auslösung der Trap bei
einem Systemaufruf, und wie wird dabei die Information übergeben, welcher Sys-
temaufruf ausgeführt werden soll?
Tip: Wälzen Sie entweder das Handbuch (C- oder Assembler-Programmierung!),
oder lassen Sie von einem Debugger einen in C oder einer anderen Programmier -
sprache geschriebenen Betriebssystemaufruf rückübersetzen in Assembler. Auch
include files von C (syscall.h, trap.h, proc.h, kernel.h, …) geben interessante Hinweise.
Aufgabe 1-3 Schichtenmodell und Kernel
a) Beschreiben Sie mit Hilfe eines Beispiels das Schichtenmodell. (Das Beispiel sollte
dabei kein Betriebssystem sein.)
b) Erläutern Sie kurz die Begriffe „virtuelle Maschine“ und „Schnittstelle“.
c) Warum werden im Schichtenmodell Schnittstellen benötigt?
d) Das Mach-Betriebssystem besteht neben dem Kernel aus verschiedenen Modulen.
Doch unterstützen die meisten modernen unixoiden Systeme das Laden von
Modulen zur Laufzeit.
Eine Übersicht über alle aktuell geladenen Module lässt sich in einem Termi-
nalfenster wie folgt ausgeben:
• Unter Linux: lsmod
• Unter FreeBSD: kldstat
• Unter Solaris: modinfo
• Unter OS X: kextstat
Überzeugen Sie sich auf einem beliebigen der aufgeführten Systeme, dass tatsäch-
lich Module geladen sind.
– Was ist bei diesen Betriebssystemen der Unterschied zu besagten modularen
Komponenten im Mach-Betriebssystem?
– Welche V or- und Nachteile ergeben sich daraus?
e) Informieren Sie sich über GNU Hurd. Welches grundlegende Konzept wird bei
Hurd verfolgt und wodurch zeichnet es sich aus?
Literatur
Custer H.: Inside Windows NT. Microsoft Press, Redmond, Washington 1993
Hardt M.: Virtualisation for Grid Computing. Cracow Grid Workshop, Krakow, Poland 2005
Koubaa, A.: Robot Operating System (ROS). Springer Verlag 2017
Popek G.J, Goldberg R.P.: Formal Requirements for Virtualizable Third Generation Architectures.
Commun. of the ACM 17, 412–421 (1974)
Vmware Inc.: Understanding full virtualization, paravirtualization and hardware assist. White paper,
vmware, Palo Alto, CA 2007 http://www.vmware.com/files/pdf/VMware_paravirtualization.pdf
[10.5.2016]

### Seite 46

27
© Springer-Verlag GmbH Deutschland 2017
R. Brause, Betriebssysteme,
DOI 10.1007/978-3-662-54100-5_2
Inhaltsverzeichnis
2.1 Prozesszustände . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  29
2.1.1 Beispiel UNIX . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  30
2.1.2 Beispiel Windows NT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  33
2.1.3 Leichtgewichtsprozesse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  34
2.1.4 Aufgaben  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  37
2.2 Prozessscheduling  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  39
2.2.1 Zielkonflikte . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  40
2.2.2 Non-präemptives Scheduling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  41
2.2.3 Präemptives Scheduling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  44
2.2.4 Mehrere Warteschlangen und Scheduler . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  46
2.2.5 Scheduling in Echtzeitbetriebssystemen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  47
2.2.6 Scheduling in Multiprozessorsystemen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  53
2.2.7 Stochastische Schedulingmodelle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  60
2.2.8 Beispiel UNIX: Scheduling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  62
2.2.9 Beispiel: Scheduling in Windows NT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  64
2.2.10 Aufgaben  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  65
2.3 Prozesssynchronisation  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  67
2.3.1 Race conditions und kritische Abschnitte . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  68
2.3.2 Signale, Semaphore und atomare Aktionen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  69
2.3.3 Beispiel UNIX: Semaphore . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  77
2.3.4 Beispiel Windows NT: Semaphore . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  78
2.3.5 Anwendungen  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  79
2.3.6 Aufgaben zur Prozesssynchronisation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  85
2.3.7 Kritische Bereiche und Monitore . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  88
2.3.8 Verklemmungen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  92
2.3.9 Aufgaben zu Verklemmungen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  101
2.4 Prozesskommunikation  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  103
2.4.1 Kommunikation mit Nachrichten . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  103
2.4.2 Beispiel UNIX: Interprozesskommunikation mit pipes . . . . . . . . . . . . . . . . . . . .  107
Prozesse 2

### Seite 47

28 2 Prozesse
2.4.3 Beispiel Windows NT: Interprozesskommunikation mit pipes . . . . . . . . . . . . . .  108
2.4.4 Prozesssynchronisation durch Kommunikation . . . . . . . . . . . . . . . . . . . . . . . . . .  108
2.4.5 Implizite und explizite Kommunikation  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  117
2.4.6 Aufgaben zur Prozesskommunikation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  118
Literatur . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  118
In früheren Zeiten waren die Rechner zu jedem Zeitpunkt für nur eine Hauptaufgabe
bestimmt. Alle Programme wurden zu einem Paket geschnürt und liefen nacheinander
durch (Stapelverarbeitung oder Batch-Betrieb). Üblicherweise gibt es heutzutage aber
nicht nur ein Programm auf einem Rechner, sondern mehrere (Mehrprogrammbetrieb,
multi-tasking). Auch gibt es nicht nur einen Benutzer (single user), sondern mehrere
(Mehrbenutzerbetrieb, multi-user).
Um Konflikte zwischen ihnen bei der Benutzung des Rechners zu vermeiden, muss
die Verteilung der Betriebsmittel auf die Programme geregelt werden. Dies spart außer -
dem noch Rechnerzeit und erniedrigt damit die Bearbeitungszeiten. Beispielsweise kann
die Zuteilung des Hauptprozessors (Central Processing Unit CPU) für den Ausdruck von
Text parallel zu einer Textverarbeitung so geregelt werden, dass die Textverarbeitung
die CPU in der Zeit erhält, in der der Drucker ein Zeichen ausdruckt. Ist dies erledigt,
schiebt der Prozessor ein neues Zeichen dem Drucker nach und arbeitet dann weiter an
der Textverarbeitung.
Zusätzlich zu jedem Programm muss also gespeichert werden, welche Betriebsmittel es
benötigt: Speicherplatz, CPU-Zeit, CPU-Inhalt etc. Die gesamte Zustandsinformation der
Betriebsmittel für ein Programm wird als eine Einheit angesehen und als Prozess (task)
bezeichnet (Abb. 2.1).
Ein Prozess kann auch einen anderen Prozess erzeugen, wobei der erzeugende Prozess
als Elternprozess und der erzeugte Prozess als Kindsprozess bezeichnet wird.
Ein Mehrprogrammsystem (multiprogramming system) erlaubt also das „gleichzei-
tige“ Ausführen mehrerer Programme und damit mehrerer Prozesse (MehrProzesssys-
tem, multi-tasking system). Ein Programm (Job ) kann dabei auch selbst mehrere Pro-
zesse erzeugen.
3UR]HVV
&38
5HJLVWHU
008
5HJLVWHU
'DWHLLQIR
=XJULIIV
UHFKWH
.HUQHO
VWDFN
3UR]HVVNRQWH[W
3UR
JUDPP
6WDFN
'DWHQ
Abb. 2.1 Zusammensetzung
der Prozessdaten

### Seite 48

2.1 Prozesszustände 29
Beispiel UNIX
Die Systemprogramme werden in UNIX als Bausteine angesehen, die beliebig miteinan-
der zu neuen, komplexen Lösungen kombiniert werden können. Die Unabhängigkeit der
Prozesse und damit auch der Prozesse erlaubt nun in UNIX, mehrere Prozesse gleich-
zeitig zu starten. Beispielsweise kann man das Programm cat, das mehrere Dateien anei-
nander hängt, das Programm pr, das einen Text formatiert, und das Programm lpr, das
einen Text ausdruckt, durch die Eingabe
cat Text1 Text2 | pr | lpr
miteinander verbinden: Die Texte „Text1“ und „Text2“ werden aneinandergehängt,
formatiert und dann ausgedruckt. Der Interpreter (shell), dem der Befehl übergeben
wird, startet dazu die drei Programme als drei eigene Prozesse, wobei das Zeichen
„|“ ein Umlenken der Ausgabe des einen Programms in die Eingabe des anderen ver -
anlasst. Gibt es mehrere Prozessoren im System, so kann jedem Prozessor ein Prozess
zugeordnet werden und die obige Operation tatsächlich parallel ablaufen. Ansonsten
bearbeitet der eine Prozessor immer nur ein Stück eines Prozesses und schaltet dann
um zum nächsten.
Zu einem diskreten Zeitpunkt ist bei einem Einprozessorsystem nur immer ein Prozess
aktiv; die anderen sind blockiert und warten. Dies wollen wir näher betrachten.
2.1 Prozesszustände
Zusätzlich zu dem Zustand „aktiv“ (running) für den einen, aktuellen Prozess müssen wir
noch unterscheiden, worauf die anderen Prozesse warten. Für jede der zahlreichen Ereig-
nismöglichkeiten gibt es meist eine eigene Warteschlange, in der die Prozesse einsortiert
werden.
Ein blockierter Prozess kann darauf warten,
• aktiv den Prozessor zu erhalten, ist aber sonst bereit (ready),
• eine Nachricht (message) von einem anderen Prozess zu erhalten,
• ein Signal von einem Zeitgeber (timer) zu erhalten,
• Daten eines Ein/Ausgabegeräts zu erhalten (io).
Üblicherweise ist der bereit-Zustand besonders ausgezeichnet: Alle Prozesse, die Ereig-
nisse erhalten und so entblockt werden, werden zunächst in die bereit-Liste (ready-queue)
verschoben und erhalten dann in der Reihenfolge den Prozessor. Die Zustände und ihre
Übergänge sind in Abb. 2.2 skizziert.

### Seite 49

30 2 Prozesse
Die Zustände „bereit“ und „blockiert“ enthalten eine oder mehrere Warteschlangen
(Listen), in die die Prozesse mit diesem Zustand eingetragen werden. Es ist klar, dass ein
Prozess immer nur in einer Liste enthalten sein kann.
Die Programme und damit die Prozesse existieren nicht ewig, sondern werden irgend-
wann erzeugt und auch beendet. Dabei verwalten die Prozesse aus Sicherheitsgründen
sich nicht selbst, sondern das Einordnen in die Warteschlangen wird von einer besonderen
Instanz des Betriebssystems, dem Scheduler, nach einer Strategie geplant. Bei einigen
Betriebssystemen gibt es darüber hinaus eine eigene Instanz, den Dispatcher, der das
eigentliche Überführen von einem Zustand in den nächsten bewirkt. Das Einordnen in eine
Warteschlange, die Zustellung der Signale und das Abspeichern der Prozessdaten werden
also von einer zentralen Instanz erledigt, die der Benutzer nicht direkt steuern kann und
die den Kern des Betriebssystems bildet. Stattdessen werden über die Betriebssystem-
aufrufe die Wünsche der Prozesse angemeldet, denen im Rahmen der Betriebsmittelver -
waltung vom Scheduler mit Rücksicht auf andere Benutzer entsprochen wird. Scheduler
und Dispatcher sind in manchen Betriebssystemen systemeigene, spezielle Prozesse, die
bei allen Ereignissen zuerst aufgerufen werden. In anderen, wie Unix, sind sie nur Kern-
funktionen, die keine eigene Prozessstruktur haben.
Im Unterschied zu dem Maschinencode werden die Zustandsdaten der Hardware (CPU,
FPU, MMU), mit denen der Prozess arbeitet, als Prozesskontext bezeichnet, s. Abb. 2.1.
Der Teil der Daten, der bei einem blockierten Prozess den letzten Zustand der CPU enthält
und damit wie ein Abbild der CPU ist, kann als virtueller Prozessor angesehen werden
und muss bei einer Umschaltung zu einem anderen Prozess bzw. Kontext (context switch)
neu geladen werden.
Die verschiedenen Betriebssysteme differieren in der Zahl der Ereignisse, auf die gewar-
tet werden kann, und der Anzahl und Typen von Warteschlangen, in denen gewartet werden
kann. Sie unterscheiden sich auch darin, welche Strategien sie für das Erzeugen und Termi-
nieren von Prozessen sowie die Zuteilung und Einordnung in Wartelisten vorsehen.
2.1.1 Beispiel UNIX
Im UNIX-Betriebssystem gibt es sechs verschiedene Zustände: die drei oben erwähn-
ten running (SRUN), blocked (SSLEEP) und ready (SW AIT) sowie stopped (SSTOP),
was einem Warten auf ein Signal des Elternprozesses bei der Fehlersuche (tracing und
EORFNLHUW
HU]HXJW WHUPLQLHUW
EHUHLW DNWLY QLFKWH[QLFKWH[
HUKDOWH
6LJQDO
=XWHLOXQJ
HUZDUWH
6LJQDO
Abb. 2.2 Prozesszustände und Übergänge

### Seite 50

2.1 Prozesszustände 31
debugging) entspricht. Außerdem existieren noch die zusätzlichen Zwischenzustände idle
(SIDL) und zombie (SZOMB), die beim Erzeugen und Terminieren eines Prozesses ent-
stehen. Die Zustandsübergänge haben dabei die in Abb. 2.3 gezeigte Gestalt.
Der Übergang von einem Zustand in einen nächsten wird durch Anfragen (System-
aufrufe) erreicht. Ruft beispielsweise ein Prozess die Funktion fork() auf, so wird vom
laufenden Prozess (von sich selbst) eine Kopie gezogen und in die bereit-Liste einge-
hängt. Damit gibt es nun zwei fast identische Prozesse, die beide aus dem fork()-Aufruf
zurückkehren. Der Unterschied zwischen beiden liegt im Rückgabewert der Funktion:
Der Elternprozess erhält die Prozesskennzahl PID des Kindes; das Kind erhält PID = 0
und erkennt daran, dass es der Kindsprozess ist und den weiteren Programmablauf durch
Abfragen anders gestalten kann. Es kann z. B. mit exec('program') bewirken, dass das
laufende Programm mit Programmcode aus der Datei „ program“ überladen wird. Alle
Zeiger und Variablen werden initialisiert (z. B. der Programmzähler auf die Anfangsad-
resse des Programms gesetzt) und der fertige Prozess in die bereit-Liste eingehängt. Damit
ist im Endeffekt vom Elternprozess ein völlig neues Programm gestartet worden.
Der Elternprozess hat dann die Möglichkeit, auf einen exit()-Systemaufruf und damit
auf das Ende des Kinds mit einem waitpid(PID) zu warten. In Abb. 2.4 ist der Ablauf
einer solchen Prozesserzeugung gezeigt.
Man beachte, dass der Kindsprozess den exit()-Aufruf im obigen Beispiel nur
dann erreicht, wenn ein Fehler bei exec() auftritt; z. B. wenn die Datei „ program“
nicht existiert, nicht lesbar ist usw. Ansonsten ist der nächste Programmbefehl nach
EORFNLHUW
HU]HXJW
QLFKWH[ LGOH EHUHLW DNWLY] RPELH QLFKWH[
VWRS
HUKDOWH6LJQDO
=XWHLOXQJ
ZDUWHDXI(UHLJQLV
ZDUWHDXI(OWHUQZHLWHUPDFKHQ
WHUPLQLHUW
Abb. 2.3 Prozesszustände und Übergänge bei UNIX
.LQG
LI3,'  
^H [HF

`
3,'  
(OWHUQ
3,' IRUN
3,'z
LI3,'  
^ 

`
3,' ZDLW6WDWXV 
H[LW6WDWXV`
Abb. 2.4 Erzeugung und Ver-
nichten eines Prozesses in
UNIX

*... weitere 446 Seiten nicht angezeigt*
