---
author: Andreas Hümmer
title: 'Lösung: CPU-Scheduling mit AnimOS'
tags:
  - uebung
  - loesung
  - praxis
  - bs
  - scheduling
bereich: BS
created: '2026-10-09'
modified: '2026-10-09'
---

# Lösung: CPU-Scheduling mit AnimOS

**Zugehörige Übung:** [[P-BS-Scheduling-AnimOS]]

---

## Teil 1: Grundlagen und Einrichtung

### Aufgabe 1.1: AnimOS kennenlernen

Die Studierenden sollten folgende Elemente identifiziert haben:

- [x] **Operate-Tab**: Hauptbereich für Prozessdefinition und Simulationssteuerung
- [x] **Prozess-Tabelle**: Tabellarische Eingabe mit Spalten für Arrival Time, CPU Burst, I/O Burst, Priority
- [x] **Strategie-Dropdown**: Auswahl zwischen FCFS, Round Robin, SJF, etc.
- [x] **Gantt-Chart**: Horizontale Balkenvisualisierung der Prozessausführung
- [x] **Statistiken**: Anzeige von Waiting Time, Turnaround Time, Response Time, CPU Utilization

### Aufgabe 1.2: Basis-Workload einrichten

Der Standard-Workload wurde korrekt eingerichtet:

| Prozess | Arrival Time | CPU Burst | I/O Burst | Priority |
|---------|-------------:|----------:|----------:|---------:|
| P1 | 0 | 8 | 0 | 1 |
| P2 | 1 | 4 | 0 | 1 |
| P3 | 2 | 2 | 0 | 1 |
| P4 | 3 | 1 | 0 | 1 |

---

## Teil 2: First Come First Served – FCFS

### Aufgabe 2.1: FCFS-Simulation

**Ausführungsreihenfolge:** P1 → P2 → P3 → P4

**Gantt-Chart:**
```
Zeit:  0        8    12  14 15
       |--------|----|----|--|
       |   P1   | P2 | P3 |P4|
```

**Ergebnistabelle:**

| Prozess | Arrival | Start | Ende | Wartezeit | Turnaround |
|---------|--------:|------:|-----:|----------:|-----------:|
| P1 | 0 | 0 | 8 | 0 | 8 |
| P2 | 1 | 8 | 12 | 7 | 11 |
| P3 | 2 | 12 | 14 | 10 | 12 |
| P4 | 3 | 14 | 15 | 11 | 12 |

**Berechnungen:**
- Wartezeit P1 = Start - Arrival = 0 - 0 = **0**
- Wartezeit P2 = 8 - 1 = **7**
- Wartezeit P3 = 12 - 2 = **10**
- Wartezeit P4 = 14 - 3 = **11**

**Durchschnittliche Wartezeit:** (0 + 7 + 10 + 11) / 4 = **7.00 Ticks**

**Durchschnittliche Turnaround-Zeit:** (8 + 11 + 12 + 12) / 4 = **10.75 Ticks**

### Aufgabe 2.2: Convoy-Effekt

**Mit P1 CPU Burst = 20:**

| Prozess | Start | Ende | Wartezeit | Turnaround |
|---------|------:|-----:|----------:|-----------:|
| P1 | 0 | 20 | 0 | 20 |
| P2 | 20 | 24 | 19 | 23 |
| P3 | 24 | 26 | 22 | 24 |
| P4 | 26 | 27 | 23 | 24 |

**Neue durchschnittliche Wartezeit:** (0 + 19 + 22 + 23) / 4 = **16.00 Ticks**

**Antworten:**
1. Die Wartezeiten steigen erheblich: P2 von 7 auf 19, P3 von 10 auf 22, P4 von 11 auf 23
2. Die durchschnittliche Wartezeit steigt von 7.00 auf 16.00 Ticks (+128%)
3. FCFS ist für interaktive Systeme ungeeignet, weil:
   - Lange Prozesse blockieren alle nachfolgenden Prozesse
   - Keine Garantie für kurze Antwortzeiten
   - Interaktive Prozesse (z.B. Tastatureingaben) müssten auf CPU-intensive Hintergrundprozesse warten

---

## Teil 3: Round Robin – RR

### Aufgabe 3.1: Round Robin mit Quantum 2

