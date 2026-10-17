---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - protokolle
---

# IPsec und VPN-Protokolle

> [!info] **Lernziele**
> - Zweck und Aufbau von VPNs verstehen
> - IPsec mit seinen Komponenten einordnen
> - Gängige VPN-Protokolle vergleichen

---

## Inhalt

### Was ist ein VPN?

Ein **Virtual Private Network (VPN)** schafft einen verschlüsselten „Tunnel" über ein unsicheres Netz (meist das Internet), sodass entfernte Geräte oder Netze sicher miteinander kommunizieren – als wären sie im selben privaten Netz.

### IPsec

**IPsec** ist ein Protokoll-Rahmenwerk zur Absicherung auf der **Netzwerkschicht (IP)**. Zentrale Bestandteile:

| Komponente | Funktion |
|------------|----------|
| **IKE (Internet Key Exchange)** | Aushandlung der Schlüssel und Parameter (v2 = IKEv2) |
| **ESP (Encapsulating Security Payload)** | Verschlüsselung und Integrität der Pakete |
| **AH (Authentication Header)** | nur Integrität/Authentizität (selten genutzt) |

Betriebsmodi:

- **Transport-Modus:** nur die Nutzlast wird geschützt (Host-zu-Host).
- **Tunnel-Modus:** das gesamte IP-Paket wird gekapselt (Site-to-Site-VPN, Gateway-zu-Gateway).

### Gängige VPN-Protokolle

| Protokoll | Einordnung |
|-----------|------------|
| **IPsec/IKEv2** | robust, breit unterstützt, komplex zu konfigurieren |
| **OpenVPN** | TLS-basiert, flexibel, bewährt |
| **WireGuard** | modern, schlank, schnell (→ [[05-WireGuard]]) |
| **PPTP** | **veraltet und unsicher – nicht verwenden** |

> [!danger] **Veraltete VPN-Technik**
> PPTP (und ungesicherte L2TP-Varianten) gelten als unsicher. Für neue Deployments: **WireGuard** oder **IPsec/IKEv2** bzw. OpenVPN mit aktuellen Verfahren.

### Sicherheitsaspekte

Ein VPN ist nur so sicher wie seine Konfiguration: moderne AEAD-Chiffren, ephemerer Schlüsselaustausch für Forward Secrecy (→ [[06-Perfect-Forward-Secrecy]]) und sorgfältiges Schlüsselmanagement (→ Modul 10) sind entscheidend.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - VPNs bauen verschlüsselte Tunnel über unsichere Netze
> - IPsec arbeitet auf der IP-Schicht: IKE (Schlüssel), ESP (Schutz), Transport-/Tunnel-Modus
> - Gängig: IPsec/IKEv2, OpenVPN, WireGuard; PPTP ist unsicher
> - Sicherheit hängt an moderner Konfiguration, Forward Secrecy und Schlüsselmanagement

---

## Übungen

1. Worin unterscheiden sich Transport- und Tunnel-Modus bei IPsec?
2. Welche Aufgabe hat IKE?
3. Warum sollte PPTP nicht mehr eingesetzt werden?

---

← [[03-SSH-und-Schluesselmanagement|← Zurück]] | [[00-Protokolle-Index|Übersicht]] | [[05-WireGuard|Weiter →]]
