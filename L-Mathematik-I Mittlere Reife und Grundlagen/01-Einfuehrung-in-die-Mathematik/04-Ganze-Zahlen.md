---
author: Open Lectures
title: Ganze Zahlen
status: final
tags:
  - content
  - mathematik
  - zahlenmengen
  - ganze-zahlen
created: 2026-10-13
modified: 2026-10-16
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

Die Einführung negativer Zahlen war historisch ein langer Prozess. Noch im 17. Jahrhundert bezeichneten einige Mathematiker negative Zahlen als „absurd" oder „falsch". Erst allmählich setzte sich die Erkenntnis durch, dass negative Zahlen mathematisch sinnvoll und praktisch nützlich sind. Heute sind sie aus der Mathematik nicht mehr wegzudenken.

---

## Definition der ganzen Zahlen

Die **ganzen Zahlen** umfassen die natürlichen Zahlen, die Null und die negativen Zahlen:

$$\mathbb{Z} = \{\ldots, -3, -2, -1, 0, 1, 2, 3, \ldots\}$$

Das Symbol $\mathbb{Z}$ kommt vom deutschen Wort „Zahlen". Die drei Punkte auf beiden Seiten bedeuten, dass die Menge in beide Richtungen unendlich weitergeht – es gibt keine größte und keine kleinste ganze Zahl.

### Bestandteile von $\mathbb{Z}$

Die ganzen Zahlen lassen sich in drei disjunkte (sich nicht überschneidende) Gruppen einteilen:

| Teilmenge | Notation | Elemente | Beschreibung |
|-----------|----------|----------|--------------|
| Positive ganze Zahlen | $\mathbb{Z}^+$ | $1, 2, 3, 4, \ldots$ | Entsprechen den natürlichen Zahlen |
| Negative ganze Zahlen | $\mathbb{Z}^-$ | $-1, -2, -3, -4, \ldots$ | Zahlen kleiner als Null |
| Die Null | — | $0$ | Weder positiv noch negativ |

> [!note] **Beziehung zu $\mathbb{N}$**
> Die natürlichen Zahlen sind eine Teilmenge der ganzen Zahlen:
> $$\mathbb{N} \subset \mathbb{Z}$$
> Jede natürliche Zahl ist auch eine ganze Zahl, aber nicht umgekehrt. Die Zahl $-3$ ist eine ganze Zahl, aber keine natürliche Zahl.

---

## Warum brauchen wir negative Zahlen?

### Motivation: Subtraktion ohne Einschränkungen

In den natürlichen Zahlen ist nicht jede Subtraktion möglich. Man kann nur dann $a - b$ berechnen, wenn $a \geq b$ ist:

| Rechnung | Ergebnis in $\mathbb{N}$? | Ergebnis in $\mathbb{Z}$ | Erklärung |
|----------|---------------------------|--------------------------|-----------|
| $7 - 3$ | ✓ Ja: $4$ | $4$ | Geht auch in $\mathbb{N}$ |
| $5 - 5$ | ✗ Nein (0 ∉ $\mathbb{N}$) | $0$ | Null liegt nicht in $\mathbb{N}$ |
| $3 - 7$ | ✗ Nein | $-4$ | Negatives Ergebnis |

Mit den ganzen Zahlen ist die Subtraktion **immer möglich**: Für beliebige ganze Zahlen $a$ und $b$ existiert stets ein eindeutiges Ergebnis $a - b \in \mathbb{Z}$. Diese Eigenschaft nennt man **Abgeschlossenheit** bezüglich der Subtraktion.

### Alltagsbeispiele für negative Zahlen

Negative Zahlen begegnen uns im Alltag häufiger, als wir vielleicht denken:

| Bereich | Beispiel | Bedeutung |
|---------|----------|-----------|
| **Temperatur** | $-5°C$ | 5 Grad unter dem Gefrierpunkt – es ist kalt genug, dass Wasser gefriert |
| **Kontostand** | $-200€$ | 200 Euro Schulden – das Konto ist „im Minus" |
| **Höhe** | $-50m$ | 50 Meter unter dem Meeresspiegel (z.B. Totes Meer: $-430m$) |
| **Geschichte** | Das Jahr $-500$ | Das Jahr 500 v. Chr. (vor Christus) |
| **Fahrstuhl** | Etage $-2$ | Zwei Stockwerke unter dem Erdgeschoss (Tiefgarage) |
| **Spielstand** | $-3$ Punkte | 3 Minuspunkte (z.B. bei Kartenspielen) |

