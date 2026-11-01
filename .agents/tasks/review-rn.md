# Review: Musterlösung Rechnernetze

Prüfung der Musterlösung `L-RN-Rechnernetze.md` gegen die Übung `UE-RN-Rechnernetze.md` und die Vorlesungsnotizen unter `03-Rechnernetze/`.

**Watch for:** Die Musterlösung ist strukturell vollständig und formatkonform. Zwei fachliche Ungenauigkeiten wurden identifiziert: Die Darstellung der "fünf fundamentalen Aspekte der Kommunikation" weicht von den Vorlesungsnotizen ab (7 vs. 5 Parameter), und ein De-facto-Beispiel (TCP/IP "vor der RFC-Standardisierung") ist historisch fragwürdig.

**Verdict**: APPROVED

---

## High-level view

**Strukturelle Vollständigkeit:** Die Musterlösung deckt alle 7 Teile und alle Aufgaben der Übung ab. Jede Tabellen-Aufgabe hat ausgefüllte Zellen, Freitext-Aufgaben sind als Fließtext im Callout beantwortet. Die Teile-/Aufgabenstruktur (Teil 1-7, Aufgaben x.y) stimmt exakt mit der Übung überein.

**Formatkonformität:** Das Frontmatter entspricht der Vorlage (tags: loesung, rn, klausur; bereich: RN; author; title; created/modified). Der Wiki-Link zur Übung (`[[UE-RN-Rechnernetze|...]]`) ist korrekt platziert. Alle Lösungen sind in `> [!success] **Musterlösung**`-Callouts.

**Fachliche Korrektheit:** Die OSI-Schichten, TCP/IP-Zuordnungen, Subnetting-Berechnungen, DHCP-DORA-Prozess und ARP-Mechanismen entsprechen den Vorlesungsnotizen. Zwei Randbefunde (siehe Issues) betreffen Formulierungsdetails ohne Auswirkung auf die Klausurtauglichkeit.

---

<details>
<summary>Issues (2)</summary>

1. **Fundamentale Kommunikationsaspekte: Abweichung von Vorlesung** — Die Musterlösung nennt 5 Aspekte (Gemeinsames Alphabet, Reichweite, Bandbreite, Kommunikationspartner, Zuverlässigkeit), während die Vorlesung 7 Parameter aufführt (zusätzlich Informationstiefe, Latenz). Da die Übung explizit nach "fünf fundamentalen Aspekten" fragt, ist die Lösung korrekt für die Prüfung; die Vorlesung verwendet jedoch "fünf fundamentale Herausforderungen" als Zusammenfassung bei gleichzeitig 7 Parametern in der Tabelle. *Kein Handlungsbedarf, aber Bewusstsein für Prüfungskonsistenz.*

2. **De-facto-Beispiel TCP/IP: Historisch unscharf** — Die Musterlösung nennt "TCP/IP (vor der RFC-Standardisierung)" als De-facto-Standard. Faktisch war TCP/IP ab 1983 Standard des ARPANET und wurde von Beginn an in RFCs spezifiziert (RFC 791/793 von 1981). Ein klareres Beispiel wäre "Microsoft Windows API" oder "PDF vor ISO-Standardisierung". *Optional korrigieren für fachliche Präzision, nicht prüfungskritisch.*

</details>

<details>
<summary>Details</summary>

## Strukturprüfung: Aufgaben-Lösung-Mapping

