---
title: "LF11a – Softwareentwicklung (AE)"
created: 2026-10-13
modified: 2026-10-13
type: index
tags:
  - index
  - lf11a
  - algorithmen
  - programmierung
  - anwendungsentwicklung
source: proTirone (CC-BY-4.0)
---

# LF11a – Softwareentwicklung

> [!info] Lernfeld-Überblick
> **Ausbildungsjahr:** 3
> **Zeitrichtwert:** 80 Stunden
> **Fachrichtung:** Anwendungsentwicklung
> **Status:** ✅ Inhalte verfügbar

## Kompetenzbeschreibung

Die Schülerinnen und Schüler verfügen über die Kompetenz, Algorithmen zu entwerfen und zu implementieren sowie deren Komplexität zu analysieren.

## Inhalte

### 01 – Algorithmen
- [x] [[01-Algorithmen/01-Grundlagen|Algorithmen-Grundlagen]] – O-Notation, Komplexitätsklassen, Bewertungskriterien

### 02 – Suchalgorithmen
- [x] [[02-Suchalgorithmen/01-Lineare-Suche|Lineare Suche]] – Sequentielle Suche, O(n)
- [x] [[02-Suchalgorithmen/02-Binaere-Suche|Binäre Suche]] – Intervallhalbierung, O(log n), Binärer Suchbaum

### 03 – Sortieralgorithmen
- [x] [[03-Sortieralgorithmen/01-Einfache-Verfahren|Einfache Verfahren]] – Insertion Sort, Selection Sort, Bubble Sort
- [x] [[03-Sortieralgorithmen/02-Rekursive-Verfahren|Rekursive Verfahren]] – Quick Sort, Merge Sort, Divide & Conquer

## Prüfungsrelevante Themen

Aus den IHK-Prüfungskatalogen (AP2):

### Algorithmen
- [x] O-Notation (Landau-Symbole)
- [x] Komplexitätsklassen
- [x] Rekursion vs. Iteration
- [x] Divide and Conquer

### Suchalgorithmen
- [x] Lineare Suche
- [x] Binäre Suche
- [x] Binärer Suchbaum

### Sortieralgorithmen
- [x] Insertion Sort
- [x] Selection Sort
- [x] Bubble Sort
- [x] Quick Sort
- [x] Merge Sort
- [ ] Shell Sort
- [ ] Heap Sort

## Übersicht: Algorithmenvergleich

| Algorithmus | Best | Average | Worst | Speicher | Stabil |
|-------------|------|---------|-------|----------|--------|
| Lineare Suche | O(1) | O(n) | O(n) | O(1) | – |
| Binäre Suche | O(1) | O(log n) | O(log n) | O(1) | – |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | ❌ |
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ |

## Querverweise

- → [[../00-LF10-Index|LF10 – Fachrichtungsspezifisch]]
- → [[../../07-LF07-Softwareprojekte/00-LF07-Index|LF07 – Softwareprojekte]]
- → [[../../05-LF05-Software/00-LF05-Index|LF05 – Software entwickeln]]

---

> [!quote] Quellenhinweis
> Inhalte basieren auf Materialien von proTirone (Karsten Reincke), lizenziert unter CC-BY-4.0.