Diese Beispiele zeigen: Negative Zahlen beschreiben Situationen, in denen etwas „weniger als nichts" ist oder in die entgegengesetzte Richtung geht.

---

## Darstellung auf dem Zahlenstrahl

Die ganzen Zahlen liegen auf einem **Zahlenstrahl**, der in beide Richtungen unendlich ist:

![[zahlenstrahl-ganze.png]]
*<span class="fig-id">01-01-04-zahlenstrahl-ganze</span>: Zahlenstrahl der ganzen Zahlen ℤ. Die Null trennt die negativen Zahlen (links) von den positiven (rechts); der Strahl setzt sich in beide Richtungen unbegrenzt fort (Pfeile).*

### Eigenschaften der Darstellung

| Aspekt | Beschreibung |
|--------|--------------|
| **Position der Null** | Die Null liegt in der Mitte und trennt positive von negativen Zahlen |
| **Positive Zahlen** | Liegen rechts von der Null |
| **Negative Zahlen** | Liegen links von der Null |
| **Ordnungsprinzip** | Je weiter rechts, desto größer die Zahl; je weiter links, desto kleiner |
| **Abstände** | Der Abstand zwischen benachbarten Zahlen ist überall gleich |
| **Symmetrie** | Jede positive Zahl hat ein „Spiegelbild" auf der negativen Seite |

Der Zahlenstrahl macht deutlich, dass die ganzen Zahlen eine natürliche Erweiterung der natürlichen Zahlen sind: Man verlängert den Strahl einfach nach links über die Null hinaus.

---

## Ordnung der ganzen Zahlen

Das Vergleichen ganzer Zahlen folgt klaren Regeln, die sich anschaulich auf dem Zahlenstrahl ablesen lassen.

### Regeln zum Vergleichen von ganzen Zahlen

| Regel | Beispiel | Begründung (auf dem Zahlenstrahl) |
|-------|----------|-----------------------------------|
| Jede positive Zahl ist größer als Null | $5 > 0$ | 5 liegt rechts von 0 |
| Jede negative Zahl ist kleiner als Null | $-3 < 0$ | -3 liegt links von 0 |
| Jede positive Zahl ist größer als jede negative | $1 > -100$ | Positive Zahlen liegen immer rechts von negativen |
| Bei negativen Zahlen: Je größer der Betrag, desto kleiner die Zahl | $-2 > -5$ | -2 liegt rechts von -5 |

**Beispiele zur Ordnung:**

$$-5 < -3 < -1 < 0 < 2 < 7$$

Diese Reihenfolge entspricht der Position auf dem Zahlenstrahl von links nach rechts.

> [!tip] **Merkregel für negative Zahlen**
> Bei negativen Zahlen kann das Vergleichen zunächst verwirrend sein. Denke an Schulden:
> - Wer $2€$ Schulden hat, ist „reicher" als jemand mit $5€$ Schulden
> - Also: $-2 > -5$
>
> Oder denke an Temperaturen:
> - $-2°C$ ist wärmer als $-5°C$
> - Also: $-2 > -5$

---

## Gegenzahl (Oppositzahl)

Zu jeder ganzen Zahl gibt es eine **Gegenzahl** (auch Oppositzahl genannt). Die Gegenzahl entsteht durch Vorzeichenwechsel:

| Zahl $a$ | Gegenzahl $-a$ | Auf dem Zahlenstrahl |
|----------|----------------|----------------------|
| $5$ | $-5$ | Spiegelbild links von 0 |
| $-3$ | $-(-3) = 3$ | Spiegelbild rechts von 0 |
| $0$ | $0$ | Null ist ihre eigene Gegenzahl |

### Eigenschaften der Gegenzahl

Die Gegenzahl hat besondere mathematische Eigenschaften:

- **Summe ist Null:** Die Summe einer Zahl und ihrer Gegenzahl ist immer Null:
  $$a + (-a) = 0$$
  Beispiel: $5 + (-5) = 0$

- **Symmetrie zur Null:** Auf dem Zahlenstrahl liegen Zahl und Gegenzahl symmetrisch zur Null, also im gleichen Abstand von der Null

