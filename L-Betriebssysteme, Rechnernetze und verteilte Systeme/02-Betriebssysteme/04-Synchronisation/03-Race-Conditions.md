---
author: Andreas Hümmer
title: Race Conditions
tags:
  - content
  - bs
  - synchronisation
  - race-condition
  - wettlaufsituation
created: '2026-10-09'
modified: '2026-10-09'
bereich: BS
---

# Race Conditions

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Race Conditions definieren und erkennen können
> - Verstehen, warum sie auftreten und wann sie gefährlich sind
> - Praktische Beispiele für Race Conditions kennen
> - Strategien zur Vermeidung kennen

---

## Definition

> [!quote] **Formale Definition**
> Eine **Race Condition** (Wettlaufsituation) tritt auf, wenn das Ergebnis einer Berechnung vom **zeitlichen Ablauf** (Timing) nebenläufiger Operationen abhängt. Sie entsteht, wenn mehrere Prozesse/Threads auf gemeinsame Daten zugreifen und mindestens einer davon **schreibend** zugreift.

Der Begriff "Race Condition" stammt aus der Elektronik, wo er ursprünglich Schaltkreise beschrieb, deren Ausgabe vom "Wettrennen" elektrischer Signale durch verschiedene Pfade abhing. In der Informatik wurde der Begriff in den 1960er Jahren übernommen, als die ersten Timesharing-Systeme die Probleme nebenläufiger Prozesse offenbarten.

Race Conditions gehören zu den heimtückischsten Fehlern in der Softwareentwicklung. Sie sind nicht-deterministisch – derselbe Code kann tausendmal korrekt laufen und beim tausendundersten Mal versagen. Sie verstecken sich, bis die Bedingungen genau stimmen: die richtige Last, das richtige Timing, der richtige Prozessor.

---

## Das Problem

Stell dir vor, zwei Personen bearbeiten gleichzeitig dasselbe Dokument – ohne zu wissen, dass der andere auch daran arbeitet. Beide laden die Version mit "10 Äpfel", einer ändert zu "15 Äpfel", der andere zu "12 Äpfel". Wer zuletzt speichert, überschreibt die Änderung des anderen. Das ist das Grundproblem.

Bei Computern passiert das Gleiche, nur viel schneller und mit schwerwiegenderen Konsequenzen. Ein Thread liest eine Variable, ein anderer Thread ändert sie gleichzeitig, und das Ergebnis hängt davon ab, wer "das Rennen gewinnt".

![[02-04-03-race-condition-basic.png]]
*<span class="fig-id">02-04-03-race-condition-basic</span>: Zwei Threads greifen auf Variable x zu – je nach Reihenfolge entstehen unterschiedliche Ergebnisse.*

---

## Klassisches Beispiel: Bankkonto

Das Bankkonto-Beispiel ist der Klassiker, weil es das Problem greifbar macht – hier geht es um echtes Geld, und die Konsequenzen sind sofort verständlich.

![[02-04-03-race-condition-bank.png]]
*<span class="fig-id">02-04-03-race-condition-bank</span>: Das klassische Bankbeispiel – ohne Synchronisation geht eine Transaktion verloren (Lost Update Problem).*

---

## Warum entstehen Race Conditions?

### Nicht-atomare Operationen

Hier liegt das Kernproblem: Was in einer Hochsprache wie eine einzelne Operation aussieht, besteht auf Maschinenebene aus mehreren Schritten. Und zwischen jedem dieser Schritte kann das Betriebssystem einen Kontextwechsel durchführen.

Selbst einfache Operationen wie `x++` bestehen aus mehreren Schritten:

![[02-04-03-race-condition-atomic.png]]
*<span class="fig-id">02-04-03-race-condition-atomic</span>: Die Operation x++ besteht aus drei Schritten (LOAD, ADD, STORE) – zwischen diesen kann ein Kontextwechsel stattfinden.*

---

## Arten von Race Conditions

Es gibt verschiedene Muster, wie Race Conditions auftreten. Diese Kategorisierung hilft beim Erkennen und Vermeiden.

### 1. Check-then-Act (TOCTOU)

"Time of Check to Time of Use" – zwischen Prüfung und Aktion ändert sich der Zustand. Dies ist eine der häufigsten Formen und besonders bei Dateisystemoperationen relevant.

```c
// UNSICHER!
if (file_exists("data.txt")) {    // Check
    // Anderer Prozess könnte Datei jetzt löschen!
    open("data.txt");              // Act → kann fehlschlagen
}
```

