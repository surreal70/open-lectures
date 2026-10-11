---
author: Andreas Hümmer
title: Deadlocks
tags:
  - content
  - bs
  - synchronisation
  - deadlock
  - verklemmung
  - banker-algorithmus
created: '2026-10-07'
modified: '2026-10-09'
bereich: BS
---

# Deadlocks (Verklemmungen)

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Definition eines Deadlocks kennen
> - Die vier notwendigen Bedingungen (Coffman-Bedingungen) verstehen
> - Die vier Strategien zur Behandlung von Deadlocks kennen
> - Den Banker's Algorithm erklären können
> - Deadlock-Situationen erkennen und lösen können

---

## Definition

> [!quote] **Formale Definition**
> Eine Menge von Prozessen befindet sich in einem **Deadlock-Zustand**, wenn jeder Prozess aus der Menge auf ein Ereignis wartet, das nur ein anderer Prozess aus der Menge auslösen kann.

Ein Deadlock ist eine Situation, in der nichts mehr geht – und auch nie wieder etwas gehen wird, solange nicht von außen eingegriffen wird. Im Gegensatz zu einer Race Condition, die sporadisch falsche Ergebnisse liefert, ist ein Deadlock absolut: Das System steht still.

Der Begriff stammt aus der Eisenbahntechnik des 19. Jahrhunderts, wo zwei Züge auf demselben Gleis aufeinander zufahren konnten und keiner zurücksetzen konnte. In der Informatik wurde das Problem in den 1960er Jahren formalisiert, als Multiprogramming-Systeme erstmals mehrere Prozesse gleichzeitig verwalteten.

Ein alltägliches Beispiel: Zwei Autos treffen an einer engen Brücke aufeinander. Keiner kann weiterfahren, keiner will zurücksetzen. Beide warten darauf, dass der andere Platz macht. Ohne externe Intervention (etwa ein Verkehrspolizist) löst sich die Situation nie.

---

## Visualisierung

![[02-04-04-deadlock-cycle.png]]
*<span class="fig-id">02-04-04-deadlock-cycle</span>: Zyklische Wartesituation – Prozess A hält Ressource A und wartet auf Ressource B, während Prozess B Ressource B hält und auf Ressource A wartet.*

---

## Die vier Coffman-Bedingungen

1971 formalisierten Edward Coffman, Melanie Elphick und Arie Shoshani die notwendigen Bedingungen für Deadlocks. Diese "Coffman-Bedingungen" sind bis heute das Fundament der Deadlock-Theorie.

Ein Deadlock kann **nur** auftreten, wenn **alle vier** Bedingungen gleichzeitig erfüllt sind. Das ist entscheidend: Verhindere eine einzige Bedingung, und Deadlocks werden unmöglich.

| Bedingung | Englisch | Beschreibung |
|-----------|----------|--------------|
| **Gegenseitiger Ausschluss** | Mutual Exclusion | Ressourcen können nur von einem Prozess gleichzeitig genutzt werden |
| **Halten und Warten** | Hold and Wait | Ein Prozess hält Ressourcen und wartet auf weitere |
| **Keine Entziehbarkeit** | No Preemption | Ressourcen können nur freiwillig freigegeben werden |
| **Zyklisches Warten** | Circular Wait | Es existiert eine zyklische Kette wartender Prozesse |

### Warum alle vier?

Fehlt eine Bedingung, entsteht kein Deadlock:

- **Ohne Mutual Exclusion:** Alle könnten die Ressource gleichzeitig nutzen – kein Konflikt.
- **Ohne Hold and Wait:** Wer wartet, hält nichts – kein anderer wird blockiert.
- **Ohne No Preemption:** Man kann dem Blockierer seine Ressource wegnehmen – Kreislauf bricht.
- **Ohne Circular Wait:** Lineare Wartekette löst sich irgendwann auf.

---

## Strategien zur Deadlock-Behandlung

Es gibt vier grundlegend verschiedene Ansätze, mit Deadlocks umzugehen. Jeder hat seine Berechtigung, abhängig vom Kontext.

