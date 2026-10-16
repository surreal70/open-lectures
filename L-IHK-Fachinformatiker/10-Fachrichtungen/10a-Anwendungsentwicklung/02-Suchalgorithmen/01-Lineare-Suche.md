---
title: "Lineare Suche"
created: 2026-10-13
modified: 2026-10-13
type: lecture
tags:
  - lf11a
  - algorithmen
  - suche
  - lineare-suche
  - sequential-search
source: proTirone (CC-BY-4.0)
---

# Lineare Suche

> [!info] Lernziele
> - Lineare Suche verstehen und implementieren
> - Anwendungsfälle erkennen
> - Komplexität analysieren

## Definition

Die **lineare Suche** (auch: sequentielle Suche) durchsucht eine Liste Element für Element von Anfang bis Ende.

> [!note] Voraussetzung
> Die Daten müssen **nicht sortiert** sein. Die lineare Suche funktioniert mit beliebig angeordneten Daten.

## Algorithmus

### Pseudocode

```
FUNKTION linearesuche(liste, suchElement):
    FÜR jedes element IN liste:
        WENN element == suchElement:
            RÜCKGABE position
    RÜCKGABE "nicht gefunden"
```

### Python-Implementierung

```python
def lineare_suche(liste, such_element):
    """
    Durchsucht eine Liste sequentiell nach einem Element.
    Gibt den Index zurück oder -1 wenn nicht gefunden.
    """
    for i in range(len(liste)):
        if liste[i] == such_element:
            return i
    return -1

# Beispiel
zahlen = [5, 2, 8, 1, 9, 3]
index = lineare_suche(zahlen, 8)
print(f"Element gefunden an Index: {index}")  # Ausgabe: 2
```

## Visualisierung

```
Suche nach: 8

Liste: [ 5 | 2 | 8 | 1 | 9 | 3 ]
         ↑
         Vergleich: 5 ≠ 8 → weiter

Liste: [ 5 | 2 | 8 | 1 | 9 | 3 ]
             ↑
             Vergleich: 2 ≠ 8 → weiter

Liste: [ 5 | 2 | 8 | 1 | 9 | 3 ]
                 ↑
                 Vergleich: 8 = 8 → GEFUNDEN!
```

## Komplexität

| Fall | Komplexität | Erklärung |
|------|-------------|-----------|
| **Best Case** | O(1) | Element ist an erster Position |
| **Average Case** | O(n/2) = O(n) | Element ist in der Mitte |
| **Worst Case** | O(n) | Element ist am Ende oder nicht vorhanden |

> [!warning] Ineffizienz
> Bei großen Datenmengen ist die lineare Suche ineffizient, da im Schnitt die Hälfte aller Elemente geprüft werden muss.

## Equals-Funktion

Das Vergleichskriterium „gleich" muss manchmal speziell definiert werden:

```python
class Produkt:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def __eq__(self, other):
        """Zwei Produkte sind gleich, wenn ihre ID gleich ist."""
        if isinstance(other, Produkt):
            return self.id == other.id
        return False

# Suche nach Produkt mit ID 42
produkte = [Produkt(1, "Apfel"), Produkt(42, "Birne"), Produkt(3, "Orange")]
such_produkt = Produkt(42, "egal")  # Name ist egal für Vergleich
```

## Anwendungsfälle

> [!success] Geeignet für
> - Kleine Datenmengen
> - Unsortierte Daten
> - Einmalige Suche (Sortieren lohnt sich nicht)
> - Daten, die nicht sortierbar sind

> [!failure] Ungeeignet für
> - Große Datenmengen
> - Häufige Suchoperationen
> - Bereits sortierte Daten (→ binäre Suche nutzen)

## Prüfungsrelevanz

> [!question] Typische Prüfungsfragen
> - Implementieren Sie eine lineare Suche
> - Welche Komplexität hat die lineare Suche?
> - Wann ist lineare Suche der binären Suche vorzuziehen?

## Querverweise

- → [[02-Binaere-Suche|Binäre Suche]] – Effizientere Alternative für sortierte Daten
- → [[../01-Algorithmen/01-Grundlagen|Algorithmen-Grundlagen]] – O-Notation
- → [[../03-Sortieralgorithmen/01-Einfache-Verfahren|Sortierverfahren]] – Nutzen lineare Suche intern

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (CC-BY-4.0).
