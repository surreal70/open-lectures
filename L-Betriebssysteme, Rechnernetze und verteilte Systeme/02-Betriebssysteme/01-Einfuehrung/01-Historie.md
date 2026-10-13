---
author: Andreas Hümmer
title: Historie der Betriebssysteme
tags:
  - content
  - bs
  - historie
  - einfuehrung
  - generationen
created: '2026-10-07'
modified: '2026-10-07'
bereich: BS
---

# Historie der Betriebssysteme

## Überblick

Die Geschichte der Betriebssysteme ist eng mit der Entwicklung der Computer-Hardware verbunden. Von den ersten Röhrenrechnern der 1940er Jahre bis zu modernen verteilten Systemen zeigt die Evolution, wie sich die Anforderungen an Software zur Hardware-Abstraktion und Ressourcenverwaltung stetig verändert haben.

> [!info] **Lernziele**
> - Die historische Entwicklung von Betriebssystemen kennen
> - Die vier Generationen von Computern und deren BS-Charakteristika verstehen
> - Wichtige Meilensteine und Pioniere der Informatik benennen können
> - Den Zusammenhang zwischen Hardware-Entwicklung und BS-Entwicklung erkennen

---

## Vorgeschichte: Die Industrielle Revolution

Die Wurzeln der Datenverarbeitung reichen bis in die Industrielle Revolution zurück.

![[industrielle-revolution.jpg]]
*02-01-01-industrielle-revolution: Fabrikhalle im 19. Jahrhundert - Beginn der Automatisierung*

### Frühe Programmierkonzepte

![[jacquard-webstuhl-lochkarten.jpg]]
*02-01-01-jacquard-webstuhl-lochkarten: Jacquard-Webstuhl (1805) - Lochkarten zur Mustersteuerung*

Der Jacquard-Webstuhl nutzte bereits Lochkarten zur Programmierung von Webmustern - ein Konzept, das später für Computer übernommen wurde.

### Charles Babbage's Vision

![[babbage-analytical-engine.jpg]]
*02-01-01-babbage-analytical-engine: Modell der Analytical Engine von Charles Babbage*

Charles Babbage entwarf um 1837 die **Analytical Engine** - einen mechanischen Universalrechner mit:
- Rechenwerk ("Mill")
- Speicher ("Store") 
- Ein-/Ausgabe über Lochkarten
- Bedingte Verzweigungen

Ada Lovelace schrieb das erste Programm für diese (nie gebaute) Maschine.

---

## Die vier Generationen

### 1. Generation (1940-1955): Röhren und Steckverbindungen

**Charakteristika:**
- Keine Betriebssysteme im eigentlichen Sinne
- Direkte Maschinenprogrammierung über Steckbretter und später Lochkarten
- Ein Programm = Ein Benutzer = Eine Aufgabe
- Enormer Raumbedarf und hoher Stromverbrauch

#### Hollerith und die Lochkarten

> [!info] Herman Hollerith (1860-1929)
> Deutsch-amerikanischer Statistiker und Erfinder, der die elektromechanische Tabelliermaschine für Lochkarten entwickelte. Seine Erfindung markiert den Beginn der Ära mechanisierter Datenverarbeitung.
/media/andhue/Wissen/open-lectures/Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/01-Einfuehrung/.assets/hollerith-tabelliermaschine.jpg


