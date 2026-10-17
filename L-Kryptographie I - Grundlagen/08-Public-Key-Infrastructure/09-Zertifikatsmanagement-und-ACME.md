---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - pki
---

# Zertifikatsmanagement und ACME

> [!info] **Lernziele**
> - Herausforderungen des Zertifikatsmanagements verstehen
> - Das ACME-Protokoll und automatische Ausstellung kennen
> - Den Nutzen kurzer Laufzeiten und Automatisierung einordnen

---

## Inhalt

### Warum Zertifikatsmanagement?

In großen Umgebungen existieren hunderte oder tausende Zertifikate. Ohne systematisches Management drohen:

- **Abgelaufene Zertifikate** → Dienstausfälle (ein häufiger, vermeidbarer Vorfall).
- **Unbekannte Zertifikate** → kein Überblick, Sicherheitslücken.
- **Manueller Aufwand** → fehleranfällig und langsam.

Zertifikatsmanagement umfasst Inventarisierung, Überwachung von Ablaufdaten, Erneuerung und Sperrung.

### ACME

Das **ACME-Protokoll (Automatic Certificate Management Environment, RFC 8555)** automatisiert die Ausstellung und Erneuerung. Bekannt wurde es durch **Let's Encrypt**, das damit kostenlose, automatisierte TLS-Zertifikate bereitstellt.

Ablauf (vereinfacht):

```
1. Client fordert Zertifikat für example.com an
2. CA stellt eine Challenge (HTTP-01 oder DNS-01)
3. Client beweist Domainkontrolle (Datei ablegen / DNS-Eintrag setzen)
4. CA validiert und stellt das Zertifikat aus
5. Client installiert es – und erneuert es automatisch rechtzeitig
```

Tools wie **certbot**, **acme.sh** oder in Reverse-Proxys (Caddy, Traefik) integrierte ACME-Clients erledigen das vollständig ohne manuelles Eingreifen.

### Trend zu kurzen Laufzeiten

> [!tip] **Kurze Gültigkeit + Automatisierung**
> Zertifikatslaufzeiten werden immer kürzer (von Jahren über 90 Tage hin zu noch kürzeren Zeiträumen). Das reduziert das Zeitfenster bei Kompromittierung und verringert die Abhängigkeit von Sperrmechanismen (→ CRL/OCSP). Praktikabel ist das nur durch **Automatisierung** – manuell wäre die häufige Erneuerung nicht zu bewältigen.

### Best Practices

- Vollständiges **Inventar** aller Zertifikate führen.
- **Monitoring** der Ablaufdaten mit rechtzeitigen Warnungen.
- **Automatische Erneuerung** (ACME) wo möglich.
- Private Schlüssel sicher speichern (HSM/KMS, → Modul 10).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Zertifikatsmanagement verhindert Ausfälle durch abgelaufene/unbekannte Zertifikate
> - ACME (RFC 8555, Let's Encrypt) automatisiert Ausstellung und Erneuerung über Domain-Challenges
> - Kurze Laufzeiten erhöhen die Sicherheit, erfordern aber Automatisierung
> - Best Practices: Inventar, Monitoring, Auto-Renewal, sichere Schlüsselablage

---

## Übungen

1. Welche Risiken entstehen ohne systematisches Zertifikatsmanagement?
2. Beschreiben Sie den ACME-Ausstellungsablauf.
3. Warum sind kurze Zertifikatslaufzeiten nur mit Automatisierung praktikabel?

---

← [[08-Certificate-Transparency|← Zurück]] | [[00-PKI-Index|Übersicht]] | [[00-Protokolle-Index|Nächstes Modul →]]
