---
title: "RFC 7636 - Proof Key for Code Exchange (PKCE)"
rfc_number: 7636
version: "September 2015"
status: Proposed Standard
author: "N. Sakimura, J. Bradley, N. Agarwal"
obsoletes: ""
obsoleted_by: ""
language: DE
tags:
  - rfc
  - oauth
  - pkce
  - security
  - authentication
---

# RFC 7636 - PKCE

## Überblick

RFC 7636 definiert PKCE (Proof Key for Code Exchange), eine Sicherheitserweiterung für OAuth 2.0, die den Authorization Code Flow gegen Interception-Angriffe schützt.

## Zusammenfassung

PKCE-Funktionen:

- **Code Verifier**: Zufällige Zeichenkette (Client-Geheimnis)
- **Code Challenge**: Hash des Verifiers
- **Schutz**: Verhindert Code Interception
- **Public Clients**: Für Apps ohne Client Secret

## PKCE-Flow

```
1. Client generiert code_verifier (43-128 Zeichen)
2. Client berechnet code_challenge = SHA256(code_verifier)
3. Authorization Request mit code_challenge
4. User authentifiziert sich
5. Authorization Server gibt Code zurück
6. Token Request mit code_verifier
7. Server validiert: SHA256(code_verifier) == code_challenge
8. Token wird ausgestellt
```

## Parameter

| Parameter | Beschreibung |
|-----------|--------------|
| code_verifier | Zufällige Zeichenkette (43-128 Zeichen) |
| code_challenge | Base64URL(SHA256(code_verifier)) |
| code_challenge_method | "S256" (empfohlen) oder "plain" |

## Sicherheitsvorteile

- Authorization Code ohne PKCE kann abgefangen werden
- Code Verifier bleibt beim Client
- Angreifer kann Token nicht abrufen ohne Verifier

## Offizielles Dokument

**RFC 7636**: [https://www.rfc-editor.org/rfc/rfc7636](https://www.rfc-editor.org/rfc/rfc7636)

## Verwandte RFCs

- [[RFC 6749 OAuth 2.0]] - OAuth 2.0 Framework
- [[RFC 8252 OAuth Native Apps]] - OAuth für native Apps
- [[RFC 7519 JWT]] - JSON Web Tokens
