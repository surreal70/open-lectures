---
title: "Der Satz des Pythagoras"
created: 2026-10-13
modified: 2026-10-25
chapter: "11"
section: "02"
status: "draft - review pending"
type: lecture
keywords:
  - Pythagoras
  - Kathetensatz
  - Hypotenusenquadrat
  - Beweis
---

# Der Satz des Pythagoras

> [!info] Lernziele
> - Den Satz des Pythagoras formulieren und verstehen
> - Die Formel korrekt anwenden
> - Die Bedeutung geometrisch interpretieren
> - Einen anschaulichen Beweis nachvollziehen

## Überblick

Der Satz des Pythagoras ist einer der bekanntesten und wichtigsten Sätze der gesamten Mathematik. Er beschreibt eine fundamentale Beziehung zwischen den Seiten eines rechtwinkligen Dreiecks und hat unzählige Anwendungen in Architektur, Navigation, Physik und vielen anderen Bereichen. Seine Eleganz und praktische Nützlichkeit haben ihn zum „Superstar" unter den mathematischen Sätzen gemacht.

## Der Satz

> [!warning] Satz des Pythagoras
> In einem **rechtwinkligen Dreieck** gilt:
> 
> $$a^2 + b^2 = c^2$$
> 
> Das Quadrat über der Hypotenuse ist gleich der Summe der Quadrate über den Katheten.

### Formulierung in Worten

> „In jedem rechtwinkligen Dreieck ist die Summe der Flächeninhalte der Quadrate über den Katheten gleich dem Flächeninhalt des Quadrates über der Hypotenuse."

Diese Formulierung macht deutlich, dass der Satz eigentlich eine Aussage über **Flächen** ist, nicht nur über Längen. Wenn du tatsächlich Quadrate auf die drei Seiten zeichnest, dann ist das große Quadrat (auf der Hypotenuse) genauso groß wie die beiden kleinen Quadrate (auf den Katheten) zusammen.

![[pythagoras-quadrate.png]]
*<span class="fig-id">11-02-pythagoras-quadrate</span>: Der Satz als Flächenaussage: Die Quadrate über den Katheten ($a^2$ und $b^2$) sind zusammen so groß wie das Quadrat über der Hypotenuse ($c^2$).*

## Historischer Hintergrund

> [!note] **Wer war Pythagoras?**
> Pythagoras von Samos (ca. 570–510 v. Chr.) war ein griechischer Philosoph und Mathematiker. Er gründete eine religiös-philosophische Gemeinschaft, die „Pythagoreer", die Mathematik als Schlüssel zum Verständnis des Universums betrachteten. Ihr Motto lautete: „Alles ist Zahl."

- Benannt nach dem griechischen Mathematiker **Pythagoras** (~570–510 v. Chr.)
- War aber schon den **Babyloniern** bekannt (~1800 v. Chr.) – auf der Tontafel „Plimpton 322" finden sich pythagoreische Tripel
- Auch in **China** und **Indien** unabhängig entdeckt
- Über **400 verschiedene Beweise** sind dokumentiert – darunter ein eleganter Beweis des US-Präsidenten James Garfield!

Die Pythagoreer hielten ihr Wissen zunächst geheim. Der Legende nach wurde ein Mitglied, das den Beweis verriet, mit dem Tod bestraft – allerdings ist diese Geschichte wohl eher Mythos als Historie.

## Anschaulicher Beweis

### Beweis durch Flächenvergleich

Dieser Beweis ist einer der elegantesten und anschaulichsten. Er basiert auf der Idee, dass die gleiche Fläche auf zwei verschiedene Arten zerlegt werden kann.

Man betrachtet ein großes Quadrat mit der Seitenlänge $(a + b)$. In seine Ecken legt man vier gleiche rechtwinklige Dreiecke (Katheten $a$, $b$); dazwischen bleibt ein gekipptes Quadrat mit der Seitenlänge $c$.

![[pythagoras-beweis.png]]
*<span class="fig-id">11-02-pythagoras-beweis</span>: Zerlegungsbeweis: Das große Quadrat $(a+b)^2$ besteht aus dem gekippten Quadrat $c^2$ und vier rechtwinkligen Dreiecken mit je Fläche $\tfrac{1}{2}ab$.*

Die Gesamtfläche des großen Quadrats lässt sich auf zwei Arten ausdrücken – einmal als $(a+b)^2$ ausmultipliziert, einmal als inneres Quadrat plus vier Dreiecke. Da beide dieselbe Fläche beschreiben:

$$a^2 + b^2 + 2ab = c^2 + 4 \cdot \frac{1}{2}ab$$
$$a^2 + b^2 + 2ab = c^2 + 2ab$$
$$a^2 + b^2 = c^2$$

> [!tip] **Warum funktioniert dieser Beweis?**
> Der Beweis nutzt die Tatsache, dass gleiche Flächen gleich bleiben, egal wie man sie zerlegt. Stell dir vor, du hast zwei identische Pizzen und schneidest sie unterschiedlich – am Ende hast du trotzdem gleich viel Pizza!

## Anwendung der Formel

Der Satz des Pythagoras wird typischerweise verwendet, um die dritte Seite eines rechtwinkligen Dreiecks zu berechnen, wenn zwei Seiten bekannt sind.

### Hypotenuse berechnen

Gegeben: Katheten $a$ und $b$, gesucht: Hypotenuse $c$

