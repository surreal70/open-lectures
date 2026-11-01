# Review: Musterlösung Verteilte Systeme

**Geprüfte Datei:** `L-VS-VerteilteSysteme.md`  
**Übungsdatei:** `UE-VS-VerteilteSysteme.md`  
**Vorlage:** `L-BS-Betriebssysteme.md`

**Watch for:** Keine blockierenden Befunde. Frontmatter, Struktur und Quellenverweise sind korrekt. Fachliche Stichproben zeigen Übereinstimmung mit den Vorlesungsnotizen.

**Verdict:** APPROVED

---

## High-Level View

Die Musterlösung deckt alle 6 Teile und alle Aufgaben der Übung vollständig ab. Jede Aufgabe erhält eine Lösung im `> [!success] **Musterlösung**`-Callout-Format, konsistent mit der BS-Vorlage. Die Teile-Struktur (1–6) und Aufgabennummerierung (1.1–6.4) stimmen exakt mit der Übung überein.

Das Frontmatter enthält alle erforderlichen Felder: `tags: loesung, vs, klausur`, `bereich: VS`, `author`, `title`, `created`, `modified`. Der Wiki-Link zur Übung ist korrekt formatiert. Die Quellenverweise am Ende referenzieren die Vorlesungsnotizen.

Die fachlichen Stichproben – Definitionen (Tanenbaum, Bal, Lamport), vier Hauptmerkmale, CAP-Theorem, Lamport-Uhren-Regeln, Quorum-Formel – stimmen wörtlich oder sinngemäß mit den Vorlesungsnotizen überein. Alle Tabellen sind vollständig ausgefüllt, keine Leerzellen gefunden.

---

<details>
<summary>Issues (0)</summary>

Keine blockierenden Befunde.

</details>

---

<details>
<summary>Details</summary>

## Vollständigkeit & Struktur

### Aufgabenabdeckung

Die Übung enthält 6 Teile mit insgesamt 22 Aufgaben (1.1–1.4, 2.1–2.6, 3.1–3.5, 4.1–4.3, 5.1–5.4, 6.1–6.4). Die Musterlösung enthält exakt dieselbe Struktur mit Lösungen für alle 22 Aufgaben.

| Teil | Übung | Lösung | Status |
|------|-------|--------|--------|
| 1: Grundlagen | 4 Aufgaben (1.1–1.4) | ✓ | Vollständig |
| 2: Kommunikation | 6 Aufgaben (2.1–2.6) | ✓ | Vollständig |
| 3: CAP & Konsistenz | 5 Aufgaben (3.1–3.5) | ✓ | Vollständig |
| 4: Replikation | 3 Aufgaben (4.1–4.3) | ✓ | Vollständig |
| 5: Koordination/Uhren | 4 Aufgaben (5.1–5.4) | ✓ | Vollständig |
| 6: Konsensalgorithmen | 4 Aufgaben (6.1–6.4) | ✓ | Vollständig |

### Teilaufgaben-Struktur

Alle Aufgaben mit Unterteilen (a/b) haben entsprechende Lösungs-Unterteile:
- 1.1 a/b ✓
- 2.2 a/b ✓
- 3.2 a/b ✓
- 3.5 a/b ✓
- 5.2 a/b ✓
- 5.3 a/b ✓
- 6.2 a/b ✓

### Frontmatter-Prüfung

```yaml
# Lösung
tags: [loesung, vs, klausur]  # ✓ korrekt
bereich: VS                    # ✓ korrekt
author: Andreas Hümmer         # ✓ vorhanden
title: 'Lösung: Verteilte Systeme (Klausurformat)'  # ✓ konsistent
created: '2026-11-01'          # ✓ vorhanden
modified: '2026-11-01'         # ✓ vorhanden
```

### Wiki-Link zur Übung

```markdown
**Zugehörige Übung:** [[UE-VS-VerteilteSysteme|Übung: Verteilte Systeme (Klausurformat)]]
```
✓ Korrekt formatiert, Link-Ziel und Anzeigetext stimmen.

### Callout-Format

Alle Lösungen verwenden das vorgegebene Format:
```markdown
> [!success] **Musterlösung**
> ...
```
✓ Konsistent über alle 22 Aufgaben.

### Tabellenvollständigkeit

Stichprobe der Tabellen:
- Aufgabe 1.2 (4 Hauptmerkmale): 4 Zeilen, alle Zellen gefüllt ✓
- Aufgabe 1.3 (Distributed vs. Parallel): 3 Kriterien × 2 Spalten, vollständig ✓
- Aufgabe 2.3 (HTTP-Methoden): 5 Methoden mit Beschreibung und Idempotenz-Flag ✓
- Aufgabe 3.5b (Quorum): 3 Konfigurationen, alle Berechnungen ausgefüllt ✓
- Aufgabe 5.4 (Lamport vs. Vektor): 3 Aspekte × 2 Spalten, vollständig ✓

---

## Fachliche Korrektheit

### Definitionen (Teil 1)

**Tanenbaum-Definition (1.1a):**
> *"Verteilte Systeme sind eine Sammlung von unabhängigen Computern, die sich gegenüber dem Anwender als ein kohärentes System darstellen."*

Vorlesungsnotiz `01-Definition.md`:
> "Verteilte Systeme sind eine Sammlung von unabhängigen Computern, die sich gegenüber dem Anwender als ein kohärentes System darstellen."

✓ Wörtlich übereinstimmend.

**Bal-Definition (1.1b):**
Lösung: "mehreren autonomen Prozessoren, die sich keinen Hauptspeicher teilen, aber mittels Austausch von Nachrichten über ein Netzwerk miteinander kooperieren"

Vorlesungsnotiz: identisch.
✓ Korrekt.

