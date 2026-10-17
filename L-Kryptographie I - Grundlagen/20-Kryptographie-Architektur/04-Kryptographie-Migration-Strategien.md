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

# Kryptographie Migration Strategien

> [!info] **Lernziele**
> - Strategien für kryptographische Migrationen kennen
> - Die Herausforderung bereits verschlüsselter Daten verstehen
> - Einen Migrationsplan skizzieren

---

## Inhalt

### Warum Migration schwierig ist

Ein Algorithmus wird selten „über Nacht" getauscht. Herausforderungen:

- **Bestandsdaten** sind mit dem alten Verfahren verschlüsselt/signiert.
- **Kompatibilität** mit Partnern/Clients muss gewahrt bleiben.
- **Verfügbarkeit**: keine Ausfälle während der Umstellung.

### Strategien

| Strategie | Beschreibung |
|-----------|--------------|
| **Dual-Support / Parallelbetrieb** | alt lesen, neu schreiben; beide Verfahren gleichzeitig gültig |
| **Lazy Re-Encryption** | Daten beim nächsten Zugriff ins neue Verfahren überführen |
| **Bulk Re-Encryption** | Bestandsdaten gebündelt neu verschlüsseln (geplant, ressourcenintensiv) |
| **Hybrid** | altes + neues Verfahren kombiniert (bes. bei PQC, → [[09-Hybride-kryptographische-Verfahren]]) |

### Bereits verschlüsselte Daten

> [!warning] **Prüfungsrelevant: das Re-Encryption-Problem**
> Neue Daten mit dem neuen Verfahren zu schützen ist einfach. Schwierig sind **Bestandsdaten**: Sie müssen entschlüsselt und neu verschlüsselt werden. Mit **Envelope Encryption** (→ [[03-Schluesselverteilung-und-Speicherung]]) wird das leichter, wenn nur der KEK wechselt – der DEK (und damit die Massendaten) bleiben unberührt.

### Migrationsplan (generisch)

```
1. Inventar erstellen (was ist betroffen?) → Modul 14
2. Crypto-Agility herstellen (Verfahren austauschbar) → Kapitel 03
3. Neues Verfahren einführen (Dual-Support)
4. Neu schreiben im neuen Verfahren
5. Bestandsdaten migrieren (lazy/bulk)
6. Altes Verfahren abschalten, wenn keine Altdaten mehr
```

### Konkreter Anlass: PQC

Die **Post-Quanten-Migration** (→ Modul 13) ist der aktuell wichtigste Anwendungsfall dieser Strategien – mit hybridem Übergang als empfohlenem Weg.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Migration ist schwierig wegen Bestandsdaten, Kompatibilität und Verfügbarkeit
> - Strategien: Dual-Support, Lazy/Bulk Re-Encryption, Hybrid
> - Envelope Encryption erleichtert das Re-Encryption-Problem (nur KEK wechseln)
> - Generischer Plan: Inventar → Agility → Dual-Support → neu schreiben → Altdaten migrieren → alt abschalten

---

## Übungen

1. Warum ist das Migrieren von Bestandsdaten besonders aufwändig?
2. Vergleichen Sie Lazy und Bulk Re-Encryption.
3. Wie hilft Envelope Encryption bei der Migration?

---

← [[03-Crypto-Agility-Design-Patterns|← Zurück]] | [[00-Architektur-Index|Übersicht]] | [[05-Defense-in-Depth-mit-Kryptographie|Weiter →]]
