---
author: Andreas Hümmer
title: Mathematische Schreibweisen und Symbole
status: final
tags:
  - content
  - mathematik
  - notation
  - symbole
created: 2026-10-13
modified: 2026-10-16
---

# Mathematische Schreibweisen und Symbole

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die wichtigsten mathematischen Symbole kennen und korrekt verwenden
> - Mathematische Ausdrücke lesen und interpretieren können
> - Den Unterschied zwischen Gleichung und Ungleichung verstehen
> - Mengennotation in Grundzügen kennen

---

## Überblick

Mathematik verwendet eine eigene Symbolsprache, die weltweit einheitlich ist. Diese Symbole ermöglichen es, komplexe Zusammenhänge kurz und präzise auszudrücken. Das Erlernen dieser Notation ist wie das Lernen eines Alphabets – es ist die Grundlage für alles Weitere.

Der große Vorteil der mathematischen Symbolsprache liegt in ihrer Kompaktheit und Eindeutigkeit. Was in Worten mehrere Sätze bräuchte, lässt sich mit Symbolen in einer Zeile ausdrücken. Gleichzeitig gibt es keine Interpretationsspielräume: Ein Symbol bedeutet immer dasselbe, unabhängig davon, wer es liest oder in welchem Land es verwendet wird.

---

## Grundlegende Rechenzeichen

### Die vier Grundrechenarten

Die vier Grundrechenarten bilden das Fundament aller mathematischen Operationen. Jede Rechenart hat ihr eigenes Symbol:

| Symbol | Name | Bedeutung | Beispiel |
|--------|------|-----------|----------|
| $+$ | Plus | Addition (Zusammenzählen) | $3 + 5 = 8$ |
| $-$ | Minus | Subtraktion (Abziehen) | $7 - 2 = 5$ |
| $\cdot$ oder $\times$ | Mal | Multiplikation (Vervielfachen) | $4 \cdot 3 = 12$ |
| $:$ oder $\div$ oder $/$ | Geteilt | Division (Teilen) | $12 : 4 = 3$ |

> [!note] **Hinweis zur Schreibweise**
> In der höheren Mathematik wird meist der Malpunkt $\cdot$ verwendet. Das Kreuz $\times$ kann mit der Variable $x$ verwechselt werden und wird daher ab der Algebra vermieden. 
>
> Bei der Division gibt es mehrere Schreibweisen:
> - $12 : 4$ (mit Doppelpunkt, typisch für Deutschland)
> - $12 \div 4$ (mit Divisionszeichen, international)
> - $\frac{12}{4}$ (als Bruch, in der höheren Mathematik bevorzugt)
> - $12 / 4$ (Schrägstrich, oft in Computerprogrammen)

### Gleichheitszeichen und Verwandte

Das Gleichheitszeichen ist eines der wichtigsten Symbole der Mathematik. Es wurde 1557 vom walisischen Mathematiker Robert Recorde eingeführt:

| Symbol | Name | Bedeutung | Beispiel |
|--------|------|-----------|----------|
| $=$ | gleich | Linke und rechte Seite haben denselben Wert | $2 + 3 = 5$ |
| $\neq$ | ungleich | Linke und rechte Seite sind verschieden | $3 \neq 5$ |
| $\approx$ | ungefähr gleich | Näherungswert (nicht exakt, aber nahe) | $\pi \approx 3{,}14$ |
| $:=$ oder $\coloneqq$ | definiert als | Einführung einer Definition | $a := 5$ (ab jetzt gilt: $a$ ist 5) |

Das Symbol $\approx$ ist besonders wichtig, wenn wir mit irrationalen Zahlen wie $\pi$ oder $\sqrt{2}$ arbeiten, die sich nicht exakt als Dezimalzahl schreiben lassen. Dann geben wir einen Näherungswert an.

---

## Vergleichszeichen (Relationen)

Vergleichszeichen drücken Größenbeziehungen zwischen Zahlen aus. Sie sind essenziell für das Arbeiten mit Ungleichungen:

| Symbol | Name | Bedeutung | Beispiel |
|--------|------|-----------|----------|
| $<$ | kleiner als | Linke Seite ist kleiner | $3 < 7$ (3 ist kleiner als 7) |
| $>$ | größer als | Linke Seite ist größer | $9 > 4$ (9 ist größer als 4) |
| $\leq$ | kleiner oder gleich | Linke Seite ist höchstens so groß | $5 \leq 5$ (5 ist kleiner oder gleich 5) |
| $\geq$ | größer oder gleich | Linke Seite ist mindestens so groß | $8 \geq 6$ (8 ist größer oder gleich 6) |

