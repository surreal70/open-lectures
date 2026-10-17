---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - pqc
---

# Migration zu quantenresistenten Systemen

> [!info] **Lernziele**
> - Die Schritte einer PQC-Migration verstehen
> - Die Rolle von Krypto-Inventar und Crypto-Agility einordnen
> - Prioritäten für die Umstellung ableiten

---

## Inhalt

### Warum jetzt migrieren?

Obwohl kryptorelevante Quantencomputer noch nicht existieren, ist die Migration **jetzt** zu beginnen – wegen „harvest now, decrypt later" (→ [[03-Auswirkungen-auf-RSA-und-ECC]]) und weil große Systeme Jahre brauchen, bis sie vollständig umgestellt sind.

### Schritte der Migration

```
1. Inventarisieren   – wo wird welche Kryptographie eingesetzt?
2. Priorisieren      – was schützt langlebige/sensible Daten?
3. Crypto-Agility    – Verfahren austauschbar machen
4. Hybrid einführen  – klassisch + PQC parallel
5. Umstellen/Testen  – schrittweise, mit Interoperabilitätstests
6. Klassik abbauen   – wenn PQC etabliert und erprobt ist
```

### Krypto-Inventar

> [!tip] **Man kann nur migrieren, was man kennt**
> Der erste und oft schwierigste Schritt ist ein vollständiges **kryptographisches Inventar** (→ Modul 14): Welche Protokolle, Bibliotheken, Zertifikate und Schlüssel sind im Einsatz, mit welchen Algorithmen und Laufzeiten? Ohne diesen Überblick ist eine geordnete Migration unmöglich.

### Crypto-Agility als Voraussetzung

Systeme müssen so gebaut sein, dass sich Algorithmen **austauschen** lassen, ohne die Architektur neu zu schreiben (→ Modul 14, Modul 20). Wer heute Crypto-Agility einplant, kann künftige Wechsel (auch über PQC hinaus) deutlich leichter vollziehen.

### Priorisierung

| Priorität | Beispiele |
|-----------|-----------|
| **Hoch** | langlebige Geheimnisse, Staats-/Gesundheits-/Finanzdaten, Root-Schlüssel |
| **Mittel** | langfristige Signaturen, Firmware/Code Signing |
| **Niedriger** | kurzlebige Sitzungsdaten (durch PFS ohnehin geschützt) |

### Empfehlungen

Behörden wie **NIST** und **BSI** (→ Modul 14) haben Fahrpläne und Übergangsfristen veröffentlicht. Der empfohlene Weg ist überwiegend **hybrid** (→ [[09-Hybride-kryptographische-Verfahren]]), bis die PQC-Verfahren breit erprobt sind.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Migration jetzt beginnen (harvest now, decrypt later; lange Umstellungsdauer)
> - Ablauf: Inventar → Priorisieren → Crypto-Agility → Hybrid → Umstellen → Klassik abbauen
> - Krypto-Inventar ist die unverzichtbare Grundlage
> - Priorität auf langlebige, sensible Daten; NIST/BSI empfehlen hybride Übergänge

---

## Übungen

1. Warum muss die PQC-Migration schon vor Verfügbarkeit von Quantencomputern beginnen?
2. Welche Rolle spielt das kryptographische Inventar?
3. Welche Daten sollten bei der Migration priorisiert werden?

---

← [[09-Hybride-kryptographische-Verfahren|← Zurück]] | [[00-PQC-Index|Übersicht]] | [[00-Standards-Index|Nächstes Modul →]]
