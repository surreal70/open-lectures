---
author: Andreas Hümmer
title: 'Lösung: Betriebssysteme (Klausurformat)'
tags:
  - loesung
  - bs
  - klausur
bereich: BS
created: '2026-10-09'
modified: '2026-10-09'
---

# Lösung: Betriebssysteme (Klausurformat)

**Zugehörige Übung:** [[UE-BS-Betriebssysteme|Übung: Betriebssysteme (Klausurformat)]]

---

## Teil 1: Grundlagen und Definition

### Aufgabe 1.1: Definition Betriebssystem

**a) Definition nach Tanenbaum:**

> [!success] **Musterlösung**
> *"Eine Softwareschicht, die alle Teile des Systems verwaltet und dem Benutzer eine Schnittstelle oder virtuelle Maschine anbietet, die leichter zu verstehen und zu programmieren ist (als die zugrundeliegende reale Hardware/Maschine)."*
> 
> Diese Definition betont die **Abstraktion**: Das Betriebssystem verbirgt die Komplexität der Hardware.

**b) Zwei Sichtweisen:**

> [!success] **Musterlösung**
> | Sichtweise | Perspektive | Beschreibung |
> |------------|-------------|--------------|
> | **Top-Down** | Benutzerperspektive | Das BS bietet eine **virtuelle Maschine** mit einheitlichen Schnittstellen (API). Es abstrahiert Hardware-Details und bietet eine komfortable Programmierumgebung. |
> | **Bottom-Up** | Systemperspektive | Das BS ist ein **Ressourcenmanager**, der CPU, Speicher und E/A-Geräte fair und effizient verteilt (zeitliches und räumliches Multiplexing). |

---

### Aufgabe 1.2: Kernaufgaben

> [!success] **Musterlösung**
> | Nr. | Aufgabe | Funktion |
> |-----|---------|----------|
> | 1 | **Schnittstelle** | Bildet die Schnittstelle zwischen Anwendungsprogrammen und Hardware-Komponenten |
> | 2 | **Programmverwaltung** | Organisiert das Laden, Starten und Beenden von Anwendungsprogrammen |
> | 3 | **Ressourcenverwaltung** | Priorisiert und verteilt CPU-, Speicher- und Schnittstellen-Ressourcen |
> | 4 | **Sicherheit** | Gewährleistet Systemsicherheit und Schnittstellenüberwachung |
> | 5 | **Geräteansteuerung** | Steuert mittels Gerätetreibern sämtliche Hardware-Komponenten |
> 
> Weitere mögliche Antworten: Datenverwaltung, Systemaufrufe bereitstellen

---

### Aufgabe 1.3: RTOS vs. General-Purpose OS

> [!success] **Musterlösung**
> | Kriterium | RTOS | General-Purpose OS |
> |-----------|------|-------------------|
> | **Ziel** | Zeitgarantien (Deadlines einhalten) | Durchsatz, Fairness |
> | **Scheduling** | Prioritätsbasiert, deterministisch | Time-Sharing |
> | **Latenz** | Mikrosekunden (garantiert) | Millisekunden (Best-Effort) |
> 
> Weitere Kriterien: Footprint (klein vs. groß), Determinismus (garantiert vs. variabel)

---

## Teil 2: Architektur und Kerneltypen

### Aufgabe 2.1: Kerneltypen

**a) Drei Haupt-Kernel-Architekturen:**

> [!success] **Musterlösung**
> | Architektur | Beispiel-OS |
> |-------------|-------------|
> | **Monolithisch** | Linux, FreeBSD |
> | **Mikrokernel** | MINIX, QNX, seL4 |
> | **Hybrid** | Windows NT, macOS (XNU) |

**b) Vor- und Nachteile monolithischer Kernel:**

