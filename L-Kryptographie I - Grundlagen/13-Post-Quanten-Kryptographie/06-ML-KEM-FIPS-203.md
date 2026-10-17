---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - pqc
---

# ML-KEM FIPS-203

> [!info] **Lernziele**
> - ML-KEM (FIPS 203) als quantenresistente Schlüsselkapselung verstehen
> - Das KEM-Konzept einordnen
> - Parameter und Einsatz kennen

---

## Inhalt

### Was ist ML-KEM?

**ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism)**, standardisiert als **FIPS 203** (2024) und hervorgegangen aus **CRYSTALS-Kyber**, ist das NIST-Standardverfahren zur **quantenresistenten Schlüsselkapselung**. Es ersetzt perspektivisch RSA/ECDH für den Schlüsselaustausch.

### Was ist ein KEM?

Ein **Key Encapsulation Mechanism (KEM)** etabliert einen gemeinsamen symmetrischen Schlüssel über einen unsicheren Kanal – analog zum hybriden Prinzip (→ [[06-RSA-OAEP-und-hybride-Verschlüsselung]]):

```
Encapsulate(pk)  → (Chiffretext c, gemeinsamer Schlüssel K)
Decapsulate(sk, c) → K
```

Der so gewonnene Schlüssel $K$ dient anschließend zur **symmetrischen** AEAD-Verschlüsselung der eigentlichen Daten.

### Parameter

| Variante | Sicherheitsniveau (ca.) |
|----------|-------------------------|
| ML-KEM-512 | ~AES-128 |
| ML-KEM-768 | ~AES-192 |
| ML-KEM-1024 | ~AES-256 |

ML-KEM basiert auf dem **Module-LWE**-Problem (→ [[05-Gitterbasierte-Kryptographie]]). Schlüssel und Chiffretexte sind im Kilobyte-Bereich – größer als bei ECC, aber praktikabel.

### Einsatz

> [!tip] **Hybrid einsetzen**
> In der Praxis wird ML-KEM oft **hybrid** mit X25519 kombiniert (→ [[09-Hybride-kryptographische-Verfahren]]): Der Sitzungsschlüssel entsteht aus beiden Anteilen, sodass die Verbindung sicher bleibt, solange **mindestens eines** der Verfahren hält. TLS-1.3-Implementierungen (z. B. X25519MLKEM768) nutzen bereits dieses Vorgehen.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - ML-KEM (FIPS 203, aus Kyber) ist der NIST-Standard für quantenresistente Schlüsselkapselung
> - KEM: Encapsulate/Decapsulate liefern einen gemeinsamen symmetrischen Schlüssel
> - Varianten 512/768/1024 entsprechen ~AES-128/192/256; basiert auf Module-LWE
> - Praxis: hybrid mit X25519 (z. B. in TLS 1.3)

---

## Übungen

1. Wozu dient ein KEM und was liefert Encapsulate?
2. Auf welchem mathematischen Problem beruht ML-KEM?
3. Warum wird ML-KEM oft hybrid mit X25519 eingesetzt?

---

← [[05-Gitterbasierte-Kryptographie|← Zurück]] | [[00-PQC-Index|Übersicht]] | [[07-ML-DSA-FIPS-204|Weiter →]]
