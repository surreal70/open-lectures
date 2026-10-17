---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - praxis
---

# Dateiverschlüsselung mit GPG

> [!info] **Lernziele**
> - GPG/OpenPGP für Dateiverschlüsselung einsetzen
> - Symmetrische und asymmetrische GPG-Nutzung unterscheiden
> - Das hybride Vorgehen von GPG nachvollziehen

---

## Inhalt

### GPG und OpenPGP

**GPG (GNU Privacy Guard)** ist die freie Implementierung des **OpenPGP**-Standards. Es dient zum Verschlüsseln und Signieren von Dateien und E-Mails (→ [[03-E-Mail-Verschluesselung-OpenPGP-SMIME]]).

### Zwei Betriebsarten

**1. Symmetrisch (Passwort):**

```bash
gpg --symmetric datei.txt      # fragt nach Passphrase, erzeugt datei.txt.gpg
gpg --decrypt datei.txt.gpg
```

Geeignet, wenn Sender und Empfänger ein gemeinsames Passwort teilen.

**2. Asymmetrisch (Public Key):**

```bash
gpg --encrypt --recipient alice@example.com datei.txt
gpg --decrypt datei.txt.gpg     # mit privatem Schlüssel des Empfängers
```

Hier verschlüsselt man mit dem **öffentlichen** Schlüssel des Empfängers.

### Hybrid unter der Haube

> [!note] **GPG arbeitet hybrid**
> Auch bei der asymmetrischen Variante verschlüsselt GPG die Datei intern mit einem zufälligen **symmetrischen Sitzungsschlüssel** (schnell) und verschlüsselt nur diesen Schlüssel asymmetrisch für den Empfänger (→ [[06-RSA-OAEP-und-hybride-Verschlüsselung]]). Das ist das klassische KEM/DEM-Prinzip.

### Signieren und Vertrauen

- **Signatur:** `gpg --sign` bzw. `--detach-sign` erzeugt eine Signatur zur Authentizitätsprüfung.
- **Schlüsselverwaltung:** Öffentliche Schlüssel werden importiert und ihr Vertrauen im **Web of Trust** (→ [[05-Zertifikatsketten-und-Vertrauensmodelle]]) bewertet – dezentral, ohne zentrale CA.

> [!tip] **Praxis**
> Vor dem ersten Verschlüsseln an eine Person deren öffentlichen Schlüssel über einen vertrauenswürdigen Kanal verifizieren (Fingerprint abgleichen), um Man-in-the-Middle zu vermeiden.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - GPG implementiert OpenPGP für Datei-/E-Mail-Verschlüsselung und Signaturen
> - Symmetrisch (Passwort) oder asymmetrisch (öffentlicher Schlüssel des Empfängers)
> - Intern immer hybrid: Sitzungsschlüssel symmetrisch, dieser asymmetrisch gekapselt
> - Vertrauen über das dezentrale Web of Trust; Fingerprints verifizieren

---

## Übungen

1. Worin unterscheiden sich symmetrische und asymmetrische GPG-Verschlüsselung?
2. Warum arbeitet GPG intern hybrid?
3. Wie stellt man Vertrauen in einen öffentlichen GPG-Schlüssel her?

---

← [[01-Festplattenverschluesselung-LUKS-BitLocker|← Zurück]] | [[00-Praxis-Index|Übersicht]] | [[03-E-Mail-Verschluesselung-OpenPGP-SMIME|Weiter →]]
