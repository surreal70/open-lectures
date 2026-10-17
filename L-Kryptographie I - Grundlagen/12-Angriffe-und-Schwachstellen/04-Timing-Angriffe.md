---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - angriffe
---

# Timing-Angriffe

> [!info] **Lernziele**
> - Timing-Angriffe als Seitenkanal verstehen
> - Typische verwundbare Operationen erkennen
> - Konstante-Zeit-Implementierung als Gegenmaßnahme kennen

---

## Inhalt

### Die Idee

Ein **Timing-Angriff** gewinnt geheime Informationen aus der **Ausführungszeit** kryptographischer Operationen. Wenn die Laufzeit vom geheimen Wert abhängt, verrät sie etwas über ihn – selbst wenn der Algorithmus mathematisch sicher ist.

### Klassisches Beispiel: Vergleich

Ein **naiver** String-Vergleich bricht beim ersten abweichenden Byte ab:

```
if (mac == erwarteter_mac)   // bricht früh ab → Laufzeit verrät, wie viele Bytes stimmten
```

Ein Angreifer misst die Antwortzeit und rekonstruiert Byte für Byte den korrekten Wert (z. B. ein MAC oder Token).

> [!tip] **Gegenmittel: konstante-Zeit-Vergleich**
> Sicherheitskritische Vergleiche müssen **immer gleich lang** dauern, unabhängig davon, wo die erste Abweichung liegt (z. B. `crypto.timingSafeEqual`, `hmac.compare_digest`). Niemals `==` für Geheimnisse verwenden.

### Weitere verwundbare Operationen

- **Modulares Potenzieren** (RSA): Square-and-Multiply mit datenabhängigen Zweigen → der private Exponent kann leaken.
- **Tabellen-Lookups** (Software-AES-S-Box): cache-abhängige Zugriffszeiten (**Cache-Timing**).
- **Branches** abhängig von Geheimnissen.

### Konstante-Zeit-Kryptographie

> [!warning] **Prüfungsrelevant**
> Sichere Implementierungen vermeiden **datenabhängige** Verzweigungen, Speicherzugriffe und Laufzeiten. Deshalb sind Verfahren wie **ChaCha20** (ARX, keine Tabellen) und **X25519/Ed25519** (→ [[05-ECDH-und-X25519]]) von Natur aus timing-robuster als tabellenbasiertes Software-AES. RSA nutzt „blinding" als Gegenmaßnahme.

Timing-Angriffe sind ein Spezialfall der allgemeineren **Seitenkanalangriffe** (→ [[05-Side-Channel-Angriffe]]).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Timing-Angriffe leiten Geheimnisse aus der Ausführungszeit ab
> - Klassisch: früh abbrechender Vergleich → konstante-Zeit-Vergleich nutzen
> - Weitere Quellen: datenabhängige Zweige, Cache-Timing bei Tabellen-Lookups
> - Abwehr: konstante-Zeit-Code, blinding; ARX-Chiffren sind robuster

---

## Übungen

1. Warum ist ein früh abbrechender MAC-Vergleich gefährlich?
2. Was bedeutet „konstante-Zeit"-Implementierung?
3. Warum ist ChaCha20 timing-robuster als tabellenbasiertes Software-AES?

---

← [[03-Padding-Oracle-Angriffe|← Zurück]] | [[00-Angriffe-Index|Übersicht]] | [[05-Side-Channel-Angriffe|Weiter →]]
