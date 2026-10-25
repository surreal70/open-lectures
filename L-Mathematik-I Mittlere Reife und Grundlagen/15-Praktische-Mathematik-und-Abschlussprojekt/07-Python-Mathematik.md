---
title: Mathematische Berechnungen mit Python
chapter: "15"
section: "15.7"
type: lecture
created: 2026-10-13
modified: 2026-10-25
status: final
tags:
  - mathematik/anwendung
  - python
  - programmierung
---

# Mathematische Berechnungen mit Python

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Einfache mathematische Berechnungen in Python durchführen
> - Das math-Modul nutzen

Python ist eine der beliebtesten Programmiersprachen weltweit – und besonders gut für mathematische Berechnungen geeignet. Die klare, lesbare Syntax macht Python ideal für Einsteiger, während mächtige Bibliotheken auch komplexe wissenschaftliche Berechnungen ermöglichen.

### Warum Python für Mathematik?

Python bietet gegenüber Taschenrechner und Tabellenkalkulation einige Vorteile:

| Vorteil | Beschreibung |
|---------|--------------|
| **Wiederholbarkeit** | Code kann gespeichert und wiederverwendet werden |
| **Automatisierung** | Tausende Berechnungen in Sekunden |
| **Präzision** | Beliebig genaue Berechnungen möglich |
| **Erweiterbarkeit** | Bibliotheken für jedes Fachgebiet |
| **Kostenlos** | Open Source, keine Lizenzkosten |

> [!note] **Namensherkunft**
> Python wurde 1991 von Guido van Rossum entwickelt und ist nach der britischen Comedygruppe „Monty Python" benannt – nicht nach der Schlange. Van Rossum wollte einen kurzen, einprägsamen Namen.

---

## Grundrechenarten

```python
a = 5 + 3    # Addition: 8
b = 10 - 4   # Subtraktion: 6
c = 6 * 7    # Multiplikation: 42
d = 15 / 4   # Division: 3.75
e = 15 // 4  # Ganzzahldivision: 3
f = 15 % 4   # Modulo (Rest): 3
g = 2 ** 10  # Potenz: 1024
```

### Die Operatoren im Detail

| Operator | Bedeutung | Beispiel | Ergebnis |
|----------|-----------|----------|----------|
| `+` | Addition | `5 + 3` | 8 |
| `-` | Subtraktion | `10 - 4` | 6 |
| `*` | Multiplikation | `6 * 7` | 42 |
| `/` | Division (Dezimal) | `15 / 4` | 3.75 |
| `//` | Ganzzahldivision | `15 // 4` | 3 |
| `%` | Modulo (Rest) | `15 % 4` | 3 |
| `**` | Potenz | `2 ** 10` | 1024 |

> [!tip] **Ganzzahldivision und Modulo**
> Diese zwei Operatoren sind besonders nützlich:
> - `//` gibt nur den ganzzahligen Anteil: 17 // 5 = 3 (ohne Rest)
> - `%` gibt nur den Rest: 17 % 5 = 2
> 
> Zusammen ergeben sie die ursprüngliche Zahl: 17 = 3 × 5 + 2

> [!example] Praktische Anwendung: Geldwechsel
> ```python
> betrag = 47  # Euro in Münzen wechseln
> zweier = betrag // 2   # 23 Zwei-Euro-Münzen
> rest = betrag % 2      # 1 Euro Rest
> print(f"{zweier} × 2€ + {rest} × 1€ = {betrag}€")
> ```

---

## Math-Modul

```python
import math

math.sqrt(25)     # Wurzel: 5.0
math.pi           # 3.14159...
math.sin(math.pi/2)  # 1.0
```

### Wichtige Funktionen des math-Moduls

| Funktion | Beschreibung | Beispiel |
|----------|--------------|----------|
| `math.sqrt(x)` | Quadratwurzel | `math.sqrt(16)` → 4.0 |
| `math.pow(x, y)` | Potenz x^y | `math.pow(2, 3)` → 8.0 |
| `math.exp(x)` | e^x | `math.exp(1)` → 2.718... |
| `math.log(x)` | Natürlicher Logarithmus | `math.log(math.e)` → 1.0 |
| `math.log10(x)` | Zehnerlogarithmus | `math.log10(100)` → 2.0 |
| `math.sin(x)` | Sinus (x in Radiant) | `math.sin(0)` → 0.0 |
| `math.cos(x)` | Kosinus | `math.cos(0)` → 1.0 |
| `math.floor(x)` | Abrunden | `math.floor(3.7)` → 3 |
| `math.ceil(x)` | Aufrunden | `math.ceil(3.2)` → 4 |

