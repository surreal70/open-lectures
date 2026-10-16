---
title: "Überprüfung von Lösungen"
created: 2026-10-13
modified: 2026-10-13
chapter: "08"
section: "03"
status: "draft - review pending"
type: lecture
keywords:
  - Probe
  - Lösungsprüfung
  - Verifikation
  - Definitionsbereich
---

# Überprüfung von Lösungen

> [!info] Lernziele
> - Die Probe als Kontrollinstrument anwenden können
> - Lösungen systematisch auf Richtigkeit prüfen
> - Definitionsbereiche bei der Prüfung berücksichtigen
> - Rechenfehler durch Proben aufdecken

## Warum Proben wichtig sind

Die **Probe** ist die Überprüfung, ob ein berechneter Wert tatsächlich eine Lösung der ursprünglichen Gleichung ist.

> [!tip] Gründe für die Probe
> - Rechenfehler aufdecken
> - Scheinlösungen identifizieren (bei nicht-äquivalenten Umformungen)
> - Prüfungspunkte sichern
> - Vertrauen in das eigene Ergebnis stärken

## Durchführung der Probe

### Grundprinzip

1. Den berechneten Wert in die **Ausgangsgleichung** einsetzen
2. Beide Seiten separat ausrechnen
3. Prüfen, ob beide Seiten gleich sind

### Standardbeispiel

**Gleichung**: $4x - 7 = 13$

**Lösung**: $x = 5$

**Probe**:
$$\text{Linke Seite: } 4 \cdot 5 - 7 = 20 - 7 = 13$$
$$\text{Rechte Seite: } 13$$
$$\text{LS} = \text{RS} \checkmark$$

### Schreibweise der Probe

**Variante 1: Ausführlich**
```
Probe: x = 5 in 4x - 7 = 13
LS: 4 · 5 - 7 = 20 - 7 = 13
RS: 13
LS = RS ✓
```

**Variante 2: Kompakt**
```
Probe: 4 · 5 - 7 = 13 ✓
```

## Beispiele für Proben

### Lineare Gleichung mit Klammern

**Gleichung**: $3(x + 2) - 5 = 2x + 4$

**Berechnung ergibt**: $x = 3$

**Probe**:
$$\text{LS: } 3(3 + 2) - 5 = 3 \cdot 5 - 5 = 15 - 5 = 10$$
$$\text{RS: } 2 \cdot 3 + 4 = 6 + 4 = 10$$
$$\text{LS} = \text{RS} \checkmark$$

### Bruchgleichung

**Gleichung**: $\frac{x + 3}{2} = 5$

**Berechnung ergibt**: $x = 7$

**Probe**:
$$\text{LS: } \frac{7 + 3}{2} = \frac{10}{2} = 5$$
$$\text{RS: } 5$$
$$\text{LS} = \text{RS} \checkmark$$

## Fehler durch Proben entdecken

### Beispiel: Rechenfehler aufgedeckt

**Gleichung**: $2x + 8 = 3x - 2$

**Falsche Berechnung**: $x = -10$

**Probe**:
$$\text{LS: } 2 \cdot (-10) + 8 = -20 + 8 = -12$$
$$\text{RS: } 3 \cdot (-10) - 2 = -30 - 2 = -32$$
$$-12 \neq -32 \quad \text{✗ Fehler!}$$

**Korrekte Lösung**: $x = 10$

**Probe der korrekten Lösung**:
$$\text{LS: } 2 \cdot 10 + 8 = 28$$
$$\text{RS: } 3 \cdot 10 - 2 = 28$$
$$\text{LS} = \text{RS} \checkmark$$

## Scheinlösungen erkennen

Bei bestimmten Umformungen (Quadrieren, Multiplikation mit Variablen) können **Scheinlösungen** entstehen – Werte, die mathematisch berechnet wurden, aber die Originalgleichung nicht erfüllen.

### Beispiel: Bruchgleichung

**Gleichung**: $\frac{6}{x-2} = \frac{x+1}{1}$

Nach Umformung: $x = 4$ oder $x = -1$... aber:

**Probe für $x = -1$**:

Wenn $x = -1$: Definitionsbereich prüfen! Hier: $x \neq 2$ ✓

$$\text{LS: } \frac{6}{-1-2} = \frac{6}{-3} = -2$$
$$\text{RS: } -1 + 1 = 0$$
$$-2 \neq 0 \quad \text{✗ Scheinlösung!}$$

## Definitionsbereich beachten

> [!warning] Wichtig
> Vor der Probe muss geprüft werden, ob die Lösung überhaupt im Definitionsbereich liegt!

### Beispiel

**Gleichung**: $\frac{12}{x} = 4$

**Definitionsbereich**: $x \neq 0$

**Lösung**: $x = 3$

**Prüfung Definitionsbereich**: $3 \neq 0$ ✓

**Probe**: $\frac{12}{3} = 4$ ✓

## Probe bei quadratischen Gleichungen

Quadratische Gleichungen haben oft zwei Lösungen – beide müssen geprüft werden!

### Beispiel

**Gleichung**: $x^2 - 5x + 6 = 0$

**Lösungen**: $x_1 = 2$ und $x_2 = 3$

**Probe für $x_1 = 2$**:
$$2^2 - 5 \cdot 2 + 6 = 4 - 10 + 6 = 0 \checkmark$$

**Probe für $x_2 = 3$**:
$$3^2 - 5 \cdot 3 + 6 = 9 - 15 + 6 = 0 \checkmark$$

Beide Lösungen sind korrekt.

## Checkliste für die Probe

> [!tip] Systematische Prüfung
> 1. ☐ Liegt die Lösung im Definitionsbereich?
> 2. ☐ In die **Ausgangsgleichung** einsetzen (nicht in Zwischenschritte!)
> 3. ☐ Linke und rechte Seite **getrennt** berechnen
> 4. ☐ Sind beide Seiten gleich?
> 5. ☐ Bei mehreren Lösungen: **alle** prüfen

## Zusammenfassung

> [!abstract] Kernpunkte
> - Die Probe ist unverzichtbar für sichere Ergebnisse
> - Immer in die **Ausgangsgleichung** einsetzen
> - Definitionsbereich vor der Probe prüfen
> - Scheinlösungen können durch nicht-äquivalente Umformungen entstehen
> - Bei mehreren Lösungen alle einzeln prüfen

## Übungsaufgaben

Führe die Probe durch und bestimme, ob die angegebenen Werte Lösungen sind:

1. $3x + 4 = 19$; $x = 5$
2. $2(x - 3) = x + 1$; $x = 7$
3. $\frac{x}{2} + 3 = x - 1$; $x = 8$
4. $x^2 - 4 = 0$; $x_1 = 2$, $x_2 = -2$
5. $\frac{5}{x+1} = 1$; $x = 4$

---

**Navigation**: [[02-Aequivalenzumformungen|← Äquivalenzumformungen]] | [[00-Gleichungen-und-Ungleichungen-Index|Übersicht]] | [[04-Lineare-Gleichungen|Lineare Gleichungen →]]
