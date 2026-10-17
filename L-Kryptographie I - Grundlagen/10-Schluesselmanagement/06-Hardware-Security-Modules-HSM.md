---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - schluessel
---

# Hardware Security Modules HSM

> [!info] **Lernziele**
> - Funktion und Zweck eines HSM verstehen
> - Die Sicherheitsvorteile gegenüber Software-Schlüsseln einordnen
> - Typische Einsatzgebiete und Zertifizierungen kennen

---

## Inhalt

### Was ist ein HSM?

Ein **Hardware Security Module (HSM)** ist ein dediziertes, manipulationssicheres Hardwaregerät, das kryptographische Schlüssel erzeugt, speichert und verwendet. Das zentrale Prinzip:

> [!tip] **Der Schlüssel verlässt das HSM nie**
> Schlüssel werden **innerhalb** des HSM erzeugt und nutzen es nie im Klartext nach außen. Anwendungen senden Daten **zum** HSM, das dort signiert/entschlüsselt und nur das Ergebnis zurückgibt. Selbst ein kompromittierter Host kann den Schlüssel nicht auslesen.

### Sicherheitsmerkmale

- **Tamper-Resistance:** physische Manipulationsversuche führen zur Löschung der Schlüssel (Zeroization).
- **Zugriffskontrolle:** mehrstufige Authentifizierung, oft „m-of-n"-Freigaben.
- **Hohe Performance:** dedizierte Krypto-Hardware für viele Operationen/Sekunde.
- **Auditing:** protokollierte Nutzung.

### Einsatzgebiete

- Schutz von **Root-CA-Schlüsseln** in einer PKI (→ Modul 8).
- Signatur- und Zahlungsinfrastruktur (z. B. Code Signing, Kartenzahlungen).
- Als Vertrauensanker für Cloud-KMS (→ [[08-Cloud-Key-Management-Services-KMS]]).

### Standards und Anbindung

- **Zertifizierung:** **FIPS 140-3** (bzw. 140-2) und Common Criteria stufen die Sicherheit ein (→ Modul 14).
- **Schnittstelle:** oft über **PKCS#11** oder herstellerspezifische APIs.

### HSM vs. TPM

| Merkmal | HSM | TPM |
|---------|-----|-----|
| Formfaktor | Appliance/Karte, oft im Rechenzentrum | Chip im einzelnen Gerät |
| Leistung | hoch, viele Operationen | gering, pro Gerät |
| Zweck | zentrale, geteilte Krypto-Dienste | Geräte-Identität/-Integrität (→ [[07-Trusted-Platform-Module-TPM]]) |

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - HSM: manipulationssichere Hardware für Schlüsselerzeugung und -nutzung
> - Schlüssel verlassen das HSM nie – selbst ein kompromittierter Host kommt nicht heran
> - Einsatz: CA-Schlüssel, Signatur-/Zahlungsinfrastruktur, KMS-Anker
> - Zertifiziert nach FIPS 140-3; Anbindung meist über PKCS#11

---

## Übungen

1. Was ist das zentrale Sicherheitsprinzip eines HSM?
2. Was geschieht bei einem physischen Manipulationsversuch?
3. Worin unterscheiden sich HSM und TPM?

---

← [[05-Key-Rotation-und-Key-Revocation|← Zurück]] | [[00-Schluessel-Index|Übersicht]] | [[07-Trusted-Platform-Module-TPM|Weiter →]]
