---
title: Absolute und relative Häufigkeiten
chapter: "13"
section: "13.4"
type: lecture
created: 2026-10-13
modified: 2026-10-25
status: draft - review pending
tags:
  - mathematik/statistik
  - haeufigkeit
---

# Absolute und relative Häufigkeiten

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Absolute Häufigkeiten bestimmen
> - Relative Häufigkeiten berechnen
> - Zwischen beiden Darstellungsformen umrechnen

Die Unterscheidung zwischen absoluter und relativer Häufigkeit ist grundlegend für die Statistik. Während die absolute Häufigkeit einfach zählt, wie oft etwas vorkommt, setzt die relative Häufigkeit diesen Wert ins Verhältnis zur Gesamtzahl. Erst die relative Häufigkeit ermöglicht sinnvolle Vergleiche zwischen unterschiedlich großen Gruppen.

> [!example] **Warum relative Häufigkeiten?**
> In Klasse A (20 Schüler) haben 10 Schüler eine 1 geschrieben.
> In Klasse B (30 Schüler) haben 12 Schüler eine 1 geschrieben.
> 
> Absolut betrachtet hat Klasse B „mehr Einser" (12 > 10).
> Relativ betrachtet war Klasse A besser: 50% vs. 40%.

## Absolute Häufigkeit

> [!note] Definition
> Die **absolute Häufigkeit** $H(x)$ gibt an, wie oft ein Wert $x$ in einer Datenreihe vorkommt.

Die absolute Häufigkeit ist die einfachste Form der Zählung. Sie beantwortet die Frage: „Wie oft kommt dieser Wert vor?"

> [!example] Beispiel
> Würfelergebnisse: 3, 1, 4, 3, 2, 3, 5, 3, 6, 2
> 
> - Absolute Häufigkeit der 3: $H(3) = 4$ (die 3 kommt 4-mal vor)
> - Absolute Häufigkeit der 1: $H(1) = 1$
> - Absolute Häufigkeit der 7: $H(7) = 0$ (kommt nicht vor)

### Eigenschaften der absoluten Häufigkeit

- Sie ist immer eine **ganze Zahl** (0, 1, 2, 3, ...)
- Sie ist immer **nicht-negativ** (≥ 0)
- Die **Summe** aller absoluten Häufigkeiten ergibt die Gesamtzahl $n$:
  $$\sum H(x_i) = n$$

## Relative Häufigkeit

> [!note] Definition
> Die **relative Häufigkeit** $h(x)$ gibt den Anteil eines Wertes an der Gesamtzahl an:
> $$h(x) = \frac{H(x)}{n}$$

Die relative Häufigkeit drückt aus, welcher **Anteil** der Gesamtmenge einen bestimmten Wert hat. Sie ist eine Dezimalzahl zwischen 0 und 1 (oder als Prozent zwischen 0% und 100%).

> [!example] Beispiel (Fortsetzung)
> Bei $n = 10$ Würfen:
> $$h(3) = \frac{4}{10} = 0{,}4 = 40\%$$
> 
> Das bedeutet: In 40% aller Würfe wurde eine 3 gewürfelt.

### Eigenschaften der relativen Häufigkeit

- Sie liegt immer zwischen **0 und 1** (bzw. 0% und 100%)
- Die **Summe** aller relativen Häufigkeiten ergibt immer 1 (bzw. 100%):
  $$\sum h(x_i) = 1$$

> [!tip] **Kontrollrechnung**
> Wenn die Summe der relativen Häufigkeiten nicht genau 1 (oder 100%) ergibt, liegt ein Rechenfehler vor oder es wurden Werte vergessen.

## Umrechnung

Die Umrechnung zwischen den verschiedenen Darstellungsformen ist wichtig und wird häufig in Prüfungen abgefragt:

| Von | Nach | Formel | Beispiel |
|----|------|--------|----------|
| Absolut → Relativ | $h = \frac{H}{n}$ | $\frac{4}{10} = 0{,}4$ |
| Relativ → Absolut | $H = h \cdot n$ | $0{,}4 \cdot 10 = 4$ |
| Relativ → Prozent | $p = h \cdot 100\%$ | $0{,}4 \cdot 100\% = 40\%$ |
| Prozent → Relativ | $h = \frac{p}{100\%}$ | $\frac{40\%}{100\%} = 0{,}4$ |

## Beispiel: Klassenarbeit

Ein vollständiges Beispiel mit allen Berechnungen:

| Note | Absolut $H$ | Relativ $h$ | Prozent |
|------|------------:|------------:|--------:|
| 1 | 3 | 0,12 | 12% |
| 2 | 6 | 0,24 | 24% |
| 3 | 8 | 0,32 | 32% |
| 4 | 5 | 0,20 | 20% |
| 5 | 2 | 0,08 | 8% |
| 6 | 1 | 0,04 | 4% |
| **Σ** | **25** | **1,00** | **100%** |

**Rechenweg für Note 3:**
- Absolute Häufigkeit: 8 Schüler haben eine 3
- Relative Häufigkeit: $h(3) = \frac{8}{25} = 0{,}32$
- Als Prozent: $0{,}32 \cdot 100\% = 32\%$

> [!warning] **Häufiger Fehler: Rundungsprobleme**
> Bei der Umrechnung in Prozent können Rundungsdifferenzen auftreten.
> 
> Beispiel: 3 von 7 Schülern = $\frac{3}{7} \approx 0{,}4286 \approx 42{,}86\%$
> 
> Rundest du alle sieben Anteile, ergibt die Summe möglicherweise nicht exakt 100%. Das ist normal und kein Fehler – aber notiere die Rundung!

> [!tip] **Kontrolle**
> Die Summe der relativen Häufigkeiten muss 1 (bzw. 100%) ergeben. Nutze diese Eigenschaft zur Kontrolle deiner Berechnungen!

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[03-Tabellen|Tabellen]] – Häufigkeiten in Tabellen darstellen
- → [[05-Balkendiagramme|Balkendiagramme]] – Häufigkeiten visualisieren
- → [[06-Kreisdiagramme|Kreisdiagramme]] – Relative Häufigkeiten als Tortenstücke
- → [[../14-Wahrscheinlichkeitsrechnung/04-Haeufigkeit-und-Wahrscheinlichkeit|Wahrscheinlichkeit]] – Relative Häufigkeit als Schätzung für Wahrscheinlichkeit

> [!warning] **Prüfungsrelevant**
> - Formeln für absolute und relative Häufigkeit
> - Umrechnung zwischen absolut, relativ und Prozent
> - Kontrollsumme: $\sum h = 1$ (bzw. 100%)

---

**Navigation:** [[03-Tabellen|← Tabellen]] | [[05-Balkendiagramme|Balkendiagramme →]]
