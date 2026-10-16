---
title: "Binäre Suche"
created: 2026-10-13
modified: 2026-10-13
type: lecture
tags:
  - lf11a
  - algorithmen
  - suche
  - binaere-suche
  - binary-search
  - divide-and-conquer
source: proTirone (CC-BY-4.0)
---

# Binäre Suche

> [!info] Lernziele
> - Binäre Suche verstehen und implementieren
> - Iterative und rekursive Variante kennen
> - Voraussetzungen und Komplexität verstehen

## Definition

Die **binäre Suche** (auch: Intervallhalbierung) teilt den Suchbereich in jeder Iteration in zwei Hälften und verwirft die Hälfte, die das gesuchte Element nicht enthalten kann.

> [!warning] Voraussetzung
> Die Daten **müssen sortiert** sein!

## Prinzip: Divide and Conquer

```
Suchbereich:  [ 1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 ]
Suche nach: 11
                         ↓ Mitte (7)
              11 > 7 → rechte Hälfte

Suchbereich:            [ 9 | 11 | 13 | 15 ]
                              ↓ Mitte (11)
              11 = 11 → GEFUNDEN!
```

## Algorithmus

### Iterative Variante

```python
def binaere_suche_iterativ(liste, such_element):
    """
    Binäre Suche (iterativ).
    Gibt den Index zurück oder -1 wenn nicht gefunden.
    """
    links = 0
    rechts = len(liste) - 1
    
    while links <= rechts:
        mitte = (links + rechts) // 2
        
        if liste[mitte] == such_element:
            return mitte
        elif liste[mitte] < such_element:
            links = mitte + 1  # Rechte Hälfte
        else:
            rechts = mitte - 1  # Linke Hälfte
    
    return -1  # Nicht gefunden

# Beispiel
zahlen = [1, 3, 5, 7, 9, 11, 13, 15]
index = binaere_suche_iterativ(zahlen, 11)
print(f"Gefunden an Index: {index}")  # Ausgabe: 5
```

### Rekursive Variante

```python
def binaere_suche_rekursiv(liste, such_element, links=0, rechts=None):
    """
    Binäre Suche (rekursiv).
    """
    if rechts is None:
        rechts = len(liste) - 1
    
    # Abbruchbedingung: Suchbereich leer
    if links > rechts:
        return -1
    
    mitte = (links + rechts) // 2
    
    if liste[mitte] == such_element:
        return mitte
    elif liste[mitte] < such_element:
        return binaere_suche_rekursiv(liste, such_element, mitte + 1, rechts)
    else:
        return binaere_suche_rekursiv(liste, such_element, links, mitte - 1)
```

## Visualisierung

```
Suche nach 11 in [1, 3, 5, 7, 9, 11, 13, 15]

Schritt 1: links=0, rechts=7, mitte=3
           [ 1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 ]
                        ↑
           7 < 11 → links = 4

Schritt 2: links=4, rechts=7, mitte=5
                        [ 9 | 11 | 13 | 15 ]
                              ↑
           11 = 11 → GEFUNDEN an Index 5

Anzahl Vergleiche: 2 (statt bis zu 8 bei linearer Suche)
```

## Komplexität

| Fall | Komplexität | Vergleiche (bei n=1000) |
|------|-------------|-------------------------|
| **Best Case** | O(1) | 1 |
| **Average Case** | O(log n) | ~10 |
| **Worst Case** | O(log n) | ~10 |

> [!tip] Effizienz
> Bei 1.000.000 Elementen braucht die binäre Suche maximal ~20 Vergleiche, während die lineare Suche im Schnitt 500.000 benötigt!

## Vergleich: Linear vs. Binär

| Elemente (n) | Linear (Worst) | Binär (Worst) |
|--------------|----------------|---------------|
| 10 | 10 | 4 |
| 100 | 100 | 7 |
| 1.000 | 1.000 | 10 |
| 1.000.000 | 1.000.000 | 20 |

## Binärer Suchbaum

Eine alternative Datenstruktur für effiziente Suche:

```
        8
       / \
      4   12
     / \  / \
    2  6 10  14
```

**Eigenschaften:**
- Jeder Knoten hat maximal 2 Kinder
- Linkes Kind < Vater < Rechtes Kind
- Suche: O(log n) bei balanciertem Baum

> [!note] Anwendung
> Binäre Suchbäume lohnen sich, wenn Daten häufiger gelesen als geschrieben werden (z.B. Dateisysteme).

## Prüfungsrelevanz

> [!question] Typische Prüfungsfragen
> - Welche Voraussetzung hat die binäre Suche?
> - Implementieren Sie eine binäre Suche (iterativ oder rekursiv)
> - Wie viele Vergleiche braucht die binäre Suche maximal bei n Elementen?
> - Vergleichen Sie lineare und binäre Suche

## Querverweise

- → [[01-Lineare-Suche|Lineare Suche]] – Für unsortierte Daten
- → [[../01-Algorithmen/01-Grundlagen|Algorithmen-Grundlagen]] – O-Notation
- → [[../03-Sortieralgorithmen/03-Rekursive-Verfahren|Rekursive Sortierverfahren]] – Ähnliches Prinzip

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (CC-BY-4.0).
