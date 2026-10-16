---
author: Andreas Hümmer
title: Synchronisationsmechanismen
tags:
  - content
  - bs
  - synchronisation
  - semaphore
  - mutex
  - monitor
  - spinlock
created: '2026-10-09'
modified: '2026-10-09'
bereich: BS
---

# Synchronisationsmechanismen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die verschiedenen Ebenen der Synchronisation kennen (Hardware, OS, Sprache)
> - Spinlocks, Mutexe und Semaphore verstehen und unterscheiden
> - Monitore und Condition Variables erklären können
> - Praktische Implementierungen in verschiedenen Sprachen kennen
> - Den richtigen Mechanismus für verschiedene Szenarien wählen können

---

## Einführung

Nachdem wir die Probleme der Nebenläufigkeit kennengelernt haben – kritische Abschnitte, Race Conditions, Deadlocks – stellt sich die Frage: Wie löst man sie? Die Antwort sind Synchronisationsmechanismen: Werkzeuge, die koordinierten Zugriff auf gemeinsame Ressourcen ermöglichen.

Die Geschichte der Synchronisationsmechanismen ist eng mit der Geschichte der Betriebssysteme verknüpft. In den 1960er Jahren, als die ersten Timesharing-Systeme aufkamen, wurden die Probleme offensichtlich. Edsger Dijkstra entwickelte 1965 das Semaphor-Konzept, Per Brinch Hansen und Tony Hoare folgten in den 1970ern mit Monitoren. Jede Generation brachte abstraktere, sicherere Mechanismen hervor.

Heute stehen Entwicklern Mechanismen auf verschiedenen Abstraktionsebenen zur Verfügung – von Hardware-Instruktionen bis zu Sprachkonstrukten. Die Wahl des richtigen Mechanismus ist eine Abwägung zwischen Performance, Sicherheit und Komfort.

---

## Übersicht der Mechanismen

Synchronisationsmechanismen existieren auf verschiedenen Abstraktionsebenen. Je höher die Ebene, desto komfortabler die Nutzung – aber auch desto mehr Overhead. Die Kunst liegt darin, den richtigen Mechanismus für den jeweiligen Anwendungsfall zu wählen.

| Ebene | Mechanismen | Charakteristik |
|-------|-------------|----------------|
| **Hardware** | Interrupt Disable, Test-and-Set, CAS, Spinlocks | Schnell, low-level, für Kernel |
| **Betriebssystem** | Semaphore, Mutexe | Blockierend, effizient |
| **Programmiersprache** | Monitore, synchronized, lock, Condition Variables | Komfortabel, weniger fehleranfällig |

Diese Schichtung ist kein Zufall: Jede höhere Ebene baut auf der darunterliegenden auf. Ein Mutex im Betriebssystem nutzt intern atomare Hardware-Operationen. Ein `synchronized`-Block in Java nutzt intern einen Mutex. Versteht man die unteren Ebenen, versteht man auch, warum die höheren so funktionieren, wie sie funktionieren.

---

## Hardware-Ebene

Die Hardware-Ebene bildet das Fundament aller Synchronisation. Ohne Hardware-Unterstützung wäre korrekte Synchronisation auf Multiprozessorsystemen unmöglich – man könnte keine atomaren Operationen garantieren.

### Unterbrechungssperre (Interrupt Disable)

Die einfachste und älteste Form der Synchronisation: Alle Interrupts deaktivieren. Die Logik ist bestechend einfach – ohne Interrupts gibt es keinen Kontextwechsel, ohne Kontextwechsel keine Unterbrechung im kritischen Abschnitt.

```c
disable_interrupts();
// Kritischer Abschnitt
// Kein Kontextwechsel möglich!
enable_interrupts();
```

Diese Methode stammt aus der Frühzeit der Betriebssysteme, als Computer noch einen einzigen Prozessor hatten. Auf einem Single-Core-System funktioniert sie perfekt: Wenn Interrupts deaktiviert sind, kann kein anderer Code laufen.

> [!danger] **Probleme**
> - Nur im **Kernel-Mode** möglich – User-Programme dürfen Interrupts nicht kontrollieren (sonst könnte ein Programm das System lahmlegen)
> - Auf **Multiprozessorsystemen** wirkungslos – ein anderer Prozessor läuft unbeirrt weiter
> - Blockiert **alle** Interrupts – auch zeitkritische wie Timer, Netzwerk oder Tastatur
> - Bei langen kritischen Abschnitten können Interrupts verloren gehen

