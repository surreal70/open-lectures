---
author: Andreas Hümmer
title: Änderungsraten
tags:
  - content
  - mathe
  - differentialrechnung
  - aenderungsrate
  - analysis
created: 2026-10-17
modified: 2026-10-17
---

# Änderungsraten

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das Konzept der Änderungsrate als fundamentale Idee der Differentialrechnung verstehen
> - Änderungsraten in verschiedenen Kontexten (Physik, Wirtschaft, Biologie) erkennen und interpretieren können
> - Den Unterschied zwischen absoluter und relativer Änderung erklären können
> - Die Verbindung zwischen Änderungsraten und Steigung von Funktionsgraphen herstellen können

---

## Überblick

Änderungsraten beschreiben, wie sich eine Größe in Abhängigkeit von einer anderen Größe verändert. Dieses Konzept begegnet uns überall im Alltag: Die Geschwindigkeit eines Autos gibt an, wie sich der Ort in Abhängigkeit von der Zeit ändert. Der Benzinverbrauch beschreibt, wie sich der Tankinhalt in Abhängigkeit von der gefahrenen Strecke ändert. Die Inflationsrate zeigt, wie sich das Preisniveau in Abhängigkeit von der Zeit entwickelt.

Die mathematische Erfassung von Änderungsraten ist der Ausgangspunkt für die gesamte Differentialrechnung. Sie bildet die Brücke zwischen anschaulichen, alltäglichen Phänomenen und der präzisen mathematischen Theorie der Ableitung.

## Der Begriff der Änderung

### Absolute Änderung

Die **absolute Änderung** einer Größe $y$ beschreibt die Differenz zwischen zwei Werten:

$$\Delta y = y_2 - y_1$$

Das Symbol $\Delta$ (griechischer Buchstabe Delta) steht dabei für "Differenz" oder "Änderung".

**Beispiel:** Ein Aktienkurs steigt von 80 € auf 92 €.
- Absolute Änderung: $\Delta y = 92\,\text{€} - 80\,\text{€} = 12\,\text{€}$

### Relative Änderung

Die **relative Änderung** setzt die absolute Änderung ins Verhältnis zum Ausgangswert:

$$\text{relative Änderung} = \frac{\Delta y}{y_1} = \frac{y_2 - y_1}{y_1}$$

Oft wird diese als Prozentwert angegeben.

**Beispiel (Fortsetzung):**
- Relative Änderung: $\frac{12\,\text{€}}{80\,\text{€}} = 0{,}15 = 15\,\%$

## Von der Änderung zur Änderungsrate

Wenn wir nicht nur wissen wollen, *dass* sich etwas ändert, sondern *wie schnell*, benötigen wir eine **Änderungsrate**. Sie setzt die Änderung einer Größe $y$ ins Verhältnis zur Änderung einer anderen Größe $x$:

$$\text{Änderungsrate} = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1}$$

### Interpretation

Die Änderungsrate gibt an, um wie viele Einheiten sich $y$ ändert, wenn sich $x$ um eine Einheit ändert.

**Einheiten:** Die Einheit der Änderungsrate ergibt sich aus dem Quotienten der Einheiten:
$$[\text{Änderungsrate}] = \frac{[y]}{[x]}$$

## Beispiele aus verschiedenen Anwendungsbereichen

### Physik: Geschwindigkeit

Die Geschwindigkeit ist die Änderungsrate des Ortes bezüglich der Zeit:

$$v = \frac{\Delta s}{\Delta t} = \frac{s_2 - s_1}{t_2 - t_1}$$

- **Einheit:** $\frac{\text{m}}{\text{s}}$ oder $\frac{\text{km}}{\text{h}}$
- **Interpretation:** Zurückgelegte Strecke pro Zeiteinheit

**Beispiel:** Ein Auto fährt in 2 Stunden von Kilometer 50 nach Kilometer 170.
$$v = \frac{170\,\text{km} - 50\,\text{km}}{2\,\text{h}} = \frac{120\,\text{km}}{2\,\text{h}} = 60\,\frac{\text{km}}{\text{h}}$$

### Wirtschaft: Grenzkosten

Die Kostenänderungsrate beschreibt, wie sich die Gesamtkosten bei Änderung der Produktionsmenge ändern:

$$\frac{\Delta K}{\Delta x} = \frac{K(x_2) - K(x_1)}{x_2 - x_1}$$

