---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - praxis
---

# Eigene Certificate Authority aufbauen

> [!info] **Lernziele**
> - Eine eigene (Test-)CA mit OpenSSL aufbauen
> - Zertifikate signieren und die Kette nachvollziehen
> - Den PKI-Workflow praktisch erleben

---

## Inhalt

### Ziel

In dieser Übung baust du eine **eigene Root-CA** und stellst damit ein Server-Zertifikat aus – der praktische Nachvollzug von Modul 8 (→ [[01-Architektur-einer-PKI]]).

> [!warning] **Nur zu Lernzwecken**
> Eine selbstgebaute CA ist für Tests/interne Zwecke gedacht. Für öffentliche Dienste nutzt man etablierte CAs (z. B. Let's Encrypt via ACME, → [[09-Zertifikatsmanagement-und-ACME]]).

### 1. Root-CA erstellen

```bash
# Privaten CA-Schlüssel erzeugen
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:4096 -out ca.key

# Selbstsigniertes Root-Zertifikat (10 Jahre)
openssl req -x509 -new -key ca.key -sha256 -days 3650 \
  -subj "/CN=Meine Test-Root-CA" -out ca.crt
```

### 2. Server-Schlüssel und CSR erstellen

```bash
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -out server.key

# Certificate Signing Request mit SAN
openssl req -new -key server.key -subj "/CN=example.local" \
  -addext "subjectAltName=DNS:example.local" -out server.csr
```

### 3. CSR von der CA signieren lassen

```bash
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key \
  -CAcreateserial -days 365 -sha256 \
  -copy_extensions copyall -out server.crt
```

### 4. Prüfen

```bash
# Zertifikat ansehen
openssl x509 -in server.crt -text -noout

# Kette gegen die CA verifizieren
openssl verify -CAfile ca.crt server.crt
# Ausgabe: server.crt: OK
```

> [!tip] **Zusammenhang zur Theorie**
> Du hast soeben eine **Vertrauenskette** erzeugt (→ [[05-Zertifikatsketten-und-Vertrauensmodelle]]): `ca.crt` ist der Vertrauensanker, `server.crt` wurde von der CA **signiert**. `openssl verify` prüft genau diese Signatur-Kette.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Root-CA = selbstsigniertes Zertifikat (`req -x509`)
> - Server: Schlüssel + CSR (`req -new`), dann von der CA signiert (`x509 -req -CA`)
> - SAN nicht vergessen; Kette mit `openssl verify -CAfile` prüfen
> - Selbstgebaute CA nur für Tests/intern

---

## Übungen

1. Bauen Sie eine Root-CA und stellen Sie ein Server-Zertifikat mit SAN aus.
2. Verifizieren Sie die Kette mit `openssl verify`.
3. Erzeugen Sie zusätzlich eine Intermediate-CA und bilden Sie eine dreistufige Kette.

---

← [[03-Digitale-Signaturen-erstellen-und-pruefen|← Zurück]] | [[00-Uebungen-Index|Übersicht]] | [[05-TLS-Verbindungen-mit-OpenSSL-analysieren|Weiter →]]
