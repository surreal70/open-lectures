---
author: Andreas Hümmer
title: Gradmaß und Bogenmaß
tags:
  - content
  - mathe
  - trigonometrie
  - gradmass
  - bogenmass
  - radiant
created: 2025-06-20
modified: 2025-06-20
---

# Gradmaß und Bogenmaß

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das Gradmaß und das Bogenmaß als Winkelmaßsysteme verstehen
> - Winkel zwischen beiden Systemen sicher umrechnen können
> - Die Vorteile des Bogenmaßes für die Analysis erkennen
> - Die wichtigsten Winkelwerte in beiden Maßen auswendig kennen

---

## Überblick

In der Mathematik existieren zwei gebräuchliche Systeme zur Winkelmessung: das **Gradmaß** (aus der Alltagsgeometrie bekannt) und das **Bogenmaß** (in der Analysis unverzichtbar). Während das Gradmaß intuitiver erscheint, ist das Bogenmaß für die Infinitesimalrechnung und die Definition der trigonometrischen Funktionen als stetige Funktionen wesentlich eleganter.

## Das Gradmaß

### Definition

Im **Gradmaß** wird ein Vollwinkel in $360$ gleiche Teile unterteilt. Jeder Teil entspricht einem Grad.

$$1 \text{ Vollwinkel} = 360°$$

Ein Grad wird weiter unterteilt in:
- **Minuten:** $1° = 60'$ (Bogenminuten)
- **Sekunden:** $1' = 60''$ (Bogensekunden)

### Historischer Hintergrund

Die Zahl 360 stammt aus der babylonischen Astronomie (ca. 2000 v. Chr.). Sie hat viele Teiler (1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, ...), was praktische Rechnungen erleichterte.

### Wichtige Winkel im Gradmaß

| Winkel | Bedeutung |
|--------|-----------|
| $0°$ | Nullwinkel |
| $30°$ | $\frac{1}{12}$ Vollwinkel |
| $45°$ | $\frac{1}{8}$ Vollwinkel |
| $60°$ | $\frac{1}{6}$ Vollwinkel |
| $90°$ | Rechter Winkel |
| $180°$ | Gestreckter Winkel |
| $360°$ | Vollwinkel |

## Das Bogenmaß

### Definition über den Einheitskreis

Das **Bogenmaß** (auch **Radiant**, Einheit: rad) ist definiert über die Bogenlänge am Einheitskreis:

> Der Winkel im Bogenmaß entspricht der Länge des Kreisbogens, den der Winkel auf dem Einheitskreis (Radius $r = 1$) ausschneidet.

$$\alpha \text{ (in rad)} = \frac{\text{Bogenlänge } b}{\text{Radius } r}$$

Für den Einheitskreis ($r = 1$) gilt direkt:

$$\alpha = b$$

### Vollwinkel im Bogenmaß

Der Umfang des Einheitskreises beträgt $U = 2\pi r = 2\pi$.

Daher gilt:

$$360° = 2\pi \text{ rad}$$

### Fundamentale Umrechnungsbeziehung

Aus $360° = 2\pi$ folgen die Umrechnungsformeln:

$$\boxed{\alpha_{\text{rad}} = \alpha_{\text{deg}} \cdot \frac{\pi}{180°}}$$

$$\boxed{\alpha_{\text{deg}} = \alpha_{\text{rad}} \cdot \frac{180°}{\pi}}$$

### Wichtige Winkel im Bogenmaß

| Gradmaß | Bogenmaß | Dezimalwert (ca.) |
|---------|----------|-------------------|
| $0°$ | $0$ | $0$ |
| $30°$ | $\frac{\pi}{6}$ | $0{,}524$ |
| $45°$ | $\frac{\pi}{4}$ | $0{,}785$ |
| $60°$ | $\frac{\pi}{3}$ | $1{,}047$ |
| $90°$ | $\frac{\pi}{2}$ | $1{,}571$ |
| $120°$ | $\frac{2\pi}{3}$ | $2{,}094$ |
| $180°$ | $\pi$ | $3{,}142$ |
| $270°$ | $\frac{3\pi}{2}$ | $4{,}712$ |
| $360°$ | $2\pi$ | $6{,}283$ |

