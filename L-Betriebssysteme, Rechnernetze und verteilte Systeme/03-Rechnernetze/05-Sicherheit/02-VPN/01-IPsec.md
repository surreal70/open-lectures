---
author: Andreas Hümmer
title: IPsec - Internet Protocol Security
tags:
  - content
  - rn
  - sicherheit
  - vpn
  - ipsec
  - esp
  - ah
  - ike
created: '2026-10-13'
modified: '2026-10-24'
bereich: RN
---

# IPsec - Internet Protocol Security

## Definition

> [!quote] Definition
> **IPsec (Internet Protocol Security)** ist eine Protokollsuite zur Absicherung der IP-Kommunikation auf Netzwerkschicht (Layer 3). Es bietet Verschlüsselung, Authentifizierung und Integritätsschutz für IP-Pakete.
>
> > [!info] Schichtenzuordnung
> > IPsec arbeitet auf **Layer 3** und ist bei IPv6 als Extension Header integriert. Siehe auch: [[../../03-Referenzmodelle/06-Netzwerkschicht/06-IPsec|IPsec in der Netzwerkschicht]]
## Komponenten

### Protokolle

| Protokoll | IP-Protocol | Funktion |
|-----------|-------------|----------|
| **ESP** | 50 | Encapsulating Security Payload – Verschlüsselung + Authentifizierung |
| **AH** | 51 | Authentication Header – Nur Authentifizierung (keine Verschlüsselung) |

### Schlüsselaustausch

| Protokoll | Port | Funktion |
|-----------|------|----------|
| **IKEv1** | UDP 500 | Internet Key Exchange Version 1 |
| **IKEv2** | UDP 500, 4500 | Internet Key Exchange Version 2 (aktuell) |

## Modi

![[ipsec-modes.png]]
*<span class="fig-id">05-02-01-ipsec-modes</span>: IPsec Transport- und Tunnel-Modus – Unterschiedliche Kapselung der Pakete.*

**Transport-Modus:**
- Original-IP-Header bleibt erhalten
- Nur die Nutzdaten werden verschlüsselt
- Einsatz: Host-to-Host-Kommunikation
- Geringerer Overhead (kein zusätzlicher IP-Header)

**Tunnel-Modus:**
- Komplettes Original-Paket wird gekapselt
- Neuer IP-Header mit Gateway-Adressen
- Einsatz: Gateway-to-Gateway (Site-to-Site VPN)
- Verbirgt interne IP-Adressen

## IKE-Phasen

Der **Internet Key Exchange (IKE)** handelt die kryptografischen Parameter aus und authentifiziert die Kommunikationspartner. IKE läuft in zwei Phasen ab:

### Phase 1: IKE SA aufbauen

**Ziel:** Sicheren Kanal für Phase 2 etablieren

**Verhandelte Parameter:**
- Verschlüsselungsalgorithmus (AES-256, AES-128)
- Hash-Algorithmus (SHA-256, SHA-384)
- Authentifizierungsmethode (Pre-Shared Key, Zertifikat)
- Diffie-Hellman-Gruppe (DH14, DH19, DH20)
- SA-Lebensdauer

**Modi in IKEv1:**

| Modus | Nachrichten | Identitätsschutz | Einsatz |
|-------|-------------|------------------|---------|
| **Main Mode** | 6 | Ja (verschlüsselt) | Standard, sicherer |
| **Aggressive Mode** | 3 | Nein (Klartext) | Schneller, aber unsicherer |

> [!warning] **Sicherheitshinweis**
> Aggressive Mode überträgt die Identität im Klartext und ist anfällig für Offline-Wörterbuchangriffe bei PSK-Authentifizierung. Main Mode bevorzugen!

### Phase 2: IPsec SA aufbauen (Quick Mode)

**Ziel:** Die eigentlichen IPsec-Parameter für den Datentransfer aushandeln

**Verhandelte Parameter:**
- IPsec-Protokoll (ESP oder AH)
- Verschlüsselungsalgorithmus für ESP
- Integritätsalgorithmus
- SA-Lebensdauer (Zeit oder Datenvolumen)
- Optional: Perfect Forward Secrecy (PFS) mit neuem DH-Austausch

**Ergebnis:** Zwei unidirektionale Security Associations (eine pro Richtung)

### IKEv2 – Modernisierte Version

