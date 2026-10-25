---
title: "Einführung in die Trigonometrie"
created: 2026-10-13
modified: 2026-10-25
chapter: "11"
section: "05"
status: final
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

## Überblick

Die Trigonometrie erweitert unsere Möglichkeiten, mit Dreiecken zu arbeiten, erheblich. Während der Satz des Pythagoras nur Seitenlängen miteinander verknüpft, stellt die Trigonometrie eine Verbindung zwischen **Winkeln und Seiten** her. Das macht sie zu einem unverzichtbaren Werkzeug in Vermessung, Navigation, Architektur und Technik.

## Was ist Trigonometrie?

**Trigonometrie** (griech. „Dreiecksmessung") beschäftigt sich mit den Beziehungen zwischen Winkeln und Seiten in Dreiecken.

> [!note] **Historischer Kontext**
> Die Trigonometrie entstand aus praktischen Bedürfnissen: Die alten Griechen brauchten sie für die Astronomie, um Sternpositionen und Planetenbahnen zu berechnen. Der Astronom Hipparchos (ca. 190–120 v. Chr.) gilt als „Vater der Trigonometrie". Er erstellte die ersten Sehnentafeln – Vorläufer unserer heutigen Sinustabellen.
> 
> Im arabischen Raum wurde die Trigonometrie im Mittelalter weiterentwickelt. Der Begriff „Sinus" stammt von einer fehlerhaften Übersetzung des arabischen Wortes „jayb" (Tasche, Bucht) ins Lateinische.

> [!note] Kernidee
> Die Winkelfunktionen beschreiben, wie sich die **Seitenverhältnisse** eines rechtwinkligen Dreiecks bei verschiedenen Winkeln ändern. Ein Dreieck mit einem 30°-Winkel hat immer dieselben Seitenverhältnisse – egal wie groß es ist!

## Das rechtwinklige Dreieck als Grundlage

![[trigonometrie-dreieck.png]]
*<span class="fig-id">11-05-trigonometrie-dreieck</span>: Bezogen auf den Winkel $\alpha$: Ankathete (anliegend), Gegenkathete (gegenüber) und Hypotenuse (gegenüber dem rechten Winkel).*

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
> **SOH-CAH-TOA** (international bekannt):
> - **S**ine = **O**pposite / **H**ypotenuse (sin = Gegenkathete / Hypotenuse)
> - **C**osine = **A**djacent / **H**ypotenuse (cos = Ankathete / Hypotenuse)
> - **T**angent = **O**pposite / **A**djacent (tan = Gegenkathete / Ankathete)
> 
> **Deutsche Variante: „GAGA HüHü AG"**:
> - **G**egenkathete, **A**nkathete für Tangens (**GA**)
> - **G**egenkathete, **A**nkathete – eine davon durch (**GA**)
> - **Hü**potenuse bei Sinus und Kosinus (**Hü** **Hü**)
> - **A**nkathete bei Kosinus, **G**egenkathete bei Sinus (**AG**)
> 
> **Oder ganz einfach als Tabelle merken**:
> - **sin** = **G**egen / **H**ypotenuse → „Gegen H"
> - **cos** = **A**n / **H**ypotenuse → „An H"
> - **tan** = **G**egen / **A**n → „Gegen An"

> [!warning] **Häufiger Fehler**
> Viele verwechseln Ankathete und Gegenkathete. Denke daran: Diese Begriffe sind immer **relativ zum betrachteten Winkel**! Die Ankathete liegt **am** Winkel an, die Gegenkathete liegt ihm **gegenüber**.

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

> [!tip] **Anschauliche Erklärung**
> Diese Identität folgt direkt aus dem Satz des Pythagoras: Wenn die Hypotenuse die Länge 1 hat, dann ist $\sin(\alpha)$ die Länge der Gegenkathete und $\cos(\alpha)$ die Länge der Ankathete. Nach Pythagoras gilt dann: Gegenkathete² + Ankathete² = Hypotenuse² → $\sin^2 + \cos^2 = 1$.

### Zwischen Tangens, Sinus und Kosinus

$$\tan(\alpha) = \frac{\sin(\alpha)}{\cos(\alpha)}$$

Diese Beziehung ist logisch: Tangens = Gegenkathete/Ankathete, und wenn man Zähler und Nenner jeweils durch die Hypotenuse teilt, erhält man sin/cos.

### Komplementärwinkel

Für Winkel $\alpha$ und $\beta$ mit $\alpha + \beta = 90°$:

$$\sin(\alpha) = \cos(\beta)$$
$$\cos(\alpha) = \sin(\beta)$$

> [!note] **Warum ist das so?**
> Bei Komplementärwinkeln tauschen Ankathete und Gegenkathete ihre Rollen. Was für den einen Winkel die Gegenkathete ist, ist für den anderen die Ankathete – und umgekehrt.

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

## Querverweise

Verwandte Themen in diesem Kapitel:

- → [[06-Sinus|Der Sinus]] – Detaillierte Behandlung
- → [[07-Kosinus|Der Kosinus]] – Detaillierte Behandlung
- → [[08-Tangens|Der Tangens]] – Detaillierte Behandlung
- → [[01-Rechtwinklige-Dreiecke|Rechtwinklige Dreiecke]] – Grundlagen
- → [[02-Satz-des-Pythagoras|Satz des Pythagoras]] – Die fundamentale Beziehung

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
