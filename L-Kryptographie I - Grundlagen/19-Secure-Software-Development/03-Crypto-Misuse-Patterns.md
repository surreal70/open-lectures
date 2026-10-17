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

# Crypto Misuse Patterns

> [!info] **Lernziele**
> - Die häufigsten Crypto-Misuse-Muster erkennen
> - Ihre Ursachen und Folgen verstehen
> - Gegenmaßnahmen zuordnen

---

## Inhalt

### Was sind Crypto-Misuse-Patterns?

Studien (z. B. zu Android-Apps) zeigen: Ein Großteil der Krypto-Fehler folgt **wenigen, immer gleichen Mustern** – nicht gebrochener Mathematik, sondern falscher Anwendung korrekter Verfahren. Diese Muster zu kennen, verhindert die häufigsten Fehler.

### Die Top-Misuse-Muster

| # | Muster | Folge | Richtig |
|---|--------|-------|---------|
| 1 | **ECB-Modus** | Muster sichtbar | AEAD (GCM) |
| 2 | **Statischer/vorhersehbarer IV** | CPA-angreifbar | zufälliger IV / Nonce-Verwaltung |
| 3 | **Nonce-Wiederverwendung** | Klartext-/Schlüssel-Leck | eindeutige Nonce (→ [[07-Nonce-Reuse-und-Schluesselwiederverwendung]]) |
| 4 | **Hartcodierte Schlüssel** | im Repo/Binary auslesbar | KMS/Secret Manager |
| 5 | **Schwacher Zufall** | vorhersagbare Schlüssel | CSPRNG (→ [[04-Secure-Random-und-Entropy]]) |
| 6 | **Passwort als Schlüssel** ohne KDF | schwach | Argon2/PBKDF2 |
| 7 | **MD5/SHA-1** | gebrochen | SHA-256/SHA-3 |
| 8 | **Verschlüsseln ohne Authentisieren** | Manipulation/Padding-Oracle | AEAD |
| 9 | **Zertifikatsprüfung deaktiviert** | MitM | Validierung erzwingen |

### Beispiel: deaktivierte Zertifikatsprüfung

> [!danger] **Ein verbreiteter, fataler Fehler**
> In Mobile-/Backend-Code wird die TLS-Zertifikatsprüfung oft „zum Testen" abgeschaltet (`verify=False`, „trust all certificates") und dann **vergessen**. Das hebelt den gesamten TLS-Schutz aus (→ [[02-HTTPS-und-Zertifikatsvalidierung]]). Niemals in Produktion.

### Warum passiert das?

- Komplexe Low-Level-APIs mit unsicheren Defaults.
- Copy-Paste aus veralteten Tutorials/Stack-Overflow-Antworten.
- Zeitdruck und fehlendes Krypto-Wissen.

Gegenmittel: misuse-resistente High-Level-APIs (→ [[02-Sichere-Implementierungsmuster]]) und Reviews (→ [[07-Code-Review-Checkliste-Kryptographie]]).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Die meisten Krypto-Fehler folgen wenigen wiederkehrenden Misuse-Mustern
> - Top-Muster: ECB, statischer IV, Nonce-Reuse, hardcodierte Schlüssel, schwacher Zufall, fehlende Auth, deaktivierte Zertifikatsprüfung
> - Ursachen: unsichere Defaults, Copy-Paste, Zeitdruck
> - Abwehr: High-Level-APIs mit sicheren Defaults und Code-Reviews

---

## Übungen

1. Nennen Sie fünf verbreitete Crypto-Misuse-Muster und die jeweils richtige Lösung.
2. Warum ist eine deaktivierte Zertifikatsprüfung so gefährlich?
3. Welche Faktoren begünstigen Crypto-Misuse in der Praxis?

---

← [[02-Sichere-Implementierungsmuster|← Zurück]] | [[00-SecDev-Index|Übersicht]] | [[04-Secure-Random-und-Entropy|Weiter →]]
