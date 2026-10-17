---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - symmetrisch
---

# Authenticated Encryption AEAD

> [!info] **Lernziele**
> - Das Konzept von Authenticated Encryption (AEAD) verstehen
> - Erkennen, warum reine Verschlüsselung ohne Integrität unsicher ist
> - Die Rolle der „Associated Data" und gängige AEAD-Verfahren kennen

---

## Inhalt

### Warum Authentizität zur Verschlüsselung gehört

Reine Verschlüsselung schützt die **Vertraulichkeit**, aber nicht die **Integrität**. Ein Angreifer kann den Chiffretext verändern, ohne den Schlüssel zu kennen – etwa im CTR-Modus gezielt einzelne Bits kippen, die sich direkt auf den Klartext auswirken. Ohne Integritätsschutz bleiben solche Manipulationen unbemerkt und ermöglichen Angriffe wie das **Padding-Oracle** (→ Modul 12).

### AEAD – Authenticated Encryption with Associated Data

**AEAD** verbindet Verschlüsselung und Authentisierung in **einer** Operation und garantiert:

- **Vertraulichkeit** der verschlüsselten Daten
- **Integrität und Authentizität** von Chiffretext **und** optionalen Zusatzdaten

Die Ver- und Entschlüsselung liefert neben dem Chiffretext ein **Authentisierungs-Tag**. Beim Entschlüsseln wird das Tag geprüft; schlägt die Prüfung fehl, wird **kein** Klartext herausgegeben.

### Associated Data (AD)

Die „Associated Data" sind Daten, die **authentifiziert, aber nicht verschlüsselt** werden – z. B. Paket-Header, die im Klartext lesbar bleiben müssen (Routing), aber nicht manipulierbar sein dürfen.

```
Eingabe:  Schlüssel K, Nonce N, Klartext P, Associated Data A
Ausgabe:  Chiffretext C, Tag T
Prüfung:  Entschlüsseln liefert P nur, wenn T über C und A gültig ist
```

### Encrypt-then-MAC als sicheres Prinzip

Die sichere Reihenfolge lautet **Encrypt-then-MAC**: zuerst verschlüsseln, dann über den **Chiffretext** authentifizieren. AEAD-Verfahren setzen dieses Prinzip intern korrekt um, sodass die fehleranfällige manuelle Kombination von Chiffre und MAC entfällt.

### Gängige AEAD-Verfahren

| Verfahren | Basis |
|-----------|-------|
| **AES-GCM** | AES-CTR + GMAC (→ [[05-Betriebsmodi-ECB-CBC-CTR-GCM]]) |
| **ChaCha20-Poly1305** | ChaCha20 + Poly1305 (→ [[06-ChaCha20-und-ChaCha20-Poly1305]]) |
| AES-CCM | AES-CTR + CBC-MAC |

> [!tip] **Best Practice**
> Verwende für neue Systeme grundsätzlich ein AEAD-Verfahren (AES-GCM oder ChaCha20-Poly1305) statt „nackter" Verschlüsselung. Beachte strikt die Nonce-Eindeutigkeit pro Schlüssel.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Verschlüsselung ohne Integrität erlaubt unbemerkte Manipulation
> - AEAD liefert Vertraulichkeit + Integrität/Authentizität in einer Operation
> - Associated Data werden authentifiziert, aber nicht verschlüsselt
> - Standard-AEADs: AES-GCM und ChaCha20-Poly1305 (Encrypt-then-MAC)

---

## Übungen

1. Warum reicht reine Verschlüsselung ohne Integritätsschutz nicht aus?
2. Wozu dienen die „Associated Data" in einem AEAD-Verfahren?
3. Nennen Sie zwei verbreitete AEAD-Verfahren und ihre Bausteine.

---

← [[06-ChaCha20-und-ChaCha20-Poly1305|← Zurück]] | [[00-Symmetrisch-Index|Übersicht]] | [[08-Padding-Nonces-und-IVs|Weiter →]]
