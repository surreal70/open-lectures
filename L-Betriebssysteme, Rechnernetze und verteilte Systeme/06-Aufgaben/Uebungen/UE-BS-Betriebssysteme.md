---
author: Andreas Hümmer
title: 'Übung: Betriebssysteme (Klausurformat)'
tags:
  - uebung
  - bs
  - klausur
  - definition
  - kernel
  - prozesse
  - scheduling
  - threads
  - synchronisation
  - speicher
  - paging
punkte_gesamt: 120
bearbeitungszeit: 180
bereich: BS
created: '2026-10-09'
modified: '2026-10-09'
---

# Übung: Betriebssysteme (Klausurformat)

**Bereich:** BS – Alle Kapitel
**Gesamtpunktzahl:** 120 Punkte
**Bearbeitungszeit:** ca. 180 Minuten

---

> [!info] **Themenübersicht**
> Diese Übung deckt die zentralen Themen des Moduls Betriebssysteme ab:
> - Teil 1: Grundlagen und Definition (15 Punkte)
> - Teil 2: Architektur und Kerneltypen (15 Punkte)
> - Teil 3: Prozesse (15 Punkte)
> - Teil 4: Scheduling (15 Punkte)
> - Teil 5: Threads (15 Punkte)
> - Teil 6: Synchronisation (25 Punkte)
> - Teil 7: Speicherverwaltung (20 Punkte)

---

## Teil 1: Grundlagen und Definition (15 Punkte)

### Aufgabe 1.1: Definition Betriebssystem (6 Punkte) ⭐

a) **Nennen Sie die Definition eines Betriebssystems nach Tanenbaum!** (2 Punkte)

_Dein Antwort:_

<br><br><br>

b) **Erklären Sie die zwei Sichtweisen auf ein Betriebssystem (Top-Down und Bottom-Up).** (4 Punkte)

| Sichtweise | Perspektive | Beschreibung |
|------------|-------------|--------------|
| Top-Down | | |
| Bottom-Up | | |

---

### Aufgabe 1.2: Kernaufgaben (5 Punkte) ⭐

**Nennen Sie fünf Kernaufgaben eines Betriebssystems und beschreiben Sie jeweils kurz deren Funktion.**

| Nr. | Aufgabe | Funktion |
|-----|---------|----------|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |

---

### Aufgabe 1.3: Betriebssystem-Typen (4 Punkte) ⭐⭐

**Erklären Sie den Unterschied zwischen einem Echtzeit-Betriebssystem (RTOS) und einem General-Purpose-Betriebssystem anhand von drei Kriterien.**

| Kriterium | RTOS | General-Purpose OS |
|-----------|------|-------------------|
| 1. | | |
| 2. | | |
| 3. | | |

---

## Teil 2: Architektur und Kerneltypen (15 Punkte)

### Aufgabe 2.1: Kerneltypen (6 Punkte) ⭐⭐

a) **Nennen Sie die drei Haupt-Kernel-Architekturen und geben Sie jeweils ein Beispiel-Betriebssystem an.** (3 Punkte)

| Architektur | Beispiel-OS |
|-------------|-------------|
| | |
| | |
| | |

b) **Nennen Sie für den monolithischen Kernel zwei Vorteile und zwei Nachteile.** (3 Punkte)

| | Monolithischer Kernel |
|-----------|---------------------|
| **Vorteile** | |
| **Nachteile** | |

---

### Aufgabe 2.2: Systemaufrufe (5 Punkte) ⭐⭐

a) **Was ist ein Systemaufruf (System Call) und wozu wird er benötigt?** (2 Punkte)

_Dein Antwort:_

<br><br><br>

b) **Erklären Sie den Ablauf eines Systemaufrufs. Was passiert zwischen User-Mode und Kernel-Mode?** (3 Punkte)

_Dein Antwort:_

<br><br><br>

---

### Aufgabe 2.3: Privilegienstufen (4 Punkte) ⭐⭐

**Erklären Sie den Unterschied zwischen User-Mode (Ring 3) und Kernel-Mode (Ring 0). Warum gibt es diese Trennung?**

_Dein Antwort:_

<br><br><br>

---

## Teil 3: Prozesse (15 Punkte)

### Aufgabe 3.1: Prozess vs. Programm (4 Punkte) ⭐

**Erklären Sie den Unterschied zwischen einem Programm und einem Prozess.** Verwenden Sie eine Analogie.

| Aspekt | Programm | Prozess |
|--------|----------|---------|
| Zustand | | |
| Speicher | | |
| Ressourcen | | |
| **Analogie** | | |

---

### Aufgabe 3.2: Prozesszustände (6 Punkte) ⭐⭐

