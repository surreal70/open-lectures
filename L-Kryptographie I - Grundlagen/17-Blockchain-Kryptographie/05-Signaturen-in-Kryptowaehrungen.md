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

# Signaturen in Kryptowährungen

> [!info] **Lernziele**
> - Die Rolle digitaler Signaturen in Kryptowährungen verstehen
> - Verwendete Signaturverfahren einordnen
> - Die Bedeutung korrekter Nonces erkennen

---

## Inhalt

### Signaturen autorisieren Transaktionen

In einer Kryptowährung gibt es keine zentrale Bank, die Transaktionen genehmigt. Stattdessen **signiert** der Besitzer jede Transaktion mit seinem **privaten Schlüssel** (→ Modul 7). Jeder im Netzwerk kann die Signatur mit dem zugehörigen öffentlichen Schlüssel prüfen. So ist belegt: Nur der rechtmäßige Eigentümer konnte die Transaktion autorisieren.

### Verwendete Verfahren

| Währung | Signaturverfahren |
|---------|-------------------|
| **Bitcoin** | ECDSA (secp256k1), neuere auch Schnorr (Taproot) |
| **Ethereum** | ECDSA (secp256k1) |
| **viele neuere** | Ed25519 (→ [[04-EdDSA-und-Ed25519]]) |

### Die Gefahr der Nonce

> [!danger] **Nonce-Fehler = gestohlene Coins**
> Bitcoin/Ethereum nutzen **ECDSA**, das für jede Signatur eine zufällige **Nonce** braucht. Eine wiederverwendete oder vorhersagbare Nonce erlaubt es, den **privaten Schlüssel** aus zwei Signaturen zu berechnen (→ [[03-ECDSA]]). Genau so wurden reale Wallets geleert. Moderne Implementierungen nutzen **deterministische Nonces (RFC 6979)**.

### Schnorr-Signaturen (Taproot)

> [!tip] **Vorteile von Schnorr**
> Bitcoins Taproot-Upgrade brachte **Schnorr-Signaturen**: Sie erlauben **Signatur-Aggregation** (mehrere Signaturen zu einer zusammenfassen) – das verbessert Privatsphäre und Effizienz (z. B. bei Multisig). Schnorr ist zudem mathematisch einfacher und beweisbar sicher.

### Multisignatur

Viele Wallets nutzen **Multisig** („m-of-n"): Eine Transaktion braucht mehrere Signaturen (z. B. 2 von 3 Schlüsseln). Das erhöht die Sicherheit (kein Single Point of Failure) – verwandt mit Secret Sharing (→ [[09-Secret-Sharing-und-Backup-Konzepte]]).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Transaktionen werden mit dem privaten Schlüssel signiert und sind öffentlich prüfbar
> - Bitcoin/Ethereum nutzen ECDSA (secp256k1), neuere Systeme Ed25519/Schnorr
> - Nonce-Fehler bei ECDSA können den privaten Schlüssel offenlegen (RFC 6979 nutzen)
> - Schnorr (Taproot) erlaubt Signatur-Aggregation; Multisig erhöht die Sicherheit

---

## Übungen

1. Welche Funktion haben Signaturen in einer Kryptowährung?
2. Warum ist eine fehlerhafte ECDSA-Nonce besonders gefährlich?
3. Welchen Vorteil bieten Schnorr-Signaturen gegenüber ECDSA?

---

← [[04-Wallets-und-Schluesselmanagement|← Zurück]] | [[00-Blockchain-Index|Übersicht]] | [[06-Konsensalgorithmen-und-Kryptographie|Weiter →]]
