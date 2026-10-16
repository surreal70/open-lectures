---
title: "Der Tangens"
created: 2026-10-13
modified: 2025-06-20
chapter: "11"
section: "08"
status: "draft - review pending"
type: lecture
keywords:
  - Tangens
  - Gegenkathete
  - Ankathete
  - Steigung
---

# Der Tangens

> [!info] Lernziele
> - Die Definition des Tangens verstehen und anwenden
> - Den Tangens zur Berechnung von Seiten nutzen
> - Den Zusammenhang zur Steigung kennen
> - Wissen, wann Tangens besonders nützlich ist

## Überblick

Der Tangens ist die dritte Winkelfunktion und hat eine besondere praktische Bedeutung: Er entspricht der **Steigung** einer Geraden. Wenn du auf einer Straße bergauf gehst, gibt der Tangens des Steigungswinkels an, wie viel Höhe du pro Meter horizontaler Strecke gewinnst. Der Name kommt vom lateinischen „tangens" (berührend), weil die Tangente eine Kurve in einem Punkt berührt.

## Definition

$$\tan(\alpha) = \frac{\text{Gegenkathete}}{\text{Ankathete}}$$

```
       C
       │╲
       │ ╲
       │  ╲
    a  │   ╲
(Gegen-│    ╲
kathete)│  α ╲
       │______╲
       A   b   B
       (Ankathete)
       
       tan(α) = a/b
```

> [!tip] **Anschauliche Vorstellung**
> Der Tangens beschreibt direkt die „Steilheit" eines Winkels: Wie viel geht es nach oben, wenn ich eine Einheit nach vorne gehe? Bei 45° ist die Antwort genau 1 (tan(45°) = 1), denn beide Katheten sind gleich lang.

## Zusammenhang mit Sinus und Kosinus

$$\tan(\alpha) = \frac{\sin(\alpha)}{\cos(\alpha)}$$

## Anwendungen

### Gegenkathete berechnen

**Gegeben**: Ankathete $b$ und Winkel $\alpha$

**Gesucht**: Gegenkathete $a$

$$a = b \cdot \tan(\alpha)$$

> [!example] Beispiel
> $b = 8$ cm, $\alpha = 50°$
> 
> $a = 8 \cdot \tan(50°) = 8 \cdot 1{,}19 \approx 9{,}54$ cm

### Ankathete berechnen

**Gegeben**: Gegenkathete $a$ und Winkel $\alpha$

**Gesucht**: Ankathete $b$

$$b = \frac{a}{\tan(\alpha)}$$

> [!example] Beispiel
> $a = 12$ cm, $\alpha = 35°$
> 
> $b = \frac{12}{\tan(35°)} = \frac{12}{0{,}7} \approx 17{,}14$ cm

### Winkel berechnen

**Gegeben**: Gegenkathete $a$ und Ankathete $b$

**Gesucht**: Winkel $\alpha$

$$\alpha = \tan^{-1}\left(\frac{a}{b}\right) = \arctan\left(\frac{a}{b}\right)$$

> [!example] Beispiel
> $a = 5$ cm, $b = 7$ cm
> 
> $\tan(\alpha) = \frac{5}{7} \approx 0{,}714$
> 
> $\alpha = \tan^{-1}(0{,}714) \approx 35{,}5°$

## Wertebereich

Im rechtwinkligen Dreieck (0° < α < 90°):

- Bei kleinen Winkeln: tan nahe 0
- Bei 45°: tan = 1
- Bei Winkeln nahe 90°: tan wird sehr groß (→ ∞)

## Wichtige Werte

| Winkel | tan |
|---|---|
| 0° | 0 |
| 30° | $\frac{\sqrt{3}}{3} \approx 0{,}577$ |
| 45° | 1 |
| 60° | $\sqrt{3} \approx 1{,}732$ |
| 90° | nicht definiert |

## Tangens und Steigung

