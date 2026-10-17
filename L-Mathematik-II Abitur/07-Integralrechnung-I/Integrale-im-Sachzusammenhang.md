---
author: Andreas Hümmer
title: Integrale im Sachzusammenhang
tags:
  - content
  - mathe
  - integralrechnung
  - anwendung
  - modellierung
created: 2026-10-17
modified: 2026-10-17
---

# Integrale im Sachzusammenhang

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Bedeutung von Integralen in praktischen Anwendungen verstehen
> - Integrale zur Berechnung von Gesamtgrößen aus Änderungsraten einsetzen können
> - Den Zusammenhang zwischen Stammfunktion und Ursprungsgröße erkennen
> - Typische Sachaufgaben mit Integralen lösen können

---

## Überblick

Integrale begegnen uns in vielen praktischen Zusammenhängen: Wenn wir die zurückgelegte Strecke aus der Geschwindigkeit berechnen, die Gesamtkosten aus den Grenzkosten ermitteln oder die aufgenommene Wassermenge aus der Zuflussrate bestimmen. Der Schlüssel liegt im Verständnis: Das Integral einer Änderungsrate ergibt die Gesamtänderung.

## Das Grundprinzip

### Von der Änderungsrate zur Bestandsgröße

Ist $f(t)$ die **momentane Änderungsrate** einer Größe $F(t)$ zur Zeit $t$, dann ist:

$$\int_a^b f(t) \, dt = F(b) - F(a)$$

Das Integral der Änderungsrate über ein Zeitintervall ergibt die **Gesamtänderung** der Größe in diesem Zeitraum.

### Interpretation

| Änderungsrate $f(t)$ | Integral $\int_a^b f(t) \, dt$ |
|---------------------|------------------------------|
| Geschwindigkeit | Zurückgelegte Strecke |
| Zuflussrate | Zugeflossene Menge |
| Produktionsrate | Produzierte Stückzahl |
| Grenzkosten | Gesamtkosten |
| Leistung | Verrichtete Arbeit |

## Anwendung: Bewegung

### Geschwindigkeit und Weg

Ist $v(t)$ die Geschwindigkeit eines Objekts zur Zeit $t$, so ist die im Zeitintervall $[t_1, t_2]$ zurückgelegte Strecke:

$$s = \int_{t_1}^{t_2} v(t) \, dt$$

### Beispiel: Beschleunigte Bewegung

Ein Auto beschleunigt aus dem Stand. Seine Geschwindigkeit ist $v(t) = 3t$ m/s für $t \geq 0$.

**Frage**: Welche Strecke legt es in den ersten 4 Sekunden zurück?

**Lösung**:
$$s = \int_0^4 3t \, dt = \left[\frac{3t^2}{2}\right]_0^4 = \frac{3 \cdot 16}{2} - 0 = 24 \text{ m}$$

### Beschleunigung und Geschwindigkeit

Analog gilt: Ist $a(t)$ die Beschleunigung, so ergibt sich die Geschwindigkeitsänderung durch Integration:

$$v(t_2) - v(t_1) = \int_{t_1}^{t_2} a(t) \, dt$$

## Anwendung: Zu- und Abfluss

### Die Situation

Ein Behälter wird mit einer zeitabhängigen Rate $z(t)$ gefüllt (oder geleert). Die Gesamtmenge, die im Zeitraum $[a, b]$ zu- oder abfließt, ist:

$$V = \int_a^b z(t) \, dt$$

### Beispiel: Wassertank

Ein Tank wird mit der Rate $z(t) = 20 - 2t$ Liter pro Minute gefüllt ($t$ in Minuten).

**Frage a)**: Wann stoppt der Zufluss?
$$z(t) = 0 \Rightarrow 20 - 2t = 0 \Rightarrow t = 10 \text{ min}$$

**Frage b)**: Wie viel Wasser fließt in den ersten 10 Minuten zu?
$$V = \int_0^{10} (20 - 2t) \, dt = \left[20t - t^2\right]_0^{10} = 200 - 100 = 100 \text{ Liter}$$

**Frage c)**: Was passiert nach $t = 10$?
Für $t > 10$ ist $z(t) < 0$, d.h. es fließt Wasser ab (falls möglich).

## Anwendung: Wirtschaft

### Grenzkosten und Gesamtkosten

Die **Grenzkosten** $K'(x)$ geben an, wie sich die Kosten bei Erhöhung der Produktionsmenge um eine Einheit ändern.

Die **Gesamtkostenänderung** bei Erhöhung der Produktion von $x_1$ auf $x_2$ Einheiten ist:

$$K(x_2) - K(x_1) = \int_{x_1}^{x_2} K'(x) \, dx$$

### Beispiel: Produktionskosten

Ein Unternehmen hat Grenzkosten von $K'(x) = 0{,}02x + 5$ Euro pro Stück.

**Frage**: Wie viel kostet die Erhöhung der Produktion von 100 auf 200 Stück?

