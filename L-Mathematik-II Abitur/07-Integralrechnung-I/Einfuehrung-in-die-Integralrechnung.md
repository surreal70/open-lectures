---
author: Andreas Hümmer
title: Einführung in die Integralrechnung
tags:
  - content
  - mathe
  - integralrechnung
  - fläche
  - grundlagen
created: 2026-10-17
modified: 2026-10-17
---

# Einführung in die Integralrechnung

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die historische Entwicklung und Motivation der Integralrechnung verstehen
> - Das Flächenproblem als Ausgangspunkt der Integralrechnung erklären können
> - Den Zusammenhang zwischen Differential- und Integralrechnung kennen
> - Die grundlegende Idee der Zerlegung in infinitesimale Teile erfassen

---

## Überblick

Die Integralrechnung ist neben der Differentialrechnung der zweite fundamentale Pfeiler der Analysis. Während die Differentialrechnung lokale Änderungsraten untersucht, befasst sich die Integralrechnung mit dem umgekehrten Problem: Wie kann man aus einer gegebenen Änderungsrate die ursprüngliche Größe rekonstruieren? Diese Fragestellung führt unmittelbar zur Berechnung von Flächen unter Kurven und bildet die Grundlage für zahlreiche Anwendungen in Naturwissenschaft und Technik.

## Das Flächenproblem

### Die Grundidee

Das klassische Problem der Integralrechnung lautet: Wie berechnet man die Fläche zwischen dem Graphen einer Funktion $f(x)$, der $x$-Achse und zwei vertikalen Begrenzungslinien bei $x = a$ und $x = b$?

Für einfache geometrische Figuren wie Rechtecke oder Dreiecke existieren bekannte Formeln. Doch wie verfährt man bei gekrümmten Begrenzungen?

### Approximation durch Rechtecke

Die fundamentale Idee besteht darin, die gesuchte Fläche durch einfachere Figuren anzunähern:

1. **Zerlegung**: Teile das Intervall $[a, b]$ in $n$ gleich breite Teilintervalle der Breite $\Delta x = \frac{b-a}{n}$
2. **Approximation**: Errichte über jedem Teilintervall ein Rechteck mit der Höhe $f(x_i)$
3. **Summation**: Addiere die Flächen aller Rechtecke

Die Summe der Rechtecksflächen ergibt:

$$S_n = \sum_{i=1}^{n} f(x_i) \cdot \Delta x$$

### Obersumme und Untersumme

Je nach Wahl der Stützstellen unterscheidet man:

- **Untersumme** $U_n$: Man wählt in jedem Teilintervall den kleinsten Funktionswert
- **Obersumme** $O_n$: Man wählt in jedem Teilintervall den größten Funktionswert

Für eine stetige Funktion $f$ auf $[a, b]$ gilt stets:

$$U_n \leq A \leq O_n$$

wobei $A$ die tatsächliche Fläche bezeichnet.

## Der Grenzübergang

### Von der Summe zum Integral

Der entscheidende Schritt besteht im Grenzübergang $n \to \infty$. Lässt man die Anzahl der Rechtecke unbegrenzt wachsen (und damit ihre Breite gegen null gehen), so konvergieren Ober- und Untersumme gegen denselben Wert:

$$\lim_{n \to \infty} U_n = \lim_{n \to \infty} O_n = A$$

Dieser gemeinsame Grenzwert definiert das **bestimmte Integral**:

$$A = \int_a^b f(x) \, dx$$

### Das Integralsymbol

Das Integralzeichen $\int$ wurde von Gottfried Wilhelm Leibniz eingeführt und ist ein stilisiertes „S" für „Summe" (lateinisch: summa). Die Notation $dx$ deutet auf die infinitesimal kleine Breite der Rechtecke hin.

## Historische Entwicklung

### Antike Vorläufer

