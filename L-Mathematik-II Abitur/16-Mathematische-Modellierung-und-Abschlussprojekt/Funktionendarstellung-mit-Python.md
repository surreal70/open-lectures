---
author: Andreas Hümmer
title: Funktionendarstellung mit Python
tags:
  - content
  - mathe
  - modellierung
  - python
  - programmierung
  - visualisierung
  - abitur
created: 2025-06-28
modified: 2025-06-28
---

# Funktionendarstellung mit Python

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Einfache Python-Programme zur Funktionsdarstellung schreiben können
> - Die Bibliotheken NumPy und Matplotlib grundlegend nutzen
> - Funktionsgraphen, Ableitungen und Integrale visualisieren
> - Mathematische Berechnungen mit Python durchführen

---

## Überblick

Python ist eine der wichtigsten Programmiersprachen für mathematische Anwendungen. Mit den Bibliotheken **NumPy** (numerische Berechnungen) und **Matplotlib** (Visualisierung) können Funktionen analysiert, dargestellt und numerisch untersucht werden.

Dieses Kapitel gibt eine praxisorientierte Einführung in die computergestützte Mathematik — keine Programmiervorkenntnisse erforderlich!

## Erste Schritte

### Python-Umgebung

Für mathematisches Arbeiten empfiehlt sich:
- **Jupyter Notebook** (interaktive Umgebung)
- **Google Colab** (kostenlos im Browser)
- **Thonny** (einfache IDE für Einsteiger)

### Bibliotheken importieren

```python
import numpy as np
import matplotlib.pyplot as plt
```

- `numpy` wird als `np` abgekürzt
- `matplotlib.pyplot` wird als `plt` abgekürzt

## Grundlegende Funktionsdarstellung

### Eine Funktion plotten

```python
import numpy as np
import matplotlib.pyplot as plt

# x-Werte von -5 bis 5 (100 Punkte)
x = np.linspace(-5, 5, 100)

# Funktionswerte berechnen
y = x**2 - 2*x - 3

# Graph zeichnen
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('f(x) = x² - 2x - 3')
plt.grid(True)
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)
plt.show()
```

### Wichtige NumPy-Funktionen

| Mathematik | NumPy |
|------------|-------|
| $e^x$ | `np.exp(x)` |
| $\ln(x)$ | `np.log(x)` |
| $\sqrt{x}$ | `np.sqrt(x)` |
| $\sin(x)$ | `np.sin(x)` |
| $\cos(x)$ | `np.cos(x)` |
| $x^n$ | `x**n` |
| $|x|$ | `np.abs(x)` |

### Mehrere Funktionen vergleichen

```python
x = np.linspace(0, 5, 100)

plt.plot(x, x**2, label='x²')
plt.plot(x, 2**x, label='2^x')
plt.plot(x, np.exp(x), label='e^x')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Vergleich: Polynom vs. Exponential')
plt.legend()
plt.grid(True)
plt.ylim(0, 50)
plt.show()
```

## Funktionsanalyse

### Nullstellen finden

```python
from scipy.optimize import fsolve

def f(x):
    return x**3 - 2*x - 5

# Nullstelle nahe x=2 suchen
nullstelle = fsolve(f, 2)
print(f"Nullstelle: x = {nullstelle[0]:.6f}")
```

Ausgabe: `Nullstelle: x = 2.094551`

### Numerische Ableitung

```python
x = np.linspace(-2, 4, 100)
y = x**3 - 3*x**2 + 2

# Numerische Ableitung (Differenzenquotient)
dx = x[1] - x[0]
dy = np.diff(y) / dx

# Plot
plt.subplot(2, 1, 1)
plt.plot(x, y, label="f(x) = x³ - 3x² + 2")
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(x[:-1], dy, label="f'(x) ≈ numerisch", color='orange')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
```

### Numerische Integration

```python
from scipy.integrate import quad

def f(x):
    return np.exp(-x**2)

# Integral von 0 bis 1
integral, fehler = quad(f, 0, 1)
print(f"∫₀¹ e^(-x²) dx = {integral:.6f}")
```

Ausgabe: `∫₀¹ e^(-x²) dx = 0.746824`

## Visualisierung von Kurvendiskussionen

### Vollständige Analyse einer Funktion

```python
import numpy as np
import matplotlib.pyplot as plt

# Funktion und Ableitungen
def f(x):
    return x**3 - 6*x**2 + 9*x + 1

def f_prime(x):
    return 3*x**2 - 12*x + 9

def f_double_prime(x):
    return 6*x - 12

x = np.linspace(-1, 5, 200)

fig, axes = plt.subplots(3, 1, figsize=(8, 10))

# f(x)
axes[0].plot(x, f(x), 'b-', linewidth=2)
axes[0].axhline(y=0, color='k', linewidth=0.5)
axes[0].axvline(x=0, color='k', linewidth=0.5)
axes[0].set_ylabel('f(x)')
axes[0].set_title('Kurvendiskussion: f(x) = x³ - 6x² + 9x + 1')
axes[0].grid(True)

# f'(x)
axes[1].plot(x, f_prime(x), 'r-', linewidth=2)
axes[1].axhline(y=0, color='k', linewidth=0.5)
axes[1].set_ylabel("f'(x)")
axes[1].grid(True)

# f''(x)
axes[2].plot(x, f_double_prime(x), 'g-', linewidth=2)
axes[2].axhline(y=0, color='k', linewidth=0.5)
axes[2].set_xlabel('x')
axes[2].set_ylabel("f''(x)")
axes[2].grid(True)

plt.tight_layout()
plt.show()
```

