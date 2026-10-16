---
author: Open Lectures
title: Natürliche Zahlen
status: draft - review pending
tags:
  - content
  - mathematik
  - zahlenmengen
  - natuerliche-zahlen
created: 2026-10-13
modified: 2026-10-13
---

# Natürliche Zahlen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Menge der natürlichen Zahlen $\mathbb{N}$ definieren können
> - Natürliche Zahlen auf dem Zahlenstrahl darstellen können
> - Eigenschaften natürlicher Zahlen kennen (Nachfolger, Vorgänger)
> - Das Dezimalsystem und Stellenwertsystem verstehen

---

## Überblick

Die natürlichen Zahlen sind die ältesten und grundlegendsten Zahlen der Mathematik. Sie entstanden aus dem Bedürfnis des Menschen zu zählen: Menschen, Tiere, Gegenstände. Die natürlichen Zahlen bilden das Fundament, auf dem alle anderen Zahlenmengen aufgebaut werden.

---

## Definition der natürlichen Zahlen

Die **natürlichen Zahlen** sind die Zahlen, die wir zum Zählen verwenden:

$$\mathbb{N} = \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, \ldots\}$$

Die drei Punkte ($\ldots$) bedeuten, dass die Folge unendlich weitergeht.

> [!note] **Variante mit Null**
> In manchen Definitionen gehört die Null zu den natürlichen Zahlen. Man schreibt dann:
> $$\mathbb{N}_0 = \{0, 1, 2, 3, 4, 5, \ldots\}$$
> In diesem Kurs verwenden wir $\mathbb{N}$ ohne Null und $\mathbb{N}_0$ mit Null.

---

## Eigenschaften natürlicher Zahlen

### Nachfolger und Vorgänger

Jede natürliche Zahl hat einen **Nachfolger** (die nächstgrößere Zahl):

| Zahl | Nachfolger |
|------|------------|
| 1 | 2 |
| 5 | 6 |
| 99 | 100 |
| $n$ | $n + 1$ |

Jede natürliche Zahl außer 1 hat einen **Vorgänger** (die nächstkleinere Zahl):

| Zahl | Vorgänger |
|------|-----------|
| 2 | 1 |
| 5 | 4 |
| 100 | 99 |
| $n$ | $n - 1$ |

> [!warning] **Achtung**
> Die Zahl 1 hat keinen Vorgänger in $\mathbb{N}$, denn 0 gehört nicht zu $\mathbb{N}$.

### Weitere Eigenschaften

- **Kleinste natürliche Zahl**: 1 (bzw. 0 bei $\mathbb{N}_0$)
- **Größte natürliche Zahl**: Es gibt keine! $\mathbb{N}$ ist unendlich.
- **Ordnung**: Natürliche Zahlen lassen sich der Größe nach ordnen: $1 < 2 < 3 < 4 < \ldots$

---

## Das Dezimalsystem

Wir verwenden das **Dezimalsystem** (Zehnersystem), das auf den Ziffern 0–9 basiert.

### Stellenwertsystem

Der Wert einer Ziffer hängt von ihrer Position (Stelle) ab:

| Stelle | Name | Wert |
|--------|------|------|
| 1. von rechts | Einer | $10^0 = 1$ |
| 2. von rechts | Zehner | $10^1 = 10$ |
| 3. von rechts | Hunderter | $10^2 = 100$ |
| 4. von rechts | Tausender | $10^3 = 1000$ |
| 5. von rechts | Zehntausender | $10^4 = 10\,000$ |

**Beispiel:** Die Zahl 3742

$$3742 = 3 \cdot 1000 + 7 \cdot 100 + 4 \cdot 10 + 2 \cdot 1$$

```
Tausender  Hunderter  Zehner  Einer
    3          7         4       2
    ↓          ↓         ↓       ↓
  3×1000    7×100     4×10     2×1
  = 3000   = 700     = 40     = 2
                              ------
                        Summe: 3742
```

---

## Darstellung auf dem Zahlenstrahl

