---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - architektur
  - vertiefung
---

# Architekturentscheidungen Kryptographie

> [!info] **Lernziele**
> - Zentrale kryptographische Architekturentscheidungen kennen
> - Typische Trade-offs abwägen
> - Entscheidungen dokumentieren

---

## Inhalt

### Die wichtigsten Entscheidungen

Beim Entwurf einer Krypto-Architektur sind grundlegende Weichenstellungen zu treffen, die später schwer zu ändern sind:

| Entscheidung | Optionen / Fragen |
|--------------|-------------------|
| **Schutzumfang** | nur Transport (TLS) oder echte E2EE? (→ [[04-Ende-zu-Ende-Verschluesselung]]) |
| **Schlüsselhoheit** | anbieter-verwaltet, BYOK oder HYOK? (→ [[08-Cloud-Key-Management-Services-KMS]]) |
| **Schlüsselspeicherung** | HSM, TPM, KMS, Software? (→ Modul 10) |
| **Verfahren** | welche Algorithmen; PQC/hybrid? (→ Modul 13) |
| **Zentral vs. verteilt** | zentraler Krypto-Dienst oder pro Komponente? |

### Typische Trade-offs

> [!warning] **Abwägungen**
> - **Sicherheit vs. Performance:** stärkere Verfahren/HSM kosten Latenz.
> - **Sicherheit vs. Usability:** E2EE erschwert serverseitige Features (Suche, Recovery).
> - **Flexibilität vs. Angriffsfläche:** viele verhandelbare Verfahren erhöhen das Downgrade-Risiko (→ [[08-Downgrade-Angriffe]]).
> - **Kontrolle vs. Aufwand:** HYOK gibt maximale Kontrolle, aber mehr Betriebsaufwand.

### Zentraler Krypto-Dienst

Ein wiederkehrendes Muster ist ein **zentraler Krypto-/Key-Service**, den alle Komponenten über eine Schnittstelle nutzen. Vorteile: einheitliche Policy, zentrale Rotation, Crypto-Agility (→ [[03-Crypto-Agility-Design-Patterns]]). Nachteil: potenzieller Single Point of Failure, der entsprechend abgesichert werden muss.

### Architecture Decision Records

> [!tip] **Entscheidungen dokumentieren**
> Kryptographische Architekturentscheidungen sollten in **ADRs (Architecture Decision Records)** festgehalten werden: Was wurde entschieden, **warum**, welche Alternativen gab es? Das macht die Architektur nachvollziehbar und erleichtert spätere Migrationen (→ [[04-Kryptographie-Migration-Strategien]]).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Grundsatzentscheidungen: Schutzumfang, Schlüsselhoheit/-speicherung, Verfahren, zentral vs. verteilt
> - Trade-offs: Sicherheit vs. Performance/Usability/Flexibilität/Aufwand
> - Zentraler Krypto-Dienst fördert Policy und Agility, braucht aber Absicherung
> - Entscheidungen in ADRs mit Begründung dokumentieren

---

## Übungen

1. Nennen Sie vier zentrale Architekturentscheidungen bei Krypto-Systemen.
2. Erläutern Sie zwei typische Trade-offs.
3. Warum sind Architecture Decision Records für Krypto sinnvoll?

---

← [[01-Threat-Modeling-fuer-Kryptographie|← Zurück]] | [[00-Architektur-Index|Übersicht]] | [[03-Crypto-Agility-Design-Patterns|Weiter →]]