**Ausführungsreihenfolge:** P1 → P2 → P3 → P1 → P4 → P2 → P1 → P1 → P1

**Gantt-Chart:**
```
Zeit:  0   2   4   6   8  9  11  13  15
       |---|---|---|---|--|---|---|---|
       |P1 |P2 |P3 |P1 |P4|P2 |P1 |P1 |
```

**Detaillierter Ablauf:**
- t=0-2: P1 läuft (verbleibend: 6)
- t=2-4: P2 läuft (verbleibend: 2)
- t=4-6: P3 läuft (verbleibend: 0) ✓ fertig
- t=6-8: P1 läuft (verbleibend: 4)
- t=8-9: P4 läuft (verbleibend: 0) ✓ fertig (nur 1 Tick benötigt)
- t=9-11: P2 läuft (verbleibend: 0) ✓ fertig
- t=11-13: P1 läuft (verbleibend: 2)
- t=13-15: P1 läuft (verbleibend: 0) ✓ fertig

**Ergebnistabelle:**

| Prozess | Arrival | Erster Start | Ende | Wartezeit | Turnaround |
|---------|--------:|-------------:|-----:|----------:|-----------:|
| P1 | 0 | 0 | 15 | 7 | 15 |
| P2 | 1 | 2 | 11 | 6 | 10 |
| P3 | 2 | 4 | 6 | 2 | 4 |
| P4 | 3 | 8 | 9 | 5 | 6 |

**Durchschnittliche Wartezeit:** (7 + 6 + 2 + 5) / 4 = **5.00 Ticks**

### Aufgabe 3.2: Quantum-Vergleich

| Quantum | Avg. Wartezeit | Avg. Turnaround | Kontextwechsel | Beobachtung |
|--------:|---------------:|----------------:|---------------:|-------------|
| 1 | ~4.5 | ~8.25 | ~14 | Sehr häufige Wechsel, hoher Overhead |
| 2 | 5.00 | 8.75 | 7 | Gute Balance |
| 4 | 5.75 | 9.50 | 4 | Weniger Wechsel |
| 10 | 7.00 | 10.75 | 3 | Fast wie FCFS |

**Antworten:**
1. **Quantum = 1:** Sehr häufige Kontextwechsel, jeder Prozess bekommt nur 1 Tick. Der Overhead für Kontextwechsel überwiegt den Vorteil der Fairness. In der Praxis würde die effektive CPU-Auslastung sinken.

2. **Quantum = 10:** Da alle Prozesse außer P1 Burst-Zeiten < 10 haben, laufen sie ohne Unterbrechung durch. P1 wird nach 8 Ticks unterbrochen, aber die kurzen Prozesse (P2, P3, P4) mussten lange warten. Das Verhalten nähert sich FCFS an.

3. **Beste Balance:** Quantum = 2-4 bietet einen guten Kompromiss zwischen Fairness (kurze Prozesse werden nicht blockiert) und Overhead (nicht zu viele Kontextwechsel). Die typische Faustregel: Quantum sollte länger sein als 80% aller CPU-Bursts, aber kurz genug für akzeptable Antwortzeiten.

---

## Teil 4: Shortest Job First – SJF

### Aufgabe 4.1: SJF-Simulation

**Ausführungsreihenfolge:** P1 → P4 → P3 → P2

**Erklärung:**
- t=0: Nur P1 verfügbar → P1 startet
- t=8: P1 fertig, P2/P3/P4 warten. Burst-Zeiten: P4(1) < P3(2) < P2(4)
- P4 wird gewählt (kürzester Burst)

**Gantt-Chart:**
```
Zeit:  0        8  9   11      15
       |--------|--|----|-------|
       |   P1   |P4| P3 |  P2   |
```

**Ergebnistabelle:**

| Prozess | Arrival | Start | Ende | Wartezeit | Turnaround |
|---------|--------:|------:|-----:|----------:|-----------:|
| P1 | 0 | 0 | 8 | 0 | 8 |
| P4 | 3 | 8 | 9 | 5 | 6 |
| P3 | 2 | 9 | 11 | 7 | 9 |
| P2 | 1 | 11 | 15 | 10 | 14 |

**Durchschnittliche Wartezeit:** (0 + 5 + 7 + 10) / 4 = **5.50 Ticks**

### Aufgabe 4.2: Starvation-Experiment

