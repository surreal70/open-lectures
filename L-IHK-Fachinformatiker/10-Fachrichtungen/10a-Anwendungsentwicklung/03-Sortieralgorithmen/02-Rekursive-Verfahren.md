---
title: "Rekursive Sortierverfahren"
created: 2026-10-13
modified: 2026-10-13
type: lecture
tags:
  - lf11a
  - algorithmen
  - sortierung
  - quicksort
  - mergesort
  - rekursion
  - divide-and-conquer
source: proTirone (CC-BY-4.0)
---

# Rekursive Sortierverfahren

> [!info] Lernziele
> - Quick Sort und Merge Sort verstehen
> - Rekursion und Divide-and-Conquer-Prinzip anwenden
> - Unterschiede zwischen den Verfahren kennen

## Übersicht

| Algorithmus | Prinzip | Average | Worst | Speicher | Stabil |
|-------------|---------|---------|-------|----------|--------|
| **Quick Sort** | Partitionierung um Pivot | O(n log n) | O(n²) | O(log n) | ❌ |
| **Merge Sort** | Teilen und Zusammenführen | O(n log n) | O(n log n) | O(n) | ✅ |

## Divide and Conquer

Beide Algorithmen folgen dem **Teile-und-Herrsche**-Prinzip:

1. **Divide**: Teile das Problem in kleinere Teilprobleme
2. **Conquer**: Löse die Teilprobleme (rekursiv)
3. **Combine**: Füge die Teillösungen zusammen

---

## Quick Sort

### Prinzip

1. Wähle ein **Pivot-Element** (möglichst mittig im Wertebereich)
2. **Partitioniere** die Liste:
   - Links: alle Elemente < Pivot
   - Rechts: alle Elemente ≥ Pivot
3. Sortiere beide Teillisten rekursiv
4. Füge zusammen: linke Liste + Pivot + rechte Liste

