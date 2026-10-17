---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - angriffe
---

# Kryptographische Implementierungsfehler

> [!info] **Lernziele**
> - Verstehen, dass die meisten Krypto-Brüche Implementierungsfehler sind
> - Typische Fehlerklassen erkennen
> - Grundregeln sicherer Implementierung kennen

---

## Inhalt

### Die wichtigste Erkenntnis

> [!warning] **Prüfungsrelevant: Die Mathematik ist selten das Problem**
> Moderne Algorithmen (AES, RSA, ECC) sind praktisch nie der Schwachpunkt. In der Realität brechen Systeme fast immer an **Implementierungs- und Anwendungsfehlern**: falsche Modi, Nonce-Fehler, schwacher Zufall, ignorierte Zertifikatsprüfung, Seitenkanäle.

### Typische Fehlerklassen (Querschnitt des Moduls)

| Fehler | Verweis |
|--------|---------|
| Unsicherer Modus (ECB, CBC ohne MAC) | [[05-Betriebsmodi-ECB-CBC-CTR-GCM]] |
| Nonce-/IV-Wiederverwendung | [[07-Nonce-Reuse-und-Schluesselwiederverwendung]] |
| Schwacher Zufall | [[06-Fehlerhafte-Zufallszahlengeneratoren]] |
| Nicht-konstante-Zeit-Vergleiche | [[04-Timing-Angriffe]] |
| Fehlende/ignorierte Zertifikatsprüfung | [[02-HTTPS-und-Zertifikatsvalidierung]] |
| Veraltete Algorithmen (MD5/SHA-1, DES) | [[02-SHA-2-und-SHA-3]] |
| Textbook-RSA ohne OAEP/PSS | [[02-RSA-Funktionsweise-und-Sicherheit]] |
| „Encrypt, aber nicht authentifizieren" | [[07-Authenticated-Encryption-AEAD]] |

### Die goldene Regel

> [!danger] **„Don't roll your own crypto"**
> Eigene kryptographische Implementierungen sind extrem fehleranfällig. Verwende **etablierte, geprüfte Bibliotheken** (libsodium, OpenSSL, die Krypto-APIs der Plattform) und deren **High-Level-Funktionen**, die sichere Voreinstellungen treffen. Low-Level-Bausteine selbst zu kombinieren ist eine häufige Fehlerquelle.

### Prinzipien sicherer Implementierung

- **Misuse-resistente APIs** bevorzugen (schwer falsch zu benutzen, → Modul 19).
- **Sichere Defaults:** AEAD, moderne Kurven, aktuelle TLS-Version.
- **Keine Geheimnisse in Logs/Fehlermeldungen** (verhindert Oracles).
- **Reviews und Audits** durch Fachleute; keine selbstgebaute Krypto in Produktion.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Die große Mehrheit realer Krypto-Brüche sind Implementierungsfehler, nicht Mathematik
> - Typisch: falscher Modus, Nonce-/Zufallsfehler, Timing, ignorierte Zertifikatsprüfung, Altalgorithmen
> - Goldene Regel: keine eigene Krypto – geprüfte Bibliotheken und High-Level-APIs nutzen
> - Sichere Defaults, misuse-resistente APIs, Reviews/Audits

---

## Übungen

1. Warum ist die Aussage „der Algorithmus ist sicher" für ein System nicht ausreichend?
2. Nennen Sie vier typische kryptographische Implementierungsfehler.
3. Was bedeutet „Don't roll your own crypto" und warum gilt es?

---

← [[08-Downgrade-Angriffe|← Zurück]] | [[00-Angriffe-Index|Übersicht]] | [[10-Sicherheitsanalyse-realer-Vorfaelle|Weiter →]]
