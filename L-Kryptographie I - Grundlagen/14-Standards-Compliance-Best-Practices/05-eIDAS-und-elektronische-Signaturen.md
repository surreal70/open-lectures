---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - standards
---

# eIDAS und elektronische Signaturen

> [!info] **Lernziele**
> - eIDAS als rechtlichen Rahmen einordnen
> - Die drei Signaturstufen und ihre Rechtswirkung kennen
> - Den Zusammenhang zu den technischen Signaturverfahren herstellen

---

## Inhalt

### Was ist eIDAS?

**eIDAS** (electronic IDentification, Authentication and trust Services) ist die EU-Verordnung, die **elektronische Identifizierung und Vertrauensdienste** europaweit rechtlich regelt – insbesondere elektronische Signaturen, Siegel, Zeitstempel und Zertifikate. Sie schafft einen einheitlichen Rechtsrahmen im Binnenmarkt.

### Die drei Signaturstufen

| Stufe | Anforderungen | Rechtswirkung |
|-------|---------------|---------------|
| **Einfache** elektronische Signatur (EES) | keine besonderen | geringe Beweiskraft |
| **Fortgeschrittene** (FES/AES) | eindeutig dem Unterzeichner zuordenbar, Manipulation erkennbar | mittlere Beweiskraft |
| **Qualifizierte** (QES) | qualifiziertes Zertifikat + sichere Signaturerstellungseinheit | der **handschriftlichen Unterschrift gleichgestellt** |

Technisch bauen diese Stufen auf den in Modul 7 behandelten Verfahren auf (→ [[01-Grundlagen-digitaler-Signaturen]], [[07-Dokumentensignaturen]]).

### Qualifizierte Vertrauensdiensteanbieter

> [!note] **QTSP und Vertrauensliste**
> Qualifizierte Signaturen erfordern einen **qualifizierten Vertrauensdiensteanbieter (QTSP)**, der behördlich überwacht und auf einer **EU-Vertrauensliste** geführt wird. Die sichere Signaturerstellungseinheit ist typischerweise ein zertifiziertes Gerät (Smartcard/HSM, → [[06-Hardware-Security-Modules-HSM]]).

### Weitere Vertrauensdienste

eIDAS regelt neben Signaturen auch **elektronische Siegel** (für juristische Personen), **qualifizierte Zeitstempel** (→ [[08-Zeitstempel-und-langfristige-Validierung]]) und **Website-Zertifikate**.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - eIDAS ist der EU-Rechtsrahmen für elektronische Signaturen und Vertrauensdienste
> - Drei Stufen: einfach, fortgeschritten, qualifiziert (QES = handschriftlich gleichgestellt)
> - QES erfordert qualifiziertes Zertifikat und sichere Signaturerstellungseinheit (QTSP)
> - Baut technisch auf den Signaturverfahren aus Modul 7 auf

---

## Übungen

1. Welche drei Signaturstufen definiert eIDAS?
2. Welche Stufe ist der handschriftlichen Unterschrift rechtlich gleichgestellt?
3. Was ist ein QTSP und welche Rolle spielt er?

---

← [[04-ISO-IEC-27001-und-Kryptographie|← Zurück]] | [[00-Standards-Index|Übersicht]] | [[06-DSGVO-und-Verschluesselung|Weiter →]]
