---
author: Andreas Hümmer
title: Stichproben
tags:
  - content
  - mathe
  - statistik
  - stichprobe
  - grundgesamtheit
created: 2025-06-26
modified: 2025-06-26
---

# Stichproben

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Unterschied zwischen Stichprobe und Grundgesamtheit erklären können
> - Verschiedene Stichprobenverfahren kennen und bewerten können
> - Die Begriffe Repräsentativität und Zufallsstichprobe verstehen
> - Stichprobenfehler von systematischen Fehlern unterscheiden können

---

## Überblick

In der Praxis ist es oft unmöglich oder zu aufwändig, alle Elemente einer Grundgesamtheit zu untersuchen. Stattdessen wird eine **Stichprobe** gezogen – eine Teilmenge, aus der Rückschlüsse auf die gesamte Population gezogen werden. Die Qualität dieser Rückschlüsse hängt entscheidend davon ab, wie die Stichprobe ausgewählt wird.

---

## Grundbegriffe

### Grundgesamtheit und Stichprobe

| Begriff | Definition | Beispiel |
|---------|------------|----------|
| **Grundgesamtheit** (Population) | Menge aller statistischen Einheiten, über die eine Aussage getroffen werden soll | Alle wahlberechtigten Deutschen |
| **Stichprobe** (Sample) | Ausgewählte Teilmenge der Grundgesamtheit | 1000 befragte Wähler |
| **Stichprobenumfang** $n$ | Anzahl der Elemente in der Stichprobe | $n = 1000$ |
| **Parameter** | Kenngröße der Grundgesamtheit (meist unbekannt) | Wahrer Stimmenanteil $p$ |
| **Schätzer/Statistik** | Aus der Stichprobe berechnete Kenngröße | Beobachteter Anteil $\hat{p}$ |

### Notation

- Grundgesamtheit: Parameter werden mit griechischen Buchstaben bezeichnet
  - Mittelwert: $\mu$
  - Standardabweichung: $\sigma$
  - Anteil: $p$
  
- Stichprobe: Statistiken werden mit lateinischen Buchstaben bezeichnet
  - Stichprobenmittel: $\bar{x}$
  - Stichprobenstandardabweichung: $s$
  - Stichprobenanteil: $\hat{p}$

---

## Arten von Stichproben

### Zufallsstichprobe (Wahrscheinlichkeitsstichprobe)

Bei einer **Zufallsstichprobe** hat jedes Element der Grundgesamtheit eine berechenbare, von null verschiedene Wahrscheinlichkeit, ausgewählt zu werden.

**Einfache Zufallsstichprobe:**
- Jedes Element hat die gleiche Auswahlwahrscheinlichkeit $\frac{1}{N}$
- Die Auswahl eines Elements beeinflusst nicht die Auswahl anderer
- Realisierung z.B. durch Losverfahren oder Zufallszahlengenerator

**Ziehen mit und ohne Zurücklegen:**

| Verfahren | Beschreibung | Wahrscheinlichkeit für Auswahl |
|-----------|--------------|-------------------------------|
| Mit Zurücklegen | Element kann mehrfach gezogen werden | Bleibt konstant: $\frac{1}{N}$ |
| Ohne Zurücklegen | Jedes Element höchstens einmal | Ändert sich: $\frac{1}{N}, \frac{1}{N-1}, \ldots$ |

Bei großen Grundgesamtheiten ($N \gg n$) ist der Unterschied vernachlässigbar.

**Geschichtete Stichprobe:**
- Grundgesamtheit wird in homogene Schichten (Strata) unterteilt
- Aus jeder Schicht wird eine Zufallsstichprobe gezogen
- Vorteil: Höhere Präzision bei heterogenen Populationen

**Klumpenstichprobe:**
- Grundgesamtheit wird in Gruppen (Klumpen) unterteilt
- Einige Klumpen werden zufällig ausgewählt und vollständig untersucht
- Vorteil: Kosteneffizienter bei räumlich verteilten Populationen

### Nicht-Zufallsstichproben

Bei **nicht-zufälligen Stichproben** ist die Auswahlwahrscheinlichkeit nicht bekannt. Statistische Schlüsse sind dann nur eingeschränkt möglich.

**Beispiele:**
- **Willkürliche Stichprobe**: Auswahl nach Belieben des Untersuchers
- **Quotenstichprobe**: Vorgegebene Quoten für bestimmte Merkmale
- **Selbstselektion**: Freiwillige Teilnahme (z.B. Online-Umfragen)

---

## Repräsentativität

Eine Stichprobe ist **repräsentativ**, wenn sie die Grundgesamtheit in Bezug auf die untersuchten Merkmale widerspiegelt.

### Bedingungen für Repräsentativität

1. **Zufällige Auswahl**: Vermeidet systematische Verzerrungen
2. **Ausreichender Umfang**: Reduziert den Stichprobenfehler
3. **Korrekte Definition der Grundgesamtheit**: Was genau wird untersucht?

### Verzerrungen (Bias)

**Auswahlverzerrung (Selection Bias):**
- Bestimmte Gruppen sind über- oder unterrepräsentiert
- Beispiel: Telefonumfragen erreichen Menschen ohne Festnetz nicht

