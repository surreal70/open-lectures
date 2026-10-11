---
author: Andreas Hümmer
title: 'Lösung: Synchronisation'
tags:
  - loesung
  - bs
  - synchronisation
bereich: BS
created: '2026-10-09'
modified: '2026-10-09'
---

# Lösung: Synchronisation

**Zugehörige Übung:** [[UE-BS-Synchronisation|Übung: Synchronisation]]

---

## Teil 1: Kritische Abschnitte

### Aufgabe 1: Definition und Struktur

**a) Was ist ein kritischer Abschnitt und wann tritt er auf?**

> [!success] **Musterlösung**
> Ein **kritischer Abschnitt** ist ein Programmabschnitt, in dem auf **gemeinsame Ressourcen** (Shared Resources) zugegriffen wird. Er tritt auf, wenn:
> - Mehrere Prozesse/Threads auf dieselben Daten zugreifen
> - Mindestens einer dieser Zugriffe schreibend ist
> 
> Kritische Abschnitte dürfen nur von einem Prozess zur gegebenen Zeit durchlaufen werden, um Race Conditions zu vermeiden.

**b) Struktur eines kritischen Abschnitts:**

> [!success] **Musterlösung**
> | Abschnitt | Funktion |
> |-----------|----------|
> | **Entry Section** | Hier versucht der Prozess, Zugang zum kritischen Abschnitt zu erlangen. Er wartet ggf. bis er an der Reihe ist. |
> | **Critical Section** | Der eigentliche geschützte Bereich, in dem auf gemeinsame Ressourcen zugegriffen wird. |
> | **Exit Section** | Der Prozess gibt seinen exklusiven Zugang auf und signalisiert anderen wartenden Prozessen. |
> | **Remainder Section** | Alles, was nicht zum kritischen Abschnitt gehört – nicht-kritischer Code. |

---

### Aufgabe 2: Anforderungen

**a) Die drei Anforderungen:**

> [!success] **Musterlösung**
> | Anforderung | Beschreibung |
> |-------------|--------------|
> | **Mutual Exclusion** | Höchstens ein Prozess darf sich zu jedem Zeitpunkt im kritischen Abschnitt befinden. |
> | **Progress** | Wenn kein Prozess im kritischen Abschnitt ist und mindestens einer eintreten möchte, muss die Entscheidung in endlicher Zeit fallen. |
> | **Bounded Waiting** | Es gibt eine obere Schranke, wie oft andere Prozesse eintreten dürfen, während ein bestimmter Prozess wartet. |

**b) Warum reicht Mutual Exclusion nicht aus?**

> [!success] **Musterlösung**
> - **Ohne Progress:** Zwei Prozesse könnten sich gegenseitig "nach Ihnen" sagen (Livelock). Keiner tritt ein, obwohl beide wollen und der Abschnitt frei ist.
> - **Ohne Bounded Waiting:** Ein Prozess könnte ewig warten, weil immer wieder andere "vordrängeln" (Starvation).
> 
> **Beispiel:** Ein Mutex, der bei gleichzeitigem Ankommen immer dem gleichen Prozess (z.B. nach ID) Vorrang gibt, erfüllt Mutual Exclusion und Progress, aber nicht Bounded Waiting – Prozesse mit hoher ID können verhungern.

---

## Teil 2: Race Conditions

### Aufgabe 3: Grundlagen

**a) Was ist eine Race Condition?**

> [!success] **Musterlösung**
> Eine **Race Condition** (Wettlaufsituation) tritt auf, wenn das Ergebnis einer Berechnung vom **zeitlichen Ablauf** nebenläufiger Operationen abhängt.
> 
> **Alltagsbeispiel:** Zwei Personen bearbeiten gleichzeitig dasselbe Google-Doc-Dokument. Beide sehen "10 Äpfel", einer ändert zu "15", der andere zu "12". Je nachdem, wessen Änderung zuletzt synchronisiert wird, steht am Ende 15 oder 12 – nicht das erwartete Ergebnis beider Änderungen.

**b) Die drei Bedingungen:**

> [!success] **Musterlösung**
> | # | Bedingung | Erklärung |
> |---|-----------|-----------|
> | 1 | **Shared State** | Mehrere Threads/Prozesse greifen auf dieselben Daten zu |
> | 2 | **Mindestens ein Write** | Mindestens ein Thread verändert die Daten (nur Lesen ist harmlos) |
> | 3 | **Keine Synchronisation** | Kein Mechanismus koordiniert den Zugriff |
> 
> → Entferne eine Bedingung = Keine Race Condition möglich!

---

### Aufgabe 4: Code-Analyse

**a) Warum ist `x++` nicht atomar?**

> [!success] **Musterlösung**
> Die Operation `x++` besteht auf Maschinenebene aus drei Schritten:
> 
> ```
> 1. LOAD  x → Register    (Wert aus Speicher in Register laden)
> 2. ADD   1 → Register    (1 zum Registerwert addieren)
> 3. STORE Register → x    (Ergebnis zurück in Speicher schreiben)
> ```
> 
> **Problem:** Zwischen jedem dieser Schritte kann ein Kontextwechsel stattfinden. Wenn zwei Threads gleichzeitig `x++` ausführen und beide LOAD ausführen, bevor einer STORE macht, liest Thread B den alten Wert, den Thread A noch nicht zurückgeschrieben hat. Beide erhöhen denselben Ausgangswert → ein Inkrement geht verloren.

