---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - advanced
  - vertiefung
---

# Multi-Party Computation MPC

> [!info] **Lernziele**
> - Das Konzept der sicheren Mehrparteienberechnung verstehen
> - Ein klassisches Beispiel nachvollziehen
> - Anwendungsfälle einordnen

---

## Inhalt

### Die Grundidee

**Secure Multi-Party Computation (MPC)** erlaubt es mehreren Parteien, gemeinsam eine Funktion über ihre **jeweils geheimen** Eingaben zu berechnen – **ohne** dass eine Partei die Eingaben der anderen erfährt. Alle lernen nur das **Ergebnis**.

> [!example] **Das Millionärsproblem (Yao, 1982)**
> Zwei Millionäre wollen herausfinden, wer reicher ist – **ohne** ihr jeweiliges Vermögen zu verraten. MPC ermöglicht genau diese Berechnung: Am Ende kennen beide nur das Ergebnis „A > B?", nicht die Zahlen.

### Abgrenzung zu HE

- **Homomorphe Verschlüsselung:** **eine** Partei rechnet auf verschlüsselten Daten einer anderen (→ [[01-Homomorphe-Verschluesselung]]).
- **MPC:** **mehrere** Parteien rechnen gemeinsam, jede behält ihre Eingabe geheim.

Beide verfolgen das Ziel „Berechnen ohne Offenlegen", mit unterschiedlichem Setting.

### Techniken

MPC kombiniert mehrere Bausteine:

- **Secret Sharing** (→ [[09-Secret-Sharing-und-Backup-Konzepte]]): Eingaben werden in Anteile zerlegt und verteilt.
- **Garbled Circuits** (Yao): Berechnung als verschlüsselter Schaltkreis.
- **Oblivious Transfer:** Datenübertragung, ohne dass der Sender erfährt, was der Empfänger abruft.

### Anwendungen

- **Gemeinsame Statistik/Analytik** über sensible Daten mehrerer Organisationen (z. B. Banken gegen Betrug, ohne Kundendaten zu teilen).
- **Privacy-preserving Machine Learning.**
- **Threshold-Signaturen / verteilte Schlüssel** (→ [[04-Threshold-Cryptography]]).
- **Auktionen und Wahlen** ohne Offenlegung der Einzelgebote/-stimmen.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - MPC: mehrere Parteien berechnen gemeinsam eine Funktion, jede Eingabe bleibt geheim
> - Alle lernen nur das Ergebnis (klassisch: Yaos Millionärsproblem)
> - Techniken: Secret Sharing, Garbled Circuits, Oblivious Transfer
> - Anwendungen: gemeinsame Analytik, privacy-preserving ML, Threshold-Signaturen

---

## Übungen

1. Was leistet MPC und was lernen die Parteien am Ende?
2. Erklären Sie das Millionärsproblem.
3. Worin unterscheiden sich MPC und homomorphe Verschlüsselung?

---

← [[02-Partially-vs-Fully-Homomorphic-Encryption|← Zurück]] | [[00-Advanced-Index|Übersicht]] | [[04-Threshold-Cryptography|Weiter →]]