Das Problem: Zwischen der Prüfung (`file_exists`) und der Aktion (`open`) vergeht Zeit. In dieser Zeitspanne kann ein anderer Prozess die Datei löschen. Der Code nimmt an, dass der Zustand zwischen Check und Act stabil bleibt – eine gefährliche Annahme.

> [!example] **TOCTOU im Alltag**
> Du schaust nach, ob die Toilette frei ist (Check), gehst zurück zu deinem Platz, holst deine Sachen, und gehst zur Toilette (Act). In der Zwischenzeit ist jemand anderes schneller gewesen. Die Toilette, die eben noch frei war, ist jetzt besetzt.

### 2. Read-Modify-Write

Das klassische Muster: Einen Wert lesen, verändern, zurückschreiben – ohne dass dieser Vorgang atomar ist.

```c
// UNSICHER!
balance = get_balance();    // Read
balance = balance + 100;    // Modify
set_balance(balance);       // Write
```

Wenn zwei Threads diesen Code gleichzeitig ausführen und beide denselben Anfangswert lesen, überschreibt der zweite die Änderung des ersten.

### 3. Lazy Initialization

Mehrere Threads erkennen gleichzeitig, dass eine Ressource noch nicht initialisiert ist, und initialisieren sie parallel.

```java
// UNSICHER! (Das "naive" Singleton-Pattern)
public static Singleton getInstance() {
    if (instance == null) {           // Thread A und B können beide hier sein
        instance = new Singleton();   // Doppelte Initialisierung!
    }
    return instance;
}
```

Im besten Fall wird nur unnötig Arbeit doppelt gemacht. Im schlimmsten Fall – wenn die Initialisierung Seiteneffekte hat – entstehen inkonsistente Zustände.

---

## Erkennen von Race Conditions

### Das Debugging-Dilemma

Race Conditions sind berüchtigt dafür, schwer zu finden und zu reproduzieren. Das liegt an ihrer Natur: Sie treten nur unter bestimmten Timing-Bedingungen auf, und diese Bedingungen sind selten reproduzierbar.

> [!danger] **Das Tückische**
> Race Conditions sind schwer zu finden, weil sie:
> - Nur manchmal auftreten (abhängig vom Timing)
> - Unter Debugger oft verschwinden (verändertes Timing)
> - Erst unter Last sichtbar werden
> - Nicht-reproduzierbar sind

**Warum verschwinden Race Conditions beim Debuggen?**

Ein Debugger verlangsamt die Ausführung dramatisch. Breakpoints stoppen einzelne Threads. Logging fügt Verzögerungen ein. All das verändert das Timing so stark, dass die Race Condition nicht mehr auftritt. Das ist frustrierend: Der Bug existiert nachweislich (die Logs zeigen es), aber sobald man genauer hinschaut, ist er weg – wie eine Quantenbeobachtung.

Ein verwandtes Phänomen ist der **Heisenbug**: Ein Bug, der sein Verhalten ändert, wenn man versucht, ihn zu beobachten (benannt nach der Heisenbergschen Unschärferelation).

### Anzeichen für mögliche Race Conditions

| Symptom | Erklärung |
|---------|-----------|
| Sporadische Fehler | Fehler tritt nicht immer auf |
| Timing-abhängig | Schnellere/langsamere Hardware → anderes Verhalten |
| Verschwindet beim Debuggen | Debugger verändert Timing |
| Unter Last schlimmer | Mehr Kontextwechsel → mehr Gelegenheiten für Race |
| "Funktioniert auf meinem Rechner" | Anderer Rechner → anderes Timing |

### Werkzeuge zur Erkennung

- **Thread Sanitizer (TSan)**: Erkennt Data Races zur Laufzeit (verfügbar in GCC, Clang)
- **Helgrind**: Valgrind-Tool für Thread-Fehler
- **Intel Inspector**: Kommerzielles Tool für Race Detection
- **Static Analysis**: Tools wie Coverity oder PVS-Studio können manche Patterns erkennen

---

## Bedingungen für Race Conditions

Für eine Race Condition müssen drei Bedingungen gleichzeitig erfüllt sein. Das ist wichtig zu verstehen, denn es zeigt auch die Vermeidungsstrategien auf: Entferne eine der Bedingungen, und die Race Condition ist unmöglich.

