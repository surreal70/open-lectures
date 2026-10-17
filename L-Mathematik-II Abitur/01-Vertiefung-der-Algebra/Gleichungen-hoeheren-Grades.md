---
author: Andreas Hümmer
title: Gleichungen höheren Grades
tags:
  - content
  - mathe
  - algebra
  - polynomgleichungen
  - substitution
  - numerische-verfahren
created: 2025-01-13
modified: 2025-01-13
---

# Gleichungen höheren Grades

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Polynomgleichungen systematisch lösen können
> - Biquadratische Gleichungen durch Substitution lösen können
> - Die Bedeutung des rationalen Nullstellensatzes kennen
> - Numerische Näherungsverfahren verstehen

---

## Überblick

Während lineare und quadratische Gleichungen mit Standardverfahren gelöst werden können, erfordern Gleichungen höheren Grades spezielle Techniken. In der Oberstufe begegnen uns vor allem Polynomgleichungen dritten und vierten Grades, die durch geschicktes Faktorisieren oder Substitution gelöst werden. Für allgemeine Polynome höheren Grades existieren keine geschlossenen Lösungsformeln, sodass numerische Verfahren wichtig werden.

## Klassifikation nach Grad

### Lineare Gleichungen (Grad 1)

$$ax + b = 0 \quad \Rightarrow \quad x = -\frac{b}{a}$$

### Quadratische Gleichungen (Grad 2)

$$ax^2 + bx + c = 0 \quad \Rightarrow \quad x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

Die **Diskriminante** $D = b^2 - 4ac$ bestimmt die Anzahl der Lösungen:
- $D > 0$: zwei verschiedene reelle Lösungen
- $D = 0$: eine doppelte reelle Lösung
- $D < 0$: keine reellen Lösungen (zwei komplexe)

### Kubische Gleichungen (Grad 3)

$$ax^3 + bx^2 + cx + d = 0$$

Ein Polynom dritten Grades hat **immer mindestens eine reelle Nullstelle** (da der Graph die x-Achse kreuzen muss).

### Gleichungen höheren Grades (Grad ≥ 4)

Für Grad 4 existiert noch eine allgemeine Lösungsformel (sehr komplex), ab Grad 5 gibt es **keine allgemeine algebraische Lösung** (Satz von Abel-Ruffini).

## Lösungsstrategien

### Strategie 1: Ausklammern

Wenn $x$ ein gemeinsamer Faktor ist:

$$x^3 - 4x = 0 \quad \Rightarrow \quad x(x^2 - 4) = 0 \quad \Rightarrow \quad x(x-2)(x+2) = 0$$

Lösungen: $x_1 = 0$, $x_2 = 2$, $x_3 = -2$

### Strategie 2: Raten und Abspalten

Der **rationale Nullstellensatz** hilft beim Finden von Kandidaten:

> Ist $p(x) = a_n x^n + \ldots + a_1 x + a_0$ ein Polynom mit ganzzahligen Koeffizienten, so hat jede rationale Nullstelle $\frac{p}{q}$ die Eigenschaft:
> - $p$ teilt $a_0$ (konstantes Glied)
> - $q$ teilt $a_n$ (Leitkoeffizient)

**Beispiel:** $p(x) = 2x^3 - 3x^2 - 11x + 6$

Kandidaten: $\pm\frac{\text{Teiler von 6}}{\text{Teiler von 2}} = \pm 1, \pm 2, \pm 3, \pm 6, \pm\frac{1}{2}, \pm\frac{3}{2}$

Test: $p(3) = 54 - 27 - 33 + 6 = 0$ ✓

Nach Polynomdivision: $p(x) = (x - 3)(2x^2 + 3x - 2) = (x - 3)(2x - 1)(x + 2)$

### Strategie 3: Substitution bei biquadratischen Gleichungen

Eine **biquadratische Gleichung** hat die Form:

$$ax^4 + bx^2 + c = 0$$

**Substitution:** $u = x^2$ (mit $u \geq 0$)

$$au^2 + bu + c = 0$$

**Beispiel:** $x^4 - 5x^2 + 4 = 0$

Mit $u = x^2$: $u^2 - 5u + 4 = 0$

$(u - 1)(u - 4) = 0 \Rightarrow u_1 = 1, u_2 = 4$

Rücksubstitution:
- $x^2 = 1 \Rightarrow x = \pm 1$
- $x^2 = 4 \Rightarrow x = \pm 2$

Lösungsmenge: $\mathbb{L} = \{-2, -1, 1, 2\}$

### Strategie 4: Spezielle Strukturen erkennen

**Beispiel:** $x^3 - 8 = 0$

$$x^3 = 8 \quad \Rightarrow \quad x = \sqrt[3]{8} = 2$$

Oder mit der Formel $a^3 - b^3 = (a-b)(a^2 + ab + b^2)$:

$$x^3 - 8 = (x - 2)(x^2 + 2x + 4) = 0$$

Die quadratische Gleichung $x^2 + 2x + 4 = 0$ hat keine reellen Lösungen ($D = 4 - 16 < 0$).

## Numerische Verfahren

### Newton-Verfahren (Übersicht)

Für die numerische Nullstellensuche bei komplizierten Gleichungen:

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

Dieses iterative Verfahren konvergiert schnell, wenn der Startwert gut gewählt ist.

### Intervallhalbierung

Einfaches, aber zuverlässiges Verfahren:

1. Finde ein Intervall $[a, b]$ mit $f(a) \cdot f(b) < 0$ (Vorzeichenwechsel)
2. Berechne den Mittelpunkt $m = \frac{a+b}{2}$
3. Wähle das Teilintervall mit Vorzeichenwechsel
4. Wiederhole bis zur gewünschten Genauigkeit

> [!tip] **Taschenrechner**
> Im Abitur werden numerische Näherungen oft mit dem grafikfähigen Taschenrechner bestimmt (SOLVE-Funktion oder graphisch).

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Polynomdivision]] – Abspalten von Linearfaktoren
- → [[Faktorisierung-von-Polynomen]] – Systematische Faktorisierung
- → [[Polynomfunktionen]] – Graphische Interpretation
- → [[Einfuehrung-in-komplexe-Zahlen]] – Komplexe Lösungen

> [!warning] **Prüfungsrelevant**
> - Lösen durch Ausklammern und Faktorisieren
> - Substitutionsmethode bei biquadratischen Gleichungen
> - Anwendung des rationalen Nullstellensatzes
> - Interpretation der Lösungsanzahl

> [!question] **Typische Prüfungsfragen**
> - Löse die Gleichung $x^4 - 10x^2 + 9 = 0$ vollständig.
> - Bestimme alle reellen Lösungen von $x^3 + x^2 - 4x - 4 = 0$.
> - Zeige, dass die Gleichung $x^5 - x - 1 = 0$ genau eine reelle Lösung hat.

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Verlag Europa-Lehrmittel
- ISB Bayern: *Lehrplan Mathematik Gymnasium*

> [!tip] **Weiterführende Links**
> - [[Glossar#Biquadratische Gleichung|Glossar: Biquadratische Gleichung]]
> - [[Glossar#Diskriminante|Glossar: Diskriminante]]
