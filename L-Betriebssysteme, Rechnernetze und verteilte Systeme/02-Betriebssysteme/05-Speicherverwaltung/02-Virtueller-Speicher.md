---
author: Andreas Hümmer
title: Virtueller Speicher
tags:
  - content
  - bs
  - speicher
  - virtual-memory
  - swapping
  - demand-paging
created: '2026-10-07'
modified: '2026-10-09'
bereich: BS
---

# Virtueller Speicher

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das Konzept des virtuellen Speichers verstehen
> - Swapping und Demand Paging erklären können
> - Die Speicherhierarchie kennen
> - Verstehen, wie mehr Speicher genutzt werden kann als physisch vorhanden
> - Page Faults und das Working Set Konzept kennen

---

## Überblick

Virtueller Speicher ist eine der elegantesten Abstraktionen in der Geschichte der Computertechnik. Er löst ein fundamentales Problem: Programme benötigen oft mehr Speicher als physisch vorhanden ist, und selbst wenn genug RAM existiert, sollen mehrere Programme gleichzeitig laufen können, ohne sich gegenseitig zu stören.

Die Idee entstand in den 1960er Jahren am MIT und der Universität Manchester. Das erste System mit virtuellem Speicher war der **Atlas Computer** (1962), der bereits Paging verwendete. Die Entwickler erkannten, dass Programme typischerweise zu jedem Zeitpunkt nur einen kleinen Teil ihres Codes und ihrer Daten aktiv nutzen – eine Beobachtung, die als **Lokalitätsprinzip** bekannt wurde und die Grundlage für virtuellen Speicher bildet.

---

## Definition

> [!quote] **Formale Definition**
> **Virtueller Speicher** ist eine Technik, die den Hauptspeicher durch Auslagern auf die Festplatte erweitert. Mehrere Pages können derselben Kachel entsprechen – aktuell nicht benötigte Pages sind zwischenzeitlich auf die Festplatte ausgelagert.

Der virtuelle Speicher kombiniert drei Techniken:

1. **Adressübersetzung:** Logische Adressen werden zur Laufzeit in physische übersetzt (→ MMU)
2. **Demand Paging:** Pages werden erst geladen, wenn sie tatsächlich benötigt werden
3. **Page Replacement:** Wenn der RAM voll ist, werden wenig genutzte Pages auf die Festplatte ausgelagert

---

## Das Lokalitätsprinzip

Der virtuelle Speicher funktioniert nur deshalb effizient, weil Programme ein vorhersagbares Zugriffsverhalten zeigen:

| Art | Beschreibung | Beispiel |
|-----|--------------|----------|
| **Zeitliche Lokalität** | Kürzlich benutzte Daten werden bald wieder benutzt | Schleifenvariable, die in jeder Iteration gelesen wird |
| **Räumliche Lokalität** | Benachbarte Adressen werden zusammen genutzt | Durchlaufen eines Arrays, sequentielles Lesen einer Datei |

> [!example] **Analogie: Schreibtisch**
> Stell dir deinen Schreibtisch als RAM vor und den Aktenschrank als Festplatte. Du holst dir nur die Akten auf den Schreibtisch, die du gerade brauchst. Wenn der Schreibtisch voll wird, räumst du Akten zurück, die du länger nicht angeschaut hast. Das funktioniert gut, weil du an einem Projekt typischerweise mit denselben Dokumenten arbeitest (zeitliche Lokalität) und verwandte Dokumente oft zusammen benötigst (räumliche Lokalität).

---

## Grundprinzip

![[02-05-02-virtueller-speicher.png]]
*<span class="fig-id">02-05-02-virtueller-speicher</span>: Virtueller Speicher: Das Programm sieht einen zusammenhängenden Adressraum, aber in Wirklichkeit liegen nur aktiv genutzte Pages im RAM. Nicht benötigte Pages sind auf die Festplatte (Swap) ausgelagert.*

### Vorteile des virtuellen Speichers

| Vorteil | Beschreibung |
|---------|--------------|
| **Größerer Adressraum** | Programme können mehr Speicher nutzen als physisch vorhanden |
| **Isolation** | Jeder Prozess hat seinen eigenen Adressraum; Zugriff auf fremden Speicher ist unmöglich |
| **Vereinfachung** | Programme können so geschrieben werden, als hätten sie den gesamten Speicher für sich |
| **Effiziente Nutzung** | Nur aktiv genutzte Daten belegen physischen RAM |
| **Sharing** | Gemeinsam genutzte Bibliotheken können einmal im RAM liegen und in mehreren Adressräumen erscheinen |