**b) Code-Analyse:**

> [!success] **Musterlösung**
> **Problem:** Die Methode `increment()` ist nicht thread-safe. Der Ausdruck `count = count + 1` ist nicht atomar (siehe oben).
> 
> Wenn Thread 1 und Thread 2 gleichzeitig `increment()` aufrufen:
> - Beide lesen `count = 0`
> - Beide berechnen `0 + 1 = 1`
> - Beide schreiben `1` zurück
> - Ergebnis: `count = 1` statt erwartet `count = 2`
> 
> **Lösung:**
> ```java
> public class Counter {
>     private int count = 0;
>     
>     public synchronized void increment() {  // synchronized hinzufügen
>         count = count + 1;
>     }
>     
>     public synchronized int getCount() {
>         return count;
>     }
> }
> ```
> Oder mit `AtomicInteger`: `private AtomicInteger count = new AtomicInteger(0);`

---

## Teil 3: Deadlocks

### Aufgabe 5: Coffman-Bedingungen

> [!success] **Musterlösung**
> | Bedingung (deutsch) | Bedingung (englisch) | Erklärung |
> |---------------------|---------------------|-----------|
> | **Gegenseitiger Ausschluss** | Mutual Exclusion | Ressourcen können nur von einem Prozess gleichzeitig genutzt werden |
> | **Halten und Warten** | Hold and Wait | Ein Prozess hält Ressourcen und wartet auf weitere |
> | **Keine Entziehbarkeit** | No Preemption | Ressourcen können nur freiwillig freigegeben werden, nicht entzogen |
> | **Zyklisches Warten** | Circular Wait | Es existiert eine zyklische Kette wartender Prozesse (P1→P2→...→Pn→P1) |
> 
> **Wichtig:** Ein Deadlock kann **nur** auftreten, wenn **alle vier** Bedingungen gleichzeitig erfüllt sind!

---

### Aufgabe 6: Deadlock-Strategien

> [!success] **Musterlösung**
> | Strategie | Beschreibung |
> |-----------|--------------|
> | **Prevention** | Eine der vier Coffman-Bedingungen **strukturell unmöglich** machen (z.B. Ressourcen-Ordnung gegen Circular Wait) |
> | **Avoidance** | Vor jeder Ressourcenzuteilung prüfen, ob der resultierende Zustand noch "sicher" ist (z.B. Banker's Algorithm) |
> | **Detection** | Deadlocks zulassen, aber periodisch erkennen und dann beheben (Prozess abbrechen, Ressourcen entziehen) |
> | **Ignorance** | "Ostrich Algorithm" – Deadlocks ignorieren und hoffen, dass sie selten genug sind (Linux, Windows nutzen dies für User-Prozesse) |

---

### Aufgabe 7: Resource Allocation Graph

> [!success] **Musterlösung**
> 
> **a) Graph:**
> ```
>     R1 ───────→ P1
>     ↑            │
>     │            │ (wartet auf)
>     │            ↓
>     P2 ←─────── R2
>     
>     P3 ───→ R3 (keine Zuteilung, nur Anforderung)
> ```
> 
> **b) Deadlock-Analyse:**
> 
> **JA, es liegt ein Deadlock vor**, aber nur für P1 und P2:
> - P1 hält R1 und wartet auf R2
> - P2 hält R2 und wartet auf R1
> - Es existiert ein **Zyklus**: P1 → R2 → P2 → R1 → P1
> 
> P3 ist nicht im Deadlock – es wartet nur auf R3, das nicht zugeteilt ist. Sobald R3 frei wird (oder zugeteilt wird), kann P3 weiterlaufen.

---

## Teil 4: Synchronisationsmechanismen

### Aufgabe 8: Semaphore

**a) P und V Operationen:**

> [!success] **Musterlösung**
> | Operation | Alternative Namen | Semantik |
> |-----------|-------------------|----------|
> | **P(S)** | wait, down, acquire | Wenn S > 0: dekrementiere S und fahre fort. Sonst: blockiere den Prozess bis S > 0 wird. |
> | **V(S)** | signal, up, release | Inkrementiere S. Falls Prozesse auf S warten, wecke einen davon auf. |
> 
> Die Namen kommen aus dem Niederländischen: **P**roberen (versuchen) und **V**erhogen (erhöhen).
> 
> **Merkhilfe:** P = "**P**assieren wollen", V = "**V**erlassen"

**b) Binär vs. Counting Semaphor:**

