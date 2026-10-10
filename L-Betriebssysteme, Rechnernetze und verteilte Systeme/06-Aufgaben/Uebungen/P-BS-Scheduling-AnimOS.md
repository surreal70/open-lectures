---
author: Andreas Hümmer
title: 'Praxisübung: CPU-Scheduling mit AnimOS'
tags:
  - uebung
  - praxis
  - bs
  - scheduling
  - animeos
  - fcfs
  - round-robin
  - sjf
  - srtf
  - hrrn
bereich: BS
created: '2026-10-09'
modified: '2026-10-09'
---

# Praxisübung: CPU-Scheduling mit AnimOS

**Bereich:** BS – Prozesse und Scheduling
**Voraussetzungen:** [[02-Scheduling|Scheduling-Grundlagen]], Webbrowser

---

> [!info] **Lernziele**
> Nach dieser Übung solltest du:
> - Den AnimOS-Simulator bedienen können
> - FCFS, Round Robin, SJF, SRTF und HRRN praktisch anwenden können
> - Scheduling-Metriken (Wartezeit, Turnaround, Antwortzeit) berechnen und interpretieren
> - Die Auswirkungen verschiedener Strategien auf unterschiedliche Workloads verstehen
> - Eine geeignete Strategie für Echtzeit-Anforderungen auswählen können

---

## Einführung

**AnimOS** ist ein interaktiver CPU-Scheduling-Simulator, entwickelt von Gregor Kotainy und Prof. Dr.-Ing. Olaf Spinczyk an der TU Dortmund. Er ermöglicht die praktische Demonstration und den Vergleich verschiedener Scheduling-Algorithmen.

