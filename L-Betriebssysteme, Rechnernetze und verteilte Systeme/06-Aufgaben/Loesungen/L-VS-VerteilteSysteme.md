---
author: Andreas Hümmer
title: 'Lösung: Verteilte Systeme (Klausurformat)'
tags:
  - loesung
  - vs
  - klausur
bereich: VS
created: '2026-11-01'
modified: '2026-11-01'
---

# Lösung: Verteilte Systeme (Klausurformat)

**Zugehörige Übung:** [[UE-VS-VerteilteSysteme|Übung: Verteilte Systeme (Klausurformat)]]

---

## Teil 1: Grundlagen und Definition (20 Punkte)

### Aufgabe 1.1: Definitionen verteilter Systeme (6 Punkte)

**a) Definition nach Tanenbaum:**

> [!success] **Musterlösung**
> *"Verteilte Systeme sind eine Sammlung von unabhängigen Computern, die sich gegenüber dem Anwender als ein kohärentes System darstellen."*
> 
> Diese Definition betont die **Benutzerperspektive**: Egal wie viele Server im Hintergrund arbeiten – für den Anwender erscheint alles als eine Einheit.

**b) Definitionen nach Bal und Lamport:**

> [!success] **Musterlösung**
> | Autor | Definition/Kernaussage |
> |-------|------------------------|
> | **Bal** | Ein verteiltes Computersystem besteht aus mehreren autonomen Prozessoren, die sich keinen Hauptspeicher teilen, aber mittels Austausch von Nachrichten über ein Netzwerk miteinander kooperieren. → Betont die **technische Architektur**: Kein Shared Memory, Kommunikation nur über Nachrichten. |
> | **Lamport** | Ein verteiltes System ist es, wenn ein Fehler eines Computers, von dessen Existenz du nichts wusstest, deinen eigenen Rechner unbrauchbar macht. → Betont die **Komplexität**: Versteckte Abhängigkeiten machen Debugging besonders herausfordernd. |

---

### Aufgabe 1.2: Die vier Hauptmerkmale (5 Punkte)

> [!success] **Musterlösung**
> | Merkmal | Beschreibung |
> |---------|--------------|
> | 1. **Skalierbarkeit** | Ein verteiltes System kann (beliebig) mit zusätzlichen Ressourcen erweitert werden, wobei die Art der Ressourcen sehr heterogen sein kann. |
> | 2. **Nebenläufigkeit** | Auf Basis von Synchronisationsalgorithmen können Teilaufgaben koordiniert auf verschiedenen Systemen parallel abgearbeitet werden. |
> | 3. **Fehlertoleranz** | Resilienz ist ein zwingendes Grundprinzip, da aufgrund der Verteilung und der umfangreichen Kommunikation häufig Fehler auftreten können. |
> | 4. **Transparenz** | Für den Benutzer ist nicht ersichtlich, wie die Aufgaben auf die Ressourcen verteilt werden und wo sich diese befinden. |

---

### Aufgabe 1.3: Distributed vs. Parallel Computing (5 Punkte)

> [!success] **Musterlösung**
> | Kriterium | Distributed Computing | Parallel Computing |
> |-----------|----------------------|-------------------|
> | **Kopplung** | Lose gekoppelt – Nodes agieren autonom und unabhängig | Eng gekoppelt – CPUs arbeiten koordiniert zusammen |
> | **Speicher** | Kein gemeinsamer Speicher – jeder Node hat eigenen Speicher | Shared Memory – alle CPUs teilen sich denselben Speicher |
> | **Kommunikation** | Über Netzwerk (Nachrichtenaustausch) – explizit und asynchron | Über Bus/Speicher – direkt durch Lesen/Schreiben gemeinsamer Variablen |
> 
> **Konsequenz:** Verteilte Systeme skalieren besser, müssen aber mit Netzwerklatenz und Partitionierung umgehen.

---

### Aufgabe 1.4: Fat-Client vs. Thin-Client (4 Punkte)

