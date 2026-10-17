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

# Anwendungsfälle Advanced Crypto

> [!info] **Lernziele**
> - Anwendungsfälle der fortgeschrittenen Verfahren überblicken
> - Die passenden Techniken je Szenario auswählen
> - Die Verfahren sinnvoll kombinieren

---

## Inhalt

### Übergreifendes Ziel: Privacy-Enhancing Technologies

Die Verfahren dieses Moduls – HE, MPC, Threshold, TEE – zählen zu den **Privacy-Enhancing Technologies (PETs)**. Sie ermöglichen Nutzen aus Daten, **ohne** diese offenzulegen.

### Welche Technik wofür?

| Szenario | Passende Technik |
|----------|------------------|
| Cloud rechnet auf verschlüsselten Daten | **HE** (→ [[01-Homomorphe-Verschluesselung]]) |
| Mehrere Parteien, gemeinsame Auswertung geheimer Eingaben | **MPC** (→ [[03-Multi-Party-Computation-MPC]]) |
| Kein Single Point of Failure beim Schlüssel | **Threshold** (→ [[04-Threshold-Cryptography]]) |
| Schnelle Verarbeitung im geschützten Hardwarebereich | **TEE** (→ [[05-Secure-Enclaves-und-TEE]]) |

### Konkrete Anwendungsfelder

- **Gesundheitswesen:** gemeinsame Forschung über Patientendaten mehrerer Kliniken (MPC/HE), ohne Datensätze zu teilen.
- **Finanzwesen:** Betrugserkennung über Banken hinweg (MPC); Schutz großer Krypto-Bestände (Threshold).
- **Werbung/Analytik:** datensparsame Messung ohne Einzeldatenweitergabe.
- **Machine Learning:** privacy-preserving Training/Inference (HE/MPC/TEE).
- **Cloud:** Confidential Computing für sensible Workloads (TEE).

### Kombination der Verfahren

> [!tip] **Oft Hybrid**
> In der Praxis werden die Verfahren **kombiniert**: z. B. ein TEE für Geschwindigkeit, dessen Korrektheit per Attestation belegt wird, ergänzt um MPC für verteiltes Vertrauen, oder HE für besonders sensible Teilberechnungen. Die Wahl folgt stets dem Schutzbedarf, der Leistungsanforderung und dem Vertrauensmodell.

### Reifegrad

> [!warning] **Noch im Reifeprozess**
> Diese Verfahren sind leistungsfähig, aber teils **rechenintensiv, komplex und jung**. Für viele Alltagsprobleme genügen klassische Verfahren (TLS, AEAD). Advanced Crypto lohnt sich dort, wo „Nutzen ohne Offenlegung" **zwingend** gefordert ist.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - HE, MPC, Threshold und TEE sind Privacy-Enhancing Technologies
> - Technikwahl folgt dem Szenario (Rechnen auf verschlüsselten Daten, Mehrparteien, Schlüsselschutz, schnelle Isolation)
> - Felder: Gesundheit, Finanzen, Analytik, ML, Cloud
> - Oft hybrid eingesetzt; noch jung/aufwändig – gezielt anwenden

---

## Übungen

1. Ordnen Sie den vier Verfahren je ein passendes Szenario zu.
2. Nennen Sie zwei konkrete Anwendungsfelder und die genutzten Techniken.
3. Warum werden diese Verfahren oft kombiniert eingesetzt?

---

← [[05-Secure-Enclaves-und-TEE|← Zurück]] | [[00-Advanced-Index|Übersicht]] | [[00-SecDev-Index|Nächstes Modul →]]
