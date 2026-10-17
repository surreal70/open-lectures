---
author: Andreas Hümmer
title: Deskriptive Statistik
tags:
  - content
  - mathe
  - statistik
  - deskriptive-statistik
  - datenanalyse
created: 2025-06-26
modified: 2025-06-26
---

# Deskriptive Statistik

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Begriff der deskriptiven Statistik erklären und von der beurteilenden Statistik abgrenzen können
> - Verschiedene Datentypen (nominal, ordinal, metrisch) unterscheiden können
> - Häufigkeitsverteilungen erstellen und interpretieren können
> - Geeignete grafische Darstellungen für unterschiedliche Datentypen wählen können

---

## Überblick

Die **deskriptive Statistik** (beschreibende Statistik) befasst sich mit der Erfassung, Aufbereitung und Darstellung von Daten. Ihr Ziel ist es, große Datenmengen übersichtlich zusammenzufassen, ohne dabei Aussagen über Zusammenhänge oder Ursachen zu treffen. Sie bildet die Grundlage für alle weiterführenden statistischen Analysen.

Im Gegensatz zur **beurteilenden (induktiven) Statistik**, die von Stichproben auf Grundgesamtheiten schließt, beschränkt sich die deskriptive Statistik auf die Beschreibung der vorliegenden Daten.

---

## Grundbegriffe der Statistik

### Statistische Einheit und Merkmal

Eine **statistische Einheit** (auch: Merkmalsträger) ist das einzelne Objekt einer Untersuchung. Das **Merkmal** ist die Eigenschaft, die an jeder Einheit erfasst wird.

| Begriff | Erklärung | Beispiel |
|---------|-----------|----------|
| Grundgesamtheit | Menge aller relevanten Einheiten | Alle Schüler einer Schule |
| Stichprobe | Ausgewählte Teilmenge | 50 zufällig gewählte Schüler |
| Merkmal | Untersuchte Eigenschaft | Körpergröße, Schulnote |
| Merkmalsausprägung | Konkreter Wert des Merkmals | 175 cm, Note 2 |

### Datentypen und Skalenniveaus

Die Art der Daten bestimmt, welche statistischen Methoden anwendbar sind:

**Qualitative (kategoriale) Merkmale:**
- **Nominal**: Kategorien ohne natürliche Ordnung
  - Beispiele: Geschlecht, Augenfarbe, Postleitzahl
  - Erlaubte Operationen: Häufigkeiten zählen, Modus bestimmen
  
- **Ordinal**: Kategorien mit natürlicher Rangordnung
  - Beispiele: Schulnoten, Zufriedenheitsskalen, Bildungsabschlüsse
  - Erlaubte Operationen: Zusätzlich Median und Quartile

**Quantitative (metrische) Merkmale:**
- **Intervallskala**: Gleiche Abstände, aber kein natürlicher Nullpunkt
  - Beispiele: Temperatur in °C, Jahreszahlen
  
- **Verhältnisskala**: Gleiche Abstände und natürlicher Nullpunkt
  - Beispiele: Körpergröße, Gewicht, Einkommen, Alter
  - Erlaubte Operationen: Alle arithmetischen Operationen, Mittelwert

---

## Häufigkeitsverteilungen

### Absolute und relative Häufigkeit

Sei $x_1, x_2, \ldots, x_n$ eine Stichprobe mit $n$ Werten und $a_1, a_2, \ldots, a_k$ die verschiedenen Merkmalsausprägungen.

**Absolute Häufigkeit** $h_j$: Anzahl der Beobachtungen mit Ausprägung $a_j$

$$h_j = \#\{i : x_i = a_j\}$$

**Relative Häufigkeit** $f_j$: Anteil der Beobachtungen mit Ausprägung $a_j$

$$f_j = \frac{h_j}{n}$$

Es gilt stets: $\sum_{j=1}^{k} h_j = n$ und $\sum_{j=1}^{k} f_j = 1$

### Beispiel: Würfelwurf

Ein Würfel wird 60-mal geworfen mit folgenden Ergebnissen:

| Augenzahl $a_j$ | 1 | 2 | 3 | 4 | 5 | 6 | Summe |
|-----------------|---|---|---|---|---|---|-------|
| Absolute Häufigkeit $h_j$ | 8 | 12 | 9 | 11 | 10 | 10 | 60 |
| Relative Häufigkeit $f_j$ | 0,133 | 0,200 | 0,150 | 0,183 | 0,167 | 0,167 | 1,000 |

### Kumulierte Häufigkeiten

Die **kumulierte (summierte) Häufigkeit** $H_j$ gibt an, wie viele Beobachtungen einen Wert kleiner oder gleich $a_j$ haben:

