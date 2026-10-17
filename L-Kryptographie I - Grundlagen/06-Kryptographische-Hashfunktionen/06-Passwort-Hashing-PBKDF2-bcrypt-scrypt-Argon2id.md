---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - hash
---

# Passwort-Hashing PBKDF2 bcrypt scrypt Argon2id

> [!info] **Lernziele**
> - Verstehen, warum Passwörter nicht mit normalen Hashes gespeichert werden
> - PBKDF2, bcrypt, scrypt und Argon2id unterscheiden
> - Die aktuelle Empfehlung für Passwort-Hashing kennen

---

## Inhalt

### Warum kein normaler Hash?

Passwörter dürfen nie im Klartext gespeichert werden. Aber auch ein einfacher schneller Hash wie SHA-256 ist **ungeeignet**: Angreifer können Milliarden Hashes pro Sekunde berechnen und mit **Rainbow Tables** oder Brute Force knacken. Genau diese Geschwindigkeit ist hier das Problem.

Passwort-Hashing braucht daher **absichtlich langsame**, ressourcenintensive Funktionen plus einen zufälligen **Salt** (→ [[07-Salt-Pepper-und-Key-Stretching]]).

### Die wichtigsten Verfahren

| Verfahren | Jahr | Härtung gegen | Hinweis |
|-----------|------|---------------|---------|
| **PBKDF2** | 2000 | CPU (Iterationen) | weit verbreitet, aber nur CPU-hart |
| **bcrypt** | 1999 | CPU, etwas Speicher | bewährt, begrenzte Passwortlänge (72 Byte) |
| **scrypt** | 2009 | CPU **und** Speicher | erschwert GPU/ASIC-Angriffe |
| **Argon2id** | 2015 | CPU und Speicher | **Gewinner** der Password Hashing Competition |

### Das Prinzip „memory-hard"

Moderne Angreifer nutzen GPUs und spezielle ASICs, die extrem viele Hashes parallel berechnen. **Speicherharte** Verfahren (scrypt, Argon2) verlangen zusätzlich viel RAM pro Berechnung – das bremst parallele Hardware-Angriffe drastisch, da Speicher teuer und schlecht parallelisierbar ist.

### Empfehlung

> [!tip] **Aktuelle Best Practice**
> Für neue Systeme ist **Argon2id** die erste Wahl. Wo Argon2 nicht verfügbar ist, sind **scrypt** oder **bcrypt** akzeptabel. **PBKDF2** nur mit hoher Iterationszahl verwenden (z. B. in Umgebungen mit FIPS-Vorgabe). Parameter (Speicher, Iterationen, Parallelität) regelmäßig an aktuelle Hardware anpassen.

> [!danger] **Niemals**
> Passwörter nie mit reinem MD5/SHA-1/SHA-256 ohne Salt und Key-Stretching speichern – das ist bei einem Datenleck praktisch sofort knackbar.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Schnelle Hashes sind für Passwörter ungeeignet (Brute Force, Rainbow Tables)
> - Passwort-Hashing braucht absichtlich langsame, gesalzene Verfahren
> - Argon2id (memory-hard) ist heutige erste Wahl; scrypt/bcrypt akzeptabel, PBKDF2 nur mit hohen Iterationen
> - Parameter an aktuelle Hardware anpassen

---

## Übungen

1. Warum ist SHA-256 allein für Passwortspeicherung ungeeignet?
2. Was bedeutet „memory-hard" und welchen Angriff erschwert es?
3. Welches Verfahren empfiehlt sich heute für neue Systeme?

---

← [[05-Message-Authentication-Codes-MAC-HMAC|← Zurück]] | [[00-Hashfunktionen-Index|Übersicht]] | [[07-Salt-Pepper-und-Key-Stretching|Weiter →]]
