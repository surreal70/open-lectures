---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - symmetrisch
---

# Betriebsmodi ECB CBC CTR GCM

> [!info] **Lernziele**
> - Verstehen, warum Blockchiffren einen Betriebsmodus brauchen
> - ECB, CBC, CTR und GCM in Funktion und Sicherheit unterscheiden
> - Den richtigen Modus für einen Anwendungsfall wählen

---

## Inhalt

### Warum Betriebsmodi?

Eine Blockchiffre wie AES verschlüsselt nur einen einzelnen Block (128 Bit). Ein **Betriebsmodus** legt fest, wie längere Nachrichten über viele Blöcke hinweg verschlüsselt werden.

### ECB – Electronic Codebook

Jeder Block wird **unabhängig** mit demselben Schlüssel verschlüsselt.

> [!danger] **ECB niemals verwenden**
> Gleiche Klartextblöcke ergeben gleiche Chiffretextblöcke. Dadurch bleiben Muster im Chiffretext sichtbar – das berüchtigte „ECB-Pinguin"-Bild zeigt, dass Strukturen eines Bildes trotz Verschlüsselung erkennbar bleiben. ECB ist nicht IND-CPA-sicher.

### CBC – Cipher Block Chaining

Jeder Klartextblock wird vor der Verschlüsselung mit dem vorherigen Chiffretextblock XOR-verknüpft; der erste Block nutzt einen zufälligen **IV**:

$$C_i = E_K(M_i \oplus C_{i-1}), \qquad C_0 = IV$$

- Gleiche Klartextblöcke ergeben nun unterschiedliche Chiffretexte.
- Nachteil: sequenziell (nicht parallelisierbar beim Verschlüsseln), braucht Padding und ist ohne zusätzlichen Integritätsschutz anfällig für **Padding-Oracle-Angriffe** (→ Modul 12).

### CTR – Counter

Verwandelt die Blockchiffre in eine **Stromchiffre**: Ein Zähler (Nonce + fortlaufender Wert) wird verschlüsselt und der resultierende Schlüsselstrom per XOR mit dem Klartext verknüpft.

$$C_i = M_i \oplus E_K(\text{Nonce} \,\|\, i)$$

- Parallelisierbar, kein Padding nötig, wahlfreier Zugriff.
- **Kritisch:** Die Nonce darf pro Schlüssel nie wiederholt werden.

### GCM – Galois/Counter Mode

**GCM** erweitert CTR um **Authentizität**: Zusätzlich zum Schlüsselstrom wird ein Authentisierungs-Tag über Galois-Feld-Multiplikation berechnet. GCM ist ein **AEAD**-Verfahren (→ [[07-Authenticated-Encryption-AEAD]]) und schützt gleichzeitig Vertraulichkeit **und** Integrität.

### Vergleich

| Modus | Vertraulichkeit | Integrität | Parallel | Padding |
|-------|-----------------|-----------|----------|---------|
| ECB | ✗ (unsicher) | ✗ | ✓ | ja |
| CBC | ✓ | ✗ | nur Entschl. | ja |
| CTR | ✓ | ✗ | ✓ | nein |
| **GCM** | ✓ | ✓ | ✓ | nein |

**Empfehlung:** Für neue Anwendungen **AES-GCM** (oder ChaCha20-Poly1305), da sie Verschlüsselung und Authentisierung in einem bieten.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Betriebsmodi erweitern eine Blockchiffre auf Nachrichten beliebiger Länge
> - ECB ist unsicher (Muster bleiben sichtbar), CBC benötigt IV und Padding
> - CTR macht die Blockchiffre zur Stromchiffre (parallel, nonce-kritisch)
> - GCM liefert zusätzlich Integrität (AEAD) und ist heute die Standardempfehlung

---

## Übungen

1. Warum ist der ECB-Modus unsicher?
2. Welche Rolle spielt der IV im CBC-Modus?
3. Was unterscheidet GCM von CTR, und warum ist dieser Unterschied wichtig?

---

← [[04-Advanced-Encryption-Standard-AES|← Zurück]] | [[00-Symmetrisch-Index|Übersicht]] | [[06-ChaCha20-und-ChaCha20-Poly1305|Weiter →]]
