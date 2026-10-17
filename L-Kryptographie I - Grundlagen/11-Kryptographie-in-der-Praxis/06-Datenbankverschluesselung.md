---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - praxis
---

# Datenbankverschlüsselung

> [!info] **Lernziele**
> - Verschiedene Ebenen der Datenbankverschlüsselung unterscheiden
> - Den Zielkonflikt zwischen Schutz und Durchsuchbarkeit verstehen
> - Ansätze wie TDE und applikationsseitige Verschlüsselung einordnen

---

## Inhalt

### Verschlüsselungsebenen

Datenbanken lassen sich auf unterschiedlichen Ebenen schützen:

| Ebene | Was wird geschützt | Gegen wen |
|-------|--------------------|-----------|
| **Transport** (TLS) | Verbindung Client↔DB | Netzwerk-Angreifer |
| **Storage / TDE** | Datendateien auf der Platte | Diebstahl der Datenträger |
| **Spalten/Feld** | einzelne sensible Felder | DB-interne Zugriffe |
| **Applikationsseitig** | Daten vor dem Schreiben | auch DB-Admin / Cloud-Betreiber |

### Transparent Data Encryption (TDE)

**TDE** verschlüsselt die Datenbankdateien auf Speicherebene transparent für die Anwendung. Es schützt **Data at Rest** (gestohlene Festplatten/Backups), aber **nicht** gegen Angreifer mit gültigem DB-Zugang – für die DB-Engine liegen die Daten im Betrieb im Klartext vor.

### Applikationsseitige Verschlüsselung

Hier verschlüsselt die **Anwendung** sensible Felder, bevor sie in die DB geschrieben werden. Vorteil: Selbst DB-Administrator oder Cloud-Betreiber sehen nur Chiffretext. Nachteil: Die DB kann über verschlüsselte Felder **nicht sinnvoll suchen/indizieren**.

### Der Zielkonflikt

> [!warning] **Prüfungsrelevant: Schutz vs. Durchsuchbarkeit**
> Je stärker ein Feld verschlüsselt ist, desto weniger kann die Datenbank damit arbeiten (Suche, Sortierung, Joins). Kompromisse wie **deterministische** Verschlüsselung (gleicher Klartext → gleicher Chiffretext, erlaubt Gleichheitssuche) schwächen die Sicherheit (Muster erkennbar, vgl. ECB). Spezialverfahren wie **suchbare** oder **homomorphe** Verschlüsselung (→ Modul 18) adressieren das, sind aber komplex und teuer.

### Empfehlung

- **Immer:** Transportverschlüsselung (TLS) und Schutz der Backups (→ [[07-Verschluesselung-von-Backups]]).
- **Sensible Felder** (Passwörter, PII): applikationsseitig, Passwörter zusätzlich gehasht (→ [[06-Passwort-Hashing-PBKDF2-bcrypt-scrypt-Argon2id]]).
- Schlüssel in HSM/KMS halten (→ Modul 10).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Schutzebenen: Transport (TLS), Storage/TDE, Spalten/Feld, applikationsseitig
> - TDE schützt Data at Rest, nicht gegen Angreifer mit DB-Zugang
> - Applikationsseitige Verschlüsselung schützt am stärksten, erschwert aber Suche/Index
> - Zielkonflikt Schutz vs. Durchsuchbarkeit; deterministische Verschlüsselung ist ein schwacher Kompromiss

---

## Übungen

1. Was schützt TDE – und was nicht?
2. Welchen Vorteil und welchen Nachteil hat applikationsseitige Verschlüsselung?
3. Warum schwächt deterministische Verschlüsselung die Sicherheit?

---

← [[05-Signal-Protokoll-und-Double-Ratchet|← Zurück]] | [[00-Praxis-Index|Übersicht]] | [[07-Verschluesselung-von-Backups|Weiter →]]
