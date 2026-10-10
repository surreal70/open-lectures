---
title: "RFC 5155 - DNS Security (DNSSEC) Hashed Authenticated Denial of Existence"
rfc_number: 5155
version: "March 2008"
status: Proposed Standard
author: "B. Laurie, G. Sisson, R. Arends, D. Blacka"
obsoletes: ""
obsoleted_by: ""
language: DE
tags:
  - rfc
  - dns
  - dnssec
  - nsec3
  - security
---

# RFC 5155 - NSEC3

## Überblick

RFC 5155 definiert NSEC3, eine verbesserte Methode zur authentifizierten Nichtexistenzbestätigung in DNSSEC, die Zone Walking verhindert.

## Zusammenfassung

NSEC3-Eigenschaften:

- **Hashed Owner Names**: Domänennamen werden gehasht
- **Zone Walking Schutz**: Enumeration erschwert
- **Opt-Out**: Unsigned Delegations überspringen
- **Iterationen**: Brute-Force-Schutz

## NSEC vs NSEC3

| NSEC | NSEC3 |
|------|-------|
| Klartext-Namen | Gehashte Namen |
| Zone Walking möglich | Zone Walking erschwert |
| Einfacher | Komplexer |
| Alle Einträge signiert | Opt-Out möglich |

## NSEC3-Parameter

| Parameter | Beschreibung |
|-----------|--------------|
| Hash Algorithm | Typisch SHA-1 (1) |
| Flags | Opt-Out Flag |
| Iterations | Anzahl Hash-Iterationen |
| Salt | Zufälliger Wert für Hashing |

## NSEC3PARAM Record

```
example.com. IN NSEC3PARAM 1 0 10 AABBCCDD
                            | | |  |
                            | | |  Salt
                            | | Iterations
                            | Flags
                            Hash Algorithm
```

## Offizielles Dokument

**RFC 5155**: [https://www.rfc-editor.org/rfc/rfc5155](https://www.rfc-editor.org/rfc/rfc5155)

## Verwandte RFCs

- [[RFC 4033-4035 DNSSEC]] - DNSSEC-Grundlagen
- [[RFC 1035 DNS]] - DNS-Spezifikation
- [[RFC 6781 DNSSEC Practices]] - DNSSEC-Betrieb
