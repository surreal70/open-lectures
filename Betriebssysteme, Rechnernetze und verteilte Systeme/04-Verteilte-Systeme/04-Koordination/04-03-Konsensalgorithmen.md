---
author: Andreas Hümmer
title: Konsensalgorithmen
tags:
  - content
- vs
- koordination
- konsens
- paxos
- raft
created: '2026-10-07'
modified: '2026-10-07'
bereich: VS
---
author: Andreas Hümmer

# Konsensalgorithmen

## Definition

Konsensalgorithmen ermöglichen es verteilten Systemen, sich auf einen gemeinsamen Wert oder eine Entscheidung zu einigen, selbst bei Ausfällen.

## Erklärung

Das Konsensproblem ist fundamental für verteilte Systeme. Paxos und Raft sind bekannte Algorithmen, die Konsens auch bei Knotenausfällen erreichen (aber nicht bei byzantinischen Fehlern ohne zusätzliche Mechanismen). Sie werden für Leader Election, replizierte State Machines und verteilte Datenbanken eingesetzt.

## Eigenschaften

- Agreement: Alle korrekten Prozesse einigen sich
- Validity: Der Wert wurde von einem Prozess vorgeschlagen
- Termination: Alle korrekten Prozesse entscheiden
- FLP-Unmöglichkeit bei asynchronen Systemen
- Benötigt Mehrheit korrekter Knoten (2f+1 für f Fehler)

## Beispiele

- Paxos in Google Chubby/Spanner
- Raft in etcd, CockroachDB
- ZAB in Apache ZooKeeper
- PBFT für byzantinische Fehlertoleranz

## Zusammenhänge

- [[Logische-Uhren]]
- [[Zeit-Synchronisation]]
- [[Replikation]]

## Prüfungstipps

- Paxos-Phasen erklären können
- Raft-Leader-Election verstehen
- FLP-Theorem kennen
- Unterschied Crash- vs. byzantinische Fehler

## Quellen

- *Quelle 1*
