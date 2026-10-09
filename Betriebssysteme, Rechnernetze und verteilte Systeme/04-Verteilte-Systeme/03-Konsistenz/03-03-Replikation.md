---
author: Andreas Hümmer
title: Replikation
tags:
  - content
- vs
- konsistenz
- replikation
- redundanz
created: '2026-10-07'
modified: '2026-10-07'
bereich: VS
---
author: Andreas Hümmer

# Replikation

## Definition

Replikation ist das Speichern von Kopien derselben Daten auf mehreren Knoten eines verteilten Systems zur Erhöhung von Verfügbarkeit und Performance.

## Erklärung

Replikationsstrategien unterscheiden sich in der Konsistenzgarantie und Performance. Synchrone Replikation wartet auf Bestätigung aller Replikate, asynchrone nicht. Primary-Backup, Multi-Primary und Quorum-basierte Ansätze bieten verschiedene Trade-offs.

## Eigenschaften

- Erhöhte Verfügbarkeit durch Redundanz
- Bessere Leseperformance durch lokale Kopien
- Synchrone vs. asynchrone Replikation
- Primary-Backup vs. Multi-Primary
- Quorum-basierte Replikation (R + W > N)

## Beispiele

- MySQL Replication (Primary-Backup)
- Cassandra (Multi-Primary mit Quorum)
- ZooKeeper (Zab Protokoll)

## Zusammenhänge

- [[CAP-Theorem]]
- [[Konsistenzmodelle]]
- [[Koordination]]

## Prüfungstipps

- Synchrone vs. asynchrone Replikation vergleichen
- Quorum-Formel (R + W > N) erklären
- Vor- und Nachteile von Replikation

## Quellen

- *Quelle 1*
