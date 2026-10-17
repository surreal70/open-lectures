---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - signaturen
---

# Digitale Zertifikate

> [!info] **Lernziele**
> - Zweck und Aufbau eines digitalen Zertifikats verstehen
> - Die Rolle der Zertifizierungsstelle (CA) einordnen
> - Den Bezug zur PKI herstellen

---

## Inhalt

### Das Problem der Schlüsselzuordnung

Public-Key-Kryptographie löst den Schlüsselaustausch, wirft aber eine neue Frage auf: **Woher weiß ich, dass ein öffentlicher Schlüssel wirklich zu einer bestimmten Person oder Website gehört?** Ein Angreifer könnte seinen eigenen Schlüssel unter fremdem Namen verbreiten (Man-in-the-Middle).

### Das digitale Zertifikat

Ein **digitales Zertifikat** bindet einen öffentlichen Schlüssel verbindlich an eine Identität. Es ist im Kern:

```
Zertifikat = { Identität (z. B. example.com),
               öffentlicher Schlüssel,
               Gültigkeitszeitraum,
               Aussteller (CA) }
           + digitale Signatur der CA darüber
```

Die **Signatur der Zertifizierungsstelle (CA)** über diese Daten macht das Zertifikat fälschungssicher: Wer der CA vertraut, kann der Zuordnung Identität ↔ Schlüssel vertrauen.

### Die Zertifizierungsstelle (CA)

Eine **CA (Certificate Authority)** ist eine vertrauenswürdige Instanz, die Identitäten prüft und Zertifikate ausstellt (signiert). Betriebssysteme und Browser liefern eine Liste vertrauenswürdiger **Root-CAs** mit. Darauf baut die gesamte **Public-Key-Infrastructure (PKI)** auf (→ Modul 8).

### X.509

Das verbreitete Zertifikatsformat ist **X.509** (→ Modul 8). Es definiert Felder wie Seriennummer, Aussteller, Subjekt, öffentlicher Schlüssel, Gültigkeit und Erweiterungen (z. B. erlaubte Verwendungszwecke).

### Vertrauenskette

Zertifikate bilden eine **Kette**: Ein Server-Zertifikat wird von einer Intermediate-CA signiert, diese von einer Root-CA. Die Prüfung folgt der Kette bis zu einer im System hinterlegten, vertrauenswürdigen Wurzel (→ Modul 8).

> [!note] **Zusammenhang Signatur ↔ Zertifikat**
> Ein Zertifikat ist selbst eine Anwendung digitaler Signaturen: Die CA **signiert** die Identitäts-Schlüssel-Zuordnung. Die Sicherheit der gesamten PKI hängt damit an der Sicherheit der zugrunde liegenden Signaturverfahren und Hashfunktionen.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Zertifikate binden einen öffentlichen Schlüssel verbindlich an eine Identität
> - Die CA signiert diese Zuordnung → fälschungssicher für alle, die der CA vertrauen
> - Standardformat ist X.509; Zertifikate bilden eine Vertrauenskette bis zur Root-CA
> - Zertifikate sind selbst eine Anwendung digitaler Signaturen (Basis der PKI)

---

## Übungen

1. Welches Problem lösen digitale Zertifikate?
2. Welche Rolle spielt die Signatur der CA?
3. Was versteht man unter einer Vertrauenskette?

---

← [[05-Signaturerstellung-und-Verifikation|← Zurück]] | [[00-Signaturen-Index|Übersicht]] | [[07-Dokumentensignaturen|Weiter →]]
