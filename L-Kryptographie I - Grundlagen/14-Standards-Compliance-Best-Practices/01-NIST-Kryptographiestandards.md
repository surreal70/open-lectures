---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - standards
---

# NIST-Kryptographiestandards

> [!info] **Lernziele**
> - Rolle und Bedeutung der NIST-Standards verstehen
> - Wichtige FIPS- und SP-Dokumente einordnen
> - Den offenen Standardisierungsprozess würdigen

---

## Inhalt

### Rolle des NIST

Das **National Institute of Standards and Technology (NIST)** der USA ist die weltweit einflussreichste Institution für kryptographische Standards. Seine Dokumente prägen Verfahren, die global eingesetzt werden – von AES bis zur Post-Quanten-Kryptographie.

### Zwei Dokumentreihen

| Reihe | Bedeutung |
|-------|-----------|
| **FIPS** (Federal Information Processing Standards) | verbindliche Standards (für US-Behörden) |
| **SP 800** (Special Publications) | Empfehlungen und Leitlinien |

### Wichtige Standards im Überblick

| Dokument | Inhalt |
|----------|--------|
| **FIPS 197** | AES (→ [[04-Advanced-Encryption-Standard-AES]]) |
| **FIPS 186** | digitale Signaturen (DSA/ECDSA/EdDSA) |
| **FIPS 180 / 202** | SHA-2 / SHA-3 (→ [[02-SHA-2-und-SHA-3]]) |
| **FIPS 198** | HMAC |
| **FIPS 203/204/205** | PQC: ML-KEM, ML-DSA, SLH-DSA (→ Modul 13) |
| **FIPS 140-3** | Sicherheitsanforderungen an Krypto-Module (→ [[03-FIPS-140-3]]) |
| **SP 800-57** | Schlüsselmanagement-Empfehlungen (→ Modul 10) |
| **SP 800-38** | Betriebsmodi (GCM etc.) |
| **SP 800-90A** | Zufallszahlengeneratoren |

### Der offene Prozess

> [!tip] **Vertrauen durch Transparenz**
> NIST wählt Algorithmen zunehmend über **offene, internationale Wettbewerbe** (AES 1997–2001, SHA-3 2007–2015, PQC 2016–2024). Diese öffentliche Begutachtung entspricht Kerckhoffs' Prinzip (→ [[06-Kerckhoffs-Prinzip]]) und schafft Vertrauen. Nach dem Dual_EC_DRBG-Vorfall (Verdacht einer Hintertür) ist Transparenz noch wichtiger geworden.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - NIST setzt global prägende Krypto-Standards (FIPS = verbindlich, SP 800 = Empfehlungen)
> - Kernstandards: AES (197), SHA (180/202), Signaturen (186), PQC (203–205), FIPS 140-3
> - Algorithmen werden über offene Wettbewerbe gewählt
> - Transparenz schafft Vertrauen (besonders nach Dual_EC_DRBG)

---

## Übungen

1. Worin unterscheiden sich FIPS- und SP-800-Dokumente?
2. Welcher FIPS-Standard definiert AES, welcher die PQC-Signaturen?
3. Warum ist der offene Auswahlprozess für das Vertrauen wichtig?

---

← [[00-Standards-Index|Übersicht]] | [[02-BSI-TR-02102|Weiter →]]
