---
author: Andreas Hümmer
title: Kritische Abschnitte
tags:
  - content
  - bs
  - synchronisation
  - kritischer-abschnitt
  - mutual-exclusion
created: '2026-10-07'
modified: '2026-10-09'
bereich: BS
---

# Kritische Abschnitte

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das Problem der Prozesssynchronisation verstehen
> - Kritische Abschnitte identifizieren können
> - Die Anforderungen an eine Lösung kennen (Mutual Exclusion, Progress, Bounded Waiting)
> - Die Struktur eines kritischen Abschnitts (Entry/Exit Section) verstehen

---

## Definition

> [!quote] **Formale Definition**
> Ein **kritischer Abschnitt** ist ein Programmabschnitt, in dem auf **gemeinsame Ressourcen** zugegriffen wird. Kritische Abschnitte dürfen nur von **einem Prozess zur gegebenen Zeit** durchlaufen werden.

Der Begriff stammt aus der frühen Betriebssystemforschung der 1960er Jahre. Edsger Dijkstra prägte ihn, als er die fundamentalen Probleme der Nebenläufigkeit untersuchte. Ein kritischer Abschnitt ist gewissermaßen eine "Engstelle" im Programm – ein Bereich, der nur von einem Prozess gleichzeitig betreten werden darf, ähnlich wie eine schmale Brücke, die nur ein Fahrzeug auf einmal passieren kann.

---

## Das Problem

Bei **nebenläufigen Prozessen** muss der Zugriff auf Ressourcen **koordiniert und wohldefiniert** ablaufen. Das Problem ist subtiler als es zunächst erscheint: Moderne CPUs führen Operationen nicht in der Reihenfolge aus, wie sie im Quellcode stehen (Out-of-Order Execution), und Compiler optimieren Code auf unerwartete Weise. Selbst wenn zwei Prozesse "nacheinander" auf eine Variable zugreifen, kann das tatsächliche Ergebnis von der Ausführungsreihenfolge auf Maschinenebene abhängen.

![[02-04-02-critical-section-problem.png]]
*<span class="fig-id">02-04-02-critical-section-problem</span>: Zwei Prozesse greifen gleichzeitig auf eine gemeinsame Variable zu – ohne Koordination ist das Ergebnis unvorhersagbar.*

Betrachten wir ein konkretes Beispiel: Ein Webserver verwaltet einen Zähler für aktive Verbindungen. Jeder eingehende Request erhöht den Zähler, jede geschlossene Verbindung verringert ihn. Ohne Schutz des kritischen Abschnitts könnte der Zähler falsche Werte anzeigen – er könnte negativ werden oder Verbindungen "verlieren". Bei einem ausgelasteten Server mit tausenden gleichzeitigen Anfragen wird dieses Problem garantiert auftreten.

> [!warning] **Was passiert ohne Schutz?**
> Ohne Synchronisation treten **Race Conditions** auf – das Ergebnis hängt vom zufälligen Timing ab.
> → Details siehe [[03-Race-Conditions|Race Conditions]]

---

## Struktur eines kritischen Abschnitts

Jeder kritische Abschnitt folgt einem charakteristischen Muster. Dieses Muster ist so fundamental, dass es in praktisch jeder Synchronisationslösung wiederkehrt – von low-level Spinlocks bis zu high-level Datenbankstransaktionen.

![[02-04-02-critical-section-structure.png]]
*<span class="fig-id">02-04-02-critical-section-structure</span>: Die vier Abschnitte eines kritischen Abschnitts – Entry Section zum Anfordern des Zugangs, der geschützte kritische Abschnitt selbst, Exit Section zum Freigeben und Remainder Section für nicht-kritischen Code.*

### Die vier Abschnitte im Detail

**Entry Section (Eingangsbereich):** Hier versucht der Prozess, Zugang zum kritischen Abschnitt zu erlangen. Je nach Implementierung wartet er aktiv (Busy Waiting/Spinlock) oder wird schlafen gelegt, bis er an der Reihe ist. Diese Phase ist oft der komplexeste Teil – hier entscheidet sich, ob die Lösung korrekt und effizient ist.

**Critical Section (Kritischer Abschnitt):** Der eigentliche geschützte Bereich. Hier findet der Zugriff auf die gemeinsame Ressource statt. Dieser Abschnitt sollte so kurz wie möglich sein, um andere Prozesse nicht unnötig zu blockieren.

