---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - architektur
  - vertiefung
---

# Crypto Agility Design Patterns

> [!info] **Lernziele**
> - Konkrete Entwurfsmuster für Crypto-Agility kennen
> - Algorithmus-Kennzeichnung und Abstraktion anwenden
> - Versionierung von Chiffretexten verstehen

---

## Inhalt

### Von der Idee zum Muster

Crypto-Agility (→ [[07-Crypto-Agility]]) wird durch konkrete **Design-Patterns** umgesetzt, die den Austausch von Verfahren ermöglichen, ohne die Architektur neu zu bauen.

### 1. Abstraktionsschicht

Anwendungen rufen **nicht** direkt AES oder RSA auf, sondern einen **Krypto-Service / eine Fassade** mit generischer Schnittstelle:

```
app.encrypt(data)  →  CryptoService  →  (aktuell) AES-256-GCM
```

Das Verfahren wird zentral konfiguriert und kann ausgetauscht werden, ohne den Anwendungscode zu ändern.

### 2. Algorithmus-Kennzeichnung (Cryptographic Agility Header)

> [!tip] **Jeder Chiffretext trägt seine Verfahrens-ID**
> Ein verschlüsseltes Objekt wird mit einem **Metadaten-Präfix** versehen, das Algorithmus und Version angibt:
> ```
> { "v": 2, "alg": "AES-256-GCM", "kid": "key-2026", "nonce": ..., "ct": ... }
> ```
> So kann das System alte Daten weiter entschlüsseln (mit dem alten Verfahren) und neue mit dem aktuellen schreiben – entscheidend für reibungslose Migration.

### 3. Mehrere Verfahren parallel

Während einer Migration werden alt und neu **gleichzeitig** unterstützt: neu schreiben im neuen Verfahren, lesen in beiden. Das ist auch die Grundlage **hybrider** PQC-Verfahren (→ [[09-Hybride-kryptographische-Verfahren]]).

### 4. Zentrale Policy und Key-IDs

- **Key-IDs** verweisen auf den konkreten Schlüssel (ermöglicht Rotation, → [[05-Key-Rotation-und-Key-Revocation]]).
- Eine **zentrale Policy** legt fest, welche Verfahren aktuell erlaubt sind.

### Antipattern

> [!danger] **Vermeiden**
> Hartcodierte Algorithmen und Chiffretexte **ohne** Verfahrens-/Versionskennung. Dann weiß das System bei einem Wechsel nicht mehr, wie alte Daten zu entschlüsseln sind – Migration wird zum Albtraum.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Abstraktionsschicht entkoppelt Anwendung vom konkreten Verfahren
> - Chiffretexte tragen Algorithmus-/Versions-ID und Key-ID → alte Daten bleiben lesbar
> - Alt und neu während der Migration parallel unterstützen (Basis auch für hybride PQC)
> - Antipattern: hartcodierte Verfahren, Chiffretexte ohne Versionskennung

---

## Übungen

1. Wie entkoppelt eine Abstraktionsschicht die Anwendung vom Verfahren?
2. Warum sollte jeder Chiffretext eine Algorithmus-/Versions-ID tragen?
3. Welches Antipattern erschwert eine spätere Migration besonders?

---

← [[02-Architekturentscheidungen-Kryptographie|← Zurück]] | [[00-Architektur-Index|Übersicht]] | [[04-Kryptographie-Migration-Strategien|Weiter →]]
