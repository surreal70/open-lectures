---
author: Andreas Hümmer
title: 'Übung: Verteilte Systeme (Klausurformat)'
tags:
  - uebung
  - vs
  - klausur
  - definition
  - kommunikation
  - konsistenz
  - koordination
  - cap
  - rpc
  - rest
punkte_gesamt: 115
bearbeitungszeit: 180
bereich: VS
created: '2026-11-01'
modified: '2026-11-01'
---

# Übung: Verteilte Systeme (Klausurformat)

**Bereich:** VS – Alle Kapitel
**Gesamtpunktzahl:** 115 Punkte
**Bearbeitungszeit:** ca. 180 Minuten

---

> [!info] **Themenübersicht**
> Diese Übung deckt die zentralen Themen des Moduls Verteilte Systeme ab:
> - Teil 1: Grundlagen und Definition (20 Punkte)
> - Teil 2: Kommunikation in Verteilten Systemen (25 Punkte)
> - Teil 3: CAP-Theorem und Konsistenz (25 Punkte)
> - Teil 4: Replikation (15 Punkte)
> - Teil 5: Koordination und Uhren (15 Punkte)
> - Teil 6: Konsensalgorithmen (15 Punkte)

---

## Teil 1: Grundlagen und Definition (20 Punkte)

### Aufgabe 1.1: Definitionen verteilter Systeme (6 Punkte) ⭐

a) **Nennen Sie die Definition eines verteilten Systems nach Tanenbaum.** (2 Punkte)

_Deine Antwort:_

<br><br><br>

b) **Erklären Sie die Definitionen nach Bal und Lamport und deren Kernaussagen.** (4 Punkte)

| Autor | Definition/Kernaussage |
|-------|------------------------|
| Bal | |
| Lamport | |

---

### Aufgabe 1.2: Die vier Hauptmerkmale (5 Punkte) ⭐

**Nennen Sie die vier Hauptmerkmale verteilter Systeme und beschreiben Sie jeweils kurz deren Bedeutung.**

| Merkmal | Beschreibung |
|---------|--------------|
| 1. | |
| 2. | |
| 3. | |
| 4. | |

---

### Aufgabe 1.3: Distributed vs. Parallel Computing (5 Punkte) ⭐⭐

**Erklären Sie den Unterschied zwischen Distributed Computing und Parallel Computing anhand der folgenden Kriterien.**

| Kriterium | Distributed Computing | Parallel Computing |
|-----------|----------------------|-------------------|
| Kopplung | | |
| Speicher | | |
| Kommunikation | | |

---

### Aufgabe 1.4: Fat-Client vs. Thin-Client (4 Punkte) ⭐⭐

**Vergleichen Sie Fat-Client und Thin-Client Architekturen.**

| Aspekt | Fat-Client | Thin-Client |
|--------|------------|-------------|
| Logik | | |
| Wartung | | |
| Offline-Fähigkeit | | |
| Beispiel | | |

---

## Teil 2: Kommunikation in Verteilten Systemen (25 Punkte)

### Aufgabe 2.1: RPC-Ablauf (5 Punkte) ⭐⭐

**Beschreiben Sie den Ablauf eines Remote Procedure Calls (RPC) in der richtigen Reihenfolge.**

| Schritt | Beschreibung |
|---------|--------------|
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |

---

### Aufgabe 2.2: Idempotenz (4 Punkte) ⭐⭐

a) **Was bedeutet Idempotenz im Kontext von RPC?** (2 Punkte)

_Deine Antwort:_

<br><br><br>

b) **Ordnen Sie die folgenden Operationen als idempotent oder nicht-idempotent ein.** (2 Punkte)

| Operation | Idempotent? (Ja/Nein) | Begründung |
|-----------|----------------------|------------|
| GET /user/123 | | |
| balance += 10 | | |
| DELETE /user/123 | | |
| POST /orders | | |

---

### Aufgabe 2.3: HTTP-Methoden und REST (5 Punkte) ⭐

**Erklären Sie die folgenden HTTP-Methoden und deren Semantik im REST-Kontext.**

| Methode | Beschreibung | Idempotent? |
|---------|--------------|-------------|
| GET | | |
| POST | | |
| PUT | | |
| DELETE | | |
| PATCH | | |

---

### Aufgabe 2.4: REST vs. SOAP (5 Punkte) ⭐⭐

**Vergleichen Sie REST und SOAP anhand der folgenden Kriterien.**

| Kriterium | REST | SOAP |
|-----------|------|------|
| Typ | | |
| Format | | |
| Bandbreite/Overhead | | |
| Sicherheit | | |
| Caching | | |

---

### Aufgabe 2.5: SOA-Dreiecksmodell (3 Punkte) ⭐