> [!success] **Musterlösung**
> | Eigenschaft | Binärer Semaphor | Counting Semaphor |
> |-------------|------------------|-------------------|
> | **Wertebereich** | 0 oder 1 | 0 bis N |
> | **Initialisierung** | Meist 1 | Anzahl verfügbarer Ressourcen |
> | **Typischer Einsatz** | Gegenseitiger Ausschluss (wie Mutex) | Verwaltung begrenzter Ressourcen (z.B. Connection Pool) |
> | **Beispiel** | Zugang zu kritischem Abschnitt | 5 Datenbankverbindungen im Pool |

---

### Aufgabe 9: Mutex vs. Semaphor

> [!success] **Musterlösung**
> | Eigenschaft | Mutex | Semaphor |
> |-------------|-------|----------|
> | **Wertebereich** | 0 oder 1 (binär) | 0 bis N (beliebig nicht-negativ) |
> | **Ownership** | Nur der Besitzer (der Thread, der gelockt hat) kann freigeben | Jeder kann V aufrufen |
> | **Typischer Einsatz** | Schutz kritischer Abschnitte | Ressourcenzählung, Producer-Consumer, Signalisierung |
> | **Rekursion** | Oft rekursiv (reentrant) – gleicher Thread kann mehrfach locken | Nie rekursiv |
> 
> **Wichtiger Unterschied:** Mutex hat Ownership-Semantik. Wenn Thread A den Mutex nimmt, kann nur Thread A ihn freigeben. Bei Semaphoren kann Thread B für Thread A "signalisieren" – das ist beabsichtigt (z.B. Producer signalisiert Consumer), kann aber auch zu Bugs führen.

---

### Aufgabe 10: Spinlock vs. Mutex

**a) Wann Spinlock, wann Mutex?**

> [!success] **Musterlösung**
> **Spinlock verwenden wenn:**
> - Kritischer Abschnitt ist **sehr kurz** (wenige Instruktionen)
> - **Multiprozessorsystem** (anderer Kern kann Lock freigeben während wir spinnen)
> - **Kontextwechsel wäre teurer** als kurzes Busy-Waiting
> - Im Kernel, wenn man nicht schlafen darf (z.B. Interrupt-Handler)
> 
> **Mutex verwenden wenn:**
> - Kritischer Abschnitt ist **länger** oder **unbekannte Dauer**
> - **Single-Core-System** oder wenn CPU-Effizienz wichtig
> - In **Anwendungsprogrammen** (fast immer)

**b) Spinlocks auf Single-Core:**

> [!success] **Musterlösung**
> Auf einem Single-Core-System ist nur **ein Thread gleichzeitig aktiv**. Wenn Thread A spinnt (busy waits), kann Thread B (der den Lock hält) **niemals laufen**, um den Lock freizugeben – es gibt nur einen Kern!
> 
> Das Ergebnis: Thread A spinnt für immer, bis sein Zeitquantum abläuft und der Scheduler Thread B aktiviert. Das ist extrem ineffizient – Thread A verschwendet sein gesamtes Zeitquantum mit nutzlosem Spinning.
> 
> Ein Mutex würde Thread A sofort schlafen legen → Thread B läuft sofort → Lock wird schneller frei.

---

## Bonusaufgabe: Producer-Consumer

> [!success] **Musterlösung**
> ```pseudocode
> // Semaphoren definieren:
> Semaphore mutex = 1;   // Schützt den Pufferzugriff
> Semaphore empty = N;   // Zählt freie Plätze (anfangs N)
> Semaphore full = 0;    // Zählt belegte Plätze (anfangs 0)
> 
> // PRODUCER:
> void producer() {
>     while (true) {
>         item = produce_item();
>         
>         P(empty);          // Warte auf freien Platz
>         P(mutex);          // Exklusiver Pufferzugriff
>         
>         insert_to_buffer(item);
>         
>         V(mutex);          // Pufferzugriff freigeben
>         V(full);           // Ein belegter Platz mehr
>     }
> }
> 
> // CONSUMER:
> void consumer() {
>     while (true) {
>         P(full);           // Warte auf belegten Platz
>         P(mutex);          // Exklusiver Pufferzugriff
>         
>         item = remove_from_buffer();
>         
>         V(mutex);          // Pufferzugriff freigeben
>         V(empty);          // Ein freier Platz mehr
>         
>         consume_item(item);
>     }
> }
> ```
> 
> **Erklärung:**
> - `empty` zählt, wie viele Plätze noch frei sind → Producer wartet wenn voll
> - `full` zählt, wie viele Plätze belegt sind → Consumer wartet wenn leer
> - `mutex` schützt den gemeinsamen Puffer vor gleichzeitigem Zugriff
> 
> **Wichtig:** Die Reihenfolge `P(empty); P(mutex)` (nicht umgekehrt!) verhindert Deadlocks. Würde der Producer `P(mutex); P(empty)` machen, könnte er mit dem Mutex blockieren während er auf `empty` wartet – der Consumer kommt nicht mehr an den Puffer.

---

## Quellen

- [[02-Kritische-Abschnitte|Kritische Abschnitte]]
- [[03-Race-Conditions|Race Conditions]]
- [[04-Deadlocks|Deadlocks]]
- [[05-Synchronisationsmechanismen|Synchronisationsmechanismen]]
