---
author: Andreas Hümmer
title: IPsec - Internet Protocol Security
tags:
  - content
  - rn
  - sicherheit
  - vpn
  - ipsec
  - esp
  - ah
  - ike
created: '2026-10-13'
modified: '2026-10-13'
bereich: RN
---

# IPsec - Internet Protocol Security

## Definition

**IPsec (Internet Protocol Security)** ist eine Protokollsuite zur Absicherung der IP-Kommunikation auf Netzwerkschicht (Layer 3). Es bietet Verschlüsselung, Authentifizierung und Integritätsschutz für IP-Pakete.

> [!info] Schichtenzuordnung
> IPsec arbeitet auf **Layer 3** und ist bei IPv6 als Extension Header integriert. Siehe auch: [[../../03-Referenzmodelle/06-Netzwerkschicht/06-IPsec|IPsec in der Netzwerkschicht]]

## Komponenten

### Protokolle

| Protokoll | IP-Protocol | Funktion |
|-----------|-------------|----------|
| **ESP** | 50 | Encapsulating Security Payload – Verschlüsselung + Authentifizierung |
| **AH** | 51 | Authentication Header – Nur Authentifizierung (keine Verschlüsselung) |

### Schlüsselaustausch

| Protokoll | Port | Funktion |
|-----------|------|----------|
| **IKEv1** | UDP 500 | Internet Key Exchange Version 1 |
| **IKEv2** | UDP 500, 4500 | Internet Key Exchange Version 2 (aktuell) |

## Modi

```
┌─────────────────────────────────────────────────────────────────┐
│                    IPsec-Modi                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   TRANSPORT-MODUS                                               │
│   ┌──────────┬──────────┬────────────────────────┐             │
│   │ IP-Header│ ESP/AH   │      Nutzdaten         │             │
│   │(original)│  Header  │    (verschlüsselt)     │             │
│   └──────────┴──────────┴────────────────────────┘             │
│   → Host-to-Host, Original-IP-Header bleibt                    │
│                                                                  │
│   TUNNEL-MODUS                                                  │
│   ┌──────────┬──────────┬──────────┬─────────────┐             │
│   │ Neuer    │ ESP/AH   │ Original │  Nutzdaten  │             │
│   │IP-Header │  Header  │IP-Header │(verschlüss.)│             │
│   └──────────┴──────────┴──────────┴─────────────┘             │
│   → Gateway-to-Gateway, komplettes Paket gekapselt             │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## IKE-Phasen

<!-- TODO: IKE Phase 1 und Phase 2 erklären -->
<!-- TODO: Main Mode vs. Aggressive Mode -->
<!-- TODO: Quick Mode -->

## Security Associations (SA)

<!-- TODO: SA-Konzept erklären -->
<!-- TODO: SAD (Security Association Database) -->
<!-- TODO: SPD (Security Policy Database) -->

## Verschlüsselung und Algorithmen

<!-- TODO: Symmetrische Algorithmen (AES, 3DES) -->
<!-- TODO: Hash-Algorithmen (SHA-256, SHA-384) -->
<!-- TODO: Diffie-Hellman-Gruppen -->

## Prüfungsrelevante Themen

> [!warning] Klausurrelevanz: Hoch
> - Transport-Modus vs. Tunnel-Modus
> - ESP vs. AH – Unterschiede
> - IKE Phase 1 und Phase 2
> - Security Associations

## Zusammenhänge

- [[00-VPN-Index]] - VPN-Übersicht
- [[../../03-Referenzmodelle/06-Netzwerkschicht/06-IPsec|IPsec (Netzwerkschicht)]] - Layer-3-Einordnung
- [[05-L2TP]] - L2TP nutzt IPsec für Verschlüsselung

## Quellen

- [[A-RFC-Index#RFC 4301|RFC 4301]] - Security Architecture for IP
- [[A-RFC-Index#RFC 4303|RFC 4303]] - ESP
- [[A-RFC-Index#RFC 4302|RFC 4302]] - AH
- [[A-RFC-Index#RFC 7296|RFC 7296]] - IKEv2