**Erklären Sie die drei Komponenten des SOA-Dreiecksmodells und deren Aufgaben.**

| Komponente | Aufgabe |
|------------|---------|
| Service Provider | |
| Service Registry | |
| Service Consumer | |

---

### Aufgabe 2.6: Synchrone vs. Asynchrone Kommunikation (3 Punkte) ⭐⭐

**Erklären Sie den Unterschied zwischen synchroner und asynchroner Kommunikation in verteilten Systemen.**

| Aspekt | Synchron (z.B. RPC) | Asynchron (z.B. Message Queue) |
|--------|---------------------|-------------------------------|
| Blockierung | | |
| Kopplung | | |
| Anwendungsfall | | |

---

## Teil 3: CAP-Theorem und Konsistenz (25 Punkte)

### Aufgabe 3.1: CAP-Theorem (6 Punkte) ⭐

**Erklären Sie die drei Eigenschaften des CAP-Theorems.**

| Eigenschaft | Erklärung |
|-------------|-----------|
| **C**onsistency | |
| **A**vailability | |
| **P**artition Tolerance | |

---

### Aufgabe 3.2: CP vs. AP Systeme (5 Punkte) ⭐⭐

a) **Was bedeutet es, wenn ein System als "CP" klassifiziert wird?** (2 Punkte)

_Deine Antwort:_

<br><br><br>

b) **Ordnen Sie die folgenden Systeme als CP oder AP ein und begründen Sie kurz.** (3 Punkte)

| System | CP oder AP? | Begründung |
|--------|-------------|------------|
| ZooKeeper | | |
| Cassandra | | |
| MongoDB (strict mode) | | |

---

### Aufgabe 3.3: ACID-Eigenschaften (4 Punkte) ⭐

**Erklären Sie die vier ACID-Eigenschaften für Datenbanktransaktionen.**

| Eigenschaft | Beschreibung |
|-------------|--------------|
| **A**tomicity | |
| **C**onsistency | |
| **I**solation | |
| **D**urability | |

---

### Aufgabe 3.4: Strong vs. Eventual Consistency (5 Punkte) ⭐⭐

**Vergleichen Sie Strong Consistency und Eventual Consistency.**

| Aspekt | Strong Consistency | Eventual Consistency |
|--------|-------------------|---------------------|
| Garantie | | |
| Latenz | | |
| Verfügbarkeit bei Partition | | |
| Anwendungsbeispiel | | |

---

### Aufgabe 3.5: Quorum-Berechnung (5 Punkte) ⭐⭐⭐

**Gegeben ist ein System mit N=5 Replikaten.**

a) **Was garantiert die Quorum-Formel R + W > N?** (2 Punkte)

_Deine Antwort:_

<br><br><br>

b) **Berechnen Sie, ob die folgenden Konfigurationen Konsistenz garantieren.** (3 Punkte)

| Konfiguration | W | R | R + W | > N? | Konsistent? |
|---------------|---|---|-------|------|-------------|
| Write-optimiert | 1 | 5 | | | |
| Read-optimiert | 5 | 1 | | | |
| Balanced | 3 | 3 | | | |

---

## Teil 4: Replikation (15 Punkte)

### Aufgabe 4.1: Synchrone vs. Asynchrone Replikation (5 Punkte) ⭐⭐

**Vergleichen Sie synchrone und asynchrone Replikation.**

| Aspekt | Synchron | Asynchron |
|--------|----------|-----------|
| Latenz | | |
| Konsistenz | | |
| Verfügbarkeit bei Ausfällen | | |
| Datenverlustrisiko bei Failover | | |

---

### Aufgabe 4.2: Primary-Backup vs. Multi-Primary (5 Punkte) ⭐⭐

**Erklären Sie die beiden Replikationsarchitekturen.**

| Aspekt | Primary-Backup | Multi-Primary |
|--------|----------------|---------------|
| Schreiboperationen | | |
| Vorteil | | |
| Nachteil | | |

---

### Aufgabe 4.3: Vor- und Nachteile der Replikation (5 Punkte) ⭐

**Nennen Sie jeweils zwei Vorteile und zwei Nachteile der Replikation.**

| | Replikation |
|---|-------------|
| **Vorteile** | 1. |
| | 2. |
| **Nachteile** | 1. |
| | 2. |

---

## Teil 5: Koordination und Uhren (15 Punkte)

### Aufgabe 5.1: Externe vs. Interne Synchronisation (3 Punkte) ⭐⭐

**Erklären Sie den Unterschied zwischen externer und interner Zeitsynchronisation.**

| Typ | Ziel | Beispiel |
|-----|------|----------|
| Extern | | |
| Intern | | |

---

### Aufgabe 5.2: Lamport-Uhren (5 Punkte) ⭐⭐