> [!tip] Wichtige Verbindung
> Der Tangens eines Winkels entspricht der **Steigung** einer Geraden!

Dies ist eine der wichtigsten praktischen Anwendungen des Tangens. In der Analysis und bei linearen Funktionen spielt diese Verbindung eine zentrale Rolle.

```
    y
    ↑
    │      ╱
    │    ╱  m = tan(α)
    │  ╱ α
    │╱________→ x
```

$$m = \tan(\alpha)$$

$$\alpha = \arctan(m)$$

> [!example] **Alltagsbeispiel**
> Eine Straße mit 15% Steigung hat den Steigungswinkel $\alpha = \arctan(0{,}15) \approx 8{,}5°$. Umgekehrt: Eine Rampe mit 6° Neigung hat die Steigung $m = \tan(6°) \approx 0{,}105 = 10{,}5\%$.

## Wann benutzt man welche Funktion?

| Gegeben | Gesucht | Funktion |
|---|---|---|
| Hypotenuse + Winkel | Gegenkathete | sin |
| Hypotenuse + Winkel | Ankathete | cos |
| Ankathete + Winkel | Gegenkathete | tan |
| Beide Katheten | Winkel | tan |

> [!tip] Merkregel
> Wenn **keine Hypotenuse** beteiligt ist → **Tangens**!

## Praktisches Beispiel

> [!example] Höhenmessung
> Von einem Punkt, der 25 m vom Fuß eines Turms entfernt ist, wird die Turmspitze unter einem Winkel von 58° gesehen. Wie hoch ist der Turm?
> 
> ```
>         ╱
>        ╱│
>       ╱ │ h
>      ╱  │
>     ╱58°│
>    ●────┘
>     25 m
> ```
> 
> **Lösung**:
> $\tan(58°) = \frac{h}{25}$
> 
> $h = 25 \cdot \tan(58°) = 25 \cdot 1{,}6 = 40$ m

## Zusammenfassung

> [!abstract] Kernpunkte
> - $\tan(\alpha) = \frac{\text{Gegenkathete}}{\text{Ankathete}}$
> - Tangens = Steigung
> - Gegenkathete: $a = b \cdot \tan(\alpha)$
> - Ankathete: $b = \frac{a}{\tan(\alpha)}$
> - Winkel: $\alpha = \tan^{-1}\left(\frac{a}{b}\right)$
> - Nutze Tangens, wenn nur die beiden Katheten beteiligt sind

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[06-Sinus|Der Sinus]] – Gegenkathete / Hypotenuse
- → [[07-Kosinus|Der Kosinus]] – Ankathete / Hypotenuse
- → [[11-Steigungen-Neigungswinkel|Steigungen und Neigungswinkel]] – Praktische Anwendung
- → [[../09-Funktionen-und-Koordinatensysteme/06-Steigung-und-Achsenabschnitt|Steigung bei linearen Funktionen]] – Verbindung zur Analysis

## Übungsaufgaben

1. Berechne die Gegenkathete:
   - $b = 10$ cm, $\alpha = 32°$
   - $b = 5$ cm, $\alpha = 60°$

2. Berechne die Ankathete:
   - $a = 8$ cm, $\alpha = 45°$
   - $a = 14$ cm, $\alpha = 70°$

3. Berechne den Winkel:
   - $a = 6$ cm, $b = 6$ cm
   - $a = 10$ cm, $b = 4$ cm

4. Eine Straße hat eine Steigung von 12%. Welchem Winkel entspricht das?

5. Ein Feuerwehrmann steht 15 m vom Haus entfernt. Er sieht den Dachfirst unter einem Winkel von 48°. Seine Augenhöhe beträgt 1,70 m. Wie hoch ist das Haus?

---

**Navigation**: [[07-Kosinus|← Kosinus]] | [[00-Pythagoras-Trigonometrie-Index|Übersicht]] | [[09-Berechnung-Seitenlaengen|Seitenlängen →]]
