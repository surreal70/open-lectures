---
title: "RFC 4033-4035 - DNS Security Extensions (DNSSEC)"
rfc_number: "4033, 4034, 4035"
version: "March 2005"
status: Proposed Standard
author: "R. Arends, R. Austein, M. Larson, D. Massey, S. Rose"
obsoletes: "RFC 2535, RFC 3008, RFC 3090, RFC 3445, RFC 3655, RFC 3658, RFC 3755, RFC 3757, RFC 3845"
obsoleted_by: ""
language: DE
tags:
  - rfc
  - dns
  - dnssec
  - security
  - cryptography
---

# RFC 4033-4035 - DNS Security Extensions (DNSSEC)

## Überblick

RFCs 4033, 4034 und 4035 definieren die DNS Security Extensions (DNSSEC), die Ursprungsauthentifizierung und Integritätssicherung für DNS-Daten bieten. DNSSEC schützt vor DNS-Spoofing- und Cache-Poisoning-Angriffen.

## Zusammenfassung

DNSSEC fügt DNS kryptografische Sicherheit hinzu:

- **RFC 4033**: Einführung und Anforderungen
- **RFC 4034**: Resource Records für DNSSEC (DNSKEY, RRSIG, NSEC, DS)
- **RFC 4035**: Protokollmodifikationen

**Hauptmerkmale:**
- **Digitale Signaturen**: RRsets mit Zonen-Privatschlüssel signiert
- **Vertrauenskette**: Von der Root-Zone bis zu einzelnen Records
- **Authentifizierte Ablehnung**: Beweis, dass ein Record nicht existiert (NSEC/NSEC3)
- **Schlüsselverwaltung**: Key Signing Keys (KSK) und Zone Signing Keys (ZSK)

## DNSSEC-Record-Typen

| Typ | Zweck |
|-----|-------|
| DNSKEY | Öffentlicher Schlüssel für Zonensignierung |
| RRSIG | Signatur über ein RRset |
| NSEC | Next Secure (authentifizierte Ablehnung) |
| NSEC3 | Gehashte authentifizierte Ablehnung |
| DS | Delegation Signer (Vertrauenskette) |
DNSSEC-Validierung ist auf DNS-Resolvern aktiviert:
- OPNsense Unbound: DNSSEC-Validierung aktiviert

**Quad9 DNSSEC:**
> "Quad9 validiert DNSSEC-Signaturen und lehnt ungültige Antworten ab"

## Offizielle Dokumente

- **RFC 4033**: [https://www.rfc-editor.org/rfc/rfc4033](https://www.rfc-editor.org/rfc/rfc4033)
- **RFC 4034**: [https://www.rfc-editor.org/rfc/rfc4034](https://www.rfc-editor.org/rfc/rfc4034)
- **RFC 4035**: [https://www.rfc-editor.org/rfc/rfc4035](https://www.rfc-editor.org/rfc/rfc4035)

## Verwandte RFCs

- [[RFC 1035 DNS]] - Basis-DNS-Spezifikation
- [[RFC 5155 NSEC3]] - NSEC3 Hashed Authenticated Denial
- [[RFC 6781 DNSSEC Practices]] - DNSSEC Operational Practices
