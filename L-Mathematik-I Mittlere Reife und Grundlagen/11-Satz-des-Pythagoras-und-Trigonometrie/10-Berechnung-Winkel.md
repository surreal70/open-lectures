---
title: "Berechnung von Winkeln"
created: 2026-10-13
modified: 2026-10-25
chapter: "11"
section: "10"
status: "draft - review pending"
type: lecture
keywords:
  - Winkelberechnung
  - Arkusfunktionen
  - arcsin
  - arccos
  - arctan
---

# Berechnung von Winkeln

> [!info] Lernziele
> - Winkel aus gegebenen Seitenlängen berechnen
> - Die Arkusfunktionen richtig anwenden
> - Den Taschenrechner korrekt benutzen
> - Typische Anwendungen beherrschen

## Überblick

Während wir bisher aus Winkeln und Seiten andere Seiten berechnet haben, geht es nun umgekehrt: Wir kennen die Seiten und suchen den Winkel. Dafür brauchen wir die **Umkehrfunktionen** (Arkusfunktionen) von Sinus, Kosinus und Tangens. Diese Berechnungen sind besonders wichtig bei Vermessungsaufgaben und in der Technik, wenn wir zum Beispiel die Neigung eines Dachs oder einer Rampe bestimmen wollen.

## Die Umkehrfunktionen

Um aus einem Seitenverhältnis den Winkel zu berechnen, brauchen wir die **Umkehrfunktionen** (Arkusfunktionen):

| Funktion | Umkehrfunktion | Schreibweisen |
|---|---|---|
| $\sin(\alpha) = x$ | $\alpha = \arcsin(x)$ | sin⁻¹(x) |
| $\cos(\alpha) = x$ | $\alpha = \arccos(x)$ | cos⁻¹(x) |
| $\tan(\alpha) = x$ | $\alpha = \arctan(x)$ | tan⁻¹(x) |

> [!note] **Was bedeutet „Umkehrfunktion"?**
> Die Arkusfunktionen machen das Gegenteil der Winkelfunktionen:
> - Sinus: Winkel → Verhältnis
> - Arkussinus: Verhältnis → Winkel
>
> Sie „kehren" den Prozess um – daher der Name.

> [!tip] **Lesehilfe**
> „arcsin(0,5) = 30°" liest man: „Der Winkel, dessen Sinus 0,5 ist, beträgt 30°."

## Formeln für die Winkelberechnung

$$\alpha = \arcsin\left(\frac{\text{Gegenkathete}}{\text{Hypotenuse}}\right)$$

$$\alpha = \arccos\left(\frac{\text{Ankathete}}{\text{Hypotenuse}}\right)$$

$$\alpha = \arctan\left(\frac{\text{Gegenkathete}}{\text{Ankathete}}\right)$$

## Auswahl der richtigen Funktion

| Bekannte Seiten | Verwende |
|---|---|
| Gegenkathete + Hypotenuse | arcsin |
| Ankathete + Hypotenuse | arccos |
| Beide Katheten | arctan |

## Beispiele

### Beispiel 1: Mit arcsin

Gegenkathete $a = 5$ cm, Hypotenuse $c = 13$ cm

$$\alpha = \arcsin\left(\frac{5}{13}\right) = \arcsin(0{,}385) \approx 22{,}6°$$

### Beispiel 2: Mit arccos

Ankathete $b = 12$ cm, Hypotenuse $c = 15$ cm

$$\alpha = \arccos\left(\frac{12}{15}\right) = \arccos(0{,}8) \approx 36{,}9°$$

### Beispiel 3: Mit arctan

Gegenkathete $a = 7$ cm, Ankathete $b = 4$ cm

$$\alpha = \arctan\left(\frac{7}{4}\right) = \arctan(1{,}75) \approx 60{,}3°$$

## Taschenrechner-Hinweise