Heute wird Interrupt-Disabling nur noch für sehr kurze, zeitkritische Kernel-Operationen verwendet – oft in Kombination mit Spinlocks, um auch andere Prozessoren zu berücksichtigen.

### Atomare Operationen

Moderne CPUs bieten spezielle Instruktionen, die garantiert unteilbar (atomar) ausgeführt werden. "Atomar" bedeutet hier: Die Operation erscheint für alle anderen Prozessoren und Threads als instantan – es gibt keinen beobachtbaren Zwischenzustand.

Diese Instruktionen sind das Fundament, auf dem alle höheren Synchronisationsmechanismen aufbauen. Ohne sie wäre korrekte Synchronisation auf Multiprozessorsystemen mathematisch unmöglich.

#### Test-and-Set (TAS)

Die klassische atomare Operation, entwickelt in den 1960er Jahren. Sie kombiniert Lesen und Schreiben in einem unteilbaren Schritt: Lies den aktuellen Wert, setze ihn auf `true`, gib den alten Wert zurück.

```c
// Pseudocode – in Hardware atomar implementiert
bool test_and_set(bool *lock) {
    bool old = *lock;   // Lesen
    *lock = true;       // Setzen
    return old;         // Alten Wert zurückgeben
}
// Alle drei Schritte passieren ATOMAR!
```

Der Trick liegt darin, dass die Hardware garantiert, dass kein anderer Prozessor zwischen Lesen und Schreiben eingreifen kann. Die CPU sperrt den Speicherbus für die Dauer der Operation.

**Verwendung für einen einfachen Lock:**

```c
while (test_and_set(&lock)) {
    // Lock ist belegt → warten (Busy Waiting)
}
// Lock erhalten → kritischer Abschnitt
critical_section();
lock = false;  // Freigeben
```

Wenn der alte Wert `false` war, haben wir den Lock erhalten (und gleichzeitig auf `true` gesetzt). War er bereits `true`, warten wir in der Schleife.

#### Compare-and-Swap (CAS)

Eine flexiblere atomare Operation, die in den 1970er Jahren bei IBM entwickelt wurde. CAS vergleicht einen Wert mit einem erwarteten Wert, und nur wenn sie übereinstimmen, ersetzt er ihn durch einen neuen Wert.

```c
// Pseudocode – in Hardware atomar implementiert
bool compare_and_swap(int *ptr, int expected, int new_value) {
    if (*ptr == expected) {
        *ptr = new_value;
        return true;   // Erfolg: Wert war wie erwartet
    }
    return false;      // Misserfolg: Wert hat sich geändert
}
```

Warum ist CAS mächtiger als TAS? Mit CAS kann man erkennen, ob sich ein Wert seit dem letzten Lesen geändert hat. Das ermöglicht **optimistisches Locking**: Man liest einen Wert, berechnet einen neuen, und versucht ihn zurückzuschreiben. Wenn jemand anderes schneller war, wiederholt man einfach.

CAS ist die Basis für **lock-free Algorithmen** – Datenstrukturen, die ohne Locks auskommen und damit Deadlocks und Priority Inversion unmöglich machen.

```c
// Lock-free Counter mit CAS
void atomic_increment(int *counter) {
    int old, new_val;
    do {
        old = *counter;
        new_val = old + 1;
    } while (!compare_and_swap(counter, old, new_val));
    // Wiederholen, bis niemand dazwischenfunkt
}
```

> [!note] **Moderne CPU-Instruktionen**
> - x86/x64: `LOCK CMPXCHG` (Compare-and-Exchange)
> - ARM: `LDREX`/`STREX` (Load/Store Exclusive)
> - RISC-V: `LR`/`SC` (Load Reserved / Store Conditional)

### Spinlocks

Ein Spinlock ist ein Lock, der durch aktives Warten (Busy Waiting) implementiert wird. Der Name kommt daher, dass der wartende Thread "spinnt" – sich im Kreis dreht und immer wieder prüft, ob der Lock frei ist.

