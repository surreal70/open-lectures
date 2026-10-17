---
author: Andreas Hümmer
title: Einführung in die mathematische Grenzwertbildung
tags:
  - content
  - mathe
  - grenzwert
  - epsilon-delta
  - analysis
  - beweistechniken
created: 2025-06-17
modified: 2025-06-17
---

# Einführung in die mathematische Grenzwertbildung

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die formale Epsilon-Definition des Grenzwerts verstehen
> - Einfache Grenzwertbeweise führen können
> - Die Verbindung zwischen anschaulicher und formaler Definition kennen
> - Die Bedeutung von Quantoren in mathematischen Definitionen verstehen
> - Typische Beweisstrategien anwenden können

---

## Überblick

Die **formale Grenzwertdefinition** nach Cauchy und Weierstraß ist der Grundpfeiler der modernen Analysis. Sie übersetzt die anschauliche Vorstellung "Die Folge nähert sich beliebig einem Wert an" in eine präzise mathematische Aussage. Diese Formalisierung ermöglicht es, Grenzwerte rigoros zu beweisen und Fehlschlüsse zu vermeiden.

Auch wenn die formale Definition im Abitur nur in Grundzügen behandelt wird, ist das Verständnis der Idee dahinter wichtig für ein tieferes Verständnis der Analysis.

## Die Epsilon-Definition für Folgen

### Anschauliche Vorstellung

Eine Folge $(a_n)$ konvergiert gegen $L$, wenn die Folgenglieder "irgendwann" alle beliebig nahe bei $L$ liegen und dort "bleiben".

### Formale Definition

$$\lim_{n \to \infty} a_n = L \quad :\Leftrightarrow \quad \forall \varepsilon > 0 \; \exists N \in \mathbb{N} : \forall n \geq N : |a_n - L| < \varepsilon$$

### Aufschlüsselung der Bestandteile

| Symbol | Bedeutung |
|--------|-----------|
| $\forall \varepsilon > 0$ | "Für jede Toleranz $\varepsilon$, egal wie klein..." |
| $\exists N \in \mathbb{N}$ | "...gibt es einen Index $N$..." |
| $\forall n \geq N$ | "...sodass für alle $n$ ab diesem Index..." |
| $\|a_n - L\| < \varepsilon$ | "...der Abstand zum Grenzwert kleiner als $\varepsilon$ ist." |

### Geometrische Interpretation

Der $\varepsilon$-Schlauch um $L$:
- Zeichne horizontale Linien bei $y = L - \varepsilon$ und $y = L + \varepsilon$
- Konvergenz bedeutet: Ab einem Index $N$ liegen **alle** Folgenpunkte im Schlauch
- Je enger der Schlauch ($\varepsilon$ kleiner), desto später muss man eventuell starten ($N$ größer)

```
    y
    ↑     L+ε ─────────────────────────
    │            •  •  •  •  •  •  •   (alle Punkte ab N)
    │     L   ─────────────────────────
    │            •  •  •  •  •  •  •
    │     L-ε ─────────────────────────
    │  •
    │    •    •
    │  •   •
    └──────────────────────────────────→ n
              ↑
              N
```

## Struktur eines Konvergenzbeweises

### Das Beweisschema

1. **Sei $\varepsilon > 0$ beliebig.** (Man darf sich $\varepsilon$ nicht aussuchen!)
2. **Finde ein geeignetes $N$** (als Funktion von $\varepsilon$).
3. **Zeige:** Für alle $n \geq N$ gilt $|a_n - L| < \varepsilon$.

### Beispiel: $\lim_{n \to \infty} \frac{1}{n} = 0$

**Behauptung:** $\forall \varepsilon > 0 \; \exists N : \forall n \geq N : \left|\frac{1}{n} - 0\right| < \varepsilon$

**Beweis:**

1. Sei $\varepsilon > 0$ beliebig gegeben.

2. Wir müssen $N$ finden, sodass $\frac{1}{n} < \varepsilon$ für alle $n \geq N$.
   
   Das ist äquivalent zu $n > \frac{1}{\varepsilon}$.
   
   Wähle $N := \left\lfloor \frac{1}{\varepsilon} \right\rfloor + 1$ (die kleinste natürliche Zahl größer als $\frac{1}{\varepsilon}$).

3. Für $n \geq N$ gilt dann:
   $$n \geq N > \frac{1}{\varepsilon} \quad \Rightarrow \quad \frac{1}{n} < \varepsilon \quad \Rightarrow \quad \left|\frac{1}{n} - 0\right| < \varepsilon \quad \checkmark$$

∎

### Beispiel: $\lim_{n \to \infty} \frac{2n+1}{n} = 2$

**Behauptung:** $\lim_{n \to \infty} \frac{2n+1}{n} = 2$

**Beweis:**

1. Sei $\varepsilon > 0$ beliebig.

2. Wir vereinfachen:
   $$\left|\frac{2n+1}{n} - 2\right| = \left|\frac{2n+1 - 2n}{n}\right| = \left|\frac{1}{n}\right| = \frac{1}{n}$$
   
   Wir brauchen: $\frac{1}{n} < \varepsilon$, also $n > \frac{1}{\varepsilon}$.
   
   Wähle $N := \left\lfloor \frac{1}{\varepsilon} \right\rfloor + 1$.

