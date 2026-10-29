---
author: Andreas Hümmer
title: Die 8 Fallacies of Distributed Computing
tags:
  - content
  - vs
  - grundlagen
  - fallacies
  - netzwerk
created: '2026-10-07'
modified: '2026-10-29'
bereich: VS
---

# Die 8 Fallacies of Distributed Computing

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Alle acht Fallacies benennen und erklären können
> - Die praktischen Auswirkungen jeder Fallacy verstehen
> - Gegenmaßnahmen für jede Fallacy kennen
> - Verstehen, warum diese Irrtümer so verbreitet sind

---

## Was sind die Fallacies?

> [!important] **Kernkonzept**
> Die **Fallacies of Distributed Computing** sind acht falsche Annahmen, die Entwickler häufig über verteilte Systeme machen. Sie wurden in den 1990er Jahren von Peter Deutsch und anderen bei Sun Microsystems formuliert und sind bis heute hochrelevant.

Diese Irrtümer sind so verbreitet, weil sie bei der **lokalen Entwicklung** zutreffen: Auf dem eigenen Rechner ist das Netzwerk zuverlässig (localhost), die Latenz ist vernachlässigbar, und es gibt nur einen Administrator (du selbst). Erst beim Deployment in Produktionsumgebungen zeigen sich die Probleme – oft erst unter Last oder bei Teilausfällen.

---

## Die acht Irrtümer im Detail

### 1. Das Netzwerk ist zuverlässig

> [!quote] **Fallacy 1**
> "The network is reliable."

**Realität:** Netzwerke fallen aus. Pakete gehen verloren. Verbindungen werden unterbrochen. Kabel werden durchtrennt. Router stürzen ab. Cloud-Regionen haben Ausfälle.

**Auswirkungen:**
- Requests können spurlos verschwinden
- Responses können verloren gehen (Request kam an, aber Antwort nicht)
- Verbindungen können mitten in einer Transaktion abbrechen

**Gegenmaßnahmen:**
- **Timeouts** für alle Netzwerkoperationen
- **Retry-Logik** mit exponential backoff
- **Idempotente Operationen** (mehrfaches Ausführen hat gleichen Effekt)
- **Circuit Breaker Pattern** zum Schutz vor kaskadierende Ausfällen
- **Health Checks** und automatisches Failover

> [!example] **Praxisbeispiel**
> Ein Online-Shop sendet eine Bestellung an das Payment-System. Die Zahlung wird durchgeführt, aber die Bestätigung geht verloren. Ohne idempotente Operationen würde ein Retry die Zahlung doppelt ausführen.

---

### 2. Latenz ist null

> [!quote] **Fallacy 2**
> "Latency is zero."

**Realität:** Jeder Netzwerkaufruf kostet Zeit – typischerweise 1-100ms im lokalen Netzwerk, 50-300ms über das Internet, und 500ms+ bei mobilen Verbindungen oder Satellitenlinks.

**Auswirkungen:**
- Viele kleine Requests summieren sich (N+1 Problem)
- Synchrone Aufrufe blockieren und verschwenden Ressourcen
- User Experience leidet bei "chatty" Protokollen

**Gegenmaßnahmen:**
- **Batching**: Mehrere Operationen zu einem Request zusammenfassen
- **Caching**: Häufig benötigte Daten lokal speichern
- **Asynchrone Kommunikation**: Nicht auf Antworten warten
- **CDNs** (Content Delivery Networks): Daten näher zum Nutzer bringen
- **Prefetching**: Daten laden, bevor sie gebraucht werden

> [!example] **Praxisbeispiel**
> Eine Webseite lädt für jedes Produkt einzeln die Bewertungen nach (100 Produkte × 50ms = 5 Sekunden). Mit Batching: ein Request für alle Bewertungen (50ms).

---

### 3. Bandbreite ist unendlich

> [!quote] **Fallacy 3**
> "Bandwidth is infinite."

**Realität:** Bandbreite ist begrenzt und oft geteilt. Mobile Verbindungen haben enge Limits. Auch in Rechenzentren kann Bandbreite zum Engpass werden, besonders bei Big-Data-Workloads.

**Auswirkungen:**
- Große Datenmengen blockieren das Netzwerk
- Andere Dienste werden ausgebremst
- Kosten für Datenübertragung (Cloud-Egress ist teuer!)

**Gegenmaßnahmen:**
- **Komprimierung** von Daten (gzip, Protocol Buffers statt JSON)
- **Pagination**: Nur benötigte Datenmengen übertragen
- **Streaming** statt vollständiger Downloads
- **Delta-Synchronisation**: Nur Änderungen übertragen
- **Data Locality**: Verarbeitung dorthin bringen, wo die Daten sind

