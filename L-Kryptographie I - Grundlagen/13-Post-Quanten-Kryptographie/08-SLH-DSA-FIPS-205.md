---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - pqc
---

# SLH-DSA FIPS-205

> [!info] **Lernziele**
> - SLH-DSA (FIPS 205) als hash-basierte Signatur verstehen
> - Die konservative Sicherheitsannahme einordnen
> - Vor- und Nachteile gegenüber ML-DSA kennen

---

## Inhalt

### Was ist SLH-DSA?

**SLH-DSA (Stateless Hash-Based Digital Signature Algorithm)**, standardisiert als **FIPS 205** (2024) und hervorgegangen aus **SPHINCS+**, ist eine **hash-basierte** quantenresistente Signatur. Ihre Besonderheit: Sie beruht **ausschließlich** auf der Sicherheit kryptographischer Hashfunktionen.

### Die konservative Sicherheitsannahme

> [!tip] **Minimale Annahmen**
> SLH-DSA braucht nur eine Annahme: dass die zugrunde liegende **Hashfunktion sicher** ist (Kollisions-/Preimage-Resistenz, → [[04-Kollisionsresistenz-und-Preimage-Resistenz]]). Hashfunktionen sind sehr gut verstanden und gelten (mit Grover-Abschlag) als quantenresistent. Deshalb ist SLH-DSA die **konservativste** Wahl – auch falls sich gitterbasierte Annahmen eines Tages als schwächer erweisen.

### Aufbau (grob)

SLH-DSA kombiniert bekannte Bausteine: **Einmalsignaturen (WOTS+)**, zu **Merkle-Bäumen** (→ [[08-Merkle-Trees]]) gebündelt und in einem **Hypertree** mit einem Few-Time-Signaturschema (FORS) kombiniert. „Stateless" bedeutet: Es muss **kein** Zustand zwischen Signaturen gespeichert werden (ein praktisches Problem älterer hash-basierter Schemata).

### Vor- und Nachteile vs. ML-DSA

| Aspekt | SLH-DSA | ML-DSA |
|--------|---------|--------|
| Sicherheitsannahme | nur Hashfunktion (sehr konservativ) | Gitterproblem |
| Signaturgröße | **groß** (mehrere KB bis zweistellige KB) | kleiner |
| Geschwindigkeit | **langsamer** | schneller |
| Rolle | Backup / höchste Vorsicht | Standardwahl (→ [[07-ML-DSA-FIPS-204]]) |

### Einsatz

SLH-DSA eignet sich dort, wo **maximale Sicherheitsmargen** zählen und Signaturgröße/Geschwindigkeit zweitrangig sind – etwa bei langlebigen Root-Signaturen, Firmware-Signierung oder als diversifizierende Zweitsignatur.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - SLH-DSA (FIPS 205, aus SPHINCS+) ist hash-basiert und zustandslos
> - Sicherheit hängt nur an der Hashfunktion → konservativste PQC-Signatur
> - Aufbau aus WOTS+, Merkle-Bäumen und FORS (Hypertree)
> - Große, langsamere Signaturen → Backup/Spezialfälle statt Standardwahl

---

## Übungen

1. Auf welcher einzigen Annahme beruht die Sicherheit von SLH-DSA?
2. Was bedeutet „stateless" und warum ist das wichtig?
3. Wann würde man SLH-DSA statt ML-DSA wählen?

---

← [[07-ML-DSA-FIPS-204|← Zurück]] | [[00-PQC-Index|Übersicht]] | [[09-Hybride-kryptographische-Verfahren|Weiter →]]
