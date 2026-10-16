---
title: "Kryptographie – Grundlagen der Verschlüsselung"
created: 2026-10-13
modified: 2026-10-13
type: lecture
tags:
  - lf09
  - kryptographie
  - verschluesselung
  - sicherheit
source: proTirone (CC-BY-4.0)
---

# Kryptographie – Grundlagen der Verschlüsselung

> [!info] Lernziele
> - Grundbegriffe der Kryptographie verstehen
> - Symmetrische und asymmetrische Verfahren unterscheiden
> - Hashfunktionen und digitale Signaturen erklären
> - TLS/SSL-Handshake nachvollziehen

## Grundbegriffe

### Definitionen

| Begriff | Definition |
|---------|------------|
| **Verschlüsselung** | Umwandlung von Klartext in Geheimtext (Chiffrat) |
| **Entschlüsselung** | Systematische Umkehr mit Kenntnis des Schlüssels |
| **Entzifferung** | Enträtselung ohne Kenntnis des Schlüssels |
| **Kryptologie** | Wissenschaft von der Verschlüsselung (Oberbegriff) |
| **Kryptographie** | Wissenschaft vom Erzeugen gut verschlüsselter Texte |
| **Kryptoanalyse** | Wissenschaft von der Entzifferung |

### Zielvorgabe

> [!important] Anforderungen an gute Verschlüsselung
> - Ver- und Entschlüsselung muss **einfach** sein, wenn der Schlüssel bekannt ist
> - Ohne Schlüssel soll Entschlüsselung **nicht möglich** sein – selbst mit beträchtlichen Ressourcen oder in Kenntnis des Verfahrens

### Beispiel: Caesar-Verschlüsselung

```
Klartext:  DAS GEHEIMNIS
Schlüssel: 3 (Verschiebung um 3 Buchstaben)
Chiffrat:  GDV JHKHLPQLV
```

> [!warning] Schwäche
> Caesar-Verschlüsselung erfüllt die Zielvorgabe NICHT: Entzifferung durch Brute-Force ist trivial (nur 26 mögliche Schlüssel).

## Symmetrische Verschlüsselung

### Prinzip

Verwendet zur **Ver- und Entschlüsselung denselben Schlüssel**.

```
┌────────┐     ┌──────────┐     ┌────────────┐     ┌──────────┐     ┌────────┐
│Klartext│────▶│Verschlüs-│────▶│  Chiffrat  │────▶│Entschlüs-│────▶│Klartext│
└────────┘     │  selung  │     └────────────┘     │  selung  │     └────────┘
               └────┬─────┘                        └────┬─────┘
                    │                                   │
                    └───────────┬───────────────────────┘
                                │
                         ┌──────┴──────┐
                         │  Schlüssel  │
                         └─────────────┘
```

### Verfahrenstypen

| Typ | Beschreibung |
|-----|--------------|
| **Substitution** | Zeichen werden ersetzt (z.B. Caesar) |
| **Transposition** | Zeichen werden umgeordnet |
| **Stromverschlüsselung** | Zeichen einzeln nacheinander verschlüsselt |
| **Blockverschlüsselung** | Klartext in Blöcke aufgeteilt |

### Moderne Verfahren

| Verfahren | Beschreibung | Status |
|-----------|--------------|--------|
| **RC4** | Stromchiffre, verarbeitet Bitstrom | ⚠️ Schwachstellen bekannt |
| **AES** | Advanced Encryption Standard (1998), 128/192/256-Bit Schlüssel, 128-Bit Blöcke | ✅ Gilt als sicher |
| **3DES** | Triple DES, dreifache DES-Anwendung | ⚠️ Veraltet |

### Vor- und Nachteile

| Vorteil | Nachteil |
|---------|----------|
| Schnellere Berechnung | Schlüssel muss mehreren bekannt sein |
| Einfache Implementierung | Schlüsselaustausch problematisch |

## Asymmetrische Verschlüsselung

### Prinzip (Public-Key-Kryptographie)

Verwendet **zwei verschiedene Schlüssel**:
- **Öffentlicher Schlüssel** (Public Key): zum Verschlüsseln, wird weitergegeben
- **Privater Schlüssel** (Private Key): zum Entschlüsseln, wird NICHT weitergegeben

```
┌────────┐     ┌──────────┐     ┌────────────┐     ┌──────────┐     ┌────────┐
│Klartext│────▶│Verschlüs-│────▶│  Chiffrat  │────▶│Entschlüs-│────▶│Klartext│
└────────┘     │  selung  │     └────────────┘     │  selung  │     └────────┘
               └────┬─────┘                        └────┬─────┘
                    │                                   │
             ┌──────┴──────┐                    ┌───────┴───────┐
             │Public Key   │                    │ Private Key   │
             │(öffentlich) │                    │ (geheim)      │
             └─────────────┘                    └───────────────┘
```

### Einwegfunktionen

Die Sicherheit basiert auf **Einwegfunktionen**:
- Einfach zu berechnen in eine Richtung
- Sehr schwer umzukehren

