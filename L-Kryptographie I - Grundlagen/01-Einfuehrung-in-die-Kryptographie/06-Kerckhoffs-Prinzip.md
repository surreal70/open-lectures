---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - kerckhoffs
  - security-by-design
  - open-source
---

# Kerckhoffs' Prinzip und moderne Sicherheitskonzepte

> [!info] **Lernziele**
> - Kerckhoffs' Prinzip erklären und anwenden können
> - Security through Obscurity kritisch bewerten
> - Moderne Sicherheitskonzepte verstehen

---

## Inhalt

### Kerckhoffs' Prinzip (1883)

Der niederländische Linguist und Kryptograph **Auguste Kerckhoffs** formulierte 1883 in seinem Aufsatz *La Cryptographie militaire* mehrere Grundsätze für militärische Verschlüsselungssysteme. Der bekannteste davon gilt bis heute als Fundament der modernen Kryptographie:

> [!quote] Kerckhoffs' Prinzip
> Ein Kryptosystem muss auch dann sicher sein, wenn dem Angreifer **alles über das System außer dem Schlüssel** bekannt ist.

Anders formuliert: Die Sicherheit eines Verfahrens darf **ausschließlich von der Geheimhaltung des Schlüssels** abhängen, niemals von der Geheimhaltung des Algorithmus. Der US-amerikanische Mathematiker **Claude Shannon** griff diesen Gedanken 1949 auf und verschärfte ihn zur sogenannten **Shannon-Maxime**: „The enemy knows the system" – man sollte immer annehmen, dass der Gegner das verwendete System vollständig kennt.

**Warum ist das sinnvoll?**

| Aspekt | Begründung |
|--------|------------|
| Schlüssel austauschbar | Ein kompromittierter Schlüssel lässt sich leicht ersetzen – ein kompromittierter Algorithmus nicht. |
| Analysierbarkeit | Ein offener Algorithmus kann von Experten weltweit auf Schwächen geprüft werden. |
| Realistische Annahme | Algorithmen gelangen durch Reverse Engineering, Spionage oder Verrat ohnehin an die Öffentlichkeit. |
| Trennung der Geheimnisse | Nur eine kleine, gut schützbare Information (der Schlüssel) muss geheim bleiben. |

### Security through Obscurity

Der Gegenentwurf zu Kerckhoffs' Prinzip ist **Security through Obscurity** (Sicherheit durch Verschleierung): Die Sicherheit beruht darauf, dass die Funktionsweise des Systems geheim gehalten wird.

Das ist aus mehreren Gründen problematisch:

- **Geheimnisse halten nicht.** Sobald der Algorithmus durch Disassemblierung, Leaks oder Insider bekannt wird, ist die gesamte Sicherheit verloren – oft ohne dass die Betreiber es merken.
- **Keine unabhängige Prüfung.** Verborgene Verfahren werden nicht von der Fachöffentlichkeit analysiert, sodass Schwächen lange unentdeckt bleiben.
- **Falsches Sicherheitsgefühl.** Verschleierung wird leicht mit echter Sicherheit verwechselt.

> [!example] Gebrochene proprietäre Verfahren
> - **A5/1** (GSM-Mobilfunk): geheim gehaltener Stromchiffre-Algorithmus, nach Bekanntwerden schnell gebrochen.
> - **CSS** (DVD-Kopierschutz): proprietär, durch einen 16-Bit-Schlüsselraum und Reverse Engineering trivial zu brechen (DeCSS).
> - **MIFARE Classic / Crypto-1** (RFID-Karten): geheime Chiffre, nach Offenlegung praktisch unsicher.
> - **RC4-ähnliche Eigenentwicklungen** in diversen Produkten.

Wichtig ist die Abgrenzung: Verschleierung als **zusätzliche** Schicht (z. B. das Verstecken von Diensten, Obfuskation) kann ein Angriff erschweren, darf aber nie die **einzige** oder **tragende** Sicherheitsmaßnahme sein.

### Open-Source-Kryptographie

Aus Kerckhoffs' Prinzip folgt direkt die Stärke offener, öffentlich dokumentierter Verfahren:

- **Peer Review:** Algorithmen wie AES, RSA oder SHA-2 wurden über Jahre von der weltweiten Forschungsgemeinschaft analysiert. Der **AES-Wettbewerb** des NIST (1997–2001) wählte Rijndael erst nach offener, internationaler Begutachtung aus.
- **Transparenz:** Jeder kann die Implementierung prüfen – etwa bei Bibliotheken wie OpenSSL oder libsodium.
- **Vertrauen durch Nachvollziehbarkeit:** Vertrauen entsteht nicht durch Geheimhaltung, sondern durch belegbare Analyse.

> [!danger] Offener Quellcode ≠ automatisch sicher
> Open Source ermöglicht Prüfung, garantiert sie aber nicht. Der Fall **Heartbleed** (OpenSSL, 2014) zeigte, dass auch weit verbreiteter, offener Code schwerwiegende Fehler über Jahre enthalten kann, wenn niemand ihn gründlich prüft. Offenheit ist eine **Voraussetzung** für Vertrauen, kein Ersatz für sorgfältige Reviews und Audits.

### Moderne Sicherheitskonzepte

Kerckhoffs' Grundgedanke – Sicherheit auf überprüfbaren Annahmen statt auf Geheimhaltung aufzubauen – findet sich in heutigen Architekturprinzipien wieder:

- **Defense in Depth:** Mehrere unabhängige Schutzschichten, sodass der Ausfall einer Schicht das Gesamtsystem nicht kompromittiert.
- **Zero Trust:** Kein implizites Vertrauen aufgrund von Netzwerkposition; jede Anfrage wird authentifiziert und autorisiert („never trust, always verify").
- **Crypto Agility:** Systeme werden so entworfen, dass Algorithmen und Schlüssellängen austauschbar sind – wichtig etwa für den Übergang zur Post-Quanten-Kryptographie.
- **Kerckhoffs im Design:** Protokolle wie TLS werden offen standardisiert (IETF-RFCs) und öffentlich begutachtet, bevor sie breit eingesetzt werden.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Die Sicherheit darf nur vom Schlüssel abhängen
> - Öffentlich bekannte Algorithmen sind besser analysiert
> - Proprietäre Geheimverfahren sind ein Warnsignal

---

## Übungen

1. Finden Sie Beispiele für gebrochene proprietäre Algorithmen
2. Diskutieren Sie: Ist Open-Source-Kryptographie immer sicherer?

---

## Weiterführende Literatur

- Kerckhoffs, Auguste: *La Cryptographie militaire*, Journal des sciences militaires, 1883
- Shannon, Claude E.: *Communication Theory of Secrecy Systems*, Bell System Technical Journal, 1949
- Ferguson, Niels; Schneier, Bruce; Kohno, Tadayoshi: *Cryptography Engineering*, 2010

---

← [[05-Kryptographische-Angriffsmodelle|← Zurück]] | [[00-Einfuehrung-Index|Übersicht]] | [[00-Mathematik-Index|Nächstes Modul →]]