## Wachstumsmodelle simulieren

### Logistisches Wachstum

```python
import numpy as np
import matplotlib.pyplot as plt

# Parameter
K = 1000    # Kapazitätsgrenze
r = 0.5     # Wachstumsrate
N0 = 10     # Anfangspopulation

# Analytische Lösung
def logistisch(t, N0, r, K):
    return K / (1 + ((K - N0) / N0) * np.exp(-r * t))

t = np.linspace(0, 20, 100)
N = logistisch(t, N0, r, K)

plt.figure(figsize=(10, 6))
plt.plot(t, N, 'b-', linewidth=2, label='Logistisches Wachstum')
plt.axhline(y=K, color='r', linestyle='--', label=f'Kapazität K = {K}')
plt.axhline(y=K/2, color='g', linestyle=':', label='Wendepunkt K/2')

plt.xlabel('Zeit t')
plt.ylabel('Population N')
plt.title('Logistisches Wachstumsmodell')
plt.legend()
plt.grid(True)
plt.show()
```

## Schwingungen darstellen

### Harmonische und gedämpfte Schwingung

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 500)

# Parameter
A = 5           # Amplitude
omega = 2       # Kreisfrequenz
gamma = 0.3     # Dämpfungsfaktor

# Ungedämpft
y_undamped = A * np.sin(omega * t)

# Gedämpft
y_damped = A * np.exp(-gamma * t) * np.sin(omega * t)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(t, y_undamped, 'b-')
plt.title('Ungedämpfte Schwingung')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(t, y_damped, 'r-')
plt.plot(t, A * np.exp(-gamma * t), 'k--', alpha=0.5)
plt.plot(t, -A * np.exp(-gamma * t), 'k--', alpha=0.5)
plt.title('Gedämpfte Schwingung')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid(True)

plt.tight_layout()
plt.show()
```

## 3D-Darstellungen

### Funktionen zweier Variablen

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Gitter erstellen
x = np.linspace(-3, 3, 50)
y = np.linspace(-3, 3, 50)
X, Y = np.meshgrid(x, y)

# Funktion: z = x² + y²
Z = X**2 + Y**2

# 3D-Plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('z = x² + y²')

plt.show()
```

## Symbolisches Rechnen mit SymPy

### Exakte Ableitungen und Integrale

```python
from sympy import symbols, diff, integrate, sin, cos, exp, simplify

x = symbols('x')

# Funktion definieren
f = x**3 * exp(-x)

# Ableitung
f_prime = diff(f, x)
print(f"f(x) = {f}")
print(f"f'(x) = {simplify(f_prime)}")

# Integral
F = integrate(f, x)
print(f"∫f(x)dx = {F}")
```

Ausgabe:
```
f(x) = x**3*exp(-x)
f'(x) = x**2*(3 - x)*exp(-x)
∫f(x)dx = (-x**3 - 3*x**2 - 6*x - 6)*exp(-x)
```

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Mathematische-Simulationen]] — Simulationen mit Python
- → [[Numerische-Naeherungsverfahren]] — Numerik implementieren
- → [[Wahrscheinlichkeitsmodelle-implementieren]] — Stochastik mit Python
- → [[Wachstumsmodelle]] — Modelle visualisieren
- → [[Vollstaendige-Kurvendiskussion]] — Kurvendiskussion automatisieren

> [!warning] **Prüfungsrelevant**
> - Python-Code verstehen und interpretieren können
> - Einfache Änderungen an gegebenem Code vornehmen
> - Graphische Ausgaben interpretieren
> - Zusammenhang zwischen Code und mathematischem Konzept erkennen

> [!question] **Typische Prüfungsfragen**
> - Was bewirkt die Zeile `y = np.sin(2*np.pi*x)` im Programm?
> - Ändern Sie den Code so, dass die Funktion $f(x) = e^{-x^2}$ dargestellt wird.
> - Interpretieren Sie den gezeigten Graphen und identifizieren Sie Nullstellen/Extrema.
> - Welchen Wert hat das berechnete Integral?

## Quellen

- Langtangen, H.P.: A Primer on Scientific Programming with Python. Springer, 2016
- VanderPlas, J.: Python Data Science Handbook. O'Reilly, 2016
- Matplotlib Documentation: https://matplotlib.org/

> [!tip] **Weiterführende Links**
> - [[Wahrscheinlichkeitsmodelle-implementieren]] — Stochastik programmieren
> - [[Vorbereitung-auf-Hochschulmathematik]] — Programmieren im Studium
> - [[Mathematische-Simulationen]] — Komplexere Simulationen
