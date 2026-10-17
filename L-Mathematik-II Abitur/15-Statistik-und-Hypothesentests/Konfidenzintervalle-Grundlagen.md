---
author: Andreas Hümmer
title: Konfidenzintervalle Grundlagen
tags:
  - content
  - mathe
  - statistik
  - konfidenzintervall
  - intervallschaetzung
created: 2025-06-26
modified: 2025-06-26
---

# Konfidenzintervalle Grundlagen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das Konzept des Konfidenzintervalls erklären können
> - Konfidenzintervalle für Anteile bei der Binomialverteilung berechnen können
> - Das Konfidenzniveau korrekt interpretieren können
> - Den Zusammenhang zwischen Stichprobenumfang, Konfidenzniveau und Intervallbreite verstehen

---

## Überblick

Eine **Punktschätzung** liefert einen einzelnen Wert für einen unbekannten Parameter. Sie sagt jedoch nichts über die Unsicherheit dieser Schätzung aus. Ein **Konfidenzintervall** (Vertrauensintervall) gibt einen Bereich an, der den wahren Parameter mit einer vorgegebenen Wahrscheinlichkeit überdeckt.

Das Konfidenzintervall kombiniert die Punktschätzung mit einer Aussage über die Schätzgenauigkeit.

---

## Das Konzept des Konfidenzintervalls

### Definition

Ein **Konfidenzintervall** zum Konfidenzniveau $(1-\alpha)$ ist ein Intervall $[U, O]$, das mit Wahrscheinlichkeit $(1-\alpha)$ den wahren Parameter $\theta$ enthält:

$$P(U \leq \theta \leq O) = 1 - \alpha$$

Dabei ist:
- $\alpha$ die **Irrtumswahrscheinlichkeit** (typisch: 0,05 oder 0,01)
- $(1-\alpha)$ das **Konfidenzniveau** (typisch: 95% oder 99%)
- $U$ die untere Intervallgrenze
- $O$ die obere Intervallgrenze

### Korrekte Interpretation

> [!warning] **Häufiger Irrtum**
> „Der wahre Parameter liegt mit 95% Wahrscheinlichkeit im Intervall" ist **falsch**!
> 
> Der wahre Parameter ist eine feste (aber unbekannte) Zahl, keine Zufallsvariable. Die Grenzen des Intervalls sind zufällig (sie hängen von der Stichprobe ab).
> 
> **Korrekt:** „Wenn wir das Verfahren oft wiederholen, enthalten 95% der so konstruierten Intervalle den wahren Parameter."

### Allgemeine Struktur

Ein symmetrisches Konfidenzintervall hat die Form:

$$\text{Punktschätzung} \pm \text{Kritischer Wert} \times \text{Standardfehler}$$

---

## Konfidenzintervall für den Anteilswert

### Voraussetzungen

- Binomialverteilte Stichprobe: $X \sim B(n, p)$
- Hinreichend große Stichprobe für Normalapproximation: $n \cdot \hat{p} \geq 5$ und $n \cdot (1-\hat{p}) \geq 5$

### Berechnung

Das approximative $(1-\alpha)$-Konfidenzintervall für $p$ lautet:

$$\left[ \hat{p} - z_{1-\frac{\alpha}{2}} \cdot \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}, \; \hat{p} + z_{1-\frac{\alpha}{2}} \cdot \sqrt{\frac{\hat{p}(1-\hat{p})}{n}} \right]$$

Wobei $z_{1-\frac{\alpha}{2}}$ das entsprechende Quantil der Standardnormalverteilung ist:

| Konfidenzniveau | $\alpha$ | $z_{1-\frac{\alpha}{2}}$ |
|-----------------|----------|--------------------------|
| 90% | 0,10 | 1,645 |
| 95% | 0,05 | 1,960 |
| 99% | 0,01 | 2,576 |

### Beispiel: Wahlumfrage

Bei einer Umfrage unter $n = 400$ Wählern geben 156 an, Partei A zu wählen.

**Punktschätzung:**
$$\hat{p} = \frac{156}{400} = 0{,}39 = 39\%$$

**95%-Konfidenzintervall:**

Standardfehler:
$$\text{SE} = \sqrt{\frac{0{,}39 \cdot 0{,}61}{400}} = \sqrt{\frac{0{,}2379}{400}} \approx 0{,}0244$$

Intervall:
$$[0{,}39 - 1{,}96 \cdot 0{,}0244; \; 0{,}39 + 1{,}96 \cdot 0{,}0244]$$
$$= [0{,}39 - 0{,}048; \; 0{,}39 + 0{,}048]$$
$$= [0{,}342; \; 0{,}438] \approx [34{,}2\%; \; 43{,}8\%]$$

**Interpretation:** Wir sind zu 95% konfident, dass der wahre Anteil der Wähler von Partei A zwischen 34,2% und 43,8% liegt.

---

