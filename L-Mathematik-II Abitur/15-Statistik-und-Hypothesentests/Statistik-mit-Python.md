---
author: Andreas Hümmer
title: Statistik mit Python
tags:
  - content
  - mathe
  - statistik
  - python
  - programmierung
  - datenanalyse
created: 2025-06-26
modified: 2025-06-26
---

# Statistik mit Python

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Grundlegende statistische Berechnungen in Python durchführen können
> - Statistische Kenngrößen mit NumPy und SciPy berechnen können
> - Hypothesentests programmatisch implementieren können
> - Einfache Visualisierungen von statistischen Daten erstellen können

---

## Überblick

Python hat sich als eine der wichtigsten Sprachen für statistische Analysen etabliert. Mit Bibliotheken wie **NumPy**, **SciPy** und **Matplotlib** lassen sich statistische Berechnungen effizient durchführen und visualisieren. Dieses Kapitel gibt eine praktische Einführung in die statistischen Möglichkeiten von Python.

---

## Grundlegende Bibliotheken

### Installation und Import

```python
# Installation (in der Kommandozeile)
# pip install numpy scipy matplotlib

# Import der Bibliotheken
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
```

### NumPy für numerische Berechnungen

NumPy bietet effiziente Arrays und grundlegende statistische Funktionen:

```python
# Daten als NumPy-Array
daten = np.array([12, 15, 18, 22, 25, 28, 30, 33, 35, 40])
```

### SciPy für statistische Tests

SciPy erweitert NumPy um fortgeschrittene statistische Funktionen:

```python
from scipy import stats
from scipy.stats import binom, norm
```

---

## Statistische Kenngrößen berechnen

### Lagemaße

```python
import numpy as np

daten = np.array([23, 45, 67, 32, 56, 78, 34, 89, 45, 67])

# Arithmetisches Mittel
mittelwert = np.mean(daten)
print(f"Mittelwert: {mittelwert}")  # Ausgabe: 53.6

# Median
median = np.median(daten)
print(f"Median: {median}")  # Ausgabe: 50.5

# Modus (mit SciPy)
from scipy import stats
modus = stats.mode(daten, keepdims=True)
print(f"Modus: {modus.mode[0]}")  # Ausgabe: 45
```

### Streuungsmaße

```python
# Varianz (Stichprobenvarianz mit n-1)
varianz = np.var(daten, ddof=1)
print(f"Varianz: {varianz:.2f}")

# Standardabweichung
std_abw = np.std(daten, ddof=1)
print(f"Standardabweichung: {std_abw:.2f}")

# Spannweite
spannweite = np.max(daten) - np.min(daten)
print(f"Spannweite: {spannweite}")

# Quartile
q1 = np.percentile(daten, 25)
q2 = np.percentile(daten, 50)  # = Median
q3 = np.percentile(daten, 75)
iqr = q3 - q1
print(f"Q1: {q1}, Q3: {q3}, IQR: {iqr}")
```

### Beispiel: Vollständige deskriptive Statistik

```python
def beschreibende_statistik(daten):
    """Gibt alle wichtigen Kenngrößen aus."""
    print("=== Beschreibende Statistik ===")
    print(f"Anzahl n:           {len(daten)}")
    print(f"Minimum:            {np.min(daten)}")
    print(f"Maximum:            {np.max(daten)}")
    print(f"Spannweite:         {np.max(daten) - np.min(daten)}")
    print(f"Mittelwert:         {np.mean(daten):.2f}")
    print(f"Median:             {np.median(daten):.2f}")
    print(f"Varianz (n-1):      {np.var(daten, ddof=1):.2f}")
    print(f"Standardabweichung: {np.std(daten, ddof=1):.2f}")
    print(f"Q1 (25%):           {np.percentile(daten, 25):.2f}")
    print(f"Q3 (75%):           {np.percentile(daten, 75):.2f}")

# Anwendung
noten = np.array([2, 3, 1, 4, 2, 3, 2, 5, 3, 2, 1, 3, 4, 2, 3])
beschreibende_statistik(noten)
```

