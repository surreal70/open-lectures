---
author: Andreas Hümmer
title: Logische-Uhren
tags:
  - content
- vs
- koordination
- logische-uhren
- lamport
- vektor
created: '2026-10-07'
modified: '2026-10-07'
bereich: VS
---
author: Andreas Hümmer

# Logische-Uhren

## Definition

Logische Uhren sind Mechanismen zur Ordnung von Ereignissen in verteilten Systemen ohne Bezug auf physikalische Zeit.

## Erklärung

Lamport-Uhren und Vektoruhren ermöglichen die Bestimmung der kausalen Reihenfolge von Ereignissen. Lamport-Uhren liefern eine partielle Ordnung (a happened-before b), Vektoruhren können auch Nebenläufigkeit erkennen.

## Eigenschaften

- Lamport-Uhren: Einzelner Zähler pro Prozess
- Happened-before Relation (→)
- Vektoruhren: Vektor mit Zähler pro Prozess
- Erkennung von kausaler Abhängigkeit
- Erkennung von Nebenläufigkeit (mit Vektoruhren)

## Beispiele

- Lamport-Uhren in Mutex-Algorithmen
- Vektoruhren in Amazon Dynamo
- Hybrid Logical Clocks (HLC)

## Zusammenhänge

- [[Zeit-Synchronisation]]
- [[Konsensalgorithmen]]
- [[Konsistenzmodelle]]

## Prüfungstipps

- Lamport-Uhr-Regeln anwenden können
- Vektoruhren vergleichen können
- Happened-before Relation formal definieren

## Quellen

- *Quelle 1*
