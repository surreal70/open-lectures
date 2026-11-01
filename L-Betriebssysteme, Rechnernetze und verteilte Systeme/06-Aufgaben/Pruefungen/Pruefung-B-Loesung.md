---
title: 'Lösung Prüfung B: Betriebssysteme, Rechnernetze und verteilte Systeme'
semester: SS26
created: '2026-11-01'
modified: '2026-11-01'
---

# Lösung Prüfung B: Betriebssysteme, Rechnernetze und verteilte Systeme

---

## Aufgabe 1: Threads vs. Prozesse (5 Punkte)

### Aufgabe 1a: Ressourcenteilung (3 Punkte)

Vervollständigen Sie die Tabelle – was teilen Threads eines Prozesses, was hat jeder Thread für sich?

| Ressource | Geteilt (pro Prozess) | Pro Thread |
|-----------|:---------------------:|:----------:|
| Heap (dynamischer Speicher) | ☐ | ☐ |
| Stack | ☐ | ☐ |
| Globale Variablen | ☐ | ☐ |
| Programmzähler (PC) | ☐ | ☐ |
| Offene Dateien | ☐ | ☐ |
| Register | ☐ | ☐ |

---

> **Musterlösung:**

| Ressource | Geteilt (pro Prozess) | Pro Thread |
|-----------|:---------------------:|:----------:|
| Heap (dynamischer Speicher) | ☑ | ☐ |
| Stack | ☐ | ☑ |
| Globale Variablen | ☑ | ☐ |
| Programmzähler (PC) | ☐ | ☑ |
| Offene Dateien | ☑ | ☐ |
| Register | ☐ | ☑ |

> **Erklärung:**
> - **Geteilt:** Heap, globale Variablen und offene Dateien gehören zum Prozess und werden von allen Threads gemeinsam genutzt.
> - **Pro Thread:** Stack (jeder Thread hat eigene lokale Variablen), Programmzähler (jeder Thread ist an einer anderen Stelle im Code) und Register (aktueller CPU-Zustand des Threads).

---

### Aufgabe 1b: Anwendung (2 Punkte)

Nennen Sie **zwei Gründe**, warum ein Webserver Threads statt separater Prozesse für Client-Anfragen verwendet.

---

> **Musterlösung (zwei der folgenden Gründe):**

1. **Schnellere Erzeugung:** Thread-Erzeugung ist 10-100x schneller als Prozess-Erzeugung (kein fork() mit Speicherkopie nötig).

2. **Schnellerer Kontextwechsel:** Threads teilen sich den Adressraum → kein TLB-Flush und keine Cache-Invalidierung beim Wechsel.

3. **Gemeinsamer Speicher:** Threads können direkt über gemeinsame Variablen kommunizieren (z.B. gemeinsamer Cache für Webseiten), ohne aufwendige IPC-Mechanismen (Pipes, Sockets).

4. **Geringerer Speicherverbrauch:** Threads teilen sich Code und Heap des Prozesses.

---

## Aufgabe 2: Speicherverwaltung (4 Punkte)

**a)** Was ist der Unterschied zwischen **Swapping** und **Paging**? (2 Punkte)

**b)** Was ist ein **Page Fault** und wann tritt er auf? (2 Punkte)

---

**a) Unterschied Swapping vs. Paging (2 Punkte)**

> **Musterlösung:**
> 
> | Kriterium | Swapping | Paging |
> |-----------|----------|--------|
> | **Einheit** | Ganzer Prozess | Einzelne Pages (z.B. 4 KB) |
> | **Granularität** | Grob | Fein |
> | **Latenz** | Hoch (gesamter Prozess wird verschoben) | Niedriger (nur benötigte Pages) |
> | **Speichereffizienz** | Niedrig (alles oder nichts) | Hoch (nur aktive Pages im RAM) |
> 
> **Kurz:** Swapping verschiebt ganze Prozesse, Paging verschiebt einzelne Speicherseiten.

**b) Page Fault (2 Punkte)**