- **Doppelte Negation:** Die Gegenzahl der Gegenzahl ist die ursprüngliche Zahl:
  $$-(-a) = a$$
  Beispiel: $-(-7) = 7$

> [!note] **Anschauliche Bedeutung**
> Die Gegenzahl beschreibt die „entgegengesetzte Richtung": Wenn $+5$ für „5 Schritte nach rechts" steht, dann steht $-5$ für „5 Schritte nach links". Zusammen ergeben sie null Schritte.

---

## Rechenoperationen in $\mathbb{Z}$

### Abgeschlossenheit

Eine wichtige Frage bei Zahlenmengen: Liegt das Ergebnis einer Operation wieder in derselben Menge?

| Operation | Abgeschlossen in $\mathbb{Z}$? | Begründung | Beispiel |
|-----------|--------------------------------|------------|----------|
| Addition | ✓ Ja | Summe zweier ganzer Zahlen ist immer ganz | $(-3) + 5 = 2 \in \mathbb{Z}$ |
| Subtraktion | ✓ Ja | Differenz zweier ganzer Zahlen ist immer ganz | $3 - 7 = -4 \in \mathbb{Z}$ |
| Multiplikation | ✓ Ja | Produkt zweier ganzer Zahlen ist immer ganz | $(-2) \cdot 3 = -6 \in \mathbb{Z}$ |
| Division | ✗ Nein | Quotient kann ein Bruch sein | $5 : 2 = 2{,}5 \notin \mathbb{Z}$ |

> [!note] **Fortschritt gegenüber $\mathbb{N}$**
> In $\mathbb{Z}$ ist nun auch die Subtraktion immer möglich! Das war die Hauptmotivation für die Einführung negativer Zahlen. 
>
> Für die Division brauchen wir allerdings eine weitere Erweiterung: Die **rationalen Zahlen** $\mathbb{Q}$ erlauben es, auch $5 : 2$ als Ergebnis darzustellen.

### Vorzeichenregeln bei Multiplikation

Beim Multiplizieren mit negativen Zahlen gelten besondere Regeln:

| Faktoren | Ergebnis | Beispiel | Merkspruch |
|----------|----------|----------|------------|
| $(+) \cdot (+)$ | $+$ (positiv) | $3 \cdot 4 = 12$ | Plus mal Plus ist Plus |
| $(+) \cdot (-)$ | $-$ (negativ) | $3 \cdot (-4) = -12$ | Plus mal Minus ist Minus |
| $(-) \cdot (+)$ | $-$ (negativ) | $(-3) \cdot 4 = -12$ | Minus mal Plus ist Minus |
| $(-) \cdot (-)$ | $+$ (positiv) | $(-3) \cdot (-4) = 12$ | Minus mal Minus ist Plus |

> [!tip] **Kurzregel für Vorzeichen**
> - **Gleiche** Vorzeichen → Ergebnis **positiv**
> - **Verschiedene** Vorzeichen → Ergebnis **negativ**

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
> - Gegenzahl: $a + (-a) = 0$ und $-(-a) = a$
> - In $\mathbb{Z}$ ist Subtraktion immer möglich, Division nicht
> - Vorzeichenregeln: gleiche Vorzeichen → positiv, verschiedene → negativ

> [!question] **Typische Prüfungsfragen**
> - Ordne der Größe nach: $-7, 3, -2, 0, -1$
> - Was ist die Gegenzahl von $-8$?
> - Warum ist $-3 > -5$?
> - Berechne: $(-4) \cdot (-3)$
> - Gib ein Beispiel, bei dem die Division in $\mathbb{Z}$ nicht abgeschlossen ist.

## Quellen

- Scheid, Harald; Schwarz, Wolfgang: *Elemente der Arithmetik und Algebra*. Springer, 2016.
- Beutelspacher, Albrecht: *Zahlen*. Rowohlt, 2013.
- Ifrah, Georges: *Universalgeschichte der Zahlen*. Campus, 1991.

> [!tip] **Weiterführende Links**
> - [Mathebibel: Ganze Zahlen](https://www.mathebibel.de/ganze-zahlen)
> - [[05-Rationale-Zahlen|Nächstes Kapitel: Rationale Zahlen]]
