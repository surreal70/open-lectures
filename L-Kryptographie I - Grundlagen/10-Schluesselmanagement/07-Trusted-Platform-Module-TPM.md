---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - schluessel
---

# Trusted Platform Module TPM

> [!info] **Lernziele**
> - Funktion eines TPM verstehen
> - Typische Anwendungsfälle kennen
> - Den Unterschied zum HSM einordnen

---

## Inhalt

### Was ist ein TPM?

Ein **Trusted Platform Module (TPM)** ist ein kleiner, fest verbauter Sicherheitschip (Standard der Trusted Computing Group, aktuell TPM 2.0). Er bietet einem **einzelnen Gerät** einen hardwarebasierten Vertrauensanker: sichere Schlüsselspeicherung, Zufallszahlen und Integritätsmessung.

### Kernfunktionen

- **Schlüsselspeicherung:** private Schlüssel werden im TPM gehalten und verlassen es nicht im Klartext.
- **Platform Configuration Registers (PCRs):** speichern Hashwerte des Bootvorgangs → Grundlage für **Measured Boot / Secure Boot**.
- **Sealing:** Daten werden so verschlüsselt, dass sie nur bei einem bestimmten (unveränderten) Systemzustand wieder entschlüsselt werden können.
- **Attestation:** das TPM kann gegenüber Dritten beweisen, in welchem Zustand das System gebootet wurde.

### Typische Anwendungen

| Anwendung | Rolle des TPM |
|-----------|---------------|
| **Festplattenverschlüsselung** | BitLocker/LUKS binden den Schlüssel an das TPM (→ Modul 11) |
| **Secure/Measured Boot** | Integrität der Boot-Kette prüfen |
| **Geräte-Identität** | eindeutige, hardwaregebundene Identität |
| **Windows 11** | TPM 2.0 ist Systemvoraussetzung |

### TPM vs. HSM

| Merkmal | TPM | HSM |
|---------|-----|-----|
| Umfang | ein Gerät | zentral/geteilt |
| Leistung | niedrig | hoch |
| Kosten | sehr gering (verbaut) | hoch |
| Zweck | Geräteintegrität/-identität | zentrale Krypto-Dienste (→ [[06-Hardware-Security-Modules-HSM]]) |

> [!tip] **Merksatz**
> TPM = Vertrauensanker **im Gerät**; HSM = Hochsicherheits-Krypto-Dienst **für viele**. Beide halten Schlüssel in Hardware, unterscheiden sich aber in Zweck und Skalierung.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - TPM: fest verbauter Sicherheitschip als Vertrauensanker eines Geräts
> - Funktionen: Schlüsselspeicherung, PCRs/Measured Boot, Sealing, Attestation
> - Anwendungen: Festplattenverschlüsselung, Secure Boot, Geräteidentität
> - Unterschied zum HSM: gerätegebunden und klein statt zentral und leistungsstark

---

## Übungen

1. Wozu dienen die PCRs eines TPM?
2. Was bedeutet „Sealing" von Daten an ein TPM?
3. Worin unterscheidet sich ein TPM von einem HSM?

---

← [[06-Hardware-Security-Modules-HSM|← Zurück]] | [[00-Schluessel-Index|Übersicht]] | [[08-Cloud-Key-Management-Services-KMS|Weiter →]]
