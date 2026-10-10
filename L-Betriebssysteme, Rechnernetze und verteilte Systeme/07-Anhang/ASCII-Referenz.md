---
author: Andreas Hümmer
title: ASCII-Referenz
tags:
  - anhang
  - referenz
  - ascii
  - zeichensatz
  - encoding
created: '2026-10-07'
modified: '2026-10-07'
bereich: Anhang
---

# ASCII-Referenz

## Überblick

**ASCII** (American Standard Code for Information Interchange) ist ein 7-Bit-Zeichensatz, der 1963 als US-amerikanischer Standard veröffentlicht wurde und die Grundlage für praktisch alle modernen Zeichenkodierungen bildet.

---

## Historische Entwicklung

### Vorgeschichte

| Jahr | Entwicklung |
|------|-------------|
| 1838 | **Morse-Code** - Erste standardisierte Zeichenkodierung |
| 1874 | **Baudot-Code** - 5-Bit-Code für Fernschreiber |
| 1932 | **CCITT-2** (ITA2) - Internationaler Telegrafencode |
| 1956 | **FIELDATA** - Militärischer 7-Bit-Code (US Army) |
| 1960 | Erste ASCII-Entwürfe (ASA X3.4) |

### ASCII-Entwicklung

| Jahr | Meilenstein |
|------|-------------|
| **1963** | **ASA X3.4-1963** - Erste ASCII-Veröffentlichung |
| 1965 | Revision mit kleineren Änderungen |
| **1967** | **ANSI X3.4-1967** - Wichtige Revision, weitgehend kompatibel mit heute |
| 1968 | ISO/IEC 646 - Internationale Version (mit nationalen Varianten) |
| **1986** | **ANSI X3.4-1986** - Letzte Revision, bis heute gültig |

### Von ASCII zu Unicode

| Jahr | Entwicklung |
|------|-------------|
| 1981 | **IBM Code Page 437** - Erste 8-Bit-Erweiterung (DOS) |
| 1985 | **ISO 8859-1** (Latin-1) - Westeuropäische Zeichen |
| 1991 | **Unicode 1.0** - Universeller Zeichensatz |
| 1993 | **UTF-8** - Variable Kodierung, ASCII-kompatibel |
| 2024 | Unicode 15.1 - Über 149.000 Zeichen |

---

## ASCII-Struktur

ASCII ist ein **7-Bit-Code** mit 128 Zeichen (0-127):

```
  Bit:  6 5 4 3 2 1 0
        | | | | | | |
        └─┴─┴─┴─┴─┴─┴─── 7 Bit = 128 Zeichen (0x00 - 0x7F)

  Aufteilung:
  ┌─────────────────────────────────────────────────────────┐
  │  0x00 - 0x1F  │  Steuerzeichen (32 Zeichen)             │
  │  0x20 - 0x7E  │  Druckbare Zeichen (95 Zeichen)         │
  │  0x7F         │  DEL (Delete)                           │
  └─────────────────────────────────────────────────────────┘
```

---

## Vollständige ASCII-Tabelle

### Steuerzeichen (0x00 - 0x1F)

