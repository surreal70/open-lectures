---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - symmetrisch
---

# ChaCha20 und ChaCha20-Poly1305

> [!info] **Lernziele**
> - ChaCha20 als moderne Stromchiffre verstehen
> - Die Kombination mit Poly1305 zu einem AEAD-Verfahren nachvollziehen
> - Einordnen, wann ChaCha20-Poly1305 gegenüber AES-GCM vorteilhaft ist

---

## Inhalt

### ChaCha20

**ChaCha20** ist eine moderne **Stromchiffre** von Daniel J. Bernstein (2008), eine Weiterentwicklung von Salsa20. Sie erzeugt aus einem 256-Bit-Schlüssel, einer Nonce und einem Blockzähler einen Schlüsselstrom, der per XOR mit dem Klartext verknüpft wird.

- **Schlüssel:** 256 Bit
- **Nonce:** 96 Bit (in der IETF-Variante, RFC 8439)
- **Aufbau:** 20 Runden aus Additionen, Rotationen und XOR (ARX-Design)

Das ARX-Design kommt ohne Lookup-Tabellen aus und ist dadurch von Natur aus resistent gegen **Cache-Timing-Seitenkanäle** – ein Vorteil gegenüber Software-AES ohne Hardwarebeschleunigung.

### Poly1305

**Poly1305** ist ein **Message Authentication Code (MAC)**: Er berechnet über die verschlüsselten Daten (und optionale Zusatzdaten) ein Authentisierungs-Tag, das Manipulationen erkennbar macht.

### ChaCha20-Poly1305

Die Kombination beider – standardisiert in **RFC 8439** – ergibt ein **AEAD**-Verfahren (→ [[07-Authenticated-Encryption-AEAD]]): Es sichert gleichzeitig Vertraulichkeit (ChaCha20) und Integrität/Authentizität (Poly1305).

### ChaCha20-Poly1305 vs. AES-GCM

| Aspekt | ChaCha20-Poly1305 | AES-GCM |
|--------|-------------------|---------|
| Typ | Stromchiffre + MAC | Blockchiffre (CTR) + GMAC |
| Hardware-Beschleunigung | nicht nötig | AES-NI vorausgesetzt für Top-Speed |
| Software-Performance | sehr schnell | langsamer ohne AES-NI |
| Seitenkanäle | robust (keine Tabellen) | heikel ohne Hardware |

In der Praxis wird ChaCha20-Poly1305 bevorzugt auf Geräten **ohne** AES-Hardware (viele Mobilgeräte). Es ist fester Bestandteil von **TLS 1.3** und wird u. a. von WireGuard genutzt.

> [!danger] **Nonce-Eindeutigkeit**
> Wie bei jeder Stromchiffre zerstört eine wiederverwendete Nonce bei gleichem Schlüssel die Sicherheit vollständig. Die 96-Bit-Nonce muss pro Schlüssel eindeutig sein.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - ChaCha20: moderne ARX-Stromchiffre (256-Bit-Schlüssel, 96-Bit-Nonce)
> - Poly1305: MAC zur Integritätssicherung
> - Kombination = AEAD (RFC 8439), Teil von TLS 1.3 und WireGuard
> - Vorteil ohne AES-Hardware und gegen Cache-Timing; Nonce muss eindeutig bleiben

---

## Übungen

1. Warum ist ChaCha20 resistenter gegen Cache-Timing-Angriffe als Software-AES?
2. Welche beiden Schutzziele deckt ChaCha20-Poly1305 ab?
3. In welchem Szenario würden Sie ChaCha20-Poly1305 statt AES-GCM wählen?

---

← [[05-Betriebsmodi-ECB-CBC-CTR-GCM|← Zurück]] | [[00-Symmetrisch-Index|Übersicht]] | [[07-Authenticated-Encryption-AEAD|Weiter →]]