| Strategie | Englisch | Idee | Aufwand |
|-----------|----------|------|---------|
| **Vorbeugung** | Prevention | Eine Coffman-Bedingung strukturell verhindern | Hoch, aber garantiert |
| **Vermeidung** | Avoidance | Nur sichere Zustände zulassen | Hoch (Laufzeit-Check) |
| **Erkennung** | Detection | Deadlocks erkennen und reagieren | Mittel |
| **Ignorieren** | Ignorance | Hoffen, dass es nicht passiert | Niedrig |

---

### 1. Prevention (Vorbeugung)

Vorbeugung bedeutet, das System so zu gestalten, dass mindestens eine der vier Coffman-Bedingungen **strukturell unmöglich** ist. Das ist die radikalste, aber auch sicherste Methode.

| Bedingung | Maßnahme | Problem |
|-----------|----------|---------|
| **Mutual Exclusion** | Ressourcen teilbar machen (z.B. Spooling) | Meist nicht möglich (Drucker braucht exklusiven Zugriff) |
| **Hold and Wait** | Alle Ressourcen auf einmal anfordern | Ineffizient, kann zu Starvation führen |
| **No Preemption** | Ressourcen entziehbar machen | Nicht bei allen Ressourcen möglich (offene Datei?) |
| **Circular Wait** | Feste Nummerierung, nur aufsteigende Anforderungen | Funktioniert gut! Praktikabelste Lösung |

#### Beispiel: Ressourcen-Ordnung gegen Circular Wait

Die eleganteste Präventionsmethode: Alle Ressourcen erhalten eine eindeutige Nummer. Ein Prozess darf nur Ressourcen in **aufsteigender** Reihenfolge anfordern.

> [!example] **Ressourcen-Ordnung**
> Ressourcen-Nummern: R1=1, R2=2, R3=3, R4=4
> 
> | Prozess | Reihenfolge | Gültig? |
> |---------|-------------|---------|
> | A | R1 → R3 → R4 | ✓ (1 < 3 < 4) |
> | B | R2 → R4 | ✓ (2 < 4) |
> | C | R3 → R1 | ✗ (3 > 1) |
> 
> → Kein Zyklus möglich, da alle Pfeile in dieselbe Richtung zeigen

In der Praxis wird diese Methode häufig verwendet. Linux-Kernel-Entwickler nutzen "lock ordering" – wer mehrere Locks braucht, muss sie in einer definierten Reihenfolge anfordern.

---

### 2. Avoidance (Vermeidung) – Banker's Algorithm

Bei der Vermeidung werden alle vier Coffman-Bedingungen zugelassen, aber das System prüft **vor jeder Ressourcenzuteilung**, ob der resultierende Zustand noch "sicher" ist. Ist er es nicht, wird die Anforderung verzögert.

> [!quote] **Sicherer Zustand**
> Ein Zustand ist **sicher**, wenn es eine Reihenfolge gibt, in der alle Prozesse ihre maximalen Ressourcenanforderungen erfüllen und ihre Arbeit beenden können, ohne dass ein Deadlock entsteht.

Der **Banker's Algorithm** wurde 1965 von Dijkstra entwickelt. Der Name kommt von der Analogie zu einem vorsichtigen Bankier: Er vergibt nur dann einen Kredit, wenn er sicher ist, dass alle Kunden (auch im schlimmsten Fall) bedient werden können.

#### Beispiel: Banker's Algorithm

Ein System hat **10 Einheiten** einer Ressource. Drei Prozesse haben folgende Anforderungen:

| Prozess | Belegt | Maximum | Noch benötigt |
|---------|--------|---------|---------------|
| P1 | 2 | 5 | 3 |
| P2 | 3 | 9 | 6 |
| P3 | 2 | 4 | 2 |

**Verfügbar:** 10 - (2+3+2) = **3 Einheiten**

**Ist der Zustand sicher?** Wir suchen eine Sequenz, in der alle Prozesse fertig werden können:

