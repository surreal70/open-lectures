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

Schon vor Zehntausenden von Jahren ritzten Menschen Kerben in Knochen oder Stöcke, um Dinge zu zählen. Diese einfache Idee – für jedes Objekt ein Zeichen – entwickelte sich über Jahrtausende zu den ausgefeilten Zahlensystemen, die wir heute kennen. Die natürlichen Zahlen sind somit nicht nur mathematische Objekte, sondern auch ein Teil unserer Kulturgeschichte.

---

## Definition der natürlichen Zahlen

Die **natürlichen Zahlen** sind die Zahlen, die wir zum Zählen verwenden:

$$\mathbb{N} = \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, \ldots\}$$

Die drei Punkte ($\ldots$) bedeuten, dass die Folge unendlich weitergeht. Es gibt keine „größte" natürliche Zahl – zu jeder Zahl kann man noch 1 addieren und erhält eine größere.

Das Symbol $\mathbb{N}$ kommt von „natural numbers" (englisch für „natürliche Zahlen"). Der Doppelstrich in der Schreibweise signalisiert, dass es sich um eine besondere Zahlenmenge handelt.

> [!note] **Variante mit Null: Gehört die Null dazu?**
> In der Mathematik gibt es zwei Konventionen, die beide verbreitet sind:
> 
> **Konvention 1 (in Deutschland üblich):** Die Null gehört **nicht** zu $\mathbb{N}$
> $$\mathbb{N} = \{1, 2, 3, 4, 5, \ldots\}$$
> Für die natürlichen Zahlen **mit** Null schreibt man dann: $\mathbb{N}_0 = \{0, 1, 2, 3, 4, 5, \ldots\}$
>
> **Konvention 2 (international):** Die Null gehört zu $\mathbb{N}$
> $$\mathbb{N} = \{0, 1, 2, 3, 4, 5, \ldots\}$$
>
> In diesem Kurs verwenden wir Konvention 1: $\mathbb{N}$ ohne Null und $\mathbb{N}_0$ mit Null.

---

## Eigenschaften natürlicher Zahlen

### Nachfolger und Vorgänger

Ein fundamentales Konzept bei natürlichen Zahlen ist die Idee des **Nachfolgers**: Zu jeder natürlichen Zahl gibt es genau eine nächstgrößere Zahl.

| Zahl | Nachfolger | Wie berechnet? |
|------|------------|----------------|
| 1 | 2 | $1 + 1 = 2$ |
| 5 | 6 | $5 + 1 = 6$ |
| 99 | 100 | $99 + 1 = 100$ |
| $n$ | $n + 1$ | Allgemeine Regel |

Entsprechend hat jede natürliche Zahl (außer 1) einen **Vorgänger** – die nächstkleinere Zahl:

| Zahl | Vorgänger | Wie berechnet? |
|------|-----------|----------------|
| 2 | 1 | $2 - 1 = 1$ |
| 5 | 4 | $5 - 1 = 4$ |
| 100 | 99 | $100 - 1 = 99$ |
| $n$ | $n - 1$ | Allgemeine Regel |

> [!warning] **Achtung: Die 1 hat keinen Vorgänger in $\mathbb{N}$**
> Die Zahl 1 hat keinen Vorgänger in $\mathbb{N}$, denn $1 - 1 = 0$, und 0 gehört nicht zu $\mathbb{N}$ (nach unserer Konvention). Diese Einschränkung war einer der Gründe, warum die Mathematik später die Menge der ganzen Zahlen $\mathbb{Z}$ einführte.

### Weitere wichtige Eigenschaften

| Eigenschaft | Beschreibung | Beispiel |
|-------------|--------------|----------|
| **Kleinste Zahl** | 1 ist die kleinste natürliche Zahl | Es gibt keine natürliche Zahl zwischen 0 und 1 |
| **Keine größte Zahl** | $\mathbb{N}$ ist unendlich | 1.000.000 + 1 ist auch in $\mathbb{N}$ |
| **Ordnung** | Zahlen lassen sich der Größe nach ordnen | $1 < 2 < 3 < 4 < \ldots$ |
| **Diskretheit** | Zwischen zwei aufeinanderfolgenden Zahlen liegt keine weitere | Zwischen 5 und 6 gibt es keine natürliche Zahl |

Die Diskretheit unterscheidet natürliche Zahlen von „dichteren" Zahlenmengen wie den rationalen Zahlen, bei denen zwischen je zwei Zahlen immer noch eine weitere liegt.

---

## Das Dezimalsystem

Wir verwenden das **Dezimalsystem** (Zehnersystem), das auf den Ziffern 0–9 basiert. „Dezimal" kommt vom lateinischen „decem" (zehn). Dieses System ist ein **Stellenwertsystem**, bei dem der Wert einer Ziffer von ihrer Position abhängt.

### Warum ausgerechnet Basis 10?

