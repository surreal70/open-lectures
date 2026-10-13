---
author: Andreas Hümmer
title: Threads
tags:
  - content
  - bs
  - prozesse
  - threads
  - multithreading
  - kernel-threads
  - user-threads
created: '2026-10-07'
modified: '2026-10-09'
bereich: BS
---

# Threads

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Definition von Threads (leichtgewichtige Prozesse) kennen
> - Den Unterschied zwischen User-Level und Kernel-Level Threads verstehen
> - Vorteile und Nachteile von Threads erklären können
> - Die Begriffe Multithreading, Multitasking und Multiprocessing unterscheiden
> - Verstehen, was Threads teilen und was sie nicht teilen
> - Die verschiedenen Threading-Modelle (1:1, N:1, M:N) kennen

---

## Definition

> [!quote] **Formale Definition**
> Ein **Thread** (auch: leichtgewichtiger Prozess, LWP) ist eine Ausführungseinheit innerhalb eines Prozesses. Threads teilen sich den Adressraum ihres Prozesses, besitzen aber jeweils einen eigenen Stack und Registersatz.

### Motivation: Warum Threads?

In vielen Anwendungen ist es sinnvoll, mehrere Aktivitäten **gleichzeitig** auszuführen:

| Anwendung | Threads für... |
|-----------|----------------|
| **Webbrowser** | Rendering, Netzwerk, JavaScript, UI |
| **Textverarbeitung** | Eingabe, Rechtschreibprüfung, Autosave |
| **Webserver** | Jede Client-Anfrage in eigenem Thread |
| **Spiele** | Grafik, Physik, KI, Audio, Netzwerk |

**Warum nicht einfach mehrere Prozesse?**

| Aspekt | Mehrere Prozesse | Mehrere Threads |
|--------|-----------------|-----------------|
| Speicher | Getrennte Adressräume | Gemeinsamer Adressraum |
| Kontextwechsel | Teuer (TLB-Flush, Cache) | Günstig (gleicher Adressraum) |
| Kommunikation | IPC nötig (Pipes, Sockets) | Direkt über gemeinsamen Speicher |
| Erzeugung | Langsam (fork kopiert) | Schnell |

> [!example] **Beispiel: Webserver**
> Ein Webserver könnte für jede Anfrage einen neuen Prozess starten (`fork()`). Das ist aber ineffizient:
> - `fork()` dauert ~1ms, Thread-Erzeugung ~10µs
> - Jeder Prozess braucht eigenen Speicher
> - Kommunikation zwischen Workern kompliziert
> 
> Mit Threads: Ein Prozess, viele Worker-Threads, gemeinsamer Cache.

---

## Prozesse und Threads im Kontext

![[02-03-03-process-threads-context.png]]
<span class="fig-id">02-03-03-01</span> *Threads innerhalb eines Prozesses teilen globale Daten, besitzen aber eigene Stacks*

### Was Threads teilen und was nicht

| Geteilt (pro Prozess) | Nicht geteilt (pro Thread) |
|----------------------|---------------------------|
| Adressraum (Code, Heap) | Stack |
| Globale Variablen | Programmzähler (PC) |
| Offene Dateien (File Descriptors) | Register |
| Signalhandler | Thread-ID (TID) |
| Code-Segment | Zustand (Running/Ready/Blocked) |
| Umgebungsvariablen | Thread-Local Storage (TLS) |
| Prozess-ID (PID) | Priorität/Scheduling-Parameter |

> [!note] **Thread-Local Storage (TLS)**
> Manchmal brauchen Threads eigene "globale" Variablen. TLS ermöglicht dies:
> ```c
> __thread int counter;  // Jeder Thread hat seinen eigenen counter
> ```

---

## Thread Control Block (TCB)

Analog zum PCB für Prozesse gibt es für Threads einen **Thread Control Block**:

| TCB-Inhalt | Beschreibung |
|------------|--------------|
| Thread-ID | Eindeutige Kennung |
| Thread-Zustand | Running, Ready, Blocked, Terminated |
| Programmzähler | Aktuelle Instruktion |
| Registerwerte | CPU-Register-Snapshot |
| Stack-Pointer | Zeiger auf Thread-Stack |
| Priorität | Scheduling-Priorität |
| Zeiger auf PCB | Zugehöriger Prozess |

Der TCB ist deutlich kleiner als ein PCB, da er keine Speicher-Informationen (Page Tables etc.) enthält – diese sind im PCB des Prozesses.

---

## User-Level vs. Kernel-Level Threads

