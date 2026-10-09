---
author: Andreas Hümmer
title: Fallacies
tags:
  - content
- vs
- grundlagen
- fallacies
- netzwerk
created: '2026-10-07'
modified: '2026-10-07'
bereich: VS
---
author: Andreas Hümmer

# Fallacies

## Definition

Die 'Fallacies of Distributed Computing' sind acht falsche Annahmen, die Entwickler häufig über verteilte Systeme machen.

## Erklärung

Peter Deutsch und andere bei Sun Microsystems formulierten diese acht Irrtümer, die bei der Entwicklung verteilter Systeme berücksichtigt werden müssen: Das Netzwerk ist zuverlässig, Latenz ist null, Bandbreite ist unendlich, das Netzwerk ist sicher, die Topologie ändert sich nicht, es gibt einen Administrator, Transportkosten sind null, das Netzwerk ist homogen.

## Eigenschaften

- Netzwerk-Unzuverlässigkeit beachten
- Latenz und Bandbreite einplanen
- Sicherheitsaspekte berücksichtigen
- Dynamische Topologien erwarten
- Heterogenität handhaben

## Beispiele

- Timeout-Handling bei Netzwerkfehlern
- Caching zur Latenzreduzierung
- Retry-Mechanismen mit Backoff

## Zusammenhänge

- [[Definition]]
- [[Eigenschaften]]
- [[CAP-Theorem]]

## Prüfungstipps

- Alle 8 Fallacies auswendig kennen
- Auswirkungen jeder Fallacy erklären können
- Gegenmaßnahmen für jede Fallacy nennen

## Quellen

- *Quelle 1*
