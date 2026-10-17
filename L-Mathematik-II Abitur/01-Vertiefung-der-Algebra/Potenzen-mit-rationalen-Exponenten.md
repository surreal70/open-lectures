---
author: Andreas Hümmer
title: Potenzen mit rationalen Exponenten
tags:
  - content
  - mathe
  - algebra
  - potenzen
  - potenzgesetze
  - wurzeln
created: 2025-01-13
modified: 2025-01-13
---

# Potenzen mit rationalen Exponenten

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Potenzen mit ganzzahligen Exponenten sicher beherrschen
> - Wurzeln als Potenzen mit rationalen Exponenten darstellen können
> - Die Potenzgesetze auf rationale Exponenten anwenden können
> - Ausdrücke mit rationalen Exponenten vereinfachen können

---

## Überblick

Die Erweiterung des Potenzbegriffs auf rationale Exponenten ermöglicht eine einheitliche Behandlung von Potenzen und Wurzeln. Statt mit zwei verschiedenen Rechenoperationen zu arbeiten, können alle Umformungen mit den Potenzgesetzen durchgeführt werden. Dies ist besonders in der Analysis von großer Bedeutung, etwa beim Ableiten von Wurzelfunktionen.

## Potenzen mit ganzzahligen Exponenten

### Definition

Für $a \in \mathbb{R}$ und $n \in \mathbb{N}$ ist:

$$a^n = \underbrace{a \cdot a \cdot \ldots \cdot a}_{n \text{ Faktoren}}$$

Zusätzlich gilt:
- $a^0 = 1$ für $a \neq 0$
- $a^{-n} = \frac{1}{a^n}$ für $a \neq 0$

### Die Potenzgesetze

Für $a, b \in \mathbb{R}$ (mit $a, b \neq 0$ bei negativen Exponenten) und $m, n \in \mathbb{Z}$:

| Regel | Formel |
|-------|--------|
| Multiplikation gleicher Basis | $a^m \cdot a^n = a^{m+n}$ |
| Division gleicher Basis | $\frac{a^m}{a^n} = a^{m-n}$ |
| Potenz einer Potenz | $(a^m)^n = a^{m \cdot n}$ |
| Produkt mit gleichem Exponenten | $(a \cdot b)^n = a^n \cdot b^n$ |
| Quotient mit gleichem Exponenten | $\left(\frac{a}{b}\right)^n = \frac{a^n}{b^n}$ |

**Beispiele:**

$$2^3 \cdot 2^4 = 2^7 = 128$$

$$\frac{5^6}{5^4} = 5^2 = 25$$

$$(3^2)^3 = 3^6 = 729$$

## Wurzeln als Potenzen

### Definition der n-ten Wurzel

Die **n-te Wurzel** aus $a$ ist diejenige (nicht-negative) Zahl, deren n-te Potenz gleich $a$ ist:

$$\sqrt[n]{a} = b \quad \Leftrightarrow \quad b^n = a \text{ und } b \geq 0$$

### Wurzeln als Potenzen schreiben

Die entscheidende Verbindung zwischen Wurzeln und Potenzen:

$$\sqrt[n]{a} = a^{\frac{1}{n}}$$

**Begründung:** Es muss gelten $(a^{\frac{1}{n}})^n = a^{\frac{n}{n}} = a^1 = a$ ✓

**Beispiele:**

$$\sqrt{a} = a^{\frac{1}{2}}$$

$$\sqrt[3]{a} = a^{\frac{1}{3}}$$

$$\sqrt[4]{a} = a^{\frac{1}{4}}$$

### Allgemeine rationale Exponenten

$$a^{\frac{m}{n}} = \sqrt[n]{a^m} = (\sqrt[n]{a})^m$$

**Beispiele:**

$$8^{\frac{2}{3}} = \sqrt[3]{8^2} = \sqrt[3]{64} = 4$$

Oder: $8^{\frac{2}{3}} = (\sqrt[3]{8})^2 = 2^2 = 4$

$$27^{-\frac{1}{3}} = \frac{1}{27^{\frac{1}{3}}} = \frac{1}{\sqrt[3]{27}} = \frac{1}{3}$$

