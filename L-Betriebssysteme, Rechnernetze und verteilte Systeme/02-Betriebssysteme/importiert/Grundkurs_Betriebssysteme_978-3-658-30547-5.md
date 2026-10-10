---
author: Andreas Hümmer
title: "Grundkurs_Betriebssysteme_978-3-658-30547-5"
tags:
  - content
  - importiert
  - bs
created: '2026-10-07'
modified: '2026-10-07'
bereich: BS
typ: sonstig
quelle: "Grundkurs_Betriebssysteme_978-3-658-30547-5.pdf"
seiten: 365
---

# Grundkurs_Betriebssysteme_978-3-658-30547-5

> [!info] Dokumentinformationen
> - **Quelle:** Grundkurs_Betriebssysteme_978-3-658-30547-5.pdf
> - **Typ:** sonstig
> - **Bereich:** BS
> - **Seiten:** 365

---

## Inhalt

### Seite 1

Peter/uni00A0Mandl
Grundkurs
Betriebssysteme
Architekturen, Betriebsmittelverwaltung,
Synchronisation, Prozesskommunikation,
Virtualisierung
5. Auflage

### Seite 2

Grundkurs Betriebssysteme

### Seite 3

Peter Mandl
Grundkurs Betriebssysteme
Architekturen, Betriebsmittelverwaltung,
Synchronisation, Prozesskommunikation,
Virtualisierung
5., aktualisierte Auflage

### Seite 4

Prof. Dr. Peter Mandl
Fakultät für Informatik und Mathematik
Hochschule München
München, Deutschland
ISBN 978-3-658-30546-8    ISBN 978-3-658-30547-5 (eBook)
https://doi.org/10.1007/978-3-658-30547-5
Die Deutsche Nationalbibliothek verzeichnet diese Publikation in der Deutschen Nationalbibliografie; detaillierte
bibliografische Daten sind im Internet über http://dnb.d-nb.de abrufbar.
Springer Vieweg
© Springer Fachmedien Wiesbaden GmbH, ein Teil von Springer Nature 2008, 2010, 2013, 2014, 2020
Das Werk einschließlich aller seiner Teile ist urheberrechtlich geschützt. Jede Verwertung, die nicht ausdrücklich
vom Urheberrechtsgesetz zugelassen ist, bedarf der vorherigen Zustimmung des Verlags. Das gilt insbesondere
für Vervielfältigungen, Bearbeitungen, Übersetzungen, Mikroverfilmungen und die Einspeicherung und Verar -
beitung in elektronischen Systemen.
Die Wiedergabe von allgemein beschreibenden Bezeichnungen, Marken, Unternehmensnamen etc. in diesem
Werk bedeutet nicht, dass diese frei durch jedermann benutzt werden dürfen. Die Berechtigung zur Benutzung
unterliegt, auch ohne gesonderten Hinweis hierzu, den Regeln des Markenrechts. Die Rechte des jeweiligen
Zeicheninhabers sind zu beachten.
Der Verlag, die Autoren und die Herausgeber gehen davon aus, dass die Angaben und Informationen in diesem
Werk zum Zeitpunkt der Veröffentlichung vollständig und korrekt sind. Weder der Verlag, noch die Autoren oder
die Herausgeber übernehmen, ausdrücklich oder implizit, Gewähr für den Inhalt des Werkes, etwaige Fehler oder
Äußerungen. Der Verlag bleibt im Hinblick auf geografische Zuordnungen und Gebietsbezeichnungen in veröf-
fentlichten Karten und Institutionsadressen neutral.
Planer: Sybille Thelen
Springer Vieweg ist ein Imprint der eingetragenen Gesellschaft Springer Fachmedien Wiesbaden GmbH und ist
ein Teil von Springer Nature.
Die Anschrift der Gesellschaft ist: Abraham-Lincoln-Str. 46, 65189 Wiesbaden, Germany

### Seite 5

V
Vorwort
Betriebssysteme stellen Dienste für Anwendungssysteme bereit und werden auch nur für
diese entwickelt. Ohne Anwendung bräuchte man nämlich auch kein Betriebssystem.
Heutige Betriebssysteme wie Unix, Linux, Windows, macOS oder Großrechnerbetriebs-
systeme sind sehr komplexe Programmsysteme, in denen viele Jahre Entwicklungsleis-
tung stecken und die auch ständig weiterentwickelt werden müssen. Sie nutzen viele
Techniken und Strategien zur Gewährleistung einer hohen Leistungsfähigkeit und zur Be-
reitstellung von optimalen Services für die Anwendungen.
Das vorliegende Lehrbuch befasst sich mit den Grundlagen von Betriebssystemen. In
kompakter Form werden wichtige Grundkonzepte, Verfahren und Algorithmen dargestellt,
die in modernen Betriebssystemen eingesetzt werden. Das Buch behandelt die folgenden
Themenkomplexe:
1. Einführung
2. Betriebssystemarchitekturen und Betriebsarten
3. Interruptverarbeitung
4. Prozesse und Threads
5. CPU-Scheduling
6. Synchronisation und Kommunikation
7. Hauptspeicherverwaltung
8. Geräte- und Dateiverwaltung
9. Betriebssystemvirtualisierung
Der Schwerpunkt liegt bei sog. Mehrzweckbetriebssystemen oder Universalbetriebs-
systemen, die überwiegend für betriebliche Informationssysteme eingesetzt werden, weni-
ger bei Realzeit- bzw. Embedded Systemen, die mehr in technischen Fragestellungen re-
levant sind. Einige grundlegende Konzepte gelten aber für alle Typen von Betriebssystemen.
Kap. 1 enthält eine Einführung in grundlegende Konzepte und Aufgaben von Betriebs-
systemen sowie eine historische Betrachtung. Kap.  2 stellt wichtige Architekturvarianten
und Betriebsarten von Betriebssystemen vor. In Kap. 3 werden die Konzepte zur Interrupt-
bearbeitung und zur Behandlung von Systemaufrufen diskutiert.

### Seite 6