| Dez | Hex | Bin | Abk | Name | Bedeutung |
|-----|-----|-----|-----|------|-----------|
| 0 | 0x00 | 0000000 | NUL | Null | Füllzeichen, String-Ende in C |
| 1 | 0x01 | 0000001 | SOH | Start of Heading | Nachrichtenkopf-Beginn |
| 2 | 0x02 | 0000010 | STX | Start of Text | Textbeginn |
| 3 | 0x03 | 0000011 | ETX | End of Text | Textende, Ctrl+C |
| 4 | 0x04 | 0000100 | EOT | End of Transmission | Übertragungsende, Ctrl+D |
| 5 | 0x05 | 0000101 | ENQ | Enquiry | Statusabfrage |
| 6 | 0x06 | 0000110 | ACK | Acknowledge | Positive Bestätigung |
| 7 | 0x07 | 0000111 | BEL | Bell | Signalton, \a |
| 8 | 0x08 | 0001000 | BS | Backspace | Rückschritt, \b |
| 9 | 0x09 | 0001001 | HT | Horizontal Tab | Tabulator, \t |
| 10 | 0x0A | 0001010 | LF | Line Feed | Zeilenvorschub, \n (Unix-Zeilenende) |
| 11 | 0x0B | 0001011 | VT | Vertical Tab | Vertikaler Tabulator, \v |
| 12 | 0x0C | 0001100 | FF | Form Feed | Seitenvorschub, \f |
| 13 | 0x0D | 0001101 | CR | Carriage Return | Wagenrücklauf, \r (Mac Classic) |
| 14 | 0x0E | 0001110 | SO | Shift Out | Zeichensatz wechseln |
| 15 | 0x0F | 0001111 | SI | Shift In | Zeichensatz zurück |
| 16 | 0x10 | 0010000 | DLE | Data Link Escape | Escape für Datenübertragung |
| 17 | 0x11 | 0010001 | DC1 | Device Control 1 | XON - Übertragung fortsetzen |
| 18 | 0x12 | 0010010 | DC2 | Device Control 2 | Gerätespezifisch |
| 19 | 0x13 | 0010011 | DC3 | Device Control 3 | XOFF - Übertragung stoppen |
| 20 | 0x14 | 0010100 | DC4 | Device Control 4 | Gerätespezifisch |
| 21 | 0x15 | 0010101 | NAK | Negative Ack | Negative Bestätigung |
| 22 | 0x16 | 0010110 | SYN | Synchronous Idle | Synchronisation |
| 23 | 0x17 | 0010111 | ETB | End of Trans Block | Blockende |
| 24 | 0x18 | 0011000 | CAN | Cancel | Abbruch |
| 25 | 0x19 | 0011001 | EM | End of Medium | Datenträger-Ende |
| 26 | 0x1A | 0011010 | SUB | Substitute | Ersatzzeichen, Ctrl+Z (DOS EOF) |
| 27 | 0x1B | 0011011 | ESC | Escape | Escape-Sequenz, \e |
| 28 | 0x1C | 0011100 | FS | File Separator | Dateitrenner |
| 29 | 0x1D | 0011101 | GS | Group Separator | Gruppentrenner |
| 30 | 0x1E | 0011110 | RS | Record Separator | Datensatztrenner |
| 31 | 0x1F | 0011111 | US | Unit Separator | Feldtrenner |

> [!info] Zeilenende-Konventionen
> - **Unix/Linux/macOS**: LF (0x0A) - `\n`
> - **Windows**: CR+LF (0x0D 0x0A) - `\r\n`
> - **Mac Classic**: CR (0x0D) - `\r`

### Druckbare Zeichen (0x20 - 0x7E)

#### Satzzeichen und Symbole (0x20 - 0x2F)

| Dez | Hex | Zeichen | Name |
|-----|-----|---------|------|
| 32 | 0x20 | ` ` | Space (Leerzeichen) |
| 33 | 0x21 | `!` | Exclamation Mark |
| 34 | 0x22 | `"` | Quotation Mark |
| 35 | 0x23 | `#` | Number Sign / Hash |
| 36 | 0x24 | `$` | Dollar Sign |
| 37 | 0x25 | `%` | Percent Sign |
| 38 | 0x26 | `&` | Ampersand |
| 39 | 0x27 | `'` | Apostrophe |
| 40 | 0x28 | `(` | Left Parenthesis |
| 41 | 0x29 | `)` | Right Parenthesis |
| 42 | 0x2A | `*` | Asterisk |
| 43 | 0x2B | `+` | Plus Sign |
| 44 | 0x2C | `,` | Comma |
| 45 | 0x2D | `-` | Hyphen-Minus |
| 46 | 0x2E | `.` | Full Stop / Period |
| 47 | 0x2F | `/` | Solidus / Slash |

