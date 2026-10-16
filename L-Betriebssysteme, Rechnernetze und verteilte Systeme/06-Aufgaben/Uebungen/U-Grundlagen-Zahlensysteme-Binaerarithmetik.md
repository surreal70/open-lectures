---
author: Andreas Hümmer
title: "Übung: Zahlensysteme und Binärarithmetik (mit IPv4-Bezug)"
tags:
  - uebung
  - grundlagen
  - zahlensysteme
  - binaerarithmetik
  - ipv4
created: 2026-10-16
modified: 2026-10-16
related: "[[00-Aufgaben-Index]]"
difficulty: mittel
aufgabennummer: 1
bearbeitungszeit: "90 Minuten"
status: draft
---

# Übung: Zahlensysteme und Binärarithmetik (mit IPv4-Bezug)

> [!info] **Lernziele**
> Diese Übung hilft dir:
> - Zahlen sicher zwischen den Systemen **binär (2)**, **dezimal (10)**, **oktal (8)** und **hexadezimal (16)** umzuwandeln
> - Die **Binärarithmetik** (Addition, UND, ODER, NICHT, Verschiebung) zu beherrschen
> - Diese Grundlagen auf **IPv4** anzuwenden: Netzadresse, Hostadresse, Netzmaske, Subnetze, Broadcast
> - Bitweise Logik zu verstehen, mit der Betriebssysteme und Netzwerkstacks Adressen verarbeiten

> [!note] **Hinweise zur Bearbeitung**
> - Rechne grundsätzlich **ohne Taschenrechner**; zeige den Rechenweg.
> - Eine IPv4-Adresse besteht aus 4 Oktetten (je 8 Bit), getrennt durch Punkte, z. B. `192.168.10.37`.
> - CIDR-Schreibweise `/n` bedeutet: die ersten `n` Bits der 32-Bit-Adresse gehören zum Netzanteil.

---

## Teil A — Umwandlung von Zahlensystemen

### Aufgabe 1: Grundlegende Umwandlungen (12 Punkte)

Wandle die folgenden Werte um. Gib jeweils den Rechenweg an.

**a)** Dezimal → Binär, Oktal und Hexadezimal: `217`  (3 Punkte)

**b)** Binär → Dezimal und Hexadezimal: `1011 0110`  (3 Punkte)

**c)** Hexadezimal → Binär und Dezimal: `0x2F`  (3 Punkte)

**d)** Oktal → Dezimal und Binär: `0o345`  (3 Punkte)

**Hinweise:**
- Für Dezimal→Binär eignet sich die wiederholte Division durch 2 (Reste von unten nach oben lesen).
- Hex-Ziffern bündeln je 4 Bit, Oktal-Ziffern je 3 Bit.

---

### Aufgabe 2: Oktettweise Umwandlung einer IPv4-Adresse (8 Punkte)

Gegeben ist die IPv4-Adresse `172.16.254.1`.

**a)** Wandle jedes der vier Oktette ins Binärsystem um (8 Bit pro Oktett). (4 Punkte)

**b)** Gib die vollständige 32-Bit-Darstellung ohne Punkte an. (2 Punkte)

**c)** Gib dieselbe Adresse oktettweise in hexadezimaler Form an (zwei Hex-Ziffern pro Oktett). (2 Punkte)

---

## Teil B — Binärarithmetik

### Aufgabe 3: Rechnen im Binärsystem (10 Punkte)

Rechne jeweils im Binärsystem (8 Bit) und gib das Ergebnis zusätzlich dezimal an.

**a)** Addition: `0101 1010 + 0010 0111` (3 Punkte)

**b)** Addition mit Übertrag über 8 Bit: `1111 0001 + 0001 1111` — tritt ein Überlauf (9. Bit) auf? (3 Punkte)

**c)** Bitweise Operationen auf `A = 1100 1010` und `B = 1010 0110`: berechne `A UND B`, `A ODER B`, `A XOR B` und `NICHT A`. (4 Punkte)

