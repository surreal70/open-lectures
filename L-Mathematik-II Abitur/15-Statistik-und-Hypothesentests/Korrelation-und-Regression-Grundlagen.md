---
author: Andreas Hümmer
title: Korrelation und Regression Grundlagen
tags:
  - content
  - mathe
  - statistik
  - korrelation
  - regression
  - zusammenhang
created: 2025-06-26
modified: 2025-06-26
---

# Korrelation und Regression Grundlagen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Korrelationskoeffizienten berechnen und interpretieren können
> - Die lineare Regressionsgerade bestimmen können
> - Den Unterschied zwischen Korrelation und Kausalität verstehen
> - Das Bestimmtheitsmaß $R^2$ interpretieren können

---

## Überblick

In vielen Situationen interessiert man sich für den **Zusammenhang** zwischen zwei Merkmalen: Steigt die Körpergröße mit dem Gewicht? Hängen Lernzeit und Prüfungsergebnis zusammen? Die **Korrelationsanalyse** misst die Stärke eines linearen Zusammenhangs, die **Regressionsanalyse** beschreibt diesen Zusammenhang durch eine Funktion.

---

## Der Korrelationskoeffizient

### Definition

Der **Korrelationskoeffizient nach Pearson** $r$ misst die Stärke und Richtung des linearen Zusammenhangs zwischen zwei metrischen Merkmalen $X$ und $Y$:

$$r = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n}(x_i - \bar{x})^2} \cdot \sqrt{\sum_{i=1}^{n}(y_i - \bar{y})^2}}$$

**Alternative Schreibweise:**

$$r = \frac{s_{xy}}{s_x \cdot s_y}$$

wobei $s_{xy} = \frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})$ die **Kovarianz** ist.

### Berechnungsformel (rechenfreundlich)

$$r = \frac{n \cdot \sum x_i y_i - \sum x_i \cdot \sum y_i}{\sqrt{n \cdot \sum x_i^2 - (\sum x_i)^2} \cdot \sqrt{n \cdot \sum y_i^2 - (\sum y_i)^2}}$$

### Eigenschaften

- **Wertebereich:** $-1 \leq r \leq 1$
- **Symmetrie:** $r_{xy} = r_{yx}$
- **Dimensionslos:** Unabhängig von den Maßeinheiten

### Interpretation

| Wert von $r$ | Interpretation |
|--------------|----------------|
| $r = 1$ | Perfekter positiver linearer Zusammenhang |
| $r = -1$ | Perfekter negativer linearer Zusammenhang |
| $r = 0$ | Kein linearer Zusammenhang |
| $0 < r < 1$ | Positiver Zusammenhang (je größer $x$, desto größer $y$) |
| $-1 < r < 0$ | Negativer Zusammenhang (je größer $x$, desto kleiner $y$) |

**Faustregeln:**

| $\lvert r \rvert$ | Stärke des Zusammenhangs |
|-------------------|-------------------------|
| $< 0{,}3$ | Schwach |
| $0{,}3$ – $0{,}7$ | Mittel |
| $> 0{,}7$ | Stark |

---

## Beispiel: Korrelationsberechnung

Gegeben sind die Daten:

| $x$ (Lernstunden) | 2 | 4 | 5 | 6 | 8 |
|-------------------|---|---|---|---|---|
| $y$ (Punktzahl) | 50 | 65 | 70 | 80 | 90 |

**Berechnung:**

Hilfstabelle:

| $i$ | $x_i$ | $y_i$ | $x_i^2$ | $y_i^2$ | $x_i \cdot y_i$ |
|-----|-------|-------|---------|---------|-----------------|
| 1 | 2 | 50 | 4 | 2500 | 100 |
| 2 | 4 | 65 | 16 | 4225 | 260 |
| 3 | 5 | 70 | 25 | 4900 | 350 |
| 4 | 6 | 80 | 36 | 6400 | 480 |
| 5 | 8 | 90 | 64 | 8100 | 720 |
| $\sum$ | 25 | 355 | 145 | 26125 | 1910 |

Mit $n = 5$:

$$r = \frac{5 \cdot 1910 - 25 \cdot 355}{\sqrt{5 \cdot 145 - 625} \cdot \sqrt{5 \cdot 26125 - 126025}}$$

$$r = \frac{9550 - 8875}{\sqrt{725 - 625} \cdot \sqrt{130625 - 126025}} = \frac{675}{\sqrt{100} \cdot \sqrt{4600}}$$

$$r = \frac{675}{10 \cdot 67{,}82} = \frac{675}{678{,}2} \approx 0{,}995$$

**Interpretation:** Es besteht ein sehr starker positiver linearer Zusammenhang zwischen Lernzeit und Punktzahl.

---

## Lineare Regression

### Das Modell

Die **lineare Regression** beschreibt den Zusammenhang durch eine Gerade:

$$\hat{y} = a + b \cdot x$$

wobei:
- $a$ der **y-Achsenabschnitt** ist
- $b$ die **Steigung** (Regressionskoeffizient) ist
- $\hat{y}$ der **vorhergesagte** (geschätzte) $y$-Wert ist

### Methode der kleinsten Quadrate

Die Regressionsgerade wird so bestimmt, dass die Summe der quadrierten Abweichungen minimal ist:

$$\sum_{i=1}^{n} (y_i - \hat{y}_i)^2 = \sum_{i=1}^{n} (y_i - a - b \cdot x_i)^2 \to \min$$

### Formeln für Steigung und Achsenabschnitt

**Steigung:**

$$b = \frac{n \cdot \sum x_i y_i - \sum x_i \cdot \sum y_i}{n \cdot \sum x_i^2 - (\sum x_i)^2} = \frac{s_{xy}}{s_x^2}$$

