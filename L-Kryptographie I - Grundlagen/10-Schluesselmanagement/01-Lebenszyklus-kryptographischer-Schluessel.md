---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - schluessel
---

# Lebenszyklus kryptographischer Schlüssel

> [!info] **Lernziele**
> - Die Phasen des Schlüssellebenszyklus kennen
> - Verstehen, warum Schlüsselmanagement oft die größte Schwachstelle ist
> - Die Bedeutung von Schlüsseltrennung einordnen

---

## Inhalt

### Warum Schlüsselmanagement?

Nach Kerckhoffs' Prinzip (→ [[06-Kerckhoffs-Prinzip]]) ruht die gesamte Sicherheit auf dem **Schlüssel**. In der Praxis scheitern Systeme selten an gebrochener Mathematik, sondern an schlechtem **Schlüsselmanagement**: schwach erzeugte, unsicher gespeicherte oder nie erneuerte Schlüssel.

### Der Lebenszyklus

```
Generierung → Verteilung → Speicherung → Nutzung
          → Rotation → Sperrung/Widerruf → Archivierung → Vernichtung
```

| Phase | Kernfrage |
|-------|-----------|
| **Generierung** | Ausreichend Entropie? (→ [[02-Sichere-Schluesselgenerierung]]) |
| **Verteilung/Speicherung** | Wie gelangt/liegt der Schlüssel sicher? (→ [[03-Schluesselverteilung-und-Speicherung]]) |
| **Nutzung** | Nur für den vorgesehenen Zweck? |
| **Rotation** | Regelmäßiger Austausch (→ [[05-Key-Rotation-und-Key-Revocation]]) |
| **Sperrung** | Bei Kompromittierung sofort widerrufen |
| **Vernichtung** | Sicheres Löschen (kein Rest im Speicher/Backup) |

### Grundprinzipien

- **Schlüsseltrennung:** Für verschiedene Zwecke verschiedene Schlüssel verwenden (z. B. nicht denselben Schlüssel für Verschlüsselung und Signatur). So begrenzt ein kompromittierter Schlüssel den Schaden.
- **Least Privilege:** Zugriff auf Schlüssel auf das Nötigste beschränken.
- **Schutz des privaten/geheimen Materials:** möglichst in HSM/TPM/KMS (→ Kapitel 6–8), nicht im Klartext auf Festplatte.

> [!danger] **Typische Fehler**
> - Schlüssel fest im Quellcode ("hardcoded") oder in Git-Repositories.
> - Gemeinsamer Schlüssel für alles.
> - Keine Rotation, kein Widerrufsplan.
> Diese Fehler sind in der Praxis weit häufiger als kryptographische Schwächen.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Die gesamte Sicherheit hängt am Schlüssel – Management ist entscheidend
> - Lebenszyklus: Generierung → Verteilung → Speicherung → Nutzung → Rotation → Sperrung → Vernichtung
> - Grundprinzipien: Schlüsseltrennung, Least Privilege, Schutz durch HSM/TPM/KMS
> - Häufigste reale Schwachstelle: hardcodierte/ungeschützte Schlüssel

---

## Übungen

1. Nennen Sie die Phasen des Schlüssellebenszyklus.
2. Warum sollte man für Verschlüsselung und Signatur getrennte Schlüssel nutzen?
3. Nennen Sie zwei typische Fehler im Schlüsselmanagement.

---

← [[00-Schluessel-Index|Übersicht]] | [[02-Sichere-Schluesselgenerierung|Weiter →]]
