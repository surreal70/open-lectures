---
title: "Punkte und Koordinaten"
created: 2026-10-13
modified: 2026-10-16
chapter: "09"
section: "02"
status: "draft - review pending"
type: lecture
keywords:
  - Koordinaten
  - Punkte
  - Abszisse
  - Ordinate
  - Koordinatenpaar
---

# Punkte und Koordinaten

> [!info] Lernziele
> - Die Schreibweise von Koordinaten verstehen und anwenden
> - Punkte im Koordinatensystem ablesen und einzeichnen
> - Die Begriffe Abszisse und Ordinate korrekt verwenden
> - Den Abstand zwischen Punkten berechnen

## Koordinaten eines Punktes

Jeder Punkt in der Ebene wird durch ein **geordnetes Zahlenpaar** beschrieben:

$$P(x | y) \quad \text{oder} \quad P(x, y)$$

Die Idee ist einfach: Um einen Punkt eindeutig zu bestimmen, braucht man zwei Informationen – wie weit nach rechts/links und wie weit nach oben/unten. Dies ist vergleichbar mit einer Adresse, die aus Straße und Hausnummer besteht.

| Komponente | Name | Bedeutung |
|---|---|---|
| $x$ | **Abszisse** (x-Koordinate) | Horizontaler Abstand vom Ursprung |
| $y$ | **Ordinate** (y-Koordinate) | Vertikaler Abstand vom Ursprung |

> [!info] **Herkunft der Begriffe**
> Das Wort „Abszisse" kommt vom lateinischen *abscindere* (abschneiden) – man „schneidet" sozusagen den Abstand auf der x-Achse ab. „Ordinate" stammt von *ordinare* (ordnen) – die vertikale Koordinate ordnet den Punkt in seiner Höhe ein.

> [!warning] Wichtig: Reihenfolge beachten!
> Die x-Koordinate steht **immer zuerst**, dann die y-Koordinate.
> $P(3, 5) \neq P(5, 3)$
>
> **Eselsbrücke**: Im Alphabet kommt „x" vor „y" – also auch in den Koordinaten!

## Punkte einzeichnen

### Vorgehensweise

1. Auf der **x-Achse** den x-Wert finden
2. Von dort **senkrecht** nach oben/unten zur y-Koordinate gehen
3. Punkt markieren und beschriften

### Beispiel

Punkt $P(3, 2)$ einzeichnen:

![[punkt-einzeichnen.png]]
*<span class="fig-id">01-09-02-punkt-einzeichnen</span>: Den Punkt P(3, 2) einzeichnen – zuerst auf der x-Achse zu 3 gehen, dann senkrecht nach oben zu y = 2; die Hilfslinien treffen sich im Punkt P.*

1. Auf der x-Achse zu $x = 3$ gehen
2. Von dort senkrecht nach oben zu $y = 2$
3. Punkt markieren: $P$

## Koordinaten ablesen

### Vorgehensweise

1. Vom Punkt eine **senkrechte Linie** zur x-Achse ziehen → x-Koordinate
2. Vom Punkt eine **waagerechte Linie** zur y-Achse ziehen → y-Koordinate

### Beispiel

![[koordinaten-ablesen.png]]
*<span class="fig-id">01-09-02-koordinaten-ablesen</span>: Koordinaten ablesen – vom Punkt Q senkrecht zur x-Achse (x = 6) und waagerecht zur y-Achse (y = 4) führen zu den Koordinaten Q(6, 4).*

Punkt $Q$: $x = 6$, $y = 4$ → $Q(6, 4)$

## Negative Koordinaten

Punkte können auch negative Koordinaten haben:

![[negative-koordinaten.png]]
*<span class="fig-id">01-09-02-negative-koordinaten</span>: Punkte mit negativen Koordinaten – A(−3, 1) liegt im zweiten Quadranten (links oben), B(2, −2) im vierten Quadranten (rechts unten).*

- $A(-3, 1)$: 3 Einheiten nach links, 1 nach oben
- $B(2, -2)$: 2 Einheiten nach rechts, 2 nach unten

## Spezielle Punkte

### Punkte auf den Achsen

| Lage | Bedingung | Beispiele |
|---|---|---|
| Auf der x-Achse | $y = 0$ | $(5, 0)$, $(-3, 0)$ |
| Auf der y-Achse | $x = 0$ | $(0, 4)$, $(0, -2)$ |
| Im Ursprung | $x = 0$ und $y = 0$ | $(0, 0)$ |

### Punkte mit gleichen Koordinaten

| Beziehung | Eigenschaft |
|---|---|
| $P(a, a)$ | Liegt auf der 1. Winkelhalbierenden |
| $P(a, -a)$ | Liegt auf der 2. Winkelhalbierenden |

## Abstände zwischen Punkten

### Horizontaler Abstand (gleiche y-Koordinate)

Für $P_1(x_1, y)$ und $P_2(x_2, y)$:

$$d = |x_2 - x_1|$$

> [!example] Beispiel
> $A(2, 3)$ und $B(7, 3)$
> 
> $d = |7 - 2| = 5$

