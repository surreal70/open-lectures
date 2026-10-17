---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - signaturen
---

# Grundlagen digitaler Signaturen

> [!info] **Lernziele**
> - Das Prinzip digitaler Signaturen verstehen
> - Den Ablauf von Signieren und Verifizieren nachvollziehen
> - Die gebotenen Schutzziele einordnen

---

## Inhalt

### Was ist eine digitale Signatur?

Eine **digitale Signatur** ist das kryptographische Gegenstück zur handschriftlichen Unterschrift: Sie belegt, **wer** ein Dokument erstellt hat und dass es **unverändert** ist. Anders als ein MAC (→ [[05-Message-Authentication-Codes-MAC-HMAC]]) nutzt sie **asymmetrische** Kryptographie und ist dadurch von **jedem** öffentlich prüfbar.

### Signieren und Verifizieren

Eine Signatur nutzt das Schlüsselpaar des Unterzeichners mit vertauschten Rollen gegenüber der Verschlüsselung:

```
Signieren (Sender, privater Schlüssel sk):
  1. Hash der Nachricht bilden:  h = H(m)
  2. Signatur erzeugen:          s = Sign(sk, h)
  3. Senden: (m, s)

Verifizieren (Empfänger, öffentlicher Schlüssel pk):
  1. Hash neu berechnen:         h' = H(m)
  2. Prüfen:                     Verify(pk, h', s) → gültig / ungültig
```

Signiert wird stets der **Hash** der Nachricht, nicht die Nachricht selbst – das ist effizient und für die Verfahren notwendig.

### Gebotene Schutzziele

| Schutzziel | Wie erfüllt |
|------------|-------------|
| **Integrität** | Jede Änderung an $m$ ändert den Hash → Signatur ungültig |
| **Authentizität** | Nur der Inhaber von $sk$ kann eine gültige Signatur erzeugen |
| **Nichtabstreitbarkeit** | Prüfbar mit öffentlichem Schlüssel → Unterzeichner kann nicht leugnen |

Die **Nichtabstreitbarkeit** ist der entscheidende Mehrwert gegenüber einem MAC: Da niemand sonst den privaten Schlüssel besitzt, ist die Urheberschaft gegenüber Dritten beweisbar.

### Wichtige Signaturverfahren

- **RSA-PSS** – signaturbasiert auf dem Faktorisierungsproblem (→ [[02-RSA-PSS]])
- **ECDSA** – elliptische Kurven, weit verbreitet (→ [[03-ECDSA]])
- **EdDSA/Ed25519** – modern, schnell, robust (→ [[04-EdDSA-und-Ed25519]])

> [!note] **Signatur ≠ Verschlüsselung**
> Signieren schützt **nicht** die Vertraulichkeit – die Nachricht bleibt lesbar. Wer beides will, kombiniert Signatur und Verschlüsselung (z. B. „sign-then-encrypt").

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Digitale Signatur = asymmetrisches Gegenstück zur Unterschrift, öffentlich prüfbar
> - Signieren mit privatem, Prüfen mit öffentlichem Schlüssel; signiert wird der Hash
> - Bietet Integrität, Authentizität und – anders als MAC – Nichtabstreitbarkeit
> - Wichtige Verfahren: RSA-PSS, ECDSA, EdDSA/Ed25519

---

## Übungen

1. Mit welchem Schlüssel signiert man, mit welchem wird geprüft?
2. Warum wird der Hash signiert und nicht die ganze Nachricht?
3. Worin unterscheidet sich eine Signatur von einem MAC hinsichtlich der Schutzziele?

---

← [[00-Signaturen-Index|Übersicht]] | [[02-RSA-PSS|Weiter →]]
