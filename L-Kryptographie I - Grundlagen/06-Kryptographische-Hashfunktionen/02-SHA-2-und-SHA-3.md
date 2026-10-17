---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - hash
---

# SHA-2 und SHA-3

> [!info] **Lernziele**
> - Die Vorgänger MD5 und SHA-1 und ihren gebrochenen Status kennen
> - Die SHA-2-Familie und ihre Varianten kennen
> - SHA-3 und das zugrunde liegende Schwamm-Prinzip verstehen
> - Die Unterschiede und Einsatzempfehlungen einordnen

---

## Inhalt

### Die Vorgänger: MD5 und SHA-1

Vor SHA-2 prägten zwei Funktionen die Praxis – beide gelten heute als **unsicher**:

- **MD5** (Rivest, 1992, 128 Bit): lange Standard, heute **kollisionsgebrochen**. Kollisionen lassen sich in Sekunden erzeugen; 2008 wurde darüber ein gefälschtes CA-Zertifikat demonstriert, 2012 missbrauchte die Schadsoftware **Flame** MD5-Kollisionen.
- **SHA-1** (NIST, 1995, 160 Bit): direkter Vorläufer von SHA-2, ebenfalls **kollisionsgebrochen**. 2017 zeigten Google und CWI mit **„SHAttered"** die erste praktische Kollision (zwei verschiedene PDFs mit identischem SHA-1).

> [!danger] **MD5 und SHA-1 nicht mehr verwenden**
> Für Signaturen, Zertifikate oder Integritätsschutz gegen Angreifer sind MD5 und SHA-1 **verboten**. Ihre Ausgaben (128/160 Bit) sind zudem zu kurz – wegen des Geburtstagsparadoxons (→ [[04-Kollisionsresistenz-und-Preimage-Resistenz]]) bieten sie nur 64 bzw. 80 Bit Kollisionssicherheit. Als reine nicht-sicherheitsrelevante Prüfsumme (gegen zufällige Fehler, nicht gegen Angreifer) ist MD5 technisch noch anzutreffen, aber das ist kein kryptographischer Einsatz.

### SHA-2

**SHA-2** (2001 vom NIST standardisiert) ist heute die am weitesten verbreitete Hashfunktionsfamilie. Sie umfasst mehrere Varianten mit unterschiedlicher Ausgabelänge:

| Variante | Ausgabe |
|----------|---------|
| SHA-224 | 224 Bit |
| SHA-256 | 256 Bit |
| SHA-384 | 384 Bit |
| SHA-512 | 512 Bit |

SHA-2 basiert auf der **Merkle-Damgård-Konstruktion**: Die Nachricht wird in Blöcke zerlegt, die nacheinander über eine Kompressionsfunktion den internen Zustand fortschreiben.

> [!note] **Length-Extension-Angriff**
> Die Merkle-Damgård-Struktur erlaubt einen **Length-Extension-Angriff**: Kennt man $H(m)$ und die Länge von $m$, kann man $H(m \,\|\, \text{Erweiterung})$ berechnen, ohne $m$ zu kennen. Deshalb darf man einen MAC **nicht** naiv als $H(\text{Schlüssel} \,\|\, m)$ bauen – man nutzt HMAC (→ [[05-Message-Authentication-Codes-MAC-HMAC]]).

### SHA-3

**SHA-3** (2015, Keccak) entstand aus einem offenen NIST-Wettbewerb – nicht, weil SHA-2 gebrochen wäre, sondern als strukturell **unabhängige Alternative**. SHA-3 nutzt eine völlig andere Konstruktion, das **Schwamm-Prinzip (Sponge)**:

- **Absorbieren:** Die Nachricht wird blockweise in einen großen internen Zustand „eingesogen".
- **Auspressen:** Beliebig viel Ausgabe wird wieder „ausgepresst".

Durch das Sponge-Design ist SHA-3 **immun gegen Length-Extension-Angriffe**. Varianten: SHA3-256, SHA3-512 sowie die Funktionen mit variabler Ausgabelänge **SHAKE128/SHAKE256**.

### Vergleich und Empfehlung

| Funktion | Jahr | Ausgabe | Status |
|----------|------|---------|--------|
| MD5 | 1992 | 128 Bit | kollisionsgebrochen – nicht verwenden |
| SHA-1 | 1995 | 160 Bit | kollisionsgebrochen (SHAttered) – nicht verwenden |
| **SHA-256** | 2001 | 256 Bit | **sicher** (Merkle-Damgård) |
| **SHA-3** | 2015 | variabel | **sicher** (Sponge) |

SHA-2 und SHA-3 gelten als **sicher**. SHA-256 ist der De-facto-Standard; SHA-3 ist die empfohlene Wahl, wenn man Length-Extension-Probleme vermeiden oder algorithmische Vielfalt (Crypto-Agility) sicherstellen will. MD5 und SHA-1 sind nur noch von historischer Bedeutung.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Vorgänger MD5 (128 Bit) und SHA-1 (160 Bit) sind kollisionsgebrochen – nicht verwenden
> - SHA-2: Merkle-Damgård, Varianten 224/256/384/512, weit verbreitet
> - SHA-2 ist anfällig für Length-Extension → HMAC statt naivem Hash-MAC
> - SHA-3 (Keccak): Sponge-Konstruktion, immun gegen Length-Extension
> - SHA-256 Standard, SHA-3 als unabhängige Alternative

---

## Übungen

1. Warum dürfen MD5 und SHA-1 nicht mehr für Signaturen verwendet werden?
2. Welche Ausgabelängen bietet die SHA-2-Familie?
3. Was ist ein Length-Extension-Angriff und warum ist SHA-3 dagegen immun?
4. Erklären Sie das Absorbieren und Auspressen beim Schwamm-Prinzip.

---

← [[01-Eigenschaften-kryptographischer-Hashfunktionen|← Zurück]] | [[00-Hashfunktionen-Index|Übersicht]] | [[03-BLAKE2-und-BLAKE3|Weiter →]]
