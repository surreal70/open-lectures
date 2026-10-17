---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - geschichte
  - grundlagen
---

# Geschichte der Kryptographie

> [!info] **Lernziele**
> - Die historische Entwicklung der Kryptographie kennen
> - Wichtige Meilensteine und Persönlichkeiten einordnen
> - Den Wandel von der klassischen zur modernen Kryptographie verstehen

---

## Inhalt

### Antike Kryptographie

Schon in der Antike bestand das Bedürfnis, Nachrichten vor Unbefugten zu schützen. Man unterscheidet dabei zwei grundlegende Ansätze, die sich bis heute durchziehen:

- **Kryptographie** verschleiert den *Inhalt* einer Nachricht.
- **Steganographie** verbirgt die *Existenz* einer Nachricht (z. B. unsichtbare Tinte, Wachstafeln unter der Beschichtung).

Frühe Verfahren:

| Verfahren | Herkunft | Prinzip |
|-----------|----------|---------|
| **Skytale** | Sparta, ca. 5. Jh. v. Chr. | Transpositionschiffre: Pergamentstreifen um einen Stab bestimmten Durchmessers gewickelt |
| **Caesar-Chiffre** | Römisches Reich, ca. 50 v. Chr. | Monoalphabetische Substitution: jeder Buchstabe um feste Anzahl Stellen verschoben |
| **Atbasch** | Hebräische Tradition | Substitution durch Spiegelung des Alphabets |

Die Caesar-Chiffre verschiebt jeden Buchstaben um einen festen Wert (klassisch um 3): aus `A` wird `D`, aus `B` wird `E` usw. Sie ist mit nur 25 möglichen Schlüsseln trivial zu brechen, illustriert aber das Grundprinzip der Substitution.

### Mittelalter und Renaissance

Der entscheidende Fortschritt dieser Epoche war die **Kryptoanalyse**. Der arabische Gelehrte **al-Kindī** beschrieb im 9. Jahrhundert die **Häufigkeitsanalyse**: Da in jeder Sprache bestimmte Buchstaben unterschiedlich häufig vorkommen (im Deutschen etwa `E` und `N`), lassen sich monoalphabetische Substitutionen durch Zählen der Zeichenhäufigkeit brechen.

Als Antwort entstanden **polyalphabetische** Verfahren:

- Die **Vigenère-Chiffre** (16. Jh., benannt nach Blaise de Vigenère) verwendet ein Schlüsselwort, das mehrere wechselnde Cäsar-Verschiebungen steuert. Sie galt lange als „le chiffre indéchiffrable", bis **Friedrich Kasiski** 1863 ein systematisches Brechverfahren veröffentlichte.

### 19. und 20. Jahrhundert

Mit Telegraphie und Funk wuchs der Bedarf an maschineller Verschlüsselung dramatisch.

- **Vernam-Chiffre / One-Time-Pad (1917):** Gilbert Vernam entwickelte ein Verfahren, das – bei wahrhaft zufälligem, einmal verwendetem Schlüssel gleicher Länge wie die Nachricht – **beweisbar sicher** ist (von Shannon später als „perfect secrecy" bewiesen).
- **Enigma (Zweiter Weltkrieg):** Die deutsche Rotor-Chiffriermaschine erzeugte eine komplexe polyalphabetische Substitution. Polnische Mathematiker um **Marian Rejewski** und später das britische Team um **Alan Turing** in Bletchley Park brachen sie – ein kriegsentscheidender Beitrag und Geburtsstunde der maschinellen Kryptoanalyse.

### Die moderne Ära

Die Computerära verlagerte die Kryptographie von Buchstaben zu Bits:

- **DES (Data Encryption Standard, 1977):** Erste öffentlich standardisierte Blockchiffre (IBM/NIST), mit 56-Bit-Schlüssel heute zu schwach.
- **Diffie-Hellman (1976):** Whitfield Diffie und Martin Hellman veröffentlichten den ersten Schlüsselaustausch über unsichere Kanäle und begründeten die **asymmetrische (Public-Key-)Kryptographie**.
- **RSA (1977):** Rivest, Shamir und Adleman lieferten das erste praktikable Public-Key-Verfahren für Verschlüsselung und Signatur.
- **AES (2001):** Rijndael von Daemen und Rijmen gewann den offenen NIST-Wettbewerb und löste DES als Standard ab.

### Aktuelle Entwicklungen

- **Post-Quanten-Kryptographie:** Quantencomputer bedrohen RSA und ECC (Shor-Algorithmus). Das NIST standardisierte 2024 erste quantenresistente Verfahren (u. a. ML-KEM/Kyber, ML-DSA/Dilithium).
- **Angewandte Kryptographie:** Blockchain-Technologien, Zero-Knowledge-Proofs und homomorphe Verschlüsselung eröffnen neue Anwendungsfelder.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Kryptographie ist Jahrtausende alt
> - Der Wettlauf zwischen Kryptographie und Kryptoanalyse treibt die Entwicklung
> - Die Computerära revolutionierte die Kryptographie grundlegend

---

## Übungen

1. Recherchieren Sie die Geschichte der Enigma-Maschine
2. Erstellen Sie eine Zeitleiste wichtiger kryptographischer Entwicklungen

---

## Weiterführende Literatur

- Singh, Simon: *Geheime Botschaften*
- Kahn, David: *The Codebreakers*

---

← [[00-Einfuehrung-Index|Zurück zur Übersicht]] | [[02-Grundbegriffe-und-Terminologie|Weiter →]]
