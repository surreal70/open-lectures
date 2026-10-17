---
author: Andreas Hümmer
title: Reelle Zahlen und Intervalle
tags:
  - content
  - mathe
  - algebra
  - reelle-zahlen
  - intervalle
  - zahlbereiche
created: 2025-01-13
modified: 2025-01-13
---

# Reelle Zahlen und Intervalle

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die verschiedenen Zahlbereiche und ihre Beziehungen kennen
> - Mit der Intervallschreibweise sicher umgehen können
> - Mengenoperationen auf Intervalle anwenden können
> - Die Vollständigkeit der reellen Zahlen verstehen

---

## Überblick

Die reellen Zahlen bilden den grundlegenden Zahlbereich für die Analysis. Sie umfassen alle Zahlen, die auf dem Zahlenstrahl dargestellt werden können, einschließlich rationaler und irrationaler Zahlen. Ein sicherer Umgang mit Intervallen und Mengenoperationen ist essentiell für das Lösen von Ungleichungen und die Angabe von Definitionsbereichen.

## Die Zahlbereiche

Die Zahlbereiche lassen sich hierarchisch ordnen:

$$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}$$

### Natürliche Zahlen $\mathbb{N}$

$$\mathbb{N} = \{1, 2, 3, 4, \ldots\}$$

Manchmal wird auch $\mathbb{N}_0 = \{0, 1, 2, 3, \ldots\}$ verwendet.

### Ganze Zahlen $\mathbb{Z}$

$$\mathbb{Z} = \{\ldots, -3, -2, -1, 0, 1, 2, 3, \ldots\}$$

### Rationale Zahlen $\mathbb{Q}$

$$\mathbb{Q} = \left\{\frac{p}{q} \mid p \in \mathbb{Z}, q \in \mathbb{N}\right\}$$

Rationale Zahlen haben eine **endliche oder periodische** Dezimaldarstellung:
- $\frac{3}{4} = 0{,}75$ (endlich)
- $\frac{1}{3} = 0{,}\overline{3}$ (periodisch)

### Irrationale Zahlen

Zahlen, die **nicht** als Bruch darstellbar sind. Ihre Dezimaldarstellung ist **unendlich und nicht-periodisch**:
- $\sqrt{2} = 1{,}41421356\ldots$
- $\pi = 3{,}14159265\ldots$
- $e = 2{,}71828182\ldots$

### Reelle Zahlen $\mathbb{R}$

Die Menge aller rationalen und irrationalen Zahlen:

$$\mathbb{R} = \mathbb{Q} \cup \{\text{irrationale Zahlen}\}$$

> [!tip] **Irrationalitätsbeweis von $\sqrt{2}$**
> Der klassische Beweis erfolgt durch Widerspruch: Angenommen, $\sqrt{2} = \frac{p}{q}$ mit vollständig gekürztem Bruch. Dann ist $2q^2 = p^2$, also $p^2$ gerade, also $p$ gerade. Sei $p = 2k$. Dann $2q^2 = 4k^2$, also $q^2 = 2k^2$, also $q$ gerade. Widerspruch zur Kürzung.

## Intervalle

Ein **Intervall** ist eine zusammenhängende Teilmenge der reellen Zahlen.

### Intervalltypen

