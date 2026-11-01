---
title: 'Prüfung B: Betriebssysteme, Rechnernetze und verteilte Systeme'
semester: SS26
punkte_gesamt: 90
bearbeitungszeit: 90
created: '2026-11-01'
modified: '2026-11-01'
---

# Prüfung B: Betriebssysteme, Rechnernetze und verteilte Systeme

**Semester:** SS26  
**Gesamtpunktzahl:** 90 Punkte  
**Bearbeitungszeit:** 90 Minuten

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

### Aufgabe 1b: Anwendung (2 Punkte)

Nennen Sie **zwei Gründe**, warum ein Webserver Threads statt separater Prozesse für Client-Anfragen verwendet.

1. _____________________________________________________________

2. _____________________________________________________________

---

## Aufgabe 2: Speicherverwaltung (4 Punkte)

**a)** Was ist der Unterschied zwischen **Swapping** und **Paging**? (2 Punkte)

_Deine Antwort:_

<br><br><br>

**b)** Was ist ein **Page Fault** und wann tritt er auf? (2 Punkte)

_Deine Antwort:_

<br><br><br>

---

## Aufgabe 3: Prozesszustände (6 Punkte)

**a)** Nennen und beschreiben Sie die **drei grundlegenden Prozesszustände** im Drei-Zustands-Modell. (3 Punkte)

| Zustand | Beschreibung |
|---------|--------------|
| | |
| | |
| | |

**b)** Beschreiben Sie die **vier möglichen Zustandsübergänge** zwischen diesen Zuständen. Geben Sie jeweils an, von welchem in welchen Zustand gewechselt wird und was diesen Übergang auslöst. (3 Punkte)

| Übergang | Von → Nach | Auslöser |
|----------|-----------|----------|
| | | |
| | | |
| | | |
| | | |

---

## Aufgabe 4: Dateisysteme (4 Punkte)

**a)** Warum ist **Journaling** bei modernen Dateisystemen notwendig? (2 Punkte)

_Deine Antwort:_

<br><br><br>

**b)** Welches Problem löst Journaling und wie funktioniert es prinzipiell? (2 Punkte)

_Deine Antwort:_

<br><br><br>

---

## Aufgabe 6: Netzwerkprotokolle (11 Punkte)

**a)** Erklären Sie die Funktionsweise des **DHCP-Protokolls** (Dynamic Host Configuration Protocol). (5 Punkte)

- Welches Problem löst DHCP?
- Wie läuft der DHCP-Vorgang ab (DORA)?
- Welche Informationen erhält ein Client vom DHCP-Server?

_Deine Antwort:_

<br><br><br><br><br>

**b)** Welche der folgenden IP-Adressen sind **private IP-Adressen** gemäß RFC 1918? (6 Punkte)

Kreuzen Sie alle zutreffenden Adressen an:

| | IP-Adresse |
|:-:|------------|
| ☐ | 10.255.255.1 |
| ☐ | 172.15.0.1 |
| ☐ | 192.168.100.50 |
| ☐ | 1.1.1.1 |
| ☐ | 172.31.255.254 |
| ☐ | 192.169.1.1 |

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

_Deine Antwort:_

<br><br>

b) Mit welchem **Initialwert** muss der Semaphor initialisiert werden? Begründen Sie. (2 Punkte)

```
Semaphore _________ = ___
```

c) Schreiben Sie den Ablauf als **Pseudocode** mit P() und V() Operationen. (4 Punkte)

```pseudocode
void auto_parkhaus() {
    // Einfahrt
    
    
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
    
    
}
```

---

### Aufgabe 5.2: Verständnisfragen (7 Punkte)

a) Was passiert, wenn ein 35. Auto einfahren möchte, während alle 34 Plätze belegt sind? Beschreiben Sie das Verhalten des Semaphors. (3 Punkte)

_Deine Antwort:_

<br><br><br>

b) Warum ist es wichtig, dass V() **nach dem Ausfahren** aufgerufen wird und nicht schon nach dem Ausparken vom Stellplatz? (2 Punkte)

_Deine Antwort:_

<br><br>

c) Handelt es sich hier um einen **binären Semaphor (Mutex)** oder einen **zählenden Semaphor**? Begründen Sie. (2 Punkte)

_Deine Antwort:_

<br><br>

---

### Aufgabe 5.3: Erweiterung (5 Punkte)

