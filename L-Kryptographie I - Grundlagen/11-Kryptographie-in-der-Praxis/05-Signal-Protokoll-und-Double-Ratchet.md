---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - praxis
---

# Signal-Protokoll und Double Ratchet

> [!info] **Lernziele**
> - Das Signal-Protokoll als modernes E2EE-Verfahren einordnen
> - Das Double-Ratchet-Prinzip verstehen
> - Forward Secrecy und Post-Compromise Security kennen

---

## Inhalt

### Das Signal-Protokoll

Das **Signal-Protokoll** ist der De-facto-Standard für Ende-zu-Ende-verschlüsselte Messenger (Signal, WhatsApp, u. a.). Es kombiniert mehrere moderne Bausteine und bietet starke Sicherheitsgarantien auch bei langfristiger, asynchroner Kommunikation.

### X3DH – der initiale Handshake

Zu Beginn vereinbaren die Teilnehmer per **X3DH (Extended Triple Diffie-Hellman)** ein gemeinsames Geheimnis – mehrere ECDH-Schritte (→ [[05-ECDH-und-X25519]]) über Identitäts-, signierte und einmalige Pre-Keys. Das funktioniert auch **asynchron**: Der Empfänger muss nicht online sein.

### Double Ratchet

Danach sorgt der **Double Ratchet** für fortlaufende Schlüsselerneuerung. Zwei „Ratchets" (Sperrklinken) greifen ineinander:

| Ratchet | Funktion |
|---------|----------|
| **Symmetric-Key Ratchet** | leitet für **jede Nachricht** einen neuen Schlüssel ab (per KDF) |
| **DH Ratchet** | tauscht bei jeder Antwort neue DH-Schlüssel aus |

Jeder Nachrichtenschlüssel wird nach Gebrauch verworfen.

### Die zwei starken Garantien

> [!tip] **Forward Secrecy + Post-Compromise Security**
> - **Forward Secrecy:** Wird ein aktueller Schlüssel kompromittiert, bleiben **vergangene** Nachrichten sicher (alte Schlüssel sind gelöscht).
> - **Post-Compromise Security (Self-Healing):** Nach einer Kompromittierung „heilt" sich die Sitzung durch den DH-Ratchet selbst – **zukünftige** Nachrichten werden wieder sicher, sobald ein frischer DH-Austausch stattfand.
>
> Diese Kombination ist die besondere Stärke des Double Ratchet.

### Bausteine

Signal nutzt durchweg moderne Primitive: **X25519** (Schlüsselaustausch), **AES-256 / ChaCha20** (Verschlüsselung), **HMAC-SHA-256** (Authentisierung) und **HKDF** (Schlüsselableitung).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Signal-Protokoll: moderner E2EE-Standard, auch asynchron (X3DH-Handshake)
> - Double Ratchet: Symmetric-Key- und DH-Ratchet erneuern Schlüssel pro Nachricht/Antwort
> - Bietet Forward Secrecy **und** Post-Compromise Security (Self-Healing)
> - Baut auf X25519, AES/ChaCha20, HMAC-SHA-256 und HKDF

---

## Übungen

1. Wozu dient der X3DH-Handshake, und warum ist er asynchron möglich?
2. Welche zwei Ratchets bilden den Double Ratchet und was tun sie?
3. Erklären Sie den Unterschied zwischen Forward Secrecy und Post-Compromise Security.

---

← [[04-Ende-zu-Ende-Verschluesselung|← Zurück]] | [[00-Praxis-Index|Übersicht]] | [[06-Datenbankverschluesselung|Weiter →]]