**y-Achsenabschnitt:**

$$a = \bar{y} - b \cdot \bar{x}$$

### Beispiel (Fortsetzung)

Mit den Werten von oben:

$$b = \frac{5 \cdot 1910 - 25 \cdot 355}{5 \cdot 145 - 625} = \frac{675}{100} = 6{,}75$$

$$\bar{x} = \frac{25}{5} = 5, \quad \bar{y} = \frac{355}{5} = 71$$

$$a = 71 - 6{,}75 \cdot 5 = 71 - 33{,}75 = 37{,}25$$

**Regressionsgerade:** $\hat{y} = 37{,}25 + 6{,}75 \cdot x$

**Interpretation:** Pro zusätzlicher Lernstunde erhöht sich die erwartete Punktzahl um etwa 6,75 Punkte.

---

## Das Bestimmtheitsmaß $R^2$

### Definition

Das **Bestimmtheitsmaß** $R^2$ gibt an, welcher Anteil der Streuung von $Y$ durch die Regression erklärt wird:

$$R^2 = r^2$$

Bei der einfachen linearen Regression ist $R^2$ das Quadrat des Korrelationskoeffizienten.

### Interpretation

- $R^2 = 0$: Das Modell erklärt nichts
- $R^2 = 1$: Das Modell erklärt die Daten perfekt
- $R^2 = 0{,}7$: 70% der Streuung werden durch das Modell erklärt

**Beispiel:** Mit $r \approx 0{,}995$ ergibt sich $R^2 \approx 0{,}99$.

99% der Variation in der Punktzahl können durch die Lernzeit erklärt werden.

---

## Korrelation ist nicht Kausalität

### Das Problem

Ein hoher Korrelationskoeffizient zeigt nur, dass zwei Variablen **zusammenhängen** – nicht, dass eine die andere **verursacht**.

### Mögliche Erklärungen für Korrelation

1. **X verursacht Y** (direkte Kausalität)
   - Mehr Lernzeit → bessere Note

2. **Y verursacht X** (umgekehrte Kausalität)
   - Schlechte Noten → mehr Lernzeit (Schüler lernt mehr nach schlechter Note)

3. **Dritte Variable Z beeinflusst beide** (Scheinkorrelation)
   - Beispiel: Eisverkauf und Ertrinkungsfälle korrelieren positiv – beide werden durch Sommerwetter verursacht

4. **Zufall** (bei kleinen Stichproben)

### Bekannte Scheinkorrelationen

| Korrelation | Wahrer Zusammenhang |
|-------------|---------------------|
| Storchenpopulation ↔ Geburtenrate | Beide hängen von Urbanisierung ab |
| Schokoladenkonsum ↔ Nobelpreise | Wohlstand beeinflusst beides |
| Schuhgröße ↔ Lesefähigkeit | Alter ist die eigentliche Variable |

> [!warning] **Merke**
> Korrelation erlaubt **keine** Kausalaussage!
> 
> „A korreliert mit B" bedeutet nicht „A verursacht B" oder „B verursacht A".

---

## Residuen und Modellprüfung

### Residuen

Das **Residuum** $e_i$ ist die Abweichung zwischen beobachtetem und vorhergesagtem Wert:

$$e_i = y_i - \hat{y}_i = y_i - (a + b \cdot x_i)$$

### Eigenschaften der Residuen

Bei korrekter Berechnung gilt:
- $\sum_{i=1}^{n} e_i = 0$ (Summe der Residuen ist null)
- $\sum_{i=1}^{n} x_i \cdot e_i = 0$

### Residuenanalyse

Die Residuen sollten:
- Zufällig um null streuen
- Keine Muster zeigen
- Annähernd normalverteilt sein

Zeigen die Residuen ein Muster (z.B. eine Kurve), ist das lineare Modell möglicherweise nicht geeignet.

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Statistische-Kenngroessen]] – Mittelwert und Streuung als Grundlagen
- → [[Deskriptive-Statistik]] – Grafische Darstellung von Zusammenhängen
- → [[Interpretation-statistischer-Ergebnisse]] – Vorsicht bei Kausalaussagen
- → [[Lineare-Funktionen]] – Mathematische Grundlagen der Geraden

> [!warning] **Prüfungsrelevant**
> - Berechnung des Korrelationskoeffizienten mit der Rechenformel
> - Interpretation des Korrelationskoeffizienten
> - Aufstellen der Regressionsgeraden
> - Vorhersage von $y$-Werten mit der Regressionsgleichung
> - Interpretation der Steigung im Sachzusammenhang
> - Erklärung, warum Korrelation keine Kausalität impliziert

> [!question] **Typische Prüfungsfragen**
> - Berechne den Korrelationskoeffizienten für die gegebenen Datenpaare und interpretiere das Ergebnis.
> - Bestimme die Regressionsgerade und sage den $y$-Wert für $x = 10$ vorher.
> - Eine Studie zeigt einen positiven Zusammenhang zwischen Bildschirmzeit und Kurzsichtigkeit. Kann man daraus schließen, dass Bildschirme kurzsichtig machen? Begründe.

---

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3. Springer Vieweg, 2016.
- Fahrmeir, L. et al.: Statistik – Der Weg zur Datenanalyse. Springer, 2016.
- ISB Bayern: Abiturprüfungen Mathematik.

> [!tip] **Weiterführende Links**
> - [[Statistik-mit-Python]] – Regression und Korrelation programmieren
> - [[Interpretation-statistischer-Ergebnisse]] – Kritischer Umgang mit Zusammenhängen
