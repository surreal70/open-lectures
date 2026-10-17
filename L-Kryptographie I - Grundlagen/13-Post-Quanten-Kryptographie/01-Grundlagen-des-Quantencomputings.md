---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - pqc
---

# Grundlagen des Quantencomputings

> [!info] **Lernziele**
> - Grundbegriffe des Quantencomputings verstehen
> - Qubits, Superposition und Verschränkung einordnen
> - Erkennen, warum Quantencomputer für die Kryptographie relevant sind

---

## Inhalt

### Warum für die Kryptographie relevant?

Quantencomputer nutzen quantenmechanische Effekte, um bestimmte Probleme **fundamental schneller** zu lösen als klassische Rechner. Zwei dieser Probleme – Faktorisierung und diskreter Logarithmus – sind genau die, auf denen RSA und ECC beruhen. Daher bedrohen hinreichend große Quantencomputer die heutige asymmetrische Kryptographie (→ [[03-Auswirkungen-auf-RSA-und-ECC]]).

### Qubits statt Bits

Ein klassisches Bit ist 0 **oder** 1. Ein **Qubit** kann sich in einer **Superposition** beider Zustände befinden – gewichtet mit Wahrscheinlichkeitsamplituden.

| Begriff | Bedeutung |
|---------|-----------|
| **Superposition** | ein Qubit repräsentiert 0 und 1 gleichzeitig (bis zur Messung) |
| **Verschränkung** | Qubits werden korreliert; der Zustand ist nicht mehr unabhängig beschreibbar |
| **Interferenz** | Amplituden verstärken/auslöschen sich – so werden falsche Antworten „weggerechnet" |
| **Messung** | kollabiert die Superposition auf einen klassischen Wert |

$n$ Qubits können $2^n$ Zustände gleichzeitig repräsentieren – die Grundlage des Rechenvorteils bei bestimmten Algorithmen.

### Was Quantencomputer NICHT können

> [!warning] **Prüfungsrelevant: kein Allheilmittel**
> Quantencomputer sind **nicht** einfach „schnellere Computer". Sie beschleunigen nur **spezielle** Probleme mit passender Struktur (z. B. Periodensuche → Shor). Allgemeine NP-vollständige Probleme lösen sie **nicht** effizient. Für die meisten Alltagsaufgaben bieten sie keinen Vorteil.

### Realitätscheck

Heutige Quantencomputer haben wenige, fehleranfällige Qubits. Für den Bruch von RSA-2048 wären Millionen stabiler, fehlerkorrigierter („logischer") Qubits nötig – aktuell nicht vorhanden. Die Bedrohung ist **zukünftig**, aber wegen „store now, decrypt later" (→ [[06-Perfect-Forward-Secrecy]]) schon heute relevant.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Qubits nutzen Superposition, Verschränkung und Interferenz
> - $n$ Qubits repräsentieren $2^n$ Zustände gleichzeitig → Vorteil bei speziellen Problemen
> - Quantencomputer beschleunigen nur strukturierte Probleme, nicht alles
> - Heute noch keine kryptorelevante Größe, aber „store now, decrypt later" macht PQC jetzt relevant

---

## Übungen

1. Was unterscheidet ein Qubit von einem klassischen Bit?
2. Erklären Sie Superposition und Verschränkung.
3. Warum sind Quantencomputer keine universell schnelleren Rechner?

---

← [[00-PQC-Index|Übersicht]] | [[02-Shor-und-Grover-Algorithmus|Weiter →]]
