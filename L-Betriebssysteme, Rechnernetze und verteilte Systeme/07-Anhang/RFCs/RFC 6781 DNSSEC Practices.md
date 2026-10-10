---
title: "RFC 6781 - DNSSEC Operational Practices, Version 2"
rfc_number: 6781
version: "December 2012"
status: Informational
author: "O. Kolkman, W. Mekking, R. Gieben"
obsoletes: "RFC 4641"
obsoleted_by: ""
language: DE
tags:
  - rfc
  - dns
  - dnssec
  - operations
  - practices
---

# RFC 6781 - DNSSEC Practices

## Überblick

RFC 6781 bietet praktische Anleitungen für den Betrieb von DNSSEC, einschließlich Key Management, Signing und Rollover.

## Zusammenfassung

DNSSEC-Betriebsthemen:

- **Key Management**: KSK und ZSK-Verwaltung
- **Key Rollover**: Sichere Schlüsselwechsel
- **Signing**: Zonensignierung
- **TTLs**: Timing-Überlegungen
- **Emergency Rollover**: Notfallverfahren

## Schlüsseltypen

| Schlüssel | Zweck | Lebensdauer |
|-----------|-------|-------------|
| KSK | Trust Anchor signieren | 1-2 Jahre |
| ZSK | Zone Records signieren | 1-3 Monate |

## Key Rollover-Verfahren

### ZSK Rollover (Pre-Publish)
```
1. Neuen ZSK in Zone publizieren
2. Warten (DNSKEY TTL + Propagation)
3. Zone mit neuem ZSK signieren
4. Warten
5. Alten ZSK entfernen
```

### KSK Rollover (Double-DS)
```
1. Neuen KSK erstellen
2. Beide DS Records beim Parent
3. Warten auf Propagation
4. Alten KSK deaktivieren
5. Alten DS entfernen
```

## Offizielles Dokument

**RFC 6781**: [https://www.rfc-editor.org/rfc/rfc6781](https://www.rfc-editor.org/rfc/rfc6781)

## Verwandte RFCs

- [[RFC 4033-4035 DNSSEC]] - DNSSEC-Spezifikation
- [[RFC 5155 NSEC3]] - NSEC3 Hashed Denial
- [[RFC 1035 DNS]] - DNS-Grundlagen