> [!tip] **Rechenstrategie**
> Bei $a^{\frac{m}{n}}$ ist es oft einfacher, **zuerst die Wurzel** zu ziehen und dann zu potenzieren, da man so mit kleineren Zahlen rechnet.

## Anwendung der Potenzgesetze

Die Potenzgesetze gelten auch für rationale Exponenten.

### Multiplikation und Division

**Beispiel 1:**
$$x^{\frac{2}{3}} \cdot x^{\frac{1}{2}} = x^{\frac{2}{3} + \frac{1}{2}} = x^{\frac{4}{6} + \frac{3}{6}} = x^{\frac{7}{6}}$$

**Beispiel 2:**
$$\frac{a^{\frac{3}{4}}}{a^{\frac{1}{2}}} = a^{\frac{3}{4} - \frac{1}{2}} = a^{\frac{3}{4} - \frac{2}{4}} = a^{\frac{1}{4}}$$

### Potenzen von Potenzen

**Beispiel 3:**
$$(x^{\frac{2}{3}})^{\frac{3}{4}} = x^{\frac{2}{3} \cdot \frac{3}{4}} = x^{\frac{6}{12}} = x^{\frac{1}{2}}$$

### Gemischte Terme vereinfachen

**Beispiel 4:** Vereinfache $\frac{(a^2 b)^{\frac{1}{2}}}{a^{\frac{1}{2}} b^{-\frac{1}{4}}}$

$$= \frac{a^{2 \cdot \frac{1}{2}} \cdot b^{\frac{1}{2}}}{a^{\frac{1}{2}} \cdot b^{-\frac{1}{4}}} = \frac{a^1 \cdot b^{\frac{1}{2}}}{a^{\frac{1}{2}} \cdot b^{-\frac{1}{4}}}$$

$$= a^{1-\frac{1}{2}} \cdot b^{\frac{1}{2}-(-\frac{1}{4})} = a^{\frac{1}{2}} \cdot b^{\frac{3}{4}}$$

## Definitionsbereiche

> [!warning] **Einschränkungen bei rationalen Exponenten**
> Für $a^{\frac{m}{n}}$ mit $a < 0$:
> - Bei **ungeradem** $n$ ist der Ausdruck definiert: $(-8)^{\frac{1}{3}} = -2$
> - Bei **geradem** $n$ ist der Ausdruck in $\mathbb{R}$ **nicht definiert**: $(-4)^{\frac{1}{2}} \notin \mathbb{R}$

Im Schulkontext wird oft vereinfachend $a \geq 0$ für rationale Exponenten vorausgesetzt.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Wiederholung-algebraischer-Grundlagen]] – Grundrechenarten und Termumformung
- → [[Wurzelterme]] – Vertiefung der Wurzelrechnung
- → [[Potenzfunktionen]] – Funktionen der Form $f(x) = x^r$
- → [[Definition-der-Ableitung]] – Ableitung von Wurzelfunktionen mit der Potenzregel

> [!warning] **Prüfungsrelevant**
> - Umschreiben von Wurzeln in Potenzschreibweise
> - Sichere Anwendung der Potenzgesetze auf rationale Exponenten
> - Vereinfachen komplexer Ausdrücke
> - Definitionsbereiche bei negativen Basen beachten

> [!question] **Typische Prüfungsfragen**
> - Vereinfache $\frac{x^{\frac{3}{2}} \cdot x^{-\frac{1}{4}}}{x^{\frac{1}{2}}}$ und gib das Ergebnis mit positivem Exponenten an.
> - Berechne $16^{-\frac{3}{4}}$ ohne Taschenrechner.
> - Schreibe $\frac{1}{\sqrt[3]{x^2}}$ als Potenz von $x$.

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Verlag Europa-Lehrmittel
- ISB Bayern: *Lehrplan Mathematik Gymnasium*

> [!tip] **Weiterführende Links**
> - [[Glossar#Potenz|Glossar: Potenz]]
> - [[Glossar#Wurzel|Glossar: Wurzel]]
