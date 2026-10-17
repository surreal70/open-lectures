---
author: Andreas Hümmer
title: Binomialtests
tags:
  - content
  - mathe
  - statistik
  - hypothesentest
  - binomialtest
  - binomialverteilung
created: 2025-06-26
modified: 2025-06-26
---

# Binomialtests

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Binomialtests für Anteilswerte durchführen können
> - Den Ablehnungsbereich für gegebenes Signifikanzniveau bestimmen können
> - Einseitige und zweiseitige Binomialtests unterscheiden können
> - Typische Abituraufgaben zu Binomialtests lösen können

---

## Überblick

Der **Binomialtest** ist ein Hypothesentest für den Parameter $p$ einer Binomialverteilung. Er prüft, ob der wahre Anteil in einer Grundgesamtheit einem vermuteten Wert entspricht. Der Binomialtest ist der wichtigste Hypothesentest im bayerischen Mathematik-Abitur.

---

## Voraussetzungen

Der Binomialtest setzt voraus:

1. **Dichotomes Merkmal:** Jede Beobachtung hat genau zwei mögliche Ausgänge (Erfolg/Misserfolg)
2. **Konstante Wahrscheinlichkeit:** Die Erfolgswahrscheinlichkeit $p$ ist bei jedem Versuch gleich
3. **Unabhängigkeit:** Die einzelnen Versuche sind voneinander unabhängig
4. **Fester Stichprobenumfang:** Die Anzahl $n$ der Versuche ist vorab festgelegt

Unter diesen Bedingungen gilt: $X \sim B(n, p)$, wobei $X$ die Anzahl der Erfolge ist.

---

## Durchführung des Binomialtests

### Schritt 1: Hypothesen aufstellen

Formuliere $H_0$ und $H_1$ entsprechend der Fragestellung:

| Testart | $H_0$ | $H_1$ |
|---------|-------|-------|
| Rechtsseitig | $p \leq p_0$ | $p > p_0$ |
| Linksseitig | $p \geq p_0$ | $p < p_0$ |
| Zweiseitig | $p = p_0$ | $p \neq p_0$ |

### Schritt 2: Signifikanzniveau festlegen

Wähle $\alpha$ (typisch: 0,05 oder 0,01) **vor** der Datenanalyse.

### Schritt 3: Ablehnungsbereich bestimmen

Der Ablehnungsbereich enthält die Werte von $X$, bei denen $H_0$ verworfen wird.

**Rechtsseitiger Test ($H_1: p > p_0$):**

Suche das kleinste $k$, sodass unter $H_0$:
$$P(X \geq k) \leq \alpha$$

Ablehnungsbereich: $\bar{A} = \{k, k+1, \ldots, n\}$

**Linksseitiger Test ($H_1: p < p_0$):**

Suche das größte $k$, sodass unter $H_0$:
$$P(X \leq k) \leq \alpha$$

Ablehnungsbereich: $\bar{A} = \{0, 1, \ldots, k\}$

**Zweiseitiger Test ($H_1: p \neq p_0$):**

Bestimme untere Grenze $k_u$ und obere Grenze $k_o$ mit:
$$P(X \leq k_u) + P(X \geq k_o) \leq \alpha$$

Ablehnungsbereich: $\bar{A} = \{0, \ldots, k_u\} \cup \{k_o, \ldots, n\}$

### Schritt 4: Testentscheidung

- Liegt der beobachtete Wert $x$ im Ablehnungsbereich: **$H_0$ ablehnen**
- Liegt $x$ nicht im Ablehnungsbereich: **$H_0$ nicht ablehnen**

---

## Ausführliches Beispiel: Rechtsseitiger Test

### Aufgabe

Ein Würfel soll auf Fairness geprüft werden. Bei 100 Würfen wurde 23-mal eine Sechs gewürfelt. Prüfe auf dem 5%-Niveau, ob der Würfel zu oft Sechsen zeigt.

### Lösung

**Schritt 1: Hypothesen**
$$H_0: p \leq \frac{1}{6} \approx 0{,}167$$
$$H_1: p > \frac{1}{6}$$

