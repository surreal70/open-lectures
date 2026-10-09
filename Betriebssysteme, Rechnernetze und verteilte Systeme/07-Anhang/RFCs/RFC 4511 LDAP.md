---
title: "RFC 4511 - Lightweight Directory Access Protocol (LDAP)"
rfc_number: 4511
version: "June 2006"
status: Proposed Standard
author: "J. Sermersheim"
obsoletes: "RFC 2251, RFC 2830, RFC 3771"
obsoleted_by: ""
language: DE
tags:
  - rfc
  - ldap
  - directory
  - authentication
  - identity
---

# RFC 4511 - LDAP

## Überblick

RFC 4511 definiert das Lightweight Directory Access Protocol (LDAP), ein Protokoll für den Zugriff auf und die Pflege von verteilten Verzeichnisinformationsdiensten über ein IP-Netzwerk. LDAP wird häufig für zentralisierte Authentifizierung und Verzeichnisdienste verwendet.

## Zusammenfassung

LDAP bietet Verzeichniszugriff:

- **Hierarchisches Datenmodell**: Baumstruktur (DIT - Directory Information Tree)
- **Distinguished Names (DN)**: Eindeutige Kennungen für Einträge
- **Attribute**: Name-Wert-Paare für Eintragsdaten
- **Operationen**: Bind, Search, Add, Delete, Modify, Compare
- **Schema**: Definiert erlaubte Attribute und Objektklassen

## Wichtige Spezifikationen

| Parameter | Wert |
|-----------|------|
| Protokoll | TCP |
| Port | 389 (LDAP) |
| Port | 636 (LDAPS - LDAP über TLS) |
| Authentifizierung | Simple (Passwort), SASL |

## LDAP-Operationen

| Operation | Beschreibung |
|-----------|--------------|
| Bind | Am Verzeichnis authentifizieren |
| Search | Nach Einträgen suchen |
| Add | Neuen Eintrag erstellen |
| Delete | Eintrag entfernen |
| Modify | Eintragsattribute ändern |
| ModifyDN | Eintrag umbenennen/verschieben |
| Compare | Attributwert vergleichen |
| Unbind | Verbindung schließen |

## DN-Format

```
cn=John Doe,ou=Users,dc=example,dc=com
```

| Komponente | Bedeutung |
|------------|-----------|
| cn | Common Name |
| ou | Organizational Unit |
| dc | Domain Component |
LDAP-Konzepte gelten für das Identitätsmanagement:
## Offizielles Dokument

**RFC 4511**: [https://www.rfc-editor.org/rfc/rfc4511](https://www.rfc-editor.org/rfc/rfc4511)

## Verwandte RFCs

- RFC 4510-4517 - LDAP Technical Specification Suite
- [[RFC 6749 OAuth 2.0]] - Moderne Alternative für Autorisierung
