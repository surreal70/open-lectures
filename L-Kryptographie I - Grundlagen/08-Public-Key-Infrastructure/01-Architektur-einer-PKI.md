---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - pki
---

# Architektur einer PKI

> [!info] **Lernziele**
> - Die Bestandteile und Aufgaben einer PKI verstehen
> - Das Zusammenspiel der Komponenten nachvollziehen
> - Den Lebenszyklus eines Zertifikats überblicken

---

## Inhalt

### Was ist eine PKI?

Eine **Public-Key-Infrastructure (PKI)** ist das organisatorische und technische Gerüst, das die vertrauenswürdige Ausstellung, Verwaltung und Prüfung digitaler Zertifikate ermöglicht. Sie beantwortet die zentrale Vertrauensfrage: **Gehört ein öffentlicher Schlüssel wirklich zu einer bestimmten Identität?** (→ [[06-Digitale-Zertifikate]])

### Komponenten einer PKI

| Komponente | Aufgabe |
|------------|---------|
| **CA (Certificate Authority)** | stellt Zertifikate aus und signiert sie (→ [[02-Certificate-Authorities-CA]]) |
| **RA (Registration Authority)** | prüft die Identität der Antragsteller vor der Ausstellung |
| **VA (Validation Authority)** | liefert Statusauskünfte (Sperrung) über CRL/OCSP (→ Kapitel 6–7) |
| **Repository** | speichert und verteilt Zertifikate und Sperrlisten |
| **Endnutzer / Teilnehmer** | besitzen Schlüsselpaare und Zertifikate |

### Der Zertifikatslebenszyklus

```
Antrag → Identitätsprüfung (RA) → Ausstellung (CA)
      → Verteilung/Nutzung → ggf. Sperrung → Ablauf → Erneuerung
```

Jede Phase muss abgesichert sein; besonders die **Identitätsprüfung** und der Schutz des **privaten CA-Schlüssels** sind kritisch.

### Vertrauensanker

Das Fundament jeder PKI sind die **Root-CAs**, deren Zertifikate als vertrauenswürdig vorinstalliert sind (im Betriebssystem oder Browser). Von ihnen leitet sich das gesamte Vertrauen über Zertifikatsketten ab (→ [[05-Zertifikatsketten-und-Vertrauensmodelle]]).

> [!note] **PKI ist Technik + Organisation + Prozesse**
> Eine PKI ist nicht nur Software: Richtlinien (Certificate Policy, CPS), physische Sicherheit der CA und geprüfte Abläufe sind ebenso Teil des Vertrauens. Ein technischer Fehler oder ein organisatorisches Versagen (z. B. eine kompromittierte CA) untergräbt die gesamte Infrastruktur.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - PKI schafft das Gerüst für vertrauenswürdige Zertifikate
> - Kernkomponenten: CA, RA, VA, Repository, Teilnehmer
> - Zertifikate durchlaufen einen Lebenszyklus von Antrag bis Erneuerung/Sperrung
> - Vertrauen gründet auf vorinstallierten Root-CAs; PKI umfasst Technik und Organisation

---

## Übungen

1. Welche Aufgabe hat die Registration Authority?
2. Beschreiben Sie den Lebenszyklus eines Zertifikats.
3. Warum ist der Schutz des privaten CA-Schlüssels besonders kritisch?

---

← [[00-PKI-Index|Übersicht]] | [[02-Certificate-Authorities-CA|Weiter →]]
