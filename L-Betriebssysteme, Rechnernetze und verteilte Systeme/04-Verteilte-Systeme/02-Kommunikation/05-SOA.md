---
author: Andreas Hümmer
title: Service-orientierte Architektur (SOA)
tags:
  - content
  - vs
  - kommunikation
  - soa
  - architektur
  - microservices
created: '2026-10-13'
modified: '2026-10-24'
bereich: VS
---

# Service-orientierte Architektur (SOA)

> [!info] Lernziele
> - SOA als Organisationskonzept verstehen
> - Unterschied zwischen SOA und konkreten Protokollen kennen
> - Vorteile von SOA benennen können
> - Zusammenhang mit Microservices verstehen

## Einleitung

SOA (Service Oriented Architecture) ist ein Organisationskonzept für verteilte Systeme. Anders als RPC, REST oder SOAP ist SOA kein Protokoll, sondern ein Architekturparadigma, das beschreibt, wie Dienste in einem Netzwerk organisiert und bereitgestellt werden.

> [!important] Kernkonzept
> In SOA werden Dienste nicht "nur" angeboten – der Server **veröffentlicht**, dass er diese Dienste anbietet, etwa in einem **Verzeichnisdienst** (Service Registry). Clients können dann dynamisch nach benötigten Diensten suchen und diese nutzen.

> [!example] Analogie
> SOA funktioniert wie ein Branchenbuch (Gelbe Seiten): Anbieter tragen ihre Dienste ein (Service Provider), das Branchenbuch verwaltet die Einträge (Service Registry), und Kunden suchen darin nach dem passenden Anbieter (Service Consumer). Der Kunde muss nicht im Voraus wissen, welcher Anbieter existiert – er schlägt einfach nach.

## SOA-Dreiecksmodell

![[soa-dreieck.png]]
*<span class="fig-id">04-02-05-soa-dreieck</span>: SOA-Dreiecksmodell – publish, lookup, bind*

### Komponenten

| Komponente | Rolle | Beispiel |
|------------|-------|----------|
| **Service Provider** | Bietet Dienste an und registriert sie | Webserver, API-Server |
| **Service Registry** | Verzeichnis aller verfügbaren Dienste | UDDI, DNS SRV, Consul |
| **Service Consumer** | Sucht und nutzt Dienste | Client-Anwendung |

## Ziele von SOA

SOA zielt auf:

- **Wiederverwendung von Code**: Services können von mehreren Anwendungen genutzt werden
- **Größere Flexibilität**: Lose Kopplung ermöglicht Änderungen ohne Auswirkungen auf andere Systeme
- **Skalierbarkeit**: Services können unabhängig skaliert werden
- **Höhere Zuverlässigkeit**: Ausfälle einzelner Services beeinträchtigen nicht das Gesamtsystem
- **Bessere Verfügbarkeit**: Services können redundant bereitgestellt werden

## Praktische Implementierungen

### DNS Service Location Records (SRV)

Ein praktisches Beispiel für Service Discovery:

```
_http._tcp.abc.com. IN SRV 0 5 80 ws1.abc.com.
```

Dieses SRV-Record ordnet einen HTTP-Service (`_http._tcp`) der Domain `abc.com` dem Server `ws1.abc.com` auf Port 80 zu.

### Moderne Implementierungen

| System | Beschreibung |
|--------|--------------|
| **Kubernetes Service Discovery** | Container-native Service Registry |
| **Consul** | Service Mesh mit Health Checks |
| **etcd** | Distributed Key-Value Store |
| **Apache ZooKeeper** | Koordination verteilter Systeme |
| **Active Directory** | Windows-basiertes Service Location |

## SOA und Microservices

Microservices sind eine moderne Ausprägung des SOA-Paradigmas:

| Aspekt | Klassische SOA | Microservices |
|--------|----------------|---------------|
| **Granularität** | Grobkörnig | Feinkörnig |
| **Kommunikation** | ESB (Enterprise Service Bus) | Direkt (REST, gRPC) |
| **Daten** | Gemeinsame Datenbank möglich | Eigene Datenbank pro Service |
| **Deployment** | Oft gemeinsam | Unabhängig |
| **Technologie** | Homogen | Polyglott |

---

## Enterprise Service Bus (ESB)

> [!important] Zentrale Komponente klassischer SOA
> Der **ESB** ist ein Middleware-System, das als zentrale Drehscheibe für die Kommunikation zwischen Services dient.

### Funktionen des ESB

| Funktion | Beschreibung |
|----------|--------------|
| **Routing** | Nachrichten zum richtigen Empfänger leiten |
| **Transformation** | Datenformate konvertieren (XML ↔ JSON) |
| **Orchestrierung** | Mehrere Services zu einem Workflow verbinden |
| **Protokoll-Bridging** | HTTP ↔ JMS ↔ SOAP ↔ ... |
| **Monitoring** | Zentrale Überwachung aller Kommunikation |
| **Security** | Authentifizierung, Autorisierung |