Das Parkhaus soll nun zusätzlich **5 Stellplätze für Elektroautos** mit Ladesäulen reservieren. Diese dürfen nur von E-Autos genutzt werden, während normale Autos die restlichen 29 Plätze nutzen.

Eine Kamera mit Kennzeichenerkennung an der Einfahrt erkennt E-Autos am "E" am Ende des Kennzeichens (z.B. "N-AB 1234**E**") und leitet diese zu den Ladeplätzen.

Erweitern Sie Ihre Lösung: Welche Semaphore benötigen Sie jetzt? Geben Sie die Definitionen an.

```
Semaphore _________ = ___
Semaphore _________ = ___
```

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

_Deine Antwort:_

<br><br><br>

**ii)** Welches Übertragungsmedium und welche Kabelkategorie empfehlen Sie für die **Etagenverkabelung** (Etagenverteiler → Arbeitsplätze)? Begründen Sie. (3 Punkte)

_Deine Antwort:_

<br><br><br>

**iii)** Nennen Sie je einen geeigneten Ethernet-Standard für Backbone und Etagenverkabelung. (2 Punkte)

| Verkabelung | Ethernet-Standard | Bandbreite |
|-------------|-------------------|------------|
| Backbone | | |
| Etage | | |

---

### Aufgabe 7b: IP-Adressierung (12 Punkte)

Die Praxis erhält den Adressbereich **10.20.0.0** für ihr internes Netzwerk. Folgende Subnetze werden benötigt:

| Subnetz | Geräte aktuell | + 20% Reserve | Funktion |
|---------|----------------|---------------|----------|
| Praxis-Netz | 23 | ? | Arbeitsplätze, Drucker |
| Server-Netz | 5 | ? | Server im Technikraum |
| Management-Netz | 8 | ? | Switches, Router, Firewall |

**i)** Berechnen Sie die benötigte Subnetzgröße für jedes Netz (4 Punkte)

Vergessen Sie nicht: Gateway + Netzwerk-Adresse + Broadcast-Adresse!

| Subnetz | Geräte + 20% + GW | Min. Adressen | CIDR-Präfix |
|---------|-------------------|---------------|-------------|
| Praxis-Netz | | | /__ |
| Server-Netz | | | /__ |
| Management-Netz | | | /__ |

**ii)** Entwerfen Sie die drei Subnetze beginnend bei 10.20.0.0. Beginnen Sie mit dem größten Subnetz und ordnen Sie sie lückenlos an. (6 Punkte)

| Subnetz | Netzadresse | CIDR | Gateway (1. Host) | Broadcast |
|---------|-------------|------|-------------------|-----------|
| | | | | |
| | | | | |
| | | | | |

**iii)** Geben Sie das Supernet an, das alle drei Netze umfasst. (2 Punkte)

```
Supernet (CIDR): _______________
```

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

| Nr | Aktion | Protokoll | Quelle | Ziel | Dest-Port | Beschreibung |
|----|--------|-----------|--------|------|-----------|--------------|
| 1 | ALLOW | TCP | Praxis-Netz | Server-Netz | 443 | Praxis → Server |
| 2 | | | | | | Praxis DNS |
| 3 | | | | | | Praxis Web |
| 4 | | | | | | Management SSH |
| 5 | DENY | any | any | any | any | Default Deny |

**ii)** Ein Paket trifft ein mit: Quelle = Praxis-PC, Ziel = Praxis-Server, Port 443. Welche Regel greift? (2 Punkte)

_Deine Antwort:_

<br><br>

**iii)** Warum ist die Reihenfolge der Regeln wichtig? Was passiert, wenn Regel 5 an Position 1 steht? (2 Punkte)

_Deine Antwort:_

<br><br>

---

## Aufgabe 8: Verteilte Systeme – SOAP (10 Punkte)

**a)** Was bedeutet **SOAP** (Simple Object Access Protocol) und wofür wird es verwendet? (5 Punkte)

_Deine Antwort:_

<br><br><br><br>

**b)** Beschreiben Sie den **Aufbau einer SOAP-Nachricht** und nennen Sie die drei Hauptbestandteile. (3 Punkte)

| Bestandteil | Funktion |
|-------------|----------|
| | |
| | |
| | |

**c)** Nennen Sie **zwei Vorteile** und **einen Nachteil** von SOAP gegenüber REST. (2 Punkte)

_Deine Antwort:_

<br><br>

---