**Exit Section (Ausgangsbereich):** Der Prozess gibt seinen exklusiven Zugang auf und signalisiert anderen wartenden Prozessen, dass sie eintreten können. Fehler in diesem Bereich sind besonders kritisch – ein vergessenes "Unlock" führt zu permanenter Blockierung.

**Remainder Section (Restbereich):** Alles, was nicht zum kritischen Abschnitt gehört. Hier kann der Prozess unabhängig arbeiten.

### Pseudocode

```c
while (true) {
    // Entry Section
    acquire_lock();          // Warte bis Zugang frei
    
    // KRITISCHER ABSCHNITT
    access_shared_resource();
    
    // Exit Section
    release_lock();          // Gib Zugang frei
    
    // Remainder Section
    do_other_work();
}
```

---

## Anforderungen an eine Lösung

Auf den ersten Blick scheint das Problem einfach: "Lass nur einen Prozess rein." Doch bei genauerem Hinsehen zeigt sich, dass eine korrekte Lösung drei Anforderungen gleichzeitig erfüllen muss – und das ist überraschend schwierig.

| Anforderung | Beschreibung | Verletzt wenn... |
|-------------|--------------|------------------|
| **Mutual Exclusion** | Höchstens ein Prozess im kritischen Abschnitt | Zwei Prozesse gleichzeitig drin |
| **Progress** | Freier Abschnitt wird betreten, Entscheidung terminiert | Niemand drin, aber keiner kommt rein |
| **Bounded Waiting** | Endliches Warten garantiert | Ein Prozess wartet ewig (Starvation) |

### 1. Mutual Exclusion (Gegenseitiger Ausschluss)

Dies ist die offensichtlichste Anforderung: Zu jedem Zeitpunkt darf sich höchstens **ein** Prozess im kritischen Abschnitt befinden. Wenn Prozess A den kritischen Abschnitt betreten hat, muss Prozess B warten, bis A den Abschnitt verlässt.

Diese Anforderung ist nicht verhandelbar – ohne sie gibt es keinen Schutz.

### 2. Progress (Fortschritt)

Wenn kein Prozess im kritischen Abschnitt ist und mindestens ein Prozess eintreten möchte, dann muss die Entscheidung, welcher Prozess eintritt, in **endlicher Zeit** fallen. Der kritische Abschnitt darf nicht "verwaisen".

Diese Anforderung verhindert Livelocks – Situationen, in denen Prozesse zwar arbeiten, aber keiner vorankommt (wie zwei Menschen, die sich in einem Gang ausweichen wollen und immer in dieselbe Richtung treten).

### 3. Bounded Waiting (Begrenztes Warten)

Es muss eine **obere Schranke** geben, wie oft andere Prozesse den kritischen Abschnitt betreten dürfen, während ein bestimmter Prozess wartet. Kein Prozess darf unendlich lange warten müssen.

Diese Anforderung garantiert Fairness und verhindert **Starvation** – das "Verhungern" eines Prozesses, der nie an die Reihe kommt.

> [!tip] **Warum alle drei?**
> Man könnte denken, Mutual Exclusion allein reicht. Aber ohne Progress könnte das System hängen bleiben, und ohne Bounded Waiting könnte ein Prozess ewig warten, obwohl andere weiterkommen.

---

## Beispiele für kritische Abschnitte

### Typische Szenarien in der Praxis

| Ressource | Kritischer Abschnitt | Gefahr ohne Schutz |
|-----------|---------------------|-------------------|
| **Shared Counter** | `counter++` | Lost Update |
| **Linked List** | Insert/Delete | Korrupte Zeiger, Speicherlecks |
| **Dateizugriff** | Schreiben | Datenverlust, korrupte Dateien |
| **Datenbank** | Transaktion | Inkonsistente Daten |
| **Hardware-Register** | I/O-Operation | Gerätefehler, Datenverlust |
| **Logging** | Log-Einträge schreiben | Verschachtelte, unleserliche Logs |

### Wann ist KEIN kritischer Abschnitt nötig?

Nicht jeder Zugriff auf gemeinsame Daten erfordert Synchronisation:

- **Lokale Variablen**: Jeder Thread hat seinen eigenen Stack – lokale Variablen sind automatisch thread-sicher.
- **Nur lesende Zugriffe**: Wenn alle Threads nur lesen (nie schreiben), gibt es keinen Konflikt.
- **Immutable Objects**: Objekte, die nach der Erstellung nie verändert werden, sind automatisch thread-sicher. Dieses Konzept nutzen funktionale Programmiersprachen wie Haskell intensiv.
- **Thread-Local Storage**: Jeder Thread hat seine eigene Kopie der Daten.