### Vertikaler Abstand (gleiche x-Koordinate)

Für $P_1(x, y_1)$ und $P_2(x, y_2)$:

$$d = |y_2 - y_1|$$

### Allgemeiner Abstand (Satz des Pythagoras)

Für beliebige Punkte $P_1(x_1, y_1)$ und $P_2(x_2, y_2)$:

$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

Diese Formel ist eine direkte Anwendung des [[../11-Satz-des-Pythagoras-und-Trigonometrie/02-Satz-des-Pythagoras|Satzes des Pythagoras]]. Man kann sich die Strecke zwischen zwei Punkten als Hypotenuse eines rechtwinkligen Dreiecks vorstellen, dessen Katheten parallel zu den Achsen verlaufen.

> [!info] **Warum funktioniert das?**
> Die horizontale Kathete hat die Länge $|x_2 - x_1|$, die vertikale Kathete $|y_2 - y_1|$. Nach Pythagoras gilt: Hypotenuse² = Kathete₁² + Kathete₂². Da wir quadrieren, sind die Betragsstriche nicht nötig – negative Werte werden automatisch positiv.

> [!example] Beispiel
> $A(1, 2)$ und $B(4, 6)$
> 
> $$d = \sqrt{(4-1)^2 + (6-2)^2} = \sqrt{9 + 16} = \sqrt{25} = 5$$

> [!tip] **Praxis-Tipp**
> Diese Formel ist auch die Grundlage für GPS-Navigation: Dein Smartphone berechnet Entfernungen nach demselben Prinzip (allerdings auf einer Kugeloberfläche, was die Rechnung etwas komplizierter macht).

## Mittelpunkt einer Strecke

Der **Mittelpunkt** $M$ der Strecke $\overline{P_1P_2}$ hat die Koordinaten:

$$M\left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$$

Die Formel ist intuitiv: Der Mittelpunkt liegt genau „in der Mitte" – also beim Durchschnitt der x-Koordinaten und beim Durchschnitt der y-Koordinaten.

> [!example] Beispiel
> $P_1(2, 4)$ und $P_2(6, 8)$
> 
> $$M\left(\frac{2+6}{2}, \frac{4+8}{2}\right) = M(4, 6)$$

> [!tip] **Anschaulich verstehen**
> Stell dir vor, du hast zwei Freunde, einer steht bei $x = 2$, der andere bei $x = 6$. Wo müsstet ihr euch treffen, damit beide den gleichen Weg haben? Genau in der Mitte bei $x = 4$. Das Gleiche gilt für die y-Koordinate.

## Zusammenfassung

> [!abstract] Kernpunkte
> - Ein Punkt wird durch das Koordinatenpaar $(x, y)$ beschrieben
> - Die x-Koordinate (Abszisse) steht immer zuerst
> - Punkte auf der x-Achse haben $y = 0$, auf der y-Achse $x = 0$
> - Der Abstand zweier Punkte wird mit dem Satz des Pythagoras berechnet
> - Der Mittelpunkt hat den Durchschnitt beider Koordinaten

## Zusammenhänge

Dieses Thema ist eng verbunden mit:

- → [[01-Kartesisches-Koordinatensystem|Kartesisches Koordinatensystem]] – Die Grundlage für das Arbeiten mit Punkten
- → [[03-Einfuehrung-Funktionen|Funktionen]] – Punkte als Teil von Funktionsgraphen
- → [[../10-Grundlagen-der-Geometrie/04-Dreiecke|Dreiecke]] – Konstruktion von Dreiecken mit gegebenen Eckpunkten
- → [[../11-Satz-des-Pythagoras-und-Trigonometrie/02-Satz-des-Pythagoras|Satz des Pythagoras]] – Herleitung der Abstandsformel

## Übungsaufgaben

1. Zeichne die folgenden Punkte in ein Koordinatensystem ein:
   - $A(3, 4)$, $B(-2, 5)$, $C(-4, -3)$, $D(5, -1)$, $E(0, 3)$, $F(-3, 0)$

2. Lies die Koordinaten der Punkte ab (eigenes Koordinatensystem zeichnen).

3. Berechne den Abstand zwischen:
   - $A(1, 1)$ und $B(4, 5)$
   - $C(-2, 3)$ und $D(4, 3)$
   - $E(0, 0)$ und $F(6, 8)$

4. Bestimme den Mittelpunkt der Strecke:
   - $\overline{AB}$ mit $A(2, 6)$ und $B(8, 2)$
   - $\overline{CD}$ mit $C(-4, 3)$ und $D(2, -5)$

5. Ein Quadrat hat die Eckpunkte $A(1, 1)$, $B(4, 1)$, $C(4, 4)$ und $D(1, 4)$. Berechne den Umfang und bestimme den Mittelpunkt.

---

**Navigation**: [[01-Kartesisches-Koordinatensystem|← Koordinatensystem]] | [[00-Funktionen-Index|Übersicht]] | [[03-Einfuehrung-Funktionen|Einführung Funktionen →]]
