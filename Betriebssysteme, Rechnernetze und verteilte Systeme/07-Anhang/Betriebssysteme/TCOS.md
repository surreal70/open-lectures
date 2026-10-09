---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# TCOS (Telesec Chipcard Operating System)

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | Smartcard-Betriebssystem |
| **Entwickler** | T-Systems (Deutsche Telekom) |
| **Standard** | ISO 7816 |
| **Einsatz** | eGK, nPA, Signaturkarten |
| **Architektur** | Java Card, Native |

## Zusammenfassung

TCOS ist ein deutsches Smartcard-Betriebssystem für hochsichere Anwendungen. Es wird in der elektronischen Gesundheitskarte (eGK), dem neuen Personalausweis (nPA) und qualifizierten Signaturkarten eingesetzt.

### Einsatzgebiete

| Anwendung | Beschreibung |
|-----------|--------------|
| **eGK** | Elektronische Gesundheitskarte |
| **nPA** | Neuer Personalausweis (eID) |
| **Signaturkarten** | Qualifizierte elektronische Signatur |
| **Bankkarten** | Debit-/Kreditkarten |
| **Zugangskarten** | Gebäudesicherheit |

### Sicherheitsarchitektur

```
TCOS Schichtenmodell
┌─────────────────────────────────────────┐
│       Anwendungen (Applets)             │
│   (eGK, eID, Signatur, Banking)         │
├─────────────────────────────────────────┤
│         TCOS API / ISO 7816             │
├─────────────────────────────────────────┤
│           TCOS Kernel                   │
│  ┌──────────────────────────────────┐  │
│  │ Krypto │ File │ Access │ PIN    │  │
│  │ Engine │ Mgmt │ Control│ Mgmt   │  │
│  └──────────────────────────────────┘  │
├─────────────────────────────────────────┤
│     Hardware Security Module (HSM)      │
│         Tamper-Resistant Chip           │
└─────────────────────────────────────────┘
```

### Sicherheitsfeatures

| Feature | Beschreibung |
|---------|--------------|
| **EAL4+/5+** | Common Criteria Zertifizierung |
| **PIN-Schutz** | Mehrfache Fehlversuche → Sperrung |
| **Krypto** | RSA, ECC, AES on-chip |
| **Tamper Detection** | Angriffserkennung |
| **Secure Messaging** | Verschlüsselte Kommunikation |

### TCOS-Varianten

- **TCOS 2.0**: Native Implementierung
- **TCOS 3.0**: Erweiterte Kryptografie
- **TCOS Identity Card**: Für nPA/eID
- **TCOS Signature Card**: Qualifizierte Signaturen

### Vergleich mit JavaCard

| Aspekt | TCOS | JavaCard |
|--------|------|----------|
| Sprache | Native/Proprietär | Java |
| Flexibilität | Fest konfiguriert | Applet-basiert |
| Performance | Höher | Etwas niedriger |
| Anwendungen | Spezifisch (D) | International |

## Siehe auch

- [[JavaCard]]
- [[ISO-7816]]

## Quellen

- [T-Systems TCOS](https://www.t-systems.com/)
- [BSI Zertifizierte Produkte](https://www.bsi.bund.de/DE/Themen/Zertifizierung/zertifizierung_node.html)
- [Wikipedia: TCOS](https://de.wikipedia.org/wiki/TCOS)
