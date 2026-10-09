---
title: "RFC 8252 - OAuth 2.0 for Native Apps"
rfc_number: 8252
version: "October 2017"
status: Best Current Practice
author: "W. Denniss, J. Bradley"
obsoletes: ""
obsoleted_by: ""
language: DE
tags:
  - rfc
  - oauth
  - native
  - mobile
  - authentication
---

# RFC 8252 - OAuth Native Apps

## Überblick

RFC 8252 definiert Best Practices für OAuth 2.0 in nativen Anwendungen (Desktop, Mobile), insbesondere zur sicheren Authentifizierung.

## Zusammenfassung

Best Practices:

- **System Browser**: Kein eingebetteter WebView
- **PKCE**: Verpflichtend für alle nativen Apps
- **Loopback Redirect**: localhost für Desktop-Apps
- **Custom URI Schemes**: Für mobile Apps
- **Kein Client Secret**: Native Apps sind Public Clients

## Warum System Browser?

| Eingebetteter WebView | System Browser |
|-----------------------|----------------|
| App kann Credentials abfangen | Isoliert von App |
| Keine SSO-Unterstützung | SSO mit anderen Apps |
| Keine Password Manager | Password Manager verfügbar |
| Phishing-Risiko | Vertrauenswürdige Adressleiste |

## Redirect-Methoden

### Mobile (Custom URI Scheme)
```
com.example.app://oauth/callback
```

### Desktop (Loopback)
```
http://127.0.0.1:port/callback
http://[::1]:port/callback
```

### Universal/App Links
```
https://app.example.com/callback
```

## Offizielles Dokument

**RFC 8252**: [https://www.rfc-editor.org/rfc/rfc8252](https://www.rfc-editor.org/rfc/rfc8252)

## Verwandte RFCs

- [[RFC 6749 OAuth 2.0]] - OAuth 2.0 Framework
- [[RFC 7636 PKCE]] - Proof Key for Code Exchange
- [[RFC 6750 OAuth Bearer Token]] - Bearer Token Usage
