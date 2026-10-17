---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - asymmetrisch
  - public-key
---

# Schlüssellängen und Sicherheitsniveaus

> [!info] **Lernziele**
> - Das Konzept des Sicherheitsniveaus (Bit-Sicherheit) verstehen
> - Schlüssellängen symmetrischer und asymmetrischer Verfahren vergleichen
> - Aktuelle Empfehlungen und den Quanteneinfluss einordnen

---

## Inhalt

### Sicherheitsniveau in Bit

Das **Sicherheitsniveau** gibt an, wie viel Aufwand der beste bekannte Angriff erfordert – gemessen in Bit. „128 Bit Sicherheit" bedeutet: Ein Angreifer muss rund $2^{128}$ Operationen aufbringen, was praktisch unerreichbar ist.

Wichtig: Dieselbe Bit-Zahl bedeutet bei verschiedenen Verfahren **unterschiedliche** Schlüssellängen, weil die zugrunde liegenden Probleme unterschiedlich schwer sind.

### Vergleichstabelle (klassische Sicherheit)

| Sicherheitsniveau | Symmetrisch (AES) | RSA / DH | ECC |
|-------------------|-------------------|----------|-----|
| 112 Bit | 3DES (abgekündigt) | 2048 Bit | 224 Bit |
| 128 Bit | AES-128 | 3072 Bit | 256 Bit |
| 192 Bit | AES-192 | 7680 Bit | 384 Bit |
| 256 Bit | AES-256 | 15360 Bit | 512 Bit |

Deutlich sichtbar: RSA-Schlüssel wachsen enorm, während ECC kompakt bleibt – der Hauptgrund für den Trend zu elliptischen Kurven.

### Aktuelle Empfehlungen

Richtlinien wie **NIST SP 800-57** und **BSI TR-02102** (→ Modul 14) empfehlen heute mindestens **128 Bit** Sicherheit:

- Symmetrisch: AES-128 oder AES-256
- RSA/DH: mindestens 3072 Bit
- ECC: mindestens 256 Bit (z. B. P-256, Curve25519)

RSA-2048 (112 Bit) gilt nur noch als Übergang und sollte für langfristig schützenswerte Daten vermieden werden.

### Einfluss von Quantencomputern

> [!warning] **Prüfungsrelevant: Quanteneinfluss**
> - **Symmetrisch:** Grover halbiert die Sicherheit – AES-256 bietet dann noch ~128 Bit und bleibt nutzbar.
> - **Asymmetrisch:** Shor bricht RSA und ECC vollständig – unabhängig von der Schlüssellänge. Hier hilft nur der Wechsel zu Post-Quanten-Verfahren (→ Modul 13).

### Krypto-Agilität

Da sich Empfehlungen und Bedrohungen ändern, sollten Systeme **Crypto-Agility** vorsehen: Algorithmen und Schlüssellängen müssen austauschbar sein, ohne die Architektur neu zu bauen (→ Modul 14 und 20).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Sicherheitsniveau in Bit misst den Angriffsaufwand ($\sim 2^{n}$)
> - Gleiches Niveau = sehr unterschiedliche Schlüssellängen (ECC ≪ RSA)
> - Heutiger Mindeststandard: 128 Bit (AES-128, RSA-3072, ECC-256)
> - Quanten: Grover halbiert symmetrisch, Shor bricht RSA/ECC → PQC; Crypto-Agility einplanen

---

## Übungen

1. Welche RSA- und ECC-Schlüssellänge entsprechen jeweils 128 Bit Sicherheit?
2. Warum bleibt AES-256 auch im Quantenzeitalter brauchbar, RSA-3072 aber nicht?
3. Was bedeutet Crypto-Agility und warum ist sie wichtig?

---

← [[06-RSA-OAEP-und-hybride-Verschlüsselung|← Zurück]] | [[00-Asymmetrisch-Index|Übersicht]] | [[00-Hashfunktionen-Index|Nächstes Modul →]]