### Kosten des virtuellen Speichers

| Kosten | Beschreibung |
|--------|--------------|
| **Page Faults** | Zugriff auf ausgelagerte Daten dauert Millisekunden statt Nanosekunden |
| **Speicherverbrauch** | Page Tables benötigen selbst Speicher |
| **Komplexität** | MMU, TLB, Page Tables erfordern Hardware und Software-Unterstützung |

---

## Speicherhierarchie

Die Speicherhierarchie ist ein fundamentales Konzept der Rechnerarchitektur. Sie nutzt die Tatsache aus, dass schneller Speicher teuer ist und langsamer Speicher billig:

![[02-05-02-speicherhierarchie.png]]
*<span class="fig-id">02-05-02-speicherhierarchie</span>: Die Speicherhierarchie als Pyramide: Je näher an der CPU (oben), desto schneller und teurer. Je weiter entfernt (unten), desto langsamer, günstiger und größer.*

### Kennzahlen der Speicherebenen

| Speicherart | Typische Zugriffszeit | Typische Größe | Kosten/GB (ca.) |
|-------------|----------------------|----------------|-----------------|
| Register | < 1 ns | Bytes (KB) | – |
| L1 Cache | 1-2 ns | 32-64 KB | – |
| L2 Cache | 3-10 ns | 256 KB - 1 MB | – |
| L3 Cache | 10-20 ns | 4-50 MB | – |
| RAM | ≈ 60-100 ns | 8-128 GB | ~3-5 € |
| SSD (NVMe) | 10-100 µs | 256 GB - 4 TB | ~0,10 € |
| SSD (SATA) | 100-500 µs | 256 GB - 4 TB | ~0,08 € |
| HDD | 5-15 ms | 1-20 TB | ~0,02 € |

> [!info] **Größenordnungen verstehen**
> Der Unterschied zwischen RAM (60 ns) und HDD (10 ms) ist ein Faktor von etwa **150.000**. Wenn ein RAM-Zugriff einer Sekunde entspräche, würde ein HDD-Zugriff fast **2 Tage** dauern!

### Warum diese Hierarchie?

Die Speicherhierarchie ist keine willkürliche Entscheidung, sondern folgt physikalischen und ökonomischen Gesetzmäßigkeiten:

1. **Physikalische Grenzen:** Je näher der Speicher an der CPU, desto schneller (kürzere Signalwege). Register sind direkt in der CPU, L1-Cache ist auf demselben Chip.

2. **Kosten-Kapazitäts-Tradeoff:** Schnelle Speichertechnologien (SRAM für Cache) sind teuer. Langsame Technologien (NAND-Flash, magnetische Platten) sind billig.

3. **Lokalitätsprinzip:** Die Hierarchie funktioniert nur, weil Programme vorhersagbare Zugriffsmuster haben. Ohne Lokalität wäre jede Cache-Ebene nutzlos.

---

## Swapping und Demand Paging

Es gibt zwei grundlegende Strategien, um den virtuellen Speicher zu realisieren:

### Swapping (Prozess-Ebene)

Beim Swapping werden **ganze Prozesse** zwischen RAM und Festplatte verschoben. Diese Technik stammt aus den frühen Multitasking-Systemen der 1960er Jahre.

![[02-05-02-swapping.png]]
*<span class="fig-id">02-05-02-swapping</span>: Swapping: Ganze Prozesse werden zwischen RAM und Swap-Bereich verschoben. Swap Out lagert einen Prozess aus, Swap In holt ihn zurück.*

| Eigenschaft | Beschreibung |
|-------------|--------------|
| **Granularität** | Ganzer Prozess wird ein- oder ausgelagert |
| **Verwendung** | Wenn ein Prozess lange blockiert ist (z.B. auf I/O wartet) |
| **Vorteil** | Einfache Verwaltung, keine Fragmentierung des Prozesses |
| **Nachteil** | Lange Latenz beim Swap-In, Verschwendung wenn Prozess nur Teil seines Speichers nutzt |

