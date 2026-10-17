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

# Konsensalgorithmen und Kryptographie

> [!info] **Lernziele**
> - Das Konsensproblem in verteilten Systemen verstehen
> - Proof-of-Work und Proof-of-Stake einordnen
> - Die Rolle der Kryptographie im Konsens erkennen

---

## Inhalt

### Das Konsensproblem

In einem dezentralen Netzwerk ohne zentrale Autorität müssen sich alle Teilnehmer auf **eine** gültige Version der Blockchain einigen – auch bei bösartigen Teilnehmern. Das ist das **Konsensproblem** (verwandt mit dem Byzantine Generals Problem).

### Proof-of-Work (PoW)

**Proof-of-Work** (Bitcoin) verlangt, dass ein Teilnehmer („Miner") eine rechenintensive **Hash-Aufgabe** löst: einen Blockheader so variieren (über eine **Nonce**), dass der Hash unter einem Zielwert liegt.

```
Finde nonce, sodass  SHA-256(Blockheader + nonce) < Ziel
```

- **Teuer zu erzeugen, billig zu prüfen:** Das Finden erfordert enorme Rechenleistung, die Verifikation nur einen Hash.
- **Sicherheit:** Eine Manipulation alter Blöcke würde erfordern, deren PoW **und** den aller Folgeblöcke neu zu berechnen – praktisch unmöglich (→ [[02-Hash-Chains]]).
- **Nachteil:** sehr hoher Energieverbrauch.

### Proof-of-Stake (PoS)

**Proof-of-Stake** (Ethereum seit „The Merge") ersetzt Rechenarbeit durch **Einsatz (Stake)**: Validatoren hinterlegen Kapital und werden pseudozufällig zur Blockerstellung ausgewählt. Fehlverhalten führt zum Verlust des Einsatzes (**Slashing**).

- **Energieeffizient** (kein Mining-Wettrennen).
- Sicherheit beruht auf ökonomischen Anreizen plus **Signaturen** der Validatoren.

### Die Rolle der Kryptographie

> [!note] **Konsens ≠ Kryptographie, aber darauf aufbauend**
> Der Konsensmechanismus selbst ist primär ein **verteiltes-Systeme-Problem**. Kryptographie liefert aber die Bausteine: **Hashfunktionen** (PoW-Puzzle, Verkettung), **Signaturen** (Validator-Abstimmungen in PoS) und zunehmend **ZKPs** (→ Modul 16) für Skalierung und Privatsphäre.

### Weitere Ansätze

BFT-basierte Verfahren (PBFT, Tendermint) und delegierte Varianten (DPoS) nutzen ebenfalls Signaturen und Hashes als Fundament.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Konsens: Einigung auf eine Kette trotz bösartiger Teilnehmer (byzantinisch)
> - PoW: rechenintensives Hash-Puzzle, sicher aber energiehungrig (Bitcoin)
> - PoS: Einsatz statt Rechenarbeit, energieeffizient, mit Slashing (Ethereum)
> - Kryptographie (Hashes, Signaturen, ZKPs) liefert die Bausteine des Konsenses

---

## Übungen

1. Was ist das Konsensproblem in einer dezentralen Blockchain?
2. Erklären Sie das Grundprinzip von Proof-of-Work.
3. Worin unterscheidet sich Proof-of-Stake von Proof-of-Work?

---

← [[05-Signaturen-in-Kryptowaehrungen|← Zurück]] | [[00-Blockchain-Index|Übersicht]] | [[00-Advanced-Index|Nächstes Modul →]]
