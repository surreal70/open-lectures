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

# Anwendungsfälle ZKP

> [!info] **Lernziele**
> - Praktische Anwendungsfälle von ZKPs kennen
> - Den Nutzen für Privatsphäre und Skalierung einordnen
> - Grenzen realistisch einschätzen

---

## Inhalt

### Wo ZKPs glänzen

Zero-Knowledge-Proofs lösen überall dort Probleme, wo man **etwas beweisen, aber nicht offenlegen** will.

| Anwendungsfeld | Nutzen |
|----------------|--------|
| **Vertrauliche Transaktionen** | Beträge/Teilnehmer verbergen, Gültigkeit beweisen (Zcash) |
| **Blockchain-Skalierung (zk-Rollups)** | viele Transaktionen bündeln, nur einen kurzen Beweis on-chain prüfen |
| **Identität / Credentials** | Alter/Eigenschaft beweisen ohne Ausweisdaten (Selective Disclosure) |
| **Authentifizierung** | Passwort-/Schlüsselkenntnis ohne Übertragung beweisen |
| **Compliance/Audit** | nachweisen, dass Regeln eingehalten wurden, ohne sensible Daten zu zeigen |
| **Verifizierbare Berechnung** | beweisen, dass eine (ausgelagerte) Berechnung korrekt war |

### Privacy-preserving Identity

> [!tip] **Beispiel: Altersnachweis**
> Statt den Personalausweis komplett vorzuzeigen, beweist ein ZKP nur die Aussage „älter als 18" – Geburtsdatum, Name und Adresse bleiben verborgen. Das ist **Datenminimierung** per Kryptographie (vgl. DSGVO, → [[06-DSGVO-und-Verschluesselung]]).

### Skalierung durch zk-Rollups

In Blockchains sind **zk-Rollups** derzeit der wichtigste praktische Treiber: Hunderte Transaktionen werden off-chain verarbeitet und mit einem einzigen **succinct** Beweis (→ [[03-zk-SNARKs]]) on-chain bestätigt. Das erhöht Durchsatz und senkt Kosten, ohne die Sicherheit aufzugeben.

### Grenzen

> [!warning] **Realistische Einordnung**
> ZKPs sind rechenintensiv in der **Beweiserstellung**, komplex zu implementieren und noch jung. Nicht jedes Privatsphäre-Problem braucht ein ZKP – oft genügen einfachere Mittel. ZKPs lohnen sich, wo „beweisen ohne verraten" **zwingend** ist.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - ZKPs ermöglichen „beweisen ohne verraten" in vielen Feldern
> - Kernanwendungen: vertrauliche Transaktionen, zk-Rollups, datensparsame Identität, verifizierbare Berechnung
> - Besonders wirkungsvoll für Privatsphäre (Selective Disclosure) und Blockchain-Skalierung
> - Grenzen: aufwändige Beweiserstellung, Komplexität – gezielt einsetzen

---

## Übungen

1. Nennen Sie drei Anwendungsfelder für ZKPs.
2. Erklären Sie, wie ein ZKP einen datensparsamen Altersnachweis ermöglicht.
3. Was leisten zk-Rollups für die Blockchain-Skalierung?

---

← [[04-zk-STARKs|← Zurück]] | [[00-ZKP-Index|Übersicht]] | [[00-Blockchain-Index|Nächstes Modul →]]
