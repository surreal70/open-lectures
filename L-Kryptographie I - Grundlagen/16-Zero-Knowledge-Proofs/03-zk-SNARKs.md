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

# zk-SNARKs

> [!info] **Lernziele**
> - zk-SNARKs und ihre Eigenschaften verstehen
> - Die Bedeutung des Trusted Setup einordnen
> - Typische Einsatzgebiete kennen

---

## Inhalt

### Was bedeutet zk-SNARK?

**zk-SNARK** steht für **Zero-Knowledge Succinct Non-interactive ARgument of Knowledge**. Die Namensbestandteile beschreiben die Eigenschaften:

| Teil | Bedeutung |
|------|-----------|
| **Zero-Knowledge** | verrät nichts über die Eingabe |
| **Succinct** | der Beweis ist **sehr klein** und schnell zu prüfen |
| **Non-interactive** | ein einziger Beweis, kein Dialog (→ [[02-Interaktive-und-nicht-interaktive-ZKP]]) |
| **Argument of Knowledge** | beweist Kenntnis einer gültigen Eingabe |

Die herausragende Eigenschaft ist **Succinctness**: Selbst für komplexe Berechnungen ist der Beweis nur wenige hundert Byte groß und in Millisekunden prüfbar – unabhängig von der Komplexität der bewiesenen Aussage.

### Das Trusted Setup

> [!danger] **Prüfungsrelevant: die Schwäche von zk-SNARKs**
> Viele zk-SNARKs benötigen ein **Trusted Setup**: einmalig werden öffentliche Parameter erzeugt, wobei geheime Zufallswerte („toxic waste") entstehen. Werden diese **nicht vernichtet**, kann ihr Besitzer **falsche Beweise** fälschen. Das Setup ist also ein kritischer Vertrauenspunkt. Moderne Varianten (z. B. PLONK mit universellem Setup) mildern das, STARKs vermeiden es ganz (→ [[04-zk-STARKs]]).

### Funktionsprinzip (grob)

Die zu beweisende Berechnung wird in ein **arithmetisches Schaltkreis-/Constraint-System** übersetzt. Der Beweiser zeigt, dass er eine Belegung kennt, die alle Constraints erfüllt – mithilfe elliptischer Kurven und Pairings.

### Einsatz

- **Zcash:** erste große Anwendung – vertrauliche Transaktionen.
- **Ethereum / zk-Rollups:** Skalierung durch gebündelte, succinct beweisbare Transaktionen.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - zk-SNARK: Zero-Knowledge, succinct (winziger Beweis), nicht-interaktiv, Wissensbeweis
> - Succinctness: kleine, schnell prüfbare Beweise auch für komplexe Aussagen
> - Viele Varianten brauchen ein Trusted Setup (toxic waste – kritischer Vertrauenspunkt)
> - Einsatz: Zcash, zk-Rollups auf Ethereum

---

## Übungen

1. Wofür stehen die Buchstaben in „zk-SNARK"?
2. Was bedeutet „Succinctness" und warum ist sie wertvoll?
3. Warum ist das Trusted Setup eine potenzielle Schwachstelle?

---

← [[02-Interaktive-und-nicht-interaktive-ZKP|← Zurück]] | [[00-ZKP-Index|Übersicht]] | [[04-zk-STARKs|Weiter →]]
