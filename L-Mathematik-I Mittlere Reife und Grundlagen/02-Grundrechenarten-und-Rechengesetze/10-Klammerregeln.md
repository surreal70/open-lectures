---
author: Andreas Hümmer
title: Klammerregeln
status: final
tags:
  - content
  - mathematik
  - rechengesetze
created: 2026-10-13
modified: 2026-10-16
---

# Klammerregeln

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Verschiedene Klammerarten kennen
> - Klammern korrekt auflösen können
> - Besonders das Minus vor der Klammer beherrschen

---

## Überblick

Klammern gruppieren Rechenausdrücke und bestimmen die Reihenfolge der Berechnung. Das Auflösen von Klammern folgt bestimmten Regeln, besonders wenn ein Vorzeichen vor der Klammer steht.

### Warum gibt es Klammern?

Klammern sind wie Regieanweisungen in der Mathematik: Sie sagen uns, was zuerst berechnet werden soll. Ohne Klammern müssten wir uns strikt an die „Punkt vor Strich"-Regel halten. Mit Klammern können wir diese Reihenfolge überschreiben.

Im Alltag nutzen wir Klammern ständig, auch wenn wir sie nicht immer aufschreiben: „Ich kaufe 3 Äpfel und 2 Birnen, jeweils für 50 Cent" bedeutet mathematisch $(3 + 2) \cdot 0{,}50$ €.

### Historischer Hintergrund

Klammern wurden erst im 16. Jahrhundert in die mathematische Notation eingeführt. Davor mussten Mathematiker komplizierte Ausdrücke umständlich in Worten beschreiben. Die Einführung von Klammern war ein großer Fortschritt für die Übersichtlichkeit mathematischer Texte.

---

## Arten von Klammern

| Klammer | Name | Verwendung |
|---------|------|------------|
| $( \quad )$ | Runde Klammern | Innerste Klammern |
| $[ \quad ]$ | Eckige Klammern | Mittlere Ebene |
| $\{ \quad \}$ | Geschweifte Klammern | Äußerste Ebene / Mengen |

Bei verschachtelten Klammern: **von innen nach außen** auflösen.

---

## Plus vor der Klammer

Das Pluszeichen vor einer Klammer kann weggelassen werden – die Vorzeichen in der Klammer bleiben unverändert:

$$+(a + b) = a + b$$
$$+(a - b) = a - b$$

**Beispiel:**
$$5 + (3 - 2) = 5 + 3 - 2 = 6$$

---

## Minus vor der Klammer

> [!warning] **Wichtig**
> Ein Minus vor der Klammer **kehrt alle Vorzeichen in der Klammer um**!

$$-(a + b) = -a - b$$
$$-(a - b) = -a + b$$

**Beispiele:**

$$7 - (3 + 2) = 7 - 3 - 2 = 2$$
$$10 - (8 - 5) = 10 - 8 + 5 = 7$$
$$-(−4 + 3) = +4 - 3 = 1$$

> [!note] **Warum werden alle Vorzeichen umgekehrt?**
> Das Minuszeichen vor der Klammer bedeutet „das Gegenteil von allem in der Klammer". Wenn in der Klammer „$+3$" steht, wird daraus „$-3$". Wenn „$-5$" steht, wird daraus „$+5$".
> 
> Mathematisch: $-(a + b) = (-1) \cdot (a + b) = (-1) \cdot a + (-1) \cdot b = -a - b$

> [!tip] **Strategie: Vorzeichen systematisch ändern**
> Gehe Term für Term durch und ändere jedes Vorzeichen:
> - $-(+3 - 7 + 2)$ wird zu $-3 + 7 - 2$
> - Plus wird Minus, Minus wird Plus

---

## Faktor vor der Klammer

Ein Faktor vor der Klammer wird mit jedem Term in der Klammer multipliziert (Distributivgesetz):

$$a \cdot (b + c) = a \cdot b + a \cdot c$$

**Beispiele:**

$$3 \cdot (4 + 5) = 12 + 15 = 27$$
$$-2 \cdot (3 - 7) = -6 + 14 = 8$$

---

## Verschachtelte Klammern

Von innen nach außen auflösen:

**Beispiel:** $5 - [3 + (2 - 4)]$

$$= 5 - [3 + (-2)]$$
$$= 5 - [1]$$
$$= 5 - 1 = 4$$

---

## Häufige Fehler

> [!warning] **Typische Fehler vermeiden**
>
> **Fehler 1:** $10 - (3 + 2) = 10 - 3 + 2 = 9$ ✗
> **Richtig:** $10 - (3 + 2) = 10 - 3 - 2 = 5$ ✓
>
> **Fehler 2:** $-(x - 3) = -x - 3$ ✗
> **Richtig:** $-(x - 3) = -x + 3$ ✓

---

## Zusammenhänge

- → [[07-Distributivgesetz|Distributivgesetz]]
- → [[09-Reihenfolge-der-Operationen|Reihenfolge der Operationen]]

> [!warning] **Prüfungsrelevant**
> - Minus vor Klammer kehrt alle Vorzeichen um
> - Verschachtelte Klammern: von innen nach außen
> - Faktor vor Klammer: ausmultiplizieren

> [!question] **Typische Prüfungsfragen**
> - Löse die Klammer auf: $8 - (5 - 3)$
> - Vereinfache: $-2 \cdot (x - 4)$
> - Berechne: $12 - [7 - (3 + 1)]$

## Quellen

- Padberg, Friedhelm: *Didaktik der Arithmetik*. Springer, 2017.
