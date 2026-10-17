---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - pqc
---

# Post-Quanten-Kryptographie Überblick

> [!info] **Lernziele**
> - Das Ziel der Post-Quanten-Kryptographie verstehen
> - Die Familien quantenresistenter Verfahren kennen
> - Den NIST-Standardisierungsprozess einordnen

---

## Inhalt

### Was ist PQC?

**Post-Quanten-Kryptographie (PQC)** umfasst kryptographische Verfahren, die auf **klassischen** Computern laufen, aber auch gegen **Quantencomputer** sicher sind. Sie beruhen auf mathematischen Problemen, für die **kein** effizienter Quantenalgorithmus bekannt ist (anders als bei Faktorisierung/diskretem Logarithmus).

> [!note] **PQC ≠ Quantenkryptographie**
> - **PQC:** klassische Algorithmen, quantenresistent (Thema dieses Moduls).
> - **Quantenkryptographie / QKD:** nutzt selbst Quantenphysik (z. B. Quantenschlüsselaustausch) – spezielle Hardware, anderes Feld.

### Familien quantenresistenter Verfahren

| Familie | Grundlage | Beispiel |
|---------|-----------|----------|
| **Gitterbasiert** | Lattice-Probleme (LWE/SIS) | ML-KEM, ML-DSA (→ [[05-Gitterbasierte-Kryptographie]]) |
| **Hash-basiert** | Sicherheit von Hashfunktionen | SLH-DSA (→ [[08-SLH-DSA-FIPS-205]]) |
| **Code-basiert** | Fehlerkorrigierende Codes | Classic McEliece |
| **Multivariat** | multivariate Gleichungssysteme | (diverse, teils gebrochen) |
| **Isogenie-basiert** | Isogenien elliptischer Kurven | SIKE (2022 gebrochen!) |

Gitterbasierte Verfahren haben sich als vielseitigster Ansatz durchgesetzt.

### Der NIST-Prozess

Das **NIST** führte ab 2016 einen offenen Wettbewerb durch. 2024 wurden die ersten Standards veröffentlicht:

- **FIPS 203 – ML-KEM** (Kyber): Schlüsselkapselung (→ [[06-ML-KEM-FIPS-203]])
- **FIPS 204 – ML-DSA** (Dilithium): Signatur (→ [[07-ML-DSA-FIPS-204]])
- **FIPS 205 – SLH-DSA** (SPHINCS+): Hash-basierte Signatur (→ [[08-SLH-DSA-FIPS-205]])

> [!warning] **Vorsicht ist Teil des Prozesses**
> Der Bruch von **SIKE** (2022) – ein zuvor aussichtsreicher Isogenie-Kandidat – zeigt, dass PQC-Verfahren noch jung sind. Deshalb empfiehlt sich oft ein **hybrider** Einsatz (klassisch + PQC, → [[09-Hybride-kryptographische-Verfahren]]), um nicht allein auf ein neues Verfahren zu setzen.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - PQC: klassische, aber quantenresistente Verfahren (nicht zu verwechseln mit QKD)
> - Familien: gitter-, hash-, code-, multivariat-, isogeniebasiert
> - NIST-Standards 2024: ML-KEM (203), ML-DSA (204), SLH-DSA (205)
> - PQC ist jung (SIKE-Bruch 2022) → hybride Nutzung empfohlen

---

## Übungen

1. Worin unterscheidet sich PQC von Quantenkryptographie (QKD)?
2. Nennen Sie drei Familien quantenresistenter Verfahren.
3. Welche drei Algorithmen hat NIST 2024 standardisiert?

---

← [[03-Auswirkungen-auf-RSA-und-ECC|← Zurück]] | [[00-PQC-Index|Übersicht]] | [[05-Gitterbasierte-Kryptographie|Weiter →]]
