---
author: Andreas Hümmer
title: Signifikanzniveau
tags:
  - content
  - mathe
  - statistik
  - hypothesentest
  - signifikanzniveau
  - alpha
created: 2025-06-26
modified: 2025-06-26
---

# Signifikanzniveau

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das Signifikanzniveau $\alpha$ definieren und interpretieren können
> - Den Zusammenhang zwischen Signifikanzniveau und Fehler 1. Art verstehen
> - Den Ablehnungsbereich für gegebenes $\alpha$ bestimmen können
> - Übliche Signifikanzniveaus kennen und ihre Wahl begründen können

---

## Überblick

Das **Signifikanzniveau** $\alpha$ ist eine zentrale Größe im Hypothesentest. Es legt fest, wie groß die Wahrscheinlichkeit maximal sein darf, die Nullhypothese fälschlicherweise abzulehnen. Damit bestimmt $\alpha$ die Strenge des Tests und damit auch, welche Stichprobenergebnisse zur Ablehnung von $H_0$ führen.

---

## Definition des Signifikanzniveaus

### Formale Definition

Das **Signifikanzniveau** $\alpha$ ist die maximale Wahrscheinlichkeit, $H_0$ abzulehnen, obwohl $H_0$ wahr ist:

$$\alpha = P(\text{Ablehnung von } H_0 \mid H_0 \text{ ist wahr})$$

Dies entspricht der Wahrscheinlichkeit für einen **Fehler erster Art**.

### Typische Werte

| Signifikanzniveau | Bedeutung | Anwendung |
|-------------------|-----------|-----------|
| $\alpha = 0{,}10$ (10%) | Weniger streng | Erste Orientierung, explorative Studien |
| $\alpha = 0{,}05$ (5%) | Standard | Die meisten wissenschaftlichen Studien |
| $\alpha = 0{,}01$ (1%) | Sehr streng | Medizin, sicherheitskritische Bereiche |

> [!note] **Konvention**
> Das Signifikanzniveau wird **vor** der Datenerhebung festgelegt, nicht nachträglich angepasst!

---

## Ablehnungsbereich und kritischer Wert

### Der Ablehnungsbereich

Der **Ablehnungsbereich** (kritischer Bereich) enthält alle Stichprobenergebnisse, bei denen $H_0$ verworfen wird. Seine Größe wird durch $\alpha$ bestimmt.

**Faustregel:** Der Ablehnungsbereich umfasst genau die $\alpha \cdot 100\%$ „extremsten" Ergebnisse unter $H_0$.

### Beim Binomialtest

Sei $X \sim B(n, p_0)$ die Anzahl der Erfolge unter $H_0$, dann:

**Rechtsseitiger Test** ($H_1: p > p_0$):
$$\text{Ablehnungsbereich} = \{k, k+1, \ldots, n\}$$
wobei $k$ der kleinste Wert ist mit $P(X \geq k) \leq \alpha$

**Linksseitiger Test** ($H_1: p < p_0$):
$$\text{Ablehnungsbereich} = \{0, 1, \ldots, k\}$$
wobei $k$ der größte Wert ist mit $P(X \leq k) \leq \alpha$

**Zweiseitiger Test** ($H_1: p \neq p_0$):
$$\text{Ablehnungsbereich} = \{0, \ldots, k_u\} \cup \{k_o, \ldots, n\}$$
wobei beide Bereiche zusammen höchstens Wahrscheinlichkeit $\alpha$ haben

### Beispiel: Binomialtest

Ein Würfel wird 60-mal geworfen. Unter der Hypothese „Würfel fair" ($p_0 = \frac{1}{6}$) ist die Anzahl der Sechsen $X \sim B(60, \frac{1}{6})$ mit $E(X) = 10$.

**Rechtsseitiger Test** mit $\alpha = 0{,}05$:

Man sucht das kleinste $k$ mit $P(X \geq k) \leq 0{,}05$.

Aus der Binomialverteilung oder Tabellen:
- $P(X \geq 15) \approx 0{,}0671 > 0{,}05$
- $P(X \geq 16) \approx 0{,}0355 \leq 0{,}05$

**Ablehnungsbereich:** $\{16, 17, \ldots, 60\}$

Bei 16 oder mehr Sechsen wird $H_0$ abgelehnt.

---

## Signifikanz und p-Wert

### Der p-Wert

Der **p-Wert** ist die Wahrscheinlichkeit, unter $H_0$ ein Ergebnis zu erhalten, das mindestens so extrem ist wie das beobachtete.

**Entscheidungsregel:**
- $p\text{-Wert} \leq \alpha$: $H_0$ ablehnen (Ergebnis ist signifikant)
- $p\text{-Wert} > \alpha$: $H_0$ nicht ablehnen

### Beispiel

Beim Würfelversuch wurden 18 Sechsen beobachtet.

$$p\text{-Wert} = P(X \geq 18) \approx 0{,}0076$$

Da $0{,}0076 < 0{,}05$, wird $H_0$ abgelehnt. Das Ergebnis ist **signifikant auf dem 5%-Niveau**.

