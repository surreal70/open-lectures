---
author: Andreas Hümmer
title: Flächenbilanz
tags:
  - content
  - mathe
  - integralrechnung
  - fläche
  - orientierte-fläche
created: 2026-10-17
modified: 2026-10-17
---

# Flächenbilanz

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Unterschied zwischen orientierter Fläche und Flächeninhalt kennen
> - Flächenbilanzen bei Vorzeichenwechsel berechnen können
> - Die Betragsintegration zur Berechnung von Gesamtflächen anwenden können
> - Typische Fehler bei der Flächenberechnung vermeiden

---

## Überblick

Das bestimmte Integral liefert eine **orientierte Fläche**, bei der Bereiche unterhalb der $x$-Achse negativ gezählt werden. In vielen Anwendungen – etwa bei der Berechnung von Materialflächen oder Volumina – benötigt man jedoch den tatsächlichen **Flächeninhalt** ohne Vorzeichenberücksichtigung. Die Flächenbilanz beschreibt, wie man mit dieser Problematik umgeht.

## Orientierte Fläche vs. Flächeninhalt

### Die orientierte Fläche

Das bestimmte Integral $\int_a^b f(x) \, dx$ liefert die **orientierte Fläche**:

- Bereiche, in denen $f(x) > 0$: positiver Beitrag
- Bereiche, in denen $f(x) < 0$: negativer Beitrag

Die Summe dieser Beiträge ist die Flächenbilanz.

### Beispiel: Sinusfunktion

$$\int_0^{2\pi} \sin(x) \, dx = \Big[-\cos(x)\Big]_0^{2\pi} = -\cos(2\pi) + \cos(0) = -1 + 1 = 0$$

Obwohl der Graph der Sinusfunktion eingeschlossene Flächen hat, ist die Bilanz null, weil sich positive und negative Anteile aufheben.

### Der tatsächliche Flächeninhalt

Für den **tatsächlichen Flächeninhalt** (ohne Vorzeichen) muss man die Beträge der Teilflächen addieren:

$$A_{\text{gesamt}} = \int_0^{\pi} \sin(x) \, dx + \left| \int_{\pi}^{2\pi} \sin(x) \, dx \right|$$

$$= \Big[-\cos(x)\Big]_0^{\pi} + \left| \Big[-\cos(x)\Big]_{\pi}^{2\pi} \right|$$

$$= (-\cos(\pi) + \cos(0)) + |{-\cos(2\pi) + \cos(\pi)}|$$

$$= (1 + 1) + |{-1 - 1}| = 2 + 2 = 4$$

## Berechnung bei Vorzeichenwechsel

### Schritt-für-Schritt-Verfahren

1. **Nullstellen bestimmen**: Finde alle $x$-Werte im Intervall $[a, b]$, an denen $f(x) = 0$
2. **Intervalle aufteilen**: Zerlege $[a, b]$ an den Nullstellen in Teilintervalle
3. **Vorzeichen prüfen**: Bestimme in jedem Teilintervall, ob $f(x) > 0$ oder $f(x) < 0$
4. **Teilintegrale berechnen**: Berechne das Integral über jedes Teilintervall
5. **Beträge addieren**: Summiere die Beträge aller Teilintegrale

### Beispiel: Parabel

Berechne den Flächeninhalt zwischen dem Graphen von $f(x) = x^2 - 4$ und der $x$-Achse im Intervall $[-3, 3]$.

**Schritt 1**: Nullstellen
$$x^2 - 4 = 0 \Rightarrow x = \pm 2$$

**Schritt 2**: Teilintervalle: $[-3, -2]$, $[-2, 2]$, $[2, 3]$

**Schritt 3**: Vorzeichen
- In $[-3, -2]$: $f(x) > 0$ (z.B. $f(-3) = 5 > 0$)
- In $[-2, 2]$: $f(x) < 0$ (z.B. $f(0) = -4 < 0$)
- In $[2, 3]$: $f(x) > 0$ (z.B. $f(3) = 5 > 0$)

**Schritt 4**: Stammfunktion: $F(x) = \frac{x^3}{3} - 4x$

$$\int_{-3}^{-2} (x^2 - 4) \, dx = \left[\frac{x^3}{3} - 4x\right]_{-3}^{-2} = \left(-\frac{8}{3} + 8\right) - \left(-9 + 12\right) = \frac{16}{3} - 3 = \frac{7}{3}$$

