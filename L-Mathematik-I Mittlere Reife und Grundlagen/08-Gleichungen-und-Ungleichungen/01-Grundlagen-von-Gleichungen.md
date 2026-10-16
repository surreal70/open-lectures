---
title: "Grundlagen von Gleichungen"
created: 2026-10-13
modified: 2026-10-13
chapter: "08"
section: "01"
status: "draft - review pending"
type: lecture
keywords:
  - Gleichung
  - Variable
  - Lösung
  - Lösungsmenge
  - Aussage
---

# Grundlagen von Gleichungen

> [!info] Lernziele
> - Den Begriff der Gleichung mathematisch definieren können
> - Variablen und ihre Rolle in Gleichungen verstehen
> - Lösungen und Lösungsmengen bestimmen können
> - Arten von Gleichungen unterscheiden können

## Was ist eine Gleichung?

Eine **Gleichung** ist eine mathematische Aussage, die behauptet, dass zwei Ausdrücke denselben Wert haben. Die beiden Seiten werden durch ein Gleichheitszeichen (=) verbunden.

### Bestandteile einer Gleichung

$$\underbrace{3x + 5}_{\text{linke Seite}} = \underbrace{17}_{\text{rechte Seite}}$$

**Elemente**:
- **Linke Seite**: Der Ausdruck links vom Gleichheitszeichen
- **Rechte Seite**: Der Ausdruck rechts vom Gleichheitszeichen
- **Variable** (Unbekannte): Der Buchstabe, dessen Wert gesucht wird (hier: $x$)
- **Koeffizienten**: Zahlen vor der Variablen (hier: 3)
- **Konstanten**: Feste Zahlenwerte (hier: 5 und 17)

## Variablen und Unbekannte

### Begriff der Variablen

Eine **Variable** ist ein Symbol (meist ein Buchstabe), das als Platzhalter für einen noch unbekannten Wert steht.

| Übliche Variablen | Verwendung |
|---|---|
| $x, y, z$ | Standardvariablen |
| $a, b, c$ | Parameter oder Koeffizienten |
| $n, m, k$ | Natürliche Zahlen, Anzahlen |
| $t$ | Zeit |

### Definitionsbereich

Der **Definitionsbereich** gibt an, welche Werte die Variable annehmen darf.

> [!example] Beispiele für Definitionsbereiche
> - Bei $x + 3 = 7$: $x \in \mathbb{R}$ (alle reellen Zahlen erlaubt)
> - Bei $\frac{1}{x} = 2$: $x \in \mathbb{R} \setminus \{0\}$ (Division durch Null ausgeschlossen)
> - Bei Altersberechnungen: $x \in \mathbb{N}_0$ (nur nicht-negative ganze Zahlen sinnvoll)

## Lösungen und Lösungsmengen

### Was ist eine Lösung?

Eine **Lösung** einer Gleichung ist ein Wert für die Variable, der die Gleichung zu einer wahren Aussage macht.

> [!example] Beispiel
> Gleichung: $2x + 3 = 11$
> 
> Probe mit $x = 4$:
> $$2 \cdot 4 + 3 = 8 + 3 = 11 \checkmark$$
> 
> Also ist $x = 4$ eine Lösung.

### Lösungsmenge

Die **Lösungsmenge** $\mathbb{L}$ enthält alle Lösungen einer Gleichung.

**Mögliche Fälle**:

| Fall | Beschreibung | Beispiel | Lösungsmenge |
|---|---|---|---|
| Genau eine Lösung | Eindeutig lösbar | $2x = 6$ | $\mathbb{L} = \{3\}$ |
| Unendlich viele Lösungen | Identität | $x + 1 = 1 + x$ | $\mathbb{L} = \mathbb{R}$ |
| Keine Lösung | Widerspruch | $x + 1 = x$ | $\mathbb{L} = \{\}$ |

## Arten von Gleichungen

### Nach Variablenanzahl

- **Eine Variable**: $3x + 5 = 14$
- **Zwei Variablen**: $2x + 3y = 12$
- **Mehrere Variablen**: $x + y + z = 10$

### Nach höchster Potenz

| Gleichungstyp | Höchste Potenz | Beispiel |
|---|---|---|
| Linear | 1 | $3x + 2 = 8$ |
| Quadratisch | 2 | $x^2 - 4x + 3 = 0$ |
| Kubisch | 3 | $x^3 - x = 0$ |

### Spezielle Gleichungstypen

- **Bruchgleichungen**: Enthalten Variable im Nenner: $\frac{3}{x} = 6$
- **Wurzelgleichungen**: Enthalten Variable unter Wurzel: $\sqrt{x} = 3$
- **Betragsgleichungen**: Enthalten Variable im Betrag: $|x - 2| = 5$

## Das Waagschalen-Prinzip

Eine Gleichung kann als **Waage im Gleichgewicht** verstanden werden:

```
    ┌───────┴───────┐
    │               │
 ┌──┴──┐         ┌──┴──┐
 │3x+5 │         │ 17  │
 └─────┘         └─────┘
```

**Regeln**:
- Beide Seiten müssen immer gleich behandelt werden
- Was links geschieht, muss auch rechts geschehen
- Das Gleichgewicht darf nie gestört werden

> [!tip] Merksatz
> Was du auf der einen Seite tust, musst du auch auf der anderen Seite tun – sonst kippt die Waage!

## Zusammenfassung

> [!abstract] Kernpunkte
> - Eine Gleichung ist eine Aussage über die Gleichheit zweier Ausdrücke
> - Die Variable ist der unbekannte Wert, der gesucht wird
> - Die Lösungsmenge enthält alle Werte, die die Gleichung erfüllen
> - Das Waagschalen-Prinzip hilft beim Verständnis von Umformungen

## Übungsaufgaben

1. Bestimme, ob die folgenden Werte Lösungen sind:
   - $x = 3$ für $2x - 1 = 5$
   - $x = -2$ für $3x + 8 = 2$
   - $x = 0$ für $5x = 0$

2. Gib den Definitionsbereich an:
   - $\frac{5}{x-2} = 1$
   - $\sqrt{x} = 4$

3. Klassifiziere die Gleichungen nach Typ:
   - $4x - 7 = 13$
   - $x^2 = 25$
   - $\frac{x+1}{x} = 3$

---

**Navigation**: [[00-Gleichungen-und-Ungleichungen-Index|← Übersicht]] | [[02-Aequivalenzumformungen|Äquivalenzumformungen →]]