> [!example] **Praxisbeispiel**
> Ein Microservice gibt bei jeder Abfrage das vollständige Kundenobjekt zurück (5 KB), obwohl der Aufrufer nur den Namen braucht (50 Bytes). Bei 1 Million Anfragen pro Tag: 5 GB statt 50 MB.

---

### 4. Das Netzwerk ist sicher

> [!quote] **Fallacy 4**
> "The network is secure."

**Realität:** Netzwerke können abgehört, manipuliert und angegriffen werden. Auch interne Netzwerke sind nicht automatisch sicher ("Zero Trust").

**Auswirkungen:**
- Daten können mitgelesen werden (Man-in-the-Middle)
- Requests können gefälscht werden
- Denial-of-Service-Angriffe sind möglich

**Gegenmaßnahmen:**
- **TLS/HTTPS** für alle Verbindungen (auch intern!)
- **Authentifizierung** für jeden Service (mTLS, JWT)
- **Autorisierung**: Principle of Least Privilege
- **Input Validation**: Niemals Eingaben vertrauen
- **Rate Limiting** und DDoS-Schutz
- **Netzwerksegmentierung** und Firewalls

> [!example] **Praxisbeispiel**
> Ein interner Service kommuniziert unverschlüsselt mit der Datenbank. Ein Angreifer, der Zugang zum Netzwerk hat (z.B. kompromittierter Server), kann alle Queries und Passwörter mitlesen.

---

### 5. Die Topologie ändert sich nicht

> [!quote] **Fallacy 5**
> "Topology doesn't change."

**Realität:** Server werden hinzugefügt, entfernt, verschoben. IP-Adressen ändern sich. Cloud-Instanzen sind ephemeral. Container starten und stoppen ständig.

**Auswirkungen:**
- Hardcodierte IP-Adressen funktionieren nicht mehr
- Statische Konfigurationen werden ungültig
- Verbindungen zu "verschwundenen" Servern schlagen fehl

**Gegenmaßnahmen:**
- **Service Discovery** (Consul, etcd, Kubernetes DNS)
- **Load Balancer** als stabile Endpunkte
- **DNS-basierte** Auflösung statt IP-Adressen
- **Health Checks** und automatische Deregistrierung
- **Konfiguration aus dem Code** heraushalten (Environment Variables, Config Servers)

> [!example] **Praxisbeispiel**
> Ein Service verbindet sich zu `192.168.1.50` (Datenbank-Server). Nach einem Wartungsfenster hat der Server eine neue IP. Alle Services müssen manuell neu konfiguriert werden – mitten in der Nacht.

---

### 6. Es gibt einen Administrator

> [!quote] **Fallacy 6**
> "There is one administrator."

**Realität:** Verteilte Systeme spannen oft mehrere Organisationen, Teams und Zuständigkeitsbereiche. Jeder hat andere Prioritäten, Wartungsfenster und Policies.

**Auswirkungen:**
- Koordination über Teamgrenzen hinweg ist schwierig
- Unterschiedliche Security-Policies und Compliance-Anforderungen
- Keine zentrale Kontrolle über alle Komponenten

**Gegenmaßnahmen:**
- **Klare Schnittstellen** (APIs) zwischen Verantwortungsbereichen
- **SLAs** (Service Level Agreements) definieren
- **Dokumentation** von Abhängigkeiten
- **Monitoring** das Teamgrenzen überspannt
- **Incident Management** mit klaren Eskalationspfaden

> [!example] **Praxisbeispiel**
> Dein Service nutzt eine API eines anderen Teams. Sie deployen ein Breaking Change am Freitagabend. Dein Service fällt aus, aber du erreichst niemanden – das andere Team hat Betriebsferien.

---

### 7. Transportkosten sind null

> [!quote] **Fallacy 7**
> "Transport cost is zero."

**Realität:** Datenübertragung kostet – in CPU-Zyklen (Serialisierung/Deserialisierung), in Latenz, und in echtem Geld (Cloud-Egress-Kosten, mobile Datenvolumen).

**Auswirkungen:**
- JSON-Parsing kann CPU-intensiv sein
- Verschlüsselung kostet Performance
- Cloud-Rechnungen explodieren bei hohem Datenvolumen

**Gegenmaßnahmen:**
- **Effiziente Serialisierung** (Protocol Buffers, MessagePack statt JSON)
- **Verbindungs-Pooling** (Connections wiederverwenden)
- **HTTP/2 oder gRPC** für effizientere Protokolle
- **Kostenmonitoring** für Cloud-Ressourcen
- **Daten dort verarbeiten, wo sie entstehen** (Edge Computing)

> [!example] **Praxisbeispiel**
> Ein Service in AWS eu-west-1 ruft ständig Daten aus us-east-1 ab. Neben der Latenz (80ms pro Aufruf) kostet jedes GB übertragener Daten $0.02. Bei 10 TB/Monat: $200 nur für Datenübertragung.

---

### 8. Das Netzwerk ist homogen

