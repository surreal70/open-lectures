---
title: "RFC 6749 - The OAuth 2.0 Authorization Framework"
rfc_number: 6749
version: "October 2012"
status: Proposed Standard
author: "D. Hardt"
obsoletes: ""
obsoleted_by: ""
language: DE
tags:
  - rfc
  - oauth
  - authorization
  - authentication
  - sso
  - iam
---

# RFC 6749 - OAuth 2.0 Authorization Framework

## Überblick

RFC 6749 definiert das OAuth 2.0 Autorisierungs-Framework, das Drittanbieter-Anwendungen ermöglicht, begrenzten Zugriff auf HTTP-Dienste zu erhalten. OAuth 2.0 wird häufig für Single Sign-On (SSO) und API-Autorisierung verwendet.

## Zusammenfassung

OAuth 2.0 bietet delegierte Autorisierung:

- **Authorization Grants**: Code, Implicit, Password, Client Credentials
- **Access Tokens**: Bearer-Tokens für API-Zugriff
- **Refresh Tokens**: Langlebige Tokens zum Erhalt neuer Access Tokens
- **Scopes**: Beschränkung des Zugriffs auf bestimmte Ressourcen
- **Rollen**: Resource Owner, Client, Authorization Server, Resource Server

## Grant-Typen

| Grant-Typ | Anwendungsfall |
|-----------|----------------|
| Authorization Code | Web-Apps mit Backend |
| Implicit | Legacy-Browser-Apps (veraltet) |
| Resource Owner Password | Vertrauenswürdige Erstanbieter-Apps |
| Client Credentials | Machine-to-Machine |

## OAuth 2.0 Flow (Authorization Code)

```
1. Benutzer → App: Fordert geschützte Ressource an
2. App → Auth Server: Autorisierungsanfrage
3. Auth Server → Benutzer: Login-Aufforderung
4. Benutzer → Auth Server: Anmeldedaten
5. Auth Server → App: Authorization Code
6. App → Auth Server: Code gegen Token tauschen
7. Auth Server → App: Access Token (+ Refresh Token)
8. App → Resource Server: Anfrage mit Access Token
```
OAuth 2.0 wird für SSO und Anwendungsintegration verwendet:

- Provider: Microsoft Entra ID
- Protokoll: OAuth 2.0 / OpenID Connect
- Anwendungen: Verschiedene SaaS-Integrationen

## Offizielles Dokument

**RFC 6749**: [https://www.rfc-editor.org/rfc/rfc6749](https://www.rfc-editor.org/rfc/rfc6749)

## Verwandte RFCs

- [[RFC 6750 OAuth Bearer Token]] - OAuth 2.0 Bearer Token Usage
- [[RFC 7636 PKCE]] - Proof Key for Code Exchange
- [[RFC 8252 OAuth Native Apps]] - OAuth 2.0 for Native Apps
- [[RFC 7519 JWT]] - JSON Web Token
- OpenID Connect Core 1.0 (baut auf OAuth 2.0 auf)
