---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - signaturen
---

# Dokumentensignaturen

> [!info] **Lernziele**
> - Anwendungsformen digitaler Dokumentensignaturen kennen
> - Rechtliche Signaturklassen (eIDAS) einordnen
> - Typische Formate und Einsatzgebiete verstehen

---

## Inhalt

### Von der Technik zur Anwendung

Dokumentensignaturen wenden die bisher behandelten Signaturverfahren konkret auf Dateien an – von PDFs über Verträge bis zu Software. Ziel: belegen, **wer** ein Dokument erstellt/freigegeben hat und dass es **unverändert** ist.

### Verbreitete Formate

| Format | Einsatz |
|--------|---------|
| **PAdES** | PDF-Signaturen (Verträge, Rechnungen) |
| **XAdES** | XML-Dokumente |
| **CAdES** | allgemeine Daten (CMS-basiert) |
| **S/MIME** | signierte E-Mails |
| **Code Signing** | signierte Software/Treiber |

Diese „AdES"-Formate (Advanced Electronic Signatures) regeln, wie Signatur, Zertifikat und Zeitstempel in das Dokument eingebettet werden.

### Rechtliche Einordnung (eIDAS)

Die EU-Verordnung **eIDAS** definiert drei Stufen (Details → Modul 14):

| Stufe | Bedeutung |
|-------|-----------|
| **Einfache** elektronische Signatur | geringste Anforderungen, geringe Beweiskraft |
| **Fortgeschrittene** (AES) | eindeutig dem Unterzeichner zuordenbar, Manipulation erkennbar |
| **Qualifizierte** (QES) | höchste Stufe, der handschriftlichen Unterschrift rechtlich gleichgestellt |

Eine **qualifizierte** Signatur erfordert ein qualifiziertes Zertifikat und eine sichere Signaturerstellungseinheit (z. B. Smartcard/HSM).

### Code Signing

Ein wichtiger Sonderfall: **Code Signing** signiert ausführbare Programme. Betriebssysteme prüfen die Signatur, um Herkunft und Unversehrtheit sicherzustellen und Warnungen vor unsignierter Software anzuzeigen.

> [!tip] **Langfristige Gültigkeit**
> Dokumentensignaturen sollen oft über Jahre gültig bleiben – länger als die Lebensdauer von Zertifikat und Algorithmus. Dafür sind Zeitstempel und erneuerbare Validierung nötig (→ [[08-Zeitstempel-und-langfristige-Validierung]]).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Dokumentensignaturen wenden Signaturverfahren auf PDFs, XML, E-Mail, Software an
> - Formate: PAdES, XAdES, CAdES, S/MIME, Code Signing
> - eIDAS stuft in einfache, fortgeschrittene und qualifizierte Signaturen ein
> - Qualifizierte Signatur ist der handschriftlichen rechtlich gleichgestellt

---

## Übungen

1. Welches Signaturformat wird für PDF-Dokumente verwendet?
2. Nennen Sie die drei eIDAS-Signaturstufen.
3. Wozu dient Code Signing?

---

← [[06-Digitale-Zertifikate|← Zurück]] | [[00-Signaturen-Index|Übersicht]] | [[08-Zeitstempel-und-langfristige-Validierung|Weiter →]]
