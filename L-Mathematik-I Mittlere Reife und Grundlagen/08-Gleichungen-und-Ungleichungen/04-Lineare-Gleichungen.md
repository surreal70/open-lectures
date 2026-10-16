---
title: "Lineare Gleichungen"
created: 2026-10-13
modified: 2026-10-13
chapter: "08"
section: "04"
status: "draft - review pending"
type: lecture
keywords:
  - Lineare Gleichung
  - Erste Grades
  - Lösung
  - Normalform
---

# Lineare Gleichungen

> [!info] Lernziele
> - Lineare Gleichungen erkennen und in Normalform bringen
> - Systematisch lineare Gleichungen lösen können
> - Sonderfälle (keine Lösung, unendlich viele Lösungen) identifizieren
> - Lösungen verifizieren

## Definition

Eine **lineare Gleichung** (Gleichung ersten Grades) ist eine Gleichung, in der die Variable nur in der ersten Potenz vorkommt.

### Normalform

$$ax + b = 0 \quad \text{mit } a \neq 0$$

- $a$: Koeffizient der Variablen
- $b$: Konstante
- $x$: Variable

### Allgemeine Form

$$ax + b = cx + d$$

> [!example] Beispiele für lineare Gleichungen
> - $3x + 5 = 14$ ✓
> - $2x - 7 = x + 3$ ✓
> - $\frac{x}{4} = 8$ ✓
> - $x^2 + 3 = 12$ ✗ (quadratisch)

## Lösungsverfahren

### Standardvorgehen

1. Vereinfachen (Klammern auflösen, zusammenfassen)
2. Alle Terme mit $x$ auf eine Seite bringen
3. Alle Konstanten auf die andere Seite bringen
4. Durch den Koeffizienten von $x$ dividieren
5. Probe durchführen

### Beispiel 1: Einfache lineare Gleichung

$$5x - 3 = 22$$

$$5x = 25 \quad | +3$$
$$x = 5 \quad | :5$$

**Probe**: $5 \cdot 5 - 3 = 25 - 3 = 22$ ✓

### Beispiel 2: Variable auf beiden Seiten

$$7x - 4 = 3x + 12$$

$$7x - 3x = 12 + 4 \quad | -3x, +4$$
$$4x = 16$$
$$x = 4 \quad | :4$$

**Probe**: $7 \cdot 4 - 4 = 28 - 4 = 24$ und $3 \cdot 4 + 12 = 12 + 12 = 24$ ✓

### Beispiel 3: Mit Brüchen

$$\frac{2x}{3} + 1 = 5$$

$$\frac{2x}{3} = 4 \quad | -1$$
$$2x = 12 \quad | \cdot 3$$
$$x = 6 \quad | :2$$

**Probe**: $\frac{2 \cdot 6}{3} + 1 = \frac{12}{3} + 1 = 4 + 1 = 5$ ✓

## Sonderfälle

### Fall 1: Keine Lösung (Widerspruch)

$$2x + 5 = 2x - 3$$
$$5 = -3 \quad | -2x$$

Diese Aussage ist **falsch** – die Gleichung hat **keine Lösung**.

$$\mathbb{L} = \{\} = \emptyset$$

> [!note] Interpretation
> Es gibt keinen Wert für $x$, der die Gleichung erfüllen kann. Die Gleichung ist ein **Widerspruch**.

### Fall 2: Unendlich viele Lösungen (Identität)

$$3x + 6 = 3(x + 2)$$
$$3x + 6 = 3x + 6$$
$$0 = 0 \quad | -3x, -6$$

Diese Aussage ist **immer wahr** – jeder Wert für $x$ ist eine Lösung.

$$\mathbb{L} = \mathbb{R}$$

> [!note] Interpretation
> Die Gleichung ist eine **Identität** – beide Seiten sind für alle $x$ gleich.

### Übersicht der Fälle

| Ergebnis | Bedeutung | Lösungsmenge |
|---|---|---|
| $x = \text{Zahl}$ | Eindeutige Lösung | $\mathbb{L} = \{\text{Zahl}\}$ |
| Wahre Aussage ($0 = 0$) | Identität | $\mathbb{L} = \mathbb{R}$ |
| Falsche Aussage ($5 = 3$) | Widerspruch | $\mathbb{L} = \emptyset$ |

## Komplexere Beispiele

### Mit mehreren Brüchen

$$\frac{x-1}{2} + \frac{x+3}{4} = 3$$

**Schritt 1**: Hauptnenner bestimmen (hier: 4)

$$\frac{2(x-1)}{4} + \frac{x+3}{4} = 3$$

**Schritt 2**: Mit Hauptnenner multiplizieren

$$2(x-1) + (x+3) = 12$$

**Schritt 3**: Auflösen und vereinfachen

$$2x - 2 + x + 3 = 12$$
$$3x + 1 = 12$$
$$3x = 11$$
$$x = \frac{11}{3}$$

### Mit Dezimalzahlen

$$0{,}5x + 1{,}2 = 2{,}7$$

**Tipp**: Mit 10 multiplizieren, um Dezimalzahlen zu eliminieren

$$5x + 12 = 27$$
$$5x = 15$$
$$x = 3$$

## Strategien und Tipps

> [!tip] Praktische Hinweise
> - **Brüche vermeiden**: Früh mit dem Hauptnenner multiplizieren
> - **Dezimalzahlen**: Mit passender Zehnerpotenz multiplizieren
> - **Vorzeichen**: Besonders beim Minuszeichen vor Klammern aufpassen
> - **Probe**: Immer in die Originalgleichung einsetzen

## Zusammenfassung

> [!abstract] Kernpunkte
> - Lineare Gleichungen haben die Variable nur in der 1. Potenz
> - Lösung durch systematisches Isolieren der Variablen
> - Drei mögliche Fälle: eine Lösung, keine Lösung, unendlich viele Lösungen
> - Bei Brüchen: Mit Hauptnenner multiplizieren
> - Probe sichert das Ergebnis ab

## Übungsaufgaben

Löse die folgenden linearen Gleichungen:

1. $4x + 9 = 25$
2. $6x - 5 = 2x + 11$
3. $3(x - 4) = 2x + 1$
4. $\frac{x}{3} + \frac{x}{6} = 5$
5. $5(x + 1) = 5x + 7$
6. $0{,}25x - 0{,}5 = 1{,}5$

---

**Navigation**: [[03-Ueberpruefung-von-Loesungen|← Überprüfung]] | [[00-Gleichungen-und-Ungleichungen-Index|Übersicht]] | [[05-Gleichungen-mit-Klammern|Gleichungen mit Klammern →]]
