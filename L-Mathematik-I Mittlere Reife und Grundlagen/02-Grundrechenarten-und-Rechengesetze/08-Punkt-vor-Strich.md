---
author: Andreas Hümmer
title: Punkt-vor-Strich-Rechnung
status: draft - review pending
tags:
  - content
  - mathematik
  - rechengesetze
created: 2026-10-13
modified: 2026-10-16
---

# Punkt-vor-Strich-Rechnung

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Regel „Punkt vor Strich" sicher anwenden können
> - Wissen, warum diese Regel existiert
> - Ausdrücke ohne Klammern korrekt berechnen können

---

## Überblick

Die Regel „**Punkt vor Strich**" legt fest, dass Multiplikation und Division (Punktrechnung) vor Addition und Subtraktion (Strichrechnung) ausgeführt werden.

### Warum heißt es „Punkt vor Strich"?

Die Bezeichnung kommt von den Rechenzeichen: Der Malpunkt „$\cdot$" und der Doppelpunkt „$:$" sind **Punkt**-Zeichen, während Plus „$+$" und Minus „$-$" **Strich**-Zeichen sind. Diese einfache Eselsbrücke hilft, die Regel zu behalten.

### Historischer Hintergrund

Die Regel ist keine willkürliche Festlegung, sondern ergibt sich aus der Natur der Multiplikation als wiederholte Addition. Sie wurde im 17. Jahrhundert international standardisiert, um Missverständnisse zu vermeiden. Ohne diese Konvention müssten wir jeden Ausdruck vollständig klammern, was sehr umständlich wäre.

---

## Die Regel

| Priorität | Operation | Symbol |
|-----------|-----------|--------|
| Höher | Punktrechnung | $\cdot$ und $:$ |
| Niedriger | Strichrechnung | $+$ und $-$ |

**Regel:** Punktrechnung wird **vor** Strichrechnung ausgeführt.

---

## Beispiele

**Beispiel 1:** $3 + 4 \cdot 2$
$$= 3 + 8 = 11$$
(Nicht $14$, denn zuerst wird $4 \cdot 2$ berechnet!)

**Beispiel 2:** $20 - 12 : 4$
$$= 20 - 3 = 17$$

**Beispiel 3:** $2 + 3 \cdot 4 - 5$
$$= 2 + 12 - 5 = 9$$

**Beispiel 4:** $8 : 2 + 6 \cdot 3$
$$= 4 + 18 = 22$$

---

## Warum diese Regel?

Die Regel ergibt sich aus der Definition der Multiplikation als wiederholte Addition:

$3 + 4 \cdot 2$ bedeutet: $3 + (4 + 4)$

Das ist $3 + 8 = 11$, nicht $(3 + 4) + (3 + 4) = 14$.

> [!note] **Anschauliches Beispiel**
> „Ich habe 3 € und kaufe 4 Brötchen für je 2 €."
> 
> Richtig: $3 + 4 \cdot 2 = 3 + 8 = 11$ € (ich gebe 8 € für Brötchen aus, habe vorher 3 € → insgesamt 11 € sind im Spiel)
> 
> Falsch wäre: $(3 + 4) \cdot 2 = 14$ € (das würde bedeuten: 7 Dinge à 2 €)

Die „Punkt vor Strich"-Regel sorgt dafür, dass solche Alltagssituationen korrekt berechnet werden, ohne dass wir ständig Klammern setzen müssen.

---

## Klammern überschreiben die Regel

Klammern haben höchste Priorität und überschreiben „Punkt vor Strich":

**Mit Klammern:** $(3 + 4) \cdot 2 = 7 \cdot 2 = 14$

**Ohne Klammern:** $3 + 4 \cdot 2 = 3 + 8 = 11$

---

## Häufige Fehler

> [!warning] **Typische Fehler vermeiden**
> 
> **Falsch:** $5 + 3 \cdot 2 = 8 \cdot 2 = 16$
> **Richtig:** $5 + 3 \cdot 2 = 5 + 6 = 11$
>
> **Falsch:** $10 - 6 : 2 = 4 : 2 = 2$
> **Richtig:** $10 - 6 : 2 = 10 - 3 = 7$

---

## Zusammenhänge

- → [[09-Reihenfolge-der-Operationen|Reihenfolge der Operationen]] – Vollständige Hierarchie
- → [[10-Klammerregeln|Klammerregeln]] – Klammern überschreiben alles

> [!warning] **Prüfungsrelevant**
> - Punktrechnung (·, :) vor Strichrechnung (+, −)
> - Klammern haben höchste Priorität
> - Bei gleicher Priorität: von links nach rechts

> [!question] **Typische Prüfungsfragen**
> - Berechne: $8 + 4 \cdot 3 - 2$
> - Berechne: $24 : 6 + 2 \cdot 5$
> - Setze Klammern, sodass das Ergebnis 20 ist: $2 + 3 \cdot 4$

## Quellen

- Padberg, Friedhelm: *Didaktik der Arithmetik*. Springer, 2017.
