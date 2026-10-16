---
author: Andreas Hümmer
title: "Lösung: Zahlensysteme und Binärarithmetik (mit IPv4-Bezug)"
tags:
  - loesung
  - grundlagen
  - zahlensysteme
  - binaerarithmetik
  - ipv4
created: 2026-10-16
modified: 2026-10-16
related: "[[U-Grundlagen-Zahlensysteme-Binaerarithmetik]]"
difficulty: mittel
status: draft
---

# Lösung: Zahlensysteme und Binärarithmetik (mit IPv4-Bezug)

> [!warning] **Spoiler-Warnung**
> Versuche die Aufgaben zuerst selbst zu lösen! Diese Datei enthält die vollständigen Lösungswege zur Übung [[U-Grundlagen-Zahlensysteme-Binaerarithmetik]].

---

## Teil A — Umwandlung von Zahlensystemen

### Lösung 1: Grundlegende Umwandlungen

**a) Dezimal `217` → Binär, Oktal, Hexadezimal**

Wiederholte Division durch 2 (Reste von unten nach oben lesen):

```
217 : 2 = 108 Rest 1
108 : 2 =  54 Rest 0
 54 : 2 =  27 Rest 0
 27 : 2 =  13 Rest 1
 13 : 2 =   6 Rest 1
  6 : 2 =   3 Rest 0
  3 : 2 =   1 Rest 1
  1 : 2 =   0 Rest 1
```

Binär (von unten gelesen): `1101 1001`

- **Hexadezimal:** Bits in 4er-Gruppen bündeln: `1101` = D, `1001` = 9 → `0xD9`
- **Oktal:** Bits in 3er-Gruppen von rechts bündeln: `11 011 001` → `3 3 1` → `0o331`

Probe Hex: `D·16 + 9 = 208 + 9 = 217` ✓
Probe Oktal: `3·64 + 3·8 + 1 = 192 + 24 + 1 = 217` ✓

**Ergebnis:** `217 = 1101 1001₂ = 0o331 = 0xD9`

---

**b) Binär `1011 0110` → Dezimal, Hexadezimal**

Stellenwerte: `128·1 + 64·0 + 32·1 + 16·1 + 8·0 + 4·1 + 2·1 + 1·0`
`= 128 + 32 + 16 + 4 + 2 = 182`

Hex: `1011` = B, `0110` = 6 → `0xB6`

**Ergebnis:** `1011 0110₂ = 182 = 0xB6`

---

**c) Hexadezimal `0x2F` → Binär, Dezimal**

- `2` = `0010`, `F` = `1111` → Binär `0010 1111`
- Dezimal: `2·16 + 15 = 32 + 15 = 47`

**Ergebnis:** `0x2F = 0010 1111₂ = 47`

---

**d) Oktal `0o345` → Dezimal, Binär**

- Dezimal: `3·64 + 4·8 + 5·1 = 192 + 32 + 5 = 229`
- Binär (jede Oktalziffer = 3 Bit): `3`=`011`, `4`=`100`, `5`=`101` → `011 100 101` = `1110 0101`

**Ergebnis:** `0o345 = 229 = 1110 0101₂`

---

### Lösung 2: Oktettweise Umwandlung einer IPv4-Adresse

Adresse: `172.16.254.1`

**a) Oktette binär:**

| Oktett | Dezimal | Binär |
|--------|---------|-------|
| 1 | 172 | `1010 1100` |
| 2 | 16  | `0001 0000` |
| 3 | 254 | `1111 1110` |
| 4 | 1   | `0000 0001` |

Rechnung für 172: `128 + 32 + 8 + 4 = 172` → `1010 1100` ✓
Für 254: `255 − 1 = 254` → `1111 1110` ✓

**b) Vollständige 32-Bit-Darstellung:**

`10101100 00010000 11111110 00000001`

**c) Hexadezimal pro Oktett:**

- 172 = `0xAC`, 16 = `0x10`, 254 = `0xFE`, 1 = `0x01`
- → `AC.10.FE.01`

---

## Teil B — Binärarithmetik

### Lösung 3: Rechnen im Binärsystem

**a) `0101 1010 + 0010 0111`**

```
  0101 1010   (90)
+ 0010 0111   (39)
-----------
  1000 0001   (129)
```

Kontrolle dezimal: `90 + 39 = 129` → `1000 0001` = `128 + 1 = 129` ✓

**b) `1111 0001 + 0001 1111`**

```
   1111 0001   (241)
 + 0001 1111   (31)
 -----------
 1 0001 0000   (272)
```

Dezimal: `241 + 31 = 272`. In 8 Bit passt nur `0 … 255`, daher **tritt ein Überlauf auf**: Es entsteht ein 9. Bit (Carry). Das in 8 Bit gehaltene Ergebnis wäre `0001 0000` (= 16), der Übertrag (Carry-Flag) ist gesetzt.

**c) Bitweise Operationen** mit `A = 1100 1010`, `B = 1010 0110`:

```
A     = 1100 1010
B     = 1010 0110

A UND B = 1000 0010   (nur wo beide 1)
A ODER B= 1110 1110   (wo mindestens eine 1)
A XOR B = 0110 1100   (wo genau eine 1)
NICHT A = 0011 0101   (jedes Bit gekippt)
```

---

### Lösung 4: Bitverschiebung und Zweierpotenzen

**a) `0000 1101 << 2`**

`0000 1101` (= 13) um 2 nach links → `0011 0100` (= 52).
Linksverschiebung um `n` Stellen = Multiplikation mit `2ⁿ`. Hier `2² = 4`, also `13 · 4 = 52` ✓.
**Faktor: 4.**

**b) `1011 0000 >> 3` (logisch)**

`1011 0000` (= 176) um 3 nach rechts, von links mit Nullen aufgefüllt → `0001 0110` (= 22).
Kontrolle: Rechtsverschiebung um 3 = ganzzahlige Division durch `2³ = 8`: `176 / 8 = 22` ✓.
**Ergebnis: 22.**

---

## Teil C — Anwendung auf IPv4

### Lösung 5: Netzmaske und UND-Verknüpfung

Gegeben: `192.168.10.37`, Maske `255.255.255.224` (`/27`).

**a) Maske binär (letztes Oktett):**

`224 = 128 + 64 + 32` → `1110 0000`. Die ersten drei Oktette sind `1111 1111`.
Also 27 Einsen gefolgt von 5 Nullen → bestätigt `/27`.

**b) Netzadresse (bitweises UND):**

Nur das letzte Oktett ist relevant (die ersten drei bleiben `192.168.10`):

```
IP      37 = 0010 0101
Maske  224 = 1110 0000
UND        = 0010 0000  = 32
```

**Netzadresse: `192.168.10.32`**

**c) Broadcast-Adresse** (Host-Bits = alle 1):

Hostanteil = untere 5 Bit. Netz-Oktett `0010 0000`, Host-Bits auf 1:

```
0010 0000  (Netz, letztes Oktett)
0001 1111  (ODER mit allen Host-Bits = 1)
---------
0011 1111  = 63
```

**Broadcast: `192.168.10.63`**

**d) Erste und letzte nutzbare Hostadresse:**

- Erste nutzbare = Netzadresse + 1 → `192.168.10.33`
- Letzte nutzbare = Broadcast − 1 → `192.168.10.62`

Das `/27`-Netz umfasst `2^5 = 32` Adressen (`.32`–`.63`), davon `32 − 2 = 30` nutzbare Hosts.

---

### Lösung 6: Subnetting

Ausgangsnetz: `10.0.0.0/24`.

**a) Nutzbare Hosts in `/24`:**

`2^(32 − 24) − 2 = 2^8 − 2 = 256 − 2 = 254` nutzbare Hostadressen.
(Netzadresse `.0` und Broadcast `.255` sind nicht nutzbar.)

**b) Präfix für 4 gleich große Subnetze:**

4 Subnetze benötigen `log₂(4) = 2` zusätzliche Netz-Bits. Aus `/24` wird daher **`/26`**.
Jedes `/26`-Subnetz hat `2^(32 − 26) = 64` Adressen, davon `62` nutzbar.
Blockgröße im letzten Oktett: `256 − 192 = 64` (Maske `255.255.255.192`).

**c) Die 4 Subnetze:**

| # | Netzadresse | Broadcast | Nutzbarer Hostbereich |
|---|-------------|-----------|------------------------|
| 1 | `10.0.0.0/26`   | `10.0.0.63`  | `10.0.0.1` – `10.0.0.62`   |
| 2 | `10.0.0.64/26`  | `10.0.0.127` | `10.0.0.65` – `10.0.0.126` |
| 3 | `10.0.0.128/26` | `10.0.0.191` | `10.0.0.129` – `10.0.0.190`|
| 4 | `10.0.0.192/26` | `10.0.0.255` | `10.0.0.193` – `10.0.0.254`|

**d) In welchem Subnetz liegt `10.0.0.150`?**

Blockgröße 64 → Grenzen bei 0, 64, 128, 192. `150` liegt zwischen `128` und `191`, also im **Subnetz 3 (`10.0.0.128/26`)**. Es ist eine gültige Hostadresse (zwischen `.129` und `.190`).

---

## Zusammenhänge

- → Übung: [[U-Grundlagen-Zahlensysteme-Binaerarithmetik]]
- → [[00-Aufgaben-Index]]

> [!tip] **Weiterführende Links**
> - [IETF RFC 791 – Internet Protocol (IPv4)](https://www.rfc-editor.org/rfc/rfc791)
> - [IETF RFC 4632 – CIDR (Classless Inter-Domain Routing)](https://www.rfc-editor.org/rfc/rfc4632)

---
*Erstellt am 2026-10-16 | Zuletzt aktualisiert: 2026-10-16*