> **Musterlösung:**
> Ein **Page Fault** (Seitenfehler) tritt auf, wenn ein Prozess auf eine Speicherseite (Page) zugreift, die sich **nicht im physischen Hauptspeicher (RAM)** befindet.
> 
> **Ablauf:**
> 1. Die CPU prüft über das Valid-Bit in der Page Table, ob die Page im RAM ist
> 2. Ist sie nicht vorhanden, wird ein Interrupt (Trap) ausgelöst
> 3. Das Betriebssystem lädt die Page von der Festplatte in einen freien Frame
> 4. Die Page Table wird aktualisiert
> 5. Der unterbrochene Befehl wird erneut ausgeführt
> 
> Page Faults sind bei Demand Paging normal – sie sind der Mechanismus, um Pages bei Bedarf nachzuladen.

---

## Aufgabe 3: Prozesszustände (6 Punkte)

**a)** Nennen und beschreiben Sie die **drei grundlegenden Prozesszustände** im Drei-Zustands-Modell. (3 Punkte)

**b)** Beschreiben Sie die **vier möglichen Zustandsübergänge** zwischen diesen Zuständen. Geben Sie jeweils an, von welchem in welchen Zustand gewechselt wird und was diesen Übergang auslöst. (3 Punkte)

**a) Die drei Prozesszustände (3 Punkte)**

> **Musterlösung:**

| Zustand | Beschreibung |
|---------|--------------|
| **Running** | Der Prozess wird gerade auf der CPU ausgeführt (aktive Berechnung) |
| **Ready** | Der Prozess ist rechenbereit und wartet auf CPU-Zuteilung |
| **Blocked** | Der Prozess wartet auf Beendigung einer E/A-Aktivität (z.B. Festplatte, Netzwerk) |

**b) Die vier Zustandsübergänge (3 Punkte)**

> **Musterlösung:**

| Übergang | Von → Nach | Auslöser |
|----------|-----------|----------|
| **Dispatch** | Ready → Running | Scheduler wählt den Prozess aus (CPU frei, höchste Priorität) |
| **Timeout** | Running → Ready | Zeitscheibe ist abgelaufen (preemptives Scheduling) |
| **Block** | Running → Blocked | Prozess startet E/A-Anforderung (z.B. `read()`, `scanf()`, `sleep()`) |
| **Wakeup** | Blocked → Ready | E/A-Operation ist abgeschlossen (z.B. Datei gelesen, Timer abgelaufen) |

---

## Aufgabe 4: Dateisysteme (4 Punkte)

**a)** Warum ist **Journaling** bei modernen Dateisystemen notwendig? (2 Punkte)

**b)** Welches Problem löst Journaling und wie funktioniert es prinzipiell? (2 Punkte)

---

**a) Warum ist Journaling notwendig? (2 Punkte)**

> **Musterlösung:**
> **Journaling** ist notwendig, um die **Konsistenz des Dateisystems** nach einem Systemabsturz oder Stromausfall zu gewährleisten.
> 
> **Das Problem ohne Journaling:**
> - Dateisystem-Operationen bestehen aus mehreren Schritten (z.B. Datei erstellen: Inode anlegen, Verzeichniseintrag hinzufügen, Blöcke zuweisen)
> - Bei einem Absturz mitten in einer Operation bleibt das Dateisystem in einem **inkonsistenten Zustand**
> - Ohne Journal muss ein zeitaufwendiger `fsck` (File System Check) das gesamte Dateisystem durchsuchen

**b) Wie funktioniert Journaling? (2 Punkte)**

> **Musterlösung:**
> Journaling funktioniert nach dem **Write-Ahead-Logging-Prinzip**:
> 
> 1. **Vor** der eigentlichen Änderung werden alle geplanten Operationen in ein **Journal** (Log) geschrieben
> 2. Dann werden die Änderungen am Dateisystem durchgeführt
> 3. Nach erfolgreicher Durchführung wird der Journal-Eintrag als abgeschlossen markiert
> 
> **Bei einem Absturz:**
> - Das Journal wird beim Neustart gelesen
> - Unvollständige Transaktionen werden entweder abgeschlossen (Redo) oder rückgängig gemacht (Undo)
> - Das Dateisystem ist innerhalb von Sekunden wieder konsistent

---

## Aufgabe 6: Netzwerkprotokolle (11 Punkte)

**a)** Erklären Sie die Funktionsweise des **DHCP-Protokolls** (Dynamic Host Configuration Protocol). (5 Punkte)

