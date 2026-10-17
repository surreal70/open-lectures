---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - pqc
---

# Auswirkungen auf RSA und ECC

> [!info] **Lernziele**
> - Konkret einordnen, welche Verfahren wie stark betroffen sind
> - Das „Harvest now, decrypt later"-Problem verstehen
> - Die zeitliche Dringlichkeit abschätzen

---

## Inhalt

### Wer ist betroffen?

| Verfahren | Bedrohung | Grund |
|-----------|-----------|-------|
| **RSA** | **gebrochen** | Shor faktorisiert $n$ |
| **Diffie-Hellman** | **gebrochen** | Shor löst diskreten Logarithmus |
| **ECC / ECDSA / ECDH** | **gebrochen** | Shor löst EC-diskreten Logarithmus |
| **AES-128** | geschwächt | Grover → ~64 Bit |
| **AES-256** | sicher | Grover → ~128 Bit |
| **SHA-256** | leicht geschwächt | Grover bei Preimage → ~128 Bit |

Kurz: **Die gesamte heute übliche asymmetrische Kryptographie ist durch Shor bedroht**, symmetrische Verfahren und Hashes nur abgeschwächt (→ [[02-Shor-und-Grover-Algorithmus]]).

### Harvest now, decrypt later

> [!danger] **Prüfungsrelevant: die Bedrohung ist schon heute real**
> Ein Angreifer kann **heute** verschlüsselten Verkehr aufzeichnen und speichern, um ihn **später** – sobald Quantencomputer verfügbar sind – zu entschlüsseln („harvest now, decrypt later"). Für langfristig schützenswerte Daten (Staatsgeheimnisse, Gesundheits-/Finanzdaten) ist der Umstieg auf PQC daher **jetzt** dringend, nicht erst, wenn Quantencomputer existieren.

### Zeitliche Einordnung

Noch gibt es keine kryptorelevanten Quantencomputer. Doch:

- Standardisierung ist abgeschlossen (NIST FIPS 203–205, 2024).
- Migration großer Systeme dauert Jahre.
- Daten müssen teils **jahrzehntelang** geschützt bleiben.

Daher haben Behörden (NIST, BSI) klare Migrationsfahrpläne veröffentlicht (→ [[10-Migration-zu-quantenresistenten-Systemen]]).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - RSA, DH und ECC werden durch Shor vollständig gebrochen – Schlüssellänge hilft nicht
> - Symmetrisch/Hashes nur durch Grover geschwächt (AES-256/SHA-384+ bleiben sicher)
> - „Harvest now, decrypt later" macht die Migration schon heute dringend
> - NIST-Standards sind fertig; Migration braucht Zeit → jetzt beginnen

---

## Übungen

1. Welche heute üblichen asymmetrischen Verfahren werden durch Shor gebrochen?
2. Was bedeutet „harvest now, decrypt later" und für wen ist es besonders relevant?
3. Warum sollte die PQC-Migration bereits heute beginnen?

---

← [[02-Shor-und-Grover-Algorithmus|← Zurück]] | [[00-PQC-Index|Übersicht]] | [[04-Post-Quanten-Kryptographie-Ueberblick|Weiter →]]
