---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - advanced
  - vertiefung
---

# Threshold Cryptography

> [!info] **Lernziele**
> - Das Prinzip der Threshold-Kryptographie verstehen
> - Threshold-Signaturen einordnen
> - Den Nutzen gegenüber einfachem Multisig erkennen

---

## Inhalt

### Die Grundidee

**Threshold-Kryptographie** verteilt eine kryptographische Fähigkeit (z. B. das Signieren oder Entschlüsseln) auf **mehrere Parteien**, sodass eine definierte Mindestzahl **$t$ von $n$** zusammenwirken muss. Kein Einzelner besitzt den vollständigen privaten Schlüssel.

```
(t, n)-Schema:  n Anteile, t müssen kooperieren
z. B. (3, 5): 3 von 5 Parteien signieren gemeinsam
```

Dies baut auf **Secret Sharing** (→ [[09-Secret-Sharing-und-Backup-Konzepte]]) auf, geht aber weiter: Der Schlüssel wird nie **rekonstruiert**, sondern die Operation wird **verteilt** ausgeführt.

### Threshold-Signaturen

> [!tip] **Der Schlüssel existiert nie an einem Ort**
> Bei einer **Threshold-Signatur** erzeugen $t$ Parteien gemeinsam eine gültige Signatur, ohne dass der private Gesamtschlüssel jemals an einer Stelle vorliegt. Das ist ein entscheidender Sicherheitsgewinn: Es gibt **keinen Single Point of Failure**, an dem der Schlüssel gestohlen werden könnte.

### Threshold vs. einfaches Multisig

| Aspekt | Klassisches Multisig | Threshold-Signatur |
|--------|----------------------|--------------------|
| Signatur | mehrere Einzelsignaturen | **eine** gemeinsame Signatur |
| Schlüssel | mehrere separate Schlüssel | ein verteilter Schlüssel |
| Sichtbarkeit | Signierende on-chain erkennbar | von außen wie normale Signatur |
| Effizienz | größer | kompakter |

Threshold-Signaturen wirken nach außen wie eine **normale** Signatur – das verbessert Privatsphäre und Effizienz gegenüber on-chain-Multisig.

### Anwendungen

- **Wallet-Sicherheit / Custody:** Schutz großer Krypto-Bestände (keine einzelne Person kann allein Geld bewegen).
- **CA-/Root-Schlüsselschutz:** verteilte Kontrolle über besonders kritische Schlüssel (→ [[06-Hardware-Security-Modules-HSM]]).
- **Verteilte Schlüsselerzeugung (DKG).**

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Threshold-Kryptographie verteilt eine Operation auf $t$ von $n$ Parteien
> - Der private Schlüssel wird nie an einem Ort rekonstruiert → kein Single Point of Failure
> - Threshold-Signaturen erzeugen eine kompakte gemeinsame Signatur (effizienter als Multisig)
> - Anwendungen: Custody, CA-Schlüsselschutz, verteilte Schlüsselerzeugung

---

## Übungen

1. Was bedeutet ein (t,n)-Threshold-Schema?
2. Welchen Sicherheitsvorteil bietet eine Threshold-Signatur?
3. Worin unterscheidet sie sich von klassischem Multisig?

---

← [[03-Multi-Party-Computation-MPC|← Zurück]] | [[00-Advanced-Index|Übersicht]] | [[05-Secure-Enclaves-und-TEE|Weiter →]]
