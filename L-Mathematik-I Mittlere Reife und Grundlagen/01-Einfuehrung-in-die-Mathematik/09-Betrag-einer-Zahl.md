---
author: Open Lectures
title: Betrag einer Zahl
status: final
tags:
  - content
  - mathematik
  - zahlenmengen
  - betrag
created: 2026-10-13
modified: 2026-10-16
---

# Betrag einer Zahl

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Betrag einer Zahl definieren und berechnen können
> - Den Betrag als Abstand zur Null auf dem Zahlenstrahl verstehen
> - Rechenregeln für Beträge anwenden können
> - Betragsgleichungen und -ungleichungen verstehen

---

## Überblick

Der Betrag einer Zahl gibt an, wie weit diese Zahl von der Null entfernt ist – ohne Berücksichtigung des Vorzeichens. Der Betrag ist immer nicht-negativ und wird durch senkrechte Striche $|a|$ notiert. Er spielt eine wichtige Rolle bei Abständen und Fehlerrechnung.

Das Konzept des Betrags ist intuitiv: Wenn du fragst „Wie weit ist es bis zur Null?", interessiert dich nur die Entfernung, nicht die Richtung. Ob eine Zahl 5 Einheiten links oder 5 Einheiten rechts von der Null liegt – der Abstand ist in beiden Fällen 5. Der Betrag abstrahiert von der Richtung und liefert nur die „reine Größe" einer Zahl.

---

## Definition

Der **Betrag** (auch: Absolutbetrag, Absolutwert) einer reellen Zahl $a$ ist wie folgt definiert:

$$|a| = \begin{cases} a & \text{falls } a \geq 0 \\ -a & \text{falls } a < 0 \end{cases}$$

### Was bedeutet diese Definition?

Die Definition sagt:
- Ist die Zahl **nicht negativ** (also positiv oder null): Der Betrag ist die Zahl selbst
- Ist die Zahl **negativ**: Der Betrag ist das Negative der Zahl (was dann positiv wird)

Oder einfacher ausgedrückt:

> Der Betrag einer Zahl ist die Zahl selbst, wenn sie positiv oder null ist, und das Negative der Zahl, wenn sie negativ ist.

Das Negative einer negativen Zahl ist positiv: $-(-5) = 5$. Daher ist der Betrag immer nicht-negativ.

### Beispiele

| Zahl $a$ | Betrag $|a|$ | Erklärung |
|----------|--------------|-----------|
| $5$ | $|5| = 5$ | $5 \geq 0$, also bleibt es $5$ |
| $-5$ | $|-5| = 5$ | $-5 < 0$, also $-(-5) = 5$ |
| $0$ | $|0| = 0$ | $0 \geq 0$, also bleibt es $0$ |
| $-3{,}7$ | $|-3{,}7| = 3{,}7$ | Vorzeichen wird entfernt |
| $\frac{2}{3}$ | $|\frac{2}{3}| = \frac{2}{3}$ | Bereits positiv, bleibt unverändert |
| $-\sqrt{2}$ | $|-\sqrt{2}| = \sqrt{2}$ | Negativ wird positiv |

> [!tip] **Faustregel**
> Der Betrag „entfernt das Minuszeichen", falls eines vorhanden ist. Ein bereits positives Vorzeichen (oder kein Vorzeichen) bleibt unverändert.

---

## Geometrische Interpretation

Der Betrag ist der **Abstand zur Null** auf dem Zahlenstrahl. Diese geometrische Sichtweise ist oft intuitiver als die algebraische Definition.

![[betrag-abstand.png]]
*<span class="fig-id">01-01-09-betrag-abstand</span>: Der Betrag als Abstand zur Null. Sowohl −5 als auch 5 haben den Abstand 5 zur Null, also |−5| = 5 und |5| = 5.*

### Symmetrie zur Null

> [!note] **Wichtige Beobachtung**
> Zwei Zahlen mit gleichem Betrag liegen **symmetrisch zur Null**:
> - $5$ und $-5$ haben beide den Betrag $5$
> - Sie sind gleich weit von der Null entfernt, aber in entgegengesetzte Richtungen
> - Auf dem Zahlenstrahl sind sie Spiegelbilder bezüglich der Null

Diese Symmetrie macht den Betrag nützlich, wenn uns nur der „Abstand" oder die „Größe" interessiert, nicht die Richtung.

---

## Alternative Darstellung

Der Betrag kann auch über die Quadratwurzel definiert werden:

$$|a| = \sqrt{a^2}$$

### Warum funktioniert das?

1. Beim Quadrieren wird das Vorzeichen eliminiert: $(-5)^2 = 25 = 5^2$
2. Die Quadratwurzel liefert die nicht-negative Wurzel: $\sqrt{25} = 5$
3. Das Ergebnis ist der Betrag

**Beispiel:**
$$|-7| = \sqrt{(-7)^2} = \sqrt{49} = 7$$