$$H_j = \sum_{i=1}^{j} h_i \quad \text{bzw.} \quad F_j = \sum_{i=1}^{j} f_i$$

---

## Grafische Darstellungen

### Für kategoriale Daten

**Säulen- und Balkendiagramm:**
- Säulen (vertikal) oder Balken (horizontal) für jede Kategorie
- Höhe/Länge entspricht der Häufigkeit
- Säulen stehen mit Abstand nebeneinander

**Kreisdiagramm (Tortendiagramm):**
- Kreissektoren entsprechen den relativen Häufigkeiten
- Winkel: $\alpha_j = f_j \cdot 360°$
- Geeignet für wenige Kategorien (max. 5-6)

### Für metrische Daten

**Histogramm:**
- Daten werden in Klassen eingeteilt
- Rechtecke über jeder Klasse
- **Wichtig**: Die Fläche (nicht die Höhe!) entspricht der Häufigkeit
- Bei gleichen Klassenbreiten: Höhe proportional zur Häufigkeit

**Klassenbildung beim Histogramm:**

Für eine Klasse $[u_j, o_j)$ mit Klassenbreite $b_j = o_j - u_j$:

$$\text{Höhe} = \frac{f_j}{b_j} \quad \text{(Häufigkeitsdichte)}$$

**Empirische Verteilungsfunktion:**

$$F_n(x) = \frac{1}{n} \cdot \#\{i : x_i \leq x\} = \frac{\text{Anzahl der Werte} \leq x}{n}$$

Dies ist eine Treppenfunktion, die bei jedem Datenpunkt um $\frac{1}{n}$ springt.

---

## Klassierung von Daten

Bei großen Datenmengen oder stetigen Merkmalen werden die Daten in **Klassen** eingeteilt.

### Regeln für die Klassenbildung

1. Die Klassen müssen **disjunkt** sein (keine Überlappung)
2. Die Klassen müssen **erschöpfend** sein (alle Werte erfasst)
3. Faustregel für die Klassenanzahl: $k \approx \sqrt{n}$ oder $k \approx 1 + 3{,}3 \cdot \log_{10}(n)$
4. Gleiche Klassenbreiten erleichtern die Interpretation

### Beispiel: Körpergrößen

50 Schüler werden nach Körpergröße erfasst:

| Klasse (cm) | Klassenmitte $m_j$ | Häufigkeit $h_j$ | Rel. Häufigkeit $f_j$ |
|-------------|-------------------|------------------|----------------------|
| [150, 160) | 155 | 5 | 0,10 |
| [160, 170) | 165 | 18 | 0,36 |
| [170, 180) | 175 | 20 | 0,40 |
| [180, 190) | 185 | 7 | 0,14 |

Die Klassenmitte $m_j = \frac{u_j + o_j}{2}$ wird für Berechnungen verwendet, wenn nur die klassierten Daten vorliegen.

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Statistische-Kenngroessen]] – Lagemaße und Streuungsmaße zur Datenbeschreibung
- → [[Stichproben]] – Wie Stichproben gezogen und bewertet werden
- → [[Binomialverteilung]] – Theoretische Verteilung für Häufigkeitsdaten
- → [[Interpretation-statistischer-Ergebnisse]] – Kritische Bewertung statistischer Darstellungen

> [!warning] **Prüfungsrelevant**
> - Unterscheidung der Skalenniveaus (nominal, ordinal, metrisch) und deren Konsequenzen für die Wahl statistischer Methoden
> - Berechnung absoluter und relativer Häufigkeiten
> - Erstellung und Interpretation von Histogrammen
> - Korrekte Klassenbildung bei metrischen Daten
> - Unterschied zwischen Häufigkeit und Häufigkeitsdichte bei ungleichen Klassenbreiten

> [!question] **Typische Prüfungsfragen**
> - Gegeben ist eine Urliste mit Messwerten. Erstelle eine Häufigkeitstabelle und zeichne ein Histogramm.
> - Welches Skalenniveau hat das Merkmal „Schulnote" und welche Kenngrößen sind sinnvoll berechenbar?
> - Erkläre den Unterschied zwischen absoluter und relativer Häufigkeit an einem Beispiel.

---

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3. Springer Vieweg, 2016.
- Bortz, J. & Schuster, C.: Statistik für Human- und Sozialwissenschaftler. Springer, 2010.
- ISB Bayern: Abiturprüfungen Mathematik – Stochastik.

> [!tip] **Weiterführende Links**
> - [[Statistische-Kenngroessen]] – Vertiefung zu Mittelwert, Median und Streuungsmaßen
> - [[Glossar]] – Definitionen statistischer Fachbegriffe
