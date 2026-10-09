---
title: "RFC 8446 - The Transport Layer Security (TLS) Protocol Version 1.3"
rfc_number: 8446
version: "August 2018"
status: Proposed Standard
author: "E. Rescorla"
obsoletes: ""
obsoleted_by: ""
language: DE
tags:
  - rfc
  - tls
  - security
  - encryption
  - cryptography
---

# RFC 8446 - TLS 1.3

## Überblick

RFC 8446 definiert das Transport Layer Security (TLS) Protokoll Version 1.3, ein wichtiges Update des TLS-Protokolls für sichere Kommunikation über das Internet. TLS 1.3 verbessert Sicherheit und Performance gegenüber früheren Versionen.

## Zusammenfassung

TLS 1.3 bietet moderne Verschlüsselung:

- **Vereinfachter Handshake**: 1-RTT (vs. 2-RTT bei TLS 1.2)
- **0-RTT-Modus**: Wiederaufnahmedaten im ersten Paket (mit Einschränkungen)
- **Legacy entfernt**: Kein RSA-Schlüsselaustausch, kein statisches DH, kein CBC
- **Forward Secrecy**: Obligatorischer ephemerer Schlüsselaustausch
- **Verschlüsselter Handshake**: Großteil des Handshakes verschlüsselt

## Wichtige Verbesserungen gegenüber TLS 1.2

| Aspekt | TLS 1.2 | TLS 1.3 |
|--------|---------|---------|
| Handshake RTT | 2 | 1 (0 für Wiederaufnahme) |
| Schlüsselaustausch | RSA, DHE, ECDHE | Nur DHE, ECDHE |
| Forward Secrecy | Optional | Obligatorisch |
| AEAD-Cipher | Optional | Obligatorisch |
| Handshake-Verschlüsselung | Teilweise | Vollständig |

## Unterstützte Cipher Suites

| Cipher Suite | Beschreibung |
|--------------|--------------|
| TLS_AES_128_GCM_SHA256 | AES-128 im GCM-Modus |
| TLS_AES_256_GCM_SHA384 | AES-256 im GCM-Modus |
| TLS_CHACHA20_POLY1305_SHA256 | ChaCha20-Poly1305 |

## Empfehlungen

- Minimum: TLS 1.2
- Bevorzugt: TLS 1.3
- Cipher Suites: Nur starke AEAD

## Offizielles Dokument

**RFC 8446**: [https://www.rfc-editor.org/rfc/rfc8446](https://www.rfc-editor.org/rfc/rfc8446)

## Verwandte RFCs

- [[RFC 8555 ACME]] - Zertifikatsautomatisierung
- [[RFC 8447 TLS IANA Registry]] - IANA Registry Updates for TLS and DTLS
- [[RFC 8449 TLS Record Size]] - Record Size Limit Extension for TLS
