---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - angriffe
---

# Downgrade-Angriffe

> [!info] **Lernziele**
> - Das Prinzip von Downgrade-Angriffen verstehen
> - Reale Beispiele einordnen
> - Gegenmaßnahmen kennen

---

## Inhalt

### Die Idee

Ein **Downgrade-Angriff** zwingt zwei Parteien, ein **schwächeres** (veraltetes, brechbares) Verfahren oder eine ältere Protokollversion zu verwenden, obwohl beide eigentlich etwas Sichereres unterstützen. Der Angreifer manipuliert dazu die **Aushandlungsphase**.

```
Client: "Ich kann TLS 1.3, 1.2, ... 1.0"
Angreifer entfernt/verfälscht die Liste
Server sieht nur: "Client kann nur TLS 1.0"  → schwache Verbindung
```

### Warum das funktioniert

Protokolle, die aus Kompatibilitätsgründen **viele** Versionen/Cipher-Suites unterstützen und unauthentifiziert aushandeln, bieten Angriffsfläche. Je mehr veraltete Optionen erlaubt sind, desto größer das Risiko.

### Reale Beispiele

> [!warning] **Prüfungsrelevant**
> - **POODLE (2014):** erzwang Rückfall auf das unsichere SSL 3.0.
> - **FREAK / Logjam (2015):** erzwangen schwache „Export"-Cipher (absichtlich geschwächte Verfahren aus den 1990ern).
> - **Version-Rollback** allgemein in SSL/TLS vor den Gegenmaßnahmen.

### Gegenmaßnahmen

> [!tip] **Schutz gegen Downgrades**
> - **Veraltete Versionen/Cipher deaktivieren** (kein SSL 3.0, TLS 1.0/1.1, keine Export-Suites).
> - **Handshake-Integrität:** TLS 1.3 signiert/hasht den gesamten Handshake, sodass Manipulationen an der Aushandlung erkannt werden.
> - **Downgrade-Sentinel:** TLS 1.3 markiert in Server-Random-Werten, wenn ein Downgrade stattfand.
> - **Feste Verfahren** ohne Verhandlung (vgl. WireGuard → [[05-WireGuard]]) vermeiden das Problem ganz.

Downgrade-Angriffe sind eng mit Man-in-the-Middle verwandt (→ [[08-Replay-und-Man-in-the-Middle-Angriffe]]).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Downgrade-Angriffe erzwingen schwächere Verfahren durch Manipulation der Aushandlung
> - Risiko steigt mit der Zahl erlaubter veralteter Optionen
> - Reale Fälle: POODLE (SSL 3.0), FREAK/Logjam (Export-Cipher)
> - Abwehr: Altlasten abschalten, Handshake-Integrität (TLS 1.3), feste Verfahren

---

## Übungen

1. Wie funktioniert ein Downgrade-Angriff grundsätzlich?
2. Nennen Sie zwei reale Downgrade-Angriffe.
3. Wie schützt TLS 1.3 gegen Downgrades?

---

← [[07-Nonce-Reuse-und-Schluesselwiederverwendung|← Zurück]] | [[00-Angriffe-Index|Übersicht]] | [[09-Kryptographische-Implementierungsfehler|Weiter →]]
