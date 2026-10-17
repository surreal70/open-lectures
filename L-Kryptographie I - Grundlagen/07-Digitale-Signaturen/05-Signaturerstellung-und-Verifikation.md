---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - signaturen
---

# Signaturerstellung und Verifikation

> [!info] **Lernziele**
> - Den praktischen Ablauf von Signaturerstellung und -prüfung verstehen
> - Typische Fehlerquellen im Signaturprozess kennen
> - Den Zusammenhang mit Zertifikaten einordnen

---

## Inhalt

### Der Gesamtprozess

Unabhängig vom konkreten Verfahren (RSA-PSS, ECDSA, Ed25519) folgt jede Signatur demselben Ablauf:

```
Signieren:
  1. Nachricht m hashen:           h = H(m)
  2. h mit privatem Schlüssel signieren → Signatur s
  3. (m, s) [+ Zertifikat] übertragen

Verifizieren:
  1. m erneut hashen:              h' = H(m)
  2. s mit öffentlichem Schlüssel prüfen
  3. Zusätzlich: Vertrauen in den öffentlichen Schlüssel prüfen
```

### Verifikation ist mehr als Mathematik

Eine mathematisch gültige Signatur beweist nur, dass sie zum zugehörigen öffentlichen Schlüssel passt. Entscheidend ist die Frage: **Gehört dieser öffentliche Schlüssel wirklich der erwarteten Person/Instanz?** Diese Vertrauensfrage beantworten **Zertifikate** und die **PKI** (→ [[06-Digitale-Zertifikate]] und Modul 8).

Vollständige Prüfung umfasst daher:

1. Kryptographische Gültigkeit der Signatur
2. Gültigkeit und Vertrauenswürdigkeit des Zertifikats (Kette bis zur vertrauenswürdigen Wurzel)
3. Gültigkeitszeitraum und Sperrstatus (→ Modul 8: CRL/OCSP)

### Typische Fehlerquellen

> [!danger] **Häufige Implementierungsfehler**
> - **Signatur geprüft, aber Zertifikatskette ignoriert** → Angreifer legt eigenen Schlüssel vor.
> - **Fehlerhafte Nonce** bei ECDSA (→ [[03-ECDSA]]).
> - **Hash-Algorithmus zu schwach** (MD5/SHA-1 → [[04-Kollisionsresistenz-und-Preimage-Resistenz]]).
> - **Verwechslung von „signiert" und „verschlüsselt"** – eine Signatur schützt nicht die Vertraulichkeit.

### Praxis

In der Praxis übernehmen Bibliotheken (OpenSSL, libsodium, GPG) diese Schritte. Wichtig ist, die **Verifikation vollständig** durchzuführen und Fehler strikt abzulehnen, statt sie zu ignorieren.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Ablauf: hashen → mit privatem Schlüssel signieren → mit öffentlichem prüfen
> - Gültige Signatur allein genügt nicht – Vertrauen in den Schlüssel (Zertifikat/PKI) ist nötig
> - Vollständige Prüfung: Signatur + Zertifikatskette + Gültigkeit/Sperrstatus
> - Häufige Fehler: ignorierte Zertifikatskette, schwacher Hash, Nonce-Fehler

---

## Übungen

1. Beschreiben Sie den vollständigen Ablauf einer Signaturprüfung.
2. Warum reicht eine mathematisch gültige Signatur nicht aus?
3. Nennen Sie zwei häufige Fehler bei der Signaturverifikation.

---

← [[04-EdDSA-und-Ed25519|← Zurück]] | [[00-Signaturen-Index|Übersicht]] | [[06-Digitale-Zertifikate|Weiter →]]