> [!tip] **Merkregel: Das hungrige Krokodil**
> Stell dir das Vergleichszeichen als Maul eines hungrigen Krokodils vor. Das Krokodil will immer die größere Zahl fressen und öffnet sein Maul in deren Richtung:
> - $3 < 7$: Die „Spitze" zeigt zur 3, das „offene Maul" zur 7 (der größeren Zahl)
> - $9 > 4$: Die „Spitze" zeigt zur 4, das „offene Maul" zur 9 (der größeren Zahl)
>
> Alternativ: Das spitze Ende zeigt immer zur kleineren Zahl.

### Unterschied zwischen $<$ und $\leq$

Der Unterschied ist subtil, aber wichtig:
- $x < 5$ bedeutet: $x$ ist **echt kleiner** als 5 (also $x$ kann 4, 3, 2, ... sein, aber **nicht** 5)
- $x \leq 5$ bedeutet: $x$ ist **kleiner oder gleich** 5 (also $x$ kann auch genau 5 sein)

---

## Klammerregeln

Klammern bestimmen die Reihenfolge der Berechnungen. Sie sind wie Regieanweisungen in einem Theaterstück: Sie sagen, was zuerst passieren soll.

### Arten von Klammern

In der Mathematik werden verschiedene Klammerarten verwendet, die oft hierarchisch eingesetzt werden:

| Klammer | Name | Verwendung |
|---------|------|------------|
| $( \quad )$ | runde Klammern | Standard-Klammern für Rechenoperationen |
| $[ \quad ]$ | eckige Klammern | Äußere Klammern bei verschachtelten Ausdrücken, Intervalle |
| $\{ \quad \}$ | geschweifte Klammern | Mengen (Aufzählung von Elementen) |

### Rechenregel: „Klammer vor Punkt vor Strich"

Diese Regel legt fest, in welcher Reihenfolge Rechenoperationen ausgeführt werden:

1. **Klammern** zuerst auflösen (bei verschachtelten Klammern: von innen nach außen)
2. **Punkt**rechnung (Multiplikation, Division)
3. **Strich**rechnung (Addition, Subtraktion)

**Beispiel mit allen Schritten:**
$$3 + 4 \cdot (2 + 5) = 3 + 4 \cdot 7 = 3 + 28 = 31$$

Ohne die Klammer wäre das Ergebnis anders:
$$3 + 4 \cdot 2 + 5 = 3 + 8 + 5 = 16$$

> [!warning] **Häufiger Fehler**
> Viele Schüler rechnen fälschlicherweise von links nach rechts und ignorieren die Regel „Punkt vor Strich".
> 
> **Falsch:** $3 + 4 \cdot 2 = 7 \cdot 2 = 14$
> **Richtig:** $3 + 4 \cdot 2 = 3 + 8 = 11$

---

## Mengensymbole

Mengen sind Sammlungen von Objekten (Elementen). Die Mengenlehre bildet das Fundament der modernen Mathematik. Eine Menge kann endlich viele Elemente haben (z.B. $\{1, 2, 3\}$) oder unendlich viele (z.B. alle natürlichen Zahlen).

| Symbol | Name | Bedeutung | Beispiel |
|--------|------|-----------|----------|
| $\in$ | Element von | gehört zur Menge | $3 \in \{1, 2, 3\}$ (3 ist Element der Menge) |
| $\notin$ | kein Element von | gehört nicht zur Menge | $5 \notin \{1, 2, 3\}$ (5 ist nicht in der Menge) |
| $\subset$ | Teilmenge von | alle Elemente sind in der größeren Menge enthalten | $\{1, 2\} \subset \{1, 2, 3\}$ |
| $\cup$ | Vereinigung | alle Elemente aus beiden Mengen | $\{1, 2\} \cup \{3\} = \{1, 2, 3\}$ |
| $\cap$ | Schnittmenge | nur gemeinsame Elemente | $\{1, 2\} \cap \{2, 3\} = \{2\}$ |
| $\emptyset$ oder $\{\}$ | leere Menge | Menge ohne Elemente | $\{1\} \cap \{2\} = \emptyset$ |

### Visualisierung: Venn-Diagramme

Mengenoperationen lassen sich gut mit Venn-Diagrammen visualisieren. Zwei überlappende Kreise zeigen, welche Elemente zu welcher Menge gehören:

![[venn-mengen.png]]
*<span class="fig-id">01-01-02-venn-mengen</span>: Venn-Diagramm der Mengen A = {1, 2} und B = {2, 3}. Die Schnittmenge A ∩ B = {2} enthält nur das gemeinsame Element, die Vereinigung A ∪ B = {1, 2, 3} alle Elemente.*

---

## Zahlenmengen-Symbole

