---
title: "RFC 8449 - Record Size Limit Extension for TLS"
rfc_number: 8449
version: "August 2018"
status: Proposed Standard
author: "D. Thomson"
obsoletes: ""
obsoleted_by: ""
language: DE
tags:
  - rfc
  - tls
  - extension
  - record
---

# RFC 8449 - TLS Record Size

## Überblick

RFC 8449 definiert eine TLS-Erweiterung zur Begrenzung der maximalen Record-Größe, wichtig für ressourcenbeschränkte Geräte.

## Zusammenfassung

Record Size Limit:

- **Kleinere Buffer**: Weniger Speicherbedarf
- **IoT-freundlich**: Für eingebettete Systeme
- **Bidirektional**: Client und Server können Limits setzen
- **Ersetzt max_fragment_length**: Modernere Alternative

## Vergleich mit max_fragment_length

| max_fragment_length | record_size_limit |
|---------------------|-------------------|
| Nur 4 Werte (512-4096) | Beliebige Größe (64-16384) |
| Veraltet | Modern |
| Beide Richtungen gleich | Pro Richtung konfigurierbar |

## Extension Format

```
record_size_limit Extension:
  extension_type: 28
  extension_data: RecordSizeLimit (uint16)

Wertebereich: 64 - 16384 Bytes
```

## Anwendungsfälle

| Szenario | Limit |
|----------|-------|
| IoT Sensoren | 64-256 Bytes |
| Embedded Devices | 512-2048 Bytes |
| Standard Server | 16384 Bytes (max) |

## Offizielles Dokument

**RFC 8449**: [https://www.rfc-editor.org/rfc/rfc8449](https://www.rfc-editor.org/rfc/rfc8449)

## Verwandte RFCs

- [[RFC 8446 TLS 1.3]] - TLS 1.3-Spezifikation
- [[RFC 8447 TLS IANA Registry]] - TLS-Registry
- [[RFC 8555 ACME]] - Zertifikatsautomatisierung
