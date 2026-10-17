---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - angriffe
---

# Padding-Oracle-Angriffe

> [!info] **Lernziele**
> - Das Prinzip des Padding-Oracle-Angriffs verstehen
> - Nachvollziehen, wie ein Informationsleck zum Klartext führt
> - Die Gegenmaßnahme (AEAD) einordnen

---

## Inhalt

### Das Oracle

Ein **Padding-Oracle-Angriff** nutzt aus, dass ein System verrät, ob ein entschlüsselter Chiffretext ein **gültiges Padding** hatte (→ [[08-Padding-Nonces-und-IVs]]). Dieses „Orakel" kann eine Fehlermeldung, ein HTTP-Status oder auch nur ein Zeitunterschied sein.

```
Angreifer → Server:  manipulierter Chiffretext
Server → Angreifer:  "Padding ungültig" oder "ok"  ← verrät 1 Bit Information
```

### Wie daraus Klartext wird

Bei CBC (→ [[05-Betriebsmodi-ECB-CBC-CTR-GCM]]) kann der Angreifer durch gezielte Manipulation des vorhergehenden Chiffretextblocks und Beobachtung der Padding-Antwort **Byte für Byte** den Klartext rekonstruieren – **ohne** den Schlüssel zu kennen. Mit relativ wenigen Anfragen pro Byte lässt sich so ein ganzer Block entschlüsseln.

### Reale Beispiele

> [!warning] **Prüfungsrelevant**
> - **Vaudenay (2002):** theoretische Grundlage des Padding-Oracle-Angriffs auf CBC.
> - **POODLE (2014):** Padding-Oracle gegen SSL 3.0.
> - **Lucky Thirteen (2013):** timing-basiertes Padding-Oracle in TLS-CBC.
> Diese Angriffe trafen reale TLS-Implementierungen.

### Gegenmaßnahmen

> [!tip] **AEAD statt „MAC danach prüfen"**
> Die wirksame Abwehr ist **Authenticated Encryption (AEAD)**: Der Chiffretext wird vor jeder Entschlüsselung über ein Authentisierungs-Tag geprüft (→ [[07-Authenticated-Encryption-AEAD]]). Ist das Tag ungültig, wird **sofort** abgelehnt – ohne Padding zu prüfen oder Informationen preiszugeben. Zusätzlich hilft **konstante-Zeit**-Verarbeitung gegen timing-basierte Varianten (→ [[04-Timing-Angriffe]]).

Kurz: CBC ohne Integritätsschutz vermeiden; AES-GCM oder ChaCha20-Poly1305 verwenden.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Padding-Oracle: ein verräterisches „gültig/ungültig"-Signal leakt Information
> - Erlaubt byteweise Klartext-Rekonstruktion bei CBC ohne Schlüsselkenntnis
> - Reale Fälle: Vaudenay, POODLE, Lucky Thirteen (TLS)
> - Abwehr: AEAD (Tag vor Entschlüsselung prüfen), konstante Zeit

---

## Übungen

1. Welches Informationsleck nutzt ein Padding-Oracle-Angriff?
2. Warum kann der Angreifer ohne Schlüssel den Klartext gewinnen?
3. Wie verhindert AEAD diesen Angriff?

---

← [[02-Known-Plaintext-und-Chosen-Plaintext-Angriffe|← Zurück]] | [[00-Angriffe-Index|Übersicht]] | [[04-Timing-Angriffe|Weiter →]]