> [!tip] **Simulator-Link**
> **[AnimOS – CPU Scheduling Simulator](https://ess.cs.tu-dortmund.de/Software/AnimOS/CPU-Scheduling/)**

---

## Teil 1: Grundlagen und Einrichtung

### Aufgabe 1.1: AnimOS kennenlernen

Öffne den AnimOS-Simulator und mache dich mit der Oberfläche vertraut.

**Zu identifizierende Elemente:**
- [ ] **Operate-Tab**: Prozessdefinition und Simulation
- [ ] **Prozess-Tabelle**: Eingabe von Arrival Time, CPU Burst, I/O Burst, Priority
- [ ] **Strategie-Dropdown**: Auswahl des Scheduling-Algorithmus
- [ ] **Gantt-Chart**: Visualisierung der Ausführungsreihenfolge
- [ ] **Statistiken**: Wartezeit, Turnaround-Zeit, Antwortzeit

### Aufgabe 1.2: Basis-Workload einrichten

Richte den folgenden **Standard-Workload** ein, der für alle Experimente verwendet wird:

| Prozess | Arrival Time | CPU Burst | I/O Burst | Priority |
|---------|-------------:|----------:|----------:|---------:|
| P1 | 0 | 8 | 0 | 1 |
| P2 | 1 | 4 | 0 | 1 |
| P3 | 2 | 2 | 0 | 1 |
| P4 | 3 | 1 | 0 | 1 |

> [!note] **Parameter-Erklärung**
> - **Arrival Time**: Wann der Prozess bereit zur Ausführung wird
> - **CPU Burst**: Benötigte CPU-Zeit in Simulationsticks
> - **I/O Burst**: Zeit für I/O-Operationen (hier 0, da wir reines CPU-Scheduling betrachten)
> - **Priority**: Scheduling-Priorität (für prioritätsbasierte Algorithmen)

> [!warning] **AnimOS-Hinweis**
> Falls AnimOS variable Burst-Bereiche erwartet, verwende die Notation mit gleichem Minimum und Maximum (z.B. `8-8` für einen Burst von 8).

---

## Teil 2: First Come First Served – FCFS

### Aufgabe 2.1: FCFS-Simulation

**Konfiguration:**
- Strategie: **First Come First Served (FCFS)**
- Zeitquantum: nicht anwendbar

Führe die Simulation durch und dokumentiere:

**Erwartete Ausführungsreihenfolge:**
```
P1 → P2 → P3 → P4
```

**Erwartetes Gantt-Chart:**
```
Zeit:  0        8    12  14 15
       |--------|----|----|--|
       |   P1   | P2 | P3 |P4|
```

**Ergebnistabelle:**

| Prozess | Start | Ende | Wartezeit | Turnaround |
|---------|------:|-----:|----------:|-----------:|
| P1 | 0 | 8 | ? | ? |
| P2 | 8 | 12 | ? | ? |
| P3 | 12 | 14 | ? | ? |
| P4 | 14 | 15 | ? | ? |

**Durchschnittliche Wartezeit:** _____ Ticks

### Aufgabe 2.2: Convoy-Effekt

Der **Convoy-Effekt** tritt auf, wenn ein langer Prozess kürzere Prozesse blockiert.

**Experiment:** Ändere P1's CPU Burst von 8 auf **20** und beobachte:

1. Wie ändern sich die Wartezeiten der anderen Prozesse?
2. Um wie viel steigt die durchschnittliche Wartezeit?
3. Warum ist FCFS für interaktive Systeme ungeeignet?

---

## Teil 3: Round Robin – RR

### Aufgabe 3.1: Round Robin mit Quantum 2

**Konfiguration:**
- Strategie: **Round Robin**
- Zeitquantum: **2**

**Erwartete Ausführungsreihenfolge:**
```
P1 → P2 → P3 → P1 → P4 → P2 → P1
```

**Erwartetes Gantt-Chart:**
```
Zeit:  0   2   4   6   8  9  11      15
       |---|---|---|---|--|---|-------|
       |P1 |P2 |P3 |P1 |P4|P2 |  P1   |
```

Dokumentiere die Ergebnisse:

| Prozess | Erster Start | Ende | Wartezeit | Turnaround |
|---------|-------------:|-----:|----------:|-----------:|
| P1 | 0 | ? | ? | ? |
| P2 | 2 | ? | ? | ? |
| P3 | 4 | ? | ? | ? |
| P4 | 8 | ? | ? | ? |

### Aufgabe 3.2: Quantum-Vergleich

Führe die Simulation mit verschiedenen Quantum-Werten durch und vergleiche:

| Quantum | Avg. Wartezeit | Avg. Turnaround | Kontextwechsel | Beobachtung |
|--------:|---------------:|----------------:|---------------:|-------------|
| 1 | | | | |
| 2 | | | | |
| 4 | | | | |
| 10 | | | | |

**Fragen:**
1. Was passiert bei sehr kleinem Quantum (q=1)?
2. Was passiert bei sehr großem Quantum (q=10)?
3. Welches Quantum bietet die beste Balance?

---

## Teil 4: Shortest Job First – SJF

### Aufgabe 4.1: SJF-Simulation

**Konfiguration:**
- Strategie: **Shortest Job First (SJF)** – non-preemptive
- Zeitquantum: nicht anwendbar

**Erwartete Ausführungsreihenfolge (nach Burst sortiert):**
```
P1 → P4 → P3 → P2
```

> [!note] **Warum P1 zuerst?**
> Zum Zeitpunkt 0 ist nur P1 verfügbar. Erst nach dessen Beendigung (t=8) wird nach dem kürzesten Job unter den wartenden Prozessen (P2, P3, P4) gewählt.

**Ergebnistabelle:**

| Prozess | Start | Ende | Wartezeit | Turnaround |
|---------|------:|-----:|----------:|-----------:|
| P1 | 0 | 8 | ? | ? |
| P4 | 8 | 9 | ? | ? |
| P3 | 9 | 11 | ? | ? |
| P2 | 11 | 15 | ? | ? |

### Aufgabe 4.2: Starvation-Experiment

**Experiment:** Setze alle Arrival Times auf **0** und vergleiche SJF mit FCFS.

| Strategie | Avg. Wartezeit | Ausführungsreihenfolge |
|-----------|---------------:|------------------------|
| FCFS | | |
| SJF | | |

**Fragen:**
1. Welche Strategie hat die niedrigere durchschnittliche Wartezeit?
2. Warum kann SJF zu Starvation führen?
3. Wie könnte man Starvation bei SJF verhindern?

---

## Teil 5: Shortest Remaining Time First – SRTF

### Aufgabe 5.1: SRTF-Simulation

**Konfiguration:**
- Strategie: **Shortest Remaining Time First (SRTF)** – preemptive

> [!warning] **AnimOS-Hinweis**
> Falls SRTF nicht als vordefinierte Strategie verfügbar ist, muss sie über den Custom-Scheduler-Editor implementiert werden.

**Erwartete Ausführung:**

| Zeit | Ereignis |
|-----:|----------|
| 0 | P1 startet (Burst=8) |
| 1 | P2 kommt an (Burst=4) → verdrängt P1 (4 < 7 verbleibend) |
| 2 | P3 kommt an (Burst=2) → verdrängt P2 (2 < 3 verbleibend) |
| 3 | P4 kommt an (Burst=1) → P3 hat auch 1 verbleibend, Tie: P3 läuft weiter |
| 4 | P3 fertig → P4 läuft |
| 5 | P4 fertig → P2 läuft (3 verbleibend) |
| 8 | P2 fertig → P1 läuft (7 verbleibend) |
| 15 | P1 fertig |

**Erwartete Ergebnisse:**

| Prozess | Erster Start | Ende | Wartezeit | Turnaround |
|---------|-------------:|-----:|----------:|-----------:|
| P1 | 0 | 15 | 7 | 15 |
| P2 | 1 | 8 | 3 | 7 |
| P3 | 2 | 4 | 0 | 2 |
| P4 | 4 | 5 | 1 | 2 |

**Durchschnittliche Wartezeit:** 2.75 Ticks

### Aufgabe 5.2: Preemption-Experiment

**Experiment:** Füge einen weiteren kurzen Prozess hinzu:

| Prozess | Arrival Time | CPU Burst |
|---------|-------------:|----------:|
| P5 | 6 | 1 |

**Fragen:**
1. Wird P1 erneut unterbrochen?
2. Wie ändert sich die Fertigstellungszeit von P1?
3. Welches Risiko besteht für lange Prozesse bei SRTF?

---

## Teil 6: Highest Response Ratio Next – HRRN

### Aufgabe 6.1: HRRN-Berechnung

**Response Ratio Formel:**
$$R = \frac{W + S}{S} = 1 + \frac{W}{S}$$

Wobei: W = Wartezeit, S = Service Time (CPU Burst)

**Berechnung zum Zeitpunkt t=8** (nach P1's Beendigung):

| Prozess | Wartezeit (W) | CPU Burst (S) | Response Ratio (R) |
|---------|---------------:|---------------:|-------------------:|
| P2 | 7 | 4 | ? |
| P3 | 6 | 2 | ? |
| P4 | 5 | 1 | ? |

Welcher Prozess wird als nächstes ausgewählt? _____

### Aufgabe 6.2: HRRN vs. SJF Vergleich

Verwende diesen alternativen Workload:

| Prozess | Arrival | CPU Burst |
|---------|--------:|----------:|
| P1 | 0 | 6 |
| P2 | 1 | 8 |
| P3 | 5 | 2 |

**Berechnung zum Zeitpunkt t=6:**

- P2: R = (5 + 8) / 8 = ___
- P3: R = (1 + 2) / 2 = ___

**Frage:** Warum wählt HRRN hier P2 obwohl P3 kürzer ist?

---

## Teil 7: Strategie-Vergleich und Echtzeit-Eignung

### Aufgabe 7.1: Gesamtvergleich

Trage die Ergebnisse aller Strategien für den Standard-Workload zusammen:

| Algorithmus | Preemptive | Avg. Wartezeit | Avg. Turnaround | Starvation-Risiko |
|-------------|:----------:|---------------:|----------------:|:-----------------:|
| FCFS | Nein | | | Nein |
| RR (q=2) | Ja | | | Nein |
| SJF | Nein | | | Ja |
| SRTF | Ja | | | Ja |
| HRRN | Nein | | | Gering |

### Aufgabe 7.2: Echtzeit-Scheduling

**Szenario:** Du entwirfst das Scheduling für ein **Echtzeit-System** mit folgenden Anforderungen:

| Prozess | Typ | Deadline | CPU Burst |
|---------|-----|----------:|----------:|
| Sensor-Polling | Periodisch | 10ms | 2ms |
| Alarm-Handler | Aperiodisch | 5ms | 1ms |
| Datenlogging | Hintergrund | - | 8ms |
| Display-Update | Periodisch | 50ms | 3ms |

**Fragen:**

1. **Welche Strategie ist für Echtzeit ungeeignet und warum?**
   
   _Hinweis: Betrachte Vorhersagbarkeit und garantierte Antwortzeiten._

2. **Welche Strategie würdest du für harte Echtzeit empfehlen?**
   
   _Hinweis: Harte Echtzeit erfordert garantierte Deadline-Einhaltung._

3. **Entwirf eine passende Scheduling-Konfiguration:**

| Queue | Prozesse | Algorithmus | Quantum |
|-------|----------|-------------|--------:|
| High | | | |
| Medium | | | |
| Low | | | |

4. **Bonus:** Recherchiere **Rate Monotonic Scheduling (RMS)** und erkläre, warum es für periodische Echtzeit-Tasks geeignet ist.

---

## Zusammenfassung und Reflexion

### Ergebnisübersicht

Vervollständige die Vergleichstabelle mit deinen Messwerten:

| Kriterium | FCFS | RR | SJF | SRTF | HRRN |
|-----------|:----:|:--:|:---:|:----:|:----:|
| Niedrigste Wartezeit | | | | ★ | |
| Beste Antwortzeit | | | | | |
| Fairness | | ★ | | | |
| Einfachheit | ★ | | | | |
| Echtzeit-Eignung | | | | | |

### Reflexionsfragen

1. Warum gibt es keinen "besten" Scheduling-Algorithmus für alle Situationen?

2. Welche Trade-offs bestehen zwischen Fairness und Effizienz?

3. Wie beeinflusst der Overhead durch Kontextwechsel die Wahl des Quantum bei Round Robin?

---

## Quellen und weiterführende Ressourcen

- [[02-Scheduling|Scheduling-Grundlagen]]
- [[01-Prozessmodell|Prozessmodell]]
- [AnimOS Dokumentation (TU Dortmund)](https://ess.cs.tu-dortmund.de/Software/AnimOS/CPU-Scheduling/)
- [OSTEP – Scheduling Kapitel](https://pages.cs.wisc.edu/~remzi/OSTEP/)

> [!tip] **Weiterführende Experimente**
> - Experimentiere mit I/O-Bursts und beobachte die Auswirkungen
> - Implementiere einen eigenen Scheduler mit dem Custom-Editor
> - Vergleiche mit realen Scheduling-Daten aus `htop` oder dem Windows Task Manager