(Rechtsseitig, weil wir „zu viele Sechsen" vermuten)

**Schritt 2: Signifikanzniveau**
$$\alpha = 0{,}05$$

**Schritt 3: Ablehnungsbereich**

Unter $H_0$ gilt $X \sim B(100, \frac{1}{6})$ mit $E(X) = 16{,}67$.

Gesucht: kleinstes $k$ mit $P(X \geq k) \leq 0{,}05$

Berechnung (mit Tabelle oder Taschenrechner):
- $P(X \geq 23) \approx 0{,}0695 > 0{,}05$
- $P(X \geq 24) \approx 0{,}0446 \leq 0{,}05$

Ablehnungsbereich: $\bar{A} = \{24, 25, \ldots, 100\}$

**Schritt 4: Entscheidung**

Beobachtet wurde $x = 23$.

Da $23 \notin \bar{A}$, wird $H_0$ **nicht abgelehnt**.

**Interpretation:** Das Ergebnis ist auf dem 5%-Niveau nicht signifikant. Die Daten liefern keinen ausreichenden Hinweis darauf, dass der Würfel zu oft Sechsen zeigt.

---

## Beispiel: Linksseitiger Test

### Aufgabe

Ein Hersteller behauptet, dass seine Samen eine Keimrate von mindestens 90% haben. Bei einer Stichprobe von $n = 50$ keimten nur 40 Samen. Prüfe auf dem 5%-Niveau, ob die Keimrate unter 90% liegt.

### Lösung

**Hypothesen:**
$$H_0: p \geq 0{,}90$$
$$H_1: p < 0{,}90$$

**Unter $H_0$:** $X \sim B(50, 0{,}9)$ mit $E(X) = 45$

**Ablehnungsbereich:**

Gesucht: größtes $k$ mit $P(X \leq k) \leq 0{,}05$

- $P(X \leq 40) \approx 0{,}0245 \leq 0{,}05$ ✓
- $P(X \leq 41) \approx 0{,}0579 > 0{,}05$

Ablehnungsbereich: $\bar{A} = \{0, 1, \ldots, 40\}$

**Entscheidung:**

$x = 40 \in \bar{A}$ → $H_0$ wird **abgelehnt**.

Die Keimrate ist signifikant niedriger als vom Hersteller angegeben.

---

## Beispiel: Zweiseitiger Test

### Aufgabe

Bei einer Münze soll geprüft werden, ob sie fair ist. Bei 80 Würfen fiel 48-mal Kopf. Teste auf dem 5%-Niveau.

### Lösung

**Hypothesen:**
$$H_0: p = 0{,}5$$
$$H_1: p \neq 0{,}5$$

**Unter $H_0$:** $X \sim B(80, 0{,}5)$ mit $E(X) = 40$

**Ablehnungsbereich (zweiseitig):**

Für $\alpha = 0{,}05$ wird auf jeder Seite etwa $\frac{\alpha}{2} = 0{,}025$ verwendet.

- Linke Grenze: größtes $k_u$ mit $P(X \leq k_u) \leq 0{,}025$
  $P(X \leq 31) \approx 0{,}0196$ → $k_u = 31$
  
- Rechte Grenze: kleinstes $k_o$ mit $P(X \geq k_o) \leq 0{,}025$
  $P(X \geq 49) \approx 0{,}0196$ → $k_o = 49$

Ablehnungsbereich: $\bar{A} = \{0, \ldots, 31\} \cup \{49, \ldots, 80\}$

**Entscheidung:**

$x = 48 \notin \bar{A}$ → $H_0$ wird **nicht abgelehnt**.

Es gibt keinen signifikanten Hinweis auf Unfairness der Münze.

---

## Berechnung von Fehlerwahrscheinlichkeiten

### Tatsächliches Signifikanzniveau

Das tatsächliche $\alpha$ kann vom vorgegebenen abweichen:

$$\alpha_{\text{tats}} = P(X \in \bar{A} \mid H_0)$$

**Beispiel:** Bei $\bar{A} = \{24, \ldots, 100\}$ und $p_0 = \frac{1}{6}$:
$$\alpha_{\text{tats}} = P(X \geq 24) \approx 0{,}0446 < 0{,}05$$

### Fehler 2. Art

Für einen spezifischen alternativen Wert $p_1$:

$$\beta(p_1) = P(X \notin \bar{A} \mid p = p_1)$$

**Beispiel:** Wenn der Würfel tatsächlich $p_1 = 0{,}25$ hat:
$$\beta(0{,}25) = P(X \leq 23 \mid p = 0{,}25)$$

Mit $X \sim B(100, 0{,}25)$: $\beta(0{,}25) \approx 0{,}4602$

Der Test würde eine erhöhte Sechser-Wahrscheinlichkeit von 25% in 46% der Fälle übersehen.

---

## Umkehraufgabe: Stichprobenumfang bestimmen

### Problemstellung

Wie groß muss $n$ sein, damit der Test bei gegebenem $\alpha$ eine bestimmte Abweichung von $p_0$ erkennt?

### Näherungsformel

Für einen rechtsseitigen Test mit Signifikanzniveau $\alpha$ und Macht $1-\beta$ bei $p_1 > p_0$:

$$n \approx \frac{\left(z_{1-\alpha}\sqrt{p_0(1-p_0)} + z_{1-\beta}\sqrt{p_1(1-p_1)}\right)^2}{(p_1 - p_0)^2}$$

### Beispiel

Wie viele Versuche braucht man, um eine Erhöhung von $p_0 = 0{,}5$ auf $p_1 = 0{,}6$ mit $\alpha = 0{,}05$ und Macht 80% ($\beta = 0{,}2$) zu erkennen?

Mit $z_{0{,}95} = 1{,}645$ und $z_{0{,}8} = 0{,}842$:

$$n \approx \frac{(1{,}645 \cdot 0{,}5 + 0{,}842 \cdot 0{,}49)^2}{0{,}1^2} = \frac{(0{,}823 + 0{,}413)^2}{0{,}01} \approx 153$$

---

## Zusammenfassung: Vorgehensweise

```
1. Hypothesen aufstellen
   └─ H₀ enthält Gleichheit, H₁ die Behauptung
   
2. Signifikanzniveau α festlegen
   └─ Typisch: 0,05 oder 0,01
   
3. Testgröße X ~ B(n, p₀) unter H₀
   
4. Ablehnungsbereich bestimmen
   ├─ Rechtsseitig: {k, ..., n} mit P(X ≥ k) ≤ α
   ├─ Linksseitig: {0, ..., k} mit P(X ≤ k) ≤ α
   └─ Zweiseitig: Beide Seiten mit je α/2
   
5. Beobachteten Wert x mit Ablehnungsbereich vergleichen
   ├─ x ∈ Ā → H₀ ablehnen
   └─ x ∉ Ā → H₀ nicht ablehnen
   
6. Interpretation im Sachzusammenhang
```

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Binomialverteilung]] – Die zugrundeliegende Verteilung
- → [[Nullhypothese-und-Alternativhypothese]] – Aufstellen der Hypothesen
- → [[Signifikanzniveau]] – Festlegung der Entscheidungsgrenze
- → [[Fehler-erster-und-zweiter-Art]] – Berechnung der Fehlerwahrscheinlichkeiten
- → [[Konfidenzintervalle-Grundlagen]] – Alternativer Ansatz über Intervalle