## Umrechnung: Beispiele

### Beispiel 1: Gradmaß → Bogenmaß

Wandle $75°$ in Bogenmaß um:

$$75° \cdot \frac{\pi}{180°} = \frac{75\pi}{180} = \frac{5\pi}{12} \approx 1{,}309 \text{ rad}$$

### Beispiel 2: Bogenmaß → Gradmaß

Wandle $\frac{5\pi}{4}$ in Gradmaß um:

$$\frac{5\pi}{4} \cdot \frac{180°}{\pi} = \frac{5 \cdot 180°}{4} = 225°$$

### Beispiel 3: Dezimales Bogenmaß → Gradmaß

Wandle $2{,}5$ rad in Gradmaß um:

$$2{,}5 \cdot \frac{180°}{\pi} \approx 2{,}5 \cdot 57{,}3° \approx 143{,}2°$$

## Vorteile des Bogenmaßes

### In der Analysis

Das Bogenmaß ist in der Analysis unverzichtbar, weil nur dann die Ableitungsformeln elegant sind:

$$\frac{d}{dx}\sin(x) = \cos(x) \quad \text{nur für } x \text{ im Bogenmaß!}$$

Im Gradmaß würde gelten:

$$\frac{d}{dx}\sin(x°) = \frac{\pi}{180} \cdot \cos(x°)$$

### Grenzwert

Der fundamentale Grenzwert

$$\lim_{x \to 0} \frac{\sin(x)}{x} = 1$$

gilt **nur im Bogenmaß**.

### Bogenlängenberechnung

Die Bogenlänge eines Kreissektors berechnet sich elegant:

$$b = r \cdot \alpha$$

wobei $\alpha$ im Bogenmaß angegeben wird.

### Kreissektorberechnung

Fläche eines Kreissektors:

$$A = \frac{1}{2} r^2 \cdot \alpha$$

## Schnelle Umrechnung: Merkregel

Eine praktische Näherung:

$$1 \text{ rad} \approx 57{,}3°$$

$$1° \approx 0{,}0175 \text{ rad}$$

Genau gilt:

$$1 \text{ rad} = \frac{180°}{\pi} \approx 57°17'45''$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Winkelmasse]] – Grundlagen der Winkelmessung
- → [[Einheitskreis]] – Das Bogenmaß wird am Einheitskreis definiert
- → [[Sinus-und-Kosinus]] – Trigonometrische Funktionen verwenden das Bogenmaß
- → [[Periodische-Vorgaenge]] – Periodenlänge im Bogenmaß

> [!warning] **Prüfungsrelevant**
> - Die Umrechnungsformeln zwischen Grad- und Bogenmaß **auswendig** können
> - Wichtige Winkel ($30°$, $45°$, $60°$, $90°$, $180°$) in beiden Maßen kennen
> - Im Abitur: Bei Analysis-Aufgaben **immer Bogenmaß** verwenden
> - Taschenrechner auf korrekten Modus (DEG/RAD) achten!

> [!question] **Typische Prüfungsfragen**
> - Rechnen Sie $135°$ in Bogenmaß um.
> - Welchem Winkel im Gradmaß entspricht $\frac{7\pi}{6}$?
> - Warum verwendet man in der Analysis das Bogenmaß statt des Gradmaßes?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020.
- Barth, F. & Haller, R.: Stochastik Leistungskurs. Ehrenwirth Verlag, 2003.

> [!tip] **Weiterführende Links**
> - [[Einheitskreis]] – Geometrische Veranschaulichung des Bogenmaßes
> - [[05-Differentialrechnung-I-Index]] – Ableitung trigonometrischer Funktionen
