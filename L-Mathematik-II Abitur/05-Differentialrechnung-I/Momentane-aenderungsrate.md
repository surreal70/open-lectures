---
author: Andreas Hümmer
title: Momentane Änderungsrate
tags:
  - content
  - mathe
  - differentialrechnung
  - aenderungsrate
  - grenzwert
  - tangente
  - analysis
created: 2026-10-17
modified: 2026-10-17
---

# Momentane Änderungsrate

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das Konzept der momentanen Änderungsrate als Grenzwert der durchschnittlichen Änderungsrate verstehen
> - Den Grenzprozess "Sekantensteigung → Tangentensteigung" geometrisch nachvollziehen können
> - Die momentane Änderungsrate als Ableitung erkennen und interpretieren können
> - Den Grenzprozess mit der h-Schreibweise formal durchführen können

---

## Überblick

Die momentane Änderungsrate beschreibt, wie sich eine Größe *genau an einem bestimmten Punkt* ändert – nicht im Durchschnitt über ein Intervall. Um dieses Konzept mathematisch zu erfassen, führen wir einen Grenzprozess durch: Wir lassen das Intervall, über das wir die durchschnittliche Änderungsrate berechnen, immer kleiner werden, bis es schließlich auf einen einzigen Punkt zusammenschrumpft.

Geometrisch entspricht dies dem Übergang von der Sekante zur Tangente.

## Vom Durchschnitt zum Augenblick

### Das Problem der Momentangeschwindigkeit

Ein Auto bewegt sich auf einer geraden Straße. Seine Position zur Zeit $t$ sei $s(t)$. 

Die **durchschnittliche Geschwindigkeit** im Zeitintervall $[t_1, t_2]$ ist:
$$\bar{v} = \frac{s(t_2) - s(t_1)}{t_2 - t_1}$$

Aber was bedeutet es, dass das Tachometer *genau jetzt* 50 km/h anzeigt? Zu einem einzelnen Zeitpunkt $t_0$ legt das Auto keine Strecke zurück, also können wir nicht einfach $\frac{0}{0}$ berechnen.

### Die Lösung: Der Grenzübergang

Wir betrachten immer kürzere Zeitintervalle um den Zeitpunkt $t_0$:

| Intervall | Dauer $\Delta t$ | Durchschnittliche Geschwindigkeit |
|-----------|------------------|-----------------------------------|
| $[t_0, t_0 + 1\,\text{s}]$ | 1 s | $\bar{v}_1$ |
| $[t_0, t_0 + 0{,}1\,\text{s}]$ | 0,1 s | $\bar{v}_2$ |
| $[t_0, t_0 + 0{,}01\,\text{s}]$ | 0,01 s | $\bar{v}_3$ |
| $\vdots$ | $\vdots$ | $\vdots$ |

Wenn diese durchschnittlichen Geschwindigkeiten gegen einen festen Wert streben, so ist dieser die **Momentangeschwindigkeit** bei $t_0$.

## Mathematische Definition

> [!note] **Definition: Momentane Änderungsrate**
> Die **momentane Änderungsrate** einer Funktion $f$ an der Stelle $x_0$ ist definiert als der Grenzwert:
> $$f'(x_0) = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}$$
> falls dieser Grenzwert existiert.

Alternative Schreibweisen:
$$f'(x_0) = \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0}$$

Dabei ist:
- $f(x_0 + h) - f(x_0)$ die Änderung der Funktionswerte
- $h$ die Schrittweite (geht gegen 0)
- Der Quotient ist die durchschnittliche Änderungsrate im Intervall $[x_0, x_0 + h]$

## Geometrische Interpretation

### Von der Sekante zur Tangente

Betrachten wir den Graphen einer Funktion $f$:

```
      y
      |
      |        Tangente (Grenzlage)
      |       /
      |  S₃  /
      |   \ /  S₂
      |    X----S₁
      |   P
      |  ·
      | ·
      |·
      +-----------------------> x
```

- **Sekante $S_1$**: Verbindet $P(x_0 | f(x_0))$ mit einem entfernten Punkt
- **Sekante $S_2$**: Verbindet $P$ mit einem näheren Punkt
- **Sekante $S_3$**: Verbindet $P$ mit einem noch näheren Punkt
- **Tangente**: Die Grenzlage der Sekanten, wenn der zweite Punkt gegen $P$ wandert

> [!note] **Geometrische Deutung**
> Die momentane Änderungsrate $f'(x_0)$ ist die **Steigung der Tangente** an den Graphen von $f$ im Punkt $P(x_0 | f(x_0))$.

## Berechnungsbeispiele

### Beispiel 1: Quadratische Funktion

Bestimme die momentane Änderungsrate von $f(x) = x^2$ an der Stelle $x_0 = 3$.

**Lösung:**
$$f'(3) = \lim_{h \to 0} \frac{f(3 + h) - f(3)}{h}$$
$$= \lim_{h \to 0} \frac{(3 + h)^2 - 9}{h}$$
$$= \lim_{h \to 0} \frac{9 + 6h + h^2 - 9}{h}$$
$$= \lim_{h \to 0} \frac{6h + h^2}{h}$$
$$= \lim_{h \to 0} \frac{h(6 + h)}{h}$$
$$= \lim_{h \to 0} (6 + h) = 6$$