```c
void spinlock_acquire(bool *lock) {
    while (test_and_set(lock)) {
        // "Spinning" – CPU dreht sich im Kreis
        // und prüft immer wieder den Lock
    }
}

void spinlock_release(bool *lock) {
    *lock = false;
}
```

Spinlocks haben einen schlechten Ruf wegen der CPU-Verschwendung. Aber in bestimmten Situationen sind sie die beste Wahl:

| Vorteile | Nachteile |
|----------|-----------|
| Kein Kontextwechsel nötig | CPU-Zeit wird verschwendet |
| Sehr schnell bei kurzer Wartezeit | Nur für kurze kritische Abschnitte |
| Einfach zu implementieren | Katastrophal auf Single-Core-Systemen |
| Kein Kernel-Aufruf nötig | Schlecht bei langer Wartezeit |

> [!tip] **Wann Spinlocks verwenden?**
> - Kritischer Abschnitt ist **sehr kurz** (wenige Instruktionen)
> - **Multiprozessorsystem** (auf Single-Core macht Spinning keinen Sinn – der blockierte Thread kann den Lock nie freigeben, während wir spinnen)
> - **Kontextwechsel wäre teurer** als kurzes Warten
> - **Im Kernel**, wenn man nicht schlafen darf (z.B. in Interrupt-Handlern)

Der Linux-Kernel verwendet Spinlocks extensiv für kurze, zeitkritische Operationen. Für Anwendungsprogramme sind sie selten die richtige Wahl.

---

## Betriebssystem-Ebene

Die Betriebssystem-Ebene bietet Synchronisationsprimitive, die **blockierend** arbeiten: Ein wartender Thread wird schlafen gelegt und vom Scheduler erst wieder aufgeweckt, wenn die Ressource frei ist. Das ist effizienter als Busy Waiting, erfordert aber Kernel-Unterstützung.

### Semaphore

Semaphore wurden 1965 von Edsger Dijkstra erfunden – eines der einflussreichsten Konzepte der Informatikgeschichte. Dijkstra suchte nach einem einfachen, aber mächtigen Primitiv für die Prozesssynchronisation und fand es in einem geschützten Zähler mit zwei Operationen.

Der Name "Semaphor" kommt von den Eisenbahnsignalen (Formsignale/Semaphore), die anzeigen, ob ein Gleisabschnitt frei ist. Die Analogie ist treffend: Ein Semaphor zeigt an, wie viele "Plätze" noch frei sind.

#### Die Operationen: P und V

Die Namen stammen aus dem Niederländischen: **P**roberen (versuchen/testen) und **V**erhogen (erhöhen). Dijkstra wählte bewusst Abkürzungen, um die Operationen als atomare Primitive zu kennzeichnen – keine ausführlichen Namen, die suggerieren könnten, man könne sie aufteilen.

| Operation | Alternative Namen | Beschreibung |
|-----------|-------------------|--------------|
| **P(S)** | wait, down, acquire | Wenn S > 0: dekrementiere S. Sonst: blockiere den aufrufenden Prozess. |
| **V(S)** | signal, up, release | Inkrementiere S. Wecke einen wartenden Prozess (falls vorhanden). |

```c
// P-Operation (wait/down) – Pseudocode
void P(Semaphore *S) {
    // Diese gesamte Operation ist ATOMAR
    if (S->value > 0) {
        S->value--;
        // Prozess darf weiterlaufen
    } else {
        // Prozess blockieren und in Warteschlange einreihen
        add_to_queue(S->waiting_queue, current_process);
        block(current_process);
    }
}

// V-Operation (signal/up) – Pseudocode
void V(Semaphore *S) {
    // Diese gesamte Operation ist ATOMAR
    S->value++;
    if (!is_empty(S->waiting_queue)) {
        // Einen wartenden Prozess aufwecken
        process = remove_from_queue(S->waiting_queue);
        wakeup(process);
    }
}
```

> [!tip] **Merkhilfe**
> - **P** = "**P**assieren wollen" – ich will durch, muss evtl. warten
> - **V** = "**V**erlassen" – ich bin fertig, andere können durch

#### Binärer Semaphor

Ein binärer Semaphor kann nur die Werte **0** und **1** annehmen. Er funktioniert wie ein Schlüssel zu einem Raum: Entweder ist der Schlüssel da (1) oder nicht (0).