> [!success] **Musterlösung**
> | | Monolithischer Kernel |
> |-----------|---------------------|
> | **Vorteile** | 1. Hohe Leistung durch direkte Kommunikation zwischen Komponenten (keine IPC-Overhead) |
> | | 2. Effizienter Ressourcenzugriff ohne Kontextwechsel zwischen Kernel-Komponenten |
> | **Nachteile** | 1. Stabilitätsrisiko: Fehler in einem Treiber können das gesamte System zum Absturz bringen |
> | | 2. Sicherheitsrisiko: Kompromittierter Treiber hat vollen Kernel-Zugriff |

---

### Aufgabe 2.2: Systemaufrufe

**a) Was ist ein Systemaufruf?**

> [!success] **Musterlösung**
> Ein **Systemaufruf** (System Call) ist die fundamentale Schnittstelle zwischen Anwendungsprogrammen im User-Space und dem Betriebssystem-Kernel. Er ermöglicht es Programmen, privilegierte Operationen anzufordern, die nur der Kernel ausführen darf (z.B. Dateien öffnen, Speicher anfordern, Netzwerkverbindungen herstellen).

**b) Ablauf eines Systemaufrufs:**

> [!success] **Musterlösung**
> 1. **User-Mode:** Anwendung ruft Bibliotheksfunktion auf (z.B. `write()`)
> 2. Wrapper legt Syscall-Nummer und Parameter in Register
> 3. **SYSCALL/TRAP-Instruktion** wird ausgelöst
> 4. **Kontextwechsel:** CPU wechselt von Ring 3 (User) zu Ring 0 (Kernel)
> 5. **Kernel-Mode:** Syscall-Handler sichert Register, Dispatcher findet passende Kernel-Funktion
> 6. Kernel-Funktion wird ausgeführt, Ergebnis in Register
> 7. **SYSRET/IRET** kehrt zurück in User-Mode
> 8. Anwendung erhält Ergebnis

---

### Aufgabe 2.3: Privilegienstufen

> [!success] **Musterlösung**
> | Aspekt | User-Mode (Ring 3) | Kernel-Mode (Ring 0) |
> |--------|-------------------|---------------------|
> | **Zugriff** | Eingeschränkt, nur eigener Adressraum | Voller Hardware-Zugriff |
> | **Instruktionen** | Nur nicht-privilegierte | Alle CPU-Instruktionen |
> | **Fehlerfolgen** | Absturz betrifft nur den Prozess | Absturz betrifft gesamtes System |
> 
> **Grund für Trennung:** Sicherheit und Stabilität. Ein fehlerhaftes oder bösartiges Anwendungsprogramm soll nicht das gesamte System gefährden können. Nur geprüfter Kernel-Code darf auf Hardware zugreifen.

---

## Teil 3: Prozesse

### Aufgabe 3.1: Prozess vs. Programm

> [!success] **Musterlösung**
> | Aspekt | Programm | Prozess |
> |--------|----------|---------|
> | **Zustand** | Passiv (Datei auf Festplatte) | Aktiv (in Ausführung) |
> | **Speicher** | Statisch gespeichert | Dynamisch im RAM |
> | **Ressourcen** | Keine | CPU-Zeit, Speicher, Dateien |
> | **Analogie** | Kochrezept (statische Anleitung) | Kochvorgang (aktive Ausführung) |
> 
> Ein Programm kann mehrere Prozesse erzeugen (wie ein Rezept von mehreren Köchen gleichzeitig ausgeführt werden kann).

---

### Aufgabe 3.2: Prozesszustände

**a) Drei-Zustands-Modell:**

> [!success] **Musterlösung**
> ```
>                    Dispatch
>         ┌──────────────────────────────┐
>         │                              ▼
>     ┌───────┐                      ┌─────────┐
>     │ Ready │◄────Wakeup──────────│ Running │
>     └───────┘                      └────┬────┘
>         ▲        Timeout/              │
>         │        Preemption            │ Block
>         │            ▲                 │
>         │            │                 ▼
>         │        ┌───┴───┐        ┌─────────┐
>         └────────│       │        │ Blocked │
>                  └───────┘        └─────────┘
> ```

**b) Zustandsübergänge:**

