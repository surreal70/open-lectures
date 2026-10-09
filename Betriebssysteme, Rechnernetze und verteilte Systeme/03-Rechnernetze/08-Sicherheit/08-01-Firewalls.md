---
author: Andreas Hümmer
title: Firewalls
tags:
  - content
- rn
- sicherheit
- firewall
- paketfilter
created: '2026-10-07'
modified: '2026-10-07'
bereich: RN
---
author: Andreas Hümmer

# Firewalls

## Definition

Eine Firewall ist ein Sicherheitssystem, das den Netzwerkverkehr basierend auf definierten Regeln filtert.

## Erklärung

Firewalls kontrollieren den Datenverkehr zwischen Netzwerkzonen (z.B. Internet und LAN). Sie können auf verschiedenen Ebenen arbeiten: Paketfilter (Schicht 3/4), Stateful Inspection und Application-Level-Gateways.

## Eigenschaften

- Paketfilter: Filterung nach IP/Port
- Stateful Inspection: Verbindungsstatus berücksichtigt
- Application-Level-Gateway: Protokollprüfung
- Default-Deny vs. Default-Allow

## Beispiele

- Linux iptables/nftables
- Windows Defender Firewall
- pfSense als Hardware-Firewall

## Zusammenhänge

- [[VPN]]
- [[TLS]]
- [[IP-Protokoll]]
- [[Ports]]

## Prüfungstipps

- Unterschied Paketfilter vs. Stateful Firewall
- Typische Firewall-Regeln

## Quellen

- *Quelle 1*
