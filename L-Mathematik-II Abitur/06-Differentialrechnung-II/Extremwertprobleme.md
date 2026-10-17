---
author: Andreas Hümmer
title: Extremwertprobleme
tags:
  - content
  - mathe
  - differentialrechnung
  - extremwertprobleme
  - optimierung
created: 2025-06-20
modified: 2025-06-20
---

# Extremwertprobleme

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Sachprobleme in mathematische Optimierungsaufgaben übersetzen können
> - Zielfunktion und Nebenbedingungen aufstellen können
> - Die systematische Lösungsstrategie für Extremwertprobleme anwenden können
> - Ergebnisse im Sachkontext interpretieren und auf Plausibilität prüfen können

---

## Überblick

**Extremwertprobleme** sind Anwendungsaufgaben, bei denen eine Größe (Fläche, Volumen, Kosten, Gewinn etc.) unter gegebenen Einschränkungen maximiert oder minimiert werden soll. Diese Aufgaben verbinden die Differentialrechnung mit der Modellierung realer Situationen und gehören zu den klassischen Abituraufgaben. Der Schlüssel liegt in der sauberen Übersetzung des Sachproblems in eine mathematische Zielfunktion.

## Grundstruktur eines Extremwertproblems

Jedes Extremwertproblem besteht aus:

1. **Zielgröße:** Was soll maximiert/minimiert werden?
2. **Nebenbedingungen:** Welche Einschränkungen gelten?
3. **Variable(n):** Welche Größen sind frei wählbar?

## Systematische Lösungsstrategie

### Schritt 1: Problem erfassen

- Lies die Aufgabe sorgfältig
- Identifiziere Zielgröße und Nebenbedingungen
- Fertige eine Skizze an (falls geometrisches Problem)

### Schritt 2: Variablen einführen

- Wähle geeignete Variable(n)
- Beachte sinnvolle Definitionsbereiche

### Schritt 3: Zielfunktion aufstellen

Drücke die zu optimierende Größe als Funktion der Variablen aus.

### Schritt 4: Nebenbedingung nutzen

Falls die Zielfunktion mehrere Variablen enthält:
- Stelle die Nebenbedingung als Gleichung auf
- Löse nach einer Variablen auf
- Setze in die Zielfunktion ein → Funktion einer Variablen

### Schritt 5: Extremum bestimmen

- Bilde $f'(x)$ und löse $f'(x) = 0$
- Prüfe hinreichende Bedingung
- Beachte Randwerte des Definitionsbereichs

### Schritt 6: Ergebnis interpretieren

- Berechne alle gesuchten Größen
- Prüfe Plausibilität
- Formuliere Antwortsatz im Sachkontext

## Beispiel 1: Rechteck mit maximalem Flächeninhalt

**Aufgabe:** Ein Rechteck soll mit einem Zaun von 100 m Länge eingezäunt werden. Welche Abmessungen hat das Rechteck mit dem größten Flächeninhalt?

### Lösung

**Schritt 1 & 2:** Skizze und Variable

```
     x
  ┌─────┐
  │     │ y
  └─────┘
```

Sei $x$ die Breite und $y$ die Höhe des Rechtecks.

**Schritt 3:** Zielfunktion

$$A(x, y) = x \cdot y \quad \text{(zu maximieren)}$$

**Schritt 4:** Nebenbedingung

Zaunlänge (Umfang): $2x + 2y = 100$

Auflösen: $y = 50 - x$

Einsetzen: $A(x) = x \cdot (50 - x) = 50x - x^2$

**Definitionsbereich:** $x \in (0, 50)$

**Schritt 5:** Extremum

$$A'(x) = 50 - 2x$$
$$A'(x) = 0 \implies x = 25$$

Hinreichende Bedingung:
$$A''(x) = -2 < 0 \implies \text{Maximum}$$

**Schritt 6:** Ergebnis

$$x = 25 \text{ m}, \quad y = 50 - 25 = 25 \text{ m}$$
$$A_{\max} = 25 \cdot 25 = 625 \text{ m}^2$$

**Antwortsatz:** Das Rechteck mit dem größten Flächeninhalt ist ein Quadrat mit Seitenlänge 25 m und Flächeninhalt 625 m².

