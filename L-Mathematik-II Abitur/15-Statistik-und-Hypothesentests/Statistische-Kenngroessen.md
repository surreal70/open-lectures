---
author: Andreas Hümmer
title: Statistische Kenngrößen
tags:
  - content
  - mathe
  - statistik
  - kenngroessen
  - mittelwert
  - streuung
created: 2025-06-26
modified: 2025-06-26
---

# Statistische Kenngrößen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Lagemaße (Mittelwert, Median, Modus) berechnen und interpretieren können
> - Streuungsmaße (Varianz, Standardabweichung, Spannweite) bestimmen können
> - Quartile und Boxplots erstellen und interpretieren können
> - Die Eignung verschiedener Kenngrößen für unterschiedliche Datentypen beurteilen können

---

## Überblick

Statistische Kenngrößen fassen die wesentlichen Eigenschaften einer Datenreihe in wenigen Zahlen zusammen. Man unterscheidet:

- **Lagemaße**: Beschreiben das Zentrum der Verteilung (Wo liegen die Daten?)
- **Streuungsmaße**: Beschreiben die Variation der Daten (Wie stark streuen die Daten?)

Die Wahl der geeigneten Kenngröße hängt vom Skalenniveau und der Form der Verteilung ab.

---

## Lagemaße

### Arithmetisches Mittel

Das **arithmetische Mittel** (Durchschnitt) $\bar{x}$ ist die Summe aller Werte geteilt durch ihre Anzahl:

$$\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i = \frac{x_1 + x_2 + \ldots + x_n}{n}$$

**Eigenschaften:**
- Berücksichtigt alle Werte
- Empfindlich gegenüber Ausreißern
- Nur für metrische Daten sinnvoll
- Schwerpunkteigenschaft: $\sum_{i=1}^{n}(x_i - \bar{x}) = 0$

**Beispiel:** Für die Werte $3, 5, 7, 8, 12$ gilt:
$$\bar{x} = \frac{3 + 5 + 7 + 8 + 12}{5} = \frac{35}{5} = 7$$

### Gewichtetes arithmetisches Mittel

Wenn Werte $a_j$ mit Häufigkeiten $h_j$ auftreten:

$$\bar{x} = \frac{\sum_{j=1}^{k} a_j \cdot h_j}{\sum_{j=1}^{k} h_j} = \sum_{j=1}^{k} a_j \cdot f_j$$

**Beispiel:** Bei Noten (1, 2, 3, 4) mit Häufigkeiten (2, 5, 8, 5):
$$\bar{x} = \frac{1 \cdot 2 + 2 \cdot 5 + 3 \cdot 8 + 4 \cdot 5}{20} = \frac{2 + 10 + 24 + 20}{20} = \frac{56}{20} = 2{,}8$$

### Median

Der **Median** $\tilde{x}$ (Zentralwert) ist der Wert, der die geordnete Datenreihe in zwei gleich große Hälften teilt.

Für die geordnete Reihe $x_{(1)} \leq x_{(2)} \leq \ldots \leq x_{(n)}$:

$$\tilde{x} = \begin{cases} x_{\left(\frac{n+1}{2}\right)} & \text{wenn } n \text{ ungerade} \\[8pt] \frac{1}{2}\left(x_{\left(\frac{n}{2}\right)} + x_{\left(\frac{n}{2}+1\right)}\right) & \text{wenn } n \text{ gerade} \end{cases}$$

**Eigenschaften:**
- Robust gegenüber Ausreißern
- Für ordinale und metrische Daten geeignet
- Minimiert die Summe der absoluten Abweichungen

**Beispiel:** 
- Ungerade Anzahl: $2, 4, 5, 8, 15$ → Median $= 5$
- Gerade Anzahl: $2, 4, 5, 8, 15, 20$ → Median $= \frac{5+8}{2} = 6{,}5$

### Modus

Der **Modus** $x_{\text{mod}}$ ist der häufigste Wert (die Merkmalsausprägung mit der größten Häufigkeit).

**Eigenschaften:**
- Für alle Skalenniveaus definiert
- Kann mehrdeutig sein (multimodal)
- Bei stetigen Daten nur nach Klassierung sinnvoll

**Beispiel:** Bei $1, 2, 2, 3, 3, 3, 4, 5$ ist der Modus $x_{\text{mod}} = 3$.

### Vergleich der Lagemaße

| Kenngröße | Skalenniveau | Ausreißerrobust | Eindeutig |
|-----------|--------------|-----------------|-----------|
| Modus | alle | ja | nicht immer |
| Median | ordinal, metrisch | ja | ja |
| Mittelwert | metrisch | nein | ja |

Bei **symmetrischen Verteilungen** gilt: Modus ≈ Median ≈ Mittelwert

Bei **schiefen Verteilungen** weichen sie voneinander ab:
- Rechtsschiefe (lange rechte Seite): Modus < Median < Mittelwert
- Linksschiefe (lange linke Seite): Mittelwert < Median < Modus

---

## Streuungsmaße

### Spannweite

Die **Spannweite** (Range) ist die Differenz zwischen größtem und kleinstem Wert:

$$R = x_{\max} - x_{\min} = x_{(n)} - x_{(1)}$$

**Eigenschaften:**
- Einfach zu berechnen
- Sehr anfällig für Ausreißer
- Nutzt nur zwei Werte