**Alle Arrival Times = 0:**

| Strategie | Reihenfolge | Avg. Wartezeit |
|-----------|-------------|---------------:|
| FCFS | P1 → P2 → P3 → P4 | (0+8+12+14)/4 = **8.50** |
| SJF | P4 → P3 → P2 → P1 | (0+1+3+7)/4 = **2.75** |

**SJF-Details bei Arrival = 0:**
```
Zeit:  0  1   3       7              15
       |--|---|-------|--------------|
       |P4|P3 |  P2   |      P1      |
```

| Prozess | Start | Ende | Wartezeit |
|---------|------:|-----:|----------:|
| P4 | 0 | 1 | 0 |
| P3 | 1 | 3 | 1 |
| P2 | 3 | 7 | 3 |
| P1 | 7 | 15 | 7 |

**Antworten:**
1. **SJF** hat die niedrigere durchschnittliche Wartezeit (2.75 vs. 8.50). SJF ist mathematisch beweisbar optimal für die minimale durchschnittliche Wartezeit.

2. **Starvation bei SJF:** Wenn ständig neue kurze Prozesse ankommen, werden lange Prozesse immer wieder nach hinten geschoben. Ein Prozess mit Burst=100 könnte theoretisch unendlich warten, wenn alle 5 Ticks ein Prozess mit Burst=4 ankommt.

3. **Starvation verhindern:**
   - **Aging:** Die Priorität eines Prozesses erhöht sich mit seiner Wartezeit (→ HRRN)
   - **Maximale Wartezeit:** Nach einer bestimmten Wartezeit wird der Prozess bevorzugt
   - **Kombinierter Ansatz:** MLFQ mit Priority Boost

---

## Teil 5: Shortest Remaining Time First – SRTF

### Aufgabe 5.1: SRTF-Simulation

**Detaillierter Ablauf:**

| Zeit | Ereignis | Laufender Prozess | Ready Queue (remaining) |
|-----:|----------|-------------------|-------------------------|
| 0 | P1 startet | P1 (8) | - |
| 1 | P2 kommt an, 4 < 7 → Preemption | P2 (4) | P1 (7) |
| 2 | P3 kommt an, 2 < 3 → Preemption | P3 (2) | P1 (7), P2 (3) |
| 3 | P4 kommt an, 1 = 1 → kein Wechsel | P3 (1) | P1 (7), P2 (3), P4 (1) |
| 4 | P3 fertig | P4 (1) | P1 (7), P2 (3) |
| 5 | P4 fertig | P2 (3) | P1 (7) |
| 8 | P2 fertig | P1 (7) | - |
| 15 | P1 fertig | - | - |

**Gantt-Chart:**
```
Zeit:  0  1  2    4  5     8        15
       |--|--|----|--|-----|---------|
       |P1|P2| P3 |P4| P2  |   P1    |
```

**Ergebnistabelle:**

| Prozess | Arrival | Erster Start | Ende | Wartezeit | Turnaround |
|---------|--------:|-------------:|-----:|----------:|-----------:|
| P1 | 0 | 0 | 15 | 7 | 15 |
| P2 | 1 | 1 | 8 | 3 | 7 |
| P3 | 2 | 2 | 4 | 0 | 2 |
| P4 | 3 | 4 | 5 | 1 | 2 |

**Durchschnittliche Wartezeit:** (7 + 3 + 0 + 1) / 4 = **2.75 Ticks**

> [!note] **Berechnung Wartezeit bei Preemption**
> Wartezeit = Turnaround - Burst
> - P1: 15 - 8 = 7
> - P2: 7 - 4 = 3
> - P3: 2 - 2 = 0
> - P4: 2 - 1 = 1

### Aufgabe 5.2: Preemption-Experiment

**Mit zusätzlichem P5 (Arrival=6, Burst=1):**

| Zeit | Ereignis |
|-----:|----------|
| 5 | P4 fertig, P2 läuft (remaining=3) |
| 6 | P5 kommt an, 1 < 2 → Preemption |
| 7 | P5 fertig, P2 läuft (remaining=2) |
| 9 | P2 fertig, P1 läuft (remaining=7) |
| 16 | P1 fertig |

**Antworten:**
1. **Ja**, P1 wird indirekt betroffen, obwohl P5 P2 verdrängt (nicht P1 direkt). P1's Wartezeit erhöht sich.

