---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - secdev
  - vertiefung
---

# Code Review Checkliste Kryptographie

> [!info] **Lernziele**
> - Eine praxistaugliche Review-Checkliste für Krypto-Code anwenden
> - Die wichtigsten Prüfpunkte systematisch abarbeiten
> - Findings den vorherigen Kapiteln zuordnen

---

## Inhalt

### Zweck

Diese Checkliste fasst die Erkenntnisse der Module 12 und 19 in eine **praktische Prüfliste** für Code-Reviews und Audits zusammen. Sie hilft, die häufigsten Fehler systematisch auszuschließen.

### Checkliste

> [!example] **Krypto-Code-Review-Checkliste**
>
> **Algorithmen & Modi**
> - [ ] Keine veralteten Verfahren (MD5, SHA-1, DES, RC4, ECB)?
> - [ ] Authenticated Encryption (AES-GCM / ChaCha20-Poly1305) statt „nur verschlüsseln"?
> - [ ] Kein Textbook-RSA (OAEP für Verschlüsselung, PSS für Signatur)?
>
> **Schlüssel & Zufall**
> - [ ] Alle Zufallswerte aus einem CSPRNG?
> - [ ] Keine hartcodierten Schlüssel/Secrets im Code/Repo?
> - [ ] Schlüssel aus KDF abgeleitet (Passwörter: Argon2/PBKDF2)?
> - [ ] Schlüsselspeicherung in HSM/KMS/Secret Manager?
>
> **Nonces & IVs**
> - [ ] Nonce/IV eindeutig bzw. korrekt zufällig?
> - [ ] Keine Nonce-Wiederverwendung (besonders GCM)?
>
> **Implementierung**
> - [ ] Konstante-Zeit-Vergleich für MACs/Tokens (kein `==`)?
> - [ ] Zertifikats-/Signaturprüfung aktiv und nicht umgangen?
> - [ ] Fehler „fail closed" (im Zweifel ablehnen)?
> - [ ] Keine Secrets in Logs/Exceptions/URLs?
>
> **Bibliotheken & Tests**
> - [ ] Etablierte, aktuelle Bibliothek (keine Eigenimplementierung)?
> - [ ] Testvektoren und Negativtests vorhanden?
> - [ ] Abhängigkeiten ohne bekannte CVEs?

### Einsatz

Diese Liste eignet sich für **Pull-Request-Reviews**, als Grundlage für automatisierte Checks (SAST) und für Audit-Vorbereitungen. Sie konkretisiert die **Crypto Policy** der Organisation (→ [[08-Kryptographische-Richtlinien-in-Unternehmen]]).

> [!tip] **Lebendes Dokument**
> Die Checkliste sollte an neue Bedrohungen und Standards angepasst werden (z. B. PQC-Bereitschaft, → Modul 13) – im Sinne der Crypto-Agility (→ [[07-Crypto-Agility]]).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Die Checkliste bündelt die wichtigsten Krypto-Prüfpunkte für Reviews
> - Bereiche: Algorithmen/Modi, Schlüssel/Zufall, Nonces/IVs, Implementierung, Bibliotheken/Tests
> - Konkretisiert die Crypto Policy und eignet sich für PR-Reviews und Audits
> - Regelmäßig aktualisieren (Crypto-Agility, PQC)

---

## Übungen

1. Wenden Sie die Checkliste auf ein Code-Beispiel Ihrer Wahl an.
2. Welche drei Prüfpunkte halten Sie für am kritischsten und warum?
3. Ergänzen Sie die Checkliste um einen Punkt zur PQC-Bereitschaft.

---

← [[06-Testing-und-Auditing-von-Crypto-Code|← Zurück]] | [[00-SecDev-Index|Übersicht]] | [[00-Architektur-Index|Nächstes Modul →]]