Es gibt zwei grundlegende Ansätze, wo Threads verwaltet werden:

### User-Level Threads (ULT)

Die Thread-Verwaltung erfolgt komplett im User-Space durch eine **Thread-Bibliothek** (z.B. GNU Portable Threads). Der Kernel weiß nichts von den Threads.

![[02-03-03-user-level-threads.png]]
<span class="fig-id">02-03-03-02</span> *User-Level Threads: Der Kernel sieht nur einen einzigen Thread*

### Kernel-Level Threads (KLT)

Die Thread-Verwaltung erfolgt im Kernel. Jeder User-Thread hat einen entsprechenden Kernel-Thread.

![[02-03-03-kernel-level-threads.png]]
<span class="fig-id">02-03-03-03</span> *Kernel-Level Threads: Jeder User-Thread hat einen Kernel-Thread*

### Vergleich

| Eigenschaft | Kernel-Threads | User-Threads |
|-------------|----------------|--------------|
| **Kontextwechsel** | Langsam (Syscall nötig) | Sehr schnell (kein Kernel) |
| **Multicore-Nutzung** | Ja, echte Parallelität | Nein, nur ein Kern |
| **Blockierung** | Nur ein Thread blockiert | Ganzer Prozess blockiert |
| **Scheduling** | Durch Kernel-Scheduler | Durch User-Bibliothek |
| **Portabilität** | OS-abhängig | Portabel |
| **Overhead** | Höher | Niedriger |

> [!danger] **Das Blocking-Problem bei ULT**
> Wenn ein User-Level Thread einen blockierenden Syscall macht (z.B. `read()`), blockiert der **gesamte Prozess** – alle anderen User-Threads stehen still!
> 
> Workaround: "Jacket" oder "Wrapper" um blockierende Syscalls, die auf non-blocking I/O umstellen.

---

## Threading-Modelle

Die Beziehung zwischen User-Threads und Kernel-Threads definiert das Threading-Modell:

### 1:1 Modell (One-to-One)

Jeder User-Thread wird auf genau einen Kernel-Thread abgebildet.

![[02-03-03-threading-model-1to1.png]]
<span class="fig-id">02-03-03-04</span> *1:1 Modell: Jeder User-Thread hat einen eigenen Kernel-Thread*

**Beispiele:** Linux (NPTL), Windows, macOS

| Vorteile | Nachteile |
|----------|-----------|
| Echte Parallelität | Kernel-Overhead pro Thread |
| Unabhängige Blockierung | Begrenzte Thread-Anzahl |
| Einfaches Modell | Kontextwechsel teurer |

### N:1 Modell (Many-to-One)

Alle User-Threads werden auf einen Kernel-Thread abgebildet.

![[02-03-03-threading-model-nto1.png]]
<span class="fig-id">02-03-03-05</span> *N:1 Modell: Alle User-Threads teilen sich einen Kernel-Thread*

**Beispiele:** GNU Portable Threads, frühe Green Threads

| Vorteile | Nachteile |
|----------|-----------|
| Schnelle Kontextwechsel | Keine echte Parallelität |
| Wenig Overhead | Blocking-Problem |
| Portabel | Kein Multicore-Nutzen |

### M:N Modell (Many-to-Many)

M User-Threads werden auf N Kernel-Threads abgebildet (M ≥ N).

![[02-03-03-threading-model-mton.png]]
<span class="fig-id">02-03-03-06</span> *M:N Modell: User-Threads werden auf einen Pool von Kernel-Threads verteilt*

**Beispiele:** Solaris LWP, frühere Windows Fibers, Go (Goroutines)

| Vorteile | Nachteile |
|----------|-----------|
| Flexibel | Sehr komplex zu implementieren |
| Echte Parallelität möglich | Kompliziertes Scheduling |
| Weniger Kernel-Threads nötig | Debug schwierig |

> [!note] **Moderne Systeme**
> Die meisten modernen Systeme (Linux, Windows, macOS) verwenden das **1:1 Modell**, da die Vorteile der echten Parallelität den Overhead überwiegen. Das M:N Modell erlebt aber eine Renaissance in Sprachen wie **Go** (Goroutines) und **Erlang/Elixir** (Prozesse).

---

## Thread-Zustände

Threads haben ähnliche Zustände wie Prozesse:

![[02-03-03-thread-states.png]]
<span class="fig-id">02-03-03-07</span> *Thread-Zustandsübergänge: create, dispatch, preempt, block, unblock, terminate*

