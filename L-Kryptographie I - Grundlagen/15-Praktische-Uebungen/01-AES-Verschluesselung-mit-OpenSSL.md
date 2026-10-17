---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - praxis
---

# AES-Verschlüsselung mit OpenSSL

> [!info] **Lernziele**
> - Dateien mit AES über OpenSSL ver- und entschlüsseln
> - Den Unterschied zwischen passwort- und schlüsselbasierter Nutzung verstehen
> - Die Bedeutung von Modus und Authentisierung praktisch nachvollziehen

---

## Inhalt

### Vorbereitung

Diese Übung benötigt **OpenSSL** (auf Linux/macOS meist vorinstalliert; `openssl version` prüft die Version). Lege eine Testdatei an:

```bash
echo "Geheime Nachricht" > geheim.txt
```

### Passwortbasierte Verschlüsselung (AES-256)

```bash
# Verschlüsseln (mit Schlüsselableitung aus Passwort, PBKDF2)
openssl enc -aes-256-cbc -pbkdf2 -salt -in geheim.txt -out geheim.enc

# Entschlüsseln
openssl enc -d -aes-256-cbc -pbkdf2 -in geheim.enc -out entschluesselt.txt
```

> [!warning] **`-pbkdf2` und `-salt` nicht vergessen**
> Ohne `-pbkdf2` nutzt OpenSSL eine veraltete, schwache Schlüsselableitung. Ein zufälliger `-salt` (Standard) verhindert Rainbow-Table-Angriffe (→ [[07-Salt-Pepper-und-Key-Stretching]]).

### Schlüssel- und IV-basierte Verschlüsselung

```bash
# Zufälligen 256-Bit-Schlüssel und IV erzeugen
key=$(openssl rand -hex 32)
iv=$(openssl rand -hex 16)

openssl enc -aes-256-cbc -K $key -iv $iv -in geheim.txt -out geheim.bin
openssl enc -d -aes-256-cbc -K $key -iv $iv -in geheim.bin -out klar.txt
```

### Beobachtung: ECB ist unsicher

> [!danger] **Selbst ausprobieren**
> Verschlüssle eine Datei mit vielen gleichen Blöcken einmal mit `-aes-256-ecb` und einmal mit `-aes-256-cbc`. Im ECB-Ergebnis bleiben Muster erkennbar – genau die Schwäche aus [[05-Betriebsmodi-ECB-CBC-CTR-GCM]].

> [!note] **Hinweis zu AEAD**
> Das OpenSSL-`enc`-Kommando bietet **keine** authenticated encryption im Alltag. Für echten Integritätsschutz nutzt man AES-GCM über die OpenSSL-Bibliothek/`openssl` mit entsprechenden Optionen oder Tools wie `age` – siehe [[07-Authenticated-Encryption-AEAD]].

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - `openssl enc -aes-256-cbc -pbkdf2 -salt` ver-/entschlüsselt Dateien passwortbasiert
> - Alternativ mit explizitem Schlüssel/IV (`-K`/`-iv`) aus `openssl rand`
> - `-pbkdf2` und Salt sind für die Sicherheit essenziell
> - ECB zeigt Muster; für Integrität braucht es AEAD (GCM)

---

## Übungen

1. Verschlüsseln und entschlüsseln Sie eine Datei passwortbasiert mit AES-256-CBC.
2. Erzeugen Sie Schlüssel und IV mit `openssl rand` und nutzen Sie sie explizit.
3. Vergleichen Sie die Ausgabe von ECB und CBC bei einer Datei mit wiederholten Daten.

---

← [[00-Uebungen-Index|Übersicht]] | [[02-RSA-und-ECC-Schluessel-generieren|Weiter →]]
