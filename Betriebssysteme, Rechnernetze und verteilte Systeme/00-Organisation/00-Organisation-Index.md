---
author: Andreas Hümmer
title: "Meta Index"
tags: [index, meta, vault-info]
created: 2026-10-07
modified: 2026-10-07
bereich: Meta
---
author: Andreas Hümmer

# Betriebssysteme, Rechnernetze und verteilte Systeme

> **Obsidian Vault für den IU-Kurs SS 2026**

## Vault-Informationen

| Eigenschaft | Wert |
|-------------|------|
| **Autor** | Andreas Hümmer |
| **Copyright** | © 2026 Andreas Hümmer |
| **Kurs** | Betriebssysteme, Rechnernetze und verteilte Systeme (IU) |
| **Semester** | Sommersemester 2026 |
| **Erstellt** | Oktober 2026 |

## Versionen

| Bereich | Version | Status |
|---------|---------|--------|
| **Betriebssysteme** | 0.9.3 | In Bearbeitung |
| **Rechnernetze** | 0.1.0 | Begonnen |
| **Verteilte Systeme** | 0.1.0 | Begonnen |

## Struktur

| Ordner | Inhalt |
|--------|--------|
| `00-Meta` | Vault-Informationen und Metadaten |
| `01-Orga` | Kursorganisation, Zeitplan, Bewertung |
| `02-Betriebssysteme` | Hauptteil: Betriebssysteme |
| `03-Rechnernetze` | Hauptteil: Rechnernetze |
| `04-Verteilte-Systeme` | Hauptteil: Verteilte Systeme |
| `05-Uebungen` | Übungsaufgaben und Lösungen |
| `06-Pruefungsvorbereitung` | Zusammenfassungen und Prüfungstipps |
| `07-Anhang` | Referenzmaterial (RFCs, IEEE, Kommandos) |

---
author: Andreas Hümmer

## Farbcodierung der Callout-Boxen

In diesem Vault werden verschiedene Callout-Boxen verwendet, um Informationen zu kategorisieren. Die Farbcodierung ist konsistent über alle Dokumente:

### Lernziele und Informationen

> [!info] **Lernziele**
> Blaue Boxen mit dem Info-Symbol kennzeichnen die **Lernziele** am Anfang jedes Kapitels. Sie beschreiben, welche Kompetenzen nach dem Durcharbeiten erworben werden sollten.

> [!note] **Hinweis / Erklärung**
> Blaue Boxen mit Notiz-Symbol enthalten ergänzende Erklärungen und Hintergrundinformationen.

### Prüfungsrelevante Inhalte

> [!warning] **Prüfungsrelevant**
> Gelb/orange Boxen markieren **prüfungsrelevante Themen**. Diese Inhalte sollten für die Prüfung beherrscht werden.

> [!question] **Häufige Prüfungsfragen**
> Hellblaue Boxen mit Fragezeichen enthalten typische **Prüfungsfragen**, die in Klausuren vorkommen können.

### Lerntipps und Merkhilfen

> [!tip] **Merkhilfen / Tipps**
> Grüne Boxen enthalten **Eselsbrücken und Merkhilfen**, die das Lernen erleichtern.

> [!example] **Beispiele**
> Violette Boxen zeigen **praktische Beispiele** zur Veranschaulichung von Konzepten.

### Warnungen und wichtige Hinweise

> [!danger] **Achtung / Fehlerquellen**
> Rote Boxen warnen vor **häufigen Fehlern** und Missverständnissen.

> [!bug] **Bekannte Probleme**
> Rote Boxen mit Bug-Symbol weisen auf **bekannte Probleme** oder Einschränkungen hin.

### Zusatzinformationen

> [!quote] **Zitate / Definitionen**
> Graue Boxen enthalten **Zitate** aus Fachliteratur oder formale **Definitionen**.

> [!abstract] **Zusammenfassung**
> Graue Boxen mit Abstract-Symbol fassen **Kernpunkte** eines Abschnitts zusammen.

### Nicht prüfungsrelevant

> [!info] **Nicht prüfungsrelevant**
> Blaue Boxen mit diesem Titel kennzeichnen **interessante Zusatzinformationen**, die für die Prüfung nicht relevant sind, aber das Verständnis vertiefen.

