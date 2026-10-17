---
author: Andreas Hümmer
title: Unendliche geometrische Reihen
tags:
  - content
  - mathe
  - reihen
  - geometrische-reihe
  - konvergenz
  - analysis
created: 2025-06-17
modified: 2025-06-17
---

# Unendliche geometrische Reihen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Zusammenhang zwischen geometrischen Folgen und Reihen verstehen
> - Das Konvergenzkriterium für geometrische Reihen kennen
> - Die Summenformel für unendliche geometrische Reihen anwenden können
> - Praktische Anwendungen wie periodische Dezimalzahlen lösen können
> - Den Grenzwert der Partialsummenfolge bestimmen können

---

## Überblick

Eine **unendliche geometrische Reihe** ist die Summe unendlich vieler Glieder einer geometrischen Folge. Während es zunächst paradox erscheint, dass eine Summe unendlich vieler positiver Zahlen endlich sein kann, zeigt die geometrische Reihe genau dieses faszinierende Phänomen – vorausgesetzt, die Glieder werden schnell genug klein.

Geometrische Reihen haben vielfältige Anwendungen: von der Zinseszinsrechnung über die Darstellung periodischer Dezimalzahlen bis hin zur Analyse von Dämpfungsprozessen.

## Von der Folge zur Reihe

### Geometrische Folge (Wiederholung)

$$a_n = a_1 \cdot q^{n-1}$$

### Partialsummen

Die **Partialsumme** $S_n$ ist die Summe der ersten $n$ Glieder:

$$S_n = a_1 + a_1 q + a_1 q^2 + \ldots + a_1 q^{n-1} = \sum_{k=0}^{n-1} a_1 q^k$$

Mit der bekannten Summenformel (für $q \neq 1$):

$$S_n = a_1 \cdot \frac{1 - q^n}{1 - q}$$

### Unendliche Reihe

Die **unendliche geometrische Reihe** ist der Grenzwert der Partialsummen:

$$S = \lim_{n \to \infty} S_n = \sum_{k=0}^{\infty} a_1 q^k$$

## Konvergenzkriterium

### Satz

Die unendliche geometrische Reihe $\sum_{k=0}^{\infty} a_1 q^k$ konvergiert genau dann, wenn $|q| < 1$.

**Beweis:**

Für $|q| < 1$ gilt $\lim_{n \to \infty} q^n = 0$, also:

$$S = \lim_{n \to \infty} a_1 \cdot \frac{1 - q^n}{1 - q} = a_1 \cdot \frac{1 - 0}{1 - q} = \frac{a_1}{1 - q}$$

Für $|q| \geq 1$ divergiert die Reihe, da $q^n$ nicht gegen 0 konvergiert.

### Die Summenformel

$$\boxed{\sum_{k=0}^{\infty} a_1 q^k = \frac{a_1}{1 - q} \quad \text{für } |q| < 1}$$

**Alternative Schreibweise** (beginnend bei $k=1$):

$$\sum_{k=1}^{\infty} a_1 q^{k-1} = \frac{a_1}{1 - q}$$

## Übersicht: Konvergenzverhalten

| Bedingung | Verhalten | Summe |
|-----------|-----------|-------|
| $\|q\| < 1$ | konvergent | $\frac{a_1}{1-q}$ |
| $q = 1$ | divergent | $+\infty$ (für $a_1 > 0$) |
| $q = -1$ | divergent | oszillierend |
| $\|q\| > 1$ | divergent | $\pm\infty$ |

## Berechnungsbeispiele

### Beispiel 1: Standardreihe

$$\sum_{k=0}^{\infty} \left(\frac{1}{2}\right)^k = 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \ldots$$

Mit $a_1 = 1$ und $q = \frac{1}{2}$:

$$S = \frac{1}{1 - \frac{1}{2}} = \frac{1}{\frac{1}{2}} = 2$$

**Anschaulich:** Halbiere einen Kuchen immer wieder – die Gesamtmenge aller Stücke ergibt den ganzen Kuchen plus noch einen.

### Beispiel 2: Reihe mit anderem Startindex

$$\sum_{k=2}^{\infty} 3 \cdot \left(\frac{1}{4}\right)^k = 3 \cdot \frac{1}{16} + 3 \cdot \frac{1}{64} + \ldots$$

Das erste Glied der Reihe ist $a = 3 \cdot \left(\frac{1}{4}\right)^2 = \frac{3}{16}$:

$$S = \frac{\frac{3}{16}}{1 - \frac{1}{4}} = \frac{\frac{3}{16}}{\frac{3}{4}} = \frac{3}{16} \cdot \frac{4}{3} = \frac{1}{4}$$

### Beispiel 3: Alternierende Reihe

$$\sum_{k=0}^{\infty} \left(-\frac{1}{3}\right)^k = 1 - \frac{1}{3} + \frac{1}{9} - \frac{1}{27} + \ldots$$