```c
Semaphore mutex = 1;  // Initialisiert mit 1 (Schlüssel ist da)

// Prozess A              // Prozess B
P(mutex);                 P(mutex);      // muss warten...
  // kritischer Abschnitt   
V(mutex);                 // jetzt kann B weiterlaufen
                            // kritischer Abschnitt
                          V(mutex);
```

- `mutex = 1`: Schlüssel ist da – ein Prozess kann eintreten
- `mutex = 0`: Schlüssel ist weg – andere müssen warten

#### Counting Semaphor (Zählsemaphor)

Ein Counting Semaphor kann beliebige nicht-negative Werte annehmen. Er verwaltet eine begrenzte Anzahl gleichartiger Ressourcen – wie ein Parkhaus mit N Stellplätzen.

```c
Semaphore pool = 5;  // 5 verfügbare Ressourcen (z.B. DB-Connections)

// Ressource anfordern
P(pool);           // Dekrementiert den Zähler (oder wartet)
use_resource();    // Ressource nutzen
V(pool);           // Ressource zurückgeben (inkrementiert)
```

- `pool = 5`: Alle 5 Ressourcen frei
- `pool = 2`: 3 belegt, 2 frei
- `pool = 0`: Alle belegt → neue Anfragen blockieren

> [!example] **Praxisbeispiel: Connection Pool**
> Eine Datenbankanwendung hat einen Pool von 10 Verbindungen. Ein Counting Semaphor mit Initialwert 10 verwaltet sie: Jeder Thread, der eine Verbindung braucht, ruft `P(pool)` auf. Wenn alle 10 belegt sind, wartet er automatisch, bis eine frei wird.

#### Producer-Consumer mit Semaphoren

Das Producer-Consumer-Problem (auch: Bounded Buffer Problem) ist ein Klassiker der Nebenläufigkeit. Ein Producer erzeugt Daten, ein Consumer verarbeitet sie. Dazwischen liegt ein Puffer mit begrenzter Kapazität.

Die Herausforderung: Der Producer darf nicht in einen vollen Puffer schreiben, der Consumer nicht aus einem leeren lesen. Drei Semaphore lösen das elegant:

```c
Semaphore mutex = 1;   // Zugriff auf Puffer schützen
Semaphore empty = N;   // Anzahl freier Plätze (anfangs N)
Semaphore full = 0;    // Anzahl belegter Plätze (anfangs 0)

// PRODUCER
void producer() {
    while (true) {
        item = produce_item();
        
        P(empty);          // Warte auf freien Platz
        P(mutex);          // Exklusiver Pufferzugriff
        insert_to_buffer(item);
        V(mutex);          // Pufferzugriff freigeben
        V(full);           // Ein Platz mehr belegt
    }
}

// CONSUMER
void consumer() {
    while (true) {
        P(full);           // Warte auf belegten Platz
        P(mutex);          // Exklusiver Pufferzugriff
        item = remove_from_buffer();
        V(mutex);          // Pufferzugriff freigeben
        V(empty);          // Ein Platz mehr frei
        
        consume_item(item);
    }
}
```

> [!warning] **Reihenfolge beachten!**
> Die Reihenfolge `P(empty); P(mutex)` ist kritisch. Würde man `P(mutex); P(empty)` schreiben, könnte ein Deadlock entstehen: Der Producer hält den Mutex und wartet auf `empty`, während der Consumer den Puffer nicht leeren kann, weil er auf den Mutex wartet.

### Mutex vs. Semaphor

Obwohl ein binärer Semaphor wie ein Mutex aussieht, gibt es konzeptuelle Unterschiede, die in der Praxis wichtig sind:

| Eigenschaft           | Mutex                           | Semaphor                                |
| --------------------- | ------------------------------- | --------------------------------------- |
| **Wertebereich**      | 0 oder 1                        | 0 bis N                                 |
| **Ownership**         | Nur der Besitzer kann freigeben | Jeder kann V aufrufen                   |
| **Zweck**             | Gegenseitiger Ausschluss        | Ressourcenzählung, Signalisierung       |
| **Typischer Einsatz** | Kritische Abschnitte schützen   | Begrenzte Ressourcen, Producer-Consumer |
| **Rekursion**         | Oft rekursiv (reentrant)        | Nie rekursiv                            |