**Beispiele:**
- Modulo-Division
- Primfaktorzerlegung großer Zahlen

### RSA-Algorithmus

- 1977 erfunden von **R**ivest, **S**hamir, **A**dleman
- Basiert auf der Schwierigkeit, große Zahlen in Primfaktoren zu zerlegen
- Schlüssellängen: 2048, 3072, 4096 Bit

### Vor- und Nachteile

| Vorteil | Nachteil |
|---------|----------|
| Schlüsselaustausch über unsichere Netze möglich | Erhöhte Rechenleistung |
| Keine Vorab-Vereinbarung nötig | RSA ~1000× langsamer als AES |

## Hybride Verschlüsselung

Kombiniert das Beste aus beiden Welten:

1. **Asymmetrisch**: Austausch eines temporären Sitzungsschlüssels
2. **Symmetrisch**: Eigentliche Datenverschlüsselung mit dem Sitzungsschlüssel

> [!tip] Praxisbeispiel
> TLS/HTTPS verwendet hybride Verschlüsselung: RSA für den Schlüsselaustausch, AES für die Datenübertragung.

## Hashverfahren

### Definition

Eine **Hashfunktion** bildet Daten variabler Länge auf einen Wert fester Länge ab.

### Eigenschaften

- Hashwert sollte für jeden Input **eineindeutig** sein
- Kleine Inputänderung → komplett anderer Hash
- **Kollisionsresistenz**: Schwer, zwei Inputs mit gleichem Hash zu finden

### Verfahren

| Verfahren | Ausgabelänge | Status |
|-----------|--------------|--------|
| **MD5** | 128 Bit | ⚠️ Unsicher (Kollisionen möglich) |
| **SHA-1** | 160 Bit | ⚠️ Unsicher |
| **SHA-256** | 256 Bit | ✅ Sicher |
| **SHA-3** | 224-512 Bit | ✅ Sicher |

### Anwendung

```bash
# Linux: SHA-256 Hash einer Datei
sha256sum datei.txt

# Linux: SHA-256 eines Strings
echo "Hello world" | sha256sum

# Windows PowerShell
Get-FileHash datei.txt -Algorithm SHA256
```

## Digitale Signatur

### Prinzip

Nutzt asymmetrische Verschlüsselung **umgekehrt**:
- Privater Schlüssel **ver**schlüsselt den Hash
- Öffentlicher Schlüssel **ent**schlüsselt zur Verifikation

### Ablauf

```
SENDER                                    EMPFÄNGER
┌─────────┐                               ┌─────────┐
│Dokument │                               │Dokument │
└────┬────┘                               └────┬────┘
     │                                         │
     ▼                                         ▼
┌─────────┐                               ┌─────────┐
│  Hash   │                               │  Hash   │
│berechnen│                               │berechnen│
└────┬────┘                               └────┬────┘
     │                                         │
     ▼                                         ▼
┌─────────────┐                           ┌─────────────┐
│Hash mit     │                           │Signatur mit │
│Private Key  │─────── Signatur ─────────▶│Public Key   │
│verschlüsseln│                           │entschlüsseln│
└─────────────┘                           └──────┬──────┘
                                                 │
                                          Vergleich: ✓ oder ✗
```

## TLS/SSL in Netzwerken

### Verschlüsselungsarten

| Art | Beschreibung |
|-----|--------------|
| **Leitungsverschlüsselung** | Nachricht nur für den Nachbarrechner verschlüsselt |
| **Ende-zu-Ende** | Nachricht vom Absender bis zum Empfänger verschlüsselt |

### TLS (Transport Layer Security)

- Verschlüsselung zwischen Layer VII und Layer IV
- Versionen: TLS 1.0 (1999), 1.1 (2006), 1.2 (2008), 1.3 (2018)
- Vorgänger: SSL (Secure Sockets Layer) 1.0-3.0

### IPsec

- Arbeitet auf Layer 3 (Vermittlungsschicht)
- Verschlüsselt IP-Pakete direkt
- Kann bei NAT zu Problemen führen

---

> [!tip] Übungen
> 1. Entschlüsseln Sie: `xvd-sulydwh-gdwhq` (Caesar mit n=3)
> 2. Berechnen Sie den SHA-256 Hash von "Hello World"
> 3. Erklären Sie, warum hybride Verschlüsselung in der Praxis bevorzugt wird

## Weiterführende Links

- [BSI Datenverschlüsselung](https://www.bsi.bund.de/DE/Themen/Verbraucherinnen-und-Verbraucher/Informationen-und-Empfehlungen/Cyber-Sicherheitsempfehlungen/Daten-sichern-verschluesseln-und-loeschen/Datenverschluesselung/datenverschluesselung_node.html)
- [Studyflix: Asymmetrische Verschlüsselung](https://studyflix.de/informatik/asymmetrische-verschlusselung-1609)
- [Cloudflare: TLS erklärt](https://www.cloudflare.com/de-de/learning/ssl/transport-layer-security-tls/)

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (Karsten Reincke), lizenziert unter CC-BY-4.0.
> Inhalte wurden für das Open-Lectures-Format angepasst.