- Welches Problem löst DHCP?
- Wie läuft der DHCP-Vorgang ab (DORA)?
- Welche Informationen erhält ein Client vom DHCP-Server?

**b)** Welche der folgenden IP-Adressen sind **private IP-Adressen** gemäß RFC 1918? (6 Punkte)

| | IP-Adresse |
|:-:|------------|
| ☐ | 10.255.255.1 |
| ☐ | 172.15.0.1 |
| ☐ | 192.168.100.50 |
| ☐ | 1.1.1.1 |
| ☐ | 172.31.255.254 |
| ☐ | 192.169.1.1 |

**a) DHCP-Protokoll (5 Punkte)**

> **Musterlösung:**
> 
> **Problem, das DHCP löst:**
> DHCP (Dynamic Host Configuration Protocol) ermöglicht die **automatische Vergabe von IP-Adressen** und Netzwerkkonfigurationen an Clients. Ohne DHCP müsste jedes Gerät manuell konfiguriert werden.
> 
> **DORA-Ablauf (4 Schritte):**
> 1. **D**iscover: Client sendet Broadcast: "Gibt es einen DHCP-Server?"
> 2. **O**ffer: Server antwortet mit einem IP-Angebot
> 3. **R**equest: Client fordert die angebotene IP offiziell an
> 4. **A**cknowledge: Server bestätigt und vergibt die IP (mit Lease-Zeit)
> 
> **Informationen vom DHCP-Server:**
> - IP-Adresse und Subnetzmaske
> - Default Gateway (Router)
> - DNS-Server-Adressen
> - Lease-Zeit (wie lange die IP gültig ist)
> - Optional: Domain-Name, NTP-Server, WINS-Server

**b) Private IP-Adressen nach RFC 1918 (6 Punkte)**

> **Musterlösung:**
> 
> | | IP-Adresse | Privat? | Begründung |
> |:-:|------------|:-------:|------------|
> | ☑ | 10.255.255.1 | Ja | 10.0.0.0/8 (10.0.0.0 – 10.255.255.255) |
> | ☐ | 172.15.0.1 | Nein | Außerhalb des privaten Bereichs (172.16-31.x.x) |
> | ☑ | 192.168.100.50 | Ja | 192.168.0.0/16 (192.168.0.0 – 192.168.255.255) |
> | ☐ | 1.1.1.1 | Nein | Öffentliche IP (Cloudflare DNS) |
> | ☑ | 172.31.255.254 | Ja | 172.16.0.0/12 (172.16.0.0 – 172.31.255.255) |
> | ☐ | 192.169.1.1 | Nein | Außerhalb des privaten Bereichs (nur 192.168.x.x) |
> 
> **RFC 1918 definiert drei private Adressbereiche:**
> - 10.0.0.0/8 (Klasse A)
> - 172.16.0.0/12 (Klasse B)
> - 192.168.0.0/16 (Klasse C)

---

## Aufgabe 5: Das Parkhaus-Problem (20 Punkte)

### Szenario

Ein Parkhaus hat **34 Stellplätze**. An der Einfahrt befindet sich eine Schranke mit Ticketautomat.

**Regel:** Es dürfen sich maximal so viele Autos im Parkhaus befinden, wie Stellplätze vorhanden sind (34). Würden mehr Autos einfahren, könnten diese:
- geparkte Autos am Ausparken hindern
- andere Autos daran hindern, die Ausfahrtsschranke zu erreichen

**Ablauf eines Autofahrers:**
```
1. An der Einfahrt warten, bis Einfahrt erlaubt
2. Ticket ziehen, Schranke öffnet
3. Einfahren und Stellplatz suchen
4. Parken (Einkaufen, Termin, etc.)
5. Zum Auto zurückkehren, ausparken
6. Zur Ausfahrt fahren, bezahlen, ausfahren
```

---

### Aufgabe 5.1: Semaphore-Modellierung (8 Punkte)

a) Welche **Ressource** muss hier durch einen Semaphor geschützt werden? (2 Punkte)

b) Mit welchem **Initialwert** muss der Semaphor initialisiert werden? Begründen Sie. (2 Punkte)

c) Schreiben Sie den Ablauf als **Pseudocode** mit P() und V() Operationen. (4 Punkte)

---

**a) Ressource (2 Punkte)**

