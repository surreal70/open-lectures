---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - protokolle
---

# Replay und Man-in-the-Middle-Angriffe

> [!info] **Lernziele**
> - Replay- und Man-in-the-Middle-Angriffe verstehen
> - Die jeweiligen Gegenmaßnahmen kennen
> - Erkennen, wie Protokolle diese Angriffe abwehren

---

## Inhalt

### Man-in-the-Middle (MitM)

Bei einem **Man-in-the-Middle-Angriff** schaltet sich ein Angreifer unbemerkt zwischen zwei Parteien, fängt die Kommunikation ab und gibt sich jeder Seite gegenüber als die jeweils andere aus.

```
Alice  ⇄  [Angreifer]  ⇄  Bob
   (glaubt, mit Bob zu reden)   (glaubt, mit Alice zu reden)
```

Besonders gefährdet ist ein **unauthentifizierter** Schlüsselaustausch: Reines Diffie-Hellman handelt mit dem Angreifer jeweils ein eigenes Geheimnis aus (→ [[03-Diffie-Hellman-Schlüsselaustausch]]).

**Gegenmaßnahme:** **Authentifizierung** des Schlüsselaustauschs (→ [[07-Schluesselvereinbarung-und-Authentifizierung]]) – per Zertifikat/PKI, Public-Key oder PSK. So wird der ausgehandelte Schlüssel an eine geprüfte Identität gebunden und der Angreifer entlarvt.

### Replay-Angriff

Bei einem **Replay-Angriff** zeichnet der Angreifer gültige (verschlüsselte) Nachrichten auf und sendet sie **später erneut**, um eine Aktion zu wiederholen – etwa eine Überweisung oder einen Login.

Beispiel: Ein aufgezeichnetes „Tür öffnen"-Kommando wird später nochmal abgespielt.

**Gegenmaßnahmen:**

| Mittel | Wirkung |
|--------|---------|
| **Nonce / Zufallswert** | jede Nachricht ist einmalig |
| **Zeitstempel** | veraltete Nachrichten werden abgelehnt |
| **Sequenznummern** | Reihenfolge erzwingen, Wiederholungen erkennen |
| **Session-Token** | an eine konkrete Sitzung gebunden |

> [!warning] **Prüfungsrelevant**
> - **MitM** wird durch **Authentifizierung** abgewehrt (nicht durch Verschlüsselung allein).
> - **Replay** wird durch **Frische-Nachweise** (Nonce, Zeitstempel, Sequenznummern) abgewehrt.
> Beides sind unterschiedliche Angriffe mit unterschiedlichen Gegenmaßnahmen.

### Schutz in realen Protokollen

- **TLS** verhindert MitM durch Zertifikatsvalidierung und Replay durch Sequenznummern/Handshake-Transcript; TLS-1.3-0-RTT-Daten haben hierbei einen dokumentierten Replay-Vorbehalt.
- **SSH** nutzt TOFU-Hostschlüssel gegen MitM.
- **WireGuard** verwendet Zähler/Zeitfenster gegen Replay.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - MitM: Angreifer schaltet sich dazwischen → Abwehr durch Authentifizierung
> - Replay: Wiedereinspielen gültiger Nachrichten → Abwehr durch Nonce/Zeitstempel/Sequenznummern
> - Verschlüsselung allein schützt gegen keinen der beiden Angriffe vollständig
> - TLS, SSH und WireGuard integrieren passende Gegenmaßnahmen

---

## Übungen

1. Wodurch wird ein Man-in-the-Middle-Angriff verhindert?
2. Nennen Sie drei Gegenmaßnahmen gegen Replay-Angriffe.
3. Warum schützt Verschlüsselung allein nicht vor Replay?

---

← [[07-Schluesselvereinbarung-und-Authentifizierung|← Zurück]] | [[00-Protokolle-Index|Übersicht]] | [[00-Schluessel-Index|Nächstes Modul →]]
