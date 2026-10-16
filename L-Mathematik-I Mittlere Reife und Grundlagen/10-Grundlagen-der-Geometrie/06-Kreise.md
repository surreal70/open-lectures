---
title: "Kreise"
created: 2026-10-13
modified: 2025-01-20
chapter: "10"
section: "06"
status: "draft - review pending"
type: lecture
keywords:
  - Kreis
  - Radius
  - Durchmesser
  - Kreiszahl Pi
  - Sehne
---

# Kreise

> [!info] Lernziele
> - Die Bestandteile eines Kreises benennen können
> - Die Bedeutung der Kreiszahl π verstehen
> - Umfang und Flächeninhalt des Kreises berechnen
> - Kreisausschnitt und Kreisbogen berechnen

---

## Einführung

Der Kreis ist eine der grundlegendsten und ästhetisch ansprechendsten Formen der Geometrie. Seit Jahrtausenden fasziniert er Mathematiker, Künstler und Philosophen gleichermaßen. Im Alltag begegnen uns Kreise überall: Räder, Uhren, Münzen, Pizzen, Teller, CDs – die Liste ist endlos.

### Der Kreis in der Geschichte

Der Kreis galt in vielen Kulturen als Symbol der Vollkommenheit. Die alten Griechen sahen in ihm die perfekte Form – ohne Anfang und Ende, überall gleichmäßig. **Euklid** definierte den Kreis in seinen „Elementen" als die Menge aller Punkte, die von einem Mittelpunkt gleich weit entfernt sind.

> [!note] **Warum Räder rund sind**
> Ein Rad muss rund sein, weil nur so die Achse immer auf gleicher Höhe bleibt. Bei einem eckigen „Rad" würde der Wagen holpern. Der konstante Radius sorgt für gleichmäßiges Rollen.

---

## Definition und Bestandteile

Ein **Kreis** ist die Menge aller Punkte, die von einem festen Punkt (Mittelpunkt) den gleichen Abstand haben.

### Grundbegriffe

```
           ●───────● B
          ╱│      ╱
         ╱ │r    ╱d
        ╱  │    ╱
       ╱   ●M  ╱
      A●──────●
          Sehne
```

| Begriff | Beschreibung | Symbol |
|---|---|---|
| **Mittelpunkt** | Zentrum des Kreises | $M$ |
| **Radius** | Abstand vom Mittelpunkt zum Kreisrand | $r$ |
| **Durchmesser** | Längste Sehne, durch Mittelpunkt | $d = 2r$ |
| **Kreislinie** | Der Rand des Kreises | - |
| **Kreisfläche** | Das Innere des Kreises | - |

### Weitere Begriffe

| Begriff | Beschreibung |
|---|---|
| **Sehne** | Verbindungsstrecke zweier Kreispunkte |
| **Tangente** | Gerade, die den Kreis in genau einem Punkt berührt |
| **Sekante** | Gerade, die den Kreis in zwei Punkten schneidet |
| **Kreisbogen** | Teil der Kreislinie |
| **Kreissektor** | „Tortenstück" (Kreisausschnitt) |
| **Kreissegment** | Fläche zwischen Sehne und Kreisbogen |

## Die Kreiszahl π

Die **Kreiszahl π** (Pi) ist das Verhältnis von Umfang zu Durchmesser bei jedem Kreis:

$$\pi = \frac{U}{d} \approx 3{,}14159...$$

### Die faszinierende Geschichte von π

Die Kreiszahl π ist eine der berühmtesten Zahlen der Mathematik. Ihre Berechnung beschäftigt die Menschheit seit über 4000 Jahren:

- **Babylonier** (ca. 2000 v. Chr.): Nutzten $\pi \approx 3{,}125$
- **Ägypter** (ca. 1650 v. Chr.): Berechneten $\pi \approx 3{,}16$
- **Archimedes** (ca. 250 v. Chr.): Bestimmte $\pi$ durch Ein- und Umschreibung von 96-Ecken zwischen 3,1408 und 3,1429
- **Zu Chongzhi** (5. Jh.): Chinesischer Mathematiker, berechnete $\pi \approx \frac{355}{113}$ (korrekt auf 6 Nachkommastellen!)
- **Heute**: Computer haben Billionen von Nachkommastellen berechnet