#### Ziffern (0x30 - 0x39)

| Dez | Hex | Zeichen | Name |
|-----|-----|---------|------|
| 48 | 0x30 | `0` | Digit Zero |
| 49 | 0x31 | `1` | Digit One |
| 50 | 0x32 | `2` | Digit Two |
| 51 | 0x33 | `3` | Digit Three |
| 52 | 0x34 | `4` | Digit Four |
| 53 | 0x35 | `5` | Digit Five |
| 54 | 0x36 | `6` | Digit Six |
| 55 | 0x37 | `7` | Digit Seven |
| 56 | 0x38 | `8` | Digit Eight |
| 57 | 0x39 | `9` | Digit Nine |

#### Weitere Satzzeichen (0x3A - 0x40)

| Dez | Hex | Zeichen | Name |
|-----|-----|---------|------|
| 58 | 0x3A | `:` | Colon |
| 59 | 0x3B | `;` | Semicolon |
| 60 | 0x3C | `<` | Less-Than Sign |
| 61 | 0x3D | `=` | Equals Sign |
| 62 | 0x3E | `>` | Greater-Than Sign |
| 63 | 0x3F | `?` | Question Mark |
| 64 | 0x40 | `@` | Commercial At |

#### Großbuchstaben (0x41 - 0x5A)

| Dez | Hex | Zeichen | | Dez | Hex | Zeichen |
|-----|-----|---------|---|-----|-----|---------|
| 65 | 0x41 | `A` | | 78 | 0x4E | `N` |
| 66 | 0x42 | `B` | | 79 | 0x4F | `O` |
| 67 | 0x43 | `C` | | 80 | 0x50 | `P` |
| 68 | 0x44 | `D` | | 81 | 0x51 | `Q` |
| 69 | 0x45 | `E` | | 82 | 0x52 | `R` |
| 70 | 0x46 | `F` | | 83 | 0x53 | `S` |
| 71 | 0x47 | `G` | | 84 | 0x54 | `T` |
| 72 | 0x48 | `H` | | 85 | 0x55 | `U` |
| 73 | 0x49 | `I` | | 86 | 0x56 | `V` |
| 74 | 0x4A | `J` | | 87 | 0x57 | `W` |
| 75 | 0x4B | `K` | | 88 | 0x58 | `X` |
| 76 | 0x4C | `L` | | 89 | 0x59 | `Y` |
| 77 | 0x4D | `M` | | 90 | 0x5A | `Z` |

#### Sonderzeichen (0x5B - 0x60)

| Dez | Hex | Zeichen | Name |
|-----|-----|---------|------|
| 91 | 0x5B | `[` | Left Square Bracket |
| 92 | 0x5C | `\` | Reverse Solidus / Backslash |
| 93 | 0x5D | `]` | Right Square Bracket |
| 94 | 0x5E | `^` | Circumflex Accent / Caret |
| 95 | 0x5F | `_` | Low Line / Underscore |
| 96 | 0x60 | `` ` `` | Grave Accent / Backtick |

#### Kleinbuchstaben (0x61 - 0x7A)

| Dez | Hex | Zeichen | | Dez | Hex | Zeichen |
|-----|-----|---------|---|-----|-----|---------|
| 97 | 0x61 | `a` | | 110 | 0x6E | `n` |
| 98 | 0x62 | `b` | | 111 | 0x6F | `o` |
| 99 | 0x63 | `c` | | 112 | 0x70 | `p` |
| 100 | 0x64 | `d` | | 113 | 0x71 | `q` |
| 101 | 0x65 | `e` | | 114 | 0x72 | `r` |
| 102 | 0x66 | `f` | | 115 | 0x73 | `s` |
| 103 | 0x67 | `g` | | 116 | 0x74 | `t` |
| 104 | 0x68 | `h` | | 117 | 0x75 | `u` |
| 105 | 0x69 | `i` | | 118 | 0x76 | `v` |
| 106 | 0x6A | `j` | | 119 | 0x77 | `w` |
| 107 | 0x6B | `k` | | 120 | 0x78 | `x` |
| 108 | 0x6C | `l` | | 121 | 0x79 | `y` |
| 109 | 0x6D | `m` | | 122 | 0x7A | `z` |