**Antwortverzerrung (Response Bias):**
- Systematisch verfälschte Antworten
- Beispiel: Sozial erwünschte Antworten bei sensiblen Fragen

**Ausfallverzerrung (Non-Response Bias):**
- Nicht-Teilnehmer unterscheiden sich systematisch von Teilnehmern
- Beispiel: Berufstätige sind tagsüber schwerer erreichbar

---

## Der Stichprobenfehler

### Zufallsfehler vs. systematischer Fehler

| Fehlerart | Ursache | Reduzierung |
|-----------|---------|-------------|
| **Zufallsfehler** | Zufällige Schwankungen durch Stichprobenauswahl | Größerer Stichprobenumfang |
| **Systematischer Fehler** | Verzerrung im Auswahlverfahren | Besseres Studiendesign |

Der **Stichprobenfehler** beschreibt die Abweichung zwischen Stichprobenstatistik und wahrem Parameter aufgrund der zufälligen Auswahl.

### Standardfehler

Der **Standardfehler** (SE) ist die Standardabweichung einer Stichprobenstatistik:

**Standardfehler des Mittelwerts:**

$$\text{SE}(\bar{x}) = \frac{\sigma}{\sqrt{n}} \approx \frac{s}{\sqrt{n}}$$

**Standardfehler des Anteils:**

$$\text{SE}(\hat{p}) = \sqrt{\frac{p(1-p)}{n}} \approx \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$

> [!note] **Gesetz der großen Zahlen**
> Mit wachsendem Stichprobenumfang $n$ nähert sich der Stichprobenmittelwert $\bar{x}$ dem wahren Mittelwert $\mu$ der Grundgesamtheit an. Der Standardfehler sinkt proportional zu $\frac{1}{\sqrt{n}}$.

### Beispiel: Wahlumfrage

Eine Wahlumfrage mit $n = 1000$ Befragten ergibt $\hat{p} = 0{,}35$ (35% Zustimmung).

Standardfehler:
$$\text{SE}(\hat{p}) = \sqrt{\frac{0{,}35 \cdot 0{,}65}{1000}} = \sqrt{\frac{0{,}2275}{1000}} \approx 0{,}015 = 1{,}5\%$$

Das Ergebnis hat eine Unsicherheit von etwa $\pm 1{,}5$ Prozentpunkten.

---

## Stichprobenumfang bestimmen

Die benötigte Stichprobengröße hängt ab von:

1. **Gewünschte Genauigkeit** (maximal akzeptierter Fehler $e$)
2. **Konfidenzniveau** (z.B. 95% → $z = 1{,}96$)
3. **Erwartete Variabilität** ($\sigma$ oder $p$)

**Formel für Anteilsschätzung:**

$$n \geq \frac{z^2 \cdot p(1-p)}{e^2}$$

Bei unbekanntem $p$ setzt man $p = 0{,}5$ (maximale Varianz).

**Beispiel:** Für eine Genauigkeit von $\pm 3\%$ bei 95% Konfidenz:

$$n \geq \frac{1{,}96^2 \cdot 0{,}5 \cdot 0{,}5}{0{,}03^2} = \frac{0{,}9604}{0{,}0009} \approx 1068$$

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Deskriptive-Statistik]] – Beschreibung der Stichprobendaten
- → [[Schaetzverfahren]] – Von der Stichprobe zum Parameter
- → [[Konfidenzintervalle-Grundlagen]] – Intervallschätzung mit Stichprobendaten
- → [[Binomialverteilung]] – Verteilung bei dichotomen Merkmalen
- → [[Normalverteilung]] – Verteilung von Stichprobenmittelwerten

> [!warning] **Prüfungsrelevant**
> - Unterscheidung Grundgesamtheit/Stichprobe und Parameter/Statistik
> - Berechnung des Standardfehlers für Anteile und Mittelwerte
> - Zusammenhang zwischen Stichprobenumfang und Genauigkeit
> - Erkennen von Verzerrungen in Studiendesigns
> - Gesetz der großen Zahlen als Grundlage für Stichprobenverfahren

> [!question] **Typische Prüfungsfragen**
> - Eine Wahlumfrage mit $n = 500$ ergibt 42% Zustimmung. Berechne den Standardfehler.
> - Erkläre, warum eine Online-Umfrage auf einer Nachrichten-Website möglicherweise nicht repräsentativ ist.
> - Wie groß muss eine Stichprobe sein, um den Anteil auf $\pm 2\%$ genau zu schätzen?

---

## Quellen

- Fahrmeir, L. et al.: Statistik – Der Weg zur Datenanalyse. Springer, 2016.
- Bortz, J. & Schuster, C.: Statistik für Human- und Sozialwissenschaftler. Springer, 2010.
- ISB Bayern: Abiturprüfungen Mathematik.

> [!tip] **Weiterführende Links**
> - [[Konfidenzintervalle-Grundlagen]] – Wie der Standardfehler in Intervallschätzungen eingeht
> - [[Nullhypothese-und-Alternativhypothese]] – Stichproben in Hypothesentests
