---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - hash
---

# Message Authentication Codes MAC HMAC

> [!info] **Lernziele**
> - Zweck und Funktionsweise eines MAC verstehen
> - HMAC als sichere Konstruktion kennen
> - MAC von digitaler Signatur abgrenzen

---

## Inhalt

### Was ist ein MAC?

Ein **Message Authentication Code (MAC)** ist ein kurzes Prüf-Tag, das mit einem **geheimen Schlüssel** über eine Nachricht berechnet wird. Er sichert gleichzeitig:

- **Integrität:** Die Nachricht wurde nicht verändert.
- **Authentizität:** Sie stammt von jemandem, der den geheimen Schlüssel kennt.

$$t = \text{MAC}(K, m)$$

Der Empfänger berechnet den MAC erneut und vergleicht ihn. Da ein Angreifer ohne $K$ keinen gültigen MAC erzeugen kann, werden Manipulationen erkannt.

### Warum nicht einfach ein Hash?

Ein reiner Hash $H(m)$ schützt nicht vor einem aktiven Angreifer – er kann Nachricht **und** Hash gemeinsam austauschen. Ein MAC benötigt den geheimen Schlüssel und verhindert das.

> [!danger] **Nicht naiv `H(K ‖ m)` verwenden**
> Bei Merkle-Damgård-Hashes (SHA-2) ist $\text{MAC} = H(K \,\|\, m)$ durch **Length-Extension** angreifbar (→ [[02-SHA-2-und-SHA-3]]). Deshalb nutzt man die bewährte HMAC-Konstruktion.

### HMAC

**HMAC** (Hash-based MAC, RFC 2104) baut aus einer beliebigen Hashfunktion einen sicheren MAC – mit zwei verschachtelten Hash-Durchläufen und zwei aus dem Schlüssel abgeleiteten Paddings (ipad, opad):

$$\text{HMAC}(K, m) = H\big((K \oplus opad) \,\|\, H((K \oplus ipad) \,\|\, m)\big)$$

Die doppelte Schachtelung macht HMAC **immun gegen Length-Extension**, selbst mit SHA-2. Verbreitet sind HMAC-SHA-256 und HMAC-SHA-512.

### MAC vs. digitale Signatur

| Merkmal | MAC/HMAC | Digitale Signatur |
|---------|----------|-------------------|
| Schlüssel | gemeinsamer geheimer | Schlüsselpaar (privat/öffentlich) |
| Prüfbar durch | nur Schlüsselinhaber | jeden (öffentlicher Schlüssel) |
| Nichtabstreitbarkeit | **nein** | **ja** |
| Geschwindigkeit | sehr schnell | langsamer |

Da beim MAC beide Seiten denselben Schlüssel kennen, kann keiner beweisen, wer das Tag erzeugt hat – daher **keine Nichtabstreitbarkeit**. Diese liefert nur die digitale Signatur (→ Modul 7).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - MAC sichert Integrität + Authentizität mit einem geheimen Schlüssel
> - Reiner Hash genügt nicht; `H(K‖m)` ist bei SHA-2 angreifbar (Length-Extension)
> - HMAC ist die sichere Standardkonstruktion (immun gegen Length-Extension)
> - MAC bietet keine Nichtabstreitbarkeit – dafür braucht es Signaturen

---

## Übungen

1. Welche zwei Schutzziele erfüllt ein MAC?
2. Warum ist $H(K \,\|\, m)$ mit SHA-256 unsicher, HMAC-SHA-256 aber nicht?
3. Warum bietet ein MAC keine Nichtabstreitbarkeit?

---

← [[04-Kollisionsresistenz-und-Preimage-Resistenz|← Zurück]] | [[00-Hashfunktionen-Index|Übersicht]] | [[06-Passwort-Hashing-PBKDF2-bcrypt-scrypt-Argon2id|Weiter →]]