#### Sonderzeichen und DEL (0x7B - 0x7F)

| Dez | Hex | Zeichen | Name |
|-----|-----|---------|------|
| 123 | 0x7B | `{` | Left Curly Bracket |
| 124 | 0x7C | `\|` | Vertical Line / Pipe |
| 125 | 0x7D | `}` | Right Curly Bracket |
| 126 | 0x7E | `~` | Tilde |
| 127 | 0x7F | (DEL) | Delete |

---

## Kompakte ASCII-Tabelle

```
     0   1   2   3   4   5   6   7   8   9   A   B   C   D   E   F
   +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
 0 |NUL|SOH|STX|ETX|EOT|ENQ|ACK|BEL|BS |HT |LF |VT |FF |CR |SO |SI |
   +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
 1 |DLE|DC1|DC2|DC3|DC4|NAK|SYN|ETB|CAN|EM |SUB|ESC|FS |GS |RS |US |
   +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
 2 |SP | ! | " | # | $ | % | & | ' | ( | ) | * | + | , | - | . | / |
   +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
 3 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | : | ; | < | = | > | ? |
   +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
 4 | @ | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O |
   +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
 5 | P | Q | R | S | T | U | V | W | X | Y | Z | [ | \ | ] | ^ | _ |
   +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
 6 | ` | a | b | c | d | e | f | g | h | i | j | k | l | m | n | o |
   +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
 7 | p | q | r | s | t | u | v | w | x | y | z | { | | | } | ~ |DEL|
   +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+

Zeile = Erste Hex-Ziffer, Spalte = Zweite Hex-Ziffer
Beispiel: 'A' = Zeile 4, Spalte 1 = 0x41 = 65 dezimal
```

---

## Verhältnis zu UTF-8 und Unicode

### Unicode - Der universelle Zeichensatz

**Unicode** wurde entwickelt, um alle Schriftsysteme der Welt in einem einheitlichen Standard abzubilden:

| Aspekt | ASCII | Unicode |
|--------|-------|---------|
| Bits | 7 | 21 (theoretisch) |
| Zeichen | 128 | >149.000 (Stand 2024) |
| Sprachen | Englisch | Alle |
| Symbole | Minimal | Emojis, Mathematik, etc. |

### UTF-8 - Die clevere Kodierung

**UTF-8** (8-bit Unicode Transformation Format) ist eine **variable-Längen-Kodierung** für Unicode:

```
┌────────────────────────────────────────────────────────────────────┐
│                    UTF-8 Kodierungsschema                          │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  Codepoint-Bereich      │  Bytes  │  Bitmuster                     │
│  ───────────────────────┼─────────┼───────────────────────────     │
│  U+0000 - U+007F        │    1    │  0xxxxxxx                      │
│  (ASCII!)               │         │  (identisch mit ASCII!)        │
│  ───────────────────────┼─────────┼───────────────────────────     │
│  U+0080 - U+07FF        │    2    │  110xxxxx 10xxxxxx             │
│  (Latin Extended, etc.) │         │                                │
│  ───────────────────────┼─────────┼───────────────────────────     │
│  U+0800 - U+FFFF        │    3    │  1110xxxx 10xxxxxx 10xxxxxx    │
│  (CJK, etc.)            │         │                                │
│  ───────────────────────┼─────────┼───────────────────────────     │
│  U+10000 - U+10FFFF     │    4    │  11110xxx 10xx... 10xx... 10xx │
│  (Emojis, historic)     │         │                                │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

