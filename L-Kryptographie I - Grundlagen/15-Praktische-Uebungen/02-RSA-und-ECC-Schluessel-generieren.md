---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - praxis
---

# RSA und ECC-Schlüssel generieren

> [!info] **Lernziele**
> - RSA- und ECC-Schlüsselpaare mit OpenSSL erzeugen
> - Öffentliche Schlüssel extrahieren und Schlüssel inspizieren
> - Die Größenunterschiede praktisch erleben

---

## Inhalt

### RSA-Schlüssel erzeugen

```bash
# Privaten RSA-Schlüssel (3072 Bit) erzeugen
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:3072 -out rsa_priv.pem

# Öffentlichen Schlüssel extrahieren
openssl pkey -in rsa_priv.pem -pubout -out rsa_pub.pem

# Schlüssel inspizieren
openssl pkey -in rsa_priv.pem -text -noout
```

### ECC-Schlüssel erzeugen

```bash
# ECC-Schlüssel auf Kurve P-256
openssl genpkey -algorithm EC -pkeyopt ec_paramgen_curve:P-256 -out ec_priv.pem
openssl pkey -in ec_priv.pem -pubout -out ec_pub.pem

# Moderne Kurve Ed25519 (für Signaturen)
openssl genpkey -algorithm ED25519 -out ed_priv.pem
```

### Größen vergleichen

> [!tip] **Selbst beobachten**
> Vergleiche die Dateigrößen: Ein P-256-Schlüssel (≈ RSA-3072-Sicherheit, → [[07-Schlüssellängen-und-Sicherheitsniveaus]]) ist **deutlich kleiner** als der RSA-3072-Schlüssel. Das verdeutlicht den praktischen Vorteil von ECC (→ [[04-Elliptische-Kurven-Kryptographie-ECC]]).

### Privaten Schlüssel mit Passphrase schützen

```bash
# Verschlüsselt (mit Passphrase) speichern
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:3072 \
  -aes-256-cbc -out rsa_priv_enc.pem
```

> [!danger] **Private Schlüssel schützen**
> Private Schlüssel niemals unverschlüsselt weitergeben oder in Repositories ablegen (→ [[01-Lebenszyklus-kryptographischer-Schluessel]]). Dateirechte restriktiv setzen (`chmod 600`).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - `openssl genpkey` erzeugt RSA-, ECC- und Ed25519-Schlüssel
> - Öffentlichen Schlüssel mit `openssl pkey -pubout` extrahieren, mit `-text` inspizieren
> - ECC-Schlüssel sind bei gleicher Sicherheit viel kleiner als RSA
> - Private Schlüssel mit Passphrase schützen und Dateirechte beschränken

---

## Übungen

1. Erzeugen Sie je ein RSA-3072- und ein P-256-Schlüsselpaar und vergleichen Sie die Größen.
2. Extrahieren Sie den öffentlichen Schlüssel und inspizieren Sie den privaten mit `-text`.
3. Erzeugen Sie einen passphrase-geschützten privaten Schlüssel.

---

← [[01-AES-Verschluesselung-mit-OpenSSL|← Zurück]] | [[00-Uebungen-Index|Übersicht]] | [[03-Digitale-Signaturen-erstellen-und-pruefen|Weiter →]]
