---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - signaturen
---

# EdDSA und Ed25519

> [!info] **Lernziele**
> - EdDSA und Ed25519 als moderne Signaturverfahren verstehen
> - Die Vorteile gegenüber ECDSA einordnen
> - Den deterministischen Signaturansatz nachvollziehen

---

## Inhalt

### EdDSA

**EdDSA (Edwards-curve Digital Signature Algorithm)** ist ein modernes Signaturschema auf **Twisted-Edwards-Kurven**. Die bekannteste Instanz ist **Ed25519** (über Curve25519), dazu kommt Ed448 für höhere Sicherheit.

### Vorteile gegenüber ECDSA

| Aspekt | ECDSA | EdDSA / Ed25519 |
|--------|-------|-----------------|
| Nonce | externe Zufalls-Nonce nötig | **deterministisch** aus Schlüssel + Nachricht |
| RNG-Abhängigkeit | kritisch (Fehler = Schlüsselverlust) | keine |
| Seitenkanäle | heikel | von Natur aus konstante Zeit |
| Geschwindigkeit | schnell | sehr schnell |

Der entscheidende Vorteil: EdDSA berechnet die Nonce **deterministisch** aus privatem Schlüssel und Nachricht. Damit entfällt die größte ECDSA-Schwachstelle – eine schlechte oder wiederverwendete Nonce (→ [[03-ECDSA]]) kann konstruktionsbedingt nicht auftreten.

### Ed25519 im Detail

- **128 Bit Sicherheitsniveau** bei 32-Byte-Schlüsseln und 64-Byte-Signaturen.
- Hohe Performance, einfache und fehlerarme Implementierung.
- Konstante-Zeit-Operationen → resistent gegen Timing-Seitenkanäle.

### Verbreitung

Ed25519 ist heute die bevorzugte Signatur in **SSH**, **TLS 1.3**, **Signal**, Git-Commit-Signaturen und vielen weiteren Systemen – oft die empfohlene Standardwahl für neue Anwendungen.

> [!tip] **Empfehlung**
> Für neue Signaturen ist **Ed25519** meist die beste Wahl: schnell, sicher und robust gegen Implementierungsfehler. RSA-PSS bzw. ECDSA bleiben relevant, wo Kompatibilität oder Zertifikats-Ökosysteme es erfordern.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - EdDSA nutzt Edwards-Kurven; Ed25519 ist die verbreitete Instanz (128 Bit)
> - Deterministische Nonce → keine RNG-Abhängigkeit, kein Nonce-Reuse-Risiko
> - Konstante-Zeit-Design, sehr schnell, fehlerarm
> - Standardwahl in SSH, TLS 1.3, Signal, Git

---

## Übungen

1. Wodurch vermeidet EdDSA die Nonce-Schwäche von ECDSA?
2. Welche Schlüssel- und Signaturgröße hat Ed25519?
3. In welchen Systemen wird Ed25519 heute eingesetzt?

---

← [[03-ECDSA|← Zurück]] | [[00-Signaturen-Index|Übersicht]] | [[05-Signaturerstellung-und-Verifikation|Weiter →]]
