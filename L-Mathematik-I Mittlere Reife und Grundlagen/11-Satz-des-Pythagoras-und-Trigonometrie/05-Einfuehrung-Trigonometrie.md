---
title: "Einführung in die Trigonometrie"
created: 2026-10-13
modified: 2026-10-13
chapter: "11"
section: "05"
status: "draft - review pending"
type: lecture
keywords:
  - Trigonometrie
  - Winkelfunktionen
  - Sinus
  - Kosinus
  - Tangens
---

# Einführung in die Trigonometrie

> [!info] Lernziele
> - Den Begriff Trigonometrie verstehen
> - Die drei Winkelfunktionen kennenlernen
> - Die Bezeichnungen im rechtwinkligen Dreieck sicher verwenden
> - Den Zusammenhang zwischen Winkeln und Seitenverhältnissen verstehen

## Was ist Trigonometrie?

**Trigonometrie** (griech. „Dreiecksmessung") beschäftigt sich mit den Beziehungen zwischen Winkeln und Seiten in Dreiecken.

> [!note] Kernidee
> Die Winkelfunktionen beschreiben, wie sich die **Seitenverhältnisse** eines rechtwinkligen Dreiecks bei verschiedenen Winkeln ändern.

## Das rechtwinklige Dreieck als Grundlage

```
       C
       │╲
       │ ╲
       │  ╲
  Gegen-│   ╲  Hypotenuse
  kathete│    ╲
       │  α  ╲
       │______╲
       A Ankathete B
```

Bezogen auf den Winkel $\alpha$:
- **Ankathete**: die Kathete, die am Winkel $\alpha$ anliegt
- **Gegenkathete**: die Kathete, die dem Winkel $\alpha$ gegenüberliegt
- **Hypotenuse**: die längste Seite (gegenüber dem rechten Winkel)

> [!warning] Wichtig
> Ankathete und Gegenkathete sind immer **bezogen auf einen bestimmten Winkel**!

## Die drei Winkelfunktionen

### Übersicht

| Funktion | Abkürzung | Verhältnis |
|---|---|---|
| **Sinus** | sin | $\frac{\text{Gegenkathete}}{\text{Hypotenuse}}$ |
| **Kosinus** | cos | $\frac{\text{Ankathete}}{\text{Hypotenuse}}$ |
| **Tangens** | tan | $\frac{\text{Gegenkathete}}{\text{Ankathete}}$ |

### Formeln

$$\sin(\alpha) = \frac{\text{Gegenkathete}}{\text{Hypotenuse}} = \frac{a}{c}$$

$$\cos(\alpha) = \frac{\text{Ankathete}}{\text{Hypotenuse}} = \frac{b}{c}$$

$$\tan(\alpha) = \frac{\text{Gegenkathete}}{\text{Ankathete}} = \frac{a}{b}$$

## Merksprüche

> [!tip] Merksprüche für die Winkelfunktionen
> 
> **GAGA HüHü AG**:
> - **G**egenkathete **A**nkathete für Tangens (**GA**)
> - **G**egenkathete und **A**nkathete für die (**GA**)
> - **Hü**potenuse bei Sinus (**Hü**)
> - **Hü**potenuse bei Kosinus (**Hü**)
> - **A**nkathete bei Kosinus, **G**egenkathete bei Sinus (**AG**)
> 
> Oder einfacher:
> - **sin** = **G**egen / **H**ypotenuse
> - **cos** = **A**n / **H**ypotenuse  
> - **tan** = **G**egen / **A**n

## Werte spezieller Winkel

| Winkel | sin | cos | tan |
|---|---|---|---|
| 0° | 0 | 1 | 0 |
| 30° | 0,5 | $\frac{\sqrt{3}}{2}$ ≈ 0,87 | $\frac{\sqrt{3}}{3}$ ≈ 0,58 |
| 45° | $\frac{\sqrt{2}}{2}$ ≈ 0,71 | $\frac{\sqrt{2}}{2}$ ≈ 0,71 | 1 |
| 60° | $\frac{\sqrt{3}}{2}$ ≈ 0,87 | 0,5 | $\sqrt{3}$ ≈ 1,73 |
| 90° | 1 | 0 | nicht definiert |

## Zusammenhänge

### Zwischen Sinus und Kosinus

$$\sin^2(\alpha) + \cos^2(\alpha) = 1$$

(Dies ist der Satz des Pythagoras in trigonometrischer Form!)

### Zwischen Tangens, Sinus und Kosinus

$$\tan(\alpha) = \frac{\sin(\alpha)}{\cos(\alpha)}$$

### Komplementärwinkel

Für Winkel $\alpha$ und $\beta$ mit $\alpha + \beta = 90°$:

$$\sin(\alpha) = \cos(\beta)$$
$$\cos(\alpha) = \sin(\beta)$$

> [!example] Beispiel
> $\sin(30°) = \cos(60°) = 0{,}5$
> $\cos(30°) = \sin(60°) = \frac{\sqrt{3}}{2}$

## Der Taschenrechner

> [!tip] Umgang mit dem Taschenrechner
> - Achte auf die Einstellung: **DEG** (Grad) statt RAD (Bogenmaß)
> - Die Tasten `sin`, `cos`, `tan` berechnen den Funktionswert zu einem Winkel
> - Die Tasten `sin⁻¹`, `cos⁻¹`, `tan⁻¹` (oder `arcsin`, `arccos`, `arctan`) berechnen den Winkel zu einem Funktionswert

## Zusammenfassung

> [!abstract] Kernpunkte
> - Trigonometrie beschreibt Beziehungen zwischen Winkeln und Seiten
> - Drei Winkelfunktionen: Sinus, Kosinus, Tangens
> - Jede Funktion ist ein Verhältnis zweier Seiten
> - Ankathete und Gegenkathete sind immer bezogen auf einen bestimmten Winkel
> - Die Funktionswerte können mit dem Taschenrechner bestimmt werden

## Übungsaufgaben

1. Bestimme für das folgende Dreieck sin(α), cos(α), tan(α):
   - Gegenkathete zu α: 3 cm
   - Ankathete zu α: 4 cm
   - Hypotenuse: 5 cm

2. Berechne mit dem Taschenrechner:
   - sin(25°)
   - cos(72°)
   - tan(45°)

3. Für welchen Winkel gilt sin(α) = 0,5?

4. Ein rechtwinkliges Dreieck hat den Winkel α = 40° und die Hypotenuse c = 10 cm. Drücke die Katheten mit Winkelfunktionen aus.

---

**Navigation**: [[04-Anwendungen-Pythagoras|← Anwendungen]] | [[00-Pythagoras-Trigonometrie-Index|Übersicht]] | [[06-Sinus|Sinus →]]
