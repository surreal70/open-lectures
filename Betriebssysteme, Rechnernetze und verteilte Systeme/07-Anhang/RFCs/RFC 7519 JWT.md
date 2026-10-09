---
title: "RFC 7519 - JSON Web Token (JWT)"
rfc_number: 7519
version: "May 2015"
status: Proposed Standard
author: "M. Jones, J. Bradley, N. Sakimura"
obsoletes: ""
obsoleted_by: ""
language: DE
tags:
  - rfc
  - jwt
  - token
  - authentication
  - json
---

# RFC 7519 - JWT

## Überblick

RFC 7519 definiert JSON Web Tokens (JWT), ein kompaktes Format für sicheren Informationsaustausch zwischen Parteien.

## Zusammenfassung

JWT-Eigenschaften:

- **Kompakt**: URL-safe Base64-Kodierung
- **Selbstbeschreibend**: Claims im Token
- **Signiert**: JWS oder verschlüsselt (JWE)
- **Stateless**: Keine Serverseitige Session
- **Standard-Claims**: iss, sub, aud, exp, etc.

## JWT-Struktur

```
Header.Payload.Signature

eyJhbGciOiJIUzI1NiJ9.
eyJzdWIiOiIxMjM0NTY3ODkwIn0.
dozjgNryP4J3jVmNHl0w5N_XgL0n3I9PlFUP0THsR8U
```

## Standard-Claims

| Claim | Beschreibung |
|-------|--------------|
| iss | Issuer - Aussteller |
| sub | Subject - Betreff |
| aud | Audience - Empfänger |
| exp | Expiration - Ablaufzeit |
| nbf | Not Before - Gültig ab |
| iat | Issued At - Ausstellungszeit |
| jti | JWT ID - Eindeutige ID |

## Signaturen

| Algorithmus | Typ |
|-------------|-----|
| HS256 | HMAC mit SHA-256 |
| RS256 | RSA mit SHA-256 |
| ES256 | ECDSA mit P-256 |

## Offizielles Dokument

**RFC 7519**: [https://www.rfc-editor.org/rfc/rfc7519](https://www.rfc-editor.org/rfc/rfc7519)

## Verwandte RFCs

- [[RFC 6749 OAuth 2.0]] - OAuth 2.0 Framework
- [[RFC 7636 PKCE]] - Proof Key for Code Exchange
- [[RFC 7515 JWS]] - JSON Web Signature
