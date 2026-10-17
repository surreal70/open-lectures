---
author: Andreas Hümmer
title: Flächen zwischen Funktionsgraphen
tags:
  - content
  - mathe
  - integralrechnung
  - flaechenberechnung
  - analysis
created: 2025-06-26
modified: 2025-06-26
---

# Flächen zwischen Funktionsgraphen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Flächen zwischen zwei Funktionsgraphen mit Integralen berechnen können
> - Die Schnittpunkte als Integrationsgrenzen bestimmen können
> - Fälle mit mehrfachen Schnittpunkten korrekt behandeln können
> - Die geometrische Bedeutung von Differenzfunktionen verstehen

---

## Überblick

Die Berechnung von **Flächen zwischen Funktionsgraphen** ist eine zentrale Anwendung der Integralrechnung. Während bei der einfachen Flächenberechnung die Fläche zwischen einem Funktionsgraphen und der $x$-Achse bestimmt wird, geht es hier um die Fläche, die von zwei Kurven eingeschlossen wird.

Diese Technik findet Anwendung in:
- Physik (Arbeit bei veränderlicher Kraft)
- Wirtschaft (Konsumenten- und Produzentenrente)
- Technik (Querschnittsflächen)
- Statistik (Differenz zwischen Verteilungen)

---

## Grundprinzip

### Die Differenzfunktion

Sind $f(x)$ und $g(x)$ zwei Funktionen mit $f(x) \geq g(x)$ im Intervall $[a, b]$, so gilt:

$$A = \int_a^b (f(x) - g(x)) \, dx$$

Die Fläche ergibt sich als Integral der **Differenzfunktion** $d(x) = f(x) - g(x)$.

### Geometrische Interpretation

```
    y ↑
      │      ╭────╮  f(x)
      │    ╱  Fläche  ╲
      │  ╭───────────────╮  g(x)
      │╱                    ╲
    ──┼───────────────────────→ x
      a                      b
```

Die Fläche zwischen den Graphen ist die Differenz der Flächen unter den einzelnen Graphen:
$$A = \int_a^b f(x) \, dx - \int_a^b g(x) \, dx = \int_a^b (f(x) - g(x)) \, dx$$

---

## Systematisches Vorgehen

### Schritt-für-Schritt-Anleitung

1. **Schnittpunkte bestimmen**: Löse $f(x) = g(x)$, um die Integrationsgrenzen zu finden
2. **Lagebeziehung prüfen**: Bestimme, welche Funktion im Intervall "oben" liegt
3. **Differenzfunktion bilden**: $d(x) = f_{\text{oben}}(x) - f_{\text{unten}}(x)$
4. **Integral berechnen**: $A = \int_a^b d(x) \, dx$
5. **Bei Vorzeichenwechsel**: Teile das Integral auf

---

## Beispiele

### Beispiel 1: Parabel und Gerade

Berechne die Fläche zwischen $f(x) = -x^2 + 4$ und $g(x) = x$.

**Schritt 1: Schnittpunkte**

$$-x^2 + 4 = x$$
$$-x^2 - x + 4 = 0 \quad | \cdot (-1)$$
$$x^2 + x - 4 = 0$$

Mit der Mitternachtsformel:
$$x_{1,2} = \frac{-1 \pm \sqrt{1 + 16}}{2} = \frac{-1 \pm \sqrt{17}}{2}$$

$$x_1 \approx -2{,}56, \quad x_2 \approx 1{,}56$$

**Schritt 2: Lagebeziehung**

Prüfe z.B. bei $x = 0$:
- $f(0) = 4$
- $g(0) = 0$

Also ist $f(x) \geq g(x)$ im Intervall.

**Schritt 3: Integral aufstellen und berechnen**

$$A = \int_{x_1}^{x_2} ((-x^2 + 4) - x) \, dx = \int_{x_1}^{x_2} (-x^2 - x + 4) \, dx$$

$$= \left[-\frac{x^3}{3} - \frac{x^2}{2} + 4x\right]_{x_1}^{x_2}$$

Nach Einsetzen und Berechnung: $A \approx 9{,}01$ FE

### Beispiel 2: Zwei Parabeln

Berechne die Fläche zwischen $f(x) = x^2$ und $g(x) = 2x - x^2$.

**Schnittpunkte:**
$$x^2 = 2x - x^2$$
$$2x^2 - 2x = 0$$
$$2x(x - 1) = 0$$
$$x_1 = 0, \quad x_2 = 1$$

**Lagebeziehung** bei $x = 0{,}5$:
- $f(0{,}5) = 0{,}25$
- $g(0{,}5) = 1 - 0{,}25 = 0{,}75$

Also ist $g(x) \geq f(x)$ im Intervall $[0, 1]$.

**Berechnung:**
$$A = \int_0^1 ((2x - x^2) - x^2) \, dx = \int_0^1 (2x - 2x^2) \, dx$$

$$= \left[x^2 - \frac{2x^3}{3}\right]_0^1 = 1 - \frac{2}{3} = \frac{1}{3}$$

---

## Mehrere Schnittpunkte