a) **Zeichnen Sie das Drei-Zustands-Modell eines Prozesses mit allen Zuständen und Übergängen.** (3 Punkte)

<br><br><br><br><br>

b) **Beschriften Sie die Übergänge mit den auslösenden Ereignissen.** (3 Punkte)

| Übergang | Auslösendes Ereignis |
|----------|---------------------|
| Ready → Running | |
| Running → Ready | |
| Running → Blocked | |
| Blocked → Ready | |

---

### Aufgabe 3.3: Process Control Block (5 Punkte) ⭐⭐

**Nennen Sie fünf Kategorien von Informationen, die im Process Control Block (PCB) gespeichert werden, und geben Sie jeweils ein konkretes Beispiel.**

| Kategorie | Beispiel |
|-----------|----------|
| 1. | |
| 2. | |
| 3. | |
| 4. | |
| 5. | |

---

## Teil 4: Scheduling (15 Punkte)

### Aufgabe 4.1: Scheduling-Grundlagen (5 Punkte) ⭐

a) **Was ist der Unterschied zwischen preemptive und non-preemptive Scheduling?** (3 Punkte)

| Eigenschaft | Preemptive | Non-Preemptive |
|-------------|------------|----------------|
| Verdrängung | | |
| Beispiel-Algorithmus | | |

b) **Warum verwenden moderne Desktop-Betriebssysteme preemptive Scheduling?** (2 Punkte)

_Dein Antwort:_

<br><br><br>

---

### Aufgabe 4.2: Scheduling-Algorithmen (6 Punkte) ⭐⭐

**Beschreiben Sie kurz die folgenden Scheduling-Algorithmen und nennen Sie jeweils einen Vor- und Nachteil:**

| Algorithmus | Beschreibung | Vorteil | Nachteil |
|-------------|--------------|---------|----------|
| FCFS | | | |
| Round Robin | | | |
| SJF | | | |

---

### Aufgabe 4.3: Scheduling-Berechnung (4 Punkte) ⭐⭐⭐

**Gegeben sind folgende Prozesse:**

| Prozess | Ankunftszeit | Burst-Zeit |
|---------|--------------|------------|
| P1 | 0 | 8 |
| P2 | 1 | 4 |
| P3 | 2 | 2 |

**Berechnen Sie die durchschnittliche Wartezeit bei FCFS (First Come First Serve).**

| Prozess | Startzeit | Endzeit | Wartezeit |
|---------|-----------|---------|-----------|
| P1 | | | |
| P2 | | | |
| P3 | | | |
| **Durchschnitt:** | | | |

---

## Teil 5: Threads (15 Punkte)

### Aufgabe 5.1: Thread-Grundlagen (5 Punkte) ⭐

a) **Was ist ein Thread und worin unterscheidet er sich von einem Prozess?** (3 Punkte)

_Dein Antwort:_

<br><br><br>

b) **Welche Ressourcen teilen sich Threads eines Prozesses, welche nicht?** (2 Punkte)

| Geteilt | Nicht geteilt |
|---------|---------------|
| | |
| | |

---

### Aufgabe 5.2: User-Level vs. Kernel-Level Threads (6 Punkte) ⭐⭐

**Vergleichen Sie User-Level Threads und Kernel-Level Threads anhand der folgenden Kriterien:**

| Kriterium | User-Level Threads | Kernel-Level Threads |
|-----------|-------------------|---------------------|
| Kontextwechsel | | |
| Multicore-Nutzung | | |
| Blockierender Syscall | | |

---

### Aufgabe 5.3: Multithreading vs. Multiprocessing (4 Punkte) ⭐⭐

**Erklären Sie den Unterschied zwischen Multithreading, Multitasking und Multiprocessing.**

| Begriff | Ebene | Beschreibung |
|---------|-------|--------------|
| Multithreading | | |
| Multitasking | | |
| Multiprocessing | | |

---

## Teil 6: Synchronisation (25 Punkte)

### Aufgabe 6.1: Kritische Abschnitte (5 Punkte) ⭐

a) **Was ist ein kritischer Abschnitt?** (2 Punkte)

_Dein Antwort:_

<br><br><br>

b) **Nennen Sie die drei Anforderungen an eine Lösung für kritische Abschnitte.** (3 Punkte)

| Anforderung | Beschreibung |
|-------------|--------------|
| 1. | |
| 2. | |
| 3. | |

---

### Aufgabe 6.2: Race Conditions (6 Punkte) ⭐⭐

a) **Was ist eine Race Condition?** (2 Punkte)

_Dein Antwort:_

<br><br><br>

