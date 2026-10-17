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

# Secure Random und Entropy

> [!info] **Lernziele**
> - Die richtige Zufallsquelle in Code wählen
> - CSPRNG-Funktionen verschiedener Sprachen kennen
> - Typische Zufallsfehler vermeiden

---

## Inhalt

### Die Regel

Jeder sicherheitsrelevante Zufallswert (Schlüssel, Nonce, IV, Salt, Token) muss aus einem **CSPRNG** stammen (→ [[02-Sichere-Schluesselgenerierung]], [[06-Fehlerhafte-Zufallszahlengeneratoren]]). Normale PRNGs sind **vorhersagbar** und damit unsicher.

### Richtige Funktionen pro Sprache

| Sprache | **Sicher (CSPRNG)** | **Unsicher (nie für Krypto)** |
|---------|---------------------|-------------------------------|
| Python | `secrets`, `os.urandom` | `random` |
| Java | `SecureRandom` | `java.util.Random` |
| Go | `crypto/rand` | `math/rand` |
| JavaScript | `crypto.getRandomValues` / Node `crypto.randomBytes` | `Math.random()` |
| C | `getrandom()`, `/dev/urandom` | `rand()` |

> [!danger] **Der häufigste Fehler**
> `Math.random()`, `random`, `rand()` & Co. sind für Spiele/Simulationen gedacht, **nicht** für Kryptographie. Sie sind deterministisch vorhersagbar. Ein damit erzeugter „Schlüssel" oder „Token" ist faktisch wertlos.

### Richtige Nutzung

```python
import secrets
key   = secrets.token_bytes(32)   # 256-Bit-Schlüssel
token = secrets.token_urlsafe(32) # URL-sicheres Token
```

### Entropie beim Systemstart

> [!warning] **Embedded/Boot-Problem**
> Frisch gebootete oder embedded Systeme haben oft **zu wenig Entropie**. Schlüssel, die zu früh erzeugt werden, können schwach oder über viele Geräte identisch sein (→ [[06-Fehlerhafte-Zufallszahlengeneratoren]]). Moderne Syscalls wie `getrandom()` **blockieren**, bis genug Entropie vorhanden ist – das ist gewollt und sicher.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Alle Krypto-Zufallswerte aus einem CSPRNG beziehen
> - Sicher: `secrets`/`os.urandom`, `SecureRandom`, `crypto/rand`, `getRandomValues`
> - Unsicher: `random`/`Math.random()`/`rand()` – nie für Krypto
> - Entropie beim Boot sicherstellen (`getrandom()` blockiert bewusst)

---

## Übungen

1. Welche Zufallsfunktion nutzen Sie in Ihrer bevorzugten Sprache für einen Schlüssel?
2. Warum ist `Math.random()` für Tokens ungeeignet?
3. Welches Problem besteht bei der Schlüsselerzeugung direkt nach dem Boot?

---

← [[03-Crypto-Misuse-Patterns|← Zurück]] | [[00-SecDev-Index|Übersicht]] | [[05-Memory-Safety-und-Side-Channels|Weiter →]]
