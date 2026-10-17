---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - signaturen
---

# RSA-PSS

> [!info] **Lernziele**
> - RSA-PSS als sicheres Signaturpadding verstehen
> - Den Unterschied zu PKCS#1 v1.5 einordnen
> - Die Rolle des Zufalls (Salt) kennen

---

## Inhalt

### Warum ein spezielles Signaturpadding?

Wie bei der Verschlüsselung ist „Textbook-RSA" auch beim Signieren unsicher. Der Hash muss vor der RSA-Operation geeignet aufbereitet (gepaddet) werden. Zwei Verfahren sind verbreitet:

- **PKCS#1 v1.5:** älteres, deterministisches Padding – funktioniert, ist aber ohne Sicherheitsbeweis und war wiederholt Ziel von Angriffen.
- **RSA-PSS (Probabilistic Signature Scheme):** modernes, **probabilistisches** Padding mit Sicherheitsbeweis.

### Funktionsweise von PSS

RSA-PSS mischt vor der Signatur den Nachrichten-Hash mit einem zufälligen **Salt** und einer Maskenfunktion (MGF, meist auf Hash-Basis). Daraus folgt:

- **Probabilistisch:** Dieselbe Nachricht erzeugt bei jeder Signatur eine **andere** Signatur (durch den frischen Salt).
- **Beweisbare Sicherheit:** PSS ist im Random-Oracle-Modell als sicher bewiesen.

```
Signatur:  s = RSA_sk( PSS-Encode(H(m), salt) )
Prüfung:   PSS-Verify(pk, m, s) rekonstruiert und vergleicht
```

### Empfehlung

> [!tip] **Best Practice**
> Für neue RSA-Signaturen **RSA-PSS** verwenden (standardisiert in PKCS#1 v2.1 / RFC 8017). PKCS#1 v1.5 nur für Kompatibilität mit Altsystemen. Wie immer bei RSA: Modul mindestens 2048, besser 3072 Bit (→ [[07-Schlüssellängen-und-Sicherheitsniveaus]]).

> [!note] **Signatur vs. Verschlüsselung bei RSA**
> OAEP ist das Padding für **Verschlüsselung** (→ [[06-RSA-OAEP-und-hybride-Verschlüsselung]]), PSS das Padding für **Signaturen**. Beide machen RSA probabilistisch und beweisbar sicher, dienen aber unterschiedlichen Zwecken.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Textbook-RSA ist auch zum Signieren unsicher – Padding nötig
> - RSA-PSS ist probabilistisch (Salt) und beweisbar sicher
> - PKCS#1 v1.5 ist älter, deterministisch, nur für Kompatibilität
> - OAEP = Verschlüsselung, PSS = Signatur

---

## Übungen

1. Warum erzeugt RSA-PSS für dieselbe Nachricht unterschiedliche Signaturen?
2. Worin unterscheiden sich PSS und PKCS#1 v1.5?
3. Welches Padding gehört zur Verschlüsselung, welches zur Signatur?

---

← [[01-Grundlagen-digitaler-Signaturen|← Zurück]] | [[00-Signaturen-Index|Übersicht]] | [[03-ECDSA|Weiter →]]
