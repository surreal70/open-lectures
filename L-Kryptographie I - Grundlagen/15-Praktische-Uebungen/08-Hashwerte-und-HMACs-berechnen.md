---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - praxis
---

# Hashwerte und HMACs berechnen

> [!info] **Lernziele**
> - Hashwerte verschiedener Verfahren berechnen
> - HMACs mit Schlüssel erzeugen
> - Den Lawineneffekt praktisch beobachten

---

## Inhalt

### Hashwerte berechnen

```bash
echo -n "Hallo Welt" > text.txt

# Verschiedene Hashfunktionen
sha256sum text.txt
sha512sum text.txt
openssl dgst -sha3-256 text.txt
b2sum text.txt            # BLAKE2 (falls verfügbar)
```

> [!danger] **Nur noch sichere Hashes**
> `md5sum` und `sha1sum` existieren noch, dürfen aber für Sicherheitszwecke nicht verwendet werden (→ [[04-Kollisionsresistenz-und-Preimage-Resistenz]]).

### Lawineneffekt beobachten

> [!tip] **Selbst ausprobieren**
> Ändere ein einziges Zeichen und vergleiche die Hashes:
> ```bash
> echo -n "Hallo Welt"  | sha256sum
> echo -n "Hallo welt"  | sha256sum   # kleines w
> ```
> Die beiden Hashes unterscheiden sich in etwa der Hälfte aller Bits – der **Lawineneffekt** (→ [[01-Eigenschaften-kryptographischer-Hashfunktionen]]).

### Integrität prüfen

```bash
# Prüfsummen-Datei erstellen und später verifizieren
sha256sum *.txt > SHA256SUMS
sha256sum -c SHA256SUMS
```

### HMAC berechnen

```bash
# HMAC-SHA-256 mit geheimem Schlüssel
openssl dgst -sha256 -hmac "mein_geheimer_schluessel" text.txt
```

Der **HMAC** sichert zusätzlich **Authentizität**: Ohne den geheimen Schlüssel lässt sich kein gültiger HMAC erzeugen (→ [[05-Message-Authentication-Codes-MAC-HMAC]]). Ein reiner Hash schützt nur gegen zufällige Änderungen, nicht gegen einen aktiven Angreifer.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - `sha256sum`, `sha512sum`, `openssl dgst -sha3-256`, `b2sum` berechnen Hashes
> - MD5/SHA-1 nicht für Sicherheit verwenden
> - Lawineneffekt: eine kleine Änderung ändert ~die Hälfte der Hash-Bits
> - `openssl dgst -hmac` erzeugt einen schlüsselbasierten HMAC (Integrität + Authentizität)

---

## Übungen

1. Berechnen Sie SHA-256, SHA-512 und SHA3-256 derselben Datei.
2. Demonstrieren Sie den Lawineneffekt mit einer minimalen Änderung.
3. Erzeugen Sie einen HMAC-SHA-256 und erklären Sie den Unterschied zum reinen Hash.

---

← [[07-Dateien-mit-GPG-verschluesseln|← Zurück]] | [[00-Uebungen-Index|Übersicht]] | [[09-Fehlkonfigurationen-identifizieren|Weiter →]]