> [!warning] Wichtig
> 1. **Winkeleinheit prüfen**: Der Taschenrechner muss auf **DEG** (Grad) eingestellt sein, nicht auf RAD!
> 
> 2. **Eingabereihenfolge**:
>    - Erst den Bruch berechnen oder eingeben
>    - Dann die Umkehrfunktion anwenden
>    
> 3. **Tastenbezeichnung**:
>    - Oft als `sin⁻¹`, `cos⁻¹`, `tan⁻¹` oder
>    - `asin`, `acos`, `atan` oder
>    - Über `SHIFT` + `sin` etc.

## Den zweiten spitzen Winkel berechnen

Da die Winkelsumme im Dreieck 180° beträgt und ein Winkel 90° ist:

$$\beta = 90° - \alpha$$

> [!example] Beispiel
> Wenn $\alpha = 35°$, dann $\beta = 90° - 35° = 55°$.

## Praktische Anwendungen

### Neigungswinkel einer Rampe

Eine Rampe ist 10 m lang und überwindet eine Höhe von 1,5 m.

![[winkel-rampe.png]]
*<span class="fig-id">11-10-winkel-rampe</span>: Eine 10 m lange Rampe überwindet 1,5 m Höhe; der Arkussinus liefert den Neigungswinkel $\alpha$.*

$$\alpha = \arcsin\left(\frac{1{,}5}{10}\right) = \arcsin(0{,}15) \approx 8{,}6°$$

### Blickwinkel zu einem Turm

Ein 50 m hoher Turm wird aus 80 m Entfernung betrachtet.

$$\alpha = \arctan\left(\frac{50}{80}\right) = \arctan(0{,}625) \approx 32°$$

### Dachneigung

Ein Satteldach hat bei einer Firsthöhe von 4 m und einer halben Hausbreite von 6 m welchen Neigungswinkel?

$$\alpha = \arctan\left(\frac{4}{6}\right) = \arctan(0{,}667) \approx 33{,}7°$$

## Wichtige Wertebereiche

Die Arkusfunktionen liefern Winkel in bestimmten Bereichen:

| Funktion | Ergebnisbereich (für positive Argumente) |
|---|---|
| arcsin | 0° bis 90° |
| arccos | 0° bis 90° |
| arctan | 0° bis 90° |

Im rechtwinkligen Dreieck sind die berechneten Winkel immer zwischen 0° und 90° – das passt also perfekt.

## Zusammenfassung

> [!abstract] Kernpunkte
> - Arkusfunktionen sind die Umkehrungen von sin, cos, tan
> - arcsin: wenn Gegenkathete und Hypotenuse bekannt
> - arccos: wenn Ankathete und Hypotenuse bekannt
> - arctan: wenn beide Katheten bekannt
> - Taschenrechner auf DEG stellen
> - Zweiter Winkel: $\beta = 90° - \alpha$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[09-Berechnung-Seitenlaengen|Seitenlängen berechnen]] – Der umgekehrte Fall
- → [[11-Steigungen-Neigungswinkel|Steigungen und Neigungswinkel]] – Praktische Anwendung
- → [[12-Vermessungsaufgaben|Vermessungsaufgaben]] – Komplexe Beispiele

## Übungsaufgaben

1. Berechne den Winkel α:
   - Gegenkathete 6 cm, Hypotenuse 10 cm
   - Ankathete 8 cm, Hypotenuse 17 cm
   - Gegenkathete 5 cm, Ankathete 12 cm

2. Berechne beide spitzen Winkel des Dreiecks mit:
   - $a = 3$ cm, $b = 4$ cm, $c = 5$ cm

3. Eine 6 m lange Leiter steht so, dass ihr Fuß 2 m von der Wand entfernt ist. Unter welchem Winkel lehnt sie an der Wand?

4. Ein Flugzeug steigt auf 3000 m Höhe, nachdem es 8 km horizontal geflogen ist. Berechne den Steigwinkel.

5. Eine Skisprungschanze hat bei einer Anlauflänge von 95 m einen Höhenunterschied von 38 m. Wie groß ist der Neigungswinkel?

---

**Navigation**: [[09-Berechnung-Seitenlaengen|← Seitenlängen]] | [[00-Pythagoras-Trigonometrie-Index|Übersicht]] | [[11-Steigungen-Neigungswinkel|Steigungen →]]
