---
author: Open Lectures
title: Multiplikation von Brüchen
status: draft - review pending
tags:
  - content
  - mathematik
  - bruchrechnung
created: 2026-10-13
modified: 2026-10-16
---

# Multiplikation von Brüchen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Brüche miteinander multiplizieren können
> - Die Regel „Zähler mal Zähler, Nenner mal Nenner" anwenden
> - Vor dem Multiplizieren kürzen können

---

## Überblick

Die Multiplikation von Brüchen ist einfacher als Addition und Subtraktion: Man multipliziert Zähler mit Zähler und Nenner mit Nenner. Kein gemeinsamer Nenner nötig!

Im Alltag begegnet uns die Bruchmultiplikation, wenn wir Anteile von Anteilen berechnen: „Die Hälfte von drei Vierteln" oder „zwei Drittel der Strecke". Das Wort „von" signalisiert oft eine Multiplikation mit Brüchen.

Interessanterweise wird das Ergebnis bei der Multiplikation mit einem echten Bruch **kleiner** als der Ausgangswert – anders als bei der Multiplikation mit ganzen Zahlen. Das irritiert anfangs, ist aber logisch: „Die Hälfte von etwas" ist weniger als das Original.

---

## Regel

$$\frac{a}{b} \cdot \frac{c}{d} = \frac{a \cdot c}{b \cdot d}$$

**Beispiel:**
$$\frac{2}{3} \cdot \frac{4}{5} = \frac{2 \cdot 4}{3 \cdot 5} = \frac{8}{15}$$

> [!note] **Warum funktioniert das so einfach?**
> Bei der Multiplikation fragen wir: „Wie viel ist ein Anteil von einem Anteil?"
> 
> $\frac{2}{3} \cdot \frac{4}{5}$ bedeutet: „Zwei Drittel von vier Fünfteln"
> 
> Wenn wir etwas in Drittel und dann in Fünftel teilen, haben wir Fünfzehntel (3 × 5 = 15).
> Davon nehmen wir 2 × 4 = 8 Stücke.

---

## Anschauliche Erklärung

$\frac{1}{2} \cdot \frac{1}{3}$ = „die Hälfte von einem Drittel"

```
    1/3 des Ganzen:
    ┌───────┬───────┬───────┐
    │   ▓   │       │       │
    │   ▓   │       │       │
    └───────┴───────┴───────┘
    
    1/2 davon (obere Hälfte des gefärbten Drittels):
    ┌───────┬───────┬───────┐
    │  ▓▓▓  │       │       │
    ├───────┼───────┼───────┤
    │       │       │       │
    └───────┴───────┴───────┘
          = 1/6 des Ganzen
```

Das Ganze wurde in 6 Teile geteilt (2 Zeilen × 3 Spalten), und wir haben 1 davon markiert: $\frac{1}{2} \cdot \frac{1}{3} = \frac{1}{6}$

---

## Kürzen vor dem Multiplizieren

> [!tip] **Rechenvorteil: Kreuzkürzen**
> Vor dem Multiplizieren kürzen spart Arbeit und hält die Zahlen klein!

**Beispiel:** $\frac{3}{8} \cdot \frac{4}{9}$

**Ohne Kürzen:**
$$\frac{3}{8} \cdot \frac{4}{9} = \frac{12}{72} = \frac{1}{6}$$ (mühsames Kürzen am Ende)

**Mit Kreuzkürzen:**
- 3 und 9 haben gemeinsamen Teiler 3: $\frac{\cancel{3}^1}{8} \cdot \frac{4}{\cancel{9}^3}$
- 4 und 8 haben gemeinsamen Teiler 4: $\frac{1}{\cancel{8}^2} \cdot \frac{\cancel{4}^1}{3}$
- Ergebnis: $\frac{1 \cdot 1}{2 \cdot 3} = \frac{1}{6}$

> [!note] **Wie funktioniert Kreuzkürzen?**
> Du darfst einen Zähler mit einem beliebigen Nenner kürzen, weil am Ende sowieso alle Zähler miteinander und alle Nenner miteinander multipliziert werden. Die Reihenfolge spielt keine Rolle.

> [!warning] **Häufiger Fehler**
> Kreuzkürzen funktioniert NUR bei Multiplikation!
> Bei Addition/Subtraktion darf man NICHT über Kreuz kürzen.

---

## Bruch mal ganze Zahl

Eine ganze Zahl als Bruch schreiben: $n = \frac{n}{1}$

$$\frac{3}{4} \cdot 5 = \frac{3}{4} \cdot \frac{5}{1} = \frac{15}{4} = 3\frac{3}{4}$$

> [!tip] **Schneller Weg**
> Bei Bruch mal ganze Zahl multiplizierst du einfach den Zähler mit der ganzen Zahl:
> $$\frac{3}{4} \cdot 5 = \frac{3 \cdot 5}{4} = \frac{15}{4}$$

---

## Gemischte Zahlen multiplizieren

Bei gemischten Zahlen: Erst in unechte Brüche umwandeln, dann multiplizieren.

**Beispiel:** $2\frac{1}{2} \cdot 1\frac{1}{3}$

$$= \frac{5}{2} \cdot \frac{4}{3} = \frac{20}{6} = \frac{10}{3} = 3\frac{1}{3}$$

> [!warning] **Häufiger Fehler**
> Man darf NICHT einfach Ganze mit Ganzen und Brüche mit Brüchen multiplizieren:
>
> **Falsch:** $2\frac{1}{2} \cdot 1\frac{1}{3} = 2 \cdot 1 + \frac{1}{2} \cdot \frac{1}{3} = 2\frac{1}{6}$ ✗
>
> **Richtig:** In unechte Brüche umwandeln → $\frac{5}{2} \cdot \frac{4}{3} = \frac{10}{3} = 3\frac{1}{3}$ ✓

---

## Das Ergebnis einschätzen

Bei der Multiplikation mit Brüchen gilt:
- Multiplikation mit echtem Bruch ($< 1$) → Ergebnis wird **kleiner**
- Multiplikation mit 1 → Ergebnis bleibt **gleich**
- Multiplikation mit unechtem Bruch ($> 1$) → Ergebnis wird **größer**

**Beispiel:** $\frac{3}{4} \cdot \frac{1}{2} = \frac{3}{8}$

$\frac{3}{8} < \frac{3}{4}$ ✓ (Das Ergebnis ist kleiner, weil wir mit $\frac{1}{2} < 1$ multipliziert haben)

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[10-Division-von-Bruechen|Division von Brüchen]] – Die Umkehroperation
- → [[05-Brueche-kuerzen|Brüche kürzen]] – Kreuzkürzen vor dem Multiplizieren
- → [[03-Gemischte-Zahlen|Gemischte Zahlen]] – Umwandlung vor dem Multiplizieren

> [!warning] **Prüfungsrelevant**
> - Zähler · Zähler, Nenner · Nenner
> - Kein gemeinsamer Nenner nötig
> - Vorher kürzen vereinfacht die Rechnung

> [!question] **Typische Prüfungsfragen**
> - Berechne: $\frac{5}{6} \cdot \frac{3}{10}$
> - Berechne: $2\frac{1}{2} \cdot \frac{4}{5}$

## Quellen

- Padberg, Friedhelm: *Didaktik der Bruchrechnung*. Springer, 2009.