> [!success] **Musterlösung**
> | Aspekt | Fat-Client | Thin-Client |
> |--------|------------|-------------|
> | **Logik** | Viel Anwendungslogik läuft lokal auf dem Client | Minimale Logik lokal, Server macht die Verarbeitung |
> | **Wartung** | Aufwändig – Updates müssen auf alle Clients verteilt werden | Einfach – zentrale Updates auf dem Server |
> | **Offline-Fähigkeit** | Gut – kann ohne Server arbeiten | Schlecht – abhängig von Serververbindung |
> | **Beispiel** | Desktop-Anwendungen (Word, Outlook), Native Mobile Apps | Webbrowser, Terminal-Clients |

---

## Teil 2: Kommunikation in Verteilten Systemen (25 Punkte)

### Aufgabe 2.1: RPC-Ablauf (5 Punkte)

> [!success] **Musterlösung**
> | Schritt | Beschreibung |
> |---------|--------------|
> | 1 | **Client-Aufruf:** Der Client ruft eine lokale Stub-Funktion auf (sieht aus wie lokaler Aufruf) |
> | 2 | **Marshalling:** Parameter werden serialisiert (in Netzwerkformat umgewandelt) |
> | 3 | **Übertragung:** Request wird über das Netzwerk zum Server gesendet |
> | 4 | **Server-Verarbeitung:** Server-Stub deserialisiert Parameter, führt die eigentliche Prozedur aus |
> | 5 | **Rückgabe:** Ergebnis wird serialisiert und an den Client zurückgesendet, Client-Stub deserialisiert das Ergebnis |

---

### Aufgabe 2.2: Idempotenz (4 Punkte)

**a) Definition von Idempotenz:**

> [!success] **Musterlösung**
> **Idempotenz** im Kontext von RPC bedeutet: Mehrfaches Ausführen einer Operation hat denselben Effekt wie einmaliges Ausführen. Dies ist kritisch bei Retries nach Timeouts – wenn ein Client nach einem Timeout den Request wiederholt, kann es sein, dass der ursprüngliche Request doch verarbeitet wurde. Ohne Idempotenz führt das zu Problemen (z.B. doppelte Buchungen).

**b) Einordnung der Operationen:**

> [!success] **Musterlösung**
> | Operation | Idempotent? (Ja/Nein) | Begründung |
> |-----------|----------------------|------------|
> | GET /user/123 | Ja | Lesen verändert keine Daten, mehrfaches Lesen liefert dasselbe Ergebnis |
> | balance += 10 | Nein | Mehrfaches Ausführen erhöht den Kontostand jedes Mal um 10 |
> | DELETE /user/123 | Ja | Nach dem ersten Löschen ist der User weg, weitere Löschversuche ändern nichts mehr |
> | POST /orders | Nein | Jeder Aufruf erstellt eine neue Bestellung |

---

### Aufgabe 2.3: HTTP-Methoden und REST (5 Punkte)

> [!success] **Musterlösung**
> | Methode | Beschreibung | Idempotent? |
> |---------|--------------|-------------|
> | **GET** | Liefert den Inhalt einer Ressource – nur lesend | Ja |
> | **POST** | Sendet Daten zur Verarbeitung an den Server – erstellt neue Ressourcen | Nein |
> | **PUT** | Speichert/ersetzt eine Ressource vollständig unter der angegebenen URI | Ja |
> | **DELETE** | Löscht die angegebene Ressource | Ja |
> | **PATCH** | Partielle Aktualisierung einer Ressource – nur einzelne Felder ändern | Nein |

---

### Aufgabe 2.4: REST vs. SOAP (5 Punkte)

> [!success] **Musterlösung**
> | Kriterium | REST | SOAP |
> |-----------|------|------|
> | **Typ** | Architekturstil – kein festes Protokoll, nutzt HTTP-Methoden | Protokoll – streng definierte Nachrichtenstruktur (Envelope, Header, Body) |
> | **Format** | Flexibel: JSON, XML, andere | Nur XML (strikt strukturiert) |
> | **Bandbreite/Overhead** | Leichtgewichtig, geringer Overhead | Ressourcenintensiv, XML-Overhead erhöht Datenmenge |
> | **Sicherheit** | HTTPS, OAuth – auf Transportebene | WS-Security – End-to-End auf Nachrichtenebene (gilt als sicherer für Enterprise) |
> | **Caching** | Unterstützt (HTTP-Caching) | Nicht direkt möglich |

---

### Aufgabe 2.5: SOA-Dreiecksmodell (3 Punkte)

