---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - hash
---

# Eigenschaften kryptographischer Hashfunktionen

> [!info] **Lernziele**
> - Die Kerneigenschaften kryptographischer Hashfunktionen kennen
> - Kryptographische von einfachen Hashfunktionen unterscheiden
> - Typische Anwendungsfälle einordnen

---

## Inhalt

### Was ist eine Hashfunktion?

Eine **Hashfunktion** bildet eine Eingabe beliebiger Länge auf einen Ausgabewert **fester** Länge ab (den Hashwert, „Digest" oder „Fingerabdruck"):

$$h = H(m), \qquad h \in \{0,1\}^n$$

Beispiel: SHA-256 liefert stets 256 Bit, egal ob die Eingabe ein Byte oder ein Gigabyte groß ist.

### Die drei kryptographischen Kerneigenschaften

| Eigenschaft | Bedeutung |
|-------------|-----------|
| **Urbildresistenz** (preimage) | Zu gegebenem $h$ ist kein $m$ mit $H(m)=h$ findbar (Einwegfunktion) |
| **Zweite-Urbildresistenz** (2nd preimage) | Zu gegebenem $m_1$ ist kein $m_2 \neq m_1$ mit gleichem Hash findbar |
| **Kollisionsresistenz** | Es ist generell kein Paar $m_1 \neq m_2$ mit $H(m_1)=H(m_2)$ findbar |

Diese Eigenschaften werden in [[04-Kollisionsresistenz-und-Preimage-Resistenz]] vertieft.

### Weitere wünschenswerte Eigenschaften

- **Lawineneffekt (avalanche):** Das Ändern eines einzigen Eingabebits ändert etwa die Hälfte der Ausgabebits.
- **Effizienz:** schnell berechenbar für beliebig große Eingaben.
- **Determinismus:** gleiche Eingabe → immer gleicher Hash.

### Kryptographisch vs. nicht-kryptographisch

Nicht jede Hashfunktion ist kryptographisch. Prüfsummen wie **CRC32** oder Hash-Tabellen-Funktionen sind schnell, aber **nicht** kollisions- oder urbildresistent – für Sicherheitszwecke ungeeignet.

> [!danger] **MD5 und SHA-1 sind gebrochen**
> Für MD5 und SHA-1 lassen sich praktisch Kollisionen erzeugen. Sie dürfen für Signaturen, Zertifikate oder Integritätssicherung **nicht** mehr verwendet werden. Aktuell: SHA-2, SHA-3 (→ [[02-SHA-2-und-SHA-3]]) oder BLAKE2/3 (→ [[03-BLAKE2-und-BLAKE3]]).

### Typische Anwendungen

- Integritätsprüfung (Datei-Prüfsummen, Downloads)
- Digitale Signaturen (es wird der Hash signiert, nicht die Nachricht)
- Nachrichtenauthentisierung (HMAC, → [[05-Message-Authentication-Codes-MAC-HMAC]])
- Passwortspeicherung (mit speziellen Verfahren, → [[06-Passwort-Hashing-PBKDF2-bcrypt-scrypt-Argon2id]])
- Datenstrukturen wie Merkle-Trees (→ [[08-Merkle-Trees]])

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Hashfunktion: beliebige Eingabe → fester Digest, deterministisch
> - Drei Kerneigenschaften: Urbild-, Zweite-Urbild- und Kollisionsresistenz
> - Lawineneffekt ist charakteristisch für kryptographische Hashes
> - MD5/SHA-1 sind gebrochen; heute SHA-2, SHA-3, BLAKE2/3

---

## Übungen

1. Grenzen Sie Urbildresistenz und Kollisionsresistenz voneinander ab.
2. Warum ist CRC32 keine kryptographische Hashfunktion?
3. Nennen Sie drei Anwendungen kryptographischer Hashfunktionen.

---

← [[00-Hashfunktionen-Index|Übersicht]] | [[02-SHA-2-und-SHA-3|Weiter →]]
