---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - angriffe
---

# Known-Plaintext und Chosen-Plaintext-Angriffe

> [!info] **Lernziele**
> - Known-Plaintext- und Chosen-Plaintext-Angriffe praktisch einordnen
> - Den Bezug zu den Angriffsmodellen herstellen
> - Gegenmaßnahmen moderner Chiffren verstehen

---

## Inhalt

### Rückbezug zu den Angriffsmodellen

Diese Angriffe wurden formal als Modelle in Modul 1 eingeführt (→ [[05-Kryptographische-Angriffsmodelle]]). Hier geht es um ihre **praktische** Ausnutzung.

### Known-Plaintext Attack (KPA)

Der Angreifer kennt **Klartext-Chiffretext-Paare** und versucht daraus Schlüssel oder weitere Klartexte zu gewinnen.

- **Praktisch:** Nachrichten enthalten oft vorhersehbare Teile – Dateiheader, Protokoll-Preamble, Standardfloskeln.
- **Historisch:** Die „Cribs" beim Enigma-Bruch (→ [[04-Enigma-und-historische-Verschluesselungsmaschinen]]).

### Chosen-Plaintext Attack (CPA)

Der Angreifer kann sich **selbst gewählte Klartexte verschlüsseln lassen** und die Chiffretexte beobachten.

- **Praktisch:** z. B. ein Webdienst, der Angreifer-Eingaben zusammen mit einem Geheimnis verschlüsselt.
- **Konsequenz:** Deterministische Verschlüsselung ist angreifbar (gleiche Eingabe → gleiche Ausgabe verrät Muster, vgl. ECB → [[05-Betriebsmodi-ECB-CBC-CTR-GCM]]).
- **BEAST/CRIME** (TLS) sind reale CPA-artige Angriffe, die vorhersagbare Teile und Kompression ausnutzten.

### Gegenmaßnahmen

> [!tip] **Probabilistische Verschlüsselung**
> Moderne Chiffren begegnen diesen Angriffen durch **Zufall bei jeder Verschlüsselung** (IV/Nonce), sodass gleiche Klartexte verschiedene Chiffretexte ergeben. Formal verlangt man **IND-CPA**-Sicherheit (und besser IND-CCA). AEAD-Verfahren (AES-GCM, ChaCha20-Poly1305) erfüllen das (→ [[07-Authenticated-Encryption-AEAD]]).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - KPA: Angreifer kennt Klartext-Chiffretext-Paare (oft durch vorhersehbare Nachrichtenteile)
> - CPA: Angreifer kann wählbare Klartexte verschlüsseln lassen (Orakel)
> - Deterministische Verschlüsselung ist CPA-anfällig (ECB, BEAST/CRIME)
> - Gegenmittel: probabilistische Verschlüsselung (IV/Nonce), IND-CPA/CCA, AEAD

---

## Übungen

1. Warum sind vorhersehbare Nachrichtenteile für KPA nützlich?
2. Wieso ist deterministische Verschlüsselung gegen CPA unsicher?
3. Wie erreichen moderne Chiffren IND-CPA-Sicherheit?

---

← [[01-Brute-Force-und-Dictionary-Angriffe|← Zurück]] | [[00-Angriffe-Index|Übersicht]] | [[03-Padding-Oracle-Angriffe|Weiter →]]