Diese Definition ist praktisch, weil sie in einer einzigen Formel funktioniert, ohne Fallunterscheidung. Sie ist besonders in der Analysis und bei Beweisen nützlich.

---

## Eigenschaften des Betrags

### Grundlegende Eigenschaften

| Eigenschaft | Formel | Beispiel | Bedeutung |
|-------------|--------|----------|-----------|
| **Nicht-Negativität** | $|a| \geq 0$ | $|-3| = 3 \geq 0$ | Beträge sind nie negativ |
| **Definitheit** | $|a| = 0 \Leftrightarrow a = 0$ | $|0| = 0$ | Nur Null hat Betrag Null |
| **Symmetrie** | $|-a| = |a|$ | $|-5| = |5| = 5$ | Vorzeichen ist egal |
| **Multiplikativität** | $|a \cdot b| = |a| \cdot |b|$ | $|(-2) \cdot 3| = 6 = 2 \cdot 3$ | Beträge multiplizieren sich |
| **Division** | $\left|\frac{a}{b}\right| = \frac{|a|}{|b|}$ | $\left|\frac{-6}{2}\right| = \frac{6}{2} = 3$ | Beträge dividieren sich |

> [!note] **Keine Additivität!**
> Achtung: Im Allgemeinen gilt $|a + b| \neq |a| + |b|$!
>
> Gegenbeispiel: $|3 + (-5)| = |-2| = 2$, aber $|3| + |-5| = 3 + 5 = 8$.
>
> Es gilt aber eine wichtige Ungleichung: $|a + b| \leq |a| + |b|$ (siehe Dreiecksungleichung).

### Die Dreiecksungleichung

Eine der wichtigsten Eigenschaften ist die **Dreiecksungleichung**:

$$|a + b| \leq |a| + |b|$$

**Beispiel:**
$$|3 + (-5)| = |-2| = 2 \leq |3| + |-5| = 3 + 5 = 8 \quad ✓$$

> [!note] **Anschauliche Erklärung**
> Stell dir vor, du gehst zuerst 3 Schritte nach rechts, dann 5 Schritte nach links. Du landest bei $-2$, also 2 Einheiten links vom Start.
> 
> Wenn du stattdessen die Gesamtzahl der Schritte zählst (3 + 5 = 8), ist das mehr als dein tatsächlicher Abstand vom Start (2).
>
> Der „direkte Weg" (linke Seite) ist nie länger als der „Umweg" (rechte Seite).

Die Dreiecksungleichung hat ihren Namen aus der Geometrie: In einem Dreieck ist jede Seite kürzer als die Summe der beiden anderen Seiten.

---

## Betragsgleichungen

### Lösen von $|x| = a$

Für $a \geq 0$ hat die Gleichung $|x| = a$ genau **zwei Lösungen** (bzw. eine für $a = 0$):

$$|x| = a \quad \Leftrightarrow \quad x = a \text{ oder } x = -a$$

**Beispiel:** Löse $|x| = 3$

Die Frage lautet: Welche Zahlen haben den Abstand 3 zur Null?

Antwort: $x = 3$ (drei Einheiten rechts) oder $x = -3$ (drei Einheiten links)

Lösungsmenge: $\mathbb{L} = \{-3, 3\}$

![[betrag-gleichung.png]]
*<span class="fig-id">01-01-09-betrag-gleichung</span>: Lösung von |x| = 3. Die beiden Lösungen −3 und 3 haben jeweils den Abstand 3 zur Null; die Lösungsmenge ist L = {−3, 3}.*

> [!warning] **Sonderfall: $|x| = a$ mit $a < 0$**
> Wenn $a$ negativ ist, hat die Gleichung **keine Lösung**: Der Betrag kann nie negativ sein!
>
> Beispiel: $|x| = -2$ hat keine Lösung, $\mathbb{L} = \emptyset$.

### Lösen von $|x - c| = a$

Diese Form fragt: „Welche Zahlen haben den Abstand $a$ zum Punkt $c$?"

$$|x - c| = a \quad \Leftrightarrow \quad x = c + a \text{ oder } x = c - a$$

**Beispiel:** Löse $|x - 2| = 5$

Die Frage: Welche Zahlen haben den Abstand 5 zur Zahl 2?

Lösung: 
- $x = 2 + 5 = 7$ (5 Einheiten rechts von 2)
- $x = 2 - 5 = -3$ (5 Einheiten links von 2)

Lösungsmenge: $\mathbb{L} = \{-3, 7\}$

> [!tip] **Interpretation merken**
> $|x - c| = a$ bedeutet: „Der Abstand von $x$ zu $c$ ist genau $a$."
>
> Die Lösungen liegen symmetrisch um $c$, jeweils im Abstand $a$.

---

## Betragsungleichungen

### Typ 1: $|x| < a$ (Abstand kleiner als $a$)

