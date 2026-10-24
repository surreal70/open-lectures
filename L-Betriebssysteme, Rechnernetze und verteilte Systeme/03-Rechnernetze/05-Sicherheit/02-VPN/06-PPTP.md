---
author: Andreas Hümmer
title: PPTP - Point-to-Point Tunneling Protocol
tags:
  - content
  - rn
  - sicherheit
  - vpn
  - pptp
  - veraltet
  - unsicher
created: '2026-10-13'
modified: '2026-10-24'
bereich: RN
---

# PPTP - Point-to-Point Tunneling Protocol

## Definition

> [!quote] Definition
> **PPTP (Point-to-Point Tunneling Protocol)** ist ein von Microsoft entwickeltes VPN-Protokoll auf Layer 2. Es gilt heute als **unsicher** und sollte nicht mehr verwendet werden.
>
> > [!danger] Sicherheitswarnung
> > PPTP ist **kryptographisch gebrochen** und sollte **nicht mehr verwendet** werden. Die MS-CHAPv2-Authentifizierung kann in wenigen Stunden geknackt werden.
## Eigenschaften

| Eigenschaft | Wert |
|-------------|------|
| **Layer** | 2 (Sicherung) |
| **Control Port** | TCP 1723 |
| **Datenprotokoll** | GRE (Protocol 47) |
| **Verschlüsselung** | MPPE (Microsoft Point-to-Point Encryption) |
| **Status** | ⚠️ **Veraltet und unsicher** |

## Architektur

![[pptp-stack.png]]
*<span class="fig-id">05-02-06-pptp-stack</span>: PPTP Protokollstruktur – Datenpfad (GRE) und Kontrollpfad (TCP 1723).*

**Datenpfad:**
- PPP-Frames werden in GRE (Generic Routing Encapsulation) gekapselt
- GRE ist ein IP-Protokoll (Protocol 47), kein TCP/UDP
- Problematisch für NAT (kein Port zum Übersetzen)

**Kontrollpfad:**
- Separate TCP-Verbindung auf Port 1723
- Tunnel-Aufbau, Session-Management, Keepalives

## Sicherheitsprobleme

> [!danger] **PPTP ist kryptographisch gebrochen!**

**MS-CHAPv2 ist gebrochen:**
- Kann mit Tools wie "ChapCrack" angegriffen werden
- Cloud-Cracking-Dienste knacken Passwörter in ~24 Stunden
- Angreifer kann aufgezeichneten Traffic nachträglich entschlüsseln

**MPPE-Verschlüsselung ist schwach:**
- Basiert auf RC4 (veraltet, bekannte Schwächen)
- Schlüssel wird aus Passwort-Hash abgeleitet
- Keine unabhängige Schlüsselgenerierung

**Keine Perfect Forward Secrecy:**
- Kompromittierter Schlüssel = alle vergangenen Daten lesbar
- Aufgezeichneter Traffic kann nachträglich entschlüsselt werden

**Bekannte Angriffe seit 2012:**
- Moxie Marlinspike & David Hulton: "Defeating PPTP VPNs"
- DEF CON 20 Präsentation
- Öffentlich verfügbare Angriffs-Tools

> [!warning] **Fazit**
> PPTP bietet **keine echte Sicherheit** mehr. Es ist bestenfalls eine Verschleierung, aber kein Schutz gegen einen motivierten Angreifer.

## Warum wird PPTP noch verwendet?

Trotz bekannter Sicherheitsprobleme findet man PPTP noch in manchen Umgebungen:

**Legacy-Systeme:**
- Alte Router und Firewalls ohne neuere VPN-Unterstützung
- Embedded Devices mit begrenzten Ressourcen
- Historische Konfigurationen, die nie migriert wurden

**Einfache Einrichtung:**
- Minimale Konfiguration erforderlich
- Keine Zertifikate oder PKI nötig
- Schnell aufzusetzen für temporäre Tests

**Native Betriebssystem-Unterstützung:**
- In allen Windows-Versionen eingebaut (seit Windows 95)
- macOS, Linux, iOS, Android haben PPTP-Clients
- Keine zusätzliche Software erforderlich

> [!danger] **Trotzdem nicht verwenden!**
> Diese "Vorteile" rechtfertigen nicht die Nutzung eines gebrochenen Protokolls. Moderne Alternativen wie WireGuard oder IKEv2 sind genauso einfach und tatsächlich sicher.

## Alternativen

| Statt PPTP | Verwende |
|------------|----------|
| Remote Access | [[02-WireGuard]], [[03-OpenVPN]] |
| Site-to-Site | [[01-IPsec]] |
| Mobile Geräte | [[01-IPsec\|IKEv2/IPsec]] |

## Prüfungsrelevanz

> [!warning] **Prüfungsrelevant**
> - PPTP ist unsicher und sollte nicht mehr verwendet werden
> - MS-CHAPv2 Authentifizierung ist gebrochen (seit 2012)
> - MPPE-Verschlüsselung basiert auf RC4 (unsicher)
> - Keine Perfect Forward Secrecy
> - Historisch wichtig: erstes weit verbreitetes VPN-Protokoll

---

## Prüfungstipps

> [!warning] **Häufige Klausurfehler**
> - PPTP als sicher bezeichnen
> - MS-CHAPv2-Schwächen nicht kennen

> [!question] **Häufige Prüfungsfragen**
> 1. Warum sollte PPTP nicht mehr verwendet werden?
> 2. Was ist das Problem mit MS-CHAPv2?
> 3. Was bedeutet "keine Perfect Forward Secrecy"?
> 4. Wie unterscheidet sich PPTP von L2TP?
> 5. Welche sicheren Alternativen gibt es?

> [!tip] **Merkhilfen**
> - **PPTP** = **P**retty **P**oor **T**unneling **P**rotocol 😉
> - **2012** = Jahr der öffentlichen Kompromittierung
> - **MS-CHAPv2** = Microsoft Challenge-Handshake (gebrochen!)
> - **MPPE** = Microsoft Point-to-Point Encryption (RC4-basiert)
> - **GRE** = Generic Routing Encapsulation (Protocol 47)
> - **TCP 1723** = Kontroll-Port

---

## Weiterführende Ressourcen

> [!note] **Sicherheitsforschung**
> - Marlinspike, M. & Hulton, D. (2012): "Defeating PPTP VPNs and WPA2-Enterprise with MS-CHAPv2"
> - DEF CON 20: "Crack Me If You Can" – MS-CHAPv2 Angriffe

> [!tip] **Migration**
> - Ersetze PPTP durch WireGuard (einfach, schnell, sicher)
> - Alternativ: IKEv2/IPsec (gute native OS-Unterstützung)
> - OpenVPN für maximale Kompatibilität

---

## Zusammenhänge

- [[00-VPN-Index]] → VPN-Übersicht
- [[05-L2TP]] → Nachfolger (sicher mit IPsec)
- [[01-IPsec]] → Sichere Alternative für Site-to-Site
- [[02-WireGuard]] → Moderne, empfohlene Alternative

---

## Quellen

- RFC 2637 – Point-to-Point Tunneling Protocol (PPTP) – Die Original-Spezifikation.
- Marlinspike, M. & Hulton, D. (2012): Defeating PPTP VPNs – DEF CON 20 Präsentation.
- Schneier, B.: PPTP Security Analysis – Frühe Kritik an PPTP-Sicherheit.

