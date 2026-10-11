---
author: Andreas Hümmer
title: Einführung Synchronisation
tags:
  - content
  - bs
  - synchronisation
  - uebersicht
created: '2026-10-09'
modified: '2026-10-09'
bereich: BS
---

# Einführung in die Synchronisation

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Verstehen, warum Synchronisation bei nebenläufigen Prozessen notwendig ist
> - Die grundlegenden Probleme der Prozesssynchronisation kennen
> - Einen Überblick über Lösungsansätze haben
> - Die Zusammenhänge zwischen den verschiedenen Themen verstehen

---

## Warum Synchronisation?

Moderne Betriebssysteme führen viele Prozesse und Threads quasi-gleichzeitig aus. Diese Nebenläufigkeit bringt enorme Vorteile – bessere CPU-Auslastung, reaktionsfähige Benutzeroberflächen, parallele Verarbeitung auf Mehrkernprozessoren. Doch sobald mehrere Ausführungseinheiten auf **gemeinsame Ressourcen** zugreifen, entstehen fundamentale Probleme.

Stell dir vor, zwei Bankangestellte bearbeiten gleichzeitig dasselbe Konto: Einer bucht eine Einzahlung, der andere eine Abhebung. Wenn beide den aktuellen Kontostand lesen, ihre Berechnung durchführen und dann das Ergebnis speichern – ohne voneinander zu wissen – geht unweigerlich eine Buchung verloren. Genau dieses Problem tritt in Software ständig auf, sobald Prozesse oder Threads Daten teilen.

![[02-04-01-sync-overview.png]]
*<span class="fig-id">02-04-01-sync-overview</span>: Überblick über die Notwendigkeit von Synchronisation bei nebenläufigen Prozessen – ohne Koordination entstehen Fehler, mit Synchronisation bleibt das System konsistent.*

Die Herausforderung: Wir wollen die Vorteile der Nebenläufigkeit nutzen, aber die Gefahren vermeiden. Dafür brauchen wir **Synchronisationsmechanismen** – Werkzeuge, die den Zugriff auf gemeinsame Ressourcen koordinieren.

---

## Die drei Grundprobleme

Die Synchronisation adressiert drei zentrale Probleme, die eng miteinander zusammenhängen:

### 1. Kritische Abschnitte

Wenn ein Programm auf gemeinsame Daten zugreift, muss dieser Codebereich besonders geschützt werden. Man nennt ihn **kritischen Abschnitt**. Das fundamentale Problem: Wie stellt man sicher, dass nur **ein einziger Prozess** gleichzeitig in einem kritischen Abschnitt arbeitet?

Die Anforderungen sind strenger als man zunächst denkt. Es genügt nicht, einfach "einen nach dem anderen" durchzulassen. Ein korrekter Schutzmechanismus muss garantieren:
- **Gegenseitiger Ausschluss**: Niemals zwei Prozesse gleichzeitig im kritischen Bereich
- **Fortschritt**: Wenn der Bereich frei ist, darf niemand grundlos blockiert werden
- **Fairness**: Kein Prozess wartet ewig, während andere immer wieder drankommen

Diese scheinbar einfachen Anforderungen sind überraschend schwer gleichzeitig zu erfüllen.

**→ Details:** [[02-Kritische-Abschnitte|Kritische Abschnitte]]

### 2. Race Conditions

Was passiert, wenn kritische Abschnitte nicht geschützt werden? Es entstehen **Race Conditions** – Wettlaufsituationen, bei denen das Ergebnis vom zufälligen Timing abhängt.

Das klassische Beispiel: Zwei Threads erhöhen gleichzeitig eine Variable `counter`. Man erwartet, dass der Zähler um 2 steigt. Aber `counter++` ist keine atomare Operation – der Compiler übersetzt sie in drei Schritte: Laden, Erhöhen, Speichern. Wenn beide Threads den alten Wert laden, bevor einer speichert, geht eine Erhöhung verloren.

Race Conditions sind besonders heimtückisch:
- Sie treten nicht bei jedem Durchlauf auf, sondern nur bei "ungünstigem" Timing
- Beim Debugging verschwinden sie oft, weil der Debugger das Timing verändert
- Unter Last werden sie häufiger, was die Fehlersuche erschwert
- Ein Race-Condition-Bug im Linux-Kernel ("Dirty COW", 2016) blieb neun Jahre unentdeckt

**→ Details:** [[03-Race-Conditions|Race Conditions]]

### 3. Deadlocks

Wenn Synchronisation falsch eingesetzt wird, entstehen neue Probleme. Das bekannteste ist der **Deadlock** – eine Situation, in der sich Prozesse gegenseitig blockieren und keiner mehr weiterkommt.

Das "Philosophenproblem" von Dijkstra illustriert dies anschaulich: Fünf Philosophen sitzen am runden Tisch, zwischen je zwei Philosophen liegt eine Gabel. Zum Essen braucht jeder zwei Gabeln. Wenn alle gleichzeitig die linke Gabel nehmen, wartet jeder auf die rechte Gabel seines Nachbarn – ewig.