> [!quote] **Fallacy 8**
> "The network is homogeneous."

**Realität:** Netzwerke bestehen aus unterschiedlicher Hardware, Software, Protokollen und Konfigurationen. Verschiedene Clients haben verschiedene Fähigkeiten.

**Auswirkungen:**
- Unterschiedliche MTU-Größen können zu Fragmentierung führen
- Nicht alle Clients unterstützen alle Protokolle
- Firewalls und Proxies können Verbindungen modifizieren

**Gegenmaßnahmen:**
- **Standardprotokolle** verwenden (HTTP, gRPC)
- **Graceful Degradation**: Fallbacks für ältere Clients
- **Feature Detection** statt Feature Assumption
- **Versionierte APIs** für Abwärtskompatibilität
- **Testen in realistischen Umgebungen** (nicht nur localhost)

> [!example] **Praxisbeispiel**
> Eine WebSocket-Verbindung funktioniert perfekt im Büro, aber bei manchen Kunden nicht – deren Corporate Proxy unterstützt kein WebSocket-Upgrade. Die App braucht einen HTTP-Long-Polling-Fallback.

---

## Zusammenfassung

| # | Fallacy | Realität | Wichtigste Gegenmaßnahme |
|---|---------|----------|--------------------------|
| 1 | Netzwerk ist zuverlässig | Ausfälle passieren | Timeouts + Retries + Idempotenz |
| 2 | Latenz ist null | 1-500ms pro Aufruf | Batching + Caching |
| 3 | Bandbreite ist unendlich | Begrenzt und teuer | Komprimierung + Pagination |
| 4 | Netzwerk ist sicher | Angriffe sind real | TLS + Authentifizierung |
| 5 | Topologie ändert sich nicht | Ständige Änderungen | Service Discovery |
| 6 | Ein Administrator | Viele Verantwortliche | SLAs + Dokumentation |
| 7 | Transportkosten sind null | CPU + Latenz + Geld | Effiziente Serialisierung |
| 8 | Netzwerk ist homogen | Verschiedene Systeme | Standards + Fallbacks |

---

## Zusammenhänge

Die acht Fallacies lassen sich in vier Kategorien einordnen:

| Kategorie | Fallacies |
|-----------|-----------|
| **Netzwerk** | #1 Zuverlässigkeit, #5 Topologie, #8 Homogenität |
| **Performance** | #2 Latenz, #3 Bandbreite, #7 Transportkosten |
| **Sicherheit** | #4 Netzwerksicherheit |
| **Betrieb** | #6 Administrator |

- [[01-Definition|Definition]] → Grundlegende Begriffe
- [[02-Eigenschaften|Eigenschaften]] → Was verteilte Systeme können sollten
- [[../02-Kommunikation/00-Kommunikation-Index|Kommunikation]] → Wie man trotzdem kommuniziert
- [[../03-Konsistenz/01-CAP-Theorem|CAP-Theorem]] → Weitere fundamentale Trade-offs

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
NA

> [!question] **Häufige Prüfungsfragen**
> 1. Nennen Sie die 8 Fallacies of Distributed Computing.
> 2. Warum ist die Annahme "Latenz ist null" problematisch?
> 3. Welche Gegenmaßnahmen gibt es gegen Netzwerkausfälle?
> 4. Was bedeutet "Topology doesn't change" und warum ist das falsch?
> 5. Erklären Sie das Circuit Breaker Pattern.

> [!tip] **Merkhilfen**
> **Eselsbrücke für die Reihenfolge:**
> "**R**eally **L**arge **B**andwidth **S**urely **T**akes **O**ne **T**o **H**eaven"
> - **R**eliable, **L**atency, **B**andwidth, **S**ecure, **T**opology, **O**ne admin, **T**ransport cost, **H**omogeneous

---

## Weiterführende Ressourcen

> [!note] **Literatur**
> - Deutsch, Peter: "The Eight Fallacies of Distributed Computing" (Original-Artikel)
> - Nygard, Michael: "Release It!" – Praxisbuch zu Resilience Patterns
> - Newman, Sam: "Building Microservices" – Kapitel zu Netzwerk-Resilienz

> [!tip] **Praktische Übungen**
> - **Chaos Engineering**: Mit Tools wie Chaos Monkey Ausfälle simulieren
> - **Network Simulation**: Mit tc (traffic control) Latenz und Paketverlust simulieren
> - **Wireshark**: Netzwerkverkehr analysieren und verstehen

---

## Quellen

- Deutsch, Peter: The Eight Fallacies of Distributed Computing – Die originale Formulierung der Fallacies bei Sun Microsystems.
- Rotem-Gal-Oz, Arnon: Fallacies of Distributed Computing Explained – Ausführliche Erklärung mit Beispielen.
- Nygard, Michael: Release It! – Praktische Patterns für resiliente Systeme.