VI
Im Kap. 4 wird erläutert, wie heutige Betriebssysteme die Ressourcen „Prozess“ und
„Thread“ verwalten. Was Threads sind und wie sie in höheren Programmiersprachen wie
Java und C# verwendet werden können, wird ebenfalls dargestellt. Kap. 5 beschreibt ver-
schiedene Strategien zur Verwaltung von Prozessen und Threads (CPU-Scheduling = Ab-
laufplanung) und erläutert, wie ein Betriebssystem einen Prozess-/Threadwechsel durch-
führt (Dispatching = Arbeitsvorbereitung, Disposition). Verschiedene Scheduling-Strategien
werden vorgestellt und mit Fallbeispielen unterlegt.
Das Thema Synchronisation und Kommunikation wird in Kap. 6 behandelt, wobei die
grundlegenden Prinzipien paralleler bzw. nebenläufiger Bearbeitung von Objekten durch
Prozesse und Threads erläutert werden. Als Mechanismen zur Synchronisation nebenläu-
figer Prozesse und Threads werden Locks, Semaphore, Mutexe und Monitore behandelt.
Es wird gezeigt, wie man diese Mechanismen in höheren Sprachen wie Java und C# ein-
setzen kann. Kommunikationsmöglichkeiten zwischen Prozessen oder Threads werden
ebenfalls vorgestellt, wobei z. B. auf das Pipe-Konzept eingegangen wird.
In Kap.  7 werden schließlich die Konzepte der Hauptspeicherverwaltung ausführlich
erläutert, wobei die virtuelle Speichertechnik im Mittelpunkt steht. Seitenersetzungsstra-
tegien werden vorgestellt und Ansätze für die Verwaltung großer Adressräume skizziert.
Ein grundlegender Einblick in einige Konzepte der Geräte- und Dateiverwaltung in-
nerhalb von Betriebssystemen folgt in Kap. 8. Es wird erläutert, wie die Geräteverwaltung
ins Betriebssystem eingebettet ist und wie Dateisysteme prinzipiell funktionieren.
Schließlich befasst sich das Kap. 9 mit den grundlegenden Konzepten und Lösungsan-
sätzen für die Virtualisierung von Betriebssystemen.
Im Anhang sind einige sinnvolle Ergänzungen zu finden. Hier werden häufig verwen-
dete Bezeichnungen für große Zahlen, zu den metrischen Grundeinheiten, die Dezimal-
und die Binärpräfix-Notation und einige gebräuchliche Datenstrukturen, die auch in Be-
triebssystemen häufig verwendet werden, überblicksartig erläutert.
In diesem Buch wird ein praxisnaher Ansatz gewählt. Der Stoff wird mit vielen Bei-
spielen aus aktuell relevanten Betriebssystemen und Programmiersprachen angereichert.
Als Beispiel-Betriebssysteme werden vorwiegend Windows, Unix und Linux herangezo-
gen. Zu jedem Kapitel sind Übungsaufgaben beigefügt. Für das Verständnis einiger Pro-
grammbeispiele sind grundlegende Kenntnisse von Programmiersprachen (C, C++, Java
und C#) nützlich, jedoch können die wesentlichen Konzepte auch ohne tiefere Program-
mierkenntnisse verstanden werden. V om Leser werden ansonsten keine weiteren Grund-
kenntnisse vorausgesetzt.
In der zweiten Auflage wurden textliche Überarbeitungen sowie einige Aktualisierun-
gen vorgenommen und es wurden zahlreiche Fehler behoben. Der Aufbau des Buches
blieb bis auf die Aufteilung von Kap. 1 in drei Einzelkapitel unverändert. Die Einführung
in wichtige Datenstrukturen wurde in den Anhang verlegt.
In der dritten Auflage wurde die Kapitelaufteilung ebenfalls beibehalten und es wurde
das Kap. 9 zum Thema Betriebssystemvirtualisierung ergänzt. Dieses Thema war uns auf-
grund der immensen Entwicklung in den letzten Jahren ein eigenes Kapitel wert. Inner -
halb der einzelnen Kapitel wurden teilweise umfangreiche Aktualisierungen  vorgenommen.
Vorwort

### Seite 7

VII
Der didaktische Aufbau wurde verbessert und es wurden neue Fallbeispiele wie etwa das
Betriebssystem macOS in die einzelnen Kapitel eingearbeitet.
Die vierte Auflage dient der Aktualisierung und Fehlerbehebung, wobei die grundle-
gende Struktur beibehalten wurde.
Die fünfte Auflage dient vor allem der Aktualisierung der einzelnen Kapitel, der Feh-
lerbehebung und der Komprimierung, wobei die grundlegende Struktur beibehalten
wurde. Das Kap. 6 wurde etwas gekürzt, die C#-Beispiele zur Synchronisation sowie auch
einige Aspekte der Kommunikation wurden entfernt. Der Anhang wurde ebenfalls etwas
reduziert.
Bedanken möchte ich mich sehr herzlich bei meinen Kolleginnen und Kollegen sowie
bei all meinen Tutoren für die Diskussionen im Rahmen der V orlesungen und Übungen.
Ganz herzlich möchte ich mich an dieser Stelle für die Anregungen von Studierenden be-
danken, die das Buch für die Nachbearbeitung von V orlesungen und zur Prüfungsvorberei-
tung nutzten. Ein herzliches Dankeschön geht auch an meine Kolleginnen und Kollegen
aus anderen Hochschulen, die das Buch ebenfalls für ihre Veranstaltungen verwenden und
mir wichtige Hinweise und Anregungen übermittelten. Für die zahlreichen textlichen Hin-
weise und die inhaltlichen Verbesserungsvorschläge zur zweiten Auflage möchte ich mei-
nem Kollegen Herrn Prof. Dr. Christian Vogt recht herzlich danken. Dem Verlag, insbe-
sondere Frau Sybille Thelen, danke ich für die Unterstützung bei den ersten beiden
Auflagen sowie der vierten Auflage und für die allzeit problemlose Zusammenarbeit. Bei
Frau Maren Mithöfer möchte ich mich ebenfalls ganz herzlich für die konstruktive Zusam-
menarbeit und für die wertvolle Unterstützung bei der dritten Auflage bedanken.
Fragen und Korrekturvorschläge richten Sie bitte an mandl@cs.hm.edu. Ich freue mich
auf weitere V orschläge, die sich aus der Nutzung des Buches ergeben. Begleitende Infor-
mationen zur V orlesung finden Sie http://www.prof-mandl.de oder unter https://github.
com/GrundkursBetriebssysteme.
München Peter Mandl
April 2020
Vorwort

### Seite 8

IX
1   Einführung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   1
1.1    Computersysteme . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   1
1.1.1    Einführung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   2
1.1.2    Aufgabe von Betriebssystemen . . . . . . . . . . . . . . . . . . . . . . . . . . . .   3
1.1.3    Grundlegende Hardwaremodelle . . . . . . . . . . . . . . . . . . . . . . . . . . .   4
1.1.4    CPU-Registersatz . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   8
1.1.5    Multicore-Prozessoren und Hyperthreading-CPUs . . . . . . . . . . . . .   9
1.1.6    Prozessorarchitektur und Mikroarchitektur . . . . . . . . . . . . . . . . . . .  10
1.1.7    Beispiele für Mikroprozessor-Architekturen . . . . . . . . . . . . . . . . . .  12
1.2    Entwicklung von Betriebssystemen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  16
1.2.1    Betriebssystemkategorien  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  16
1.2.2    Universalbetriebssysteme . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  17
1.2.3    Historische Entwicklung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  17
1.2.4    Geschichte von Microsoft Windows . . . . . . . . . . . . . . . . . . . . . . . .  18
1.2.5    Geschichte von Unix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  20
1.2.6    Geschichte von Linux  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  22
1.2.7    Geschichte von macOS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  23
1.3    Übungsaufgaben. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  24
Literatur . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  24
2   Betriebssystemarchitekturen und Betriebsarten .......................  25
2.1    Zugriffsschutz in Betriebssystemen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  26
2.2    Betriebssystemarchitekturen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  27
2.2.1    Klassische Architekturen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  27
2.2.2    Mikrokern-Architektur . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  29
2.2.3    Architekturbeispiele . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  31
2.3    Klassische Großrechnerbetriebsarten . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  35
2.3.1    Multiprocessing und Multitasking . . . . . . . . . . . . . . . . . . . . . . . . . .  35
2.3.2    Batchverarbeitung und interaktive Verarbeitung . . . . . . . . . . . . . . .  36
2.3.3    Teilnehmerbetrieb . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  36
2.3.4    Teilhaberbetrieb . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  37
Inhaltsverzeichnis

### Seite 9

X
2.4    Terminalserver-Betrieb . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  38
2.5    Verteilte Verarbeitung. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  40
2.5.1    Echt verteilte Betriebssysteme . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  40
2.5.2    Client-/Server-Systeme . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  41
2.5.3    Peer-to-Peer-Systeme (P2P) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  41
2.5.4    Kommunikations-Middleware . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  42
2.5.5    Application-Server-Betrieb . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  43
2.6    Virtualisierung von Betriebs- und Laufzeitsystemen . . . . . . . . . . . . . . . . . .  45
2.7    Cloud Computing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  46
2.8    Übungsaufgaben. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  48
Literatur . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  48
3   Interruptverarbeitung  ............................................  49
3.1    Interrupts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  50
3.1.1    Überblick . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  50
3.1.2    Interrupt-Bearbeitung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  51
3.1.3    Interrupt-Verarbeitung in Arbeitsplatzrechnern . . . . . . . . . . . . . . . .  57
3.1.4    Interrupt-Bearbeitung unter Windows . . . . . . . . . . . . . . . . . . . . . . .  60
3.1.5    Interruptverarbeitung unter Linux . . . . . . . . . . . . . . . . . . . . . . . . . .  64
3.2    Systemaufrufe  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  66
3.2.1    Systemaufrufe aus Sicht eines Anwendungsprogrammierers . . . . .  66
3.2.2    Software-Interrupts unter Linux  . . . . . . . . . . . . . . . . . . . . . . . . . . .  68
3.2.3    Software-Interrupts unter Windows . . . . . . . . . . . . . . . . . . . . . . . . .  70
3.3    Übungsaufgaben. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  71
Literatur . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  72
4   Prozesse und Threads .............................................  73
4.1    Prozesse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  74
4.1.1    Prozessmodell  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  74
4.1.2    Prozessverwaltung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  75
4.1.3    Prozesslebenszyklus . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  77
4.2    Threads . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  78
4.2.1    Threadmodell . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  78
4.2.2    Implementierung von Threads . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  79
4.2.3    V or-/Nachteile und Einsatzgebiete von Threads . . . . . . . . . . . . . . .  81
4.3    Programmierkonzepte für Threads in Java. . . . . . . . . . . . . . . . . . . . . . . . . .  83
4.4    Prozesse und Threads in konkreten Betriebssystemen  . . . . . . . . . . . . . . . .  88
4.4.1    Prozesse und Threads unter Windows . . . . . . . . . . . . . . . . . . . . . . .  88
4.4.2    Prozesse und Threads unter unixoiden Betriebssystemen . . . . . . . .  92
4.5    Übungsaufgaben. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  97
Literatur . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  98
Inhaltsverzeichnis

### Seite 10

XI
5   CPU-Scheduling  .................................................  99
5.1    Scheduling-Kriterien . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
5.2    Scheduling-Verfahren . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
5.2.1    Verdrängende und nicht verdrängende Verfahren . . . . . . . . . . . . . . 102
5.2.2    Überblick über Scheduling-Verfahren . . . . . . . . . . . . . . . . . . . . . . . 103
5.2.3    Multi-Level-Scheduling mit Prioritäten . . . . . . . . . . . . . . . . . . . . . . 106
5.2.4    Round-Robin-Scheduling mit Prioritäten  . . . . . . . . . . . . . . . . . . . . 106
5.3    Vergleich ausgewählter Scheduling-Verfahren . . . . . . . . . . . . . . . . . . . . . . 108
5.3.1    CPU-Scheduling im ursprünglichen Unix . . . . . . . . . . . . . . . . . . . . 112
5.3.2    CPU-Scheduling unter Linux . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
5.3.3    CPU-Scheduling unter Windows . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
5.3.4    CPU-Scheduling unter macOS  . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129
5.3.5    Scheduling von Threads in Java . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
5.3.6    Zusammenfassung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133
5.4    Übungsaufgaben. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133
Literatur . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
6   Synchronisation und Kommunikation  ............................... 139
6.1    Grundlegendes zur Synchronisation  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140
6.1.1    Nebenläufigkeit, atomare Aktionen und Race Conditions . . . . . . . . 140
6.1.2    Kritische Abschnitte und wechselseitiger Ausschluss . . . . . . . . . . . 143
6.1.3    Eigenschaften nebenläufiger Programme  . . . . . . . . . . . . . . . . . . . . 146
6.2    Synchronisationskonzepte . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147
6.2.1    Sperren . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147
6.2.2    Semaphore . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150
6.2.3    Monitore . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155
6.3    Synchronisationstechniken moderner Betriebssysteme . . . . . . . . . . . . . . . . 160
6.4    Synchronisationsmechanismen in Java . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161
6.4.1    Die Java-Synchronisationsprimitive „synchronized“. . . . . . . . . . . . 162
6.4.2    Warten auf Bedingungen in Java . . . . . . . . . . . . . . . . . . . . . . . . . . . 168
6.4.3    Weitere Synchronisationsmechanismen in Java . . . . . . . . . . . . . . . . 171
6.5    Kommunikation von Prozessen und Threads . . . . . . . . . . . . . . . . . . . . . . . . 174
6.5.1    Überblick über Kommunikationsmöglichkeiten . . . . . . . . . . . . . . . 174
6.5.2    Verbindungsorientierte versus verbindungslose Kommunikation . . . 175
6.5.3    Speicherbasierte versus nachrichtenbasierte Kommunikation . . . . . 175
6.5.4    Fallbeispiel: Rechnerinterne Kommunikation über Pipes . . . . . . . . 178
6.6    Übungsaufgaben. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 182
Literatur . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 183
7   Hauptspeicherverwaltung  ......................................... 185
7.1    Grundlegende Betrachtungen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186
7.1.1    Speicherhierarchien . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186
7.1.2    Lokalität . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187
Inhaltsverzeichnis

### Seite 11

XII
7.1.3    Adressen und Adressräume . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188
7.1.4    Techniken der Speicherverwaltung . . . . . . . . . . . . . . . . . . . . . . . . . 190
7.2    Virtueller Speicher . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 192
7.2.1    Grundbegriffe und Funktionsweise . . . . . . . . . . . . . . . . . . . . . . . . . 192
7.2.2    Optimierung der Speicherverwaltung . . . . . . . . . . . . . . . . . . . . . . . 202
7.2.3    Seitenersetzung und Verdrängung (Replacement) . . . . . . . . . . . . . . 207
7.2.4    Vergleich von Seitenersetzungsverfahren . . . . . . . . . . . . . . . . . . . . 218
7.2.5    Speicherbelegungs- und Vergabestrategien (Placement) . . . . . . . . . 220
7.2.6    Entladestrategie (Cleaning) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 223
7.2.7    Shared Memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 225
7.3    Speicherverwaltung in ausgewählten Systemen  . . . . . . . . . . . . . . . . . . . . . 226
7.3.1    Linux-Speicherverwaltung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 227
7.3.2    Windows-Speicherverwaltung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 230
7.3.3    macOS-Speicherverwaltung. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 234
7.4    Übungsaufgaben. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 236
Literatur . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 238
8   Geräte- und Dateiverwaltung  ...................................... 239
8.1    Aufgaben und Überblick . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 240
8.1.1    Grundlegendes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 240
8.1.2    Gerätearten . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 244
8.1.3    Kommunikation mit Controllern . . . . . . . . . . . . . . . . . . . . . . . . . . . 247
8.1.4    Geräteanbindung aus Sicht des Betriebssystems . . . . . . . . . . . . . . . 248
8.2    Dateiverwaltung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 250
8.2.1    Allgemeines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 250
8.2.2    Dateisysteme in unixoiden Betriebssystemen . . . . . . . . . . . . . . . . . 252
8.2.3    Dateisysteme unter Windows . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 255
8.3    Storage-Systeme  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 260
8.3.1    RAID-Plattensysteme  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 260
8.3.2    NAS und SAN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 264
8.4    Übungsaufgaben. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 267
Literatur . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 268
9  Betriebssystemvirtualisierung ...................................... 269
9.1   Grundbegriffe und Einsatzgebiete . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 270
9.1.1   Virtualisierungsterminologie  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 270
9.1.2   Einsatz der Virtualisierungstechnik  . . . . . . . . . . . . . . . . . . . . . . . . . 271
9.1.3   V or- und Nachteile der Virtualisierung . . . . . . . . . . . . . . . . . . . . . . 272
9.2   Virtualisierbarkeit der Hardware  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 273
9.2.1   Hardware-V oraussetzungen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 273
9.2.2   Virtualisierung bei x86-Prozessoren  . . . . . . . . . . . . . . . . . . . . . . . . 275
9.2.3   Virtualisierungstechniken in Prozessoren  . . . . . . . . . . . . . . . . . . . . 276
9.3   Varianten der Betriebssystemvirtualisierung . . . . . . . . . . . . . . . . . . . . . . . . 278
Inhaltsverzeichnis

### Seite 12

XIII
9.3.1   Typ-1-Hypervisor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 278
9.3.2   Typ-2-Hypervisor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 278
9.3.3   Paravirtualisierung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 279
9.3.4   Weitere Virtualisierungsansätze . . . . . . . . . . . . . . . . . . . . . . . . . . . . 280
9.4   Betriebsmittelverwaltung bei Betriebssystemvirtualisierung  . . . . . . . . . . . 281
9.4.1   Interruptverarbeitung und Gerätesteuerung . . . . . . . . . . . . . . . . . . . 281
9.4.2   CPU-Scheduling  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 282
9.4.3   Speicherverwaltung  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 285
9.5   Containerisierung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 287
9.6   Zusammenfassung  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 288
9.7   Übungsaufgaben . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 289
Literatur . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 289
10   Schlussbemerkung  ............................................... 291
11   Lösungen zu den Übungsaufgaben .................................. 293
11.1    Einführung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 293
11.2    Betriebssystemarchitekturen und Betriebsarten . . . . . . . . . . . . . . . . . . . . . 295
11.3    Interruptverarbeitung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 297
11.4    Prozesse und Threads . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 300
11.5    CPU-Scheduling  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 304
11.6    Synchronisation und Kommunikation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 311
11.7    Hauptspeicherverwaltung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 317
11.8    Geräte- und Dateiverwaltung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 323
11.9    Betriebssystemvirtualisierung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 326
Anhang ............................................................ 329
Literatur ........................................................... 347
Stichwortverzeichnis ................................................. 349
Inhaltsverzeichnis

### Seite 13

1
© Springer Fachmedien Wiesbaden GmbH, ein Teil von Springer Nature 2020
P. Mandl, Grundkurs Betriebssysteme,
https://doi.org/10.1007/978-3-658-30547-5_1
1Einführung
Dieses Kapitel geht auf die grundlegenden Aufgaben von Betriebssystemen ein. Das Ka-
pitel beginnt mit einer Einführung in den Aufbau eines Computersystems, das aus Soft-
ware und Hardware besteht. Ausgehend von der V on-Neumann-Maschine als Basis unse-
rer heutigen Rechnersysteme wird ein einfaches Hardwaremodell für unsere weitere
Betrachtung eingeführt. Weiterhin wird ein kurzer Abriss der Geschichte der Betriebssys-
tementwicklung vor allem am Beispiel von Windows und Unix gegeben. Betriebssysteme
stellen gewissermaßen Betriebsmittelverwalter dar, welche die Anwendungen mit den ver-
fügbaren Betriebsmitteln wie Speicher und Prozessorzeit sowie Geräte und Dateien ver -
sorgen. Darauf wird in diesem Kapitel ebenfalls eingegangen.
Zielsetzung des Kapitels
Der Studierende soll die grundlegenden Aufgaben von Betriebssystemen verstehen und
erläutern können. Weiterhin soll die historische Entwicklung von Betriebssystemen nach-
vollzogen werden können.
Wichtige Begriffe
V on-Neumann-Maschine, Prozessor, Mehrkernprozessor, CPU-Register, Betriebsmittel,
Programmzähler, PSW, Universalbetriebssystem, Mehrzweckbetriebssystem.
1.1  Computersysteme
In diesem Abschnitt soll zunächst ein Überblick über die Aufgaben von Computersyste-
men gegeben werden, so weit sie für das Verständnis von Betriebssystemen von Belang
sind. Wichtig sind vor allem die grundlegenden Zusammenhänge der Rechnerhardware.
Wir werden später noch auf einige Aspekte der Hardware im Zusammenhang mit der

### Seite 14

2
Speicherverwaltung und der Interrupt-Verarbeitung eingehen, jedoch auch dort auf einem
relativ abstrakten Level.1
1.1.1  Einführung
Computersysteme (Synonym: Rechnersysteme) bestehen – etwas vereinfacht dargestellt –
aus Hardware, System- und Anwendungssoftware. Unter Systemsoftware versteht man
zum einen das Betriebssystem (Operating System) und zum anderen systemnahe Software
wie Compiler, Interpreter, Editoren usw. Anwendungssoftware wie Bankanwendungen,
Buchhaltungssysteme, Browser usw. nutzen die Systemsoftware für einen ordnungsgemä-
ßen Ablauf. In Abb. 1.1 wird die grobe Zusammensetzung eines Computersystems skiz-
ziert.
Aus der Abbildung wird auch deutlich, dass man zur Hardware neben den physikali-
schen Ein- und Ausgabe-Geräten auch die sog. Mikroarchitektur (auch Mikroprozessor -
architektur) einschließlich der Mikroprogramme zählt, wobei es hier keine Rolle spielt, ob
letztere software- oder hardwaretechnisch realisiert sind. Weiterhin wird die Maschinen-
sprache der Hardware zugeordnet. Jedes Computersystem hat seine eigene Maschinen-
sprache, die aus Maschinenbefehlen besteht. Die Menge der Maschinenbefehle eines
Rechnersystems wird als Befehlssatz  bezeichnet. Jeder Befehl ist durch ein Mikropro-
gramm realisiert. Mikroprogramme werden oft auch als Firmware  bezeichnet. Man unter-
scheidet Testbefehle, Sprungbefehle (BRANCH), Transportbefehle (MOV), arithmetische
(ADD) und logische Befehle (CMP, SHIFT) usw. Die Bezeichnungen für die Befehle
werden vom Hardware-Architekten des Rechnersystems festgelegt und daher hier nur bei-
spielhaft aufgeführt.
1 Wer sich für Hardware und Rechnerarchitekturen interessiert, dem seien (Herrmann 2002) und
(Brinkschulte und Ungerer 2010) wärmstens empfohlen.
Ein-/Ausgabe-Geräte
CPUs
(Prozessorarchitektur und
Mikroarchitektur)
Betriebssystem
Firmware
und Hardware
Systemnahe Software (Datenbanken,
Compiler, Interpreter,…)
Anwendungssoftware (Browser, Bankanwendung,
Buchhaltungsanwendung,… )
Systemsoftware
Abb. 1.1 Hard- und Software eines Computersystems
1 Einführung

### Seite 15

3
1.1.2  Aufgabe von Betriebssystemen
Das Betriebssystem soll den Anwendungsprogrammierer bzw. den Anwender von De-
tails der Rechnerhardware entlasten. Modern strukturierte Betriebssysteme kapseln den
Zugriff auf die Betriebsmittel, der Zugriff funktioniert also nur über Betriebssystem-
funktionen. Das Betriebssystem stellt somit eine virtuelle Maschine über der Hard-
ware bereit.
Für das weitere Verständnis wollen wir vorab den Begriff des Prozesses einführen. Er
wird in Kap. 4 ausführlich diskutiert. Wir vereinbaren vorerst, dass ein Prozess eine Ab-
laufumgebung eines Programms darstellt und aus Sicht des Betriebssystems eine Ver -
waltungseinheit für die Zuordnung von Ressourcen zu Programmen darstellt. Eine
wichtige Ressource ist der erforderliche Speicher, den wir zunächst logisch als den Ad-
ressraum des Prozesses bezeichnen. Programme werden also in den Adressraum eines
Prozesses geladen und kommen in diesen zum Ablauf. Ebenso kann ein Prozess in meh-
rere Ablaufeinheiten zerlegt werden, die auch parallel ablaufen können. Für die Be-
schreibung dieser Ablaufeinheiten verwenden wir den Begriff des Threads, der auch in
Kap.  4 noch eingehend diskutiert wird. Bis dahin soll uns diese einfache Definition
genügen.
Die wesentliche Aufgabe des Betriebssystems ist also die Betriebsmittelverwaltung.
Als Betriebsmittel versteht man Hardware- und Software-Ressourcen und zwar u. a.
die Prozessoren, die Prozesse (Software), Speicher, Dateien und Geräte. Dies sind re-
ale Betriebsmittel, aber auch sog. virtuelle Betriebsmittel wie virtueller Speicher, vir -
tuelle Prozessoren und virtuelle Koprozessoren werden durch das Betriebssystem
verwaltet.
Man kann Betriebsmittel auch nach verschiedenen Kriterien klassifizieren. Genannt
wurde bereits die Unterscheidung nach Hardware- und Softwarebetriebsmittel. Ein Hard-
warebetriebsmittel ist z. B. der Prozessor, ein Softwarebetriebsmittel eine Nachricht oder
ein Prozess. Weiterhin unterscheidet man entziehbare und nicht entziehbare, sowie exklu-
siv oder gemeinsam („shared“) nutzbare Betriebsmittel.
Beispiele
• Prozessoren sind entziehbare Betriebsmittel
• Drucker sind nicht entziehbare Betriebsmittel
• Prozessoren sind zu einer Zeit nur exklusiv nutzbar
• Magnetplatten sind „shared“, also gemeinsam nutzbar
Das Betriebssystem muss dafür Sorge tragen, dass exklusive Betriebsmittel konfliktfrei
genutzt werden. Die Entscheidung hierfür trifft üblicherweise ein Scheduling- Algorithmus,
der im Betriebssystem implementiert ist.
1.1 Computersysteme

### Seite 16

4
1.1.3  Grundlegende Hardwaremodelle
Das Betriebssystem verwaltet also die Rechnerhardware und sonstige softwaretechnische
Ressourcen. Die zu Grunde liegende Rechnerhardware sollte daher in den Grundzügen
klar sein, um die Aufgaben und die Funktionsweise von Betriebssystemen zu verstehen.
Ein Systemprogrammierer, der hardwarenahe Programme entwickelt, muss natürlich von
der Hardware etwas mehr verstehen als wir hier für das grundlegende Verständnis von Be-
triebssystemen benötigen.
Man unterscheidet zwei grundlegende Computermodelle:2
• V on-Neumann-Rechner
• Harvard-Rechner
Von-Neumann-Architektur Wie Abb. 1.2 zeigt besteht der V on-Neumann-Rechner, der
von John von Neumann im Jahre 1946 entwickelt wurde, aus den vier Funktionseinheiten
Steuereinheit oder Leitwerk (Control Unit, CU), Rechenwerk bzw. Arithmetisch Logische
Einheit (ALU oder Processing Unit, PU), Speicher (Memory) sowie Ein-/Ausgabe (Input/
Output, I/O). Das Leitwerk holt die Maschinenbefehle3 nacheinander in den Speicher und
2 Quantencomputer betrachten wir in diesem Buch nicht. Hierfür sei auf (Homeister 2015) verwiesen.
3 Eine Folge von zusammengehörigen Maschinenbefehlen nennen wir übrigens ein Programm.
Steuer-
einheit
Arithmetisch
Logische
Einheit /ALU)
Register
…
Ein-/Ausgabe-Geräte
Kommunikationssystem, Bus
Haupt-
speicher
Externe
Speicher
CPU
Drucker
Abb. 1.2 Architektur eines V on-Neumann-Rechners
1 Einführung

