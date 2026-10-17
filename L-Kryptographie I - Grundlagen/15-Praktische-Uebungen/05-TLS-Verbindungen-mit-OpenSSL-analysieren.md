---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - praxis
---

# TLS-Verbindungen mit OpenSSL analysieren

> [!info] **Lernziele**
> - TLS-Verbindungen mit OpenSSL untersuchen
> - Zertifikatskette und ausgehandelte Parameter auslesen
> - Unterstützte Protokollversionen prüfen

---

## Inhalt

### Verbindung inspizieren

```bash
# Verbindung zu einem Server aufbauen und Details anzeigen
openssl s_client -connect example.com:443 -servername example.com
```

Interessant in der Ausgabe:

- **Certificate chain:** die präsentierte Zertifikatskette (→ [[05-Zertifikatsketten-und-Vertrauensmodelle]]).
- **Protocol / Cipher:** ausgehandelte TLS-Version und Cipher-Suite.
- **Verify return code:** Ergebnis der Kettenprüfung.

### Zertifikat extrahieren und ansehen

```bash
# Nur das Serverzertifikat holen und anzeigen
echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null \
  | openssl x509 -text -noout
```

Achte auf **Gültigkeitszeitraum**, **SAN** und **Aussteller**.

### Protokollversionen testen

```bash
# Prüfen, ob (veraltetes) TLS 1.0 noch akzeptiert wird
openssl s_client -connect example.com:443 -tls1   # sollte fehlschlagen
# TLS 1.3 erzwingen
openssl s_client -connect example.com:443 -tls1_3
```

> [!warning] **Interpretation**
> Akzeptiert ein Server noch **TLS 1.0/1.1** oder schwache Cipher, ist das ein Finding für ein Audit (→ [[09-Fehlkonfigurationen-identifizieren]]). Moderne Server sollten TLS 1.2+ (idealerweise 1.3) mit AEAD-Suiten erzwingen (→ [[01-TLS-1.2-und-TLS-1.3]]).

### Ablaufdatum schnell prüfen

```bash
echo | openssl s_client -connect example.com:443 2>/dev/null \
  | openssl x509 -noout -dates
```

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - `openssl s_client -connect host:443` zeigt Kette, Protokoll und Cipher
> - Zertifikat per `openssl x509 -text` inspizieren (SAN, Gültigkeit, Aussteller)
> - Protokollversionen gezielt mit `-tls1`/`-tls1_3` testen
> - Alte Versionen/Cipher sind ein Audit-Finding

---

## Übungen

1. Analysieren Sie eine HTTPS-Verbindung und notieren Sie TLS-Version und Cipher.
2. Extrahieren Sie das Serverzertifikat und prüfen Sie SAN und Gültigkeit.
3. Testen Sie, ob der Server veraltete TLS-Versionen akzeptiert.

---

← [[04-Eigene-Certificate-Authority-aufbauen|← Zurück]] | [[00-Uebungen-Index|Übersicht]] | [[06-SSH-Schluessel-sicher-verwalten|Weiter →]]
