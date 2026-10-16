---
title: "Geometrische Konstruktionen"
created: 2026-10-13
modified: 2025-01-20
chapter: "10"
section: "12"
status: "draft - review pending"
type: lecture
keywords:
  - Konstruktion
  - Zirkel
  - Lineal
  - Mittelsenkrechte
  - Winkelhalbierende
---

# Geometrische Konstruktionen

> [!info] Lernziele
> - Grundkonstruktionen mit Zirkel und Lineal durchführen
> - Konstruktionsschritte beschreiben können
> - Mittelsenkrechte und Winkelhalbierende konstruieren
> - Dreiecke nach verschiedenen Vorgaben konstruieren

---

## Einführung

Geometrische Konstruktionen mit Zirkel und Lineal haben eine über 2500 Jahre alte Tradition. Die alten Griechen entwickelten diese Kunst zu hoher Perfektion – und stellten dabei Fragen, die erst Jahrhunderte später beantwortet werden konnten.

### Historischer Hintergrund

> [!note] **Euklid und die Konstruktionswerkzeuge**
> In Euklids „Elementen" (ca. 300 v. Chr.) sind nur zwei Werkzeuge erlaubt: ein **Zirkel** zum Zeichnen von Kreisen und ein **Lineal ohne Skala** zum Zeichnen von Geraden. Diese Einschränkung führte zu berühmten „unlösbaren" Problemen:
> 
> - **Quadratur des Kreises**: Kann man ein Quadrat mit gleichem Flächeninhalt wie ein Kreis konstruieren? Nein – erst 1882 bewies Ferdinand von Lindemann, dass dies unmöglich ist, weil π transzendent ist.
> - **Würfelverdopplung**: Kann man einen Würfel konstruieren, der das doppelte Volumen hat? Nein – dies führt auf $\sqrt[3]{2}$, das nicht konstruierbar ist.
> - **Winkeldreiteilung**: Kann man jeden Winkel in drei gleiche Teile teilen? Nein – im Allgemeinen nicht.

Diese „Unmöglichkeitsbeweise" gehören zu den tiefsten Erkenntnissen der Mathematik.

---

## Werkzeuge und Regeln

### Erlaubte Werkzeuge

Bei klassischen Konstruktionen sind nur erlaubt:
- **Lineal** (ohne Maßeinteilung) zum Zeichnen von Geraden
- **Zirkel** zum Zeichnen von Kreisen und Abtragen von Strecken

> [!tip] **Warum diese Einschränkung?**
> Die Griechen wollten Konstruktionen, die **exakt** sind – unabhängig von Messfehlern. Ein Lineal mit Skala kann verrutschen, aber der Schnittpunkt zweier Kreise ist eindeutig definiert.

In der Praxis (und im Unterricht) werden oft auch Geodreieck, Winkelmesser und markiertes Lineal verwendet – aber die „klassischen" Konstruktionen bleiben ein faszinierendes Gebiet.

## Grundkonstruktionen

### 1. Strecke abtragen

**Aufgabe**: Eine Strecke $\overline{AB}$ auf eine Gerade $g$ übertragen.

**Konstruktion**:
1. Zirkel auf Länge $\overline{AB}$ einstellen
2. Zirkel auf Punkt $P$ der Geraden $g$ setzen
3. Kreisbogen schlagen
4. Schnittpunkt mit $g$ markieren

### 2. Mittelsenkrechte einer Strecke

**Aufgabe**: Die Mittelsenkrechte der Strecke $\overline{AB}$ konstruieren.

**Konstruktion**:
1. Zirkel auf mehr als halbe Streckenlänge einstellen
2. Kreisbogen um $A$ schlagen
3. Kreisbogen um $B$ mit gleicher Öffnung schlagen
4. Beide Schnittpunkte verbinden

```
         ●
        ╱│╲
       ╱ │ ╲
      ╱  │  ╲
●────────●────────●
A    M   │        B
     ╲   │   ╱
      ╲  │  ╱
       ╲ │ ╱
         ●
```

> [!tip] Anwendung
> Jeder Punkt auf der Mittelsenkrechten hat den gleichen Abstand zu $A$ und $B$.

### 3. Lot auf eine Gerade

**Aufgabe**: Das Lot von einem Punkt $P$ auf eine Gerade $g$ fällen.

**Konstruktion**:
1. Kreisbogen um $P$, der $g$ in zwei Punkten $A$ und $B$ schneidet
2. Mittelsenkrechte von $\overline{AB}$ konstruieren
3. Diese geht durch $P$ und steht senkrecht auf $g$

### 4. Winkelhalbierende

**Aufgabe**: Einen Winkel halbieren.

**Konstruktion**:
1. Kreisbogen um den Scheitelpunkt $S$
2. Schnittpunkte $A$ und $B$ mit den Schenkeln markieren
3. Kreisbögen um $A$ und $B$ mit gleicher Öffnung
4. Schnittpunkt $C$ der Kreisbögen
5. Strahl von $S$ durch $C$ ist die Winkelhalbierende

