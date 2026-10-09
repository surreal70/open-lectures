---
author: Prof. Dr. Schmidt
created: 2025-12-01
modified: 2026-10-09
tags:
  - pruefung
  - musterklausur
---

> [!info] **Lernziele**
> - Prüfungsformat und -umfang kennenlernen
> - Typische Aufgabenstellungen verstehen
> - Zeitmanagement für Klausur üben

## Überblick

Musterklausur zur Vorbereitung auf die schriftliche Prüfung.

**Bearbeitungszeit:** 90 Minuten  
**Erlaubte Hilfsmittel:** keine

---

## Aufgabe 1 (20 Punkte)

Erklären Sie den Quick Sort Algorithmus und führen Sie ihn auf der Liste `[7, 2, 1, 6, 8, 5, 3, 4]` durch.

## Aufgabe 2 (15 Punkte)

Bestimmen Sie die Zeitkomplexität der folgenden Funktion und begründen Sie Ihre Antwort.

```python
def find_pairs(arr):
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == 10:
                pairs.append((arr[i], arr[j]))
    return pairs
```

## Aufgabe 3 (15 Punkte)

Vergleichen Sie Merge Sort und Bubble Sort hinsichtlich:
- Zeitkomplexität (Best, Average, Worst Case)
- Speicherkomplexität
- Stabilität

## Zusammenhänge

- → [[01-Grundlagen/01-Komplexitaetsanalyse]]
- → [[03-Algorithmen/01-Sortieralgorithmen]]

> [!warning] **Prüfungsrelevant**
> - Diese Klausur entspricht dem echten Prüfungsformat

> [!question] **Typische Prüfungsfragen**
> - Siehe Aufgaben oben

## Quellen

- Musterklausur Algorithmen und Datenstrukturen, WS 2025/26

> [!tip] **Weiterführende Links**
> - [[Uebungsaufgaben/01-Komplexitaet-Uebung]]
- [[00-Organisation/01-Kursueberblick]]
