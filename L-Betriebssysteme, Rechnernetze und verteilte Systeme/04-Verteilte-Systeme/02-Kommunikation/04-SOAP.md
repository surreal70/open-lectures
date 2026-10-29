---
author: Andreas Hümmer
title: SOAP (Simple Object Access Protocol)
tags:
  - content
  - vs
  - kommunikation
  - soap
  - xml
  - webservices
created: '2026-10-13'
modified: '2026-10-24'
bereich: VS
---

# SOAP (Simple Object Access Protocol)

> [!info] Lernziele
> - SOAP als Protokoll verstehen und von REST abgrenzen
> - Aufbau einer SOAP-Nachricht kennen
> - Vor- und Nachteile von SOAP benennen können
> - Anwendungsfälle für SOAP identifizieren

## Einleitung

SOAP (Simple Object Access Protocol, auch: Simple Object Architecture Protocol) ist ein Protokoll zum Austausch XML-basierter Datensätze über ein Rechnernetzwerk. Es wurde ursprünglich von Microsoft entwickelt und ist heute ein W3C-Standard.

> [!important] Kernkonzept
> SOAP ist ein **Protokoll** (nicht nur ein Architekturstil wie REST), das XML für den Nachrichtenaustausch verwendet. Es definiert eine strikte Nachrichtenstruktur mit Envelope, Header und Body und bietet eingebaute Standards für Sicherheit (WS-Security) und Transaktionen.

> [!example] Analogie
> SOAP ist wie ein formeller Geschäftsbrief mit strenger Struktur: Er hat einen Umschlag (Envelope) mit Absender und Empfänger, einen Briefkopf (Header) mit Metadaten und formellen Angaben, und den eigentlichen Briefinhalt (Body). Jedes Element hat seinen festen Platz – keine Abweichungen erlaubt.

## SOAP-Nachrichtenstruktur

### Aufbau einer SOAP-Nachricht

```xml
<?xml version="1.0"?>
<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope">
  <s:Header>
    <!-- Metadaten, Authentifizierung, Routing -->
  </s:Header>
  <s:Body>
    <!-- Eigentliche Nutzdaten / Payload -->
  </s:Body>
</s:Envelope>
```

![[soap-envelope.png]]
*<span class="fig-id">04-02-04-soap-envelope</span>: Struktur einer SOAP-Nachricht mit Envelope, Header und Body*

### Komponenten

| Komponente | Pflicht | Beschreibung |
|------------|---------|--------------|
| **Envelope** | ✓ | Wurzelelement, definiert den Namespace |
| **Header** | ✗ | Metadaten, Authentifizierung, Routing |
| **Body** | ✓ | Eigentliche Nutzdaten oder Fault-Element |
| **Fault** | ✗ | Standardisierte Fehlerinformationen |

## SOAP vs. REST

| Aspekt | SOAP | REST |
|--------|------|------|
| **Typ** | Protokoll | Architekturstil |
| **Format** | Nur XML | JSON, XML, andere |
| **Bandbreite** | Höherer Overhead | Leichtgewichtig |
| **Kopplung** | Engere Bindung Client/Server | Lose Kopplung |
| **Caching** | Nicht direkt möglich | Unterstützt |
| **Sicherheit** | WS-Security (sehr robust) | HTTPS, OAuth |
| **Standardisierung** | Stark (WSDL, WS-*) | Weniger formal |

## Vor- und Nachteile

### Vorteile

- **Sicherheit**: WS-Security bietet umfassende Sicherheitsmechanismen
- **Transaktionen**: ACID-Transaktionen über WS-AtomicTransaction
- **Zuverlässigkeit**: WS-ReliableMessaging für garantierte Zustellung
- **Typsicherheit**: WSDL definiert exakte Schnittstellen
- **Plattformunabhängig**: XML als universelles Format

### Nachteile

- **Overhead**: XML-Struktur erhöht Datenmenge erheblich
- **Komplexität**: Viele Standards (WS-*) zu beherrschen
- **Performance**: Parsing von XML ist aufwändig
- **Flexibilität**: Strikte Struktur weniger agil

---

## WS-*-Standards im Detail

> [!important] Die Stärke von SOAP liegt in den WS-*-Standards
> Diese Standards machen SOAP für Enterprise-Anwendungen attraktiv, erhöhen aber die Komplexität erheblich.

### WS-Security

Bietet End-to-End-Sicherheit auf Nachrichtenebene (nicht nur Transportebene):

| Feature | Beschreibung |
|---------|--------------|
| **Verschlüsselung** | XML Encryption für Teile oder ganze Nachricht |
| **Signatur** | XML Signature für Integrität und Authentizität |
| **Tokens** | Username/Password, X.509, Kerberos, SAML |
| **Timestamps** | Schutz vor Replay-Attacken |

