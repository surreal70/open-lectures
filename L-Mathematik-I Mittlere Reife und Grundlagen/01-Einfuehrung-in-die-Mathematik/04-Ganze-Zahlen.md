---
author: Open Lectures
title: Ganze Zahlen
status: draft - review pending
tags:
  - content
  - mathematik
  - zahlenmengen
  - ganze-zahlen
created: 2026-10-13
modified: 2026-10-13
---

# Ganze Zahlen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Menge der ganzen Zahlen $\mathbb{Z}$ definieren können
> - Verstehen, warum negative Zahlen eingeführt wurden
> - Ganze Zahlen auf dem Zahlenstrahl darstellen können
> - Die Beziehung zwischen $\mathbb{N}$ und $\mathbb{Z}$ kennen

---

## Überblick

Die ganzen Zahlen erweitern die natürlichen Zahlen um die Null und die negativen Zahlen. Diese Erweiterung war notwendig, um Subtraktionen wie $3 - 5$ durchführen zu können, die in den natürlichen Zahlen kein Ergebnis haben. Im Alltag begegnen uns negative Zahlen etwa bei Temperaturen unter null oder bei Schulden.

---

## Definition der ganzen Zahlen

Die **ganzen Zahlen** umfassen die natürlichen Zahlen, die Null und die negativen Zahlen:

$$\mathbb{Z} = \{\ldots, -3, -2, -1, 0, 1, 2, 3, \ldots\}$$

Das Symbol $\mathbb{Z}$ kommt vom deutschen Wort „Zahlen".

### Bestandteile von $\mathbb{Z}$

| Teilmenge | Notation | Elemente |
|-----------|----------|----------|
| Positive ganze Zahlen | $\mathbb{Z}^+$ | $1, 2, 3, 4, \ldots$ |
| Negative ganze Zahlen | $\mathbb{Z}^-$ | $-1, -2, -3, -4, \ldots$ |
| Die Null | — | $0$ |

> [!note] **Beziehung zu $\mathbb{N}$**
> Die natürlichen Zahlen sind eine Teilmenge der ganzen Zahlen:
> $$\mathbb{N} \subset \mathbb{Z}$$
> Jede natürliche Zahl ist auch eine ganze Zahl, aber nicht umgekehrt.

---

## Warum brauchen wir negative Zahlen?

### Motivation: Subtraktion

In den natürlichen Zahlen ist nicht jede Subtraktion möglich:

| Rechnung | Ergebnis in $\mathbb{N}$? | Ergebnis in $\mathbb{Z}$ |
|----------|---------------------------|--------------------------|
| $7 - 3$ | ✓ Ja: $4$ | $4$ |
| $5 - 5$ | ✗ Nein (0 ∉ $\mathbb{N}$) | $0$ |
| $3 - 7$ | ✗ Nein | $-4$ |

Mit den ganzen Zahlen ist die Subtraktion **immer möglich**.

### Alltagsbeispiele

Negative Zahlen begegnen uns täglich:

- **Temperatur**: $-5°C$ bedeutet 5 Grad unter dem Gefrierpunkt
- **Kontostand**: $-200€$ bedeutet 200 Euro Schulden
- **Höhe**: $-50m$ bedeutet 50 Meter unter dem Meeresspiegel
- **Geschichte**: Das Jahr $-500$ bezeichnet 500 v. Chr.

---

## Darstellung auf dem Zahlenstrahl

Die ganzen Zahlen liegen auf einem **Zahlenstrahl**, der in beide Richtungen unendlich ist:

```
    ←──┬────┬────┬────┬────┬────┬────┬────┬────┬────┬──→
      -4   -3   -2   -1    0    1    2    3    4    5
                         
       negative Zahlen    │    positive Zahlen
                          ↑
                        Null
```

### Eigenschaften der Darstellung

- Die **Null** liegt in der Mitte und trennt positive von negativen Zahlen
- **Positive Zahlen** liegen rechts von der Null
- **Negative Zahlen** liegen links von der Null
- Je weiter rechts, desto **größer** die Zahl
- Je weiter links, desto **kleiner** die Zahl

---