### Seite 17

5
führt sie aus. Damit stellt das Leitwerk den „Befehlsprozessor“ dar. Das Rechenwerk kann
auch als „Datenprozessor“ bezeichnet werden, der logische und arithmetische Operatio-
nen ausführt. Im Speicher liegen die Maschinenbefehle und die zu verarbeitenden Daten.
Maschinenbefehle und Daten sind also in einem gemeinsamen Speicher.
Die Ein-/Ausgabe ist die Verbindung externer Geräte (Tastatur, Maus, Festplatten, …)
mit dem Rechenwerk, stellt also die Schnittstelle nach außen dar. Alle Komponenten wer-
den über ein Transport- oder Kommunikationssystem, auch als Bussystem bezeichnet,
miteinander verbunden.
Rechenwerk und Leitwerk werden heute in der Regel in einem Prozessor, der als Zen-
traleinheit (CPU, Central Processing Unit) oder Rechnerkern bezeichnet wird, zusam-
mengefasst. Wir gehen im Weiteren auch davon aus. Die in der Abbildung gezeigten
Register sind kleine und schnelle Speicherbereiche, auf die weiter unten noch eingegan-
gen wird.
Harvard-Architektur Der Harvard-Rechner, der nach der Struktur des Mark-I-Rech-
ners (entwickelt von 1939 bis 1944 an der Harvard University) benannt ist, hat im Unter-
schied zum V on-Neumann-Rechner zwei getrennte Speicher, einen für die Daten und ei-
nen für die Maschinenbefehle. Beide Speicher werden auch über einen getrennten Bus
mit der CPU verbunden. Für die Übertragung von Maschinenbefehlen und Daten stehen
damit doppelt so viele Leitungen zur Verfügung, weshalb der Harvard-Rechner auch ef-
fizienter ist. Diese Effizienz muss aber mit einem Hardware-Mehraufwand erkauft wer -
den. Zudem muss man sich überlegen, wie man Daten und Maschinenbefehle trennen
kann. Heute wird die Harvard-Architektur daher nur sehr selten eingesetzt. Den Standard
stellt die V on-Neumann-Architektur dar, die in modernen Rechnern um einige Bausteine
erweitert wurde.
Caches Eine wichtige Erweiterung für Rechnerarchitekturen sind Caches. Hier handelt
es sich um schnelle Pufferspeicher, die in unterschiedlichen Speicherebenen zum Einsatz
kommen. Ein Cache speichert Daten bzw. Codeteile und dient der Zugriffsoptimierung.
Heute werden auch Hierarchien von Caches verwendet. Je näher ein Cache an der CPU
liegt, desto höher ist die Zugriffsgeschwindigkeit. Man spricht hier auch von Level-n-
Caches (Level-1, Level-2 oder L1, L2, usw.). Je kleiner n ist, desto schneller ist der Cache.
Heutige Rechnersysteme haben meist zwei, drei oder sogar vier Cache-Levels. Um ein
Gefühl für die Leistungsfähigkeit von Speichersystemen bzw. Caches zu bekommen, sei
hier erwähnt, dass die Zugriffszeiten auf heutige Hauptspeichersysteme etwa um den Fak-
tor 106 schneller als die Zugriffszeiten auf externe Speichermedien (Festplatten) und die
Zugriffszeiten von heutigen Cache-Speichern etwa 10 bis 100 mal schneller als die Zu-
griffszeiten gängiger Hauptspeicher sind. Es soll noch erwähnt werden, dass bei Caches
zum Teil eine Trennung von Code- und Daten gemäß der Harvard-Architektur durchaus
üblich ist.
1.1 Computersysteme

### Seite 18

6
Bussystem CPU und Hauptspeicher sind über ein schnelles Bussystem – auch CPU-Bus
oder Systembus genannt – miteinander verbunden, wobei ein Bussystem im Prinzip eine
Menge von parallelen Datenleitungen darstellt. Je nach Rechnersystem sind z. B. 32 bzw.
64 (und in Zukunft sicher mehr) Datenleitungen verfügbar, womit – vereinfacht ausge-
drückt – zwischen CPU und Hauptspeicher genau so viele Bit parallel übertragen werden
können. Der CPU-Bus bestand ursprünglich aus drei Teilen: Der Datenbus, der Adressbus
und der Steuerbus. Über den Datenbus werden Daten zwischen Hauptspeicher und CPU
übertragen, der Adressbus dient der Adressierung des Hauptspeichers, und über den Steu-
erbus werden Steuerinformationen ausgetauscht. CPUs und Arbeitsspeicher kommunizie-
ren heute über sehr optimierte Bussysteme wie etwa einem Front Side Bus (FSB) oder über
Punkt-zu-Punkt-Verbindungen. Der Chip-Hersteller AMD verwendet beispielsweise ein
bidirektionales Kommunikationssystem namens HyperTransport mit einer Bandbreite
von mehr als 50 GBit/s. Intel nutzt in seiner Intel-Core i-Serie eine serielle, bidirektionale
Punkt-zu-Punkt-Schnittstelle zwischen Prozessoren mit der Bezeichnung QuickPath In-
terconnection (QPI), die eine maximale Bandbreite von mehr als 100 GBit/s erreicht.
Externe Systeme Externe Systeme sind über einen Ein-/Ausgabe-Bus (E-/A-Bus) unter-
einander und über den CPU-Bus mit der CPU und dem Hauptspeicher verbunden. An ex-
ternen Systemen gibt es u.  a. Plattenspeicher, Bildschirm, Keyboard und Maus, sowie
Drucker und Netzwerkadapter. Viele externe Geräte verfügen wiederum über eigene Con-
troller, die mit der CPU zum Zwecke des Datenaustauschs kommunizieren.
Takt Eine Rechneranlage arbeitet taktgesteuert. Das sog. System-Clock-Signal wird von
einem Clock-Generator erzeugt. Die Ausführung eines Maschinenbefehls erfordert in der
Regel eine festgelegte Anzahl an Bearbeitungsphasen, wobei jede in einem Takt abgear -
beitet wird. Bei den meisten Prozessoren sind es mindestens drei bis vier Phasen, die ge-
meinsam als Maschinenzyklus bezeichnet werden: Diese Phasen sind das Holen vom
Speicher, das Dekodieren, das Ausführen des Befehls und das Zurückschreiben der Ergeb-
nisse in den Speicher oder in ein Register. Bei der Entwicklung neuer Prozessoren ver -
suchte und versucht man ständig, die Anzahl der Takte durch eine parallele Ausführung
der Phasen zu reduzieren.
Die Rechnerleistung wird über verschiedene Kenngrößen dargestellt. Hierzu gehören
die Größe des Hauptspeichers (gemessen in Megabyte bzw. Gigabyte), die Größe der Plat-
tenbereiche (gemessen in Gigabyte bzw. Terabyte) und die Rechengeschwindigkeit der
CPU gemessen in MIPS (Million Instructions Per Second, also Maschinenbefehlsausfüh-
rungen pro Sekunde). Oft wird auch noch die Taktfrequenz zur Bewertung herangezogen,
die aber heute für sich alleine keine allzu großen Schlüsse zulässt. Es kommt nämlich
immer darauf an, was das Rechnersystem in einem Taktzyklus ausrichten kann.
Die und Chipsatz  Heute legt man in der Halbleitertechnik soviel Funktionalität wie
möglich rund um die CPUs auf einen Chip, bzw. auf einen sog. Die. Ein Die (Nacktchip)
1 Einführung

### Seite 19

7
ist ein rechteckiger Halbleiter-Chip.4 Weiterhin wird heute der Zugang zum Hauptspeicher
sowie zu den externen Geräten oft auf dem sog. Chipsatz bereitgestellt. Die CPUs greifen
z. B. über den Front Side Bus oder über eine andere Technologie auf die North- und South-
bridge zu. Über die Southbridge werden die externen Geräte wie Festplatten angebunden,
die schnellere Northbridge dient der Anbindung des Arbeitsspeichers. Die und Chipsatz
sind auf einem Motherboard platziert.
Speicher Der in Rechnersystemen verbaute Speicher ist vielfältig (Abb. 1.3). Man unter-
scheidet flüchtige und nicht flüchtige Speicherchips. Flüchtige Speicherchips vom Typ
SDRAM oder SRAM werden für Arbeitsspeicher  oder Caches benutzt. Der Arbeitsspei-
cher, auch Hauptspeicher oder Main Memory genannt, ist der zentrale Speicher im Rech-
nersystem, in dem auch die Programme und Daten für die Ausführung liegen.  Nicht flüch-
tige Speicherchips werden für das Basic Input Output System (BIOS) 5 genutzt. Die
Speicherbausteine werden als ROM (Read Only Memory) oder EEPROM (Electrically
Erasable Read Only Memory) bezeichnet. In kleineren Rechnersystemen etwa für Smart-
phones sowie für externe Speicher von Rechnersystemen wie Solid State Drives (SSD)
und Chipkarten werden häufig Flashspeicher eingesetzt. Die technischen Details der ver -
schiedenen Speichervarianten sind für unsere Betrachtung nicht weiter relevant.
Für externe Speicher werden häufig noch mechanische Festplatten, sog. Hard Disk
Drives (HDD) verwendet, bei denen Daten auf magnetisch beschichteten Scheiben ge-
speichert werden.
4 Man spricht auch von einem ungehäusten Halbleiter-Chip.
5 Auf das BIOS und dessen Funktion werden wir noch zu sprechen kommen.
SDRAM SRAM ROM, EEPROM Flash
/square4Caches
BIOS = Basic Input Output System
DDR4, DDR5 = Double DataRate (Versionen 4 und 5)
EEROM = Electrically erasable programm able read-only memory
Flash = Spezieller EEPROM-Typ
MRAM = Magneto-resistive random-access memory
NRAM = Nano random-access memory
NRAM
/square4SD-Card
/square4Smartphones
/square4SSD
MRAM
Nicht flüchtige Speicherchips
Speicherchips
Flüchtige Speicherchips
/square4Arbeitsspei-
cher, z. B.
DDR4, DDR5
/square4BIOS /square4Spielautomaten
/square4Luft- und Raum-
fahrt
ROM = Read-only memory
SDRAM = Synchronous dynamic random-access memory
SD-Card = Secure Digital Memory Card
SRAM = Static dynamic random-access memory
SSD = Solid State Disk
/square4Alternative
für SDRAM
Beispiel-
nutzungen
Legende:
Abb. 1.3 Übersicht über Speicherchips
1.1 Computersysteme

### Seite 20

8
1.1.4  CPU-Registersatz
Jede CPU enthält einen Registersatz mit einigen kleinen aber schnellen Speichern (sog.
Register). Diese schnellen Speicher werden benötigt, um die Maschinenbefehle auszu-
führen. Alle Register, die durch Software direkt angesprochen werden können, repräsen-
tieren das Programmiermodell eines Prozessors. Darüber hinaus gibt es weitere Register,
sog. Hilfsregister, die nur prozessorintern verwendet werden. Je nach Maschinenbefehl
wird ein Register oder es werden sogar mehrere Register verwendet. Die Maschinenbe-
fehle schreiben ihre Operanden oft in Register oder lesen Operanden aus Registern. Man
nennt die Register je nach Typ Integerregister, Universalregister, Gleitkommaregister,
Datenregister, Segmentregister usw.
Weitere, spezielle Register sind der Program Counter (PC, Programmzähler, Befehls-
zähler), der die Hauptspeicheradresse des nächsten auszuführenden Befehls enthält, das
Instruction Register (IR, Befehlsregister), das den aktuellen auszuführenden Maschinen-
befehl enthält und das Stack-Pointer-Register (SP), das auf den aktuellen Programmstack6
verweist. Darüber hinaus gibt es Statusregister, auch PSW (= Program Status Word) ge-
nannt, welche für Vergleichsoperationen benutzt werden, und weitere Kontrollbits wie
etwa den aktuellen Modus7 (Benutzermodus, Kernelmodus), in dem sich die Rechneran-
lage befindet, enthalten.
Der Registersatz des mittlerweile in die Jahre gekommenen Prozessors 8086 von Intel
(I-8086) verfügt unter anderem beispielsweise über vier 16-Bit breite Arbeits- bzw. Mehr-
zweckregister mit den Bezeichnungen AX, BX, CX und DX, vier Adress- und Indexregis-
ter, wovon eines auf den Anfang des Stacks zeigt (SS) und ein Register, das als Stapelzei-
ger bzw. Stack-Pointer (SP) bezeichnet wird und auf den aktuellen Stack-Inhalt verweist.
Der Befehlszähler bzw. Befehlszeiger  heißt beim Intel 8086 auch Instruction Pointer oder
kurz IP. Das 16-Bit-Statusregister SR (entspricht dem PSW-Register) hat die oben erläu-
terte Bedeutung.
Hinzu kommen noch spezielle interne Kontroll- und Steuerregister für die CPU und für
die Steuerung externer Geräte. Diese Register werden mit CR0, CR1, CR2, CR3 usw. be-
zeichnet. Sie werden u. a. für die Interruptbearbeitung (siehe Kap.  3) sowie für die Spei-
cherverwaltung benötigt. Im Register CR0 kann z. B. über ein Flag eingestellt werden, ob
der Paging-Mechanismus für die Speicherverwaltung aktiviert werden soll (siehe Kap. 7).
Im Register CR2 steht die Speicheradresse, bei der ein Seitenfehler ausgelöst wurde, im
Register CR3 steht die Basisadresse für die Seitentabellen eines Prozesses, ebenfalls eine
wichtige Adresse für die Speicherverwaltung (zur Speicherverwaltung siehe Kap. 7).
Exkurs: Stack
Unter einem Stack im o. g. Sinne versteht man einen reservierten Teil des Adressraums
und ein dazugehöriges Prozessor-Spezialregister, das als Stack-Pointer oder Stapelzeiger
6 Was ein Stack ist, wird weiter unten erläutert.
7 Die Begriffe „Benutermodus“ und „Kernelmodus“ werden in Kap. 2 erläutert.
1 Einführung

### Seite 21

9
bezeichnet wird. Der Stack-Pointer zeigt immer auf die Adresse des oberen Endes des
Stapels (Top of Stack). Im Stapelspeicher legt das Betriebssystem die Aufrufinformation
(Aufrufrahmen) aller Unterprogramme ab, die noch nicht beendet sind, sowie einige zu-
sätzliche, zwischengespeicherte Daten. Wie wir noch sehen werden, legt das Betriebssys-
tem bei Unterbrechungen oder Funktionsaufrufen die Rücksprunginformationen auf den
Stack. Damit kann nach Abarbeitung einer Unterbrechungsroutine oder der aufgerufenen
Funktion, Prozedur oder Methode wieder der Weg zurück zur unterbrochenen Codestelle
gefunden werden. Heutige Programmiersprachen nutzen ebenfalls einen Stack für diese
Zwecke. In der Softwaretechnik wird unter einem Stapelspeicher auch allgemein eine
Datenstruktur mit der oben dargestellten Funktionalität bezeichnet (siehe auch Anhang).
1.1.5  Multicore-Prozessoren und Hyperthreading-CPUs
Multicore-Prozessoren (auch: Mehrkernprozessor) sind Mikroprozessoren mit mehreren
vollständigen CPUs. Rechnerkerne oder auch Prozessorkerne sind Funktionseinheiten, die
unabhängig von anderen Rechnerkernen Programme ausführen können. Sie stellen also
eigene Ausführungseinheiten dar und ermöglichen die Parallelisierung der Programmaus-
führung. Viele Ressourcen mit Ausnahme des Busses und ggf. einiger Caches-Levels sind
bei Mehrkernprozessoren repliziert. Als Dualcore-Prozessor (Doppelkernprozessor) be-
zeichnet man einen Multicore-Prozessor mit zwei CPUs. Mikroprozessoren mit einem
Hauptprozessor bezeichnet man zur Abgrenzung als Singlecore-Prozessoren (Einzelkern-
prozessor). Bei vier Kernen spricht man von einem Quadcore-Prozessor usw.
Multicore-Prozessoren sind kostengünstiger zu entwickeln als mehrere einzelne CPUs.
Man kann mit einem Dualcore-Prozessor je nach Anwendung die 1,3- bis 1,7-fache Leis-
tung erbringen als mit einem Singlecore-Prozessor.
Der Einsatz von Multicore-Prozessoren dient auch dazu, das Abwärmeproblem bei
Prozessoren zu lösen, da z. B. ein Dualcore-Prozessor unwesentlich mehr Abwärme er -
zeugt als ein Prozessor mit einem Rechnerkern.
Im Gegensatz dazu sind sog. Hyperthreading-CPUs mehrfädige (engl. multithreading)
Singlecore-Prozessoren mit mehreren Programmzählern und Registersätzen sowie Inter -
rupt-Controllern, die sich gegenüber dem Betriebssystem aber als Multicore- Prozessor
darstellen. Das Betriebssystem sieht also zwei oder mehrere CPUs (Rechnerkerne), ob-
wohl auf der physikalischen CPU nur einer vorhanden ist. Die Rechnerkerne sind logische
Bausteine. Es handelt sich bei Hyperthreading-CPUs also nicht um echte Multicore-Pro-
zessoren. Hyperthreading wurde von Intel eingeführt. Intel arbeitet bei  einigen Prozesso-
ren (z. B. bei der Core-i-Serie) sowohl mit Multicore-Prozessoren als auch mit Hyper -
threading. Aus Sicht des Betriebssystems hat damit z.  B. eine Dualcore- Maschine mit
Hyperthreading vier Rechnerkerne.
1.1 Computersysteme