> [!success] **Musterlösung**
> | Komponente | Aufgabe |
> |------------|---------|
> | **Service Provider** | Bietet Dienste an und registriert sie im Verzeichnis (publish) |
> | **Service Registry** | Verzeichnis aller verfügbaren Dienste – ermöglicht dynamisches Finden von Services |
> | **Service Consumer** | Sucht benötigte Dienste im Verzeichnis (lookup) und nutzt sie (bind) |
> 
> Das Modell ermöglicht **lose Kopplung**: Der Consumer muss nicht im Voraus wissen, welche Provider existieren.

---

### Aufgabe 2.6: Synchrone vs. Asynchrone Kommunikation (3 Punkte)

> [!success] **Musterlösung**
> | Aspekt | Synchron (z.B. RPC) | Asynchron (z.B. Message Queue) |
> |--------|---------------------|-------------------------------|
> | **Blockierung** | Client blockiert und wartet auf Antwort des Servers | Client sendet Nachricht und arbeitet sofort weiter |
> | **Kopplung** | Engere Kopplung – beide Seiten müssen gleichzeitig verfügbar sein | Lose Kopplung – Sender und Empfänger können zeitlich entkoppelt sein |
> | **Anwendungsfall** | Direkte Anfragen, bei denen sofortige Antwort benötigt wird (z.B. Datenbankabfrage) | Hintergrundverarbeitung, Event-Driven Architectures, Lastspitzen abfangen |

---

## Teil 3: CAP-Theorem und Konsistenz (25 Punkte)

### Aufgabe 3.1: CAP-Theorem (6 Punkte)

> [!success] **Musterlösung**
> | Eigenschaft | Erklärung |
> |-------------|-----------|
> | **C**onsistency | Alle Knoten sehen zur gleichen Zeit dieselben Daten – jede Leseoperation liefert den Wert der letzten Schreiboperation (Linearisierbarkeit) |
> | **A**vailability | Jede Anfrage erhält eine (nicht-fehlerhafte) Antwort – ohne Garantie auf Aktualität. Das System antwortet auch bei Teilausfällen. |
> | **P**artition Tolerance | Das System arbeitet trotz Nachrichtenverlust oder Netzwerkpartitionen weiter – Kommunikation zwischen Knoten kann unterbrochen sein |
> 
> **Kernaussage:** Ein verteiltes System kann höchstens zwei der drei Eigenschaften gleichzeitig garantieren. Da Partitionen unvermeidlich sind, liegt die reale Wahl zwischen C und A.

---

### Aufgabe 3.2: CP vs. AP Systeme (5 Punkte)

**a) CP-System:**

> [!success] **Musterlösung**
> Ein **CP-System** priorisiert **Consistency** und **Partition Tolerance**. Bei einer Netzwerkpartition opfert es die Verfügbarkeit: Das System verweigert Antworten oder blockiert, bis die Konsistenz wiederhergestellt ist. Motto: "Lieber nichts als Falsches."

**b) Einordnung der Systeme:**

> [!success] **Musterlösung**
> | System | CP oder AP? | Begründung |
> |--------|-------------|------------|
> | **ZooKeeper** | CP | Garantiert konsistente Konfigurationsdaten – bei Partition werden Schreiboperationen blockiert, bis ein Quorum erreicht ist |
> | **Cassandra** | AP | Priorisiert Verfügbarkeit – bei Partition arbeiten Knoten unabhängig weiter, Daten werden später synchronisiert (Eventual Consistency) |
> | **MongoDB (strict mode)** | CP | Im "strict mode" wartet MongoDB auf Bestätigung aller Replikate – bei Partition sinkt die Verfügbarkeit |

---

### Aufgabe 3.3: ACID-Eigenschaften (4 Punkte)

> [!success] **Musterlösung**
> | Eigenschaft | Beschreibung |
> |-------------|--------------|
> | **A**tomicity (Atomarität) | Transaktion ist entweder vollständig oder gar nicht – bei Fehlern wird der vorherige Zustand wiederhergestellt (Alles-oder-Nichts-Prinzip) |
> | **C**onsistency (Konsistenz) | Daten befinden sich immer in einem gültigen Zustand – Integritätsbedingungen werden eingehalten, keine Zwischenzustände sichtbar |
> | **I**solation (Isolierung) | Gleichzeitige Zugriffe beeinflussen sich nicht – parallele Transaktionen sehen sich gegenseitig nicht |
> | **D**urability (Dauerhaftigkeit) | Erfolgreiche Änderungen bleiben auch bei Systemausfällen bestehen – werden persistent gespeichert |

