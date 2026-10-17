---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - standards
---

# ISO IEC 27001 und Kryptographie

> [!info] **Lernziele**
> - ISO/IEC 27001 als ISMS-Standard einordnen
> - Die Rolle der Kryptographie darin verstehen
> - Den risikobasierten Ansatz nachvollziehen

---

## Inhalt

### Was ist ISO/IEC 27001?

**ISO/IEC 27001** ist der internationale Standard für ein **Information Security Management System (ISMS)** – ein systematischer, organisationsweiter Rahmen zum Management von Informationssicherheit. Anders als FIPS oder TR-02102 regelt er keine konkreten Algorithmen, sondern den **Managementprozess**.

### Kryptographie als ein Baustein

Kryptographie ist in ISO 27001 ein **Kontrollbereich** unter vielen. Im Anhang A (bzw. in ISO/IEC 27002 als Leitfaden) finden sich Maßnahmen wie:

- **Richtlinie zur Verwendung von Kryptographie** (wann, wie, welche Verfahren).
- **Schlüsselmanagement** über den gesamten Lebenszyklus (→ Modul 10).

Kryptographie ist also kein Selbstzweck, sondern dient den übergeordneten Schutzzielen (→ [[03-Schutzziele]]) im Rahmen des Risikomanagements.

### Risikobasierter Ansatz

> [!tip] **Maßnahmen folgen dem Risiko**
> ISO 27001 verlangt, Schutzmaßnahmen – auch kryptographische – aus einer **Risikobewertung** abzuleiten: Welche Werte sind wie schützenswert, welche Bedrohungen bestehen? Verschlüsselung wird dort eingesetzt, wo das Risiko es rechtfertigt, nicht pauschal. Das verbindet Kryptographie mit dem Inventar- und Risikomanagement (→ [[09-Kryptographisches-Inventar-und-Risikomanagement]]).

### Zertifizierung

Organisationen können sich nach ISO 27001 **zertifizieren** lassen – ein in vielen Branchen und Ausschreibungen anerkannter Nachweis für systematische Informationssicherheit. Die Zertifizierung bezieht sich auf das **Managementsystem**, nicht auf einzelne Produkte.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - ISO/IEC 27001 standardisiert ein Informationssicherheits-Managementsystem (ISMS)
> - Kryptographie ist ein Kontrollbereich (Richtlinie + Schlüsselmanagement), kein Algorithmus-Standard
> - Maßnahmen werden risikobasiert abgeleitet
> - Zertifizierung bezieht sich auf das Managementsystem der Organisation

---

## Übungen

1. Worin unterscheidet sich ISO 27001 von FIPS/TR-02102?
2. Welche kryptografiebezogenen Maßnahmen nennt der Standard?
3. Was bedeutet der „risikobasierte Ansatz" für den Einsatz von Verschlüsselung?

---

← [[03-FIPS-140-3|← Zurück]] | [[00-Standards-Index|Übersicht]] | [[05-eIDAS-und-elektronische-Signaturen|Weiter →]]
