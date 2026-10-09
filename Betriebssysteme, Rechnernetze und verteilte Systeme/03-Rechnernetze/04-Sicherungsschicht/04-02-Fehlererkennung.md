---
author: Andreas Hümmer
title: Fehlererkennung
tags:
  - content
- rn
- data-link
- fehlererkennung
- crc
- checksum
created: '2026-10-07'
modified: '2026-10-07'
bereich: RN
---
author: Andreas Hümmer

# Fehlererkennung

## Definition

Fehlererkennung ermöglicht das Identifizieren von Übertragungsfehlern in empfangenen Daten.

## Erklärung

Bei der Datenübertragung können durch Störungen Bitfehler auftreten. Verfahren wie Paritätsprüfung, Checksummen und CRC (Cyclic Redundancy Check) ermöglichen die Erkennung solcher Fehler.

## Eigenschaften

- Paritätsbit: Einfach, erkennt einzelne Bitfehler
- Checksumme: Summe aller Bytes
- CRC: Polynomielle Division, sehr zuverlässig
- Hamming-Distanz bestimmt Erkennungsfähigkeit

## Beispiele

- CRC-32 bei Ethernet
- Internet-Checksumme bei IP/UDP/TCP
- Hamming-Code für Fehlerkorrektur

## Zusammenhänge

- [[Rahmenbildung]]
- [[MAC-Protokolle]]

## Prüfungstipps

- Funktionsweise von CRC verstehen
- Unterschied Fehlererkennung vs. Fehlerkorrektur

## Quellen

- *Quelle 1*
