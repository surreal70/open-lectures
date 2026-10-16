---
title: "Einfache Sortierverfahren"
created: 2026-10-13
modified: 2026-10-13
type: lecture
tags:
  - lf11a
  - algorithmen
  - sortierung
  - insertion-sort
  - selection-sort
  - bubble-sort
source: proTirone (CC-BY-4.0)
---

# Einfache Sortierverfahren

> [!info] Lernziele
> - Insertion Sort, Selection Sort und Bubble Sort verstehen
> - Die Algorithmen implementieren können
> - Unterschiede und Namensgebung kennen

## Übersicht

| Algorithmus | Prinzip | Komplexität | Stabil |
|-------------|---------|-------------|--------|
| **Insertion Sort** | Einfügen an richtiger Stelle | O(n²) | ✅ Ja |
| **Selection Sort** | Auswählen des nächsten Elements | O(n²) | ❌ Nein |
| **Bubble Sort** | Paarweises Vertauschen | O(n²) | ✅ Ja |

---

## Insertion Sort (Einfügesortieren)

### Namensgebung

> Der Name kommt daher, dass man immer die oberste Karte vom unsortierten Stapel nimmt und an der richtigen Stelle im sortierten Stapel **einfügt**.

### Prinzip

1. Nimm das nächste Element aus dem unsortierten Bereich
2. Finde die richtige Position im sortierten Bereich
3. Füge das Element dort ein (verschiebe andere nach rechts)

### Visualisierung

```
Unsortiert: [5, 2, 8, 1]

Schritt 1: [5] | [2, 8, 1]    → 5 ist sortiert
Schritt 2: [2, 5] | [8, 1]    → 2 vor 5 eingefügt
Schritt 3: [2, 5, 8] | [1]    → 8 am Ende eingefügt
Schritt 4: [1, 2, 5, 8] | []  → 1 am Anfang eingefügt
```

### Python-Implementierung

```python
def insertion_sort(liste):
    for i in range(1, len(liste)):
        aktuell = liste[i]
        j = i - 1
        
        # Verschiebe größere Elemente nach rechts
        while j >= 0 and liste[j] > aktuell:
            liste[j + 1] = liste[j]
            j -= 1
        
        # Füge Element an richtiger Stelle ein
        liste[j + 1] = aktuell
    
    return liste
```

### Eigenschaften

- **Best Case O(n)**: Bereits sortierte Liste
- **In-place**: Kein zusätzlicher Speicher nötig
- **Stabil**: Relative Reihenfolge bleibt erhalten
- **Gut für**: Kleine Listen, fast sortierte Daten

---

## Selection Sort (Auswahlsortieren)

### Namensgebung

> Der Name kommt daher, dass man aus dem unsortierten Stapel immer das von der Zielreihenfolge her nächste Element **auswählt**.

### Prinzip

1. Finde das kleinste Element im unsortierten Bereich
2. Tausche es mit dem ersten Element des unsortierten Bereichs
3. Verkleinere den unsortierten Bereich um 1

### Visualisierung

```
[5, 2, 8, 1]

Schritt 1: Minimum = 1 → [1, 2, 8, 5] | []
Schritt 2: Minimum = 2 → [1, 2, 8, 5] | (2 bleibt)
Schritt 3: Minimum = 5 → [1, 2, 5, 8] | 
Schritt 4: [1, 2, 5, 8] → fertig
```

### Python-Implementierung

```python
def selection_sort(liste):
    n = len(liste)
    
    for i in range(n):
        # Finde Index des Minimums im unsortierten Bereich
        min_idx = i
        for j in range(i + 1, n):
            if liste[j] < liste[min_idx]:
                min_idx = j
        
        # Tausche Minimum an die richtige Position
        liste[i], liste[min_idx] = liste[min_idx], liste[i]
    
    return liste
```

### Eigenschaften

- **Immer O(n²)**: Auch bei sortierter Liste
- **In-place**: Kein zusätzlicher Speicher
- **Instabil**: Relative Reihenfolge kann sich ändern
- **Wenige Swaps**: Maximal n Vertauschungen

---

## Bubble Sort (Blasensortieren)

### Namensgebung

> Der Name kommt daher, dass Elemente auf falschen Positionen schrittweise „wie Blasen" nach oben an ihre richtige Position **aufsteigen**.

### Prinzip

1. Gehe die Liste von vorne durch
2. Vergleiche jeweils zwei benachbarte Elemente
3. Tausche sie, wenn sie in falscher Reihenfolge sind
4. Wiederhole, bis keine Vertauschungen mehr nötig

### Visualisierung

```
[5, 2, 8, 1]

Durchlauf 1:
  [5, 2, 8, 1] → 5 > 2 → tauschen → [2, 5, 8, 1]
  [2, 5, 8, 1] → 5 < 8 → ok
  [2, 5, 8, 1] → 8 > 1 → tauschen → [2, 5, 1, 8]

Durchlauf 2:
  [2, 5, 1, 8] → 2 < 5 → ok
  [2, 5, 1, 8] → 5 > 1 → tauschen → [2, 1, 5, 8]

Durchlauf 3:
  [2, 1, 5, 8] → 2 > 1 → tauschen → [1, 2, 5, 8]

Durchlauf 4: Keine Tausche → FERTIG
```

### Python-Implementierung

```python
def bubble_sort(liste):
    n = len(liste)
    
    for i in range(n):
        getauscht = False
        
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
                getauscht = True
        
        # Optimierung: Abbruch wenn nichts getauscht wurde
        if not getauscht:
            break
    
    return liste
```

### Eigenschaften

- **Best Case O(n)**: Bereits sortierte Liste (mit Optimierung)
- **In-place**: Kein zusätzlicher Speicher
- **Stabil**: Relative Reihenfolge bleibt erhalten
- **Viele Swaps**: Oft ineffizient

---

## Vergleich

| Kriterium | Insertion | Selection | Bubble |
|-----------|-----------|-----------|--------|
| Best Case | O(n) ✅ | O(n²) | O(n) ✅ |
| Worst Case | O(n²) | O(n²) | O(n²) |
| Speicher | O(1) | O(1) | O(1) |
| Stabil | ✅ Ja | ❌ Nein | ✅ Ja |
| Swaps | Wenige | Sehr wenige | Viele |

> [!tip] Empfehlung
> Für kleine oder fast sortierte Listen: **Insertion Sort**
> Für minimale Swap-Anzahl: **Selection Sort**
> Bubble Sort hauptsächlich zu Lernzwecken

## Prüfungsrelevanz

> [!question] Typische Prüfungsfragen
> - Warum heißt Insertion Sort "Insertion Sort"?
> - Implementieren Sie einen der drei Algorithmen
> - Sortieren Sie die gegebene Liste schrittweise mit Bubble Sort
> - Welcher der drei Algorithmen ist stabil?

## Querverweise

- → [[02-Rekursive-Verfahren|Rekursive Verfahren]] – Quick Sort, Merge Sort
- → [[../01-Algorithmen/01-Grundlagen|Algorithmen-Grundlagen]] – Komplexitätsanalyse
- → [[../02-Suchalgorithmen/01-Lineare-Suche|Lineare Suche]] – Wird intern verwendet

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (CC-BY-4.0).
