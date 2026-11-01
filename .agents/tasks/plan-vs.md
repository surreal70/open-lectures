# Plan: Übungsaufgaben Verteilte Systeme (UE-VS)

**Erstellt:** 2025-01-30
**Autor:** Andreas Hümmer
**Gesamtpunktzahl:** ~115 Punkte
**Bearbeitungszeit:** ca. 180 Minuten

---

## 1. Abzudeckende Hauptthemen

Basierend auf dem Verzeichnis `/04-Verteilte-Systeme/` werden folgende Kapitel abgedeckt:

| Teil | Themenbereich | Quelle |
|------|---------------|--------|
| 1 | Grundlagen & Definition | 01-Grundlagen/ |
| 2 | Kommunikation (RPC, REST, SOAP, SOA) | 02-Kommunikation/ |
| 3 | Konsistenz (CAP, Modelle) | 03-Konsistenz/ |
| 4 | Koordination (Uhren, Konsens) | 04-Koordination/ |

---

## 2. Geplante Aufgabenstruktur

### Teil 1: Grundlagen und Definition (20 Punkte)

| Nr. | Aufgabe | Typ | ⭐ | Punkte |
|-----|---------|-----|---|--------|
| 1.1 | Definition nach Tanenbaum, Bal, Lamport | Definition | ⭐ | 6 |
| 1.2 | Distributed vs. Parallel Computing: Unterschiede (Speicher, Kopplung, Kommunikation) | Verständnis | ⭐⭐ | 5 |
| 1.3 | Die 4 Hauptmerkmale verteilter Systeme (Skalierbarkeit, Nebenläufigkeit, Fehlertoleranz, Transparenz) | Definition | ⭐ | 5 |
| 1.4 | Fat-Client vs. Thin-Client: Vergleichstabelle | Anwendung | ⭐⭐ | 4 |

**Inhalte aus:** 01-Definition.md, 02-Eigenschaften.md, 03-Fallacies.md

---

### Teil 2: Die 8 Fallacies of Distributed Computing (15 Punkte)

| Nr. | Aufgabe | Typ | ⭐ | Punkte |
|-----|---------|-----|---|--------|
| 2.1 | Nennen Sie alle 8 Fallacies | Definition | ⭐ | 4 |
| 2.2 | Zu 4 Fallacies jeweils: Realität und eine Gegenmaßnahme | Verständnis | ⭐⭐ | 8 |
| 2.3 | Praxisbeispiel: Welche Fallacy ist verletzt? (Szenario-Analyse) | Anwendung | ⭐⭐ | 3 |

**Inhalte aus:** 03-Fallacies.md

---

### Teil 3: Kommunikation in Verteilten Systemen (25 Punkte)

| Nr. | Aufgabe | Typ | ⭐ | Punkte |
|-----|---------|-----|---|--------|
| 3.1 | RPC: Ablauf eines RPC-Aufrufs mit 5-7 Schritten | Verständnis | ⭐⭐ | 5 |
| 3.2 | Idempotenz: Definition + Beispiele idempotent/nicht-idempotent | Verständnis | ⭐⭐ | 4 |
| 3.3 | REST: HTTP-Methoden und Semantik (GET, POST, PUT, DELETE, PATCH) | Definition | ⭐ | 5 |
| 3.4 | REST vs. SOAP: Vergleichstabelle (Typ, Format, Bandbreite, Sicherheit) | Verständnis | ⭐⭐ | 5 |
| 3.5 | SOA-Dreiecksmodell: Provider, Registry, Consumer erklären | Definition | ⭐ | 3 |
| 3.6 | Synchron vs. Asynchron: Unterschiede (Message Queues vs. RPC) | Verständnis | ⭐⭐ | 3 |

**Inhalte aus:** 01-RPC.md, 02-Message-Queues.md, 03-REST.md, 04-SOAP.md, 05-SOA.md

---

### Teil 4: CAP-Theorem und Konsistenz (25 Punkte)

| Nr. | Aufgabe | Typ | ⭐ | Punkte |
|-----|---------|-----|---|--------|
| 4.1 | CAP-Theorem: Die 3 Eigenschaften erklären (C, A, P) | Definition | ⭐ | 6 |
| 4.2 | CP vs. AP: Verhalten bei Netzwerkpartition + Beispielsysteme | Verständnis | ⭐⭐ | 5 |
| 4.3 | ACID-Eigenschaften erklären (Atomarität, Konsistenz, Isolation, Dauerhaftigkeit) | Definition | ⭐ | 4 |
| 4.4 | Strong vs. Eventual Consistency: Unterschiede + Anwendungsfälle | Verständnis | ⭐⭐ | 5 |
| 4.5 | Quorum-Formel: R + W > N erklären + Beispielberechnung | Anwendung | ⭐⭐⭐ | 5 |