> **Musterlösung:**
> Die **Stellplätze im Parkhaus** (bzw. die Kapazität des Parkhauses) müssen durch einen Semaphor geschützt werden. Der Semaphor zählt die Anzahl der verfügbaren Plätze.

**b) Initialwert (2 Punkte)**

```
Semaphore stellplaetze = 34
```

> **Begründung:** Der Initialwert entspricht der Anzahl der verfügbaren Stellplätze. Bei jedem einfahrenden Auto wird der Zähler um 1 dekrementiert (P-Operation), bei jedem ausfahrenden Auto um 1 inkrementiert (V-Operation).

**c) Pseudocode (4 Punkte)**

```pseudocode
Semaphore stellplaetze = 34;

void auto_parkhaus() {
    // Einfahrt
    P(stellplaetze);        // Warten bis Platz frei, dann "reservieren"
    
    ticket_ziehen();
    einfahren();
    stellplatz_suchen();
    
    // Parken
    parke_und_erledige_termin();
    
    // Ausfahrt
    ausparken();
    zur_ausfahrt_fahren();
    bezahlen();
    ausfahren();
    
    V(stellplaetze);        // Platz wieder freigeben
}
```

---

### Aufgabe 5.2: Verständnisfragen (7 Punkte)

a) Was passiert, wenn ein 35. Auto einfahren möchte, während alle 34 Plätze belegt sind? Beschreiben Sie das Verhalten des Semaphors. (3 Punkte)

b) Warum ist es wichtig, dass V() **nach dem Ausfahren** aufgerufen wird und nicht schon nach dem Ausparken vom Stellplatz? (2 Punkte)

c) Handelt es sich hier um einen **binären Semaphor (Mutex)** oder einen **zählenden Semaphor**? Begründen Sie. (2 Punkte)

---

**a) Verhalten bei vollem Parkhaus (3 Punkte)**

> **Musterlösung:**
> Wenn alle 34 Plätze belegt sind, hat der Semaphor den Wert 0. Das 35. Auto ruft P(stellplaetze) auf:
> 
> 1. Die P-Operation prüft den Semaphor-Wert (0)
> 2. Da der Wert 0 ist, kann er nicht weiter dekrementiert werden
> 3. Das Auto (der aufrufende Prozess/Thread) wird **blockiert** und in eine Warteschlange eingereiht
> 4. Das Auto wartet vor der Schranke (außerhalb des Parkhauses)
> 5. Erst wenn ein anderes Auto ausfährt und V() aufruft (Semaphor wird 1), wird das wartende Auto aufgeweckt und kann einfahren

**b) Zeitpunkt der V-Operation (2 Punkte)**

> **Musterlösung:**
> Würde V() bereits nach dem Ausparken vom Stellplatz aufgerufen, wäre das Auto noch im Parkhaus (auf dem Weg zur Ausfahrt). Ein neues Auto könnte einfahren, obwohl das alte noch nicht draußen ist. 
> 
> Das Problem: Das einfahrende Auto und das ausfahrende Auto könnten sich im Parkhaus blockieren – es könnte zu einem Stau kommen, bei dem keines der Autos die Ausfahrt erreichen kann.
> 
> Daher muss V() erst aufgerufen werden, wenn das Auto das Parkhaus **vollständig verlassen** hat.

**c) Semaphor-Typ (2 Punkte)**

> **Musterlösung:**
> Es handelt sich um einen **zählenden Semaphor** (Counting Semaphore).
> 
> **Begründung:** 
> - Der Semaphor kann Werte von 0 bis 34 annehmen (nicht nur 0 und 1)
> - Er zählt die Anzahl der verfügbaren Ressourcen (Stellplätze)
> - Mehrere Autos können gleichzeitig im Parkhaus sein (bis zu 34)
> 
> Ein binärer Semaphor (Mutex) hätte nur die Werte 0 und 1 und würde nur einem einzigen Auto den Zugang erlauben.

---

### Aufgabe 5.3: Erweiterung (5 Punkte)

Das Parkhaus soll nun zusätzlich **5 Stellplätze für Elektroautos** mit Ladesäulen reservieren. Diese dürfen nur von E-Autos genutzt werden, während normale Autos die restlichen 29 Plätze nutzen.