### Quartile und Interquartilsabstand

Die **Quartile** teilen die geordnete Datenreihe in vier gleiche Teile:

- $Q_1$ (1. Quartil, 25%-Quantil): 25% der Werte sind kleiner
- $Q_2$ (2. Quartil, 50%-Quantil): entspricht dem Median
- $Q_3$ (3. Quartil, 75%-Quantil): 75% der Werte sind kleiner

Der **Interquartilsabstand** (IQR) umfasst die mittleren 50% der Daten:

$$\text{IQR} = Q_3 - Q_1$$

**Berechnung der Quartile:** Bei $n$ Werten in geordneter Reihenfolge
- Position von $Q_1$: $\frac{n+1}{4}$
- Position von $Q_3$: $\frac{3(n+1)}{4}$

Bei nicht-ganzzahligen Positionen wird interpoliert.

### Varianz

Die **Varianz** $s^2$ misst die durchschnittliche quadrierte Abweichung vom Mittelwert:

$$s^2 = \frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})^2$$

**Verschiebungssatz** (für einfachere Berechnung):

$$s^2 = \frac{1}{n} \sum_{i=1}^{n} x_i^2 - \bar{x}^2 = \overline{x^2} - \bar{x}^2$$

> [!note] **Stichprobenvarianz**
> In der beurteilenden Statistik wird oft durch $(n-1)$ statt $n$ geteilt (Bessel-Korrektur), um einen unverzerrten Schätzer zu erhalten:
> $$s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2$$

**Beispiel:** Für $x_1=2, x_2=4, x_3=6$ mit $\bar{x}=4$:
$$s^2 = \frac{(2-4)^2 + (4-4)^2 + (6-4)^2}{3} = \frac{4 + 0 + 4}{3} = \frac{8}{3} \approx 2{,}67$$

### Standardabweichung

Die **Standardabweichung** $s$ ist die Wurzel aus der Varianz:

$$s = \sqrt{s^2} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})^2}$$

**Eigenschaften:**
- Gleiche Einheit wie die Daten (im Gegensatz zur Varianz)
- Interpretierbar als „typische Abweichung vom Mittelwert"
- Bei annähernd normalverteilten Daten liegen etwa 68% der Werte im Intervall $[\bar{x}-s, \bar{x}+s]$

### Variationskoeffizient

Der **Variationskoeffizient** $V$ ermöglicht den Vergleich der relativen Streuung bei unterschiedlichen Mittelwerten:

$$V = \frac{s}{\bar{x}} \cdot 100\%$$

Nur sinnvoll für $\bar{x} > 0$ und verhältnisskalierte Daten.

---

## Der Boxplot

Der **Boxplot** (Kastenschaubild) ist eine kompakte grafische Darstellung der wichtigsten Kenngrößen:

```
                    Ausreißer
                        *
    ─────┬──────────────────────────┬─────
         │          ┌───────────────┤
    ─────┼──────────┤       |       │─────
         │          └───────────────┤
    ─────┴──────────────────────────┴─────
        Min        Q1    Q2   Q3   Max
         (ohne     (Median)       (ohne
        Ausreißer)               Ausreißer)
```

**Elemente:**
- **Box**: Vom 1. bis 3. Quartil, enthält 50% der Daten
- **Linie in der Box**: Median
- **Whisker** (Antennen): Bis zum kleinsten/größten Wert, der kein Ausreißer ist
- **Ausreißer**: Werte außerhalb von $[Q_1 - 1{,}5 \cdot \text{IQR}, Q_3 + 1{,}5 \cdot \text{IQR}]$

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Deskriptive-Statistik]] – Grundlagen der Datenerfassung und Darstellung
- → [[Stichproben]] – Kenngrößen als Schätzer für Parameter
- → [[Schaetzverfahren]] – Wie Kenngrößen zur Parameterschätzung genutzt werden
- → [[Normalverteilung]] – Bedeutung von Mittelwert und Standardabweichung

> [!warning] **Prüfungsrelevant**
> - Berechnung von Mittelwert, Median und Modus aus Urlisten und Häufigkeitstabellen
> - Berechnung von Varianz und Standardabweichung (mit Verschiebungssatz)
> - Interpretation und Erstellung von Boxplots
> - Entscheidung für geeignete Kenngrößen bei schiefen Verteilungen oder Ausreißern
> - Vergleich von Verteilungen anhand ihrer Kenngrößen

> [!question] **Typische Prüfungsfragen**
> - Berechne Mittelwert, Median und Standardabweichung für eine gegebene Datenreihe.
> - Interpretiere den gegebenen Boxplot: Wie groß ist der Interquartilsabstand? Gibt es Ausreißer?
> - Warum ist bei Gehaltsverteilungen der Median aussagekräftiger als der Mittelwert?

---

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3. Springer Vieweg, 2016.
- Fahrmeir, L. et al.: Statistik – Der Weg zur Datenanalyse. Springer, 2016.
- ISB Bayern: Abiturprüfungen Mathematik.

> [!tip] **Weiterführende Links**
> - [[Konfidenzintervalle-Grundlagen]] – Wie Streuungsmaße in Intervallschätzungen eingehen
> - [[Normalverteilung]] – Die Standardabweichung als Parameter