## Einflussfaktoren auf die Intervallbreite

Die **Intervallbreite** $2 \cdot z_{1-\frac{\alpha}{2}} \cdot \text{SE}$ wird beeinflusst durch:

### 1. Stichprobenumfang $n$

$$\text{Breite} \propto \frac{1}{\sqrt{n}}$$

- Größerer Stichprobenumfang → schmaleres Intervall
- Um die Breite zu halbieren, muss $n$ vervierfacht werden

### 2. Konfidenzniveau $(1-\alpha)$

- Höheres Konfidenzniveau → breiteres Intervall
- 99%-Intervall ist breiter als 95%-Intervall
- Trade-off zwischen Sicherheit und Präzision

### 3. Variabilität der Daten

- Bei Anteilen: Breite maximal bei $p = 0{,}5$
- Bei Mittelwerten: abhängig von der Streuung $\sigma$ oder $s$

---

## Bestimmung des Stichprobenumfangs

Oft möchte man vorab wissen, wie groß die Stichprobe sein muss, um eine gewünschte Genauigkeit zu erreichen.

### Formel für Anteilswerte

Für eine maximale Fehlerspanne $e$ bei Konfidenzniveau $(1-\alpha)$:

$$n \geq \frac{z_{1-\frac{\alpha}{2}}^2 \cdot p(1-p)}{e^2}$$

Bei unbekanntem $p$ setzt man konservativ $p = 0{,}5$:

$$n \geq \frac{z_{1-\frac{\alpha}{2}}^2 \cdot 0{,}25}{e^2}$$

### Beispiel

Wie viele Personen müssen befragt werden, um den Anteil auf $\pm 2\%$ genau zu schätzen (95% Konfidenz)?

$$n \geq \frac{1{,}96^2 \cdot 0{,}25}{0{,}02^2} = \frac{0{,}9604}{0{,}0004} = 2401$$

Es werden mindestens 2401 Personen benötigt.

---

## Sigma-Regeln und Konfidenzintervalle

Bei normalverteilten Größen oder bei Anwendung des zentralen Grenzwertsatzes gelten die **Sigma-Regeln**:

| Bereich | Wahrscheinlichkeit |
|---------|-------------------|
| $\mu \pm 1\sigma$ | ca. 68,3% |
| $\mu \pm 1{,}96\sigma$ | ca. 95% |
| $\mu \pm 2\sigma$ | ca. 95,4% |
| $\mu \pm 2{,}58\sigma$ | ca. 99% |
| $\mu \pm 3\sigma$ | ca. 99,7% |

Diese Regeln bilden die Grundlage für die Wahl der kritischen Werte.

---

## Konfidenzintervall vs. Prognoseintervall

| | Konfidenzintervall | Prognoseintervall |
|-|-------------------|-------------------|
| **Bezieht sich auf** | Unbekannten Parameter | Zukünftige Beobachtung |
| **Wird schmaler bei größerem $n$** | Ja | Begrenzt |
| **Beispiel** | „Wahres $p$ liegt zwischen..." | „Nächste Messung liegt zwischen..." |

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Schaetzverfahren]] – Punktschätzung als Grundlage
- → [[Stichproben]] – Standardfehler und Stichprobenumfang
- → [[Signifikanzniveau]] – Zusammenhang $\alpha$ bei Tests und Intervallen
- → [[Binomialverteilung]] – Verteilung für Anteilswerte
- → [[Normalverteilung]] – Quantile der Standardnormalverteilung

> [!warning] **Prüfungsrelevant**
> - Berechnung von Konfidenzintervallen für Anteilswerte
> - Kenntnis der kritischen Werte: $z_{0{,}975} = 1{,}96$ für 95%, $z_{0{,}995} = 2{,}58$ für 99%
> - Korrekte Interpretation: nicht „Parameter liegt mit 95% im Intervall"
> - Zusammenhang: größere Stichprobe → schmaleres Intervall
> - Bestimmung des benötigten Stichprobenumfangs für vorgegebene Genauigkeit

> [!question] **Typische Prüfungsfragen**
> - Von 200 Befragten sind 72 für eine Maßnahme. Berechne das 95%-Konfidenzintervall für den wahren Anteil.
> - Interpretiere das Konfidenzintervall $[0{,}42; 0{,}58]$ korrekt.
> - Wie verändert sich die Breite des Konfidenzintervalls, wenn der Stichprobenumfang verdoppelt wird?

---

## Quellen

- Fahrmeir, L. et al.: Statistik – Der Weg zur Datenanalyse. Springer, 2016.
- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3. Springer Vieweg, 2016.
- ISB Bayern: Abiturprüfungen Mathematik.

> [!tip] **Weiterführende Links**
> - [[Binomialtests]] – Konfidenzintervalle und Hypothesentests hängen zusammen
> - [[Interpretation-statistischer-Ergebnisse]] – Kommunikation von Konfidenzintervallen
