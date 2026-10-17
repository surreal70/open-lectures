---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - verschlüsselung
  - hashing
  - signatur
  - kodierung
---

# Verschlüsselung, Hashing, Kodierung und Signierung

> [!info] **Lernziele**
> - Die vier Verfahren klar unterscheiden können
> - Anwendungsfälle für jedes Verfahren kennen
> - Typische Fehler bei der Verwechslung vermeiden

---

## Inhalt

Vier Verfahren werden in der Praxis ständig verwechselt – mit teils gravierenden Sicherheitsfolgen. Entscheidend ist, sie nach **Umkehrbarkeit**, **Schlüsselbedarf** und **Schutzziel** zu unterscheiden.

### Verschlüsselung (Encryption)

**Zweck:** Vertraulichkeit. Verschlüsselung macht Daten unlesbar für Unbefugte und ist **mit dem passenden Schlüssel umkehrbar**.

- Benötigt einen **Schlüssel** (symmetrisch oder asymmetrisch).
- Ohne Schlüssel soll die Rückgewinnung des Klartexts praktisch unmöglich sein.
- Beispiele: AES (symmetrisch), RSA (asymmetrisch).

```
"Passwort123"  ──[ E(K, ·) ]──►  "9f3a...c7"  ──[ D(K, ·) ]──►  "Passwort123"
```

### Hashing

**Zweck:** Integrität / Fingerabdruck. Eine Hashfunktion bildet beliebig lange Eingaben auf einen **festen** Ausgabewert ab und ist eine **Einwegfunktion** – aus dem Hashwert lässt sich der Eingabewert nicht zurückrechnen.

- **Kein Schlüssel** nötig (reine Funktion).
- Eigenschaften guter kryptographischer Hashes: Kollisionsresistenz, Urbildresistenz, Lawineneffekt (kleine Eingabeänderung → völlig anderer Hash).
- Beispiele: SHA-256, SHA-3. (MD5 und SHA-1 gelten als gebrochen.)

> [!tip] Passwörter
> Passwörter werden **gehasht**, nicht verschlüsselt – und zwar mit speziellen, absichtlich langsamen Verfahren wie **bcrypt**, **scrypt** oder **Argon2** samt zufälligem **Salt**. So ist selbst bei einem Datenbankleck der Klartext nicht wiederherstellbar.

### Kodierung (Encoding)

**Zweck: KEINE Sicherheit.** Kodierung wandelt Daten lediglich in ein anderes **Darstellungsformat** um, etwa für die Übertragung über Kanäle, die nur bestimmte Zeichen zulassen.

- **Kein Schlüssel**, vollständig und trivial **umkehrbar von jedem**.
- Beispiele: Base64, Hexadezimal, URL-Encoding, ASCII.

> [!danger] Häufigster Anfängerfehler
> Base64 ist **keine** Verschlüsselung! `UGFzc3dvcnQ=` lässt sich von jedem sofort zu `Passwort` zurückwandeln. Kodierung verbirgt nichts – sie dient nur der Darstellung.

### Signierung (Signing)

**Zweck:** Authentizität und Nichtabstreitbarkeit. Eine digitale Signatur belegt, **wer** eine Nachricht erstellt hat und dass sie **unverändert** ist.

- Benötigt ein **asymmetrisches Schlüsselpaar**: Signieren mit dem **privaten** Schlüssel, Prüfen mit dem **öffentlichen**.
- Ablauf: Nachricht hashen → Hash mit privatem Schlüssel signieren → Empfänger prüft mit öffentlichem Schlüssel.
- Beispiele: RSA-Signatur, ECDSA, Ed25519.

```
Signieren:  Signatur = Sign(sk, H(M))
Prüfen:     Verify(pk, M, Signatur)  →  gültig / ungültig
```

### Vergleichstabelle

| Verfahren | Umkehrbar | Schlüssel | Schutzziel |
|-----------|-----------|-----------|------------|
| Verschlüsselung | Ja | Ja | Vertraulichkeit |
| Hashing | Nein | Nein | Integrität |
| Kodierung | Ja | Nein | Keines |
| Signierung | – | Ja (asymm.) | Authentizität |

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Kodierung ≠ Verschlüsselung (häufiger Fehler!)
> - Hashing ist eine Einwegfunktion
> - Signieren = Hashen + mit privatem Schlüssel verschlüsseln

---

## Übungen

1. Warum ist Base64 keine Verschlüsselung?
2. Erklären Sie, warum man Passwörter hasht statt verschlüsselt

---

← [[03-Schutzziele|← Zurück]] | [[00-Einfuehrung-Index|Übersicht]] | [[05-Kryptographische-Angriffsmodelle|Weiter →]]
