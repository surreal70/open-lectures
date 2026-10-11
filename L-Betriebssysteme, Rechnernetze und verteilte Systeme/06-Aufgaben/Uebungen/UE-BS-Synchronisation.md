---
author: Andreas Hümmer
title: 'Übung: Synchronisation'
tags:
  - uebung
  - bs
  - synchronisation
  - kritischer-abschnitt
  - race-condition
  - deadlock
  - semaphore
punkte_gesamt: 50
bearbeitungszeit: 90
bereich: BS
created: '2026-10-09'
modified: '2026-10-09'
---

# Übung: Synchronisation

**Bereich:** BS – Prozesssynchronisation
**Gesamtpunktzahl:** 50 Punkte
**Bearbeitungszeit:** ca. 90 Minuten

---

> [!info] **Themenübersicht**
> Diese Übung deckt die zentralen Themen der Prozesssynchronisation ab:
> - Kritische Abschnitte (Aufgaben 1-2)
> - Race Conditions (Aufgaben 3-4)
> - Deadlocks (Aufgaben 5-7)
> - Synchronisationsmechanismen (Aufgaben 8-10)

---

## Teil 1: Kritische Abschnitte (10 Punkte)

### Aufgabe 1: Definition und Struktur (4 Punkte) ⭐

a) **Was ist ein kritischer Abschnitt und wann tritt er auf?** (2 Punkte)

_Dein Antwort:_

<br><br><br>

b) **Erklären Sie die Struktur eines kritischen Abschnitts.** Benennen Sie die vier Abschnitte (Entry Section, Critical Section, Exit Section, Remainder Section) und deren Funktion. (2 Punkte)

_Dein Antwort:_

<br><br><br>

---

### Aufgabe 2: Anforderungen (6 Punkte) ⭐⭐

a) **Nennen Sie die drei Anforderungen an eine Lösung für kritische Abschnitte!** (3 Punkte)

| Anforderung | Beschreibung |
|-------------|--------------|
| 1. | |
| 2. | |
| 3. | |

b) **Warum reicht nur Mutual Exclusion nicht aus?** Erklären Sie anhand eines Beispiels, was passiert, wenn Progress oder Bounded Waiting fehlt. (3 Punkte)

_Dein Antwort:_

<br><br><br>

---

## Teil 2: Race Conditions (12 Punkte)

### Aufgabe 3: Grundlagen (6 Punkte) ⭐

a) **Was ist eine Race Condition?** Geben Sie eine Definition und ein Alltagsbeispiel. (3 Punkte)

_Dein Antwort:_

<br><br><br>

b) **Welche drei Bedingungen müssen für eine Race Condition erfüllt sein?** (3 Punkte)

| # | Bedingung | Erklärung |
|---|-----------|-----------|
| 1 | | |
| 2 | | |
| 3 | | |

---

### Aufgabe 4: Code-Analyse (6 Punkte) ⭐⭐

a) **Warum ist die Operation `x++` nicht atomar?** Zerlegen Sie die Operation in ihre Einzelschritte und erklären Sie, wo ein Kontextwechsel problematisch wäre. (3 Punkte)

_Dein Antwort:_

<br><br><br>

b) **Analysieren Sie folgenden Code auf Race Conditions.** Identifizieren Sie das Problem und schlagen Sie eine Lösung vor. (3 Punkte)

```java
public class Counter {
    private int count = 0;
    
    public void increment() {
        count = count + 1;
    }
    
    public int getCount() {
        return count;
    }
}

// Thread 1 und Thread 2 rufen gleichzeitig increment() auf
```

_Dein Antwort:_

<br><br><br>

---

## Teil 3: Deadlocks (14 Punkte)

### Aufgabe 5: Coffman-Bedingungen (6 Punkte) ⭐⭐

**Nennen und erklären Sie die vier notwendigen Bedingungen für einen Deadlock (Coffman-Bedingungen)!**

| Bedingung (deutsch) | Bedingung (englisch) | Erklärung |
|---------------------|---------------------|-----------|
| 1. | | |
| 2. | | |
| 3. | | |
| 4. | | |

---

### Aufgabe 6: Deadlock-Strategien (4 Punkte) ⭐⭐

**Welche vier Strategien gibt es zur Behandlung von Deadlocks?** Beschreiben Sie jede kurz.