> [!note] **Moderner Einsatz**
> Reines Swapping wird heute selten verwendet. Linux kombiniert Swapping mit Demand Paging: Der **OOM-Killer** (Out-of-Memory Killer) terminiert Prozesse nur im Notfall, normalerweise werden einzelne Pages ausgelagert.

### Demand Paging (Page-Ebene)

Demand Paging lädt Pages **erst bei Bedarf** (Lazy Loading). Dies ist die Standardtechnik moderner Betriebssysteme.

![[02-05-02-demand-paging.png]]
*<span class="fig-id">02-05-02-demand-paging</span>: Demand Paging: Pages werden erst bei Zugriff geladen. Ist die Page im RAM, erfolgt der Zugriff direkt. Andernfalls wird ein Page Fault ausgelöst und die Page von der Festplatte nachgeladen.*

| Eigenschaft | Beschreibung |
|-------------|--------------|
| **Granularität** | Einzelne Pages (typisch 4 KB) |
| **Verwendung** | Standard bei allen modernen Systemen |
| **Vorteil** | Minimaler RAM-Verbrauch, schneller Programmstart |
| **Nachteil** | Page Faults verursachen kurze Verzögerungen |

### Vergleich: Swapping vs. Demand Paging

| Kriterium | Swapping | Demand Paging |
|-----------|----------|---------------|
| Einheit | Ganzer Prozess | Einzelne Page |
| Latenz beim Auslagern | Hoch (gesamter Prozess) | Niedrig (nur eine Page) |
| Speichereffizienz | Niedrig | Hoch |
| Komplexität | Einfach | Komplex (Page Tables, Ersetzung) |
| Moderne Verwendung | Selten, nur bei Speichernotstand | Standard |

---

## Page Fault

> [!quote] **Definition**
> Ein **Page Fault** (Seitenfehler) tritt auf, wenn ein Prozess auf eine Speicherseite zugreift, die sich nicht im physischen Hauptspeicher befindet.

Page Faults sind ein normaler Teil des Demand Paging – sie sind kein „Fehler" im Sinne eines Programmfehlers, sondern ein Mechanismus, um Pages bei Bedarf nachzuladen.

### Arten von Page Faults

| Art | Beschreibung | Behandlung |
|-----|--------------|------------|
| **Minor (Soft) Fault** | Page ist im RAM, aber nicht in der Page Table des Prozesses (z.B. Shared Library bereits geladen) | Page Table Update, sehr schnell |
| **Major (Hard) Fault** | Page muss von der Festplatte geladen werden | I/O-Operation, langsam (Millisekunden) |
| **Invalid Fault** | Zugriff auf nicht-existente oder geschützte Adresse | Segmentation Fault, Prozess wird terminiert |

### Ablauf bei Page Fault

Der Ablauf eines Major Page Faults ist komplex und involviert mehrere Systemkomponenten:

1. **Trap-Auslösung:** CPU erkennt über das Valid-Bit in der Page Table, dass die Page nicht im RAM ist, und löst einen Interrupt aus

2. **Kontextwechsel:** CPU wechselt in den Kernel-Mode; der aktuelle Zustand des Prozesses wird gesichert

3. **Validierung:** Betriebssystem prüft:
   - Ist die Adresse überhaupt gültig für diesen Prozess?
   - Hat der Prozess die nötigen Rechte (Read/Write/Execute)?

4. **Freien Frame finden:** 
   - Gibt es einen freien Frame? → Verwende ihn
   - Alle Frames belegt? → Page Replacement (eine andere Page auslagern)

5. **Disk I/O:** Page wird von der Festplatte (Swap-Partition oder Datei) gelesen

6. **Page Table Update:** Eintrag wird aktualisiert (physische Adresse, Valid-Bit = 1)

7. **Prozess fortsetzen:** Der unterbrochene Befehl wird erneut ausgeführt

> [!warning] **Performance-Implikationen**
> Ein Major Page Fault kostet typischerweise **10-15 Millisekunden** (bei HDD) oder **100-500 Mikrosekunden** (bei SSD). Im Vergleich: Ein normaler Speicherzugriff dauert **60-100 Nanosekunden**. Das ist ein Unterschied von Faktor 1.000 bis 100.000!

### Page Fault Rate

