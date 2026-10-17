---
author: Andreas Hümmer
title: Lagebeziehungen von Geraden
tags:
  - content
  - mathe
  - analytische-geometrie
  - geraden
  - lagebeziehungen
created: 2026-10-17
modified: 2026-10-17
---

# Lagebeziehungen von Geraden

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die vier möglichen Lagebeziehungen zweier Geraden im Raum unterscheiden können
> - Rechnerische Verfahren zur Bestimmung der Lagebeziehung anwenden
> - Schnittpunkte schneidender Geraden berechnen können
> - Den Begriff "windschief" verstehen und erkennen

---

## Überblick

Im dreidimensionalen Raum gibt es vier mögliche Lagebeziehungen zwischen zwei Geraden: Sie können identisch, parallel, schneidend oder windschief sein. Die Unterscheidung zwischen schneidend und windschief ist eine Besonderheit des Raumes, die in der Ebene nicht existiert. Die systematische Untersuchung dieser Beziehungen ist ein zentrales Thema der analytischen Geometrie.

## Die vier Lagebeziehungen

Zwei Geraden $g$ und $h$ im Raum können zueinander sein:

| Lagebeziehung | Beschreibung | Gemeinsame Punkte |
|---------------|--------------|-------------------|
| **Identisch** | $g$ und $h$ sind dieselbe Gerade | unendlich viele |
| **Parallel** | gleiche Richtung, verschiedene Lage | keine |
| **Schneidend** | genau ein gemeinsamer Punkt | genau einer |
| **Windschief** | nicht parallel und kein Schnittpunkt | keine |

### Besonderheit im Raum

In der Ebene sind nicht-parallele Geraden automatisch schneidend. Im Raum gibt es zusätzlich die **windschiefen Geraden**: Sie haben verschiedene Richtungen, liegen aber in verschiedenen parallelen Ebenen und schneiden sich daher nicht.

## Gegeben: Zwei Geraden in Parameterform

$$g: \vec{x} = \vec{a} + t \cdot \vec{u}, \quad t \in \mathbb{R}$$
$$h: \vec{x} = \vec{b} + s \cdot \vec{v}, \quad s \in \mathbb{R}$$

## Schritt 1: Richtungsvektoren vergleichen

Prüfe, ob die Richtungsvektoren $\vec{u}$ und $\vec{v}$ **kollinear** (parallel) sind:

$$\vec{u} = \lambda \cdot \vec{v} \quad \text{für ein } \lambda \in \mathbb{R}$$

**Wenn ja:** Die Geraden sind parallel oder identisch → weiter mit Schritt 2a

**Wenn nein:** Die Geraden sind schneidend oder windschief → weiter mit Schritt 2b

## Schritt 2a: Parallele Richtungen

Die Richtungsvektoren sind kollinear. Prüfe nun, ob ein Punkt von $g$ auch auf $h$ liegt.

**Methode:** Setze den Aufpunkt von $g$ in die Gleichung von $h$ ein und prüfe, ob ein $s$ existiert.

- **Wenn ein $s$ existiert:** Die Geraden sind **identisch**
- **Wenn kein $s$ existiert:** Die Geraden sind **parallel** (echt parallel)

### Beispiel: Parallel oder identisch?

$$g: \vec{x} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} + t \cdot \begin{pmatrix} 2 \\ 4 \\ 2 \end{pmatrix}$$

$$h: \vec{x} = \begin{pmatrix} 2 \\ 4 \\ 4 \end{pmatrix} + s \cdot \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix}$$

**Richtungsvektoren:** $\begin{pmatrix} 2 \\ 4 \\ 2 \end{pmatrix} = 2 \cdot \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix}$ → kollinear ✓

**Punktprobe:** Liegt $(1, 2, 3)$ auf $h$?

$1 = 2 + s \Rightarrow s = -1$

$2 = 4 + 2s = 4 - 2 = 2$ ✓

$3 = 4 + s = 4 - 1 = 3$ ✓

Da alle Gleichungen mit $s = -1$ erfüllt sind, sind $g$ und $h$ **identisch**.

## Schritt 2b: Nicht-parallele Richtungen

Die Richtungsvektoren sind nicht kollinear. Setze die Geradengleichungen gleich und löse das Gleichungssystem:

$$\vec{a} + t \cdot \vec{u} = \vec{b} + s \cdot \vec{v}$$

Dies ergibt drei Gleichungen für zwei Unbekannte ($t$ und $s$):

$$a_1 + t \cdot u_1 = b_1 + s \cdot v_1$$
$$a_2 + t \cdot u_2 = b_2 + s \cdot v_2$$
$$a_3 + t \cdot u_3 = b_3 + s \cdot v_3$$

