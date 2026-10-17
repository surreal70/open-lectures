---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - pki
---

# X509-Zertifikate

> [!info] **Lernziele**
> - Den Aufbau eines X.509-Zertifikats kennen
> - Wichtige Felder und Erweiterungen verstehen
> - Kodierungen und Dateiformate einordnen

---

## Inhalt

### Der X.509-Standard

**X.509** ist das dominierende Format für digitale Zertifikate (TLS, S/MIME, Code Signing). Die heute übliche Version ist **X.509 v3**, die flexible Erweiterungen erlaubt.

### Wichtige Felder

| Feld | Bedeutung |
|------|-----------|
| **Version** | meist v3 |
| **Seriennummer** | eindeutige Nummer (vom Aussteller) |
| **Signaturalgorithmus** | z. B. SHA-256 mit RSA / ECDSA |
| **Aussteller (Issuer)** | die ausstellende CA |
| **Gültigkeit** | Not Before / Not After |
| **Subjekt (Subject)** | Inhaber-Identität |
| **Subject Public Key** | der zertifizierte öffentliche Schlüssel |
| **Erweiterungen (v3)** | Zusatzinformationen (s. u.) |
| **Signatur** | Signatur der CA über alle obigen Felder |

### Wichtige v3-Erweiterungen

- **Subject Alternative Name (SAN):** die eigentlichen Domainnamen (moderne Browser ignorieren den Common Name und werten nur SAN aus).
- **Key Usage / Extended Key Usage:** erlaubte Verwendungszwecke (z. B. Serverauthentifizierung, Signatur).
- **Basic Constraints:** ob das Zertifikat eine CA ist (`CA:TRUE/FALSE`).
- **CRL Distribution Points / AIA:** wo Sperrstatus und Aussteller-Zertifikat zu finden sind.

### Kodierung und Dateiformate

- **DER:** binäre Kodierung.
- **PEM:** Base64-kodiertes DER mit `-----BEGIN CERTIFICATE-----`-Rahmen – das verbreitetste Textformat.
- Dateiendungen: `.crt`, `.cer`, `.pem` (Zertifikate), `.key` (Schlüssel), `.p12`/`.pfx` (Zertifikat + privater Schlüssel gebündelt, PKCS#12).

> [!note] **Common Name ist veraltet**
> Früher stand der Hostname im **Common Name (CN)**. Moderne TLS-Clients prüfen ausschließlich die **SAN**-Erweiterung. Ein Zertifikat ohne passenden SAN-Eintrag wird abgelehnt, selbst wenn der CN stimmt.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - X.509 (v3) ist das Standard-Zertifikatsformat mit flexiblen Erweiterungen
> - Kernfelder: Seriennummer, Aussteller, Subjekt, öffentlicher Schlüssel, Gültigkeit, Signatur
> - Wichtige Erweiterungen: SAN, Key Usage, Basic Constraints, CRL/AIA
> - Kodierung DER/PEM; SAN ersetzt den veralteten Common Name

---

## Übungen

1. Nennen Sie fünf Kernfelder eines X.509-Zertifikats.
2. Warum ist die SAN-Erweiterung heute wichtiger als der Common Name?
3. Worin unterscheiden sich DER- und PEM-Kodierung?

---

← [[03-Root--und-Intermediate-Zertifikate|← Zurück]] | [[00-PKI-Index|Übersicht]] | [[05-Zertifikatsketten-und-Vertrauensmodelle|Weiter →]]