Natürliche Zahlen lassen sich auf einem Zahlenstrahl darstellen:

```
    ←──┬────┬────┬────┬────┬────┬────┬────┬────┬────┬──→
       1    2    3    4    5    6    7    8    9   10  ...
```

Der Zahlenstrahl zeigt:
- Die Zahlen sind **gleichmäßig** verteilt
- Größere Zahlen liegen weiter **rechts**
- Der Strahl geht nach rechts **unendlich** weiter

---

## Gerade und ungerade Zahlen

Natürliche Zahlen lassen sich in zwei Gruppen einteilen:

### Gerade Zahlen
Zahlen, die durch 2 teilbar sind:
$$2, 4, 6, 8, 10, 12, 14, \ldots$$

Allgemein: $2n$ für $n \in \mathbb{N}$

### Ungerade Zahlen
Zahlen, die nicht durch 2 teilbar sind:
$$1, 3, 5, 7, 9, 11, 13, \ldots$$

Allgemein: $2n - 1$ für $n \in \mathbb{N}$

| Eigenschaft | Gerade Zahlen | Ungerade Zahlen |
|-------------|---------------|-----------------|
| Endziffer | 0, 2, 4, 6, 8 | 1, 3, 5, 7, 9 |
| Teilbar durch 2 | Ja | Nein |
| Beispiele | 24, 106, 5000 | 37, 501, 999 |

---

## Rechenoperationen mit natürlichen Zahlen

### Abgeschlossenheit

| Operation | Abgeschlossen in $\mathbb{N}$? | Begründung |
|-----------|--------------------------------|------------|
| Addition | ✓ Ja | $3 + 5 = 8 \in \mathbb{N}$ |
| Multiplikation | ✓ Ja | $3 \cdot 5 = 15 \in \mathbb{N}$ |
| Subtraktion | ✗ Nein | $3 - 5 = -2 \notin \mathbb{N}$ |
| Division | ✗ Nein | $5 : 3 = 1{,}\overline{6} \notin \mathbb{N}$ |

> [!note] **Erklärung**
> „Abgeschlossen" bedeutet: Das Ergebnis der Operation liegt wieder in derselben Zahlenmenge. Bei Subtraktion und Division kann das Ergebnis außerhalb von $\mathbb{N}$ liegen – deshalb brauchen wir weitere Zahlenmengen!

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[02-Mathematische-Symbole|Mathematische Symbole]] – Die Notation $\mathbb{N}$
- → [[04-Ganze-Zahlen|Ganze Zahlen]] – Erweiterung um negative Zahlen
- → [[07-Zahlenstrahl-und-Zahlenmengen|Zahlenstrahl]] – Visualisierung aller Zahlenmengen
- → [[08-Positive-und-negative-Zahlen|Positive und negative Zahlen]] – Vorzeichen

> [!warning] **Prüfungsrelevant**
> - Definition: $\mathbb{N} = \{1, 2, 3, \ldots\}$
> - Unterschied zwischen $\mathbb{N}$ und $\mathbb{N}_0$
> - Stellenwertsystem: Einer, Zehner, Hunderter, ...
> - Abgeschlossenheit: Addition und Multiplikation ja, Subtraktion und Division nein

> [!question] **Typische Prüfungsfragen**
> - Was ist der Nachfolger von 999?
> - Ist $0 \in \mathbb{N}$? Begründe.
> - Zerlege 4527 nach Stellenwerten.
> - Warum ist die Subtraktion in $\mathbb{N}$ nicht abgeschlossen?

## Quellen

- Barner, Martin; Flohr, Friedrich: *Analysis I*. De Gruyter, 2000.
- Beutelspacher, Albrecht: *Zahlen*. Rowohlt, 2013.

> [!tip] **Weiterführende Links**
> - [Mathebibel: Natürliche Zahlen](https://www.mathebibel.de/natuerliche-zahlen)
> - [[04-Ganze-Zahlen|Nächstes Kapitel: Ganze Zahlen]]
