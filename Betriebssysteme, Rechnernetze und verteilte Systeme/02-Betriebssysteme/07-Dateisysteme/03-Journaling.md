---
author: Andreas Hümmer
title: Journaling
tags:
  - content
  - bs
  - dateisystem
  - journaling
created: '2026-10-07'
modified: '2026-10-07'
bereich: BS
---

# Journaling

## Definition

Journaling-Dateisysteme protokollieren Änderungen in einem Journal, bevor sie auf das Dateisystem geschrieben werden.

## Erklärung

Das Journal ermöglicht schnelle Wiederherstellung nach Systemabstürzen. Bei einem Absturz werden unvollständige Transaktionen aus dem Journal wiederholt oder rückgängig gemacht. Varianten: Metadata-Only, Full Data Journaling.

## Eigenschaften

- Schnelle Recovery nach Absturz
- Transaktions-basierte Updates
- Write-Ahead-Logging
- Trade-off: Sicherheit vs. Performance

## Beispiele

- *Beispiel 1*

## Zusammenhänge

- [[Grundlagen]]
- [[Implementierung]]

## Prüfungstipps

- *Prüfungstipp 1*

## Quellen

- *Quelle 1*
