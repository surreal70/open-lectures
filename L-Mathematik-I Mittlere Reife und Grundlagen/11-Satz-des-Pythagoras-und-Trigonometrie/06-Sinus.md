---
title: "Der Sinus"
created: 2026-10-13
modified: 2026-10-25
chapter: "11"
section: "06"
status: final
type: lecture
keywords:
  - Sinus
  - Gegenkathete
  - Hypotenuse
  - Winkelfunktion
---

# Der Sinus

> [!info] Lernziele
> - Die Definition des Sinus verstehen und anwenden
> - Den Sinus zur Berechnung von Seiten nutzen
> - Den Sinus zur Berechnung von Winkeln nutzen
> - Den Verlauf der Sinusfunktion kennen

## Überblick

Der Sinus ist die wohl bekannteste der drei Winkelfunktionen. Er beschreibt das Verhältnis von Gegenkathete zu Hypotenuse in einem rechtwinkligen Dreieck. Der Name „Sinus" stammt aus dem Lateinischen und bedeutet „Bogen" oder „Bucht" – eine Anspielung auf die bogenförmige Kurve, die der Sinus beschreibt.

## Definition

$$\sin(\alpha) = \frac{\text{Gegenkathete}}{\text{Hypotenuse}}$$

![[sinus-dreieck.png]]
*<span class="fig-id">11-06-sinus-dreieck</span>: Im rechtwinkligen Dreieck ist $\sin(\alpha)$ das Verhältnis von Gegenkathete $a$ zur Hypotenuse $c$.*

> [!tip] **Anschauliche Vorstellung**
> Stelle dir vor, du schaust von Punkt A aus zum Punkt C hinauf. Der Sinus gibt an, wie „steil" dieser Blick ist – als Anteil der Hypotenuse. Bei α = 0° schaust du horizontal (sin = 0), bei α = 90° schaust du senkrecht nach oben (sin = 1).

## Anwendungen

### Gegenkathete berechnen

**Gegeben**: Hypotenuse $c$ und Winkel $\alpha$

**Gesucht**: Gegenkathete $a$

$$a = c \cdot \sin(\alpha)$$

> [!example] Beispiel
> $c = 10$ cm, $\alpha = 35°$
> 
> $a = 10 \cdot \sin(35°) = 10 \cdot 0{,}574 = 5{,}74$ cm

### Hypotenuse berechnen

**Gegeben**: Gegenkathete $a$ und Winkel $\alpha$

**Gesucht**: Hypotenuse $c$

$$c = \frac{a}{\sin(\alpha)}$$

> [!example] Beispiel
> $a = 8$ cm, $\alpha = 50°$
> 
> $c = \frac{8}{\sin(50°)} = \frac{8}{0{,}766} \approx 10{,}44$ cm

### Winkel berechnen

**Gegeben**: Gegenkathete $a$ und Hypotenuse $c$

**Gesucht**: Winkel $\alpha$

$$\alpha = \sin^{-1}\left(\frac{a}{c}\right) = \arcsin\left(\frac{a}{c}\right)$$

> [!example] Beispiel
> $a = 5$ cm, $c = 13$ cm
> 
> $\sin(\alpha) = \frac{5}{13} \approx 0{,}385$
> 
> $\alpha = \sin^{-1}(0{,}385) \approx 22{,}6°$

## Wertebereich

Der Sinus kann nur Werte zwischen -1 und 1 annehmen:

$$-1 \leq \sin(\alpha) \leq 1$$

Im rechtwinkligen Dreieck (0° < α < 90°):

$$0 < \sin(\alpha) < 1$$

## Wichtige Werte

Diese Werte solltest du auswendig kennen – sie kommen in Prüfungen häufig vor und helfen, Ergebnisse zu überprüfen:

| Winkel | sin | Merkregel |
|---|---|---|
| 0° | 0 | Am Anfang ist nichts „steil" |
| 30° | 0,5 | Genau die Hälfte |
| 45° | $\frac{\sqrt{2}}{2} \approx 0{,}707$ | Gleich wie cos(45°) |
| 60° | $\frac{\sqrt{3}}{2} \approx 0{,}866$ | Fast 1, aber noch nicht ganz |
| 90° | 1 | Maximum – senkrecht nach oben |

> [!tip] **Merkregel für die Werte**
> Die Sinuswerte bei 0°, 30°, 45°, 60°, 90° folgen einem Muster:
> $$\frac{\sqrt{0}}{2}, \frac{\sqrt{1}}{2}, \frac{\sqrt{2}}{2}, \frac{\sqrt{3}}{2}, \frac{\sqrt{4}}{2}$$
> Das ergibt: $0, 0{,}5, \frac{\sqrt{2}}{2}, \frac{\sqrt{3}}{2}, 1$

## Der Graph der Sinusfunktion

![[sinus-graph.png]]
*<span class="fig-id">11-06-sinus-graph</span>: Der Sinus steigt zwischen 0° und 90° monoton von 0 auf 1 an.*

- Bei 0°: sin = 0
- Bei 90°: sin = 1 (Maximum)
- Der Sinus steigt zwischen 0° und 90° monoton an

## Praktisches Beispiel

> [!example] Rampe
> Eine Rollstuhlrampe soll einen Höhenunterschied von 60 cm überwinden. Der maximale Steigungswinkel beträgt 6°. Wie lang muss die Rampe mindestens sein?
> 
> ![[sinus-rampe.png]]
> *<span class="fig-id">11-06-sinus-rampe</span>: Rampe mit Höhenunterschied 0,6 m und Steigungswinkel 6°.*
> 
> **Lösung**:
> $\sin(6°) = \frac{0{,}6}{c}$
> 
> $c = \frac{0{,}6}{\sin(6°)} = \frac{0{,}6}{0{,}105} \approx 5{,}7$ m

## Zusammenfassung

> [!abstract] Kernpunkte
> - $\sin(\alpha) = \frac{\text{Gegenkathete}}{\text{Hypotenuse}}$
> - Gegenkathete: $a = c \cdot \sin(\alpha)$
> - Hypotenuse: $c = \frac{a}{\sin(\alpha)}$
> - Winkel: $\alpha = \sin^{-1}\left(\frac{a}{c}\right)$
> - Werte zwischen 0 und 1 für Winkel zwischen 0° und 90°

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[05-Einfuehrung-Trigonometrie|Einführung Trigonometrie]] – Überblick über alle Winkelfunktionen
- → [[07-Kosinus|Der Kosinus]] – Die „Schwester" des Sinus
- → [[08-Tangens|Der Tangens]] – sin/cos als Verhältnis
- → [[09-Berechnung-Seitenlaengen|Seitenlängen berechnen]] – Anwendungen

## Übungsaufgaben

1. Berechne die Gegenkathete:
   - $c = 15$ cm, $\alpha = 40°$
   - $c = 8$ cm, $\alpha = 25°$

2. Berechne die Hypotenuse:
   - $a = 6$ cm, $\alpha = 30°$
   - $a = 12$ cm, $\alpha = 55°$

3. Berechne den Winkel:
   - $a = 4$ cm, $c = 8$ cm
   - $a = 7$ cm, $c = 10$ cm

4. Ein Drachenseil ist 50 m lang. Der Drachen fliegt in einem Winkel von 62° zur Horizontalen. Wie hoch fliegt er?

---

**Navigation**: [[05-Einfuehrung-Trigonometrie|← Einführung]] | [[00-Pythagoras-Trigonometrie-Index|Übersicht]] | [[07-Kosinus|Kosinus →]]
