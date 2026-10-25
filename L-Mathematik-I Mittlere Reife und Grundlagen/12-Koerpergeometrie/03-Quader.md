---
title: Der Quader
chapter: "12"
section: "12.3"
type: lecture
created: 2026-10-13
modified: 2026-10-25
status: draft - review pending
tags:
  - mathematik/geometrie/koerper
  - quader
  - volumen
  - oberflaeche
---

# Der Quader

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Eigenschaften des Quaders beschreiben
> - Volumen eines Quaders berechnen
> - Oberfläche eines Quaders berechnen
> - Raumdiagonale bestimmen
> - Praktische Aufgaben mit Quadern lösen

## Definition und Eigenschaften

### Was ist ein Quader?

> [!note] Definition
> Ein **Quader** ist ein Körper mit sechs rechteckigen Flächen. Gegenüberliegende Flächen sind parallel und kongruent. Alle Winkel sind rechte Winkel (90°).

Der Quader ist die häufigste Körperform in unserer gebauten Umwelt: Räume, Möbel, Bücher, Smartphones, Verpackungen – fast alles hat Quaderform. Der Grund ist einfach: Quader lassen sich optimal stapeln ohne Lücken, und rechteckige Formen sind leicht herzustellen und zu vermessen.

### Eigenschaften

| Eigenschaft | Wert |
|-------------|------|
| Flächen | 6 (paarweise kongruent) |
| Kanten | 12 (je 4 gleich lang) |
| Ecken | 8 |
| Winkel | alle 90° |

### Bezeichnungen

Die drei verschiedenen Kantenlängen werden bezeichnet als:
- **a** = Länge
- **b** = Breite
- **c** = Höhe

> [!tip] Der Würfel als Spezialfall
> Ein [[02-Wuerfel|Würfel]] ist ein spezieller Quader mit $a = b = c$.

> [!info] **Quader im Bauwesen**
> Die meisten Räume sind quaderförmig. Das macht das Berechnen von Raumvolumen (für Heizung, Klimaanlage) und Wandflächen (für Tapeten, Farbe) besonders einfach. Architekten sprechen vom „Kubus", wenn sie einen würfelförmigen Baukörper meinen.

## Volumen des Quaders

### Formel

> [!note] Volumenformel
> $$V = a \cdot b \cdot c$$
> Volumen = Länge × Breite × Höhe

Alternative Schreibweise:
$$V = G \cdot h$$
wobei $G = a \cdot b$ die Grundfläche und $h = c$ die Höhe ist.

Diese Formel ist die Grundlage für alle Prismenvolumina: Grundfläche mal Höhe. Anschaulich kann man sich vorstellen, dass der Quader aus vielen dünnen Scheiben besteht, die übereinandergestapelt werden.

> [!tip] **Merkregel für Volumen**
> Das Volumen eines Quaders (und jedes Prismas) entspricht dem „Stapeln" der Grundfläche: Wie viele Schichten von 1 cm Höhe passen übereinander? Jede Schicht hat das Volumen der Grundfläche in cm³.

### Beispielrechnungen

> [!example] Beispiel 1: Volumen berechnen
> Ein Quader hat die Maße: Länge 8 cm, Breite 5 cm, Höhe 3 cm.
> 
> **Lösung:**
> $$V = 8 \cdot 5 \cdot 3 = 120 \text{ cm}^3$$

> [!example] Beispiel 2: Fehlende Maße berechnen
> Ein Quader hat das Volumen 240 cm³, die Länge 10 cm und die Breite 6 cm. Wie hoch ist er?
> 
> **Lösung:**
> $$V = a \cdot b \cdot c$$
> $$240 = 10 \cdot 6 \cdot c$$
> $$240 = 60c$$
> $$c = 4 \text{ cm}$$

## Oberfläche des Quaders

### Formel

> [!note] Oberflächenformel
> $$O = 2(ab + ac + bc)$$
> 
> Oder ausführlich:
> $$O = 2 \cdot \text{Grundfläche} + 2 \cdot \text{Seitenfläche}_1 + 2 \cdot \text{Seitenfläche}_2$$

### Flächenbezeichnungen

| Fläche | Anzahl | Größe |
|--------|--------|-------|
| Grundfläche/Deckfläche | 2 | $a \cdot b$ |
| Vorder-/Rückseite | 2 | $a \cdot c$ |
| Seitenflächen | 2 | $b \cdot c$ |

### Beispielrechnungen

> [!example] Beispiel 3: Oberfläche berechnen
> Ein Quader hat die Maße: $a = 6$ cm, $b = 4$ cm, $c = 2$ cm.
> 
> **Lösung:**
> $$O = 2(6 \cdot 4 + 6 \cdot 2 + 4 \cdot 2)$$
> $$O = 2(24 + 12 + 8)$$
> $$O = 2 \cdot 44 = 88 \text{ cm}^2$$

> [!example] Beispiel 4: Geschenkpapier
> Wie viel Geschenkpapier braucht man mindestens für einen Karton mit 30 cm × 20 cm × 10 cm?
> 
> **Lösung:**
> $$O = 2(30 \cdot 20 + 30 \cdot 10 + 20 \cdot 10)$$
> $$O = 2(600 + 300 + 200)$$
> $$O = 2 \cdot 1100 = 2200 \text{ cm}^2 = 0,22 \text{ m}^2$$

## Diagonalen des Quaders

### Flächendiagonalen

Auf jeder Seitenfläche:
- Grundfläche: $d_1 = \sqrt{a^2 + b^2}$
- Vorderseite: $d_2 = \sqrt{a^2 + c^2}$
- Seitenfläche: $d_3 = \sqrt{b^2 + c^2}$