> [!warning] **Das Ownership-Problem**
> Bei Semaphoren kann ein anderer Thread V aufrufen als derjenige, der P aufgerufen hat. Das ist gewollt (z.B. für Signalisierung), kann aber zu Bugs führen, wenn man versehentlich einen binären Semaphor wie einen Mutex verwendet. Echte Mutexe erzwingen, dass nur der Besitzer freigeben kann.

---

## Programmiersprachen-Ebene

Die Programmiersprachen-Ebene bietet die höchste Abstraktion: Synchronisation wird Teil der Sprache selbst. Der Compiler kann auf korrekte Nutzung prüfen, und viele Fehler werden unmöglich.

### Monitore

Ein Monitor ist ein höheres Abstraktionskonzept, das 1974 unabhängig von Per Brinch Hansen und Tony Hoare entwickelt wurde. Die Idee: Statt Daten und Locks getrennt zu verwalten, kapselt man sie zusammen. Ein Monitor ist ein Objekt, bei dem automatisch nur ein Thread gleichzeitig eine Methode ausführen kann.

Das Konzept ist heute in Sprachen wie Java (`synchronized`), C# (`lock`), und Python (`threading.Lock`) allgegenwärtig – auch wenn es oft nicht explizit "Monitor" genannt wird.

```java
// Java: Jedes Objekt kann als Monitor dienen
public class BankKonto {
    private int kontostand = 0;  // Private Daten
    
    // Synchronisierte Methoden – nur eine gleichzeitig aktiv
    public synchronized void einzahlen(int betrag) {
        kontostand += betrag;
    }
    
    public synchronized void abheben(int betrag) {
        kontostand -= betrag;
    }
    
    public synchronized int getKontostand() {
        return kontostand;
    }
}
// Der Compiler garantiert: Nur ein Thread kann gleichzeitig 
// einzahlen ODER abheben ODER getKontostand aufrufen
```

**Warum sind Monitore besser als manuelle Locks?**

1. **Kapselung**: Daten und Schutz sind zusammen – man kann die Daten nicht versehentlich ohne Lock zugreifen
2. **Automatisch**: Kein vergessenes `unlock()` möglich
3. **Weniger Fehler**: Der Compiler erzwingt die Struktur
4. **Lesbarkeit**: Der Code drückt die Intention aus, nicht die Mechanik

### Condition Variables

Manchmal reicht ein Monitor nicht: Ein Thread muss auf eine bestimmte Bedingung warten, nicht nur auf den Zugang zum Monitor. Beispiel: "Warte, bis der Puffer nicht mehr leer ist."

Condition Variables ermöglichen genau das: Innerhalb eines Monitors auf eine Bedingung warten und dabei den Monitor vorübergehend freigeben.

| Operation | Beschreibung |
|-----------|--------------|
| `wait(cond)` | Gibt den Monitor-Lock frei und blockiert, bis `signal` oder `broadcast` aufgerufen wird. Beim Aufwachen wird der Lock wieder erworben. |
| `signal(cond)` | Weckt **einen** wartenden Thread auf |
| `broadcast(cond)` | Weckt **alle** wartenden Threads auf |

```java
// Java: Bounded Buffer mit wait/notify
public class BoundedBuffer {
    private int[] buffer = new int[10];
    private int count = 0;
    
    public synchronized void put(int item) throws InterruptedException {
        while (count == buffer.length) {
            wait();  // Puffer voll → Monitor freigeben und warten
        }
        buffer[count++] = item;
        notifyAll();  // Alle wartenden Consumer aufwecken
    }
    
    public synchronized int get() throws InterruptedException {
        while (count == 0) {
            wait();  // Puffer leer → Monitor freigeben und warten
        }
        int item = buffer[--count];
        notifyAll();  // Alle wartenden Producer aufwecken
        return item;
    }
}
```

> [!warning] **Immer `while`, nie `if`!**
> Nach dem Aufwachen aus `wait()` muss die Bedingung **erneut** geprüft werden:
> - **Spurious Wakeups**: Manche Implementierungen können Threads ohne `signal` aufwecken
> - **Konkurrenz**: Ein anderer Thread könnte schneller gewesen sein und die Bedingung wieder ungültig gemacht haben
> - **Broadcast**: Bei `notifyAll` wachen alle auf, aber nur einer kann die Ressource nutzen

