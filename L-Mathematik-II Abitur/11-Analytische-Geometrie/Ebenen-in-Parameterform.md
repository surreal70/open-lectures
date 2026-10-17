---
author: Andreas Hümmer
title: Ebenen in Parameterform
tags:
  - content
  - mathe
  - analytische-geometrie
  - ebenen
  - parameterform
created: 2026-10-17
modified: 2026-10-17
---

# Ebenen in Parameterform

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Ebenen durch Parametergleichungen mit zwei Parametern beschreiben können
> - Stützvektor und Spannvektoren einer Ebene identifizieren
> - Ebenengleichungen aus drei Punkten oder aus Punkt und zwei Richtungen aufstellen
> - Prüfen können, ob ein Punkt in einer Ebene liegt

---

## Überblick

Die Parameterform ist eine von mehreren Möglichkeiten, Ebenen im Raum zu beschreiben. Sie verwendet einen Aufpunkt und zwei linear unabhängige Richtungsvektoren, die die Ebene aufspannen. Diese Darstellung ist besonders anschaulich und eignet sich gut zum Aufstellen von Ebenengleichungen aus gegebenen Punkten.

## Die Parametergleichung einer Ebene

Eine Ebene $E$ im Raum wird durch einen **Stützvektor** $\vec{a}$ und zwei **Spannvektoren** $\vec{u}$ und $\vec{v}$ beschrieben:

$$E: \vec{x} = \vec{a} + r \cdot \vec{u} + s \cdot \vec{v}, \quad r, s \in \mathbb{R}$$

Dabei ist:
- $\vec{a}$ der **Stützvektor** (Ortsvektor eines Punktes auf der Ebene)
- $\vec{u}$ und $\vec{v}$ die **Spannvektoren** (spannen die Ebene auf)
- $r$ und $s$ die **Parameter** (durchlaufen unabhängig alle reellen Zahlen)

### Wichtige Voraussetzung

Die Spannvektoren $\vec{u}$ und $\vec{v}$ müssen **linear unabhängig** sein, d.h. keiner darf ein Vielfaches des anderen sein:

$$\vec{u} \neq \lambda \cdot \vec{v} \quad \text{für alle } \lambda \in \mathbb{R}$$

Andernfalls würde die Gleichung nur eine Gerade beschreiben.

### Komponentenweise Darstellung

In Koordinatenschreibweise:

$$E: \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix} + r \cdot \begin{pmatrix} u_1 \\ u_2 \\ u_3 \end{pmatrix} + s \cdot \begin{pmatrix} v_1 \\ v_2 \\ v_3 \end{pmatrix}$$

## Aufstellen einer Ebenengleichung

### Aus drei Punkten

Sind drei nicht auf einer Geraden liegende Punkte $A$, $B$ und $C$ gegeben, so bestimmen sie eindeutig eine Ebene:

$$E: \vec{x} = \vec{OA} + r \cdot \overrightarrow{AB} + s \cdot \overrightarrow{AC}$$

Die Spannvektoren sind die Verbindungsvektoren vom ersten Punkt zu den beiden anderen.

### Beispiel: Ebene durch drei Punkte

Gegeben: $A = (1, 2, 3)$, $B = (4, 2, 5)$, $C = (2, 5, 3)$

**Spannvektoren:**
$$\overrightarrow{AB} = \begin{pmatrix} 4-1 \\ 2-2 \\ 5-3 \end{pmatrix} = \begin{pmatrix} 3 \\ 0 \\ 2 \end{pmatrix}$$

$$\overrightarrow{AC} = \begin{pmatrix} 2-1 \\ 5-2 \\ 3-3 \end{pmatrix} = \begin{pmatrix} 1 \\ 3 \\ 0 \end{pmatrix}$$

**Lineare Unabhängigkeit prüfen:** $\begin{pmatrix} 3 \\ 0 \\ 2 \end{pmatrix} \neq \lambda \cdot \begin{pmatrix} 1 \\ 3 \\ 0 \end{pmatrix}$ für alle $\lambda$ ✓

**Ebenengleichung:**
$$E: \vec{x} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} + r \cdot \begin{pmatrix} 3 \\ 0 \\ 2 \end{pmatrix} + s \cdot \begin{pmatrix} 1 \\ 3 \\ 0 \end{pmatrix}$$

### Aus Punkt und zwei Richtungen

Ist ein Punkt $P$ und sind zwei Richtungen $\vec{u}$ und $\vec{v}$ gegeben (etwa parallel zu zwei Geraden oder Kanten), setzt man direkt:

$$E: \vec{x} = \vec{OP} + r \cdot \vec{u} + s \cdot \vec{v}$$

## Punktprobe

Um zu prüfen, ob ein Punkt $P = (p_1, p_2, p_3)$ in der Ebene $E$ liegt, setzt man die Koordinaten ein und prüft, ob ein Wertepaar $(r, s)$ existiert, das alle drei Gleichungen erfüllt.

### Beispiel: Punktprobe

Gegeben: $E: \vec{x} = \begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix} + r \cdot \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix} + s \cdot \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}$

Liegt $P = (5, 3, 3)$ in $E$?

Gleichungssystem:
1. $5 = 1 + 2r + 0s \Rightarrow 2r = 4 \Rightarrow r = 2$
2. $3 = 0 + 1r + 1s \Rightarrow s = 3 - r = 3 - 2 = 1$
3. Probe: $3 = 2 + 0r + 1s = 2 + 0 \cdot 2 + 1 \cdot 1 = 3$ ✓

Mit $r = 2$ und $s = 1$ sind alle Gleichungen erfüllt. $P$ liegt in $E$. ✓

## Spezielle Ebenen

### Koordinatenebenen in Parameterform

| Ebene | Parameterdarstellung |
|-------|---------------------|
| $xy$-Ebene | $\vec{x} = r \cdot \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} + s \cdot \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}$ |
| $xz$-Ebene | $\vec{x} = r \cdot \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} + s \cdot \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$ |
| $yz$-Ebene | $\vec{x} = r \cdot \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} + s \cdot \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$ |

### Ebenen parallel zu einer Koordinatenebene

Eine Ebene parallel zur $xy$-Ebene in Höhe $z = c$:

$$E: \vec{x} = \begin{pmatrix} 0 \\ 0 \\ c \end{pmatrix} + r \cdot \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} + s \cdot \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}$$

## Äquivalente Darstellungen

Dieselbe Ebene kann durch verschiedene Parametergleichungen dargestellt werden:

1. **Anderer Aufpunkt:** Jeder Punkt auf der Ebene kann als Stützvektor dienen
2. **Andere Spannvektoren:** Jede Linearkombination $\vec{u}' = \alpha \vec{u} + \beta \vec{v}$ mit geeignetem zweiten Vektor
3. **Skalierte Spannvektoren:** $\vec{u}$ und $\vec{v}$ können unabhängig skaliert werden

## Spurgeraden

Die **Spurgeraden** einer Ebene sind die Schnittgeraden mit den Koordinatenebenen:

- **Spurgerade $g_{xy}$:** Schnitt mit der $xy$-Ebene (setze $z = 0$)
- **Spurgerade $g_{xz}$:** Schnitt mit der $xz$-Ebene (setze $y = 0$)
- **Spurgerade $g_{yz}$:** Schnitt mit der $yz$-Ebene (setze $x = 0$)

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Geraden-in-Parameterform]] — Eindimensionales Analogon
- → [[Ebenen-in-Koordinatenform]] — Alternative Darstellungsform
- → [[Normalenform]] — Darstellung mit Normalenvektor
- → [[Kreuzprodukt]] — Berechnung des Normalenvektors aus Spannvektoren
- → [[Lagebeziehungen-von-Ebenen]] — Schnitt und Parallelität

> [!warning] **Prüfungsrelevant**
> - Ebenengleichung aus drei Punkten aufstellen
> - Prüfung der linearen Unabhängigkeit der Spannvektoren
> - Punktprobe durch Lösen des Gleichungssystems
> - Umrechnung zwischen Parameter- und Koordinatenform

> [!question] **Typische Prüfungsfragen**
> - Stellen Sie die Gleichung der Ebene durch die Punkte $A(1|0|2)$, $B(3|1|4)$ und $C(2|3|1)$ in Parameterform auf.
> - Prüfen Sie, ob der Punkt $P(5|2|6)$ in der Ebene $E: \vec{x} = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} + r \begin{pmatrix} 2 \\ 0 \\ 1 \end{pmatrix} + s \begin{pmatrix} 0 \\ 1 \\ 2 \end{pmatrix}$ liegt.
> - Bestimmen Sie die Spurgerade der Ebene $E$ mit der $xy$-Ebene.

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg, 2018
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Europa-Lehrmittel, 2016
- Bigalke, A.; Köhler, N.: *Mathematik Gymnasiale Oberstufe*, Cornelsen, 2019

> [!tip] **Weiterführende Links**
> - [[Schnittpunkte-und-Schnittgeraden]] — Durchstoßpunkte berechnen
> - [[Winkelberechnungen]] — Winkel zwischen Ebenen