Die Basis 10 ist vermutlich historisch bedingt: Menschen haben zehn Finger und nutzten diese zum Zählen. Andere Kulturen verwendeten andere Basen:
- Die Maya nutzten Basis 20 (Finger und Zehen)
- Die Babylonier nutzten Basis 60 (daher haben wir 60 Sekunden pro Minute)
- Computer nutzen Basis 2 (Binärsystem: nur 0 und 1)

### Stellenwertsystem

Der Wert einer Ziffer hängt von ihrer Position (Stelle) ab. Jede Stelle hat einen zehnmal größeren Wert als die Stelle rechts davon:

| Stelle | Name | Wert | Als Potenz |
|--------|------|------|------------|
| 1. von rechts | Einer | $1$ | $10^0 = 1$ |
| 2. von rechts | Zehner | $10$ | $10^1 = 10$ |
| 3. von rechts | Hunderter | $100$ | $10^2 = 100$ |
| 4. von rechts | Tausender | $1\,000$ | $10^3 = 1\,000$ |
| 5. von rechts | Zehntausender | $10\,000$ | $10^4 = 10\,000$ |
| 6. von rechts | Hunderttausender | $100\,000$ | $10^5 = 100\,000$ |
| 7. von rechts | Millionen | $1\,000\,000$ | $10^6 = 1\,000\,000$ |

**Detailliertes Beispiel:** Die Zahl 3742 analysieren

$$3742 = 3 \cdot 1000 + 7 \cdot 100 + 4 \cdot 10 + 2 \cdot 1$$

```
Stelle:       Tausender  Hunderter  Zehner  Einer
Ziffer:           3          7         4       2
                  ↓          ↓         ↓       ↓
Berechnung:   3×1000     7×100     4×10     2×1
               = 3000    = 700     = 40     = 2
                                          ──────
                                   Summe:  3742
```

> [!tip] **Merkregel für große Zahlen**
> Große Zahlen werden oft mit Punkten oder Leerzeichen in Dreiergruppen gegliedert (von rechts):
> - 1.000.000 (eine Million)
> - 7 500 000 (7,5 Millionen)
> 
> Dies erleichtert das Lesen und vermeidet Fehler.

---

## Darstellung auf dem Zahlenstrahl

Natürliche Zahlen lassen sich auf einem Zahlenstrahl darstellen. Der Zahlenstrahl ist eine gerade Linie, auf der Zahlen als Punkte markiert werden:

```
    ←──┬────┬────┬────┬────┬────┬────┬────┬────┬────┬──→
       1    2    3    4    5    6    7    8    9   10  ...
```

### Was der Zahlenstrahl zeigt

- **Gleichmäßige Verteilung**: Die Abstände zwischen benachbarten Zahlen sind immer gleich groß
- **Ordnung**: Größere Zahlen liegen weiter rechts, kleinere weiter links
- **Unendlichkeit**: Der Strahl geht nach rechts unendlich weiter (angedeutet durch Pfeil oder $\ldots$)
- **Keine negativen Zahlen**: Der Zahlenstrahl für $\mathbb{N}$ beginnt bei 1 (oder 0 für $\mathbb{N}_0$)

Der Zahlenstrahl macht abstrakte Beziehungen anschaulich: Man „sieht" sofort, dass 7 größer als 3 ist, weil 7 rechts von 3 liegt.

---

## Gerade und ungerade Zahlen

Eine wichtige Einteilung der natürlichen Zahlen unterscheidet zwischen geraden und ungeraden Zahlen. Diese Unterscheidung ist fundamental für viele mathematische Überlegungen.

### Gerade Zahlen

**Definition:** Eine Zahl ist **gerade**, wenn sie durch 2 ohne Rest teilbar ist.

$$\text{Gerade Zahlen: } 2, 4, 6, 8, 10, 12, 14, \ldots$$

Allgemeine Form: $2n$ für $n \in \mathbb{N}$ (also das Doppelte einer natürlichen Zahl)

### Ungerade Zahlen

**Definition:** Eine Zahl ist **ungerade**, wenn sie bei Division durch 2 den Rest 1 lässt.

$$\text{Ungerade Zahlen: } 1, 3, 5, 7, 9, 11, 13, \ldots$$

Allgemeine Form: $2n - 1$ für $n \in \mathbb{N}$

### Schnelle Erkennungsregel

| Eigenschaft | Gerade Zahlen | Ungerade Zahlen |
|-------------|---------------|-----------------|
| **Endziffer** | 0, 2, 4, 6, 8 | 1, 3, 5, 7, 9 |
| **Teilbar durch 2** | Ja | Nein |
| **Rest bei Division durch 2** | 0 | 1 |
| **Beispiele** | 24, 106, 5000, 1234 | 37, 501, 999, 4321 |

