---
author: Andreas Hümmer
title: CAP-Theorem
tags:
  - content
  - vs
  - konsistenz
  - cap
  - theorem
  - tradeoff
created: '2026-10-07'
modified: '2026-10-29'
bereich: VS
---

# CAP-Theorem

> [!info] Lernziele
> - CAP-Theorem und seine drei Eigenschaften verstehen
> - Trade-offs in verteilten Systemen erklären können
> - Praktische Systeme als CP oder AP klassifizieren
> - PACELC als Erweiterung kennen

## Einleitung

Das CAP-Theorem ist eines der fundamentalsten Konzepte in verteilten Systemen. Es beschreibt die unvermeidlichen Trade-offs, die Designer bei der Architektur verteilter Datenspeicher treffen müssen.

> [!important] Kernkonzept
> Das CAP-Theorem (Brewer, 2000) besagt: Ein verteiltes System kann höchstens **zwei** der drei Eigenschaften **Consistency** (C), **Availability** (A) und **Partition Tolerance** (P) gleichzeitig garantieren. Da Netzwerkpartitionen in der Praxis unvermeidlich sind, ist P meist unverhandelbar – die Wahl liegt zwischen C und A.

> [!example] Analogie
> Stell dir ein Filialnetz einer Bank vor: Bei einer Netzwerkstörung (Partition) zwischen Filialen kannst du entweder **Konsistenz** wahren (Kontostände werden eingefroren bis die Verbindung wiederhergestellt ist – keine Abhebungen möglich) oder **Verfügbarkeit** (Filialen arbeiten unabhängig weiter, aber Kontostände könnten temporär abweichen). Beides gleichzeitig ist unmöglich.

## Die drei CAP-Eigenschaften

### Consistency (Konsistenz)

> Alle Knoten sehen zur gleichen Zeit dieselben Daten.

- Jede Leseoperation liefert den Wert der letzten Schreiboperation
- Entspricht der **Linearisierbarkeit** in der Theorie
- Erfordert Koordination zwischen allen Knoten

### Availability (Verfügbarkeit)

> Jede Anfrage erhält eine (nicht-fehlerhafte) Antwort – ohne Garantie auf Aktualität.

- Keine Anfrage bleibt unbeantwortet
- System antwortet auch bei Teilausfällen
- Antwort muss korrekt sein (keine Fehlermeldung)

### Partition Tolerance (Partitionstoleranz)

> Das System arbeitet trotz Nachrichtenverlust oder Netzwerkpartitionen weiter.

- Kommunikation zwischen Knoten kann unterbrochen sein
- System muss trotzdem funktionsfähig bleiben
- In verteilten Systemen praktisch unvermeidlich

## CAP-Trade-offs

![[cap-dreieck.png]]
*<span class="fig-id">04-03-01-cap-dreieck</span>: Das CAP-Dreieck zeigt die Trade-offs in verteilten Systemen.*

### Systemklassifikation

| Klasse | Eigenschaften | Verhalten bei Partition | Beispiele |
|--------|---------------|------------------------|-----------|
| **CP** | Consistency + Partition Tolerance | Opfert Verfügbarkeit | HBase, MongoDB (strict), ZooKeeper |
| **AP** | Availability + Partition Tolerance | Opfert Konsistenz | Cassandra, DynamoDB, CouchDB |
| **CA** | Consistency + Availability | Nicht partitionstolerant | Traditionelle RDBMS (single-node) |

> [!warning] Wichtig
> CA-Systeme existieren praktisch nicht in verteilten Umgebungen, da Netzwerkpartitionen nicht ausgeschlossen werden können. Die reale Wahl liegt zwischen CP und AP.

## PACELC-Erweiterung

Das PACELC-Theorem erweitert CAP um das Verhalten im Normalfall (ohne Partition):

> **P**artition → **A**vailability vs. **C**onsistency  
> **E**lse → **L**atency vs. **C**onsistency

| System | Partition | Else (Normal) |
|--------|-----------|---------------|
| Cassandra | AP | EL (niedrige Latenz, eventual consistent) |
| MongoDB | CP | EC (Konsistenz vor Latenz) |
| DynamoDB | AP | EC oder EL (konfigurierbar) |

## Zusammenhänge

| Thema | Beziehung | Verweis |
|-------|-----------|---------|
| PACELC | erweitert CAP-Theorem | [[02-Konsistenzmodelle]] |
| Konsistenzmodelle | werden durch CAP beeinflusst | [[02-Konsistenzmodelle]] |
| Replikationsstrategien | werden durch CAP bestimmt | [[03-Replikation]] |
| ACID-Transaktionen | stehen im Gegensatz zu CAP | [[02-Konsistenzmodelle#ACID-Eigenschaften]] |
| BASE | relaxierte Alternative zu ACID | [[02-Konsistenzmodelle#BASE als Alternative zu ACID]] |

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
NA

> [!question] Verständnisfragen
> - Was passiert bei einem CP-System während einer Partition?
> - Wie verhält sich ein AP-System bei Netzwerkausfällen?
> - Was bedeutet PACELC und wie erweitert es CAP?

> [!tip] Merkhilfe
> **CAP = "Choose Any Pair"**:
> - **C**onsistency: Alle sehen das Gleiche
> - **A**vailability: Alle bekommen Antwort
> - **P**artition Tolerance: Funktioniert trotz Netzausfall
> 
> Bei Partition (unvermeidlich): CP = "Lieber nichts als Falsches", AP = "Lieber was als nichts"

---

> [!tip] **Weiterführende Ressourcen**
> - [[02-Konsistenzmodelle]] – Verschiedene Konsistenzstufen
> - [[03-Replikation]] – Replikationsstrategien
> - [[../01-Grundlagen/02-Eigenschaften]] – ACID-Eigenschaften

---

## Quellen

- Brewer, Eric: Towards Robust Distributed Systems, Keynote PODC, 2000
- Gilbert, Seth & Lynch, Nancy: Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services, ACM SIGACT News, 2002
