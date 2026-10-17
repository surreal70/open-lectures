---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - hash
---

# Salt Pepper und Key Stretching

> [!info] **Lernziele**
> - Zweck von Salt und Pepper beim Passwort-Hashing verstehen
> - Key-Stretching als Schutzmechanismus einordnen
> - Diese Techniken korrekt kombinieren

---

## Inhalt

### Salt

Ein **Salt** ist ein zufälliger, **pro Passwort eindeutiger** Wert, der vor dem Hashen zum Passwort hinzugefügt wird. Er wird zusammen mit dem Hash gespeichert (er muss **nicht** geheim sein).

Zweck:

- **Verhindert Rainbow Tables:** Vorberechnete Hash-Tabellen werden nutzlos, da jeder Hash durch den individuellen Salt anders ausfällt.
- **Verhindert das Erkennen gleicher Passwörter:** Zwei Nutzer mit identischem Passwort erhalten durch unterschiedliche Salts verschiedene Hashes.

```
Nutzer A: hash = Argon2id(salt_A, "passwort")
Nutzer B: hash = Argon2id(salt_B, "passwort")   → völlig anderer Hash
```

### Pepper

Ein **Pepper** ist ein zusätzliches Geheimnis, das – anders als der Salt – **nicht** in der Datenbank, sondern separat (z. B. in der Anwendungskonfiguration oder einem HSM) gespeichert wird und für **alle** Passwörter gleich sein kann.

Zweck: Selbst bei einem reinen **Datenbankleck** (ohne Zugriff auf die Anwendung) bleiben die Hashes ohne den Pepper unknackbar. Der Pepper ist eine Verteidigung in der Tiefe, kein Ersatz für Salt.

### Key-Stretching

**Key-Stretching** macht das Hashen absichtlich **langsam und aufwendig**, indem die Berechnung viele Iterationen (und bei memory-hard Verfahren viel Speicher) benötigt. Dadurch sinkt die Zahl der Rateversuche, die ein Angreifer pro Sekunde durchführen kann, drastisch.

Genau das leisten die Passwort-Hashing-Verfahren PBKDF2, bcrypt, scrypt und Argon2id (→ [[06-Passwort-Hashing-PBKDF2-bcrypt-scrypt-Argon2id]]) über ihre Kostenparameter.

### Richtige Kombination

> [!tip] **Best Practice**
> `hash = Argon2id(pepper + passwort, salt)` mit
> - **Salt:** zufällig, pro Passwort, mitgespeichert
> - **Pepper:** geheim, anwendungsweit, getrennt gespeichert
> - **Key-Stretching:** über passende Argon2id-Parameter
>
> So greifen alle drei Mechanismen ineinander.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Salt: zufällig pro Passwort, nicht geheim, verhindert Rainbow Tables und gleiche Hashes
> - Pepper: anwendungsweites Geheimnis, getrennt gespeichert, schützt bei reinem DB-Leck
> - Key-Stretching: absichtlich teure Berechnung, senkt Rateversuche pro Sekunde
> - Zusammen mit Argon2id ergibt das die sichere Passwortspeicherung

---

## Übungen

1. Warum muss ein Salt nicht geheim sein, ein Pepper aber schon?
2. Welchen Angriff verhindert der Salt konkret?
3. Was bewirkt Key-Stretching aus Sicht des Angreifers?

---

← [[06-Passwort-Hashing-PBKDF2-bcrypt-scrypt-Argon2id|← Zurück]] | [[00-Hashfunktionen-Index|Übersicht]] | [[08-Merkle-Trees|Weiter →]]
