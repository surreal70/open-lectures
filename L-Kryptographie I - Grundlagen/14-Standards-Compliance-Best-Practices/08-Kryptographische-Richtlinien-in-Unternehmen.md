---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - standards
---

# Kryptographische Richtlinien in Unternehmen

> [!info] **Lernziele**
> - Zweck einer kryptographischen Richtlinie verstehen
> - Typische Inhalte kennen
> - Die Rolle für Governance und Compliance einordnen

---

## Inhalt

### Warum eine Richtlinie?

Ohne verbindliche Vorgaben trifft jedes Team eigene (oft inkonsistente oder unsichere) Krypto-Entscheidungen. Eine **kryptographische Richtlinie (Crypto Policy)** legt organisationsweit fest, **welche** Verfahren **wie** einzusetzen sind – und schafft damit Konsistenz, Sicherheit und Nachweisbarkeit.

### Typische Inhalte

| Bereich | Festlegungen |
|---------|--------------|
| **Zugelassene Algorithmen** | z. B. AES-256, SHA-256+, ECDSA/Ed25519; **verbotene** Verfahren (MD5, SHA-1, DES, ECB) |
| **Schlüssellängen** | Mindestvorgaben nach NIST/BSI (→ [[02-BSI-TR-02102]]) |
| **Schlüsselmanagement** | Erzeugung, Speicherung (HSM/KMS), Rotation, Vernichtung (→ Modul 10) |
| **Protokolle** | nur TLS 1.2+/1.3, SSH mit Public-Key etc. |
| **Zertifikate** | CA-Nutzung, Laufzeiten, Erneuerung (→ Modul 8) |
| **Verantwortlichkeiten** | wer entscheidet, wer prüft, wer betreibt |
| **Ausnahmen & Review** | Abweichungen dokumentieren, regelmäßig überprüfen |

### Einbettung in die Governance

> [!tip] **Teil des ISMS**
> Eine Crypto Policy ist in der Regel Bestandteil des **ISMS** nach ISO 27001 (→ [[04-ISO-IEC-27001-und-Kryptographie]]). Sie übersetzt abstrakte Standards (NIST, BSI) in **konkrete, verbindliche** Vorgaben für die eigene Organisation und verweist auf das Krypto-Inventar und Risikomanagement (→ [[09-Kryptographisches-Inventar-und-Risikomanagement]]).

### Lebender Charakter

Eine gute Richtlinie ist **nicht statisch**: Sie wird regelmäßig an neue Standards, Bedrohungen (PQC!) und Prognosezeiträume angepasst – und ist damit praktischer Ausdruck von **Crypto-Agility** (→ [[07-Crypto-Agility]]).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Eine Crypto Policy legt organisationsweit erlaubte/verbotene Verfahren und deren Einsatz fest
> - Inhalte: Algorithmen, Schlüssellängen, Schlüsselmanagement, Protokolle, Zertifikate, Rollen
> - Teil des ISMS (ISO 27001); übersetzt Standards in verbindliche Vorgaben
> - Wird regelmäßig aktualisiert (gelebte Crypto-Agility)

---

## Übungen

1. Welchen Zweck erfüllt eine kryptographische Richtlinie?
2. Nennen Sie vier typische Inhalte einer solchen Richtlinie.
3. Warum muss eine Crypto Policy regelmäßig aktualisiert werden?

---

← [[07-Crypto-Agility|← Zurück]] | [[00-Standards-Index|Übersicht]] | [[09-Kryptographisches-Inventar-und-Risikomanagement|Weiter →]]
