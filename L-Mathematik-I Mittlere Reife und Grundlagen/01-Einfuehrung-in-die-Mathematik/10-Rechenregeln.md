---
author: Open Lectures
title: Mathematische Notation und Rechenregeln
status: final
tags:
  - content
  - mathematik
  - rechenregeln
  - notation
created: 2026-10-13
modified: 2026-10-16
---

# Mathematische Notation und Rechenregeln

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Rechengesetze (Kommutativ-, Assoziativ-, Distributivgesetz) kennen und anwenden
> - Die Reihenfolge der Rechenoperationen beherrschen
> - Terme korrekt aufstellen und umformen können
> - Klammern richtig setzen und auflösen können

---

## Überblick

Die Rechenregeln bilden das Grundgerüst der Mathematik. Sie legen fest, in welcher Reihenfolge Operationen ausgeführt werden und welche Umformungen erlaubt sind. Das Beherrschen dieser Regeln ist Voraussetzung für alle weiteren mathematischen Themen.

Diese Regeln sind nicht willkürlich festgelegt, sondern haben sich über Jahrhunderte entwickelt, um eindeutige und widerspruchsfreie Ergebnisse zu garantieren. Wenn jeder dieselben Regeln befolgt, kommt auch jeder zum selben Ergebnis – unabhängig davon, in welchem Land oder zu welcher Zeit gerechnet wird.

---

## Die Rechengesetze

Die folgenden drei Gesetze sind fundamentale Eigenschaften der Addition und Multiplikation. Sie bilden die Grundlage für das Umformen von Termen.

### Kommutativgesetz (Vertauschungsgesetz)

Bei Addition und Multiplikation darf die Reihenfolge der Zahlen vertauscht werden, ohne dass sich das Ergebnis ändert:

| Operation | Gesetz | Beispiel |
|-----------|--------|----------|
| Addition | $a + b = b + a$ | $3 + 5 = 5 + 3 = 8$ |
| Multiplikation | $a \cdot b = b \cdot a$ | $4 \cdot 7 = 7 \cdot 4 = 28$ |

Der Name kommt vom lateinischen „commutare" (vertauschen). Die Reihenfolge ist egal.

> [!warning] **Achtung: Nicht für Subtraktion und Division!**
> Subtraktion und Division sind **nicht** kommutativ:
> - $5 - 3 = 2$, aber $3 - 5 = -2$ → $5 - 3 \neq 3 - 5$
> - $6 : 2 = 3$, aber $2 : 6 = \frac{1}{3}$ → $6 : 2 \neq 2 : 6$
>
> Bei Subtraktion und Division kommt es auf die Reihenfolge an!

### Assoziativgesetz (Verbindungsgesetz)

Bei Addition und Multiplikation dürfen Klammern beliebig gesetzt oder weggelassen werden:

| Operation | Gesetz | Beispiel |
|-----------|--------|----------|
| Addition | $(a + b) + c = a + (b + c)$ | $(2 + 3) + 4 = 2 + (3 + 4) = 9$ |
| Multiplikation | $(a \cdot b) \cdot c = a \cdot (b \cdot c)$ | $(2 \cdot 3) \cdot 4 = 2 \cdot (3 \cdot 4) = 24$ |

Der Name kommt vom lateinischen „associare" (verbinden). Die Klammerung ist egal.

> [!note] **Praktische Bedeutung**
> Dank des Assoziativgesetzes können wir $2 + 3 + 4$ oder $2 \cdot 3 \cdot 4$ ohne Klammern schreiben – das Ergebnis ist unabhängig von der Klammerung. Wir können bei langen Summen oder Produkten die Terme beliebig gruppieren, was das Kopfrechnen erleichtert.
>
> **Beispiel:** $25 \cdot 4 \cdot 7 = (25 \cdot 4) \cdot 7 = 100 \cdot 7 = 700$ (einfacher als $25 \cdot (4 \cdot 7) = 25 \cdot 28$)

### Distributivgesetz (Verteilungsgesetz)

Das Distributivgesetz verbindet Multiplikation mit Addition/Subtraktion. Es erlaubt, Multiplikation über eine Klammer zu „verteilen":

