---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - pqc
---

# Shor und Grover-Algorithmus

> [!info] **Lernziele**
> - Den Shor-Algorithmus und seine Wirkung verstehen
> - Den Grover-Algorithmus einordnen
> - Die unterschiedliche Bedrohung für asymmetrische und symmetrische Verfahren erkennen

---

## Inhalt

### Shor-Algorithmus

Der **Shor-Algorithmus** (1994) löst auf einem Quantencomputer die **Faktorisierung** großer Zahlen und den **diskreten Logarithmus** in **polynomieller** Zeit – also effizient.

> [!danger] **Shor bricht die asymmetrische Kryptographie**
> Genau diese beiden Probleme sind die Grundlage von **RSA, Diffie-Hellman und ECC** (→ [[03-Auswirkungen-auf-RSA-und-ECC]]). Ein hinreichend großer Quantencomputer würde diese Verfahren **vollständig** brechen – und zwar unabhängig von der Schlüssellänge. Größere Schlüssel helfen **nicht**.

Shor nutzt die Quanten-Fouriertransformation zur effizienten **Periodensuche**, aus der sich die Faktoren bzw. der Logarithmus ableiten lassen.

### Grover-Algorithmus

Der **Grover-Algorithmus** (1996) beschleunigt die **unstrukturierte Suche**: Statt $N$ Möglichkeiten klassisch durchzuprobieren, braucht er nur etwa $\sqrt{N}$ Schritte – ein **quadratischer** Speedup.

Auf Kryptographie angewandt bedeutet das eine **Halbierung** der effektiven Schlüssellänge symmetrischer Verfahren:

| Verfahren | klassisch | mit Grover |
|-----------|-----------|------------|
| AES-128 | 128 Bit | ~64 Bit (zu wenig) |
| AES-256 | 256 Bit | ~128 Bit (weiterhin sicher) |

### Die zentrale Unterscheidung

> [!warning] **Prüfungsrelevant**
> - **Shor** → **asymmetrisch** (RSA/ECC/DH) wird **gebrochen**. Hier hilft nur ein Wechsel zu Post-Quanten-Verfahren.
> - **Grover** → **symmetrisch/Hashes** werden nur **geschwächt** (halbe Bit-Sicherheit). Gegenmittel: Schlüssel-/Ausgabelänge verdoppeln (AES-256, SHA-384/512).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Shor löst Faktorisierung und diskreten Logarithmus polynomiell → bricht RSA/ECC/DH
> - Größere asymmetrische Schlüssel helfen gegen Shor nicht
> - Grover halbiert die effektive Sicherheit symmetrischer Verfahren (quadratischer Speedup)
> - Gegen Grover: AES-256 / SHA-384+; gegen Shor: Post-Quanten-Kryptographie

---

## Übungen

1. Welche beiden Probleme löst der Shor-Algorithmus effizient?
2. Warum bleibt AES-256 trotz Grover sicher?
3. Erklären Sie den grundlegenden Unterschied der Bedrohung durch Shor und Grover.

---

← [[01-Grundlagen-des-Quantencomputings|← Zurück]] | [[00-PQC-Index|Übersicht]] | [[03-Auswirkungen-auf-RSA-und-ECC|Weiter →]]
