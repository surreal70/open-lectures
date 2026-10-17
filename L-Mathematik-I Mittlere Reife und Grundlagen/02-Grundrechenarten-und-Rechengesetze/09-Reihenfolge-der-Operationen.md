---
author: Andreas Hümmer
title: Reihenfolge von Rechenoperationen
status: draft - review pending
tags:
  - content
  - mathematik
  - rechengesetze
created: 2026-10-13
modified: 2026-10-16
---

# Reihenfolge von Rechenoperationen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die vollständige Hierarchie der Rechenoperationen kennen
> - Komplexe Ausdrücke in der richtigen Reihenfolge berechnen
> - Die Regel „von links nach rechts" bei gleicher Priorität anwenden

---

## Überblick

Bei komplexen Rechenausdrücken mit mehreren Operationen muss eine eindeutige Reihenfolge eingehalten werden. Diese Hierarchie ist international standardisiert.

### Warum brauchen wir eine feste Reihenfolge?

Ohne klare Regeln wäre der Ausdruck $2 + 3 \cdot 4$ mehrdeutig: Ist das Ergebnis $20$ (erst addieren, dann multiplizieren) oder $14$ (erst multiplizieren, dann addieren)? Die international vereinbarte Prioritätsreihenfolge sorgt dafür, dass jeder Mathematiker auf der Welt zum selben Ergebnis kommt. Auch Computer und Taschenrechner folgen diesen Regeln.

### Die Regel im englischsprachigen Raum: PEMDAS/BODMAS

Im englischen Sprachraum gibt es die Merkregel **PEMDAS** (USA) oder **BODMAS** (UK):
- **P**arentheses / **B**rackets (Klammern)
- **E**xponents / **O**rder (Potenzen)
- **M**ultiplication & **D**ivision (von links nach rechts)
- **A**ddition & **S**ubtraction (von links nach rechts)

---

## Die Prioritätsreihenfolge

| Priorität | Operation | Beispiel |
|-----------|-----------|----------|
| 1 (höchste) | Klammern | $(3 + 2)$ zuerst |
| 2 | Potenzen | $2^3$ vor $\cdot$ |
| 3 | Punkt ($\cdot$, $:$) | $4 \cdot 5$ vor $+$ |
| 4 (niedrigste) | Strich ($+$, $-$) | Zuletzt |

> [!tip] **Merkregel: KLAPS**
> **KL**ammern → **A**lles hoch (Potenzen) → **P**unkt → **S**trich

---

## Bei gleicher Priorität

Operationen gleicher Priorität werden **von links nach rechts** ausgeführt:

**Beispiel 1:** $20 - 5 + 3$
$$= 15 + 3 = 18$$

**Beispiel 2:** $24 : 4 : 2$
$$= 6 : 2 = 3$$

**Beispiel 3:** $2^{3^2}$
Bei Potenzen: von rechts nach links (Ausnahme!)
$$= 2^9 = 512$$

---

## Komplexe Beispiele

**Beispiel 1:** $3 + 4 \cdot 2^2$
$$= 3 + 4 \cdot 4 = 3 + 16 = 19$$

**Beispiel 2:** $(3 + 4) \cdot 2^2$
$$= 7 \cdot 4 = 28$$

**Beispiel 3:** $2 + 3 \cdot (4 + 5) - 6 : 2$
$$= 2 + 3 \cdot 9 - 3 = 2 + 27 - 3 = 26$$

**Beispiel 4:** $\frac{12 + 8}{4} + 3$
$$= \frac{20}{4} + 3 = 5 + 3 = 8$$
(Der Bruchstrich wirkt wie eine Klammer!)

---

## Bruchstriche und Wurzeln

Bruchstriche und Wurzelzeichen sind „unsichtbare Klammern" – sie fassen alles zusammen, was unter bzw. über ihnen steht.

- **Bruchstrich:** Zähler und Nenner zuerst vollständig berechnen
- **Wurzel:** Ausdruck unter der Wurzel zuerst berechnen

**Beispiel:** $\sqrt{9 + 16}$
$$= \sqrt{25} = 5$$
(Nicht $\sqrt{9} + \sqrt{16} = 3 + 4 = 7$!)

> [!warning] **Häufiger Fehler**
> Die Wurzel darf **nicht** auf einzelne Summanden aufgeteilt werden:
> - $\sqrt{a + b} \neq \sqrt{a} + \sqrt{b}$
> - $\sqrt{9 + 16} = \sqrt{25} = 5$, aber $\sqrt{9} + \sqrt{16} = 3 + 4 = 7$
> 
> Dasselbe gilt für Brüche: $\frac{a + b}{c} = \frac{a}{c} + \frac{b}{c}$ (das geht), aber $\frac{a}{b + c} \neq \frac{a}{b} + \frac{a}{c}$ (das geht nicht!)

> [!tip] **Merkregel für Bruchstriche**
> Der Bruchstrich wirkt wie eine große Klammer um Zähler und Nenner. Berechne immer erst oben und unten komplett, bevor du teilst.

---

## Zusammenhänge

- → [[08-Punkt-vor-Strich|Punkt vor Strich]]
- → [[10-Klammerregeln|Klammerregeln]]

> [!warning] **Prüfungsrelevant**
> - Reihenfolge: Klammer → Potenz → Punkt → Strich
> - Bei gleicher Priorität: von links nach rechts
> - Bruchstrich und Wurzelzeichen wirken wie Klammern

> [!question] **Typische Prüfungsfragen**
> - Berechne: $5 + 2^3 \cdot 3 - 4$
> - Berechne: $\frac{8 + 4}{3} \cdot 2$
> - In welcher Reihenfolge wird berechnet: $a + b \cdot c^2$?

## Quellen

- Padberg, Friedhelm: *Didaktik der Arithmetik*. Springer, 2017.
