---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - angriffe
---

# Brute-Force und Dictionary-Angriffe

> [!info] **Lernziele**
> - Brute-Force- und Dictionary-Angriffe unterscheiden
> - Den Einfluss von Schlüssel-/Passwortlänge einschätzen
> - Gegenmaßnahmen kennen

---

## Inhalt

### Brute-Force-Angriff

Beim **Brute-Force-Angriff** probiert der Angreifer **systematisch alle möglichen** Schlüssel oder Passwörter durch, bis einer passt. Der Aufwand wächst exponentiell mit der Länge:

| Schlüssellänge | Mögliche Schlüssel |
|----------------|--------------------|
| 40 Bit | $2^{40} \approx 10^{12}$ (in Sekunden brechbar) |
| 56 Bit (DES) | $2^{56}$ (1998 gebrochen) |
| 128 Bit | $2^{128}$ (praktisch unmöglich) |
| 256 Bit | $2^{256}$ (auch für Quantencomputer außer Reichweite) |

Deshalb ist **Schlüssellänge** die erste Verteidigung: Ab 128 Bit ist reines Durchprobieren chancenlos (→ [[07-Schlüssellängen-und-Sicherheitsniveaus]]).

### Dictionary-Angriff

Ein **Dictionary-Angriff** probiert nicht alle Kombinationen, sondern eine **Liste wahrscheinlicher** Passwörter (häufige Passwörter, geleakte Listen, Wörterbücher, Varianten). Er nutzt aus, dass menschlich gewählte Passwörter **nicht gleichverteilt** sind.

Varianten:

- **Rainbow Tables:** vorberechnete Hash-Tabellen (durch **Salt** unwirksam, → [[07-Salt-Pepper-und-Key-Stretching]]).
- **Credential Stuffing:** geleakte Nutzer/Passwort-Paare bei anderen Diensten ausprobieren.

### Gegenmaßnahmen

> [!tip] **Schutz gegen Rateangriffe**
> - **Lange, zufällige** Schlüssel/Passwörter (hohe Entropie).
> - **Passwort-Hashing** mit Salt und Key-Stretching (Argon2 etc.) → jeder Rateversuch wird teuer (→ [[06-Passwort-Hashing-PBKDF2-bcrypt-scrypt-Argon2id]]).
> - **Rate Limiting** und Account-Sperren gegen Online-Angriffe.
> - **Mehr-Faktor-Authentifizierung (MFA)** als zusätzliche Hürde.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Brute Force probiert alle Schlüssel durch – ab 128 Bit chancenlos
> - Dictionary-Angriffe nutzen die Vorhersagbarkeit menschlicher Passwörter
> - Salt macht Rainbow Tables unwirksam; Credential Stuffing nutzt Leaks
> - Schutz: hohe Entropie, langsames Passwort-Hashing, Rate Limiting, MFA

---

## Übungen

1. Worin unterscheiden sich Brute-Force- und Dictionary-Angriffe?
2. Warum sind Rainbow Tables bei gesalzenen Hashes nutzlos?
3. Nennen Sie drei Gegenmaßnahmen gegen Rateangriffe.

---

← [[00-Angriffe-Index|Übersicht]] | [[02-Known-Plaintext-und-Chosen-Plaintext-Angriffe|Weiter →]]
