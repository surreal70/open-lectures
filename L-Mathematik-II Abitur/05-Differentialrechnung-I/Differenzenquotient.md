---
author: Andreas Hümmer
title: Differenzenquotient
tags:
  - content
  - mathe
  - differentialrechnung
  - differenzenquotient
  - sekante
  - analysis
created: 2026-10-17
modified: 2026-10-17
---

# Differenzenquotient

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Differenzenquotienten als mathematischen Fachbegriff für die durchschnittliche Änderungsrate kennen
> - Verschiedene Schreibweisen des Differenzenquotienten beherrschen
> - Den Differenzenquotienten für verschiedene Funktionstypen berechnen können
> - Die Verbindung zur Sekantensteigung sicher herstellen können

---

## Überblick

Der **Differenzenquotient** ist der mathematische Fachbegriff für die durchschnittliche Änderungsrate einer Funktion. Er beschreibt das Verhältnis der Änderung der Funktionswerte (Differenz der $y$-Werte) zur Änderung der Argumente (Differenz der $x$-Werte). Der Name setzt sich zusammen aus "Differenz" (Unterschied) und "Quotient" (Bruch/Verhältnis).

Der Differenzenquotient ist der Ausgangspunkt für die Definition der Ableitung – durch Grenzübergang wird aus dem Differenzenquotienten der [[Differentialquotient|Differentialquotient]].

## Definition

> [!note] **Definition: Differenzenquotient**
> Sei $f$ eine Funktion und $x_0, x_1 \in D_f$ mit $x_0 \neq x_1$. Der **Differenzenquotient** von $f$ bezüglich $x_0$ und $x_1$ ist:
> $$\frac{\Delta f}{\Delta x} = \frac{f(x_1) - f(x_0)}{x_1 - x_0}$$

## Verschiedene Schreibweisen

### Zwei-Punkte-Form

Mit zwei beliebigen Stellen $x_1$ und $x_2$:
$$\frac{f(x_2) - f(x_1)}{x_2 - x_1}$$

### h-Schreibweise

Mit Startstelle $x_0$ und Schrittweite $h = x_1 - x_0$:
$$\frac{f(x_0 + h) - f(x_0)}{h}$$

Diese Schreibweise ist besonders wichtig für den späteren Grenzübergang $h \to 0$.

### Delta-Notation

Mit $\Delta x = x_1 - x_0$ und $\Delta y = f(x_1) - f(x_0)$:
$$\frac{\Delta y}{\Delta x} = \frac{\Delta f}{\Delta x}$$

### Leibniz-Notation (Vorform)

Als Vorstufe zur Ableitung:
$$\frac{\Delta f}{\Delta x} \quad \text{wird zu} \quad \frac{df}{dx} \quad \text{für } \Delta x \to 0$$

## Berechnungsbeispiele

### Beispiel 1: Polynomfunktion

Berechne den Differenzenquotienten von $f(x) = x^2 + 2x - 3$ für $x_0 = 1$ und $x_1 = 4$.

**Lösung:**
$$\frac{f(4) - f(1)}{4 - 1} = \frac{(16 + 8 - 3) - (1 + 2 - 3)}{3} = \frac{21 - 0}{3} = 7$$

### Beispiel 2: Mit h-Schreibweise

Berechne den Differenzenquotienten von $f(x) = x^2$ an der Stelle $x_0 = 2$ mit allgemeinem $h$.

**Lösung:**
$$\frac{f(2 + h) - f(2)}{h} = \frac{(2 + h)^2 - 4}{h}$$
$$= \frac{4 + 4h + h^2 - 4}{h} = \frac{4h + h^2}{h} = \frac{h(4 + h)}{h} = 4 + h$$

Der Differenzenquotient hängt noch von $h$ ab. Für $h \to 0$ erhalten wir die Ableitung $f'(2) = 4$.

### Beispiel 3: Exponentialfunktion

Berechne den Differenzenquotienten von $f(x) = e^x$ für $x_0 = 0$ und $x_1 = 1$.

**Lösung:**
$$\frac{f(1) - f(0)}{1 - 0} = \frac{e^1 - e^0}{1} = e - 1 \approx 1{,}718$$

### Beispiel 4: Allgemeine Form für Potenzfunktionen

Für $f(x) = x^n$ mit $n \in \mathbb{N}$ an einer beliebigen Stelle $x_0$:

$$\frac{f(x_0 + h) - f(x_0)}{h} = \frac{(x_0 + h)^n - x_0^n}{h}$$

Mit der binomischen Formel:
$$(x_0 + h)^n = x_0^n + n \cdot x_0^{n-1} \cdot h + \binom{n}{2} x_0^{n-2} \cdot h^2 + \ldots + h^n$$

Einsetzen und kürzen:
$$= \frac{n \cdot x_0^{n-1} \cdot h + \text{(Terme mit } h^2, h^3, \ldots)}{h}$$
$$= n \cdot x_0^{n-1} + \text{(Terme mit } h, h^2, \ldots)$$

