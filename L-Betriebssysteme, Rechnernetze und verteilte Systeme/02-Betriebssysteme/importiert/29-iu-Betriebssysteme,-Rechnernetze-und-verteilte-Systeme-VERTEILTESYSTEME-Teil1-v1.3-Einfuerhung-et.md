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
quelle: "29-iu-Betriebssysteme, Rechnernetze und verteilte Systeme-VERTEILTESYSTEME-Teil1-v1.3 - Einfuerhung et al.pdf"
seiten: 48
---

# Betriebssysteme, Rechnernetze und verteilte Systeme

> [!info] Dokumentinformationen
> - **Quelle:** 29-iu-Betriebssysteme, Rechnernetze und verteilte Systeme-VERTEILTESYSTEME-Teil1-v1.3 - Einfuerhung et al.pdf
> - **Typ:** sonstig
> - **Bereich:** BS
> - **Seiten:** 48
> - **Autor:** Andreas Hümmer

---

## Inhalt

### Seite 1

Betriebssysteme,
Rechnernetze und
verteilte Systeme
Sommersemester 2026
Andreas Hümmer
V 1.3
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE

### Seite 2

Verteilte Systeme
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme

### Seite 3

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
Was betrachten wir hier?
Hardware
BIOS/UEFI
Betriebssystem
Benutzersoftware
Netzwerk

### Seite 4

Verteilte Systeme
Definitionen und Überblick
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme

### Seite 5

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
Verteilte Systeme
Verteilte Systeme sind eine Sammlung von unabhängigen
Computern, die sich gegenüber dem Anwender als ein
kohärentes System darstellen. [Tanenbaum]
Ein verteiltes Computersystem besteht aus mehreren
autonomen Prozessoren, die sich keinen Hauptspeicher teilen
aber, mittels Austausch von Nachrichten über ein Netzwerk,
miteinander Kooperieren. [Bal]
Ein verteiltes System ist es, wenn ein Fehler eines Computers,
von dessen Existenz Du nichts wusstest, deinen eigenen
Rechner unbrauchbar macht.[Lamport]

### Seite 6

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
Multithreading, -tasking, -processing
Multithreadding Multitasking Multiprocessing
Quasi-gleichzeitiges
Abarbeiten mehrere
Thread des selben
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
Ausführungsz
eit
Ausführungsz
eit
Nebenläufig
(concurrent)
Parall
el

### Seite 7

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
Abgrenzung des Themas
CPU
Speicher
CPU
Speicher
CPU
Speicher
CPU
Speicher
Distributed
Computing
CPU
Speicher
CPU CPU
Multiprocessi
ng
CPU
Speicher
CPU
Speicher
CPU
Speicher
Shared Storage
Parallel
Computing

### Seite 8

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
Definitionen
 Teilnehmer in einem verteilten System werden als Nodes
bezeichnet
 Die teilnehmenden Nodes sind miteinander vernetzt
 Nodes in einem verteilten System kommunizieren
miteinander, dies kann auf unterschiedliche Weise erfolgen
 In einem verteilten System müssen Prozessor, Speicher und
Kommunikation gemeinsam betrachtet werden
 Auch und insbesondere kann es in verteilten Systemen zu
Konflikten oder kritischen Abschnitten kommen, die eine
sorgfältige Synchronisation erfordern
 Eine Transaktionsverwaltung muss die Konsistenz der
Daten garantieren
 Einhergehend mit der Transaktionsverwaltung muss auch
die Persistenz der (flüchtigen) Daten sicher gestellt sein

### Seite 9

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
Definitionen II
 Der Service, der durch ein verteiltes System bereit gestellt
wird verbirgt die Komplexität gegenüber dem Benutzer
 Es erscheint als würde der Dienst von „einem“ System
erbracht, unabhängig davon wie viele Systeme tatsächlich
involviert sind

### Seite 10

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
Nodes
 Jeder Node in einem verteilten System kann eigenständig
agieren
 Autonomie
 Ein Node ist umgangssprachlich ein Synonym für Computer,
Prozess, Prozessor
 Ein Node kann ein vollwertiges System mit eigenem
Betriebssystem sein
 Ein Teil eines Systems sein (z.B.: Mehrprozessorsystem)

### Seite 11

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
Abgeleitete Merkmale eines verteilten Systems
 Skalierbarkeit
 Ein verteiltes System kann (beliebig) mit zusätzlichen Ressourcen
