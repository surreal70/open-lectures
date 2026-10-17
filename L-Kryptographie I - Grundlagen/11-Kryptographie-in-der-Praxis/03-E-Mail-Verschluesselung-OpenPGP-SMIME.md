---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - praxis
---

# E-Mail-Verschlüsselung OpenPGP SMIME

> [!info] **Lernziele**
> - OpenPGP und S/MIME zur E-Mail-Verschlüsselung vergleichen
> - Die unterschiedlichen Vertrauensmodelle verstehen
> - Grenzen der E-Mail-Verschlüsselung einordnen

---

## Inhalt

### Zwei konkurrierende Standards

Für Ende-zu-Ende-verschlüsselte E-Mail gibt es zwei etablierte Ansätze:

| Merkmal | OpenPGP (GPG) | S/MIME |
|---------|---------------|--------|
| Vertrauensmodell | **Web of Trust** (dezentral) | **PKI/Zertifikate** (zentrale CAs) |
| Schlüsselverteilung | Keyserver, manuell | über Zertifikate/Verzeichnisse |
| Verbreitung | technisch versiert, Open Source | Unternehmen, oft in Clients integriert |
| Format | PGP/MIME | X.509-Zertifikate |

Beide bieten **Verschlüsselung** (Vertraulichkeit) und **Signatur** (Authentizität), arbeiten hybrid und unterscheiden sich vor allem im Vertrauensmodell (→ [[05-Zertifikatsketten-und-Vertrauensmodelle]]).

### Grenzen

> [!danger] **Was E-Mail-Verschlüsselung NICHT schützt**
> - **Metadaten:** Betreff, Absender, Empfänger und Zeitpunkt bleiben bei OpenPGP/S-MIME typischerweise **unverschlüsselt** sichtbar.
> - **Komplexität:** Schlüsselverwaltung ist fehleranfällig; Nutzerfehler sind häufig.
> - **EFAIL (2018):** Schwächen in der Zusammenarbeit von Mail-Clients und HTML-Rendering ermöglichten in bestimmten Konstellationen das Ausleiten von Klartext – ein Implementierungs-, kein Algorithmusproblem.

### Einordnung

E-Mail-Verschlüsselung ist sinnvoll, aber umständlich. Für vertrauliche Kommunikation bieten moderne Messenger mit **Ende-zu-Ende-Verschlüsselung** (→ [[04-Ende-zu-Ende-Verschluesselung]], [[05-Signal-Protokoll-und-Double-Ratchet]]) oft bessere Usability und zusätzlichen Schutz (z. B. Forward Secrecy), den klassische E-Mail-Verschlüsselung nicht bietet.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - OpenPGP (Web of Trust) und S/MIME (PKI/Zertifikate) verschlüsseln und signieren E-Mail
> - Unterschied liegt v. a. im Vertrauensmodell; beide arbeiten hybrid
> - Metadaten bleiben sichtbar; Usability ist schwierig (EFAIL als Mahnung)
> - Für vertrauliche Kommunikation sind moderne E2EE-Messenger oft die bessere Wahl

---

## Übungen

1. Worin unterscheiden sich die Vertrauensmodelle von OpenPGP und S/MIME?
2. Welche Teile einer E-Mail bleiben trotz Verschlüsselung sichtbar?
3. Was war die Ursache der EFAIL-Schwachstelle?

---

← [[02-Dateiverschluesselung-mit-GPG|← Zurück]] | [[00-Praxis-Index|Übersicht]] | [[04-Ende-zu-Ende-Verschluesselung|Weiter →]]
