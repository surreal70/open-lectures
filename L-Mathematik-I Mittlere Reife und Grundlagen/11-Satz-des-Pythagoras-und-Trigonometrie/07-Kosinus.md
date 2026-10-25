---
title: "Der Kosinus"
created: 2026-10-13
modified: 2026-10-25
chapter: "11"
section: "07"
status: final
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

## Überblick

Der Kosinus ist der „Bruder" des Sinus und beschreibt das Verhältnis von Ankathete zu Hypotenuse. Während der Sinus misst, wie weit man „nach oben" kommt, misst der Kosinus, wie weit man „nach vorne" kommt. Der Name stammt vom lateinischen „cosinus", was „Komplement-Sinus" bedeutet – denn $\cos(\alpha) = \sin(90° - \alpha)$.

## Definition

$$\cos(\alpha) = \frac{\text{Ankathete}}{\text{Hypotenuse}}$$

![[kosinus-dreieck.png]]
*<span class="fig-id">11-07-kosinus-dreieck</span>: Im rechtwinkligen Dreieck ist $\cos(\alpha)$ das Verhältnis von Ankathete $b$ zur Hypotenuse $c$.*

> [!tip] **Anschauliche Vorstellung**
> Wenn du auf der Hypotenuse entlanggehst, gibt der Kosinus an, wie viel du dabei „horizontal" vorankommst. Bei α = 0° gehst du rein horizontal (cos = 1), bei α = 90° gehst du rein vertikal und kommst horizontal nicht voran (cos = 0).

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

![[kosinus-graph.png]]
*<span class="fig-id">11-07-kosinus-graph</span>: Der Kosinus fällt zwischen 0° und 90° monoton von 1 auf 0 ab.*

- Bei 0°: cos = 1 (Maximum)
- Bei 90°: cos = 0
- Der Kosinus fällt zwischen 0° und 90° monoton ab

## Zusammenhang zwischen Sinus und Kosinus

### Komplementärwinkel

$$\cos(\alpha) = \sin(90° - \alpha)$$

Diese Beziehung erklärt auch den Namen „Kosinus" – er ist der Sinus des Komplementwinkels.

> [!example] Beispiel
> $\cos(30°) = \sin(60°) = \frac{\sqrt{3}}{2}$
> 
> Die Werte „tauschen die Plätze" bei Komplementwinkeln!

### Trigonometrischer Pythagoras

$$\sin^2(\alpha) + \cos^2(\alpha) = 1$$

> [!note] **Warum gilt das?**
> Diese fundamentale Identität folgt direkt aus dem Satz des Pythagoras. In einem rechtwinkligen Dreieck mit Hypotenuse 1 sind die Katheten gerade $\sin(\alpha)$ und $\cos(\alpha)$. Nach Pythagoras: $\sin^2 + \cos^2 = 1^2 = 1$.

> [!tip] **Praktischer Nutzen**
> Mit dieser Formel kannst du einen Wert aus dem anderen berechnen:
> - $\cos(\alpha) = \sqrt{1 - \sin^2(\alpha)}$
> - $\sin(\alpha) = \sqrt{1 - \cos^2(\alpha)}$

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
> ![[kosinus-schatten.png]]
> *<span class="fig-id">11-07-kosinus-schatten</span>: Ein 12 m hoher Mast mit Sonnenstand 35° zur Horizontalen wirft einen Schatten.*
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

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[06-Sinus|Der Sinus]] – Die „Schwester" des Kosinus
- → [[08-Tangens|Der Tangens]] – sin/cos als Verhältnis
- → [[05-Einfuehrung-Trigonometrie|Einführung Trigonometrie]] – Überblick
- → [[09-Berechnung-Seitenlaengen|Seitenlängen berechnen]] – Anwendungen

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
