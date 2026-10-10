---
author: Andreas Hümmer
title: Scheduling
tags:
  - content
  - bs
  - prozesse
  - scheduling
  - fcfs
  - round-robin
  - sjf
created: '2026-10-07'
modified: '2026-10-09'
bereich: BS
---

# Scheduling

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das Basisziel des Schedulings erklären können
> - Verschiedene Scheduling-Algorithmen kennen und unterscheiden können
> - Preemptive vs. Non-Preemptive Scheduling verstehen
> - Die Ziele und Kriterien für Scheduling-Entscheidungen kennen
> - Konkrete Beispiele für Scheduling-Strategien durchrechnen können

---

## Definition

> [!quote] **Formale Definition**
> **Scheduling** ist der Prozess der geordneten CPU-Zuteilung an konkurrierende Prozesse durch einen Scheduler-Algorithmus.

In einem Multitasking-Betriebssystem möchten mehrere Prozesse gleichzeitig die CPU nutzen. Da in der Regel nur eine begrenzte Anzahl von CPUs (oder CPU-Kernen) vorhanden ist, muss das Betriebssystem entscheiden, welcher Prozess zu welchem Zeitpunkt ausgeführt wird. Diese Entscheidung trifft der **Scheduler** – eine zentrale Komponente des Betriebssystem-Kernels.

---

## Grundlegendes

### Basisziel

Das Basisziel des Schedulings ist der **geordnete Ablauf konkurrierender Prozesse**. Ohne Scheduling würde ein Prozess die CPU monopolisieren, bis er beendet ist – andere Prozesse müssten warten, egal wie dringend ihre Aufgaben sind.

![[assets/scheduler-overview.png]]
<span class="fig-id">02-03-02-scheduler-overview</span> *Übersicht des Scheduling-Ablaufs: Prozesse gelangen in die Ready-Queue, der Scheduler wählt einen aus, dieser erhält die CPU und wird entweder beendet oder verdrängt – im letzteren Fall kehrt er in die Warteschlange zurück.*

Der Scheduler wird in verschiedenen Situationen aktiv:
- Ein neuer Prozess wird erzeugt (fork)
- Ein laufender Prozess beendet sich (exit)
- Ein Prozess blockiert (z.B. auf I/O-Wartezeit)
- Ein Interrupt tritt auf (z.B. Timer-Interrupt)
- Ein blockierter Prozess wird wieder bereit (z.B. I/O abgeschlossen)

### Scheduling-Ziele

Die Ziele des Schedulings hängen stark vom Einsatzbereich des Systems ab. Ein Webserver hat andere Anforderungen als ein Echtzeitsystem in einem Auto.

| Ziel | Beschreibung | Typisches System |
|------|--------------|------------------|
| **Kurze Antwortzeiten** | Schnelle Reaktion auf Benutzereingaben | Desktop, Smartphone |
| **Optimale CPU-Auslastung** | CPU möglichst nicht im Leerlauf | Server, Cloud |
| **Hoher Durchsatz** | Viele Aufträge pro Zeiteinheit | Batch-Systeme |
| **Fairness** | Alle Prozesse erhalten CPU-Zeit | Mehrbenutzersysteme |
| **Echtzeitverhalten** | Garantierte Reaktionszeiten | Embedded, Industriesteuerung |
| **Energieeffizienz** | Minimaler Stromverbrauch | Mobile Geräte, IoT |

> [!note] **Wichtig**
> Es gibt kein "one fits all" – Zielsetzungen müssen für jedes System individuell festgelegt werden! Manche Ziele stehen sogar im Konflikt: Maximale CPU-Auslastung kann zu längeren Antwortzeiten führen.

### Scheduling-Metriken

Um Scheduling-Algorithmen zu vergleichen, werden verschiedene Metriken verwendet:

| Metrik | Formel | Bedeutung |
|--------|--------|-----------|
| **Wartezeit** | Zeit in Ready-Queue | Zeit, die ein Prozess auf CPU wartet |
| **Turnaround-Zeit** | Endzeit − Ankunftszeit | Gesamtzeit vom Ankommen bis Beenden |
| **Antwortzeit** | Erste CPU-Zuteilung − Ankunft | Zeit bis zur ersten Reaktion |
| **Durchsatz** | Prozesse / Zeiteinheit | Anzahl abgeschlossener Prozesse |
| **CPU-Auslastung** | Aktive Zeit / Gesamtzeit | Prozentsatz der CPU-Nutzung |