Eine Kamera mit Kennzeichenerkennung an der Einfahrt erkennt E-Autos am "E" am Ende des Kennzeichens (z.B. "N-AB 1234**E**") und leitet diese zu den Ladeplätzen.

Erweitern Sie Ihre Lösung: Welche Semaphore benötigen Sie jetzt? Geben Sie die Definitionen an.

---

> **Musterlösung:**

```
Semaphore normale_plaetze = 29    // Für normale Autos
Semaphore e_plaetze = 5           // Nur für Elektroautos
```

> **Erklärung:**
> - Die Kamera erkennt anhand des Kennzeichens (Postfix "E"), ob es sich um ein E-Auto handelt
> - Normale Autos verwenden nur `P(normale_plaetze)` und `V(normale_plaetze)`
> - E-Autos verwenden nur `P(e_plaetze)` und `V(e_plaetze)`
> - Die beiden Gruppen von Stellplätzen werden unabhängig voneinander verwaltet

---

## Aufgabe 7: Rechnernetze – Arztpraxis-Netzwerk (30 Punkte)

### Szenario

Eine Gemeinschaftspraxis plant ihr Netzwerk. Die Praxis befindet sich in einem zweistöckigen Gebäude.

**Gebäudestruktur:**

```
Technikraum (Keller) ──── Steigzone ──── Etagenverteiler EG ──── Arbeitsplätze EG
         │                                      
         └──────────────────────────── Etagenverteiler 1.OG ──── Arbeitsplätze 1.OG
```

| Bereich | Geräte |
|---------|--------|
| Erdgeschoss | 12 Arbeitsplätze, 2 Drucker |
| 1. Stock | 8 Arbeitsplätze, 1 Drucker |
| Technikraum (Keller) | Server, Router, Firewall |

| Strecke | Von | Nach | Länge |
|---------|-----|------|-------|
| Backbone (Steigzone) | Technikraum | Etagenverteiler | 40m (EG) / 70m (1.OG) |
| Etagenverkabelung | Etagenverteiler | Arbeitsplatz (max.) | 55m |

**Wichtig:** Der Technikraum hat einen separaten Stromanschluss mit eigener Erdung (USV-Anlage für die Server).

---

### Aufgabe 7a: Verkabelung (8 Punkte)

**i)** Welches Übertragungsmedium empfehlen Sie für die **Backbone-Verkabelung** (Technikraum → Etagenverteiler)? Begründen Sie unter Berücksichtigung der separaten Erdung. (3 Punkte)

**ii)** Welches Übertragungsmedium und welche Kabelkategorie empfehlen Sie für die **Etagenverkabelung** (Etagenverteiler → Arbeitsplätze)? Begründen Sie. (3 Punkte)

**iii)** Nennen Sie je einen geeigneten Ethernet-Standard für Backbone und Etagenverkabelung. (2 Punkte)

---

**i) Backbone-Verkabelung (3 Punkte)**

> **Musterlösung:**
> Für die Backbone-Verkabelung (Technikraum → Etagenverteiler) empfehle ich **Glasfaser (LWL)**.
> 
> **Begründungen:**
> 1. **Potentialtrennung:** Der Technikraum hat eine separate Erdung (USV-Anlage). Bei Kupferverkabelung könnten Ausgleichsströme über die Kabelschirmung fließen, was zu Störungen, Geräteschäden oder sogar Brandgefahr führen kann. LWL ist elektrisch nicht leitend und bietet automatisch galvanische Trennung.
> 2. **Zukunftssicherheit:** LWL ermöglicht höhere Bandbreiten für zukünftige Erweiterungen.
> 3. **Störungsfreiheit:** Keine elektromagnetischen Interferenzen im Backbone.

**ii) Etagenverkabelung (3 Punkte)**

> **Musterlösung:**
> Für die Etagenverkabelung empfehle ich **Kupfer, Kategorie Cat 6a**.
> 
> **Begründungen:**
> 1. **Länge geeignet:** Mit max. 55m liegt die Strecke deutlich unter der 100m-Grenze für Kupfer-Ethernet.
> 2. **Kostengünstig:** Kupfer ist günstiger als LWL für kurze Strecken und die Endgeräte haben Standard-RJ45-Anschlüsse.
> 3. **Zukunftssicher:** Cat 6a unterstützt bis zu 10 Gbit/s und ist damit auch für zukünftige Anforderungen gerüstet.
> 4. **Keine Potentialprobleme:** Innerhalb einer Etage gibt es keine separate Erdung.

