---
title: "Bruchgleichungen (einfache Fälle)"
created: 2026-10-13
modified: 2026-10-13
chapter: "08"
section: "06"
status: "draft - review pending"
type: lecture
keywords:
  - Bruchgleichung
  - Hauptnenner
  - Definitionsbereich
  - Scheinlösung
---

# Bruchgleichungen (einfache Fälle)

> [!info] Lernziele
> - Bruchgleichungen erkennen und klassifizieren
> - Den Hauptnenner bestimmen und anwenden
> - Definitionsbereiche korrekt angeben
> - Scheinlösungen identifizieren und ausschließen

## Was sind Bruchgleichungen?

Eine **Bruchgleichung** ist eine Gleichung, bei der die Variable im Nenner eines Bruchs vorkommt.

> [!example] Beispiele
> - $\frac{3}{x} = 6$ ← Variable im Nenner
> - $\frac{x+1}{x-2} = 3$ ← Variable im Nenner
> - $\frac{x}{3} = 5$ ← keine Bruchgleichung (Variable nur im Zähler)

## Definitionsbereich

> [!warning] Wichtig
> Division durch Null ist nicht erlaubt! Werte, die den Nenner zu Null machen, müssen ausgeschlossen werden.

### Bestimmung des Definitionsbereichs

1. Nenner = 0 setzen
2. Nach der Variablen auflösen
3. Diese Werte aus dem Definitionsbereich ausschließen

> [!example] Beispiel
> $$\frac{5}{x-3} = 2$$
> 
> Nenner: $x - 3 = 0 \Rightarrow x = 3$
> 
> **Definitionsbereich**: $D = \mathbb{R} \setminus \{3\}$ oder $x \neq 3$

## Lösungsverfahren

### Grundprinzip

1. **Definitionsbereich** bestimmen
2. Mit dem **Hauptnenner** multiplizieren
3. Entstandene Gleichung **lösen**
4. **Probe** durchführen (Scheinlösungen ausschließen)

### Beispiel 1: Einfache Bruchgleichung

$$\frac{6}{x} = 2$$

**Definitionsbereich**: $x \neq 0$

**Lösung**: Multiplikation mit $x$
$$6 = 2x$$
$$x = 3$$

**Probe**: $\frac{6}{3} = 2$ ✓

$x = 3$ liegt im Definitionsbereich ✓

$$\mathbb{L} = \{3\}$$

### Beispiel 2: Mit Term im Nenner

$$\frac{12}{x+2} = 4$$

**Definitionsbereich**: $x + 2 \neq 0 \Rightarrow x \neq -2$

**Lösung**: Multiplikation mit $(x+2)$
$$12 = 4(x+2)$$
$$12 = 4x + 8$$
$$4 = 4x$$
$$x = 1$$

**Probe**: $\frac{12}{1+2} = \frac{12}{3} = 4$ ✓

$$\mathbb{L} = \{1\}$$

## Bruchgleichungen mit mehreren Brüchen

### Hauptnenner finden

Der **Hauptnenner** ist das kleinste gemeinsame Vielfache (kgV) aller Nenner.

| Nenner | Hauptnenner |
|---|---|
| $2$ und $3$ | $6$ |
| $x$ und $2$ | $2x$ |
| $(x-1)$ und $(x+1)$ | $(x-1)(x+1)$ |

### Beispiel 3: Zwei Brüche

$$\frac{x}{2} + \frac{x}{3} = 10$$

**Definitionsbereich**: $D = \mathbb{R}$ (keine Variable im Nenner)

**Hauptnenner**: 6

**Multiplikation mit 6**:
$$\frac{6x}{2} + \frac{6x}{3} = 60$$
$$3x + 2x = 60$$
$$5x = 60$$
$$x = 12$$

**Probe**: $\frac{12}{2} + \frac{12}{3} = 6 + 4 = 10$ ✓

### Beispiel 4: Variable im Nenner bei mehreren Brüchen

$$\frac{3}{x} + \frac{2}{x} = 10$$

**Definitionsbereich**: $x \neq 0$

**Zusammenfassen** (gleicher Nenner):
$$\frac{5}{x} = 10$$

**Multiplikation mit $x$**:
$$5 = 10x$$
$$x = \frac{1}{2}$$

**Probe**: $\frac{3}{\frac{1}{2}} + \frac{2}{\frac{1}{2}} = 6 + 4 = 10$ ✓

## Scheinlösungen

> [!danger] Wichtig
> Eine **Scheinlösung** ist ein berechneter Wert, der nicht im Definitionsbereich liegt. Sie muss ausgeschlossen werden!

### Beispiel: Scheinlösung erkennen

$$\frac{x+3}{x-2} = \frac{5}{x-2}$$

**Definitionsbereich**: $x \neq 2$

**Multiplikation mit $(x-2)$**:
$$x + 3 = 5$$
$$x = 2$$

**Prüfung**: $x = 2$ liegt **nicht** im Definitionsbereich!

$$\mathbb{L} = \emptyset$$

Die Gleichung hat **keine Lösung**.

## Zusammenfassung des Lösungswegs

```
┌─────────────────────────────────────┐
│ 1. Definitionsbereich bestimmen     │
│    (Nenner ≠ 0)                     │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ 2. Hauptnenner finden               │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ 3. Mit Hauptnenner multiplizieren   │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ 4. Entstandene Gleichung lösen      │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ 5. Lösung im D-Bereich? → Probe     │
└─────────────────────────────────────┘
```

## Typische Fehler

> [!warning] Vermeiden Sie diese Fehler
> - Definitionsbereich vergessen
> - Nicht alle Terme mit dem Hauptnenner multiplizieren
> - Scheinlösungen nicht ausschließen
> - Probe in die umgeformte statt in die Originalgleichung einsetzen

## Zusammenfassung

> [!abstract] Kernpunkte
> - Bei Bruchgleichungen steht die Variable im Nenner
> - Der Definitionsbereich schließt Werte aus, die den Nenner zu Null machen
> - Lösung durch Multiplikation mit dem Hauptnenner
> - Scheinlösungen müssen durch Prüfung des Definitionsbereichs erkannt werden
> - Die Probe erfolgt immer in der Originalgleichung

## Übungsaufgaben

Bestimme jeweils den Definitionsbereich und löse:

1. $\frac{8}{x} = 4$
2. $\frac{15}{x-1} = 5$
3. $\frac{x}{4} + \frac{x}{6} = 5$
4. $\frac{2}{x} + \frac{3}{x} = 1$
5. $\frac{x+2}{x-3} = 2$
6. $\frac{6}{x+1} = \frac{6}{x+1}$ (Sonderfall!)

---

**Navigation**: [[05-Gleichungen-mit-Klammern|← Klammern]] | [[00-Gleichungen-und-Ungleichungen-Index|Übersicht]] | [[07-Lineare-Ungleichungen|Lineare Ungleichungen →]]
