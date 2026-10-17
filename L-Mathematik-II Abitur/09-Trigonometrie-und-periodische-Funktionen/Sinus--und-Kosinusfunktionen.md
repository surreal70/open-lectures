---
author: Andreas Hümmer
title: Sinus- und Kosinusfunktionen
tags:
  - content
  - mathe
  - trigonometrie
  - sinusfunktion
  - kosinusfunktion
  - parameter
  - amplitude
  - periode
created: 2025-06-20
modified: 2025-06-20
---

# Sinus- und Kosinusfunktionen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die allgemeine Sinusfunktion mit ihren Parametern verstehen
> - Die Auswirkung von Amplitude, Periode und Phasenverschiebung auf den Graphen beschreiben können
> - Aus einem Graphen die Parameter ablesen können
> - Funktionsgleichungen für gegebene Graphen aufstellen können

---

## Überblick

Die **allgemeinen Sinus- und Kosinusfunktionen** entstehen aus den Grundfunktionen $\sin(x)$ und $\cos(x)$ durch Streckung, Stauchung und Verschiebung. Diese Transformationen werden durch Parameter beschrieben, die direkte physikalische Bedeutung haben: Amplitude, Periode und Phasenverschiebung. Das Verständnis dieser Parameter ist fundamental für die Beschreibung von Schwingungen und Wellen.

## Die allgemeine Sinusfunktion

### Standardform

Die allgemeine Sinusfunktion hat die Form:

$$f(x) = a \cdot \sin(b(x - c)) + d$$

Oder äquivalent:

$$f(x) = a \cdot \sin(bx + \varphi) + d$$

wobei $\varphi = -bc$ die **Phase** ist.

### Bedeutung der Parameter

| Parameter | Symbol | Bedeutung | Einfluss auf den Graph |
|-----------|--------|-----------|------------------------|
| Amplitude | $a$ | Maximale Auslenkung | Streckung/Stauchung vertikal |
| Frequenzfaktor | $b$ | Bestimmt die Periode | Stauchung/Streckung horizontal |
| Phasenverschiebung | $c$ | Verschiebung in $x$-Richtung | Graph nach rechts/links |
| Mittelwert | $d$ | Vertikale Verschiebung | Graph nach oben/unten |

## Die Amplitude $|a|$

### Definition

Die **Amplitude** ist der Betrag der maximalen Auslenkung vom Mittelwert:

$$\text{Amplitude} = |a|$$

### Auswirkung

- $|a| > 1$: Streckung in $y$-Richtung
- $|a| < 1$: Stauchung in $y$-Richtung
- $a < 0$: Spiegelung an der $x$-Achse

### Wertebereich

Die Funktion $f(x) = a \cdot \sin(bx) + d$ hat den Wertebereich:

$$W = [d - |a|, d + |a|]$$

### Beispiel

$f(x) = 3\sin(x)$ hat:
- Amplitude: $3$
- Wertebereich: $[-3, 3]$

## Die Periode $T$

### Definition

Die **Periode** $T$ ist die kleinste positive Zahl, für die gilt:

$$f(x + T) = f(x) \quad \text{für alle } x$$

### Berechnung

Aus dem Parameter $b$ ergibt sich die Periode:

$$\boxed{T = \frac{2\pi}{|b|}}$$

Umgekehrt:
$$b = \frac{2\pi}{T}$$

### Auswirkung

- $|b| > 1$: Periode kleiner als $2\pi$ (Stauchung horizontal)
- $|b| < 1$: Periode größer als $2\pi$ (Streckung horizontal)

### Beispiel

$f(x) = \sin(2x)$ hat:
- Periode: $T = \frac{2\pi}{2} = \pi$
- Der Graph „schwingt doppelt so schnell"

$g(x) = \sin\left(\frac{x}{3}\right)$ hat:
- Periode: $T = \frac{2\pi}{1/3} = 6\pi$
- Der Graph „schwingt dreimal so langsam"

## Die Phasenverschiebung $c$

### Definition

Die **Phasenverschiebung** gibt an, um wie viel der Graph in $x$-Richtung verschoben ist.

Bei $f(x) = \sin(b(x - c))$:
- $c > 0$: Verschiebung nach **rechts**
- $c < 0$: Verschiebung nach **links**

### Alternative Schreibweise

Bei $f(x) = \sin(bx + \varphi)$ ist die Phasenverschiebung:

$$c = -\frac{\varphi}{b}$$

### Beispiel

$f(x) = \sin\left(x - \frac{\pi}{4}\right)$:
- Phasenverschiebung: $c = \frac{\pi}{4}$ nach rechts
- Der Graph beginnt seinen „Anstieg" bei $x = \frac{\pi}{4}$

