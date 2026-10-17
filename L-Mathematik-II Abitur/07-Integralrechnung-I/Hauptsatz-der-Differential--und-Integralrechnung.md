---
author: Andreas Hümmer
title: Hauptsatz der Differential- und Integralrechnung
tags:
  - content
  - mathe
  - integralrechnung
  - hauptsatz
  - analysis
created: 2026-10-17
modified: 2026-10-17
---

# Hauptsatz der Differential- und Integralrechnung

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Hauptsatz der Differential- und Integralrechnung formulieren können
> - Verstehen, warum Integration und Differentiation inverse Operationen sind
> - Die Integralfunktion und ihre Eigenschaften kennen
> - Den Hauptsatz zur Berechnung bestimmter Integrale anwenden können

---

## Überblick

Der Hauptsatz der Differential- und Integralrechnung ist eines der zentralen Ergebnisse der Analysis. Er stellt die fundamentale Verbindung zwischen der Differentialrechnung (lokale Änderungsraten) und der Integralrechnung (Flächenberechnung) her. Dieser Satz ermöglicht es, bestimmte Integrale mithilfe von Stammfunktionen zu berechnen, was die praktische Anwendung der Integralrechnung enorm vereinfacht.

## Die Integralfunktion

### Definition

Sei $f$ eine stetige Funktion auf dem Intervall $[a, b]$. Dann definiert man die **Integralfunktion** $I_a$ durch:

$$I_a(x) = \int_a^x f(t) \, dt$$

Die Integralfunktion ordnet jedem $x \in [a, b]$ die orientierte Fläche zwischen dem Graphen von $f$ und der $t$-Achse im Intervall $[a, x]$ zu.

### Eigenschaften der Integralfunktion

1. $I_a(a) = \int_a^a f(t) \, dt = 0$
2. $I_a(x)$ ist auf $[a, b]$ stetig
3. $I_a(x)$ ist auf $(a, b)$ differenzierbar

### Beispiel

Für $f(t) = t$ und $a = 0$ ist die Integralfunktion:

$$I_0(x) = \int_0^x t \, dt = \left[\frac{t^2}{2}\right]_0^x = \frac{x^2}{2}$$

## Der erste Teil des Hauptsatzes

### Formulierung

> **Erster Teil des Hauptsatzes**
> 
> Sei $f$ stetig auf $[a, b]$. Dann ist die Integralfunktion
> $$I_a(x) = \int_a^x f(t) \, dt$$
> auf $(a, b)$ differenzierbar, und es gilt:
> $$\frac{d}{dx} \int_a^x f(t) \, dt = f(x)$$

### Bedeutung

Die Ableitung der Integralfunktion ist die ursprüngliche Funktion. Anders gesagt: Die Integralfunktion ist eine **Stammfunktion** von $f$.

### Beweisskizze

Für kleine $h > 0$ gilt nach Definition der Ableitung:

$$\frac{I_a(x+h) - I_a(x)}{h} = \frac{1}{h} \int_x^{x+h} f(t) \, dt$$

Nach dem Mittelwertsatz der Integralrechnung existiert ein $\xi \in [x, x+h]$ mit:

$$\frac{1}{h} \int_x^{x+h} f(t) \, dt = f(\xi)$$

Für $h \to 0$ gilt $\xi \to x$, und wegen der Stetigkeit von $f$ folgt:

$$\lim_{h \to 0} \frac{I_a(x+h) - I_a(x)}{h} = \lim_{\xi \to x} f(\xi) = f(x)$$

## Der zweite Teil des Hauptsatzes

### Formulierung

> **Zweiter Teil des Hauptsatzes**
> 
> Sei $f$ stetig auf $[a, b]$ und $F$ eine beliebige Stammfunktion von $f$. Dann gilt:
> $$\int_a^b f(x) \, dx = F(b) - F(a)$$

### Bedeutung

Dieser Teil liefert die praktische Methode zur Berechnung bestimmter Integrale: Man sucht eine Stammfunktion und wertet sie an den Grenzen aus.

### Schreibweise

$$\int_a^b f(x) \, dx = \Big[ F(x) \Big]_a^b = F(b) - F(a)$$

### Beweis

Sei $F$ eine Stammfunktion von $f$. Die Integralfunktion $I_a(x)$ ist ebenfalls eine Stammfunktion von $f$ (nach dem ersten Teil). Da zwei Stammfunktionen sich nur um eine Konstante unterscheiden, gilt:

