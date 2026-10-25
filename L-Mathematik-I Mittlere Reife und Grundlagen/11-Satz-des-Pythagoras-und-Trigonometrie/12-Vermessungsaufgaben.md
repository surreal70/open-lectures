---
title: "Praktische Vermessungsaufgaben"
created: 2026-10-13
modified: 2026-10-25
chapter: "11"
section: "12"
status: "draft - review pending"
type: lecture
keywords:
  - Vermessung
  - Höhenmessung
  - Entfernungsmessung
  - Peilung
  - Navigation
---

# Praktische Vermessungsaufgaben

> [!info] Lernziele
> - Trigonometrie auf reale Vermessungsprobleme anwenden
> - Unzugängliche Höhen und Entfernungen berechnen
> - Mit Peil- und Sichtwinkeln arbeiten
> - Mehrstufige Berechnungen durchführen

## Überblick

Die Vermessung ist eine der ältesten Anwendungen der Trigonometrie. Schon die alten Ägypter nutzten trigonometrische Prinzipien, um die Pyramiden zu bauen und das Land nach den Nilüberschwemmungen neu zu vermessen. Heute ist die Vermessung ein Beruf, der von Landvermessern über Architekten bis zu Satellitennavigationsingenieuren reicht.

Das Besondere an Vermessungsaufgaben: Wir können oft nicht direkt messen, was uns interessiert. Die Höhe eines Turms, die Breite eines Flusses, die Entfernung zu einem Berggipfel – all das lässt sich nicht mit einem Maßband bestimmen. Aber mit Trigonometrie können wir diese „unzugänglichen" Größen berechnen!

> [!note] **Historischer Kontext**
> Der griechische Mathematiker Thales (ca. 600 v. Chr.) soll die Höhe der Pyramiden von Gizeh mit einem einfachen Trick gemessen haben: Er wartete, bis sein eigener Schatten genauso lang war wie er selbst (also bei 45° Sonnenstand), und maß dann den Schatten der Pyramide. Die Trigonometrie macht heute weit präzisere Messungen möglich – zu jeder Tageszeit!

## Höhenmessung durch Anvisieren

### Grundprinzip

Um die Höhe eines Objekts zu bestimmen, das man nicht direkt messen kann:

![[vermessung-anvisieren.png]]
*<span class="fig-id">11-12-vermessung-anvisieren</span>: Höhenmessung durch Anvisieren – zur berechneten Höhe $h_2 = d \cdot \tan(\alpha)$ wird die Augenhöhe $a$ addiert.*

Gesamthöhe = Augenhöhe + berechnete Höhe

$$h_{gesamt} = a + d \cdot \tan(\alpha)$$

> [!example] Beispiel
> Ein Baum wird aus 25 m Entfernung unter einem Winkel von 32° anvisiert. Die Augenhöhe beträgt 1,70 m.
> 
> $h = 1{,}70 + 25 \cdot \tan(32°) = 1{,}70 + 25 \cdot 0{,}625 = 1{,}70 + 15{,}6 = 17{,}3$ m

### Messung von zwei Standorten

Wenn der Abstand zum Objekt unbekannt ist, misst man von zwei Punkten:

![[vermessung-zwei-standorte.png]]
*<span class="fig-id">11-12-vermessung-zwei-standorte</span>: Messung von zwei Standorten B und A im Abstand $d$ mit den Höhenwinkeln $\beta$ und $\alpha$.*

Mit bekanntem Abstand $d$ zwischen den Standorten:

$$h = \frac{d \cdot \tan(\alpha) \cdot \tan(\beta)}{\tan(\beta) - \tan(\alpha)}$$

## Entfernungsmessung

### Über einen bekannten Höhenunterschied

Wenn die Höhe bekannt ist, kann die Entfernung berechnet werden:

$$d = \frac{h}{\tan(\alpha)}$$

> [!example] Beispiel
> Ein Leuchtturm ist 45 m hoch. Von einem Schiff aus wird seine Spitze unter einem Winkel von 12° gesehen.
> 
> $d = \frac{45}{\tan(12°)} = \frac{45}{0{,}213} \approx 211$ m

### Peiltriangulation

![[vermessung-peiltriangulation.png]]
*<span class="fig-id">11-12-vermessung-peiltriangulation</span>: Peiltriangulation – aus der Basislinie $b$ und den Peilwinkeln $\alpha$ und $\beta$ lässt sich die Entfernung zum Ziel bestimmen.*

Mit der Basislinie $b$ und den Peilwinkeln:

$$\text{Entfernung von A} = \frac{b \cdot \sin(\beta)}{\sin(180° - \alpha - \beta)}$$

## Typische Aufgabentypen

### Turmhöhe

