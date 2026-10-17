---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - praxis
---

# Festplattenverschlüsselung LUKS BitLocker

> [!info] **Lernziele**
> - Zweck und Grenzen der Festplattenverschlüsselung verstehen
> - LUKS und BitLocker einordnen
> - Die Rolle von TPM und Schlüsselableitung kennen

---

## Inhalt

### Zweck: Data at Rest

**Festplattenverschlüsselung (Full Disk Encryption, FDE)** schützt Daten im **Ruhezustand** – etwa bei Verlust oder Diebstahl eines Geräts. Ohne das Geheimnis (Passwort/Schlüssel) sind die Daten unlesbar.

> [!note] **Wichtige Grenze**
> FDE schützt nur das **ausgeschaltete** oder gesperrte Gerät. Läuft das System und ist die Platte entschlüsselt eingebunden, bieten FDE **keinen** Schutz gegen Angriffe auf das laufende System (Malware, Live-Zugriff).

### LUKS (Linux)

**LUKS (Linux Unified Key Setup)** ist der Standard unter Linux (via `dm-crypt`):

- Verschlüsselung typischerweise mit **AES-XTS** (ein für Blockgeräte geeigneter Modus).
- Das Volumen wird mit einem zufälligen **Master-Key** verschlüsselt; dieser liegt – mit dem Passwort via KDF (Argon2/PBKDF2) abgeleitetem Schlüssel – verschlüsselt im LUKS-Header.
- Mehrere **Key-Slots** erlauben verschiedene Passphrasen/Schlüssel für dasselbe Volumen.

### BitLocker (Windows)

**BitLocker** ist Microsofts FDE-Lösung:

- Nutzt in der Regel das **TPM** (→ [[07-Trusted-Platform-Module-TPM]]), um den Schlüssel an das Gerät und den unveränderten Bootzustand zu binden.
- Optional mit PIN oder USB-Schlüssel als zusätzlichem Faktor.
- Recovery-Key für den Notfall (unbedingt sicher aufbewahren).

### Warum XTS statt GCM?

Blockgeräte brauchen einen Modus, der sektorweise arbeitet, keine Längenänderung verursacht und ohne pro-Sektor-Nonce auskommt. **XTS** erfüllt das. Es bietet allerdings **keine Authentizität** – FDE schützt Vertraulichkeit, nicht Integrität gegen gezielte Manipulation.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - FDE schützt Data at Rest bei Verlust/Diebstahl, nicht das laufende System
> - LUKS (Linux): AES-XTS, Master-Key im Header, mehrere Key-Slots, KDF für Passphrasen
> - BitLocker (Windows): meist TPM-gebunden, optional PIN/USB, Recovery-Key
> - XTS ist der FDE-Modus; er bietet Vertraulichkeit, aber keine Integrität

---

## Übungen

1. Wogegen schützt Festplattenverschlüsselung – und wogegen nicht?
2. Welche Rolle spielt das TPM bei BitLocker?
3. Warum wird für FDE AES-XTS statt AES-GCM verwendet?

---

← [[00-Praxis-Index|Übersicht]] | [[02-Dateiverschluesselung-mit-GPG|Weiter →]]
