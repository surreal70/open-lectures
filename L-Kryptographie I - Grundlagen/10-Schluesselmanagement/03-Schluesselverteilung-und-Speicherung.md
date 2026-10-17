---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - schluessel
---

# Schlüsselverteilung und Speicherung

> [!info] **Lernziele**
> - Methoden zur sicheren Schlüsselverteilung kennen
> - Sichere und unsichere Speicherorte unterscheiden
> - Das Konzept der Schlüsselhierarchie (KEK/DEK) verstehen

---

## Inhalt

### Schlüsselverteilung

Wie gelangt ein Schlüssel sicher zum Empfänger?

| Methode | Beschreibung |
|---------|--------------|
| **Asymmetrischer Austausch** | Diffie-Hellman/ECDH (→ [[03-Diffie-Hellman-Schlüsselaustausch]]) |
| **Schlüsselkapselung** | symmetrischen Schlüssel mit RSA-OAEP kapseln (→ [[06-RSA-OAEP-und-hybride-Verschlüsselung]]) |
| **Out-of-band** | über einen separaten, vertrauenswürdigen Kanal |
| **Pre-Shared Key** | vorab manuell verteilt (kleine, geschlossene Systeme) |

### Sichere Speicherung

> [!danger] **Wo Schlüssel NICHT hingehören**
> - Im Quellcode oder in Git-Repositories (hardcoded).
> - Im Klartext in Konfigurationsdateien oder Logs.
> - In Umgebungsvariablen ohne Zugriffsschutz (nur bedingt akzeptabel).

Sichere Alternativen:

| Ort | Eignung |
|-----|---------|
| **HSM** | höchste Sicherheit, Schlüssel verlässt Hardware nie (→ [[06-Hardware-Security-Modules-HSM]]) |
| **TPM** | hardwaregebunden pro Gerät (→ [[07-Trusted-Platform-Module-TPM]]) |
| **Cloud-KMS** | verwaltete Schlüssel, Zugriff per API/IAM (→ [[08-Cloud-Key-Management-Services-KMS]]) |
| **Secret Manager / Vault** | Vault, AWS Secrets Manager etc. |
| **OS-Keystore** | Keychain, Windows DPAPI |

### Schlüsselhierarchie: KEK und DEK

Ein bewährtes Muster trennt Schlüssel in zwei Ebenen:

- **DEK (Data Encryption Key):** verschlüsselt die eigentlichen Daten.
- **KEK (Key Encryption Key):** verschlüsselt den DEK ("Envelope Encryption").

```
Daten  ──verschlüsselt mit──►  DEK
DEK    ──verschlüsselt mit──►  KEK (im HSM/KMS)
```

Vorteil: Nur der KEK muss im HSM/KMS besonders geschützt werden; der verschlüsselte DEK kann bei den Daten liegen. Eine Rotation des KEK erfordert nicht, alle Daten neu zu verschlüsseln.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Verteilung sicher per asymmetrischem Austausch, Kapselung oder out-of-band
> - Schlüssel niemals im Code/Klartext speichern; HSM, TPM, KMS, Vault nutzen
> - Envelope Encryption trennt DEK (Daten) und KEK (schützt DEK)
> - Der KEK liegt besonders geschützt im HSM/KMS

---

## Übungen

1. Nennen Sie zwei sichere Methoden der Schlüsselverteilung.
2. Warum dürfen Schlüssel nicht im Git-Repository liegen?
3. Erklären Sie den Unterschied zwischen DEK und KEK.

---

← [[02-Sichere-Schluesselgenerierung|← Zurück]] | [[00-Schluessel-Index|Übersicht]] | [[04-Key-Derivation-Functions-KDF|Weiter →]]