> [!success] **Musterlösung**
> | Übergang | Auslösendes Ereignis |
> |----------|---------------------|
> | Ready → Running | **Dispatch:** Scheduler wählt Prozess aus (CPU frei, höchste Priorität) |
> | Running → Ready | **Timeout/Preemption:** Zeitscheibe abgelaufen oder höher-priorer Prozess bereit |
> | Running → Blocked | **Block:** Prozess wartet auf E/A-Operation (z.B. read(), scanf()) |
> | Blocked → Ready | **Wakeup:** E/A-Operation abgeschlossen, Prozess wieder rechenbereit |

---

### Aufgabe 3.3: Process Control Block

> [!success] **Musterlösung**
> | Kategorie | Beispiel |
> |-----------|----------|
> | **Identifikation** | PID (Prozess-ID), PPID (Parent-PID), UID (User-ID) |
> | **CPU-Kontext** | Programmzähler (PC), Register, Stack-Pointer |
> | **Speicherinfo** | Seitentabellen, Segmentgrenzen, Adressraum-Grenzen |
> | **Ressourcen** | Offene Dateien (File Descriptors), Geräte, Sockets |
> | **Scheduling** | Priorität, Zustand (Running/Ready/Blocked), verbrauchte CPU-Zeit |

---

## Teil 4: Scheduling

### Aufgabe 4.1: Scheduling-Grundlagen

**a) Preemptive vs. Non-Preemptive:**

> [!success] **Musterlösung**
> | Eigenschaft | Preemptive | Non-Preemptive |
> |-------------|------------|----------------|
> | **Verdrängung** | Scheduler kann laufenden Prozess jederzeit unterbrechen | Prozess läuft bis er freiwillig abgibt (Beendigung/Blockierung) |
> | **Beispiel-Algorithmus** | Round Robin, SRTF, MLFQ | FCFS, SJF |

**b) Warum preemptive?**

> [!success] **Musterlösung**
> Preemptive Scheduling gewährleistet **schnelle Reaktionszeiten** und verhindert, dass ein einziger Prozess die CPU monopolisiert. Interaktive Anwendungen (GUI, Browser) reagieren dadurch sofort auf Benutzereingaben, auch wenn im Hintergrund rechenintensive Aufgaben laufen.

---

### Aufgabe 4.2: Scheduling-Algorithmen

> [!success] **Musterlösung**
> | Algorithmus | Beschreibung | Vorteil | Nachteil |
> |-------------|--------------|---------|----------|
> | **FCFS** | First Come First Serve – Prozesse werden in Ankunftsreihenfolge abgearbeitet | Einfach zu implementieren, keine Starvation | Convoy-Effekt: lange Prozesse blockieren kurze |
> | **Round Robin** | Jeder Prozess erhält eine feste Zeitscheibe (Quantum), dann wird gewechselt | Faire CPU-Verteilung, gute Antwortzeiten | Overhead durch Kontextwechsel, Quantum-Wahl kritisch |
> | **SJF** | Shortest Job First – kürzester Prozess wird zuerst ausgeführt | Optimal für durchschnittliche Wartezeit | Starvation langer Prozesse, Burst-Zeit muss geschätzt werden |

---

### Aufgabe 4.3: Scheduling-Berechnung

> [!success] **Musterlösung**
> **FCFS-Reihenfolge:** P1 → P2 → P3 (nach Ankunftszeit)
> 
> | Prozess | Ankunft | Burst | Startzeit | Endzeit | Wartezeit |
> |---------|---------|-------|-----------|---------|-----------|
> | P1 | 0 | 8 | 0 | 8 | 0 - 0 = **0** |
> | P2 | 1 | 4 | 8 | 12 | 8 - 1 = **7** |
> | P3 | 2 | 2 | 12 | 14 | 12 - 2 = **10** |
> 
> **Durchschnittliche Wartezeit:** (0 + 7 + 10) / 3 = **17/3 ≈ 5,67**
> 
> **Erklärung:** Die Wartezeit ist die Zeit, die ein Prozess in der Ready-Queue verbringt, also Startzeit minus Ankunftszeit.

---

## Teil 5: Threads

