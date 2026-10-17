---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - schluessel
---

# Sichere Schlüsselgenerierung

> [!info] **Lernziele**
> - Die Bedeutung guter Zufallsquellen für die Schlüsselerzeugung verstehen
> - CSPRNG und Entropiequellen einordnen
> - Reale Schwachstellen durch schlechten Zufall kennen

---

## Inhalt

### Zufall ist die Grundlage

Ein kryptographischer Schlüssel ist nur so stark wie der Zufall, aus dem er erzeugt wurde. Ein 256-Bit-Schlüssel mit nur 40 Bit echter Entropie bietet auch nur 40 Bit Sicherheit (→ [[05-Wahrscheinlichkeitsrechnung-und-Entropie]]). Schlüsselgenerierung heißt deshalb vor allem: **genügend unvorhersehbare Zufälligkeit** gewinnen.

### CSPRNG statt normaler PRNG

| Typ | Eignung |
|-----|---------|
| Normaler PRNG (z. B. `rand()`, Mersenne-Twister) | **ungeeignet** – vorhersagbar |
| **CSPRNG** (kryptographisch sicher) | geeignet |

Ein **CSPRNG** (Cryptographically Secure Pseudo-Random Number Generator) wird aus echter Entropie geseedet und ist so konstruiert, dass aus bisherigen Ausgaben keine künftigen vorhersagbar sind.

Betriebssystem-Quellen:

- **Linux:** `/dev/urandom`, Syscall `getrandom()`
- **Windows:** `BCryptGenRandom`
- Sprachbibliotheken: Java `SecureRandom`, Python `secrets`, Go `crypto/rand`, Node `crypto.randomBytes`.

> [!danger] **Niemals selbst würfeln**
> Niemals `Math.random()`, `rand()` oder selbstgebaute Zufallsgeneratoren für Schlüssel/Nonces verwenden. Immer die kryptographische Systemschnittstelle nutzen.

### Reale Schwachstellen

> [!warning] **Prüfungsrelevant: Zufalls-Desaster**
> - **Debian-OpenSSL-Bug (2008):** Ein entfernter Code-Teil reduzierte die Entropie dramatisch – nur noch ~32.767 mögliche Schlüssel, massenhaft kompromittierbar.
> - **Schwache IoT-Schlüssel:** Geräte erzeugen beim ersten Boot Schlüssel, bevor genug Entropie vorhanden ist → viele Geräte teilen Schlüssel.
> - **Dual_EC_DRBG:** ein mutmaßlich mit Hintertür versehener RNG-Standard.

### Best Practices

- Immer den OS-CSPRNG bzw. geprüfte Bibliotheken verwenden.
- Auf ausreichende Entropie **vor** der Schlüsselerzeugung achten (besonders bei frisch gebooteten/embedded Systemen).
- Schlüssel möglichst direkt im HSM/TPM erzeugen (→ [[06-Hardware-Security-Modules-HSM]], [[07-Trusted-Platform-Module-TPM]]), sodass sie das sichere Element nie verlassen.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Schlüsselstärke hängt direkt an der Entropie der Zufallsquelle
> - Nur CSPRNGs verwenden (OS-Schnittstelle, geprüfte Bibliotheken) – nie normale PRNGs
> - Reale Desaster: Debian-OpenSSL-Bug, schwache IoT-Schlüssel, Dual_EC_DRBG
> - Idealerweise Schlüssel direkt im HSM/TPM erzeugen

---

## Übungen

1. Warum ist ein normaler PRNG für Schlüssel ungeeignet?
2. Nennen Sie zwei CSPRNG-Schnittstellen eines Betriebssystems oder einer Sprache.
3. Was war die Ursache des Debian-OpenSSL-Bugs von 2008?

---

← [[01-Lebenszyklus-kryptographischer-Schluessel|← Zurück]] | [[00-Schluessel-Index|Übersicht]] | [[03-Schluesselverteilung-und-Speicherung|Weiter →]]
