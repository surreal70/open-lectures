---
title: "RFC 8447 - IANA Registry Updates for TLS and DTLS"
rfc_number: 8447
version: "August 2018"
status: Proposed Standard
author: "J. Salowey, S. Turner"
obsoletes: ""
obsoleted_by: ""
language: DE
tags:
  - rfc
  - tls
  - iana
  - registry
---

# RFC 8447 - TLS IANA Registry

## Überblick

RFC 8447 aktualisiert die IANA-Register für TLS und DTLS, reorganisiert veraltete Einträge und etabliert neue Richtlinien.

## Zusammenfassung

Registry-Updates:

- **Cipher Suites**: Veraltete markiert
- **Extensions**: Neue Extensions hinzugefügt
- **Deprecated**: Unsichere Algorithmen gekennzeichnet
- **Recommended**: Empfehlungen für Implementierungen

## Deprecated Cipher Suites

| Status | Cipher Suites |
|--------|---------------|
| DEPRECATED | *_EXPORT_* |
| DEPRECATED | *_anon_* |
| DEPRECATED | *_NULL_* |
| DEPRECATED | *_DES_* (single DES) |
| DEPRECATED | *_RC4_* |

## Recommended Cipher Suites

| TLS Version | Empfohlene Suites |
|-------------|-------------------|
| TLS 1.3 | TLS_AES_128_GCM_SHA256 |
| TLS 1.3 | TLS_AES_256_GCM_SHA384 |
| TLS 1.3 | TLS_CHACHA20_POLY1305_SHA256 |
| TLS 1.2 | TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 |

## Offizielles Dokument

**RFC 8447**: [https://www.rfc-editor.org/rfc/rfc8447](https://www.rfc-editor.org/rfc/rfc8447)

## Verwandte RFCs

- [[RFC 8446 TLS 1.3]] - TLS 1.3-Spezifikation
- [[RFC 8449 TLS Record Size]] - TLS-Erweiterung
- [[RFC 8555 ACME]] - Zertifikatsautomatisierung