IKEv2 (RFC 7296) vereinfacht den Austausch:
- Nur **4 Nachrichten** für initialen Austausch (statt 6+3)
- Integrierte NAT-Traversal-Unterstützung (Port 4500)
- Eingebaute DoS-Abwehr (Cookies)
- MOBIKE-Erweiterung für IP-Wechsel (Roaming)

## Security Associations (SA)

Eine **Security Association (SA)** ist ein Vertrag zwischen zwei IPsec-Peers, der alle Parameter für die sichere Kommunikation festlegt.

### SA-Eigenschaften

- **Unidirektional:** Für bidirektionale Kommunikation werden zwei SAs benötigt
- **Protokollspezifisch:** Separate SAs für ESP und AH
- **Eindeutig identifiziert durch:**
  - Security Parameter Index (SPI) – 32-Bit-Zufallswert
  - Ziel-IP-Adresse
  - Protokoll (ESP oder AH)

### SA-Inhalte

| Parameter | Beschreibung |
|-----------|--------------|
| SPI | Eindeutige Kennung der SA |
| Sequenznummer | Anti-Replay-Schutz |
| Verschlüsselungsalgorithmus | z.B. AES-256-GCM |
| Verschlüsselungsschlüssel | Symmetrischer Schlüssel |
| Integritätsalgorithmus | z.B. HMAC-SHA-256 |
| Integritätsschlüssel | Schlüssel für MAC |
| SA-Lebensdauer | Zeit oder Datenvolumen |
| IPsec-Modus | Transport oder Tunnel |

### Datenbanken

**SAD (Security Association Database):**
- Speichert alle aktiven Security Associations
- Wird bei jedem ein-/ausgehenden IPsec-Paket konsultiert
- Lookup über (SPI, Ziel-IP, Protokoll)

**SPD (Security Policy Database):**
- Definiert Regeln: Welcher Traffic wird wie behandelt?
- Drei mögliche Aktionen:
  - **PROTECT:** IPsec anwenden (mit welcher SA?)
  - **BYPASS:** Ungeschützt durchlassen
  - **DISCARD:** Paket verwerfen
- Selektoren: Quell-/Ziel-IP, Ports, Protokoll

> [!example] **SPD-Regel Beispiel**
> "Traffic von 10.0.0.0/24 nach 192.168.0.0/24 auf Port 443 → PROTECT mit ESP-Tunnel"

## Verschlüsselung und Algorithmen

IPsec unterstützt verschiedene kryptografische Algorithmen. Die Auswahl erfolgt während der IKE-Verhandlung.

### Symmetrische Verschlüsselung (ESP)

| Algorithmus | Schlüssellänge | Status | Bemerkung |
|-------------|----------------|--------|-----------|
| **AES-GCM** | 128/256 Bit | ✓ Empfohlen | Authentifizierte Verschlüsselung, schnell |
| **AES-CBC** | 128/256 Bit | ✓ Akzeptabel | Benötigt separaten Integritätsschutz |
| **ChaCha20-Poly1305** | 256 Bit | ✓ Empfohlen | Gut für Software-Implementierungen |
| 3DES | 168 Bit | ⚠ Veraltet | Nur für Legacy-Systeme |
| DES | 56 Bit | ✗ Unsicher | Nicht verwenden! |

### Integritätsalgorithmen

| Algorithmus | Ausgabelänge | Status |
|-------------|--------------|--------|
| **HMAC-SHA-256** | 256 Bit | ✓ Empfohlen |
| **HMAC-SHA-384** | 384 Bit | ✓ Empfohlen |
| HMAC-SHA-1 | 160 Bit | ⚠ Veraltet |
| HMAC-MD5 | 128 Bit | ✗ Unsicher |

### Diffie-Hellman-Gruppen (Schlüsselaustausch)

| Gruppe | Typ | Größe | Status |
|--------|-----|-------|--------|
| DH 14 | MODP | 2048 Bit | ✓ Minimum |
| DH 15 | MODP | 3072 Bit | ✓ Empfohlen |
| DH 16 | MODP | 4096 Bit | ✓ Hoch |
| **DH 19** | ECP | 256 Bit | ✓ Empfohlen (ECDH) |
| **DH 20** | ECP | 384 Bit | ✓ Empfohlen (ECDH) |
| DH 21 | ECP | 521 Bit | ✓ Hoch (ECDH) |

