---
author: Andreas Hümmer
title: Division von Brüchen
status: draft - review pending
tags:
  - content
  - mathematik
  - bruchrechnung
created: 2026-10-13
modified: 2026-10-16
---

# Division von Brüchen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Brüche durcheinander dividieren können
> - Die Regel „mit dem Kehrwert multiplizieren" anwenden
> - Den Kehrwert eines Bruchs bilden können

---

## Überblick

Division durch einen Bruch bedeutet: **mit dem Kehrwert multiplizieren**. Dies verwandelt jede Bruchdivision in eine Multiplikation, die wir bereits beherrschen.

Diese Regel erscheint auf den ersten Blick wie Zauberei, ist aber mathematisch gut begründet. Die Grundidee: Division ist die Umkehrung der Multiplikation. Wenn Multiplizieren mit $\frac{1}{2}$ „halbieren" bedeutet, dann muss Dividieren durch $\frac{1}{2}$ „verdoppeln" bedeuten – und das entspricht der Multiplikation mit 2 (dem Kehrwert von $\frac{1}{2}$).

---

## Kehrwert

Der **Kehrwert** (auch: Reziproke oder Inverses) eines Bruchs entsteht durch Vertauschen von Zähler und Nenner:

$$\text{Kehrwert von } \frac{a}{b} = \frac{b}{a}$$

| Bruch | Kehrwert |
|-------|----------|
| $\frac{2}{3}$ | $\frac{3}{2}$ |
| $\frac{5}{7}$ | $\frac{7}{5}$ |
| $4 = \frac{4}{1}$ | $\frac{1}{4}$ |
| $\frac{1}{8}$ | $\frac{8}{1} = 8$ |

> [!note] **Eigenschaft des Kehrwerts**
> Ein Bruch mal seinem Kehrwert ergibt immer 1:
> $$\frac{a}{b} \cdot \frac{b}{a} = \frac{a \cdot b}{b \cdot a} = 1$$
>
> Das ist wie Hin- und Rückweg: Wenn du zuerst mit $\frac{2}{3}$ multiplizierst und dann mit $\frac{3}{2}$, bist du wieder beim Ausgangswert.

> [!warning] **Null hat keinen Kehrwert**
> Der Kehrwert von 0 existiert nicht, denn $\frac{1}{0}$ ist nicht definiert.
> Deshalb ist auch Division durch 0 verboten!

---

## Regel

$$\frac{a}{b} : \frac{c}{d} = \frac{a}{b} \cdot \frac{d}{c}$$

**Merksatz:** „Dividieren durch einen Bruch = Multiplizieren mit dem Kehrwert"

> [!tip] **Eselsbrücke**
> „Bruch durch Bruch – stürz' und mal!" (Kehrwert bilden = „stürzen" des zweiten Bruchs)

**Beispiel:**
$$\frac{3}{4} : \frac{2}{5} = \frac{3}{4} \cdot \frac{5}{2} = \frac{15}{8} = 1\frac{7}{8}$$

---

## Anschauliche Erklärung

Die Frage $\frac{1}{2} : \frac{1}{4}$ bedeutet: „Wie oft passt $\frac{1}{4}$ in $\frac{1}{2}$?"

```
    1/2:    ┌───────────┬───────────┐
            │    ▓▓▓    │           │
            │    ▓▓▓    │           │
            └───────────┴───────────┘
            
    1/4:    ┌─────┬─────┬─────┬─────┐
            │  ▓  │     │     │     │
            │  ▓  │     │     │     │
            └─────┴─────┴─────┴─────┘
            
    Antwort: 2 mal → 1/2 : 1/4 = 2
```

Ein Halbes enthält zwei Viertel. Daher: $\frac{1}{2} : \frac{1}{4} = 2$

Mit der Regel: $\frac{1}{2} : \frac{1}{4} = \frac{1}{2} \cdot \frac{4}{1} = \frac{4}{2} = 2$ ✓

> [!note] **Warum wird das Ergebnis größer?**
> Division durch einen echten Bruch ($< 1$) ergibt ein **größeres** Ergebnis!
> 
> Das ist zunächst verwirrend, aber logisch: „Wie oft passt ein kleines Stück in ein größeres?" – Je kleiner das Stück, desto öfter passt es hinein.
>
> $6 : 2 = 3$ (Sechs enthält drei Zweier)
> $6 : \frac{1}{2} = 12$ (Sechs enthält zwölf Halbe)

---

## Beispiele

| Rechnung | Umwandlung | Ergebnis |
|----------|------------|----------|
| $\frac{2}{3} : \frac{4}{5}$ | $\frac{2}{3} \cdot \frac{5}{4}$ | $\frac{10}{12} = \frac{5}{6}$ |
| $\frac{5}{6} : 2$ | $\frac{5}{6} \cdot \frac{1}{2}$ | $\frac{5}{12}$ |
| $3 : \frac{1}{4}$ | $3 \cdot 4$ | $12$ |

### Division durch ganze Zahl

$$\frac{5}{6} : 2 = \frac{5}{6} \cdot \frac{1}{2} = \frac{5}{12}$$

> [!tip] **Schneller Weg**
> Bruch durch ganze Zahl: Multipliziere den Nenner mit der ganzen Zahl.
> $\frac{5}{6} : 2 = \frac{5}{6 \cdot 2} = \frac{5}{12}$

### Ganze Zahl durch Bruch

$$3 : \frac{1}{4} = 3 \cdot 4 = 12$$

„Wie viele Viertel passen in 3?" – In jedes Ganze passen 4 Viertel, also in 3 Ganze: 12 Viertel.

---

## Kehrwert von gemischten Zahlen

Um den Kehrwert einer gemischten Zahl zu bilden, wandle sie zuerst in einen unechten Bruch um:

**Beispiel:** Kehrwert von $2\frac{1}{3}$

1. In unechten Bruch umwandeln: $2\frac{1}{3} = \frac{7}{3}$
2. Kehrwert bilden: $\frac{3}{7}$

> [!warning] **Häufiger Fehler**
> Den Kehrwert einer gemischten Zahl NICHT so bilden:
>
> **Falsch:** Kehrwert von $2\frac{1}{3}$ = $\frac{1}{2}\frac{3}{1}$ = ??? ✗
>
> **Richtig:** $2\frac{1}{3} = \frac{7}{3}$ → Kehrwert = $\frac{3}{7}$ ✓

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[09-Multiplikation-von-Bruechen|Multiplikation von Brüchen]] – Nach der Umwandlung multiplizieren
- → [[05-Brueche-kuerzen|Brüche kürzen]] – Auch bei Division kürzen möglich
- → [[03-Gemischte-Zahlen|Gemischte Zahlen]] – Umwandlung für Kehrwert

> [!warning] **Prüfungsrelevant**
> - Kehrwert: Zähler und Nenner vertauschen
> - Division = Multiplikation mit Kehrwert
> - Division durch Null ist verboten (Kehrwert von 0 existiert nicht)

> [!question] **Typische Prüfungsfragen**
> - Berechne: $\frac{5}{8} : \frac{3}{4}$
> - Was ist der Kehrwert von $2\frac{1}{3}$?

## Quellen

- Padberg, Friedhelm: *Didaktik der Bruchrechnung*. Springer, 2009.
