---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - secdev
  - vertiefung
---

# Memory Safety und Side Channels

> [!info] **Lernziele**
> - Den Zusammenhang von Memory Safety und Krypto-Sicherheit verstehen
> - Maßnahmen gegen Seitenkanäle im Code kennen
> - Den sicheren Umgang mit Schlüsselmaterial im Speicher beachten

---

## Inhalt

### Memory Safety

Selbst perfekte Kryptographie nützt nichts, wenn der umgebende Code **Speicherfehler** hat. Das prominenteste Beispiel ist **Heartbleed** (2014): ein Buffer-Over-Read in OpenSSL gab Speicherinhalte – inklusive privater Schlüssel – preis (→ [[10-Sicherheitsanalyse-realer-Vorfaelle]]).

> [!tip] **Speichersichere Sprachen**
> Sprachen wie **Rust**, Go oder Java verhindern große Klassen von Speicherfehlern (Buffer Overflows, Use-after-free) von vornherein. Für neue Krypto-nahe Projekte sind sie C/C++ vorzuziehen. In C/C++ sind strenge Reviews, Sanitizer und Fuzzing Pflicht.

### Schlüsselmaterial im Speicher

> [!warning] **Geheimnisse nicht im Speicher liegen lassen**
> - Schlüssel nach Gebrauch **überschreiben/löschen** (z. B. `sodium_memzero`). Vorsicht: Compiler optimieren naives Nullsetzen oft weg.
> - Auslagern in **Swap** oder **Core-Dumps** vermeiden (Speicher sperren, z. B. `mlock`).
> - Geheimnisse möglichst kurz im Klartext halten; idealerweise im HSM/TEE (→ Modul 10, 18).

### Seitenkanäle im Code

Auch korrekter Code kann über **Seitenkanäle** leaken (→ [[05-Side-Channel-Angriffe]]). Entwicklerrelevante Gegenmaßnahmen:

- **Konstante-Zeit-Operationen** für Geheimnisse (keine datenabhängigen Zweige/Zugriffe, → [[04-Timing-Angriffe]]).
- **Konstante-Zeit-Vergleich** für MACs/Tokens (`timingSafeEqual`, `compare_digest`).
- Bevorzugt **Primitive ohne datenabhängige Tabellen** (ChaCha20, X25519).

### Zusammenspiel

Krypto-Sicherheit ist nur so stark wie der **gesamte** Code drumherum: Speicherfehler, Seitenkanäle und schlampiger Umgang mit Geheimnissen untergraben jede noch so starke Chiffre.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Speicherfehler (z. B. Heartbleed) können Schlüssel leaken – unabhängig vom Algorithmus
> - Speichersichere Sprachen (Rust/Go) vermeiden ganze Fehlerklassen
> - Schlüsselmaterial sicher löschen, Swap/Core-Dumps vermeiden, möglichst im HSM/TEE
> - Konstante-Zeit-Code und tabellenfreie Primitive gegen Seitenkanäle

---

## Übungen

1. Wie konnte Heartbleed trotz korrekter Kryptographie Schlüssel offenlegen?
2. Welche Vorsichtsmaßnahmen gelten für Schlüsselmaterial im Speicher?
3. Welche entwicklerseitigen Maßnahmen reduzieren Timing-Seitenkanäle?

---

← [[04-Secure-Random-und-Entropy|← Zurück]] | [[00-SecDev-Index|Übersicht]] | [[06-Testing-und-Auditing-von-Crypto-Code|Weiter →]]
