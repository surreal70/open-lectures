---
author: Andreas Hümmer
title: Additionstheoreme
tags:
  - content
  - mathe
  - trigonometrie
  - additionstheoreme
  - formeln
created: 2025-06-20
modified: 2025-06-20
---

# Additionstheoreme

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Additionstheoreme für Sinus und Kosinus kennen und anwenden können
> - Funktionswerte zusammengesetzter Winkel berechnen können
> - Die Doppelwinkelformeln als Spezialfall ableiten können
> - Die Theoreme zum Lösen von Gleichungen und Vereinfachen nutzen können

---

## Überblick

Die **Additionstheoreme** sind fundamentale Formeln, die es ermöglichen, trigonometrische Funktionen von Winkelsummen und -differenzen in Produkte einzelner Funktionswerte umzuschreiben. Sie bilden die Grundlage für viele weitere trigonometrische Identitäten und haben zahlreiche Anwendungen in Analysis, Physik und Technik.

## Die Additionstheoreme für Sinus und Kosinus

### Additionstheorem für Sinus

$$\boxed{\sin(\alpha + \beta) = \sin(\alpha)\cos(\beta) + \cos(\alpha)\sin(\beta)}$$

$$\boxed{\sin(\alpha - \beta) = \sin(\alpha)\cos(\beta) - \cos(\alpha)\sin(\beta)}$$

### Additionstheorem für Kosinus

$$\boxed{\cos(\alpha + \beta) = \cos(\alpha)\cos(\beta) - \sin(\alpha)\sin(\beta)}$$

$$\boxed{\cos(\alpha - \beta) = \cos(\alpha)\cos(\beta) + \sin(\alpha)\sin(\beta)}$$

### Merkregel

**Sinus (Summe):** „Sinus-Cosinus plus Cosinus-Sinus"  
**Kosinus (Summe):** „Cosinus-Cosinus minus Sinus-Sinus"

Bei der Differenz ändert sich jeweils das **Vorzeichen in der Mitte**.

## Geometrischer Beweis

### Beweis des Kosinus-Additionstheorems

Betrachten wir zwei Punkte $P_1$ und $P_2$ auf dem Einheitskreis:
- $P_1 = (\cos(\alpha), \sin(\alpha))$
- $P_2 = (\cos(\beta), \sin(\beta))$

Der Abstand zwischen $P_1$ und $P_2$ kann auf zwei Arten berechnet werden:

**Methode 1:** Mit dem Kosinussatz im Dreieck $OP_1P_2$:
$$|P_1P_2|^2 = 2 - 2\cos(\alpha - \beta)$$

**Methode 2:** Mit der Abstandsformel:
$$|P_1P_2|^2 = (\cos(\alpha) - \cos(\beta))^2 + (\sin(\alpha) - \sin(\beta))^2$$

Gleichsetzen und Vereinfachen liefert das Additionstheorem.

## Das Additionstheorem für Tangens

$$\tan(\alpha + \beta) = \frac{\tan(\alpha) + \tan(\beta)}{1 - \tan(\alpha)\tan(\beta)}$$

$$\tan(\alpha - \beta) = \frac{\tan(\alpha) - \tan(\beta)}{1 + \tan(\alpha)\tan(\beta)}$$

### Herleitung

$$\tan(\alpha + \beta) = \frac{\sin(\alpha + \beta)}{\cos(\alpha + \beta)}$$

Einsetzen der Additionstheoreme und Division durch $\cos(\alpha)\cos(\beta)$ liefert die Formel.

## Anwendung: Berechnung von Funktionswerten

### Beispiel 1: $\sin(75°)$

$75° = 45° + 30°$

$$\sin(75°) = \sin(45° + 30°)$$
$$= \sin(45°)\cos(30°) + \cos(45°)\sin(30°)$$
$$= \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} + \frac{\sqrt{2}}{2} \cdot \frac{1}{2}$$
$$= \frac{\sqrt{6}}{4} + \frac{\sqrt{2}}{4}$$
$$= \frac{\sqrt{6} + \sqrt{2}}{4}$$

### Beispiel 2: $\cos(15°)$

$15° = 45° - 30°$