### Seite 22

10
1.1.6  Prozessorarchitektur und Mikroarchitektur
Architekturen von Rechnersystemen beschreiben den Aufbau eines Prozessors, wobei
zwei Sichten eingenommen werden. Man unterscheidet die Prozessorarchitektur und die
Mikroarchitektur oder Mikroprozessorarchitektur.
Die Prozessorarchitektur (auch als Befehlssatzarchitektur oder Programmiermodell be-
zeichnet) definiert die Grenze zwischen Hardware und Software und stellt für den System-
programmierer und den Compiler den sichtbaren Teil des Prozessors dar. Hierzu gehören
der Befehlssatz (Maschinenbefehle), die Befehlsformate, die Adressierungsarten für Be-
fehle, das Unterbrechungssystem und das Speichermodell (Register, Adressraumaufbau).
Hardware-Details und interne Prozessorvorgänge werden nicht betrachtet und spielen für
den systemnahen Programmierer auch nicht die wesentliche Rolle. Beispiele für Prozes-
sorarchitekturen sind die Intel Architekturen 32 und 64 (IA 32 und IA 64) sowie Intel 64
und AMD x64.
Die Mikroarchitektur beschreibt die Implementierung der Prozessorarchitektur bzw.
des Befehlssatzes. Hierzu gehören die Hardware-Struktur, der Entwurf der Kontroll- und
Datenpfade im Prozessor, die Art und Anzahl der Ausführungseinheiten (Rechnerkerne),
spezielle Mechanismen wie Pipelining und die Cache-Nutzung. Beispiele für Mikroarchi-
tekturen der Firma Intel sind Haswell, Sandy- Skylake und Ice Lake. Systemprogrammie-
rer und Compiler müssen die Mikroarchitektur zumindest grob verstehen, sonst kann kein
effizienter Code erzeugt werden. Allerdings steht das Verständnis über die Prozessorarchi-
tektur im V ordergrund. Je hardwarenäher ein Systemprogrammierer entwickelt, umso
mehr muss er sich mit der Funktionsweise der Hardware (CPU, externe Geräte), also mit
der Mikroarchitektur, beschäftigen.
Für unsere weitere Betrachtung der Aufgaben und der Funktionsweise von Betriebs-
systemen verwenden wir ein vereinfachtes Modell der Mikroarchitektur, wobei wir uns
stark an heutiger PC-Hardware mit mehreren Rechnerkernen orientieren. Konkret betrach-
ten wir in diesem Buch sog. UMA-Multiprozessoren (Uniform Memory Access), bei denen
sich alle Rechnerkerne einen gemeinsamen Speicher teilen, der über ein Kommunikati-
onssystem (Bus) für alle erreichbar ist. Dabei kann jeder Rechnerkern den gesamten Spei-
cher mit gleicher Geschwindigkeit adressieren.
Als Alternative dazu seien NUMA-Multiprozessoren (Non Uniform Memory Access)
ewähnt, bei denen jede CPU einen eigenen Speicher (Arbeitsspeicher) besitzt, aber der
gesamte Speicher als ein einziger Adressraum für alle Rechnerkerne sichtbar ist. Lokale
Speicherbereiche sind bei dieser Architektur schneller im Zugriff als weiter entfernte
Speicher (Tanenbaum und Bos 2016).
Bei unserer weiteren Betrachtung befassen wir uns vor allem mit symmetrischen Multi-
prozessorsystemen (SMP), bei denen es nur eine Kopie des Betriebssystems gibt, das alle
Ressourcen, auch alle Rechnerkerne verwaltet. Das Betriebssystem regelt also, welche
Programmteile auf welchen Rechnerkernen wann zum Ablauf kommen.
1 Einführung

### Seite 23

11
Heute sind meist mehrere Rechnerkerne samt ihrem Leit- und Rechenwerk und dem
Registersatz auf einem Chip (einem Die) untergebracht. In jedem Rechnerkern bzw. auf
dem Die liegen gewöhnlich auch meist zwei bis vierstufige Caches sowie die MMU (Me-
mory Management Unit) und der TLB (Translation Lookaside Buffer).
Was den Registersatz anbelangt, sind für uns neben den Mehrzweck- und Gleitkomma-
registern einige Steuerregister von Bedeutung. Zu diesen zählen wir beispielsweise das
PSW, das Befehlsregister, aber auch spezielle Register zur Adressierung von Daten und
Code, wie etwa der Programmzähler, der Stackpointer sowie Register zur Adressierung
von Code und Daten spielen in unserer Betrachtung eine Rolle.
Abb. 1.4 zeigt ein Schema eines Main- bzw. Motherboards mit mehreren Rechnerker -
nen, in denen jeweils Caches sowie eine MMU integriert sind. Ein weiterer gemeinsamer
(shared) Cache befindet ebenfalls meist auf dem gleichen Die. Dies kann aber von Prozes-
sor zu Prozessor unterschiedlich sein und ist auch ständig in Weiterentwicklung. Für un-
sere eher logische Sicht spielt es im Weiteren keine Rolle. Im Modell sind auch ein Chip-
satz mit einer Northbridge, an welcher der Hauptspeicher und der Grafikprozessor
angebunden sind, sowie eine Southbridge zur Anbindung externer Geräte bzw. Bussys-
teme skizziert. Die Northbridge wird über einen Speicherbus, in diesem Fall ein Front
Side Bus, an die Rechnerkerne gekoppelt. Auch dies kann in konkreten Rechnersystemen,
insbesondere bei Server- und Mainframe-Systemen anders gelöst sein.
Anbindung externer Geräte über USB, S-ATA, PCI, …)
Rechnerkern 1 … n (CPU )
Cache
(L1, L2, …)
Mehrzweck-
register
Gleitkomma-
register
Status-
register
Leitwerk und Steuerwerk
Chipsatz
MMU
TLB
Motherboard
Ein Die
Gemeinsamer Cache (L3, L4,…)
…
Lokaler
Interrupt
Controller
Grafikprozessor
(on-Die)
Memory
Controller
Arbeitsspeicher
(RAM)
Digitale Ausgänge
(HDMI, DVI)
Kommunikationssystem (Punkt-zu-Punkt-Verbindungen oder Front Side Bus (FSB))
Southbridge
Interrupt
Controller
Northbridge
(bei Intel)
Abb. 1.4 Vereinfachtes Mikroarchitekturmodell
1.1 Computersysteme

### Seite 24

12
Wie wir im Kap. 7 noch sehen werden, sind die Bausteine MMU und TLB für die Ver-
waltung des Hauptspeichers von Bedeutung. Der Interrupt-Controller, für unsere verein-
fachte Sicht in der Southbridge integriert, ist für die Ein-/Ausgabe von Bedeutung (siehe
Kap. 3). Einige Ausführungen zum Zugriff auf externe Geräte über die bekannten Buss-
systeme werden im Kap. 8 erläutert. Zu weiteren Einzelheiten wird auf die Literatur ver -
wiesen (Brinkschulte und Ungerer 2010).
Ein handelsüblicher PC verfügt heute z.  B. über vier bis acht Rechnerkerne, einen
Hauptspeicher mit sechzehn Gigabyte, einen Festplattenspeicher (HDD = hard disk drive)
mit einem bis zu mehreren Terabyte bei einer Rechnergeschwindigkeit von mehreren Tau-
send MIPS. Neben den klassischen Festplattenlaufwerken, die heute noch in Rechnersys-
teme verbaut werden, verbreiten sich die schnelleren Flash-Speicher (SSD) immer mehr.
Mischungen beider Speichervarianten sind heute vorwiegend anzutreffen.
1.1.7  Beispiele für Mikroprozessor-Architekturen
Das oben dargestellte Architekturmodell ist natürlich eine starke Vereinfachung. Heutige
Mikroarchitekturen sind weit komplexer und verfügen über weitere Bausteine wie etwa
Pipelines, Gleitkomma-Arithmetik und schnelle Netzwerkanbindungen, und man spricht
dabei auch von superskalaren Architekturen, bei denen die Befehlsbearbeitung mehr und
mehr parallelisiert wird, um die Leistung zu verbessern. Betrachten wir beispielhaft einige
gängige Mikroprozessoren:
Pentium-Prozessor Der Pentium-Prozessor der Firma Intel8 wurde 1993 eingeführt und
verfügt schon über eine superskalare Architektur. Er hat einen 64-Bit breiten CPU-Bus,
der die CPU mit einem Code-Cache (Level-1- bzw. L1-Cache) und einem Daten-Cache
(Level-2- bzw. L2-Cache) verbindet. Der V orgängerprozessor Intel-80386 hatte aus Platz-
gründen noch keinen Cache. Erst mit der 80486-Architektur wurde ein L1-Cache in der
CPU und ein L2-Cache außerhalb der CPU auf dem Motherboard realisiert. Die Maschi-
nenbefehle werden vom Hauptspeicher über den L1-Cache und über einen Prefetch-Puffer
in die erforderlichen Register geladen.
Der Registersatz des Intel Pentium verfügt über 16 Register, von denen die meisten
eine Breite von 32 Bit verfügen. Davon sind vier als Mehrzweckregister (siehe Abb.  1.5)
ausgestattet, die auch aus Kompatibilitätsgründen zu V orgängerprozessoren als 16-Bit-
und als 8-Bit-Register verwendbar sind (AX = 16-Bit-Register, AH = 8-Bit-Register). Alle
allgemeinen Register können für arithmetische und logische Operationen verwendet
werden.
8 Pentium ist eigentlich eine ganze Serie von Prozessoren mit unterschiedlicher Ausstattung (Pen-
tium Pro, Pentium II, Pentium III, Pentium III Xeon, Pentium 4, …).
1 Einführung

### Seite 25

13
Itanium-Prozessor Der Itanium-Prozessor, der von Intel und HP (Hewlett-Packard) ent-
wickelt wurde und im Jahre 2001 auf den Markt kam, verfügt über eine echte 64-Bit-
Architektur und ist der erste Prozessor mit der sog. IA64-Architektur. Er ist nur noch über
einen Firmware-Emulationsmodus mit der IA32-Architektur kompatibel. Diese Prozes-
sorserie ist mit 128 Integerregistern (General Purpose Register) und 128 Gleitkommare-
gistern ausgestattet. Die Integerregister sind 64 Bit und die Gleitkommaregister 82 Bit
breit. Der L1- und der L2-Cache sind hier in der CPU untergebracht. Je nach Modell be-
findet sich ein L3-Cache auch direkt auf dem Die oder außerhalb. Die Caches sind natür -
lich schon viel größer als beim Intel Pentium (je nach Modell 3, 8, 24, 30, … MiB). Die
Entwicklung des Itanium-Prozessor wurde mittlerweile wegen Erfolglosigkeit eingestellt.
Core-i-Prozessoren Die Firma Intel entwickelt seit 2008 die Prozessorfamilie Intel
Core-i-Serie  in mehreren Klassen (Intel Core i3, i5, i7, i9). Es handelt sich hier um x64-
Mehrkernprozessoren mit aktuell bis zu 18 Kernen, welche die etwas ältere Intel- Core- 2-
Familie ablöst. Je Kern gibt es jeweils einen L1- und L2-Cache ab der Mikroarchitektur
Haswell und folgende (Skylake, Icelake) auch einen gemeinsam für alle Kerne verfügba-
ren L3-Cache. In der Haswell-Mikroarchitektur wird auch ein gemeinsamer L4-Cache
unterstützt. Die Größen der Caches sind je nach Typ und Ausstattung unterschiedlich. Eine
typische Größe des L1-Cache ist z. B. 64 KiB, für den L2-Cache 256 KiB und für den L3-
Cache zwei bis acht MiB. Der L4-Cache kann deutlich größer sein (128 MiB). Die Prozes-
soren verfügen über 16 Gleitkommaregister (64-Bit breit) und 16 Mehrzweckregister
(128-Bit breit).
Opteron-Prozessoren Die Firma AMD entwickelt die verschiedenen 64-Bit-Mehrkern-
prozessoren auf Basis der AMD64-Mikroarchitektur (AMD-K8-, AMD-K9-und Mikro-
architektur) mit der Bezeichnung AMD Opteron  (genaue Bezeichnungen sind AMD
Opteron K8, K9) speziell für Serversysteme. Der AMD Opteron K10 basiert bereits auf
der AMD-K10-Mikroarchitektur und verfügt wie die Core-i-Prozessoren von Intel je Kern
über einen L1- und einen L2-Cache, der L3-Cache ist auch nur einmal für alle Kerne vor-
handen. Ein L3-Cache kann je Kern zwei MiB (insgesamt 16 MiB) groß sein, der L1- und
der L2-Cache sind je nach Ausstattung vergleichbar mit den Intel-Prozessoren. Der L1-
Cache ist zweigeteilt in einen Daten-Cache je Kern (max. zwei MiB) und einen Cache für
EAX
EBX
ECX
EDX
31 15 0
AH
BH
CH
DH
AL
DL
CL
BL
AX
BX
CX
DX
Registerbezeichnungen:
[E]AX: Akkumulator
[E]BX: Basisregister
[E]CX: Zählregister
[E]DX: Datenregister
Abb. 1.5 Intel-Pentium-Prozessor, allgemeine Register
1.1 Computersysteme

### Seite 26

14
die Machinenbefehle (64 KiB). Auch die Registersätze sind vergleichbar. Die letzte Opte-
ron-Verison wurde 2012 auf dem Markt gebracht.
Ryzen-Prozessoren Seit 2017 gibt es von AMD die Ryzen-Prozessoren mit unterschied-
lichen Ausprägungen bis zu 16 Kernen mit 32 Threads und einem L3-Cache bis zu 64 MiB
auf der Basis der Zen-Mikroarchitektur.
Weitere Prozessoren Einige weitere Mikroprozessoren sollen noch erwähnt werden: Die
Firma Sun (nun Oracle) bietet mit ihrem RISC-Prozessoren vom Typ SPARC64  ebenfalls
eine Familie von superskalaren Mikroprozessoren mit einer 64-Bit-Architektur an. Ein im
Jahr 2009 auf dem Markt gekommener Prozessor dieser Familie hat die Bezeichnung
SPARC64 VIII. Er ist mit acht Rechnerkernen ausgestattet, verfügt über einen bis zu
64 KiB großen L1-Cache, und einen bis zu sechs MiB großen L2-Cache, hat jedoch kei-
nen L3-Cache. Die Anzahl der verfügbaren Register variiert je nach Prozessortyp. Die
ersten SPARC-Prozessoren hatten 128 Register mit einer Breite von 32  Bit. Bei den
64-Bit-Prozessoren sind es deutlich weniger. Einer der neueren Prozessoren aus dem Jahr
2017 von Oracle ist der SPARC M8 mit 32 Kernen, einem 16  KiB L1-Cache, einem
128 KiB L2-Cache und einem 64 MiB L3-Cache.
Erwähnt werden sollen noch der AMD Athlon (in PCs verwendet), der MIPS64, der
IBM Power 4, der DEC Alpha sowie Prozessoren für Großrechner wie etwa der IBM Sys-
tem z9 (die V orgängerversionen hieß zSeries und noch früher System/370). Die Prozesso-
ren der IBM-Mainframe-Technologie verfügen heute über eine Vielzahl von Prozessoren
(z. B. bis zu 64 Prozessoren im IBM-System z10 Enterprise Class), von denen einige für
spezielle Aufgaben wie die Virtualisierung verwendet werden und einige als Ersatzprozes-
soren dienen.
Genannt werden sollen noch Grafikprozessoren (GPU), die rechenintensive Aufgaben
der Computergrafik übernehmen und damit die CPUs entlasten. Sie werden meist auf dem
Die der CPU integriert oder sind „onboard“ auf der Hauptplatine als integrierte Grafik-
prozessoren zu finden. Nvdia Corporation, Intel und AMD sind die bekanntesten Herstel-
ler von Grafikprozessoren. Sie verfügen über einen eigenen Speicher und über viele (tau-
sende) von kleinen Rechnerkernen. Da diese speziellen Prozessoren sehr gut geeignet
sind, um viele kleine Berechnungen parallel durchzuführen, werden sie heute nicht nur für
die Darstellung der grafischen Oberfläche verwendet, sondern immer mehr auch für an-
dere Aufgaben wie etwa für umfangreiche Berechnungen im Machine Learning oder für
Simulationen. Diese „Fremdnutzung“ bezeichnet man als General Purpose Computation
on Graphics Processing Unit (GPGPU). Es handelt sich um spezielle Grafikprozessoren,
die aufgrund ihrer massiv parallel arbeitenden Recheneinheiten oft auch für andere Auf-
gaben, wie etwa für umfangreiche Berechnungen im Machine Learning oder für Simula-
tionen, eingesetzt werden.
9 z steht für „zero downtime“, da das System z von IBM komplett redundant ausgelegt ist.
1 Einführung

