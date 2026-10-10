---
author: Andreas Hümmer
title: Kritische Abschnitte
tags:
  - content
  - bs
  - synchronisation
  - kritischer-abschnitt
  - mutex
  - race-condition
created: '2026-10-07'
modified: '2026-10-07'
bereich: BS
---

# Kritische Abschnitte

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das Problem der Prozesssynchronisation verstehen
> - Kritische Abschnitte identifizieren können
> - Die Anforderungen an eine Lösung kennen (Mutual Exclusion, Progress, Bounded Waiting)
> - Race Conditions erkennen und vermeiden können
> - Verschiedene Lösungsansätze (aktives Warten, Hardware, OS, Sprache) unterscheiden

---

## Definition

> [!quote] **Formale Definition**
> Ein **kritischer Abschnitt** ist ein Programmabschnitt, in dem es zu Konflikten kommen kann. Kritische Abschnitte dürfen nur von einem Prozess zur gegebenen Zeit durchlaufen werden.

---

## Das Problem

Bei **nebenläufigen Prozessen** muss der Zugriff auf Ressourcen **koordiniert und wohldefiniert** ablaufen.

```
┌─────────────────────────────────────────────────────────────┐
│              PROBLEM: UNKONTROLLIERTER ZUGRIFF              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Prozess A              Gemeinsame              Prozess B  │
│                          Variable                           │
│   ┌─────────┐           ┌─────────┐           ┌─────────┐  │
│   │ x = x+1 │──────────▶│  x = 5  │◀──────────│ x = x*2 │  │
│   └─────────┘           └─────────┘           └─────────┘  │
│                                                             │
│   Problem: Was ist der Endwert von x?                      │
│   - Falls A zuerst: (5+1)*2 = 12                           │
│   - Falls B zuerst: (5*2)+1 = 11                           │
│   - Überlappend: ???  → UNDEFINIERT!                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Race Conditions

> [!quote] **Definition**
> Eine **Race Condition** (Wettlaufsituation) kann auftreten, wenn nebenläufige Prozesse auf gemeinsame Daten zugreifen und mindestens einer davon **schreibend** zugreift. Das Ergebnis ist nicht vorhersagbar und kann inkorrekt sein.

```
┌─────────────────────────────────────────────────────────────┐
│              RACE CONDITION – BEISPIEL                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Kontostand: 1000€                                        │
│                                                             │
│   Thread A: Abheben 200€        Thread B: Einzahlen 100€   │
│   ┌────────────────────┐        ┌────────────────────┐     │
│   │ read(konto) → 1000 │        │ read(konto) → 1000 │     │
│   │ konto = 1000 - 200 │        │ konto = 1000 + 100 │     │
│   │ write(konto) = 800 │        │ write(konto) = 1100│     │
│   └────────────────────┘        └────────────────────┘     │
│                                                             │
│   Erwartet: 1000 - 200 + 100 = 900€                        │
│   Tatsächlich: 800€ ODER 1100€ (je nachdem wer zuletzt     │
│                schreibt)                                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Anforderungen an eine Lösung

Jede Lösung für das Problem kritischer Abschnitte muss erfüllen:

| Anforderung | Beschreibung |
|-------------|--------------|
| **Mutual Exclusion** | Höchstens ein Prozess darf sich gleichzeitig im kritischen Abschnitt befinden |
| **Progress** (Fortschritt) | Wenn kein Prozess im kritischen Abschnitt ist, muss ein wartender Prozess eintreten können |
| **Bounded Waiting** | Kein Prozess darf unendlich lange warten (keine Starvation) |

```
┌─────────────────────────────────────────────────────────────┐
│              KRITISCHER ABSCHNITT – STRUKTUR                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌────────────────────────────────────────────────────┐   │
│   │              Entry Section                          │   │
│   │         (Erlaubnis einholen / warten)              │   │
│   └────────────────────────────────────────────────────┘   │
│                          │                                  │
│                          ▼                                  │
│   ╔════════════════════════════════════════════════════╗   │
│   ║           KRITISCHER ABSCHNITT                      ║   │
│   ║      (Zugriff auf gemeinsame Ressource)            ║   │
│   ║                                                     ║   │
│   ║      Nur EIN Prozess gleichzeitig!                 ║   │
│   ╚════════════════════════════════════════════════════╝   │
│                          │                                  │
│                          ▼                                  │
│   ┌────────────────────────────────────────────────────┐   │
│   │              Exit Section                           │   │
│   │          (Ressource freigeben)                     │   │
│   └────────────────────────────────────────────────────┘   │
│                          │                                  │
│                          ▼                                  │
│   ┌────────────────────────────────────────────────────┐   │
│   │           Remainder Section                         │   │
│   │        (Nicht-kritischer Code)                     │   │
│   └────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Lösungsansätze

### Übersicht

```
┌─────────────────────────────────────────────────────────────┐
│              LÖSUNGSANSÄTZE                                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. Aktives Warten (Busy Waiting)                          │
│     └── Spinlocks                                          │
│                                                             │
│  2. Mit Hardwareunterstützung                              │
│     ├── Unterbrechungssperre                               │
│     └── Atomare Operationen (Test-and-Set, Compare-and-Swap)│
│                                                             │
│  3. Mit Betriebssystemunterstützung                        │
│     └── Semaphore                                          │
│                                                             │
│  4. Mit Sprachunterstützung                                │
│     └── Monitore                                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 1. Aktives Warten (Spinlock)