### Aufgabe 5.1: Thread-Grundlagen

**a) Was ist ein Thread?**

> [!success] **Musterlösung**
> Ein **Thread** (leichtgewichtiger Prozess) ist eine Ausführungseinheit innerhalb eines Prozesses. Threads eines Prozesses teilen sich den Adressraum und Ressourcen, besitzen aber jeweils einen eigenen Stack und Registersatz.
> 
> **Unterschied zu Prozess:** Prozesse haben getrennte Adressräume (isoliert), Threads teilen sich denselben Adressraum (können direkt kommunizieren). Thread-Erzeugung und -Wechsel ist deutlich schneller als bei Prozessen.

**b) Geteilte und nicht-geteilte Ressourcen:**

> [!success] **Musterlösung**
> | Geteilt (pro Prozess) | Nicht geteilt (pro Thread) |
> |-----------------------|---------------------------|
> | Adressraum (Code, Heap) | Stack |
> | Globale Variablen | Programmzähler (PC) |
> | Offene Dateien (File Descriptors) | Register |
> | Code-Segment | Thread-ID, Priorität |

---

### Aufgabe 5.2: User-Level vs. Kernel-Level Threads

> [!success] **Musterlösung**
> | Kriterium | User-Level Threads | Kernel-Level Threads |
> |-----------|-------------------|---------------------|
> | **Kontextwechsel** | Sehr schnell (kein Kernel nötig, nur User-Space-Bibliothek) | Langsamer (Syscall für Wechsel erforderlich) |
> | **Multicore-Nutzung** | Nein, alle Threads laufen auf einem Kern | Ja, echte Parallelität auf mehreren Kernen |
> | **Blockierender Syscall** | Ganzer Prozess blockiert (alle User-Threads warten) | Nur der eine Thread blockiert, andere laufen weiter |

---

### Aufgabe 5.3: Multithreading vs. Multiprocessing

> [!success] **Musterlösung**
> | Begriff | Ebene | Beschreibung |
> |---------|-------|--------------|
> | **Multithreading** | Innerhalb Prozess | Quasi-gleichzeitiges Abarbeiten mehrerer Threads **desselben** Prozesses |
> | **Multitasking** | OS-Ebene | Quasi-gleichzeitiges Abarbeiten mehrerer **Prozesse** (Time-Sharing) |
> | **Multiprocessing** | Hardware-Ebene | **Echtes** gleichzeitiges Abarbeiten auf mehreren Prozessoren/Kernen |

---

## Teil 6: Synchronisation

### Aufgabe 6.1: Kritische Abschnitte

**a) Was ist ein kritischer Abschnitt?**

> [!success] **Musterlösung**
> Ein **kritischer Abschnitt** ist ein Programmabschnitt, in dem auf **gemeinsame Ressourcen** (Shared Resources) zugegriffen wird. Er darf nur von einem Prozess/Thread zur gegebenen Zeit durchlaufen werden, um Race Conditions zu vermeiden.

**b) Drei Anforderungen:**

> [!success] **Musterlösung**
> | Anforderung | Beschreibung |
> |-------------|--------------|
> | **Mutual Exclusion** | Höchstens ein Prozess darf sich zu jedem Zeitpunkt im kritischen Abschnitt befinden |
> | **Progress** | Wenn kein Prozess im kritischen Abschnitt ist und mindestens einer eintreten möchte, muss die Entscheidung in endlicher Zeit fallen |
> | **Bounded Waiting** | Es gibt eine obere Schranke, wie oft andere Prozesse eintreten dürfen, während ein bestimmter Prozess wartet |

---

### Aufgabe 6.2: Race Conditions

**a) Was ist eine Race Condition?**

> [!success] **Musterlösung**
> Eine **Race Condition** (Wettlaufsituation) tritt auf, wenn das Ergebnis einer Berechnung vom **zeitlichen Ablauf** nebenläufiger Operationen abhängt. Das Ergebnis ist nicht deterministisch und kann bei verschiedenen Durchläufen unterschiedlich sein.

**b) Warum ist `x++` nicht atomar?**

