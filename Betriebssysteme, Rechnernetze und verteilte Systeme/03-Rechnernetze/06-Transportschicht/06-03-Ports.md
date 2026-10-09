---
author: Andreas Hümmer
title: Ports
tags:
  - content
- rn
- transport-layer
- ports
- adressierung
created: '2026-10-07'
modified: '2026-10-07'
bereich: RN
---
author: Andreas Hümmer

# Ports

## Definition

Ports sind 16-Bit-Nummern, die Transportprotokolle zur Identifikation von Anwendungen verwenden.

## Erklärung

Ports ermöglichen die Multiplex-Kommunikation über eine IP-Adresse. Sie unterscheiden verschiedene Dienste und Anwendungen auf demselben Host. Well-Known Ports (0-1023) sind für Standarddienste reserviert.

## Eigenschaften

- 16-Bit-Nummern (0-65535)
- Well-Known Ports: 0-1023
- Registered Ports: 1024-49151
- Dynamic/Private Ports: 49152-65535

## Beispiele

- Port 80: HTTP
- Port 443: HTTPS
- Port 22: SSH
- Port 53: DNS

## Zusammenhänge

- [[TCP]]
- [[UDP]]
- [[DNS]]
- [[HTTP]]

## Prüfungstipps

- Wichtige Well-Known Ports auswendig kennen
- Unterschied Quell- und Zielport

## Quellen

- *Quelle 1*