> [!tip] **Empfohlene Kombinationen (2024+)**
> - **Verschlüsselung:** AES-256-GCM oder ChaCha20-Poly1305
> - **Integrität:** Implizit bei GCM/Poly1305, sonst SHA-256/384
> - **DH-Gruppe:** DH 19 (Curve P-256) oder DH 20 (Curve P-384)
> - **PRF:** SHA-256 oder SHA-384

### Perfect Forward Secrecy (PFS)

**Problem ohne PFS:**
- Kompromittierter Langzeit-Schlüssel ermöglicht Entschlüsselung aller aufgezeichneten Sessions

**Lösung mit PFS:**
- Neuer Diffie-Hellman-Austausch für jede Phase-2-SA
- Kompromittierter Schlüssel betrifft nur eine Session
- Aufgezeichneter Traffic bleibt geschützt

> [!warning] **Praxisempfehlung**
> PFS sollte immer aktiviert sein, auch wenn es zusätzliche Rechenzeit kostet.

## Prüfungsrelevanz

> [!warning] **Prüfungsrelevant**
> - Transport-Modus vs. Tunnel-Modus
> - ESP (Verschlüsselung + Integrität) vs. AH (nur Integrität)
> - IKE Phase 1 (ISAKMP SA) vs. Phase 2 (IPsec SA)
> - Security Association (SA) und SPI
> - Perfect Forward Secrecy (PFS)
> - Main Mode vs. Aggressive Mode

---

## Prüfungstipps

> [!warning] **Häufige Klausurfehler**
> - ESP und AH verwechseln (AH verschlüsselt NICHT!)
> - Transport- und Tunnel-Modus verwechseln

> [!question] **Häufige Prüfungsfragen**
> 1. Warum bietet AH keine Vertraulichkeit?
> 2. Was ist der Unterschied zwischen Transport- und Tunnel-Modus?
> 3. Welche Aufgabe hat IKE Phase 1 vs. Phase 2?
> 4. Wie wird eine Security Association identifiziert?
> 5. Was bewirkt Perfect Forward Secrecy?
> 6. Warum ist Aggressive Mode unsicherer als Main Mode?

> [!tip] **Merkhilfen**
> - **ESP** = **E**ncryption + **S**ecurity + **P**ayload (verschlüsselt!)
> - **AH** = **A**uthentication **H**eader (nur Integrität, keine Verschlüsselung)
> - **Transport** = Host-to-Host, Original-Header bleibt
> - **Tunnel** = Gateway-to-Gateway, komplettes Paket gekapselt
> - **Phase 1** = Sicheren Kanal aufbauen (IKE SA)
> - **Phase 2** = IPsec-Parameter verhandeln (IPsec SA)
> - **SA-Tripel** = SPI + Ziel-IP + Protokoll

---

## Weiterführende Ressourcen

> [!note] **RFC-Standards**
> - RFC 4301 – Security Architecture for the Internet Protocol
> - RFC 4303 – IP Encapsulating Security Payload (ESP)
> - RFC 4302 – IP Authentication Header (AH)
> - RFC 7296 – Internet Key Exchange Protocol Version 2 (IKEv2)

> [!tip] **Praktische Tools**
> - **Wireshark** → IPsec-Traffic analysieren (Filter: `esp` oder `isakmp`)
> - **strongSwan** → Open-Source IPsec-Implementierung
> - **Cisco IOS** → `show crypto ipsec sa` für SA-Status

---

## Zusammenhänge

- [[00-VPN-Index]] → VPN-Übersicht
- [[../../03-Referenzmodelle/06-Netzwerkschicht/06-IPsec|IPsec (Netzwerkschicht)]] → Layer-3-Einordnung
- [[05-L2TP]] → L2TP nutzt IPsec für Verschlüsselung
- [[../01-Firewalls|Firewalls]] → IPsec-Traffic durch Firewalls (UDP 500, 4500, ESP/AH)

---

## Quellen

- RFC 4301 – Security Architecture for the Internet Protocol – Die Basis-Spezifikation für IPsec.
- RFC 7296 – Internet Key Exchange Protocol Version 2 (IKEv2) – Aktueller Standard für Schlüsselaustausch.
- Tanenbaum, Andrew S.: Computernetzwerke – Grundlagen der Netzwerksicherheit und VPN-Technologien.