## Ordnung der ganzen Zahlen

### Vergleichen von ganzen Zahlen

| Regel | Beispiel |
|-------|----------|
| Jede positive Zahl ist größer als Null | $5 > 0$ |
| Jede negative Zahl ist kleiner als Null | $-3 < 0$ |
| Jede positive Zahl ist größer als jede negative | $1 > -100$ |
| Bei negativen Zahlen: Je größer der Betrag, desto kleiner die Zahl | $-2 > -5$ |

**Beispiele zur Ordnung:**

$$-5 < -3 < -1 < 0 < 2 < 7$$

> [!tip] **Merkregel**
> Auf dem Zahlenstrahl gilt: Die Zahl, die weiter **rechts** liegt, ist die **größere**.

---

## Gegenzahl (Oppositzahl)

Zu jeder ganzen Zahl gibt es eine **Gegenzahl**:

| Zahl $a$ | Gegenzahl $-a$ |
|----------|----------------|
| $5$ | $-5$ |
| $-3$ | $-(-3) = 3$ |
| $0$ | $0$ |

### Eigenschaften der Gegenzahl

- Die Summe einer Zahl und ihrer Gegenzahl ist Null: $a + (-a) = 0$
- Auf dem Zahlenstrahl liegen Zahl und Gegenzahl symmetrisch zur Null
- Die Gegenzahl der Gegenzahl ist die ursprüngliche Zahl: $-(-a) = a$

---

## Rechenoperationen in $\mathbb{Z}$

### Abgeschlossenheit

| Operation | Abgeschlossen in $\mathbb{Z}$? | Begründung |
|-----------|--------------------------------|------------|
| Addition | ✓ Ja | $(-3) + 5 = 2 \in \mathbb{Z}$ |
| Subtraktion | ✓ Ja | $3 - 7 = -4 \in \mathbb{Z}$ |
| Multiplikation | ✓ Ja | $(-2) \cdot 3 = -6 \in \mathbb{Z}$ |
| Division | ✗ Nein | $5 : 2 = 2{,}5 \notin \mathbb{Z}$ |

> [!note] **Fortschritt gegenüber $\mathbb{N}$**
> In $\mathbb{Z}$ ist nun auch die Subtraktion immer möglich! Für die Division brauchen wir aber eine weitere Erweiterung → rationale Zahlen.

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[03-Natuerliche-Zahlen|Natürliche Zahlen]] – Die Grundlage: $\mathbb{N} \subset \mathbb{Z}$
- → [[08-Positive-und-negative-Zahlen|Positive und negative Zahlen]] – Rechnen mit Vorzeichen
- → [[09-Betrag-einer-Zahl|Betrag einer Zahl]] – Abstand zur Null
- → [[05-Rationale-Zahlen|Rationale Zahlen]] – Nächste Erweiterung: $\mathbb{Z} \subset \mathbb{Q}$

> [!warning] **Prüfungsrelevant**
> - Definition: $\mathbb{Z} = \{\ldots, -2, -1, 0, 1, 2, \ldots\}$
> - $\mathbb{N} \subset \mathbb{Z}$ (natürliche Zahlen sind Teilmenge)
> - Gegenzahl: $a + (-a) = 0$
> - In $\mathbb{Z}$ ist Subtraktion immer möglich, Division nicht

> [!question] **Typische Prüfungsfragen**
> - Ordne der Größe nach: $-7, 3, -2, 0, -1$
> - Was ist die Gegenzahl von $-8$?
> - Warum ist $-3 > -5$?
> - Gib ein Beispiel, bei dem die Division in $\mathbb{Z}$ nicht abgeschlossen ist.

## Quellen

- Scheid, Harald; Schwarz, Wolfgang: *Elemente der Arithmetik und Algebra*. Springer, 2016.
- Beutelspacher, Albrecht: *Zahlen*. Rowohlt, 2013.

> [!tip] **Weiterführende Links**
> - [Mathebibel: Ganze Zahlen](https://www.mathebibel.de/ganze-zahlen)
> - [[05-Rationale-Zahlen|Nächstes Kapitel: Rationale Zahlen]]