Sogar auf dem 1%-Niveau wäre das Ergebnis signifikant ($0{,}0076 < 0{,}01$).

### Interpretation des p-Werts

| p-Wert | Interpretation |
|--------|----------------|
| $p > 0{,}10$ | Kein Hinweis gegen $H_0$ |
| $0{,}05 < p \leq 0{,}10$ | Schwacher Hinweis gegen $H_0$ |
| $0{,}01 < p \leq 0{,}05$ | Signifikant (mäßig starker Hinweis) |
| $p \leq 0{,}01$ | Hochsignifikant (starker Hinweis) |

> [!warning] **Häufiger Fehler**
> Der p-Wert ist **nicht** die Wahrscheinlichkeit, dass $H_0$ wahr ist!
> 
> Er sagt nur: „Wenn $H_0$ wahr wäre, wie wahrscheinlich wäre dann dieses oder ein extremeres Ergebnis?"

---

## Wahl des Signifikanzniveaus

### Abwägung zwischen Fehlern

Die Wahl von $\alpha$ ist eine Abwägung:

- **Kleines $\alpha$**: Weniger Fehler 1. Art, aber mehr Fehler 2. Art
- **Großes $\alpha$**: Mehr Fehler 1. Art, aber weniger Fehler 2. Art

```
α klein ──────────────────────── α groß
   │                                  │
   │  Wenig falsch-positive          │  Viele falsch-positive
   │  Viele falsch-negative          │  Wenig falsch-negative
   │  Schwerer zu "beweisen"         │  Leichter zu "beweisen"
```

### Kriterien für die Wahl

1. **Schwere der Konsequenzen:** Bei gravierenden Folgen eines Fehlers 1. Art wählt man $\alpha$ klein
2. **Konventionen des Fachgebiets:** In der Medizin oft $\alpha = 0{,}01$, in der Psychologie $\alpha = 0{,}05$
3. **Stichprobenumfang:** Bei kleinen Stichproben kann zu kleines $\alpha$ dazu führen, dass praktisch nie abgelehnt wird

### Beispiele

| Situation | Empfohlenes $\alpha$ | Begründung |
|-----------|---------------------|------------|
| Medikamentenzulassung | 0,01 | Falsche Zulassung gefährdet Patienten |
| Marketingstudie | 0,10 | Geringe Konsequenzen bei Fehlentscheidung |
| Qualitätskontrolle | 0,05 | Standardwert, Abwägung Kosten/Qualität |

---

## Statistische vs. praktische Signifikanz

### Unterschied

- **Statistische Signifikanz:** Das Ergebnis ist unwahrscheinlich unter $H_0$
- **Praktische Signifikanz:** Der gefundene Effekt ist groß genug, um relevant zu sein

### Beispiel

Eine Studie mit $n = 10.000$ Personen zeigt, dass Medikament A den Blutdruck um durchschnittlich 1 mmHg mehr senkt als Medikament B.

- **Statistisch signifikant:** Ja, bei dieser Stichprobengröße ist selbst dieser kleine Unterschied nachweisbar
- **Praktisch signifikant:** Nein, 1 mmHg Unterschied ist klinisch irrelevant

> [!tip] **Merke**
> Statistische Signifikanz sagt nichts über die Größe oder Wichtigkeit eines Effekts aus!

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Nullhypothese-und-Alternativhypothese]] – Was getestet wird
- → [[Fehler-erster-und-zweiter-Art]] – Die Konsequenzen von $\alpha$
- → [[Binomialtests]] – Anwendung auf konkrete Testprobleme
- → [[Konfidenzintervalle-Grundlagen]] – $\alpha$ und Konfidenzniveau hängen zusammen

> [!warning] **Prüfungsrelevant**
> - Definition: $\alpha = P(\text{Ablehnung} \mid H_0 \text{ wahr})$
> - Übliche Werte: 1%, 5%, 10%
> - Ablehnungsbereich bestimmen für gegebenes $\alpha$
> - Entscheidungsregel: p-Wert $\leq \alpha$ → Ablehnung
> - $\alpha$ wird VOR dem Test festgelegt, nicht nachträglich
> - Unterschied zwischen statistischer und praktischer Signifikanz

> [!question] **Typische Prüfungsfragen**
> - Was bedeutet ein Signifikanzniveau von 5%?
> - Bestimme den Ablehnungsbereich für einen rechtsseitigen Binomialtest mit $n=100$, $p_0=0{,}3$ und $\alpha=0{,}05$.
> - Der p-Wert eines Tests beträgt 0,03. Ist das Ergebnis auf dem 5%-Niveau signifikant? Auf dem 1%-Niveau?

---

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3. Springer Vieweg, 2016.
- Fahrmeir, L. et al.: Statistik – Der Weg zur Datenanalyse. Springer, 2016.
- ISB Bayern: Abiturprüfungen Mathematik.

> [!tip] **Weiterführende Links**
> - [[Fehler-erster-und-zweiter-Art]] – Was passiert bei falschen Entscheidungen?
> - [[Binomialtests]] – Konkrete Anwendung der Konzepte