```c
// Einfacher Spinlock (NICHT sicher!)
while (lock == 1) {
    // Warten (Busy Waiting)
}
lock = 1;        // Kritischer Abschnitt betreten

// ... kritischer Abschnitt ...

lock = 0;        // Verlassen
```

> [!warning] **Problem**
> Diese einfache Version ist **nicht sicher** – zwischen Prüfung und Setzen kann ein Kontextwechsel stattfinden!

### 2. Hardware: Test-and-Set (Atomare Operation)

```c
// Test-and-Set ist ATOMAR (nicht unterbrechbar)
bool test_and_set(bool *lock) {
    bool old = *lock;
    *lock = true;
    return old;     // Gibt alten Wert zurück
}

// Verwendung:
while (test_and_set(&lock)) {
    // Warten
}
// Kritischer Abschnitt
lock = false;
```

### 3. Betriebssystem: Semaphore

Siehe → [[02-Semaphore|Semaphore]]

### 4. Sprache: Monitore

```
┌─────────────────────────────────────────────────────────────┐
│                      MONITOR                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌─────────────────────────────────────────────────────┐  │
│   │              MONITOR "BankKonto"                    │  │
│   │  ┌─────────────────────────────────────────────┐    │  │
│   │  │  Private Daten:                             │    │  │
│   │  │    - kontostand: int                        │    │  │
│   │  └─────────────────────────────────────────────┘    │  │
│   │                                                     │  │
│   │  ┌─────────────────────────────────────────────┐    │  │
│   │  │  Methoden (nur eine gleichzeitig aktiv):    │    │  │
│   │  │    - einzahlen(betrag)                      │    │  │
│   │  │    - abheben(betrag)                        │    │  │
│   │  │    - kontostand_abfragen()                  │    │  │
│   │  └─────────────────────────────────────────────┘    │  │
│   └─────────────────────────────────────────────────────┘  │
│                                                             │
│   → Mutex ist in den Monitor eingebaut!                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Praktische Beispiele

### Java: synchronized

```java
public class BankKonto {
    private int kontostand = 0;
    
    public synchronized void einzahlen(int betrag) {
        kontostand += betrag;  // Kritischer Abschnitt
    }
    
    public synchronized void abheben(int betrag) {
        kontostand -= betrag;  // Kritischer Abschnitt
    }
}
```

### C: pthread_mutex

```c
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;

pthread_mutex_lock(&lock);
// Kritischer Abschnitt
kontostand += betrag;
pthread_mutex_unlock(&lock);
```

---

## Zusammenhänge

- [[02-Semaphore|Semaphore]] → Lösung für kritische Abschnitte
- [[03-Deadlocks|Deadlocks]] → Können bei falscher Synchronisation entstehen
- [[03-Threads|Threads]] → Threads teilen Adressraum → kritische Abschnitte nötig

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - Definition kritischer Abschnitt und Race Condition
> - Die drei Anforderungen (Mutual Exclusion, Progress, Bounded Waiting)
> - Lösungsansätze im Überblick
> - Warum einfaches Busy Waiting nicht funktioniert

> [!question] **Häufige Prüfungsfragen**
> 1. Was ist ein kritischer Abschnitt und wann tritt er auf?
> 2. Was ist eine Race Condition? Geben Sie ein Beispiel!
> 3. Nennen Sie die drei Anforderungen an eine Lösung für kritische Abschnitte!
> 4. Warum ist ein einfacher Spinlock ohne atomare Operationen nicht sicher?
> 5. Welche Lösungsansätze gibt es für das Problem kritischer Abschnitte?

> [!tip] **Merkhilfen**
> - **Kritischer Abschnitt** = "Engpass auf der Einbahnstraße"
> - **Race Condition** = "Zwei greifen gleichzeitig zum letzten Keks"
> - **Mutex** = "Mutually Exclusive" = gegenseitiger Ausschluss
> - **Test-and-Set** = "Atomar prüfen UND setzen in einem Schritt"

---

## Weiterführende Ressourcen

> [!note] **Videos (YouTube)**
> 
> | | Video | Beschreibung |
> |---|-------|--------------|
> | 🎬 | [Vfhcap eduloop – Race Conditions](https://www.youtube.com/watch?v=dlOg4Dz-bgM) | Race Conditions erklärt (Deutsch) |
> | 🎬 | [CoreDumped – Concurrency](https://www.youtube.com/watch?v=3X93PnKRNUo) | Nebenläufigkeit und Synchronisation |

> [!note] **Workshop-Links**
> - Race Condition Beispielcode: https://dextutor.com/program-to-simulate-race-condition/
> - Java Race Conditions: https://www.javatpoint.com/race-condition-in-java

---

## Quellen

- IU Skript: Betriebssysteme, Rechnernetze und verteilte Systeme - Teil 5 (Ressourcen)
- Tanenbaum: Modern Operating Systems