## Beispiel 2: Dose mit minimalem Materialverbrauch

**Aufgabe:** Eine zylindrische Dose soll ein Volumen von 1 Liter (= 1000 cm³) fassen. Welche Abmessungen minimieren den Materialverbrauch für Boden, Deckel und Mantel?

### Lösung

**Skizze und Variable:**

Sei $r$ der Radius und $h$ die Höhe des Zylinders.

**Zielfunktion:** Oberfläche

$$O(r, h) = 2\pi r^2 + 2\pi rh \quad \text{(zu minimieren)}$$

**Nebenbedingung:** Volumen

$$V = \pi r^2 h = 1000$$
$$\implies h = \frac{1000}{\pi r^2}$$

**Einsetzen:**

$$O(r) = 2\pi r^2 + 2\pi r \cdot \frac{1000}{\pi r^2} = 2\pi r^2 + \frac{2000}{r}$$

**Definitionsbereich:** $r > 0$

**Ableitung:**

$$O'(r) = 4\pi r - \frac{2000}{r^2}$$

**Nullstelle:**

$$4\pi r = \frac{2000}{r^2}$$
$$4\pi r^3 = 2000$$
$$r^3 = \frac{500}{\pi}$$
$$r = \sqrt[3]{\frac{500}{\pi}} \approx 5{,}42 \text{ cm}$$

**Hinreichende Bedingung:**

$$O''(r) = 4\pi + \frac{4000}{r^3}$$

Für $r > 0$ ist $O''(r) > 0$ → Minimum

**Höhe:**

$$h = \frac{1000}{\pi r^2} = \frac{1000}{\pi \cdot \left(\frac{500}{\pi}\right)^{2/3}} = \frac{1000}{\pi^{1/3} \cdot 500^{2/3}}$$

Es ergibt sich: $h = 2r \approx 10{,}84$ cm

**Antwortsatz:** Die Dose mit minimalem Materialverbrauch hat Radius $r \approx 5{,}4$ cm und Höhe $h \approx 10{,}8$ cm. Die optimale Form hat $h = 2r$.

## Typische Extremwertprobleme

| Problemtyp | Zielgröße | Typische Nebenbedingung |
|------------|-----------|-------------------------|
| Einzäunung | Fläche maximieren | Zaunlänge fest |
| Behälter | Material minimieren | Volumen fest |
| Verpackung | Volumen maximieren | Materialfläche fest |
| Gewinn | Gewinn maximieren | Produktionsfunktion |
| Weg/Zeit | Strecke minimieren | Geometrische Bedingung |

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Extremstellen]] – Mathematische Grundlage
- → [[Optimierungsaufgaben]] – Weitere Anwendungen
- → [[Vollstaendige-Kurvendiskussion]] – Analyse der Zielfunktion
- → [[Anwendungen-in-Physik-und-Technik]] – Praktische Kontexte
- → [[Ableitungsregeln]] – Berechnung der Ableitungen

> [!warning] **Prüfungsrelevant**
> - Immer erst Skizze anfertigen und Variable benennen
> - Zielfunktion muss von EINER Variablen abhängen
> - Nebenbedingung eliminiert überzählige Variablen
> - Definitionsbereich der Zielfunktion beachten (oft physikalisch eingeschränkt)
> - Randwerte prüfen, falls Definitionsbereich abgeschlossen
> - Ergebnis im Sachkontext formulieren

> [!question] **Typische Prüfungsfragen**
> - Stellen Sie die Zielfunktion und Nebenbedingung auf
> - Bestimmen Sie die optimalen Abmessungen
> - Zeigen Sie, dass für die optimale Lösung gilt: [Beziehung]
> - Wie ändert sich das Optimum, wenn die Nebenbedingung variiert wird?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020
- ISB Bayern: Lehrplan Mathematik Gymnasium (LehrplanPLUS)

> [!tip] **Weiterführende Links**
> - [[Optimierungsaufgaben]] – Weitere Beispiele und Aufgabentypen
> - [[Anwendungen-in-Physik-und-Technik]] – Physikalische Optimierung