2. **P1's Fertigstellungszeit:** steigt von 15 auf **16** Ticks (+1)

3. **Risiko für lange Prozesse:** 
   - **Starvation:** Lange Prozesse können theoretisch unendlich warten
   - **Unvorhersehbare Laufzeit:** Die tatsächliche Fertigstellungszeit hängt von allen zukünftigen Ankünften ab
   - **Hoher Overhead:** Viele Kontextwechsel bei häufigen kurzen Ankünften

---

## Teil 6: Highest Response Ratio Next – HRRN

### Aufgabe 6.1: HRRN-Berechnung

**Zum Zeitpunkt t=8 (nach P1's Beendigung):**

| Prozess | Arrival | Wartezeit (W) | CPU Burst (S) | R = (W+S)/S |
|---------|--------:|--------------:|--------------:|------------:|
| P2 | 1 | 8-1 = 7 | 4 | (7+4)/4 = **2.75** |
| P3 | 2 | 8-2 = 6 | 2 | (6+2)/2 = **4.00** |
| P4 | 3 | 8-3 = 5 | 1 | (5+1)/1 = **6.00** |

**Ausgewählt:** P4 (höchstes Response Ratio = 6.00)

**Zum Zeitpunkt t=9:**

| Prozess | Wartezeit (W) | CPU Burst (S) | R = (W+S)/S |
|---------|---------------:|---------------:|------------:|
| P2 | 9-1 = 8 | 4 | (8+4)/4 = **3.00** |
| P3 | 9-2 = 7 | 2 | (7+2)/2 = **4.50** |

**Ausgewählt:** P3 (höchstes Response Ratio = 4.50)

**Reihenfolge:** P1 → P4 → P3 → P2 (identisch zu SJF für diesen Workload)

### Aufgabe 6.2: HRRN vs. SJF Vergleich

**Workload:**

| Prozess | Arrival | CPU Burst |
|---------|--------:|----------:|
| P1 | 0 | 6 |
| P2 | 1 | 8 |
| P3 | 5 | 2 |

**Zum Zeitpunkt t=6:**

| Prozess | Wartezeit | Burst | Response Ratio |
|---------|----------:|------:|---------------:|
| P2 | 5 | 8 | (5+8)/8 = **1.625** |
| P3 | 1 | 2 | (1+2)/2 = **1.50** |

**HRRN wählt P2** (1.625 > 1.50), obwohl P3 kürzer ist.

**SJF würde P3 wählen** (2 < 8).

**Warum?** HRRN berücksichtigt die **Wartezeit** als Fairness-Faktor. P2 wartet bereits seit 5 Ticks, P3 erst seit 1 Tick. Das "Aging" durch die lange Wartezeit erhöht P2's Priorität ausreichend, um den kürzeren Burst von P3 zu übertreffen.

**Fazit:** HRRN reduziert Starvation, indem lange wartende Prozesse bevorzugt werden – auch wenn sie längere Burst-Zeiten haben.

---

## Teil 7: Strategie-Vergleich und Echtzeit-Eignung

### Aufgabe 7.1: Gesamtvergleich

| Algorithmus | Preemptive | Avg. Wartezeit | Avg. Turnaround | Starvation-Risiko |
|-------------|:----------:|---------------:|----------------:|:-----------------:|
| FCFS | Nein | 7.00 | 10.75 | Nein |
| RR (q=2) | Ja | 5.00 | 8.75 | Nein |
| SJF | Nein | 5.50 | 9.25 | Ja |
| SRTF | Ja | **2.75** | **6.50** | Ja |
| HRRN | Nein | 5.50 | 9.25 | Gering |

### Aufgabe 7.2: Echtzeit-Scheduling

**Szenario-Wiederholung:**

| Prozess | Typ | Deadline | CPU Burst |
|---------|-----|----------:|----------:|
| Sensor-Polling | Periodisch | 10ms | 2ms |
| Alarm-Handler | Aperiodisch | 5ms | 1ms |
| Datenlogging | Hintergrund | - | 8ms |
| Display-Update | Periodisch | 50ms | 3ms |

**Antworten:**

1. **Ungeeignete Strategien für Echtzeit:**
   - **FCFS:** Keine Garantie für Antwortzeiten. Ein langer Prozess (Datenlogging) könnte den Alarm-Handler blockieren und die 5ms-Deadline verletzen.
   - **Round Robin (ohne Prioritäten):** Alle Prozesse werden gleich behandelt. Der kritische Alarm-Handler muss auf seine Zeitscheibe warten.
   - **SJF/SRTF ohne Prioritäten:** Burst-Zeit ist nicht das richtige Kriterium für Echtzeit – Deadlines sind entscheidend.

2. **Empfohlene Strategie für harte Echtzeit:**
   - **Prioritätsbasiertes Preemptive Scheduling** mit statischen Prioritäten nach Deadline
   - **Rate Monotonic Scheduling (RMS)** für periodische Tasks
   - **Earliest Deadline First (EDF)** für dynamische Deadlines
   
   Alle kritischen Prozesse müssen höhere Priorität als Hintergrundprozesse haben.

3. **Passende Scheduling-Konfiguration:**

| Queue | Prozesse | Algorithmus | Quantum |
|-------|----------|-------------|--------:|
| High (Kritisch) | Alarm-Handler | Preemptive Priority | - |
| Medium (Periodisch) | Sensor-Polling, Display-Update | RMS / RR | 5ms |
| Low (Hintergrund) | Datenlogging | FCFS | - |

4. **Rate Monotonic Scheduling (RMS):**
   
   RMS ist optimal für periodische Tasks mit festen Perioden:
   - **Regel:** Je kürzer die Periode, desto höher die Priorität
   - **Mathematisch beweisbar optimal** für unabhängige, periodische Tasks
   - **Schedulability-Test:** Σ(Ci/Ti) ≤ n(2^(1/n) - 1)
   
   Für unser Beispiel:
   - Sensor-Polling: Periode ~10ms → höchste Priorität
   - Display-Update: Periode ~50ms → niedrigere Priorität
   
   RMS garantiert, dass alle Deadlines eingehalten werden, solange die CPU-Auslastung unter dem Grenzwert bleibt.

---

## Zusammenfassung: Ergebnisübersicht

| Kriterium | FCFS | RR | SJF | SRTF | HRRN |
|-----------|:----:|:--:|:---:|:----:|:----:|
| Niedrigste Wartezeit | | | | ★ | |
| Beste Antwortzeit | | ★ | | ★ | |
| Fairness | | ★ | | | ★ |
| Einfachheit | ★ | | | | |
| Echtzeit-Eignung | | | | | |
| Kein Starvation | ★ | ★ | | | (★) |

**Legende:**
- ★ = Algorithmus ist gut in dieser Kategorie
- (★) = Bedingt gut (HRRN reduziert, aber eliminiert Starvation nicht vollständig)

---

## Reflexionsfragen – Musterlösungen

1. **Warum gibt es keinen "besten" Scheduling-Algorithmus für alle Situationen?**
   
   Verschiedene Systeme haben unterschiedliche Anforderungen:
   - **Desktop:** Schnelle Antwortzeiten für Benutzerinteraktion
   - **Server:** Hoher Durchsatz und Fairness
   - **Echtzeit:** Garantierte Deadline-Einhaltung
   - **Batch:** Maximale CPU-Auslastung
   
   Ein Algorithmus kann nicht alle Ziele gleichzeitig optimieren. Es gibt inhärente Trade-offs.

2. **Welche Trade-offs bestehen zwischen Fairness und Effizienz?**
   
   - **Round Robin:** Fair (alle bekommen gleich viel), aber nicht effizient (viele Kontextwechsel)
   - **SJF/SRTF:** Effizient (minimale Wartezeit), aber unfair (lange Prozesse verhungern)
   - **MLFQ:** Versucht Balance durch dynamische Anpassung

3. **Wie beeinflusst der Overhead durch Kontextwechsel die Wahl des Quantum bei Round Robin?**
   
   - Ein Kontextwechsel kostet typisch 1-10 µs
   - Bei Quantum = 1ms und Overhead = 10µs: 1% Overhead
   - Bei Quantum = 10µs und Overhead = 10µs: 50% Overhead!
   
   **Faustregel:** Quantum sollte mindestens 10-100x größer sein als der Kontextwechsel-Overhead, aber klein genug für akzeptable Antwortzeiten (typisch 10-100ms).
