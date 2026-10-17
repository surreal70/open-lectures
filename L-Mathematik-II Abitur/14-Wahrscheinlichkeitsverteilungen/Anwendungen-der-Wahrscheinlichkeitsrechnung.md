---
author: Andreas Hümmer
title: Anwendungen der Wahrscheinlichkeitsrechnung
tags:
  - content
  - mathe
  - stochastik
  - anwendungen
  - modellierung
created: 2026-10-17
modified: 2026-10-17
---

# Anwendungen der Wahrscheinlichkeitsrechnung

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Reale Situationen als stochastische Modelle formalisieren können
> - Die passende Verteilung für verschiedene Problemtypen wählen
> - Wahrscheinlichkeitsrechnungen im Sachkontext interpretieren
> - Entscheidungen auf Basis von Wahrscheinlichkeiten begründen

---

## Überblick

Die Wahrscheinlichkeitsrechnung findet in zahlreichen Bereichen Anwendung — von der Qualitätskontrolle über medizinische Tests bis zur Risikoabschätzung. In diesem Kapitel werden typische Anwendungsfelder vorgestellt und die mathematischen Konzepte aus [[Binomialverteilung]], [[Normalverteilung]] und [[Normalapproximation]] auf konkrete Probleme angewendet.

## Qualitätskontrolle

### Annahme- und Ablehnungsentscheidungen

Ein Unternehmen erhält eine Lieferung von 10.000 Bauteilen. Erfahrungsgemäß sind 2% der Teile defekt. Eine Stichprobe von 100 Teilen wird geprüft.

**Modellierung**: $X \sim B(100, 0{,}02)$ mit $X$ = Anzahl defekter Teile

**Kenngrößen**:
$$\mu = n \cdot p = 100 \cdot 0{,}02 = 2$$
$$\sigma = \sqrt{npq} = \sqrt{100 \cdot 0{,}02 \cdot 0{,}98} = 1{,}4$$

**Fragen**:

a) Wahrscheinlichkeit für höchstens 3 defekte Teile:
$$P(X \leq 3) = \sum_{k=0}^{3} \binom{100}{k} \cdot 0{,}02^k \cdot 0{,}98^{100-k} \approx 0{,}859$$

b) Wahrscheinlichkeit für mindestens 5 defekte Teile:
$$P(X \geq 5) = 1 - P(X \leq 4) \approx 1 - 0{,}949 = 0{,}051$$

### Akzeptanzregel

Die Lieferung wird **akzeptiert**, wenn höchstens $c$ defekte Teile gefunden werden. Die Wahl von $c$ beeinflusst:

- **Produzentenrisiko**: Wahrscheinlichkeit, eine gute Lieferung abzulehnen
- **Konsumentenrisiko**: Wahrscheinlichkeit, eine schlechte Lieferung anzunehmen

## Medizinische Tests

### Sensitivität und Spezifität

Ein medizinischer Test zur Erkennung einer Krankheit hat:
- **Sensitivität**: 95% (Wahrscheinlichkeit, einen Kranken als krank zu erkennen)
- **Spezifität**: 98% (Wahrscheinlichkeit, einen Gesunden als gesund zu erkennen)

Die Krankheit tritt bei 1% der Bevölkerung auf.

### Vierfeldertafel

| | Test positiv | Test negativ | Summe |
|---|-------------|--------------|-------|
| Krank | 0,95% | 0,05% | 1% |
| Gesund | 1,98% | 97,02% | 99% |
| Summe | 2,93% | 97,07% | 100% |

### Positiver Vorhersagewert

Wie groß ist die Wahrscheinlichkeit, tatsächlich krank zu sein, wenn der Test positiv ist?

Mit dem [[Satz-von-Bayes|Satz von Bayes]]:

$$P(\text{krank} | \text{Test}^+) = \frac{P(\text{Test}^+ | \text{krank}) \cdot P(\text{krank})}{P(\text{Test}^+)}$$

$$= \frac{0{,}95 \cdot 0{,}01}{0{,}0293} = \frac{0{,}0095}{0{,}0293} \approx 0{,}324$$

**Interpretation**: Nur etwa 32% der positiv Getesteten sind tatsächlich krank! Dies liegt an der geringen Prävalenz der Krankheit.

## Wahlprognosen und Umfragen

### Stichprobenziehung

Bei einer Wahlumfrage werden 1000 Personen befragt. Der wahre Stimmenanteil einer Partei sei $p = 0{,}35$ (35%).

**Modellierung**: $X \sim B(1000, 0{,}35)$

**Kenngrößen**:
$$\mu = 1000 \cdot 0{,}35 = 350$$
$$\sigma = \sqrt{1000 \cdot 0{,}35 \cdot 0{,}65} \approx 15{,}08$$

### 95%-Konfidenzintervall

Mit der [[Normalapproximation]]:

$$P(350 - 1{,}96 \cdot 15{,}08 \leq X \leq 350 + 1{,}96 \cdot 15{,}08) \approx 0{,}95$$

$$P(320 \leq X \leq 380) \approx 0{,}95$$

Als Anteil: $[32\%, 38\%]$

**Interpretation**: Mit 95%-iger Sicherheit liegt der beobachtete Anteil im Intervall $[32\%; 38\%]$.

## Versicherungsmathematik

### Risikoberechnung

Eine Versicherung versichert 10.000 Haushalte gegen Einbruch. Die jährliche Einbruchwahrscheinlichkeit beträgt $p = 0{,}02$. Der durchschnittliche Schaden beträgt 5.000 €.

