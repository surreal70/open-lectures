---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - pki
---

# Zertifikatsketten und Vertrauensmodelle

> [!info] **Lernziele**
> - Den Aufbau und die Prüfung einer Zertifikatskette verstehen
> - Verschiedene Vertrauensmodelle unterscheiden
> - Die Grenzen des hierarchischen Modells einordnen

---

## Inhalt

### Die Zertifikatskette

Vertrauen wird über eine **Kette** vom Endzertifikat bis zu einem vertrauenswürdigen Anker aufgebaut:

```
Endnutzer-Zertifikat (example.com)
   ↑ signiert von
Intermediate-CA
   ↑ signiert von
Root-CA  ← im System als vertrauenswürdig hinterlegt
```

### Prüfung der Kette (Path Validation)

Ein Client prüft bei jedem Glied:

1. **Signatur:** Ist das Zertifikat vom angegebenen Aussteller korrekt signiert?
2. **Gültigkeit:** Liegt die aktuelle Zeit im Gültigkeitszeitraum?
3. **Sperrstatus:** Ist das Zertifikat nicht gesperrt (CRL/OCSP, → Kapitel 6–7)?
4. **Constraints:** Darf das Zwischenzertifikat überhaupt ausstellen (Basic Constraints, Path Length)?
5. **Anker:** Endet die Kette bei einer vertrauenswürdigen Root?

Erst wenn **alle** Glieder bestehen, gilt das Endzertifikat als vertrauenswürdig.

### Vertrauensmodelle

| Modell | Beschreibung | Beispiel |
|--------|--------------|----------|
| **Hierarchisch** | Baum mit Root-CA an der Spitze | TLS/Web-PKI |
| **Web of Trust** | dezentral, Nutzer signieren sich gegenseitig | PGP/GPG |
| **Trust on First Use (TOFU)** | erster Schlüssel wird akzeptiert und gemerkt | SSH |

### Grenzen des hierarchischen Modells

> [!danger] **Jede vertrauenswürdige CA kann jede Domain zertifizieren**
> Im Web-PKI-Modell vertraut der Browser hunderten Root-CAs – und **jede** davon könnte theoretisch ein Zertifikat für jede beliebige Domain ausstellen. Eine einzige kompromittierte oder bösartige CA gefährdet somit alle. Gegenmaßnahmen sind **Certificate Transparency** (→ [[08-Certificate-Transparency]]) und Techniken wie CAA-DNS-Records.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Vertrauen entsteht über eine Kette bis zu einer hinterlegten Root-CA
> - Pfadprüfung: Signatur, Gültigkeit, Sperrstatus, Constraints, Vertrauensanker
> - Modelle: hierarchisch (Web-PKI), Web of Trust (PGP), TOFU (SSH)
> - Schwäche der Hierarchie: jede vertraute CA kann jede Domain zertifizieren → CT als Gegenmittel

---

## Übungen

1. Welche Schritte umfasst die Prüfung einer Zertifikatskette?
2. Vergleichen Sie hierarchisches Modell und Web of Trust.
3. Was ist die zentrale Schwäche des Web-PKI-Vertrauensmodells?

---

← [[04-X509-Zertifikate|← Zurück]] | [[00-PKI-Index|Übersicht]] | [[06-Certificate-Revocation-Lists-CRL|Weiter →]]