| Strategie | Beschreibung |
|-----------|--------------|
| 1. Prevention | |
| 2. Avoidance | |
| 3. Detection | |
| 4. Ignorance | |

---

### Aufgabe 7: Resource Allocation Graph (4 Punkte) ⭐⭐⭐

**Gegeben ist folgender Resource Allocation Graph. Liegt ein Deadlock vor? Begründen Sie!**

```
Prozesse: P1, P2, P3
Ressourcen: R1 (1 Instanz), R2 (1 Instanz), R3 (1 Instanz)

Zuteilungen:
- R1 → P1 (R1 ist P1 zugeteilt)
- R2 → P2 (R2 ist P2 zugeteilt)

Anforderungen:
- P1 → R2 (P1 wartet auf R2)
- P2 → R1 (P2 wartet auf R1)
- P3 → R3 (P3 wartet auf R3)
```

a) Zeichnen Sie den Graphen. (2 Punkte)

<br><br><br><br>

b) Liegt ein Deadlock vor? Begründen Sie Ihre Antwort! (2 Punkte)

_Dein Antwort:_

<br><br><br>

---

## Teil 4: Synchronisationsmechanismen (14 Punkte)

### Aufgabe 8: Semaphore (6 Punkte) ⭐⭐

a) **Was sind die Operationen P und V bei Semaphoren? Erklären Sie die Semantik!** (3 Punkte)

| Operation | Alternative Namen | Semantik |
|-----------|-------------------|----------|
| P(S) | | |
| V(S) | | |

b) **Was ist der Unterschied zwischen einem binären Semaphor und einem Counting Semaphor?** (3 Punkte)

_Dein Antwort:_

<br><br><br>

---

### Aufgabe 9: Mutex vs. Semaphor (4 Punkte) ⭐⭐

**Was ist der Unterschied zwischen Mutex und Semaphor?** Nennen Sie mindestens drei Unterschiede.

| Eigenschaft | Mutex | Semaphor |
|-------------|-------|----------|
| Wertebereich | | |
| Ownership | | |
| Typischer Einsatz | | |

---

### Aufgabe 10: Spinlock vs. Mutex (4 Punkte) ⭐⭐⭐

a) **Wann verwendet man Spinlocks, wann Mutexe?** (2 Punkte)

_Dein Antwort:_

<br><br><br>

b) **Warum sind Spinlocks auf Single-Core-Systemen problematisch?** (2 Punkte)

_Dein Antwort:_

<br><br><br>

---

## Bonusaufgabe: Producer-Consumer (5 Punkte) ⭐⭐⭐

**Lösen Sie das Producer-Consumer Problem mit Semaphoren!**

Gegeben:
- Ein Puffer mit N Plätzen
- Ein Producer, der Items produziert und in den Puffer legt
- Ein Consumer, der Items aus dem Puffer nimmt und verarbeitet

Schreiben Sie Pseudocode für Producer und Consumer mit den notwendigen Semaphoren.

```pseudocode
// Semaphoren definieren:


// PRODUCER:
void producer() {
    while (true) {
        item = produce_item();
        
        // Synchronisation:
        
        
        insert_to_buffer(item);
        
        // Synchronisation:
        
    }
}

// CONSUMER:
void consumer() {
    while (true) {
        // Synchronisation:
        
        
        item = remove_from_buffer();
        
        // Synchronisation:
        
        
        consume_item(item);
    }
}
```

---

## Selbsteinschätzung

Nach Bearbeitung der Aufgaben:

| Thema | Sicher | Unsicher | Muss wiederholen |
|-------|:------:|:--------:|:----------------:|
| Kritische Abschnitte | ☐ | ☐ | ☐ |
| Race Conditions | ☐ | ☐ | ☐ |
| Deadlocks | ☐ | ☐ | ☐ |
| Semaphore | ☐ | ☐ | ☐ |
| Mutex/Spinlock | ☐ | ☐ | ☐ |

---

## Quellen

- [[02-Kritische-Abschnitte|Kritische Abschnitte]]
- [[03-Race-Conditions|Race Conditions]]
- [[04-Deadlocks|Deadlocks]]
- [[05-Synchronisationsmechanismen|Synchronisationsmechanismen]]