**Vorgehen:**
1. Löse zwei der Gleichungen nach $t$ und $s$
2. Setze die Lösung in die dritte Gleichung ein (Probe)

- **Wenn die Probe stimmt:** Die Geraden **schneiden sich**
- **Wenn die Probe nicht stimmt:** Die Geraden sind **windschief**

### Beispiel: Schneidend oder windschief?

$$g: \vec{x} = \begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix} + t \cdot \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}$$

$$h: \vec{x} = \begin{pmatrix} 3 \\ 1 \\ 1 \end{pmatrix} + s \cdot \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}$$

**Richtungsvektoren nicht kollinear** (verschiedene Nullstellen) ✓

**Gleichungssystem:**
1. $1 + t = 3 + 0 \cdot s \Rightarrow t = 2$
2. $0 + t = 1 + s \Rightarrow s = t - 1 = 1$
3. **Probe:** $2 + 0 \cdot t = 1 + s$ → $2 = 1 + 1 = 2$ ✓

Die Probe stimmt! Die Geraden **schneiden sich**.

**Schnittpunkt:** Setze $t = 2$ in $g$ ein:
$$S = \begin{pmatrix} 1 + 2 \\ 0 + 2 \\ 2 + 0 \end{pmatrix} = \begin{pmatrix} 3 \\ 2 \\ 2 \end{pmatrix}$$

### Beispiel: Windschiefe Geraden

$$g: \vec{x} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} + t \cdot \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}$$

$$h: \vec{x} = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} + s \cdot \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}$$

**Gleichungssystem:**
1. $1 + t = 0 \Rightarrow t = -1$
2. $0 = 1 + s \Rightarrow s = -1$
3. **Probe:** $0 + t = 0 + s$ → $-1 = -1$ ✓

Warte, die Probe stimmt. Prüfen wir nochmal mit allen drei Gleichungen korrekt:

1. $1 + t = 0 + 0 \cdot s \Rightarrow t = -1$
2. $0 + 0 \cdot t = 1 + s \Rightarrow s = -1$
3. $0 + t = 0 + s$ → $-1 = -1$ ✓

Tatsächlich schneiden sich diese Geraden. Besseres Beispiel für windschief:

$$g: \vec{x} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} + t \cdot \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$$ (x-Achse)

$$h: \vec{x} = \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} + s \cdot \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$$ (parallel zur z-Achse, verschoben)

**Gleichungssystem:**
1. $t = 0$ 
2. $0 = 1 \Rightarrow$ Widerspruch!

Bereits Gleichung 2 liefert einen Widerspruch. Die Geraden sind **windschief**.

## Zusammenfassung: Entscheidungsbaum

```
Sind die Richtungsvektoren kollinear?
│
├─ Ja → Liegt ein Punkt von g auf h?
│        ├─ Ja → IDENTISCH
│        └─ Nein → PARALLEL
│
└─ Nein → Hat das LGS eine Lösung?
          ├─ Ja → SCHNEIDEND (Schnittpunkt berechenbar)
          └─ Nein → WINDSCHIEF
```

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Geraden-in-Parameterform]] — Grundlagen der Geradendarstellung
- → [[Schnittpunkte-und-Schnittgeraden]] — Berechnung von Schnittpunkten
- → [[Abstaende-zwischen-Punkten-und-Geraden]] — Abstand windschiefer Geraden
- → [[Winkelberechnungen]] — Schnittwinkel zweier Geraden
- → [[Gleichungssysteme]] — Lösen linearer Gleichungssysteme

> [!warning] **Prüfungsrelevant**
> - Systematisches Prüfschema für Lagebeziehungen
> - Erkennen kollinearer Richtungsvektoren
> - Aufstellen und Lösen des Gleichungssystems zum Schnittpunkt
> - Unterscheidung schneidend vs. windschief durch Probe

> [!question] **Typische Prüfungsfragen**
> - Untersuchen Sie die Lage der Geraden $g$ und $h$ zueinander und bestimmen Sie ggf. den Schnittpunkt.
> - Zeigen Sie, dass die Geraden $g: \vec{x} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} + t \begin{pmatrix} 2 \\ 1 \\ -1 \end{pmatrix}$ und $h: \vec{x} = \begin{pmatrix} 0 \\ 1 \\ 2 \end{pmatrix} + s \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$ windschief sind.
> - Für welchen Wert von $a$ schneiden sich die Geraden $g$ und $h$?

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg, 2018
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Europa-Lehrmittel, 2016
- Bigalke, A.; Köhler, N.: *Mathematik Gymnasiale Oberstufe*, Cornelsen, 2019

> [!tip] **Weiterführende Links**
> - [[Lagebeziehungen-von-Ebenen]] — Analoges für Ebenen
> - [[Geometrische-Anwendungen]] — Praktische Aufgaben