Diese Ungleichung fragt: „Welche Zahlen liegen näher an der Null als $a$ Einheiten?"

$$|x| < a \quad \Leftrightarrow \quad -a < x < a$$

**Beispiel:** Löse $|x| < 3$

Alle Zahlen, deren Abstand zur Null kleiner als 3 ist:

Lösung: $-3 < x < 3$, also das **offene Intervall** $(-3, 3)$

```
    ←──┬────┬────┬────┬────┬────┬────┬──→
      -4   -3   -2   -1    0    1    2    3    4
            ○────────────────────────○
                    Lösungsmenge
            (Grenzen nicht enthalten)
```

### Typ 2: $|x| > a$ (Abstand größer als $a$)

Diese Ungleichung fragt: „Welche Zahlen liegen weiter von der Null entfernt als $a$ Einheiten?"

$$|x| > a \quad \Leftrightarrow \quad x < -a \text{ oder } x > a$$

**Beispiel:** Löse $|x| > 2$

Alle Zahlen, deren Abstand zur Null größer als 2 ist:

Lösung: $x < -2$ oder $x > 2$, also $(-\infty, -2) \cup (2, \infty)$

```
    ←──┬────┬────┬────┬────┬────┬────┬──→
      -4   -3   -2   -1    0    1    2    3    4
    ━━━━━━━━○              ○━━━━━━━━
        Lösungsmenge     Lösungsmenge
```

### Zusammenfassung der Ungleichungstypen

| Ungleichung | Lösung | Geometrische Bedeutung |
|-------------|--------|------------------------|
| $|x| < a$ | $-a < x < a$ | Innerhalb des Intervalls |
| $|x| \leq a$ | $-a \leq x \leq a$ | Innerhalb, Grenzen eingeschlossen |
| $|x| > a$ | $x < -a$ oder $x > a$ | Außerhalb des Intervalls |
| $|x| \geq a$ | $x \leq -a$ oder $x \geq a$ | Außerhalb, Grenzen eingeschlossen |

---

## Abstand zwischen zwei Zahlen

Der **Abstand** zwischen zwei Zahlen $a$ und $b$ auf dem Zahlenstrahl wird mit dem Betrag berechnet:

$$d(a, b) = |a - b| = |b - a|$$

Die Reihenfolge spielt keine Rolle, da $|a - b| = |b - a|$ (Symmetrieeigenschaft).

### Beispiele

| Zahlen | Berechnung | Abstand |
|--------|------------|---------|
| $3$ und $7$ | $|3 - 7| = |-4| = 4$ | $4$ |
| $-2$ und $5$ | $|-2 - 5| = |-7| = 7$ | $7$ |
| $-4$ und $-1$ | $|-4 - (-1)| = |-3| = 3$ | $3$ |
| $2$ und $2$ | $|2 - 2| = |0| = 0$ | $0$ (identische Punkte) |

> [!tip] **Anwendung: Toleranzintervalle**
> In der Technik wird oft angegeben: „Der Wert soll 10 betragen, mit einer Toleranz von ±0,5."
>
> Mathematisch: $|x - 10| \leq 0{,}5$, also $9{,}5 \leq x \leq 10{,}5$.

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[08-Positive-und-negative-Zahlen|Positive und negative Zahlen]] – Vorzeichen
- → [[07-Zahlenstrahl-und-Zahlenmengen|Zahlenstrahl]] – Visualisierung von Abständen
- → [[04-Ganze-Zahlen|Ganze Zahlen]] – Gegenzahl: $a$ und $-a$

> [!warning] **Prüfungsrelevant**
> - Definition: $|a| = a$ für $a \geq 0$, $|a| = -a$ für $a < 0$
> - Geometrisch: Abstand zur Null
> - $|a| \geq 0$ (immer nicht-negativ)
> - $|a \cdot b| = |a| \cdot |b|$
> - Dreiecksungleichung: $|a + b| \leq |a| + |b|$
> - Lösen von $|x| = a$: zwei Lösungen $x = \pm a$ (für $a \geq 0$)
> - Abstand zwischen Zahlen: $d(a,b) = |a - b|$

> [!question] **Typische Prüfungsfragen**
> - Berechne $|-7| + |3|$.
> - Löse die Gleichung $|x - 4| = 6$.
> - Für welche $x$ gilt $|x| \leq 5$?
> - Bestimme den Abstand zwischen $-3$ und $8$.
> - Warum gilt $|a + b| \leq |a| + |b|$?

## Quellen

- Papula, Lothar: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1. Springer, 2018.
- Forster, Otto: *Analysis 1*. Springer, 2016.
- Griesel, Heinz et al.: *Elemente der Mathematik*. Schroedel, 2019.

> [!tip] **Weiterführende Links**
> - [Mathebibel: Betrag](https://www.mathebibel.de/betrag)
> - [[10-Rechenregeln|Nächstes Kapitel: Rechenregeln]]