$$\Delta K = \int_{100}^{200} (0{,}02x + 5) \, dx = \left[0{,}01x^2 + 5x\right]_{100}^{200}$$
$$= (400 + 1000) - (100 + 500) = 1400 - 600 = 800 \text{ Euro}$$

### Grenzerlös und Gesamterlös

Analog: Der **Grenzerlös** $E'(x)$ integriert ergibt den Gesamterlös.

## Anwendung: Physik

### Arbeit und Leistung

Die **Leistung** $P(t)$ ist die momentane Arbeitsrate. Die verrichtete **Arbeit** im Zeitintervall $[t_1, t_2]$ ist:

$$W = \int_{t_1}^{t_2} P(t) \, dt$$

### Kraft und Arbeit

Wirkt eine ortsabhängige Kraft $F(x)$ entlang eines Weges, so ist die Arbeit:

$$W = \int_{x_1}^{x_2} F(x) \, dx$$

### Beispiel: Feder

Eine Feder wird mit der Kraft $F(x) = kx$ gespannt ($k$ = Federkonstante).

Die Arbeit zum Spannen um die Strecke $s$:
$$W = \int_0^s kx \, dx = \left[\frac{1}{2}kx^2\right]_0^s = \frac{1}{2}ks^2$$

## Mittelwert einer Funktion

### Definition

Der **Mittelwert** (Durchschnittswert) einer Funktion $f$ auf dem Intervall $[a, b]$ ist:

$$\bar{f} = \frac{1}{b-a} \int_a^b f(x) \, dx$$

### Interpretation

Der Mittelwert ist die Höhe eines Rechtecks mit der Breite $(b-a)$, das dieselbe Fläche hat wie die Fläche unter dem Graphen von $f$.

### Beispiel: Durchschnittstemperatur

Die Temperatur im Tagesverlauf sei $T(t) = 15 + 8\sin\left(\frac{\pi t}{12}\right)$ °C für $0 \leq t \leq 24$ (Stunden).

**Durchschnittstemperatur**:
$$\bar{T} = \frac{1}{24} \int_0^{24} \left(15 + 8\sin\left(\frac{\pi t}{12}\right)\right) dt$$

$$= \frac{1}{24} \left[15t - 8 \cdot \frac{12}{\pi}\cos\left(\frac{\pi t}{12}\right)\right]_0^{24}$$

$$= \frac{1}{24} \left[(360 - \frac{96}{\pi}\cos(2\pi)) - (0 - \frac{96}{\pi}\cos(0))\right]$$

$$= \frac{1}{24} \cdot 360 = 15 \text{ °C}$$

## Strategien für Sachaufgaben

### Schritt-für-Schritt

1. **Identifiziere** die gegebene Größe: Ist es eine Änderungsrate oder ein Bestand?
2. **Erkenne** den Zusammenhang: Integration liefert die Gesamtänderung
3. **Setze** die Integrationsgrenzen entsprechend der Fragestellung
4. **Berechne** das Integral
5. **Interpretiere** das Ergebnis im Sachkontext mit Einheiten

### Einheiten prüfen

Die Einheit des Integrals ist das Produkt aus:
- Einheit des Integranden
- Einheit der Integrationsvariablen

**Beispiel**: $v$ in m/s, $t$ in s → $\int v \, dt$ in m/s · s = m

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Bestimmte-Integrale]] – Die mathematische Grundlage
- → [[Hauptsatz-der-Differential--und-Integralrechnung]] – Der theoretische Zusammenhang
- → [[Momentane-aenderungsrate]] – Ableitung als Änderungsrate
- → [[Exponentielles-Wachstum]] – Wachstumsprozesse modellieren
- → [[Anwendungen-in-Physik-und-Technik]] – Weitere physikalische Anwendungen

> [!warning] **Prüfungsrelevant**
> - Das Integral einer Änderungsrate ergibt die Gesamtänderung
> - Geschwindigkeit → Weg, Zuflussrate → Menge, Grenzkosten → Kosten
> - Der Mittelwert: $\bar{f} = \frac{1}{b-a} \int_a^b f(x) \, dx$
> - Einheiten im Ergebnis beachten und interpretieren

> [!question] **Typische Prüfungsfragen**
> - Ein Auto fährt mit der Geschwindigkeit $v(t) = 20 + 2t$ m/s. Welche Strecke legt es in 10 Sekunden zurück?
> - Die Zuflussrate in einen Teich ist $z(t) = 100e^{-0{,}1t}$ Liter/min. Berechne die Wassermenge, die in der ersten Stunde zufließt.
> - Erkläre den Zusammenhang zwischen Grenzkosten und Gesamtkosten mithilfe der Integralrechnung.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Tietze, J.: Einführung in die angewandte Wirtschaftsmathematik. Springer Spektrum, 2013.
- Tipler, P. A.; Mosca, G.: Physik für Wissenschaftler und Ingenieure. Springer Spektrum, 2015.

> [!tip] **Weiterführende Links**
> - [[Flaechenberechnung]] – Geometrische Anwendungen
> - [[Anwendungen-in-Physik-und-Technik]] – Weitere Beispiele aus der Physik
