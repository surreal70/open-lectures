---
author: Open Lectures
title: Betrag einer Zahl
status: draft - review pending
tags:
  - content
  - mathematik
  - zahlenmengen
  - betrag
created: 2026-10-13
modified: 2026-10-13
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

---

## Definition

Der **Betrag** (auch: Absolutbetrag) einer reellen Zahl $a$ ist definiert als:

$$|a| = \begin{cases} a & \text{falls } a \geq 0 \\ -a & \text{falls } a < 0 \end{cases}$$

Oder einfacher ausgedrückt:

> Der Betrag einer Zahl ist die Zahl selbst, wenn sie positiv oder null ist, und das Negative der Zahl, wenn sie negativ ist.

### Beispiele

| Zahl $a$ | Betrag $|a|$ | Erklärung |
|----------|--------------|-----------|
| $5$ | $|5| = 5$ | $5 \geq 0$, also bleibt es $5$ |
| $-5$ | $|-5| = 5$ | $-5 < 0$, also $-(-5) = 5$ |
| $0$ | $|0| = 0$ | $0 \geq 0$, also bleibt es $0$ |
| $-3{,}7$ | $|-3{,}7| = 3{,}7$ | Vorzeichen entfernen |
| $\frac{2}{3}$ | $|\frac{2}{3}| = \frac{2}{3}$ | Bereits positiv |

---

## Geometrische Interpretation

Der Betrag ist der **Abstand zur Null** auf dem Zahlenstrahl:

```
                    Abstand = 5              Abstand = 5
                    ←─────────→              ←─────────→
    ←──┬────┬────┬────┬────┬────┬────┬────┬────┬────┬──→
      -6   -5   -4   -3   -2   -1    0    1    2    3    4    5
            ●                        ●                        ●
           -5                        0                        5

                      |-5| = 5               |5| = 5
```

> [!note] **Wichtige Beobachtung**
> Zwei Zahlen mit gleichem Betrag liegen **symmetrisch zur Null**:
> - $5$ und $-5$ haben beide den Betrag $5$
> - Sie sind gleich weit von der Null entfernt

---

## Alternative Darstellung

Der Betrag kann auch über die Quadratwurzel definiert werden:

$$|a| = \sqrt{a^2}$$

**Beispiel:**
$$|-7| = \sqrt{(-7)^2} = \sqrt{49} = 7$$

Diese Definition ist nützlich, weil sie immer einen nicht-negativen Wert liefert.

---

## Eigenschaften des Betrags

### Grundlegende Eigenschaften

| Eigenschaft | Formel | Beispiel |
|-------------|--------|----------|
| Nicht-Negativität | $|a| \geq 0$ | $|-3| = 3 \geq 0$ |
| Definitheit | $|a| = 0 \Leftrightarrow a = 0$ | $|0| = 0$ |
| Symmetrie | $|-a| = |a|$ | $|-5| = |5| = 5$ |
| Multiplikativität | $|a \cdot b| = |a| \cdot |b|$ | $|(-2) \cdot 3| = |-6| = 6 = 2 \cdot 3$ |
| Division | $\left|\frac{a}{b}\right| = \frac{|a|}{|b|}$ (für $b \neq 0$) | $\left|\frac{-6}{2}\right| = \frac{6}{2} = 3$ |

### Dreiecksungleichung

Eine der wichtigsten Eigenschaften ist die **Dreiecksungleichung**:

$$|a + b| \leq |a| + |b|$$

**Beispiel:**
$$|3 + (-5)| = |-2| = 2 \leq |3| + |-5| = 3 + 5 = 8 \quad ✓$$

> [!note] **Anschaulich**
> Der „direkte Weg" (links) ist nie länger als der „Umweg" (rechts).

---

## Betragsgleichungen

### Lösen von $|x| = a$

Für $a \geq 0$ hat die Gleichung $|x| = a$ genau **zwei Lösungen**:

$$|x| = a \quad \Leftrightarrow \quad x = a \text{ oder } x = -a$$

**Beispiel:** $|x| = 3$

Lösung: $x = 3$ oder $x = -3$

Lösungsmenge: $\mathbb{L} = \{-3, 3\}$

```
    ←──┬────┬────┬────┬────┬────┬────┬──→
      -4   -3   -2   -1    0    1    2    3    4
            ●                        ●
           -3                        3
           ←───── Abstand 3 ─────→
```

### Lösen von $|x - c| = a$

$$|x - c| = a \quad \Leftrightarrow \quad x = c + a \text{ oder } x = c - a$$

**Beispiel:** $|x - 2| = 5$

Lösung: $x = 2 + 5 = 7$ oder $x = 2 - 5 = -3$

Lösungsmenge: $\mathbb{L} = \{-3, 7\}$

> [!tip] **Interpretation**
> $|x - c| = a$ bedeutet: „Der Abstand von $x$ zu $c$ ist $a$."

---

## Betragsungleichungen

### Typ 1: $|x| < a$ (Abstand kleiner als $a$)

$$|x| < a \quad \Leftrightarrow \quad -a < x < a$$

**Beispiel:** $|x| < 3$

Lösung: $-3 < x < 3$, also das Intervall $(-3, 3)$

```
    ←──┬────┬────┬────┬────┬────┬────┬──→
      -4   -3   -2   -1    0    1    2    3    4
            ○────────────────────────○
                    Lösungsmenge
```

### Typ 2: $|x| > a$ (Abstand größer als $a$)

$$|x| > a \quad \Leftrightarrow \quad x < -a \text{ oder } x > a$$

**Beispiel:** $|x| > 2$

Lösung: $x < -2$ oder $x > 2$, also $(-\infty, -2) \cup (2, \infty)$

```
    ←──┬────┬────┬────┬────┬────┬────┬──→
      -4   -3   -2   -1    0    1    2    3    4
    ━━━━━━━━○              ○━━━━━━━━
        Lösungsmenge     Lösungsmenge
```

---

## Abstand zwischen zwei Zahlen

Der **Abstand** zwischen zwei Zahlen $a$ und $b$ auf dem Zahlenstrahl ist:

$$d(a, b) = |a - b| = |b - a|$$

**Beispiele:**

| Zahlen | Abstand | Berechnung |
|--------|---------|------------|
| $3$ und $7$ | $4$ | $|3 - 7| = |-4| = 4$ |
| $-2$ und $5$ | $7$ | $|-2 - 5| = |-7| = 7$ |
| $-4$ und $-1$ | $3$ | $|-4 - (-1)| = |-3| = 3$ |

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
> - Lösen von $|x| = a$: zwei Lösungen $x = \pm a$
> - Abstand: $d(a,b) = |a - b|$

> [!question] **Typische Prüfungsfragen**
> - Berechne $|-7| + |3|$.
> - Löse die Gleichung $|x - 4| = 6$.
> - Für welche $x$ gilt $|x| \leq 5$?
> - Bestimme den Abstand zwischen $-3$ und $8$.

## Quellen

- Papula, Lothar: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1. Springer, 2018.
- Forster, Otto: *Analysis 1*. Springer, 2016.

> [!tip] **Weiterführende Links**
> - [Mathebibel: Betrag](https://www.mathebibel.de/betrag)
> - [[10-Rechenregeln|Nächstes Kapitel: Rechenregeln]]