$$I_a(x) = F(x) + C$$

Für $x = a$: $I_a(a) = 0 = F(a) + C$, also $C = -F(a)$.

Für $x = b$: $I_a(b) = F(b) + C = F(b) - F(a)$.

Da $I_a(b) = \int_a^b f(t) \, dt$, folgt die Behauptung.

## Anwendungsbeispiele

### Beispiel 1: Polynomfunktion

Berechne $\int_1^4 (2x - 3) \, dx$.

**Stammfunktion**: $F(x) = x^2 - 3x$

**Auswertung**:
$$\int_1^4 (2x - 3) \, dx = \Big[ x^2 - 3x \Big]_1^4 = (16 - 12) - (1 - 3) = 4 - (-2) = 6$$

### Beispiel 2: Exponentialfunktion

Berechne $\int_0^1 e^{2x} \, dx$.

**Stammfunktion**: $F(x) = \frac{1}{2}e^{2x}$

**Auswertung**:
$$\int_0^1 e^{2x} \, dx = \Big[ \frac{1}{2}e^{2x} \Big]_0^1 = \frac{1}{2}e^2 - \frac{1}{2}e^0 = \frac{1}{2}(e^2 - 1)$$

### Beispiel 3: Ableitung einer Integralfunktion

Bestimme $\frac{d}{dx} \int_2^x \cos(t^2) \, dt$.

Nach dem ersten Teil des Hauptsatzes:
$$\frac{d}{dx} \int_2^x \cos(t^2) \, dt = \cos(x^2)$$

## Erweiterungen

### Variable untere Grenze

$$\frac{d}{dx} \int_x^b f(t) \, dt = -f(x)$$

Das negative Vorzeichen entsteht, weil:
$$\int_x^b f(t) \, dt = -\int_b^x f(t) \, dt$$

### Variable in beiden Grenzen

$$\frac{d}{dx} \int_{g(x)}^{h(x)} f(t) \, dt = f(h(x)) \cdot h'(x) - f(g(x)) \cdot g'(x)$$

Dies folgt aus dem Hauptsatz zusammen mit der Kettenregel.

## Die fundamentale Verbindung

### Zusammenfassung

Der Hauptsatz zeigt:

| Operation | Umkehroperation |
|-----------|-----------------|
| Differentiation | Integration |
| Integration | Differentiation |

Genauer:
- Differenziert man eine Stammfunktion, erhält man die ursprüngliche Funktion.
- Integriert man eine Funktion und differenziert das Ergebnis, erhält man die ursprüngliche Funktion zurück.

### Symbolisch

$$\frac{d}{dx} \int f(x) \, dx = f(x)$$

$$\int f'(x) \, dx = f(x) + C$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Definition-der-Ableitung]] – Die Ableitung als Grundlage
- → [[Stammfunktionen]] – Stammfunktionen als Werkzeug für den Hauptsatz
- → [[Bestimmte-Integrale]] – Anwendung des Hauptsatzes
- → [[Konvergenz]] – Grenzwertbegriff im Beweis
- → [[Monotonieverhalten]] – Anwendung: Stammfunktion monoton, wenn Integrand vorzeichenfest

> [!warning] **Prüfungsrelevant**
> - Die Formel $\int_a^b f(x) \, dx = F(b) - F(a)$ ist zentral!
> - Die Integralfunktion $I_a(x) = \int_a^x f(t) \, dt$ ist eine Stammfunktion von $f$
> - $\frac{d}{dx} \int_a^x f(t) \, dt = f(x)$ sicher beherrschen
> - Die Auswertungsklammer $\Big[ F(x) \Big]_a^b$ korrekt verwenden

> [!question] **Typische Prüfungsfragen**
> - Formuliere den Hauptsatz der Differential- und Integralrechnung.
> - Berechne $\frac{d}{dx} \int_1^x \sqrt{t^3 + 1} \, dt$ ohne das Integral auszuwerten.
> - Erkläre, warum Differentiation und Integration „inverse" Operationen sind.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Forster, O.: Analysis 1. Springer Spektrum, 2016.
- Königsberger, K.: Analysis 1. Springer, 2004.

> [!tip] **Weiterführende Links**
> - [[Bestimmte-Integrale]] – Anwendung des Hauptsatzes
> - [[Grundlegende-Integrationsregeln]] – Praktische Integrationstechniken
