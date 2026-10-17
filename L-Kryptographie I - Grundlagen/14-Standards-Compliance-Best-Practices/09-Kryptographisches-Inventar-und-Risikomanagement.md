---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - standards
---

# Kryptographisches Inventar und Risikomanagement

> [!info] **Lernziele**
> - Zweck eines kryptographischen Inventars verstehen
> - Den Bezug zum Risikomanagement herstellen
> - Die Bedeutung für PQC-Migration und Crypto-Agility einordnen

---

## Inhalt

### Das kryptographische Inventar

Ein **kryptographisches Inventar (Cryptographic Bill of Materials, CBOM)** ist eine vollständige Bestandsaufnahme aller in einer Organisation eingesetzten Kryptographie:

- **Wo** wird Kryptographie verwendet (Anwendungen, Dienste, Protokolle)?
- **Welche** Algorithmen, Schlüssellängen und Bibliotheken?
- **Welche** Zertifikate und Schlüssel, mit welchen Laufzeiten?

> [!tip] **Man kann nur verwalten, was man kennt**
> Ohne Inventar ist weder gezieltes Risikomanagement noch eine geordnete Migration möglich. Gerade für die **PQC-Umstellung** (→ [[10-Migration-zu-quantenresistenten-Systemen]]) ist das Inventar der unverzichtbare erste Schritt.

### Verbindung zum Risikomanagement

Das Inventar ist die Grundlage, um **Risiken** zu bewerten:

```
Inventar  →  Risikobewertung  →  Maßnahmen  →  Überwachung
(was ist da?) (was ist gefährdet?) (was tun?)   (wirkt es?)
```

Typische Risikofragen:

- Welche Systeme nutzen **veraltete** Verfahren (MD5, SHA-1, DES, TLS 1.0)?
- Wo laufen **Zertifikate** bald ab oder sind zu schwach?
- Welche Daten sind **langlebig** und damit durch „harvest now, decrypt later" gefährdet (→ [[03-Auswirkungen-auf-RSA-und-ECC]])?

### Kontinuierlicher Prozess

> [!warning] **Prüfungsrelevant**
> Krypto-Inventar und Risikomanagement sind **kein Einmalprojekt**, sondern ein **fortlaufender** Prozess: Neue Systeme kommen hinzu, Standards ändern sich, Prognosezeiträume (→ [[02-BSI-TR-02102]]) laufen ab. Das Inventar muss aktuell gehalten und regelmäßig gegen die geltende Crypto Policy (→ [[08-Kryptographische-Richtlinien-in-Unternehmen]]) geprüft werden.

### Werkzeuge

Scanner und CBOM-Werkzeuge können TLS-Konfigurationen, Zertifikate und teils Codeabhängigkeiten automatisch erfassen und so das Inventar unterstützen.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Das Krypto-Inventar (CBOM) erfasst alle eingesetzten Verfahren, Schlüssel und Zertifikate
> - Es ist die Grundlage für Risikobewertung, Richtlinien-Prüfung und Migration
> - Besonders kritisch als erster Schritt der PQC-Migration
> - Fortlaufender Prozess, kein Einmalprojekt – regelmäßig aktualisieren

---

## Übungen

1. Was erfasst ein kryptographisches Inventar?
2. Wie hängen Inventar und Risikomanagement zusammen?
3. Warum ist das Inventar der erste Schritt jeder PQC-Migration?

---

← [[08-Kryptographische-Richtlinien-in-Unternehmen|← Zurück]] | [[00-Standards-Index|Übersicht]] | [[00-Uebungen-Index|Nächstes Modul →]]
