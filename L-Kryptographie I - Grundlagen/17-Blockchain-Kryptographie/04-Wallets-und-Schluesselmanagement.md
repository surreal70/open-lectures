---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - blockchain
  - vertiefung
---

# Wallets und Schlüsselmanagement

> [!info] **Lernziele**
> - Verstehen, was eine Wallet kryptographisch ist
> - HD-Wallets und Seed-Phrasen einordnen
> - Verwahrungsarten und Risiken kennen

---

## Inhalt

### Was ist eine Wallet?

Eine **Wallet** speichert keine Coins – diese „liegen" in der Blockchain. Sie verwaltet die **privaten Schlüssel**, mit denen Transaktionen autorisiert werden (→ [[05-Signaturen-in-Kryptowaehrungen]]). Die **Adresse** leitet sich aus dem öffentlichen Schlüssel ab (meist über Hashfunktionen).

```
Seed → privater Schlüssel → öffentlicher Schlüssel → Adresse
```

### HD-Wallets und Seed-Phrase

> [!tip] **Hierarchisch-deterministische Wallets (BIP-32/39)**
> Moderne **HD-Wallets** leiten beliebig viele Schlüssel **deterministisch** aus einem einzigen **Seed** ab. Dieser Seed wird als **Mnemonic/Seed-Phrase** (12–24 Wörter, BIP-39) dargestellt – leicht zu notieren, aber auch leicht zu stehlen.
>
> **Wer die Seed-Phrase hat, kontrolliert alle abgeleiteten Schlüssel und damit das gesamte Guthaben.**

### Verwahrungsarten

| Typ | Beschreibung | Risiko |
|-----|--------------|--------|
| **Hot Wallet** | mit dem Internet verbunden (Software/App) | bequem, aber angreifbar |
| **Cold Wallet** | offline (Hardware-Wallet, Paper) | sicherer, weniger bequem |
| **Custodial** | Dritter (Börse) verwahrt die Schlüssel | Vertrauen in den Anbieter nötig |
| **Non-Custodial** | Nutzer hält Schlüssel selbst | volle Kontrolle, volle Verantwortung |

### Risiken

> [!danger] **Kein Zurück bei Verlust**
> - **Seed-Verlust** → Guthaben unwiederbringlich weg (keine „Passwort vergessen"-Funktion).
> - **Seed-Diebstahl** → sofortiger Totalverlust.
> - **Custodial-Risiko:** „Not your keys, not your coins" – Börsenpleiten/Hacks betrafen Kundengelder.
>
> Hardware-Wallets (ein spezialisiertes Secure Element, vgl. TPM/HSM → Modul 10) schützen den Schlüssel, indem er das Gerät nie verlässt.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Eine Wallet verwaltet private Schlüssel, nicht die Coins selbst
> - HD-Wallets leiten alle Schlüssel aus einem Seed (12–24-Wort-Phrase) ab
> - Verwahrung: hot vs. cold, custodial vs. non-custodial
> - Seed-Verlust/-Diebstahl = Totalverlust; Hardware-Wallets schützen den Schlüssel

---

## Übungen

1. Was verwaltet eine Wallet tatsächlich – und wo liegen die Coins?
2. Welche Bedeutung hat die Seed-Phrase bei einer HD-Wallet?
3. Vergleichen Sie custodial und non-custodial Verwahrung.

---

← [[03-Merkle-Trees-in-Blockchains|← Zurück]] | [[00-Blockchain-Index|Übersicht]] | [[05-Signaturen-in-Kryptowaehrungen|Weiter →]]