Die **Page Fault Rate** (p) ist der Anteil der Speicherzugriffe, die einen Page Fault verursachen. Die effektive Zugriffszeit (EAT) berechnet sich:

```
EAT = (1 - p) × Speicherzugriffszeit + p × Page-Fault-Zeit
```

> [!example] **Beispielrechnung**
> - Speicherzugriffszeit: 100 ns
> - Page-Fault-Zeit: 10 ms = 10.000.000 ns
> - Page Fault Rate: p = 0,001 (1 von 1000 Zugriffen)
> 
> EAT = 0,999 × 100 ns + 0,001 × 10.000.000 ns
> EAT = 99,9 ns + 10.000 ns = **10.100 ns**
> 
> Selbst bei einer Page Fault Rate von nur 0,1% verlangsamt sich das System um Faktor 100!

---

## Seitenersetzungsstrategien

Wenn der RAM voll ist und eine neue Page geladen werden muss, muss eine vorhandene Page weichen. Die Wahl des „Opfers" beeinflusst die Performance erheblich.

### Optimal (OPT / Belady)

Ersetze die Page, die am längsten nicht mehr benötigt wird.

| Eigenschaft | Beschreibung |
|-------------|--------------|
| **Vorteil** | Theoretisch optimal, minimale Page Faults |
| **Nachteil** | Nicht implementierbar (erfordert Wissen über Zukunft) |
| **Verwendung** | Nur als Benchmark zum Vergleich anderer Algorithmen |

### FIFO (First In, First Out)

Ersetze die Page, die am längsten im RAM ist.

| Eigenschaft | Beschreibung |
|-------------|--------------|
| **Vorteil** | Einfach zu implementieren (Queue) |
| **Nachteil** | Ignoriert Nutzungshäufigkeit; **Belady-Anomalie** möglich |
| **Verwendung** | Selten, wegen schlechter Performance |

> [!info] **Belady-Anomalie**
> Bei FIFO kann es passieren, dass mehr Frames zu **mehr** Page Faults führen – ein kontraintuitives Verhalten, das 1969 von László Bélády entdeckt wurde.

### LRU (Least Recently Used)

Ersetze die Page, die am längsten nicht benutzt wurde.

| Eigenschaft | Beschreibung |
|-------------|--------------|
| **Vorteil** | Nutzt zeitliche Lokalität, gute Ergebnisse |
| **Nachteil** | Aufwendig zu implementieren (Zeitstempel oder Stack) |
| **Verwendung** | Konzeptuell ideal, aber exakte Implementierung zu teuer |

### Clock (Second Chance)

Approximation von LRU mit einem Reference-Bit pro Page.

| Eigenschaft | Beschreibung |
|-------------|--------------|
| **Vorteil** | Effizient implementierbar, gute Ergebnisse |
| **Nachteil** | Nur Approximation von LRU |
| **Verwendung** | Standard in vielen Betriebssystemen (Linux, Windows) |

### Vergleich der Strategien

| Algorithmus | Page Faults | Implementierungsaufwand | Praxiseinsatz |
|-------------|-------------|-------------------------|---------------|
| OPT | Minimal | Unmöglich | Nur theoretisch |
| FIFO | Hoch | Sehr einfach | Kaum |
| LRU | Niedrig | Hoch | Selten exakt |
| Clock | Niedrig | Mittel | Sehr häufig |

---

## Working Set

> [!quote] **Definition**
> Das **Working Set** eines Prozesses ist die Menge der Seiten, die der Prozess in einem bestimmten Zeitfenster (Δ) aktiv nutzt.

Das Working Set Modell wurde 1968 von **Peter Denning** eingeführt und ist fundamental für das Verständnis von virtuellem Speicher.

![[02-05-02-working-set.png]]
*<span class="fig-id">02-05-02-working-set</span>: Working Set: Das Zeitfenster (Δ=3) bestimmt, welche Pages zum aktuellen Working Set gehören. Bei den ersten drei Zugriffen ist das Working Set {P1, P2}, später wechselt es zu {P4, P5}.*

### Working Set Size (WSS)

Die Größe des Working Sets variiert im Laufe der Programmausführung:

