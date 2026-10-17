---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - protokolle
---

# HTTPS und Zertifikatsvalidierung

> [!info] **Lernziele**
> - HTTPS als TLS-gesichertes HTTP verstehen
> - Den Ablauf der Zertifikatsvalidierung im Browser kennen
> - Ergänzende Mechanismen wie HSTS einordnen

---

## Inhalt

### Was ist HTTPS?

**HTTPS** ist schlicht **HTTP über TLS** (→ [[01-TLS-1.2-und-TLS-1.3]]). Es schützt Webverkehr vor Mitlesen und Manipulation und stellt sicher, dass der Client wirklich mit dem erwarteten Server spricht.

### Zertifikatsvalidierung im Browser

Beim Verbindungsaufbau prüft der Browser das Serverzertifikat in mehreren Schritten:

1. **Kette aufbauen** bis zu einer vertrauenswürdigen Root-CA (→ [[05-Zertifikatsketten-und-Vertrauensmodelle]]).
2. **Signaturen** jedes Kettenglieds prüfen.
3. **Gültigkeitszeitraum** kontrollieren.
4. **Hostname-Abgleich:** Stimmt die aufgerufene Domain mit dem **SAN** des Zertifikats überein? (→ [[04-X509-Zertifikate]])
5. **Sperrstatus** prüfen (OCSP/CRL, → Modul 8).
6. **CT-Nachweis** (SCT) verlangen (→ [[08-Certificate-Transparency]]).

Schlägt ein Schritt fehl, zeigt der Browser eine Warnung und bricht ab.

### HSTS

> [!tip] **HTTP Strict Transport Security**
> Mit dem **HSTS**-Header weist ein Server den Browser an, die Seite **ausschließlich** über HTTPS aufzurufen. Das verhindert SSL-Stripping-Angriffe, bei denen ein Angreifer die Verbindung auf unverschlüsseltes HTTP herunterstuft. Mit „Preloading" ist HSTS sogar schon vor dem ersten Besuch aktiv.

### Häufige Fehlerquellen

> [!danger] **Zertifikatswarnungen nicht wegklicken**
> Warnungen wie „Zertifikat abgelaufen", „Hostname passt nicht" oder „unbekannter Aussteller" bedeuten, dass die Authentizität **nicht** gesichert ist – möglicherweise ein Man-in-the-Middle-Angriff (→ [[08-Replay-und-Man-in-the-Middle-Angriffe]]). Solche Warnungen dürfen nicht leichtfertig ignoriert werden.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - HTTPS ist HTTP über TLS – Vertraulichkeit, Integrität, Server-Authentizität
> - Validierung: Kette, Signaturen, Gültigkeit, Hostname (SAN), Sperrstatus, CT
> - HSTS erzwingt HTTPS und verhindert SSL-Stripping
> - Zertifikatswarnungen signalisieren mögliche Angriffe

---

## Übungen

1. Was bedeutet das „S" in HTTPS technisch?
2. Nennen Sie vier Schritte der Zertifikatsvalidierung im Browser.
3. Wogegen schützt HSTS?

---

← [[01-TLS-1.2-und-TLS-1.3|← Zurück]] | [[00-Protokolle-Index|Übersicht]] | [[03-SSH-und-Schluesselmanagement|Weiter →]]