> [!tip] **Schnelltest**
> Um zu prüfen, ob eine Zahl gerade oder ungerade ist, musst du nur auf die **letzte Ziffer** schauen:
> - Letzte Ziffer gerade (0, 2, 4, 6, 8) → Zahl ist gerade
> - Letzte Ziffer ungerade (1, 3, 5, 7, 9) → Zahl ist ungerade
>
> **Beispiel:** Ist 47.856.293 gerade oder ungerade?  
> → Letzte Ziffer ist 3 (ungerade) → Die Zahl ist ungerade.

### Rechenregeln mit geraden und ungeraden Zahlen

| Operation | Ergebnis | Beispiel |
|-----------|----------|----------|
| gerade + gerade | gerade | $4 + 6 = 10$ |
| ungerade + ungerade | gerade | $3 + 5 = 8$ |
| gerade + ungerade | ungerade | $4 + 5 = 9$ |
| gerade × gerade | gerade | $4 \cdot 6 = 24$ |
| ungerade × ungerade | ungerade | $3 \cdot 5 = 15$ |
| gerade × ungerade | gerade | $4 \cdot 5 = 20$ |

---

## Rechenoperationen mit natürlichen Zahlen

### Abgeschlossenheit – wann bleiben wir in $\mathbb{N}$?

Ein wichtiges Konzept ist die **Abgeschlossenheit**: Liegt das Ergebnis einer Operation wieder in derselben Zahlenmenge?

| Operation | Abgeschlossen in $\mathbb{N}$? | Begründung | Beispiel |
|-----------|--------------------------------|------------|----------|
| Addition | ✓ Ja | Summe zweier natürlicher Zahlen ist immer natürlich | $3 + 5 = 8 \in \mathbb{N}$ |
| Multiplikation | ✓ Ja | Produkt zweier natürlicher Zahlen ist immer natürlich | $3 \cdot 5 = 15 \in \mathbb{N}$ |
| Subtraktion | ✗ Nein | Ergebnis kann negativ oder null sein | $3 - 5 = -2 \notin \mathbb{N}$ |
| Division | ✗ Nein | Ergebnis ist oft kein ganzzahliger Wert | $5 : 3 = 1{,}\overline{6} \notin \mathbb{N}$ |

> [!note] **Warum ist das wichtig?**
> Die Nicht-Abgeschlossenheit von Subtraktion und Division zeigt eine Grenze der natürlichen Zahlen auf. Um Rechnungen wie $3 - 5$ oder $5 : 3$ durchführen zu können, brauchte die Mathematik neue Zahlenmengen:
> - Für Subtraktion → **ganze Zahlen** $\mathbb{Z}$ (mit negativen Zahlen)
> - Für Division → **rationale Zahlen** $\mathbb{Q}$ (Brüche)
>
> Die Entwicklung der Mathematik kann als schrittweise Erweiterung der Zahlenmengen verstanden werden, um immer mehr Operationen zu ermöglichen.

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[02-Mathematische-Symbole|Mathematische Symbole]] – Die Notation $\mathbb{N}$
- → [[04-Ganze-Zahlen|Ganze Zahlen]] – Erweiterung um negative Zahlen
- → [[07-Zahlenstrahl-und-Zahlenmengen|Zahlenstrahl]] – Visualisierung aller Zahlenmengen
- → [[08-Positive-und-negative-Zahlen|Positive und negative Zahlen]] – Vorzeichen

> [!warning] **Prüfungsrelevant**
> - Definition: $\mathbb{N} = \{1, 2, 3, \ldots\}$
> - Unterschied zwischen $\mathbb{N}$ und $\mathbb{N}_0$ (mit bzw. ohne Null)
> - Stellenwertsystem: Einer, Zehner, Hunderter, ...
> - Gerade Zahlen: Endziffer 0, 2, 4, 6, 8 – ungerade: 1, 3, 5, 7, 9
> - Abgeschlossenheit: Addition und Multiplikation ja, Subtraktion und Division nein

> [!question] **Typische Prüfungsfragen**
> - Was ist der Nachfolger von 999?
> - Ist $0 \in \mathbb{N}$? Begründe (je nach Konvention).
> - Zerlege 4527 nach Stellenwerten.
> - Ist die Zahl 123.456 gerade oder ungerade?
> - Warum ist die Subtraktion in $\mathbb{N}$ nicht abgeschlossen?

## Quellen

- Barner, Martin; Flohr, Friedrich: *Analysis I*. De Gruyter, 2000.
- Beutelspacher, Albrecht: *Zahlen*. Rowohlt, 2013.
- Ifrah, Georges: *Universalgeschichte der Zahlen*. Campus, 1991.

> [!tip] **Weiterführende Links**
> - [Mathebibel: Natürliche Zahlen](https://www.mathebibel.de/natuerliche-zahlen)
> - [[04-Ganze-Zahlen|Nächstes Kapitel: Ganze Zahlen]]