| Bedingung | Beschreibung | Beispiel |
|-----------|--------------|----------|
| **Shared State** | Mehrere Threads greifen auf dieselben Daten zu | Globale Variable, Heap-Objekt |
| **Mindestens ein Write** | Mindestens ein Thread verändert die Daten | `counter++`, `list.add()` |
| **Keine Synchronisation** | Kein Mechanismus koordiniert den Zugriff | Kein Lock, kein Semaphor |

> [!tip] **Die Drei-Bedingungen-Regel**
> Entferne **eine** der drei Bedingungen, und die Race Condition verschwindet:
> - Kein Shared State → Keine Race Condition
> - Nur lesende Zugriffe → Keine Race Condition  
> - Synchronisation → Keine Race Condition

---

## Vermeidungsstrategien

Die Strategien ergeben sich direkt aus den drei Bedingungen. Jede Strategie eliminiert eine der Bedingungen.

### 1. Shared State vermeiden (Bedingung 1 eliminieren)

Der eleganteste Ansatz: Wenn Threads keine Daten teilen, können sie sich nicht in die Quere kommen.

```c
// Statt globalen Zustand zu teilen:
void process_item(int* global_result) {
    *global_result += calculate();  // Gefährlich!
}

// Besser: Lokal arbeiten, am Ende zusammenführen:
int process_item_local() {
    int local_result = calculate();
    return local_result;  // Sicher!
}
// Am Ende: results = sum(all_local_results)
```

Dieser Ansatz ist das Fundament von **Map-Reduce**: Jeder Worker arbeitet isoliert auf seiner Partition, am Ende werden die Ergebnisse zusammengeführt.

### 2. Immutable Objects (Bedingung 2 eliminieren)

Objekte, die nach der Erstellung nie verändert werden, sind automatisch thread-sicher. Wenn es keine Writes gibt, gibt es keine Race Conditions.

```java
// Mutable (gefährlich):
class Point {
    public int x, y;  // Kann jederzeit geändert werden
}

// Immutable (sicher):
final class ImmutablePoint {
    private final int x, y;  // Einmal gesetzt, nie geändert
    
    public ImmutablePoint(int x, int y) {
        this.x = x;
        this.y = y;
    }
    
    public ImmutablePoint move(int dx, int dy) {
        return new ImmutablePoint(x + dx, y + dy);  // Neues Objekt!
    }
}
```

Funktionale Programmiersprachen wie Haskell und Erlang machen Immutability zum Standard – ein Grund, warum sie für nebenläufige Systeme beliebt sind.

### 3. Synchronisation (Bedingung 3 eliminieren)

Der klassische Ansatz: Die Zugriffe koordinieren, sodass sie nicht mehr gleichzeitig stattfinden.

```java
synchronized void updateBalance(int amount) {
    balance = balance + amount;  // Jetzt sicher!
}
```

→ Details: [[05-Synchronisationsmechanismen|Synchronisationsmechanismen]]

### 4. Thread-Local Storage

Jeder Thread hat seine eigene Kopie der Daten – eine Variante von "Shared State vermeiden".

```java
// Java ThreadLocal
private static ThreadLocal<Integer> threadId = 
    ThreadLocal.withInitial(() -> nextId.getAndIncrement());
```

### 5. Atomare Operationen

Hardware-unterstützte Operationen, die unteilbar sind. Sie kombinieren Read-Modify-Write in einer einzigen, nicht unterbrechbaren Operation.

```java
// Java AtomicInteger
AtomicInteger counter = new AtomicInteger(0);
counter.incrementAndGet();  // Atomar!
```

```c
// C11 Atomics
#include <stdatomic.h>
atomic_int counter = 0;
atomic_fetch_add(&counter, 1);  // Atomar!
```

---

## Praktische Beispiele aus der Geschichte

Race Conditions haben zu einigen der spektakulärsten Software-Fehler geführt. Diese Beispiele zeigen, dass das Problem nicht akademisch ist, sondern reale Konsequenzen hat.

### Linux Kernel: Dirty COW (CVE-2016-5195)

Eine der bekanntesten Race Conditions der jüngeren Geschichte. Der Name "Dirty COW" bezieht sich auf Copy-on-Write (COW), einen Mechanismus zur Speicheroptimierung.

**Das Problem:** Im Copy-on-Write-Code des Linux-Kernels existierte ein winziges Zeitfenster zwischen der Berechtigungsprüfung und dem tatsächlichen Schreibvorgang. Ein Angreifer konnte dieses Fenster ausnutzen, um Schreibzugriff auf eigentlich schreibgeschützte Dateien zu erlangen.