---

## Praktische Implementierungen

### Java

Java war eine der ersten Mainstream-Sprachen mit eingebauter Thread-Unterstützung (1995). Jedes Objekt kann als Monitor dienen.

```java
// 1. synchronized auf Methode
public synchronized void criticalSection() {
    // Impliziter Lock auf 'this'
}

// 2. synchronized auf Block (flexibler)
public void method() {
    synchronized(this) {
        // Kritischer Abschnitt
    }
    // Hier kein Lock mehr
}

// 3. ReentrantLock (seit Java 5, flexibler)
private final Lock lock = new ReentrantLock();

public void method() {
    lock.lock();
    try {
        // Kritischer Abschnitt
    } finally {
        lock.unlock();  // IMMER in finally!
    }
}
```

### C (POSIX Threads)

POSIX Threads (pthreads) ist der Standard für Thread-Programmierung auf Unix-Systemen.

```c
#include <pthread.h>

pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;

void* thread_function(void* arg) {
    pthread_mutex_lock(&lock);
    // Kritischer Abschnitt
    pthread_mutex_unlock(&lock);
    return NULL;
}

// Mit Condition Variable
pthread_cond_t cond = PTHREAD_COND_INITIALIZER;

// Warten
pthread_mutex_lock(&lock);
while (!condition_met) {
    pthread_cond_wait(&cond, &lock);  // Gibt Lock frei während Warten
}
pthread_mutex_unlock(&lock);

// Signalisieren
pthread_mutex_lock(&lock);
condition_met = true;
pthread_cond_signal(&cond);  // Oder pthread_cond_broadcast(&cond)
pthread_mutex_unlock(&lock);
```

### Python

Python's Global Interpreter Lock (GIL) macht echte Parallelität in CPython unmöglich, aber für I/O-bound Code sind Locks trotzdem wichtig.

```python
import threading

lock = threading.Lock()

# Mit Context Manager (empfohlen – automatisches Unlock)
with lock:
    # Kritischer Abschnitt
    pass

# Mit Condition Variable
condition = threading.Condition()

# Warten
with condition:
    while not data_ready:
        condition.wait()
    # Bedingung erfüllt, verarbeiten

# Signalisieren
with condition:
    data_ready = True
    condition.notify_all()
```

### C++

Modernes C++ (seit C++11) hat Threading in der Standardbibliothek.

```cpp
#include <mutex>
#include <condition_variable>

std::mutex mtx;

// Mit lock_guard (RAII – automatisches Unlock)
{
    std::lock_guard<std::mutex> guard(mtx);
    // Kritischer Abschnitt
}  // Hier wird automatisch unlocked

// Mit unique_lock (flexibler, für Condition Variables nötig)
std::condition_variable cv;
std::unique_lock<std::mutex> lock(mtx);
cv.wait(lock, []{ return ready; });  // Wartet bis ready==true
```

---

## Vergleich der Mechanismen

| Mechanismus | Ebene | Wartetyp | Overhead | Geeignet für |
|-------------|-------|----------|----------|--------------|
| **Interrupt Disable** | Hardware | Keiner | Minimal | Nur Kernel, sehr kurz |
| **Spinlock** | Hardware | Busy Wait | Niedrig | Kurze kritische Abschnitte, Multi-Core |
| **Semaphor** | OS | Sleep | Mittel | Ressourcenzählung, Producer-Consumer |
| **Mutex** | OS | Sleep | Mittel | Kritische Abschnitte |
| **Monitor** | Sprache | Sleep | Mittel-Hoch | Objekt-basierte Synchronisation |
| **Condition Variable** | Sprache | Sleep | Mittel | Warten auf komplexe Bedingungen |

**Faustregel für die Wahl:**
- **Kernel-Code, sehr kurz**: Spinlock
- **Kritischer Abschnitt in Anwendung**: Mutex oder Monitor
- **Begrenzte Ressourcen zählen**: Counting Semaphor
- **Auf Bedingung warten**: Condition Variable
- **Objektorientierter Code**: Monitor (`synchronized`)

---

## Gefahren und Best Practices

### Häufige Fehler

