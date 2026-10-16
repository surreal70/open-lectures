---
title: Mathematische Berechnungen mit Python
chapter: "15"
section: "15.7"
type: lecture
created: 2026-10-13
modified: 2026-10-13
status: draft - review pending
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

## Math-Modul

```python
import math

math.sqrt(25)     # Wurzel: 5.0
math.pi           # 3.14159...
math.sin(math.pi/2)  # 1.0
```

## Statistik

```python
daten = [2, 4, 4, 4, 5, 5, 7, 9]
mittelwert = sum(daten) / len(daten)  # 5.0
```

---

**Navigation:** [[06-Tabellenkalkulation|← Tabellenkalkulation]] | [[08-Simulation|Simulation →]]
