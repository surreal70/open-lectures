---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - schutzziele
  - cia
  - sicherheit
---

# Schutzziele: Vertraulichkeit, Integrität, Authentizität und Nichtabstreitbarkeit

> [!info] **Lernziele**
> - Die vier klassischen Schutzziele erklären können
> - Kryptographische Verfahren den Schutzzielen zuordnen
> - Anwendungsfälle für jedes Schutzziel identifizieren

---

## Inhalt

### Vertraulichkeit (Confidentiality)

**Vertraulichkeit** bedeutet, dass Informationen nur für befugte Personen zugänglich sind. Unbefugte dürfen weder den Inhalt lesen noch rekonstruieren können.

- **Mittel:** Verschlüsselung (symmetrisch oder asymmetrisch).
- **Anwendungsfälle:** verschlüsselte E-Mails, HTTPS-Übertragung, Festplattenverschlüsselung.

Beispiel: Beim Online-Banking verhindert TLS, dass ein Angreifer im selben WLAN die übertragenen Kontodaten mitlesen kann.

### Integrität (Integrity)

**Integrität** stellt sicher, dass Daten nicht **unbemerkt verändert** wurden – weder durch Übertragungsfehler noch durch gezielte Manipulation.

- **Mittel:** kryptographische Hashfunktionen (Erkennung zufälliger Änderungen) und **MACs** (Erkennung gezielter Manipulation mit geheimem Schlüssel).
- **Anwendungsfälle:** Prüfsummen bei Downloads, Nachrichtenauthentisierung in Protokollen.

Wichtig: Eine reine Hashprüfsumme schützt nur gegen zufällige Fehler. Gegen einen aktiven Angreifer, der auch den Hashwert austauschen kann, braucht es einen schlüsselbasierten MAC.

### Authentizität (Authenticity)

**Authentizität** garantiert, dass die **Identität des Kommunikationspartners** bzw. der Datenursprung verifiziert ist – die Nachricht stammt wirklich von dem angegebenen Absender.

- **Mittel:** digitale Signaturen, MACs, Zertifikate.
- **Anwendungsfälle:** Server-Authentifizierung über TLS-Zertifikate, signierte Software-Updates.

### Nichtabstreitbarkeit (Non-Repudiation)

**Nichtabstreitbarkeit** verhindert, dass ein Absender nachträglich **abstreiten** kann, eine Nachricht gesendet oder eine Handlung vorgenommen zu haben.

- **Mittel:** digitale Signaturen mit dem **privaten** Schlüssel des Absenders, oft kombiniert mit Zeitstempeln.
- **Anwendungsfälle:** rechtsverbindliche elektronische Verträge, qualifizierte elektronische Signaturen.

Der Unterschied zur Authentizität: Ein MAC belegt Authentizität **nur gegenüber dem Partner**, der denselben geheimen Schlüssel kennt – dieser könnte die Nachricht selbst erzeugt haben. Eine digitale Signatur hingegen kann **jeder Dritte** mit dem öffentlichen Schlüssel prüfen, weshalb nur sie echte Nichtabstreitbarkeit liefert.

### Das CIA-Triad und Erweiterungen

Im Englischen fasst man die drei klassischen Kernziele der Informationssicherheit als **CIA-Triad** zusammen:

| Buchstabe | Ziel | Deutsch |
|-----------|------|---------|
| **C** | Confidentiality | Vertraulichkeit |
| **I** | Integrity | Integrität |
| **A** | Availability | **Verfügbarkeit** |

Beachte: Das „A" im CIA-Triad steht für **Verfügbarkeit** (Daten und Dienste sind bei Bedarf nutzbar) – ein Ziel, das primär durch Redundanz und Betrieb erreicht wird, nicht durch Kryptographie. Die oben behandelte **Authentizität** und **Nichtabstreitbarkeit** sind Erweiterungen, ebenso wie:

- **Zurechenbarkeit (Accountability):** Handlungen lassen sich eindeutig einem Akteur zuordnen.
- **Verbindlichkeit:** Kombination aus Authentizität und Nichtabstreitbarkeit im rechtlichen Kontext.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Vertraulichkeit: Nur Berechtigte können Daten lesen
> - Integrität: Daten wurden nicht unbemerkt verändert
> - Authentizität: Die Identität des Absenders ist verifiziert
> - Nichtabstreitbarkeit: Der Absender kann die Nachricht nicht leugnen

---

## Übungen

1. Ordnen Sie folgende Verfahren den Schutzzielen zu: AES, SHA-256, RSA-Signatur, HMAC
2. Welche Schutzziele sind bei einer HTTPS-Verbindung erfüllt?

---

← [[02-Grundbegriffe-und-Terminologie|← Zurück]] | [[00-Einfuehrung-Index|Übersicht]] | [[04-Verschluesselung-Hashing-Kodierung-Signierung|Weiter →]]
