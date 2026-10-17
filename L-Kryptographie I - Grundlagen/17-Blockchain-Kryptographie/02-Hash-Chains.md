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

# Hash Chains

> [!info] **Lernziele**
> - Das Prinzip einer Hash-Chain verstehen
> - Nachvollziehen, wie sie Unveränderlichkeit erzeugt
> - Den Bezug zur Blockchain herstellen

---

## Inhalt

### Was ist eine Hash-Chain?

Eine **Hash-Chain** ist eine Folge von Datenblöcken, bei der jeder Block den **Hash des vorhergehenden** enthält:

```
Block 0 (Genesis)   Block 1              Block 2
+------------+      +--------------+     +--------------+
| Daten      |      | Daten        |     | Daten        |
| prev: ---  |      | prev: H(B0)  |     | prev: H(B1)  |
+------------+      +--------------+     +--------------+
       └── H(B0) ──────────┘   └── H(B1) ──────────┘
```

### Warum unveränderlich?

> [!tip] **Der Dominoeffekt**
> Ändert jemand nachträglich Block 1, ändert sich dessen Hash. Da Block 2 den alten Hash von Block 1 gespeichert hat, passt die Kette nicht mehr – und alle **folgenden** Blöcke werden ungültig. Um die Manipulation zu verbergen, müsste der Angreifer **alle** nachfolgenden Blöcke neu berechnen. In einer Blockchain mit Proof-of-Work (→ [[06-Konsensalgorithmen-und-Kryptographie]]) ist genau das praktisch unmöglich.

### Voraussetzung: sichere Hashfunktion

Die Unveränderlichkeit beruht vollständig auf der **Kollisions- und Urbildresistenz** der Hashfunktion (→ [[04-Kollisionsresistenz-und-Preimage-Resistenz]]). Blockchains nutzen daher moderne Hashes (Bitcoin: SHA-256, Ethereum: Keccak-256).

### Abgrenzung zum Merkle-Tree

- **Hash-Chain:** verkettet **Blöcke** in einer Linie (zeitliche Reihenfolge).
- **Merkle-Tree:** fasst die **Transaktionen innerhalb** eines Blocks baumförmig zusammen (→ [[03-Merkle-Trees-in-Blockchains]]).

Beide arbeiten zusammen: Die Chain sichert die Reihenfolge der Blöcke, der Tree den Inhalt jedes Blocks.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Hash-Chain: jeder Block enthält den Hash des Vorgängers
> - Nachträgliche Änderungen brechen alle folgenden Hashes (Dominoeffekt)
> - Sicherheit beruht auf Kollisions-/Urbildresistenz der Hashfunktion
> - Chain verkettet Blöcke, Merkle-Tree fasst Transaktionen im Block zusammen

---

## Übungen

1. Was enthält jeder Block einer Hash-Chain außer seinen Daten?
2. Warum macht eine Änderung an einem alten Block die ganze Folgekette ungültig?
3. Worin unterscheidet sich eine Hash-Chain von einem Merkle-Tree?

---

← [[01-Kryptographie-in-Blockchains|← Zurück]] | [[00-Blockchain-Index|Übersicht]] | [[03-Merkle-Trees-in-Blockchains|Weiter →]]
