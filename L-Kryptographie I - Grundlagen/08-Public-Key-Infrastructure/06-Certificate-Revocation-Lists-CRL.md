---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - pki
---

# Certificate Revocation Lists CRL

> [!info] **Lernziele**
> - Zweck der Zertifikatssperrung verstehen
> - Aufbau und Funktion einer CRL kennen
> - Vor- und Nachteile von CRLs einordnen

---

## Inhalt

### Warum Sperrung?

Ein Zertifikat ist bis zum Ablaufdatum gültig – aber manchmal muss es **vorzeitig** für ungültig erklärt werden:

- Der private Schlüssel wurde kompromittiert.
- Die zugrunde liegenden Angaben stimmen nicht mehr (z. B. Domain-Inhaber gewechselt).
- Die CA hat fehlerhaft ausgestellt.

Dafür gibt es die **Sperrung (Revocation)**.

### Certificate Revocation List (CRL)

Eine **CRL** ist eine von der CA signierte Liste der **Seriennummern gesperrter Zertifikate** nebst Sperrzeitpunkt und -grund. Clients laden sie herunter und prüfen, ob ein Zertifikat darauf steht.

```
CRL = { Aussteller, Ausstellungszeit, nächste Aktualisierung,
        [ (Seriennummer, Sperrdatum, Grund), ... ] }
      + Signatur der CA
```

### Vor- und Nachteile

| Vorteil | Nachteil |
|---------|----------|
| einfach, signiert, offline prüfbar | Listen werden **groß** |
| etabliert, breit unterstützt | **Aktualität** begrenzt (Cache bis „next update") |
| | Download-Last und Latenz |

> [!note] **Das Grundproblem der Sperrprüfung**
> CRLs können sehr groß und veraltet sein. Lädt ein Client die CRL nicht (Netzfehler), stellt sich die Frage: ablehnen (**hard-fail**, sicherer, aber störanfällig) oder akzeptieren (**soft-fail**, verfügbarer, aber unsicher)? Viele Clients nutzen soft-fail – ein bekanntes Sicherheitsdilemma. OCSP (→ [[07-Online-Certificate-Status-Protocol-OCSP]]) adressiert die Aktualität.

### Moderne Entwicklung

Wegen der Schwächen setzen Browser zunehmend auf vorverarbeitete, gebündelte Sperrlisten (z. B. CRLite, OneCRL), die die CA-CRLs kompakt im Client vorhalten.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Sperrung macht Zertifikate vor Ablauf ungültig (Schlüsselkompromittierung etc.)
> - Eine CRL ist eine signierte Liste gesperrter Seriennummern
> - Nachteile: Größe, begrenzte Aktualität, Download-Last
> - Hard-fail vs. soft-fail ist ein grundlegendes Sperrprüfungs-Dilemma

---

## Übungen

1. Nennen Sie zwei Gründe für die vorzeitige Sperrung eines Zertifikats.
2. Was enthält eine CRL und wer signiert sie?
3. Erklären Sie den Unterschied zwischen hard-fail und soft-fail.

---

← [[05-Zertifikatsketten-und-Vertrauensmodelle|← Zurück]] | [[00-PKI-Index|Übersicht]] | [[07-Online-Certificate-Status-Protocol-OCSP|Weiter →]]