---

## Preemptive vs. Non-Preemptive

Bevor wir die einzelnen Algorithmen betrachten, ist es wichtig, den fundamentalen Unterschied zwischen den zwei Scheduling-Ansätzen zu verstehen:

### Non-Preemptive (kooperativ)

Bei non-preemptive Scheduling behält ein Prozess die CPU, bis er sie **freiwillig** abgibt:
- Der Prozess beendet sich (exit)
- Der Prozess blockiert auf I/O oder eine Ressource

Der Scheduler kann einen laufenden Prozess **nicht** unterbrechen. Dies ist einfacher zu implementieren, aber problematisch wenn ein Prozess die CPU "monopolisiert".

### Preemptive (verdrängend)

Bei preemptive Scheduling kann der Scheduler einen laufenden Prozess **jederzeit** unterbrechen und die CPU einem anderen Prozess zuweisen. Dies geschieht typischerweise durch einen Timer-Interrupt, der regelmäßig auslöst (z.B. alle 10ms).

| Eigenschaft | Non-Preemptive | Preemptive |
|-------------|----------------|------------|
| **Verdrängung** | Nein | Ja |
| **Kontextwechsel** | Nur bei Beendigung/Blockierung | Jederzeit möglich |
| **Antwortzeiten** | Schlechter | Besser |
| **Overhead** | Geringer | Höher |
| **Implementierung** | Einfacher | Komplexer |
| **Beispiele** | FCFS, SJF | RR, SRTF, MLFQ |

> [!tip] **Moderne Systeme**
> Alle modernen Desktop- und Server-Betriebssysteme (Windows, Linux, macOS) verwenden preemptive Scheduling, um schnelle Reaktionszeiten zu gewährleisten.

---

## Scheduling-Strategien

### Übersicht

| Kategorie | Algorithmen | Charakteristik |
|-----------|-------------|----------------|
| **Einfach** | FCFS (First Come First Serve) | Ankunftsreihenfolge |
| **Zeitscheibenbasiert** | RR (Round Robin), VRR | Faire Zeitverteilung |
| **Vorhersagebasiert** | SPN/SJF, SRTF, HRRN | Optimiert Wartezeiten |
| **Prioritätenbasiert** | FB, MLQ, MLFQ | Dynamische Anpassung |

---

### 1. FCFS – First Come First Serve

**Non-Preemptive**: Prozesse werden strikt in Ankunftsreihenfolge abgearbeitet – wie eine Warteschlange an der Supermarktkasse.

**Algorithmus:**
1. Neuer Prozess wird ans Ende der Ready-Queue gestellt
2. Wenn CPU frei, wird der erste Prozess aus der Queue genommen
3. Prozess läuft bis zur Beendigung oder Blockierung

![[assets/fcfs-example.png]]
<span class="fig-id">02-03-02-fcfs-example</span> *FCFS-Beispiel: P1 blockiert P2 und P3 trotz kurzer Burst-Zeiten.*

| Vorteile | Nachteile |
|----------|-----------|
| Einfach zu implementieren | **Convoy-Effekt**: lange Prozesse blockieren kurze |
| Fair in Bezug auf Reihenfolge | Schlechte durchschnittliche Wartezeiten |
| Kein Starvation möglich | Ungeeignet für interaktive Systeme |

> [!example] **Convoy-Effekt**
> Stell dir vor, du stehst mit einem Artikel an der Kasse, aber vor dir ist jemand mit einem vollen Einkaufswagen. Du musst warten, obwohl du in Sekunden fertig wärst. Genau das passiert bei FCFS, wenn ein CPU-intensiver Prozess vor vielen kurzen I/O-Prozessen steht.

---

### 2. Round Robin (RR)

