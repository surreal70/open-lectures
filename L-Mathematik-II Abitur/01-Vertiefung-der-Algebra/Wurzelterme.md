---
author: Andreas Hümmer
title: Wurzelterme
tags:
  - content
  - mathe
  - algebra
  - wurzeln
  - radikanden
  - rationalisieren
created: 2025-01-13
modified: 2025-01-13
---

# Wurzelterme

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Wurzelterme vereinfachen und zusammenfassen können
> - Die Wurzelgesetze sicher anwenden können
> - Nenner rationalisieren können
> - Den Definitionsbereich von Wurzeltermen bestimmen können

---

## Überblick

Wurzelterme begegnen uns in der Mathematik häufig, etwa bei der Lösung quadratischer Gleichungen, in der Geometrie oder bei der Berechnung von Abständen. Das sichere Vereinfachen von Wurzeltermen und das Rationalisieren von Nennern sind wichtige Techniken, die auch für das Ableiten von Wurzelfunktionen in der Analysis benötigt werden.

## Grundlagen der Wurzelrechnung

### Definition der Wurzel

Die **n-te Wurzel** aus einer nicht-negativen Zahl $a$ ist die nicht-negative Zahl $b$ mit $b^n = a$:

$$\sqrt[n]{a} = b \quad \Leftrightarrow \quad b^n = a \text{ und } b \geq 0$$

**Spezialfälle:**
- $\sqrt{a} = \sqrt[2]{a}$ (Quadratwurzel)
- $\sqrt[3]{a}$ (Kubikwurzel, auch für $a < 0$ definiert)

### Definitionsbereich

Für **gerade Wurzeln** ($n = 2, 4, 6, \ldots$) muss der **Radikand nicht-negativ** sein:

$$\sqrt[n]{a} \text{ ist für } a \geq 0 \text{ definiert (bei geradem } n\text{)}$$

Für **ungerade Wurzeln** ($n = 3, 5, 7, \ldots$) ist der Ausdruck für alle $a \in \mathbb{R}$ definiert:

$$\sqrt[3]{-8} = -2 \quad \text{(da } (-2)^3 = -8\text{)}$$

## Wurzelgesetze

Für $a, b \geq 0$ und $n, m \in \mathbb{N}$ mit $n, m \geq 2$:

### Produktregel

$$\sqrt[n]{a \cdot b} = \sqrt[n]{a} \cdot \sqrt[n]{b}$$

**Beispiel:** $\sqrt{12} = \sqrt{4 \cdot 3} = \sqrt{4} \cdot \sqrt{3} = 2\sqrt{3}$

### Quotientenregel

$$\sqrt[n]{\frac{a}{b}} = \frac{\sqrt[n]{a}}{\sqrt[n]{b}} \quad \text{für } b > 0$$

**Beispiel:** $\sqrt{\frac{25}{49}} = \frac{\sqrt{25}}{\sqrt{49}} = \frac{5}{7}$

### Potenzregel

$$\sqrt[n]{a^m} = a^{\frac{m}{n}} = (\sqrt[n]{a})^m$$

**Beispiel:** $\sqrt{x^6} = x^3$ für $x \geq 0$

### Verschachtelung von Wurzeln

$$\sqrt[m]{\sqrt[n]{a}} = \sqrt[m \cdot n]{a}$$

**Beispiel:** $\sqrt{\sqrt[3]{a}} = \sqrt[6]{a}$

## Vereinfachen von Wurzeltermen

### Radikand vereinfachen (Teilweise Wurzelziehen)

Man zerlegt den Radikanden in ein Produkt und zieht den Quadratzahl-Anteil vor die Wurzel:

**Beispiel 1:**
$$\sqrt{72} = \sqrt{36 \cdot 2} = 6\sqrt{2}$$

**Beispiel 2:**
$$\sqrt{50x^3} = \sqrt{25 \cdot 2 \cdot x^2 \cdot x} = 5x\sqrt{2x} \quad \text{für } x \geq 0$$

### Wurzelterme zusammenfassen

Gleichartige Wurzelterme können addiert werden:

$$3\sqrt{5} + 7\sqrt{5} = 10\sqrt{5}$$

$$2\sqrt{12} - 3\sqrt{27} = 2 \cdot 2\sqrt{3} - 3 \cdot 3\sqrt{3} = 4\sqrt{3} - 9\sqrt{3} = -5\sqrt{3}$$

> [!warning] **Häufiger Fehler**
> $\sqrt{a + b} \neq \sqrt{a} + \sqrt{b}$
> 
> Gegenbeispiel: $\sqrt{9 + 16} = \sqrt{25} = 5 \neq 3 + 4 = 7$

## Rationalisieren des Nenners

Das **Rationalisieren** beseitigt Wurzeln aus dem Nenner eines Bruchs.

### Bei einfachen Wurzeln

Man erweitert mit der Wurzel:

$$\frac{3}{\sqrt{5}} = \frac{3 \cdot \sqrt{5}}{\sqrt{5} \cdot \sqrt{5}} = \frac{3\sqrt{5}}{5}$$

### Bei Summen/Differenzen mit Wurzeln

Man erweitert mit dem **konjugierten Ausdruck** (dritte binomische Formel):

$$\frac{2}{3 + \sqrt{5}} = \frac{2(3 - \sqrt{5})}{(3 + \sqrt{5})(3 - \sqrt{5})} = \frac{2(3 - \sqrt{5})}{9 - 5} = \frac{2(3 - \sqrt{5})}{4} = \frac{3 - \sqrt{5}}{2}$$

**Allgemein:**
$$\frac{1}{a + \sqrt{b}} \cdot \frac{a - \sqrt{b}}{a - \sqrt{b}} = \frac{a - \sqrt{b}}{a^2 - b}$$

### Bei zwei Wurzeln

$$\frac{1}{\sqrt{a} + \sqrt{b}} = \frac{\sqrt{a} - \sqrt{b}}{(\sqrt{a} + \sqrt{b})(\sqrt{a} - \sqrt{b})} = \frac{\sqrt{a} - \sqrt{b}}{a - b}$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Potenzen-mit-rationalen-Exponenten]] – Wurzeln als Potenzen schreiben
- → [[Wurzelfunktionen]] – Die Wurzelfunktion $f(x) = \sqrt{x}$
- → [[Definitionsbereich]] – Definitionsbereiche bestimmen
- → [[Wiederholung-algebraischer-Grundlagen]] – Binomische Formeln

> [!warning] **Prüfungsrelevant**
> - Teilweise Wurzelziehen (Vereinfachen von Radikanden)
> - Gleichartige Wurzelterme zusammenfassen
> - Rationalisieren des Nenners
> - Definitionsbereich bei Wurzeltermen angeben

> [!question] **Typische Prüfungsfragen**
> - Vereinfache $\sqrt{180}$ so weit wie möglich.
> - Rationalisiere den Nenner: $\frac{6}{2 - \sqrt{3}}$
> - Für welche $x$ ist der Term $\sqrt{x^2 - 4x + 3}$ definiert?

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Verlag Europa-Lehrmittel
- ISB Bayern: *Lehrplan Mathematik Gymnasium*

> [!tip] **Weiterführende Links**
> - [[Glossar#Wurzel|Glossar: Wurzel]]
> - [[Glossar#Radikand|Glossar: Radikand]]
