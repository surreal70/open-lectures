---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - secdev
  - vertiefung
---

# Testing und Auditing von Crypto Code

> [!info] **Lernziele**
> - Testmethoden für Krypto-Code kennen
> - Die Rolle von Testvektoren verstehen
> - Auditing und Werkzeuge einordnen

---

## Inhalt

### Besonderheiten beim Testen von Krypto

Krypto-Code zu testen ist schwieriger als normaler Code: Ein Fehler führt selten zu einem offensichtlichen Absturz, sondern zu einer **stillen Schwächung** der Sicherheit. „Es funktioniert" heißt nicht „es ist sicher".

### Testvektoren

> [!tip] **Bekannte Antworten prüfen**
> Standards (NIST, RFCs) liefern **offizielle Testvektoren**: feste Eingaben mit bekannten korrekten Ausgaben. Eine Implementierung muss diese exakt reproduzieren. Das ist der wichtigste Korrektheitstest für Krypto-Code (z. B. NIST CAVP für AES, SHA).

### Testmethoden

| Methode | Zweck |
|---------|-------|
| **Testvektoren** | Korrektheit gegen bekannte Referenzwerte |
| **Round-Trip-Tests** | `decrypt(encrypt(x)) == x` |
| **Property-based / Fuzzing** | zufällige/ungültige Eingaben, Robustheit |
| **Negativtests** | manipulierte Chiffretexte/Signaturen werden **abgelehnt** |
| **Konstante-Zeit-Tests** | Timing-Verhalten prüfen (z. B. dudect) |

### Auditing

Über automatisierte Tests hinaus braucht sicherheitskritischer Code **Audits**:

- **Code-Review** durch Krypto-Kundige (→ [[07-Code-Review-Checkliste-Kryptographie]]).
- **Statische Analyse** (Linter/SAST, die z. B. ECB oder `Math.random()` erkennen).
- **Externe Security-Audits** / Pentests für kritische Systeme.
- **Abhängigkeits-Scans** (veraltete Krypto-Bibliotheken mit CVEs).

### Nicht gegen sich selbst testen

> [!warning] **Interoperabilität prüfen**
> Teste gegen **unabhängige** Implementierungen (z. B. deine Ver-/Entschlüsselung gegen OpenSSL). Ein System, das nur mit sich selbst kompatibel ist, kann denselben Fehler auf beiden Seiten haben und ihn so verdecken.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Krypto-Fehler schwächen still – „läuft" ≠ „sicher"
> - Offizielle Testvektoren sind der zentrale Korrektheitstest
> - Methoden: Testvektoren, Round-Trip, Fuzzing, Negativtests, Timing-Tests
> - Audits: Reviews, SAST, externe Pentests, Dependency-Scans; gegen unabhängige Implementierungen testen

---

## Übungen

1. Warum reicht „der Code funktioniert" bei Kryptographie nicht aus?
2. Wozu dienen offizielle Testvektoren?
3. Warum sollte man gegen eine unabhängige Implementierung testen?

---

← [[05-Memory-Safety-und-Side-Channels|← Zurück]] | [[00-SecDev-Index|Übersicht]] | [[07-Code-Review-Checkliste-Kryptographie|Weiter →]]