---

### Aufgabe 3.4: Strong vs. Eventual Consistency (5 Punkte)

> [!success] **Musterlösung**
> | Aspekt | Strong Consistency | Eventual Consistency |
> |--------|-------------------|---------------------|
> | **Garantie** | Neuester Wert wird sofort bei jedem Lesevorgang geliefert | Alle Replikate konvergieren irgendwann zum selben Zustand |
> | **Latenz** | Höher – Koordination zwischen Knoten erforderlich | Niedriger – keine Synchronisation vor Antwort |
> | **Verfügbarkeit bei Partition** | Eingeschränkt – System blockiert für Konsistenz | Bleibt verfügbar – Knoten arbeiten unabhängig weiter |
> | **Anwendungsbeispiel** | Bankensysteme, Finanztransaktionen, Inventar | Social Media Feeds, DNS, CDNs, Produktbewertungen |

---

### Aufgabe 3.5: Quorum-Berechnung (5 Punkte)

**a) Quorum-Formel:**

> [!success] **Musterlösung**
> Die Formel **R + W > N** garantiert, dass bei jedem Lesevorgang mindestens ein Knoten den aktuellen (zuletzt geschriebenen) Wert enthält. Die Schnittmenge zwischen Write-Quorum und Read-Quorum ist nie leer, wodurch Konsistenz sichergestellt wird.

**b) Berechnung der Konfigurationen (N=5):**

> [!success] **Musterlösung**
> | Konfiguration | W | R | R + W | > N? | Konsistent? |
> |---------------|---|---|-------|------|-------------|
> | Write-optimiert | 1 | 5 | 6 | 6 > 5 ✓ | Ja |
> | Read-optimiert | 5 | 1 | 6 | 6 > 5 ✓ | Ja |
> | Balanced | 3 | 3 | 6 | 6 > 5 ✓ | Ja |
> 
> Alle drei Konfigurationen garantieren Konsistenz, da R + W = 6 > 5 = N.

---

## Teil 4: Replikation (15 Punkte)

### Aufgabe 4.1: Synchrone vs. Asynchrone Replikation (5 Punkte)

> [!success] **Musterlösung**
> | Aspekt | Synchron | Asynchron |
> |--------|----------|-----------|
> | **Latenz** | Höher – wartet auf Bestätigung aller Replikate | Niedriger – kehrt sofort zurück |
> | **Konsistenz** | Strong Consistency – alle Replikate haben denselben Stand | Eventual Consistency – temporäre Abweichungen möglich |
> | **Verfügbarkeit bei Ausfällen** | Niedriger – ein ausgefallenes Replikat blockiert Schreiboperationen | Höher – System arbeitet trotz Ausfällen weiter |
> | **Datenverlustrisiko bei Failover** | Kein Datenverlust – alle bestätigten Writes sind repliziert | Möglich – noch nicht replizierte Daten können verloren gehen |

---

### Aufgabe 4.2: Primary-Backup vs. Multi-Primary (5 Punkte)

> [!success] **Musterlösung**
> | Aspekt | Primary-Backup | Multi-Primary |
> |--------|----------------|---------------|
> | **Schreiboperationen** | Nur der Primary akzeptiert Writes, Backups empfangen Replikate | Mehrere Knoten können gleichzeitig Writes akzeptieren |
> | **Vorteil** | Einfach zu implementieren, keine Schreibkonflikte | Höhere Verfügbarkeit, bessere geografische Verteilung, kein Single Point of Failure für Writes |
> | **Nachteil** | Single Point of Failure für Writes, Failover erforderlich bei Primary-Ausfall | Komplexe Konfliktauflösung bei gleichzeitigen Writes auf denselben Datensatz |

---

### Aufgabe 4.3: Vor- und Nachteile der Replikation (5 Punkte)

