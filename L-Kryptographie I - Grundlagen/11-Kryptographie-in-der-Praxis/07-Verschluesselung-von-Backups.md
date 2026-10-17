---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - praxis
---

# Verschlüsselung von Backups

> [!info] **Lernziele**
> - Die Notwendigkeit verschlüsselter Backups verstehen
> - Das Spannungsfeld Verschlüsselung vs. Wiederherstellbarkeit einordnen
> - Best Practices für Backup-Schlüssel kennen

---

## Inhalt

### Warum Backups verschlüsseln?

Backups enthalten oft eine **vollständige Kopie** sensibler Daten – und liegen häufig an weniger geschützten Orten (externe Medien, Cloud, Offsite). Ein gestohlenes unverschlüsseltes Backup ist ein Totalverlust der Vertraulichkeit. Daher: Backups **immer verschlüsseln**.

### Das zentrale Dilemma

> [!warning] **Prüfungsrelevant: Backup-Schlüssel**
> Ein verschlüsseltes Backup ist nur so gut wie die Verfügbarkeit seines Schlüssels. **Geht der Schlüssel verloren, ist das Backup wertlos** – man hat sich selbst ausgesperrt. Umgekehrt darf der Schlüssel nicht zusammen mit dem Backup gespeichert werden. Dieses Dilemma löst man mit durchdachtem Schlüsselmanagement (→ Modul 10), inklusive Secret Sharing (→ [[09-Secret-Sharing-und-Backup-Konzepte]]).

### Verschlüsselungsansätze

- **Clientseitig vor dem Upload:** Daten werden lokal verschlüsselt, der Backup-Anbieter sieht nur Chiffretext (echtes „Zero-Knowledge"-Backup).
- **Serverseitig:** der Anbieter verschlüsselt – schützt bei Festplattendiebstahl, aber der Anbieter hat (potenziell) Zugriff.

Für maximale Vertraulichkeit ist **clientseitige** Verschlüsselung mit eigenem Schlüssel vorzuziehen.

### Best Practices

- **AEAD-Verschlüsselung** (AES-GCM / ChaCha20-Poly1305) für Vertraulichkeit **und** Integrität.
- **3-2-1-Regel** kombiniert mit Verschlüsselung: 3 Kopien, 2 Medien, 1 offsite – alle verschlüsselt.
- **Schlüssel getrennt vom Backup** aufbewahren, redundant gesichert (z. B. via Secret Sharing).
- **Wiederherstellung regelmäßig testen** – inklusive Entschlüsselung. Ein nie getestetes Backup ist kein Backup.
- **Unveränderliche (immutable) Backups** gegen Ransomware erwägen.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Backups immer verschlüsseln – sie sind vollständige Datenkopien an exponierten Orten
> - Dilemma: Schlüsselverlust macht das Backup wertlos, Schlüssel nie beim Backup lagern
> - Clientseitige Verschlüsselung bietet die höchste Vertraulichkeit
> - Best Practices: AEAD, 3-2-1-Regel, getrennte redundante Schlüssel, Restore-Tests

---

## Übungen

1. Warum müssen Backups verschlüsselt werden?
2. Welches Dilemma besteht bei Backup-Schlüsseln und wie löst man es?
3. Worin unterscheidet sich clientseitige von serverseitiger Backup-Verschlüsselung?

---

← [[06-Datenbankverschluesselung|← Zurück]] | [[00-Praxis-Index|Übersicht]] | [[08-Kryptographie-in-Cloud-Umgebungen|Weiter →]]