---

## Binomialverteilung

### Wahrscheinlichkeiten berechnen

```python
from scipy.stats import binom

n = 20  # Anzahl Versuche
p = 0.3  # Erfolgswahrscheinlichkeit

# P(X = k) - Einzelwahrscheinlichkeit
k = 5
p_genau = binom.pmf(k, n, p)
print(f"P(X = {k}) = {p_genau:.4f}")

# P(X <= k) - Kumulierte Wahrscheinlichkeit
p_hoechstens = binom.cdf(k, n, p)
print(f"P(X <= {k}) = {p_hoechstens:.4f}")

# P(X >= k)
p_mindestens = 1 - binom.cdf(k-1, n, p)
print(f"P(X >= {k}) = {p_mindestens:.4f}")

# P(X > k)
p_mehr_als = 1 - binom.cdf(k, n, p)
print(f"P(X > {k}) = {p_mehr_als:.4f}")
```

### Erwartungswert und Standardabweichung

```python
# Erwartungswert
E_X = binom.mean(n, p)
print(f"E(X) = {E_X}")

# Varianz
Var_X = binom.var(n, p)
print(f"Var(X) = {Var_X}")

# Standardabweichung
Std_X = binom.std(n, p)
print(f"σ(X) = {Std_X:.4f}")
```

### Visualisierung der Binomialverteilung

```python
import matplotlib.pyplot as plt

n, p = 20, 0.3
x = np.arange(0, n+1)
wahrscheinlichkeiten = binom.pmf(x, n, p)

plt.figure(figsize=(10, 6))
plt.bar(x, wahrscheinlichkeiten, color='steelblue', edgecolor='navy')
plt.xlabel('Anzahl Erfolge k')
plt.ylabel('P(X = k)')
plt.title(f'Binomialverteilung B({n}, {p})')
plt.xticks(x)
plt.grid(axis='y', alpha=0.3)
plt.show()
```

---

## Binomialtest in Python

### Ablehnungsbereich bestimmen

```python
def ablehnungsbereich_rechts(n, p0, alpha):
    """Bestimmt den Ablehnungsbereich für rechtsseitigen Test."""
    from scipy.stats import binom
    
    for k in range(n+1):
        if 1 - binom.cdf(k-1, n, p0) <= alpha:
            return list(range(k, n+1))
    return []

def ablehnungsbereich_links(n, p0, alpha):
    """Bestimmt den Ablehnungsbereich für linksseitigen Test."""
    from scipy.stats import binom
    
    for k in range(n, -1, -1):
        if binom.cdf(k, n, p0) <= alpha:
            return list(range(0, k+1))
    return []

# Beispiel: n=50, p0=0.3, alpha=0.05
n, p0, alpha = 50, 0.3, 0.05

ab_rechts = ablehnungsbereich_rechts(n, p0, alpha)
print(f"Rechtsseitiger Test: Ablehnungsbereich = {{{min(ab_rechts)}, ..., {n}}}")

ab_links = ablehnungsbereich_links(n, p0, alpha)
print(f"Linksseitiger Test: Ablehnungsbereich = {{0, ..., {max(ab_links)}}}")
```

### Vollständiger Binomialtest