$$\cos(15°) = \cos(45° - 30°)$$
$$= \cos(45°)\cos(30°) + \sin(45°)\sin(30°)$$
$$= \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} + \frac{\sqrt{2}}{2} \cdot \frac{1}{2}$$
$$= \frac{\sqrt{6} + \sqrt{2}}{4}$$

### Beispiel 3: $\tan(75°)$

$$\tan(75°) = \tan(45° + 30°) = \frac{\tan(45°) + \tan(30°)}{1 - \tan(45°)\tan(30°)}$$
$$= \frac{1 + \frac{1}{\sqrt{3}}}{1 - 1 \cdot \frac{1}{\sqrt{3}}} = \frac{\sqrt{3} + 1}{\sqrt{3} - 1}$$

Rationalisieren:
$$= \frac{(\sqrt{3} + 1)^2}{(\sqrt{3} - 1)(\sqrt{3} + 1)} = \frac{4 + 2\sqrt{3}}{2} = 2 + \sqrt{3}$$

## Herleitung der Doppelwinkelformeln

Die Doppelwinkelformeln sind Spezialfälle der Additionstheoreme mit $\beta = \alpha$:

### Sinus

$$\sin(2\alpha) = \sin(\alpha + \alpha) = \sin(\alpha)\cos(\alpha) + \cos(\alpha)\sin(\alpha)$$
$$= 2\sin(\alpha)\cos(\alpha)$$

### Kosinus

$$\cos(2\alpha) = \cos(\alpha + \alpha) = \cos(\alpha)\cos(\alpha) - \sin(\alpha)\sin(\alpha)$$
$$= \cos^2(\alpha) - \sin^2(\alpha)$$

### Tangens

$$\tan(2\alpha) = \frac{2\tan(\alpha)}{1 - \tan^2(\alpha)}$$

## Anwendung: Vereinfachung von Ausdrücken

### Beispiel

Vereinfache $\sin(x)\cos(y) + \cos(x)\sin(y)$:

Dies ist genau das Additionstheorem rückwärts gelesen:
$$\sin(x)\cos(y) + \cos(x)\sin(y) = \sin(x + y)$$

### Beispiel: Lineare Kombination

Der Ausdruck $a\sin(x) + b\cos(x)$ kann mit den Additionstheoremen umgeschrieben werden:

$$a\sin(x) + b\cos(x) = r\sin(x + \varphi)$$

wobei:
$$r = \sqrt{a^2 + b^2}$$
$$\tan(\varphi) = \frac{b}{a}$$

Dies ist wichtig für die Behandlung von Schwingungen!

## Weitere nützliche Formeln

### Dreifache Winkel

$$\sin(3\alpha) = 3\sin(\alpha) - 4\sin^3(\alpha)$$
$$\cos(3\alpha) = 4\cos^3(\alpha) - 3\cos(\alpha)$$

Diese folgen durch mehrfache Anwendung der Additionstheoreme.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Trigonometrische-Identitaeten]] – Weitere Identitäten und Herleitungen
- → [[Einheitskreis]] – Geometrischer Hintergrund
- → [[Trigonometrische-Gleichungen]] – Anwendung zum Lösen von Gleichungen
- → [[Phasenverschiebung]] – Anwendung bei Schwingungen

> [!warning] **Prüfungsrelevant**
> - Die Additionstheoreme für Sinus und Kosinus **auswendig** können
> - Funktionswerte wie $\sin(75°)$ oder $\cos(15°)$ berechnen können
> - Die Doppelwinkelformeln als Spezialfall ableiten können
> - Ausdrücke der Form $a\sin(x) + b\cos(x)$ zusammenfassen können

> [!question] **Typische Prüfungsfragen**
> - Berechnen Sie $\cos(105°)$ exakt ohne Taschenrechner.
> - Vereinfachen Sie $\sin(x + \frac{\pi}{6})$ mit dem Additionstheorem.
> - Schreiben Sie $\sqrt{3}\sin(x) + \cos(x)$ in der Form $r\sin(x + \varphi)$.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020.
- Heuser, H.: Lehrbuch der Analysis, Teil 1. Springer Vieweg, 2009.

> [!tip] **Weiterführende Links**
> - [[Trigonometrische-Gleichungen]] – Lösen mit Additionstheoremen
> - [[Anwendungen-bei-Schwingungen-und-Wellen]] – Physikalische Anwendung
