---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - praxis
---

# SSH-Schlüssel sicher verwalten

> [!info] **Lernziele**
> - SSH-Schlüsselpaare sicher erzeugen und einsetzen
> - Den ssh-agent nutzen
> - Fingerprints prüfen und Schlüssel verwalten

---

## Inhalt

### Schlüsselpaar erzeugen

```bash
# Modernes Ed25519-Schlüsselpaar mit Passphrase
ssh-keygen -t ed25519 -C "nutzer@beispiel" -f ~/.ssh/id_ed25519
```

Dabei:

- `-t ed25519` wählt das moderne, robuste Verfahren (→ [[04-EdDSA-und-Ed25519]]).
- Eine **Passphrase** schützt den privaten Schlüssel auf der Platte.
- Es entstehen `id_ed25519` (privat) und `id_ed25519.pub` (öffentlich).

### Öffentlichen Schlüssel auf den Server bringen

```bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub nutzer@server
# fügt den öffentlichen Schlüssel in ~/.ssh/authorized_keys auf dem Server ein
```

### ssh-agent verwenden

```bash
eval "$(ssh-agent -s)"      # Agent starten
ssh-add ~/.ssh/id_ed25519   # Schlüssel laden (Passphrase einmal eingeben)
```

Der **ssh-agent** hält den entschlüsselten Schlüssel im Speicher, sodass die Passphrase nicht bei jeder Verbindung nötig ist (→ [[03-SSH-und-Schluesselmanagement]]).

### Fingerprint prüfen (gegen MitM)

```bash
# Fingerprint des eigenen Schlüssels
ssh-keygen -lf ~/.ssh/id_ed25519.pub
```

> [!warning] **Host-Key-Warnung ernst nehmen**
> Meldet SSH beim Verbinden eine **geänderte** Host-Identität, kann ein Man-in-the-Middle vorliegen (→ [[08-Replay-und-Man-in-the-Middle-Angriffe]]). Nicht blind bestätigen – den Fingerprint über einen vertrauenswürdigen Kanal verifizieren.

### Härtung (Serverseite)

> [!tip] **Empfohlene sshd-Einstellungen**
> - `PasswordAuthentication no` (nur Schlüssel)
> - `PermitRootLogin no`
> - nur moderne Schlüsseltypen zulassen

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - `ssh-keygen -t ed25519` erzeugt ein modernes Schlüsselpaar (mit Passphrase)
> - `ssh-copy-id` verteilt den öffentlichen Schlüssel in authorized_keys
> - ssh-agent hält den Schlüssel im Speicher; Fingerprints gegen MitM prüfen
> - Server härten: nur Public-Key, kein Root-Login

---

## Übungen

1. Erzeugen Sie ein Ed25519-Schlüsselpaar mit Passphrase.
2. Richten Sie Public-Key-Authentifizierung zu einem (Test-)Server ein.
3. Laden Sie den Schlüssel in den ssh-agent und prüfen Sie den Fingerprint.

---

← [[05-TLS-Verbindungen-mit-OpenSSL-analysieren|← Zurück]] | [[00-Uebungen-Index|Übersicht]] | [[07-Dateien-mit-GPG-verschluesseln|Weiter →]]