**Die Konsequenzen:**
- Lokale Privilege Escalation zu Root
- Angreifer konnte beliebige Dateien überschreiben (z.B. `/etc/passwd`)
- Der Bug war seit 2007 im Kernel – also 9 Jahre unentdeckt
- Betroffen waren Millionen von Linux-Servern und Android-Geräten

> [!warning] **9 Jahre unentdeckt**
> Dirty COW zeigt, wie lange Race Conditions unentdeckt bleiben können. Der Code wurde tausendfach reviewed, der Bug blieb verborgen.

### Therac-25 (1985-1987)

Ein tragisches Beispiel, bei dem Race Conditions Menschenleben kosteten. Der Therac-25 war ein medizinisches Bestrahlungsgerät.

**Das Problem:** Eine Race Condition zwischen der Benutzeroberfläche und der Maschinensteuerung. Wenn ein Operator schnell genug tippte, konnte er den Sicherheitszustand der Maschine ändern, bevor die entsprechenden Hardware-Schutzmaßnahmen aktiviert wurden.

**Die Konsequenzen:**
- Mindestens 6 Patienten erhielten massive Überdosen
- 3 Patienten starben direkt an den Folgen
- Der Bug war schwer zu reproduzieren (abhängig von der Tippgeschwindigkeit)
- Führte zu grundlegenden Änderungen in der Zertifizierung medizinischer Software

### Northeast Blackout (2003)

Der Stromausfall, der 55 Millionen Menschen in den USA und Kanada betraf, wurde durch eine Race Condition in einem Alarm-System verschlimmert.

**Das Problem:** Eine Race Condition im XA/21-Energiemanagementsystem führte dazu, dass Alarme nicht angezeigt wurden. Die Operatoren wussten nicht, dass Leitungen überlastet waren.

**Die Konsequenz:** Was ein lokales Problem hätte bleiben können, kaskadierte zu einem flächendeckenden Blackout.

---

## Zusammenhänge

- [[02-Kritische-Abschnitte|Kritische Abschnitte]] → Race Conditions treten in kritischen Abschnitten auf
- [[04-Deadlocks|Deadlocks]] → Falsche Synchronisation führt zu Deadlocks
- [[05-Synchronisationsmechanismen|Synchronisationsmechanismen]] → Lösungen für Race Conditions
- [[03-Threads|Threads]] → Threads teilen Adressraum → anfällig für Race Conditions

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - Definition Race Condition
> - Warum x++ nicht atomar ist
> - Lost Update Problem (Bankbeispiel)
> - Drei Voraussetzungen für Race Conditions
> - TOCTOU-Probleme

> [!question] **Häufige Prüfungsfragen**
> 1. Was ist eine Race Condition? Geben Sie ein Beispiel!
> 2. Warum ist die Operation x++ nicht atomar?
> 3. Welche Bedingungen müssen für eine Race Condition erfüllt sein?
> 4. Wie kann man Race Conditions vermeiden?
> 5. Analysieren Sie folgenden Code auf Race Conditions!

> [!tip] **Merkhilfen**
> - **Race Condition** = "Wettrennen mit unvorhersagbarem Sieger"
> - **Lost Update** = "Beide editieren gleichzeitig, einer verliert"
> - **TOCTOU** = "Zwischen Schauen und Handeln ändert sich die Welt"
> - **Heisenbug** = "Der Bug, der verschwindet, wenn du ihn anschaust"
> - **Drei Bedingungen** = "Shared + Write + No Sync = Race"
> - **Vermeidung** = "Nicht teilen, nicht ändern, oder synchronisieren"

---

## Weiterführende Ressourcen

> [!note] **Videos (YouTube)**
>
> | | Video | Beschreibung |
> |---|-------|--------------|
> | 🎬 | [Vfhcap eduloop – Race Conditions](https://www.youtube.com/watch?v=dlOg4Dz-bgM) | Race Conditions erklärt (Deutsch) |
> | 🎬 | [CoreDumped – Concurrency](https://www.youtube.com/watch?v=3X93PnKRNUo) | Nebenläufigkeit und ihre Gefahren |

> [!note] **Workshop-Links**
> - Race Condition Beispielcode: https://dextutor.com/program-to-simulate-race-condition/
> - Java Race Conditions: https://www.javatpoint.com/race-condition-in-java

---

## Quellen

- IU Skript: Betriebssysteme, Rechnernetze und verteilte Systeme - Teil 5 (Ressourcen)
- Tanenbaum: Modern Operating Systems
- CVE-2016-5195 "Dirty COW": https://dirtycow.ninja/
