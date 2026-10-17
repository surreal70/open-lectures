---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - pki
---

# Online Certificate Status Protocol OCSP

> [!info] **Lernziele**
> - OCSP als Online-Sperrprüfung verstehen
> - Den Datenschutz-Nachteil und OCSP-Stapling kennen
> - OCSP von CRL abgrenzen

---

## Inhalt

### Von der Liste zur Einzelabfrage

Statt eine ganze Sperrliste herunterzuladen (CRL, → [[06-Certificate-Revocation-Lists-CRL]]), fragt das **Online Certificate Status Protocol (OCSP)** den Status **eines einzelnen** Zertifikats direkt bei der CA (genauer: einem OCSP-Responder) ab.

```
Client → OCSP-Responder:  "Status von Zertifikat Seriennummer X?"
OCSP-Responder → Client:  signierte Antwort: good / revoked / unknown
```

Vorteil: aktueller und schlanker als eine große CRL.

### Der Datenschutz-Nachteil

> [!danger] **OCSP verrät das Surfverhalten**
> Bei klassischem OCSP fragt der **Client** bei jedem Verbindungsaufbau die CA nach dem Zertifikatsstatus. Damit erfährt die CA, **welche Websites** der Nutzer wann besucht – ein Datenschutzproblem. Zudem entstehen Latenz und Abhängigkeit von der Verfügbarkeit des Responders.

### OCSP-Stapling

Die Lösung ist **OCSP-Stapling**: Nicht der Client, sondern der **Server** holt regelmäßig eine signierte, zeitgestempelte OCSP-Antwort bei der CA und „heftet" sie an den TLS-Handshake an. Vorteile:

- Der Client muss die CA **nicht** selbst kontaktieren → kein Datenschutzleck, keine Zusatzlatenz.
- Die CA wird entlastet.

Mit **OCSP Must-Staple** (eine Zertifikatserweiterung) kann ein Zertifikat sogar verlangen, dass eine gültige gestapelte Antwort vorliegt – sonst wird es abgelehnt (schließt die soft-fail-Lücke).

### OCSP vs. CRL

| Merkmal | CRL | OCSP |
|---------|-----|------|
| Abfrage | ganze Liste | einzelnes Zertifikat |
| Aktualität | begrenzt (Cache) | hoch |
| Datenschutz | gut (kein Tracking) | problematisch (ohne Stapling) |
| Last | Download groß | viele Einzelabfragen |

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - OCSP prüft den Sperrstatus einzelner Zertifikate online (good/revoked/unknown)
> - Aktueller als CRL, aber klassisches OCSP verrät das Surfverhalten an die CA
> - OCSP-Stapling löst das: der Server liefert die signierte Statusantwort mit
> - OCSP Must-Staple erzwingt eine gültige gestapelte Antwort

---

## Übungen

1. Worin unterscheidet sich OCSP von einer CRL?
2. Welches Datenschutzproblem hat klassisches OCSP?
3. Wie behebt OCSP-Stapling dieses Problem?

---

← [[06-Certificate-Revocation-Lists-CRL|← Zurück]] | [[00-PKI-Index|Übersicht]] | [[08-Certificate-Transparency|Weiter →]]