| Phase | WSS | Beispiel |
|-------|-----|----------|
| **Initialisierung** | Wachsend | Programm lädt Bibliotheken, initialisiert Datenstrukturen |
| **Stabile Phase** | Konstant | Programm arbeitet mit festen Datenstrukturen |
| **Phasenübergang** | Sprunghaft | Programm wechselt zu anderer Aufgabe (z.B. von Laden zu Verarbeiten) |

### Thrashing

> [!quote] **Definition**
> **Thrashing** tritt auf, wenn das System mehr Zeit mit Paging verbringt als mit produktiver Arbeit. Das passiert, wenn die Summe aller Working Sets den verfügbaren RAM übersteigt.

Symptome von Thrashing:
- CPU-Auslastung sinkt, obwohl viele Prozesse laufen
- Festplattenaktivität ist sehr hoch
- System reagiert extrem langsam
- Page Fault Rate explodiert

### Thrashing vermeiden

| Strategie | Beschreibung |
|-----------|--------------|
| **Working Set Strategie** | Prozess erhält nur RAM, wenn sein gesamtes Working Set Platz hat |
| **Page Fault Frequency (PFF)** | Überwache Page Fault Rate; zu hoch → mehr Frames; zu niedrig → weniger Frames |
| **Swapping** | Ganze Prozesse auslagern, um anderen genug RAM zu geben |
| **OOM-Killer** | Im Notfall: Prozesse terminieren (Linux) |

> [!tip] **Praktische Empfehlung**
> Wenn ein System thrasht, hilft oft nur: RAM erweitern oder Prozesse beenden. Mehr Swap-Space hilft kaum, weil das Problem nicht der Speicherplatz ist, sondern die Zugriffszeit.

---

## Swap-Space Verwaltung

Der Swap-Space ist der Bereich auf der Festplatte, der für ausgelagerte Pages verwendet wird.

### Swap in verschiedenen Betriebssystemen

| System | Swap-Implementierung |
|--------|---------------------|
| **Linux** | Dedizierte Swap-Partition oder Swap-Datei; mehrere Swap-Bereiche mit Prioritäten möglich |
| **Windows** | Auslagerungsdatei (pagefile.sys); Größe oft automatisch verwaltet |
| **macOS** | Dynamische Swap-Dateien in /private/var/vm/ |

### Linux Swap-Kommandos

```bash
# Swap-Nutzung anzeigen
$ free -h
              total        used        free      shared  buff/cache   available
Mem:           15Gi       8,2Gi       1,5Gi       1,2Gi       5,8Gi       5,7Gi
Swap:          8,0Gi       512Mi       7,5Gi

# Detaillierte Swap-Informationen
$ swapon --show
NAME      TYPE      SIZE   USED PRIO
/dev/sda2 partition 8G     512M -2

# Swappiness anzeigen (0-100, höher = aggressiver swappen)
$ cat /proc/sys/vm/swappiness
60
```

> [!note] **Swappiness**
> Der Linux-Kernel-Parameter `swappiness` (0-100) steuert, wie aggressiv das System Pages auslagert. Ein niedriger Wert (z.B. 10) bevorzugt das Auslagern von File-Cache; ein hoher Wert (z.B. 60) lagert auch Prozess-Speicher früher aus. Für Desktop-Systeme wird oft 10-20 empfohlen.

---

## Copy-on-Write (CoW)

Eine wichtige Optimierung im Zusammenhang mit virtuellem Speicher:

> [!quote] **Definition**
> **Copy-on-Write** (CoW) verzögert das Kopieren von Speicherseiten, bis tatsächlich eine Schreiboperation stattfindet. Bis dahin teilen sich mehrere Prozesse dieselbe physische Page.

### Anwendung bei fork()

Wenn ein Prozess mit `fork()` einen Kindprozess erzeugt:

1. **Ohne CoW:** Gesamter Speicher wird kopiert → langsam, verschwenderisch
2. **Mit CoW:** Kind erhält Kopie der Page Table, aber Pages sind als read-only markiert

Erst wenn Eltern- oder Kindprozess schreibt:
- Page Fault wird ausgelöst
- Nur die betroffene Page wird kopiert
- Beide Prozesse haben nun eigene Kopie dieser Page

> [!tip] **Vorteil**
> Die Kombination `fork()` + `exec()` (neues Programm starten) kopiert praktisch keinen Speicher, weil `exec()` den Adressraum sofort ersetzt.

---

## Zusammenhänge

