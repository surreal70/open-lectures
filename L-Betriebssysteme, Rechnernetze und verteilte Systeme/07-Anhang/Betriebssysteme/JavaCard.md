---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# Java Card

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | Smartcard-Plattform |
| **Entwickler** | Oracle (früher Sun) |
| **Erstveröffentlichung** | 1996 |
| **Aktuelle Version** | 3.1 (2019) |
| **Lizenz** | Proprietär (Spezifikation offen) |
| **Standard** | ISO 7816 kompatibel |

## Zusammenfassung

Java Card ist eine Softwareplattform, die Java-Applets auf Smartcards ausführt. Sie ermöglicht sichere, portable Anwendungen auf ressourcenbeschränkten Chipkarten und wird in SIM-Karten, BankCards und Zugangskarten weltweit eingesetzt.

### Verbreitung

- **>6 Milliarden** Java Cards im Einsatz
- Praktisch alle SIM-Karten
- Viele Bank- und Kreditkarten
- Regierungs-IDs weltweit

### Eingeschränkte JVM

Java Card verwendet eine stark reduzierte Java Virtual Machine:

| Feature | Java SE | Java Card |
|---------|---------|-----------|
| Datentypen | Alle | byte, short, boolean |
| int/long | Ja | Optional |
| Strings | Ja | Nein |
| Garbage Collection | Automatisch | Optional/Eingeschränkt |
| Threads | Ja | Nein |
| float/double | Ja | Nein |

### Architektur

```
Java Card Architektur
┌─────────────────────────────────────────┐
│          Java Card Applets              │
│    (Banking, SIM, PKI, Transport)       │
├─────────────────────────────────────────┤
│         Java Card API                   │
│  (javacard.*, javacardx.*)              │
├─────────────────────────────────────────┤
│    Java Card Runtime Environment        │
│           (JCRE)                        │
├─────────────────────────────────────────┤
│   Java Card Virtual Machine (JCVM)      │
├─────────────────────────────────────────┤
│    Native OS / Hardware                 │
│    (Crypto-Coprozessor, EEPROM)         │
└─────────────────────────────────────────┘
```

### Lebenszyklus eines Applets

1. **Entwicklung**: Java-Code schreiben
2. **Kompilierung**: javac + Converter → CAP-Datei
3. **Installation**: CAP auf Karte laden
4. **Personalisierung**: Daten/Schlüssel laden
5. **Nutzung**: APDU-Kommunikation
6. **Löschen**: Applet entfernen (optional)

### Sicherheitsfeatures

| Feature | Beschreibung |
|---------|--------------|
| **Firewall** | Applet-Isolation |
| **Atomic Operations** | Transaktionen |
| **Crypto API** | RSA, ECC, AES, DES |
| **Secure Channel** | Global Platform SCP |
| **PIN Management** | Integriert |

### GlobalPlatform

GlobalPlatform definiert Standards für:
- Card Manager (Kartenverwaltung)
- Secure Channel Protocol (SCP02, SCP03)
- Applet-Installation
- Sicherheitsdomänen

## Siehe auch

- [[TCOS]]
- [[ISO-7816]]

## Quellen

- [Oracle Java Card](https://www.oracle.com/java/technologies/javacard.html)
- [Java Card Specification](https://docs.oracle.com/en/java/javacard/)
- [GlobalPlatform](https://globalplatform.org/)
- [Wikipedia: Java Card](https://en.wikipedia.org/wiki/Java_Card)
