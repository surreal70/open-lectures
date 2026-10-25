---
title: "Anwendungen des Satzes des Pythagoras"
created: 2026-10-13
modified: 2026-10-25
chapter: "11"
section: "04"
status: "draft - review pending"
type: lecture
keywords:
  - Anwendung
  - Raumdiagonale
  - Flächen
  - Koordinaten
---

# Anwendungen des Satzes des Pythagoras

> [!info] Lernziele
> - Den Satz des Pythagoras auf praktische Probleme anwenden
> - Räumliche Probleme auf ebene Dreiecke zurückführen
> - Die Raumdiagonale berechnen können
> - Sachaufgaben systematisch lösen

## Überblick

Der wahre Wert des Satzes des Pythagoras zeigt sich in seinen vielfältigen Anwendungen. Von der Berechnung von Diagonalen über Höhenbestimmungen bis hin zur Entfernungsmessung – überall, wo rechtwinklige Dreiecke verborgen sind, hilft uns Pythagoras weiter. In diesem Abschnitt lernst du, solche Dreiecke in praktischen Situationen zu erkennen und zu nutzen.

## Diagonalen

Diagonalen in Rechtecken und Quadern sind klassische Anwendungen des Satzes des Pythagoras. Sie begegnen uns täglich – bei Bildschirmen, Türen, Regalen und vielem mehr.

### Diagonale im Rechteck

$$d = \sqrt{l^2 + b^2}$$

> [!tip] **Alltagsanwendung**
> Passt ein langer Gegenstand diagonal in einen Raum? Passt ein Bild durch eine Tür? Diese Fragen beantwortet die Diagonalenformel!

### Diagonale im Quadrat

$$d = a\sqrt{2}$$

Bei einem Quadrat mit Seitenlänge $a$ ist die Diagonale immer $a \cdot \sqrt{2} \approx 1{,}414 \cdot a$. Das bedeutet: Die Diagonale ist etwa 41% länger als die Seite.

### Raumdiagonale im Quader

Die Raumdiagonale verbindet zwei gegenüberliegende Ecken eines Quaders und durchquert den gesamten Körper. Die Berechnung erfolgt durch zweimalige Anwendung des Pythagoras – oder mit der eleganten Formel:

![[quader-raumdiagonale.png]]
*<span class="fig-id">11-04-quader-raumdiagonale</span>: Die Raumdiagonale $d$ des Quaders. Die gestrichelte Flächendiagonale der Grundfläche dient als Zwischenschritt der Herleitung.*

$$d = \sqrt{a^2 + b^2 + c^2}$$

> [!note] **Herleitung**
> Die Formel entsteht durch zweimalige Anwendung des Pythagoras:
> 1. Erst die Flächendiagonale der Grundfläche: $d_1 = \sqrt{a^2 + b^2}$
> 2. Dann die Raumdiagonale mit $d_1$ und der Höhe $c$: $d = \sqrt{d_1^2 + c^2} = \sqrt{a^2 + b^2 + c^2}$

> [!example] Beispiel
> Quader mit $a = 3$ cm, $b = 4$ cm, $c = 12$ cm
> 
> $d = \sqrt{9 + 16 + 144} = \sqrt{169} = 13$ cm
> 
> *Interessant: (3, 4, 12, 13) bildet ein „räumliches pythagoreisches Quadrupel"!*

### Raumdiagonale im Würfel

$$d = a\sqrt{3}$$

Ein Würfel mit Kantenlänge $a$ hat eine Raumdiagonale von $a \cdot \sqrt{3} \approx 1{,}732 \cdot a$. Die Raumdiagonale ist also etwa 73% länger als die Kante.

> [!tip] **Praktische Anwendung: Möbeltransport**
> Willst du wissen, ob ein langer Gegenstand durch ein Zimmer passt? Die Raumdiagonale gibt die längste gerade Strecke im Raum an.

## Höhenberechnung im gleichschenkligen Dreieck

Im gleichschenkligen Dreieck halbiert die Höhe die Basis und erzeugt zwei kongruente rechtwinklige Dreiecke. Diese Eigenschaft macht die Höhenberechnung mit Pythagoras besonders elegant.

![[gleichschenklig-hoehe.png]]
*<span class="fig-id">11-04-gleichschenklig-hoehe</span>: Die Höhe $h$ halbiert die Basis im Punkt $M$ und bildet zwei rechtwinklige Dreiecke mit Hypotenuse $a$ und halber Basis $\tfrac{c}{2}$.*

Die Höhe $h$ im gleichschenkligen Dreieck:

$$h = \sqrt{a^2 - \left(\frac{c}{2}\right)^2}$$

> [!tip] **Warum funktioniert das?**
> Die Höhe teilt das gleichschenklige Dreieck exakt in der Mitte. Es entstehen zwei rechtwinklige Dreiecke mit:
> - Hypotenuse = Schenkel $a$
> - Eine Kathete = Höhe $h$
> - Andere Kathete = halbe Basis $\frac{c}{2}$

> [!example] Beispiel
> Gleichschenkliges Dreieck mit $a = 5$ cm, $c = 6$ cm
> 
> $h = \sqrt{25 - 9} = \sqrt{16} = 4$ cm
> 
> *Prüfung: Die Fläche beträgt $\frac{1}{2} \cdot 6 \cdot 4 = 12$ cm²*

## Höhe im gleichseitigen Dreieck

