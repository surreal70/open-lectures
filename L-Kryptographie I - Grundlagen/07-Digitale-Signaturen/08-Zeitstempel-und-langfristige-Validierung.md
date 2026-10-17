---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - signaturen
---

# Zeitstempel und langfristige Validierung

> [!info] **Lernziele**
> - Zweck kryptographischer Zeitstempel verstehen
> - Das Problem der langfristigen Signaturgültigkeit erkennen
> - Mechanismen zur Langzeitvalidierung einordnen

---

## Inhalt

### Warum Zeitstempel?

Eine Signatur allein beantwortet nicht die Frage: **Wann** wurde signiert? Das ist aber entscheidend, denn:

- Zertifikate laufen ab oder werden gesperrt.
- Algorithmen altern und werden gebrochen (vgl. MD5/SHA-1 → [[04-Kollisionsresistenz-und-Preimage-Resistenz]]).

Ein **kryptographischer Zeitstempel** belegt, dass ein Dokument zu einem bestimmten Zeitpunkt bereits in dieser Form existierte.

### Trusted Timestamping (TSA)

Eine **Time Stamping Authority (TSA)** signiert den Hash eines Dokuments zusammen mit der aktuellen Zeit (Standard: RFC 3161):

```
1. Client sendet H(Dokument) an die TSA
2. TSA signiert { H(Dokument), Zeitpunkt }
3. Zeitstempel-Token wird an das Dokument angehängt
```

Damit ist beweisbar, dass die Signatur **vor** Ablauf oder Bruch des Zertifikats gültig erstellt wurde.

### Das Problem der Langzeitgültigkeit

Soll eine Signatur über Jahrzehnte gültig bleiben (z. B. Verträge, Archive), reichen Zertifikat und Algorithmus allein nicht aus. Lösungsmechanismen:

- **Validierungsdaten einbetten:** Zertifikatskette und Sperrinformationen (CRL/OCSP, → Modul 8) werden zum Signaturzeitpunkt mitgespeichert, damit die Prüfung auch später nachvollziehbar bleibt.
- **Archiv-Zeitstempel erneuern:** Bevor ein Algorithmus oder Zeitstempel schwach wird, wird ein **neuer** Zeitstempel (mit stärkerem Verfahren) über die bestehende Signatur gelegt. So entsteht eine Kette, die die Gültigkeit fortschreibt.

Diese Konzepte sind in **PAdES-LTV** (Long-Term Validation) und dem Profil **AdES-A** (Archival) standardisiert.

> [!tip] **Grundidee**
> Langzeitvalidierung „friert" den Vertrauensstatus zum Signaturzeitpunkt ein und erneuert den Schutz, bevor die zugrunde liegende Kryptographie veraltet – ein praktisches Beispiel für Crypto-Agility (→ Modul 14).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Zeitstempel belegen den Zeitpunkt einer Signatur – wichtig bei Ablauf/Bruch von Zertifikaten
> - Eine TSA signiert Hash + Zeit (RFC 3161)
> - Langzeitgültigkeit erfordert eingebettete Validierungsdaten und erneuerte Archiv-Zeitstempel
> - Standardisiert u. a. in PAdES-LTV / AdES-A

---

## Übungen

1. Welche Frage beantwortet ein Zeitstempel, die eine Signatur allein nicht klärt?
2. Wie funktioniert Trusted Timestamping nach RFC 3161?
3. Warum müssen Archiv-Zeitstempel erneuert werden?

---

← [[07-Dokumentensignaturen|← Zurück]] | [[00-Signaturen-Index|Übersicht]] | [[00-PKI-Index|Nächstes Modul →]]
