---
author: Andreas Hümmer
title: Wiederholung des Funktionsbegriffs
tags:
  - content
  - mathe
  - funktionen
  - grundbegriffe
  - definition
created: 2025-01-22
modified: 2025-01-22
---

# Wiederholung des Funktionsbegriffs

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die formale Definition einer Funktion kennen und anwenden können
> - Verschiedene Darstellungsformen von Funktionen (Graph, Tabelle, Term, Pfeildiagramm) beherrschen
> - Zwischen Funktion und Relation unterscheiden können
> - Grundlegende Begriffe wie Argument, Funktionswert, Urbild und Bild sicher verwenden können

---

## Überblick

Eine Funktion ist eines der zentralen Konzepte der Mathematik. Sie beschreibt eine eindeutige Zuordnung zwischen zwei Mengen und ermöglicht es, Zusammenhänge präzise zu modellieren. In diesem Kapitel wiederholen und vertiefen wir den Funktionsbegriff als Grundlage für alle weiteren Betrachtungen.

## Formale Definition einer Funktion

### Definition

Eine **Funktion** $f$ von einer Menge $D$ in eine Menge $W$ ist eine Vorschrift, die jedem Element $x \in D$ **genau ein** Element $y \in W$ zuordnet.

**Schreibweisen:**

$$f: D \to W, \quad x \mapsto f(x)$$

Dabei heißt:
- $D$ die **Definitionsmenge** (oder Definitionsbereich)
- $W$ die **Wertemenge** (oder Zielmenge)
- $x$ das **Argument** (oder die unabhängige Variable)
- $f(x) = y$ der **Funktionswert** (oder die abhängige Variable)

### Beispiel

Die Funktion $f: \mathbb{R} \to \mathbb{R}$ mit $f(x) = x^2$ ordnet jeder reellen Zahl ihr Quadrat zu:

| $x$  | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
|------|------|------|-----|-----|-----|-----|
| $f(x)$ | $4$ | $1$ | $0$ | $1$ | $4$ | $9$ |

## Darstellungsformen von Funktionen

### 1. Analytische Darstellung (Funktionsterm)

Die Zuordnungsvorschrift wird durch einen mathematischen Ausdruck angegeben:

$$f(x) = 2x^3 - 5x + 1$$

**Vorteile:** Exakte Berechnung aller Funktionswerte, algebraische Manipulation möglich.

### 2. Graphische Darstellung

Der **Graph** einer Funktion $f$ ist die Menge aller Punkte $(x, f(x))$:

$$G_f = \{(x, y) \in D \times W \mid y = f(x)\}$$

Die graphische Darstellung ermöglicht eine visuelle Erfassung des Funktionsverhaltens.

**Vertikaler Linientest:** Eine Kurve ist genau dann der Graph einer Funktion, wenn jede vertikale Gerade die Kurve in höchstens einem Punkt schneidet.

### 3. Tabellarische Darstellung

Wertepaare werden in einer Tabelle aufgelistet. Diese Darstellung ist besonders bei Messdaten üblich:

```
x    | 0    | 1    | 2    | 3    | 4
f(x) | 2.1  | 3.5  | 4.8  | 6.2  | 7.9
```

**Nachteil:** Nur diskrete Werte, Zwischenwerte müssen interpoliert werden.

### 4. Pfeildiagramm

Bei endlichen Mengen kann die Zuordnung durch Pfeile visualisiert werden:

```
  D           W
┌───┐       ┌───┐
│ a │ ───→  │ 1 │
│ b │ ───→  │ 2 │
│ c │ ───→  │ 2 │
└───┘       └───┘
```

## Funktion versus Relation

### Definition einer Relation

Eine **Relation** $R$ zwischen den Mengen $A$ und $B$ ist eine Teilmenge des kartesischen Produkts $A \times B$:

$$R \subseteq A \times B$$

### Unterschied zur Funktion

| Eigenschaft | Relation | Funktion |
|------------|----------|----------|
| Zuordnung | beliebig | eindeutig |
| Mehrere Bilder möglich | ja | nein |
| Kein Bild möglich | ja | nein |

**Beispiel:** Die Relation „ist Quadratwurzel von" zwischen $\mathbb{R}$ und $\mathbb{R}_{\geq 0}$:
- Die Zahl $4$ hat zwei Quadratwurzeln: $2$ und $-2$
- Dies ist **keine Funktion**, da die Zuordnung nicht eindeutig ist

Die Hauptquadratwurzelfunktion $f(x) = \sqrt{x}$ ist hingegen eine Funktion, da sie nur die positive Wurzel zuordnet.

## Wichtige Begriffe

### Urbild und Bild

Für eine Funktion $f: D \to W$ und eine Teilmenge $M \subseteq D$:

- Das **Bild** von $M$ unter $f$:
$$f(M) = \{f(x) \mid x \in M\} = \{y \in W \mid \exists x \in M: f(x) = y\}$$

- Das **Urbild** einer Menge $N \subseteq W$:
$$f^{-1}(N) = \{x \in D \mid f(x) \in N\}$$

**Beispiel:** Für $f(x) = x^2$ mit $D = \mathbb{R}$:
- $f(\{-1, 2, 3\}) = \{1, 4, 9\}$
- $f^{-1}(\{4\}) = \{-2, 2\}$

### Injektivität, Surjektivität, Bijektivität

Eine Funktion $f: D \to W$ heißt:

**Injektiv (eineindeutig):** Verschiedene Argumente haben verschiedene Bilder:
$$\forall x_1, x_2 \in D: x_1 \neq x_2 \Rightarrow f(x_1) \neq f(x_2)$$

Äquivalent: $f(x_1) = f(x_2) \Rightarrow x_1 = x_2$

**Surjektiv:** Jedes Element der Wertemenge wird angenommen:
$$\forall y \in W \, \exists x \in D: f(x) = y$$

**Bijektiv:** Injektiv und surjektiv zugleich – eine umkehrbare Zuordnung.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Definitionsbereich]] – Bestimmung der Menge aller zulässigen Argumente
- → [[Wertebereich]] – Bestimmung der Menge aller möglichen Funktionswerte
- → [[Umkehrfunktionen]] – Existenz und Bildung der Umkehrfunktion bei bijektiven Funktionen
- → [[Reelle-Zahlen-und-Intervalle]] – Grundlagen zu Zahlenmengen und Intervallen

> [!warning] **Prüfungsrelevant**
> - Formale Definition einer Funktion kennen und erklären können
> - Unterschied zwischen Funktion und Relation an Beispielen erläutern
> - Injektivität, Surjektivität und Bijektivität überprüfen
> - Verschiedene Darstellungsformen ineinander überführen

> [!question] **Typische Prüfungsfragen**
> - Erkläre den Unterschied zwischen einer Funktion und einer Relation.
> - Zeige, dass die Funktion $f(x) = 2x + 1$ bijektiv auf $\mathbb{R}$ ist.
> - Warum ist $f(x) = x^2$ auf $\mathbb{R}$ nicht injektiv? Wie kann man den Definitionsbereich einschränken, um Injektivität zu erreichen?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I. N. et al.: Taschenbuch der Mathematik. Verlag Harri Deutsch, 2012.
- ISB Bayern: Lehrplan Mathematik Gymnasium.

> [!tip] **Weiterführende Links**
> - [[03-Elementare-Funktionstypen-Index|Elementare Funktionstypen]] – Überblick über verschiedene Funktionsklassen
> - [[Glossar]] – Mathematische Fachbegriffe