erweitert werden, wobei die Art der Ressourcen sehr heterogen sein
kann
 Nebenläufigkeit
 Auf Basis von Synchronisationsalgorithmen können Teilaufgaben
koordiniert auf verschiedenen Systemen parallel abgearbeitet
werden
 Fehlertoleranz
 Resilienz ist ein zwingendes Grundprinzip für verteilte Systeme, da
aufgrund der Verteilung und der hierbei eingesetzten
umfangreichen Kommunikation häufig Fehler auftreten können
 Transparenz
 Für den Benutzer ist nicht ersichtlich, wie die Aufgaben auf die
Ressourcen verteilt werden und wo sich diese befinden

### Seite 12

Verteilte Systeme
Skalierung und Betriebsmodi
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme

### Seite 13

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
Skalierbarkeit und Verteilung
 Horizontal
 Vertikal
••• ••• ••• ••• •••…
horizontale
Verteilung
(gleiche Aufgaben)
horizontale
Skalierung
(mehr Server)
•••
•••
•••vertikale
Verteilung
(verschieden
e
Aufgaben)
•••
vertikale Skalierung
(mehr Leistung pro
Server)

### Seite 14

Client/Server (2-Tier)                                                           Multitier
Client und Server sind Rollen-Bezeichnungen
 Beispiel: Ein Server kann als Druckserver agieren, kann gleichzeitig
aber auch Client eines Dateiservers sein.
Server
Client
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
Client / Server und Multitier Modell
Server
Client
Server
Client
P
C
Webserv
er
P
C
Webserv
er
DB-
Server
Client
Client

### Seite 15

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
Fat vs Thin-Clients
Thin-Client                                                                            Fat-Client
•••
Darstellu
ng
Logi
k
Date
n
•••
Darstellu
ng
Logi
k
Date
n
•••

### Seite 16

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
Verteiltes System auf Client/Server Basis
•••
(Thin)
Clients
Anwendungs-
Server
Datenbank-
Server
•••
Redundanz,
Lastverteilung
Aufgabenverteil
ung
Kapselung

### Seite 17

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
Cloud Computing
 On Demand Bereitstellung von Rechenleistung, Speicher und
Diensten über das Internet
 Nutzungsbasierte Abrechnung -> Kostenkotrolle notwendig!!
 Typische Service Modelle:
IaaS
Infrastructure as a
Service
PaaS
Plattform as a Service
SaaS
Software as a Service
Mehr Kontrolle                        IT Ressourcen                            weniger
Kontrolle

### Seite 18

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
Cloud Computing
Bild:
Gartner/Checkpoint

### Seite 19

Verteilte Systeme
Kommunikation und Synchronisation
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme

### Seite 20

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
Transaktionen, Persistenz, Konsistenz
Persistenz und Konsistenz in verteilten System werden erfüllt, wenn die Transaktion
den ACID-Eigenschaften genügt:
 Atomicity (Atomarität): Diese Eigenschaft garantiert, dass eine Transaktion mit per
sistenten Daten immer entweder vollständig oder ohne jegliche Auswirkung ist, da
das System im Fehlerfall in einen vor der Transaktion gesicherten Zustand
zurückgesetzt werden kann.
 Consistency (Konsistenz): Diese Eigenschaft stellt sicher, dass sich die Daten für
einen Beobachter immer in einem gültigen Zustand befinden, so dass nie
irgendwelche Zwischenzustände nach außen hin sichtbar werden.
 Isolation (Isolierung): Diese Eigenschaft verhindert, dass sich verschiedene, aber
gleichzeitige Zugriffe durch ihre Überlappung gegenseitig beeinflussen – was
insbesondere bedeutet, dass Schreibzugriffe serialisiert werden müssen.
 Durability (Dauerhaftigkeit): Diese letzte der vier Eigenschaften besagt schließlich,
dass die effektiv vorgenommenen Änderungen an den Daten auch bei
Systemausfällen weiterhin Bestand haben.

### Seite 21

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
Synchronisation
Verteile System arbeiten im allgemeinen nebenläufig, wodurch eine Synchronisation
der vereitelten Prozesse notwendig ist. Die Methoden, die hierfür angewandt werden
sind:
 Mutex/Semaphore:
Ein Verfahren zum gegenseitigen Ausschluss von konkurrierenden Speicherzugriffen
nebenläufiger Prozesse. (Mutex erlaubt nur einen Zugriff, Semaphore erlaubt eine
bestimmte Anzahl gleichzeitiger Zugriffe.)
 Token-Passing:
Sogenannte Freitoken werden im Netz von Teilnehmer zu Teilnehmer weitergereicht.
Der Teilnehmer, der Daten senden möchte, reserviert sich einen solchen Token und
hängt seine Daten an.
 Barrier:
Die beteiligten Prozesse werden so lange blockiert, bis von allen Teilnehmern die
erforderliche Synchronisationsnachricht gesendet wurde. (Nachteil: Es können
Deadlocks entstehen, die wiederum durch Timeouts beendet werden müssen.)

### Seite 22

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
Kommunikation: Nachrichtenaustausch
 Nodes kommunizieren direkt miteinander
 Nachricht (Message)
 Kommt von einem (einzelnen) Sender
 Ist bestimmt für einen (einzelnen) Empfänger
 Ist ein Paket (klar begrenzt)
 Alternative: Datenstrom
 Kontinuierlicher Fluss von Daten (ohne
Nachrichtengrenzen)
 Vom Sender zum Empfänger
 Die Kommunikation (Paket oder Datenstrom) kann
unidirektional oder bidirektional sein.

### Seite 23

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
Kommunikation: Nachrichtenaustausch
 Was kann schief gehen?
 Nachricht geht verloren
 Wird unterwegs verändert
 Reihenfolge der Nachrichten stimmt nicht
 Übermittlung dauert zu lange
 Teilnehmer
 Unicast: 1 Sender, 1 Empfänger
 Broadcast: 1 Sender, alle bekannten Empfänger
 Multicast: 1 Sender, ausgewählte Gruppe an Empfängern
 Convergecast: mehrere Sender, 1 Empfänger
(Sensornetze, Torrent)

### Seite 24

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
Kommunikation: Shared Storage
 Nodes kommunizieren nicht direkt, sondern über einen
geteilten Speicher (shared storage)
 Fragen:
 Ist es ein zentraler Speicher oder ein verteilter Speicher?
 Wie soll sich dieser Speicher bei gleichzeitigem Zugriff
verhalten?
-> Synchronisierung erforderlich
 Verteiltes Speichern
 Replikation: Kopie der Daten auf verschiedenen Knoten –
Redundanz
 Partitionierung: Aufteilung der Daten in Teilmenge und
Speichern der Teilmengen auf unterschiedlichen Knoten

### Seite 25

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
Kommunikations API
Low Level, Beispiel Sockets
 Geeignet für Nachrichten und Streams
 Folgt dem Unix-Prinzip: Alles ist eine Datei
 Komplexe API, erlaubt aber volle Kontrolle über alle Details
 Für Interoperabilität mit anderen (Arten) von Systemen:
Serialisierung z.B. über XML, JSON…
 High Level, Beispiel HTTP/RCP/REST
 Siehe nachfolgende Slides

### Seite 26

Verteilte Systeme
Das HTTP Protokoll
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme

### Seite 27

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
HTTP & WWW
 Webserver stellen Webseiten bereit
 Diese werden  mittels Uniform Ressource Locator (URI)
identifiziert
 Die Seiten sind mit Hypertext Markup Language (HTML)
formatiert
 Webbrowser requesten Seiten von Servern
 Server und Browser kommunizieren mittels Hypertext
Transfer Protocol (HTTP)
 HTTP/1.1: RFC 7230-7235
Entschuldigung für das DENGLISCH. Für einige
Bezeichnungen macht es keinen Sinn diese in Deutsche
zu übersetzen

### Seite 28

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
Das HTTP Protokoll
 Request Primitiven:
 GET: Erhalte den Inhalt einer URL
 HEAD: Vergleichbar mit GET, stellt aber nur
Metadaten bereit
 POST: Stellt eine URL zur Verfügung die mit einem
Programm korrespondiert, welches die Daten
akzeptieren kann die via POST Nachricht übermittelt
werden
 PUT: Stellt eine URL bereit in der die Daten die via
PUT übermittelt wurden gespeichert werden soll
 …DELETE, TRACE, OPTIONS, …
 Reply: Liefert eine Seite zurück, plus Fehlercode, Staus
 REDIRECT: Beispiel für eine Fehlercode, der dem
Browser mitteilt die zurück gelieferte URL zu
verwenden anstelle der aufgerufenen.
Comput
er
Webserv
er
Mobil
e
http requesthttp reply
http
request
http
reply

### Seite 29

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
Das HTTP Protokoll
Clien
t
Webserv
er
http
request
http
reply
HTT
P
GET
POST
PUTDELET
E
JSO
N
Bild/Beispiel:
O°Reilly