> [!success] **Musterlösung**
> Die Operation `x++` besteht auf Maschinenebene aus drei Schritten:
> 
> ```
> 1. LOAD  x → Register    (Wert aus Speicher in Register laden)
> 2. ADD   1 → Register    (1 zum Registerwert addieren)
> 3. STORE Register → x    (Ergebnis zurück in Speicher schreiben)
> ```
> 
> **Problem:** Zwischen jedem dieser Schritte kann ein Kontextwechsel stattfinden. Wenn zwei Threads gleichzeitig `x++` ausführen:
> - Thread A: LOAD x=5
> - *Kontextwechsel*
> - Thread B: LOAD x=5, ADD 6, STORE 6
> - *Kontextwechsel*
> - Thread A: ADD 6, STORE 6
> - **Ergebnis:** x=6 statt x=7 (ein Inkrement verloren!)

---

### Aufgabe 6.3: Deadlocks

**a) Coffman-Bedingungen:**

> [!success] **Musterlösung**
> | Bedingung | Erklärung |
> |-----------|-----------|
> | **Mutual Exclusion** | Ressourcen können nur von einem Prozess gleichzeitig genutzt werden |
> | **Hold and Wait** | Ein Prozess hält Ressourcen und wartet auf weitere |
> | **No Preemption** | Ressourcen können nur freiwillig freigegeben werden, nicht entzogen |
> | **Circular Wait** | Es existiert eine zyklische Kette wartender Prozesse (P1→P2→...→Pn→P1) |
> 
> **Wichtig:** Alle vier Bedingungen müssen gleichzeitig erfüllt sein!

**b) Zwei Deadlock-Strategien:**

> [!success] **Musterlösung**
> | Strategie | Beschreibung |
> |-----------|--------------|
> | **Prevention** | Eine der vier Coffman-Bedingungen strukturell unmöglich machen (z.B. Ressourcen-Ordnung gegen Circular Wait: alle Ressourcen durchnummerieren, nur in aufsteigender Reihenfolge anfordern) |
> | **Detection** | Deadlocks zulassen, aber periodisch erkennen (z.B. durch Zyklensuche im Resource Allocation Graph) und dann beheben (Prozess abbrechen, Ressourcen entziehen) |
> 
> Weitere: Avoidance (Banker's Algorithm), Ignorance (Ostrich Algorithm)

---

### Aufgabe 6.4: Semaphore

**a) P und V Operationen:**

> [!success] **Musterlösung**
> | Operation | Semantik |
> |-----------|----------|
> | **P(S)** | *wait/down/acquire:* Wenn S > 0: dekrementiere S und fahre fort. Sonst: blockiere den Prozess bis S > 0 wird. |
> | **V(S)** | *signal/up/release:* Inkrementiere S. Falls Prozesse auf S warten, wecke einen davon auf. |

**b) Mutex vs. Semaphor:**

> [!success] **Musterlösung**
> | Eigenschaft | Mutex | Semaphor |
> |-------------|-------|----------|
> | **Wertebereich** | 0 oder 1 (binär) | 0 bis N (beliebig nicht-negativ) |
> | **Ownership** | Nur der Besitzer (der Thread, der gelockt hat) kann freigeben | Jeder kann V aufrufen (kein Ownership) |
> | **Typischer Einsatz** | Schutz kritischer Abschnitte (exklusiver Zugriff) | Ressourcenzählung, Producer-Consumer, Signalisierung |

---

## Teil 7: Speicherverwaltung

### Aufgabe 7.1: Virtueller Speicher

**a) Was ist virtueller Speicher?**

> [!success] **Musterlösung**
> **Virtueller Speicher** ist eine Technik, die den Hauptspeicher durch Auslagern auf die Festplatte (Swap) erweitert. Jeder Prozess erhält einen eigenen virtuellen Adressraum, der größer sein kann als der physisch vorhandene RAM.
> 
> **Gelöstes Problem:** Programme können mehr Speicher nutzen als physisch vorhanden ist. Zudem wird Speicherschutz ermöglicht (Prozesse sehen nur ihren eigenen Adressraum).