**iii) Ethernet-Standards (2 Punkte)**

> **Musterlösung:**

| Verkabelung | Ethernet-Standard | Bandbreite |
|-------------|-------------------|------------|
| Backbone | 10GBASE-SR (LWL, OM3/OM4) | 10 Gbit/s |
| Etage | 1000BASE-T oder 2.5GBASE-T (Cat 6a) | 1–2,5 Gbit/s |

---

### Aufgabe 7b: IP-Adressierung (12 Punkte)

Die Praxis erhält den Adressbereich **10.20.0.0** für ihr internes Netzwerk. Folgende Subnetze werden benötigt:

| Subnetz | Geräte aktuell | + 20% Reserve | Funktion |
|---------|----------------|---------------|----------|
| Praxis-Netz | 23 | ? | Arbeitsplätze, Drucker |
| Server-Netz | 5 | ? | Server im Technikraum |
| Management-Netz | 8 | ? | Switches, Router, Firewall |

**i)** Berechnen Sie die benötigte Subnetzgröße für jedes Netz (4 Punkte)

**ii)** Entwerfen Sie die drei Subnetze beginnend bei 10.20.0.0. Beginnen Sie mit dem größten Subnetz und ordnen Sie sie lückenlos an. (6 Punkte)

**iii)** Geben Sie das Supernet an, das alle drei Netze umfasst. (2 Punkte)

---

**i) Bedarfsberechnung (4 Punkte)**

> **Musterlösung:**

| Subnetz | Geräte | +20% | +GW | Gesamt | +Netz+BC | Min. Größe | CIDR |
|---------|--------|------|-----|--------|----------|------------|------|
| Praxis-Netz | 23 | 28 (aufrunden) | +1 | 29 | +2 = 31 | 32 (2⁵) | /27 |
| Server-Netz | 5 | 6 | +1 | 7 | +2 = 9 | 16 (2⁴) | /28 |
| Management-Netz | 8 | 10 (aufrunden) | +1 | 11 | +2 = 13 | 16 (2⁴) | /28 |

**ii) Subnetz-Design (6 Punkte)**

> **Musterlösung:**
> Beginnend mit dem größten Subnetz, lückenlos angeordnet:

| Subnetz | Netzadresse | CIDR | Gateway (1. Host) | Broadcast |
|---------|-------------|------|-------------------|-----------|
| Praxis-Netz | 10.20.0.0 | /27 | 10.20.0.1 | 10.20.0.31 |
| Server-Netz | 10.20.0.32 | /28 | 10.20.0.33 | 10.20.0.47 |
| Management-Netz | 10.20.0.48 | /28 | 10.20.0.49 | 10.20.0.63 |

**iii) Supernet (2 Punkte)**

> **Musterlösung:**
> ```
> Supernet (CIDR): 10.20.0.0/26
> ```
> 
> Das /26-Netz umfasst die Adressen 10.20.0.0 bis 10.20.0.63 und enthält alle drei Subnetze.

---

### Aufgabe 7c: Paketfilter (10 Punkte)

Die Firewall im Technikraum soll folgende Regeln umsetzen:

**Anforderungen:**
- Praxis-PCs dürfen ins Internet (HTTP/HTTPS)
- Praxis-PCs dürfen DNS-Anfragen stellen (Port 53)
- Praxis-PCs dürfen auf den Praxis-Server zugreifen (HTTPS, Port 443)
- Aus dem Internet darf **niemand** auf interne Netze zugreifen
- Management-Netz darf auf alle internen Geräte zugreifen (SSH, Port 22)
- Alles andere wird blockiert (Default-Deny)

**i)** Vervollständigen Sie das Regelwerk. (6 Punkte)

**ii)** Ein Paket trifft ein mit: Quelle = Praxis-PC, Ziel = Praxis-Server, Port 443. Welche Regel greift? (2 Punkte)

**iii)** Warum ist die Reihenfolge der Regeln wichtig? Was passiert, wenn Regel 5 an Position 1 steht? (2 Punkte)

---

**i) Regelwerk (6 Punkte)**

> **Musterlösung:**