**Beispiel:** Die Produktionskosten steigen von 5000 € bei 100 Stück auf 6200 € bei 120 Stück.
$$\frac{\Delta K}{\Delta x} = \frac{6200\,\text{€} - 5000\,\text{€}}{120 - 100} = \frac{1200\,\text{€}}{20} = 60\,\frac{\text{€}}{\text{Stück}}$$

### Biologie: Wachstumsrate

Die Wachstumsrate einer Population beschreibt die Änderung der Individuenzahl pro Zeiteinheit:

$$\frac{\Delta N}{\Delta t} = \frac{N_2 - N_1}{t_2 - t_1}$$

**Beispiel:** Eine Bakterienkultur wächst von 1000 auf 2500 Bakterien in 4 Stunden.
$$\frac{\Delta N}{\Delta t} = \frac{2500 - 1000}{4\,\text{h}} = 375\,\frac{\text{Bakterien}}{\text{h}}$$

## Änderungsrate und Funktionsgraph

Gegeben sei eine Funktion $f$ mit dem Graphen $G_f$. Betrachten wir zwei Punkte $P(x_1 | f(x_1))$ und $Q(x_2 | f(x_2))$ auf dem Graphen.

Die Änderungsrate zwischen diesen Punkten ist:

$$\frac{\Delta y}{\Delta x} = \frac{f(x_2) - f(x_1)}{x_2 - x_1}$$

**Geometrische Interpretation:** Diese Änderungsrate entspricht der **Steigung der Sekante** durch die Punkte $P$ und $Q$.

```
      y
      |           Q
      |          /
      |         / Sekante
      |        /
      |    P  /
      |   ---/---
      |
      +----------------> x
```

Die Verbindungsgerade zwischen zwei Punkten eines Graphen heißt **Sekante** (von lat. *secare* = schneiden).

## Die zentrale Fragestellung

Die bisherigen Betrachtungen liefern immer nur eine **durchschnittliche** Änderungsrate über ein Intervall $[x_1, x_2]$. In vielen Anwendungen interessiert uns jedoch die **momentane** Änderungsrate an einem bestimmten Punkt:

- Wie schnell fährt das Auto *genau jetzt* (nicht im Durchschnitt der letzten Stunde)?
- Wie schnell wächst die Population *in diesem Moment*?
- Wie steil ist der Graph *an dieser Stelle*?

Diese Frage führt uns zum Konzept der [[Momentane-aenderungsrate|momentanen Änderungsrate]] und damit zur Ableitung.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Durchschnittliche-aenderungsrate|Durchschnittliche Änderungsrate]] – Vertiefung und formale Definition
- → [[Momentane-aenderungsrate|Momentane Änderungsrate]] – Der Übergang zum Grenzwert
- → [[Differenzenquotient|Differenzenquotient]] – Mathematische Formalisierung
- → [[Grenzwerte-von-Funktionen|Grenzwerte von Funktionen]] – Voraussetzung für den Grenzübergang
- → [[Lineare-Funktionen|Lineare Funktionen]] – Konstante Änderungsrate

> [!warning] **Prüfungsrelevant**
> - Das Konzept der Änderungsrate muss in Sachkontexten sicher angewendet werden können
> - Einheiten müssen korrekt angegeben und interpretiert werden
> - Der Zusammenhang zwischen Änderungsrate und Sekantensteigung ist fundamental wichtig
> - Die Unterscheidung zwischen durchschnittlicher und momentaner Änderungsrate ist essentiell

> [!question] **Typische Prüfungsfragen**
> - "Interpretieren Sie die Änderungsrate im Sachkontext."
> - "Berechnen Sie die durchschnittliche Änderungsrate der Funktion $f$ im Intervall $[a, b]$ und erläutern Sie deren Bedeutung."
> - "Erklären Sie den Zusammenhang zwischen der Änderungsrate und der Steigung der Sekante."

## Quellen

- Griesel, H., Postel, H., Suhr, F. (2019): *Elemente der Mathematik – Qualifikationsphase*. Schroedel Verlag.
- Büchter, A., Henn, H.-W. (2015): *Elementare Analysis*. Springer Spektrum.
- Papula, L. (2018): *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1. Springer Vieweg.

> [!tip] **Weiterführende Links**
> - [[Differentialquotient|Differentialquotient]] – Der nächste Schritt zur Ableitung
> - [[Wachstumsprozesse|Wachstumsprozesse]] – Anwendung von Änderungsraten in der Modellierung