$$c = \sqrt{a^2 + b^2}$$

> [!example] Beispiel
> $a = 3$ cm, $b = 4$ cm
> 
> $c = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$ cm

### Kathete berechnen

Gegeben: Hypotenuse $c$ und eine Kathete $a$, gesucht: Kathete $b$

$$b = \sqrt{c^2 - a^2}$$

> [!example] Beispiel
> $c = 13$ cm, $a = 5$ cm
> 
> $b = \sqrt{13^2 - 5^2} = \sqrt{169 - 25} = \sqrt{144} = 12$ cm

> [!warning] **Häufiger Fehler**
> Bei der Berechnung einer Kathete wird oft versehentlich addiert statt subtrahiert:
> - **Falsch**: $a = \sqrt{c^2 + b^2}$ ❌
> - **Richtig**: $a = \sqrt{c^2 - b^2}$ ✓
> 
> Merke: Die Hypotenuse ist die **längste** Seite. Da das Ergebnis unter der Wurzel positiv sein muss, ziehst du das kleinere Quadrat (Kathete²) vom größeren (Hypotenuse²) ab.

## Formelübersicht

| Gesucht | Formel |
|---|---|
| Hypotenuse $c$ | $c = \sqrt{a^2 + b^2}$ |
| Kathete $a$ | $a = \sqrt{c^2 - b^2}$ |
| Kathete $b$ | $b = \sqrt{c^2 - a^2}$ |

## Wichtige Hinweise

> [!warning] Voraussetzung
> Der Satz des Pythagoras gilt **nur für rechtwinklige Dreiecke**!

> [!tip] Rechenschritte
> 1. Prüfen: Ist das Dreieck rechtwinklig?
> 2. Identifizieren: Welche Seite ist die Hypotenuse?
> 3. Einsetzen: Werte in die richtige Formel einsetzen
> 4. Ausrechnen: Quadrieren, Addieren/Subtrahieren, Wurzel ziehen

## Die Umkehrung des Satzes

> [!note] Umkehrung
> Wenn in einem Dreieck $a^2 + b^2 = c^2$ gilt (wobei $c$ die längste Seite ist), dann ist das Dreieck **rechtwinklig**.

Dies ermöglicht die **Prüfung auf Rechtwinkligkeit**. Diese Umkehrung ist besonders nützlich im Bauwesen: Handwerker können damit prüfen, ob eine Ecke wirklich rechtwinklig ist, ohne einen Winkelmesser zu benötigen.

> [!tip] **Anwendung im Alltag**
> Willst du prüfen, ob die Ecke deines Zimmers rechtwinklig ist? Miss 3 Meter an einer Wand, 4 Meter an der anderen, und prüfe, ob die Diagonale genau 5 Meter beträgt. Wenn ja, ist die Ecke rechtwinklig!

## Pythagoras im Alltag

Der Satz des Pythagoras begegnet uns überall:

- **Bildschirmdiagonalen**: Die „Zollangabe" bei Fernsehern ist die Diagonale – berechnet mit Pythagoras
- **Navigation**: GPS-Geräte berechnen Entfernungen „Luftlinie" mit dem Satz
- **Bauwesen**: Berechnung von Dachschrägen, Leiterlängen, Treppenstufen
- **Sport**: Die Diagonale eines Fußballfelds, der kürzeste Weg über den Platz

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[01-Rechtwinklige-Dreiecke|Rechtwinklige Dreiecke]] – Grundlagen und Bezeichnungen
- → [[03-Berechnung-unbekannter-Seiten|Berechnung unbekannter Seiten]] – Praktische Anwendungen
- → [[04-Anwendungen-Pythagoras|Anwendungen]] – Raumdiagonalen und mehr
- → [[../06-Potenzen-Wurzeln-und-Zahlendarstellung/06-Quadratwurzeln|Quadratwurzeln]] – Die mathematische Grundlage

## Zusammenfassung

> [!abstract] Kernpunkte
> - Im rechtwinkligen Dreieck: $a^2 + b^2 = c^2$
> - Die Hypotenuse $c$ liegt dem rechten Winkel gegenüber
> - Die Formel kann nach jeder Seite umgestellt werden
> - Der Satz gilt nur für rechtwinklige Dreiecke
> - Mit der Umkehrung kann man prüfen, ob ein Dreieck rechtwinklig ist

## Übungsaufgaben

1. Berechne die fehlende Seite:
   - $a = 6$ cm, $b = 8$ cm, $c = ?$
   - $a = 5$ cm, $c = 13$ cm, $b = ?$
   - $b = 15$ cm, $c = 17$ cm, $a = ?$

2. Prüfe, ob die Dreiecke rechtwinklig sind:
   - $a = 9$, $b = 12$, $c = 15$
   - $a = 4$, $b = 5$, $c = 6$

3. Ein rechtwinkliges Dreieck hat die Katheten 7 cm und 24 cm. Wie lang ist die Hypotenuse?

4. Die Hypotenuse eines rechtwinkligen Dreiecks ist 25 cm lang. Eine Kathete misst 7 cm. Wie lang ist die andere Kathete?

---

**Navigation**: [[01-Rechtwinklige-Dreiecke|← Rechtwinklige Dreiecke]] | [[00-Pythagoras-Trigonometrie-Index|Übersicht]] | [[03-Berechnung-unbekannter-Seiten|Anwendungen →]]