3. Für $n \geq N$:
   $$\left|\frac{2n+1}{n} - 2\right| = \frac{1}{n} \leq \frac{1}{N} < \varepsilon \quad \checkmark$$

∎

## Die Epsilon-Delta-Definition für Funktionen

### Definition

$$\lim_{x \to x_0} f(x) = L \quad :\Leftrightarrow \quad \forall \varepsilon > 0 \; \exists \delta > 0 : 0 < |x - x_0| < \delta \Rightarrow |f(x) - L| < \varepsilon$$

### Unterschied zur Folgendefinition

- Bei Folgen: Index $N$ (diskret)
- Bei Funktionen: Umgebungsradius $\delta$ (kontinuierlich)
- Bei Funktionen: $x \neq x_0$ ist erlaubt (der Grenzwert hängt nicht vom Funktionswert an $x_0$ ab)

## Wichtige Beweistechniken

### Technik 1: Rückwärts rechnen

Beginne mit der Ungleichung $|a_n - L| < \varepsilon$ und löse nach $n$ auf, um $N$ zu bestimmen.

### Technik 2: Abschätzen

Oft kann man $|a_n - L|$ durch einen einfacheren Ausdruck abschätzen:

$$|a_n - L| \leq \text{einfacherer Ausdruck} < \varepsilon$$

### Technik 3: Standardschranken nutzen

Für große $n$ gelten oft Vereinfachungen wie:
- $\frac{1}{n} \leq 1$
- $n \geq 1$
- $n^2 + n \geq n^2$

### Beispiel mit Abschätzung

Zeige: $\lim_{n \to \infty} \frac{n}{n^2 + 1} = 0$

**Beweis:**

$$\left|\frac{n}{n^2 + 1} - 0\right| = \frac{n}{n^2 + 1} < \frac{n}{n^2} = \frac{1}{n}$$

Wähle $N$ so, dass $\frac{1}{N} < \varepsilon$, also $N > \frac{1}{\varepsilon}$.

Für $n \geq N$: $\frac{n}{n^2 + 1} < \frac{1}{n} \leq \frac{1}{N} < \varepsilon$ ∎

## Negation der Konvergenzdefinition

### Wann ist eine Folge divergent?

Die **Negation** der Konvergenzdefinition lautet:

$$\forall L \in \mathbb{R} \; \exists \varepsilon > 0 : \forall N \in \mathbb{N} \; \exists n \geq N : |a_n - L| \geq \varepsilon$$

**In Worten:** Für jeden potentiellen Grenzwert $L$ gibt es eine Toleranz $\varepsilon$, die von unendlich vielen Folgengliedern überschritten wird.

### Anwendung: Divergenznachweis

Für $a_n = (-1)^n$:

Angenommen, $\lim a_n = L$ existiert.

- Teilfolge $(a_{2k}) = (1, 1, 1, \ldots) \to 1$
- Teilfolge $(a_{2k+1}) = (-1, -1, -1, \ldots) \to -1$

Widerspruch: Ein Grenzwert kann nicht gleichzeitig 1 und -1 sein!

Also ist $((-1)^n)$ divergent.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Konvergenz]] – Anschauliche Einführung und Kriterien
- → [[Grenzwerte-von-Folgen]] – Praktische Berechnung
- → [[Grenzwerte-von-Funktionen]] – Übertragung auf Funktionen
- → [[Stetigkeit]] – Anwendung der Epsilon-Delta-Definition
- → [[Divergenz]] – Negation der Konvergenz

> [!warning] **Prüfungsrelevant**
> - Das Verständnis der Epsilon-Definition (nicht unbedingt Beweise führen) ist wichtig
> - Die geometrische Interpretation mit dem Epsilon-Schlauch sollte erklärt werden können
> - Im Leistungskurs: Einfache Beweise nach dem Beweisschema
> - Die Struktur der Definition (Quantorenreihenfolge) verstehen
> - Zusammenhang zwischen Epsilon-Definition und Grenzwertsätzen

> [!question] **Typische Prüfungsfragen**
> - Erkläre anhand einer Skizze, was die Epsilon-Definition geometrisch bedeutet.
> - Zeige mit der Epsilon-Definition, dass $\lim_{n \to \infty} \frac{1}{n^2} = 0$.
> - Warum ist es wichtig, dass $\varepsilon$ beliebig gewählt werden kann und nicht umgekehrt zuerst $N$ festgelegt wird?

## Quellen

- Forster, O.: Analysis 1. Springer Spektrum, 2016.
- Heuser, H.: Lehrbuch der Analysis, Teil 1. Springer Vieweg, 2009.
- Königsberger, K.: Analysis 1. Springer, 2004.

> [!tip] **Weiterführende Links**
> - [[Definition-der-Ableitung]] – Der Grenzwert des Differenzenquotienten
> - [[Unendliche-geometrische-Reihen]] – Konvergenzbeweis für Reihen