$$a \cdot (b + c) = a \cdot b + a \cdot c$$
$$a \cdot (b - c) = a \cdot b - a \cdot c$$

Der Name kommt vom lateinischen „distribuere" (verteilen).

**Beispiele:**

$$3 \cdot (4 + 5) = 3 \cdot 4 + 3 \cdot 5 = 12 + 15 = 27$$
$$5 \cdot (10 - 2) = 5 \cdot 10 - 5 \cdot 2 = 50 - 10 = 40$$

> [!tip] **Umkehrung: Ausklammern**
> Das Distributivgesetz funktioniert auch rückwärts – man nennt das **Ausklammern**:
> $$6 + 9 = 3 \cdot 2 + 3 \cdot 3 = 3 \cdot (2 + 3) = 3 \cdot 5 = 15$$
>
> Gemeinsame Faktoren können „vor die Klammer gezogen" werden. Das ist besonders beim Vereinfachen von Termen nützlich.

### Anwendung beim Kopfrechnen

Die Rechengesetze helfen beim geschickten Kopfrechnen:

| Aufgabe | Geschickte Umformung | Ergebnis |
|---------|---------------------|----------|
| $17 + 28 + 3$ | $17 + 3 + 28 = 20 + 28$ | $48$ |
| $4 \cdot 13 \cdot 25$ | $4 \cdot 25 \cdot 13 = 100 \cdot 13$ | $1300$ |
| $7 \cdot 98$ | $7 \cdot (100 - 2) = 700 - 14$ | $686$ |
| $6 \cdot 15$ | $6 \cdot (10 + 5) = 60 + 30$ | $90$ |

---

## Reihenfolge der Rechenoperationen

### Die Regel: „Klammer vor Potenz vor Punkt vor Strich"

Wenn ein Ausdruck mehrere verschiedene Operationen enthält, ist die Reihenfolge festgelegt:

| Priorität | Operation | Symbol | Wird ausgeführt... |
|-----------|-----------|--------|-------------------|
| 1 (höchste) | Klammern | $( \, )$ | Zuerst, von innen nach außen |
| 2 | Potenzen | $a^n$ | Nach Klammern |
| 3 | Punktrechnung | $\cdot$, $:$ | Nach Potenzen |
| 4 (niedrigste) | Strichrechnung | $+$, $-$ | Zuletzt |

### Detaillierte Beispiele

**Beispiel 1:** $3 + 4 \cdot 2$
$$= 3 + 8 = 11 \quad \text{(Punkt vor Strich: erst } 4 \cdot 2\text{)}$$

**Beispiel 2:** $(3 + 4) \cdot 2$
$$= 7 \cdot 2 = 14 \quad \text{(Klammer zuerst: erst } 3 + 4\text{)}$$

**Beispiel 3:** $2 + 3 \cdot 4^2$
$$= 2 + 3 \cdot 16 = 2 + 48 = 50 \quad \text{(Potenz → Punkt → Strich)}$$

**Beispiel 4:** $24 : 4 \cdot 2$
$$= 6 \cdot 2 = 12 \quad \text{(gleiche Priorität: von links nach rechts)}$$

**Beispiel 5 (komplex):** $2 \cdot (3 + 4)^2 - 5$
$$= 2 \cdot 7^2 - 5 = 2 \cdot 49 - 5 = 98 - 5 = 93$$

> [!warning] **Bei gleicher Priorität: Von links nach rechts**
> Wenn Operationen gleicher Priorität aufeinandertreffen, wird **von links nach rechts** gerechnet:
> $$20 - 5 + 3 = 15 + 3 = 18 \quad \text{(nicht } 20 - 8 = 12\text{)}$$
> $$24 : 4 : 2 = 6 : 2 = 3 \quad \text{(nicht } 24 : 2 = 12\text{)}$$

---

## Klammerregeln

Klammern sind mächtige Werkzeuge, um die Reihenfolge zu steuern. Beim Auflösen von Klammern muss man auf das Vorzeichen vor der Klammer achten.

### Klammern auflösen: Plus vor der Klammer

Wenn ein Pluszeichen (oder kein Zeichen) vor der Klammer steht, bleiben alle Vorzeichen in der Klammer unverändert:

$$+(a + b) = a + b$$
$$+(a - b) = a - b$$