### Seite 27

15
Anzumerken ist noch, dass für mobile Geräte wie Smartphones spezielle Prozessoren
mit geringer Leistungsaufnahme wie z. B. ARM-Prozessoren (Advanced RISC Machi-
nes)10 eingesetzt werden. Diese Prozessoren werden in der Regel in Ein-Chip-Systeme
gemeinsam mit einem Grafikprozessor (GPU), einem LTE-Modem, einem Multimedia-
Prozessor, Einheiten für Bluetooth und WLAN usw. integriert. Bei den ARM-Prozessoren
handelt es sich heute auch schon um 64-Bit-Prozessoren.
Anmerkungen zu 64-Bit-Architekturen von Intel und AMD
Die IA64- und die IA32-Architektur sind Intel-Architekturen (IA), welche die prinzipiel-
len Arbeitsweisen von Prozessoren und deren Befehlssätze festlegen. Die IA64- Architektur
löst die IA32-Architektur ab. Die IA32-Architektur wird oft auch als i386- oder x86-
Architektur bezeichnet und ist die Basis aller Intel-80386-Prozessoren. Die IA64-
Architektur wurde speziell für den Intel-Itanium/Itanium2-Prozessor entwickelt.
Das Attribut „64-Bit“ wird in der Computertechnik vielfältig benutzt und trägt daher
auch zur Verwirrung bei. Man spricht u.  a. von 64-Bit-CPUs, 64-Bit-Hauptspeichern,
64-Bit-Architekturen und 64-Bit-Betriebssystemen. Man kann grundsätzlich sagen, dass
64-Bit-Betriebssysteme 64-Bit-Architekturen unterstützen. Sinngemäß gilt dies auch für
die Attribute „16-Bit“, „32-Bit“ und „128-Bit“. Wenn man von einer 64-Bit-Architektur
spricht, so meint man allerdings in erster Linie, dass die CPU auf die parallele Verarbei-
tung von 64 Bit ausgelegt ist. Davon sind die Daten- und Adressbusbreite (64 Datenleitun-
gen, 64 Adressleitungen), die Registergrößen und auch der Befehlssatz betroffen. Ein
64-Bit-Mikroprozessor verfügt über 64 Datenleitungen, mit denen Daten parallel zwi-
schen CPUs und Hauptspeicher übertragen werden können. Es ist aber nicht unbedingt der
Fall, dass alle CPUs mit 64-Bit-Datenpfaden auch 64-Bit-Adresspfade zur Adressierung
des Hauptspeichers zur Verfügung stellen. Ein Pentium-Prozessor verfügt z.  B. über
64-Bit-Datenpfade, aber nur 32-Bit-Adressleitungen. Auch 64-Bit-Prozessoren nutzen
nicht immer 64 Adressleitungen für die Hauptspeicheradressierung (mehr dazu in Kap. 7).
Zwei wichtige Mitbewerber am Markt der 64-Bit-Mikroprozessoren sind die Unter -
nehmen AMD und Intel. Diese Unternehmen haben für die Entwicklung von 64-Bit-CPUs
unterschiedliche Ansätze gewählt. Während Intel mit seiner IA64-Architektur eine Ab-
koppelung von der 32-Bit-Architektur unternahm, ging AMD mit seiner AMD64-Archi-
tektur, die auch als x64-Architektur 11 bezeichnet wird, eine Kompatibilitätsstrategie im
Hinblick auf die Kompatibilität zu x86-fähigen Programmen. Die älteren 32-Bit-
Prozessoren wurden von AMD um 64-Bit-Register erweitert. Die x64-Architektur ist da-
durch zu vorhandener 32-Bit- und sogar 16-Bit-Software abwärtskompatibel. Es gibt ent-
sprechende Kompatibilitätsmodi, die man im Prozessor einstellen kann. Die Register der
x64-Architektur sind nur Erweiterungen der 32-Bit-Architektur. Dementsprechend heißen
diese Register auch so ähnlich wie die Register der 80 × 86-Prozessoren (aus EAX wird
z. B. RAX).
10 Siehe hierzu http://www.arm.com, letzter Zugriff am 02.03.2020.
11 Früher nannte man die Architektur auch AMD64- und noch früher x86-64-Architektur.
1.1 Computersysteme

### Seite 28

16
Die Firma Intel hat aufgrund der nicht so erfolgreichen Itanium-Vermarktung ebenfalls
eine IA32-kompatible Prozessorarchitektur namens Intel 64 auf den Markt gebracht (siehe
Intel-Core-Prozessoren), die sich in einigen Instruktionen von der x64-Architektur unter-
scheidet.
1.2  Entwicklung von Betriebssystemen
Bevor wir die Entwicklungsgeschichte der Betriebssysteme betrachten, wollen wir eine
Kategorisierung versuchen und den Begriff des Mehrzweckbetriebssystems bzw. Univer -
salbetriebssystems, das wir im Weiteren in den Fokus unserer Betrachtung stellen,
einführen.
1.2.1  Betriebssystemkategorien
Man kann heutige Betriebssysteme grob in mehrere Kategorien einordnen, und wie man
sieht, werden manche Betriebssysteme auch für verschiedene Zwecke verwendet:
• Großrechner oder Mainframes (High-End-Systeme wie IBM OS/390 (heute IBM z/
OS)12 und Fujitsu BS 2000/OSD)
• Serverbetriebssysteme (Unix, Windows NT/2000/2003/2008, Windows 10)
• PC-Betriebssysteme (Windows-Derivate, Linux aus verschiedenen Distributionen,
Mac OS X, …)
• Echtzeitbetriebssysteme (VxWorks, QNX, Embedded Linux, NetBSD, …)
• Embedded Systems (VxWorks, QNX, Embedded Linux, NetBSD, Microsoft
Windows CE)
• Betriebssysteme für Tablet-PCs  wie das Apple iPad (iOS, Erweiterungen von Windows
und Linux, Android Honeycomb)
• Betriebssysteme für Handheld-Computer (Palm OS, Windows Mobile, Windows
Phone, Symbian, Android von der Open Handset Alliance (Hauptmitglied ist Google))
• Smartcard-Betriebssysteme (Chipkarte mit spezieller Java Virtual Machine, JVM) wie
TeleSec Chipcard Operating System (TCOS) von T-Systems, Java Card OpenPlatform
(JCOP) für Java Smartcards ursprünglich von IBM und Smart Card Chip Operating
System (STARCOS) von G&D
12 System z (vorher: zSeries) heißt die aktuelle Architektur der Mainframes der Firma IBM. Gegen-
über der V orgängerarchitektur S/390 unterscheidet sich System z u. a. durch die 64-Bit-Adressie-
rung. Das Modell IBM z15 mit bis zu 190 Prozessorkernen und bis zu 40 Terabyte Hauptspeicher
erschien 2019.
1 Einführung

### Seite 29

17
Typisch für Echtzeitsysteme ist die Forderung nach einer garantierten maximalen Re-
aktionszeit, in der auf ein externes Ereignis (Signal eines technischen Prozesses) reagiert
werden muss.
Embedded Systems (eingebettete Systeme) können als Spezialfall von Echtzeitsyste-
men betrachtet werden (Baumgarten und Siegert 2006). Als Embedded System bezeichnet
man ein Rechner- bzw. Steuerungssystem, das in Geräten (Telefone, DVD-Player, Wasch-
maschinen, Fernseher), Fahrzeugen (Flugzeuge, Autos) oder Robotern eingebaut ist und
dort seine Aufgaben meist unsichtbar verrichtet. Embedded Systems kann man weitge-
hend als geschlossene Systeme betrachten, die eine dedizierte Aufgabe übernehmen. Das
Betriebssystem ist klein ausgelegt, da meist wenige Ressourcen verfügbar sind. Oft ver -
fügen Embedded Systems aufgrund der knappen Ressourcen nicht über ein Betriebssys-
tem. Die Software bedient dann direkt die Hardwareschnittstellen. Embedded Systems
sind oft auch Echtzeitsysteme.
Weiterhin kann man noch Netzwerkbetriebssysteme (wie Novell Netware) und ver -
teilte Betriebssysteme als spezielle Betriebssystemkategorien sehen.
1.2.2  Universalbetriebssysteme
Unter die Kategorie Universal- oder Mehrzweckbetriebssystemen (engl.: general purpose
operating system) fallen Betriebssysteme wie Unix und Windows, aber auch Großrechner-
betriebssysteme, die für verschiedenste Zwecke, meist aber nicht für strenge Realzeitan-
forderungen einsetzbar sind. Diese Betriebssysteme findet man häufig in Unternehmen.
Sie sind besonders gut für betriebliche Informations- und Steuerungssysteme und für Sys-
teme in der Verwaltung geeignet.
1.2.3  Historische Entwicklung
In (Tanenbaum und Bos 2016) wird die Entwicklung von Betriebssystemen seit 1945 in
fünf Generationen eingeteilt. In den ersten Jahren der Nachkriegszeit bis etwa 1955 gab es
noch keine Betriebssysteme. Die heutigen Universalbetriebssysteme werden seit den
50er-Jahren entwickelt. Anfangs waren die Betriebssysteme noch sehr einfach. Mit der
Verbesserung und Verkleinerung der Hardware (Ablösung der Transistoren durch inte-
grierte Bausteine (Integrated Circuits, IC))13 Mitte der 60er-Jahre wurden Betriebssysteme
immer komplexer. Bekannte Systeme zu dieser Zeit waren IBM System/360 (Serie von
Rechnern), IBM System/370, 3080 und 3090. Mehrere Programme liefen bereits gleich-
zeitig oder quasi-gleichzeitig im Rechnersystem ab. Später kam der Mehrbenutzerbetrieb
13 Integrierte Schaltkreise (IC) sind auf einem einzigen Stück Halbleitersubstrat untergebrachte elek-
tronische Schaltungen.
1.2 Entwicklung von Betriebssystemen

### Seite 30

18
hinzu. Am M.I.T. entwickelte man die Betriebssysteme CTSS 14 und MULTICS.15 DEC
entwickelte die Minicomputer DEC PDP-1 und PDP-11 auf denen Unix als Betriebssys-
tem eingeführt wurde. Seit den 80er-Jahren folgten verbesserte Betriebssysteme für Groß-
rechner wie IBM OS/360. Personal Computer und Workstations wie mit Betriebssystemen
MS-DOS, Unix, Unix BSD, Unix System V , IBM OS/2, Microsoft Windows-Derivate und
Linux kamen auf dem Markt. Die Benutzerfreundlichkeit stieg immer mehr durch komfor-
table Bediensysteme, sog. grafische Oberflächen. Gerade was die Benutzerfreundlichkeit
anbelangt wurden vor allem in den letzten Jahren nochmals deutliche Fortschritte erzielt.
Besonders zu erwähnen sind hier die Benutzerschnittstellen der Betriebssysteme des Un-
ternehmens Apple. Heutige PCs und Notebooks sind wesentlich leistungsfähiger als die
Mainframes der 70er- und 80er-Jahre.
In den letzten Jahren wurden zudem die kleineren mobilen Geräte ebenfalls immer
leistungsfähiger und deren Betriebssysteme immer komplexer. Sie ähneln heute den Be-
triebssystemen für klassische PCs. Die Verbreitung von kleinen, leistungsfähigen Geräten
(Mobiltelefone, Smartphones, PDAs, Notepads) stieg rasant und die Einsatzmöglichkeiten
ebenso. Insbesondere Betriebssysteme wie Google Android und Apple iOS gelten derzeit
als die V orreiter in diesem Umfeld. Der Trend zu mobilen Anwendungen hat aber erst be-
gonnen und es bleibt abzuwarten, was die nächsten Jahre ergeben werden.
1.2.4  Geschichte von Microsoft Windows
Das Betriebssystem mit der größten Verbreitung ist Windows, das aus MS-DOS (Microsoft
Disk Operating System) hervorging. MS-DOS wurde 1981 im IBM-Auftrag von Micro-
soft entwickelt. Microsoft kaufte es seinerseits von der Firma Seattle Computer Products.
Es wurde zunächst auf Basis eines Intel-8088-Prozessors als 8-Bit-Betriebssystem (es
unterstützte also einen 8-Bit-Datenbus) auf dem Markt gebracht und bis MS-DOS V8.0
weiterentwickelt.
MS-DOS war ein einfaches Betriebssystem mit Kommandozeilen-orientierter Benut-
zeroberfläche. Die Basis war QDOS (quick and dirty operating system), ein Betriebssys-
tem für den Mikroprozessor Intel 8088. QDOS wurde von Tim Paterson bei der Firma
Seattle Computer Products entwickelt, 1981 von Microsoft übernommen und zu MS-DOS
weiterentwickelt. Das Betriebssystem war CP/M sehr ähnlich, hatte aber einige Verbesse-
rungen bei der Dateiverwaltung, z. B. das FAT-Dateisystem, das wir in Kap.  8 noch be-
trachten werden. Die Ursprungsversion von MS-DOS unterstützte noch keine Festplatte,
sondern nur Floppy-Laufwerke.
Windows war zunächst nur eine grafische Oberfläche für MS-DOS, entwickelte sich
anfangs sehr langsam und war durch die Kompatibilität zu MS-DOS sehr eingeschränkt
und auch fehleranfällig. Erst mit Windows NT und Windows 95 gelang der Durchbruch.
14 CTSS ist die Abkürzung für „Compatible Timer Sharing System“.
15 MULTICS steht abkürzend für „MULTIplexed Information and Computing Service“.
1 Einführung

### Seite 31

19
Heute sind mit Windows 2008 bzw. Windows 7 leistungsfähige Betriebssysteme auf dem
Markt, die sowohl im Arbeitsplatzbereich, als auch im Serverbereich eingesetzt werden.
Die Geschichte von Windows und dessen Ursprung in MS-DOS bzw. QDOS bis hin zum
heutigen Windows NT 10.0 ist in Abb. 1.6 und 1.7 etwas vereinfacht skizziert. Das heutige
Windows setzt immer noch auf Windows NT (New Technology) auf. Die Planung von
Microsoft ist nicht genau durchschaubar. So ist noch nicht ersichtlich, wann ein Betriebs-
system auf dem Markt kommt, das nicht mehr auf NT basiert.
Windows NT hatte im Jahre 2000 einen Codeumfang von ca. 29 Mio. LOC (Lines of
Code). Bei Windows Vista sprach man bereits von einem Codeumfang von 50  Mio.
LOC.  Entsprechend dürften die weiteren Versionen von Windows noch umfangreicher
sein, genauere Zahlen sind nicht veröffentlicht. Dem gegenüber wirkt der Linux-Kernel
(siehe unten), ein Unix-Derivat, mit über 26 Mio. LOC in Version 5.2 (2019) bzw. recht
schlank. Allerdings muss man beim Vergleich beachten, welche Softwarebausteine mit-
gerechnet werden.16
16 Die Anzahl der Codezeilen sind nicht unbedingt eine gute Metrik für die Funktionalität. Die Met-
rik erlaubt aber doch eine gewisse Einschätzung, wenn man bedenkt, dass die Entwickler von Be-
triebssystemen meist guten Code entwickeln.
CP/M
86-DOS
Seattle Computer
Products
MS-DOS
MS-DOS 1.0
(12.08.1981)
86-DOS nur
umbenannt
QDOS
MS-DOS 8.0
(Ende 1999)
Microsoft kauft
QDOS
Windows 1.0
(1985)
Windows 3.1
(1993)
Windows 95
(1995)
Windows
Windows ME
(2000)
Durchbruch
Grafische Oberfläche
für MS-DOS
Abb. 1.6 V on MS-DOS zu Windows
1.2 Entwicklung von Betriebssystemen

### Seite 32