Die wichtigsten Zahlenmengen haben eigene Symbole. Diese werden mit Doppelstrich geschrieben (sogenannte „Blackboard Bold"-Schrift):

| Symbol | Name | Elemente | Herkunft des Namens |
|--------|------|----------|---------------------|
| $\mathbb{N}$ | Natürliche Zahlen | $1, 2, 3, 4, \ldots$ | „Natürlich" – die natürlichsten Zahlen zum Zählen |
| $\mathbb{N}_0$ | Natürliche Zahlen mit Null | $0, 1, 2, 3, \ldots$ | |
| $\mathbb{Z}$ | Ganze Zahlen | $\ldots, -2, -1, 0, 1, 2, \ldots$ | „Zahlen" (deutsch) |
| $\mathbb{Q}$ | Rationale Zahlen | Alle Brüche $\frac{p}{q}$ | „Quotient" (lat. für Bruch) |
| $\mathbb{R}$ | Reelle Zahlen | Alle Zahlen auf dem Zahlenstrahl | „Real" (die „echten" Zahlen) |

Diese Mengen bauen aufeinander auf: Jede natürliche Zahl ist auch eine ganze Zahl, jede ganze Zahl ist auch eine rationale Zahl, und jede rationale Zahl ist auch eine reelle Zahl.

---

## Weitere wichtige Symbole

| Symbol | Name | Bedeutung | Beispiel |
|--------|------|-----------|----------|
| $\sum$ | Summenzeichen | Summe mehrerer Zahlen (griechisches Sigma) | $\sum_{i=1}^{3} i = 1+2+3 = 6$ |
| $\prod$ | Produktzeichen | Produkt mehrerer Zahlen (griechisches Pi) | $\prod_{i=1}^{3} i = 1 \cdot 2 \cdot 3 = 6$ |
| $\sqrt{\phantom{x}}$ | Wurzel | Quadratwurzel (welche Zahl mal sich selbst?) | $\sqrt{9} = 3$ (denn $3 \cdot 3 = 9$) |
| $\|x\|$ oder $|x|$ | Betrag | Abstand zur Null (immer positiv) | $\|-5\| = 5$ |
| $\infty$ | Unendlich | unbegrenzt groß (keine Zahl!) | „$x$ geht gegen $\infty$" |
| $\ldots$ | Auslassungspunkte | „und so weiter" | $1, 2, 3, \ldots$ |
| $\therefore$ | Folglich | „daraus folgt" | |
| $\Rightarrow$ | Implikation | „wenn..., dann..." | $x = 2 \Rightarrow x^2 = 4$ |

> [!note] **Das Symbol $\infty$**
> Unendlich ($\infty$) ist **keine Zahl**, sondern ein Konzept. Man kann nicht mit $\infty$ rechnen wie mit normalen Zahlen. Ausdrücke wie $\infty + 1$ oder $\frac{\infty}{2}$ sind nicht definiert. Das Symbol drückt aus, dass etwas unbegrenzt wächst oder sich einer Grenze nähert.

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[01-Bedeutung-der-Mathematik|Bedeutung der Mathematik]] – Warum wir diese Symbole brauchen
- → [[03-Natuerliche-Zahlen|Natürliche Zahlen]] – Die Menge $\mathbb{N}$
- → [[07-Zahlenstrahl-und-Zahlenmengen|Zahlenstrahl und Zahlenmengen]] – Visualisierung der Mengen
- → [[10-Rechenregeln|Rechenregeln]] – Anwendung der Symbole

> [!warning] **Prüfungsrelevant**
> - Die Symbole für die vier Grundrechenarten und Vergleichszeichen
> - Regel „Klammer vor Punkt vor Strich"
> - Symbole für Zahlenmengen: $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$
> - Elementbeziehung $\in$ und $\notin$
> - Unterschied zwischen $<$ und $\leq$

> [!question] **Typische Prüfungsfragen**
> - Was bedeutet das Symbol $\leq$?
> - Berechne: $2 + 3 \cdot (4 - 1)$
> - Ist $-3 \in \mathbb{N}$? Begründe.
> - Was ist $\{1, 2, 3\} \cap \{2, 3, 4\}$?
> - Schreibe den Ausdruck „5 ist kleiner oder gleich 7" mit mathematischen Symbolen.

## Quellen

- Papula, Lothar: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1. Springer, 2018.
- Taschner, Rudolf: *Zahl Zeit Zufall*. Ecowin, 2007.
- Cajori, Florian: *A History of Mathematical Notations*. Dover, 1993.

> [!tip] **Weiterführende Links**
> - [Mathebibel: Mathematische Zeichen](https://www.mathebibel.de/mathematische-zeichen)
> - [[03-Natuerliche-Zahlen|Nächstes Kapitel: Natürliche Zahlen]]
