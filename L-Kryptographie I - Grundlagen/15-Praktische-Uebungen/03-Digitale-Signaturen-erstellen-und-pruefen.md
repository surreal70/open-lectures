---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - praxis
---

# Digitale Signaturen erstellen und prüfen

> [!info] **Lernziele**
> - Dateien mit OpenSSL signieren und verifizieren
> - Die Rolle des Hashwerts praktisch nachvollziehen
> - Manipulationen erkennen

---

## Inhalt

### Vorbereitung

Es wird ein Schlüsselpaar aus der vorherigen Übung benötigt (→ [[02-RSA-und-ECC-Schluessel-generieren]]). Testdatei:

```bash
echo "Vertrag: Betrag 1000 EUR" > vertrag.txt
```

### Signieren

```bash
# Signatur erstellen (RSA-PSS empfohlen)
openssl dgst -sha256 -sign rsa_priv.pem \
  -sigopt rsa_padding_mode:pss -out vertrag.sig vertrag.txt
```

Signiert wird intern der **SHA-256-Hash** der Datei (→ [[01-Grundlagen-digitaler-Signaturen]]), nicht die Datei selbst.

### Verifizieren

```bash
openssl dgst -sha256 -verify rsa_pub.pem \
  -sigopt rsa_padding_mode:pss -signature vertrag.sig vertrag.txt
# Ausgabe: "Verified OK"
```

### Manipulation erkennen

> [!tip] **Selbst ausprobieren**
> Ändere die Datei nach dem Signieren (z. B. Betrag auf 9000 EUR) und prüfe erneut:
> ```bash
> echo "Vertrag: Betrag 9000 EUR" > vertrag.txt
> openssl dgst -sha256 -verify rsa_pub.pem -sigopt rsa_padding_mode:pss \
>   -signature vertrag.sig vertrag.txt
> # Ausgabe: "Verification Failure"
> ```
> Jede Änderung ändert den Hash → die Signatur wird ungültig. Das demonstriert die **Integrität** (→ [[03-Schutzziele]]).

### Mit Ed25519 signieren

```bash
openssl pkeyutl -sign -inkey ed_priv.pem -rawin -in vertrag.txt -out vertrag_ed.sig
openssl pkeyutl -verify -pubin -inkey ed_pub.pem -rawin -in vertrag.txt -sigfile vertrag_ed.sig
```

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - `openssl dgst -sign/-verify` signiert und prüft Dateien (RSA-PSS empfohlen)
> - Signiert wird der Hash; jede Manipulation macht die Signatur ungültig
> - „Verified OK" vs. „Verification Failure" zeigt Integrität und Authentizität
> - Ed25519-Signaturen über `openssl pkeyutl`

---

## Übungen

1. Signieren Sie eine Datei mit RSA-PSS und verifizieren Sie sie.
2. Verändern Sie die Datei und beobachten Sie das Prüfergebnis.
3. Wiederholen Sie die Übung mit einem Ed25519-Schlüssel.

---

← [[02-RSA-und-ECC-Schluessel-generieren|← Zurück]] | [[00-Uebungen-Index|Übersicht]] | [[04-Eigene-Certificate-Authority-aufbauen|Weiter →]]