20
1.2.5  Geschichte von Unix
Unix entstand aus dem Betriebssystem MULTICS zunächst unter einer PDP-7 und wurde
von Ken Thompson und Dennis Ritchie in den Bell Labs entwickelt. Danach entstanden
zwei inkompatible Versionen: BSD Unix aus der Berkeley University als V orgänger von
Sun OS und System V von AT&T. Das BSD-System findet man heute in Derivaten wie
FreeBSD, OpenBSD, BSDI, Mac OS X und NetBSD wieder.
Standardisierungsbemühungen der IEEE 17 brachten gegen Ende der 80er-Jahre einen
Standard namens POSIX (Portable Operating System Interface) hervor, der eine einheit-
liche Schnittstelle eines kompatiblen Unix-Systems definiert. Andere Standardisierungs-
bemühungen der Open Group18 brachten den als XPG (Unix Portability Guide) bezeichne-
ten Standard hervor, der durch diverse Unix-Hersteller unterstützt wird. Weiterhin wird
das System V, das ursprünglich von den USL (Unix System Laboratories) von AT&T
stammt, als Standard gehandelt. Hier wurde der Standard SVID (System V Interface Defi-
nition) als Schnittstellenspezifikation entwickelt.
Die neueste Standardisierung von Unix-Systemen ist die sog. Single Unix Specification
(SUS), die seit dem Jahr 2013 in einer Version 4 (SUSv4) vorliegt und auch durch einen
17 IEEE = Institute for Electrical and Electronic Engineers, vergleichbar mit VDI in Deutschland.
18 Die Open Group ist ein Konsortium aus mehreren Unternehmen, die (u.  a.) Unix-Systeme
herstellen.
Windows Server
(2012)
Windows Server
(2016)
bis NT 6.3
NT 10.0
Windows Phone 8
(2012)
bis NT 6.3
Von hier ab sog. Service-Updates
Windows Server
(2019)
Windows NT
Windows NT 3.1
(1993)
Windows NT 4.0
(1996)
Windows CE
(1998)
Danach „Pocket“, Windows „Mobile“ ...
(heute nicht mehr relevant)
Windows 2003
(2003)
Windows Vista
(2006/2007)
Windows 2000
(2000)
NT 6.0
Windows Server
(2008)
NT 6.0
NT 6.1
Windows XP
(2001)
Windows 7
(2009)
Bis NT 6.3
Windows 8
(2012)
NT 10.0
...Kein
Windows 9!
Mobile Betriebssysteme
Neue Basis für alle Windows-
Betriebs systeme
Abb. 1.7 V on Windows zu Windows NT
1 Einführung

### Seite 33

21
internationalen Standard der ISO/IEC 19 genormt ist. Dieser Standard wurde gemeinsam
von IEEE und der Open Group entwickelt und wird derzeit von der Austin Common Stan-
dards Revision Group (kurz Austin Group) gepflegt. Den Normierungen sind im Wesent-
lichen Schnittstellenspezifikationen für die Unix-Kommandos und für Systemdienste un-
terworfen. Die Unix-Hersteller müssen nachweisen, dass sie die Standards erfüllen, und
dürfen dann ihre Unix-Produkte als standardkonform bezeichnen. Eine Zertifizierung
nach dem ISO-Standard erlaubt z. B. die Führung des Labels Unix 04. Die wichtigsten
Unix-Hersteller unterstützen heute diese Standards (IBM AIX, HP-UX, Mac OS X, Ora-
cle Solaris), was sie aber nicht daran hindert, Alleinstellungsmerkmale zu ergänzen, so-
dass sich Unix-Derivate trotzdem teilweise stark unterscheiden.
In Abb. 1.8 ist die Unix-Entwicklung beginnend bei OTSS über MULTICS und Unics
bis hin zu den heutigen Derivaten skizziert. Wie man aus der Skizze erkennen kann, ging
auch das Betriebssystem macOS über den V orgänger NextStep aus dieser Entwicklung
hervor. Der Übergang von OTSS zu MULTICS wurde seinerzeit über ein ARPA-Projekt
gefördert.20
19 ISO = International Standardisation Organisation; die Unix-Norm heißt 9945:2003. IEC = Inter -
national Electrotechnical Commission; IEC ist ein internationales elektrotechnisches Normierungs-
gremium mit Sitz in Genf für Normen im Bereich der Elektrotechnik und Elektronik. Einige Nor -
men werden gemeinsam mit ISO entwickelt, darum ISO/IEC.
20 ARPA war die US-amerikanische Forschungsbehörde, die heute DARPA (Defences Advandes Re-
search Project Agency) heißt.
MULTICS(1965)
Unics (1969)
AT&T
ARPA-FörderungOTSS
MIT
Bell Labs (AT&T)
General Electric
BSD (ab 1977)
Berkeley
University
AT&T V6/V7
System V (1983)
AT&T
Betriebssystem für
Großrechner
NextStep
Steve Jobs, Next
macOS
Apple
SunOS
Sun Solaris
Nun
Oracle
HP UX AIX SINIX, ...
HPSun IBM Siemens
NetBSD
OpenBSD
FreeBSD
Freie Unixe
Abb. 1.8 Unix-Entwicklungsgeschichte
1.2 Entwicklung von Betriebssystemen

### Seite 34

22
1.2.6  Geschichte von Linux
Linus Torvalds begann schließlich 1991 aus dem Unix-Clone MINIX von Tanenbaum das
Betriebssystem Linux (der Name stammt von seinem V ornamen, anstelle von „s“ wurde
„x“ von Unix eingesetzt) als Open-Source-Unix zu entwickeln (Abb. 1.9). Er verwendete
dabei die GNU-GPL-Lizenz (General Public Licence), was für eine freie Nutzung von
V orteil war. Linux V1.0 wurde schließlich im Jahre 1994 und Linux 2.0 im Jahre 1996
freigegeben. Im Januar 2020 wurde die zu der Zeit aktuelle Version mit der Versionsnum-
mer 5.5 bezeichnet.
Linux wird wie auch Unix im Wesentlichen in der Programmiersprache C entwickelt.
Heute ist Linux das populärste Unix-Derivat und ist zertifiziert nach POSIX 1003.1a. Wei-
terhin implementiert Linux auch die Systemaufrufe von SVID Release 4 und BSD-Unix,
ist allerdings nicht SUSv3-konform. Es gibt mittlerweile eine Reihe von sog. Linux-
Distributionen, die alle auf dem gleichen Kernel aufsetzen. Hierzu gehören Debian, Red
Hat (derzeit am bekanntesten und größten), Fedora (kostenloser Entwicklungszweig von
Red Hat), SUSE, Ubuntu (sehr populär für Privatanwender), CentOS und Chrome OS, um
nur einige zu nennen. Android (Google) nutzt ebenfalls einen Linux-Kernel, allerdings in
einer abgekoppelten Version. Verschiedene Distributoren bieten kommerzielle Dienste wie
Wartungs- und Supportleistungen und sog. Enterprise Lizenzen an. Damit ist Linux auch
seit längerer Zeit für den kommerziellen Einsatz geeignet und wird insbesondere im
Web-Umfeld (z. B. als Betriebssystem für Webserver) stark eingesetzt.
MINIX (1987)
Linux 1.0 (1994)
UNIXe Tanenbaum
Erste Veröﬀentlichung: 1991
Linux 2.0 (1996)
...
CentOS
Debian RedHat SUSE
FedoraEnterprise Linux
Chrome OS
Google
Android
Linux heute 5.5 (Januar 2020)
Ubuntu OpenSUSE Fire OS
Amazon
Abb. 1.9 Entwicklungsgeschichte von Linux
1 Einführung

### Seite 35

23
Der Linux-Kernel wird heute, mehr als 25 Jahre nach der ersten Version, immer noch
von Linus Torvalds verwaltet. Er legt fest, welche Funktionen in den offiziellen Kernel
eingebaut werden.
1.2.7  Geschichte von macOS
macOS ist ein Betriebssystem der Firma Apple Inc., einem US-amerikanischer Hard- und
Softwarehersteller. Wie schon bei der Unix-Geschichte ging auch das Betriebssystem ma-
cOS über den V orgänger NeXTStep aus der Unix-Entwicklung hervor, wie in Abb. 1.10
skizziert ist. Das Betriebssystem NeXTStep wurde von NeXT, einem Unternehmen von
Steve Jobs entwickelt und zwar zu der Zeit, nachdem er Apple verlassen hatte. Neben
FreeBSD hatte auch noch Mach, das an der Carnegie Mellon University (CMU) in Penn-
sylvania entwickelte Betriebssystem, Einfluss auf NeXTStep. NeXTStep wurde später zu
OpenStep (1996) umbenannt. Als Steve Jobs, einer der Apple-Gründer wieder zu Apple
zurückkam (die Firma NeXT wurde von Apple gekauft), nahm er OpenStep mit.
Apple entwickelte aus OpenStep das Betriebssystem Rhapsody, aus dem dann schließ-
lich im Jahre 2001 Mac OS X wurde. Bereits zwei Jahre vorher wurde das Betriebssystem
Mac OS X Server auf Basis von Rhapsody veröffentlicht.
Darwin (1999)
FreeBSD
iOS (2007)
Mac OS X (2001)
umbenannt
macOS 10.x
WatchOS
Mach (1985-1994)
Rhapsody (1998)
X römisch 10
Frei verfügbarer Teil von Rhapsody
2006 eingestellt
Apple
Apple
Apple Watch (2014)
1997: Firma NeXT wurde von
Apple gekauft, Steve Jobs
kam wieder zu Apple
macOS (2016)
High Sierra, 10.13.x (2017)
Mojave, 10.14.x (2018)
Catalina 10.15.x (2019)
iOS 12.2.x (2018)
iOS 13.3.x (2020)
OpenStep (1996)
NeXT, Steve Jobs
NeXTStep (1988)
umbenannt
Mac OS X Server (1999)
iPadOSiPad (2019)
Abb. 1.10 Entwicklungsgeschichte von macOS
1.2 Entwicklung von Betriebssystemen

### Seite 36

24
Apple stellte im Jahre 1999 einen Teil von Rhapsody, Darwin genannt, frei zur Verfü-
gung, stellte diesen Teil dann aber 2006 wieder ein.
Mac OS X wurde zunächst im Jahr 2012 in OS X und dann im Jahr 2017 nach macOS
umbenannt. Weitere Ableitungen aus macOS sind iOS als Betriebssystem für Smartphones
sowie das wiederum davon abgeleitete WatchOS als Betriebssystem für die Apple-Uhren
und das iPadOS für Apple iPads (Tablets).
1.3  Übungsaufgaben
1. Nennen Sie fünf Betriebssystemkategorien!
2. Was ist ein V on-Neumann-Rechner und wie unterscheidet er sich von einem
Harvard- Rechner?
3. Wozu braucht man in Computern CPU-Register?
4. Was ist ein Program Status Word (PSW) und wozu wird es verwendet?
5. Was ist ein Mehrzweck- oder Universalbetriebssystem?
6. Was ist ein Mehrkernprozessor?
7. Was versteht man unter einer Prozessorarchitektur?
8. Was ist mit einer Mikroarchitektur gemeint?
9. Welche Unix-Standards kennen Sie und was standardisieren diese?
10. Was versteht man unter einem symmetrischen Multiprozessorsystem?
11. Was sind UMA-Multiprozessoren?
Literatur
Baumgarten, U., & Siegert H.-J. (2006). Betriebssysteme (6. Aufl.). München: Oldenbourg.
Brinkschulte, U., & Ungerer, T. (2010). Mikrocontroller und Mikroprozessoren (3. Aufl.). Berlin/
Heidelberg: Springer.
Herrmann, P. (2002). Rechnerarchitektur (3. Aufl.). Braunschweig/Wiesbaden/Vieweg.
Homeister, M. (2015). Quantum Computing verstehen Grundlagen – Anwendungen – Perspektiven
(4. Aufl.). Wiesbaden: Springer Vieweg.
Tanenbaum, A. S., & Bos, H. (2016). Moderne Betriebssysteme (4., akt. Aufl.). (deutsche Überset-
zung von Tanenbaum & Bos 2015). Hallbergmoos/Pearson Deutschland.
1 Einführung

### Seite 37

25© Springer Fachmedien Wiesbaden GmbH, ein Teil von Springer Nature 2020
P. Mandl, Grundkurs Betriebssysteme,
https://doi.org/10.1007/978-3-658-30547-5_2
2Betriebssystemarchitekturen und
Betriebsarten
Dieses Kapitel führt in Betriebssystemarchitekturen und typische Betriebsarten von Be-
triebssystemen ein. Dazu ist es zunächst notwendig, die Zugriffsschutzkonzepte von Be-
triebssystemen zu erläutern und Begriffe wie Benutzermodus und Kernelmodus einzufüh-
ren. Häufig verwendete Begriffe zu historischen und aktuell üblichen Betriebsarten wie
Multitasking und Timesharing werden gegeneinander abgegrenzt. Spezielle Betriebsarten
wie Teilnehmer- und Teilhaberbetrieb sowie der Application-Server-Betrieb werden ein-
geführt. Der heute wieder an Bedeutung gewinnende Terminalbetrieb, allerdings im
Gegensatz zu früher mit grafischer Oberfläche anstelle von blockorientierten, alpha-
numerischen Terminals, wird ebenfalls kurz vorgestellt. Dabei wird erläutert, was ein Ter-
minalserver ist. Ebenso wird auf die sich immer weiter verbreitenden Konzepte der Vir -
tualisierung, insbesondere auf die Virtualisierung von Betriebssystemen eingegangen.
Eine kurze Einführung zu Cloud Computing, das zunehmend an Bedeutung gewinnt,
rundet diese Einführung ab.
Zielsetzung des Kapitels
Der Studierende soll die gängigen Architekturvarianten verstehen und erläutern können.
Weiterhin sollen die verschiedenen Betriebsarten und die grundlegenden Konzepte zur
Virtualisierung und für das Cloud Computing wiedergegeben werden können.
Wichtige Begriffe
Kernel, Betriebssystemkernel, Timesharing, Stapelsystem, Teilnehmer- und Teilhaberbe-
trieb, Transaktionsmonitor, Application-Server, Multiprocessing, Multitasking, Mehr -
zweckbetriebssystem, Verteiltes System, Terminalserver, Virtualisierung, Betriebssystem-
virtualisierung, Cloud Computing.

### Seite 38

26
2.1  Zugriffsschutz in Betriebssystemen
Das Betriebssystem wird üblicherweise von den Anwendungen abgeschottet, damit es vor
unprivilegierten Zugriffen geschützt ist. Gewisse Aufgaben, wie der Zugriff auf die Hard-
ware oder die Verwaltung spezieller Ressourcen dürfen nicht direkt durch Anwendungen
möglich sein. Auch ist es nicht zulässig, dass Anwendungen andere Anwendungen beein-
trächtigen, z. B. indem sie Datenbereiche von ihnen sehen oder verändern können. Da
Anwendungen aber die Dienste des Betriebssystems benötigen, um die vom Betriebssys-
tem verwalteten Betriebsmittel nutzen zu können, ist eine dedizierte, abgesicherte Schnitt-
stelle erforderlich, die einen kontrollierten Übergang von einer Anwendung in das Be-
triebssystem ermöglicht.
Für diese Zwecke gibt es in der Regel einen privilegierten und einen nicht- privilegierten
Modus. Man spricht in diesem Zusammenhang auch von Benutzer- und Kernelmodus.
Diese beiden Modi sind für heutige Betriebssysteme typisch. Sie haben folgende
Bedeutung:
• Im Benutzermodus (Usermodus) laufen üblicherweise Anwendungsprogramme ab. In die-
sem Modus ist ein Zugriff auf kernelspezifische Code- und Datenbereiche nicht möglich
• Im Kernelmodus (privilegierter Modus) werden Programmteile des Betriebssystems
ausgeführt, die einem gewissen Schutz unterliegen. Damit kann das Betriebssystem
auch eine Abschottung von Datenstrukturen und Codeteilen des Betriebssystems vor
Zugriffen aus Anwendungsprogrammen heraus vornehmen
Für die Realisierung dieser beiden Modi benötigt man die Unterstützung des Prozes-
sors in zweifacher Hinsicht. Zum einen müssen diese Modi darstellbar bzw. einstellbar
sein, was in der Regel über ein Steuer- und Kontrollregister (z. B. interne Kontrollregister
bei Intel-Prozessoren) möglich ist. Zum anderen muss es einen Maschinenbefehl geben,
der einen kontrollierten Übergang vom Benutzermodus in den privilegierten Modus er -
möglicht, damit ein Anwendungsprogramm eine Betriebssystemfunktion, wie z. B. zum
Anlegen einer Datei, aufrufen kann.
Bei den älteren x86-Intel-Architekturen wird das Schutzkonzept über vier Privilegie-
rungsstufen realisiert, die als Ringe (Ring 0 bis 3) bezeichnet werden (siehe hierzu
Abb. 2.1). Ein Anwendungsprogramm läuft zu einer Zeit in genau einem Ring. In anderen
Prozessoren und auch bei neueren x64/IA64-Prozessoren gibt es seit jeher nur zwei Ringe,
weshalb Betriebssysteme aus Kompatibilitätsgründen ebenfalls nur zwei Ringe nutzen.
Die Abbildung bzw. Nutzung der Ringe auf Modi erfolgt häufig folgendermaßen:
• Mit dem Ring 0 wird der Kernelmodus realisiert
• Der Benutzermodus wird auf Ring 3 abgebildet
2 Betriebssystemarchitekturen und Betriebsarten