**Vorteil gegenüber HTTPS:** Sicherheit bleibt erhalten, auch wenn die Nachricht über Intermediäre (Proxies, Message Broker) geroutet wird.

### WS-ReliableMessaging

Garantierte Zustellung auch bei Netzwerkproblemen:

```
Sender: Message 1, Sequence=1
Sender: Message 2, Sequence=2
Receiver: Ack für Sequence 1, 2
Sender: Message 3, Sequence=3
[Netzwerkfehler]
Sender: (Timeout) Retry Message 3, Sequence=3
Receiver: Ack für Sequence 3
```

### WS-AtomicTransaction

Verteilte Transaktionen über mehrere Services:

```
Coordinator: Begin Transaction
  → Service A: Reserve Inventory
  → Service B: Charge Payment
  → Service C: Create Shipping Order
Coordinator: Commit (alle erfolgreich) oder Rollback (einer fehlgeschlagen)
```

---

## Warum SOAP heute noch?

> [!question] Ist SOAP nicht veraltet?
> SOAP ist weniger populär als früher, aber in bestimmten Branchen immer noch Standard.

### Branchen mit SOAP-Dominanz

| Branche | Grund |
|---------|-------|
| **Banken & Finanzwesen** | WS-Security, Transaktionen, Compliance |
| **Versicherungen** | Komplexe Datenstrukturen, Legacy-Integration |
| **Gesundheitswesen** | HL7/FHIR-Integration, Audit-Anforderungen |
| **Regierung** | Standards, Interoperabilität, Dokumentation |
| **SAP-Ökosystem** | RFC, BAPI, native SOAP-Unterstützung |

### Migration von SOAP zu REST

Viele Unternehmen migrieren schrittweise:
1. **Facade-Pattern**: REST-API vor SOAP-Backend
2. **Parallel-Betrieb**: Neue Features in REST, alte in SOAP
3. **Strangler Pattern**: Schrittweises Ersetzen von SOAP-Endpoints

## WSDL (Web Services Description Language)

WSDL beschreibt SOAP-Services maschinenlesbar:
- **Types**: Datentypen (meist XML Schema)
- **Messages**: Ein- und Ausgabenachrichten
- **PortType**: Operationen des Services
- **Binding**: Protokoll und Format
- **Service**: Konkrete Endpunkt-Adresse

## Anwendungsfälle

SOAP eignet sich besonders für:
- **Enterprise-Anwendungen** mit hohen Sicherheitsanforderungen
- **Finanzsektor** (Banken, Versicherungen)
- **B2B-Integration** mit verschiedenen Partnern
- **Systeme mit ACID-Transaktionsanforderungen**
- **Legacy-Systeme** mit bestehenden SOAP-Schnittstellen

## Zusammenhänge

| Beziehung | Konzept | Beschreibung |
|-----------|---------|--------------|
| Alternative zu | [[03-REST]] | Schwergewichtiger, aber sicherer |
| Basiert auf | XML | Nachrichtenformat |
| Beschrieben durch | WSDL | Maschinenlesbare Schnittstellenbeschreibung |
| Sicherheit | WS-Security | End-to-End-Verschlüsselung und Signatur |
| Nutzt | HTTP/HTTPS | Transportprotokoll |

---

> [!warning] **Prüfungsrelevant**
> - SOAP-Nachrichtenstruktur (Envelope, Header, Body)
> - Unterschiede zwischen SOAP und REST

> [!question] **Typische Prüfungsfragen**
> - Vergleichen Sie SOAP und REST hinsichtlich Overhead, Sicherheit und Flexibilität.
> - Wann würden Sie SOAP statt REST einsetzen?
> - Warum gilt SOAP als sicherer als REST?
> - Was ist der Unterschied zwischen einem Protokoll und einem Architekturstil?
> - Welche Rolle spielt WSDL bei SOAP?

> [!tip] **Merkhilfe**
> **SOAP = Sicherer, aber aufwändiger**:
> - **S**trikt strukturiert (XML)
> - **O**verhead durch Envelope
> - **A**CID-Transaktionen möglich
> - **P**rotokoll (nicht nur Stil)

---

## Weiterführende Ressourcen

- [[03-REST]] – Leichtgewichtige Alternative
- [[01-RPC]] – Grundlegendes Aufrufkonzept
- [[05-SOA]] – Service-orientierte Architektur

---

## Quellen

- W3C (2007). SOAP Version 1.2 Part 1: Messaging Framework. https://www.w3.org/TR/soap12-part1/
- W3C (2007). SOAP Version 1.2 Part 2: Adjuncts. https://www.w3.org/TR/soap12-part2/
- W3C (2007). Web Services Description Language (WSDL) Version 2.0. https://www.w3.org/TR/wsdl20/
- OASIS (2006). Web Services Security (WS-Security) 1.1. OASIS Standard.