> [!example] Beispiel
> Von einem Punkt P sieht man die Spitze eines Turms unter einem Höhenwinkel von 28°. Man geht 50 m auf den Turm zu und misst nun einen Winkel von 42°. Wie hoch ist der Turm?
> 
> ![[vermessung-turmhoehe.png]]
> *<span class="fig-id">11-12-vermessung-turmhoehe</span>: Turmhöhe aus zwei Messungen – von Q unter 28°, nach 50 m von P unter 42°.*
> 
> Es gilt:
> - $\tan(28°) = \frac{h}{x + 50}$
> - $\tan(42°) = \frac{h}{x}$
> 
> Aus der zweiten Gleichung: $h = x \cdot \tan(42°)$
> 
> Eingesetzt in die erste:
> $\tan(28°) = \frac{x \cdot \tan(42°)}{x + 50}$
> 
> $(x + 50) \cdot \tan(28°) = x \cdot \tan(42°)$
> 
> $x \cdot \tan(28°) + 50 \cdot \tan(28°) = x \cdot \tan(42°)$
> 
> $50 \cdot 0{,}532 = x \cdot (0{,}9 - 0{,}532)$
> 
> $x = \frac{26{,}6}{0{,}368} \approx 72{,}3$ m
> 
> $h = 72{,}3 \cdot \tan(42°) \approx 65$ m

### Bergbesteigung

> [!example] Beispiel
> Ein Wanderer will einen Gipfel erreichen, der 1200 m über seinem Standort liegt. Der Weg führt im Schnitt mit 25° Steigung bergauf. Wie lang ist der Weg?
> 
> $$s = \frac{h}{\sin(\alpha)} = \frac{1200}{\sin(25°)} = \frac{1200}{0{,}423} \approx 2837 \text{ m}$$

### Flugzeugbeobachtung

> [!example] Beispiel
> Ein Flugzeug fliegt in 8000 m Höhe. Es wird unter einem Winkel von 35° zur Horizontalen gesehen. Wie weit ist es (auf dem Boden gemessen) entfernt?
> 
> $$d = \frac{8000}{\tan(35°)} = \frac{8000}{0{,}7} \approx 11{,}43 \text{ km}$$

## Hilfsmittel in der Praxis

Moderne Vermessungstechnik nutzt hochpräzise Instrumente, aber die mathematischen Grundlagen bleiben dieselben:

- **Theodolit**: Präzisionsinstrument zur Winkelmessung (horizontal und vertikal), erreicht Genauigkeiten von Winkelsekunden
- **Neigungsmesser**: Für Steigungen und einfache Winkel, oft als Smartphone-App verfügbar
- **Entfernungsmesser**: Laserbasiert für direkte Messungen bis zu mehreren hundert Metern
- **Geodreieck/Kompass**: Für einfache Peilungen und Kartenarbeit
- **GPS**: Nutzt Triangulation zu mindestens 4 Satelliten, um Positionen weltweit zu bestimmen

> [!tip] **Moderne Anwendung**
> Die GPS-Navigation in deinem Smartphone basiert auf denselben trigonometrischen Prinzipien! Durch die Laufzeitmessung von Signalen mehrerer Satelliten wird deine Position per Triangulation berechnet.

## Zusammenfassung

> [!abstract] Kernpunkte
> - Unzugängliche Höhen mit Trigonometrie berechenbar
> - Kombination aus bekannter Strecke und gemessenem Winkel
> - Bei unbekannter Entfernung: zwei Messungen von verschiedenen Punkten
> - Augenhöhe bei Höhenmessungen berücksichtigen
> - Ergebnisse auf Plausibilität prüfen

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[08-Tangens|Der Tangens]] – Grundlage der meisten Vermessungsberechnungen
- → [[10-Berechnung-Winkel|Winkelberechnung]] – Arkusfunktionen anwenden
- → [[11-Steigungen-Neigungswinkel|Steigungen und Neigungswinkel]] – Verwandte Anwendungen
- → [[02-Satz-des-Pythagoras|Satz des Pythagoras]] – Oft kombiniert mit Trigonometrie

## Übungsaufgaben

1. Ein 80 m hoher Fernsehturm wird unter einem Winkel von 15° gesehen. Wie weit ist der Beobachter entfernt?

2. Von zwei Punkten A und B im Abstand von 100 m wird ein Kirchturm angepeilt: Von A unter 38°, von B unter 52°. Berechne die Höhe des Turms.

3. Ein Hubschrauber fliegt in konstanter Höhe. Von einem Beobachtungspunkt wird er zunächst unter 25° gesehen. Nach 30 Sekunden beträgt der Winkel 48°. Der Hubschrauber ist dann genau über dem Beobachter geflogen. In welcher Höhe fliegt er?

4. Von einem Aussichtspunkt (100 m über dem See) sieht man ein Boot unter einem Tiefenwinkel von 8°. Wie weit ist das Boot entfernt?

5. Eine Seilbahn überwindet einen Höhenunterschied von 800 m bei einer Bahnlänge von 2200 m. Wie groß ist der Neigungswinkel?

---

**Navigation**: [[11-Steigungen-Neigungswinkel|← Steigungen]] | [[00-Pythagoras-Trigonometrie-Index|Übersicht]] | [[../12-Koerpergeometrie/00-Koerpergeometrie-Index|Körpergeometrie →]]