**Modellierung**: $X \sim B(10000, 0{,}02)$ mit $X$ = Anzahl Einbrüche

**Kenngrößen**:
$$\mu = 10000 \cdot 0{,}02 = 200$$
$$\sigma = \sqrt{10000 \cdot 0{,}02 \cdot 0{,}98} = 14$$

**Erwarteter Gesamtschaden**:
$$E(\text{Schaden}) = 200 \cdot 5000 \text{ €} = 1.000.000 \text{ €}$$

**Prämienberechnung**:

Mindestprämie pro Haushalt: $\frac{1.000.000}{10.000} = 100$ €

Mit Sicherheitszuschlag (z.B. für 2σ-Abweichung):
$$\text{Maximaler Schaden}_{95\%} \approx (200 + 2 \cdot 14) \cdot 5000 = 1.140.000 \text{ €}$$

Prämie mit Zuschlag: 114 € pro Haushalt

## Glücksspiele und Fairness

### Erwartungswert bei Lotterien

Beim Lotto „6 aus 49" beträgt die Wahrscheinlichkeit für 6 Richtige:

$$P(\text{6 Richtige}) = \frac{1}{\binom{49}{6}} = \frac{1}{13.983.816} \approx 7{,}15 \cdot 10^{-8}$$

Bei einem Einsatz von 1 € und einem Jackpot von 10 Millionen €:

$$E(\text{Gewinn}) \approx 10.000.000 \cdot 7{,}15 \cdot 10^{-8} - 1 = 0{,}715 - 1 = -0{,}285 \text{ €}$$

**Interpretation**: Im Mittel verliert man 28,5 Cent pro Spiel (ohne Berücksichtigung der kleineren Gewinne).

### Roulette

Beim Setzen auf „Rot" (18 von 37 Feldern):

$$E(\text{Gewinn}) = 1 \cdot \frac{18}{37} + (-1) \cdot \frac{19}{37} = -\frac{1}{37} \approx -0{,}027 \text{ €}$$

Der Hausvorteil beträgt etwa 2,7%.

## Zuverlässigkeitstheorie

### Systemzuverlässigkeit

Ein technisches System besteht aus 5 unabhängigen Komponenten, die jeweils mit Wahrscheinlichkeit $p = 0{,}99$ funktionieren.

**a) Serienschaltung** (alle müssen funktionieren):

$$P(\text{System funktioniert}) = 0{,}99^5 \approx 0{,}951$$

**b) Parallelschaltung** (mindestens eine muss funktionieren):

$$P(\text{System funktioniert}) = 1 - (1-0{,}99)^5 = 1 - 0{,}01^5 \approx 1 - 10^{-10}$$

### Redundanz

Durch Parallelschaltung (Redundanz) lässt sich die Systemzuverlässigkeit dramatisch erhöhen.

## Entscheidungen unter Unsicherheit

### Erwartungswert-Prinzip

Bei Entscheidungen unter Risiko wählt man oft die Alternative mit dem höchsten [[Erwartungswert]].

**Beispiel**: Investitionsentscheidung

| Szenario | Wahrscheinlichkeit | Projekt A | Projekt B |
|----------|-------------------|-----------|-----------|
| Boom | 30% | +100.000 € | +150.000 € |
| Normal | 50% | +50.000 € | +30.000 € |
| Krise | 20% | -20.000 € | -80.000 € |

$$E(A) = 0{,}3 \cdot 100 + 0{,}5 \cdot 50 + 0{,}2 \cdot (-20) = 30 + 25 - 4 = 51 \text{ T€}$$

$$E(B) = 0{,}3 \cdot 150 + 0{,}5 \cdot 30 + 0{,}2 \cdot (-80) = 45 + 15 - 16 = 44 \text{ T€}$$

Nach dem Erwartungswert-Prinzip ist Projekt A vorzuziehen.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Binomialverteilung]] — Grundlage für Stichprobenprobleme
- → [[Normalapproximation]] — Vereinfachung bei großen Stichproben
- → [[Erwartungswert]] — Zentrale Kenngröße für Entscheidungen
- → [[Standardabweichung]] — Maß für die Unsicherheit
- → [[Bedingte-Wahrscheinlichkeit]] — Grundlage für Testinterpretation
- → [[Satz-von-Bayes]] — Umkehrung von bedingten Wahrscheinlichkeiten

> [!warning] **Prüfungsrelevant**
> - Modellierung von Sachsituationen mit der Binomialverteilung
> - Berechnung und Interpretation von Erwartungswert und Standardabweichung im Kontext
> - Interpretation von Wahrscheinlichkeiten als Risiken oder Chancen
> - Begründung von Entscheidungen mit stochastischen Argumenten

> [!question] **Typische Prüfungsfragen**
> - Modelliere die beschriebene Situation mit einer geeigneten Verteilung und begründe deine Wahl.
> - Berechne die Wahrscheinlichkeit für das beschriebene Ereignis und interpretiere das Ergebnis.
> - Beurteile, ob die Entscheidung unter Risikogesichtspunkten sinnvoll ist.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3. Springer Vieweg, 2016.
- Tietze, J.: Einführung in die angewandte Wirtschaftsmathematik. Springer, 2013.
- ISB Bayern: Lehrplan Mathematik, Gymnasium, Oberstufe.

> [!tip] **Weiterführende Links**
> - [[15-Statistik-und-Hypothesentests-Index|Modul 15: Statistik]] — Vertiefung: Hypothesentests und Konfidenzintervalle
> - [[16-Mathematische-Modellierung-und-Abschlussprojekt-Index|Modul 16: Modellierung]] — Komplexere Modellierungsaufgaben
