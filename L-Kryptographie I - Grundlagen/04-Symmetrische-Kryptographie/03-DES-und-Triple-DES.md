---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - symmetrisch
---

# DES und Triple-DES

> [!info] **Lernziele**
> - Aufbau und Geschichte von DES verstehen
> - Die Schwäche der Schlüssellänge einordnen
> - Triple-DES als Übergangslösung und seine Grenzen kennen

---

## Inhalt

### DES – Data Encryption Standard

**DES** wurde 1977 vom NIST (damals NBS) als erster öffentlicher Verschlüsselungsstandard festgelegt, basierend auf IBMs „Lucifer". Es ist eine **Blockchiffre** mit:

- **Blockgröße:** 64 Bit
- **Schlüssellänge:** 56 Bit (plus 8 Paritätsbits)
- **Struktur:** 16-Runden-**Feistel-Netzwerk**

### Das Feistel-Netzwerk

DES teilt jeden 64-Bit-Block in zwei 32-Bit-Hälften $L$ und $R$. In jeder Runde gilt:

$$L_{i} = R_{i-1}, \qquad R_{i} = L_{i-1} \oplus f(R_{i-1}, K_i)$$

Der Charme: Die Entschlüsselung verwendet **dieselbe** Struktur, nur mit umgekehrter Rundenschlüsselreihenfolge. Die Rundenfunktion $f$ muss dafür nicht einmal invertierbar sein.

### Die Schwäche: 56-Bit-Schlüssel

Der Schlüsselraum von $2^{56} \approx 7{,}2 \cdot 10^{16}$ war schon in den 1990ern angreifbar. 1998 brach die EFF-Maschine „Deep Crack" einen DES-Schlüssel in unter drei Tagen per Brute Force. DES gilt seitdem als **unsicher**.

### Triple-DES (3DES)

Als Übergangslösung wendet **3DES** DES dreifach an – im EDE-Schema (Encrypt-Decrypt-Encrypt) mit zwei oder drei Schlüsseln:

$$C = E_{K_3}(D_{K_2}(E_{K_1}(M)))$$

- Mit drei unabhängigen Schlüsseln ergibt sich eine effektive Sicherheit von etwa 112 Bit (wegen des Meet-in-the-Middle-Angriffs nicht volle 168 Bit).
- Das mittlere „Decrypt" sorgt für Abwärtskompatibilität: Mit $K_1=K_2=K_3$ verhält sich 3DES wie einfaches DES.

> [!danger] **3DES ist abgekündigt**
> 3DES ist langsam und wegen der kleinen 64-Bit-Blockgröße anfällig für Geburtstags-Angriffe (Sweet32). NIST hat 3DES zum 31.12.2023 für neue Anwendungen **verboten**. Für neue Systeme ist **AES** zu verwenden (→ [[04-Advanced-Encryption-Standard-AES]]).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - DES: 64-Bit-Block, 56-Bit-Schlüssel, 16-Runden-Feistel-Netzwerk
> - 56 Bit sind zu wenig – 1998 per Brute Force gebrochen
> - 3DES (EDE) als Übergang, effektiv ~112 Bit, aber langsam und mit 64-Bit-Block-Schwäche
> - Beide veraltet; Standard ist heute AES

---

## Übungen

1. Erklären Sie, warum die Entschlüsselung im Feistel-Netzwerk dieselbe Struktur nutzt.
2. Warum bietet 3DES mit drei Schlüsseln nicht volle 168 Bit Sicherheit?
3. Welche zwei Gründe sprechen heute gegen den Einsatz von 3DES?

---

← [[02-Blockchiffren-und-Stromchiffren|← Zurück]] | [[00-Symmetrisch-Index|Übersicht]] | [[04-Advanced-Encryption-Standard-AES|Weiter →]]
