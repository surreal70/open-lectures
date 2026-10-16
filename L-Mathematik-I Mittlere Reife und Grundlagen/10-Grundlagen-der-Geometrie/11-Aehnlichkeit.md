---
title: "Ähnlichkeit"
created: 2026-10-13
modified: 2026-10-13
chapter: "10"
section: "11"
status: "draft - review pending"
type: lecture
keywords:
  - Ähnlichkeit
  - Streckfaktor
  - Strahlensätze
  - Maßstab
  - proportional
---

# Ähnlichkeit

> [!info] Lernziele
> - Den Begriff Ähnlichkeit verstehen und von Kongruenz unterscheiden
> - Den Streckfaktor bestimmen und anwenden
> - Die Strahlensätze kennen und nutzen
> - Ähnlichkeit in praktischen Situationen erkennen

## Definition

Zwei Figuren sind **ähnlich**, wenn sie die **gleiche Form**, aber nicht notwendig die gleiche **Größe** haben.

$$\triangle ABC \sim \triangle DEF$$

> [!note] Unterschied zu Kongruenz
> - **Kongruent**: gleiche Form UND gleiche Größe
> - **Ähnlich**: gleiche Form, Größe kann unterschiedlich sein

## Eigenschaften ähnlicher Figuren

Bei ähnlichen Figuren gilt:
- Alle **entsprechenden Winkel** sind gleich
- Alle **entsprechenden Seiten** stehen im **gleichen Verhältnis**

$$\frac{a'}{a} = \frac{b'}{b} = \frac{c'}{c} = k$$

wobei $k$ der **Streckfaktor** (Ähnlichkeitsfaktor) ist.

## Der Streckfaktor k

Der **Streckfaktor** gibt an, um welchen Faktor die Seiten vergrößert oder verkleinert wurden.

| Streckfaktor | Wirkung |
|---|---|
| $k > 1$ | Vergrößerung |
| $k = 1$ | Kongruenz |
| $0 < k < 1$ | Verkleinerung |

> [!example] Beispiel
> Ein Dreieck mit Seiten $a = 3$, $b = 4$, $c = 5$ wird mit $k = 2$ gestreckt:
> 
> $a' = 3 \cdot 2 = 6$
> $b' = 4 \cdot 2 = 8$
> $c' = 5 \cdot 2 = 10$

### Streckfaktor berechnen

$$k = \frac{\text{Seite der neuen Figur}}{\text{entsprechende Seite der Originalfigur}}$$

## Ähnlichkeitssätze für Dreiecke

### Satz 1: WWW (Winkel-Winkel-Winkel)

Zwei Dreiecke sind ähnlich, wenn sie in **allen drei Winkeln** übereinstimmen.

> [!tip] Vereinfachung
> Es reicht, **zwei Winkel** zu vergleichen (der dritte ergibt sich aus der Winkelsumme 180°).

### Satz 2: SSS (Seiten proportional)

Zwei Dreiecke sind ähnlich, wenn alle **entsprechenden Seiten im gleichen Verhältnis** stehen.

$$\frac{a'}{a} = \frac{b'}{b} = \frac{c'}{c}$$

### Satz 3: SWS (Seite-Winkel-Seite)

Zwei Dreiecke sind ähnlich, wenn **zwei Seiten proportional** sind und der **eingeschlossene Winkel** gleich ist.

## Die Strahlensätze

Die **Strahlensätze** beschreiben Verhältnisse bei parallelen Geraden.

### Konfiguration

```
           Z
          ╱╲
         ╱  ╲
        ╱    ╲
    ───A──────B───    g
      ╱        ╲
     ╱          ╲
────A'──────────B'─── h (parallel zu g)
```

### Erster Strahlensatz

$$\frac{ZA}{ZA'} = \frac{ZB}{ZB'}$$

oder

$$\frac{ZA}{AA'} = \frac{ZB}{BB'}$$

### Zweiter Strahlensatz

$$\frac{AB}{A'B'} = \frac{ZA}{ZA'} = \frac{ZB}{ZB'}$$

Die parallelen Strecken verhalten sich wie die Strahlenabschnitte.

## Anwendungen

### Maßstab

Der **Maßstab** ist der Streckfaktor zwischen Abbildung und Original.

$$\text{Maßstab} = \frac{\text{Länge auf der Karte}}{\text{Länge in Wirklichkeit}}$$

> [!example] Beispiel
> Maßstab 1:100 bedeutet: 1 cm auf dem Plan entspricht 100 cm = 1 m in Wirklichkeit.
> 
> Auf dem Plan sind zwei Punkte 3 cm entfernt.
> → Tatsächliche Entfernung: $3 \cdot 100 = 300$ cm = 3 m

### Höhenbestimmung

Mit Ähnlichkeit kann man Höhen messen, die nicht direkt zugänglich sind.

> [!example] Beispiel: Baumhöhe
> Ein 2 m langer Stock wirft einen 1,5 m langen Schatten.
> Ein Baum wirft einen 15 m langen Schatten.
> Wie hoch ist der Baum?
> 
> $$\frac{h_{Baum}}{h_{Stock}} = \frac{Schatten_{Baum}}{Schatten_{Stock}}$$
> $$\frac{h}{2} = \frac{15}{1{,}5}$$
> $$h = 2 \cdot 10 = 20 \text{ m}$$

## Flächenverhältnis bei Ähnlichkeit

Wenn der Streckfaktor für Längen $k$ ist, dann ist der Faktor für Flächen $k^2$.

$$\frac{A'}{A} = k^2$$

> [!example] Beispiel
> Ein Quadrat wird mit $k = 3$ vergrößert.
> 
> Die neue Fläche ist $3^2 = 9$-mal so groß wie die ursprüngliche.

## Zusammenfassung

> [!abstract] Kernpunkte
> - Ähnliche Figuren haben gleiche Form, aber unterschiedliche Größe
> - Entsprechende Winkel sind gleich, Seiten stehen im gleichen Verhältnis
> - Der Streckfaktor $k$ gibt das Vergrößerungs-/Verkleinerungsverhältnis an
> - Die Strahlensätze liefern Verhältnisgleichungen bei Parallelenschnitt
> - Flächen ändern sich mit $k^2$

## Übungsaufgaben

1. Prüfe auf Ähnlichkeit:
   - Dreieck mit Seiten 3, 4, 5 und Dreieck mit Seiten 6, 8, 10
   - Dreieck mit Winkeln 30°, 60°, 90° und Dreieck mit Winkeln 30°, 60°, 90°

2. Ein Dreieck mit Seiten 5, 8, 10 wird mit $k = 1{,}5$ vergrößert. Berechne die neuen Seitenlängen.

3. Maßstab 1:500. Wie lang ist eine Strecke in Wirklichkeit, die auf dem Plan 4 cm misst?

4. Strahlensatz: $ZA = 6$ cm, $AA' = 9$ cm, $ZB = 8$ cm. Berechne $BB'$.

5. Ein Rechteck hat die Seitenlängen 4 cm und 6 cm. Es wird mit $k = 2{,}5$ vergrößert. Um wie viel hat sich die Fläche vergrößert?

---

**Navigation**: [[10-Kongruenz|← Kongruenz]] | [[00-Geometrie-Index|Übersicht]] | [[12-Geometrische-Konstruktionen|Konstruktionen →]]
