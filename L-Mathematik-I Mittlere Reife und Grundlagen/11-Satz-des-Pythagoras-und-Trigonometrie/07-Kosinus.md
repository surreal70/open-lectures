---
title: "Der Kosinus"
created: 2026-10-13
modified: 2026-10-13
chapter: "11"
section: "07"
status: "draft - review pending"
type: lecture
keywords:
  - Kosinus
  - Ankathete
  - Hypotenuse
  - Winkelfunktion
---

# Der Kosinus

> [!info] Lernziele
> - Die Definition des Kosinus verstehen und anwenden
> - Den Kosinus zur Berechnung von Seiten nutzen
> - Den Kosinus zur Berechnung von Winkeln nutzen
> - Den Zusammenhang zum Sinus kennen

## Definition

$$\cos(\alpha) = \frac{\text{Ankathete}}{\text{Hypotenuse}}$$

```
       C
       │╲
       │ ╲
       │  ╲
    a  │   ╲  c
       │    ╲(Hypotenuse)
       │  α ╲
       │______╲
       A   b   B
       (Ankathete)
       
       cos(α) = b/c
```

## Anwendungen

### Ankathete berechnen

**Gegeben**: Hypotenuse $c$ und Winkel $\alpha$

**Gesucht**: Ankathete $b$

$$b = c \cdot \cos(\alpha)$$

> [!example] Beispiel
> $c = 10$ cm, $\alpha = 35°$
> 
> $b = 10 \cdot \cos(35°) = 10 \cdot 0{,}819 = 8{,}19$ cm

### Hypotenuse berechnen

**Gegeben**: Ankathete $b$ und Winkel $\alpha$

**Gesucht**: Hypotenuse $c$

$$c = \frac{b}{\cos(\alpha)}$$

> [!example] Beispiel
> $b = 6$ cm, $\alpha = 48°$
> 
> $c = \frac{6}{\cos(48°)} = \frac{6}{0{,}669} \approx 8{,}97$ cm

### Winkel berechnen

**Gegeben**: Ankathete $b$ und Hypotenuse $c$

**Gesucht**: Winkel $\alpha$

$$\alpha = \cos^{-1}\left(\frac{b}{c}\right) = \arccos\left(\frac{b}{c}\right)$$

> [!example] Beispiel
> $b = 8$ cm, $c = 10$ cm
> 
> $\cos(\alpha) = \frac{8}{10} = 0{,}8$
> 
> $\alpha = \cos^{-1}(0{,}8) \approx 36{,}9°$

## Wertebereich

Der Kosinus kann nur Werte zwischen -1 und 1 annehmen:

$$-1 \leq \cos(\alpha) \leq 1$$

Im rechtwinkligen Dreieck (0° < α < 90°):

$$0 < \cos(\alpha) < 1$$

## Wichtige Werte

| Winkel | cos |
|---|---|
| 0° | 1 |
| 30° | $\frac{\sqrt{3}}{2} \approx 0{,}866$ |
| 45° | $\frac{\sqrt{2}}{2} \approx 0{,}707$ |
| 60° | 0,5 |
| 90° | 0 |

## Der Graph der Kosinusfunktion

```
  cos(α)
    1 ┤●
      │ ╲
  0,5 ┤   ╲
      │     ╲
    0 ┼───────●────→ α
      │  30  60  90
```

- Bei 0°: cos = 1 (Maximum)
- Bei 90°: cos = 0
- Der Kosinus fällt zwischen 0° und 90° monoton ab

## Zusammenhang zwischen Sinus und Kosinus

### Komplementärwinkel

$$\cos(\alpha) = \sin(90° - \alpha)$$

> [!example] Beispiel
> $\cos(30°) = \sin(60°) = \frac{\sqrt{3}}{2}$

### Trigonometrischer Pythagoras

$$\sin^2(\alpha) + \cos^2(\alpha) = 1$$

## Vergleich: Sinus vs. Kosinus

| Eigenschaft | Sinus | Kosinus |
|---|---|---|
| Formel | $\frac{\text{Gegenkathete}}{\text{Hypotenuse}}$ | $\frac{\text{Ankathete}}{\text{Hypotenuse}}$ |
| Wert bei 0° | 0 | 1 |
| Wert bei 45° | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{2}}{2}$ |
| Wert bei 90° | 1 | 0 |
| Verhalten 0°→90° | steigend | fallend |

## Praktisches Beispiel

> [!example] Schatten
> Ein 12 m hoher Mast wirft bei einem Sonnenstand von 35° (gemessen zur Horizontalen) einen Schatten. Wie lang ist der Schatten?
> 
> ```
>     │  ╱
>     │ ╱
> 12m │╱ 35°
>     └─────────
>       Schatten
> ```
> 
> Der Schattenwinkel am Boden ist der Komplementwinkel: $90° - 35° = 55°$
> 
> Oder direkt mit Tangens: $\tan(35°) = \frac{12}{s}$
> 
> $s = \frac{12}{\tan(35°)} = \frac{12}{0{,}7} \approx 17{,}1$ m

## Zusammenfassung

> [!abstract] Kernpunkte
> - $\cos(\alpha) = \frac{\text{Ankathete}}{\text{Hypotenuse}}$
> - Ankathete: $b = c \cdot \cos(\alpha)$
> - Hypotenuse: $c = \frac{b}{\cos(\alpha)}$
> - Winkel: $\alpha = \cos^{-1}\left(\frac{b}{c}\right)$
> - Kosinus fällt von 1 (bei 0°) auf 0 (bei 90°)

## Übungsaufgaben

1. Berechne die Ankathete:
   - $c = 20$ cm, $\alpha = 55°$
   - $c = 9$ cm, $\alpha = 30°$

2. Berechne die Hypotenuse:
   - $b = 7$ cm, $\alpha = 42°$
   - $b = 15$ cm, $\alpha = 60°$

3. Berechne den Winkel:
   - $b = 6$ cm, $c = 12$ cm
   - $b = 5$ cm, $c = 8$ cm

4. Prüfe: $\sin^2(40°) + \cos^2(40°) = ?$

5. Ein Flugzeug fliegt mit einer Geschwindigkeit von 800 km/h in einem Steigwinkel von 12°. Wie schnell bewegt es sich horizontal vorwärts?

---

**Navigation**: [[06-Sinus|← Sinus]] | [[00-Pythagoras-Trigonometrie-Index|Übersicht]] | [[08-Tangens|Tangens →]]
