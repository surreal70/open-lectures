---
title: "Quadratische Gleichungen"
created: 2026-10-13
modified: 2025-07-21
chapter: "08"
section: "08"
status: "draft - review pending"
type: lecture
keywords:
  - Quadratische Gleichung
  - Normalform
  - Reinquadratische Gleichung
  - Diskriminante
---

# Quadratische Gleichungen

> [!info] Lernziele
> - Quadratische Gleichungen erkennen und klassifizieren
> - Die Normalform herstellen können
> - Einfache quadratische Gleichungen durch Wurzelziehen lösen
> - Das Konzept der Diskriminante verstehen

## Historischer Kontext

Quadratische Gleichungen gehören zu den ältesten mathematischen Problemen. Die **Babylonier** lösten sie bereits um 2000 v. Chr. – allerdings nur für positive Lösungen, da negative Zahlen als „nicht existent" galten. Sie formulierten Aufgaben wie: „Die Fläche eines Quadrats plus die Seitenlänge ergibt 0;45" (in ihrem Sexagesimalsystem, entspricht etwa 3/4).

Die **indischen Mathematiker** machten im frühen Mittelalter entscheidende Fortschritte. **Brahmagupta** (598–668 n. Chr.) formulierte erstmals Regeln für negative Zahlen und akzeptierte sie als gültige Lösungen. Er schrieb: „Die Zahl, deren Quadrat, vermehrt um 1, gleich 10 ist" – und gab sowohl $x = 3$ als auch $x = -3$ als Lösung an.

Die allgemeine **Lösungsformel** (heute als p-q-Formel oder Mitternachtsformel bekannt) wurde im 16. Jahrhundert in Europa standardisiert, basierend auf den Arbeiten arabischer und indischer Mathematiker.

> [!tip] **Warum „quadratisch"?**
> Der Name kommt vom lateinischen „quadratus" (Quadrat). Geometrisch gesehen: Wenn $x$ die Seitenlänge eines Quadrats ist, dann ist $x^2$ seine Fläche. Quadratische Gleichungen beschreiben also ursprünglich Flächenprobleme.

## Definition

Eine **quadratische Gleichung** ist eine Gleichung, in der die Variable in der zweiten Potenz vorkommt (und nicht höher). Sie ist damit die nächste Stufe nach den linearen Gleichungen.

### Allgemeine Form

$$ax^2 + bx + c = 0 \quad \text{mit } a \neq 0$$

- $a$: Koeffizient von $x^2$ (≠ 0)
- $b$: Koeffizient von $x$
- $c$: Konstante (absolutes Glied)

### Normalform

$$x^2 + px + q = 0$$

Die Normalform erhält man durch Division durch $a$:
$$\frac{ax^2 + bx + c}{a} = 0 \Rightarrow x^2 + \frac{b}{a}x + \frac{c}{a} = 0$$

Dabei ist $p = \frac{b}{a}$ und $q = \frac{c}{a}$.

> [!example] Beispiel: Umwandlung in Normalform
> $$2x^2 + 6x - 8 = 0 \quad | :2$$
> $$x^2 + 3x - 4 = 0$$
> 
> Hier: $p = 3$ und $q = -4$

## Arten quadratischer Gleichungen

| Typ | Form | Beispiel |
|---|---|---|
| Allgemein | $ax^2 + bx + c = 0$ | $2x^2 + 5x - 3 = 0$ |
| Reinquadratisch | $ax^2 + c = 0$ (ohne $x$-Term) | $3x^2 - 12 = 0$ |
| Gemischt ohne c | $ax^2 + bx = 0$ | $x^2 - 4x = 0$ |

## Reinquadratische Gleichungen

Diese sind am einfachsten zu lösen, da nur $x^2$ und eine Konstante vorkommen.

### Lösungsmethode: Wurzelziehen

$$x^2 = k$$

| Fall | Lösung |
|---|---|
| $k > 0$ | $x = \pm\sqrt{k}$ (zwei Lösungen) |
| $k = 0$ | $x = 0$ (eine Lösung) |
| $k < 0$ | keine reelle Lösung |

> [!example] Beispiel 1: Zwei Lösungen
> $$x^2 = 25$$
> $$x = \pm\sqrt{25}$$
> $$x_1 = 5, \quad x_2 = -5$$

> [!example] Beispiel 2: Keine Lösung
> $$x^2 = -9$$
> 
> Es gibt keine reelle Zahl, deren Quadrat negativ ist.
> $$\mathbb{L} = \emptyset$$

### Ausführliches Beispiel

$$3x^2 - 48 = 0$$

$$3x^2 = 48 \quad | +48$$
$$x^2 = 16 \quad | :3$$
$$x = \pm 4$$

