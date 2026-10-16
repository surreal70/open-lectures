---
title: Zufallsexperimente simulieren
chapter: "15"
section: "15.8"
type: lecture
created: 2026-10-13
modified: 2026-10-13
status: draft - review pending
tags:
  - mathematik/wahrscheinlichkeit
  - simulation
  - python
---

# Zufallsexperimente simulieren

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Zufallszahlen erzeugen
> - Experimente simulieren
> - Relative Häufigkeiten mit Wahrscheinlichkeiten vergleichen

## Python: random-Modul

```python
import random

# Würfel simulieren
wurf = random.randint(1, 6)

# Münze werfen
muenze = random.choice(['Kopf', 'Zahl'])
```

## Simulation: Würfel 1000x

```python
import random

wuerfe = [random.randint(1,6) for _ in range(1000)]
sechsen = wuerfe.count(6)
print(f"Relative Häufigkeit: {sechsen/1000}")
# Erwartet: ≈ 0.167 (1/6)
```

## Gesetz der großen Zahlen

Je mehr Durchläufe, desto näher kommt die relative Häufigkeit an die theoretische Wahrscheinlichkeit.

---

**Navigation:** [[07-Python-Mathematik|← Python]] | [[09-Mathematische-Modelle|Modelle →]]