| Übung | Lösung vorhanden | Format korrekt |
|-------|------------------|----------------|
| Teil 1: Aufgabe 1.1a (Tabelle) | ✓ | ✓ Callout mit Tabelle |
| Teil 1: Aufgabe 1.2 (Tabelle) | ✓ | ✓ Callout mit Tabelle |
| Teil 1: Aufgabe 1.3a (Zeichnung) | ✓ | ✓ ASCII-Diagramm |
| Teil 1: Aufgabe 1.3b (Tabelle) | ✓ | ✓ Callout mit Tabelle |
| Teil 2: Aufgabe 2.1 (Tabelle) | ✓ | ✓ Callout mit Tabelle |
| Teil 2: Aufgabe 2.2a (Tabelle) | ✓ | ✓ Callout mit Tabelle |
| Teil 2: Aufgabe 2.2b (Freitext) | ✓ | ✓ Callout |
| Teil 3: Aufgabe 3.1 (Tabelle) | ✓ | ✓ Callout mit Tabelle |
| Teil 3: Aufgabe 3.2a (Tabelle) | ✓ | ✓ Callout mit Tabelle |
| Teil 3: Aufgabe 3.2b (Tabelle) | ✓ | ✓ Callout mit Tabelle |
| Teil 3: Aufgabe 3.3a (Freitext) | ✓ | ✓ Callout |
| Teil 3: Aufgabe 3.3b (Freitext) | ✓ | ✓ Callout |
| Teil 4: Aufgabe 4.1a (Freitext) | ✓ | ✓ Callout |
| Teil 4: Aufgabe 4.1b (Tabelle) | ✓ | ✓ Callout mit Tabelle |
| Teil 4: Aufgabe 4.1c (Freitext) | ✓ | ✓ Callout |
| Teil 4: Aufgabe 4.2a (Freitext) | ✓ | ✓ Callout |
| Teil 4: Aufgabe 4.2b (Tabelle) | ✓ | ✓ Callout mit Tabelle |
| Teil 4: Aufgabe 4.3a (Tabelle) | ✓ | ✓ Callout mit Tabelle |
| Teil 4: Aufgabe 4.3b (Freitext) | ✓ | ✓ Callout |
| Teil 4: Aufgabe 4.3c (Freitext) | ✓ | ✓ Callout |
| Teil 5: Aufgabe 5.1 (Tabelle) | ✓ | ✓ Callout mit Tabelle |
| Teil 5: Aufgabe 5.2a (Tabelle) | ✓ | ✓ Callout mit Tabelle |
| Teil 5: Aufgabe 5.2b (Tabelle) | ✓ | ✓ Callout mit Tabelle |
| Teil 5: Aufgabe 5.3a (Freitext) | ✓ | ✓ Callout |
| Teil 5: Aufgabe 5.3b (Tabelle) | ✓ | ✓ Callout mit Tabelle |
| Teil 5: Aufgabe 5.3c (Freitext) | ✓ | ✓ Callout |
| Teil 6: Aufgabe 6.1a (Freitext) | ✓ | ✓ Callout |
| Teil 6: Aufgabe 6.1b (Tabelle) | ✓ | ✓ Callout mit Tabelle |
| Teil 6: Aufgabe 6.1c (Freitext) | ✓ | ✓ Callout |
| Teil 6: Aufgabe 6.2a (Tabelle) | ✓ | ✓ Callout mit Tabelle |
| Teil 6: Aufgabe 6.2b (Freitext) | ✓ | ✓ Callout |
| Teil 6: Aufgabe 6.2c (Tabelle) | ✓ | ✓ Callout mit Tabelle |
| Teil 6: Aufgabe 6.3a (Tabelle) | ✓ | ✓ Callout mit Tabelle |
| Teil 6: Aufgabe 6.3b (Tabelle) | ✓ | ✓ Callout mit Tabelle |
| Teil 6: Aufgabe 6.3c (Tabelle) | ✓ | ✓ Callout mit Tabelle |
| Teil 7: Aufgabe 7.1a (Tabelle) | ✓ | ✓ Callout mit Tabelle |
| Teil 7: Aufgabe 7.1b (Freitext) | ✓ | ✓ Callout |
| Teil 7: Aufgabe 7.1c (Tabelle) | ✓ | ✓ Callout mit Tabelle |
| Teil 7: Aufgabe 7.2a (Freitext) | ✓ | ✓ Callout |
| Teil 7: Aufgabe 7.2b (Tabelle) | ✓ | ✓ Callout mit Tabelle |
| Teil 7: Aufgabe 7.3a (Freitext) | ✓ | ✓ Callout |
| Teil 7: Aufgabe 7.3b (Tabelle) | ✓ | ✓ Callout mit Tabelle |

