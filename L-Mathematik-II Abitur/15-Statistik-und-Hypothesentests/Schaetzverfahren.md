---
author: Andreas Hümmer
title: Schätzverfahren
tags:
  - content
  - mathe
  - statistik
  - schaetzverfahren
  - punktschaetzung
created: 2025-06-26
modified: 2025-06-26
---

# Schätzverfahren

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Begriff der Punktschätzung erklären und Beispiele nennen können
> - Gütekriterien für Schätzer (Erwartungstreue, Effizienz, Konsistenz) verstehen
> - Schätzer für Mittelwert, Varianz und Anteilswert anwenden können
> - Den Unterschied zwischen Punktschätzung und Intervallschätzung kennen

---

## Überblick

**Schätzverfahren** sind Methoden, um aus Stichprobendaten auf unbekannte Parameter der Grundgesamtheit zu schließen. Man unterscheidet:

- **Punktschätzung**: Ein einzelner Wert wird als Schätzung angegeben
- **Intervallschätzung**: Ein Bereich wird angegeben, der den Parameter mit einer gewissen Wahrscheinlichkeit enthält

Dieses Kapitel behandelt die Punktschätzung. Die Intervallschätzung wird in [[Konfidenzintervalle-Grundlagen]] vertieft.

---

## Grundbegriffe

### Schätzer und Schätzwert

Ein **Schätzer** (Schätzfunktion) ist eine Rechenvorschrift, die aus den Stichprobenwerten $X_1, X_2, \ldots, X_n$ einen Schätzwert für den unbekannten Parameter $\theta$ berechnet.

$$\hat{\theta} = g(X_1, X_2, \ldots, X_n)$$

- Der Schätzer $\hat{\theta}$ ist eine Zufallsvariable (vor der Stichprobenziehung)
- Der Schätzwert ist die konkrete Realisierung (nach der Stichprobenziehung)

**Beispiel:** Der Stichprobenmittelwert $\bar{X} = \frac{1}{n}\sum_{i=1}^{n} X_i$ ist ein Schätzer für den Erwartungswert $\mu$ der Grundgesamtheit.

### Stichprobenfunktionen als Schätzer

| Parameter | Schätzer | Formel |
|-----------|----------|--------|
| Erwartungswert $\mu$ | Stichprobenmittel $\bar{X}$ | $\frac{1}{n}\sum_{i=1}^{n} X_i$ |
| Varianz $\sigma^2$ | Stichprobenvarianz $S^2$ | $\frac{1}{n-1}\sum_{i=1}^{n} (X_i - \bar{X})^2$ |
| Anteil $p$ | Stichprobenanteil $\hat{p}$ | $\frac{X}{n}$ (X = Anzahl Erfolge) |

---

## Gütekriterien für Schätzer

Nicht jeder Schätzer ist gleich gut. Die folgenden Kriterien helfen bei der Bewertung:

### Erwartungstreue (Unverzerrtheit)

Ein Schätzer $\hat{\theta}$ heißt **erwartungstreu** (unverzerrt), wenn sein Erwartungswert gleich dem wahren Parameter ist:

$$E(\hat{\theta}) = \theta$$

Der **Bias** (Verzerrung) ist definiert als:

$$\text{Bias}(\hat{\theta}) = E(\hat{\theta}) - \theta$$

Ein erwartungstreuer Schätzer hat Bias = 0.

**Beispiele:**
- $\bar{X}$ ist erwartungstreu für $\mu$: $E(\bar{X}) = \mu$
- Die Stichprobenvarianz mit Nenner $(n-1)$ ist erwartungstreu für $\sigma^2$
- Die Varianz mit Nenner $n$ ist **nicht** erwartungstreu (unterschätzt systematisch)

### Effizienz

Von zwei erwartungstreuen Schätzern ist derjenige **effizienter**, der die kleinere Varianz hat:

$$\text{Var}(\hat{\theta}_1) < \text{Var}(\hat{\theta}_2) \Rightarrow \hat{\theta}_1 \text{ ist effizienter}$$

Der Stichprobenmittelwert $\bar{X}$ ist der effizienteste erwartungstreue Schätzer für $\mu$ bei normalverteilten Daten.

### Konsistenz

Ein Schätzer heißt **konsistent**, wenn er mit wachsendem Stichprobenumfang gegen den wahren Parameter konvergiert:

$$\lim_{n \to \infty} P(|\hat{\theta}_n - \theta| > \varepsilon) = 0 \quad \text{für alle } \varepsilon > 0$$

In der Praxis bedeutet dies: Je größer die Stichprobe, desto genauer die Schätzung.

### Mittlerer quadratischer Fehler

Der **mittlere quadratische Fehler** (MSE) kombiniert Verzerrung und Varianz:

$$\text{MSE}(\hat{\theta}) = E[(\hat{\theta} - \theta)^2] = \text{Var}(\hat{\theta}) + [\text{Bias}(\hat{\theta})]^2$$

Für erwartungstreue Schätzer gilt: $\text{MSE} = \text{Var}(\hat{\theta})$

---

## Wichtige Schätzer im Detail

### Schätzer für den Erwartungswert

Der **Stichprobenmittelwert** ist der Standardschätzer für $\mu$:

$$\bar{X} = \frac{1}{n} \sum_{i=1}^{n} X_i$$