**Probe**: $3 \cdot (\pm 4)^2 - 48 = 3 \cdot 16 - 48 = 48 - 48 = 0$ ✓

## Gemischt ohne absolutes Glied

Gleichungen der Form $ax^2 + bx = 0$ können durch **Ausklammern** gelöst werden.

$$x^2 - 6x = 0$$
$$x(x - 6) = 0$$

Nach dem **Nullproduktsatz** gilt: Ein Produkt ist Null, wenn mindestens ein Faktor Null ist.

$$x = 0 \quad \text{oder} \quad x - 6 = 0$$
$$x_1 = 0, \quad x_2 = 6$$

> [!warning] **Häufiger Fehler: Division durch Variable**
> $$x^2 - 6x = 0$$
> $$x^2 = 6x \quad | :x$$ ← **FALSCH!** (Division durch möglicherweise 0)
> $$x = 6$$ ← Die Lösung $x = 0$ geht verloren!
>
> **Richtig** ist das Ausklammern:
> $$x^2 - 6x = 0$$
> $$x(x - 6) = 0$$
> $$x_1 = 0 \text{ oder } x_2 = 6$$
>
> Merke: Nie durch die Variable dividieren – dabei können Lösungen verloren gehen!

## Anzahl der Lösungen und Diskriminante

Die **Diskriminante** $D$ bestimmt die Anzahl der Lösungen:

$$D = p^2 - 4q \quad \text{(für Normalform)} \quad \text{oder} \quad D = b^2 - 4ac$$

| Diskriminante | Anzahl Lösungen |
|---|---|
| $D > 0$ | 2 verschiedene reelle Lösungen |
| $D = 0$ | 1 reelle Lösung (Doppellösung) |
| $D < 0$ | Keine reelle Lösung |

> [!example] Beispiel: Diskriminante bestimmen
> $$x^2 - 4x + 3 = 0$$
> 
> Hier: $p = -4$, $q = 3$
> 
> $$D = (-4)^2 - 4 \cdot 3 = 16 - 12 = 4 > 0$$
> 
> → Zwei verschiedene Lösungen

## Grafische Interpretation

Die Lösungen einer quadratischen Gleichung $ax^2 + bx + c = 0$ sind die **Nullstellen** der Parabel $y = ax^2 + bx + c$.

```
      y
      ↑
      │    ╭─╮
      │   ╱   ╲      D > 0: zwei Nullstellen
 ─────┼──●─────●──→ x
      │
```

```
      y
      ↑
      │    ╭─╮
      │   ╱   ╲      D = 0: eine Nullstelle
 ─────┼────●──────→ x
      │
```

```
      y
      ↑
      │    ╭─╮
      │   ╱   ╲      D < 0: keine Nullstelle
      │  ╱     ╲
 ─────┼──────────→ x
      │
```

## Zusammenfassung

> [!abstract] Kernpunkte
> - Quadratische Gleichungen haben $x^2$ als höchste Potenz
> - Die Normalform ist $x^2 + px + q = 0$
> - Reinquadratische Gleichungen ($x^2 = k$): Wurzelziehen
> - Gleichungen ohne Konstante ($x^2 + bx = 0$): Ausklammern
> - Die Diskriminante bestimmt die Anzahl der Lösungen
> - Nie durch $x$ dividieren – dabei können Lösungen verloren gehen!

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[09-Loesungsformel-quadratische-Gleichungen|Lösungsformel]] – Die p-q-Formel und Mitternachtsformel
- → [[10-Faktorisierung-quadratischer-Gleichungen|Faktorisierung]] – Alternative Lösungsmethode
- → [[06-Potenzen-Wurzeln-und-Zahlendarstellung/06-Quadratwurzeln|Quadratwurzeln]] – Mathematische Grundlage
- → [[09-Funktionen-und-Koordinatensysteme/09-Parabeln|Parabeln]] – Grafische Darstellung

## Übungsaufgaben

1. Bringe in Normalform: $3x^2 - 6x + 9 = 0$
2. Löse durch Wurzelziehen: $x^2 = 49$
3. Löse durch Wurzelziehen: $2x^2 - 50 = 0$
4. Löse durch Ausklammern: $x^2 + 7x = 0$
5. Bestimme die Diskriminante: $x^2 - 6x + 9 = 0$
6. Hat die Gleichung $x^2 + 4 = 0$ eine Lösung?

---

**Navigation**: [[07-Lineare-Ungleichungen|← Ungleichungen]] | [[00-Gleichungen-und-Ungleichungen-Index|Übersicht]] | [[09-Loesungsformel-quadratische-Gleichungen|Lösungsformel →]]