Im gleichseitigen Dreieck mit Seitenlänge $a$:

$$h = \frac{a\sqrt{3}}{2}$$

Diese Formel ergibt sich direkt aus der allgemeinen Höhenformel, da im gleichseitigen Dreieck alle Seiten gleich lang sind ($a = c$).

> [!note] **Wichtige Verhältnisse**
> Im gleichseitigen Dreieck mit Seitenlänge $a$ gilt:
> - Höhe: $h = \frac{a\sqrt{3}}{2} \approx 0{,}866 \cdot a$
> - Fläche: $A = \frac{a^2\sqrt{3}}{4}$
> - Der Schwerpunkt teilt die Höhe im Verhältnis 2:1

## Praktische Anwendungen

### Baugerüste und Leitern

> [!example] Beispiel
> Eine Leiter soll bis zu einem 4 m hohen Fenster reichen. Der Neigungswinkel erfordert einen Fußabstand von 1,5 m. Wie lang muss die Leiter sein?
> 
> $$l = \sqrt{4^2 + 1{,}5^2} = \sqrt{16 + 2{,}25} = \sqrt{18{,}25} \approx 4{,}27 \text{ m}$$

> [!warning] **Sicherheit bei Leitern**
> Die Berufsgenossenschaft empfiehlt: Der Fußabstand sollte etwa ein Viertel der Leiterlänge betragen. Das entspricht einem Anstellwinkel von etwa 75°. Bei zu steilem Winkel kann die Leiter nach hinten kippen!

### Dachkonstruktionen

> [!example] Beispiel
> Ein Satteldach hat eine Spannweite von 10 m und eine Firsthöhe von 3 m. Wie lang ist eine Dachseite?
> 
> Halbe Spannweite: $5$ m
> 
> $$d = \sqrt{5^2 + 3^2} = \sqrt{25 + 9} = \sqrt{34} \approx 5{,}83 \text{ m}$$

### Abstände im Koordinatensystem

Abstand zweier Punkte $P_1(x_1, y_1)$ und $P_2(x_2, y_2)$:

$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

Im dreidimensionalen Raum mit $P_1(x_1, y_1, z_1)$ und $P_2(x_2, y_2, z_2)$:

$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}$$

### Flächenberechnung mit Pythagoras

Wenn die Höhe nicht gegeben ist, kann sie oft mit Pythagoras berechnet werden.

> [!example] Beispiel: Fläche eines gleichschenkligen Dreiecks
> Seiten: $a = b = 10$ cm, $c = 12$ cm
> 
> **Höhe berechnen**:
> $h = \sqrt{10^2 - 6^2} = \sqrt{100 - 36} = \sqrt{64} = 8$ cm
> 
> **Fläche**:
> $A = \frac{1}{2} \cdot 12 \cdot 8 = 48$ cm²

## Mehrfache Anwendung

Manchmal muss der Satz mehrfach angewendet werden.

> [!example] Beispiel: Höhe einer Pyramide
> Eine quadratische Pyramide hat eine Grundkante von 6 cm und eine Seitenkante von 5 cm.
> 
> **Schritt 1**: Halbe Diagonale der Grundfläche
> $d_{halb} = \frac{6\sqrt{2}}{2} = 3\sqrt{2} \approx 4{,}24$ cm
> 
> **Schritt 2**: Höhe berechnen
> $h = \sqrt{5^2 - (3\sqrt{2})^2} = \sqrt{25 - 18} = \sqrt{7} \approx 2{,}65$ cm

## Zusammenfassung

> [!abstract] Kernpunkte
> - Rechteckdiagonale: $d = \sqrt{l^2 + b^2}$
> - Raumdiagonale Quader: $d = \sqrt{a^2 + b^2 + c^2}$
> - Höhe im gleichschenkligen Dreieck durch Pythagoras berechenbar
> - Koordinatenabstand: Differenzen quadrieren und Wurzel ziehen
> - Bei komplexen Aufgaben: Problem in Teilprobleme zerlegen

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[02-Satz-des-Pythagoras|Satz des Pythagoras]] – Die theoretische Grundlage
- → [[03-Berechnung-unbekannter-Seiten|Berechnung unbekannter Seiten]] – Grundlegende Berechnungen
- → [[../12-Koerpergeometrie/03-Quader|Quader]] – Raumdiagonalen bei Körpern
- → [[../09-Funktionen-und-Koordinatensysteme/02-Punkte-und-Koordinaten|Koordinatensystem]] – Abstandsberechnungen

## Übungsaufgaben

1. Berechne die Raumdiagonale eines Quaders mit den Maßen 8 cm × 6 cm × 24 cm.

2. Ein gleichseitiges Dreieck hat die Seitenlänge 12 cm. Berechne die Höhe.

3. Wie weit sind die Punkte $A(3, 1)$ und $B(7, 4)$ voneinander entfernt?

4. Ein Fernseher hat die Maße 80 cm × 60 cm. Wie groß ist die Bildschirmdiagonale?

5. Ein Schrank (80 × 50 × 200 cm) soll durch eine Tür (90 × 210 cm) getragen werden. Passt der Schrank diagonal durch die Tür?

---

**Navigation**: [[03-Berechnung-unbekannter-Seiten|← Berechnung]] | [[00-Pythagoras-Trigonometrie-Index|Übersicht]] | [[05-Einfuehrung-Trigonometrie|Trigonometrie →]]
