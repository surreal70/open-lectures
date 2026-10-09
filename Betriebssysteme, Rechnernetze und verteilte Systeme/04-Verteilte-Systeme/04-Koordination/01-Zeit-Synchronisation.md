---
author: Andreas Hümmer
title: Zeit-Synchronisation
tags:
  - content
  - vs
  - koordination
  - zeit
  - ntp
  - synchronisation
created: '2026-10-07'
modified: '2026-10-07'
bereich: VS
---

# Zeit-Synchronisation

## Definition

Zeit-Synchronisation in verteilten Systemen befasst sich mit der Koordination von Uhren zwischen verschiedenen Knoten.

## Erklärung

Da physikalische Uhren driften, benötigen verteilte Systeme Mechanismen zur Zeitsynchronisation. NTP synchronisiert Uhren mit Zeitservern, erreicht aber nur begrenzte Genauigkeit. Für strikte Ordnung werden oft logische Uhren bevorzugt.

## Eigenschaften

- Physikalische Uhren driften (Quarz-Ungenauigkeit)
- NTP für Internet-Zeitsynchronisation
- Precision Time Protocol (PTP) für höhere Genauigkeit
- GPS-basierte Synchronisation möglich
- Begrenzte Genauigkeit in WANs

## Beispiele

- NTP-Server-Hierarchie (Stratum)
- Google TrueTime mit GPS und Atomuhren
- PTP in Rechenzentren

## Zusammenhänge

- [[Logische-Uhren]]
- [[Konsensalgorithmen]]
- [[CAP-Theorem]]

## Prüfungstipps

- NTP-Funktionsweise erklären
- Cristians Algorithmus verstehen
- Berkeley-Algorithmus kennen

## Quellen

- *Quelle 1*
