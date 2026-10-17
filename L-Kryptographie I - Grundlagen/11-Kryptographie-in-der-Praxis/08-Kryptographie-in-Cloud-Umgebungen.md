---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - praxis
---

# Kryptographie in Cloud-Umgebungen

> [!info] **Lernziele**
> - Kryptographische Schutzmaßnahmen in der Cloud einordnen
> - Das Modell der geteilten Verantwortung verstehen
> - Datenschutz- und Souveränitätsaspekte kennen

---

## Inhalt

### Das Modell der geteilten Verantwortung

In der Cloud ist Sicherheit **geteilt**: Der Anbieter sichert die Infrastruktur („Security **of** the Cloud"), der Kunde ist für die korrekte Nutzung verantwortlich („Security **in** the Cloud") – inklusive Verschlüsselung und Schlüsselmanagement.

### Schutz in drei Zuständen

| Zustand | Maßnahme |
|---------|----------|
| **At Rest** | Storage-Verschlüsselung, KMS-verwaltete Schlüssel (→ Modul 10) |
| **In Transit** | TLS zwischen Diensten und zum Kunden (→ Modul 9) |
| **In Use** | Confidential Computing / TEEs (→ Modul 18) |

### Wer kontrolliert die Schlüssel?

> [!warning] **Prüfungsrelevant: Schlüsselhoheit**
> Entscheidend ist, **wer die Schlüssel kontrolliert**:
> - **Anbieter-verwaltet:** bequem, aber der Anbieter kann (potenziell) entschlüsseln.
> - **BYOK:** Kunde bringt eigenes Schlüsselmaterial ein.
> - **HYOK / externes HSM:** Schlüssel verbleibt beim Kunden; der Anbieter kann nicht entschlüsseln.
> Für sensible Daten in der Cloud ist clientseitige bzw. HYOK-Verschlüsselung die stärkste Option (→ [[08-Cloud-Key-Management-Services-KMS]]).

### Datenschutz und Souveränität

Bei personenbezogenen Daten sind rechtliche Rahmen (DSGVO, → Modul 14) und die **Datensouveränität** relevant: In welcher Jurisdiktion liegen Daten und Schlüssel? Clientseitige Verschlüsselung mit kundeneigenen Schlüsseln reduziert die Abhängigkeit vom Anbieter und das Risiko fremden Zugriffs.

### Typische Fehler

> [!danger] **Häufige Cloud-Fehlkonfigurationen**
> - Offen zugängliche Storage-Buckets ohne Verschlüsselung/Zugriffsschutz.
> - Schlüssel und Secrets im Code oder in Umgebungsvariablen statt im KMS/Secret Manager.
> - Zu weite IAM-Rechte auf Schlüssel (kein Least Privilege).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Cloud-Sicherheit ist geteilte Verantwortung: Anbieter (Infrastruktur) vs. Kunde (Nutzung)
> - Schutz in drei Zuständen: at rest, in transit, in use (Confidential Computing)
> - Schlüsselhoheit ist entscheidend: Anbieter-verwaltet vs. BYOK vs. HYOK
> - Datensouveränität/DSGVO beachten; häufige Fehler sind offene Buckets und ungeschützte Secrets

---

## Übungen

1. Was besagt das Modell der geteilten Verantwortung?
2. Worin unterscheiden sich anbieter-verwaltete Schlüssel, BYOK und HYOK?
3. Nennen Sie zwei typische kryptographische Fehlkonfigurationen in der Cloud.

---

← [[07-Verschluesselung-von-Backups|← Zurück]] | [[00-Praxis-Index|Übersicht]] | [[00-Angriffe-Index|Nächstes Modul →]]
