---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - zkp
  - vertiefung
---

# Grundlagen Zero-Knowledge-Proofs

> [!info] **Lernziele**
> - Das Konzept eines Zero-Knowledge-Proofs verstehen
> - Die drei Kerneigenschaften kennen
> - Ein anschauliches Beispiel nachvollziehen

---

## Inhalt

### Die Grundidee

Ein **Zero-Knowledge-Proof (ZKP)** erlaubt es einem **Beweiser (Prover)**, einem **Prüfer (Verifier)** zu beweisen, dass er ein Geheimnis kennt oder eine Aussage wahr ist – **ohne** das Geheimnis selbst preiszugeben.

> [!example] **Höhle von Ali Baba**
> Eine ringförmige Höhle mit einer magischen Tür, die nur ein Geheimwort öffnet. Der Beweiser geht in einen der beiden Gänge; der Prüfer ruft, aus welchem Gang er herauskommen soll. Kennt der Beweiser das Wort, schafft er es immer. Nach vielen Runden ist der Prüfer überzeugt – ohne je das Wort erfahren zu haben.

### Die drei Kerneigenschaften

| Eigenschaft | Bedeutung |
|-------------|-----------|
| **Vollständigkeit (Completeness)** | Ist die Aussage wahr und beide ehrlich, wird der Beweis akzeptiert |
| **Korrektheit (Soundness)** | Ist die Aussage falsch, kann ein Betrüger den Prüfer nur mit vernachlässigbarer Wahrscheinlichkeit täuschen |
| **Zero-Knowledge** | Der Prüfer lernt **nichts** außer der Tatsache, dass die Aussage wahr ist |

### Warum nützlich?

ZKPs lösen scheinbar widersprüchliche Anforderungen: etwas **beweisen**, ohne es zu **verraten**. Beispiele:

- Beweisen, dass man volljährig ist, ohne das Geburtsdatum zu zeigen.
- Beweisen, ein Passwort zu kennen, ohne es zu übertragen.
- In Blockchains Transaktionen validieren, ohne Beträge offenzulegen (→ [[05-Anwendungsfaelle-ZKP]]).

### Abgrenzung

Ein ZKP ist mehr als eine Signatur: Es beweist **Wissen/Wahrheit** ohne Offenlegung. Die konkrete Umsetzung kann **interaktiv** oder **nicht-interaktiv** sein (→ [[02-Interaktive-und-nicht-interaktive-ZKP]]).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - ZKP beweist Wissen/Wahrheit, ohne das Geheimnis preiszugeben
> - Drei Eigenschaften: Vollständigkeit, Korrektheit (Soundness), Zero-Knowledge
> - Anschauung: Höhle von Ali Baba
> - Ermöglicht „beweisen ohne verraten" – z. B. Altersnachweis, Blockchain-Privatsphäre

---

## Übungen

1. Nennen und erklären Sie die drei Kerneigenschaften eines ZKP.
2. Erläutern Sie das Höhlen-Beispiel in eigenen Worten.
3. Geben Sie zwei praktische Anwendungen für ZKPs an.

---

← [[00-ZKP-Index|Übersicht]] | [[02-Interaktive-und-nicht-interaktive-ZKP|Weiter →]]