**Eigenschaften:**
- Erwartungstreu: $E(\bar{X}) = \mu$
- Varianz: $\text{Var}(\bar{X}) = \frac{\sigma^2}{n}$
- Standardfehler: $\text{SE}(\bar{X}) = \frac{\sigma}{\sqrt{n}}$

### Schätzer für die Varianz

Die **korrigierte Stichprobenvarianz** mit Nenner $(n-1)$:

$$S^2 = \frac{1}{n-1} \sum_{i=1}^{n} (X_i - \bar{X})^2$$

**Warum $(n-1)$ statt $n$?**

Durch die Verwendung von $\bar{X}$ statt $\mu$ verliert man einen Freiheitsgrad. Die Division durch $(n-1)$ korrigiert diese Unterschätzung (Bessel-Korrektur).

Alternativ mit Verschiebungssatz:
$$S^2 = \frac{1}{n-1} \left( \sum_{i=1}^{n} X_i^2 - n\bar{X}^2 \right)$$

### Schätzer für den Anteilswert

Bei einer Bernoulli-Stichprobe (Erfolg/Misserfolg) mit $X$ Erfolgen bei $n$ Versuchen:

$$\hat{p} = \frac{X}{n}$$

**Eigenschaften:**
- Erwartungstreu: $E(\hat{p}) = p$
- Varianz: $\text{Var}(\hat{p}) = \frac{p(1-p)}{n}$
- Standardfehler: $\text{SE}(\hat{p}) = \sqrt{\frac{p(1-p)}{n}}$

---

## Beispiel: Qualitätskontrolle

In einer Produktionsstätte werden Glühbirnen hergestellt. Aus einer Tagesproduktion werden $n = 100$ Glühbirnen zufällig ausgewählt und getestet. 8 sind defekt.

**Punktschätzung für den Ausschussanteil:**

$$\hat{p} = \frac{8}{100} = 0{,}08 = 8\%$$

**Standardfehler der Schätzung:**

$$\text{SE}(\hat{p}) = \sqrt{\frac{0{,}08 \cdot 0{,}92}{100}} = \sqrt{\frac{0{,}0736}{100}} \approx 0{,}027 = 2{,}7\%$$

Die Punktschätzung beträgt 8% mit einer Unsicherheit von etwa 2,7 Prozentpunkten.

---

## Maximum-Likelihood-Methode

Die **Maximum-Likelihood-Schätzung** (MLE) ist ein allgemeines Verfahren zur Konstruktion von Schätzern:

1. Stelle die Likelihood-Funktion auf: $L(\theta) = P(X_1, \ldots, X_n | \theta)$
2. Finde den Wert $\hat{\theta}$, der $L(\theta)$ maximiert

**Beispiel:** Für eine Binomialverteilung $X \sim B(n, p)$ mit beobachtetem Wert $x$:

$$L(p) = \binom{n}{x} p^x (1-p)^{n-x}$$

Die Maximierung liefert: $\hat{p}_{ML} = \frac{x}{n}$ – den bekannten Stichprobenanteil.

> [!note] **Für das Abitur**
> Die Maximum-Likelihood-Methode wird im bayerischen Abitur nicht direkt abgefragt. Wichtig ist das Verständnis, dass die üblichen Schätzer (Mittelwert, Anteil) optimale Eigenschaften haben.

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Stichproben]] – Grundlagen der Stichprobentheorie
- → [[Konfidenzintervalle-Grundlagen]] – Von der Punktschätzung zur Intervallschätzung
- → [[Statistische-Kenngroessen]] – Berechnungsformeln für Mittelwert und Varianz
- → [[Binomialverteilung]] – Verteilungsannahme für Anteilsschätzer
- → [[Normalverteilung]] – Verteilung von Stichprobenmittelwerten

> [!warning] **Prüfungsrelevant**
> - Berechnung von Stichprobenmittelwert, Stichprobenvarianz und Stichprobenanteil
> - Standardfehler des Mittelwerts: $\text{SE}(\bar{X}) = \frac{s}{\sqrt{n}}$
> - Standardfehler des Anteils: $\text{SE}(\hat{p}) = \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$
> - Interpretation der Erwartungstreue: Der Schätzer „trifft im Mittel"
> - Bessel-Korrektur bei der Varianzschätzung

> [!question] **Typische Prüfungsfragen**
> - Aus einer Stichprobe von 50 Messwerten wurde $\bar{x} = 12{,}4$ und $s = 2{,}1$ berechnet. Gib den Standardfehler des Mittelwerts an.
> - Warum wird bei der Berechnung der Stichprobenvarianz durch $(n-1)$ und nicht durch $n$ geteilt?
> - Bei 200 Befragten gaben 68 an, Produkt A zu bevorzugen. Schätze den Anteil in der Grundgesamtheit und berechne den Standardfehler.

---

## Quellen

- Fahrmeir, L. et al.: Statistik – Der Weg zur Datenanalyse. Springer, 2016.
- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3. Springer Vieweg, 2016.
- ISB Bayern: Abiturprüfungen Mathematik.

> [!tip] **Weiterführende Links**
> - [[Konfidenzintervalle-Grundlagen]] – Intervallschätzung als Erweiterung
> - [[Nullhypothese-und-Alternativhypothese]] – Schätzer in Hypothesentests
