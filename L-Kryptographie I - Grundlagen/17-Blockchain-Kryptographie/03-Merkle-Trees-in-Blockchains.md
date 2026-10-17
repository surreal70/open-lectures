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

# Merkle Trees in Blockchains

> [!info] **Lernziele**
> - Die Rolle von Merkle-Trees in Blockchains verstehen
> - Den Nutzen des Merkle Root im Blockheader einordnen
> - SPV / Light Clients nachvollziehen

---

## Inhalt

### Transaktionen im Block

Ein Block enthält viele Transaktionen. Statt alle einzeln im Blockheader zu speichern, werden sie über einen **Merkle-Tree** (→ [[08-Merkle-Trees]]) zu einem einzigen **Merkle Root** zusammengefasst, der im **Blockheader** steht.

```
Blockheader: { prev_hash, merkle_root, nonce, timestamp, ... }
                              │
                        Merkle Root
                        /          \
                  H(T1+T2)        H(T3+T4)
                  /     \         /     \
                H(T1)  H(T2)    H(T3)  H(T4)
                 T1     T2       T3     T4   (Transaktionen)
```

### Nutzen: Integrität und Effizienz

- **Integrität:** Jede Änderung an einer Transaktion ändert den Merkle Root und damit den Blockheader → sofort erkennbar.
- **Kompakter Blockheader:** Der Header referenziert alle Transaktionen über **einen** Hash.

### SPV / Light Clients

> [!tip] **Mitgliedsbeweis ohne die ganze Blockchain**
> Ein **Light Client (SPV, Simplified Payment Verification)** muss nicht die komplette Blockchain speichern. Um zu prüfen, ob eine Transaktion in einem Block enthalten ist, genügt der **Merkle-Pfad** – nur $\log_2 n$ Hashes statt aller Transaktionen (→ [[08-Merkle-Trees]]). Das macht Wallets auf Mobilgeräten praktikabel.

### Varianten

Verschiedene Blockchains nutzen Weiterentwicklungen: Bitcoin einen klassischen binären Merkle-Tree, Ethereum eine **Merkle-Patricia-Trie** für Zustände (Kontostände, Verträge), die zusätzlich effiziente Schlüssel-Wert-Beweise erlaubt.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Transaktionen eines Blocks werden zum Merkle Root im Blockheader zusammengefasst
> - Jede Transaktionsänderung ändert den Root → Integritätsschutz
> - SPV/Light Clients prüfen Enthaltensein über kurze Merkle-Pfade ($\log_2 n$ Hashes)
> - Ethereum nutzt Merkle-Patricia-Tries für Zustände

---

## Übungen

1. Wo steht der Merkle Root und was fasst er zusammen?
2. Warum ändert eine manipulierte Transaktion den gesamten Block?
3. Wie kann ein Light Client eine Transaktion ohne die ganze Blockchain prüfen?

---

← [[02-Hash-Chains|← Zurück]] | [[00-Blockchain-Index|Übersicht]] | [[04-Wallets-und-Schluesselmanagement|Weiter →]]