Bereits Archimedes (ca. 287–212 v. Chr.) verwendete die Methode der Erschöpfung, um Flächen und Volumina zu berechnen. Er approximierte Kreisflächen durch ein- und umschreibende Vielecke.

### Entwicklung im 17. Jahrhundert

Die eigentliche Integralrechnung wurde unabhängig voneinander von Isaac Newton (1643–1727) und Gottfried Wilhelm Leibniz (1646–1716) entwickelt. Beide erkannten den fundamentalen Zusammenhang zwischen Integration und Differentiation.

### Riemann-Integral

Bernhard Riemann (1826–1866) legte die rigorose mathematische Grundlage für das Integral. Das nach ihm benannte Riemann-Integral definiert die Integration über Zerlegungssummen und Grenzwertbildung.

## Der Zusammenhang zur Differentialrechnung

### Das umgekehrte Problem

Die Integralrechnung löst gewissermaßen das inverse Problem zur Differentiation:

| Differentialrechnung | Integralrechnung |
|---------------------|------------------|
| Gegeben: Funktion $f(x)$ | Gegeben: Ableitung $f'(x)$ |
| Gesucht: Ableitung $f'(x)$ | Gesucht: Funktion $f(x)$ |
| Frage: Wie schnell ändert sich $f$? | Frage: Welche Funktion hat diese Änderungsrate? |

### Anschauliche Interpretation

Wenn $v(t)$ die Geschwindigkeit eines Objekts zur Zeit $t$ beschreibt, dann ergibt das Integral $\int_a^b v(t) \, dt$ die zurückgelegte Strecke im Zeitintervall $[a, b]$.

Dies entspricht der physikalischen Beziehung: Die Geschwindigkeit ist die Ableitung des Weges nach der Zeit, also umgekehrt erhält man den Weg durch Integration der Geschwindigkeit.

## Anwendungsgebiete

Die Integralrechnung findet breite Anwendung in:

- **Physik**: Berechnung von Arbeit, Energie, Schwerpunkten
- **Technik**: Bestimmung von Volumina, Massen, Trägheitsmomenten
- **Wirtschaft**: Berechnung von Gesamtkosten aus Grenzkosten
- **Statistik**: Berechnung von Wahrscheinlichkeiten bei stetigen Verteilungen
- **Geometrie**: Flächen- und Volumenberechnungen

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Definition-der-Ableitung]] – Die Ableitung als Grundlage für den inversen Zusammenhang
- → [[Grenzwerte-von-Folgen]] – Grenzwertbildung als zentrales Konzept
- → [[Polynomfunktionen]] – Einfache Beispiele für Stammfunktionen
- → [[Stammfunktionen]] – Der nächste Schritt: Stammfunktionen finden
- → [[Bestimmte-Integrale]] – Formale Definition des bestimmten Integrals

> [!warning] **Prüfungsrelevant**
> - Das Flächenproblem als Motivation für die Integralrechnung verstehen
> - Die Approximation durch Rechtecksummen erklären können
> - Den Zusammenhang zwischen Ableitung und Integration kennen
> - Die Notation $\int_a^b f(x) \, dx$ korrekt interpretieren

> [!question] **Typische Prüfungsfragen**
> - Erläutere das Grundprinzip der Flächenberechnung durch Zerlegung in Rechtecke.
> - Warum konvergieren Ober- und Untersumme bei stetigen Funktionen gegen denselben Wert?
> - Beschreibe den Zusammenhang zwischen Differentiation und Integration am Beispiel Geschwindigkeit-Weg.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I. N. et al.: Taschenbuch der Mathematik. Verlag Harri Deutsch, 2012.
- Forster, O.: Analysis 1. Springer Spektrum, 2016.

> [!tip] **Weiterführende Links**
> - [[Stammfunktionen]] – Wie findet man Stammfunktionen?
> - [[Hauptsatz-der-Differential--und-Integralrechnung]] – Der zentrale Satz der Analysis
