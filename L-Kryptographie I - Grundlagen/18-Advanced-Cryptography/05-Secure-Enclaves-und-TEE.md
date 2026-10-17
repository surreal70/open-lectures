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

# Secure Enclaves und TEE

> [!info] **Lernziele**
> - Das Konzept eines Trusted Execution Environment verstehen
> - Confidential Computing einordnen
> - Vor- und Nachteile gegenüber HE/MPC kennen

---

## Inhalt

### Was ist ein TEE?

Ein **Trusted Execution Environment (TEE)** ist ein durch die **Hardware** isolierter, geschützter Bereich eines Prozessors (eine **Enclave**), in dem Code und Daten so ausgeführt werden, dass selbst ein privilegierter Angreifer (Betriebssystem, Hypervisor, Cloud-Betreiber) sie **nicht einsehen oder verändern** kann.

Beispiele: **Intel SGX**, **AMD SEV**, **ARM TrustZone**, **AWS Nitro Enclaves**.

### Confidential Computing

> [!tip] **Schutz von Daten „in use"**
> TEEs ermöglichen **Confidential Computing**: die Verarbeitung sensibler Daten im Klartext **innerhalb** der Enclave, während sie nach außen geschützt bleiben. Das adressiert – wie homomorphe Verschlüsselung – den Zustand „in use" (→ [[08-Kryptographie-in-Cloud-Umgebungen]]), aber mit anderem Ansatz.

### Attestation

Ein zentrales Feature ist **Remote Attestation**: Die Enclave kann gegenüber einem entfernten Nutzer **kryptographisch beweisen**, dass sie echt ist und genau den erwarteten Code ausführt – bevor dieser ihr Geheimnisse anvertraut.

### TEE vs. HE/MPC

| Ansatz | Schutzprinzip | Leistung | Vertrauen |
|--------|---------------|----------|-----------|
| **TEE** | Hardware-Isolation | **schnell** (nahe nativer Speed) | Vertrauen in Hardware/Hersteller |
| **HE** | Mathematik | sehr langsam | nur Mathematik |
| **MPC** | Verteilung | langsam, kommunikationsintensiv | keine Einzelpartei |

> [!danger] **TEEs sind nicht unverwundbar**
> Der Preis für die Geschwindigkeit ist ein **Vertrauen in die Hardware**. TEEs waren Ziel realer **Seitenkanalangriffe** (z. B. Foreshadow/L1TF gegen SGX, → [[05-Side-Channel-Angriffe]]). Sie sind ein starkes Werkzeug, aber kein Allheilmittel – rein mathematische Verfahren (HE/MPC) brauchen dieses Hardwarevertrauen nicht.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - TEE: hardwareisolierte Enclave, schützt Code/Daten auch vor privilegierten Angreifern
> - Confidential Computing schützt Daten „in use" bei nahezu nativer Geschwindigkeit
> - Remote Attestation beweist Echtheit und korrekten Code der Enclave
> - Vorteil: schnell; Nachteil: Hardwarevertrauen nötig, Seitenkanal-angreifbar

---

## Übungen

1. Was schützt ein TEE und wogegen?
2. Wozu dient Remote Attestation?
3. Vergleichen Sie TEE und homomorphe Verschlüsselung hinsichtlich Vertrauen und Leistung.

---

← [[04-Threshold-Cryptography|← Zurück]] | [[00-Advanced-Index|Übersicht]] | [[06-Anwendungsfaelle-Advanced-Crypto|Weiter →]]
