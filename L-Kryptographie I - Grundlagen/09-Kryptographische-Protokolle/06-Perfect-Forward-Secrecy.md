---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - protokolle
---

# Perfect Forward Secrecy

> [!info] **Lernziele**
> - Das Konzept Perfect Forward Secrecy verstehen
> - Den Unterschied zwischen statischem und ephemerem Schlüsselaustausch kennen
> - Die Bedeutung für langfristige Vertraulichkeit einordnen

---

## Inhalt

### Das Problem ohne Forward Secrecy

Stell dir vor, ein Angreifer zeichnet verschlüsselten Verkehr heute auf und speichert ihn. Wird **später** der private Langzeitschlüssel des Servers kompromittiert, könnte er damit **alle aufgezeichneten alten Sitzungen** entschlüsseln. Genau dieses „store now, decrypt later"-Szenario verhindert Forward Secrecy.

### Perfect Forward Secrecy (PFS)

**Perfect Forward Secrecy** garantiert: Die Kompromittierung eines Langzeitschlüssels gefährdet **keine** vergangenen Sitzungen. Jede Sitzung nutzt einen **eigenen, kurzlebigen (ephemeren)** Sitzungsschlüssel, der nach Gebrauch verworfen wird und nicht aus dem Langzeitschlüssel ableitbar ist.

### Ephemerer Schlüsselaustausch

Der Schlüssel liegt in der Verwendung **ephemerer** Diffie-Hellman-Varianten:

| Variante | Forward Secrecy? |
|----------|------------------|
| statisches RSA (Schlüsseltransport) | **nein** |
| statisches DH | nein |
| **DHE** (ephemeral DH) | **ja** |
| **ECDHE** (ephemeral EC-DH) | **ja** |

Bei **(EC)DHE** erzeugen beide Seiten pro Sitzung frische, zufällige Schlüssel (→ [[03-Diffie-Hellman-Schlüsselaustausch]], [[05-ECDH-und-X25519]]). Das gemeinsame Geheimnis existiert nur temporär; der Langzeitschlüssel dient lediglich zur **Authentifizierung**, nicht zur Verschlüsselung der Sitzungsschlüssel.

### In der Praxis

> [!tip] **PFS ist heute Standard**
> - **TLS 1.3** erzwingt (EC)DHE → Forward Secrecy ist immer gegeben (→ [[01-TLS-1.2-und-TLS-1.3]]).
> - **TLS 1.2** bietet PFS nur mit DHE-/ECDHE-Cipher-Suites (nicht mit statischem RSA).
> - **WireGuard** und das **Signal-Protokoll** bieten PFS durch regelmäßige neue Handshakes bzw. fortlaufende Schlüsselerneuerung.

Gerade im Hinblick auf künftige Quantencomputer ist PFS wichtig: Es begrenzt den Schaden aufgezeichneter, später entschlüsselter Kommunikation.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - PFS schützt vergangene Sitzungen auch bei späterem Verlust des Langzeitschlüssels
> - Erreicht durch ephemere Schlüssel pro Sitzung (DHE/ECDHE)
> - Statisches RSA/DH bietet keine Forward Secrecy
> - TLS 1.3, WireGuard und Signal bieten PFS standardmäßig

---

## Übungen

1. Welches Angriffsszenario verhindert Perfect Forward Secrecy?
2. Warum bietet statischer RSA-Schlüsseltransport keine PFS?
3. Welche Rolle spielt der Langzeitschlüssel bei ECDHE?

---

← [[05-WireGuard|← Zurück]] | [[00-Protokolle-Index|Übersicht]] | [[07-Schluesselvereinbarung-und-Authentifizierung|Weiter →]]