Mit $a_1 = 1$ und $q = -\frac{1}{3}$:

$$S = \frac{1}{1 - (-\frac{1}{3})} = \frac{1}{\frac{4}{3}} = \frac{3}{4}$$

## Anwendung: Periodische Dezimalzahlen

### Satz

Jede periodische Dezimalzahl lässt sich als Bruch (rationale Zahl) darstellen.

### Beispiel: $0,\overline{3} = 0,333...$

$$0,\overline{3} = 0,3 + 0,03 + 0,003 + \ldots = \frac{3}{10} + \frac{3}{100} + \frac{3}{1000} + \ldots$$

Dies ist eine geometrische Reihe mit $a_1 = \frac{3}{10}$ und $q = \frac{1}{10}$:

$$0,\overline{3} = \frac{\frac{3}{10}}{1 - \frac{1}{10}} = \frac{\frac{3}{10}}{\frac{9}{10}} = \frac{3}{9} = \frac{1}{3}$$

### Beispiel: $0,\overline{12} = 0,121212...$

$$0,\overline{12} = \frac{12}{100} + \frac{12}{10000} + \frac{12}{1000000} + \ldots$$

Mit $a_1 = \frac{12}{100}$ und $q = \frac{1}{100}$:

$$0,\overline{12} = \frac{\frac{12}{100}}{1 - \frac{1}{100}} = \frac{\frac{12}{100}}{\frac{99}{100}} = \frac{12}{99} = \frac{4}{33}$$

## Anwendung: Zinseszins und Rentenrechnung

### Ewige Rente

Eine **ewige Rente** zahlt jährlich einen festen Betrag $R$, beginnend in einem Jahr. Bei Zinssatz $i$ ist der Barwert:

$$PV = \frac{R}{1+i} + \frac{R}{(1+i)^2} + \frac{R}{(1+i)^3} + \ldots$$

Mit $a_1 = \frac{R}{1+i}$ und $q = \frac{1}{1+i}$:

$$PV = \frac{\frac{R}{1+i}}{1 - \frac{1}{1+i}} = \frac{\frac{R}{1+i}}{\frac{i}{1+i}} = \frac{R}{i}$$

**Beispiel:** Eine ewige Rente von 1.000 € pro Jahr bei 5% Zinsen hat den Barwert:

$$PV = \frac{1000}{0,05} = 20.000 \text{ €}$$

## Anwendung: Zenons Paradoxon

Achilles läuft mit 10 m/s, die Schildkröte mit 1 m/s. Die Schildkröte startet 10 m voraus.

**Paradoxon:** Achilles erreicht die Startposition → Schildkröte ist 1 m weiter → Achilles erreicht diese → usw.

**Auflösung:** Die Gesamtstrecke bis zum Einholen:

$$s = 10 + 1 + 0,1 + 0,01 + \ldots = \sum_{k=0}^{\infty} 10 \cdot \left(\frac{1}{10}\right)^k = \frac{10}{1 - 0,1} = \frac{10}{0,9} = \frac{100}{9} \approx 11,11 \text{ m}$$

Die unendlich vielen "Etappen" summieren sich zu einer endlichen Strecke!

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Geometrische-Folgen]] – Grundlage: Die geometrische Folge
- → [[Konvergenz]] – Wann konvergiert eine Reihe?
- → [[Grenzwerte-von-Folgen]] – Grenzwert der Partialsummenfolge
- → [[Wachstumsprozesse]] – Anwendungen in der Modellierung
- → [[Exponentialfunktionen]] – Kontinuierliches Pendant

> [!warning] **Prüfungsrelevant**
> - Die Summenformel $S = \frac{a_1}{1-q}$ für $|q| < 1$ ist Standardwissen
> - Konvergenzbedingung $|q| < 1$ muss bekannt sein
> - Umwandlung periodischer Dezimalzahlen in Brüche ist ein Klassiker
> - Anwendungen im Kontext (Zins, Physik) werden gerne gestellt
> - Vorsicht beim Startindex: Erstes Glied $a_1$ richtig bestimmen!

> [!question] **Typische Prüfungsfragen**
> - Berechne $\sum_{k=1}^{\infty} 2 \cdot \left(\frac{2}{3}\right)^k$.
> - Stelle $0,\overline{27}$ als gekürzten Bruch dar.
> - Ein Ball fällt aus 1 m Höhe und springt jeweils auf 80% der vorherigen Höhe zurück. Welche Gesamtstrecke legt er zurück?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I. N. et al.: Taschenbuch der Mathematik. Europa-Lehrmittel, 2020.
- Tietze, J.: Einführung in die angewandte Wirtschaftsmathematik. Springer Spektrum, 2019.

> [!tip] **Weiterführende Links**
> - [[Einfuehrung-in-die-mathematische-Grenzwertbildung]] – Formale Beweise für Reihenkonvergenz
> - [[Logarithmusfunktionen]] – Für Berechnungen mit Exponenten