```
              C
             ╱
            ╱
    ●──────●──────●
   A      ╱S      B
         ╱
        ╱
```

### 5. Parallele durch einen Punkt

**Aufgabe**: Eine Parallele zu einer Geraden $g$ durch einen Punkt $P$ konstruieren.

**Konstruktion** (mit Wechselwinkeln):
1. Beliebige Gerade durch $P$, die $g$ in $Q$ schneidet
2. Winkel bei $Q$ messen (Kreisbogen)
3. Gleichen Winkel bei $P$ abtragen (Wechselwinkel)

## Dreieckskonstruktionen

### SSS – Drei Seiten gegeben

**Gegeben**: $a = 5$ cm, $b = 4$ cm, $c = 6$ cm

1. Seite $c$ als Strecke $\overline{AB}$ zeichnen
2. Kreis um $A$ mit Radius $b$
3. Kreis um $B$ mit Radius $a$
4. Schnittpunkt = $C$
5. Dreieck $ABC$ verbinden

### SWS – Zwei Seiten und eingeschlossener Winkel

**Gegeben**: $b = 5$ cm, $c = 7$ cm, $\alpha = 40°$

1. Seite $c$ als Strecke $\overline{AB}$ zeichnen
2. Winkel $\alpha$ bei $A$ antragen
3. Auf dem freien Schenkel Länge $b$ abtragen → Punkt $C$
4. $B$ und $C$ verbinden

### WSW – Seite und anliegende Winkel

**Gegeben**: $c = 8$ cm, $\alpha = 50°$, $\beta = 60°$

1. Seite $c$ als Strecke $\overline{AB}$ zeichnen
2. Winkel $\alpha$ bei $A$ antragen
3. Winkel $\beta$ bei $B$ antragen
4. Schnittpunkt der Schenkel = $C$

### Rechtwinkliges Dreieck über Thaleskreis

**Gegeben**: Hypotenuse $c$ und ein Winkel $\alpha$

1. Hypotenuse $c$ als Durchmesser $\overline{AB}$ zeichnen
2. Thaleskreis (Halbkreis über $AB$)
3. Winkel $\alpha$ bei $A$ antragen
4. Schnittpunkt mit Thaleskreis = $C$

> [!note] Satz des Thales
> Jeder Punkt auf dem Halbkreis über dem Durchmesser bildet mit den Endpunkten ein rechtwinkliges Dreieck.

## Konstruktionsbeschreibung

Eine vollständige Konstruktionsbeschreibung enthält:
1. Gegebene Größen
2. Nummerierte Schritte
3. Begründung (welcher Satz wird genutzt)

## Zusammenfassung

> [!abstract] Kernpunkte
> - Klassische Konstruktionen nur mit Zirkel und Lineal
> - Mittelsenkrechte: beide Endpunkte als Kreismittelpunkte
> - Winkelhalbierende: Kreisbögen mit gleichem Radius
> - Dreieckskonstruktionen nach SSS, SWS, WSW
> - Der Thaleskreis erzeugt rechte Winkel

## Zusammenhänge

Konstruktionen verbinden viele geometrische Konzepte:

- → [[10-Kongruenz|Kongruenzsätze]] – Bestimmen, welche Dreiecke konstruierbar sind
- → [[01-Punkte-Strecken-Geraden|Punkte, Strecken, Geraden]] – Die Grundelemente jeder Konstruktion
- → [[02-Winkel-und-Winkelarten|Winkel]] – Winkel konstruieren und halbieren
- → [[06-Kreise|Kreise]] – Zirkel als Hauptwerkzeug
- → [[04-Dreiecke|Dreiecke]] – Besondere Punkte (Um-, Inkreis) durch Konstruktion finden
- → [[09-Symmetrie|Symmetrie]] – Spiegelungen lassen sich konstruieren

> [!tip] **Konstruktion üben**
> Konstruktionen lassen sich nicht nur aus dem Buch lernen – man muss sie selbst durchführen! Jede Konstruktion mehrfach üben, bis die Handgriffe sitzen.

## Übungsaufgaben

1. Konstruiere die Mittelsenkrechte einer 8 cm langen Strecke.

2. Konstruiere einen Winkel von 60° und halbiere ihn.

3. Konstruiere ein Dreieck mit:
   - $a = 6$ cm, $b = 5$ cm, $c = 7$ cm
   - $a = 5$ cm, $\beta = 45°$, $c = 6$ cm
   - $\alpha = 40°$, $\beta = 70°$, $c = 8$ cm

4. Konstruiere ein rechtwinkliges Dreieck mit Katheten 4 cm und 3 cm.

5. Konstruiere den Umkreis eines Dreiecks (Schnittpunkt der Mittelsenkrechten).

---

**Navigation**: [[11-Aehnlichkeit|← Ähnlichkeit]] | [[00-Geometrie-Index|Übersicht]] | [[../11-Satz-des-Pythagoras-und-Trigonometrie/00-Pythagoras-Trigonometrie-Index|Pythagoras →]]
