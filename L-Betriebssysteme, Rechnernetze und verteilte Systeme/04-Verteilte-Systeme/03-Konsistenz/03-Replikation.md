---
author: Andreas Hümmer
title: Replikation
tags:
  - content
  - vs
  - konsistenz
  - replikation
  - redundanz
  - verfuegbarkeit
created: '2026-10-07'
modified: '2026-10-13'
bereich: VS
---

# Replikation

> [!info] Lernziele
> - Replikationsstrategien und ihre Trade-offs verstehen
> - Synchrone vs. asynchrone Replikation unterscheiden
> - Quorum-basierte Replikation erklären können
> - Primary-Backup vs. Multi-Primary Architekturen kennen

## Einleitung

Replikation ist das Speichern von Kopien derselben Daten auf mehreren Knoten eines verteilten Systems. Sie dient der Erhöhung von Verfügbarkeit, Fehlertoleranz und Leseperformance.

> [!important] Kernkonzept
> Replikation schafft **Redundanz**: Dieselben Daten existieren auf mehreren Knoten. Der Trade-off liegt zwischen **Konsistenz** (alle Kopien synchron halten) und **Performance/Verfügbarkeit** (nicht auf alle Kopien warten). Die Wahl der Replikationsstrategie bestimmt das Verhalten des Systems im Fehlerfall.

> [!example] Analogie
> Replikation ist wie das Führen von Kopien eines wichtigen Dokuments: **Synchrone Replikation** entspricht einem Notar, der erst bestätigt, wenn alle Parteien unterschrieben haben – sicher, aber langsam. **Asynchrone Replikation** ist wie eine E-Mail an alle mit dem Dokument – schnell, aber ohne Garantie, dass alle es sofort gelesen haben.

## Replikationsstrategien

### Synchron vs. Asynchron

```mermaid
sequenceDiagram
    participant C as Client
    participant P as Primary
    participant R1 as Replica 1
    participant R2 as Replica 2
    
    Note over C,R2: Synchrone Replikation
    C->>P: Write
    P->>R1: Replicate
    P->>R2: Replicate
    R1-->>P: ACK
    R2-->>P: ACK
    P-->>C: Commit
    
    Note over C,R2: Asynchrone Replikation
    C->>P: Write
    P-->>C: Commit
    P->>R1: Replicate (später)
    P->>R2: Replicate (später)
```

| Aspekt | Synchron | Asynchron |
|--------|----------|-----------|
| **Latenz** | Höher (wartet auf alle) | Niedriger |
| **Konsistenz** | Strong | Eventual |
| **Verfügbarkeit** | Niedriger bei Ausfällen | Höher |
| **Datenverlust** | Kein | Möglich bei Failover |

### Primary-Backup vs. Multi-Primary

| Architektur | Beschreibung | Vorteile | Nachteile |
|-------------|--------------|----------|-----------|
| **Primary-Backup** | Ein Primary für Schreiboperationen | Einfach, keine Konflikte | Single Point of Failure, Failover nötig |
| **Multi-Primary** | Mehrere Knoten akzeptieren Writes | Höhere Verfügbarkeit | Konfliktauflösung nötig |

```mermaid
graph LR
    subgraph pb["Primary-Backup"]
        P[Primary] --> R1[Replica]
        P --> R2[Replica]
        Client1[Client] --> P
    end
    
    subgraph mp["Multi-Primary"]
        P1[Primary 1] <--> P2[Primary 2]
        P1 <--> P3[Primary 3]
        P2 <--> P3
        Client2[Client] --> P1
        Client3[Client] --> P2
    end
```

## Quorum-basierte Replikation

Bei N Replikaten:
- **W** = Anzahl Knoten, die bei Write bestätigen müssen
- **R** = Anzahl Knoten, die bei Read abgefragt werden

> [!warning] Quorum-Formel
> **R + W > N** garantiert, dass mindestens ein Knoten bei Read den aktuellen Wert hat.

### Konfigurationsbeispiele (N=3)

| Konfiguration | W | R | Eigenschaften |
|---------------|---|---|---------------|
| **Write-optimiert** | 1 | 3 | Schnelle Writes, langsame Reads |
| **Read-optimiert** | 3 | 1 | Langsame Writes, schnelle Reads |
| **Balanced** | 2 | 2 | Kompromiss |

```mermaid
graph TD
    subgraph quorum["Quorum (N=3, W=2, R=2)"]
        N1[Node 1 ✓]
        N2[Node 2 ✓]
        N3[Node 3]
        
        W["Write: 2 von 3 ACK"]
        R["Read: 2 von 3 abfragen"]
    end
```

## Vor- und Nachteile

### Vorteile

- **Verfügbarkeit**: System läuft bei Knotenausfällen weiter
- **Performance**: Lesezugriffe können lokal bedient werden
- **Latenz**: Geografisch verteilte Replikate reduzieren Netzwerklatenz
- **Lastverteilung**: Anfragen auf mehrere Knoten verteilen

### Nachteile

- **Komplexität**: Synchronisation und Konfliktauflösung nötig
- **Speicher**: Mehrfache Datenhaltung
- **Konsistenz**: Trade-off mit Performance
- **Bandbreite**: Replikationstraffic

## Zusammenhänge

```mermaid
graph TD
    REP[Replikation] --> |"Trade-off"| CAP[CAP-Theorem]
    REP --> |"beeinflusst"| KM[Konsistenzmodelle]
    REP --> |"erfordert"| SYNC[Synchronisation]
    REP --> |"erhöht"| AVAIL[Verfügbarkeit]
    QUORUM[Quorum] --> |"Strategie für"| REP
    
    style REP fill:#4a86e8,color:#fff
```

---

## Prüfungstipps

> [!warning] Häufige Prüfungsfragen
> - Vergleichen Sie synchrone und asynchrone Replikation
> - Erklären Sie die Quorum-Formel R + W > N
> - Was sind Vor- und Nachteile von Primary-Backup?

> [!question] Verständnisfragen
> - Wann kann bei asynchroner Replikation Datenverlust auftreten?
> - Wie löst Multi-Primary Schreibkonflikte?
> - Warum garantiert R + W > N Konsistenz?

> [!tip] Merkhilfe
> **Quorum-Formel**: R + W > N
> - Bei N=3: Wenn W=2 und R=2, dann 2+2=4 > 3 ✓
> - Mindestens ein Knoten hat bei jedem Read den aktuellen Wert
> 
> **Eselsbrücke**: "Read plus Write muss größer als die Anzahl Nodes sein"

---

## Weiterführende Ressourcen

- [[01-CAP-Theorem]] – Trade-offs bei Replikation
- [[02-Konsistenzmodelle]] – Konsistenzgarantien
- [[../04-Koordination/03-Konsensalgorithmen]] – Koordination zwischen Replikaten

---

## Quellen

Die Inhalte basieren auf dem Kurshandbuch "Betriebssysteme, Rechnernetze und verteilte Systeme" der IU Internationalen Hochschule sowie den zugehörigen Vorlesungsmaterialien.
