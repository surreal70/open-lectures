---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - praxis
---

# Dateien mit GPG verschlüsseln

> [!info] **Lernziele**
> - GPG-Schlüssel erzeugen und Dateien verschlüsseln
> - Symmetrische und asymmetrische GPG-Nutzung praktisch durchführen
> - Signieren mit GPG anwenden

---

## Inhalt

### Vorbereitung

Diese Übung nutzt **GnuPG** (`gpg --version` prüft die Installation).

### Schlüsselpaar erzeugen

```bash
gpg --full-generate-key
# Empfehlung: ECC (Curve 25519) oder RSA 4096, mit Ablaufdatum und Passphrase
```

Schlüssel auflisten:

```bash
gpg --list-keys           # öffentliche
gpg --list-secret-keys    # private
```

### Symmetrisch (passwortbasiert)

```bash
echo "Testdaten" > daten.txt
gpg --symmetric --cipher-algo AES256 daten.txt   # erzeugt daten.txt.gpg
gpg --decrypt daten.txt.gpg
```

### Asymmetrisch (für Empfänger)

```bash
# An eine Empfänger-ID verschlüsseln (deren öffentlicher Schlüssel muss importiert sein)
gpg --encrypt --recipient empfaenger@example.com daten.txt

# Entschlüsseln (mit eigenem privatem Schlüssel)
gpg --decrypt daten.txt.gpg
```

GPG arbeitet dabei intern **hybrid** (→ [[02-Dateiverschluesselung-mit-GPG]]).

### Signieren und prüfen

```bash
# Abgetrennte Signatur erstellen
gpg --detach-sign daten.txt        # erzeugt daten.txt.sig
# Prüfen
gpg --verify daten.txt.sig daten.txt
```

### Öffentlichen Schlüssel teilen

```bash
gpg --export --armor meine@mail.de > meine-mail.pub.asc
# Fingerprint zur Verifikation anzeigen
gpg --fingerprint meine@mail.de
```

> [!tip] **Fingerprint verifizieren**
> Vor dem ersten Verschlüsseln an eine Person deren **Fingerprint** über einen zweiten, vertrauenswürdigen Kanal abgleichen – so vermeidest du Man-in-the-Middle beim Schlüsselaustausch.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - `gpg --full-generate-key` erzeugt ein Schlüsselpaar (ECC/RSA, mit Passphrase)
> - Symmetrisch: `--symmetric`; asymmetrisch: `--encrypt --recipient`
> - Signieren/Prüfen mit `--detach-sign` / `--verify`
> - Öffentliche Schlüssel exportieren und Fingerprints verifizieren

---

## Übungen

1. Erzeugen Sie ein GPG-Schlüsselpaar und verschlüsseln Sie eine Datei symmetrisch.
2. Verschlüsseln Sie eine Datei asymmetrisch für einen (Test-)Empfänger.
3. Erstellen und prüfen Sie eine abgetrennte Signatur.

---

← [[06-SSH-Schluessel-sicher-verwalten|← Zurück]] | [[00-Uebungen-Index|Übersicht]] | [[08-Hashwerte-und-HMACs-berechnen|Weiter →]]