b) **Warum ist die Operation `x++` nicht atomar? Zerlegen Sie die Operation in ihre Einzelschritte.** (4 Punkte)

_Dein Antwort:_

<br><br><br>

---

### Aufgabe 6.3: Deadlocks (8 Punkte) ⭐⭐

a) **Nennen und erklären Sie die vier Coffman-Bedingungen für einen Deadlock.** (4 Punkte)

| Bedingung | Erklärung |
|-----------|-----------|
| 1. | |
| 2. | |
| 3. | |
| 4. | |

b) **Nennen Sie zwei Strategien zur Deadlock-Behandlung und beschreiben Sie diese kurz.** (4 Punkte)

| Strategie | Beschreibung |
|-----------|--------------|
| 1. | |
| 2. | |

---

### Aufgabe 6.4: Semaphore (6 Punkte) ⭐⭐⭐

a) **Erklären Sie die Operationen P (wait) und V (signal) bei Semaphoren.** (3 Punkte)

| Operation | Semantik |
|-----------|----------|
| P(S) | |
| V(S) | |

b) **Was ist der Unterschied zwischen einem Mutex und einem Semaphor?** (3 Punkte)

| Eigenschaft | Mutex | Semaphor |
|-------------|-------|----------|
| Wertebereich | | |
| Ownership | | |
| Typischer Einsatz | | |

---

## Teil 7: Speicherverwaltung (20 Punkte)

### Aufgabe 7.1: Virtueller Speicher (6 Punkte) ⭐⭐

a) **Was ist virtueller Speicher und welches Problem löst er?** (3 Punkte)

_Dein Antwort:_

<br><br><br>

b) **Was ist ein Page Fault und was passiert dabei?** (3 Punkte)

_Dein Antwort:_

<br><br><br>

---

### Aufgabe 7.2: Paging (8 Punkte) ⭐⭐

a) **Erklären Sie die Begriffe Page und Frame im Kontext von Paging.** (2 Punkte)

| Begriff | Beschreibung |
|---------|--------------|
| Page | |
| Frame | |

b) **Welche Informationen enthält ein Page-Table-Eintrag? Nennen Sie mindestens vier.** (4 Punkte)

| Information | Bedeutung |
|-------------|-----------|
| 1. | |
| 2. | |
| 3. | |
| 4. | |

c) **Was ist der TLB (Translation Lookaside Buffer) und wozu dient er?** (2 Punkte)

_Dein Antwort:_

<br><br><br>

---

### Aufgabe 7.3: Page-Ersetzung (6 Punkte) ⭐⭐⭐

a) **Nennen Sie drei Page-Ersetzungsalgorithmen und beschreiben Sie diese kurz.** (6 Punkte)

| Algorithmus | Beschreibung | Vor-/Nachteil |
|-------------|--------------|---------------|
| 1. | | |
| 2. | | |
| 3. | | |

---

## Selbsteinschätzung

Nach Bearbeitung der Aufgaben:

| Thema | Sicher | Unsicher | Muss wiederholen |
|-------|:------:|:--------:|:----------------:|
| Definition/Aufgaben BS | ☐ | ☐ | ☐ |
| Kerneltypen | ☐ | ☐ | ☐ |
| Systemaufrufe | ☐ | ☐ | ☐ |
| Prozesse | ☐ | ☐ | ☐ |
| Scheduling | ☐ | ☐ | ☐ |
| Threads | ☐ | ☐ | ☐ |
| Kritische Abschnitte | ☐ | ☐ | ☐ |
| Race Conditions | ☐ | ☐ | ☐ |
| Deadlocks | ☐ | ☐ | ☐ |
| Semaphore/Mutex | ☐ | ☐ | ☐ |
| Virtueller Speicher | ☐ | ☐ | ☐ |
| Paging | ☐ | ☐ | ☐ |

---

## Quellen

### Grundlagen
- [[02-Definition|Definition eines Betriebssystems]]
- [[03-Aufgaben|Aufgaben eines Betriebssystems]]

### Architektur
- [[01-Kerneltypen|Kerneltypen]]
- [[03-Systemaufrufe|Systemaufrufe]]

### Prozesse & Threads
- [[01-Prozessmodell|Prozessmodell]]
- [[02-Scheduling|Scheduling]]
- [[03-Threads|Threads]]

### Synchronisation
- [[02-Kritische-Abschnitte|Kritische Abschnitte]]
- [[03-Race-Conditions|Race Conditions]]
- [[04-Deadlocks|Deadlocks]]
- [[05-Synchronisationsmechanismen|Synchronisationsmechanismen]]

### Speicherverwaltung
- [[02-Virtueller-Speicher|Virtueller Speicher]]
- [[03-Paging|Paging]]