### Konstanten

```python
import math
print(math.pi)    # 3.141592653589793
print(math.e)     # 2.718281828459045
print(math.tau)   # 6.283185307179586 (= 2π)
```

> [!warning] **Häufiger Fehler: Grad vs. Radiant**
> Trigonometrische Funktionen in Python erwarten Winkel in **Radiant**, nicht in Grad!
> 
> ```python
> import math
> # Falsch: math.sin(90) gibt nicht 1
> print(math.sin(90))  # → 0.894...
> 
> # Richtig: Umrechnung Grad → Radiant
> winkel_grad = 90
> winkel_rad = math.radians(winkel_grad)
> print(math.sin(winkel_rad))  # → 1.0
> ```

---

## Statistik

```python
daten = [2, 4, 4, 4, 5, 5, 7, 9]
mittelwert = sum(daten) / len(daten)  # 5.0
```

### Eingebaute Funktionen für Listen

| Funktion | Beschreibung | Beispiel |
|----------|--------------|----------|
| `sum(liste)` | Summe aller Elemente | `sum([1,2,3])` → 6 |
| `len(liste)` | Anzahl der Elemente | `len([1,2,3])` → 3 |
| `min(liste)` | Kleinster Wert | `min([3,1,4])` → 1 |
| `max(liste)` | Größter Wert | `max([3,1,4])` → 4 |
| `sorted(liste)` | Sortierte Liste | `sorted([3,1,4])` → [1,3,4] |

### Statistik-Modul (ab Python 3.4)

```python
import statistics

daten = [2, 4, 4, 4, 5, 5, 7, 9]
print(statistics.mean(daten))      # Mittelwert: 5
print(statistics.median(daten))    # Median: 4.5
print(statistics.mode(daten))      # Modalwert: 4
print(statistics.stdev(daten))     # Standardabweichung: 2.14...
```

> [!example] Vollständiges Beispiel: Notenauswertung
> ```python
> import statistics
> 
> noten = [2, 3, 1, 4, 2, 3, 2, 1, 3, 2]
> 
> print(f"Anzahl Noten: {len(noten)}")
> print(f"Durchschnitt: {statistics.mean(noten):.2f}")
> print(f"Median: {statistics.median(noten)}")
> print(f"Beste Note: {min(noten)}")
> print(f"Schlechteste: {max(noten)}")
> ```

---

## Formeln programmieren

Python eignet sich hervorragend, um mathematische Formeln zu implementieren:

> [!example] Quadratische Gleichung lösen
> ```python
> import math
> 
> # ax² + bx + c = 0
> def quadratische_formel(a, b, c):
>     diskriminante = b**2 - 4*a*c
>     if diskriminante < 0:
>         return "Keine reelle Lösung"
>     elif diskriminante == 0:
>         x = -b / (2*a)
>         return f"Eine Lösung: x = {x}"
>     else:
>         x1 = (-b + math.sqrt(diskriminante)) / (2*a)
>         x2 = (-b - math.sqrt(diskriminante)) / (2*a)
>         return f"Zwei Lösungen: x₁ = {x1}, x₂ = {x2}"
> 
> # Beispiel: x² - 5x + 6 = 0
> print(quadratische_formel(1, -5, 6))
> # Ausgabe: Zwei Lösungen: x₁ = 3.0, x₂ = 2.0
> ```

---

## Zusammenhänge

Python als mathematisches Werkzeug verbindet Mathematik mit Informatik:

- → [[06-Tabellenkalkulation|Tabellenkalkulation]] – Alternative für einfache Berechnungen
- → [[08-Simulation|Simulation]] – Python für Zufallsexperimente
- → [[../06-Potenzen-Wurzeln-und-Zahlendarstellung/06-Quadratwurzeln|Quadratwurzeln]] – mathematische Grundlagen
- → [[../08-Gleichungen-und-Ungleichungen/09-Loesungsformel-quadratische-Gleichungen|Quadratische Gleichungen]] – Formel im Code

---

**Navigation:** [[06-Tabellenkalkulation|← Tabellenkalkulation]] | [[08-Simulation|Simulation →]]
