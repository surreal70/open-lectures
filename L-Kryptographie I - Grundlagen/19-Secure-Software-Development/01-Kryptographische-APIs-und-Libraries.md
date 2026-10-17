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

# Kryptographische APIs und Libraries

> [!info] **Lernziele**
> - Etablierte Krypto-Bibliotheken kennen
> - High-Level- von Low-Level-APIs unterscheiden
> - Das Prinzip „keine eigene Krypto" verinnerlichen

---

## Inhalt

### Keine eigene Krypto implementieren

> [!danger] **Don't roll your own crypto**
> Die wichtigste Regel sicherer Krypto-Entwicklung: Implementiere kryptographische Algorithmen **nicht selbst**. Nutze **etablierte, geprüfte Bibliotheken**. Selbst erfahrene Entwickler bauen subtile, sicherheitskritische Fehler ein (→ [[09-Kryptographische-Implementierungsfehler]]).

### Etablierte Bibliotheken

| Sprache/Umfeld | Empfohlene Bibliotheken |
|----------------|-------------------------|
| C/C++ | **libsodium**, OpenSSL/BoringSSL |
| Python | **cryptography** (pyca), PyNaCl |
| Java | JCA/JCE, Bouncy Castle, Tink |
| Go | `crypto/*` (Standardbibliothek) |
| JavaScript | Web Crypto API, Node `crypto` |
| plattformübergreifend | **Google Tink** |

### High-Level vs. Low-Level

- **High-Level-APIs** (z. B. libsodium `crypto_secretbox`, Tink) treffen **sichere Voreinstellungen**: moderner Algorithmus, korrekte Nonce-Behandlung, AEAD. Der Entwickler kann wenig falsch machen.
- **Low-Level-APIs** (einzelne Primitive, Modi, Padding) bieten Flexibilität, verlagern aber die Verantwortung für korrekte Kombination auf den Entwickler – fehleranfällig.

> [!tip] **Bevorzuge High-Level**
> Wähle wann immer möglich die **High-Level-Schnittstelle**. libsodium und Tink sind gerade dafür entworfen, Missbrauch schwer zu machen (misuse-resistant, → [[02-Sichere-Implementierungsmuster]]).

### Auswahlkriterien für Bibliotheken

- **Aktiv gepflegt** und breit genutzt (zeitnahe Sicherheitsupdates).
- **Auditiert** / gute Reputation.
- **Moderne Verfahren** als Default (AEAD, X25519, Argon2).
- **Klar dokumentiert**, mit sicheren Beispielen.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Niemals eigene Krypto implementieren – geprüfte Bibliotheken nutzen
> - Etabliert: libsodium, pyca/cryptography, Tink, Standardbibliotheken
> - High-Level-APIs mit sicheren Defaults bevorzugen (misuse-resistant)
> - Bibliotheken nach Pflege, Audit, modernen Defaults und Doku auswählen

---

## Übungen

1. Warum sollte man keine eigene Krypto implementieren?
2. Worin unterscheiden sich High-Level- und Low-Level-APIs?
3. Nennen Sie je eine empfohlene Bibliothek für zwei Sprachen Ihrer Wahl.

---

← [[00-SecDev-Index|Übersicht]] | [[02-Sichere-Implementierungsmuster|Weiter →]]