Deadlocks erfordern vier Bedingungen gleichzeitig:
- Exklusiver Ressourcenzugriff
- Halten und Warten auf weitere Ressourcen
- Keine gewaltsame Entziehung möglich
- Zyklische Wartebeziehung

Die gute Nachricht: Man kann Deadlocks verhindern, vermeiden, erkennen oder (in der Praxis oft) einfach ignorieren und darauf hoffen, dass sie selten genug auftreten.

**→ Details:** [[04-Deadlocks|Deadlocks]]

---

## Lösungsansätze

Für die Synchronisation existieren Mechanismen auf unterschiedlichen Ebenen des Systems:

| Ebene | Mechanismen |
|-------|-------------|
| **Hardware** | Unterbrechungssperre, Atomare Operationen (Test-and-Set, CAS), Spinlocks |
| **Betriebssystem** | Semaphore (P/V-Operationen), Mutexe |
| **Programmiersprache** | Monitore, Condition Variables, `synchronized` (Java), `lock` (C#), `with` (Python) |

*Jede Ebene baut auf der darunterliegenden auf.*

Jede Ebene baut auf der darunterliegenden auf. Atomare Hardware-Operationen ermöglichen die Implementierung von Semaphoren im Betriebssystem. Diese wiederum bilden die Grundlage für komfortable Sprachkonstrukte wie Javas `synchronized`-Blöcke.

**→ Details:** [[05-Synchronisationsmechanismen|Synchronisationsmechanismen]]

---

## Übersicht der Themen

| Kapitel | Thema | Kernfrage |
|---------|-------|-----------|
| [[02-Kritische-Abschnitte\|02]] | Kritische Abschnitte | Welcher Code muss geschützt werden? |
| [[03-Race-Conditions\|03]] | Race Conditions | Was passiert ohne Schutz? |
| [[04-Deadlocks\|04]] | Deadlocks | Was kann bei Synchronisation schiefgehen? |
| [[05-Synchronisationsmechanismen\|05]] | Mechanismen | Wie schützt man richtig? |

---

## Praxisrelevanz

Synchronisation ist in der modernen Softwareentwicklung allgegenwärtig:

| Anwendungsbereich | Beispiel | Synchronisationsbedarf |
|-------------------|----------|------------------------|
| **Webserver** | Apache, nginx | Tausende gleichzeitige Anfragen auf gemeinsame Daten |
| **Datenbanken** | MySQL, PostgreSQL | ACID-Transaktionen mit Isolation garantieren |
| **Betriebssysteme** | Linux Kernel | Prozesse teilen sich Kernel-Datenstrukturen |
| **Spiele** | Unity, Unreal | Separate Threads für Grafik, Physik, KI, Audio |
| **Bankensysteme** | Überweisungen | Kontobewegungen müssen atomar sein |
| **Cloud-Dienste** | AWS, Azure | Verteilte Systeme mit konsistenten Daten |

> [!warning] **Wichtig für die Praxis**
> Synchronisationsfehler sind besonders tückisch:
> - Sie treten oft nur unter Last auf
> - Sie sind schwer reproduzierbar
> - Sie können zu Datenverlust oder Sicherheitslücken führen
> - Sie werden bei Code-Reviews leicht übersehen

---

## Historischer Kontext

Die Grundlagen der Synchronisation wurden in den 1960er Jahren gelegt, als Timesharing-Systeme aufkamen:

- **1965**: Edsger Dijkstra erfindet Semaphore mit P/V-Operationen
- **1971**: Coffman definiert die vier Bedingungen für Deadlocks
- **1974**: Hoare und Brinch Hansen entwickeln Monitore
- **1970er**: Das Producer-Consumer-Problem wird zum Standardbeispiel
- **Heute**: Multicore-CPUs machen Synchronisation wichtiger denn je

> [!tip] **Dijkstra über Semaphore**
> Die Namen P ("proberen" = versuchen) und V ("verhogen" = erhöhen) stammen aus dem Niederländischen – Dijkstras Muttersprache.

---

## Weiterführende Ressourcen

> [!note] **Videos (YouTube)**
>
> | | Video | Beschreibung |
> |---|-------|--------------|
> | 🎬 | [CoreDumped – Concurrency](https://www.youtube.com/watch?v=3X93PnKRNUo) | Überblick Nebenläufigkeit und Synchronisation |
> | 🎬 | [Vfhcap eduloop – Race Conditions](https://www.youtube.com/watch?v=dlOg4Dz-bgM) | Race Conditions erklärt (Deutsch) |

---

## Quellen

- IU Skript: Betriebssysteme, Rechnernetze und verteilte Systeme - Teil 5 (Ressourcen)
- Tanenbaum: Modern Operating Systems
- Dijkstra, E.W.: "Cooperating Sequential Processes" (1965)
- Coffman, E.G. et al.: "System Deadlocks" (1971)