![[hollerith-tabelliermaschine.jpg]]
*02-01-01-hollerith-tabelliermaschine: Hollerith-Tabelliermaschine (ca. 1890) - Quelle: [Computer History Museum](https://www.computerhistory.org)*

![[hollerith-lochkarte.jpg]]
*02-01-01-hollerith-lochkarte: Hollerith-Lochkarte - Datenträger für die US-Volkszählung 1890*

**Die US-Volkszählung 1890:**

Nach der Volkszählung 1880 sammelte das US Census Bureau mehr Daten als es verarbeiten konnte. 1888 wurde ein Wettbewerb ausgeschrieben, um eine effizientere Methode zu finden:

| Teilnehmer | Datenerfassung | Aufbereitung |
|------------|----------------|--------------|
| Teilnehmer 1 | 144,5 Stunden | 44,5 Stunden |
| Teilnehmer 2 | 100,5 Stunden | 55,5 Stunden |
| **Herman Hollerith** | **72,5 Stunden** | **5,5 Stunden** |

Holleriths System war revolutionär schnell und gewann den Auftrag für die Volkszählung 1890.

**Komponenten des Hollerith-Systems:**
- **Pantograph**: Zum Stanzen der Lochkarten (ca. 500 Karten/Tag)
- **Kartenleser**: Federbetätigte Metallstifte durchdringen die Löcher und tauchen in Quecksilber ein, wodurch elektrische Schaltkreise geschlossen werden
- **Zähldials**: 40 Zifferblätter für verschiedene Datenkategorien (Alter, Geschlecht, etc.)
- **Sortiertisch**: Zur Ablage der gelesenen Karten

Ein erfahrener Bediener konnte **80 Lochkarten pro Minute** verarbeiten.

**Holleriths Vermächtnis:**
1896 gründete Hollerith die *Tabulating Machine Company*, die 1911 mit anderen Firmen zur *Computing-Tabulating-Recording Company (CTR)* fusionierte. 1924 wurde diese in **International Business Machines (IBM)** umbenannt.

> [!tip] Weiterführende Links
> - [The Hollerith Machine - U.S. Census Bureau](https://www.census.gov/about/history/bureau-history/census-innovations/technology/hollerith-machine.html)
> - [Herman Hollerith - Wikipedia](https://en.wikipedia.org/wiki/Herman_Hollerith)
> - [Tabulating Machine - Wikipedia](https://en.wikipedia.org/wiki/Tabulating_machine)
> - [IBM History: The Punched Card Tabulator](https://www.ibm.com/history/punched-card-tabulator)
> - [Smithsonian: From Herman Hollerith to IBM](https://americanhistory.si.edu/collections/object-groups/tabulating-equipment/from-herman-hollerith-to-ibm)
> - [Library of Congress: Hollerith's Electric Tabulating Machine](https://www.loc.gov/resource/mcc.023/)

#### Erste Computer

Die 1940er Jahre markierten den Beginn der eigentlichen Computerära. Mehrere bahnbrechende Maschinen entstanden, oft unabhängig voneinander und unter dem Druck des Zweiten Weltkriegs.

---

##### Zuse Z3 (1941) - Der erste programmierbare Computer

> [!info] Konrad Zuse (1910-1995)
> Deutscher Bauingenieur und Computerpionier. Er baute den Z3 in der Wohnung seiner Eltern in Berlin - ohne Kenntnis von parallelen Entwicklungen in anderen Ländern.

![[zuse-z3-deutsches-museum.jpg]]
*02-01-01-zuse-z3-deutsches-museum: Nachbau der Zuse Z3 im Deutschen Museum München - Quelle: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Z3_Deutsches_Museum.JPG), Lizenz: CC BY-SA 3.0*

Die Z3 war der weltweit erste funktionierende, programmierbare, vollautomatische digitale Computer.

**Technische Daten:**

| Eigenschaft | Wert |
|-------------|------|
| Fertigstellung | 12. Mai 1941 |
| Technologie | 2.600 elektromechanische Relais |
| Taktfrequenz | 5-10 Hz |
| Wortlänge | 22 Bit (Gleitkomma) |
| Speicher | 64 Worte |
| Programmierung | Lochstreifen aus Zelluloid |
| Gewicht | ca. 1 Tonne |
| Leistungsaufnahme | ca. 4.000 Watt |
| Kosten | ca. 50.000 Reichsmark |

**Schicksal:** Die Original-Z3 wurde am 21. Dezember 1943 bei einem alliierten Bombenangriff auf Berlin zerstört. Ein funktionsfähiger Nachbau von 1961 ist heute im **Deutschen Museum in München** ausgestellt.

**Bedeutung:** 1998 wurde nachgewiesen, dass die Z3 prinzipiell Turing-vollständig war - sie konnte also theoretisch jede berechenbare Funktion ausführen.

> [!tip] Weiterführende Links - Zuse Z3
> - [Z3 (computer) - Wikipedia](https://en.wikipedia.org/wiki/Z3_(computer))
> - [Konrad Zuse - Wikipedia](https://en.wikipedia.org/wiki/Konrad_Zuse)
> - [Deutsches Museum - Zuse Z3](https://www.deutsches-museum.de/museumsinsel/ausstellung/informatik)
> - [Horst Zuse (Sohn) über die Z3](http://www.horst-zuse.homepage.t-online.de/z3.html)

---

##### Colossus (1943) - Der erste elektronische programmierbare Computer

![[colossus.jpg]]
*02-01-01-colossus: Colossus Mark 2 in Bletchley Park, bedient von "Wrens" (Women's Royal Naval Service) - Quelle: [The National Museum of Computing](https://www.tnmoc.org)*

> [!info] Tommy Flowers (1905-1998)
> Britischer Ingenieur der Post Office Research Station, der Colossus entwarf. Nach dem Krieg wurde seine bahnbrechende Arbeit jahrzehntelang geheim gehalten.

Colossus war der weltweit erste programmierbare, elektronische, digitale Computer. Er wurde entwickelt, um die verschlüsselten Nachrichten der deutschen Lorenz-Chiffriermaschine zu knacken.

**Historische Bedeutung:**
- Der erste Mark 2 wurde am **1. Juni 1944** fertig - gerade rechtzeitig für die Planungen zum **D-Day** (6. Juni 1944)
- Die Existenz von Colossus wurde bis Mitte der 1970er Jahre geheim gehalten
- Alle Maschinen wurden nach dem Krieg zerstört (auf Befehl Winston Churchills)
- Ein funktionsfähiger Nachbau wurde 2008 im **National Museum of Computing** in Bletchley Park fertiggestellt

**Beteiligte Personen:**
- **Tommy Flowers** - Hauptentwickler
- **Max Newman** - Mathematiker, Konzept
- **Alan Turing** - Beitrag zur Kryptoanalyse (entwarf nicht Colossus selbst, sondern die elektromechanische Bombe für Enigma)

> [!tip] Weiterführende Links - Colossus
> - [Colossus computer - Wikipedia](https://en.wikipedia.org/wiki/Colossus_computer)
> - [The National Museum of Computing - Colossus](https://www.tnmoc.org/colossus)
> - [Bletchley Park](https://bletchleypark.org.uk/)
> - [IEEE Spectrum: The Computer That Helped Win World War II](https://spectrum.ieee.org/colossus-computer-ieee-milestone)

---

##### ENIAC (1946) - Der erste elektronische Universalrechner

![[eniac.jpg]]
*02-01-01-eniac: ENIAC in der Moore School of Electrical Engineering, University of Pennsylvania - Quelle: U.S. Army Photo*

![[eniac-programmiererinnen.jpg]]
*02-01-01-eniac-programmiererinnen: ENIAC-Programmiererinnen bei der Verkabelung - Die "ENIAC Six" waren die ersten Software-Entwicklerinnen der Geschichte - Quelle: U.S. Army Photo*

> [!info] ENIAC = Electronic Numerical Integrator and Computer
> Der erste programmierbare, elektronische, universell einsetzbare Digitalcomputer. Von der Presse als "Giant Brain" (Riesengehirn) bezeichnet.

**Technische Daten:**

| Eigenschaft       | Wert                                                          |
| ----------------- | ------------------------------------------------------------- |
| Fertigstellung    | 1945, offiziell eingeweiht 15. Februar 1946                   |
| Entwickler        | John Mauchly & J. Presper Eckert (University of Pennsylvania) |
| Röhren            | 17.468 Vakuumröhren                                           |
| Gewicht           | ca. 30 Tonnen                                                 |
| Grundfläche       | ca. 167 m²                                                    |
| Leistungsaufnahme | 150 kW                                                        |
| Kosten            | $487.000 (ca. $7 Mio. in 2024)                                |
| Geschwindigkeit   | 1.000x schneller als elektromechanische Rechner               |
| Betriebsdauer     | 1945-1955 (Aberdeen Proving Ground)                           |

**Die ENIAC Six - Die ersten Programmiererinnen:**
Sechs Mathematikerinnen programmierten den ENIAC, um ballistische Flugbahnen zu berechnen:

| Name                   | Späterer Name         |
| ---------------------- | --------------------- |
| Betty Jean Jennings    | Jean Bartik           |
| Frances "Betty" Snyder | Betty Holberton       |
| Kathleen McNulty       | Kay Mauchly Antonelli |
| Marlyn Wescoff         | Marlyn Meltzer        |
| Frances Bilas          | Fran Spence           |
| Ruth Lichterman        | Ruth Teitelbaum       |

Sie wurden 1997 in die **Women in Technology International Hall of Fame** aufgenommen.

**Anwendungen:**
- Ursprünglich für Artillerie-Schusstafel-Berechnungen
- Erstes Programm: Machbarkeitsstudie für die Wasserstoffbombe
- Später: Wettervorhersagen, Zufallszahlen, Windkanal-Berechnungen

> [!tip] Weiterführende Links - ENIAC
> - [ENIAC - Wikipedia](https://en.wikipedia.org/wiki/ENIAC)
> - [Penn Today: ENIAC's Anniversary](https://penntoday.upenn.edu/news/eniacs-anniversary-nod-its-female-computers)
> - [IEEE Spectrum: The Women Behind ENIAC](https://spectrum.ieee.org/the-women-behind-eniac)
> - [Computer History Museum - ENIAC](https://www.computerhistory.org/revolution/birth-of-the-computer/4/78)
> - [Documentary: Top Secret Rosies](https://en.wikipedia.org/wiki/Top_Secret_Rosies:_The_Female_%22Computers%22_of_WWII)

---

##### Vergleich der ersten Computer

| Maschine | Jahr | Land | Technologie | Programmierbar | Turing-vollständig |
|----------|------|------|-------------|----------------|-------------------|
| **Zuse Z3** | 1941 | Deutschland | Elektromech. Relais | ✓ (Lochstreifen) | ✓ (prinzipiell) |
| **Colossus** | 1943 | Großbritannien | Röhren | ✓ (Schalter/Stecker) | ✗ (spezialzweck) |
| **ENIAC** | 1945 | USA | Röhren | ✓ (Verkabelung) | ✓ |

> [!note] Wer war "der Erste"?
> Die Frage "Wer baute den ersten Computer?" hat keine einfache Antwort:
> - **Z3** (1941): Erster *programmierbarer, vollautomatischer* Computer (elektromechanisch)
> - **Colossus** (1943): Erster *elektronischer, programmierbarer* Computer (nicht universell)
> - **ENIAC** (1945): Erster *elektronischer, universeller* Computer

---

### 2. Generation (1955-1965): Transistoren und Batch-Systeme

Die zweite Generation markierte den Übergang von Vakuumröhren zu **Transistoren** - eine Revolution, die Computer kleiner, schneller, zuverlässiger und kostengünstiger machte.

> [!info] Der Transistor
> 1947 bei Bell Labs erfunden (Bardeen, Brattain, Shockley - Nobelpreis 1956). Transistoren verbrauchen weniger Strom, erzeugen weniger Wärme und sind zuverlässiger als Röhren.

**Charakteristika:**
- **Transistoren** statt Vakuumröhren → kleinere, zuverlässigere Rechner
- Trennung von **Operatoren** und **Programmierern**
- Entstehung der **Batch-Verarbeitung** (Stapelverarbeitung)
- Erste echte Betriebssysteme (z.B. IBM IBSYS, SHARE Operating System)
- Einführung höherer Programmiersprachen (FORTRAN, COBOL)
- Magnetkernspeicher als Hauptspeicher

---

#### Übergang: Harvard Mark I (1944)

![[harvard-mark-i.jpg]]
*02-01-01-harvard-mark-i: Harvard Mark I (ASCC) - Einer der letzten elektromechanischen Großrechner, Übergang zur Computerära - Quelle: [Harvard University](https://chsi.harvard.edu)*

> [!info] Harvard Mark I (1944)
> Obwohl technisch noch zur 1. Generation gehörend (elektromechanisch), war der Mark I ein wichtiger Übergang zur modernen Computerära und wurde bis in die 1950er Jahre genutzt.

**Technische Daten:**

| Eigenschaft           | Mark 1 (1943)                     | Mark 2 (1944) |
| --------------------- | --------------------------------- | ------------- |
| Röhren (Vakuumröhren) | 1.600                             | 2.400         |
| Leistungsaufnahme     | 8,5 kW                            | 8,5 kW        |
| Geschwindigkeit       | -                                 | 5x schneller  |
| Eingabe               | Lochstreifen (5.000 Zeichen/Sek.) | Lochstreifen  |
| Anzahl gebaut         | 1                                 | 10            |

| Eigenschaft | Wert |
|-------------|------|
| Offizieller Name | IBM Automatic Sequence Controlled Calculator (ASCC) |
| Fertigstellung | 7. August 1944 |
| Entwickler | Howard Aiken (Harvard) / IBM |
| Länge | 15,5 m (51 ft) |
| Höhe | 2,4 m (8 ft) |
| Gewicht | ca. 4,5 Tonnen |
| Komponenten | 765.000 elektromechanische Teile |
| Antrieb | 50-Fuß-Antriebswelle, 5 PS Elektromotor |
| Einsatz | Ballistische Berechnungen, Manhattan-Projekt |

**Bedeutung:**
- Eines der ersten Programme: Berechnungen für die Atombombe (John von Neumann, März 1944)
- **Grace Hopper** arbeitete am Mark I und prägte den Begriff "Bug" (obwohl die berühmte Motte 1947 im Mark II gefunden wurde)
- Inspiriert von Charles Babbages Analytical Engine

> [!note] Der erste "Bug"
> Am 9. September 1947 fand Grace Hoppers Team eine echte Motte in einem Relais des Harvard Mark II. Sie klebten sie ins Logbuch mit dem Vermerk "First actual case of bug being found" - der Begriff "Debugging" war geboren (obwohl Edison den Begriff "Bug" bereits 1878 für technische Probleme verwendete).

---

#### Transistor-Mainframes: IBM 7090/7094

![[ibm-7094.jpg]]
*02-01-01-ibm-7094: IBM 7094 Konsole - Transistorisierter Großrechner der 2. Generation - Quelle: [Computer History Museum](https://www.computerhistory.org)*

Die **IBM 7090** (1959) und ihr Nachfolger **IBM 7094** (1962) waren die dominierenden wissenschaftlichen Großrechner der 2. Generation.

**Technische Daten IBM 7090/7094:**

| Eigenschaft | IBM 7090 (1959) | IBM 7094 (1962) |
|-------------|-----------------|-----------------|
| Technologie | Transistoren | Transistoren |
| Wortlänge | 36 Bit | 36 Bit |
| Speicher | 32.768 Worte | 32.768 Worte |
| Taktzykluszeit | 2,18 µs | 2,0 µs (7094 II: 1,4 µs) |
| Geschwindigkeit | ~100 KFLOPS | ~200 KFLOPS |
| Kaufpreis | $2,9 Mio. (~$23 Mio. heute) | - |
| Monatsmiete | $63.500 (~$514.000 heute) | - |

**Kulturelle Bedeutung:**
- 1961 sang ein IBM 7094 erstmals "Daisy Bell" durch Sprachsynthese - diese Szene inspirierte HAL 9000 in "2001: A Space Odyssey"
- Verwendet für NASA-Berechnungen, Wettervorhersagen, wissenschaftliche Simulationen

---

#### Batch-Verarbeitung

Die 2. Generation etablierte die **Batch-Verarbeitung** als Standard-Arbeitsweise:

![[lochkarten-sortiert.jpg]]
*02-01-01-lochkarten-sortiert: Lochkarten-Stapel sortiert in Ablagefächern - Jobs warteten oft Stunden oder Tage auf Verarbeitung*

![[papertape-archiv.jpg]]
*02-01-01-papertape-archiv: Lochstreifen-Archiv (Papertape) - Alternative zu Lochkarten für Programm- und Datenspeicherung*

**Der Batch-Workflow:**

```
┌──────────────┐    ┌─────────────┐    ┌─────────────┐
│ Programmierer│    │   Operator  │    │  Computer   │
│ schreibt     │ -> │   sammelt   │ -> │  verarbeitet│
│ auf Karten   │    │   Jobs      │    │   Batch     │
└──────────────┘    └─────────────┘    └─────────────┘
                                            │
      Stunden bis Tage Wartezeit            v
                                       ┌─────────────┐
┌──────────────┐    ┌─────────────┐    │   Drucker   │
│ Programmierer│ <- │   Operator  │ <- │   druckt    │
│ holt Output  │    │   sortiert  │    │   Ergebnis  │
└──────────────┘    └─────────────┘    └─────────────┘
```

**Vorteile:**
- Bessere Auslastung der teuren Hardware (Kosten: $1000+/Stunde)
- Automatisierte Job-Abfolge ohne manuelle Eingriffe
- Reduzierung der Rüstzeiten zwischen Jobs

**Nachteile:**
- Lange Wartezeiten für Programmierer ("Turnaround Time")
- Keine Interaktion während der Ausführung
- Ein Tippfehler → warten auf nächsten Batch-Lauf
- Fehlersuche extrem zeitaufwändig

---

#### Residente Monitore - Die Vorläufer der Betriebssysteme

> [!info] Was ist ein Resident Monitor?
> Ein **Resident Monitor** war ein kleines Programm, das permanent im Speicher verblieb ("resident") und die Ausführung von Batch-Jobs automatisierte. Er kann als direkter Vorläufer moderner Betriebssysteme betrachtet werden.

Die ersten Computer hatten **kein Betriebssystem**. Ein Operator musste jeden Job manuell einrichten: Lochkarten laden, Programm starten, Ergebnis abholen. Dies war extrem ineffizient bei teuren Maschinen, die $1000+ pro Stunde kosteten.

**Die Lösung: Monitor-Programme**

1953 trafen sich IBM 701-Benutzer auf der Eastern Joint Computer Conference und diskutierten das Problem der ineffizienten Jobplanung. Dies führte zur Entwicklung der ersten **Monitor-Programme**.

**Evolution der Batch-Monitore:**

| Jahr | System | Computer | Bedeutung |
|------|--------|----------|-----------|
| 1955 | GM OS | IBM 701 | Erstes Monitor-Programm (General Motors) |
| 1956 | **GM-NAA I/O** | IBM 704 | Erstes echtes "Betriebssystem" |
| 1959 | SHARE OS | IBM 709 | Von IBM-Benutzergruppe SHARE entwickelt |
| 1960 | **IBSYS** | IBM 7090/7094 | IBMs offizielles Batch-System |

> [!note] GM-NAA I/O (1956)
> Entwickelt von **Robert L. Patrick** (General Motors) und **Owen Mock** (North American Aviation) für den IBM 704. Die Hauptfunktion war die automatische Ausführung des nächsten Programms nach Abschluss des vorherigen - die Grundidee der Batch-Verarbeitung.

![[batch-speicher-layout.png]]
*02-01-01-batch-speicher-layout: Basierend auf Stallings, "Operating Systems" und Gordon College CS322 Lecture Notes*

**Aufgaben des Residenten Monitors:**
- **Job Control Language (JCL) interpretieren**: Steuerkarten wie `$JOB`, `$FORTRAN`, `$RUN` auswerten
- **Programme laden**: Compiler und Anwendungen in den Speicher laden
- **I/O-Operationen**: Ein-/Ausgabe für Benutzerprogramme abwickeln
- **Job-Sequenzierung**: Automatischer Übergang zum nächsten Job
- **Buchhaltung**: Ressourcenverbrauch protokollieren

**Beispiel eines Batch-Jobs mit JCL:**

```
$JOB user123            ; Benutzer identifizieren
$FORTRAN                ; FORTRAN-Compiler laden
   [Quellprogramm auf Lochkarten]
$LOAD                   ; Übersetztes Programm laden
$RUN                    ; Programm ausführen
   [Datenkarten]
$EOJ                    ; Ende des Jobs
```

**Probleme der frühen Monitore:**

| Problem | Beschreibung | Spätere Lösung |
|---------|--------------|----------------|
| **Kein Speicherschutz** | Benutzerprogramm konnte Monitor überschreiben | Hardware-Schutz (Protection Rings) |
| **Kein I/O-Schutz** | Job konnte zu viele Karten lesen | Privilegierte I/O-Befehle |
| **Endlosschleifen** | Job blockierte alle anderen | Timer-Interrupt |
| **Keine Parallelität** | CPU wartete auf langsame I/O | Spooling, Multiprogramming |

---

#### Die Erfindung der Hardware-Interrupts

> [!info] Interrupt = Unterbrechung
> Ein **Interrupt** ist ein Hardware-Signal, das die CPU veranlasst, ihre aktuelle Arbeit zu unterbrechen und eine spezielle Routine (Interrupt Service Routine, ISR) auszuführen. Dies war eine revolutionäre Erfindung, die moderne Multitasking-Systeme erst ermöglichte.

**Das Problem vor Interrupts: Polling**

Ohne Interrupts musste die CPU in einer Schleife ständig alle Geräte abfragen ("Polling"):

```
LOOP:
    Prüfe Tastatur      ; Taste gedrückt?
    Prüfe Drucker       ; Fertig?
    Prüfe Bandlaufwerk  ; Daten bereit?
    ...
    GOTO LOOP           ; Endlos wiederholen!
```

Dies verschwendete wertvolle CPU-Zyklen und war bei langsamen Geräten extrem ineffizient.

**Die Lösung: Hardware-Interrupts**

![[hardware-interrupt-ablauf.png]]
*02-01-01-hardware-interrupt-ablauf: Die CPU arbeitet am Hauptprogramm, während das Gerät autonom arbeitet. Meldet das Gerät "Fertig!", löst es ein Interrupt-Signal aus. Die CPU unterbricht das Hauptprogramm, führt die Interrupt-Service-Routine (ISR) aus und kehrt per Rücksprung (IRET) zum Hauptprogramm zurück.*

**Geschichte der Interrupt-Erfindung:**

| Jahr | System            | Innovation                            | Entwickler/Ort                    |
| ---- | ----------------- | ------------------------------------- | --------------------------------- |
| 1951 | UNIVAC I          | Overflow Trap (Fehler-Interrupt)      | Eckert-Mauchly                    |
| 1954 | **NBS DYSEAC**    | Erster I/O-Interrupt + DMA            | National Bureau of Standards      |
| 1955 | IBM 704           | Transfer Trap (Debugging)             | IBM                               |
| 1956 | **UNIVAC 1103A**  | Erstes vollständiges Interrupt-System | Turner & Rawlings, NACA Lewis Lab |
| 1957 | Lincoln Labs TX-2 | Vektorisierte Interrupts              | MIT Lincoln Labs                  |

> [!note] UNIVAC 1103A - Der Durchbruch (1956)
> **Dick Turner** und **Joe Rawlings** am NACA Lewis Flight Propulsion Laboratory (heute NASA Glenn Research Center) entwickelten das erste praktische Interrupt-System. Ihr 1103 wurde normalerweise für Batch-Verarbeitung genutzt, musste aber für Windkanal-Experimente unterbrochen werden können, um Echtzeit-Messdaten zu erfassen. Das System wurde im Februar 1956 betriebsbereit.
> 
> *Quelle: Turner & Rawlings, "Realization of Randomly Timed Computer Input and Output by Means of an Interrupt Feature", IRE Transactions on Electronic Computers, Juni 1958*

**Arten von Interrupts:**

| Typ | Auslöser | Beispiel |
|-----|----------|----------|
| **I/O-Interrupt** | Gerät meldet Bereitschaft | Tastendruck, Disk-Transfer fertig |
| **Timer-Interrupt** | Zeitgeber läuft ab | Prozess-Scheduling (Time-Sharing) |
| **Hardware-Fehler** | Defekte Hardware | Speicherfehler, Stromausfall |
| **Software-Interrupt (Trap)** | Programm löst aus | Division durch Null, Systemaufruf |

**Warum waren Interrupts revolutionär?**

1. **Effiziente I/O**: CPU muss nicht auf langsame Geräte warten
2. **Echtzeitfähigkeit**: Sofortige Reaktion auf externe Ereignisse
3. **Multiprogramming möglich**: Wechsel zwischen Programmen bei I/O-Wartezeiten
4. **Time-Sharing möglich**: Timer-Interrupt für faire CPU-Zuteilung
5. **Fehlerbehandlung**: Automatische Reaktion auf Ausnahmesituationen

**Von Polling zu Interrupts:**

![[polling-vs-interrupts.png]]
*02-01-01-polling-vs-interrupts: Beim **Polling** fragt die CPU das Gerät permanent ab ("Fertig?") und verschwendet dabei Rechenzeit. Mit **Interrupts** arbeitet die CPU ungestört weiter, bis das Gerät sich von selbst meldet – erst dann wird die Interrupt-Service-Routine (ISR) ausgeführt.*

---

#### Spooling - Simultaneous Peripheral Operations On-Line

Mit der Einführung von Interrupts wurde ein weiteres wichtiges Konzept möglich: **Spooling**.

> [!info] SPOOL = Simultaneous Peripheral Operations On-Line
> Spooling ermöglicht es, I/O-Operationen parallel zur CPU-Verarbeitung auszuführen. Eingabedaten werden auf schnelle Medien (Trommel, Disk) zwischengespeichert, während die CPU rechnet.

![[spooling-architektur.png]]
*02-01-01-spooling-architektur: Langsame mechanische Geräte (Kartenleser, Drucker) schreiben bzw. lesen über einen schnellen Puffer (Disk/Trommel). Die CPU greift nur auf diesen Puffer zu und muss daher nie auf die langsamen Geräte warten.*

**Vorteile von Spooling:**
- CPU muss nicht auf Kartenleser/Drucker warten
- Jobs können sofort nach Abschluss ausgegeben werden
- Bessere Geräteauslastung durch Pufferung

---

#### Wichtige Computer der 2. Generation

| Computer | Jahr | Land | Besonderheit |
|----------|------|------|--------------|
| **TRADIC** | 1954 | USA | Erster vollständig transistorisierter Computer |
| **IBM 7090** | 1959 | USA | Wissenschaftlicher Transistor-Mainframe |
| **IBM 1401** | 1959 | USA | Meistverkaufter Computer seiner Zeit |
| **UNIVAC 1107** | 1962 | USA | Erster Computer mit Thin-Film-Speicher |
| **IBM 7094** | 1962 | USA | Schnellster wissenschaftlicher Computer |
| **CDC 6600** | 1964 | USA | Erster Supercomputer (Seymour Cray) |

---

#### Programmiersprachen der 2. Generation

Mit der 2. Generation entstanden die ersten höheren Programmiersprachen:

| Sprache | Jahr | Entwickler | Zweck |
|---------|------|------------|-------|
| **FORTRAN** | 1957 | IBM (John Backus) | Wissenschaftliche Berechnungen |
| **LISP** | 1958 | John McCarthy | Künstliche Intelligenz |
| **COBOL** | 1959 | Grace Hopper et al. | Geschäftsanwendungen |
| **ALGOL** | 1960 | Internationales Komitee | Algorithmen-Beschreibung |

> [!tip] Weiterführende Links - 2. Generation
> - [IBM 7090/7094 - Wikipedia](https://en.wikipedia.org/wiki/IBM_7090)
> - [Harvard Mark I - Wikipedia](https://en.wikipedia.org/wiki/Harvard_Mark_I)
> - [Harvard Collection: Mark I](https://chsi.harvard.edu/harvard-ibm-mark-1-about)
> - [Batch Processing - Wikipedia](https://en.wikipedia.org/wiki/Batch_processing)
> - [Transistor Computer - Wikipedia](https://en.wikipedia.org/wiki/Transistor_computer)
> - [IBM 7094 singt "Daisy Bell" (YouTube)](https://www.youtube.com/watch?v=41U78QP8nBk)
> - [Computer History Museum - IBM 7094](https://www.computerhistory.org/revolution/mainframe-computers/7/166)
> - [Grace Hopper und der erste Bug](https://www.navy.mil/CHIPS/ArticleDetails.aspx?id=5475)
> - [Resident Monitor - Wikipedia](https://en.wikipedia.org/wiki/Resident_monitor)
> - [GM-NAA I/O - Wikipedia](https://en.wikipedia.org/wiki/GM-NAA_I/O)
> - [History of IBM Mainframe OS - Wikipedia](https://en.wikipedia.org/wiki/History_of_IBM_mainframe_operating_systems)
> - [History of Interrupts - Mark Smotherman (Clemson University)](https://mark.people.clemson.edu/interrupts.html)
> - [Interrupt - Wikipedia](https://en.wikipedia.org/wiki/Interrupt)
> - [UNIVAC 1103 - Wikipedia](https://en.wikipedia.org/wiki/UNIVAC_1103)
> - [Computer History Museum: Operating Systems at Conception](https://softwarepreservation.computerhistory.org/os/gm.html)

---

### 3. Generation (1965-1980): ICs und Multiprogramming

Die dritte Generation brachte den Durchbruch der **integrierten Schaltkreise (ICs)** und damit eine drastische Verkleinerung und Leistungssteigerung. Gleichzeitig entstanden revolutionäre Konzepte wie **Time-Sharing** und **Multiprogramming**, die mehreren Benutzern ermöglichten, einen Computer gleichzeitig zu nutzen.

> [!info] Integrierte Schaltkreise (ICs)
> 1958 unabhängig von Jack Kilby (Texas Instruments) und Robert Noyce (Fairchild) erfunden. ICs integrieren mehrere Transistoren auf einem Chip und ermöglichten kompaktere, zuverlässigere und günstigere Computer.

**Charakteristika:**
- **Integrierte Schaltkreise (ICs)** ermöglichen komplexere Systeme
- **Multiprogramming**: Mehrere Programme gleichzeitig im Speicher
- **Time-Sharing**: Mehrere Benutzer teilen sich interaktiv einen Rechner
- **Interrupts** zur effizienten Hardware-Steuerung
- Erste echte Betriebssysteme (OS/360, MULTICS, UNIX)
- Aufkommen der Minicomputer

---

#### IBM System/360 (1964) - Die Computer-Revolution

![[ibm-system360-mainframe.jpg]]
*02-01-01-ibm-system360-mainframe: IBM System/360 - Die erste kompatible Rechnerfamilie, hier im Computer History Museum - Quelle: [Wikimedia Commons](https://commons.wikimedia.org)*

> [!info] "Die $5 Milliarden Wette"
> Die Entwicklung des System/360 kostete IBM rund $5 Milliarden (ca. $45 Mrd. heute) - mehr als die Entwicklung der Atombombe. Es war das riskanteste Projekt der Unternehmensgeschichte und wurde zum größten Erfolg.

Das **IBM System/360** war ein Wendepunkt in der Computergeschichte - die erste Familie kompatibler Computer, von kleinen Einsteigermodellen bis zu Großrechnern.

**Revolutionäre Konzepte:**
- **Aufwärtskompatibilität**: Programme liefen auf allen Modellen der Familie
- **Trennung von Architektur und Implementierung**: Gleiche Software, unterschiedliche Hardware
- **8-Bit-Byte** als Standard (vorher variierten Wortlängen)
- **Mikroprogrammierung**: Flexiblere Prozessorsteuerung

**Technische Daten System/360:**

| Modell   | Jahr | Leistung           | Speicher    | Besonderheit         |
| -------- | ---- | ------------------ | ----------- | -------------------- |
| Model 30 | 1965 | 34.500 Instr./s    | 8-64 KB     | Einsteigermodell     |
| Model 50 | 1965 | 500.000 Instr./s   | 64-512 KB   | Mittlere Leistung    |
| Model 65 | 1965 | 750.000 Instr./s   | 128 KB-1 MB | Großrechner          |
| Model 91 | 1967 | 16,6 Mio. Instr./s | bis 8 MB    | Supercomputer-Klasse |

**Schlüsselpersonen:**
- **Gene Amdahl** - Chefarchitekt
- **Fred Brooks** - Projektmanager (später Autor von "The Mythical Man-Month")
- **Thomas J. Watson Jr.** - IBM-Chairman, genehmigte das Projekt

**Marktbeherrschung:**
In den 1960er-70er Jahren produzierte IBM **80% aller Computer in den USA** und **70% weltweit**. Der Begriff "IBM-kompatibel" wurde zum Industriestandard.

---

#### Der Wandel vom Einprogramm- zum Mehrprogrammbetrieb

Mit der 3. Generation vollzog sich ein fundamentaler Paradigmenwechsel: Computer liefen nicht mehr nur ein Programm zur Zeit, sondern konnten mehrere Programme "gleichzeitig" bearbeiten. Dies war eine direkte Antwort auf das Problem der **ineffizienten CPU-Nutzung**.

##### Das Problem: I/O-Wartezeiten verschwenden CPU-Zyklen

Im **Uniprogramming** (Einprogrammbetrieb) wurde ein Programm vollständig abgearbeitet, bevor das nächste starten konnte. Das grundlegende Problem: CPU-Operationen sind extrem schnell (elektrische Signale), während I/O-Operationen mechanische Geräte erfordern und entsprechend langsam sind.

**Geschwindigkeitsunterschiede (typische Werte, 1960er Jahre):**

| Komponente | Zugriffszeit | Verhältnis |
|------------|--------------|------------|
| CPU-Zyklus | ~1 µs | 1× |
| Magnetkernspeicher | ~10 µs | 10× |
| Trommelspeicher | ~10 ms | 10.000× |
| Magnetband | ~100 ms | 100.000× |
| Lochkartenleser | ~1 s | 1.000.000× |

Während die CPU auf I/O wartete, war sie **vollständig untätig** - bei Maschinen, die $1000+ pro Stunde kosteten, ein enormes Effizienzproblem!

##### CPU-Auslastung bei Uniprogramming

![[uniprogramming-auslastung.png]]
*02-01-01-uniprogramming-auslastung: Bei Uniprogramming läuft nur ein Job zur Zeit. Während Job A auf I/O wartet (rot), bleibt die CPU untätig – Job B kann erst starten, wenn Job A komplett fertig ist. Die CPU ist dadurch den Großteil der Zeit im Leerlauf.*

**Berechnung der CPU-Auslastung:**

$$\text{CPU-Auslastung} = \frac{\text{CPU-aktive Zeit}}{\text{Gesamtzeit}}$$

Bei einem typischen Programm mit 20% CPU-Arbeit und 80% I/O-Wartezeit ergibt sich:
- **Uniprogramming**: ~20% CPU-Auslastung (80% der Zeit wartet die CPU!)

##### Die Lösung: Multiprogramming

Die Idee war einfach aber revolutionär: **Wenn Programm A auf I/O wartet, lasse Programm B auf der CPU laufen!**

![[multiprogramming-auslastung.png]]
*02-01-01-multiprogramming-auslastung: Bei Multiprogramming liegen mehrere Jobs gleichzeitig im Speicher. Wartet ein Job auf I/O, nutzt ein anderer die CPU. Die untere Zeile ("CPU gesamt") zeigt: Die CPU bleibt nahezu durchgehend aktiv – die Auslastung steigt dramatisch.*

**Multiprogramming-Formel (Tanenbaum):**

Wenn jeder Prozess einen Anteil $p$ seiner Zeit mit I/O-Warten verbringt, und $n$ Prozesse im Speicher sind:

$$\text{CPU-Auslastung} = 1 - p^n$$

| I/O-Warteanteil (p) | 1 Prozess | 2 Prozesse | 3 Prozesse | 4 Prozesse |
|---------------------|-----------|------------|------------|------------|
| 50% | 50% | 75% | 87,5% | 93,75% |
| 80% | 20% | 36% | 49% | 59% |
| 90% | 10% | 19% | 27% | 34% |

*Quelle: Tanenbaum, "Modern Operating Systems", Formel basierend auf statistisch unabhängigen Prozessen*

> [!example] Rechenbeispiel
> Bei 80% I/O-Wartezeit und 4 Programmen im Speicher:
> - **Uniprogramming**: CPU-Auslastung = 20%
> - **Multiprogramming**: CPU-Auslastung = 1 - 0,8⁴ = 1 - 0,4096 ≈ **59%**
> 
> Das ist fast eine **Verdreifachung** der CPU-Effizienz!

##### Time-Sharing: Interaktive Mehrbenutzer-Systeme

**Multiprogramming** allein reichte für Batch-Jobs. Aber Wissenschaftler und Ingenieure wollten **interaktiv** mit dem Computer arbeiten - nicht Lochkarten einwerfen und Stunden auf Ergebnisse warten.

Die Lösung: **Time-Sharing** (Zeitscheiben-Verfahren), bei dem die CPU alle 10-100 Millisekunden zwischen den Benutzern wechselt.

![[time-sharing-prinzip.png]]
*02-01-01-time-sharing-prinzip: Die CPU teilt ihre Zeit in kurze Quanten (hier je 100 ms) auf und wechselt per Timer-Interrupt (T-INT) reihum zwischen den Benutzern. Bei ~10 Wechseln pro Sekunde entsteht für jeden User der Eindruck, den Computer allein zu nutzen.*

**Time-Sharing im Detail:**

![[time-sharing-detail.png]]
*02-01-01-time-sharing-detail: Mehrere Terminals sind über einen Terminal-Konzentrator (Frontend) mit dem Mainframe verbunden. Dort liegen die Jobs aller Benutzer gleichzeitig im Speicher, und die CPU wechselt alle 10–100 ms zwischen ihnen. Jeder Benutzer hatte das Gefühl, den Computer alleine zu nutzen!*
##### CTSS - Das erste Time-Sharing-System (1961)

> [!info] Fernando J. Corbató (1926-2019)
> MIT-Professor und Turing-Preisträger (1990). Corbató entwickelte CTSS und leitete später das MULTICS-Projekt. Er gilt als Erfinder des Computer-Passworts.

Das **Compatible Time-Sharing System (CTSS)** wurde 1961 am MIT unter der Leitung von **Fernando Corbató** demonstriert - zunächst auf einer modifizierten IBM 709, später auf der IBM 7094.

**CTSS Meilensteine:**
- **November 1961**: Erste Demonstration auf IBM 709 (3 Benutzer gleichzeitig)
- **1962**: Übergang auf modifizierte IBM 7094
- **1963**: Regulärer Betrieb für MIT-Benutzer
- **1973**: Abschaltung (12 Jahre Betrieb!)

**Innovationen von CTSS:**
- Erstes echtes **Multi-User Time-Sharing** System
- Erste Implementierung von **Computer-Passwörtern** für Benutzerauthentifizierung
- Frühe Form von **E-Mail** (CTSS MAIL)
- **Interaktive Text-Editoren** (statt Lochkarten)
- Antwortzeiten in **Sekunden statt Stunden**

> [!quote] Fernando Corbató über Time-Sharing (1962)
> *"In the early 1960s, we are in the midst of a third major modification to computer usage: the improvement of man-machine interaction by a process called time-sharing."*
> — F.J. Corbató, M. Merwin-Daggett, R.C. Daley: "An Experimental Time-Sharing System", AFIPS Conference, 1962

**Vergleich Batch vs. Time-Sharing:**

| Aspekt | Batch-Verarbeitung | Time-Sharing |
|--------|-------------------|--------------|
| Turnaround-Zeit | Stunden bis Tage | Sekunden |
| Benutzerinteraktion | Keine (Lochkarten) | Interaktiv (Terminal) |
| Fehlersuche | Extrem mühsam | Sofortige Rückmeldung |
| Benutzer gleichzeitig | 1 (seriell) | Dutzende |
| Programmiereffizienz | Niedrig | Hoch |

##### Technische Voraussetzungen für Time-Sharing

Time-Sharing erforderte mehrere Hardware- und Software-Innovationen:

| Voraussetzung | Beschreibung | Einführung |
|---------------|--------------|------------|
| **Hardware-Interrupts** | CPU kann unterbrochen werden | 1954-1956 |
| **Timer-Interrupt** | Periodische Unterbrechung für Scheduling | ~1960 |
| **Speicherschutz** | Benutzer können sich nicht gegenseitig stören | System/360 |
| **Privilegierte Modi** | Trennung von Kernel- und Benutzermodus | System/360 |
| **Virtueller Speicher** | Jeder Benutzer hat eigenen Adressraum | 1961 (Atlas) |

##### Weiterführende Quellen

> [!tip] Weiterführende Links - Multiprogramming & Time-Sharing
> - [IBM History: Time-Sharing](https://www.ibm.com/history/time-sharing) - Umfassende Geschichte von IBM
> - [CTSS - Wikipedia](https://en.wikipedia.org/wiki/Compatible_Time-Sharing_System)
> - [MIT CSAIL: Fernando Corbató Nachruf](https://www.csail.mit.edu/news/fernando-corby-corbato-1926-2019)
> - [Corbató et al. 1962 Paper (PDF)](https://cseweb.ucsd.edu/classes/wi19/cse221-a/papers/corbato62.pdf) - Original CTSS Paper
> - [JMU OpenCSF: Multiprogramming](https://users.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/Multiprogramming.html) - Exzellente Erklärung mit Formeln
> - Tanenbaum, "Modern Operating Systems" - Kapitel über Multiprogramming

---

#### [[07-Anhang/Betriebssysteme/MULTICS|MULTICS]] (1964-1969) - Der einflussreiche Vorläufer

> [!info] MULTICS = Multiplexed Information and Computing Service
> Ein Gemeinschaftsprojekt von MIT, Bell Labs und General Electric. Obwohl kommerziell nicht erfolgreich, beeinflusste [[07-Anhang/Betriebssysteme/MULTICS|MULTICS]] praktisch alle modernen Betriebssysteme.

MULTICS sollte ein "Computing Utility" werden - Computer als Dienstleistung wie Strom oder Wasser.

**Revolutionäre Konzepte von MULTICS:**

| Konzept | Beschreibung | Heutiger Erbe |
|---------|--------------|---------------|
| **Hierarchisches Dateisystem** | Ordner in Ordnern | Standard in allen OS |
| **Segmented Memory** | Virtueller Speicher mit Segmenten | Paging/Virtual Memory |
| **Ring-basierte Sicherheit** | Zugriffsrechte in konzentrischen Ringen | CPU Protection Rings |
| **Dynamisches Linking** | Bibliotheken zur Laufzeit laden | Shared Libraries, DLLs |
| **Hot Swapping** | Hardware-Austausch im Betrieb | Server-Wartung |

**Timeline:**
- 1964: Projekt beginnt (MIT Project MAC, Bell Labs, General Electric)
- 1967: Erste GE-645 Hardware an MIT geliefert
- 1969: Bell Labs steigt aus → führt direkt zu UNIX
- 1970: GE verkauft Computerabteilung an Honeywell
- 1985: Letztes kommerzielles MULTICS-System installiert
- 2007: Quellcode als Open Source freigegeben

---

#### [[07-Anhang/Betriebssysteme/UNIX|UNIX]] (1969) - Die Geburt eines Betriebssystem-Imperiums

> [!info] Ken Thompson & Dennis Ritchie
> Nach dem Ausstieg aus [[07-Anhang/Betriebssysteme/MULTICS|MULTICS]] entwickelten Thompson und Ritchie bei Bell Labs [[07-Anhang/Betriebssysteme/UNIX|UNIX]] auf einer ungenutzten PDP-7. Der Name ist ein Wortspiel: MULTICS (MULTIplexed) → UNICS (UNiplexed) → UNIX

**Die Entstehungsgeschichte:**

| Jahr | Meilenstein |
|------|-------------|
| **1969** | Ken Thompson schreibt UNIX auf einer PDP-7 (in Assembler) |
| **1970** | UNIX wird auf die PDP-11 portiert |
| **1971** | Erste UNIX-Dokumentation (*UNIX Programmer's Manual*) |
| **1973** | UNIX wird in C neu geschrieben (Dennis Ritchies Sprache) |
| **1974** | Erste wissenschaftliche Publikation |
| **1975+** | Bell Labs lizenziert UNIX an Universitäten (fast kostenlos) |

> [!note] Daraus entstandene UNIX-Linien
> Aus der Universitätslizenzierung entwickelten sich die großen UNIX-Zweige:
> **BSD** (Berkeley) · **System V** (AT&T) · und später **Linux** (1991)

**UNIX-Philosophie:**
- "Do one thing and do it well" (Ein Programm = eine Aufgabe)
- "Everything is a file" (Alles ist eine Datei)
- Programme sollen zusammenarbeiten (Pipes: `|`)
- Text als universelles Interface

**Einfluss:**
[[07-Anhang/Betriebssysteme/UNIX|UNIX]] ist der Vorfahre von:
- **[[07-Anhang/Betriebssysteme/Linux|Linux]]** (1991, Linus Torvalds)
- **[[07-Anhang/Betriebssysteme/macOS|macOS]]** (basiert auf [[07-Anhang/Betriebssysteme/BSD|BSD]]/Darwin)
- **[[07-Anhang/Betriebssysteme/Android|Android]]** (Linux-Kernel)
- **[[07-Anhang/Betriebssysteme/iOS|iOS]]** (Darwin)
- Praktisch alle Server im Internet

> [!tip] Weiterführender Link
> - [Geschichte der Unix Betriebssysteme als PDF (Levenez)](https://www.levenez.com/unix/redirect_unix_pdf.html)

---

#### Minicomputer: DEC PDP-Serie

Die 3. Generation brachte auch die **Minicomputer** - kleiner und günstiger als Mainframes, aber leistungsfähiger als die späteren PCs.

![[dec-pdp-1.jpg]]
*02-01-01-dec-pdp-1: DEC PDP-1 (1960) - Einer der ersten kommerziellen Minicomputer - Quelle: [Computer History Museum](https://www.computerhistory.org)*

##### PDP-1 (1960)

| Eigenschaft | Wert |
|-------------|------|
| Hersteller | Digital Equipment Corporation (DEC) |
| Preis | $120.000 (vs. $1+ Mio. für IBM Mainframes) |
| Wortlänge | 18 Bit |
| Taktfrequenz | 200 kHz |
| Besonderheit | Erstes Computerspiel "Spacewar!" (1962) |

![[dec-pdp-11.jpg]]
*02-01-01-dec-pdp-11: DEC PDP-11 (1970) - Der einflussreichste Minicomputer aller Zeiten - Quelle: [Wikimedia Commons](https://commons.wikimedia.org)*

##### PDP-11 (1970) - Der Minicomputer-König

> [!info] 600.000 verkaufte Einheiten
> Die PDP-11 war einer der erfolgreichsten Computer überhaupt und blieb bis in die 1990er Jahre in Produktion.

**Technische Daten:**

| Eigenschaft | Wert |
|-------------|------|
| Architektur | 16 Bit |
| Bus-System | UNIBUS (revolutionär!) |
| Speicher | bis 4 MB |
| Produktion | 1970-1990+ |
| Verkaufte Einheiten | ~600.000 |

**Bedeutung der PDP-11:**
- **[[07-Anhang/Betriebssysteme/UNIX|UNIX]] wurde hier entwickelt** (ursprünglich auf PDP-7, dann PDP-11)
- **C wurde hier entwickelt** (Dennis Ritchie)
- Erste Computer mit einheitlichem Bus für alle Komponenten
- Beeinflusste viele spätere Architekturen (inkl. VAX, x86)

---

#### Schlüsselkonzepte der 3. Generation

| Konzept | Beschreibung | Bedeutung |
|---------|--------------|-----------|
| **Multiprogramming** | Mehrere Programme im Speicher, CPU wechselt bei I/O-Wartezeiten | Bessere CPU-Auslastung |
| **Time-Sharing** | Zeitscheiben für interaktive Multi-User-Nutzung | Demokratisierung der Computer |
| **Spooling** | Simultaneous Peripheral Operations On-Line | Asynchrone I/O |
| **Interrupts** | Hardware-Signale zur Ereignisbehandlung | Reaktive Systeme |
| **Virtueller Speicher** | Programme größer als physischer Speicher | Flexibilität |

---

#### Wichtige Systeme der 3. Generation

| System | Jahr | Typ | Besonderheit |
|--------|------|-----|--------------|
| **IBM System/360** | 1964 | Mainframe-Familie | Erste kompatible Computerfamilie |
| **[[MULTICS]]** | 1964-69 | Betriebssystem | Vorläufer aller modernen OS |
| **DEC PDP-8** | 1965 | Minicomputer | Erster erfolgreicher Minicomputer |
| **IBM System/370** | 1970 | Mainframe | Virtueller Speicher |
| **DEC PDP-11** | 1970 | Minicomputer | UNIX-Geburtsort, 600.000 verkauft |
| **[[UNIX]]** | 1969/1973 | Betriebssystem | Basis aller modernen Systeme |
| **Cray-1** | 1976 | Supercomputer | Erster kommerzieller Supercomputer |

---

> [!tip] Weiterführende Links - 3. Generation
> - [IBM System/360 - Wikipedia](https://en.wikipedia.org/wiki/IBM_System/360)
> - [MULTICS - Wikipedia](https://en.wikipedia.org/wiki/Multics)
> - [MULTICS History](https://multicians.org/history.html)
> - [History of Unix - Wikipedia](https://en.wikipedia.org/wiki/History_of_Unix)
> - [PDP-11 - Wikipedia](https://en.wikipedia.org/wiki/PDP-11)
> - [Ars Technica: Tour of the PDP-11](https://arstechnica.com/gadgets/2022/03/a-brief-tour-of-the-pdp-11-the-most-influential-minicomputer-of-all-time/)
> - [IEEE Spectrum: The Strange Birth of Unix](https://spectrum.ieee.org/the-strange-birth-and-long-life-of-unix)
> - [Computer History Museum: Minicomputers](https://www.computerhistory.org/revolution/minicomputers/11)
> - [The Mythical Man-Month (Fred Brooks)](https://en.wikipedia.org/wiki/The_Mythical_Man-Month)

---

### 4. Generation (1980-heute): Personal Computer und Netzwerke

Die vierte Generation markierte die **Demokratisierung des Computing** - Computer wurden vom exklusiven Großrechner zum persönlichen Werkzeug für jedermann. Der Mikroprozessor ermöglichte kompakte, erschwingliche Systeme, während grafische Benutzeroberflächen die Bedienung revolutionierten.

> [!info] VLSI-Technologie
> **Very Large Scale Integration (VLSI)** ermöglichte ab Ende der 1970er Jahre die Integration von hunderttausenden Transistoren auf einem Chip. Der Intel 8086 (1978) hatte 29.000 Transistoren - ein moderner Prozessor hat Milliarden.

**Charakteristika:**
- **Mikroprozessoren** ermöglichen erschwingliche Personal Computer
- **Grafische Benutzeroberflächen (GUIs)** ersetzen Kommandozeilen
- **Vernetzung** (LAN, Internet) wird Standard
- **Mobile Betriebssysteme** für Smartphones und Tablets
- **Open Source** als alternatives Entwicklungsmodell (Linux)
- **Virtualisierung** und Cloud Computing

---

#### Xerox Alto (1973) - Der Visionär

![[xerox-alto-maus-1973.jpg]]
*02-01-01-xerox-alto-maus-1973: Xerox Alto (1973) - Erster Personal Computer mit grafischer Oberfläche und Maus - Quelle: [Computer History Museum](https://www.computerhistory.org)*

> [!info] XEROX PARC
> Das **Palo Alto Research Center** (gegründet 1970) entwickelte viele Technologien, die die moderne Computerwelt prägen: GUI, Maus, Ethernet, Laserdrucker, WYSIWYG-Textverarbeitung. Xerox selbst vermarktete diese Innovationen nicht erfolgreich - andere profitierten davon.

Der **Xerox Alto** war seiner Zeit um über ein Jahrzehnt voraus und enthielt praktisch alle Konzepte moderner Desktop-Computer.

**Technische Daten:**

| Eigenschaft | Wert |
|-------------|------|
| Entwicklungsbeginn | 1972, erste Maschine März 1973 |
| Entwickler | Butler Lampson, Chuck Thacker et al. (XEROX PARC) |
| CPU | Bit-slice, ca. 5,88 MHz |
| RAM | 128 KB - 512 KB |
| Display | 606 × 808 Pixel, vertikal (wie ein Blatt Papier!) |
| Eingabe | Tastatur + 3-Tasten-Maus |
| Speicher | 2,5 MB Wechselplatte |
| Netzwerk | Ethernet (auch von PARC erfunden) |
| Stückzahl | ca. 2.000 (nur intern bei Xerox + Universitäten) |
| Preis | $32.000 (nur intern, nie kommerziell verkauft) |

**Revolutionäre Innovationen des Alto:**
- **Grafische Benutzeroberfläche (GUI)** mit Fenstern, Menüs, Icons
- **WYSIWYG-Textverarbeitung** (Bravo-Editor)
- **Maus** als Zeigegerät (basierend auf Doug Engelbart's Erfindung)
- **Ethernet-Netzwerk** (erste Implementation)
- **Objektorientierte Programmierung** (Smalltalk)
- **E-Mail** innerhalb von PARC

**Das berühmte Xerox-Apple-Treffen:**
1979 besuchte Steve Jobs PARC und sah den Alto. Er erkannte sofort das Potenzial der GUI:

> *"They showed me really three things. But I was so blinded by the first one I didn't even really see the other two... [the GUI] was so obvious that a computer should work that way."*
> — Steve Jobs

Jobs verhandelte, dass Apple-Ingenieure PARC besuchen durften - im Austausch für Aktienoptionen. Apple übernahm die GUI-Konzepte und entwickelte sie weiter für Lisa (1983) und Macintosh (1984).

---

#### IBM PC (1981) - Der Industriestandard

![[ibm-pc-xt-1983.jpg]]
*02-01-01-ibm-pc-xt-1983: IBM PC XT (1983) - Erweitertes Modell mit Festplatte - Quelle: [Computer History Museum](https://www.computerhistory.org)*

> [!info] "Project Chess"
> IBM entwickelte den PC in nur 12 Monaten mit einem kleinen Team in Boca Raton, Florida - außerhalb der normalen IBM-Bürokratie. Die Entscheidung, Standard-Komponenten von Drittanbietern zu verwenden, ermöglichte das Tempo - und die späteren Klone.

Am **12. August 1981** stellte IBM den **IBM Personal Computer 5150** vor und legitimierte damit den Personal Computer als seriöses Geschäftswerkzeug.

**Technische Daten IBM PC 5150:**

| Eigenschaft | Wert |
|-------------|------|
| Vorstellung | 12. August 1981 |
| CPU | Intel 8088, 4,77 MHz |
| RAM | 16 KB - 256 KB (erweiterbar auf 640 KB) |
| Speicher | Kassette oder 5,25" Disketten (160 KB) |
| Display | Monochrom oder CGA (4 Farben) |
| Betriebssystem | PC-DOS 1.0 (Microsoft MS-DOS) |
| Preis | $1.565 - $6.000 (je nach Ausstattung) |
| Slogan | *"A tool for modern times"* |

**Die Entscheidungen, die die Industrie prägten:**

| Entscheidung | Konsequenz |
|--------------|------------|
| **Intel 8088** statt eigener CPU | x86-Architektur wird Standard |
| **MS-DOS** von Microsoft lizenziert | Microsoft wird Software-Gigant |
| **Offene Architektur** (publizierte Specs) | "IBM-kompatible" Klone entstehen |
| **ISA-Bus** für Erweiterungskarten | Standard für Jahrzehnte |

**Die Geburt von [[07-Anhang/Betriebssysteme/MS-DOS|MS-DOS]]:**
IBM fragte ursprünglich Digital Research ([[07-Anhang/Betriebssysteme/CP-M|CP/M]]-Entwickler) wegen eines Betriebssystems. Die Verhandlungen scheiterten - und IBM wandte sich an Microsoft. Bill Gates kaufte QDOS ("Quick and Dirty Operating System") für $50.000 und lizenzierte es als [[07-Anhang/Betriebssysteme/MS-DOS|MS-DOS]] an IBM.

**Schlüsselpersonen:**
- **Don Estridge** - "Vater des IBM PC", Leiter des Projekts
- **Bill Lowe** - Überzeugte IBM-Management vom PC-Konzept
- **Bill Gates** - Microsoft-Gründer, lieferte MS-DOS

> [!warning] IBMs strategischer Fehler
> IBM behielt keine Exklusivrechte an MS-DOS oder dem BIOS-Design. Dies ermöglichte Compaq, Dell und anderen, "IBM-kompatible" PCs zu bauen. IBM verlor die Kontrolle über den Markt, den es geschaffen hatte.

---

#### Die Heimcomputer-Revolution (1982-1985)

Die frühen 1980er Jahre erlebten einen Boom erschwinglicher Heimcomputer, die eine ganze Generation an das Programmieren heranführten.

##### Commodore 64 (1982) - Der Meistverkaufte

![[commodore-c64.jpg]]
*02-01-01-commodore-c64: Commodore 64 (1982) - Der meistverkaufte Heimcomputer aller Zeiten - Quelle: [Wikimedia Commons](https://commons.wikimedia.org)*

> [!info] Guinness-Weltrekord
> Der C64 hält den **Guinness-Weltrekord** als meistverkaufter einzelner Computertyp aller Zeiten. Schätzungen reichen von **12,5 bis 17 Millionen** verkauften Einheiten.

**Technische Daten:**

| Eigenschaft | Wert |
|-------------|------|
| Vorstellung | Januar 1982 (CES) |
| Markteinführung | August 1982 |
| CPU | MOS 6510, 1 MHz (6502-Derivat) |
| RAM | 64 KB (daher der Name) |
| Grafik | VIC-II: 320×200, 16 Farben, Sprites |
| Sound | **SID 6581**: 3 Stimmen, legendärer Synthesizer |
| Preis USA | $595 (später $200) |
| Produktionsende | 1994 |

**Warum war der C64 so erfolgreich?**
- **Aggressiver Preis**: Commodore-Gründer Jack Tramiel: *"We need to build computers for the masses, not the classes"*
- **Überlegene Grafik und Sound** für Spiele
- **Starke Software-Bibliothek** (über 10.000 Titel)
- **Massenvertrieb** über Kaufhäuser (nicht nur Fachgeschäfte)

##### Sinclair ZX Spectrum (1982) - Der Europäer

![[zx-spectrum.jpg]]
*02-01-01-zx-spectrum: Sinclair ZX Spectrum (1982) - Der populärste britische Heimcomputer - Quelle: [Wikimedia Commons](https://commons.wikimedia.org)*

**Technische Daten:**

| Eigenschaft | Wert |
|-------------|------|
| Vorstellung | 23. April 1982 |
| CPU | Zilog Z80A, 3,5 MHz |
| RAM | 16 KB oder 48 KB |
| Grafik | 256×192, 8 Farben (+ 8 "bright") |
| Sound | 1-Bit Beeper |
| Preis UK | £125 (16K) / £175 (48K) |
| Besonderheit | Gummi-Tastatur |

Der Spectrum prägte die britische Spieleindustrie und brachte Millionen Europäern das Programmieren bei.

##### Vergleich der Heimcomputer

| Computer | Jahr | CPU | RAM | Preis | Verkauft |
|----------|------|-----|-----|-------|----------|
| **Apple II** | 1977 | 6502, 1 MHz | 4-48 KB | $1.298+ | 6 Mio. |
| **Commodore 64** | 1982 | 6510, 1 MHz | 64 KB | $595 | 12-17 Mio. |
| **ZX Spectrum** | 1982 | Z80, 3,5 MHz | 16-48 KB | £125 | 5 Mio. |
| **Atari 800** | 1979 | 6502, 1,8 MHz | 8-48 KB | $999 | 2 Mio. |
| **Amstrad CPC** | 1984 | Z80, 4 MHz | 64 KB | £249 | 3 Mio. |

---

#### Apple Macintosh (1984) - Die GUI-Revolution

![[apple-macintosh-1984.jpg]]
*02-01-01-apple-macintosh-1984: Apple Macintosh 128K (1984) - Der Computer, der die grafische Oberfläche popularisierte - Quelle: [Computer History Museum](https://www.computerhistory.org)*

> [!info] "1984" - Der berühmteste Werbespot
> Der Mac wurde am **22. Januar 1984** während des Super Bowl XVIII mit einem von **Ridley Scott** inszenierten Werbespot eingeführt, der auf George Orwells "1984" anspielte. IBM wurde als "Big Brother" dargestellt, der Mac als Befreier. Der Spot lief nur einmal im TV und gilt als einer der einflussreichsten Werbespots aller Zeiten.

Am **24. Januar 1984** stellte Steve Jobs den Macintosh vor - und der Mac begrüßte das Publikum mit synthetischer Sprache: *"Hello, I am Macintosh. It sure is great to get out of that bag."*

**Technische Daten Macintosh 128K:**

| Eigenschaft | Wert |
|-------------|------|
| Vorstellung | 24. Januar 1984 |
| CPU | Motorola 68000, 7,83 MHz |
| RAM | 128 KB (sehr knapp!) |
| Display | 9" Monochrom, 512×342 Pixel |
| Speicher | 3,5" Diskette, 400 KB |
| Maus | Einknopf-Maus |
| Preis | $2.495 (~$7.500 heute) |
| Verkäufe | 70.000 bis Mai 1984 |

**Was den Mac besonders machte:**

| Feature | Bedeutung |
|---------|-----------|
| **Vollständige GUI** | Fenster, Icons, Menüs, Maus als Standard |
| **WYSIWYG** | "What You See Is What You Get" - Bildschirm = Ausdruck |
| **Proportionalschrift** | Keine Schreibmaschinen-Fonts mehr |
| **Desktop-Metapher** | Papierkorb, Ordner, Dateien |
| **Pull-down-Menüs** | Konsistente Bedienung in allen Programmen |

**Der Mac und Desktop Publishing:**
1985 erschienen **Aldus PageMaker** und der **Apple LaserWriter** - zusammen mit dem Mac begründeten sie das **Desktop Publishing** und retteten Apple finanziell.

---

#### Microsoft Windows - Der lange Weg zur Dominanz

Microsoft Windows brauchte Jahre, um von einer belächelten DOS-Erweiterung zum dominierenden Desktop-Betriebssystem zu werden.

**Die Windows-Evolution:**

| Version            | Jahr      | Bedeutung                                                                 |
| ------------------ | --------- | ------------------------------------------------------------------------- |
| **[[Windows-1]]**  | 1985      | Erste Version, gekachelte Fenster (kein Überlappen!), $100                |
| **Windows 2.0**    | 1987      | Überlappende Fenster, Tastenkürzel, Word/Excel                            |
| **[[Windows-3]]**  | 1990      | Erster kommerzieller Erfolg, Protected Mode, 10 Mio. Verkäufe in 2 Jahren |
| **Windows 3.1**    | 1992      | TrueType-Fonts, Multimedia, stabilerer                                    |
| **[[Windows-95]]** | 1995      | Start-Menü, Taskbar, 32-Bit, Plug and Play, **Durchbruch!**               |
| **[[Windows-98]]** | 1998      | USB-Support, Internet Explorer integriert                                 |
| **[[Windows-NT]]** | 1993-2000 | Separate Linie für Business, 32-Bit, NTFS                                 |
| **[[Windows-XP]]** | 2001      | Vereinigung von 9x und NT-Linie, Luna-Design                              |
| **[[Windows-7]]**  | 2009      | Optimiert, beliebt, lange Lebensdauer                                     |
| **[[Windows-10]]** | 2015      | "Windows as a Service", letztes nummeriertes Windows (bis...)             |
| **[[Windows-11]]** | 2021      | Neues Design, TPM 2.0 Anforderung                                         |

**[[07-Anhang/Betriebssysteme/Windows-95|Windows 95]] - Die Revolution:**

> [!info] Der Launch von [[07-Anhang/Betriebssysteme/Windows-95|Windows 95]]
> Microsoft investierte **$300 Millionen** in den Windows 95-Launch. Das Empire State Building wurde in Windows-Farben beleuchtet, die Rolling Stones lizenzierten "Start Me Up" für die Kampagne. 1 Million Kopien wurden in den ersten 4 Tagen verkauft.

[[07-Anhang/Betriebssysteme/Windows-95|Windows 95]] etablierte die bis heute bekannte Desktop-Metapher:
- **Start-Button und Taskbar** (erstmals)
- **32-Bit Multitasking** (preemptive, nicht kooperativ)
- **Lange Dateinamen** (nicht mehr 8.3)
- **Plug and Play** (automatische Hardwareerkennung)

> [!tip] Weiterführender Link
> - [Geschichte der Windows Betriebssysteme als PDF (Levenez)](https://www.levenez.com/windows/windows.pdf)

---

#### [[07-Anhang/Betriebssysteme/Linux|Linux]] (1991) - Die Open-Source-Revolution

> [!quote] Die berühmteste Usenet-Nachricht
> *"Hello everybody out there using minix -*
> *I'm doing a (free) operating system (just a hobby, won't be big and*
> *professional like gnu) for 386(486) AT clones."*
> — **Linus Torvalds**, comp.os.minix, 25. August 1991

![[frueh-pc-terminal.jpg]]
*02-01-01-frueh-pc-terminal: Frühe PC-Workstation - Systeme wie diese waren die Zielplattform für Linux*

Am **25. August 1991** kündigte der 21-jährige finnische Student **Linus Torvalds** in der Newsgroup comp.os.minix sein "kleines" Projekt an - ein freies Betriebssystem für x86-PCs.

**Die Entstehung von [[07-Anhang/Betriebssysteme/Linux|Linux]]:**

| Zeitpunkt | Meilenstein |
|-----------|-------------|
| **1991, April** | Linus beginnt mit der Entwicklung (inspiriert von MINIX) |
| **1991, August** | Erste öffentliche Ankündigung auf comp.os.minix |
| **1991, Sept.** | Linux 0.01 verfügbar (10.000 Zeilen Code) |
| **1992** | Linux 0.12 mit GNU GPL-Lizenz |
| **1993** | 300+ Entwickler, Linux 1.0 in Vorbereitung |
| **1994** | Linux 1.0 veröffentlicht |
| **1996** | Linux 2.0, SMP-Support |
| **2003** | Linux 2.6 (Kernel bleibt bei 2.6.x für 8 Jahre) |
| **2011** | Linux 3.0 (Jubiläumsversion, 20 Jahre) |
| **2015** | Linux 4.0 |
| **2019** | Linux 5.0 |
| **2022** | Linux 6.0 |

**Warum wurde [[07-Anhang/Betriebssysteme/Linux|Linux]] erfolgreich?**

| Faktor | Erklärung |
|--------|-----------|
| **Timing** | Freies [[UNIX]] für x86, als [[BSD]] in Rechtsstreit war |
| **GNU GPL** | "Copyleft" hält Code frei, Beiträge fließen zurück |
| **Internet** | Globale Zusammenarbeit erstmals möglich |
| **[[Minix]]** | Lehrreiches Vorbild (Andrew Tanenbaum) |
| **Pragmatismus** | "Rough consensus and running code" |

**[[07-Anhang/Betriebssysteme/Linux|Linux]] heute:**
- **100%** der Top 500 Supercomputer laufen unter [[07-Anhang/Betriebssysteme/Linux|Linux]]
- **>70%** aller Server im Internet
- **[[07-Anhang/Betriebssysteme/Android|Android]]** (Linux-Kernel): >3 Milliarden aktive Geräte
- **96%** aller Cloud-Infrastruktur
- Basis für: Chrome OS, Steam Deck, Smart TVs, Router, IoT-Geräte

---

#### Mobile Betriebssysteme - Computing in der Tasche

Die 2000er Jahre brachten den nächsten Paradigmenwechsel: Computer wurden tragbar und allgegenwärtig.

**Die Smartphone-Revolution:**

| Jahr | Ereignis |
|------|----------|
| 2000 | **[[Symbian]]** dominiert frühe Smartphones |
| 2005 | Google kauft Android Inc. |
| 2007 | **Apple iPhone** mit [[iOS]] - "Das Internet in deiner Tasche" |
| 2008 | **[[Android]] 1.0** (HTC Dream/T-Mobile G1) |
| 2010 | **iPad** begründet Tablet-Markt |
| 2012 | [[Android]] überholt [[iOS]] weltweit |
| 2015 | Windows Phone eingestellt (effektiv) |

**Marktanteile mobile OS (2026):**

| OS | Weltweit | USA |
|----|----------|-----|
| **[[Android]]** | ~70% | ~42% |
| **[[iOS]]** | ~30% | ~58% |
| Andere | <1% | <1% |

**Designprinzipien mobiler OS:**

| Desktop-OS | Mobile-OS |
|------------|-----------|
| Maus + Tastatur | Touch + Gesten |
| Fenstersystem | Fullscreen-Apps |
| Dateisystem sichtbar | App-zentriert, Sandboxing |
| Unbegrenzter Strom | Energiemanagement kritisch |
| Immer online optional | Always-connected Annahme |
| Offene Installation | App Stores (Kontrolle) |

---

#### Moderne Entwicklungen (2010-heute)

##### Cloud Computing und Virtualisierung

**Von lokaler Software zu Cloud-Services:**

| Paradigma | Beispiel | Bedeutung |
|-----------|----------|-----------|
| **IaaS** | AWS EC2, Azure VM | Virtuelle Server mieten |
| **PaaS** | Heroku, Google App Engine | Plattform ohne Infrastruktur-Sorgen |
| **SaaS** | Office 365, Google Workspace | Software als Dienst |

##### Containerisierung

**Docker (2013)** und **Kubernetes (2014)** revolutionierten das Deployment:

![[virtualisierung-container.png]]
*02-01-01-virtualisierung-container: Der zentrale Unterschied liegt im Umgang mit dem Betriebssystem: Virtuelle Maschinen virtualisieren über einen Hypervisor die komplette Hardware, sodass **jede VM ihr eigenes Gast-OS** mitbringt (ressourcenintensiv). Container teilen sich dagegen **ein gemeinsames Host-OS** und isolieren nur die Anwendungen über die Container-Runtime – dadurch sind sie leichtgewichtig und starten in Sekunden.*

##### Weitere moderne Trends

| Trend | Beschreibung |
|-------|--------------|
| **Edge Computing** | Verarbeitung nahe an Datenquellen |
| **IoT-Betriebssysteme** | [[FreeRTOS]], [[Zephyr]], Embedded [[Linux]] |
| **Unikernels** | Minimale OS für einzelne Anwendungen |
| **WebAssembly (Wasm)** | Plattformunabhängige Ausführung |
| **KI-Integration** | Copiloten, Assistenten im OS |

---

#### Detaillierte Timeline der 4. Generation

| Jahr | Hardware | Software/OS | Meilenstein |
|------|----------|-------------|-------------|
| 1971 | Intel 4004 | - | Erster Mikroprozessor |
| 1973 | Xerox Alto | Alto OS | Erste GUI, Maus, Ethernet |
| 1974 | Intel 8080 | [[CP-M]] (1974) | Erster 8-Bit PC-Standard |
| 1975 | Altair 8800 | Altair BASIC | Erster kommerzieller PC-Kit |
| 1976 | Apple I | - | Wozniak's Einzelplatine |
| 1977 | Apple II | Apple DOS | Erster erfolgreicher Heimcomputer |
| 1979 | - | VisiCalc | Erste Tabellenkalkulation ("Killer-App") |
| 1981 | IBM PC 5150 | PC-DOS/[[MS-DOS]] | IBM legitimiert den PC |
| 1982 | Commodore 64 | KERNAL/BASIC | Meistverkaufter Computer |
| 1983 | Apple Lisa | Lisa OS | Erste kommerzielle GUI (zu teuer) |
| 1984 | Macintosh | System 1 | GUI wird massentauglich |
| 1985 | - | Windows 1.0, AmigaOS | Microsoft beginnt GUI-Ära |
| 1987 | - | OS/2 | IBM/Microsoft Kooperation |
| 1990 | - | Windows 3.0 | Windows wird erfolgreich |
| 1991 | - | [[Linux]] 0.01 | Open-Source-Revolution beginnt |
| 1993 | - | [[Windows-NT]] 3.1 | 32-Bit Business-OS |
| 1995 | - | [[Windows-95]] | Start-Menü, Taskbar, Mainstream |
| 2001 | iPod | [[Windows-XP]], [[macOS]] (Mac OS X) | Vereinigung der Windows-Linien |
| 2007 | iPhone | [[iOS]] | Smartphone-Revolution |
| 2008 | - | [[Android]] 1.0 | Google betritt Mobilmarkt |
| 2011 | - | Chrome OS | Browser als OS |
| 2013 | - | Docker | Container-Revolution |
| 2015 | - | [[Windows-10]] | "Windows as a Service" |
| 2020 | Apple M1 | [[macOS]] Big Sur | ARM erobert Desktop |
| 2021 | - | [[Windows-11]] | Neue Ära (TPM, WSL2) |

---

> [!tip] Weiterführende Links - 4. Generation
> - [Xerox Alto - Wikipedia](https://en.wikipedia.org/wiki/Xerox_Alto)
> - [Computer History Museum: Alto](https://www.computerhistory.org/revolution/input-output/14/347)
> - [IBM PC - Wikipedia](https://en.wikipedia.org/wiki/IBM_Personal_Computer)
> - [IBM History: The PC](https://www.ibm.com/history/personal-computer)
> - [Commodore 64 - Wikipedia](https://en.wikipedia.org/wiki/Commodore_64)
> - [C64-Wiki (Community)](https://www.c64-wiki.com/)
> - [Apple Macintosh - Wikipedia](https://en.wikipedia.org/wiki/Macintosh_128K)
> - [Apple's "1984" Ad - Smithsonian](https://americanhistory.si.edu/explore/stories/remembering-apples-1984-super-bowl-ad)
> - [Microsoft Windows History](https://en.wikipedia.org/wiki/Microsoft_Windows_version_history)
> - [History of Linux - Wikipedia](https://en.wikipedia.org/wiki/History_of_Linux)
> - [Ars Technica: How Linux was born](https://arstechnica.com/information-technology/2015/08/how-linux-was-born-as-told-by-linus-torvalds-himself/)
> - [The Linux Foundation](https://www.linuxfoundation.org/)
> - [Android History - Wikipedia](https://en.wikipedia.org/wiki/Android_version_history)
> - [iOS History - Wikipedia](https://en.wikipedia.org/wiki/IOS_version_history)

---

## Pioniere der Informatik

### Frühe Visionäre

| Person | Beitrag |
|--------|---------|
| **Charles Babbage** (1791-1871) | Konzept der "Analytical Engine" - mechanischer Universalrechner |
| **Ada Lovelace** (1815-1852) | Erstes Computerprogramm (für Babbage's Maschine) |
| **Herman Hollerith** (1860-1929) | Lochkarten-Tabelliermaschine, Gründer von IBM-Vorgänger |

### 20. Jahrhundert

| Person | Beitrag |
|--------|---------|
| **Konrad Zuse** (1910-1995) | Erbauer der Z3, erste höhere Programmiersprache (Plankalkül) |
| **Alan Turing** (1912-1954) | Theoretische Grundlagen, Turing-Maschine, Entschlüsselung |
| **John von Neumann** (1903-1957) | Von-Neumann-Architektur (Programm im Speicher) |
| **Grace Hopper** (1906-1992) | Erster Compiler, COBOL, Begriff "Bug" populär gemacht |

> [!tip] Von-Neumann-Architektur
> Die meisten heutigen Computer basieren noch immer auf der Von-Neumann-Architektur:
> - Programm und Daten im selben Speicher
> - Sequentielle Befehlsabarbeitung
> - Zentrale Recheneinheit (CPU)

---

## Wichtige Konzepte der BS-Entwicklung

### Entwicklung der Programmausführung

![[programmausfuehrung-evolution.png]]
*02-01-01-programmausfuehrung-evolution: Die Zuordnung von Benutzern/Jobs zur CPU entwickelte sich über drei Generationen: von der direkten 1:1-Nutzung (ein User belegt die CPU exklusiv) über die sequentielle Batch-Abarbeitung mehrerer Jobs (n:1) bis zum Time-Sharing, bei dem die CPU per Zeitscheiben quasi-parallel zwischen vielen Benutzern wechselt.*

### Evolution der Abstraktionsebenen

1. **Keine Abstraktion** → Direkte Hardware-Programmierung
2. **Batch-Monitore** → Automatisierte Job-Steuerung
3. **Resident Monitors** → Permanente BS-Komponente im Speicher
4. **Time-Sharing OS** → Benutzer-Abstraktion und Ressourcenteilung
5. **Moderne OS** → Vollständige Hardware-Abstraktion, Virtualisierung

---

## Bildergalerie

Alle Bilder befinden sich im Ordner `assets/`:

### Vorgeschichte und 1. Generation

| Datei | Beschreibung | Quelle |
|-------|--------------|--------|
| `industrielle-revolution.jpg` | Fabrikhalle 19. Jahrhundert | Public Domain |
| `jacquard-webstuhl-lochkarten.jpg` | Jacquard-Webstuhl mit Lochkarten | Public Domain |
| `babbage-analytical-engine.jpg` | Babbage's Analytical Engine | Public Domain |
| `hollerith-tabelliermaschine.jpg` | Hollerith-Tabelliermaschine (ca. 1890) | Computer History Museum |
| `hollerith-lochkarte.jpg` | Hollerith-Lochkarte | Public Domain |
| `zuse-z3-deutsches-museum.jpg` | Nachbau der Zuse Z3 | Deutsches Museum, Wikimedia CC BY-SA 3.0 |
| `colossus.jpg` | Colossus Mark 2 in Bletchley Park | TNMOC/GCHQ |
| `eniac.jpg` | ENIAC | U.S. Army Photo (Public Domain) |
| `eniac-programmiererinnen.jpg` | ENIAC-Programmiererinnen "ENIAC Six" | U.S. Army Photo (Public Domain) |

### 2. Generation (Transistoren)

| Datei | Beschreibung | Quelle |
|-------|--------------|--------|
| `harvard-mark-i.jpg` | Harvard Mark I (ASCC) | Harvard University |
| `ibm-7094.jpg` | IBM 7094 Konsole | Computer History Museum |
| `papertape-archiv.jpg` | Lochstreifen-Archiv (Papertape) | - |
| `lochkarten-sortiert.jpg` | Lochkarten sortiert | - |

### 3. Generation (Integrierte Schaltkreise)

| Datei | Beschreibung | Quelle |
|-------|--------------|--------|
| `ibm-system360-mainframe.jpg` | IBM System/360 | Wikimedia Commons |
| `dec-pdp-1.jpg` | DEC PDP-1 | Computer History Museum |
| `dec-pdp-11.jpg` | DEC PDP-11 | Wikimedia Commons |

### 4. Generation (Personal Computer)

| Datei | Beschreibung | Quelle |
|-------|--------------|--------|
| `xerox-alto-maus-1973.jpg` | Xerox Alto mit Maus (1973) | Computer History Museum |
| `ibm-pc-xt-1983.jpg` | IBM PC XT (1983) | Computer History Museum |
| `commodore-c64.jpg` | Commodore 64 (1982) | Wikimedia Commons |
| `zx-spectrum.jpg` | Sinclair ZX Spectrum (1982) | Wikimedia Commons |
| `apple-macintosh-1984.jpg` | Apple Macintosh 128K (1984) | Computer History Museum |
| `frueh-pc-terminal.jpg` | Frühe PC-Workstation | - |

---

## Zusammenhänge

- [[02-Definition]] - Was ist ein Betriebssystem?
- [[03-Aufgaben]] - Aufgaben moderner Betriebssysteme
- [[01-Kerneltypen]] - Wie hat sich die Architektur entwickelt?
- [[01-Prozessmodell]] - Von Single-Task zu Multiprogramming

---

## Prüfungstipps

> [!warning] Prüfungsrelevant
> - Unterschied zwischen Batch-Verarbeitung und Time-Sharing
> - Bedeutung von Multiprogramming und Interrupts
> - **Übergang vom Einprogramm- zum Mehrprogrammbetrieb** (Uniprogramming → Multiprogramming)
> - **CPU-Auslastung**: Formel $1 - p^n$ (p = I/O-Warteanteil, n = Anzahl Prozesse)
> - **Time-Slicing**: Periodischer CPU-Wechsel durch Timer-Interrupt
> - Die Bedeutung offener vs. proprietärer Systeme
> - Wichtige Konzepte der BS-Entwicklung (Direkte Ausführung → Batch → Time-Sharing)
> - Evolution der Abstraktionsebenen (keine Abstraktion → moderne OS mit Virtualisierung)
> - Cloud Computing und Virtualisierung (IaaS, PaaS, SaaS, Container)
> - Das Konzept der Batch-Verarbeitung (Workflow, Vor- und Nachteile, Turnaround Time)
> - Residente Monitore als Vorläufer der Betriebssysteme (Speicher-Layout, Aufgaben, JCL)
> - Hardware-Interrupts (Polling vs. Interrupts, Arten, Bedeutung für Multitasking)
> - Spooling (Simultaneous Peripheral Operations On-Line, Pufferung, Parallelität)

**Typische Prüfungsfragen:**
1. Welche Probleme lösten Batch-Systeme und welche neuen Probleme entstanden?
2. Warum war die Einführung von Interrupts ein wichtiger Meilenstein?
3. Was unterscheidet Multiprogramming von Time-Sharing?
4. Welchen Einfluss hatte UNIX auf moderne Betriebssysteme?
5. Wie unterscheiden sich mobile Betriebssysteme konzeptionell von Desktop-Systemen?
6. Welche Rolle spielte Open Source (Linux) in der Entwicklung moderner Server-Infrastruktur?

> [!info] Interessante Fragen in diesem Zusammenhang (nicht prüfungsrelevant)
> - Die vier Generationen mit ihren Charakteristika und Jahreszahlen
> - Wichtige Pioniere und ihre Beiträge (Zuse, Turing, von Neumann, Hopper, Torvalds)
> - Warum war die offene Architektur des IBM PC sowohl Erfolg als auch Problem für IBM?
> - Was waren die Schlüsselinnovationen des Xerox Alto und wer profitierte davon?

---

## Quellen

- Vorlesung: "Betriebssysteme, Rechnernetze und verteilte Systeme" - Teil 2: Einführung und Historie (IU), Version 2.0, SS 2026
- Tanenbaum, A. S. & Bos, H.: Modern Operating Systems, Kapitel 1
- Silberschatz, Galvin, Gagne: Operating System Concepts, Chapter 1

### Direkte Quellenreferenzen

**Tanenbaum, A. S. & Bos, H.: Modern Operating Systems (5th Edition)**
- Kapitel 1: Introduction
  - 1.1 What Is an Operating System?
  - 1.2 History of Operating Systems
    - 1.2.1 The First Generation (1945-1955): Vacuum Tubes
    - 1.2.2 The Second Generation (1955-1965): Transistors and Batch Systems
    - 1.2.3 The Third Generation (1965-1980): ICs and Multiprogramming
    - 1.2.4 The Fourth Generation (1980-Present): Personal Computers
    - 1.2.5 The Fifth Generation (1990-Present): Mobile Computers
  - 1.3 Computer Hardware Review
  - 1.5 Operating System Concepts (Prozesse, Adressräume, Dateien)

**Silberschatz, A., Galvin, P. B. & Gagne, G.: Operating System Concepts (10th Edition)**
- Chapter 1: Introduction
  - 1.1 What Operating Systems Do
  - 1.2 Computer-System Organization
  - 1.4 Operating-System Structure
  - 1.5 Operating-System Operations (Interrupts, Timer, Dual-Mode)
  - 1.10 Computing Environments (Mobile, Client-Server, Cloud)
- Chapter 2: Operating-System Structures
  - 2.1 Operating-System Services
  - 2.3 System Calls

### Weiterführende Literatur (in der Vorlesung empfohlen)

- Sandner/Spengler: "Die Entwicklung der Datenverarbeitung von Hollerith Lochkartenmaschinen zu IBM Enterprise-Server"
  - URL: http://www.cedix.de/Literature/History/SandnerSpengler.pdf
- Wikibooks: "Computergeschichte: 1900 bis heute"
  - URL: https://de.wikibooks.org/wiki/Computergeschichte:_1900_bis_heute

### Weitere verwendete Quellen

- Turner, L. R. & Rawlings, J. H.: "Realization of Randomly Timed Computer Input and Output by Means of an Interrupt Feature", IRE Transactions on Electronic Computers, EC-7, 2, Juni 1958, S. 141-149
- Smotherman, M.: "History and Overview of Interrupts and Interrupt Systems", Clemson University, 2017
- Gordon College CS322 Lecture Notes: "Operating Systems History"
- Bell, C. G. & Newell, A.: "Computer Structures: Readings and Examples", McGraw-Hill, 1971
- Corbató, F. J., Merwin-Daggett, M. & Daley, R. C.: "An Experimental Time-Sharing System", AFIPS Conference Proceedings, Mai 1962
- IBM History: "Time-Sharing" - https://www.ibm.com/history/time-sharing
- JMU OpenCSF: "Processes and Multiprogramming" - https://users.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/Multiprogramming.html