```python
def binomialtest(x, n, p0, alternative='greater', alpha=0.05):
    """
    Führt einen Binomialtest durch.
    
    Parameter:
    - x: beobachtete Anzahl Erfolge
    - n: Stichprobenumfang
    - p0: Wahrscheinlichkeit unter H0
    - alternative: 'greater', 'less' oder 'two-sided'
    - alpha: Signifikanzniveau
    """
    from scipy.stats import binom
    
    print(f"=== Binomialtest ===")
    print(f"n = {n}, x = {x}, p₀ = {p0}, α = {alpha}")
    print()
    
    # Hypothesen ausgeben
    if alternative == 'greater':
        print(f"H₀: p ≤ {p0}")
        print(f"H₁: p > {p0}")
        p_wert = 1 - binom.cdf(x-1, n, p0)
    elif alternative == 'less':
        print(f"H₀: p ≥ {p0}")
        print(f"H₁: p < {p0}")
        p_wert = binom.cdf(x, n, p0)
    else:  # two-sided
        print(f"H₀: p = {p0}")
        print(f"H₁: p ≠ {p0}")
        # Zweiseitiger p-Wert
        p_wert = 2 * min(binom.cdf(x, n, p0), 1 - binom.cdf(x-1, n, p0))
        p_wert = min(p_wert, 1.0)
    
    print()
    print(f"p-Wert: {p_wert:.4f}")
    print()
    
    if p_wert <= alpha:
        print(f"Entscheidung: H₀ wird abgelehnt (p-Wert ≤ α)")
        print(f"Das Ergebnis ist statistisch signifikant auf dem {alpha*100}%-Niveau.")
    else:
        print(f"Entscheidung: H₀ wird nicht abgelehnt (p-Wert > α)")
        print(f"Das Ergebnis ist nicht statistisch signifikant.")
    
    return p_wert

# Beispiel: Qualitätskontrolle
# Von 200 Produkten sind 18 defekt. Ist die Ausschussrate > 5%?
binomialtest(x=18, n=200, p0=0.05, alternative='greater', alpha=0.05)
```

---

## Fehlerwahrscheinlichkeiten berechnen

```python
def fehler_analyse(n, p0, p1, alpha=0.05, test_art='greater'):
    """
    Berechnet α (tatsächlich) und β für einen Binomialtest.
    
    p0: Wahrscheinlichkeit unter H0
    p1: Alternative Wahrscheinlichkeit (für β-Berechnung)
    """
    from scipy.stats import binom
    
    # Ablehnungsbereich bestimmen
    if test_art == 'greater':
        for k in range(n+1):
            if 1 - binom.cdf(k-1, n, p0) <= alpha:
                kritischer_wert = k
                break
        
        # Tatsächliches alpha
        alpha_tats = 1 - binom.cdf(kritischer_wert - 1, n, p0)
        
        # Beta: P(X < kritischer_wert | p1)
        beta = binom.cdf(kritischer_wert - 1, n, p1)
        
    print(f"=== Fehleranalyse ===")
    print(f"n = {n}, p₀ = {p0}, p₁ = {p1}, α = {alpha}")
    print()
    print(f"Kritischer Wert: {kritischer_wert}")
    print(f"Ablehnungsbereich: {{{kritischer_wert}, ..., {n}}}")
    print()
    print(f"Tatsächliches α: {alpha_tats:.4f}")
    print(f"Fehler 2. Art β(p₁={p1}): {beta:.4f}")
    print(f"Macht (1-β): {1-beta:.4f}")
    
    return alpha_tats, beta

# Beispiel
fehler_analyse(n=100, p0=0.5, p1=0.6, alpha=0.05)
```

---

## Korrelation und Regression

```python
import numpy as np
from scipy import stats

# Beispieldaten: Lernzeit (x) und Punktzahl (y)
x = np.array([2, 4, 5, 6, 8, 10, 12])
y = np.array([50, 65, 70, 75, 85, 90, 95])

# Korrelationskoeffizient
r, p_wert = stats.pearsonr(x, y)
print(f"Korrelationskoeffizient r = {r:.4f}")
print(f"p-Wert: {p_wert:.4f}")
print(f"Bestimmtheitsmaß R² = {r**2:.4f}")

# Lineare Regression
steigung, achsenabschnitt, r_value, p_value, std_err = stats.linregress(x, y)
print(f"\nRegressionsgerade: ŷ = {achsenabschnitt:.2f} + {steigung:.2f}·x")

# Vorhersage
x_neu = 7
y_vorhergesagt = achsenabschnitt + steigung * x_neu
print(f"Vorhersage für x={x_neu}: ŷ = {y_vorhergesagt:.2f}")
```