> [!example] **Java-Beispiel: Immutable String**
> In Java sind Strings unveränderlich. Mehrere Threads können denselben String lesen, ohne Synchronisation zu benötigen. Operationen wie `concat()` erzeugen einen neuen String, statt den bestehenden zu ändern.

---

## Lösungsansätze im Überblick

Es gibt mehrere Ebenen, auf denen kritische Abschnitte geschützt werden können:

| Ebene                  | Mechanismen                             | Charakteristik                      |
| ---------------------- | --------------------------------------- | ----------------------------------- |
| **Hardware**           | Unterbrechungssperre, Test-and-Set, CAS | Schnell, aber low-level             |
| **Betriebssystem**     | Semaphore, Mutexe                       | Blockierend, effizient              |
| **Programmiersprache** | Monitore, `synchronized`, `lock`        | Komfortabel, weniger fehleranfällig |

Die Wahl hängt vom Anwendungsfall ab: Kernel-Entwickler nutzen Hardware-Primitiven, Anwendungsentwickler greifen zu Sprachkonstrukten.

**→ Details:** [[05-Synchronisationsmechanismen|Synchronisationsmechanismen]]

---

## Historischer Kontext

Das Problem der kritischen Abschnitte wurde in den 1960er Jahren erkannt, als die ersten Timesharing-Systeme aufkamen:

- **1962**: Per Brinch Hansen beschreibt erstmals das Problem des gegenseitigen Ausschlusses
- **1965**: Edsger Dijkstra veröffentlicht seine Lösung mit Semaphoren
- **1965**: Dekker's Algorithm – erste korrekte Software-Lösung für zwei Prozesse
- **1981**: Peterson's Algorithm – elegantere Lösung, leichter zu verstehen
- **Heute**: Hardware bietet atomare Operationen, Sprachen bieten high-level Konstrukte

> [!note] **Dijkstras Einfluss**
> Dijkstra prägte nicht nur den Begriff "kritischer Abschnitt", sondern auch die formale Analyse von Nebenläufigkeit. Seine Arbeit legte den Grundstein für moderne Konzepte wie Semaphore und Monitore.

---

## Zusammenhänge

- [[03-Race-Conditions|Race Conditions]] → Entstehen in ungeschützten kritischen Abschnitten
- [[04-Deadlocks|Deadlocks]] → Können bei falscher Synchronisation entstehen
- [[05-Synchronisationsmechanismen|Synchronisationsmechanismen]] → Lösungen für kritische Abschnitte
- [[03-Threads|Threads]] → Threads teilen Adressraum → kritische Abschnitte nötig

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - Definition kritischer Abschnitt
> - Die drei Anforderungen (Mutual Exclusion, Progress, Bounded Waiting)
> - Struktur: Entry Section, Critical Section, Exit Section

> [!question] **Häufige Prüfungsfragen**
> 1. Was ist ein kritischer Abschnitt und wann tritt er auf?
> 2. Nennen Sie die drei Anforderungen an eine Lösung für kritische Abschnitte!
> 3. Was bedeutet "Mutual Exclusion"?
> 4. Erklären Sie die Struktur eines kritischen Abschnitts (Entry/Exit)!
> 5. Warum reicht nur Mutual Exclusion nicht aus?
> 6. Was ist der Unterschied zwischen Progress und Bounded Waiting?

> [!tip] **Merkhilfen**
> - **Kritischer Abschnitt** = "Engpass auf der Einbahnstraße"
> - **Mutual Exclusion** = "Nur einer darf rein"
> - **Progress** = "Es darf nicht stocken"
> - **Bounded Waiting** = "Keiner wird vergessen"
> - **Entry/Exit** = "Türsteher am Club"
> - Die drei Anforderungen: **M**utual exclusion, **P**rogress, **B**ounded waiting → "MPB"

---

## Weiterführende Ressourcen

> [!note] **Videos (YouTube)**
>
> | | Video | Beschreibung |
> |---|-------|--------------|
> | 🎬 | [CoreDumped – Concurrency](https://www.youtube.com/watch?v=3X93PnKRNUo) | Nebenläufigkeit und Synchronisation |

---

## Quellen

- IU Skript: Betriebssysteme, Rechnernetze und verteilte Systeme - Teil 5 (Ressourcen)
- Tanenbaum: Modern Operating Systems
- Dijkstra, E.W.: "Solution of a Problem in Concurrent Programming Control" (1965)
- Peterson, G.L.: "Myths About the Mutual Exclusion Problem" (1981)
