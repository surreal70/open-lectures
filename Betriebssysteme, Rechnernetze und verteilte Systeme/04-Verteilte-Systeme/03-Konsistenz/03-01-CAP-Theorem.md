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
modified: '2026-10-07'
bereich: VS
---
author: Andreas Hümmer

# CAP-Theorem

## Definition

Das CAP-Theorem besagt, dass ein verteiltes System höchstens zwei der drei Eigenschaften Konsistenz (C), Verfügbarkeit (A) und Partitionstoleranz (P) gleichzeitig garantieren kann.

## Erklärung

Eric Brewer formulierte das CAP-Theorem, das fundamentale Trade-offs in verteilten Systemen beschreibt. Bei Netzwerkpartitionen (P ist notwendig) muss zwischen starker Konsistenz (C) und Verfügbarkeit (A) gewählt werden. CP-Systeme opfern Verfügbarkeit, AP-Systeme akzeptieren eventuelle Konsistenz.

## Eigenschaften

- Consistency: Alle Knoten sehen gleiche Daten
- Availability: Jede Anfrage erhält eine Antwort
- Partition Tolerance: System funktioniert trotz Netzwerkpartitionen
- Trade-off zwischen CA, CP, AP
- In der Praxis ist P meist unverhandelbar

## Beispiele

- CP: HBase, MongoDB (im strict mode)
- AP: Cassandra, DynamoDB
- CA: Traditionelle RDBMS (ohne Verteilung)

## Zusammenhänge

- [[Konsistenzmodelle]]
- [[Replikation]]
- [[ACID]]

## Prüfungstipps

- CAP-Theorem formal erklären können
- Beispiele für CP und AP Systeme nennen
- PACELC als Erweiterung kennen

## Quellen

- *Quelle 1*