Die Flächendiagonalen werden mit dem [[11-Satz-des-Pythagoras-und-Trigonometrie/02-Satz-des-Pythagoras|Satz des Pythagoras]] berechnet, da jede Seitenfläche ein Rechteck ist.

### Raumdiagonale

> [!note] Raumdiagonale
> $$d_R = \sqrt{a^2 + b^2 + c^2}$$

Die Raumdiagonale verbindet zwei gegenüberliegende Ecken des Quaders und ist die längste Strecke innerhalb des Körpers. Die Formel erhält man durch zweimalige Anwendung des Satzes des Pythagoras: Erst berechnet man die Flächendiagonale der Grundfläche, dann bildet diese mit der Höhe und der Raumdiagonale ein rechtwinkliges Dreieck.

> [!tip] **Praktische Bedeutung der Raumdiagonale**
> Die Raumdiagonale gibt an, wie lang ein Gegenstand maximal sein darf, um diagonal in einen Karton zu passen. Das ist wichtig beim Verpacken von langen, dünnen Gegenständen wie Schirmen, Angelruten oder Poster-Rollen.

> [!example] Beispiel 5: Raumdiagonale berechnen
> Ein Quader hat die Maße 4 cm × 3 cm × 2 cm.
> 
> **Lösung:**
> $$d_R = \sqrt{4^2 + 3^2 + 2^2} = \sqrt{16 + 9 + 4} = \sqrt{29} \approx 5,39 \text{ cm}$$

### Praktische Anwendung

> [!example] Beispiel 6: Stab im Karton
> Passt ein 50 cm langer Stab diagonal in einen Karton mit 40 cm × 30 cm × 20 cm?
> 
> **Lösung:**
> $$d_R = \sqrt{40^2 + 30^2 + 20^2} = \sqrt{1600 + 900 + 400} = \sqrt{2900} \approx 53,85 \text{ cm}$$
> 
> Ja, der Stab passt (53,85 cm > 50 cm).

## Praktische Anwendungen

### Verpackung und Transport

> [!example] Beispiel 7: Container
> Ein Frachtcontainer hat die Innenmaße 12 m × 2,4 m × 2,6 m.
> 
> a) Welches Volumen hat er?
> $$V = 12 \cdot 2{,}4 \cdot 2{,}6 = 74{,}88 \text{ m}^3$$
> 
> b) Wie viele Kartons (60 cm × 40 cm × 40 cm) passen hinein?
> - In der Länge: $12 \text{ m} \div 0{,}6 \text{ m} = 20$ Kartons
> - In der Breite: $2{,}4 \text{ m} \div 0{,}4 \text{ m} = 6$ Kartons
> - In der Höhe: $2{,}6 \text{ m} \div 0{,}4 \text{ m} = 6$ Kartons (1 passt nicht)
> - Gesamt: $20 \cdot 6 \cdot 6 = 720$ Kartons

### Aquarium und Schwimmbad

> [!example] Beispiel 8: Aquarium
> Ein Aquarium hat die Maße 80 cm × 40 cm × 50 cm.
> 
> a) Wie viel Liter fasst es maximal?
> $$V = 80 \cdot 40 \cdot 50 = 160.000 \text{ cm}^3 = 160 \text{ Liter}$$
> 
> b) Es wird bis 5 cm unter den Rand gefüllt. Wie viel Wasser ist drin?
> $$V = 80 \cdot 40 \cdot 45 = 144.000 \text{ cm}^3 = 144 \text{ Liter}$$

### Materialbedarf

> [!example] Beispiel 9: Holzkiste
> Eine offene Holzkiste (ohne Deckel) soll die Innenmaße 50 cm × 30 cm × 25 cm haben.
> 
> Wie viel Holzfläche wird benötigt?
> $$O_{\text{offen}} = ab + 2ac + 2bc$$
> $$O = 50 \cdot 30 + 2 \cdot 50 \cdot 25 + 2 \cdot 30 \cdot 25$$
> $$O = 1500 + 2500 + 1500 = 5500 \text{ cm}^2 = 0{,}55 \text{ m}^2$$

## Quadernetz

### Aufbau

Ein Quadernetz besteht aus 6 Rechtecken, die zusammengefaltet den Quader ergeben:

![[quadernetz.png]]
*<span class="fig-id">12-03-quadernetz</span>: Quadernetz aus sechs Rechtecken – je zwei Flächen mit den Maßen $a\times b$, $b\times c$ und $a\times c$.*

## Zusammenfassung

> [!abstract] Formeln auf einen Blick
> | Größe | Formel |
> |-------|--------|
> | Volumen | $V = a \cdot b \cdot c$ |
> | Oberfläche | $O = 2(ab + ac + bc)$ |
> | Raumdiagonale | $d_R = \sqrt{a^2 + b^2 + c^2}$ |

## Übungsaufgaben

> [!question] Aufgabe 1
> Ein Quader hat die Maße 12 cm × 8 cm × 5 cm. Berechnen Sie:
> a) das Volumen
> b) die Oberfläche
> c) die Raumdiagonale

> [!question] Aufgabe 2
> Ein Schwimmbecken ist 25 m lang, 12,5 m breit und enthält 750 m³ Wasser. Wie hoch steht das Wasser?

> [!question] Aufgabe 3
> Ein quaderförmiger Raum hat 4 m × 5 m Grundfläche und 2,5 m Höhe. Wie viel Farbe braucht man für die Wände (ohne Decke und Boden) bei 0,5 Liter pro m²?

> [!question] Aufgabe 4
> Ein USB-Stick (5 cm × 2 cm × 0,5 cm) wird in einen Karton (20 cm × 15 cm × 10 cm) gepackt. Wie viele passen maximal hinein?

---

**Navigation:** [[02-Wuerfel|← Würfel]] | [[04-Prisma|Prisma →]]