**Hinweise:**
- Übertrag beim Addieren wie im Dezimalsystem, nur zur Basis 2.
- `NICHT` kippt jedes Bit (Einerkomplement).

---

### Aufgabe 4: Bitverschiebung und Zweierpotenzen (6 Punkte)

**a)** Verschiebe `0000 1101` um 2 Stellen nach links (`<< 2`). Welchen dezimalen Faktor entspricht das? (3 Punkte)

**b)** Verschiebe `1011 0000` um 3 Stellen nach rechts (`>> 3`, logisch, mit Nullen auffüllen). Gib das Ergebnis dezimal an. (3 Punkte)

---

## Teil C — Anwendung auf IPv4

### Aufgabe 5: Netzmaske und UND-Verknüpfung (10 Punkte)

Gegeben: IP-Adresse `192.168.10.37` mit Netzmaske `255.255.255.224` (entspricht `/27`).

**a)** Schreibe die Netzmaske `255.255.255.224` binär (nur das letzte Oktett genügt für die Rechnung, die ersten drei sind `1111 1111`). (2 Punkte)

**b)** Bestimme die **Netzadresse** durch bitweises UND von IP-Adresse und Netzmaske. Zeige die Rechnung für das letzte Oktett. (4 Punkte)

**c)** Bestimme die **Broadcast-Adresse** (Hostanteil auf lauter Einsen setzen). (2 Punkte)

**d)** Gib den **ersten und letzten nutzbaren Hostadresse** des Netzes an. (2 Punkte)

**Hinweise:**
- Netzanteil = `255.255.255.224` → die oberen 3 Bit des letzten Oktetts sind Netz, die unteren 5 sind Host.
- Broadcast = Netzadresse mit allen Host-Bits = 1.

---

### Aufgabe 6: Subnetting (14 Punkte)

Ein Unternehmen erhält das Netz `10.0.0.0/24` und möchte es in Subnetze aufteilen.

**a)** Wie viele Hostadressen (nutzbar) stehen in `/24` zur Verfügung? Begründe mit der Formel. (2 Punkte)

**b)** Das Netz soll in **4 gleich große Subnetze** geteilt werden. Welche neue Präfixlänge `/n` wird benötigt und warum? (3 Punkte)

**c)** Gib für alle 4 Subnetze jeweils an: Netzadresse, Broadcast-Adresse, nutzbarer Hostbereich. (6 Punkte)

**d)** In welchem Subnetz liegt die Adresse `10.0.0.150`? (3 Punkte)

**Hinweise:**
- Nutzbare Hosts pro Netz: `2^(32 − n) − 2` (Netz- und Broadcast-Adresse abziehen).
- Subnetzgröße (Blockgröße) im letzten Oktett: `256 − <Maskenwert des letzten Oktetts>`.

---

## Punkteverteilung

| Aufgabe | Thema | Punkte |
|---------|-------|--------|
| Aufgabe 1 | Grundlegende Umwandlungen | 12 |
| Aufgabe 2 | IPv4 oktettweise | 8 |
| Aufgabe 3 | Binärarithmetik | 10 |
| Aufgabe 4 | Bitverschiebung | 6 |
| Aufgabe 5 | Netzmaske / UND | 10 |
| Aufgabe 6 | Subnetting | 14 |
| **Gesamt** | | **60** |

---

## Zusammenhänge

- → [[00-Aufgaben-Index]]
- → Lösungen: [[L-Grundlagen-Zahlensysteme-Binaerarithmetik]]

> [!tip] **Weiterführende Links**
> - [IETF RFC 791 – Internet Protocol (IPv4)](https://www.rfc-editor.org/rfc/rfc791)
> - [IETF RFC 4632 – CIDR (Classless Inter-Domain Routing)](https://www.rfc-editor.org/rfc/rfc4632)

---
*Erstellt am 2026-10-16 | Zuletzt aktualisiert: 2026-10-16*
