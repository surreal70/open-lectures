---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - angriffe
---

# Sicherheitsanalyse realer Vorfälle

> [!info] **Lernziele**
> - Reale kryptographische Vorfälle systematisch einordnen
> - Wiederkehrende Fehlerursachen erkennen
> - Lehren für die eigene Praxis ableiten

---

## Inhalt

### Warum Vorfälle analysieren?

Aus realen Brüchen lernt man mehr als aus der Theorie: Sie zeigen, **wo** Systeme tatsächlich scheitern – fast immer an der Implementierung oder am Betrieb, nicht an der Mathematik.

### Übersicht wichtiger Vorfälle

| Vorfall | Jahr | Ursache | Lehre |
|---------|------|---------|-------|
| **DES-Bruch (Deep Crack)** | 1998 | zu kurzer Schlüssel (56 Bit) | ausreichende Schlüssellänge (→ [[03-DES-und-Triple-DES]]) |
| **Debian-OpenSSL** | 2008 | kaputter RNG | guter Zufall (→ [[06-Fehlerhafte-Zufallszahlengeneratoren]]) |
| **Flame (MD5)** | 2012 | MD5-Kollision → gefälschtes Zertifikat | gebrochene Hashes meiden (→ [[04-Kollisionsresistenz-und-Preimage-Resistenz]]) |
| **Heartbleed** | 2014 | OpenSSL-Bufferfehler | Memory Safety, Audits (→ [[06-Kerckhoffs-Prinzip]]) |
| **POODLE** | 2014 | SSL-3.0-Downgrade + Padding-Oracle | Altlasten abschalten (→ [[08-Downgrade-Angriffe]]) |
| **DROWN/FREAK/Logjam** | 2015 | schwache/Export-Cipher | keine veralteten Suiten |
| **SHAttered** | 2017 | SHA-1-Kollision | moderne Hashes (→ [[02-SHA-2-und-SHA-3]]) |
| **KRACK** | 2017 | Nonce-Reuse im WPA2-Handshake | Nonce-Eindeutigkeit (→ [[07-Nonce-Reuse-und-Schluesselwiederverwendung]]) |

### Wiederkehrende Muster

> [!warning] **Prüfungsrelevant: die immer gleichen Ursachen**
> 1. **Veraltete Verfahren** zu lange im Einsatz (DES, MD5, SHA-1, SSL 3.0).
> 2. **Schwacher/fehlerhafter Zufall** (Debian, PS3).
> 3. **Implementierungsfehler** (Heartbleed, Padding-Oracles).
> 4. **Falsche Nutzung** korrekter Primitive (Nonce-Reuse, fehlende Authentisierung).
>
> Die Mathematik hielt in all diesen Fällen – gebrochen wurde drumherum.

### Lehren für die Praxis

- Moderne, geprüfte Verfahren und **Crypto-Agility** (schnell wechseln können, → Modul 14).
- Gute Zufallsquellen, AEAD, konstante-Zeit-Code.
- Geprüfte Bibliotheken statt Eigenbau; regelmäßige Audits und Updates.
- Aus Vorfällen anderer lernen (CVE-Datenbanken, Post-Mortems).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Reale Brüche entstehen fast immer durch Implementierung/Betrieb, nicht durch Mathematik
> - Wiederkehrende Ursachen: Altlasten, schwacher Zufall, Bugs, Fehlnutzung
> - Beispiele: DES, Debian-OpenSSL, Flame, Heartbleed, POODLE, SHAttered, KRACK
> - Lehren: moderne Verfahren, Crypto-Agility, geprüfte Libraries, Audits

---

## Übungen

1. Nennen Sie drei reale Vorfälle und ihre jeweilige Ursache.
2. Welche vier wiederkehrenden Fehlermuster lassen sich erkennen?
3. Welche praktischen Lehren ziehen Sie daraus für ein eigenes Projekt?

---

← [[09-Kryptographische-Implementierungsfehler|← Zurück]] | [[00-Angriffe-Index|Übersicht]] | [[00-PQC-Index|Nächstes Modul →]]