$$\int_{-2}^{2} (x^2 - 4) \, dx = \left[\frac{x^3}{3} - 4x\right]_{-2}^{2} = \left(\frac{8}{3} - 8\right) - \left(-\frac{8}{3} + 8\right) = -\frac{32}{3}$$

$$\int_{2}^{3} (x^2 - 4) \, dx = \left[\frac{x^3}{3} - 4x\right]_{2}^{3} = (9 - 12) - \left(\frac{8}{3} - 8\right) = -3 + \frac{16}{3} = \frac{7}{3}$$

**Schritt 5**: Flächeninhalt
$$A = \frac{7}{3} + \left|-\frac{32}{3}\right| + \frac{7}{3} = \frac{7}{3} + \frac{32}{3} + \frac{7}{3} = \frac{46}{3}$$

## Alternative: Das Betragsintegral

### Schreibweise

Der Flächeninhalt kann auch geschrieben werden als:

$$A = \int_a^b |f(x)| \, dx$$

### Praktische Berechnung

Das Betragsintegral wird **nicht** direkt berechnet, sondern durch Fallunterscheidung:

$$\int_a^b |f(x)| \, dx = \sum_{\text{Teilintervalle}} \left| \int_{x_i}^{x_{i+1}} f(x) \, dx \right|$$

Dies ist äquivalent zum oben beschriebenen Verfahren.

## Typische Aufgabenstellungen

### Aufgabentyp 1: Orientierte Fläche

> „Berechne $\int_a^b f(x) \, dx$."

Hier wird direkt das Integral berechnet, Vorzeichen werden berücksichtigt (Flächenbilanz).

### Aufgabentyp 2: Flächeninhalt

> „Berechne den Flächeninhalt zwischen dem Graphen von $f$ und der $x$-Achse."

Hier müssen Nullstellen bestimmt und Beträge addiert werden.

### Aufgabentyp 3: Eingeschlossene Fläche

> „Berechne die von $f$ und $g$ eingeschlossene Fläche."

Hier berechnet man $\int_a^b |f(x) - g(x)| \, dx$, wobei $a$ und $b$ die Schnittpunkte sind.

## Häufige Fehler

### Fehler 1: Vorzeichen ignorieren

❌ „Der Flächeninhalt ist $\int_0^{2\pi} \sin(x) \, dx = 0$."

✅ Die Flächenbilanz ist 0, aber der Flächeninhalt ist 4.

### Fehler 2: Nullstellen übersehen

❌ Bei einer Funktion mit Vorzeichenwechsel das Integral direkt über das gesamte Intervall berechnen.

✅ Zuerst Nullstellen bestimmen und dann in Teilintervallen arbeiten.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Bestimmte-Integrale]] – Definition des bestimmten Integrals
- → [[Flaechenberechnung]] – Allgemeine Flächenberechnungen
- → [[Nullstellen]] – Bestimmung der Nullstellen für die Intervallzerlegung
- → [[Betrag-und-Betragsgleichungen]] – Der Betrag in der Mathematik
- → [[Integrale-im-Sachzusammenhang]] – Anwendung auf reale Probleme

> [!warning] **Prüfungsrelevant**
> - Unterschied zwischen orientierter Fläche und Flächeninhalt beachten!
> - Bei Flächeninhalt: Nullstellen bestimmen und Beträge addieren
> - Aufgabenstellung genau lesen: „Integral" vs. „Flächeninhalt"
> - Negative Integralwerte korrekt interpretieren

> [!question] **Typische Prüfungsfragen**
> - Berechne den Flächeninhalt, den der Graph von $f(x) = x^3 - x$ im Intervall $[-1, 1]$ mit der $x$-Achse einschließt.
> - Erkläre anhand eines Beispiels, warum das bestimmte Integral negativ sein kann, obwohl Flächen immer positiv sind.
> - Warum gilt $\int_{-\pi}^{\pi} \sin(x) \, dx = 0$, obwohl die Sinusfunktion keine Nullfunktion ist?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I. N. et al.: Taschenbuch der Mathematik. Verlag Harri Deutsch, 2012.
- Tietze, J.: Einführung in die angewandte Wirtschaftsmathematik. Springer Spektrum, 2013.

> [!tip] **Weiterführende Links**
> - [[Flaechenberechnung]] – Flächen zwischen zwei Kurven
> - [[Integrale-im-Sachzusammenhang]] – Praktische Anwendungen
