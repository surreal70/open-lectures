---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - hash
---

# Merkle Trees

> [!info] **Lernziele**
> - Aufbau und Funktionsweise eines Merkle-Trees verstehen
> - Den Nutzen für effiziente Integritätsprüfung erkennen
> - Anwendungsfälle wie Blockchain und Zertifikatstransparenz einordnen

---

## Inhalt

### Aufbau

Ein **Merkle-Tree** (Hash-Baum) ist eine Baumstruktur, in der jeder Blattknoten den Hash eines Datenblocks enthält und jeder innere Knoten den Hash der Verkettung seiner Kinder:

```
                 Root-Hash
                /         \
          H(H1+H2)       H(H3+H4)
          /      \       /      \
        H1=H(D1) H2=H(D2) H3=H(D3) H4=H(D4)
         |        |        |        |
        D1       D2       D3       D4
```

Der **Root-Hash (Merkle Root)** fasst den gesamten Datenbestand in einem einzigen Hashwert zusammen. Ändert sich ein einziges Datenblatt, ändert sich der Root-Hash.

### Effiziente Verifikation

Der große Vorteil: Um zu beweisen, dass ein bestimmter Block Teil des Baums ist, braucht man **nicht** alle Daten – nur den **Merkle-Pfad** (die Hashes der Geschwisterknoten entlang des Weges zur Wurzel).

Bei $n$ Blättern umfasst ein solcher Beweis nur $\log_2 n$ Hashes. Für eine Million Blöcke genügen also rund **20 Hashes** statt einer Million – das macht Merkle-Trees extrem skalierbar.

### Anwendungen

| Anwendung | Rolle des Merkle-Trees |
|-----------|------------------------|
| **Blockchain** | Transaktionen eines Blocks werden zum Merkle Root zusammengefasst (→ Modul 17) |
| **Git** | Versionsverwaltung baut auf Hash-Bäumen auf |
| **Certificate Transparency** | Append-only-Logs für Zertifikate (→ Modul 8) |
| **BitTorrent / IPFS** | Integritätsprüfung einzelner Datenblöcke |
| **Backup/Sync** | schnelles Erkennen geänderter Teile großer Datenmengen |

### Sicherheit

Die Sicherheit beruht auf der **Kollisionsresistenz** der verwendeten Hashfunktion (→ [[04-Kollisionsresistenz-und-Preimage-Resistenz]]): Könnte ein Angreifer Kollisionen erzeugen, ließe sich ein Datenblock unbemerkt austauschen, ohne den Root-Hash zu ändern. Deshalb werden moderne Hashes (SHA-256, BLAKE3) eingesetzt.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Merkle-Tree: Blätter = Daten-Hashes, innere Knoten = Hash der Kinder, Wurzel fasst alles zusammen
> - Mitgliedsbeweis über Merkle-Pfad benötigt nur $\log_2 n$ Hashes
> - Anwendungen: Blockchain, Git, Certificate Transparency, P2P-Systeme
> - Sicherheit hängt an der Kollisionsresistenz der Hashfunktion

---

## Übungen

1. Wie entsteht der Root-Hash aus den Datenblöcken?
2. Wie viele Hashes umfasst ein Mitgliedsbeweis bei 1024 Blättern?
3. Warum ist Kollisionsresistenz die kritische Eigenschaft für Merkle-Trees?

---

← [[07-Salt-Pepper-und-Key-Stretching|← Zurück]] | [[00-Hashfunktionen-Index|Übersicht]] | [[00-Signaturen-Index|Nächstes Modul →]]
