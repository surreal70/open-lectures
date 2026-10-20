# Untersuchungsbericht: Kirchhoffsche Regeln in L-Physik-I

## Zusammenfassung

Die Ausarbeitung der Kirchhoffschen Regeln steht vor der Herausforderung, dass **alle Voraussetzungsdateien in Modul 08 und 09 noch TODO-Platzhalter sind**. Eine sinnvolle Ausarbeitung ist möglich, sollte aber auf Realschul-Niveau erfolgen und die Regeln als didaktische Brücke zwischen den grundlegenden Konzepten (Strom, Spannung, Widerstand) und den Anwendungen (Reihen-/Parallelschaltung, Widerstandsnetzwerke) positionieren.

---

## 1. Evidenz: Bestehende Inhalte

### Modul 09 – Schaltungsgesetze

| Datei | Status | Inhalt |
|-------|--------|--------|
| `Reihenschaltung.md` | TODO-Platzhalter | `<!-- TODO: Inhalt ergänzen -->` |
| `Parallelschaltung.md` | TODO-Platzhalter | `<!-- TODO: Inhalt ergänzen -->` |
| `Kirchhoffsche-Regeln.md` | TODO-Platzhalter | `<!-- TODO: Inhalt ergänzen -->` |
| `Widerstandsnetzwerke.md` | TODO-Platzhalter | `<!-- TODO: Inhalt ergänzen -->` |
| `Elektrische-Leistung.md` | TODO-Platzhalter | (nicht untersucht) |

**Befund:** Kein ausgearbeitetes Material vorhanden. Die Kirchhoff-Konzepte werden nirgends implizit verwendet, da alle Dateien leer sind.

### Modul 08 – Elektrischer Strom und Spannung

| Datei | Status |
|-------|--------|
| `Stromstaerke.md` | TODO-Platzhalter |
| `Spannung.md` | TODO-Platzhalter |
| `Widerstand.md` | TODO-Platzhalter |
| `Ohmsches-Gesetz.md` | TODO-Platzhalter |
| `Messschaltungen.md` | TODO-Platzhalter |

**Befund:** Alle Grundlagen-Dateien sind ebenfalls noch nicht ausgearbeitet.

### Vault-Kontext

Aus `00-Meta/00-Meta-Index.md`:
- **Niveau:** Realschule / Mittlere Reife (Wahlpflichtfächergruppe I)
- **Zielgruppe:** Schüler der Realschule, Einsteiger, Auszubildende
- **Voraussetzungen:** Grundkenntnisse in Mathematik

---

## 2. Strukturvorlagen und Konventionen

### Aus `.kiro/steering/obsidian-lecture-notes.md`

Jede Content-Note muss folgende Struktur haben:

1. **Frontmatter** (YAML: author, created, modified, tags)
2. **Titel (H1)**
3. **Callout: Lernziele** (`[!info]`)
4. **Überblick** (Einführung ins Thema)
5. **Thema 1...n** (mindestens 3 Themen)
6. **Zusammenhänge** (Crosslinks zu anderen Vault-Dokumenten)
7. **Callout: Prüfungsrelevant** (`[!warning]`)
8. **Callout: Prüfungsfragen** (`[!question]`)
9. **Quellen**
10. **Callout: Weiterführende Links** (`[!tip]`)

### Referenzbeispiel

Die Datei `L-Mathematik-I/07-Terme-und-algebraische-Ausdruecke/01-Variablen-und-Platzhalter.md` zeigt ein vollständiges Beispiel mit:
- Vollständigem Frontmatter inkl. `learning_objectives`
- Historischer Einordnung
- Tabellen für Übersicht
- Praxisbeispielen in Callouts
- Häufigen Fehlern (`[!warning]`)
- Klaren Querverweisen

---

## 3. Didaktische Einordnung

### LehrplanPLUS Bayern Realschule