### Visualisierung

```python
import matplotlib.pyplot as plt

# Streudiagramm mit Regressionsgerade
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='steelblue', s=100, label='Datenpunkte')

# Regressionsgerade einzeichnen
x_linie = np.linspace(min(x), max(x), 100)
y_linie = achsenabschnitt + steigung * x_linie
plt.plot(x_linie, y_linie, color='coral', linewidth=2, 
         label=f'Regression: ŷ = {achsenabschnitt:.1f} + {steigung:.2f}x')

plt.xlabel('Lernzeit (Stunden)')
plt.ylabel('Punktzahl')
plt.title(f'Lineare Regression (r = {r:.3f})')
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

---

## Konfidenzintervall für Anteile

```python
def konfidenzintervall_anteil(x, n, konfidenz=0.95):
    """
    Berechnet das Konfidenzintervall für einen Anteilswert.
    
    x: Anzahl Erfolge
    n: Stichprobenumfang
    konfidenz: Konfidenzniveau (z.B. 0.95 für 95%)
    """
    from scipy.stats import norm
    
    p_hat = x / n
    alpha = 1 - konfidenz
    z = norm.ppf(1 - alpha/2)
    
    # Standardfehler
    se = np.sqrt(p_hat * (1 - p_hat) / n)
    
    # Konfidenzintervall
    untergrenze = p_hat - z * se
    obergrenze = p_hat + z * se
    
    print(f"=== {konfidenz*100:.0f}%-Konfidenzintervall ===")
    print(f"Stichprobe: {x} Erfolge bei n = {n}")
    print(f"Punktschätzung p̂ = {p_hat:.4f}")
    print(f"Standardfehler SE = {se:.4f}")
    print(f"z-Wert: {z:.3f}")
    print(f"Konfidenzintervall: [{untergrenze:.4f}, {obergrenze:.4f}]")
    print(f"                    [{untergrenze*100:.2f}%, {obergrenze*100:.2f}%]")
    
    return untergrenze, obergrenze

# Beispiel: Wahlumfrage
konfidenzintervall_anteil(x=156, n=400, konfidenz=0.95)
```

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Statistische-Kenngroessen]] – Theorie zu Mittelwert, Varianz etc.
- → [[Binomialtests]] – Mathematische Grundlagen des Binomialtests
- → [[Korrelation-und-Regression-Grundlagen]] – Theorie zu Korrelation und Regression
- → [[Konfidenzintervalle-Grundlagen]] – Mathematischer Hintergrund

> [!warning] **Prüfungsrelevant**
> - Python-Syntax für grundlegende Berechnungen
> - Verwendung von `numpy` für Kenngrößen
> - Verwendung von `scipy.stats.binom` für Binomialverteilung
> - Kumulierte Wahrscheinlichkeiten: `cdf` und `1 - cdf`
> - Korrelation mit `scipy.stats.pearsonr`
> - Regression mit `scipy.stats.linregress`

> [!question] **Typische Prüfungsfragen**
> - Schreibe ein Python-Programm, das für eine Datenreihe Mittelwert, Median und Standardabweichung berechnet.
> - Berechne mit Python die Wahrscheinlichkeit $P(X \geq 12)$ für $X \sim B(20, 0{,}4)$.
> - Implementiere einen Binomialtest und bestimme den Ablehnungsbereich.

---

## Quellen

- VanderPlas, J.: Python Data Science Handbook. O'Reilly, 2016.
- McKinney, W.: Python for Data Analysis. O'Reilly, 2017.
- NumPy Documentation: https://numpy.org/doc/
- SciPy Documentation: https://docs.scipy.org/

> [!tip] **Weiterführende Links**
> - [[Binomialtests]] – Mathematische Grundlagen verstehen
> - [[Interpretation-statistischer-Ergebnisse]] – Ergebnisse richtig interpretieren