### Seite 30

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
Request: Statischer und dynamischer Inhalt
GET Requests können auf eine statische Webseite oder auf die Ausführung
eines Programmes referenzieren
 Der Server kann einfache Modifikationen der Seite vornehmen (z.B.
SSI – Server Side Include)
 Der Server kann die Antwort auf den Request aufgrund der
Parameter im Request berechnen
 Typisch: „?“ als indikator das ein key=value Paar existiert. Diese Paare
werden mittels „&“ separiert
Beispiel GET: http://nowhere.org/path/elsewhere/somewhere?key=rust&param=blue
Vergleich HTTP: https://tools.ieft.org/html/tfc7321#section-4.3.1
 Konvention: GET verändert den Zustand der Ressource NICHT
POST Request verweisen auf eine Programmausführung, wobei POST die
Parameter für dieses Programm liefert.
 POST ändert für gewöhnlich den Zustand.
 Die Ausgabe des Programms wird als gerenderte Seite an den Client
zurück geliefert.
 Die key=value Paare werden bei POST im Nachrichtenrumpf
übermittelt

### Seite 31

Verteilte Systeme
Typische APIs und Anwendungen
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme

### Seite 32

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
REST API
REST – Representational State Transfer
[Roy Fieldings 1996]
Eine REST API wird z.B. angesprochen, wenn ein Client eine
GET, POST, etc. Anfrage an einen Webserver stellt.
REST-Paradigmen:
 Client/Server
 Zustandslosigkeit
 Caching
 Einheitliche Schnittstelle
 Mehrschichtige Systeme
 Code-on-Demand (optional)

### Seite 33

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
SOAP
SOAP – Simple Object Access Protocol
oder Simple Object Architecture Protocol
SOAP dient als Protokoll zum Austausch XML basierter
Datensätze über ein Rechnernetzwerk
<?xml version="1.0"?>
<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-
envelope">
<s:Header>
</s:Header>
<s:Body>
</s:Body>
</s:Envelope> https://www.w3.org/TR/soap12-pa
rt1/

### Seite 34

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
REST/SOAP - Unterschiede
 SOAP ist ein Protokoll, REST ein Designstil
 REST ist Leistungsfähiger, da es weniger Bandbreiten und
Ressourcen benötigt
 SOAP erfordert eine engere Bindung zwischen Client und
Server
 REST bietet eine klarere Client/Server Trennung als SOAP
 REST Aufrufe können zwischengespeichert werden
 SOAP gilt als sicherer
https://www.redhat.com/de/topics/integration/whats-the-differ
ence-between-soap-rest

### Seite 35

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
RPC – RFC 707, 1057, 5531
RPC – Remote Procedure Call
RPC ist eine Generalisierung von z.B. REST Aufrufen. Es existieren viele individuelle
Implementationen
Ein Client schickt eine Nachricht (ggf. zusammen mit Parametern) an einen Server,
worauf hin der Server ein Programm startet und die Ausgaben dieses Programms
an den Client zurück liefert.
ACHTUNG: RPC Aufrufe können
blockierend sein!
Beispiele: HTTP-Get,
HTTP-POST, Java: RMI
(Remopte Method
Invocation), SAP: RFC
(Remote Function Call)
Praxis: Windows RPC
Dienst (Port 135/tcp),
Unix Portmapper (Port
111/tcp)
Schema:
Microsoft

### Seite 36

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
SOA
SOA: Service Oriented Architecture
 Die Dienste, die ein Server bereit stellt werden
nicht „nur“ angeboten; der Server veröffentlicht
das er diese Dienste anbietet etwa in einem
Verzeichnisdienst.
 SOA selbst ist ein Organisationskonzept, welches
auf Wiederverwendung von Code, größere
Flexibilität, Skalierbarkeit, höhere Zuverlässigkeit
und Verfügbarkeit zielt.
 Eine praktische Implementierung findet sich  z.B.
im Microservice-Paradigma
Beispiel: Active Directory Service Location Records:
SRV _http._tcp.abc.com. IN SRV 0 5 80 ws1.abc.com. Maps a
service to a
particular  server
Comput
er
Director
y
service
request
service
reply
Servie
lookup
repl
y
Service
Provider

### Seite 37

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
HTTP - Entwicklung
+ keep alive
+ pipelinng
+ streams
+ compressed
header
+push
+ basiert auf
UDP streams

### Seite 38

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
HTTP/ 1
Übersicht/Bilder aus https://www.youtube.com/@ByteB
yteGo

