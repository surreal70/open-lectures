---
title: "Einsetzen von Variablen"
chapter: "07"
section: "03"
type: topic
status: final
learning_objectives:
  - "Zahlenwerte für Variablen einsetzen"
  - "Termwerte berechnen"
  - "Wertetabellen erstellen"
  - "Terme auf Gleichheit prüfen"
tags:
  - mathematik
  - terme
  - einsetzen
  - termwert
created: 2026-10-13
modified: 2026-10-16
---

# Einsetzen von Variablen

> [!info] Lernziele
> - Zahlenwerte für Variablen einsetzen
> - Termwerte berechnen
> - Wertetabellen erstellen
> - Terme auf Gleichheit prüfen

## Überblick

Das **Einsetzen** von Zahlen für Variablen ermöglicht die Berechnung konkreter Termwerte.

Das Einsetzen ist der entscheidende Schritt, der abstrakte Mathematik mit der Realität verbindet. Ein Term wie $U = 2a + 2b$ für den Umfang eines Rechtecks ist zunächst nur eine allgemeine Formel. Erst wenn wir konkrete Maße einsetzen (z.B. $a = 5$ cm und $b = 3$ cm), erhalten wir ein praktisches Ergebnis: $U = 16$ cm.

> [!info] **Warum Klammern beim Einsetzen?**
> Beim Einsetzen sollte man die Zahl immer in Klammern setzen. Das verhindert Fehler, besonders bei negativen Zahlen oder wenn Potenzen vorkommen. Aus $x^2$ mit $x = -3$ wird so $(-3)^2 = 9$, nicht $-3^2 = -9$.

## Methode

1. Variable durch Klammer mit Zahl ersetzen
2. Rechenregeln (Punkt vor Strich, Klammern) beachten
3. Ausrechnen

## Beispiele

### Einfaches Einsetzen

**Term:** $T = 3x + 5$

Für x = 4:
$$T = 3 \cdot (4) + 5 = 12 + 5 = 17$$

### Mit mehreren Variablen

**Term:** $T = 2a - 3b$

Für a = 5, b = 2:
$$T = 2 \cdot (5) - 3 \cdot (2) = 10 - 6 = 4$$

### Mit Potenzen

**Term:** $T = x^2 + 2x$

Für x = 3:
$$T = (3)^2 + 2 \cdot (3) = 9 + 6 = 15$$

Für x = −2:
$$T = (-2)^2 + 2 \cdot (-2) = 4 - 4 = 0$$

> [!warning] **Häufiger Fehler: Negative Zahlen in Potenzen**
> Bei negativen Zahlen ist die Klammer entscheidend:
> - $(-2)^2 = (-2) \cdot (-2) = +4$ ✓ (minus mal minus = plus)
> - $-2^2 = -(2^2) = -4$ ✗ (hier wird nur die 2 quadriert, dann das Minus davor gesetzt)
> 
> Immer Klammern setzen, um Fehler zu vermeiden!

## Wertetabellen

Wertetabellen sind ein wichtiges Werkzeug, um das Verhalten eines Terms für verschiedene Werte zu untersuchen. Sie bilden die Grundlage für das Zeichnen von Funktionsgraphen (→ [[09-Funktionen-und-Koordinatensysteme/04-Funktionstabellen-und-Graphen|Funktionstabellen und Graphen]]).

| x | x² | 2x | x² + 2x |
|---|----|----|---------|
| −2 | 4 | −4 | 0 |
| −1 | 1 | −2 | −1 |
| 0 | 0 | 0 | 0 |
| 1 | 1 | 2 | 3 |
| 2 | 4 | 4 | 8 |

> [!tip] **Praktischer Tipp: Spaltenweise rechnen**
> Bei Wertetabellen ist es oft einfacher, zuerst eine ganze Spalte zu berechnen, bevor man zur nächsten geht. So behält man den Überblick und macht weniger Fehler.

> [!example] **Anwendung: Tabellenkalkulation**
> In Programmen wie Excel oder LibreOffice Calc funktionieren Formeln genauso: Eine Zelle enthält einen Term (z.B. `=A1*2+3`), und das Programm setzt automatisch den Wert aus Zelle A1 ein.

## Zusammenhänge

### Voraussetzungen

- [[02-Mathematische-Terme]]

## Prüfungsrelevanz

> [!warning] Prüfungsrelevanz: Hoch
> Grundvoraussetzung für Funktionen und Gleichungen.

## Typische Prüfungsfragen

1. Berechne den Wert von 4x − 3 für x = 2.
2. Erstelle eine Wertetabelle für x² − 1 mit x ∈ {−2, −1, 0, 1, 2}.
3. Für welchen Wert von x gilt: 2x + 1 = 7?

## Quellen

- Lambacher Schweizer Mathematik 7

## Weiterführende Links

- [[04-Zusammenfassen-gleichartiger-Terme]]
- [[09-Funktionen-und-Koordinatensysteme/00-Funktionen-Index|Funktionen]]
