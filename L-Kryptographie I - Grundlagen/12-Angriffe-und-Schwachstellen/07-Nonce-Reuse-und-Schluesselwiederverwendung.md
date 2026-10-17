---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - angriffe
---

# Nonce-Reuse und Schlüsselwiederverwendung

> [!info] **Lernziele**
> - Die Folgen von Nonce-Wiederverwendung verstehen
> - Risiken der Schlüsselwiederverwendung einordnen
> - Reale Vorfälle und Gegenmaßnahmen kennen

---

## Inhalt

### Nonce-Wiederverwendung

Eine **Nonce** (number used once) darf pro Schlüssel nur **einmal** verwendet werden (→ [[08-Padding-Nonces-und-IVs]]). Bei Wiederholung brechen verschiedene Verfahren auf unterschiedliche Weise:

**Stromchiffren / CTR:** Gleicher Schlüsselstrom für zwei Nachrichten:

$$c_1 \oplus c_2 = m_1 \oplus m_2$$

Der Schlüssel fällt heraus; der Angreifer gewinnt Information über die Klartexte.

> [!danger] **GCM: Nonce-Reuse ist katastrophal**
> Bei AES-GCM führt eine wiederholte Nonce nicht nur zum Klartextleck, sondern erlaubt die **Berechnung des Authentisierungsschlüssels** – der Angreifer kann danach **beliebige Nachrichten fälschen**. Nonce-Eindeutigkeit ist hier absolut kritisch.

### Schlüsselwiederverwendung

Denselben Schlüssel für **unterschiedliche Zwecke** oder über zu lange Zeit zu verwenden, erhöht das Risiko:

- **Zweck-Vermischung:** derselbe Schlüssel für Verschlüsselung und Signatur/MAC kann Interaktionen zwischen den Verfahren ermöglichen → Schlüsseltrennung (→ [[01-Lebenszyklus-kryptographischer-Schluessel]]).
- **Zu große Datenmengen** pro Schlüssel: Geburtstagsgrenzen (z. B. bei 64-Bit-Block-Chiffren → Sweet32).

### Reale Vorfälle

> [!warning] **Prüfungsrelevant**
> - **WEP (WLAN):** zu kurzer IV, der sich wiederholte → vollständig gebrochen.
> - **KRACK (2017):** erzwang im WPA2-Handshake die **Wiederverwendung einer Nonce** und brach so die Verschlüsselung.
> - **Nonce-Reuse in diversen GCM-Implementierungen.**

### Gegenmaßnahmen

- Nonces **zählerbasiert** oder ausreichend zufällig und eindeutig verwalten.
- **Nonce-missbrauchsresistente** Verfahren erwägen (z. B. AES-GCM-SIV).
- Schlüssel regelmäßig **rotieren** und Zweck trennen (→ [[05-Key-Rotation-und-Key-Revocation]]).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Nonce-Reuse bei Stromchiffren/CTR leakt $m_1 \oplus m_2$
> - Bei GCM ermöglicht Nonce-Reuse Fälschungen (Authentisierungsschlüssel kompromittiert)
> - Schlüsselwiederverwendung: Zweck-Vermischung und Geburtstagsgrenzen beachten
> - Reale Fälle: WEP, KRACK; Abwehr: eindeutige Nonces, GCM-SIV, Rotation/Trennung

---

## Übungen

1. Was verrät die Wiederverwendung eines Schlüsselstroms?
2. Warum ist Nonce-Reuse bei GCM besonders gefährlich?
3. Was war die Kernidee des KRACK-Angriffs?

---

← [[06-Fehlerhafte-Zufallszahlengeneratoren|← Zurück]] | [[00-Angriffe-Index|Übersicht]] | [[08-Downgrade-Angriffe|Weiter →]]
