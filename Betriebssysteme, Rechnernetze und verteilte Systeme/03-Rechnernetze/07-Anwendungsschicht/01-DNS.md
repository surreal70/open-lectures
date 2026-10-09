---
author: Andreas Hümmer
title: DNS
tags:
  - content
  - rn
  - application-layer
  - dns
  - namensaufloesung
created: '2026-10-07'
modified: '2026-10-07'
bereich: RN
---

# DNS

## Definition

DNS (Domain Name System) ist das verteilte System zur Auflösung von Domainnamen in IP-Adressen.

## Erklärung

DNS übersetzt menschenlesbare Domainnamen (z.B. google.com) in IP-Adressen. Es ist hierarchisch aufgebaut mit Root-Servern, TLD-Servern und autoritativen Name-Servern. DNS verwendet primär UDP auf Port 53.

## Eigenschaften

- Hierarchisches, verteiltes System
- Caching zur Performanceoptimierung
- Verschiedene Record-Typen (A, AAAA, MX, CNAME)
- UDP Port 53 (TCP für Zone Transfers)

## Beispiele

- A-Record: Domainname → IPv4-Adresse
- AAAA-Record: Domainname → IPv6-Adresse
- MX-Record: Mail-Server einer Domain

## Zusammenhänge

- [[HTTP]]
- [[Ports]]
- [[UDP]]

## Prüfungstipps

- DNS-Auflösungsprozess verstehen
- Wichtige Record-Typen kennen

## Quellen

- *Quelle 1*
