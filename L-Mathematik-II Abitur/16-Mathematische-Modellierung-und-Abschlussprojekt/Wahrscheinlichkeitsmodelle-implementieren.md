---
author: Andreas Hümmer
title: Wahrscheinlichkeitsmodelle implementieren
tags:
  - content
  - mathe
  - modellierung
  - stochastik
  - simulation
  - abitur
created: 2025-06-28
modified: 2025-06-28
---

# Wahrscheinlichkeitsmodelle implementieren

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Zufallsexperimente am Computer simulieren können
> - Das Gesetz der großen Zahlen durch Simulation veranschaulichen
> - Monte-Carlo-Methoden verstehen und anwenden
> - Wahrscheinlichkeitsverteilungen numerisch untersuchen

---

## Überblick

Die **Implementierung von Wahrscheinlichkeitsmodellen** verbindet Stochastik mit Informatik. Statt Wahrscheinlichkeiten nur theoretisch zu berechnen, können wir Zufallsexperimente millionenfach simulieren und die Ergebnisse statistisch auswerten.

Dieser Ansatz ist besonders nützlich bei:
- Komplexen Situationen ohne einfache analytische Lösung
- Überprüfung theoretischer Berechnungen
- Anschaulicher Demonstration stochastischer Gesetze

## Grundlagen der Zufallssimulation

### Pseudozufallszahlen

Computer erzeugen **Pseudozufallszahlen** — deterministisch berechnete Folgen, die statistisch wie echte Zufallszahlen aussehen.

```python
import random

# Zufallszahl zwischen 0 und 1
x = random.random()

# Zufällige Ganzzahl von a bis b (inklusive)
wuerfel = random.randint(1, 6)

# Zufälliges Element aus einer Liste
farbe = random.choice(['rot', 'schwarz', 'grün'])
```

### Reproduzierbarkeit

Mit einem **Seed** werden Ergebnisse reproduzierbar:

```python
random.seed(42)  # Immer gleiche Folge
print(random.random())  # 0.6394267984578837
```

## Simulation von Zufallsexperimenten

### Würfelwurf simulieren

```python
import random

def wuerfeln(n):
    """Simuliert n Würfelwürfe"""
    ergebnisse = [random.randint(1, 6) for _ in range(n)]
    return ergebnisse

# 10000 Würfe
wuerfe = wuerfeln(10000)

# Relative Häufigkeiten
for augenzahl in range(1, 7):
    rel_haeufigkeit = wuerfe.count(augenzahl) / len(wuerfe)
    print(f"Augenzahl {augenzahl}: {rel_haeufigkeit:.4f} (theo: 0.1667)")
```

Typische Ausgabe:
```
Augenzahl 1: 0.1658 (theo: 0.1667)
Augenzahl 2: 0.1672 (theo: 0.1667)
...
```

### Münzwurf und Gesetz der großen Zahlen

```python
import random
import matplotlib.pyplot as plt

def muenzwurf_simulation(max_n):
    """Simuliert Münzwürfe und zeigt Konvergenz"""
    kopf_anzahl = 0
    rel_haeufigkeiten = []
    
    for i in range(1, max_n + 1):
        if random.random() < 0.5:
            kopf_anzahl += 1
        rel_haeufigkeiten.append(kopf_anzahl / i)
    
    return rel_haeufigkeiten

# Simulation
n = 10000
rel_haeuf = muenzwurf_simulation(n)

# Visualisierung
plt.figure(figsize=(10, 6))
plt.plot(rel_haeuf)
plt.axhline(y=0.5, color='r', linestyle='--', label='Erwartungswert 0.5')
plt.xlabel('Anzahl Würfe')
plt.ylabel('Relative Häufigkeit (Kopf)')
plt.title('Gesetz der großen Zahlen')
plt.legend()
plt.show()
```

## Binomialverteilung simulieren

### Simulation eines Bernoulli-Experiments

