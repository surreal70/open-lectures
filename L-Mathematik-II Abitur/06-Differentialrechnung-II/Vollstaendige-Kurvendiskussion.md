---
author: Andreas Hümmer
title: Vollständige Kurvendiskussion
tags:
  - content
  - mathe
  - differentialrechnung
  - kurvendiskussion
  - analysis
created: 2025-06-20
modified: 2025-06-20
---

# Vollständige Kurvendiskussion

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Alle Schritte einer vollständigen Kurvendiskussion beherrschen
> - Die Ergebnisse der einzelnen Schritte interpretieren und zusammenführen können
> - Funktionsgraphen anhand der berechneten Eigenschaften skizzieren können
> - Kurvendiskussionen für verschiedene Funktionstypen durchführen können

---

## Überblick

Die **vollständige Kurvendiskussion** ist eine systematische Methode zur Untersuchung des Verlaufs einer Funktion. Sie kombiniert alle Werkzeuge der Differentialrechnung, um ein umfassendes Bild des Funktionsverhaltens zu erhalten. Die Kurvendiskussion gehört zu den zentralen Abituraufgaben und erfordert sowohl rechnerische Fähigkeiten als auch ein gutes Verständnis der Zusammenhänge.

## Die Schritte der Kurvendiskussion

### Schritt 1: Definitionsbereich

Bestimme alle $x$-Werte, für die $f(x)$ definiert ist.

**Kritische Stellen:**
- Gebrochenrationale Funktionen: Nenner $\neq 0$
- Wurzelfunktionen: Radikand $\geq 0$
- Logarithmusfunktionen: Argument $> 0$

### Schritt 2: Symmetrie

Prüfe auf Achsensymmetrie oder Punktsymmetrie:

- **Achsensymmetrie** zur $y$-Achse: $f(-x) = f(x)$ für alle $x$
- **Punktsymmetrie** zum Ursprung: $f(-x) = -f(x)$ für alle $x$

### Schritt 3: Nullstellen und Schnittpunkte

- **Nullstellen:** Löse $f(x) = 0$
- **y-Achsenabschnitt:** Berechne $f(0)$ (falls definiert)

### Schritt 4: Grenzwerte und Asymptoten

- **Verhalten für $x \to \pm\infty$:** Bestimme $\lim_{x \to \infty} f(x)$ und $\lim_{x \to -\infty} f(x)$
- **Senkrechte Asymptoten:** An Definitionslücken
- **Waagerechte/Schiefe Asymptoten:** Grenzverhalten

### Schritt 5: Ableitung und Monotonie

- Berechne $f'(x)$
- Bestimme Nullstellen von $f'$
- Untersuche Vorzeichen von $f'$ → Monotoniebereiche

### Schritt 6: Extrempunkte

- Kritische Stellen: $f'(x_0) = 0$
- Klassifikation mit $f''$ oder Vorzeichenwechsel
- Berechne Extremwerte: $f(x_0)$

### Schritt 7: Krümmung und Wendepunkte

- Berechne $f''(x)$
- Nullstellen von $f''$ → Wendekandidaten
- Prüfe hinreichende Bedingung
- Bestimme Krümmungsintervalle

### Schritt 8: Wertebereich

Fasse zusammen, welche $y$-Werte angenommen werden.

### Schritt 9: Graph skizzieren

Trage alle berechneten Punkte und Eigenschaften ein.

## Vollständiges Beispiel

**Funktion:** $f(x) = \frac{x^2 - 1}{x^2 + 1}$

### Schritt 1: Definitionsbereich

Der Nenner $x^2 + 1 > 0$ für alle $x \in \mathbb{R}$.

$$D_f = \mathbb{R}$$

### Schritt 2: Symmetrie

$$f(-x) = \frac{(-x)^2 - 1}{(-x)^2 + 1} = \frac{x^2 - 1}{x^2 + 1} = f(x)$$

Die Funktion ist **achsensymmetrisch** zur $y$-Achse.

### Schritt 3: Nullstellen und y-Achsenabschnitt

**Nullstellen:**
$$f(x) = 0 \iff x^2 - 1 = 0 \iff x = \pm 1$$

Nullstellen: $x_1 = -1$, $x_2 = 1$

**y-Achsenabschnitt:**
$$f(0) = \frac{0 - 1}{0 + 1} = -1$$

### Schritt 4: Grenzverhalten

$$\lim_{x \to \pm\infty} \frac{x^2 - 1}{x^2 + 1} = \lim_{x \to \pm\infty} \frac{1 - \frac{1}{x^2}}{1 + \frac{1}{x^2}} = 1$$

