---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - praxis
---

# Fehlkonfigurationen identifizieren

> [!info] **Lernziele**
> - Typische kryptographische Fehlkonfigurationen erkennen
> - Werkzeuge zur Analyse einsetzen
> - Findings bewerten und priorisieren

---

## Inhalt

### Ziel

In dieser Übung analysierst du Systeme auf **kryptographische Fehlkonfigurationen** – die in der Praxis häufigste Ursache für Schwächen (→ [[09-Kryptographische-Implementierungsfehler]]).

### Checkliste typischer Findings

| Bereich | Fehlkonfiguration |
|---------|-------------------|
| TLS-Version | TLS 1.0/1.1 noch aktiv |
| Cipher | schwache/Export-Cipher, RC4, CBC ohne Not |
| Zertifikat | abgelaufen, selbstsigniert (öffentlich), schwacher Schlüssel, fehlender SAN |
| Hash/Signatur | MD5/SHA-1 in Zertifikaten |
| HSTS | fehlt |
| Schlüssel | zu kurz (RSA < 2048), im Repo eingecheckt |

### Werkzeuge

```bash
# TLS-Konfiguration manuell prüfen (→ Übung 05)
openssl s_client -connect ziel:443 -servername ziel

# Protokollversionen durchtesten
for v in tls1 tls1_1 tls1_2 tls1_3; do
  echo "== $v =="
  echo | openssl s_client -connect ziel:443 -$v 2>&1 | grep -E "Protocol|Cipher|alert"
done
```

Weitere nützliche (teils externe) Tools: **testssl.sh**, **sslscan**, **nmap --script ssl-enum-ciphers**. Für Repositories: Secret-Scanner (z. B. gitleaks) gegen eingecheckte Schlüssel.

### Secrets im Code suchen

```bash
# grobe Suche nach eingecheckten Schlüsseln/Secrets
grep -rIE "BEGIN (RSA|EC|OPENSSH|PGP) PRIVATE KEY|api[_-]?key" . --exclude-dir=.git
```

> [!warning] **Priorisierung**
> Findings nach Risiko bewerten (→ [[09-Kryptographisches-Inventar-und-Risikomanagement]]): Ein öffentlich erreichbarer Dienst mit TLS 1.0 und abgelaufenem Zertifikat ist dringlicher als ein internes Testsystem. Immer im Kontext bewerten.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Fehlkonfigurationen sind die häufigste reale Krypto-Schwäche
> - Typisch: alte TLS-Versionen, schwache Cipher, schlechte Zertifikate, fehlendes HSTS, Secrets im Code
> - Werkzeuge: openssl s_client, testssl.sh, sslscan, nmap; Secret-Scanner für Repos
> - Findings risikobasiert priorisieren

---

## Übungen

1. Testen Sie einen (Test-)Server auf unterstützte TLS-Versionen und Cipher.
2. Finden Sie mindestens drei mögliche Fehlkonfigurationen und bewerten Sie deren Risiko.
3. Durchsuchen Sie ein Repository nach versehentlich eingecheckten Schlüsseln.

---

← [[08-Hashwerte-und-HMACs-berechnen|← Zurück]] | [[00-Uebungen-Index|Übersicht]] | [[10-Kryptographische-Sicherheitsarchitektur-entwerfen|Weiter →]]