**Preemptive**: Jeder Prozess erhält eine feste Zeitscheibe (Quantum). Nach Ablauf wird er unterbrochen und ans Ende der Queue gestellt – wie ein Karussell, bei dem jeder eine Runde fahren darf.

**Algorithmus:**
1. Prozesse werden in einer zirkulären Queue verwaltet
2. Der erste Prozess erhält die CPU für maximal ein Quantum
3. Nach Ablauf: Prozess wird unterbrochen und ans Ende gestellt
4. Nächster Prozess aus der Queue erhält die CPU

![[assets/round-robin-example.png]]
<span class="fig-id">02-03-02-round-robin-example</span> *Round-Robin-Beispiel: P2 und P3 beenden vor Ablauf ihres Quantums, P1 erhält die verbleibende Zeit.*

| Vorteile | Nachteile |
|----------|-----------|
| Faire CPU-Verteilung | Overhead durch Kontextwechsel |
| Gute Antwortzeiten | Quantum-Wahl kritisch |
| Keine Starvation | Längere Turnaround-Zeit als SJF |

**Die Quantum-Wahl ist entscheidend:**

| Quantum | Effekt |
|---------|--------|
| **Zu klein** (< 10ms) | Viele Kontextwechsel, hoher Overhead |
| **Zu groß** (> 100ms) | Nähert sich FCFS an, schlechte Antwortzeiten |
| **Optimal** (10-100ms) | Balance zwischen Overhead und Reaktionszeit |

> [!note] **Typische Werte**
> - Linux: 4ms (interaktiv) bis 40ms (Batch)
> - Windows: ca. 20ms (variabel je nach Prozesstyp)

---

### 3. SJF/SPN – Shortest Job First

**Non-Preemptive**: Der Prozess mit der kürzesten (geschätzten) Ausführungszeit wird zuerst ausgeführt – wie die Expresskasse für Kunden mit wenigen Artikeln.

**Algorithmus:**
1. Alle bereiten Prozesse nach Burst-Zeit sortieren
2. Den kürzesten Prozess zur Ausführung auswählen
3. Prozess läuft bis zur Beendigung

![[assets/sjf-example.png]]
<span class="fig-id">02-03-02-sjf-example</span> *SJF-Beispiel: Prozesse werden nach Burst-Zeit sortiert, kürzeste zuerst.*

| Vorteile | Nachteile |
|----------|-----------|
| **Optimal** für durchschnittliche Wartezeit | Burst-Zeit muss bekannt/geschätzt werden |
| Ideal für Batch-Systeme | **Starvation** langer Prozesse möglich |
| Mathematisch beweisbar optimal | Nicht praktikabel für interaktive Systeme |

> [!danger] **Starvation-Problem**
> Ein langer Prozess kann theoretisch unendlich warten, wenn ständig neue kurze Prozesse ankommen. In der Praxis ein ernstes Problem!

**Burst-Zeit-Schätzung:**

Da die tatsächliche Burst-Zeit im Voraus nicht bekannt ist, wird sie geschätzt – meist durch **exponentielles Glätten** der vorherigen Burst-Zeiten:

```
τ(n+1) = α × t(n) + (1-α) × τ(n)

wobei:
- τ(n+1) = geschätzte nächste Burst-Zeit
- t(n)   = tatsächliche letzte Burst-Zeit  
- τ(n)   = vorherige Schätzung
- α      = Gewichtungsfaktor (typisch 0.5)
```

---

### 4. SRTF – Shortest Remaining Time First

**Preemptive** Version von SJF: Der Prozess mit der kürzesten **verbleibenden** Ausführungszeit wird ausgeführt. Wenn ein neuer Prozess mit kürzerer verbleibender Zeit ankommt, wird der aktuelle verdrängt.

**Algorithmus:**
1. Bei jedem Scheduling-Ereignis: prüfe alle bereiten Prozesse
2. Wähle den mit der kürzesten verbleibenden Zeit
3. Verdränge aktuellen Prozess falls nötig

![[assets/srtf-example.png]]
<span class="fig-id">02-03-02-srtf-example</span> *SRTF-Beispiel: P2 verdrängt P1 bei Ankunft, da seine verbleibende Zeit kürzer ist.*

