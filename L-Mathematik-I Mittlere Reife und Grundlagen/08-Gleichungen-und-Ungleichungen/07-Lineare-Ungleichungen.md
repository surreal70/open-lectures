---
title: "Lineare Ungleichungen"
created: 2026-10-13
modified: 2026-10-13
chapter: "08"
section: "07"
status: "draft - review pending"
type: lecture
keywords:
  - Ungleichung
  - Intervall
  - Lösungsmenge
  - Vorzeichenwechsel
---

# Lineare Ungleichungen

> [!info] Lernziele
> - Den Unterschied zwischen Gleichungen und Ungleichungen verstehen
> - Ungleichungen systematisch lösen können
> - Die Vorzeichenregel bei Multiplikation/Division anwenden
> - Lösungsmengen in Intervallschreibweise und grafisch darstellen

## Ungleichungen vs. Gleichungen

| Gleichung | Ungleichung |
|---|---|
| $2x + 3 = 11$ | $2x + 3 < 11$ |
| Genau eine Lösung (meist) | Unendlich viele Lösungen (meist) |
| $x = 4$ | $x < 4$ (alle Zahlen kleiner als 4) |

### Ungleichungszeichen

| Zeichen | Bedeutung | Beispiel |
|---|---|---|
| $<$ | kleiner als | $x < 5$ |
| $>$ | größer als | $x > 3$ |
| $\leq$ | kleiner oder gleich | $x \leq 7$ |
| $\geq$ | größer oder gleich | $x \geq -2$ |

## Lösungsverfahren

### Grundregel

Ungleichungen werden **ähnlich wie Gleichungen** gelöst, mit einer wichtigen Ausnahme:

> [!danger] Vorzeichenregel
> Bei **Multiplikation oder Division mit einer negativen Zahl** muss das **Ungleichungszeichen umgedreht** werden!

### Beispiel 1: Einfache Ungleichung

$$3x + 5 < 14$$
$$3x < 9 \quad | -5$$
$$x < 3 \quad | :3$$

**Lösungsmenge**: $\mathbb{L} = \{x \in \mathbb{R} \mid x < 3\}$ oder $\mathbb{L} = (-\infty, 3)$

### Beispiel 2: Mit negativer Division

$$-2x + 6 > 10$$
$$-2x > 4 \quad | -6$$
$$x < -2 \quad | :(-2) \text{ ← Zeichen dreht sich!}$$

**Lösungsmenge**: $\mathbb{L} = (-\infty, -2)$

## Die Vorzeichenregel im Detail

### Warum dreht sich das Zeichen?

Betrachte die wahre Aussage: $3 < 5$

| Operation | Ergebnis | Aussage |
|---|---|---|
| $\cdot 2$ | $6 < 10$ | wahr ✓ |
| $\cdot (-2)$ | $-6 < -10$? | falsch! |
| $\cdot (-2)$ mit Umdrehen | $-6 > -10$ | wahr ✓ |

> [!tip] Merksatz
> Multiplizieren oder Dividieren mit einer **negativen Zahl** → Ungleichungszeichen **umkehren**!

## Darstellung der Lösungsmenge

### Mengennotation

$$\mathbb{L} = \{x \in \mathbb{R} \mid x > 2\}$$
„Alle reellen Zahlen $x$, für die $x > 2$ gilt"

### Intervallschreibweise

| Ungleichung | Intervall |
|---|---|
| $x > 2$ | $(2, +\infty)$ |
| $x \geq 2$ | $[2, +\infty)$ |
| $x < 5$ | $(-\infty, 5)$ |
| $x \leq 5$ | $(-\infty, 5]$ |
| $2 < x < 5$ | $(2, 5)$ |
| $2 \leq x \leq 5$ | $[2, 5]$ |

> [!note] Konvention
> - Runde Klammer $($ oder $)$: Grenzwert **nicht** enthalten
> - Eckige Klammer $[$ oder $]$: Grenzwert **enthalten**
> - Bei $\pm\infty$ immer runde Klammer

### Grafische Darstellung (Zahlengerade)

**Beispiel**: $x \geq 2$

```
────────┬────────────────────→
       [●========================>
        2
```

**Beispiel**: $x < -1$

```
←════════════════●)─────────────→
                 -1
```

- Ausgefüllter Punkt ($\bullet$): Wert gehört dazu ($\leq$ oder $\geq$)
- Offener Punkt ($\circ$): Wert gehört nicht dazu ($<$ oder $>$)

## Ungleichungen mit Variablen auf beiden Seiten

$$5x - 3 > 2x + 9$$

**Schritt 1**: Variable auf eine Seite
$$5x - 2x > 9 + 3$$
$$3x > 12$$

**Schritt 2**: Isolieren
$$x > 4$$

**Lösungsmenge**: $\mathbb{L} = (4, +\infty)$

## Doppelungleichungen

Eine **Doppelungleichung** gibt einen Bereich an:

$$-3 < 2x + 1 \leq 7$$

**Lösung**: Alle drei Teile gleichzeitig umformen

$$-3 < 2x + 1 \leq 7 \quad | -1$$
$$-4 < 2x \leq 6 \quad | :2$$
$$-2 < x \leq 3$$

**Lösungsmenge**: $\mathbb{L} = (-2, 3]$

```
────────(○───────────────●]────────→
       -2                 3
```

## Sonderfälle

### Alle reellen Zahlen als Lösung

$$2x + 1 > 2x - 5$$
$$1 > -5$$ (immer wahr)

$$\mathbb{L} = \mathbb{R}$$

### Keine Lösung

$$3x + 2 < 3x - 4$$
$$2 < -4$$ (nie wahr)

$$\mathbb{L} = \emptyset$$

## Zusammenfassung

> [!abstract] Kernpunkte
> - Ungleichungen werden wie Gleichungen gelöst
> - Bei Multiplikation/Division mit negativer Zahl: Zeichen umdrehen!
> - Lösungsmengen sind oft Intervalle mit unendlich vielen Werten
> - Darstellung: Mengennotation, Intervallschreibweise oder Zahlengerade
> - $<$, $>$ → offenes Intervall; $\leq$, $\geq$ → geschlossenes Intervall

## Übungsaufgaben

Löse und gib die Lösungsmenge in Intervallschreibweise an:

1. $2x + 7 < 15$
2. $-3x \geq 12$
3. $4x - 5 > x + 7$
4. $-2(x - 3) \leq 10$
5. $1 < 3x - 2 \leq 13$
6. $5 - 2x > 3x + 20$

Stelle die Lösungen auf einer Zahlengeraden dar.

---

**Navigation**: [[06-Bruchgleichungen|← Bruchgleichungen]] | [[00-Gleichungen-und-Ungleichungen-Index|Übersicht]] | [[08-Quadratische-Gleichungen|Quadratische Gleichungen →]]
