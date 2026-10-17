---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - pqc
---

# ML-DSA FIPS-204

> [!info] **Lernziele**
> - ML-DSA (FIPS 204) als quantenresistente Signatur verstehen
> - Die Einordnung als gitterbasiertes Verfahren kennen
> - ML-DSA von SLH-DSA abgrenzen

---

## Inhalt

### Was ist ML-DSA?

**ML-DSA (Module-Lattice-Based Digital Signature Algorithm)**, standardisiert als **FIPS 204** (2024) und hervorgegangen aus **CRYSTALS-Dilithium**, ist das primäre NIST-Standardverfahren für **quantenresistente digitale Signaturen**. Es ersetzt perspektivisch RSA-PSS und ECDSA/EdDSA.

### Grundlage und Eigenschaften

ML-DSA beruht wie ML-KEM auf **Gitterproblemen** (Module-LWE/SIS, → [[05-Gitterbasierte-Kryptographie]]) und nutzt das **Fiat-Shamir-with-Aborts**-Paradigma.

- **Deterministisch oder randomisiert** signierbar.
- Gute Performance bei Signieren und Verifizieren.
- Schlüssel und Signaturen im **Kilobyte-Bereich** (größer als Ed25519, aber praktikabel).

| Variante | Sicherheitsniveau (ca.) |
|----------|-------------------------|
| ML-DSA-44 | ~AES-128 |
| ML-DSA-65 | ~AES-192 |
| ML-DSA-87 | ~AES-256 |

### ML-DSA vs. SLH-DSA

> [!note] **Zwei standardisierte Signaturverfahren**
> - **ML-DSA** (gitterbasiert): die **empfohlene Standardwahl** – schnell, kompakter.
> - **SLH-DSA** (hash-basiert, → [[08-SLH-DSA-FIPS-205]]): konservativere Alternative mit sehr gut verstandener Sicherheit, aber größeren/langsameren Signaturen.
>
> ML-DSA wird meist bevorzugt; SLH-DSA dient als Rückfalloption, falls sich gitterbasierte Annahmen als schwächer erweisen.

### Einsatz

ML-DSA eignet sich für Zertifikate, Code Signing und Protokolle. Wie bei ML-KEM wird in Übergangsphasen ein **hybrider** Einsatz (klassisch + PQC) empfohlen (→ [[09-Hybride-kryptographische-Verfahren]]).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - ML-DSA (FIPS 204, aus Dilithium) ist der primäre NIST-Standard für PQC-Signaturen
> - Gitterbasiert (Module-LWE/SIS), Fiat-Shamir-with-Aborts, gute Performance
> - Varianten 44/65/87 ≈ AES-128/192/256; Schlüssel/Signaturen im KB-Bereich
> - Standardwahl gegenüber dem konservativeren, aber größeren SLH-DSA

---

## Übungen

1. Aus welchem Verfahren ging ML-DSA hervor und worauf beruht es?
2. Worin unterscheiden sich ML-DSA und SLH-DSA?
3. Warum empfiehlt sich in der Übergangsphase ein hybrider Einsatz?

---

← [[06-ML-KEM-FIPS-203|← Zurück]] | [[00-PQC-Index|Übersicht]] | [[08-SLH-DSA-FIPS-205|Weiter →]]
