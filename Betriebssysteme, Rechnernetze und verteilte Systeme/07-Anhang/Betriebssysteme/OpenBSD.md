---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# OpenBSD

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | Unix-Betriebssystem |
| **Entwickler** | OpenBSD Project |
| **Gründer** | Theo de Raadt |
| **Erstveröffentlichung** | Oktober 1996 |
| **Aktuelle Version** | 7.x |
| **Lizenz** | BSD-Lizenz |
| **Motto** | "Only two remote holes in the default install!" |

## Zusammenfassung

OpenBSD ist ein BSD-Derivat mit extremem Fokus auf Sicherheit, Code-Qualität und kryptographische Korrektheit. Das Projekt führte zahlreiche Sicherheitsmechanismen ein, die später in andere Betriebssysteme übernommen wurden.

### Sicherheitsinnovationen

| Feature | Beschreibung |
|---------|--------------|
| **W^X** | Speicher ist schreibbar ODER ausführbar, nie beides |
| **ASLR** | Address Space Layout Randomization |
| **ProPolice** | Stack-Smashing-Schutz |
| **pledge()** | Syscall-Filterung für Prozesse |
| **unveil()** | Dateisystem-Sichtbarkeit einschränken |

### Wichtige Projekte aus OpenBSD

- **OpenSSH**: De-facto-Standard für sichere Remote-Verbindungen
- **LibreSSL**: Sichere TLS-Bibliothek (OpenSSL-Fork)
- **OpenBGPD**: BGP-Routing-Daemon
- **pf**: Packet Filter Firewall
- **OpenNTPD**: NTP-Daemon
- **mandoc**: Manpage-Compiler

### Code-Audit-Prozess

OpenBSD ist bekannt für kontinuierliche Sicherheitsaudits des gesamten Quellcodes. Jede Codezeile wird regelmäßig auf potenzielle Sicherheitslücken überprüft.

### Einsatzgebiete

- Firewalls und Router
- VPN-Gateways
- Sicherheitskritische Server
- Embedded Security Appliances

## Siehe auch

- [[BSD]]
- [[FreeBSD]]
- [[NetBSD]]

## Quellen

- [OpenBSD.org](https://www.openbsd.org/)
- [OpenBSD FAQ](https://www.openbsd.org/faq/)
- [Wikipedia: OpenBSD](https://en.wikipedia.org/wiki/OpenBSD)