1. **P3** braucht 2, wir haben 3 → P3 kann laufen
   - Nach P3: Verfügbar = 3 + 2 = **5**
2. **P1** braucht 3, wir haben 5 → P1 kann laufen
   - Nach P1: Verfügbar = 5 + 2 = **7**
3. **P2** braucht 6, wir haben 7 → P2 kann laufen ✓

**Sichere Sequenz:** P3 → P1 → P2

> [!warning] **Limitation**
> Der Banker's Algorithm erfordert, dass jeder Prozess seinen maximalen Bedarf im Voraus angibt. Das ist in der Praxis oft nicht möglich oder praktikabel.

---

### 3. Detection (Erkennung)

Bei dieser Strategie werden Deadlocks zugelassen – aber erkannt und behoben. Das System führt periodisch oder bei Verdacht einen Erkennungsalgorithmus aus.

#### Erkennung mit Resource Allocation Graph

Ein Resource Allocation Graph (RAG) visualisiert, welcher Prozess welche Ressource hält und welche er anfordert. Ein **Zyklus im Graphen** bedeutet einen potenziellen Deadlock.

**Legende:**
- Kreis (○) = Prozess
- Quadrat (□) = Ressource
- Pfeil Prozess → Ressource = "Prozess wartet auf diese Ressource"
- Pfeil Ressource → Prozess = "Ressource ist diesem Prozess zugeteilt"

> [!tip] **Zyklus-Erkennung**
> Bei **Single-Instance-Ressourcen** (nur ein Exemplar pro Typ) gilt: Zyklus = Deadlock.
> Bei **Multi-Instance-Ressourcen** ist ein Zyklus notwendig, aber nicht hinreichend.

#### Recovery (Behebung)

Wurde ein Deadlock erkannt, muss er behoben werden. Keine dieser Methoden ist elegant:

| Methode | Beschreibung | Nachteil |
|---------|--------------|----------|
| **Prozess abbrechen** | Einen oder mehrere Prozesse im Zyklus terminieren | Arbeit geht verloren |
| **Ressourcen entziehen** | Einem Prozess seine Ressource wegnehmen | Kann den Prozess beschädigen |
| **Rollback** | Prozess auf früheren Checkpoint zurücksetzen | Erfordert Checkpointing |

In der Praxis wird oft der "billigste" Prozess (wenig Laufzeit, wenig Ressourcen) zum Opfer.

---

### 4. Ignorance (Ignorieren) – Der Ostrich-Algorithmus

Der pragmatischste Ansatz: Deadlocks einfach ignorieren und hoffen, dass sie selten genug auftreten.

> [!note] **Praxis**
> Die meisten modernen Betriebssysteme (Linux, Windows, macOS) verwenden diesen Ansatz für Anwendungs-Deadlocks. Der Grund: Die Kosten für Prevention/Avoidance/Detection übersteigen oft den Nutzen.

**Wann ist Ignorieren akzeptabel?**
- Deadlocks treten extrem selten auf (z.B. einmal pro Monat)
- Die Kosten eines Deadlocks sind gering (Prozess kann neu gestartet werden)
- Die Kosten der Vermeidung wären unverhältnismäßig hoch

**Der Name "Ostrich Algorithm"** kommt von der (falschen) Annahme, dass Strauße bei Gefahr den Kopf in den Sand stecken. Die Idee: Wenn man das Problem nicht sieht, existiert es nicht.

> [!warning] **Nicht akzeptabel bei...**
> - Sicherheitskritischen Systemen (Flugzeuge, medizinische Geräte)
> - Systemen mit hohen Verfügbarkeitsanforderungen
> - Echtzeitsystemen

---

## Klassische Deadlock-Probleme

### Dining Philosophers (Philosophenproblem)

Das bekannteste Deadlock-Problem wurde 1965 von Dijkstra formuliert und später von Tony Hoare in die heute bekannte Form gebracht.

