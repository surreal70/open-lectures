---
author: Andreas Hümmer
created: 2026-10-13
modified: 2026-10-13
tags:
  - content
  - lf03
  - binaer
  - subnetting
source: proTirone (CC-BY-4.0), Karsten Reincke
---

# Bitweise Operationen für Netzwerke

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Dezimalzahlen in Binärzahlen umrechnen können
> - Die bitweisen Operationen AND, OR, XOR und NOT kennen
> - Die AND-Operation für Subnetting anwenden können
> - Subnetzmasken binär verstehen

---

## Überblick

Bitweise Operationen sind fundamental für das Verständnis von IP-Adressierung und Subnetting. Die wichtigste Operation ist **AND**, mit der Netzwerkadressen berechnet werden.

## Zahlensysteme

### Dezimal zu Binär

Um eine Dezimalzahl in Binär umzurechnen, teile wiederholt durch 2:

```
192 : 2 = 96 Rest 0
 96 : 2 = 48 Rest 0
 48 : 2 = 24 Rest 0
 24 : 2 = 12 Rest 0
 12 : 2 =  6 Rest 0
  6 : 2 =  3 Rest 0
  3 : 2 =  1 Rest 1
  1 : 2 =  0 Rest 1

Von unten nach oben lesen: 192 = 11000000
```

### Binär zu Dezimal

Jede Position hat einen Stellenwert (2^n):

```
Position:  7   6   5   4   3   2   1   0
Wert:    128  64  32  16   8   4   2   1
Bits:      1   1   0   0   0   0   0   0

11000000 = 128 + 64 = 192
```

### Wichtige Binärwerte

| Dezimal | Binär | Verwendung |
|---------|-------|------------|
| 0 | `00000000` | Alle Bits 0 |
| 128 | `10000000` | Höchstes Bit |
| 192 | `11000000` | /2 Präfix |
| 224 | `11100000` | /3 Präfix |
| 240 | `11110000` | /4 Präfix |
| 248 | `11111000` | /5 Präfix |
| 252 | `11111100` | /6 Präfix |
| 254 | `11111110` | /7 Präfix |
| 255 | `11111111` | Alle Bits 1 |

## Bitweise Operationen

### AND-Operation

Ergebnis ist 1, wenn **beide** Bits 1 sind:

| A | B | A AND B |
|---|---|---------|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

**Anwendung: Netzwerkadresse berechnen**

```
IP:    192.168.1.100  = 11000000.10101000.00000001.01100100
Maske: 255.255.255.0  = 11111111.11111111.11111111.00000000
       ───────────────────────────────────────────────────── AND
Netz:  192.168.1.0    = 11000000.10101000.00000001.00000000
```

### OR-Operation

Ergebnis ist 1, wenn **mindestens ein** Bit 1 ist:

| A | B | A OR B |
|---|---|--------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

**Anwendung: Broadcastadresse berechnen**

```
Netz:      192.168.1.0   = 11000000.10101000.00000001.00000000
Inv.Maske: 0.0.0.255     = 00000000.00000000.00000000.11111111
           ───────────────────────────────────────────────────── OR
Broadcast: 192.168.1.255 = 11000000.10101000.00000001.11111111
```

### NOT-Operation (Invertierung)

Kehrt alle Bits um:

| A | NOT A |
|---|-------|
| 0 | 1 |
| 1 | 0 |

**Anwendung: Wildcard-Maske berechnen**

```
Subnetzmaske:  255.255.255.0   = 11111111.11111111.11111111.00000000
               ─────────────────────────────────────────────────────── NOT
Wildcard:      0.0.0.255       = 00000000.00000000.00000000.11111111
```

### XOR-Operation

Ergebnis ist 1, wenn die Bits **unterschiedlich** sind:

| A | B | A XOR B |
|---|---|---------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

## Praktische Beispiele

> [!example] **Übung 1: Dezimal zu Binär**
> Wandle folgende Dezimalzahlen in Binär um:
> - [ ] 172
> - [ ] 16
> - [ ] 45
> - [ ] 200

> [!example] **Übung 2: Netzwerkadresse berechnen**
> Gegeben: `172.16.45.200/20`
> 
> 1. Schreibe IP und Maske binär auf
> 2. Führe die AND-Operation durch
> 3. Wandle das Ergebnis zurück in Dezimal

**Lösung:**
```
IP:    172.16.45.200  = 10101100.00010000.00101101.11001000
Maske: 255.255.240.0  = 11111111.11111111.11110000.00000000
       ───────────────────────────────────────────────────── AND
Netz:  172.16.32.0    = 10101100.00010000.00100000.00000000
```

## Zusammenhänge

- → [[08-IPv4-Adressen|IPv4-Adressen]]
- → [[09-IPv4-Klassen|IPv4-Adressklassen und Subnetting]]
- → [[05-Adressierung|Adressierungskonzepte]]

> [!warning] **Prüfungsrelevant**
> - Umrechnung Dezimal ↔ Binär
> - AND-Operation für Netzwerkberechnung
> - Stellenwerttabelle (128, 64, 32, 16, 8, 4, 2, 1)
> - Subnetzmasken in Binärdarstellung

> [!question] **Typische Prüfungsfragen**
> - Wandeln Sie 192 in eine Binärzahl um.
> - Was ist das Ergebnis von 192 AND 240?
> - Berechnen Sie die Netzwerkadresse für 10.20.30.40/16
> - Wie lautet die Binärdarstellung von 255.255.255.192?

## Quellen

- proTirone: LF03:08 Bitweise Operationen (Karsten Reincke, CC-BY-4.0)

> [!tip] **Weiterführende Links**
> - [Binär-Rechner online](https://www.rapidtables.com/convert/number/binary-to-decimal.html)
> - [[08-IPv4-Adressen|Nächstes Kapitel: IPv4-Adressen]]
