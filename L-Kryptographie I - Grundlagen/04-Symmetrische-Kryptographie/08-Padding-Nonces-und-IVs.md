---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - symmetrisch
---

# Padding Nonces und IVs

> [!info] **Lernziele**
> - Zweck und Funktionsweise von Padding verstehen
> - IV und Nonce unterscheiden und korrekt einsetzen
> - Typische Fehler und ihre Sicherheitsfolgen kennen

---

## Inhalt

### Padding

Blockchiffren verarbeiten vollständige Blöcke. Ist die Nachricht kein Vielfaches der Blockgröße, füllt **Padding** den letzten Block auf. Das verbreitetste Schema ist **PKCS#7**: Es werden $k$ Bytes mit dem Wert $k$ angehängt.

```
Blockgröße 8, Nachricht "KRYPTO" (6 Byte):
K R Y P T O 02 02        → 2 Bytes mit Wert 0x02 ergänzt
```

Ist die Nachricht bereits ein Vielfaches der Blockgröße, wird ein **kompletter** Padding-Block angehängt, damit die Entschlüsselung das Padding eindeutig entfernen kann.

> [!danger] **Padding-Oracle**
> Verrät ein System (etwa durch unterschiedliche Fehlermeldungen oder Antwortzeiten), ob das Padding nach der Entschlüsselung gültig war, kann ein Angreifer den Klartext Byte für Byte rekonstruieren – ohne den Schlüssel. Gegenmittel: Authenticated Encryption (→ [[07-Authenticated-Encryption-AEAD]]), die manipulierte Chiffretexte vor der Padding-Prüfung ablehnt. Stromchiffren und CTR/GCM brauchen gar kein Padding.

### Initialisierungsvektor (IV)

Ein **IV** sorgt dafür, dass gleiche Klartexte unter demselben Schlüssel unterschiedliche Chiffretexte ergeben (z. B. im CBC-Modus). Anforderungen:

- **Unvorhersehbar/zufällig** (bei CBC: ein vorhersehbarer IV ermöglicht Angriffe wie BEAST).
- Darf **öffentlich** übertragen werden (meist dem Chiffretext vorangestellt).
- Muss **nicht geheim**, aber pro Nachricht **verschieden** sein.

### Nonce (number used once)

Eine **Nonce** ist ein Wert, der pro Schlüssel **nur einmal** verwendet werden darf. Sie wird bei Stromchiffren und in CTR/GCM eingesetzt.

### IV vs. Nonce

| Eigenschaft | IV (z. B. CBC) | Nonce (z. B. CTR/GCM) |
|-------------|----------------|------------------------|
| Hauptanforderung | unvorhersehbar/zufällig | einmalig pro Schlüssel |
| Wiederholung | problematisch | **fatal** |
| Geheim? | nein | nein |

> [!danger] **Nonce-Wiederverwendung in GCM**
> Wird in AES-GCM dieselbe Nonce mit demselben Schlüssel zweimal benutzt, lässt sich nicht nur der Klartext teilweise rekonstruieren – es kann sogar der **Authentisierungsschlüssel** kompromittiert werden, wodurch der Angreifer beliebige Nachrichten fälschen kann. Nonce-Eindeutigkeit ist in GCM absolut kritisch.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Padding (z. B. PKCS#7) füllt den letzten Block auf; CTR/GCM brauchen keins
> - Padding-Oracles erlauben Klartext-Rekonstruktion – AEAD schützt davor
> - IV: unvorhersehbar, pro Nachricht verschieden, darf öffentlich sein
> - Nonce: einmalig pro Schlüssel – Wiederverwendung (bes. in GCM) ist fatal

---

## Übungen

1. Wenden Sie PKCS#7-Padding auf eine 5-Byte-Nachricht bei Blockgröße 8 an.
2. Worin unterscheiden sich die Anforderungen an IV und Nonce?
3. Warum ist Nonce-Wiederverwendung in AES-GCM besonders gefährlich?

---

← [[07-Authenticated-Encryption-AEAD|← Zurück]] | [[00-Symmetrisch-Index|Übersicht]] | [[00-Asymmetrisch-Index|Nächstes Modul →]]