### ESB-Architektur

![[esb-architektur.png]]
*<span class="fig-id">04-02-05-esb-architektur</span>: Enterprise Service Bus als zentrale Middleware*

### Kritik am ESB

- **Single Point of Failure**: ESB-Ausfall legt alles lahm
- **Bottleneck**: Alle Kommunikation geht durch eine Stelle
- **Komplexität**: ESB-Konfiguration wird zum Monolithen
- **Vendor Lock-in**: Proprietäre ESB-Produkte

---

## API Gateway

> [!tip] Modernes Pendant zum ESB
> Das **API Gateway** übernimmt viele ESB-Funktionen, aber ohne die zentrale Orchestrierungslogik.

### Funktionen

| Funktion | API Gateway | ESB |
|----------|-------------|-----|
| Routing | ✓ | ✓ |
| Authentifizierung | ✓ | ✓ |
| Rate Limiting | ✓ | Teilweise |
| Protokoll-Transformation | Einfach | Komplex |
| Orchestrierung | ✗ | ✓ |
| Business-Logik | ✗ | ✓ |

### Bekannte API Gateways

- **Kong**: Open Source, Lua/Nginx-basiert
- **AWS API Gateway**: Managed Service
- **Apigee**: Google Cloud, Enterprise-Features
- **Traefik**: Cloud-native, Kubernetes-Integration

---

## Service Mesh

> [!important] Die nächste Evolution nach API Gateway
> Ein **Service Mesh** ist eine dedizierte Infrastrukturschicht für Service-zu-Service-Kommunikation in Microservices-Architekturen.

### Architektur: Sidecar-Pattern

![[service-mesh.png]]
*<span class="fig-id">04-02-05-service-mesh</span>: Service Mesh mit Sidecar-Proxies und Control Plane*

### Funktionen

| Funktion | Beschreibung |
|----------|--------------|
| **mTLS** | Automatische Verschlüsselung zwischen Services |
| **Traffic Management** | Canary Releases, A/B Testing, Retries |
| **Observability** | Distributed Tracing, Metriken, Logs |
| **Resilience** | Circuit Breaker, Timeouts, Rate Limiting |
| **Policy Enforcement** | Autorisierung auf Service-Ebene |

### Bekannte Service Meshes

| Produkt | Beschreibung |
|---------|--------------|
| **Istio** | Feature-reich, Kubernetes-native |
| **Linkerd** | Leichtgewichtig, einfacher |
| **Consul Connect** | HashiCorp, Multi-Plattform |
| **AWS App Mesh** | AWS-managed |

### Wann Service Mesh?

Service Meshes lohnen sich bei:
- Vielen Services (>10-20)
- Hohen Security-Anforderungen
- Komplexem Traffic Management
- Bedarf an Observability

Für kleinere Systeme ist der Overhead oft zu hoch.

## Zusammenhänge

| Beziehung | Konzept | Beschreibung |
|-----------|---------|--------------|
| Nutzt | [[03-REST]] | Häufiges Protokoll für Services |
| Nutzt | [[04-SOAP]] | Enterprise-Protokoll für Services |
| Moderne Form | Microservices | Feinkörnige, unabhängige Services |
| Erfordert | Service Discovery | DNS SRV, Kubernetes, Consul |

---

> [!warning] **Prüfungsrelevant**
> - SOA-Dreiecksmodell (Provider, Registry, Consumer)
> - Unterschied SOA vs. Protokoll (SOA ist Architekturparadigma)
> - Vorteile: Wiederverwendung, Flexibilität, Skalierbarkeit
> - Zusammenhang SOA und Microservices

> [!question] **Typische Prüfungsfragen**
> - Erklären Sie das SOA-Dreiecksmodell (Provider, Registry, Consumer).
> - Was unterscheidet SOA von einem Protokoll wie SOAP?
> - Welche Vorteile bietet SOA?
> - Warum ist ein Verzeichnisdienst wichtig für SOA?
> - Wie hängen SOA und Microservices zusammen?

> [!tip] **Merkhilfe**
> **SOA = Gelbe Seiten für Services**:
> - **S**ervices werden veröffentlicht (publish)
> - **O**rganisiert in einem Verzeichnis (registry)
> - **A**bgerufen bei Bedarf (lookup + bind)

---

## Weiterführende Ressourcen

- [[03-REST]] – Häufiges Protokoll für SOA
- [[04-SOAP]] – Enterprise-Protokoll für SOA
- [[01-RPC]] – Grundlegendes Kommunikationskonzept

---

## Quellen

- Erl, T. (2007). *SOA Principles of Service Design*. Prentice Hall.
- OASIS (2006). Reference Model for Service Oriented Architecture 1.0.
- Newman, S. (2015). *Building Microservices*. O'Reilly Media.
- Fowler, M. (2014). Microservices – a definition of this new architectural term. martinfowler.com.