Die momentane Änderungsrate von $f(x) = x^2$ an der Stelle $x_0 = 3$ ist $f'(3) = 6$.

### Beispiel 2: Kubische Funktion

Bestimme die momentane Änderungsrate von $f(x) = x^3$ an der Stelle $x_0 = 2$.

**Lösung:**
$$f'(2) = \lim_{h \to 0} \frac{(2 + h)^3 - 8}{h}$$

Zunächst entwickeln wir $(2 + h)^3$:
$$(2 + h)^3 = 8 + 12h + 6h^2 + h^3$$

Einsetzen:
$$f'(2) = \lim_{h \to 0} \frac{8 + 12h + 6h^2 + h^3 - 8}{h} = \lim_{h \to 0} \frac{12h + 6h^2 + h^3}{h}$$
$$= \lim_{h \to 0} (12 + 6h + h^2) = 12$$

### Beispiel 3: Wurzelfunktion

Bestimme die momentane Änderungsrate von $f(x) = \sqrt{x}$ an der Stelle $x_0 = 4$.

**Lösung:**
$$f'(4) = \lim_{h \to 0} \frac{\sqrt{4 + h} - 2}{h}$$

Wir erweitern mit der konjugierten Wurzel:
$$= \lim_{h \to 0} \frac{(\sqrt{4 + h} - 2)(\sqrt{4 + h} + 2)}{h(\sqrt{4 + h} + 2)}$$
$$= \lim_{h \to 0} \frac{(4 + h) - 4}{h(\sqrt{4 + h} + 2)}$$
$$= \lim_{h \to 0} \frac{h}{h(\sqrt{4 + h} + 2)}$$
$$= \lim_{h \to 0} \frac{1}{\sqrt{4 + h} + 2} = \frac{1}{2 + 2} = \frac{1}{4}$$

## Näherungsweise Berechnung

Wenn der exakte Grenzwert schwer zu berechnen ist, kann die momentane Änderungsrate durch durchschnittliche Änderungsraten mit kleinem $h$ angenähert werden.

**Beispiel:** $f(x) = 2^x$ an der Stelle $x_0 = 1$

| $h$ | $\frac{f(1 + h) - f(1)}{h}$ |
|-----|---------------------------|
| 0,1 | $\frac{2^{1{,}1} - 2}{0{,}1} \approx 1{,}435$ |
| 0,01 | $\frac{2^{1{,}01} - 2}{0{,}01} \approx 1{,}391$ |
| 0,001 | $\frac{2^{1{,}001} - 2}{0{,}001} \approx 1{,}387$ |

Der Grenzwert ist $f'(1) = 2 \cdot \ln(2) \approx 1{,}386$.

## Existenz der momentanen Änderungsrate

Die momentane Änderungsrate existiert nicht an jeder Stelle:

- **Sprungstellen**: An Unstetigkeitsstellen existiert keine Tangente
- **Knickstellen**: Auch bei Stetigkeit kann es Stellen geben, an denen von links und rechts unterschiedliche Tangentensteigungen entstehen
- **Senkrechte Tangente**: Wenn die Steigung gegen $\pm \infty$ geht

Eine Funktion heißt **differenzierbar** an einer Stelle, wenn dort die momentane Änderungsrate existiert.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Durchschnittliche-aenderungsrate|Durchschnittliche Änderungsrate]] – Ausgangspunkt des Grenzprozesses
- → [[Differenzenquotient|Differenzenquotient]] – Formale Bezeichnung
- → [[Differentialquotient|Differentialquotient]] – Der Grenzwert selbst
- → [[Definition-der-Ableitung|Definition der Ableitung]] – Verallgemeinerung
- → [[Grenzwerte-von-Funktionen|Grenzwerte von Funktionen]] – Mathematische Grundlage

> [!warning] **Prüfungsrelevant**
> - Die Grenzwertdefinition $f'(x_0) = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}$ muss auswendig gekonnt werden
> - Der Grenzprozess muss bei einfachen Funktionen durchgeführt werden können
> - Die geometrische Deutung als Tangentensteigung ist fundamental
> - Das Erkennen, wann die momentane Änderungsrate nicht existiert

> [!question] **Typische Prüfungsfragen**
> - "Bestimmen Sie die momentane Änderungsrate von $f$ an der Stelle $x_0$ mithilfe des Grenzwerts."
> - "Erläutern Sie den geometrischen Zusammenhang zwischen Sekante und Tangente."
> - "An welchen Stellen ist die Funktion nicht differenzierbar? Begründen Sie."

## Quellen

- Bigalke, A., Köhler, N. (2015): *Mathematik – Qualifikationsphase*. Cornelsen Verlag.
- Griesel, H., Postel, H., Suhr, F. (2019): *Elemente der Mathematik – Qualifikationsphase*. Schroedel Verlag.
- Papula, L. (2018): *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1. Springer Vieweg.

> [!tip] **Weiterführende Links**
> - [[Geometrische-Bedeutung-der-Ableitung|Geometrische Bedeutung der Ableitung]] – Vertiefte Betrachtung
> - [[Tangenten-und-Normalen|Tangenten und Normalen]] – Anwendung der Tangentensteigung