> [!success] **Musterlösung**
> | | Replikation |
> |---|-------------|
> | **Vorteile** | 1. **Verfügbarkeit:** System läuft bei Knotenausfällen weiter – Redundanz schützt vor Datenverlust |
> | | 2. **Performance:** Lesezugriffe können von lokalen/nächsten Replikaten bedient werden – reduziert Latenz und verteilt Last |
> | **Nachteile** | 1. **Komplexität:** Synchronisation und Konfliktauflösung zwischen Replikaten erforderlich – erhöht Entwicklungsaufwand |
> | | 2. **Konsistenz-Trade-off:** Je mehr Replikate, desto schwieriger ist es, alle synchron zu halten – Trade-off zwischen Konsistenz und Performance |

---

## Teil 5: Koordination und Uhren (15 Punkte)

### Aufgabe 5.1: Externe vs. Interne Synchronisation (3 Punkte)

> [!success] **Musterlösung**
> | Typ | Ziel | Beispiel |
> |-----|------|----------|
> | **Extern** | Alle Uhren stimmen mit einer autoritativen externen Referenz (Realzeit) überein | NTP mit Stratum-0-Referenz (Atomuhr), Cristians Algorithmus |
> | **Intern** | Alle Uhren stimmen untereinander überein – nicht unbedingt mit der Realzeit | Berkeley-Algorithmus – Durchschnitt aller Uhren im Cluster |

---

### Aufgabe 5.2: Lamport-Uhren (5 Punkte)

**a) Regeln für Lamport-Uhren:**

> [!success] **Musterlösung**
> | Situation | Regel |
> |-----------|-------|
> | **Lokales Ereignis** | C := C + 1 (Zähler vor jedem lokalen Ereignis inkrementieren) |
> | **Senden einer Nachricht** | C := C + 1, sende C mit der Nachricht (Zeitstempel mitsenden) |
> | **Empfangen einer Nachricht mit Zeitstempel T** | C := max(C, T) + 1 (eigenen Zähler auf Maximum setzen und inkrementieren) |

**b) Hauptlimitation von Lamport-Uhren:**

> [!success] **Musterlösung**
> Lamport-Uhren können **keine Nebenläufigkeit erkennen**. Sie garantieren nur: Wenn a → b (a happened-before b), dann C(a) < C(b). Der Umkehrschluss gilt jedoch nicht: Aus C(a) < C(b) folgt nicht zwingend a → b. Zwei Ereignisse mit C(a) < C(b) könnten auch nebenläufig sein. Für die Erkennung von Nebenläufigkeit benötigt man Vektoruhren.

---

### Aufgabe 5.3: Happened-Before Relation (4 Punkte)

**a) Definition der Happened-Before Relation (→):**

> [!success] **Musterlösung**
> Die Happened-Before Relation (→) ist definiert durch:
> 1. **Lokale Ordnung:** Wenn a und b Ereignisse im selben Prozess sind und a vor b kommt, dann a → b
> 2. **Nachrichtenübertragung:** Wenn a das Senden einer Nachricht und b das Empfangen derselben ist, dann a → b
> 3. **Transitivität:** Wenn a → b und b → c, dann a → c

**b) Nebenläufigkeit:**

> [!success] **Musterlösung**
> Zwei Ereignisse a und b sind **nebenläufig** (concurrent, geschrieben a || b), wenn weder a → b noch b → a gilt. Das bedeutet, keines der beiden Ereignisse hat das andere kausal beeinflusst – sie sind in keiner kausalen Beziehung zueinander.

---

### Aufgabe 5.4: Lamport-Uhren vs. Vektoruhren (3 Punkte)

> [!success] **Musterlösung**
> | Aspekt | Lamport-Uhren | Vektoruhren |
> |--------|---------------|-------------|
> | **Speicherbedarf** | O(1) – ein einzelner Zähler | O(n) – ein Zähler pro Prozess im System |
> | **Erkennt a → b** | Ja – wenn a → b, dann C(a) < C(b) | Ja – wenn a → b, dann V(a) < V(b) |
> | **Erkennt Nebenläufigkeit** | Nein – kann a || b nicht von a → b unterscheiden | Ja – wenn weder V(a) ≤ V(b) noch V(b) ≤ V(a), dann a || b |

---

## Teil 6: Konsensalgorithmen (15 Punkte)

### Aufgabe 6.1: Konsensproblem (4 Punkte)