**Beispiel:** $5 + (3 - 2) = 5 + 3 - 2 = 6$

### Klammern auflösen: Minus vor der Klammer

Wenn ein Minuszeichen vor der Klammer steht, werden **alle Vorzeichen** in der Klammer umgekehrt:

$$-(a + b) = -a - b$$
$$-(a - b) = -a + b$$

> [!tip] **Merkregel: Minus dreht alles um**
> Ein Minus vor der Klammer „dreht" alle Vorzeichen innerhalb der Klammer um:
> - Plus wird zu Minus
> - Minus wird zu Plus

**Beispiele:**

| Ausdruck | Auflösung | Ergebnis |
|----------|-----------|----------|
| $5 + (3 - 2)$ | $5 + 3 - 2$ | $6$ |
| $5 - (3 - 2)$ | $5 - 3 + 2$ | $4$ |
| $5 - (3 + 2)$ | $5 - 3 - 2$ | $0$ |
| $10 - (4 - 7 + 2)$ | $10 - 4 + 7 - 2$ | $11$ |

### Verschachtelte Klammern

Bei mehreren ineinander geschachtelten Klammern arbeitet man **von innen nach außen**:

$$3 \cdot [2 + (4 - 1)]$$
$$= 3 \cdot [2 + 3]$$
$$= 3 \cdot 5$$
$$= 15$$

In der Mathematik werden oft verschiedene Klammertypen verwendet, um die Übersicht zu behalten: $(...)$, $[...]$, $\{...\}$.

---

## Rechengesetze für Brüche

Die Bruchrechnung folgt eigenen Regeln, die sich aus den allgemeinen Rechengesetzen ableiten.

### Addition und Subtraktion von Brüchen

**Gleicher Nenner:** Zähler addieren/subtrahieren, Nenner bleibt
$$\frac{a}{c} + \frac{b}{c} = \frac{a + b}{c}$$

**Beispiel:** $\frac{2}{5} + \frac{1}{5} = \frac{2+1}{5} = \frac{3}{5}$

**Verschiedene Nenner:** Erst auf gleichen Nenner bringen (erweitern), dann addieren
$$\frac{1}{2} + \frac{1}{3} = \frac{3}{6} + \frac{2}{6} = \frac{5}{6}$$

Der gemeinsame Nenner ist hier 6 (das kleinste gemeinsame Vielfache von 2 und 3).

### Multiplikation von Brüchen

**Regel:** Zähler mal Zähler, Nenner mal Nenner
$$\frac{a}{b} \cdot \frac{c}{d} = \frac{a \cdot c}{b \cdot d}$$

**Beispiel:**
$$\frac{2}{3} \cdot \frac{4}{5} = \frac{2 \cdot 4}{3 \cdot 5} = \frac{8}{15}$$

> [!tip] **Vor dem Multiplizieren kürzen**
> Es ist oft einfacher, vor der Multiplikation zu kürzen:
> $$\frac{3}{4} \cdot \frac{8}{9} = \frac{3}{4} \cdot \frac{8}{9} = \frac{\cancel{3}^1}{4} \cdot \frac{8}{\cancel{9}_3} = \frac{1 \cdot 8}{4 \cdot 3} = \frac{8}{12} = \frac{2}{3}$$

### Division von Brüchen

**Regel:** Mit dem Kehrwert multiplizieren
$$\frac{a}{b} : \frac{c}{d} = \frac{a}{b} \cdot \frac{d}{c} = \frac{a \cdot d}{b \cdot c}$$

**Beispiel:**
$$\frac{3}{4} : \frac{2}{5} = \frac{3}{4} \cdot \frac{5}{2} = \frac{15}{8}$$

> [!note] **Merkspruch für Division**
> „Dividieren durch einen Bruch heißt multiplizieren mit dem Kehrbruch."
> 
> Der Kehrwert von $\frac{2}{5}$ ist $\frac{5}{2}$ (Zähler und Nenner tauschen).

---

## Potenzgesetze (Vorschau)

Potenzen sind verkürzte Schreibweisen für wiederholte Multiplikation. Für sie gelten eigene Rechengesetze:

| Gesetz | Formel | Beispiel | Erklärung |
|--------|--------|----------|-----------|
| Gleiche Basis, Multiplikation | $a^m \cdot a^n = a^{m+n}$ | $2^3 \cdot 2^2 = 2^5 = 32$ | Exponenten addieren |
| Gleiche Basis, Division | $a^m : a^n = a^{m-n}$ | $2^5 : 2^2 = 2^3 = 8$ | Exponenten subtrahieren |
| Potenz einer Potenz | $(a^m)^n = a^{m \cdot n}$ | $(2^3)^2 = 2^6 = 64$ | Exponenten multiplizieren |
| Potenz eines Produkts | $(a \cdot b)^n = a^n \cdot b^n$ | $(2 \cdot 3)^2 = 4 \cdot 9 = 36$ | Potenz verteilen |

Diese Gesetze werden in späteren Kapiteln ausführlich behandelt.

---

## Neutrale und inverse Elemente

Jede Grundrechenart hat besondere Elemente mit speziellen Eigenschaften:

### Neutrale Elemente: „Ändern nichts"

| Operation | Neutrales Element | Eigenschaft | Beispiel |
|-----------|-------------------|-------------|----------|
| Addition | $0$ | $a + 0 = a$ | $7 + 0 = 7$ |
| Multiplikation | $1$ | $a \cdot 1 = a$ | $7 \cdot 1 = 7$ |

### Inverse Elemente: „Machen rückgängig"

| Operation | Inverses zu $a$ | Eigenschaft | Beispiel |
|-----------|-----------------|-------------|----------|
| Addition | $-a$ (Gegenzahl) | $a + (-a) = 0$ | $5 + (-5) = 0$ |
| Multiplikation | $\frac{1}{a}$ (Kehrwert) | $a \cdot \frac{1}{a} = 1$ | $5 \cdot \frac{1}{5} = 1$ |

> [!note] **Kein multiplikatives Inverses für Null**
> Die Null hat keinen Kehrwert, denn $\frac{1}{0}$ ist nicht definiert. Das ist der Grund, warum man nicht durch Null teilen darf.

---

## Zusammenfassung: Übersichtstafel

![[rechengesetze.png]]
*<span class="fig-id">01-01-10-rechengesetze</span>: Übersicht der grundlegenden Rechengesetze – Kommutativ-, Assoziativ- und Distributivgesetz sowie die Reihenfolge der Operationen (Klammer → Potenz → Punkt → Strich).*

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[02-Mathematische-Symbole|Mathematische Symbole]] – Notation
- → [[05-Rationale-Zahlen|Rationale Zahlen]] – Bruchrechnung
- → [[08-Positive-und-negative-Zahlen|Vorzeichen]] – Vorzeichenregeln

> [!warning] **Prüfungsrelevant**
> - Kommutativ-, Assoziativ-, Distributivgesetz und ihre Anwendung
> - Reihenfolge: Klammer vor Potenz vor Punkt vor Strich
> - Minus vor Klammer kehrt alle Vorzeichen um
> - Bruchrechnung: Addition mit Hauptnenner, Multiplikation Zähler·Zähler / Nenner·Nenner
> - Division durch Bruch = Multiplikation mit Kehrwert
> - Neutrale Elemente: 0 für Addition, 1 für Multiplikation

> [!question] **Typische Prüfungsfragen**
> - Berechne: $5 + 3 \cdot (4 - 2)^2$
> - Vereinfache: $3 \cdot (x + 2) - 2 \cdot (x - 1)$
> - Berechne: $\frac{2}{3} + \frac{3}{4}$
> - Welches Rechengesetz wurde angewendet: $3 \cdot 7 = 7 \cdot 3$?
> - Löse die Klammer auf: $8 - (3 - 5 + 2)$

## Quellen

- Padberg, Friedhelm: *Didaktik der Arithmetik*. Springer, 2017.
- Scheid, Harald: *Elemente der Arithmetik und Algebra*. Springer, 2016.
- Griesel, Heinz et al.: *Elemente der Mathematik*. Schroedel, 2019.

> [!tip] **Weiterführende Links**
> - [Mathebibel: Rechengesetze](https://www.mathebibel.de/rechengesetze)
> - [[02-Grundrechenarten-Index|Nächstes Modul: Grundrechenarten]]