- [[01-Adressraeume|Adressräume]] → Virtueller Speicher erweitert den Adressraum
- [[03-Paging|Paging]] → Technische Umsetzung des virtuellen Speichers
- [[04-Segmentierung|Segmentierung]] → Alternative/Ergänzung zu Paging
- [[../03-Prozesse/01-Prozessmodell|Prozessmodell]] → Jeder Prozess hat eigenen virtuellen Adressraum

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - Konzept des virtuellen Speichers und Lokalitätsprinzip
> - Page Fault: Arten und Behandlung
> - Speicherhierarchie (Zugriffszeiten kennen!)

> [!question] **Häufige Prüfungsfragen**
> 1. Was ist virtueller Speicher und welche Vorteile bietet er?
> 2. Erklären Sie das Lokalitätsprinzip (zeitlich und räumlich)!
> 3. Was passiert bei einem Page Fault? Beschreiben Sie den Ablauf!
> 4. Erklären Sie die Speicherhierarchie und nennen Sie typische Zugriffszeiten!
> 5. Was versteht man unter Thrashing und wie kann es vermieden werden?
> 6. Vergleichen Sie die Seitenersetzungsstrategien FIFO, LRU und Clock!
> 7. Was ist der Unterschied zwischen Swapping und Demand Paging?
> 8. Berechnen Sie die effektive Zugriffszeit bei gegebener Page Fault Rate!

> [!tip] **Merkhilfen**
> - **Virtueller Speicher** = „Mehr Platz als da ist" (Illusion durch Auslagerung)
> - **Lokalität** = „Was ich gerade brauche, brauche ich gleich wieder"
> - **Page Fault** = „Seite nicht gefunden – Festplatte muss ran"
> - **Thrashing** = „System erstickt an Page Faults"
> - **Working Set** = „Die Seiten, die der Prozess gerade wirklich braucht"
> - **LRU** = „Wer am längsten nicht dran war, fliegt raus"
> - **FIFO-Anomalie** = „Mehr Platz, mehr Probleme" (Belady)

---

## Weiterführende Ressourcen

> [!note] **Videos (YouTube)**
>
> | | Video | Beschreibung |
> |---|-------|--------------|
> | 🎬 | [CoreDumped – Virtual Memory](https://www.youtube.com/watch?v=A9WLYbE0p-I) | Einführung in virtuellen Speicher |
> | 🎬 | [Computerphile – Virtual Memory](https://www.youtube.com/watch?v=5lFnKYCZT5o) | Anschauliche Erklärung mit Beispielen |
> | 🎬 | [MIT 6.004 – Virtual Memory](https://www.youtube.com/watch?v=cjZrQDWJZOg) | Akademische Vorlesung (MIT OpenCourseWare) |

---

## Quellen

- Vorlesung: „Betriebssysteme, Rechnernetze und verteilte Systeme" – IU, Teil 5 (Ressourcen)
- Tanenbaum, A. S. & Bos, H.: Modern Operating Systems, 5th Edition, Kapitel 3
- Silberschatz, A., Galvin, P. B. & Gagne, G.: Operating System Concepts, 10th Edition, Kapitel 9-10
- Arpaci-Dusseau, R. & Arpaci-Dusseau, A.: Operating Systems: Three Easy Pieces (OSTEP), Kapitel 18-22
- Denning, P. J.: The Working Set Model for Program Behavior (1968)

### Direkte Quellenreferenzen

**Tanenbaum, A. S. & Bos, H.: Modern Operating Systems (5th Edition)**
- Kapitel 3: Memory Management
  - 3.3 Virtual Memory (→ Grundkonzept)
  - 3.4 Page Replacement Algorithms (→ FIFO, LRU, Clock)
  - 3.5 Design Issues for Paging Systems (→ Working Set, Thrashing)

**Silberschatz, A., Galvin, P. B. & Gagne, G.: Operating System Concepts (10th Edition)**
- Chapter 9: Virtual Memory
  - 9.1 Background (→ Demand Paging)
  - 9.2 Demand Paging (→ Page Fault Handling)
  - 9.4 Page Replacement (→ Algorithmen)
  - 9.6 Thrashing (→ Working Set Model)
  - 9.7 Memory-Mapped Files
- Chapter 10: Mass-Storage Structure (→ Speicherhierarchie)
