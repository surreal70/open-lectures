---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - protokolle
---

# Schlüsselvereinbarung und Authentifizierung

> [!info] **Lernziele**
> - Schlüsselvereinbarung und Authentifizierung als zwei getrennte Aufgaben verstehen
> - Erkennen, warum beide zusammengehören
> - Gängige Authentifizierungsmechanismen einordnen

---

## Inhalt

### Zwei getrennte Probleme

Ein sicheres Protokoll muss **zwei** Dinge leisten:

1. **Schlüsselvereinbarung:** ein gemeinsames Geheimnis über einen unsicheren Kanal etablieren (→ [[03-Diffie-Hellman-Schlüsselaustausch]]).
2. **Authentifizierung:** sicherstellen, dass man mit dem **richtigen** Partner spricht und nicht mit einem Angreifer.

Beide gehören zusammen: Schlüsselvereinbarung allein (z. B. reines DH) ist anfällig für Man-in-the-Middle (→ [[08-Replay-und-Man-in-the-Middle-Angriffe]]), weil nicht geprüft wird, **wer** am anderen Ende sitzt.

### Authentifiziertes Schlüsselabkommen (AKE)

Ein **Authenticated Key Exchange (AKE)** verbindet beides: Der ephemere Schlüsselaustausch (für Forward Secrecy) wird durch einen Langzeit-Authentifizierungsmechanismus abgesichert.

```
ECDHE  → gemeinsames Sitzungsgeheimnis (Vertraulichkeit + PFS)
  +
Signatur/Zertifikat  → Nachweis der Identität (Authentizität)
```

Genau so arbeitet TLS: Der Server signiert seinen Anteil am Schlüsselaustausch mit dem privaten Schlüssel zu seinem Zertifikat – so ist der ausgehandelte Schlüssel an eine geprüfte Identität gebunden.

### Authentifizierungsmechanismen

| Mechanismus | Beispiel |
|-------------|----------|
| **Zertifikate (PKI)** | TLS-Serverauthentifizierung (→ Modul 8) |
| **Pre-Shared Key (PSK)** | WireGuard, IoT, einfache Setups |
| **Public-Key / TOFU** | SSH (→ [[03-SSH-und-Schluesselmanagement]]) |
| **Passwort-basiert (PAKE)** | moderne passwortbasierte Verfahren (z. B. OPAQUE) |

### Gegenseitige Authentifizierung

Oft authentifiziert sich nur der Server (z. B. normales HTTPS). Bei **mutual TLS (mTLS)** weisen sich **beide** Seiten per Zertifikat aus – wichtig in Zero-Trust-Architekturen und Service-zu-Service-Kommunikation.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Sichere Protokolle brauchen Schlüsselvereinbarung **und** Authentifizierung
> - Reiner Schlüsselaustausch ohne Authentifizierung ist MitM-anfällig
> - AKE verbindet ephemeren Austausch (PFS) mit Identitätsnachweis
> - Mechanismen: Zertifikate/PKI, PSK, Public-Key/TOFU, PAKE; mTLS für beidseitige Auth

---

## Übungen

1. Warum ist reiner Diffie-Hellman ohne Authentifizierung unsicher?
2. Wie bindet TLS den ausgehandelten Schlüssel an eine Identität?
3. Was bedeutet mutual TLS?

---

← [[06-Perfect-Forward-Secrecy|← Zurück]] | [[00-Protokolle-Index|Übersicht]] | [[08-Replay-und-Man-in-the-Middle-Angriffe|Weiter →]]