## Die vertikale Verschiebung $d$

### Definition

Der Parameter $d$ verschiebt den Graphen in $y$-Richtung:
- $d > 0$: Verschiebung nach **oben**
- $d < 0$: Verschiebung nach **unten**

### Mittelwertlinie

Die horizontale Gerade $y = d$ ist die **Mittelwertlinie** oder **Ruhelage** der Schwingung.

### Beispiel

$f(x) = \sin(x) + 2$ oszilliert um die Linie $y = 2$ mit Wertebereich $[1, 3]$.

## Analyse eines gegebenen Graphen

### Systematisches Vorgehen

1. **Mittelwert $d$:** Mitte zwischen Maximum und Minimum
   $$d = \frac{y_{\max} + y_{\min}}{2}$$

2. **Amplitude $|a|$:** Abstand vom Mittelwert zum Maximum
   $$|a| = \frac{y_{\max} - y_{\min}}{2}$$

3. **Periode $T$:** Abstand zwischen zwei aufeinanderfolgenden Maxima (oder Minima)

4. **Frequenzfaktor $b$:**
   $$b = \frac{2\pi}{T}$$

5. **Phasenverschiebung $c$:** Position des ersten „typischen Punkts" (z.B. Nulldurchgang mit positivem Anstieg)

### Beispiel

Ein Graph oszilliert zwischen $y = 1$ und $y = 5$, hat die Periode $\pi$, und schneidet die Mittelwertlinie bei $x = \frac{\pi}{6}$ mit positivem Anstieg.

Berechnung:
- $d = \frac{1 + 5}{2} = 3$
- $|a| = \frac{5 - 1}{2} = 2$
- $T = \pi \Rightarrow b = \frac{2\pi}{\pi} = 2$
- Phasenverschiebung: $c = \frac{\pi}{6}$

Funktionsgleichung:
$$f(x) = 2\sin\left(2\left(x - \frac{\pi}{6}\right)\right) + 3$$

## Zusammenhang zwischen Sinus und Kosinus

### Phasenbeziehung

Sinus und Kosinus unterscheiden sich nur durch eine Phasenverschiebung:

$$\cos(x) = \sin\left(x + \frac{\pi}{2}\right)$$

$$\sin(x) = \cos\left(x - \frac{\pi}{2}\right)$$

### Praktische Konsequenz

Jede Kosinusfunktion kann als Sinusfunktion geschrieben werden und umgekehrt:

$$a\cos(bx + \varphi) = a\sin\left(bx + \varphi + \frac{\pi}{2}\right)$$

## Kurvendiskussion

### Nullstellen

$f(x) = a\sin(b(x - c)) + d = 0$

$$\sin(b(x - c)) = -\frac{d}{a}$$

(Lösbar nur wenn $\left|\frac{d}{a}\right| \leq 1$)

### Extremstellen

Maxima und Minima bei:
$$f'(x) = ab\cos(b(x - c)) = 0$$

Das heißt: $b(x - c) = \frac{\pi}{2} + k\pi$

### Wendestellen

$$f''(x) = -ab^2\sin(b(x - c)) = 0$$

Das heißt: $b(x - c) = k\pi$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Sinus-und-Kosinus]] – Die Grundfunktionen
- → [[Phasenverschiebung]] – Vertiefung der Phasenbeziehung
- → [[Periodische-Vorgaenge]] – Physikalische Interpretation
- → [[Anwendungen-bei-Schwingungen-und-Wellen]] – Praktische Anwendung

> [!warning] **Prüfungsrelevant**
> - Die Formeln $T = \frac{2\pi}{|b|}$ und $b = \frac{2\pi}{T}$ sicher anwenden
> - Aus dem Graphen alle Parameter ablesen können
> - Zu gegebenen Parametern den Graphen skizzieren können
> - Funktionsgleichungen für beschriebene Schwingungen aufstellen

> [!question] **Typische Prüfungsfragen**
> - Bestimmen Sie Amplitude, Periode und Phasenverschiebung von $f(x) = 2\sin(3x - \pi) + 1$.
> - Skizzieren Sie den Graphen von $f(x) = -\cos(2x)$ für $x \in [0, 2\pi]$.
> - Eine Schwingung hat die Amplitude 4, die Periode $\pi$ und beginnt bei $x = 0$ im Maximum bei $y = 5$. Geben Sie die Funktionsgleichung an.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020.
- Lambacher Schweizer: Mathematik für Gymnasien, Oberstufe. Klett Verlag, 2019.

> [!tip] **Weiterführende Links**
> - [[Phasenverschiebung]] – Detaillierte Behandlung der Phase
> - [[Anwendungen-bei-Schwingungen-und-Wellen]] – Physikalische Kontexte