a) **Nennen Sie die Regeln für Lamport-Uhren.** (3 Punkte)

| Situation | Regel |
|-----------|-------|
| Lokales Ereignis | |
| Senden einer Nachricht | |
| Empfangen einer Nachricht mit Zeitstempel T | |

b) **Was ist die Hauptlimitation von Lamport-Uhren?** (2 Punkte)

_Deine Antwort:_

<br><br><br>

---

### Aufgabe 5.3: Happened-Before Relation (4 Punkte) ⭐⭐

a) **Definieren Sie die Happened-Before Relation (→).** (2 Punkte)

_Deine Antwort:_

<br><br><br>

b) **Wann sind zwei Ereignisse nebenläufig (concurrent)?** (2 Punkte)

_Deine Antwort:_

<br><br><br>

---

### Aufgabe 5.4: Lamport-Uhren vs. Vektoruhren (3 Punkte) ⭐⭐

**Vergleichen Sie Lamport-Uhren und Vektoruhren.**

| Aspekt | Lamport-Uhren | Vektoruhren |
|--------|---------------|-------------|
| Speicherbedarf | | |
| Erkennt a → b | | |
| Erkennt Nebenläufigkeit | | |

---

## Teil 6: Konsensalgorithmen (15 Punkte)

### Aufgabe 6.1: Konsensproblem (4 Punkte) ⭐

**Nennen Sie die vier Anforderungen an einen Konsensalgorithmus.**

| Anforderung | Beschreibung |
|-------------|--------------|
| Agreement | |
| Validity | |
| Termination | |
| Integrity | |

---

### Aufgabe 6.2: Paxos-Algorithmus (5 Punkte) ⭐⭐⭐

a) **Nennen Sie die drei Rollen im Paxos-Algorithmus und deren Aufgaben.** (3 Punkte)

| Rolle | Aufgabe |
|-------|---------|
| Proposer | |
| Acceptor | |
| Learner | |

b) **Beschreiben Sie kurz den 2-Phasen-Ablauf von Paxos.** (2 Punkte)

| Phase | Beschreibung |
|-------|--------------|
| Phase 1 (Prepare/Promise) | |
| Phase 2 (Accept/Accepted) | |

---

### Aufgabe 6.3: Raft-Algorithmus (4 Punkte) ⭐⭐

**Erklären Sie die drei Rollen im Raft-Algorithmus und deren Zustandsübergänge.**

| Rolle | Beschreibung | Wann Übergang? |
|-------|--------------|----------------|
| Follower | | |
| Candidate | | |
| Leader | | |

---

### Aufgabe 6.4: FLP-Theorem (2 Punkte) ⭐⭐

**Was besagt das FLP-Unmöglichkeitstheorem und welche praktische Konsequenz hat es?**

_Deine Antwort:_

<br><br><br>

---

## Selbsteinschätzung

Nach Bearbeitung der Aufgaben:

| Thema | Sicher | Unsicher | Muss wiederholen |
|-------|:------:|:--------:|:----------------:|
| Definition/Merkmale VS | ☐ | ☐ | ☐ |
| Fat/Thin Client | ☐ | ☐ | ☐ |
| RPC | ☐ | ☐ | ☐ |
| REST/SOAP | ☐ | ☐ | ☐ |
| SOA | ☐ | ☐ | ☐ |
| CAP-Theorem | ☐ | ☐ | ☐ |
| ACID | ☐ | ☐ | ☐ |
| Konsistenzmodelle | ☐ | ☐ | ☐ |
| Replikation/Quorum | ☐ | ☐ | ☐ |
| Zeitsynchronisation | ☐ | ☐ | ☐ |
| Lamport-/Vektoruhren | ☐ | ☐ | ☐ |
| Konsensalgorithmen | ☐ | ☐ | ☐ |

---

## Quellen

### Grundlagen
- [[01-Definition|Definition verteilter Systeme]]
- [[02-Eigenschaften|Eigenschaften verteilter Systeme]]

### Kommunikation
- [[01-RPC|Remote Procedure Call (RPC)]]
- [[03-REST|REST (Representational State Transfer)]]
- [[04-SOAP|SOAP (Simple Object Access Protocol)]]
- [[05-SOA|Service-orientierte Architektur (SOA)]]

### Konsistenz
- [[01-CAP-Theorem|CAP-Theorem]]
- [[02-Konsistenzmodelle|Konsistenzmodelle]]
- [[03-Replikation|Replikation]]

### Koordination
- [[01-Zeit-Synchronisation|Zeit-Synchronisation]]
- [[02-Logische-Uhren|Logische Uhren]]
- [[03-Konsensalgorithmen|Konsensalgorithmen]]

