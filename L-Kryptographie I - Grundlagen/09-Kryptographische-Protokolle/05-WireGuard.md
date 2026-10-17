---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - protokolle
---

# WireGuard

> [!info] **Lernziele**
> - WireGuard als modernes VPN-Protokoll verstehen
> - Die fest gewählten kryptographischen Bausteine kennen
> - Die Vorteile gegenüber IPsec/OpenVPN einordnen

---

## Inhalt

### Was ist WireGuard?

**WireGuard** ist ein modernes, bewusst **minimalistisches** VPN-Protokoll (seit 2020 im Linux-Kernel). Sein Leitgedanke: maximale Einfachheit bei maximaler Sicherheit. Der gesamte Code ist um Größenordnungen kleiner als bei IPsec oder OpenVPN, was die Angriffsfläche und Fehleranfälligkeit drastisch senkt.

### Feste kryptographische Primitive

Anders als IPsec/TLS verhandelt WireGuard **keine** Algorithmen aus, sondern legt sie fest (keine „Cipher Agility"):

| Zweck | Verfahren |
|-------|-----------|
| Schlüsselaustausch | **Curve25519** (ECDH, → [[05-ECDH-und-X25519]]) |
| Verschlüsselung | **ChaCha20-Poly1305** (AEAD, → [[06-ChaCha20-und-ChaCha20-Poly1305]]) |
| Hash | **BLAKE2s** (→ [[03-BLAKE2-und-BLAKE3]]) |
| Handshake-Rahmen | **Noise Protocol Framework** |

> [!tip] **Warum keine Algorithmenverhandlung?**
> Verhandelbare Verfahren (wie in TLS 1.2) sind eine häufige Quelle für Downgrade-Angriffe und Komplexität. WireGuard wählt stattdessen eine feste, moderne Suite. Muss ein Verfahren ersetzt werden, geschieht das über eine neue Protokollversion – ein bewusster Verzicht auf Flexibilität zugunsten von Einfachheit und Sicherheit.

### Eigenschaften

- **Perfect Forward Secrecy** durch regelmäßige neue Handshakes (→ [[06-Perfect-Forward-Secrecy]]).
- **Sehr schnell**, auch dank ChaCha20 ohne AES-Hardware.
- **Einfache Konfiguration:** jeder Peer hat ein Schlüsselpaar; erlaubte IPs werden explizit zugeordnet.
- **Stealth:** antwortet nicht auf unauthentifizierte Pakete (schwer zu scannen).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - WireGuard ist ein minimalistisches, modernes VPN mit kleiner Codebasis
> - Feste Primitive: Curve25519, ChaCha20-Poly1305, BLAKE2s, Noise-Framework
> - Keine Algorithmenverhandlung → weniger Angriffsfläche, keine Downgrades
> - Schnell, einfach konfigurierbar, mit Forward Secrecy

---

## Übungen

1. Welche vier kryptographischen Bausteine nutzt WireGuard fest?
2. Welchen Vorteil bietet der Verzicht auf Algorithmenverhandlung?
3. Wie erreicht WireGuard Perfect Forward Secrecy?

---

← [[04-IPsec-und-VPN-Protokolle|← Zurück]] | [[00-Protokolle-Index|Übersicht]] | [[06-Perfect-Forward-Secrecy|Weiter →]]