> [!note] **Warum ist π so besonders?**
> π ist eine **irrationale Zahl** – sie hat unendlich viele Nachkommastellen ohne Muster. Mehr noch: π ist **transzendent**, d.h. sie kann nicht als Lösung einer Polynomgleichung mit ganzzahligen Koeffizienten auftreten. Deshalb ist es unmöglich, mit Zirkel und Lineal ein Quadrat mit gleichem Flächeninhalt wie ein gegebener Kreis zu konstruieren („Quadratur des Kreises").

> [!tip] **π-Merkregel**
> Die ersten Nachkommastellen kann man sich merken: 3,14159... → „Wie? Ich soll wissen Wurzeln" (3-1-4-1-5-9 Buchstaben pro Wort). Für Rechnungen reicht meist $\pi \approx 3{,}14$ oder der Taschenrechner.

> [!warning] **Häufiger Fehler**
> π ist **keine** Zahl wie $\frac{22}{7}$ – das ist nur eine Näherung! In Prüfungen solltest du das π-Symbol stehen lassen, bis der Taschenrechner verlangt wird.

## Umfang des Kreises

Der **Umfang** $U$ ist die Länge der Kreislinie:

$$U = \pi \cdot d = 2 \cdot \pi \cdot r$$

> [!example] Beispiel
> Ein Kreis hat den Radius $r = 5$ cm.
> 
> $$U = 2 \cdot \pi \cdot 5 = 10\pi \approx 31{,}42 \text{ cm}$$

## Flächeninhalt des Kreises

Der **Flächeninhalt** $A$ der Kreisfläche:

$$A = \pi \cdot r^2$$

> [!example] Beispiel
> Ein Kreis hat den Radius $r = 5$ cm.
> 
> $$A = \pi \cdot 5^2 = 25\pi \approx 78{,}54 \text{ cm}^2$$

## Formeln umstellen

### Radius aus Umfang

$$r = \frac{U}{2\pi}$$

### Radius aus Fläche

$$r = \sqrt{\frac{A}{\pi}}$$

> [!example] Beispiel
> Ein Kreis hat den Umfang $U = 62{,}8$ cm.
> 
> $$r = \frac{62{,}8}{2\pi} = \frac{62{,}8}{6{,}28} = 10 \text{ cm}$$

## Kreisausschnitt (Sektor)

Ein **Kreisausschnitt** ist ein „Tortenstück" mit Mittelpunktswinkel $\alpha$.

```
         ╱╲
        ╱α ╲
       ╱    ╲
      ╱──────╲
     Kreissektor
```

### Bogenlänge

$$b = \frac{\alpha}{360°} \cdot 2\pi r = \frac{\alpha \cdot \pi \cdot r}{180°}$$

### Flächeninhalt des Sektors

$$A_{Sektor} = \frac{\alpha}{360°} \cdot \pi r^2$$

> [!example] Beispiel
> Kreissektor mit $r = 6$ cm und $\alpha = 60°$
> 
> $$b = \frac{60°}{360°} \cdot 2\pi \cdot 6 = \frac{1}{6} \cdot 12\pi = 2\pi \approx 6{,}28 \text{ cm}$$
> 
> $$A = \frac{60°}{360°} \cdot \pi \cdot 36 = \frac{1}{6} \cdot 36\pi = 6\pi \approx 18{,}85 \text{ cm}^2$$

## Kreisring

Ein **Kreisring** entsteht zwischen zwei konzentrischen Kreisen.

```
    ╭───────────────╮
   ╱   ╭───────╮    ╲
  │   │         │    │
  │   │    M    │    │
  │   │         │    │
   ╲   ╰───────╯    ╱
    ╰───────────────╯
```

$$A_{Ring} = \pi \cdot R^2 - \pi \cdot r^2 = \pi(R^2 - r^2)$$

wobei $R$ der äußere und $r$ der innere Radius ist.

## Zusammenfassung

> [!abstract] Kernpunkte
> - Der Kreis ist definiert durch Mittelpunkt und Radius
> - Die Kreiszahl $\pi \approx 3{,}14159$ verbindet Umfang und Durchmesser
> - Umfang: $U = 2\pi r$
> - Fläche: $A = \pi r^2$
> - Kreisausschnitt: Anteil entsprechend dem Winkel ($\frac{\alpha}{360°}$)

## Zusammenhänge

Der Kreis verbindet viele mathematische Themen:

- → [[07-Umfangsberechnungen|Umfangsberechnungen]] – Kreisumfang als Sonderfall
- → [[08-Flaechenberechnungen|Flächenberechnungen]] – Kreisfläche und zusammengesetzte Figuren
- → [[05-Zylinder|Zylinder]] – Kreis als Grundfläche
- → [[08-Kugel|Kugel]] – Der Kreis in 3D erweitert
- → [[05-Einfuehrung-Trigonometrie|Trigonometrie]] – Sinus und Kosinus am Einheitskreis
- → [[02-Winkel-und-Winkelarten|Winkel]] – Der Vollwinkel 360° entspricht dem Kreisumfang

## Übungsaufgaben

1. Berechne Umfang und Fläche:
   - Kreis mit $r = 3$ cm
   - Kreis mit $d = 10$ cm

2. Bestimme den Radius:
   - Umfang $U = 25{,}12$ cm
   - Fläche $A = 50{,}24$ cm²

3. Ein Kreisausschnitt hat $r = 8$ cm und $\alpha = 45°$. Berechne Bogenlänge und Fläche.

4. Ein Kreisring hat die Radien $R = 5$ cm und $r = 3$ cm. Berechne den Flächeninhalt.

5. Ein Fahrradreifen hat einen Durchmesser von 70 cm. Wie weit fährt das Fahrrad bei einer Radumdrehung?

---

**Navigation**: [[05-Vierecke|← Vierecke]] | [[00-Geometrie-Index|Übersicht]] | [[07-Umfangsberechnungen|Umfangsberechnungen →]]
