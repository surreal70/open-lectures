---
author: Andreas Hümmer
title: Nullhypothese und Alternativhypothese
tags:
  - content
  - mathe
  - statistik
  - hypothesentest
  - nullhypothese
created: 2025-06-26
modified: 2025-06-26
---

# Nullhypothese und Alternativhypothese

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Null- und Alternativhypothese korrekt aufstellen können
> - Die Rolle der Nullhypothese im Testverfahren erklären können
> - Zwischen einseitigen und zweiseitigen Tests unterscheiden können
> - Hypothesen aus Sachzusammenhängen ableiten können

---

## Überblick

Ein **Hypothesentest** ist ein systematisches Verfahren, um auf Basis von Stichprobendaten zu entscheiden, ob eine Behauptung über einen Parameter der Grundgesamtheit haltbar ist oder nicht. Zentral dabei ist die Gegenüberstellung zweier sich widersprechender Aussagen: der **Nullhypothese** und der **Alternativhypothese**.

---

## Die Nullhypothese $H_0$

### Definition

Die **Nullhypothese** $H_0$ ist die Aussage, die zunächst als wahr angenommen wird und die es zu widerlegen gilt. Sie beschreibt typischerweise:

- Keinen Effekt („kein Unterschied")
- Keine Veränderung („alles wie bisher")
- Den Zustand, den wir anzweifeln wollen

### Eigenschaften

- Die Nullhypothese enthält immer ein **Gleichheitszeichen** (=, ≤ oder ≥)
- Sie wird so lange beibehalten, bis die Daten sie eindeutig widerlegen
- Sie ist die „Standardannahme" – wie die Unschuldsvermutung vor Gericht

### Beispiele

| Sachzusammenhang | Nullhypothese $H_0$ |
|------------------|---------------------|
| Münze ist fair | $p = 0{,}5$ |
| Medikament wirkt nicht besser | $p_{\text{neu}} = p_{\text{alt}}$ |
| Ausschussquote unverändert | $p = 0{,}05$ |
| Mittlere Lebensdauer beträgt 1000h | $\mu = 1000$ |

---

## Die Alternativhypothese $H_1$

### Definition

Die **Alternativhypothese** $H_1$ (auch $H_A$) ist die Aussage, die wir nachweisen möchten. Sie beschreibt die Abweichung von der Nullhypothese und enthält typischerweise:

- Einen Effekt („es gibt einen Unterschied")
- Eine Veränderung („es ist anders als behauptet")
- Das, was wir zeigen wollen

### Eigenschaften

- Die Alternativhypothese enthält ein **Ungleichheitszeichen** (<, > oder ≠)
- Sie wird nur angenommen, wenn die Daten stark genug gegen $H_0$ sprechen
- Sie formuliert die „Forschungshypothese" oder den Verdacht

### Zusammenhang $H_0$ und $H_1$

$H_0$ und $H_1$ schließen sich gegenseitig aus und decken alle Möglichkeiten ab:

$$H_0 \cup H_1 = \text{alle möglichen Parameterwerte}$$
$$H_0 \cap H_1 = \emptyset$$

---

## Einseitige und zweiseitige Tests

Je nach Fragestellung unterscheidet man:

### Zweiseitiger Test

**Situation:** Man vermutet eine Abweichung vom Sollwert, aber nicht in welche Richtung.

$$H_0: p = p_0 \quad \text{gegen} \quad H_1: p \neq p_0$$

**Ablehnungsbereich:** Beide Enden der Verteilung

**Beispiel:** „Die Münze ist unfair" – sie könnte zu oft Kopf ODER zu oft Zahl zeigen.

### Rechtsseitiger Test

**Situation:** Man vermutet, dass der Parameter größer ist als behauptet.

$$H_0: p \leq p_0 \quad \text{gegen} \quad H_1: p > p_0$$

**Ablehnungsbereich:** Rechtes Ende der Verteilung (große Werte)

**Beispiel:** „Der Ausschussanteil ist gestiegen" – wir befürchten mehr Defekte als erlaubt.

### Linksseitiger Test

**Situation:** Man vermutet, dass der Parameter kleiner ist als behauptet.

$$H_0: p \geq p_0 \quad \text{gegen} \quad H_1: p < p_0$$

**Ablehnungsbereich:** Linkes Ende der Verteilung (kleine Werte)

**Beispiel:** „Die Trefferquote ist gesunken" – wir befürchten weniger Erfolge als normal.

### Übersicht

| Testtyp | $H_0$ | $H_1$ | Ablehnungsbereich |
|---------|-------|-------|-------------------|
| Zweiseitig | $p = p_0$ | $p \neq p_0$ | Beide Seiten |
| Rechtsseitig | $p \leq p_0$ | $p > p_0$ | Rechts (große Werte) |
| Linksseitig | $p \geq p_0$ | $p < p_0$ | Links (kleine Werte) |

---

## Aufstellen der Hypothesen

### Schritt-für-Schritt-Anleitung

1. **Fragestellung analysieren:** Was soll nachgewiesen werden?
2. **Forschungshypothese identifizieren:** Das ist typischerweise $H_1$
3. **Nullhypothese formulieren:** Das Gegenteil bzw. „kein Effekt"
4. **Testart bestimmen:** Einseitig oder zweiseitig?

### Beispiel: Qualitätskontrolle

**Sachzusammenhang:** Ein Hersteller garantiert, dass höchstens 5% seiner Produkte defekt sind. Ein Käufer vermutet, dass der Anteil höher ist, und möchte dies nachweisen.

**Analyse:**
- Der Käufer will nachweisen: „Anteil > 5%" → Das ist $H_1$
- Der Hersteller behauptet: „Anteil ≤ 5%" → Das ist $H_0$
- Es geht nur um „zu viel Ausschuss" → Rechtsseitiger Test

**Hypothesen:**
$$H_0: p \leq 0{,}05$$
$$H_1: p > 0{,}05$$

### Beispiel: Medikamentenstudie

**Sachzusammenhang:** Ein neues Medikament soll besser wirken als das bisherige Standardmedikament mit Wirksamkeit $p_0 = 0{,}60$.

**Hypothesen:**
$$H_0: p \leq 0{,}60 \quad \text{(neues Medikament nicht besser)}$$
$$H_1: p > 0{,}60 \quad \text{(neues Medikament besser)}$$

### Beispiel: Münzwurf

**Sachzusammenhang:** Es soll geprüft werden, ob eine Münze fair ist.

**Hypothesen:**
$$H_0: p = 0{,}5 \quad \text{(Münze fair)}$$
$$H_1: p \neq 0{,}5 \quad \text{(Münze unfair)}$$

Hier ist ein zweiseitiger Test angebracht, da sowohl $p > 0{,}5$ als auch $p < 0{,}5$ auf Unfairness hindeuten würde.

---

## Die Logik des Testens

### Grundprinzip: Widerspruchsbeweis

Das Testverfahren folgt dem Prinzip des indirekten Beweises:

1. **Annahme:** $H_0$ ist wahr
2. **Berechnung:** Wie wahrscheinlich ist das beobachtete (oder ein extremeres) Ergebnis unter $H_0$?
3. **Entscheidung:** Ist diese Wahrscheinlichkeit sehr klein, widersprechen die Daten der Annahme → $H_0$ wird verworfen

### Was bedeutet „$H_0$ ablehnen"?

- Die Daten liefern **genügend Evidenz gegen $H_0$**
- Wir entscheiden uns für $H_1$
- Es gibt einen **statistisch signifikanten** Befund

### Was bedeutet „$H_0$ nicht ablehnen"?

- Die Daten liefern **nicht genügend Evidenz gegen $H_0$**
- Wir behalten $H_0$ bei (Entscheidung für $H_0$)
- Das bedeutet **nicht**, dass $H_0$ wahr ist!

> [!warning] **Wichtige Unterscheidung**
> „$H_0$ nicht ablehnen" ≠ „$H_0$ bewiesen"
> 
> Wir können $H_0$ nie beweisen, nur widerlegen. Fehlt die Evidenz für eine Ablehnung, bleibt $H_0$ die Arbeitshypothese – mehr nicht.

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Signifikanzniveau]] – Die Schwelle für die Ablehnung von $H_0$
- → [[Fehler-erster-und-zweiter-Art]] – Mögliche Fehlentscheidungen beim Testen
- → [[Binomialtests]] – Konkrete Durchführung des Hypothesentests
- → [[Konfidenzintervalle-Grundlagen]] – Zusammenhang zwischen Tests und Intervallen

> [!warning] **Prüfungsrelevant**
> - Korrektes Aufstellen von $H_0$ und $H_1$ aus dem Sachzusammenhang
> - Entscheidung für einseitigen oder zweiseitigen Test
> - Die Nullhypothese enthält IMMER das Gleichheitszeichen
> - $H_1$ formuliert das, was nachgewiesen werden soll
> - Unterscheidung: „$H_0$ nicht ablehnen" vs. „$H_0$ beweisen"

> [!question] **Typische Prüfungsfragen**
> - Ein Hersteller behauptet, dass sein Produkt in mindestens 80% der Fälle wirkt. Ein Verbraucherverband zweifelt dies an. Formuliere $H_0$ und $H_1$.
> - Erkläre, warum man die Alternativhypothese so formuliert, dass sie die zu beweisende Aussage enthält.
> - Liegt ein einseitiger oder zweiseitiger Test vor, wenn geprüft werden soll, ob sich die Trefferquote eines Spielers verändert hat?

---

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3. Springer Vieweg, 2016.
- Fahrmeir, L. et al.: Statistik – Der Weg zur Datenanalyse. Springer, 2016.
- ISB Bayern: Abiturprüfungen Mathematik.

> [!tip] **Weiterführende Links**
> - [[Signifikanzniveau]] – Wie wird die Entscheidungsgrenze festgelegt?
> - [[Binomialtests]] – Anwendung auf Anteilswerte