> [!warning] **Prüfungsrelevant**
> - Korrektes Aufstellen von $H_0$ und $H_1$ aus dem Sachzusammenhang
> - Bestimmung des Ablehnungsbereichs mit Taschenrechner/Tabelle
> - Durchführung der Testentscheidung
> - Berechnung des tatsächlichen Signifikanzniveaus
> - Berechnung von $\beta$ für gegebenes alternatives $p_1$
> - Interpretation im Sachzusammenhang

> [!question] **Typische Prüfungsfragen**
> - Bei einer Qualitätskontrolle soll geprüft werden, ob der Ausschussanteil über 5% liegt. Von 200 Produkten sind 16 defekt. Führe einen Test zum 5%-Niveau durch.
> - Bestimme den Ablehnungsbereich für einen rechtsseitigen Test mit $n=50$, $p_0=0{,}3$, $\alpha=0{,}05$.
> - Berechne die Fehlerwahrscheinlichkeit 2. Art, wenn der wahre Anteil $p_1=0{,}4$ beträgt.

---

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3. Springer Vieweg, 2016.
- Fahrmeir, L. et al.: Statistik – Der Weg zur Datenanalyse. Springer, 2016.
- ISB Bayern: Abiturprüfungen Mathematik.

> [!tip] **Weiterführende Links**
> - [[Interpretation-statistischer-Ergebnisse]] – Ergebnisse richtig kommunizieren
> - [[Statistik-mit-Python]] – Binomialtests programmieren