> [!success] **Musterlösung**
> | Anforderung | Beschreibung |
> |-------------|--------------|
> | **Agreement** | Alle korrekten Prozesse einigen sich auf denselben Wert – keine unterschiedlichen Entscheidungen |
> | **Validity** | Der gewählte Wert wurde von mindestens einem Prozess vorgeschlagen – keine willkürlichen Werte |
> | **Termination** | Alle korrekten Prozesse treffen irgendwann eine Entscheidung – kein endloses Warten |
> | **Integrity** | Ein Prozess entscheidet höchstens einmal – keine nachträgliche Änderung der Entscheidung |

---

### Aufgabe 6.2: Paxos-Algorithmus (5 Punkte)

**a) Rollen und Aufgaben:**

> [!success] **Musterlösung**
> | Rolle | Aufgabe |
> |-------|---------|
> | **Proposer** | Schlägt Werte vor – initiiert den Konsensvorgang mit einer Proposal-Nummer |
> | **Acceptor** | Stimmt über Vorschläge ab – akzeptiert oder lehnt Proposals basierend auf Regeln ab |
> | **Learner** | Lernt den akzeptierten Wert – wird informiert, sobald Konsens erreicht ist |

**b) 2-Phasen-Ablauf:**

> [!success] **Musterlösung**
> | Phase | Beschreibung |
> |-------|--------------|
> | **Phase 1 (Prepare/Promise)** | Proposer sendet Prepare(n) mit Proposal-Nummer n. Acceptor antwortet mit Promise, wenn n höher als alle bisherigen Nummern ist, und teilt ggf. bereits akzeptierte Werte mit. |
> | **Phase 2 (Accept/Accepted)** | Proposer sendet Accept(n, v) mit dem Wert v an alle Acceptors. Acceptor akzeptiert, wenn er kein höheres n gesehen hat, und informiert Learner. |

---

### Aufgabe 6.3: Raft-Algorithmus (4 Punkte)

> [!success] **Musterlösung**
> | Rolle | Beschreibung | Wann Übergang? |
> |-------|--------------|----------------|
> | **Follower** | Passiver Zustand – reagiert nur auf Anfragen von Leader und Candidates | → Candidate: Bei Timeout (keine Heartbeats vom Leader empfangen) |
> | **Candidate** | Bewirbt sich als neuer Leader – startet Wahl und bittet um Stimmen | → Leader: Bei Erhalt der Mehrheit der Stimmen; → Follower: Bei Entdeckung eines aktuellen Leaders oder Wahlniederlage |
> | **Leader** | Einziger, der Client-Anfragen verarbeitet und Log-Einträge zu Followern repliziert | → Follower: Wenn ein anderer Leader mit höherer Term-Nummer entdeckt wird |

---

### Aufgabe 6.4: FLP-Theorem (2 Punkte)

> [!success] **Musterlösung**
> Das **FLP-Unmöglichkeitstheorem** (Fischer, Lynch, Paterson, 1985) besagt: In einem **asynchronen** verteilten System ist es **unmöglich**, einen deterministischen Konsensalgorithmus zu konstruieren, der alle drei Eigenschaften (Agreement, Validity, Termination) garantiert, wenn auch nur ein Prozess ausfallen kann.
> 
> **Praktische Konsequenz:** Reale Konsensalgorithmen nutzen Workarounds wie Timeouts (machen das System teilweise synchron), Randomisierung oder akzeptieren schwächere Garantien. Paxos und Raft verwenden Timeouts, um das FLP-Theorem in der Praxis zu umgehen.

---

## Quellen

- [[01-Definition|Definition verteilter Systeme]]
- [[02-Eigenschaften|Eigenschaften verteilter Systeme]]
- [[01-RPC|Remote Procedure Call (RPC)]]
- [[03-REST|REST (Representational State Transfer)]]
- [[04-SOAP|SOAP (Simple Object Access Protocol)]]
- [[05-SOA|Service-orientierte Architektur (SOA)]]
- [[01-CAP-Theorem|CAP-Theorem]]
- [[02-Konsistenzmodelle|Konsistenzmodelle]]
- [[03-Replikation|Replikation]]
- [[01-Zeit-Synchronisation|Zeit-Synchronisation]]
- [[02-Logische-Uhren|Logische Uhren]]
- [[03-Konsensalgorithmen|Konsensalgorithmen]]