**Waagerechte Asymptote:** $y = 1$

### Schritt 5: Ableitung und Monotonie

Mit Quotientenregel:
$$f'(x) = \frac{2x(x^2+1) - (x^2-1) \cdot 2x}{(x^2+1)^2} = \frac{2x(x^2+1-x^2+1)}{(x^2+1)^2} = \frac{4x}{(x^2+1)^2}$$

**Nullstelle von f':** $f'(x) = 0 \iff x = 0$

**Vorzeichenuntersuchung:** (Nenner immer positiv)

| Intervall | $(-\infty, 0)$ | $(0, \infty)$ |
|-----------|----------------|---------------|
| $f'(x)$ | $-$ | $+$ |
| Monotonie | fallend | steigend |

### Schritt 6: Extrempunkte

Bei $x = 0$: Wechsel von $-$ nach $+$ → **lokales Minimum**

$$f(0) = -1$$

**Tiefpunkt:** $T(0 \mid -1)$

(Wegen Achsensymmetrie und Monotonieverhalten ist dies auch das globale Minimum)

### Schritt 7: Krümmung und Wendepunkte

$$f'(x) = 4x(x^2+1)^{-2}$$

Mit Produktregel:
$$f''(x) = 4(x^2+1)^{-2} + 4x \cdot (-2)(x^2+1)^{-3} \cdot 2x$$
$$= \frac{4}{(x^2+1)^2} - \frac{16x^2}{(x^2+1)^3} = \frac{4(x^2+1) - 16x^2}{(x^2+1)^3} = \frac{4 - 12x^2}{(x^2+1)^3}$$

**Nullstellen von f'':**
$$4 - 12x^2 = 0 \iff x^2 = \frac{1}{3} \iff x = \pm\frac{1}{\sqrt{3}}$$

**Wendepunkte:**
$$f\left(\frac{1}{\sqrt{3}}\right) = \frac{\frac{1}{3} - 1}{\frac{1}{3} + 1} = \frac{-\frac{2}{3}}{\frac{4}{3}} = -\frac{1}{2}$$

Wendepunkte: $W_1\left(-\frac{1}{\sqrt{3}} \mid -\frac{1}{2}\right)$, $W_2\left(\frac{1}{\sqrt{3}} \mid -\frac{1}{2}\right)$

### Schritt 8: Wertebereich

Aus Minimum und Asymptote: $W_f = [-1, 1)$

### Zusammenfassung

| Eigenschaft | Ergebnis |
|-------------|----------|
| Definitionsbereich | $\mathbb{R}$ |
| Symmetrie | achsensymmetrisch |
| Nullstellen | $x = \pm 1$ |
| y-Achsenabschnitt | $(0 \mid -1)$ |
| Asymptote | $y = 1$ (waagerecht) |
| Tiefpunkt | $T(0 \mid -1)$ |
| Wendepunkte | $W_{1,2}\left(\pm\frac{1}{\sqrt{3}} \mid -\frac{1}{2}\right)$ |
| Wertebereich | $[-1, 1)$ |

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Monotonieverhalten]] – Schritt 5 der Kurvendiskussion
- → [[Extremstellen]] – Schritt 6 der Kurvendiskussion
- → [[Wendepunkte]] – Schritt 7 der Kurvendiskussion
- → [[Kruemmungsverhalten]] – Krümmungsanalyse
- → [[Gebrochenrationale-Funktionen]] – Häufiger Funktionstyp

> [!warning] **Prüfungsrelevant**
> - Die Reihenfolge der Schritte kann variieren, aber alle sollten behandelt werden
> - Symmetrie früh prüfen – spart Rechenaufwand
> - Ergebnisse am Ende in Tabelle zusammenfassen
> - Skizze muss zu berechneten Werten passen
> - Bei gebrochenrationalen Funktionen: Asymptoten nicht vergessen!

> [!question] **Typische Prüfungsfragen**
> - Führen Sie eine vollständige Kurvendiskussion für $f$ durch
> - Skizzieren Sie den Graphen anhand der berechneten Eigenschaften
> - Bestimmen Sie den Wertebereich der Funktion
> - Zeigen Sie, dass die Gerade $y = a$ waagerechte Asymptote ist

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020
- ISB Bayern: Lehrplan Mathematik Gymnasium (LehrplanPLUS)

> [!tip] **Weiterführende Links**
> - [[Extremwertprobleme]] – Anwendung der Kurvendiskussion
> - [[Parameterabhaengige-Funktionen]] – Funktionenscharen untersuchen