| Bezeichnung | Schreibweise | Menge | Beschreibung |
|-------------|--------------|-------|--------------|
| Abgeschlossenes Intervall | $[a, b]$ | $\{x \in \mathbb{R} \mid a \leq x \leq b\}$ | Mit Randpunkten |
| Offenes Intervall | $(a, b)$ oder $]a, b[$ | $\{x \in \mathbb{R} \mid a < x < b\}$ | Ohne Randpunkte |
| Halboffenes Intervall | $[a, b)$ oder $[a, b[$ | $\{x \in \mathbb{R} \mid a \leq x < b\}$ | Linker Rand enthalten |
| Halboffenes Intervall | $(a, b]$ oder $]a, b]$ | $\{x \in \mathbb{R} \mid a < x \leq b\}$ | Rechter Rand enthalten |

### Unbeschränkte Intervalle

| Schreibweise | Menge | Beschreibung |
|--------------|-------|--------------|
| $[a, \infty)$ | $\{x \in \mathbb{R} \mid x \geq a\}$ | Von $a$ bis Unendlich |
| $(a, \infty)$ | $\{x \in \mathbb{R} \mid x > a\}$ | Größer als $a$ |
| $(-\infty, b]$ | $\{x \in \mathbb{R} \mid x \leq b\}$ | Bis $b$ einschließlich |
| $(-\infty, b)$ | $\{x \in \mathbb{R} \mid x < b\}$ | Kleiner als $b$ |
| $(-\infty, \infty)$ | $\mathbb{R}$ | Alle reellen Zahlen |

> [!warning] **Unendlich ist keine Zahl**
> Bei $\infty$ steht **immer eine runde Klammer**, da Unendlich kein Element von $\mathbb{R}$ ist und nicht „erreicht" werden kann.

## Mengenoperationen mit Intervallen

### Vereinigung ($\cup$)

$$[1, 3] \cup [2, 5] = [1, 5]$$

$$[1, 2] \cup [3, 4] = [1, 2] \cup [3, 4]$$ (keine Vereinfachung möglich)

### Schnittmenge ($\cap$)

$$[1, 4] \cap [2, 6] = [2, 4]$$

$$[1, 2] \cap [3, 4] = \emptyset$$

### Differenz ($\setminus$)

$$[0, 5] \setminus [2, 3] = [0, 2) \cup (3, 5]$$

$$\mathbb{R} \setminus \{0\} = (-\infty, 0) \cup (0, \infty)$$

### Komplement

Das Komplement von $A$ bezüglich $\mathbb{R}$:

$$\overline{[2, 5]} = \mathbb{R} \setminus [2, 5] = (-\infty, 2) \cup (5, \infty)$$

## Anwendung: Definitionsbereiche

Die Intervallschreibweise wird häufig zur Angabe von Definitionsbereichen verwendet:

**Beispiel 1:** $f(x) = \sqrt{x - 2}$

Der Radikand muss nicht-negativ sein: $x - 2 \geq 0 \Rightarrow x \geq 2$

$$D_f = [2, \infty)$$

**Beispiel 2:** $f(x) = \frac{1}{x^2 - 4}$

Der Nenner darf nicht Null sein: $x^2 - 4 \neq 0 \Rightarrow x \neq \pm 2$

$$D_f = \mathbb{R} \setminus \{-2, 2\} = (-\infty, -2) \cup (-2, 2) \cup (2, \infty)$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Wiederholung-algebraischer-Grundlagen]] – Grundlegende Rechenoperationen
- → [[Ungleichungen]] – Lösungsmengen als Intervalle
- → [[Betrag-und-Betragsgleichungen]] – Betragsungleichungen und Intervalle
- → [[Definitionsbereich]] – Bestimmung von Definitionsbereichen

> [!warning] **Prüfungsrelevant**
> - Korrekte Verwendung der Intervallschreibweise (runde/eckige Klammern)
> - Mengenoperationen durchführen können
> - Definitionsbereiche in Intervallschreibweise angeben
> - Unterscheidung offener und abgeschlossener Intervalle

> [!question] **Typische Prüfungsfragen**
> - Gib den Definitionsbereich von $f(x) = \sqrt{4 - x^2}$ in Intervallschreibweise an.
> - Berechne $[-3, 2] \cap [0, 5]$ und $[-3, 2] \cup [0, 5]$.
> - Welche Zahlen gehören zu $\mathbb{Q}$, welche zu $\mathbb{R} \setminus \mathbb{Q}$: $\sqrt{4}$, $\sqrt{5}$, $0{,}\overline{12}$, $\pi$?

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Verlag Europa-Lehrmittel
- ISB Bayern: *Lehrplan Mathematik Gymnasium*

> [!tip] **Weiterführende Links**
> - [[Glossar#Reelle Zahlen|Glossar: Reelle Zahlen]]
> - [[Glossar#Intervall|Glossar: Intervall]]