### Seite 39

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
HTTP/ 1.1
Übersicht/Bilder aus https://www.youtube.com/@ByteB
yteGo
Keep
alive
Pipelini
ng

### Seite 40

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
HTTP/ 2
Übersicht/Bilder aus https://www.youtube.com/@ByteB
yteGo
Strea
ms
Pus
h

### Seite 41

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
HTTP/ 3 - QUIC
Speziell für Mobilgeräte, da
Verbindungen
Bei Netzwerk/Adresswechseln erhalten
bleiben
Übersicht/Bilder aus https://www.youtube.com/@ByteB
yteGo

### Seite 42

Verteilte Systeme
Mobile Computing
iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme

### Seite 43

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
Mobile Computing
 Standortwechsel (teilweise sehr schnell)
 Häufige Neukonfigurationen des Netzwerkes
 Geringere Verfügbarkeit im Vergleich zu kabelgebundenen
Netzen
 Leichteres Abhören (Wiretapping) im Vergleich zu
kabelgebundenen Netzwerken
 Etablierung neuer Benutzerschnittstellen
 Das Mobilgerät kommuniziert mit anderen mobilen oder
stationären Geräten
 Mobile Datenübertragung setzt ein Funknetz voraus und
ist Standortunabhängig

### Seite 44

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
Kommunikationsanforderungen
 Es kann zu Verbindungsunterbrechungen kommen
 Es kann zu Abkopplungen kommen
 Ziel: Für den Benutzer soll die Kommunikation auch bei
Unterbrechung fehlerfrei weiter bestehen.
 Auf technischer Ebene sind Korrektur und
Kompensationsmaßnahmen nötig
 Fehlerkorrektur/Retransmission auf Protokollebene (TCP)
 Einsatz von Stellvertreter-Systemen (Proxies)
 Einsatz von resilienten VPN Verbindungen
 Einsatz von speziellen Protokollen (HTTP / 3)

### Seite 45

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
Standortbestimmung
Wie kann der Standort eines mobilen Gerätes bestimmt werden?
 GNSS (Global Navigation Satellite System)
 GPS (USA, 31 operative Satelliten)
 GLONASS (GUS, 22 operative Satelliten)
 GALILEO (EU, 22 operative Satelliten)
 BEIDU (VRC)
Genauigkeit zivil: ca. 2-15 m
Bei Verwendung von Referenzstationen ca. 4cm (Funk) oder
bei EGNOS ca. 1-3m
 WLAN-Ortungsdienst (WiFi Positioning Service)
 Funkzellen Erfassung/Triangulation

### Seite 46

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
Reichweite von Funknetzen
 Große Reichweite (WAN)
 Zelluläre Netze, wie GSM, UMTS, LTE, 5G – ca. 2-35km
 Richtfunk (Punkt-zu-Punkt) – „line of sight“
 Satellitenfunk – global, abh. von der Satellitenabdeckung
 Mittlere Reichweite (MAN)
 LPWAN – Low Power Wide Area Network
 LoRaWAN – Long Range Wide Area Network
 Geringe Reichweite (LAN)
 WLAN/WiFi – bis zu 50m
 DECT – 50-300 m
 Kurzreichweite (PAN)
 Bluetooth (802.15)
 NFC – Near Field Communication

### Seite 47

iu © 2025 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte
Systeme
Kanalaufteilung im Funkbereich
 Mehrere Kanäle teilen sich bei Funknetzen den selben Funkbereich
(Frequenzband). Wie können mehrere Kanäle realisiert werden?
 Frequenz-Multiplexing (FDMA)
 Die Teilnehmer nutzen für ihr Funksignal verschiedene Frequenzen
 Raum-Multiplexing (SDMA)
 Die Sendebereiche werden in räumliche Zellen mit unterschiedlichen
Frequenzen unterteilt, so dass möglichst wenige Überlappungen
entstehen. Ist räumlich keine Überlappung möglich kann die gleiche
Frequenz verwendet werden
 Zeit-Multiplexing (TDMA)
 Jeder Teilnehmer bekommt Sendezeit (Zeitslots) zugewiesen, in der er
kommunizieren darf

### Seite 48

iu © 2023 Andreas Hümmer iu INTERNATIONALE
HOCHSCHULE
Betriebssysteme, Rechnernetze und verteilte
Systeme
Verteilte Systeme –
Praxisteil
Praxis
 Konstruktion eines verteilten Systems auf dem Papier
 Ggf. Vertiefung und „Simulation“ in der HA
 Simulationen mit dem GNS3