| Nr | Aktion | Protokoll | Quelle | Ziel | Dest-Port | Beschreibung |
|----|--------|-----------|--------|------|-----------|--------------|
| 1 | ALLOW | TCP | Praxis-Netz | Server-Netz | 443 | Praxis → Server |
| 2 | ALLOW | UDP/TCP | Praxis-Netz | Internet | 53 | Praxis DNS |
| 3 | ALLOW | TCP | Praxis-Netz | Internet | 80, 443 | Praxis Web |
| 4 | ALLOW | TCP | Management-Netz | Praxis-Netz, Server-Netz | 22 | Management SSH |
| 5 | DENY | any | any | any | any | Default Deny |

> **Wichtig zur Reihenfolge:** Regel 1 (Praxis → Server) muss vor Regel 3 (Praxis → Internet) stehen, weil spezifischere Regeln zuerst kommen müssen.

**ii) Regel-Matching (2 Punkte)**

> **Musterlösung:**
> Das Paket (Praxis-PC → Praxis-Server, Port 443) wird von **Regel 1** erfasst und erlaubt.
> 
> - Regel 1 greift: Quelle = Praxis-Netz ✓, Ziel = Server-Netz ✓, Port = 443 ✓
> - Das Paket wird durchgelassen (ALLOW)

**iii) Reihenfolge (2 Punkte)**

> **Musterlösung:**
> Firewalls arbeiten nach dem **First-Match-Wins-Prinzip**: Die erste passende Regel entscheidet, nachfolgende Regeln werden nicht mehr geprüft.
> 
> Wenn Regel 5 (DENY any any) an Position 1 stünde, würde **jedes Paket sofort blockiert** – die erlaubenden Regeln 2-4 würden nie erreicht. Niemand könnte mehr kommunizieren.
> 
> Daher muss die Default-Deny-Regel immer am **Ende** stehen.

---

## Aufgabe 8: Verteilte Systeme – SOAP (10 Punkte)

**a)** Was bedeutet **SOAP** (Simple Object Access Protocol) und wofür wird es verwendet? (5 Punkte)

**b)** Beschreiben Sie den **Aufbau einer SOAP-Nachricht** und nennen Sie die drei Hauptbestandteile. (3 Punkte)

**c)** Nennen Sie **zwei Vorteile** und **einen Nachteil** von SOAP gegenüber REST. (2 Punkte)

**a) SOAP-Grundlagen (5 Punkte)**

> **Musterlösung:**
> **SOAP** (Simple Object Access Protocol) ist ein Protokoll für den Austausch strukturierter Informationen in verteilten Systemen.
> 
> **Verwendung:**
> - Kommunikation zwischen Anwendungen über Netzwerke (typischerweise HTTP/HTTPS)
> - Web Services in Unternehmensumgebungen
> - Stark typisierte, formale Service-Schnittstellen
> - Transaktionssichere Kommunikation (z.B. Banken, Versicherungen)
> 
> **Eigenschaften:**
> - XML-basiertes Nachrichtenformat
> - Plattform- und sprachunabhängig
> - Unterstützt WS-*-Standards (WS-Security, WS-Transaction, etc.)

**b) Aufbau einer SOAP-Nachricht (3 Punkte)**

> **Musterlösung:**

| Bestandteil | Funktion |
|-------------|----------|
| **Envelope** | Wurzelelement, das die Nachricht als SOAP-Nachricht identifiziert |
| **Header** | Optional: Metadaten wie Authentifizierung, Routing, Transaktions-IDs |
| **Body** | Pflicht: Enthält die eigentlichen Nutzdaten (Request/Response) |

> Optional: **Fault** (im Body) für Fehlermeldungen

**c) Vorteile und Nachteile (2 Punkte)**

> **Musterlösung:**
> 
> **Vorteile gegenüber REST:**
> 1. **Strikte Typisierung:** WSDL definiert exakt die Schnittstelle (maschinenlesbar, automatische Code-Generierung)
> 2. **Eingebaute Sicherheit:** WS-Security bietet Verschlüsselung und Signaturen auf Nachrichtenebene
> 3. **Transaktionsunterstützung:** WS-Transaction für verteilte Transaktionen
> 
> **Nachteil:**
> - **Overhead:** XML-Format ist verbose, größere Nachrichten, höherer Parsing-Aufwand als JSON bei REST

---
