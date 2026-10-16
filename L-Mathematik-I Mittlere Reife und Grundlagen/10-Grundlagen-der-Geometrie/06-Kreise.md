---
title: "Kreise"
created: 2026-10-13
modified: 2026-10-13
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

> [!note] Eigenschaften von π
> - π ist eine irrationale Zahl (unendlich viele Nachkommastellen, kein Muster)
> - Für Rechnungen: $\pi \approx 3{,}14$ oder $\pi \approx \frac{22}{7}$
> - Auf dem Taschenrechner: π-Taste verwenden

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