### Seite 39

27
• Der Übergang von einem höheren auf einen niedrigeren (höher priorisierten) Ring, also
von Ring 3 nach Ring 0 erfolgt über eine privilegierte Operation (z. B. der int-Befehl
im x86-Befehlssatz)1. Die anderen Ringe werden nicht verwendet2
• Beim Wechsel von Ring 3 nach Ring 0 wird ein Kontextwechsel durchgeführt. Was dies
genau bedeutet, wird in Kap. 3 noch weiter ausgeführt
• Bei Aufruf eines privilegierten Befehls in einem nicht dafür gedachten Ring wird eine
Ausnahme (ein sog. Trap) ausgelöst, die in dem dafür privilegierten Ring bearbeitet wird
V on diesem Zugriffsschutz gehen wir nun bei der weiteren Betrachtung der Architektu-
ren aus und werden in Kap.  3 im Rahmen der Virtualisierungskonzepte nochmals darauf
zurückkommen.
2.2  Betriebssystemarchitekturen
2.2.1  Klassische Architekturen
Betriebssysteme sind sehr komplexe Softwaresysteme und intern in Komponenten bzw.
Module strukturiert. Etwas ältere Betriebssysteme besitzen meist einen rein monolithi-
schen Betriebssystemkern (Kernel), wie dies in Abb. 2.2 dargestellt ist. Der gesamte Kern
mit allen Modulen stellt bei dieser Architekturvariante ein zusmmenhängendes Pro-
gramm dar.
1 Mehr dazu in Kap. 3 bei der Diskussion von Systemcalls.
2 Bei der Betriebssystemvirtualisierung mit Hardwareunterstützung kommt wieder ein neuer Modus
hinzu; dazu mehr in Kap. 9.
Aufruf eines
privilegierten
Befehls
Kernelmodus
Ring 0
Ring 1
unbenutzt
unbenutzt
Ring 2
Anwendung
Ring 3
(Usermodus)
Usermodus
Kernelmodus
Systemcall
Abb. 2.1 Schutzringe bei x86-Prozessoren und deren Nutzung in Betriebssystemen
2.2 Betriebssystemarchitekturen

### Seite 40

28
Alle Module eines monolithischen Kerns werden im privilegierten Modus ausgeführt
und haben den kompletten Kerneladressraum im Zugriff. Meist findet man einen sog.
Diensteverteiler, der die Systemaufrufe der Anwendungen entgegennimmt und an die ein-
zelnen Kernelmodule weiterleitet. Die ursprüngliche Struktur des Betriebssystems wird
ggf. im Zuge der Weiterentwicklung aufgegeben. Das alte MS-DOS, aber auch ältere
Unix-Derivate und auch Linux verfügen über eine derartige Architektur.
Als Weiterentwicklung bzw. Verbesserung des monolithischen Kerns wurden neuere
Betriebssysteme üblicherweise in Schichten strukturiert, wie dies in Abb. 2.3 beispielhaft
dargestellt ist. Dadurch gelang es, den Kernel flexibler und überschaubarer zu gestalten.
Einen Standard für die Schichtung gibt es allerdings nicht, da dies vom jeweiligen Design
des Systems abhängt. Höhere Schichten nutzen die Module der darunter liegenden Schicht
und nur in äußersten Ausnahmefällen und wohlbegründet (z. B. aufgrund von Leistungs-
argumenten) tiefere Schichtenfunktionalität direkt. Die unterste Schicht dient meist dem
Zugriff auf die konkrete Hardware. Abhängigkeiten von der Hardware sind also in dieser
Schicht gekapselt, was eine Portierung auf eine andere Hardwareplattform erleichtert. Die
Schnittstelle zur Hardware wird oft noch – zumindest teilweise – in Assemblersprache
programmiert.
Die typischen Komponenten des Kernels wie Memory-Manager (Speicherverwaltung),
Prozess-Manager (Prozessverwaltung), File-Manager (Dateiverwaltung), E/A-Manager
(Ein-/Ausgabeverwaltung), Netzwerk-Manager (Netzwerkzugang) und Treiber (Hard-
warezugang) werden auf Schichten verteilt, die in den verschiedenen Betriebssystemen
zum Teil sehr unterschiedlich festgelegt sind.
Als Beispiele heute weit verbreiteter Betriebssysteme mit Schichtenarchitektur sind
verschiedene Unix-Derivate (Ableitungen von Unix sind HP UX, Sun Solaris, …) und
Windows-Derivate (2000, 2003, XP, Vista, 7, 2008, 8, 2012) zu nennen.
Hardware
Anwendung 1 Anwendung 2 ... Anwendung n
Systemdienste-
Schnittstelle
Dienstverteiler
Kernel
Hardware-
Schnittstelle
Modul
Abb. 2.2 Monolithischer Kernel
2 Betriebssystemarchitekturen und Betriebsarten

### Seite 41

29
2.2.2  Mikrokern-Architektur
Im Gegensatz zu monolithischen Architekturen wird eine Betriebssystemarchitektur, die
einen leichtgewichtigen Kernel enthält, als Mikrokern-Architektur (auch Mikrokernel-
Architektur) bezeichnet. Der Kernel wird bei dieser Architekturvariante dadurch entlastet,
dass Funktionalität in Anwendungsprozesse, sog. Serverprozesse, die im Benutzermodus
laufen, ausgelagert wird. Nicht die gesamte Kernelfunktionalität läuft also im Kernelmo-
dus und auch nicht in einem einzigen zusammenhängenden Programm.
Der Kernel übernimmt hier im Wesentlichen die Abwicklung der Kommunikation zwi-
schen den sog. Client- und Serverprozessen. Beispiele für Mikrokern-Betriebssysteme
sind Mach von der Carnegy Mellon University (CMU), Hurt, L4 sowie Amoeba und Cho-
rus (Tanenbaum und Bos 2016). Besonders für Echtzeitanwendungen werden Mikrokern-
Betriebssysteme häufig verwendet. Beispielsweise wird QNX (Entwicklungsfirmen Gor -
don Bell und Dan Dodge), das auch als BlackBerry Tablet OS im Smartphone Blackberry
eingesetzt wird, als echtzeitfähiges Betriebssystem mit Mikrokern für eingebettete Sys-
teme bezeichnet. Das Betriebssystem Mach diente auch als eine Basis des Betriebssys-
tems macOS von der Firma Apple Inc (siehe Kap. 1).
Die Mikrokern-Architektur entstand aus dem Trend, den Kernel „leichter“ zu machen.
Aus dem Kernel ausgelagerte Serverprozesse können z.  B. ein File-Server oder ein
Memory- Server sein. Clientprozesse greifen bei dieser Betriebssystemarchitektur auf den
Mikrokern über eine Service-Request-Schnittstelle zu. Der Mikrokern leitet die Requests
an die entsprechenden Server, die in nicht privilegierten Anwendungsprozessen ablaufen,
weiter und stellt umgekehrt den Clientprozessen die Ergebnisse zu.
Hardware
Anwendung 1 Anwendung 2 ... Anwendung n
Systemdienste-
Schnittstelle
Schicht 2
Schicht 1
Schicht 3
Abb. 2.3 Schichtenorientierter Kernel
2.2 Betriebssystemarchitekturen

### Seite 42

30
Generell kann man sagen, dass die Mikrokern-Architektur nicht sehr leistungsfähig ist
und daher auch in der Praxis in ihrer reinen Form nicht angewendet wird. Heutige Imple-
mentierungen wie Windows sind z. B. so ausgelegt, dass zumindest der Memory-Manager,
der Prozess-Manager, der Netzwerk-Manager, der E/A-Manager und der File-Manager im
Kernelmodus ablaufen (Russinovich et al. 2012b). Abb. 2.4 verdeutlicht diese Architektur-
variante (nach Tanenbaum und Bos 2016).
Eine Weiterführung des Mikrokernel-Konzepts wird in der sog. Exokernel-Architektur
versucht. Hier wird der Kern bzw. der Code, der im Kernelmodus abläuft, weiter reduziert.
Abstraktionsschichten werden dort, wo es möglich ist, entfernt. Der Zugriff auf Hardware-
Ressourcen erfolgt hier direkt über die Anwendungen, wobei der Exokernel lediglich die
Aufgabe der Konfliktvermeidung übernimmt. Mit diesem Ansatz zielt man darauf ab, die
Effizienz zu erhöhen (Tanenbaum und Bos 2016). Reduzierungen des Kernels werden
auch gelegentlich als Nano- oder Picokernel bezeichnet (Shapiro et al. 1992). Man spricht
dann auch von einem Hybrid-Kernel. In Abb. 2.5 findet sich eine grobe Gegenüberstellung
der drei Architekturansätze Monolith, Mikrokernel und Hybrid-Kernel mit typischen Auf-
gabenverteilungen.
Mikrokern
Hardware
Usermodus
Kernelmodus
Client-
prozess … Server-
Prozess … ...
Service Request
Client-
prozess
Abb. 2.4 Mikrokern-
Architektur
Anwendung
Alle Betriebssystem-
komponenten
Hardware
Anwendung
Betriebssystem
Anwendung
Basiskommunikation,
Speicher- und CPU-Verwaltung
Hardware
Prozess-
kommunikation
File-
server
Geräte
treiber
Anwendung
Hardware
File-
server
…
Basiskommunikation, Speicher-
und CPU-Verwaltung +
Prozesskommunikation + Treiber
Sonstige
Server
Betriebssystem mit
monolithischem Kernel
Betriebssystem mit
Mikro-Kernel
Betriebssystem mit
Hybrid-Kernel
Komponente
im Kernelmodus
Komponente im
Usermodus
Abb. 2.5 Vergleich der verschiedenen Kernel-Architekturansätze
2 Betriebssystemarchitekturen und Betriebsarten

### Seite 43

31
2.2.3  Architekturbeispiele
Im Folgenden werden die konkreten Betriebssystemarchitekturen von Unix, Linux, And-
roid und Windows (ab 2003) etwas vereinfacht beschrieben.
Bei Unix ist eine klare Systemcall-Schnittstelle vorhanden, welche den Zugang zur
geschichteten, monolithischen Kernelfunktionalität ermöglicht. Jedes Benutzerprogramm
wird in der Regel von einer sog. Shell aus gestartet. Eine Shell stellt einen Kommando-
Interpreter dar. Beispiele hierfür sind die Korn-Shell und die Bourne-Shell. Innerhalb der
Shell können dann weitere Programme gestartet werden. Wie man aus der Abb.  2.6 erse-
hen kann, gibt es im Unix-Kernel Komponenten wie die Speicherverwaltung, das Datei-
system, die Prozessverwaltung usw.
Die Linux-Architektur (Abb.  2.7) ähnelt der Unix-Architektur sehr stark. Auch hier
handelt es sich um einen geschichteten, monolitischen Kernel, der für alle Linux-Derivate
gleich ist. Aus dem Usermodus kommt man über einen Aufruf aus der C-Library über eine
Systemcall-Schnittstelle geordnet in den Kernelmodus. Im monolitischen Kernel sind die
wesentlichen Betriebssystemfunktionen implementiert. Die Systemdienst-Schnittstelle
(Systemcall Interface) stellt ca. 380 Systemcalls bereit, die C-Library etwa 2000 Funktio-
nen für den kontrollierten Zugriff auf den Linux-Kernel.3
Android ist ein Linux-Derivat und wurde als Open-Source-Plattform von der Open
Handset Alliance, einem Zusammenschluss unterschiedlicher Unternehmen, entwickelt
und wird heute überwiegend für Smartphones, Fernseher und Tablets eingesetzt. V or allem
Google war und ist in der Android-Entwicklung federführend. Für Android wurde der
3 Stand März 2020, siehe https://en.wikipedia.org/wiki/Linux_kernel, letzter Zugriff am 03.03.2020.
Hardware
Usermodus
Kernelmodus
System Call Interface
Speicher-
verwaltung
Prozess-
verwaltung
Geräte-
verwaltung
Datei-
verwaltung
Weitere Libraries
C-Library
(fopen, exec, socket, calloc, …)
Anwendungsprogramme (vi, sh, sed, …)
Abb. 2.6 Architektur von Unix
2.2 Betriebssystemarchitekturen

### Seite 44

32
Linux-Kernel 2.6.26 als Basis verwendet und von der Linux-Kernel-Entwicklung abge-
koppelt. Mit der Android-Version 4.x wurde auf den Linux-Kernel 3.x umgestellt. Seit
2019 ist die Android-Version 10 im Einsatz.
Der Kernel wurde an einigen Stellen abgespeckt und an mehreren Stellen auch erwei-
tert, um den Anforderungen von mobilen Geräten gerecht zu werden. Beispielsweise
wurde ein spezielles Energie-Management ergänzt, da die Steuerung der Stromversorgung
über Aku in Smartphones und sonstigen mobilen Geräten andere Anforderungen erfüllen
muss. Auch wurde die Speicherverwaltung angepasst und es wurden spezielle Mechanis-
men für die interne Kommunikation ergänzt.
Das Betriebssystem macOS von Apple wurde aus verschiedenen Richtungen beeinflusst,
was sich auch heute noch im Kernel widerspiegelt (Abb. 2.8). Die grafische Benutzerober-
fläche von macOS wird als Aqua bezeichnet. Cocoa und Java sind Programmierschnittstellen
zur Entwicklung von Anwendungen, die wiederum auf eine Bereitstellungsebene mit ver-
schiedenen Diensten (Core Services, Grafik-Subsystem usw.) aufsetzen. Über die Bibliothek
libSystem.dylib, die verschiedene C-Bibliotheken wie libc zusammenfasst, wird der Kernel-
zugang ermöglicht. Darwin wird auch als das  Basisbetriebssystem (core operating system) für
macOS bezeichnet und enthält den hybriden XNU-Kernel (X is not Unix), der wiederum aus
BSD-Teilen und Mach’s Mikrokernel besteht. Das CPU-Scheduling, die Interruptverarbei-
tung, die Hauptspeicherverwaltung und weitere essenzielle Funktionen sind im Mac Mikor-
kernel enthalten. Aus dem BSD- Unix (konkret aus FreeBSD) wurde z. B. das Dateisystem
und die Netzwerkimplementierung übernommen.
iOS ist ein macOS-Derivat, das für Smartphones entwickelt wurde. Dementsprechend
enthält es auch einen Darwin-Kern, ebenso wie die Betriebssysteme watchOS und iPadOS
von Apple, die wiederum von iOS abstammen.
Hardware
Usermodus
Kernelmodus
System Call Interface
(TRAP, CALL, BRK, INT,…, je nach Hardware, ca. 380 Systemcalls)
Kernel
(Geräteverwaltung, Dateisystem, Speicherverwaltung,
Prozessverwaltung, Netzwerkverwaltung, …)
Weitere Libraries
C-Library glibc
(fopen, exec, socket, calloc, …, ca. 2000 Funktionen )
Anwendungsprogramme (vi, bash, openoffice,….)
Abb. 2.7 Architektur von Linux
2 Betriebssystemarchitekturen und Betriebsarten

### Seite 45