Für $h \to 0$ bleibt nur $n \cdot x_0^{n-1}$ übrig – das ist die [[Potenzregel|Potenzregel]]!

## Geometrische Interpretation

Der Differenzenquotient ist die **Steigung der Sekante** durch die Punkte $P(x_0 | f(x_0))$ und $Q(x_1 | f(x_1))$.

```
       y
       |          Q(x₁|f(x₁))
       |         /|
       |        / |
       |       /  | Δy = f(x₁) - f(x₀)
       |      /   |
       |   P /    |
       |----+-----+
       |     Δx = x₁ - x₀
       |
       +------------+-------> x
              x₀    x₁
```

Die Steigung dieser Sekante berechnet sich als:
$$m_{\text{Sekante}} = \frac{\text{Gegenkathete}}{\text{Ankathete}} = \frac{\Delta y}{\Delta x}$$

## Eigenschaften des Differenzenquotienten

### Vorzeichen

- $\frac{\Delta f}{\Delta x} > 0$: Funktion steigt im Mittel im betrachteten Intervall
- $\frac{\Delta f}{\Delta x} < 0$: Funktion fällt im Mittel im betrachteten Intervall
- $\frac{\Delta f}{\Delta x} = 0$: Funktionswerte an den Intervallenden sind gleich

### Symmetrie

Im Allgemeinen gilt:
$$\frac{f(x_1) - f(x_0)}{x_1 - x_0} = \frac{f(x_0) - f(x_1)}{x_0 - x_1}$$

Die Reihenfolge der Punkte beeinflusst das Ergebnis nicht.

### Abhängigkeit vom Intervall

Der Differenzenquotient hängt von der Wahl des Intervalls ab. Verschiedene Intervalle liefern im Allgemeinen verschiedene Werte:

**Beispiel:** $f(x) = x^2$
- Intervall $[0, 2]$: $\frac{4 - 0}{2 - 0} = 2$
- Intervall $[1, 3]$: $\frac{9 - 1}{3 - 1} = 4$
- Intervall $[2, 4]$: $\frac{16 - 4}{4 - 2} = 6$

## Differenzenquotient bei speziellen Funktionen

### Lineare Funktionen

Bei $f(x) = mx + b$ ist der Differenzenquotient für jedes Intervall gleich $m$:
$$\frac{f(x_1) - f(x_0)}{x_1 - x_0} = \frac{(mx_1 + b) - (mx_0 + b)}{x_1 - x_0} = \frac{m(x_1 - x_0)}{x_1 - x_0} = m$$

### Konstante Funktionen

Bei $f(x) = c$ ist der Differenzenquotient stets 0:
$$\frac{f(x_1) - f(x_0)}{x_1 - x_0} = \frac{c - c}{x_1 - x_0} = 0$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Durchschnittliche-aenderungsrate|Durchschnittliche Änderungsrate]] – Synonymer Begriff aus der Anwendung
- → [[Differentialquotient|Differentialquotient]] – Der Grenzwert des Differenzenquotienten
- → [[Momentane-aenderungsrate|Momentane Änderungsrate]] – Was bei $h \to 0$ passiert
- → [[Definition-der-Ableitung|Definition der Ableitung]] – Formalisierung des Grenzübergangs
- → [[Lineare-Funktionen|Lineare Funktionen]] – Konstanter Differenzenquotient

> [!warning] **Prüfungsrelevant**
> - Die Formel $\frac{f(x_0 + h) - f(x_0)}{h}$ muss sicher beherrscht werden
> - Umformen des Differenzenquotienten zur Vorbereitung des Grenzübergangs ist häufige Aufgabe
> - Die geometrische Deutung als Sekantensteigung wird oft abgefragt
> - Der Zusammenhang zur Ableitung muss verstanden sein

> [!question] **Typische Prüfungsfragen**
> - "Bestimmen Sie den Differenzenquotienten von $f$ an der Stelle $x_0$ mit Schrittweite $h$."
> - "Vereinfachen Sie den Differenzenquotienten so, dass der Grenzübergang $h \to 0$ möglich wird."
> - "Welche geometrische Bedeutung hat der Differenzenquotient?"

## Quellen

- Griesel, H., Postel, H., Suhr, F. (2019): *Elemente der Mathematik – Qualifikationsphase*. Schroedel Verlag.
- Bigalke, A., Köhler, N. (2015): *Mathematik – Qualifikationsphase*. Cornelsen Verlag.
- Bronstein, I.N., Semendjajew, K.A. (2012): *Taschenbuch der Mathematik*. Verlag Europa-Lehrmittel.

> [!tip] **Weiterführende Links**
> - [[Differentialquotient|Differentialquotient]] – Der nächste Schritt: Grenzübergang
> - [[Potenzregel|Potenzregel]] – Ergebnis des Grenzübergangs für Potenzfunktionen