**Inhalte aus:** 01-CAP-Theorem.md, 02-Konsistenzmodelle.md, 03-Replikation.md

---

### Teil 5: Koordination und Uhren (15 Punkte)

| Nr. | Aufgabe | Typ | ⭐ | Punkte |
|-----|---------|-----|---|--------|
| 5.1 | Lamport-Uhren: Regeln und Beispielberechnung | Verständnis | ⭐⭐ | 5 |
| 5.2 | Happened-Before-Relation: Definition + Nebenläufigkeit erklären | Definition | ⭐⭐ | 4 |
| 5.3 | Externe vs. Interne Synchronisation: Unterschied + Beispiele (NTP, Berkeley) | Verständnis | ⭐⭐ | 3 |
| 5.4 | Vektoruhren vs. Lamport-Uhren: Vergleich (Erkennung Nebenläufigkeit) | Verständnis | ⭐⭐ | 3 |

**Inhalte aus:** 01-Zeit-Synchronisation.md, 02-Logische-Uhren.md

---

### Teil 6: Konsensalgorithmen (15 Punkte)

| Nr. | Aufgabe | Typ | ⭐ | Punkte |
|-----|---------|-----|---|--------|
| 6.1 | Konsensproblem: Die 4 Anforderungen (Agreement, Validity, Termination, Integrity) | Definition | ⭐ | 4 |
| 6.2 | Paxos: Rollen (Proposer, Acceptor, Learner) und 2-Phasen-Ablauf | Verständnis | ⭐⭐⭐ | 5 |
| 6.3 | Raft: Rollen (Leader, Follower, Candidate) und Leader Election | Verständnis | ⭐⭐ | 4 |
| 6.4 | FLP-Theorem: Aussage und praktische Konsequenz | Definition | ⭐⭐ | 2 |

**Inhalte aus:** 03-Konsensalgorithmen.md

---

## 3. Punkteverteilung nach Schwierigkeit

| Schwierigkeit | Punkte | Anteil |
|---------------|--------|--------|
| ⭐ (leicht) | ~37 | ~32% |
| ⭐⭐ (mittel) | ~63 | ~55% |
| ⭐⭐⭐ (schwer) | ~15 | ~13% |
| **Gesamt** | **~115** | 100% |

---

## 4. Verifizierte Quellen-Wiki-Links

Die folgenden Dateinamen existieren und können als Wiki-Links verwendet werden:

### Grundlagen
- `[[01-Definition|Definition verteilter Systeme]]`
- `[[02-Eigenschaften|Eigenschaften verteilter Systeme]]`
- `[[03-Fallacies|Die 8 Fallacies of Distributed Computing]]`

### Kommunikation
- `[[01-RPC|Remote Procedure Call (RPC)]]`
- `[[02-Message-Queues|Message Queues]]`
- `[[03-REST|REST (Representational State Transfer)]]`
- `[[04-SOAP|SOAP (Simple Object Access Protocol)]]`
- `[[05-SOA|Service-orientierte Architektur (SOA)]]`
- `[[06-gRPC|gRPC]]`
- `[[07-GraphQL|GraphQL]]`
- `[[08-WebSockets|WebSockets]]`

### Konsistenz
- `[[01-CAP-Theorem|CAP-Theorem]]`
- `[[02-Konsistenzmodelle|Konsistenzmodelle]]`
- `[[03-Replikation|Replikation]]`

### Koordination
- `[[01-Zeit-Synchronisation|Zeit-Synchronisation]]`
- `[[02-Logische-Uhren|Logische Uhren]]`
- `[[03-Konsensalgorithmen|Konsensalgorithmen]]`

---

## 5. Selbsteinschätzungs-Themen (für Tabelle am Ende)

1. Definition/Merkmale VS
2. Fallacies
3. RPC
4. REST/SOAP
5. SOA
6. CAP-Theorem
7. ACID
8. Konsistenzmodelle
9. Replikation/Quorum
10. Lamport-Uhren
11. Vektoruhren
12. Konsensalgorithmen

---

## 6. Hinweise zur Implementierung

- **Prüfungsrelevanz beachten:** Einige Themen (Fallacies, Message Queues, Logische Uhren, Konsensalgorithmen, Replikation) sind laut Vorlesungsnotizen als "NA" (nicht prüfungsrelevant) markiert. Dennoch können sie für das Verständnis abgefragt werden.
- **Format exakt einhalten:** YAML-Frontmatter, Callout-Struktur, Tabellenformate wie in UE-BS-Betriebssysteme.md
- **Punkteverteilung:** Gesamtsumme ~115 Punkte (Vorlage BS hatte 120 Punkte)
- **Bearbeitungszeit:** 180 Minuten wie in der Vorlage