**1. Deadlock durch falsche Lock-Reihenfolge:**
```c
// Thread 1: lock(A), lock(B)
// Thread 2: lock(B), lock(A)  → DEADLOCK!
```
**Lösung:** Locks immer in der **gleichen Reihenfolge** nehmen, dokumentieren!

**2. Vergessenes Unlock:**
```c
void function() {
    mutex_lock(&m);
    if (error) return;  // FEHLER: Mutex bleibt gelockt!
    mutex_unlock(&m);
}
```
**Lösung:** RAII (C++), try-finally (Java), `with` (Python), oder `defer` (Go)

**3. Signal statt Broadcast:**
```c
cond_signal(&c);  // Weckt nur EINEN Thread
// Aber was, wenn mehrere auf verschiedene Bedingungen warten?
```
**Lösung:** Im Zweifel `broadcast` verwenden – es ist sicherer

**4. Race Condition beim Prüfen der Bedingung:**
```java
// FALSCH:
if (count == 0) {
    wait();  // Zwischen Prüfung und Wait könnte sich count ändern!
}

// RICHTIG:
while (count == 0) {
    wait();
}
```

> [!tip] **Best Practices**
> - Kritische Abschnitte **so kurz wie möglich** halten
> - Locks immer in **gleicher, dokumentierter Reihenfolge** nehmen
> - **RAII/try-finally/with** für automatisches Freigeben nutzen
> - **Dokumentieren**, welche Daten durch welchen Lock geschützt werden
> - Bei Condition Variables: immer **while-Schleife**, nie **if**
> - Im Zweifel **broadcast statt signal**
> - **Testen unter Last** – Race Conditions zeigen sich oft erst dann

---

## Zusammenhänge

- [[02-Kritische-Abschnitte|Kritische Abschnitte]] → Diese Mechanismen schützen sie
- [[03-Race-Conditions|Race Conditions]] → Diese Mechanismen verhindern sie
- [[04-Deadlocks|Deadlocks]] → Können bei falscher Nutzung entstehen

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - P und V Operationen verstehen und anwenden
> - Unterschied binärer vs. Counting Semaphor
> - Unterschied Spinlock vs. Mutex

> [!question] **Häufige Prüfungsfragen**
> 1. Was sind die Operationen P und V bei Semaphoren? Erklären Sie die Semantik!
> 2. Was ist der Unterschied zwischen Mutex und Semaphor?
> 3. Lösen Sie das Producer-Consumer Problem mit Semaphoren!
> 4. Was ist ein Monitor und wie funktioniert er?
> 5. Wann verwendet man Spinlocks, wann Mutexe?
> 6. Was ist der Unterschied zwischen signal und broadcast bei Condition Variables?
> 7. Warum muss man nach wait() die Bedingung erneut prüfen?

> [!tip] **Merkhilfen**
> - **Spinlock** = "Aktives Warten wie ein Hamsterrad"
> - **Semaphor** = "Ampel für Ressourcen (P=rot werden, V=grün werden)"
> - **Mutex** = "Schlüssel zum Raum – nur einer hat ihn"
> - **Monitor** = "Objekt mit eingebautem Türsteher"
> - **Condition Variable** = "Warteraum mit Aufrufsystem"
> - **P** = **P**assieren wollen, **V** = **V**erlassen
> - **while statt if** = "Nach dem Aufwachen nochmal nachschauen"

---

## Weiterführende Ressourcen

> [!note] **Videos (YouTube)**
>
> | | Video | Beschreibung |
> |---|-------|--------------|
> | 🎬 | [CoreDumped – Concurrency](https://www.youtube.com/watch?v=3X93PnKRNUo) | Überblick Synchronisation |

> [!note] **Workshop & Dokumentation**
> - MOSS Deadlock Simulator: http://www.ontko.com/moss/deadlock/user_guide.html
> - Java Concurrency Tutorial: https://docs.oracle.com/javase/tutorial/essential/concurrency/
> - The Little Book of Semaphores: https://greenteapress.com/wp/semaphores/

---

## Quellen
- Tanenbaum: Modern Operating Systems
- Dijkstra: "Cooperating Sequential Processes" (1965)
- Hoare: "Monitors: An Operating System Structuring Concept" (1974)
- Brinch Hansen: "Operating System Principles" (1973)
