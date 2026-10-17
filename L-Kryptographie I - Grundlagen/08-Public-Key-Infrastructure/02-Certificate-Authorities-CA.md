---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - pki
---

# Certificate Authorities CA

> [!info] **Lernziele**
> - Aufgaben und Verantwortung einer Certificate Authority verstehen
> - Die Risiken einer kompromittierten CA einordnen
> - Verschiedene CA-Typen kennen

---

## Inhalt

### Rolle der CA

Eine **Certificate Authority (CA)** ist die vertrauenswürdige Instanz, die digitale Zertifikate ausstellt. Sie bestätigt mit ihrer **Signatur**, dass ein öffentlicher Schlüssel zu einer geprüften Identität gehört. Das Vertrauen aller Teilnehmer gründet letztlich auf der Integrität der CA.

### Aufgaben

- **Identitätsprüfung** (oft über eine RA) vor der Ausstellung
- **Ausstellung** und Signatur von Zertifikaten
- **Verwaltung** des eigenen Schlüsselmaterials (Schutz des privaten CA-Schlüssels, meist im HSM, → Modul 10)
- **Sperrung** kompromittierter Zertifikate und Veröffentlichung des Status (CRL/OCSP)

### CA-Typen

| Typ | Beschreibung |
|-----|--------------|
| **Öffentliche CA** | vertrauenswürdig für Internet-TLS (z. B. Let's Encrypt), in Browsern vorinstalliert |
| **Interne/Unternehmens-CA** | für organisationsinterne Zertifikate (VPN, interne Dienste) |
| **Root-CA** | oberste Instanz, offline gehalten (→ [[03-Root--und-Intermediate-Zertifikate]]) |
| **Intermediate-CA** | stellt im Alltag aus, von der Root signiert |

### Das zentrale Risiko

> [!danger] **Kompromittierte CA**
> Wird der private Schlüssel einer CA gestohlen, kann der Angreifer **beliebige gültige Zertifikate** fälschen – für jede Domain. Reale Vorfälle: Der **DigiNotar-Hack (2011)** führte zu gefälschten Google-Zertifikaten und zur vollständigen Entfernung der CA aus allen Browsern. Deshalb werden Root-Schlüssel offline und in HSMs gehalten und der Betrieb streng auditiert.

### Validierungsstufen

Öffentliche CAs stellen Zertifikate in verschiedenen Prüftiefen aus: **DV** (Domain Validation, nur Domainkontrolle), **OV** (Organization Validation) und **EV** (Extended Validation, umfangreiche Organisationsprüfung).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Die CA signiert Zertifikate und bürgt für die Identität-Schlüssel-Zuordnung
> - Aufgaben: Prüfung, Ausstellung, Schlüsselschutz, Sperrung
> - Root-CAs bleiben offline; Intermediate-CAs stellen im Alltag aus
> - Eine kompromittierte CA (z. B. DigiNotar 2011) gefährdet das gesamte Vertrauen

---

## Übungen

1. Welche Kernaufgaben hat eine CA?
2. Warum werden Root-CA-Schlüssel offline gehalten?
3. Welche Folgen hatte der DigiNotar-Vorfall?

---

← [[01-Architektur-einer-PKI|← Zurück]] | [[00-PKI-Index|Übersicht]] | [[03-Root--und-Intermediate-Zertifikate|Weiter →]]
