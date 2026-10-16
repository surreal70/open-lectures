---
title: "Statistische Grundlagen"
created: 2026-10-13
modified: 2026-10-13
type: lecture
tags:
  - lf11c
  - statistik
  - mittelwert
  - median
  - varianz
  - standardabweichung
source: proTirone (CC-BY-4.0)
---

# Statistische Grundlagen

> [!info] Lernziele
> - Statistische Kennzahlen berechnen können
> - Unterschied zwischen Mittelwert und Median verstehen
> - Varianz und Standardabweichung interpretieren

## Grundlegende Kennzahlen

### Minimum und Maximum

| Kennzahl | Definition |
|----------|------------|
| **Minimum** | Kleinster Wert einer Datenreihe |
| **Maximum** | Größter Wert einer Datenreihe |
| **Spannweite** | Maximum − Minimum |

### Mittelwert (Arithmetisches Mittel)

$$\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n} = \frac{x_1 + x_2 + ... + x_n}{n}$$

> [!note] Eigenschaft
> Aussagekräftig für **gleichmäßig verteilte** Werte. Ausreißer verfälschen den Mittelwert stark.

### Median (Zentralwert)

Der **Median** ist der Wert, der die sortierte Datenreihe in zwei gleich große Hälften teilt.

**Berechnung:**
1. Alle Werte nach Größe sortieren
2. Bei **ungerader** Anzahl: mittlerer Wert
3. Bei **gerader** Anzahl: Mittelwert der beiden mittleren Werte

> [!tip] Vorteil
> Ausreißer fallen beim Median nicht so stark ins Gewicht wie beim Mittelwert.

## Beispiel: Blutdruckwerte

| Typ | Unsortiert | Sortiert |
|-----|------------|----------|
| Systole | `[182, 158, 179, 170]` | `[158, 170, 179, 182]` |
| Puls | `[66, 75, 67, 78]` | `[66, 67, 75, 78]` |

### Systole-Berechnungen

- **Minimum:** 158
- **Maximum:** 182
- **Spannweite:** 182 − 158 = 24
- **Mittelwert:** (182 + 158 + 179 + 170) / 4 = **172**
- **Median:** (170 + 179) / 2 = **174,5**

### Puls-Berechnungen

- **Minimum:** 66
- **Maximum:** 78
- **Spannweite:** 78 − 66 = 12
- **Mittelwert:** (66 + 75 + 67 + 78) / 4 = **71,5**
- **Median:** (67 + 75) / 2 = **71**

## Streuungsmaße

### Varianz

Die **Varianz** misst die durchschnittliche quadratische Abweichung vom Mittelwert.

$$\sigma^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n}$$

**Berechnung Schritt für Schritt:**
1. Mittelwert $\bar{x}$ berechnen
2. Jeden Wert vom Mittelwert subtrahieren
3. Differenzen quadrieren
4. Quadrate addieren
5. Durch Anzahl teilen

### Beispiel: Varianz der Systole-Werte

Mit $\bar{x} = 172$:

$$\sigma^2 = \frac{(158-172)^2 + (170-172)^2 + (179-172)^2 + (182-172)^2}{4}$$

$$= \frac{(-14)^2 + (-2)^2 + 7^2 + 10^2}{4} = \frac{196 + 4 + 49 + 100}{4} = \frac{349}{4} = 87,25$$

### Standardabweichung

Die **Standardabweichung** ist die Quadratwurzel der Varianz.

$$\sigma = \sqrt{\sigma^2}$$

> [!note] Vorteil
> Die Standardabweichung hat dieselbe Einheit wie die Messwerte und ist daher leichter interpretierbar.

**Beispiel:**
- Systole: $\sigma = \sqrt{87,25} \approx 9,34$
- Puls: $\sigma = \sqrt{26,5} \approx 5,15$

> [!tip] Interpretation
> Je **kleiner** die Standardabweichung, desto **gleichförmiger** die Messwerte.

## Zusammenhangsmaße

### Kovarianz

Die **Kovarianz** gibt Auskunft über den Zusammenhang zweier Variablen.

$$Cov(X,Y) = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{n}$$

| Kovarianz | Interpretation |
|-----------|----------------|
| positiv | Wenn X steigt, steigt auch Y |
| negativ | Wenn X steigt, sinkt Y |
| ≈ 0 | Kein linearer Zusammenhang |

### Beispiel: Kovarianz Systole/Puls

| Systole | Puls | Systole − MW | Puls − MW | Produkt |
|---------|------|--------------|-----------|---------|
| 182 | 66 | 10 | −5 | −50 |
| 158 | 75 | −14 | 4 | −56 |
| 179 | 67 | 7 | −4 | −28 |
| 170 | 78 | −2 | 7 | −14 |
| | | | **Summe:** | **−148** |

$$Cov = \frac{-148}{4} = -37$$

### Korrelationskoeffizient

Der **Korrelationskoeffizient** normiert die Kovarianz auf den Bereich [−1, +1].

$$r = \frac{Cov(X,Y)}{\sigma_X \cdot \sigma_Y}$$

| Wert | Interpretation |
|------|----------------|
| r ≈ +1 | Starker positiver Zusammenhang |
| r ≈ 0 | Kein linearer Zusammenhang |
| r ≈ −1 | Starker negativer Zusammenhang |

**Beispiel:**
$$r = \frac{-37}{9,34 \times 5,15} = \frac{-37}{48,1} \approx -0,77$$

> [!note] Interpretation
> Ein Korrelationskoeffizient von −0,77 deutet auf einen **starken negativen Zusammenhang** hin: Wenn die Systole sinkt, steigt tendenziell der Puls.

## Prüfungsrelevanz

> [!question] Typische Prüfungsfragen
> - Berechnen Sie Mittelwert und Median für gegebene Daten
> - Was ist der Unterschied zwischen Varianz und Standardabweichung?
> - Interpretieren Sie einen gegebenen Korrelationskoeffizienten
> - Wann ist der Median aussagekräftiger als der Mittelwert?

## Querverweise

- → [[02-Datenvisualisierung|Datenvisualisierung]] – Grafische Darstellung
- → [[../02-Prozessanalyse/06-Six-Sigma|Six Sigma]] – DPMO, Normalverteilung
- → [[../03-Datenqualitaet/01-Qualitaetskriterien|Datenqualität]] – Qualitätsmerkmale

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (CC-BY-4.0).