```python
import random
import numpy as np
import matplotlib.pyplot as plt

def binomial_simulation(n, p, anzahl_versuche):
    """Simuliert die Binomialverteilung"""
    ergebnisse = []
    
    for _ in range(anzahl_versuche):
        erfolge = sum(1 for _ in range(n) if random.random() < p)
        ergebnisse.append(erfolge)
    
    return ergebnisse

# Parameter
n = 20      # Anzahl Versuche pro Experiment
p = 0.3     # Erfolgswahrscheinlichkeit
N = 10000   # Anzahl Simulationen

# Simulation
ergebnisse = binomial_simulation(n, p, N)

# Histogramm
plt.figure(figsize=(10, 6))
plt.hist(ergebnisse, bins=range(n+2), density=True, alpha=0.7, 
         edgecolor='black', label='Simulation')

# Theoretische Verteilung zum Vergleich
from scipy.stats import binom
k = np.arange(0, n+1)
plt.plot(k, binom.pmf(k, n, p), 'ro-', label='Theorie')

plt.xlabel('Anzahl Erfolge k')
plt.ylabel('Relative Häufigkeit / Wahrscheinlichkeit')
plt.title(f'Binomialverteilung B({n}, {p})')
plt.legend()
plt.show()
```

## Normalverteilung und Grenzwertsatz

### Zentraler Grenzwertsatz veranschaulichen

```python
import numpy as np
import matplotlib.pyplot as plt

def zeige_grenzwertsatz(n_wuerfel, n_simulationen):
    """Demonstriert den zentralen Grenzwertsatz"""
    summen = []
    
    for _ in range(n_simulationen):
        # Summe von n Würfelwürfen
        summe = sum(np.random.randint(1, 7) for _ in range(n_wuerfel))
        summen.append(summe)
    
    return summen

# Verschiedene Anzahlen von Würfeln
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

for ax, n in zip(axes.flat, [1, 2, 5, 30]):
    summen = zeige_grenzwertsatz(n, 10000)
    ax.hist(summen, bins=30, density=True, alpha=0.7)
    ax.set_title(f'Summe von {n} Würfel(n)')
    ax.set_xlabel('Summe')
    ax.set_ylabel('Relative Häufigkeit')

plt.tight_layout()
plt.show()
```

Die Verteilung nähert sich mit steigender Würfelzahl einer Normalverteilung.

## Monte-Carlo-Integration

### Prinzip

Die Fläche unter einer Kurve kann durch zufälliges Werfen von Punkten geschätzt werden:

$$\int_a^b f(x)\,dx \approx (b-a) \cdot h \cdot \frac{\text{Treffer unter der Kurve}}{\text{Gesamtanzahl Punkte}}$$

### Beispiel: $\int_0^1 x^2\,dx$

```python
import random

def monte_carlo_integral(f, a, b, h, n):
    """Monte-Carlo-Integration"""
    treffer = 0
    
    for _ in range(n):
        x = random.uniform(a, b)
        y = random.uniform(0, h)
        if y <= f(x):
            treffer += 1
    
    flaeche = (b - a) * h * (treffer / n)
    return flaeche

# f(x) = x^2 von 0 bis 1
def f(x):
    return x**2

integral = monte_carlo_integral(f, 0, 1, 1, 100000)
print(f"Monte-Carlo: {integral:.6f}")
print(f"Exakt: {1/3:.6f}")
```

Typische Ausgabe:
```
Monte-Carlo: 0.333521
Exakt: 0.333333
```

### Beispiel: $\pi$ berechnen

```python
import random

def pi_monte_carlo(n):
    """Schätzt pi durch Punktewurf in Quadrat/Kreis"""
    treffer = 0
    
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            treffer += 1
    
    return 4 * treffer / n

# Verschiedene Stichprobengrößen
for n in [100, 1000, 10000, 100000, 1000000]:
    pi_approx = pi_monte_carlo(n)
    fehler = abs(pi_approx - 3.14159265359)
    print(f"n = {n:>7}: π ≈ {pi_approx:.6f}, Fehler: {fehler:.6f}")
```

Typische Ausgabe:
```
n =     100: π ≈ 3.120000, Fehler: 0.021593
n =    1000: π ≈ 3.168000, Fehler: 0.026407
n =   10000: π ≈ 3.142800, Fehler: 0.001207
n =  100000: π ≈ 3.139320, Fehler: 0.002273
n = 1000000: π ≈ 3.141288, Fehler: 0.000305
```