Ein Thread kann für verschiedene Ereignisse blockieren:
- I/O-Operationen (read, write)
- Synchronisation (Mutex, Semaphore)
- Sleep/Delay
- Warten auf andere Threads (join)

---

## Multithreading vs. Multitasking vs. Multiprocessing

![[02-03-03-multi-comparison.png]]
<span class="fig-id">02-03-03-08</span> *Vergleich: Multithreading, Multitasking und Multiprocessing*

| Begriff | Ebene | Beschreibung |
|---------|-------|--------------|
| **Multithreading** | Innerhalb Prozess | Quasi-gleichzeitiges Abarbeiten mehrerer Threads **desselben** Prozesses |
| **Multitasking** | OS-Ebene | Quasi-gleichzeitiges Abarbeiten mehrerer **Prozesse** (Time-Sharing) |
| **Multiprocessing** | Hardware-Ebene | **Echtes** gleichzeitiges Abarbeiten auf mehreren Prozessoren/Kernen |

> [!note] **Kombination**
> Moderne Systeme kombinieren alle drei: Mehrere Prozesse (Multitasking), jeder mit mehreren Threads (Multithreading), verteilt auf mehrere Kerne (Multiprocessing).

---

## Thread-Erzeugung in der Praxis

### POSIX Threads (pthreads) – C/Linux

```c
#include <pthread.h>
#include <stdio.h>

void* thread_function(void* arg) {
    int id = *(int*)arg;
    printf("Thread %d läuft\n", id);
    return NULL;
}

int main() {
    pthread_t thread;
    int id = 1;
    
    // Thread erzeugen
    pthread_create(&thread, NULL, thread_function, &id);
    
    // Auf Thread warten
    pthread_join(thread, NULL);
    
    return 0;
}
```

**Kompilieren:** `gcc -pthread program.c -o program`

### Java Threads

```java
// Variante 1: Thread-Klasse erweitern
class MyThread extends Thread {
    public void run() {
        System.out.println("Thread läuft");
    }
}

// Variante 2: Runnable implementieren (bevorzugt)
class MyRunnable implements Runnable {
    public void run() {
        System.out.println("Thread läuft");
    }
}

// Verwendung
Thread t1 = new MyThread();
t1.start();

Thread t2 = new Thread(new MyRunnable());
t2.start();
```

### Python Threads

```python
import threading

def worker(name):
    print(f"Thread {name} läuft")

# Thread erzeugen und starten
t = threading.Thread(target=worker, args=("Worker-1",))
t.start()
t.join()  # Warten auf Beendigung
```

> [!warning] **Python GIL**
> Python hat einen **Global Interpreter Lock (GIL)**, der verhindert, dass mehrere Threads gleichzeitig Python-Bytecode ausführen. Für CPU-intensive Aufgaben sind daher **Multiprocessing** oder alternative Implementierungen (PyPy, Cython) besser geeignet.

---

## Vorteile und Nachteile von Threads

### Vorteile

| Vorteil | Erklärung |
|---------|-----------|
| **Responsiveness** | UI bleibt reaktiv, während Hintergrundarbeit läuft |
| **Ressourcenteilung** | Threads teilen Speicher → weniger RAM-Verbrauch |
| **Schnelle Erzeugung** | Thread-Erzeugung 10-100x schneller als Prozess |
| **Schneller Kontextwechsel** | Kein Adressraum-Wechsel nötig |
| **Multicore-Nutzung** | Threads können parallel auf verschiedenen Kernen laufen |
| **Einfache Kommunikation** | Gemeinsamer Speicher statt IPC |

### Nachteile

| Nachteil | Erklärung |
|----------|-----------|
| **Komplexe Programmierung** | Thread-sichere Programmierung ist schwierig |
| **Synchronisation nötig** | Race Conditions müssen verhindert werden |
| **Debugging schwierig** | Timing-abhängige Fehler schwer reproduzierbar |
| **Deadlock-Risiko** | Bei falscher Synchronisation |
| **Ressourcen-Overhead** | Jeder Thread braucht eigenen Stack (typisch 1-8 MB) |
| **Fehler-Propagation** | Ein abstürzender Thread kann den ganzen Prozess beenden |

> [!danger] **Thread-Safety**
> Gemeinsamer Speicher ist Segen und Fluch zugleich. Ohne korrektes Locking entstehen **Race Conditions** und **Data Races**. Mehr dazu in [[01-Kritische-Abschnitte|Kritische Abschnitte]].

---

## Zusammenhänge

