---
author: Andreas Hümmer
title: Anwendungen algebraischer Methoden
tags:
  - content
  - mathe
  - algebra
  - anwendungen
  - modellierung
  - textaufgaben
created: 2025-01-13
modified: 2025-01-13
---

# Anwendungen algebraischer Methoden

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Sachsituationen in algebraische Gleichungen übersetzen können
> - Optimierungsprobleme mit algebraischen Methoden lösen können
> - Physikalische und technische Anwendungen mathematisch modellieren können
> - Lösungen auf Plausibilität prüfen und interpretieren können

---

## Überblick

Die Algebra ist kein Selbstzweck, sondern ein mächtiges Werkzeug zur Lösung praktischer Probleme. Ob in der Physik, Wirtschaft, Technik oder im Alltag – überall treten Fragestellungen auf, die sich durch algebraische Modellierung und Gleichungslösen bearbeiten lassen. Dieses Kapitel zeigt exemplarisch, wie die gelernten Methoden angewendet werden.

## Modellierungskreislauf

Der Prozess vom Problem zur Lösung folgt typischerweise diesem Schema:

1. **Verstehen:** Sachsituation analysieren, relevante Größen identifizieren
2. **Modellieren:** Mathematisches Modell aufstellen (Gleichung/Ungleichung)
3. **Lösen:** Algebraische Methoden anwenden
4. **Interpretieren:** Mathematische Lösung im Sachkontext deuten
5. **Validieren:** Ergebnis auf Plausibilität prüfen

> [!tip] **Systematisches Vorgehen**
> - Variable(n) mit Einheit definieren: „Sei $x$ die gesuchte Länge in cm."
> - Gleichung(en) aufstellen und kommentieren
> - Lösung berechnen und Einheit angeben
> - Probe durchführen und Antwort formulieren

## Geometrische Anwendungen

### Beispiel 1: Rechteck mit vorgegebenem Umfang

**Aufgabe:** Ein Rechteck hat einen Umfang von 24 cm. Welche Maße muss es haben, damit die Fläche maximal wird?

**Modellierung:**

Sei $x$ die Länge und $y$ die Breite (in cm).

- Umfang: $2x + 2y = 24 \Rightarrow y = 12 - x$
- Fläche: $A(x) = x \cdot y = x(12 - x) = 12x - x^2$

**Lösung:**

Die Fläche ist eine nach unten geöffnete Parabel. Maximum am Scheitelpunkt:

$$x_S = -\frac{12}{2 \cdot (-1)} = 6$$

Also $x = 6$ cm und $y = 12 - 6 = 6$ cm.

**Antwort:** Das Rechteck mit maximalem Flächeninhalt ist ein Quadrat mit Seitenlänge 6 cm. Die maximale Fläche beträgt 36 cm².

### Beispiel 2: Pythagoras-Anwendung

**Aufgabe:** Eine Leiter lehnt an einer Wand. Der Fuß ist 3 m von der Wand entfernt, die Leiter reicht 4 m hoch. Wie lang ist die Leiter?

**Modellierung:** Satz des Pythagoras

$$l^2 = 3^2 + 4^2 = 9 + 16 = 25$$

$$l = 5 \text{ m}$$

## Physikalische Anwendungen

### Beispiel 3: Freier Fall

**Aufgabe:** Ein Stein wird aus 80 m Höhe fallen gelassen. Nach welcher Zeit erreicht er den Boden? (Luftwiderstand vernachlässigt, $g = 10 \frac{\text{m}}{\text{s}^2}$)

**Modellierung:** Weg-Zeit-Gesetz des freien Falls

$$h(t) = h_0 - \frac{1}{2}gt^2$$

$$0 = 80 - 5t^2$$

$$t^2 = 16 \Rightarrow t = 4 \text{ s}$$

(Negative Lösung $t = -4$ entfällt, da Zeit positiv)

### Beispiel 4: Schiefer Wurf

**Aufgabe:** Ein Ball wird mit 20 m/s unter einem Winkel von 45° geworfen. In welcher Entfernung landet er?

**Modellierung:** Bahngleichung (vereinfacht)

$$y = x \cdot \tan(45°) - \frac{g \cdot x^2}{2v_0^2 \cdot \cos^2(45°)}$$

Mit $\tan(45°) = 1$, $\cos(45°) = \frac{1}{\sqrt{2}}$:

$$0 = x - \frac{10 \cdot x^2}{2 \cdot 400 \cdot 0{,}5} = x - \frac{x^2}{40}$$

$$x\left(1 - \frac{x}{40}\right) = 0 \Rightarrow x = 40 \text{ m}$$

## Wirtschaftliche Anwendungen

### Beispiel 5: Gewinnmaximierung

**Aufgabe:** Ein Unternehmen produziert ein Produkt. Die Kostenfunktion ist $K(x) = x^2 + 10x + 100$ (in €), der Verkaufspreis beträgt 50 € pro Stück. Bei welcher Stückzahl wird der Gewinn maximal?

**Modellierung:**

- Erlös: $E(x) = 50x$
- Gewinn: $G(x) = E(x) - K(x) = 50x - x^2 - 10x - 100 = -x^2 + 40x - 100$

**Lösung:**

Scheitelpunkt der nach unten geöffneten Parabel:

$$x_S = -\frac{40}{2 \cdot (-1)} = 20$$

$$G(20) = -400 + 800 - 100 = 300 \text{ €}$$

**Antwort:** Bei 20 Stück ist der Gewinn mit 300 € maximal.

### Beispiel 6: Mischungsrechnung

**Aufgabe:** Wie viel Liter einer 30%igen und einer 70%igen Salzlösung müssen gemischt werden, um 10 Liter einer 45%igen Lösung zu erhalten?

**Modellierung:**

Sei $x$ die Menge der 30%igen Lösung (in Litern).

Dann ist $(10 - x)$ die Menge der 70%igen Lösung.

Salzgehalt:
$$0{,}30 \cdot x + 0{,}70 \cdot (10 - x) = 0{,}45 \cdot 10$$

$$0{,}30x + 7 - 0{,}70x = 4{,}5$$

$$-0{,}40x = -2{,}5 \Rightarrow x = 6{,}25$$

**Antwort:** 6,25 Liter der 30%igen und 3,75 Liter der 70%igen Lösung.

## Zahlenrätsel und Logik

### Beispiel 7: Altersrätsel

**Aufgabe:** Heute ist Vater dreimal so alt wie sein Sohn. In 12 Jahren wird er nur noch doppelt so alt sein. Wie alt sind beide heute?

**Modellierung:**

Sei $s$ das heutige Alter des Sohnes.

- Vater heute: $3s$
- In 12 Jahren: $(s + 12)$ und $(3s + 12)$

Bedingung: $3s + 12 = 2(s + 12)$

$$3s + 12 = 2s + 24 \Rightarrow s = 12$$

**Antwort:** Der Sohn ist 12 Jahre alt, der Vater 36 Jahre.

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Gleichungssysteme]] – Systeme in Anwendungsaufgaben
- → [[Ungleichungen]] – Nebenbedingungen und Gültigkeitsbereiche
- → [[Quadratische-Funktionen]] – Extremwertaufgaben
- → [[Wachstumsprozesse]] – Exponentielles Wachstum modellieren

> [!warning] **Prüfungsrelevant**
> - Systematische Modellierung von Textaufgaben
> - Definitionsbereich im Sachkontext beachten (z.B. $x > 0$)
> - Interpretation der mathematischen Lösung
> - Plausibilitätsprüfung (Einheiten, Größenordnung)

> [!question] **Typische Prüfungsfragen**
> - Ein Draht von 60 cm Länge wird zu einem Rechteck gebogen. Welche Maße hat das flächengrößte Rechteck?
> - Zwei Autos fahren aufeinander zu: eines mit 80 km/h, das andere mit 100 km/h. Die Entfernung beträgt 270 km. Nach welcher Zeit treffen sie sich?
> - Ein Händler mischt zwei Kaffeesorten zu 8 €/kg und 12 €/kg. Wie viel von jeder Sorte braucht er für 20 kg Mischung zu 9 €/kg?

## Quellen

- Papula, L.: *Mathematik für Ingenieure und Naturwissenschaftler*, Band 1, Springer Vieweg
- Bronstein, I. N. et al.: *Taschenbuch der Mathematik*, Verlag Europa-Lehrmittel
- ISB Bayern: *Lehrplan Mathematik Gymnasium*

> [!tip] **Weiterführende Links**
> - [[Glossar#Modellierung|Glossar: Modellierung]]
> - [[Projekte]] – Weitere Modellierungsprojekte