## Markov-Ketten simulieren

### Einfaches Wettermodell

Angenommen, das Wetter folgt einer Markov-Kette:
- Von "sonnig" zu "sonnig": 80%, zu "regnerisch": 20%
- Von "regnerisch" zu "sonnig": 40%, zu "regnerisch": 60%

```python
import random

def wetter_simulation(tage, start='sonnig'):
    """Simuliert Wetterfolge mit Markov-Kette"""
    zustand = start
    verlauf = [zustand]
    
    for _ in range(tage - 1):
        if zustand == 'sonnig':
            zustand = 'sonnig' if random.random() < 0.8 else 'regnerisch'
        else:
            zustand = 'sonnig' if random.random() < 0.4 else 'regnerisch'
        verlauf.append(zustand)
    
    return verlauf

# 365 Tage simulieren
wetter = wetter_simulation(365)
sonnige_tage = wetter.count('sonnig')
print(f"Sonnige Tage: {sonnige_tage} ({100*sonnige_tage/365:.1f}%)")
```

Die langfristige Verteilung (stationäre Verteilung) kann berechnet werden:
$$P(\text{sonnig}) = \frac{0{,}4}{0{,}2 + 0{,}4} = \frac{2}{3} \approx 66{,}7\%$$

## Konfidenzintervalle durch Simulation

### Bootstrap-Methode

```python
import numpy as np

def bootstrap_konfidenzintervall(daten, anzahl_bootstrap=10000, 
                                  konfidenz=0.95):
    """Schätzt Konfidenzintervall für den Mittelwert"""
    n = len(daten)
    mittelwerte = []
    
    for _ in range(anzahl_bootstrap):
        # Ziehe n Werte mit Zurücklegen
        stichprobe = np.random.choice(daten, size=n, replace=True)
        mittelwerte.append(np.mean(stichprobe))
    
    alpha = (1 - konfidenz) / 2
    untere = np.percentile(mittelwerte, 100 * alpha)
    obere = np.percentile(mittelwerte, 100 * (1 - alpha))
    
    return untere, obere

# Beispiel: Reaktionszeiten (ms)
daten = [234, 256, 278, 245, 267, 289, 312, 223, 251, 276]
untere, obere = bootstrap_konfidenzintervall(daten)
print(f"95%-Konfidenzintervall: [{untere:.1f}, {obere:.1f}] ms")
```

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Binomialverteilung]] — Theoretische Grundlagen
- → [[Normalverteilung]] — Grenzwertsatz
- → [[Konfidenzintervalle]] — Statistische Schätzung
- → [[Funktionendarstellung-mit-Python]] — Python-Grundlagen
- → [[Mathematische-Simulationen]] — Allgemeine Simulationstechniken

> [!warning] **Prüfungsrelevant**
> - Zufallsexperimente in Simulation umsetzen
> - Gesetz der großen Zahlen erklären und veranschaulichen
> - Monte-Carlo-Prinzip verstehen
> - Zusammenhang zwischen relativer Häufigkeit und Wahrscheinlichkeit

> [!question] **Typische Prüfungsfragen**
> - Beschreiben Sie, wie man die Wahrscheinlichkeit eines Ereignisses durch Simulation schätzt.
> - Wie verändert sich die Genauigkeit der Schätzung bei Vervierfachung der Simulationszahl?
> - Erklären Sie anhand des gezeigten Codes das Gesetz der großen Zahlen.
> - Warum konvergiert die Monte-Carlo-Schätzung gegen den wahren Wert?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3. Springer Vieweg, 2016
- Ross, S.M.: Simulation. Academic Press, 2012
- ISB Bayern: Lehrplan Mathematik, Gymnasium

> [!tip] **Weiterführende Links**
> - [[Funktionendarstellung-mit-Python]] — Python für Mathematik
> - [[Mathematische-Simulationen]] — Weitere Simulationstechniken
> - [[Vorbereitung-auf-Hochschulmathematik]] — Stochastik an der Hochschule