Laut vorheriger Analyse (nicht in dieser Untersuchung erneut verifiziert):
- Kirchhoffsche Regeln sind **nicht explizit im LehrplanPLUS** genannt
- Sie sind **implizit notwendig** für das Verständnis von Reihen-/Parallelschaltungen (Jg. 10)
- Die Begriffe "Knotenregel" und "Maschenregel" werden im Realschulunterricht typischerweise nicht verwendet

### Empfehlung zum didaktischen Niveau

**Realschul-gerecht (empfohlen):**
- Knotenregel als "Stromerhaltung an Verzweigungen"
- Maschenregel als "Spannungen addieren sich im geschlossenen Stromkreis"
- Verzicht auf formale Summennotation (Σ)
- Anschauliche Wasserkreislauf-Analogie

**Optionale Vertiefung:**
- Formale Notation für interessierte Schüler
- Hinweis auf Gymnasium/Ingenieurstudium

---

## 4. Strukturvorschlag für Kirchhoffsche-Regeln.md

```markdown
---
title: "Kirchhoffsche Regeln"
chapter: "09"
section: "03"
type: topic
status: draft
learning_objectives:
  - "Die Knotenregel (1. Kirchhoffsches Gesetz) verstehen und anwenden"
  - "Die Maschenregel (2. Kirchhoffsches Gesetz) verstehen und anwenden"
  - "Beide Regeln zur Analyse einfacher Schaltungen nutzen"
tags:
  - physik
  - elektrizitaet
  - schaltungen
  - kirchhoff
created: 2025-01-20
modified: 2025-01-20
---

# Kirchhoffsche Regeln

> [!info] **Lernziele**
> - Die Knotenregel (1. Kirchhoffsches Gesetz) verstehen und anwenden
> - Die Maschenregel (2. Kirchhoffsches Gesetz) verstehen und anwenden
> - Beide Regeln zur Analyse einfacher Schaltungen nutzen

## Überblick

Die Kirchhoffschen Regeln beschreiben, wie sich Strom und Spannung in
elektrischen Schaltungen verhalten. Sie wurden 1845 von Gustav Robert
Kirchhoff formuliert und bilden die Grundlage für die Analyse aller
elektrischen Netzwerke.

## Die Knotenregel (1. Kirchhoffsches Gesetz)

### Grundidee
[Wasserkreislauf-Analogie: Was hineinfließt, muss auch herausfließen]

### Formulierung
[Summe der zufließenden Ströme = Summe der abfließenden Ströme]

### Anwendungsbeispiel
[Stromverzweigung mit konkreten Zahlenwerten]

## Die Maschenregel (2. Kirchhoffsches Gesetz)

### Grundidee
[Höhenunterschied-Analogie: Rundweg ohne Höhenänderung]

### Formulierung
[Summe aller Spannungen in einem geschlossenen Stromkreis = 0]

### Anwendungsbeispiel
[Reihenschaltung mit Spannungsmessung]

## Anwendung in Schaltungen

### Einfache Stromverzweigung
[Rechenbeispiel mit Knotenregel]

### Reihenschaltung von Widerständen
[Rechenbeispiel mit Maschenregel]

### Kombinierte Anwendung
[Einfaches Netzwerk mit beiden Regeln]

## Zusammenhänge

Voraussetzungen:
- → [[../08-Elektrischer-Strom-und-Spannung/Stromstaerke|Stromstärke]]
- → [[../08-Elektrischer-Strom-und-Spannung/Spannung|Spannung]]
- → [[../08-Elektrischer-Strom-und-Spannung/Ohmsches-Gesetz|Ohmsches Gesetz]]

Weiterführend:
- → [[Reihenschaltung]]
- → [[Parallelschaltung]]
- → [[Widerstandsnetzwerke]]

> [!warning] **Prüfungsrelevant**
> - Knotenregel: Stromaufteilung an Verzweigungspunkten berechnen
> - Maschenregel: Spannungen in Reihenschaltungen bestimmen
> - Kombination beider Regeln für einfache Netzwerke

> [!question] **Typische Prüfungsfragen**
> - An einem Knotenpunkt fließen 2 A und 3 A zu. Wie groß ist der abfließende Strom?
> - Eine Batterie mit 9 V versorgt zwei Lampen in Reihe. Die erste hat 4 V. Welche Spannung liegt an der zweiten?
> - Erkläre mit eigenen Worten, warum sich Ströme an Verzweigungen aufteilen.

## Quellen

- Lambacher Schweizer Physik (Realschule)
- Dorn-Bader Physik

> [!tip] **Weiterführende Links**
> - [[../17-Elektrizitaetslehre-Vertiefung/17-Elektrizitaetslehre-Vertiefung-Index|Elektrizitätslehre – Vertiefung]] (für formale Behandlung)
> - [Leifiphysik: Kirchhoffsche Regeln](https://www.leifiphysik.de/)
```