---
author: Andreas Hümmer

## Verwendete Symbole und Konventionen

| Symbol | Bedeutung |
|--------|-----------|
| `→` | Verweis auf anderes Dokument (Crosslink) |
| `[[...]]` | Obsidian-interner Link |
| `#tag` | Schlagwort zur Kategorisierung |
| `┌─┐` | ASCII-Diagramme zur Visualisierung |
| `≈` | Ungefähr / Circa |
| `⊕` | XOR (Exklusiv-Oder) |

---
author: Andreas Hümmer

## Changelog

### Version 0.9.3 (Betriebssysteme) - Oktober 2026
- **Ordnerstruktur reorganisiert** (logischere Reihenfolge):
  - 01-Einfuehrung (unverändert)
  - 02-Architektur (unverändert)
  - 03-Prozesse (unverändert)
  - 04-Synchronisation (vorher 07) – folgt logisch auf Prozesse
  - 05-Speicherverwaltung (vorher 04)
  - 06-Ein-Ausgabe (unverändert)
  - 07-Dateisysteme (vorher 05) – ans Ende verschoben
- Alle Dateien umbenannt (neue Präfixe)
- Alle internen Crosslinks aktualisiert

### Version 0.9.2 (Betriebssysteme) - Oktober 2026
- **Kapitel 03-Prozesse komplett überarbeitet**
  - 03-01-Prozessmodell: PCB, Prozesszustände, Interrupts, ASCII-Diagramme
  - 03-02-Scheduling: FCFS, RR, SJF, SRTF, HRRN, MLFQ mit Berechnungen
  - 03-03-Threads: User-/Kernel-Threads, Multithreading vs. Multitasking
  - 03-04-Interprozesskommunikation: Pipes, Signals, Sockets, Shared Memory
- **Kapitel 04-Speicherverwaltung komplett überarbeitet**
  - 04-01-Adressraeume: MMU, Belegungsstrategien, Speicherschutz
  - 04-02-Virtueller-Speicher: Speicherhierarchie, Swapping, Demand Paging
  - 04-03-Paging: Page Tables, TLB, Ersetzungsalgorithmen
- **Kapitel 07-Synchronisation komplett überarbeitet**
  - 07-01-Kritische-Abschnitte: Race Conditions, Mutex, Lösungsansätze
  - 07-02-Semaphore: P/V Operationen, Producer-Consumer
  - 07-03-Deadlocks: Coffman-Bedingungen, Banker's Algorithm
- Alle Dokumente mit Lernzielen, Prüfungstipps und ASCII-Diagrammen
- Quellmaterial: IU Skript Teil 5 (Ressourcen) integriert

### Version 0.9.1 (Betriebssysteme) - Oktober 2026
- **Architektur-Kapitel vervollständigt** (02-Architektur)
  - 02-03-Systemaufrufe: Lernziele hinzugefügt, Prüfungstipps strukturiert
  - 02-04-Von-Neumann-vs-Harvard: Lernziele und Prüfungsrelevanz ergänzt
  - 02-05-RISC-vs-CISC: Lernziele und Prüfungsrelevanz ergänzt
  - 02-06-CPU-Architekturen: Vollständige Dokumentation
- **Callout-Boxen vereinheitlicht** über alle Dokumente
  - `[!info]` für Lernziele (konsistent)
  - `[!warning]` für Prüfungsrelevant
  - `[!question]` für Häufige Prüfungsfragen
  - `[!tip]` für Merkhilfen
- **Meta-Index erweitert**
  - Farbcodierung der Callout-Boxen dokumentiert
  - Symbole und Konventionen hinzugefügt
  - Weiterführende Ressourcen mit externen Links

### Version 0.7.1 (Betriebssysteme) - Oktober 2026
- Einführung und Historie vollständig
- Neuer Abschnitt: Einprogramm- zu Mehrprogrammbetrieb
- RFC-Dokumentation erweitert (52 RFCs)
- IEEE 802 Standards hinzugefügt

### Version 0.1.0 (Rechnernetze) - Oktober 2026
- Grundstruktur angelegt
- Historie begonnen

### Version 0.1.0 (Verteilte Systeme) - Oktober 2026
- Grundstruktur angelegt


