---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - pki
---

# Root- und Intermediate-Zertifikate

> [!info] **Lernziele**
> - Den Unterschied zwischen Root- und Intermediate-Zertifikaten verstehen
> - Die Gründe für die gestufte Hierarchie nachvollziehen
> - Den Schutz des Root-Schlüssels einordnen

---

## Inhalt

### Die gestufte Hierarchie

PKIs verwenden fast nie direkt die Root-CA zum Ausstellen von Endnutzer-Zertifikaten. Stattdessen gibt es eine **Hierarchie**:

```
Root-CA  (selbstsigniert, offline)
   │ signiert
Intermediate-CA  (online, stellt im Alltag aus)
   │ signiert
Endnutzer-Zertifikat  (z. B. example.com)
```

### Root-Zertifikat

- **Selbstsigniert:** Die Root-CA signiert ihr eigenes Zertifikat – sie ist der Vertrauensanker.
- **Vorinstalliert:** Root-Zertifikate sind in Betriebssystemen und Browsern hinterlegt.
- **Offline gehalten:** Der private Root-Schlüssel wird möglichst selten und nur offline (Air-Gap, HSM) genutzt.

### Intermediate-Zertifikat

- Von der Root-CA signiert, übernimmt das **tägliche Ausstellen**.
- Dadurch bleibt der Root-Schlüssel geschützt; nur die Intermediate ist online exponiert.

### Warum diese Trennung?

> [!tip] **Sicherheit durch Isolation**
> Wird eine Intermediate-CA kompromittiert, kann sie gesperrt und ersetzt werden, **ohne** die Root (und damit das in Milliarden Geräten verankerte Vertrauen) auszutauschen. Müsste man die Root tauschen, wäre ein globales Software-Update nötig. Die Trennung begrenzt also den Schaden und erleichtert die Wiederherstellung.

### Prüfung

Beim Verbindungsaufbau sendet ein Server i. d. R. sein Zertifikat **plus** die Intermediate(s). Der Client baut daraus die Kette bis zu einer vertrauenswürdigen Root zusammen (→ [[05-Zertifikatsketten-und-Vertrauensmodelle]]).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Root-CA: selbstsigniert, vorinstalliert, offline – der Vertrauensanker
> - Intermediate-CA: von der Root signiert, stellt im Alltag aus
> - Die Trennung schützt den Root-Schlüssel und begrenzt Schäden bei Kompromittierung
> - Der Client baut die Kette vom Server- über Intermediate- zum Root-Zertifikat

---

## Übungen

1. Warum ist ein Root-Zertifikat selbstsigniert?
2. Welchen Vorteil bietet die Trennung in Root- und Intermediate-CA?
3. Welche Zertifikate sendet ein Server typischerweise beim Verbindungsaufbau?

---

← [[02-Certificate-Authorities-CA|← Zurück]] | [[00-PKI-Index|Übersicht]] | [[04-X509-Zertifikate|Weiter →]]