Wenn sich die Funktionen **mehrfach schneiden**, wechselt die Lagebeziehung. In diesem Fall muss das Integral **aufgeteilt** werden.

### Allgemeine Formel bei Vorzeichenwechsel

Haben $f$ und $g$ Schnittpunkte bei $a = s_0 < s_1 < s_2 < \ldots < s_n = b$, so gilt:

$$A = \sum_{i=0}^{n-1} \left| \int_{s_i}^{s_{i+1}} (f(x) - g(x)) \, dx \right|$$

> [!warning] **Wichtig**
> Die Betragsstriche sind notwendig, da sonst negative Flächenanteile entstehen können!

### Beispiel: Sinus und Kosinus

Berechne die Fläche zwischen $f(x) = \sin x$ und $g(x) = \cos x$ im Intervall $[0, 2\pi]$.

**Schnittpunkte:**
$$\sin x = \cos x \Rightarrow \tan x = 1 \Rightarrow x = \frac{\pi}{4}, \frac{5\pi}{4}$$

**Teilintervalle und Lagebeziehung:**

| Intervall | Testpunkt | oben | unten |
|-----------|-----------|------|-------|
| $[0, \frac{\pi}{4}]$ | $x = 0$ | $\cos x$ | $\sin x$ |
| $[\frac{\pi}{4}, \frac{5\pi}{4}]$ | $x = \pi$ | $\sin x$ | $\cos x$ |
| $[\frac{5\pi}{4}, 2\pi]$ | $x = \frac{3\pi}{2}$ | $\cos x$ | $\sin x$ |

**Berechnung:**

$$A = \int_0^{\pi/4} (\cos x - \sin x) \, dx + \int_{\pi/4}^{5\pi/4} (\sin x - \cos x) \, dx + \int_{5\pi/4}^{2\pi} (\cos x - \sin x) \, dx$$

Jedes Teilintegral ergibt $\sqrt{2}$, also:
$$A = 3 \cdot \sqrt{2} \cdot 2 = 4\sqrt{2} \approx 5{,}66 \text{ FE}$$

---

## Praktische Methode mit Betragsfunktion

Alternativ kann man die Fläche auch direkt berechnen:

$$A = \int_a^b |f(x) - g(x)| \, dx$$

Diese Formel liefert **immer** die korrekte (positive) Fläche, erfordert aber die Kenntnis der Nullstellen von $f(x) - g(x)$.

---

## Anwendungsbeispiel: Konsumenten- und Produzentenrente

In der Wirtschaftsmathematik beschreiben:
- **Nachfragefunktion** $p_N(q)$: Preis, den Käufer zu zahlen bereit sind
- **Angebotsfunktion** $p_A(q)$: Preis, zu dem Verkäufer anbieten

Der **Marktgleichgewichtspunkt** $(q^*, p^*)$ ergibt sich aus $p_N(q^*) = p_A(q^*)$.

$$\text{Konsumentenrente} = \int_0^{q^*} (p_N(q) - p^*) \, dq$$

$$\text{Produzentenrente} = \int_0^{q^*} (p^* - p_A(q)) \, dq$$

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Flaechenberechnung|Flächenberechnung]] – Grundlagen der Flächenberechnung mit Integralen
- → [[Bestimmte-Integrale|Bestimmte Integrale]] – Mathematische Grundlage
- → [[Nullstellen|Nullstellen]] – Zur Bestimmung der Schnittpunkte
- → [[Rotationskoerper|Rotationskörper]] – Weiterführende geometrische Anwendung
- → [[Volumenberechnungen|Volumenberechnungen]] – Dreidimensionale Erweiterung

> [!warning] **Prüfungsrelevant**
> - Die Schnittpunkte der Funktionen sind die **Integrationsgrenzen**
> - Bei mehreren Schnittpunkten: **Aufteilen** oder **Betrag** verwenden
> - Die Differenz "obere minus untere Funktion" muss im Intervall **positiv** sein
> - Vergiss nicht, die Lagebeziehung durch **Einsetzen eines Testpunkts** zu prüfen!

> [!question] **Typische Prüfungsfragen**
> - Berechne die von den Graphen $f(x) = x^2$ und $g(x) = x + 2$ eingeschlossene Fläche.
> - Die Graphen von $f$ und $g$ schneiden sich in den Punkten $A(-1|2)$ und $B(3|4)$. Erkläre, wie du die eingeschlossene Fläche berechnest.
> - Warum muss man bei der Flächenberechnung zwischen Graphen auf die Lagebeziehung achten?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1, Springer Vieweg, 2018
- Bronstein, I. N. et al.: Taschenbuch der Mathematik, Europa-Lehrmittel, 2020
- ISB Bayern: Lehrplan Mathematik Gymnasium, Analysis

> [!tip] **Weiterführende Links**
> - [[Rotationskoerper|Rotationskörper]] – Körper durch Rotation eingeschlossener Flächen
> - [[Anwendungen-in-der-Physik|Anwendungen in der Physik]] – Arbeit als Fläche unter der Kraft-Weg-Kurve
