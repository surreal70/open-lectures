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

# Sichere Implementierungsmuster

> [!info] **Lernziele**
> - Bewährte Muster sicherer Krypto-Implementierung kennen
> - Sichere Defaults und misuse-resistente APIs verstehen
> - Verbreitete Antipatterns vermeiden

---

## Inhalt

### Sichere Defaults

Gute Krypto-Implementierungen sind **sicher ohne Zutun**: Die Standardeinstellung ist die sichere. Der Entwickler muss nicht erst Experte werden, um es richtig zu machen.

| Statt… | …sicherer Default |
|--------|-------------------|
| manuell Modus wählen | AEAD (AES-GCM/ChaCha20-Poly1305) |
| Nonce selbst verwalten | Bibliothek erzeugt/prüft Nonce |
| Padding manuell | kein Padding nötig (AEAD/Stream) |
| Algorithmus frei wählbar | moderne Kurve/Hash fest vorgegeben |

### Misuse-resistente APIs

> [!tip] **Schwer falsch zu benutzen**
> Eine gute API macht **Fehler schwer**: Sie verlangt keine gefährlichen Entscheidungen (Modus, IV, Padding) vom Aufrufer. Beispiel libsodium: `crypto_secretbox_easy(message, nonce, key)` – eine Funktion, sichere Primitive, klare Nonce-Regel. Es gibt kaum einen Weg, es unsicher zu nutzen.

### Bewährte Muster

- **Authenticated Encryption immer** (nie „nur verschlüsseln", → [[07-Authenticated-Encryption-AEAD]]).
- **Konstante-Zeit-Vergleiche** für Geheimnisse/MACs (→ [[04-Timing-Angriffe]]).
- **CSPRNG** für alle Zufallswerte (→ [[04-Secure-Random-und-Entropy]]).
- **Schlüssel aus KDF** ableiten, nicht direkt aus Passwörtern (→ [[04-Key-Derivation-Functions-KDF]]).
- **Secrets nicht loggen**, nicht in Exceptions/URLs.
- **Fail closed:** Im Fehlerfall ablehnen, nicht „durchlassen".

### Antipatterns

> [!danger] **Vermeiden**
> - ECB-Modus, Textbook-RSA, statische IV/Nonce.
> - `==` für MAC-/Token-Vergleich.
> - MD5/SHA-1 für Sicherheit; Passwörter mit schnellem Hash.
> - Schlüssel im Code/Repo (hardcoded).
> - „Verschlüsseln" per Base64 (ist Kodierung! → [[04-Verschluesselung-Hashing-Kodierung-Signierung]]).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Sichere Defaults: AEAD, verwaltete Nonces, moderne Verfahren voreingestellt
> - Misuse-resistente APIs verhindern gefährliche Entscheidungen (z. B. libsodium)
> - Muster: AEAD, konstante-Zeit-Vergleich, CSPRNG, KDF, kein Secret-Logging, fail closed
> - Antipatterns: ECB, Textbook-RSA, statische Nonce, `==`-MAC-Vergleich, hardcodierte Schlüssel

---

## Übungen

1. Was bedeutet „misuse-resistant API" an einem Beispiel?
2. Nennen Sie vier bewährte Implementierungsmuster.
3. Listen Sie drei Antipatterns und je deren Gegenmaßnahme auf.

---

← [[01-Kryptographische-APIs-und-Libraries|← Zurück]] | [[00-SecDev-Index|Übersicht]] | [[03-Crypto-Misuse-Patterns|Weiter →]]