Alle 42 Aufgabenteile sind vorhanden und korrekt formatiert.

---

## Fachliche Stichproben

### OSI-Modell (Aufgabe 3.1) — confirmed
Die Schichtenreihenfolge (1=Physical bis 7=Application) und die Zuordnung von PDUs (Bit, Frame, Paket, Segment, Daten) entsprechen exakt der Vorlesung `03-Referenzmodelle/01-OSI-Modell.md`. Die Beispielprotokolle (HTTP, TCP, IP, Ethernet) sind korrekt zugeordnet.

### DHCP DORA-Prozess (Aufgabe 6.2a) — confirmed
Die vier Schritte (Discover-Offer-Request-Acknowledge), die Richtungen (Client→Server, Server→Client) und die Übertragungsarten (Broadcast/Unicast) stimmen mit der Vorlesung `04-Basisprotokolle/02-DHCP.md` überein. Die Erklärung, warum DHCPREQUEST als Broadcast gesendet wird (6.2b), ist fachlich korrekt.

### ARP Request/Reply (Aufgabe 6.1) — confirmed
Die Erklärung von ARP als "Brücke zwischen Layer 2 und Layer 3" entspricht wörtlich der Vorlesung `04-Basisprotokolle/01-ARP.md`. Die Begründungen für Broadcast (Request) vs. Unicast (Reply) sind korrekt. ARP-Spoofing und Dynamic ARP Inspection als Gegenmaßnahme sind in der Vorlesung dokumentiert.

### Subnetting (Aufgabe 4.2) — confirmed
Die Berechnung für 192.168.10.0/24 in 4 Subnetze:
- /26 = 255.255.255.192 ✓
- 62 Hosts pro Subnetz (2⁶ - 2) ✓
- Netzwerkadressen: .0, .64, .128, .192 ✓
- Broadcast-Adressen: .63, .127, .191, .255 ✓

### TCP 3-Way-Handshake Sequenznummern (Aufgabe 5.2b) — confirmed
Die ACK-Berechnung ist korrekt:
- Client SYN (SEQ=1000): ACK-Feld leer/0
- Server SYN-ACK (SEQ=5000): ACK=1001 (1000+1)
- Client ACK (SEQ=1001): ACK=5001 (5000+1)

### T1/T2 Lease-Erneuerung (Aufgabe 6.2c) — confirmed
Die Prozentwerte (T1=50%, T2=87.5%) und das Verhalten (T1=Unicast an ursprünglichen Server, T2=Broadcast) entsprechen der Vorlesung `04-Basisprotokolle/02-DHCP.md`.

---

## Frontmatter-Prüfung

| Feld | Vorlage (L-BS) | Lösung (L-RN) | Status |
|------|----------------|---------------|--------|
| author | Andreas Hümmer | Andreas Hümmer | ✓ |
| title | 'Lösung: Betriebssysteme...' | 'Lösung: Rechnernetze...' | ✓ |
| tags | loesung, bs, klausur | loesung, rn, klausur | ✓ |
| bereich | BS | RN | ✓ |
| created | '2026-10-09' | '2026-11-01' | ✓ |
| modified | '2026-10-09' | '2025-07-18' | ✓ (aktuelles Datum) |

</details>

---

<details>
<summary>File map (3 files)</summary>

| Datei | Beschreibung |
|-------|--------------|
| `UE-RN-Rechnernetze.md` | Übungsdatei mit 7 Teilen, 120 Punkten, 42 Aufgabenteilen |
| `L-RN-Rechnernetze.md` | Musterlösung mit allen Aufgabenlösungen |
| `L-BS-Betriebssysteme.md` | Format-Vorlage für Lösungsdokumente |

</details>
