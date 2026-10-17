---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - blockchain
  - vertiefung
---

# Kryptographie in Blockchains

> [!info] **Lernziele**
> - Verstehen, welche kryptographischen Bausteine eine Blockchain tragen
> - Den Zusammenhang von Hashes und Signaturen einordnen
> - Erkennen, dass Blockchain kein neues Krypto-Verfahren ist

---

## Inhalt

### Blockchain = bekannte Bausteine neu kombiniert

Eine **Blockchain** erfindet keine neue Kryptographie, sondern kombiniert **bekannte** Bausteine zu einem manipulationssicheren, verteilten Register:

| Baustein | Rolle in der Blockchain | Modul |
|----------|-------------------------|-------|
| **Hashfunktionen** | verketten Blöcke, sichern Integrität | Modul 6 |
| **Merkle-Trees** | fassen Transaktionen effizient zusammen | [[08-Merkle-Trees]] |
| **Digitale Signaturen** | autorisieren Transaktionen (Eigentum) | Modul 7 |
| **Public-Key-Kryptographie** | Adressen = Schlüsselpaare | Modul 5 |

### Die Grundidee

Transaktionen werden zu **Blöcken** gebündelt; jeder Block enthält den **Hash des Vorgängers** (→ [[02-Hash-Chains]]). Dadurch entsteht eine Kette, in der eine nachträgliche Änderung eines alten Blocks **alle** folgenden Hashes ungültig machen würde – das macht die Historie fälschungssicher.

Transaktionen innerhalb eines Blocks werden über einen **Merkle-Tree** (→ [[03-Merkle-Trees-in-Blockchains]]) zu einem einzigen Wurzel-Hash zusammengefasst.

### Eigentum durch Signaturen

> [!tip] **„Not your keys, not your coins"**
> In Kryptowährungen ist das Eigentum an eine **digitale Signatur** gebunden: Nur wer den privaten Schlüssel besitzt, kann eine Transaktion autorisieren (→ [[05-Signaturen-in-Kryptowaehrungen]]). Der private Schlüssel **ist** faktisch das Vermögen – geht er verloren, sind die Coins unwiederbringlich weg.

### Wichtige Einordnung

> [!warning] **Blockchain ≠ Verschlüsselung**
> Eine öffentliche Blockchain ist **transparent**, nicht geheim: Transaktionen sind für alle lesbar. „Krypto" bezieht sich hier auf Hashes und Signaturen, **nicht** auf Vertraulichkeit. Wer Vertraulichkeit will, braucht Zusatztechniken (z. B. ZKPs, → Modul 16).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Blockchain kombiniert Hashes, Merkle-Trees und Signaturen – keine neue Kryptographie
> - Block-Verkettung über Vorgänger-Hashes macht die Historie fälschungssicher
> - Eigentum wird durch digitale Signaturen (privater Schlüssel) belegt
> - Öffentliche Blockchains sind transparent, nicht vertraulich

---

## Übungen

1. Welche vier kryptographischen Bausteine trägt eine Blockchain?
2. Warum macht die Hash-Verkettung die Historie fälschungssicher?
3. Warum bedeutet „Blockchain" nicht automatisch Vertraulichkeit?

---

← [[00-Blockchain-Index|Übersicht]] | [[02-Hash-Chains|Weiter →]]