---

## 5. Empfehlungen für Diagramme/Illustrationen

### Empfohlene PNG-Grafiken

| Grafik | Beschreibung | Priorität |
|--------|--------------|-----------|
| `kirchhoff-knotenregel.png` | Knotenpunkt mit 3 Strompfeilen (zufließend/abfließend) | Hoch |
| `kirchhoff-maschenregel.png` | Geschlossene Masche mit Spannungspfeilen | Hoch |
| `kirchhoff-wasseranalogie.png` | Wasserkreislauf als Veranschaulichung | Mittel |
| `kirchhoff-beispielschaltung.png` | Einfache Schaltung mit Widerständen | Mittel |

### Stilempfehlung

Gemäß `math-graphics.md` Steering:
- **Hintergrund:** Grau (#E5E7EB)
- **Primärfarbe:** Blau (#2563EB)
- **Mehrfarbig** (2-3 Blau-Variationen) für bessere Unterscheidbarkeit
- Pfeile für Strom- und Spannungsrichtungen
- Beschriftungen mit Symbolen (I₁, I₂, U₁, U₂)

---

## 6. Abhängigkeiten und Reihenfolge

### Empfohlene Ausarbeitungsreihenfolge für Modul 09

1. **Zuerst Modul 08 ausarbeiten** (Grundlagen!)
   - Stromstärke
   - Spannung
   - Widerstand
   - Ohmsches Gesetz

2. **Dann Modul 09:**
   1. Kirchhoffsche Regeln (als theoretische Basis)
   2. Reihenschaltung (Anwendung der Maschenregel)
   3. Parallelschaltung (Anwendung der Knotenregel)
   4. Elektrische Leistung
   5. Widerstandsnetzwerke (kombinierte Anwendung)

### Alternative: Isolierte Ausarbeitung

Falls nur Kirchhoffsche-Regeln.md ausgearbeitet werden soll:
- Kurze Wiederholung der Grundbegriffe (I, U, R) im Überblick einfügen
- Explizite Hinweise auf fehlende Voraussetzungen als TODO-Links
- Eigenständig verständliche Erklärungen

---

## 7. Fazit und Empfehlungen

### Haupterkenntnisse

1. **Alle relevanten Dateien sind Platzhalter** – keine existierenden Inhalte zum Aufbauen
2. **Vault-Niveau ist Realschule** – didaktisch angepasste Darstellung erforderlich
3. **Kirchhoff als Brücke** – verbindet Grundlagen (Modul 08) mit Anwendungen (Rest von Modul 09)

### Empfehlungen

1. **Idealer Ansatz:** Zuerst Modul 08 ausarbeiten, dann Kirchhoff
2. **Pragmatischer Ansatz:** Kirchhoff eigenständig ausarbeiten mit eingebetteten Grundlagen
3. **Didaktisches Niveau:** Realschul-gerecht ohne formale Notation, mit Alltagsanalogien
4. **Grafiken:** Mindestens Knotenregel- und Maschenregel-Diagramme als PNG

### Offene Fragen

- Soll die formale Notation (Σ) als optionale Vertiefung enthalten sein?
- Wie umfangreich sollen Rechenbeispiele sein?
- Sollen Übungsaufgaben direkt in die Datei oder in separate Übungsdateien?
