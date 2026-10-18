---
title: "Überprüfung von Lösungen"
created: 2026-10-13
modified: 2026-10-16
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

Die **Probe** ist die Überprüfung, ob ein berechneter Wert tatsächlich eine Lösung der ursprünglichen Gleichung ist. Sie ist kein optionaler Zusatzschritt, sondern ein wesentlicher Teil des Lösungsprozesses.

Historisch gesehen war die Probe schon bei den babylonischen Mathematikern üblich. Sie formulierten ihre Lösungen oft als: „Du hast es richtig gefunden, wenn du zurücksetzt und das Ursprüngliche erhältst." Dieses Prinzip gilt bis heute.

> [!tip] **Gründe für die Probe**
> - **Rechenfehler aufdecken**: Selbst kleine Vorzeichenfehler werden sichtbar
> - **Scheinlösungen identifizieren**: Bei nicht-äquivalenten Umformungen können falsche Lösungen entstehen
> - **Prüfungspunkte sichern**: In Klausuren gibt es oft Punkte für die Probe
> - **Vertrauen stärken**: Du weißt sicher, dass dein Ergebnis stimmt
>
> In der Praxis: Programmierer nennen das „Testen" – auch dort wird geprüft, ob eine Lösung wirklich funktioniert.

> [!warning] **Häufiger Fehler: Probe in Zwischenschritt**
> Die Probe muss **immer in die Ausgangsgleichung** eingesetzt werden, nicht in einen Zwischenschritt! 
> 
> Warum? Ein Rechenfehler im Zwischenschritt würde sonst nicht auffallen – man würde nur prüfen, ob der Fehler konsistent weitergerechnet wurde.

## Durchführung der Probe

Die Probe folgt immer demselben einfachen Ablauf, egal um welchen Gleichungstyp es sich handelt. Im Kern geht es darum, den gefundenen Wert zurück in die Gleichung einzusetzen und zu prüfen, ob die Behauptung „linke Seite gleich rechte Seite" tatsächlich stimmt. Die folgenden Schritte halten dieses Vorgehen fest.

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

**Variante 1: Ausführlich** – linke und rechte Seite getrennt einsetzen und vergleichen.

Probe $x = 5$ in $4x - 7 = 13$:

$$\text{LS}: 4 \cdot 5 - 7 = 20 - 7 = 13$$
$$\text{RS}: 13$$
$$\text{LS} = \text{RS} \quad \checkmark$$

**Variante 2: Kompakt** – direkt einsetzen und bestätigen.

$$4 \cdot 5 - 7 = 13 \quad \checkmark$$

## Beispiele für Proben

Das Grundprinzip bleibt gleich, doch je nach Bauart der Gleichung sieht die Rechnung beim Einsetzen etwas anders aus. Die beiden folgenden Fälle zeigen, wie die Probe aussieht, wenn Klammern oder Brüche im Spiel sind – die Schritte sind dieselben, nur die Zwischenrechnungen unterscheiden sich.

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

Hier zeigt sich der eigentliche Wert der Probe: Nicht jeder berechnete Wert ist automatisch eine echte Lösung. Gerade weil manche Umformungen zusätzliche Werte ins Spiel bringen, ist das Einsetzen in die Ausgangsgleichung das einzige verlässliche Mittel, um echte Lösungen von Scheinlösungen zu trennen.

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

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[02-Aequivalenzumformungen|Äquivalenzumformungen]] – Welche Umformungen zu Scheinlösungen führen können
- → [[06-Bruchgleichungen|Bruchgleichungen]] – Hier entstehen besonders oft Scheinlösungen
- → [[08-Quadratische-Gleichungen|Quadratische Gleichungen]] – Probe bei zwei Lösungen
- → [[01-Grundlagen-von-Gleichungen|Definitionsbereich]] – Wann Werte ausgeschlossen werden müssen

## Übungsaufgaben

Führe die Probe durch und bestimme, ob die angegebenen Werte Lösungen sind:

1. $3x + 4 = 19$; $x = 5$
2. $2(x - 3) = x + 1$; $x = 7$
3. $\frac{x}{2} + 3 = x - 1$; $x = 8$
4. $x^2 - 4 = 0$; $x_1 = 2$, $x_2 = -2$
5. $\frac{5}{x+1} = 1$; $x = 4$

---

**Navigation**: [[02-Aequivalenzumformungen|← Äquivalenzumformungen]] | [[00-Gleichungen-und-Ungleichungen-Index|Übersicht]] | [[04-Lineare-Gleichungen|Lineare Gleichungen →]]