> [!important] ASCII-Kompatibilität
> **UTF-8 ist vollständig abwärtskompatibel mit ASCII!**
> - Jede gültige ASCII-Datei ist automatisch eine gültige UTF-8-Datei
> - Die ersten 128 Zeichen (0x00-0x7F) sind identisch
> - ASCII-Programme können UTF-8-Text verarbeiten (solange nur ASCII-Zeichen vorkommen)

### Beispiele für UTF-8-Kodierung

| Zeichen | Unicode | UTF-8 (hex) | UTF-8 (binär) |
|---------|---------|-------------|---------------|
| `A` | U+0041 | 41 | 01000001 |
| `ä` | U+00E4 | C3 A4 | 11000011 10100100 |
| `€` | U+20AC | E2 82 AC | 11100010 10000010 10101100 |
| `😀` | U+1F600 | F0 9F 98 80 | 11110000 10011111 10011000 10000000 |

---

## Wichtige ASCII-Escape-Sequenzen

In Programmiersprachen werden Steuerzeichen oft als Escape-Sequenzen dargestellt:

| Sequenz | ASCII | Dez | Name | Verwendung |
|---------|-------|-----|------|------------|
| `\0` | NUL | 0 | Null | String-Terminator in C |
| `\a` | BEL | 7 | Bell | Signalton |
| `\b` | BS | 8 | Backspace | Cursor zurück |
| `\t` | HT | 9 | Tab | Horizontaler Tabulator |
| `\n` | LF | 10 | Newline | Zeilenumbruch (Unix) |
| `\v` | VT | 11 | Vertical Tab | Vertikaler Tabulator |
| `\f` | FF | 12 | Form Feed | Seitenumbruch |
| `\r` | CR | 13 | Carriage Return | Wagenrücklauf |
| `\e` | ESC | 27 | Escape | Terminal-Sequenzen |
| `\\` | \ | 92 | Backslash | Backslash-Zeichen |
| `\'` | ' | 39 | Single Quote | Apostroph |
| `\"` | " | 34 | Double Quote | Anführungszeichen |

---

## ASCII-Art für Diagramme

Für technische Dokumentation werden oft Box-Drawing-Zeichen verwendet. Diese sind **nicht** Teil des originalen ASCII, sondern stammen aus Code Page 437 oder Unicode:

### Nur-ASCII Box-Drawing

```
Ecken und Linien (reines ASCII):
+---+     +---------+
|   |     |  Box    |
+---+     +---------+

Pfeile:
->  <-  ^  v  -->  <--  |  ||

Baumstrukturen:
+-- Ordner1
|   +-- Datei1
|   +-- Datei2
+-- Ordner2
    +-- Datei3
```

### Unicode Box-Drawing (UTF-8)

```
┌───┬───┐   ╔═══╦═══╗   ╭───╮
│   │   │   ║   ║   ║   │   │
├───┼───┤   ╠═══╬═══╣   │   │
│   │   │   ║   ║   ║   ╰───╯
└───┴───┘   ╚═══╩═══╝

Pfeile: → ← ↑ ↓ ↔ ↕ ⇒ ⇐ ⇑ ⇓
```

---

## Quellen

- ANSI X3.4-1986: American National Standard for Information Systems - Coded Character Sets - 7-Bit American National Standard Code for Information Interchange (7-Bit ASCII)
- ISO/IEC 646:1991: Information technology - ISO 7-bit coded character set for information interchange
- RFC 20: ASCII format for Network Interchange (1969)
- The Unicode Standard, Version 15.1 (2024)
- [ASCII - Wikipedia](https://en.wikipedia.org/wiki/ASCII)
- [UTF-8 - Wikipedia](https://en.wikipedia.org/wiki/UTF-8)
- [Unicode Consortium](https://home.unicode.org/)