- [[01-Prozessmodell|Prozessmodell]] → Threads existieren innerhalb von Prozessen
- [[02-Scheduling|Scheduling]] → Threads werden vom Scheduler eingeplant
- [[01-Kritische-Abschnitte|Kritische Abschnitte]] → Threads erfordern Synchronisation
- [[02-Semaphore|Semaphore]] → Synchronisationsmechanismus für Threads
- [[03-Deadlocks|Deadlocks]] → Können bei falscher Thread-Synchronisation auftreten

---

## Praktische Kommandos

### Linux/Unix

| Kommando | Beschreibung |
|----------|--------------|
| `ps -eLf` | Alle Threads aller Prozesse anzeigen |
| `ps -T -p <PID>` | Threads eines bestimmten Prozesses |
| `top -H` | Threads in top anzeigen (statt Prozesse) |
| `htop` | Threads interaktiv (F2 → Display → Show custom thread names) |
| `cat /proc/<PID>/status` | Thread-Anzahl unter "Threads:" |
| `ls /proc/<PID>/task/` | Thread-IDs eines Prozesses |

```bash
# Beispiel: Threads von Firefox anzeigen
ps -T -p $(pgrep -x firefox) | head -20

# Anzahl der Threads eines Prozesses
cat /proc/$(pgrep -x firefox)/status | grep Threads
```

### Windows

| Kommando | Beschreibung |
|----------|--------------|
| Task-Manager | Spalte "Threads" einblenden |
| `Get-Process \| Select Name,Threads` | PowerShell: Thread-Anzahl |
| Process Explorer | Sysinternals-Tool mit Thread-Details |

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - Definition Thread vs. Prozess
> - User-Level vs. Kernel-Level Threads (Vor-/Nachteile)
> - **Was teilen Threads, was nicht?**
> - Unterschied Multithreading/Multitasking/Multiprocessing
> - Blocking-Problem bei User-Level Threads

> [!question] **Häufige Prüfungsfragen**
> 1. Was ist der Unterschied zwischen einem Prozess und einem Thread?
> 2. Vergleichen Sie User-Level und Kernel-Level Threads!
> 3. Was passiert, wenn ein User-Level Thread einen blockierenden Syscall macht?
> 4. Erklären Sie den Unterschied zwischen Multithreading und Multiprocessing!
> 5. Welche Vorteile bieten Threads gegenüber Prozessen?
> 6. Beschreiben Sie das 1:1, N:1 und M:N Threading-Modell!
> 7. Warum ist Thread-Programmierung fehleranfällig?

> [!tip] **Merkhilfen**
> - **Thread** = "Faden" (mehrere Fäden in einem Stoff/Prozess)
> - **User-Thread blockiert** = "Eine verstopfte Leitung blockiert das ganze Haus"
> - **Kernel-Thread blockiert** = "Nur ein Zimmer ist betroffen"
> - **1:1** = "Jeder bekommt seinen eigenen Kellner"
> - **N:1** = "Alle teilen sich einen Kellner"
> - **M:N** = "Kellner-Pool bedient alle Gäste"

---

## Weiterführende Ressourcen

> [!note] **Videos (YouTube)**
> 
> | | Video | Beschreibung |
> |---|-------|--------------|
> | 🎬 | [CoreDumped – Threads on a Single Core](https://www.youtube.com/watch?v=M9HHWFp84f0) | Wie Threads auf einem Kern quasi-parallel laufen |
> | 🎬 | [CoreDumped – Threads on Multicore Systems](https://www.youtube.com/watch?v=5sw9XJokAqw) | Echte Parallelität auf Mehrkernprozessoren |
> | 🎬 | [CoreDumped – Concurrency](https://www.youtube.com/watch?v=3X93PnKRNUo) | Nebenläufigkeit und ihre Herausforderungen |

> [!tip] **Weiterführende Links**
> - [POSIX Threads Programming (LLNL)](https://hpc-tutorials.llnl.gov/posix/)
> - [Java Concurrency Tutorial (Oracle)](https://docs.oracle.com/javase/tutorial/essential/concurrency/)
> - [Python threading Dokumentation](https://docs.python.org/3/library/threading.html)

---

## Quellen

- IU Skript: Betriebssysteme, Rechnernetze und verteilte Systeme - Teil 5 (Ressourcen)
- Tanenbaum, A.: Modern Operating Systems, 4th Edition
- Silberschatz, A.: Operating System Concepts, 10th Edition
- Arpaci-Dusseau: Operating Systems: Three Easy Pieces (OSTEP)
