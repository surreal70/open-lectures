---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - protokolle
---

# SSH und Schlüsselmanagement

> [!info] **Lernziele**
> - Funktionsweise von SSH verstehen
> - Public-Key-Authentifizierung gegenüber Passwörtern einordnen
> - Das TOFU-Modell und Schlüsselverwaltung kennen

---

## Inhalt

### Was ist SSH?

**Secure Shell (SSH)** sichert den Fernzugriff auf Systeme (Shell, Dateiübertragung, Tunnel). Es bietet Vertraulichkeit, Integrität und Authentifizierung – sowohl des **Servers** als auch des **Clients**.

Der Verbindungsaufbau nutzt einen Schlüsselaustausch (meist ECDH/X25519, → [[05-ECDH-und-X25519]]), um Sitzungsschlüssel zu vereinbaren; danach schützt symmetrische AEAD-Verschlüsselung die Sitzung.

### Public-Key-Authentifizierung

Statt eines Passworts kann sich der Nutzer mit einem **Schlüsselpaar** anmelden:

```
~/.ssh/id_ed25519       (privater Schlüssel, geheim halten!)
~/.ssh/id_ed25519.pub   (öffentlicher Schlüssel → auf Server in authorized_keys)
```

- Der Server fordert den Client auf, eine Challenge mit dem privaten Schlüssel zu signieren.
- Vorteile gegenüber Passwörtern: resistent gegen Brute Force und Phishing, kein Geheimnis wird übertragen.
- Empfohlen: **Ed25519**-Schlüssel (→ [[04-EdDSA-und-Ed25519]]), privater Schlüssel mit Passphrase geschützt.

### Server-Authentifizierung: TOFU

> [!note] **Trust on First Use**
> SSH nutzt kein zentrales Zertifikatssystem, sondern **Trust on First Use**: Beim ersten Verbindungsaufbau wird der Host-Schlüssel des Servers angezeigt und in `~/.ssh/known_hosts` gespeichert. Ändert sich dieser Schlüssel später unerwartet, warnt SSH deutlich – ein möglicher Man-in-the-Middle-Angriff (→ [[08-Replay-und-Man-in-the-Middle-Angriffe]]). Der erste Fingerprint sollte über einen vertrauenswürdigen Kanal verifiziert werden.

### Schlüsselverwaltung

- **ssh-agent:** hält entschlüsselte private Schlüssel temporär im Speicher, damit die Passphrase nicht wiederholt eingegeben werden muss.
- **SSH-Zertifikate:** In größeren Umgebungen kann eine SSH-CA Host- und User-Schlüssel signieren – das skaliert besser als `known_hosts`/`authorized_keys` und erlaubt Ablaufzeiten.

> [!tip] **Best Practice**
> Passwort-Authentifizierung deaktivieren, nur Public-Key (oder SSH-CA) zulassen, Ed25519 verwenden, private Schlüssel mit Passphrase schützen.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - SSH sichert Fernzugriff mit Schlüsselaustausch und AEAD-Verschlüsselung
> - Public-Key-Authentifizierung ist Passwörtern überlegen (Ed25519 empfohlen)
> - Server-Authentifizierung über TOFU (known_hosts) – Fingerprint prüfen
> - Verwaltung über ssh-agent und optional SSH-Zertifikate (SSH-CA)

---

## Übungen

1. Welche Vorteile hat Public-Key- gegenüber Passwort-Authentifizierung?
2. Was bedeutet TOFU im SSH-Kontext?
3. Wozu dient ein ssh-agent?

---

← [[02-HTTPS-und-Zertifikatsvalidierung|← Zurück]] | [[00-Protokolle-Index|Übersicht]] | [[04-IPsec-und-VPN-Protokolle|Weiter →]]