**Lamport-Definition (1.1b):**
Lösung: "Ein verteiltes System ist es, wenn ein Fehler eines Computers, von dessen Existenz du nichts wusstest, deinen eigenen Rechner unbrauchbar macht."

Vorlesungsnotiz: identisch (mit "Du" statt "du" – stilistische Variante).
✓ Korrekt.

### Vier Hauptmerkmale (1.2)

Lösung nennt: Skalierbarkeit, Nebenläufigkeit, Fehlertoleranz, Transparenz.

Vorlesungsnotiz `02-Eigenschaften.md` – Tabelle "Abgeleitete Merkmale":
| Merkmal | Beschreibung |
|---------|--------------|
| Skalierbarkeit | Ein verteiltes System kann (beliebig) mit zusätzlichen Ressourcen erweitert werden... |
| Nebenläufigkeit | Auf Basis von Synchronisationsalgorithmen können Teilaufgaben koordiniert... |
| Fehlertoleranz | Resilienz ist ein zwingendes Grundprinzip... |
| Transparenz | Für den Benutzer ist nicht ersichtlich... |

✓ Alle vier Merkmale und Beschreibungen stimmen überein.

### CAP-Theorem (3.1)

Lösung definiert:
- **Consistency:** "Alle Knoten sehen zur gleichen Zeit dieselben Daten – jede Leseoperation liefert den Wert der letzten Schreiboperation (Linearisierbarkeit)"
- **Availability:** "Jede Anfrage erhält eine (nicht-fehlerhafte) Antwort – ohne Garantie auf Aktualität"
- **Partition Tolerance:** "Das System arbeitet trotz Nachrichtenverlust oder Netzwerkpartitionen weiter"

Vorlesungsnotiz `01-CAP-Theorem.md`:
- "Alle Knoten sehen zur gleichen Zeit dieselben Daten" ✓
- "Jede Anfrage erhält eine (nicht-fehlerhafte) Antwort – ohne Garantie auf Aktualität" ✓
- "Das System arbeitet trotz Nachrichtenverlust oder Netzwerkpartitionen weiter" ✓

✓ Exakt übereinstimmend.

### Lamport-Uhren (5.2)

Lösung – Regeln:
| Situation | Regel |
|-----------|-------|
| Lokales Ereignis | C := C + 1 |
| Senden | C := C + 1, sende C mit der Nachricht |
| Empfangen mit T | C := max(C, T) + 1 |

Vorlesungsnotiz `02-Logische-Uhren.md`:
1. "Vor jedem lokalen Ereignis: C := C + 1"
2. "Beim Senden einer Nachricht: C := C + 1, sende C mit der Nachricht"
3. "Beim Empfangen einer Nachricht mit Zeitstempel T: C := max(C, T) + 1"

✓ Regeln stimmen überein.

**Limitation:**
Lösung: "Lamport-Uhren können keine Nebenläufigkeit erkennen... Aus C(a) < C(b) folgt nicht zwingend a → b"

Vorlesungsnotiz: "Lamport-Uhren garantieren nur: Wenn a → b, dann C(a) < C(b). Der Umkehrschluss gilt nicht!"

✓ Korrekt.

### Quorum-Berechnung (3.5)

Lösung für N=5:
| Konfiguration | W | R | R + W | > N? |
|---------------|---|---|-------|------|
| Write-optimiert | 1 | 5 | 6 | 6 > 5 ✓ |
| Read-optimiert | 5 | 1 | 6 | 6 > 5 ✓ |
| Balanced | 3 | 3 | 6 | 6 > 5 ✓ |

Mathematische Prüfung:
- 1 + 5 = 6 > 5 ✓
- 5 + 1 = 6 > 5 ✓
- 3 + 3 = 6 > 5 ✓

✓ Berechnungen korrekt.

### RPC-Ablauf (2.1)

Lösung beschreibt 5 Schritte:
1. Client-Aufruf (Stub)
2. Marshalling
3. Übertragung
4. Server-Verarbeitung (Deserialisierung + Ausführung)
5. Rückgabe (Serialisierung + Rücksendung)

Vorlesungsnotiz `01-RPC.md`:
1. Client-Aufruf: Der Client ruft eine lokale Stub-Funktion auf
2. Marshalling: Parameter werden serialisiert
3. Übertragung: Request wird über das Netzwerk zum Server gesendet
4. Server-Stub: Empfängt die Nachricht und deserialisiert die Parameter
5. Ausführung: Die eigentliche Prozedur wird auf dem Server ausgeführt
6. Rückgabe: Ergebnis wird serialisiert und an den Client zurückgesendet
7. Client empfängt: Der Client-Stub deserialisiert das Ergebnis

Die Lösung fasst die Schritte 4-5 und 6-7 zusammen – dies ist eine akzeptable Vereinfachung für Klausurformat, da die Kernschritte erhalten bleiben.

✓ Fachlich korrekt.

---

## Quellenverweise

Die Lösung enthält am Ende Wiki-Links zu den relevanten Vorlesungsnotizen:

```markdown
## Quellen

- [[01-Definition|Definition verteilter Systeme]]
- [[02-Eigenschaften|Eigenschaften verteilter Systeme]]
- [[01-RPC|Remote Procedure Call (RPC)]]
- [[03-REST|REST (Representational State Transfer)]]
...
```

✓ Quellenverweise vorhanden und konsistent mit BS-Vorlage.

</details>

---

<details>
<summary>File Map</summary>

| Datei | Beschreibung |
|-------|--------------|
| `L-VS-VerteilteSysteme.md` | Geprüfte Musterlösung |
| `UE-VS-VerteilteSysteme.md` | Zugehörige Übung (Referenz) |
| `L-BS-Betriebssysteme.md` | Format-Vorlage (Referenz) |

</details>