![[02-04-04-dining-philosophers.png]]
*<span class="fig-id">02-04-04-dining-philosophers</span>: Fünf Philosophen am runden Tisch – jeder braucht zwei Gabeln zum Essen, aber zwischen je zwei Philosophen liegt nur eine.*

**Das Szenario:** Fünf Philosophen sitzen an einem runden Tisch. Zwischen je zwei Philosophen liegt eine Gabel. Zum Essen braucht jeder Philosoph **zwei Gabeln** – die linke und die rechte. Die Philosophen denken und essen abwechselnd.

**Das Deadlock-Szenario:** Wenn alle fünf Philosophen gleichzeitig hungrig werden und jeder seine linke Gabel nimmt, hat keiner zwei Gabeln. Alle warten auf die rechte Gabel – die aber der rechte Nachbar hält. Deadlock.

**Lösungsansätze:**
1. **Ressourcen-Ordnung:** Gabeln nummerieren, immer die niedrigere zuerst nehmen
2. **Maximale Teilnehmerzahl:** Nur 4 Philosophen dürfen gleichzeitig versuchen zu essen
3. **Beide Gabeln atomar:** Nur beide Gabeln zusammen oder keine
4. **Asymmetrie:** Ein Philosoph nimmt zuerst die rechte Gabel

> [!example] **Warum ist dieses Problem wichtig?**
> Das Philosophenproblem ist eine Abstraktion realer Probleme: Datenbankzugriffe, Netzwerkprotokollen, oder jede Situation, in der mehrere Akteure mehrere Ressourcen benötigen.

---

## Zusammenhänge

- [[02-Kritische-Abschnitte|Kritische Abschnitte]] → Deadlocks entstehen bei Synchronisation
- [[03-Race-Conditions|Race Conditions]] → Anderes Problem, gleiche Ursache
- [[05-Synchronisationsmechanismen|Synchronisationsmechanismen]] → Falsche Nutzung → Deadlocks

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - Die vier Coffman-Bedingungen (auswendig!)
> - Unterschied Prevention, Avoidance, Detection, Ignorance
> - Banker's Algorithm verstehen und anwenden
> - Resource Allocation Graph interpretieren

> [!question] **Häufige Prüfungsfragen**
> 1. Nennen und erklären Sie die vier notwendigen Bedingungen für einen Deadlock!
> 2. Wie kann man Deadlocks durch Ressourcen-Ordnung verhindern?
> 3. Erklären Sie den Banker's Algorithm anhand eines Beispiels!
> 4. Gegeben ein Resource Allocation Graph: Liegt ein Deadlock vor?
> 5. Welche Strategien gibt es zur Behandlung von Deadlocks?

> [!tip] **Merkhilfen**
> - **4 Bedingungen**: "**M**u**H**-**N**o-**C**y" = **M**utual exclusion, **H**old&wait, **N**o preemption, **C**ircular wait
> - **Banker's Algorithm** = "Vorsichtiger Bankier gibt nur Kredit, wenn Rückzahlung sicher"
> - **Philosophen** = "Alle greifen gleichzeitig zur linken Gabel → keiner kann essen"
> - **Ostrich** = "Kopf in den Sand – wenn ich es nicht sehe, existiert es nicht"
> - **RAG-Zyklus** = "Jeder wartet auf den nächsten, der letzte auf den ersten"

---

## Weiterführende Ressourcen

> [!note] **Videos (YouTube)**
>
> | | Video | Beschreibung |
> |---|-------|--------------|
> | 🎬 | [CoreDumped – Concurrency](https://www.youtube.com/watch?v=3X93PnKRNUo) | Nebenläufigkeit und Deadlocks |

> [!note] **Workshop**
> - MOSS Deadlock Simulator: http://www.ontko.com/moss/deadlock/user_guide.html
> - Beispielcode: https://github.com/KR-Ravindra/Deadlock-Simulation

---

## Quellen

- IU Skript: Betriebssysteme, Rechnernetze und verteilte Systeme - Teil 5 (Ressourcen)
- Tanenbaum: Modern Operating Systems
- Coffman et al.: "System Deadlocks" (1971)