| Vorteile | Nachteile |
|----------|-----------|
| Optimal für durchschnittliche Wartezeit | Noch höherer Overhead als RR |
| Besser als SJF bei unterschiedlichen Ankunftszeiten | Starvation-Problem bleibt |
| | Häufige Kontextwechsel möglich |

---

### 5. HRRN – Highest Response Ratio Next

HRRN löst das Starvation-Problem von SJF, indem es die **Wartezeit** in die Entscheidung einbezieht. Je länger ein Prozess wartet, desto höher wird seine Priorität.

**Response Ratio:**

```
                   Wartezeit + Bedienzeit      W + S
Response Ratio = ───────────────────────── = ───────
                       Bedienzeit                S
```

**Eigenschaften:**
- Für neue Prozesse: RR = 1 (Wartezeit = 0)
- Mit zunehmender Wartezeit steigt RR
- Kurze Prozesse werden bevorzugt (wie SJF)
- Aber lange Prozesse "altern" und erhöhen ihre Priorität

| Vorteile | Nachteile |
|----------|-----------|
| Keine Starvation durch **Aging** | Komplexere Berechnung |
| Gute durchschnittliche Wartezeiten | Burst-Zeit muss geschätzt werden |
| Fairer als SJF | Non-preemptive |

---

### 6. Multi-Level Queue (MLQ)

Bei MLQ werden Prozesse in **verschiedene Kategorien** eingeteilt, die jeweils eine eigene Warteschlange mit eigenem Scheduling-Algorithmus haben.

**Typische Aufteilung:**
1. **Systemprozesse** (höchste Priorität)
2. **Interaktive Prozesse** (z.B. GUI-Anwendungen)
3. **Interaktive Editoren** (z.B. Texteditoren)
4. **Batch-Prozesse** (niedrigste Priorität)

Innerhalb jeder Queue kann ein anderer Algorithmus verwendet werden (z.B. RR für interaktive, FCFS für Batch).

> [!warning] **Problem**
> Ein Prozess bleibt dauerhaft in seiner Queue – er kann nicht aufsteigen oder absteigen. Dies ist unflexibel und kann zu Starvation führen.

---

### 7. Multi-Level Feedback Queue (MLFQ)

MLFQ ist die **flexiblere Variante** von MLQ: Prozesse können zwischen Queues wechseln, basierend auf ihrem Verhalten. Dies kombiniert die Vorteile mehrerer Algorithmen.

![[assets/mlfq.png]]
<span class="fig-id">02-03-02-mlfq</span> *Multi-Level Feedback Queue: Neue Prozesse starten oben, sinken bei CPU-Verbrauch ab, können durch Priority Boost wieder aufsteigen.*

**Regeln:**

| Regel | Beschreibung |
|-------|--------------|
| **Regel 1** | Neue Prozesse starten in der höchsten Queue (Queue 0) |
| **Regel 2** | Wenn ein Prozess sein Quantum verbraucht, steigt er ab |
| **Regel 3** | Wenn ein Prozess vor Quantum-Ende blockiert (I/O), bleibt er in seiner Queue |
| **Regel 4** | Nach einer bestimmten Zeit werden alle Prozesse in die höchste Queue zurückgesetzt (**Priority Boost**) |
| **Regel 5** | CPU-Zeit wird über alle Quanten hinweg gezählt (**Gaming Prevention**) |

**Warum funktioniert MLFQ gut?**

- **Interaktive Prozesse** (viel I/O, kurze CPU-Bursts) bleiben in hohen Queues → schnelle Reaktion
- **CPU-intensive Prozesse** sinken in niedrige Queues → werden nicht bevorzugt, aber auch nicht ausgehungert
- **Priority Boost** verhindert Starvation und passt sich an Verhaltensänderungen an

> [!tip] **Praxisrelevanz**
> MLFQ (oder Varianten davon) wird in vielen modernen Betriebssystemen verwendet, darunter BSD, Solaris und teilweise in Linux und Windows.

---

## Scheduling in der Praxis

### Linux: Completely Fair Scheduler (CFS)

Seit Linux 2.6.23 verwendet Linux den **Completely Fair Scheduler**:

- Verwendet einen Rot-Schwarz-Baum statt Queues
- Jeder Prozess hat eine "virtuelle Laufzeit" (vruntime)
- Der Prozess mit der niedrigsten vruntime wird ausgewählt
- Gewichtung nach nice-Wert möglich

```bash
# Prozess mit niedriger Priorität starten
nice -n 19 ./mein_programm

# Priorität eines laufenden Prozesses ändern
renice -n 10 -p 1234
```

### Windows: Priority-Based Preemptive Scheduling

Windows verwendet ein prioritätsbasiertes System mit 32 Prioritätsstufen:

- **0**: System-Idle
- **1-15**: Variable Prioritäten (normale Anwendungen)
- **16-31**: Echtzeit-Prioritäten

```powershell
# Prozess mit hoher Priorität starten
Start-Process -FilePath "programm.exe" -Priority High
```

---

## Zusammenhänge

- [[01-Prozessmodell|Prozessmodell]] → Prozesszustände werden durch Scheduler verändert
- [[03-Threads|Threads]] → Können ebenfalls geschedult werden (Thread-Scheduling)
- [[01-Kritische-Abschnitte|Kritische Abschnitte]] → Scheduling kann Race Conditions beeinflussen

---

## Praktische Tools

> [!note] **AnimOS – Interaktives Tool**
> Die TU Dortmund bietet ein interaktives Scheduling-Tool:
> https://ess.cs.tu-dortmund.de/Software/AnimOS/CPU-Scheduling/
> 
> Damit können verschiedene Algorithmen visualisiert und verglichen werden.

### Praxisübung

- [[P-BS-Scheduling-AnimOS|Praxisübung: CPU-Scheduling mit AnimOS]] – Hands-on Übung mit AnimOS
- [[LOE-P-BS-Scheduling-AnimOS|Lösungen zur Praxisübung]]

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - Unterschied Preemptive vs. Non-Preemptive
> - FCFS, Round Robin, SJF/SPN verstehen
> - Multi-Level Feedback Queue Konzept
> - Vor- und Nachteile der Algorithmen
> - Starvation-Problem und Lösungsansätze

> [!question] **Häufige Prüfungsfragen**
> 1. Was ist der Convoy-Effekt bei FCFS?
> 2. Erklären Sie den Unterschied zwischen preemptive und non-preemptive Scheduling!
> 3. Wie funktioniert eine Multi-Level Feedback Queue?
> 4. Warum ist SJF optimal für die durchschnittliche Wartezeit?

> [!tip] **Merkhilfen**
> - **FCFS** = "Warteschlange an der Kasse" (wer zuerst da ist)
> - **RR** = "Karussell" (jeder bekommt eine Runde)
> - **SJF** = "Expresskasse" (wenige Artikel zuerst)
> - **MLFQ** = "Aufzug mit Gedächtnis" (neu oben, bei Verzögerung nach unten, aber mit Chance wieder hoch)

---

## Weiterführende Ressourcen

> [!note] **Videos (YouTube)**
> 
> | | Video | Beschreibung |
> |---|-------|--------------|
> | 🎬 | [CoreDumped – Scheduling](https://www.youtube.com/watch?v=O2tV9q6784k) | Scheduling-Grundlagen: FCFS, SJF, Round Robin, Prioritäten |
> | 🎬 | [CoreDumped – Concurrency](https://www.youtube.com/watch?v=3X93PnKRNUo) | Nebenläufigkeit und ihre Herausforderungen |

> [!tip] **Weiterführende Links**
> - [AnimOS – Scheduling-Simulator](https://ess.cs.uni-osnabrueck.de/software/AnimOS/)
> - [OSTEP – Scheduling Kapitel (kostenlos)](https://pages.cs.wisc.edu/~remzi/OSTEP/)

---

## Quellen

- IU Skript: Betriebssysteme, Rechnernetze und verteilte Systeme - Teil 5 (Ressourcen)
- Tanenbaum, A.: Modern Operating Systems, 4th Edition
- Silberschatz, A.: Operating System Concepts, 10th Edition
- Arpaci-Dusseau: Operating Systems: Three Easy Pieces (OSTEP)
