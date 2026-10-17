---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - praxis
---

# Ende-zu-Ende-Verschlüsselung

> [!info] **Lernziele**
> - Das Prinzip der Ende-zu-Ende-Verschlüsselung verstehen
> - E2EE von Transportverschlüsselung abgrenzen
> - Chancen und gesellschaftliche Spannungsfelder einordnen

---

## Inhalt

### Was ist E2EE?

Bei **Ende-zu-Ende-Verschlüsselung (E2EE)** werden Daten **beim Sender** verschlüsselt und erst **beim Empfänger** wieder entschlüsselt. Zwischenstationen – auch der Dienstbetreiber selbst – sehen nur Chiffretext und können nicht mitlesen.

### Abgrenzung zur Transportverschlüsselung

```
Transportverschlüsselung (z. B. TLS):
  Sender ──TLS──► Server (sieht Klartext!) ──TLS──► Empfänger

Ende-zu-Ende-Verschlüsselung:
  Sender ──verschlüsselt──► Server (sieht nur Chiffretext) ──► Empfänger
```

> [!warning] **Prüfungsrelevant: TLS ≠ E2EE**
> Bei reiner Transportverschlüsselung (TLS) liegt die Nachricht **auf dem Server im Klartext** vor. Nur E2EE stellt sicher, dass selbst der Betreiber nicht mitlesen kann. Viele Dienste werben mit „Verschlüsselung", meinen aber nur Transportverschlüsselung.

### Bausteine

E2EE kombiniert die bekannten Verfahren: asymmetrischer Schlüsselaustausch zur Schlüsselvereinbarung, symmetrische AEAD-Verschlüsselung der Inhalte, Authentifizierung der Partner und idealerweise **Perfect Forward Secrecy** (→ [[06-Perfect-Forward-Secrecy]]). Das prominenteste Beispiel ist das **Signal-Protokoll** (→ [[05-Signal-Protokoll-und-Double-Ratchet]]).

### Schlüsselverifikation

Damit E2EE gegen Man-in-the-Middle schützt, müssen die Partner die **Identität** des Schlüssels prüfen – z. B. über **Sicherheitsnummern/Safety Numbers** oder QR-Code-Abgleich in Messengern.

### Spannungsfeld

E2EE steht im Zentrum gesellschaftlicher Debatten (Privatsphäre vs. staatlicher Zugriff). Technisch gilt: Eine „Hintertür" für Berechtigte schwächt die Sicherheit für alle, da sie ein zusätzliches Angriffsziel schafft.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - E2EE verschlüsselt beim Sender, entschlüsselt beim Empfänger – der Server sieht nur Chiffretext
> - Abzugrenzen von Transportverschlüsselung (TLS), bei der der Server Klartext sieht
> - Bausteine: Schlüsselaustausch, AEAD, Authentifizierung, möglichst Forward Secrecy
> - Schlüsselverifikation (Safety Numbers) schützt gegen MitM

---

## Übungen

1. Worin unterscheidet sich E2EE von Transportverschlüsselung?
2. Warum kann der Betreiber bei echter E2EE nicht mitlesen?
3. Wie schützt man sich bei E2EE gegen Man-in-the-Middle?

---

← [[03-E-Mail-Verschluesselung-OpenPGP-SMIME|← Zurück]] | [[00-Praxis-Index|Übersicht]] | [[05-Signal-Protokoll-und-Double-Ratchet|Weiter →]]