> [!note] Sortierarbeit
> Die eigentliche Arbeit findet **vor** dem rekursiven Aufruf statt (auf dem „Hinweg").

### Visualisierung

```
[5, 2, 8, 1, 9, 3]    Pivot = 5

Partitionierung:
  < 5: [2, 1, 3]
  ≥ 5: [5, 8, 9]

Rekursion links: [2, 1, 3] → Pivot = 2
  < 2: [1]
  ≥ 2: [2, 3]
  Ergebnis: [1, 2, 3]

Rekursion rechts: [5, 8, 9] → Pivot = 8
  < 8: [5]
  ≥ 8: [8, 9]
  Ergebnis: [5, 8, 9]

Endergebnis: [1, 2, 3] + [5, 8, 9] = [1, 2, 3, 5, 8, 9]
```

### Python-Implementierung

```python
def quick_sort(liste):
    # Abbruchbedingung
    if len(liste) <= 1:
        return liste
    
    # Pivot wählen (hier: mittleres Element)
    pivot = liste[len(liste) // 2]
    
    # Partitionierung
    kleiner = [x for x in liste if x < pivot]
    gleich = [x for x in liste if x == pivot]
    groesser = [x for x in liste if x > pivot]
    
    # Rekursion und Zusammenführung
    return quick_sort(kleiner) + gleich + quick_sort(groesser)

# Beispiel
zahlen = [5, 2, 8, 1, 9, 3]
print(quick_sort(zahlen))  # [1, 2, 3, 5, 8, 9]
```

### Eigenschaften

- **Average Case O(n log n)**: Bei guter Pivot-Wahl
- **Worst Case O(n²)**: Bei schlechter Pivot-Wahl (z.B. bereits sortiert, Pivot = erstes Element)
- **In-place möglich**: Mit entsprechender Implementierung
- **Instabil**: Relative Reihenfolge nicht garantiert

---

## Merge Sort

### Prinzip

1. **Teile** die Liste in zwei gleich große Hälften
2. Sortiere beide Hälften rekursiv
3. **Merge** die sortierten Hälften zusammen

> [!note] Sortierarbeit
> Die eigentliche Arbeit findet **nach** dem rekursiven Aufruf statt (auf dem „Rückweg").

### Visualisierung

```
[5, 2, 8, 1, 9, 3]

TEILEN (Hinweg):
         [5, 2, 8, 1, 9, 3]
              /        \
       [5, 2, 8]      [1, 9, 3]
        /    \          /    \
     [5, 2]  [8]     [1, 9]  [3]
      /  \            /  \
    [5]  [2]       [1]  [9]

MERGEN (Rückweg):
    [5]  [2]       [1]  [9]
      \  /            \  /
     [2, 5]  [8]     [1, 9]  [3]
        \    /          \    /
       [2, 5, 8]      [1, 3, 9]
              \        /
         [1, 2, 3, 5, 8, 9]
```

### Python-Implementierung

```python
def merge_sort(liste):
    # Abbruchbedingung
    if len(liste) <= 1:
        return liste
    
    # Teilen
    mitte = len(liste) // 2
    links = merge_sort(liste[:mitte])
    rechts = merge_sort(liste[mitte:])
    
    # Mergen
    return merge(links, rechts)

def merge(links, rechts):
    """Fügt zwei sortierte Listen zu einer sortierten Liste zusammen."""
    ergebnis = []
    i = j = 0
    
    while i < len(links) and j < len(rechts):
        if links[i] <= rechts[j]:
            ergebnis.append(links[i])
            i += 1
        else:
            ergebnis.append(rechts[j])
            j += 1
    
    # Restliche Elemente anhängen
    ergebnis.extend(links[i:])
    ergebnis.extend(rechts[j:])
    
    return ergebnis
```

### Eigenschaften

- **Immer O(n log n)**: Garantierte Performance
- **Speicher O(n)**: Benötigt zusätzlichen Speicher für Merge
- **Stabil**: Relative Reihenfolge bleibt erhalten
- **Gut für**: Große Datenmengen, externe Sortierung (Dateien)

---

## Vergleich: Quick Sort vs. Merge Sort

| Kriterium | Quick Sort | Merge Sort |
|-----------|------------|------------|
| Average | O(n log n) | O(n log n) |
| Worst Case | O(n²) ❌ | O(n log n) ✅ |
| Speicher | O(log n) ✅ | O(n) ❌ |
| Stabil | ❌ Nein | ✅ Ja |
| Sortierarbeit | Vor Rekursion | Nach Rekursion |
| Pivot nötig? | ✅ Ja | ❌ Nein |

> [!tip] Wann welchen verwenden?
> - **Quick Sort**: Wenn Speicher knapp ist und Pivot gut wählbar
> - **Merge Sort**: Wenn garantierte Performance wichtig ist

## Rekursion verstehen

```
┌────────────────────────────────────────┐
│           Rekursiver Aufruf            │
│                                        │
│  1. Abbruchbedingung prüfen            │
│     └─► Wenn erfüllt: Rückgabe         │
│                                        │
│  2. Problem verkleinern                │
│     └─► Teilprobleme erzeugen          │
│                                        │
│  3. Rekursiver Aufruf für Teilprobleme │
│     └─► Aufruf derselben Funktion      │
│                                        │
│  4. Ergebnisse kombinieren             │
│     └─► Teillösungen zusammenführen    │
└────────────────────────────────────────┘
```

## Prüfungsrelevanz

> [!question] Typische Prüfungsfragen
> - Was ist ein Pivot-Element?
> - Wo findet bei Quick Sort / Merge Sort die Sortierarbeit statt?
> - Warum kann Quick Sort im Worst Case O(n²) haben?
> - Implementieren Sie die Merge-Funktion
> - Erklären Sie das Divide-and-Conquer-Prinzip

## Querverweise

- → [[01-Einfache-Verfahren|Einfache Verfahren]] – Insertion, Selection, Bubble Sort
- → [[../01-Algorithmen/01-Grundlagen|Algorithmen-Grundlagen]] – Komplexitätsanalyse
- → [[../02-Suchalgorithmen/02-Binaere-Suche|Binäre Suche]] – Ähnliches Teilungsprinzip

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (CC-BY-4.0).