33
Windows (bzw. dessen V orgänger) wurde so konzipiert, dass auch Nicht-Windows-
Anwendungen wie OS/2- und POSIX-Anwendungen in diesem Betriebssystem ablaufen
können. Bei Windows ist die Architektur daher etwas komplizierter als beim klassischen
Unix. Verschiedene Subsysteme laufen im Benutzermodus ab, die wesentlichen Kompo-
nenten des Betriebssystems sind aber nur im Kernelmodus ablauffähig.
Die Subsysteme für POSIX und OS/2 sind heute nicht mehr so relevant. Das POSIX-
Subsystem wurde nur entwickelt, um den Anforderungen des amerikanischen Verteidi-
gungsministeriums an Betriebssysteme Rechnung zu tragen. In diesem Subsystem können
POSIX-konforme Anwendungen ablaufen. Das OS/2-Subsystem ermöglichte den Ablauf
von OS/2-Anwendungen und wurde nur entwickelt, um IBM-Kunden eine Möglichkeit
der Migration zu bieten. Dieses Subsystem wird seit Windows 2000 nicht mehr unter -
stützt. Auch das POSIX-Subsystem wird nicht mehr in allen Windows-Derivaten unter -
stützt. Unter Windows XP ist es beispielsweise nicht mehr im Lieferumfang enthalten. In
neueren Windows-Versionen erscheint das POSIX-Subsystem wieder mit der Bezeich-
nung „Subsystem for Unix-based Application“ (SUA) (Russinovich et  al. 2012a). Die
Subsysteme werden im Benutzermodus über den Prozess csrss zur Verfügung gestellt.
Wichtige Windows-Schichten und deren Zusammenhänge sind in Abb.  2.9 grob skiz-
ziert. Anwendungen im Usermodus können die Dienste des Betriebssystems über die Win-
dows-API (Win32-API, WinAPI) aus der Bibliothek 4 kernel32.dll nutzen, die ihrerseits
wieder die Dienste der NT-API (implementiert in der DLL Ntdll.dll) nutzt, um System-
calls wie NtCreateFile usw. abzusetzen.
4 Bibliotheken (Libraries) heißen unter Windows auch DLLs = Dynamic Link Libraries, da die Mo-
dule dynamisch zur Laufzeit nachgeladen werden.
Hardware
Usermodus
Kernelmodus
Systemcall Interface
Application Services: Cocoa, Java, ...
Core Services, Grafik-Subsystem, …
Mach Mikrokernel
(Scheduling, Interrupt-Handling, Speicherverwaltung, …)
Grafische Benutzerschnittstelle Aqua
libSystem.dylib
(Verschiedene C-Bibliotheken wie libc zusammengefasst)
BSD (Filesystem, Netzwerkschnittstelle, Prozessmodell, …)
Kernel „XNU“
Betriebssystem Darwin
Abb. 2.8 Architektur von macOS
2.2 Betriebssystemarchitekturen

### Seite 46

34
Im Benutzermodus laufen auch aus dem Kernelmodus ausgelagerte wichtige System-
prozesse und Windows-Services sowie die genannten Subsysteme. Im Windows-
Betriebssystem sind durch die Ausgliederung dieser Komponenten vom Kernel- in den
Benutzermodus gewisse Ansätze (nur Ansätze!) der Mikrokern-Architektur implemen-
tiert. Interessant ist auch die sog. Hardware Abstraction Layer (HAL), die den Zugriff auf
die eigentliche Hardware weitgehend kapselt und somit durch eine Austauschmöglichkeit
dieser Schicht auch die vereinfachte Unterstützung verschiedener Rechnerarchitekturen
ermöglicht (Russinovich et al. 2012a).
Die oberen Schichten des Kernelmodus werden auch gemeinsam als Executive be-
zeichnet und ebenfalls in der Datei Ntoskrnl.exe zur Verfügung gestellt. Hier werden im
Wesentlichen die Implementierungen der Systemdienste über einen Dispatching-
Mechanismus zugänglich gemacht. Die Hauptkomponenten des Kernels sind der Prozess-
und Thread-Manager, der E/A-Manager und der Memory-Manager.
In der Abbildung werden auch einige Hinweise über die Größenordnungen von Soft-
warekomponenten gegegen. Der CPU-Scheduler alleine hat z.  B. eine Größe von ca.
75.000 Codezeilen. Interessant ist auch, dass das gesamte .NET-Framework im Usermo-
dus abläuft und ebenso wie die anderen Anwendungen die Windows-API für den Zugriff
auf das Betriebssystem nutzt.
Wie die Architekturskizzen zeigen, sind sowohl moderne Unix- als auch Windows-
Derivate geschichtete Betriebssysteme mit einer gekapselten Hardwareschnittstelle. Die-
ser Aspekt wird heute auch immer wichtiger, da man nicht mehr das ganze Betriebssystem
neu entwickeln möchte, wenn man die Hardwareplattform (z.  B. durch Unterstützung
Usermodus
Kernelmodus
GUI (shell32.dll,…)
Dynamische Libraries (ole32dll,…)
Subsystem-API (kernel32.dll,…)
Prozess der
Subsysteme
(csrss.exe)
NT-Dienste: smss,
lsass, services,
winlogon
Native NT-API (C/C++-Routinen ntll.dl(vgl. libcunter Unix))
NTOS-Kernschicht
(ntoskrnl.exe) in C
NTCreateProcess
NTCreateFile,…
Systemdienste,
Kern, NTOS
= ntoskrnl.exe
Gerätetreiber NTOS-Ausführungsschicht
(ntoskrnl.exe) in C
GUI-Treiber
Win32k.sys
HAL (hal.dll)
x64: 1 % Assembler, x86: 2 % Assembler, Rest in C
Hardware
Geräte, CPU, MMU, Interrupt-Controller, Speicher
CreateProcess,
DeleteFile, …
Wrapper für
NT-API-Aufrufe
= Win32-API
(WinAPI)
.NET setzt hier auf
CPU-Scheduler: ~75 Kloc
Virt. Speicher: ~175 Kloc
Abb. 2.9 Architektur von Windows
2 Betriebssystemarchitekturen und Betriebsarten

### Seite 47

35
eines neuen Prozessors) austauscht. Betriebssysteme wie Unix und Windows unterstützen
heute eine ganze Fülle von verschiedenen Hardwareplattformen. Ohne eine Abstraktions-
schicht wie die Hardware Abstraction Layer von Windows wäre dies nicht mit vertretba-
rem Aufwand möglich.
2.3  Klassische Großrechnerbetriebsarten
Viele Begriffe aus der Welt der Betriebssysteme haben ihren Ursprung in Mainframe-
Systemen. Insbesondere wurde dort auch der Begriff „Betriebsart“ verwendet, um gewisse
Eigenschaften von Betriebssystemen zu erläutern. Einige Begriffe sollen im Folgenden
eingeführt werden.
2.3.1  Multiprocessing und Multitasking
Multitasking (Syn.: Mehrprogrammbetrieb oder Multiprogramming) ist ein Begriff, der
bereits mehrfach verwendet wurde. Dieser Begriff bezeichnet im Gegensatz zum Einpro-
grammbetrieb (Singletasking) die Möglichkeit der „gleichzeitigen“ oder aber auch „quasi-
gleichzeitigen“ Ausführung von Programmen in einem Betriebssystem. Unter einem Ein-
programmbetrieb versteht man, dass zu einer Zeit nur ein Programm in den Speicher
geladen und ausgeführt werden kann. Parallelverarbeitung wird in diesem Fall nicht unter-
stützt. Die alten PC-Betriebssysteme wie MS-DOS unterstützen z. B. nur Singletasking.
Diese Betriebsart ist heute, außer in einfachen Betriebssystemen (z. B. bei einfachen Em-
bedded Systems), nicht mehr üblich.
Die meisten modernen Mehrzweckbetriebssysteme wie Windows, Unix, macOS,
IBM/390, BS2000 OSD usw. unterstützen heute den Mehrprogrammbetrieb, wobei die An-
zahl der nebenläufigen Programme meist wesentlich höher als die Anzahl der vorhande-
nen CPUs ist. Auch mit einer CPU ist ein Mehrprogrammbetrieb möglich und auch üblich.
Wesentliches Merkmal ist hier, dass ein Programm zu einer Zeit auf einem Prozessor, den
das Betriebssystem zugewiesen hat, ausgeführt wird.
Im Mehrprogrammbetrieb können also mehrere Programme nebenläufig ausgeführt
werden. Die erforderlichen Betriebsmittel werden nach verschiedenen Strategien (Priori-
täten, Zeitscheibenverfahren) zugeteilt. Die Zuordnung des Prozessors nach Zeitinterval-
len  an die nebenläufigen Programme wird als Timesharing bezeichnet.
Einprozessorsysteme verwalten genau einen Prozessor (CPU). Die meisten Mehr -
zweckbetriebssysteme sind heute Mehrprozessorsysteme, die mehrere CPUs oder sonstige
Spezialprozessoren verwalten. Spezialprozessoren sind z. B. Prozessoren in Grafik- und
Netzwerkkarten.
2.3 Klassische Großrechnerbetriebsarten

### Seite 48

36
2.3.2  Batchverarbeitung und interaktive Verarbeitung
Im Stapelbetrieb, auch Batchprocessing genannt (Unterscheidung nach der zeitlichen Ab-
wicklung), werden die Aufträge (Jobs) an das Betriebssystem zunächst in eine Warte-
schlange des Betriebssystems eingetragen und dann z.  B. unter Berücksichtigung von
Prioritäten oder der Reihe nach abgearbeitet. Insbesondere in Mainframe-Anwendungen
ist der Stapelbetrieb z. B. für Abrechnungs- oder Buchungsläufe immer noch weit verbrei-
tet. Dagegen wird bei der Dialogverarbeitung eine Kommunikation des Benutzers mit dem
System ermöglicht. Der Auftrag an das System muss zum Startzeitpunkt nicht vollständig
formuliert sein, sondern wird sozusagen im Dialog ergänzt.
2.3.3  Teilnehmerbetrieb
Im Hinblick auf die Programmnutzungsart unterscheidet man Teilhaber- und Teilnehmer-
betrieb, wobei der Teilhaberbetrieb in der Regel eine Systemsoftware mit der Bezeich-
nung Transaktionsmonitor benötigt. Die Unterscheidung ist auf den ersten Blick nicht
ganz einleuchtend und soll daher erläutert werden.
Die ursprünglich typische Nutzungsart von Online-Systemen, die von Benutzern über
eine Dialogschnittstelle verwendet werden konnten, war der Teilnehmerbetrieb. Im Teil-
nehmerbetrieb erhält jeder Anwender seinen eigenen Benutzerprozess5 sowie weitere Be-
triebsmittel vom Betriebssystem zugeteilt. Der Benutzer meldet sich über einen Login-
Dialog beim System an und bekommt die Betriebsmittel dediziert zugeordnet. Dies ist
auch heute noch die übliche V orgehensweise in modernen Betriebssystemen. Unter Unix
und Windows arbeitet man üblicherweise nach dem Login-V organg im Teilnehmerbetrieb.
Größere Anwendungen, die viele Benutzer unterstützen, sind aber durch eine dedizierte
Betriebsmittelzuweisung nicht besonders leistungsfähig. Wenn z. B. 100 oder mehr Be-
nutzer gleichzeitig ein Buchhaltungssystem verwenden, dann muss das Betriebssystem im
Teilnehmerbetrieb jedem Benutzer einen Prozess zuordnen (siehe Abb.  2.10). Das Pro-
gramm wird jedes Mal neu gestartet, und das System muss sehr viel Leistung erbringen,
obwohl es vielleicht gar nicht sein müsste. Diese klassischen betrieblichen Informations-
systeme wie Buchhaltungs-, Auftrags- oder Kundenverwaltungssysteme haben nämlich
meistens nur kurze Dialogschritte zu bearbeiten. Die meiste Zeit sitzt der Anwender vor
seinem Bildschirm und denkt. Der zugeordnete Prozess muss sehr wenig tun, belegt aber
viele Betriebsmittel. Hinzu kommt, dass derartige Anwendungen in der Regel auch Daten-
banken benötigen. Wenn viele Prozesse Verbindungen zu einer Datenbank unterhalten
müssen, reduziert dies die Leistungsfähigkeit eines Systems enorm.
5 Ein Prozess stellt im Betriebssystem eine Ablaufumgebung für ein Programm bereit. Wir werden
diesen Begriff noch ausführlich erläutern.
2 Betriebssystemarchitekturen und Betriebsarten

### Seite 49

37
2.3.4  Teilhaberbetrieb
Gewissermaßen zur Optimierung dieser Anwendungen wurde der Teilhaberbetrieb erfun-
den. Im Teilhaberbetrieb werden Prozesse und Betriebsmittel über einen Transaktionsmo-
nitor zugeteilt (Abb.  2.11). Dies ist möglich, da die Benutzer aus Sicht des Betriebssys-
tems die meiste Zeit „denken“, bevor eine Eingabe in das System erfolgt. Die Betriebsart
Teilhaberbetrieb ist ideal für dialogorientierte Programme mit vielen parallel arbeitenden
Anwendern, die meistens kurze und schnelle Transaktionen ausführen, wie dies etwa bei
einem Buchungssystem für Flugbuchungen der Fall ist. Unter einer Transaktion wird hier-
bei ein atomar auszuführender Service verstanden, der entweder ganz oder gar nicht aus-
geführt wird. Werden innerhalb der Ausführung einer Transaktion mehrere Operationen
etwa auf einer Datenbank erforderlich, so darf dies nur in einem Stück erfolgen. 6 Das
Transaktionskonzept ist für betriebliche Informationssysteme ein sehr wichtiges Konzept,
das bei der Entwicklung fehlertoleranter Anwendungssysteme unterstützt.
Ein Transaktionsmonitor ist ein sehr komplexes Dienstprogramm, das oberhalb des
Kernels angesiedelt ist und viele Aufgaben wie die Zugangskontrolle, die Verteilung der
Anfragen auf bereitgestellte Prozesse und die Optimierung der Zugriffe sowie die Verwal-
tung der Ressourcen und auch die Zuordnung von Datenbankverbindungen übernimmt.
Transaktionsmonitore kommen ursprünglich aus der Mainframe-Welt, sind aber heute
auch in Unix- und Windows-Umgebungen stark verbreitet.7 Bei der Programmierung einer
Transaktionsanwendung geht man etwas anders vor als bei der klassischen Programmie-
rung. Man hängt in der Regel seine Programme, auch Transaktionsprogramme genannt, in
6 Klassische Transaktionen müssen verschiedene Korrektheitskriterien erfüllen, die auch mit dem
Akronym ACID (Atomarity, Consistency, Isolation und Durability) umschrieben werden.
7 Beispiele für Transaktionsmonitore sind IBM CICS, IBM IMS, Fujitsu OpenUTM (früher von
Siemens), Oracle BEA Tuxedo und IBM Encina (früher von Transarc).
U1 U2 U3 Un
Datenhaltung (Datenbanken)
P1 P2 P3 Pn
Ux
Betriebssystem
Px
Prozess mit
geladenem
Programm
User Interface
Zugang
...
...
Datenbankverbindungen
Abb. 2.10 Teilnehmerbetrieb
2.3 Klassische Großrechnerbetriebsarten

### Seite 50

38
den Transaktionsmonitor ein, der die eigentliche Steuerung übernimmt. Transaktionsmo-
nitore stellen also die Ablaufumgebung für die Transaktionsanwendungen bereit. Der Auf-
ruf eines Transaktionsprogramms erfolgt über die Angabe eines Transaktionscodes (TAC),
der die Programmteile adressiert.
In Abb.  2.12 ist ein vereinfachter Ablauf des Aufrufs eines Transaktionsprogramms
dargestellt. Das Transaktionsprogramm läuft in der Umgebung des Transaktionsmonitors.
Über einen TAC erfolgt die Adressierung. Ein Dispatcher (Verteiler) teilt benötigte Res-
sourcen wie z. B. einen Prozess zu und gibt den Aufruf samt seiner Input-Daten an das
Transaktionsprogramm weiter. Meist werden Daten aus Datenbanken gelesen, verarbeitet
und ggf. verändert. Nach der Bearbeitung werden die Ergebnisse für die Ausgabe auf dem
Terminal aufbereitet und an das Terminal gesendet.
2.4  Terminalserver-Betrieb
Ein Terminalserver verwaltet Terminals bzw. Client-Arbeitsplätze. Sinn und Zweck von
Terminalserver-Systemen ist es, die Administration verteilter Komponenten zu vereinfa-
chen und besser kontrollieren zu können. Eine zentrale Serverlandschaft, die aus großen
Serverfarmen bestehen kann, bedient „dumme“ Clientrechner (sog. Thin Clients), wobei
die Anwendungsprogramme vollständig in den Servern ablaufen und die Clientrechner
nur noch für Zwecke der Präsentation eingesetzt werden. Die Idee hinter Terminaldiensten
ist die Zentralisierung von Betriebsmitteln, um die beteiligten Systeme leichter adminis-
trieren zu können. Dies kann als Gegenbewegung zur starken Verteilung der Systeme ge-
sehen werden. Eine leistungsfähige „Terminalserverfarm“ stellt Ressourcen wie Rechen-
leistung, Hauptspeicher, Plattenspeicher usw. bereit. Der Anwender arbeitet mit der
gewohnten Benutzeroberfläche, die Anwendungen laufen aber komplett im Server ab,
U1 U2 U3 Un
Datenhaltung (Datenbanken)
P1 P2 P3 Pm
Ux
Betriebssystem
Px
Prozess durch TM
verwaltet
User Interface
Zugang über TM gesteuert
...
...
Datenbankverbindungen
Transak/g415ons-
monitor (TM)
n >> m
Abb. 2.11 Teilhaberbetrieb
2 Betriebssystemarchitekturen und Betriebsarten

*... weitere 315 Seiten nicht angezeigt*