**b) Was ist ein Page Fault?**

> [!success] **Musterlösung**
> Ein **Page Fault** (Seitenfehler) tritt auf, wenn ein Prozess auf eine Speicherseite zugreift, die sich nicht im physischen Hauptspeicher befindet (ausgelagert auf Festplatte).
> 
> **Ablauf:**
> 1. CPU löst Trap/Interrupt aus
> 2. Betriebssystem prüft, ob Zugriff gültig
> 3. Freien Frame finden (ggf. Page ersetzen)
> 4. Page von Festplatte einlesen
> 5. Page Table aktualisieren
> 6. Prozess fortsetzen

---

### Aufgabe 7.2: Paging

**a) Page und Frame:**

> [!success] **Musterlösung**
> | Begriff | Beschreibung |
> |---------|--------------|
> | **Page** | Block fester Größe im **virtuellen** Adressraum eines Prozesses (typisch 4 KB) |
> | **Frame (Kachel)** | Block gleicher Größe im **physischen** Speicher (RAM), nimmt eine Page auf |

**b) Page-Table-Eintrag:**

> [!success] **Musterlösung**
> | Information | Bedeutung |
> |-------------|-----------|
> | **Frame Number** | Adresse des zugehörigen Frames im physischen Speicher |
> | **Valid Bit** | 1 = Page ist im RAM, 0 = ausgelagert (auf Festplatte) |
> | **Modified Bit** | 1 = Page wurde verändert (Dirty Bit), muss bei Ersetzung zurückgeschrieben werden |
> | **Referenced Bit** | 1 = Page wurde kürzlich zugegriffen (für Ersetzungsalgorithmen) |
> | **Protection Bits** | Zugriffsrechte (Read, Write, Execute) |

**c) TLB:**

> [!success] **Musterlösung**
> Der **TLB** (Translation Lookaside Buffer) ist ein schneller Hardware-Cache in der CPU, der kürzlich verwendete Page-Table-Einträge speichert.
> 
> **Zweck:** Ohne TLB erfordert jeder Speicherzugriff zwei RAM-Zugriffe (Page Table + Daten). Mit TLB kann die Adressübersetzung bei einem Hit in ~1ns erfolgen statt ~100ns (RAM-Zugriff).

---

### Aufgabe 7.3: Page-Ersetzung

> [!success] **Musterlösung**
> | Algorithmus | Beschreibung | Vor-/Nachteil |
> |-------------|--------------|---------------|
> | **FIFO** | First In, First Out – älteste Page wird ersetzt | Einfach zu implementieren, aber Belady's Anomalie (mehr Frames können mehr Page Faults verursachen) |
> | **LRU** | Least Recently Used – am längsten nicht benutzte Page wird ersetzt | Optimal in der Praxis, aber aufwendig zu implementieren (Zeitstempel oder Stack nötig) |
> | **Clock** | Second Chance – Zeiger läuft im Kreis, Pages mit R=1 bekommen zweite Chance | Guter Kompromiss zwischen Einfachheit und Leistung, approximiert LRU |
> 
> Weitere: LFU (Least Frequently Used), OPT (theoretisch optimal, kennt Zukunft)

---

## Quellen

- [[02-Definition|Definition eines Betriebssystems]]
- [[03-Aufgaben|Aufgaben eines Betriebssystems]]
- [[01-Kerneltypen|Kerneltypen]]
- [[03-Systemaufrufe|Systemaufrufe]]
- [[01-Prozessmodell|Prozessmodell]]
- [[02-Scheduling|Scheduling]]
- [[03-Threads|Threads]]
- [[02-Kritische-Abschnitte|Kritische Abschnitte]]
- [[03-Race-Conditions|Race Conditions]]
- [[04-Deadlocks|Deadlocks]]
- [[05-Synchronisationsmechanismen|Synchronisationsmechanismen]]
- [[02-Virtueller-Speicher|Virtueller Speicher]]
- [[03-Paging|Paging]]
