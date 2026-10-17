---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - architektur
  - vertiefung
---

# Enterprise Kryptographie-Architektur

> [!info] **Lernziele**
> - Kryptographie auf Unternehmensebene ganzheitlich betrachten
> - Governance, Betrieb und Technik zusammenführen
> - Das Wissen des gesamten Kurses integrieren

---

## Inhalt

### Kryptographie als Unternehmensfunktion

Auf Unternehmensebene ist Kryptographie keine Einzelmaßnahme, sondern eine **durchgängige Funktion**, die Technik, Prozesse und Organisation verbindet. Dieses Abschlusskapitel führt die Fäden des gesamten Kurses zusammen.

### Die Säulen einer Enterprise-Krypto-Architektur

| Säule | Inhalt | Verweis |
|-------|--------|---------|
| **Governance** | Crypto Policy, Rollen, Verantwortlichkeiten | [[08-Kryptographische-Richtlinien-in-Unternehmen]] |
| **Standards/Compliance** | NIST, BSI, FIPS, DSGVO, eIDAS | Modul 14 |
| **Schlüsselmanagement** | zentrales KMS/HSM, Rotation, Lifecycle | Modul 10 |
| **Inventar & Risiko** | CBOM, Risikobewertung | [[09-Kryptographisches-Inventar-und-Risikomanagement]] |
| **Crypto-Agility** | austauschbare Verfahren, PQC-Bereitschaft | [[03-Crypto-Agility-Design-Patterns]], Modul 13 |
| **Betrieb** | Monitoring, Incident Response, Audits | Modul 19 |

### Zentralisierung vs. Föderation

> [!tip] **Zentrale Dienste, dezentrale Nutzung**
> Große Organisationen bündeln Kryptographie oft in **zentralen Diensten** (KMS, PKI, Secret-Management, Service Mesh), die von vielen Teams genutzt werden. Das sichert einheitliche Policy, zentrale Rotation und Crypto-Agility – während die einzelnen Anwendungen die Dienste nur **konsumieren** und nicht selbst Krypto implementieren (→ [[01-Kryptographische-APIs-und-Libraries]]).

### Lebenszyklus und kontinuierliche Verbesserung

Eine Enterprise-Architektur ist **nie fertig**:

```
Inventar → Risikobewertung → Policy → Umsetzung
       → Monitoring/Audit → Anpassung (neue Bedrohungen/Standards) → ...
```

Aktuell treibt vor allem die **PQC-Migration** (→ Modul 13) diesen Zyklus.

### Zusammenführung des Kurses

> [!example] **Der rote Faden**
> Von den Grundlagen (Schutzziele, Kerckhoffs) über Verfahren (symmetrisch, asymmetrisch, Hashes, Signaturen), Infrastruktur (PKI, Protokolle, Schlüsselmanagement), Praxis und Angriffe bis zu Zukunftsthemen (PQC, ZKP) und sicherer Entwicklung – eine Enterprise-Architektur **integriert** all diese Bausteine zu einem konsistenten, überprüfbaren Ganzen.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Enterprise-Kryptographie verbindet Governance, Standards, Schlüsselmanagement, Inventar, Agility und Betrieb
> - Zentrale Krypto-Dienste (KMS, PKI, Secret-Management) mit dezentraler Nutzung
> - Kontinuierlicher Verbesserungszyklus; aktuell PQC-getrieben
> - Integriert alle Bausteine des Kurses zu einem konsistenten Ganzen

---

## Übungen

1. Nennen Sie die Säulen einer Enterprise-Krypto-Architektur.
2. Warum werden Krypto-Funktionen oft zentralisiert?
3. Skizzieren Sie den kontinuierlichen Verbesserungszyklus.

---

← [[06-Kryptographie-in-Microservices|← Zurück]] | [[00-Architektur-Index|Übersicht]] | [[00-Meta-Index|Zurück zur Gesamtübersicht]]
