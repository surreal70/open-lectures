---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - standards
---

# DSGVO und Verschlüsselung

> [!info] **Lernziele**
> - Die Rolle von Verschlüsselung in der DSGVO verstehen
> - Pseudonymisierung und Anonymisierung abgrenzen
> - Die Bedeutung bei Datenpannen einordnen

---

## Inhalt

### Verschlüsselung als empfohlene Maßnahme

Die **DSGVO (Datenschutz-Grundverordnung)** nennt Verschlüsselung ausdrücklich als Beispiel für geeignete **technische Maßnahmen** zum Schutz personenbezogener Daten (Art. 32 – „Sicherheit der Verarbeitung"). Sie ist nicht pauschal vorgeschrieben, aber eine der wichtigsten Maßnahmen nach dem **Stand der Technik** und dem Risiko.

### Pseudonymisierung vs. Anonymisierung

> [!warning] **Prüfungsrelevant: wichtiger Unterschied**
> - **Pseudonymisierung:** Personenbezug ist mit Zusatzwissen (z. B. einem Schlüssel) **wiederherstellbar**. Pseudonymisierte Daten bleiben **personenbezogen** und unterliegen der DSGVO. Verschlüsselung ist eine Form der Pseudonymisierung.
> - **Anonymisierung:** Personenbezug ist **unwiderruflich** entfernt. Anonyme Daten fallen **nicht** mehr unter die DSGVO.
>
> Verschlüsselte Daten sind also **nicht** anonym – mit dem Schlüssel ist der Bezug wiederherstellbar.

### Bedeutung bei Datenpannen

Bei einer **Datenpanne** (Art. 33/34) kann wirksame Verschlüsselung entscheidend sein: Sind die betroffenen Daten so verschlüsselt, dass die Täter sie nicht nutzen können, entfällt unter Umständen die Pflicht zur **Benachrichtigung der Betroffenen** – ein starker praktischer Anreiz, personenbezogene Daten zu verschlüsseln.

### Weitere Bezüge

- **Datensouveränität / Drittlandtransfer:** Verschlüsselung (idealerweise mit kundeneigenen Schlüsseln, → [[08-Cloud-Key-Management-Services-KMS]]) reduziert Risiken beim Transfer in Drittländer.
- **Datenminimierung und Löschung:** „Kryptographisches Löschen" (Schlüssel vernichten → Daten unlesbar) kann Löschpflichten unterstützen.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - DSGVO nennt Verschlüsselung als zentrale technische Schutzmaßnahme (Art. 32)
> - Pseudonymisierung (reversibel, DSGVO-relevant) ≠ Anonymisierung (irreversibel, DSGVO-frei)
> - Verschlüsselte Daten sind pseudonym, nicht anonym
> - Wirksame Verschlüsselung kann Melde-/Benachrichtigungspflichten bei Datenpannen reduzieren

---

## Übungen

1. Welche Rolle schreibt die DSGVO der Verschlüsselung zu?
2. Worin unterscheiden sich Pseudonymisierung und Anonymisierung?
3. Warum kann Verschlüsselung bei einer Datenpanne vorteilhaft sein?

---

← [[05-eIDAS-und-elektronische-Signaturen|← Zurück]] | [[00-Standards-Index|Übersicht]] | [[07-Crypto-Agility|Weiter →]]
