---
author: Andreas Hümmer
title: Division
status: final
tags:
  - content
  - mathematik
  - grundrechenarten
  - division
created: 2026-10-13
modified: 2026-10-16
---

# Division

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Division als Aufteilen und als Umkehrung der Multiplikation verstehen
> - Fachbegriffe (Dividend, Divisor, Quotient) korrekt verwenden
> - Schriftliche Division durchführen können
> - Vorzeichenregeln bei der Division anwenden
> - Wissen, warum Division durch Null verboten ist

---

## Überblick

Die **Division** (lat. „dividere" = teilen) ist die Umkehroperation der Multiplikation. Sie beantwortet Fragen wie „Wie oft passt eine Zahl in eine andere?" oder „Wie groß ist jeder Teil, wenn ich gerecht aufteile?".

### Historischer Hintergrund

Die Division ist die jüngste und komplexeste der vier Grundrechenarten. Das Divisionszeichen „$\div$" wurde 1659 vom Schweizer Mathematiker Johann Heinrich Rahn eingeführt. In Deutschland verwendet man traditionell den Doppelpunkt „$:$", während im englischsprachigen Raum der Schrägstrich „$/$" oder das Obelus-Zeichen „$\div$" üblich ist. Die Bruchschreibweise $\frac{a}{b}$ hat sich in der höheren Mathematik durchgesetzt, weil sie am übersichtlichsten ist.

### Division im Alltag

Division begegnet uns häufiger als man denkt:
- **Gerecht teilen**: 12 Bonbons auf 4 Kinder verteilen → $12 : 4 = 3$ Bonbons pro Kind
- **Preisvergleich**: Welcher Joghurt ist günstiger? Preis durch Menge teilen ergibt den Kilopreis
- **Durchschnitte**: Notendurchschnitt = Summe aller Noten geteilt durch Anzahl der Noten
- **Geschwindigkeit**: 150 km in 2 Stunden → $150 : 2 = 75$ km/h

---

## Definition und Fachbegriffe

$$\underbrace{a}_{\text{Dividend}} : \underbrace{b}_{\text{Divisor}} = \underbrace{c}_{\text{Quotient}}$$

| Begriff | Bedeutung | Beispiel |
|---------|-----------|----------|
| **Dividend** | Zahl, die geteilt wird | In $12 : 3$: die $12$ |
| **Divisor** | Zahl, durch die geteilt wird | In $12 : 3$: die $3$ |
| **Quotient** | Ergebnis der Division | In $12 : 3 = 4$: die $4$ |

### Verschiedene Schreibweisen

$$12 : 3 = \frac{12}{3} = 12 \div 3 = 4$$

---

## Zwei Bedeutungen der Division

### 1. Aufteilen (Verteilen)

*„12 Äpfel werden gleichmäßig auf 3 Kinder verteilt. Wie viele bekommt jedes Kind?"*

$$12 : 3 = 4 \quad \text{(jedes Kind bekommt 4 Äpfel)}$$

### 2. Ausmessen (Enthalten-sein)

*„Wie oft passt 3 in 12?"*

$$12 : 3 = 4 \quad \text{(3 passt 4-mal in 12)}$$

---

## Zusammenhang mit der Multiplikation

Division ist die Umkehroperation der Multiplikation:

$$\text{Wenn } a \cdot b = c, \text{ dann } c : b = a \text{ und } c : a = b$$

**Beispiel:**
- $4 \cdot 3 = 12$
- $12 : 3 = 4$
- $12 : 4 = 3$

### Probe durch Multiplikation

$$\text{Wenn } a : b = c, \text{ dann } c \cdot b = a$$

**Beispiel:** $20 : 4 = 5$ → Probe: $5 \cdot 4 = 20$ ✓

---

## Schriftliche Division

### Beispiel: $7524 : 12$

![[schriftliche-division.png]]
*<span class="fig-id">01-02-04-schriftliche-division</span>: Schriftliche Division 7524 : 12 = 627 – schrittweises Teilen und Herunterholen der nächsten Ziffer, bis der Rest 0 erreicht ist.*

**Schritte:**
1. $75 : 12 = 6$ Rest $3$ (da $6 \cdot 12 = 72$)
2. Hole die $2$ herunter → $32 : 12 = 2$ Rest $8$
3. Hole die $4$ herunter → $84 : 12 = 7$ Rest $0$

---

## Division mit Rest

Wenn die Division nicht aufgeht:

$$17 : 5 = 3 \text{ Rest } 2$$

Denn: $5 \cdot 3 = 15$ und $17 - 15 = 2$

**Schreibweisen:**
- $17 : 5 = 3 \text{ R } 2$
- $17 = 5 \cdot 3 + 2$
- $17 : 5 = 3{,}4$

---

## Vorzeichenregeln

Die Regeln sind identisch zur Multiplikation:

| Rechnung | Ergebnis | Regel |
|----------|----------|-------|
| $(+) : (+)$ | $+$ | Gleiche Vorzeichen → Plus |
| $(+) : (-)$ | $-$ | Verschiedene Vorzeichen → Minus |
| $(-) : (+)$ | $-$ | Verschiedene Vorzeichen → Minus |
| $(-) : (-)$ | $+$ | Gleiche Vorzeichen → Plus |

**Beispiele:**
- $12 : 3 = 4$
- $12 : (-3) = -4$
- $(-12) : 3 = -4$
- $(-12) : (-3) = 4$

---

## Division durch Null

> [!danger] **Verboten: Division durch Null**
> $$a : 0 \text{ ist nicht definiert!}$$

Dies ist eine der wichtigsten Regeln der Mathematik und hat tiefgreifende Gründe.

### Warum?

Angenommen, $6 : 0 = x$. Dann müsste gelten: $x \cdot 0 = 6$.

Aber: $x \cdot 0 = 0$ für **jedes** $x$, niemals $6$.

→ Es gibt keine Zahl $x$, die die Gleichung erfüllt.

### Sonderfall: $0 : 0$

Auch $0 : 0$ ist nicht definiert, denn $x \cdot 0 = 0$ gilt für **jedes** $x$.

→ Unendlich viele „Lösungen" = keine eindeutige Lösung.

> [!note] **Anschauliche Erklärung**
> Stell dir vor, du sollst 12 Äpfel auf 0 Kinder verteilen. Das macht keinen Sinn – es gibt niemanden, der etwas bekommen könnte! Oder anders: „Wie oft passt 0 in 12?" – Egal wie oft du 0 addierst, du erreichst nie 12.

> [!warning] **Merke**
> - $0 : a = 0$ (für $a \neq 0$) ist erlaubt – null Äpfel auf 5 Kinder verteilt ergibt 0 Äpfel pro Kind
> - $a : 0$ ist **verboten** (undefiniert)
> - In Taschenrechnern und Programmen führt Division durch 0 zu Fehlermeldungen („Error" oder „undefined")

---

## Eigenschaften der Division

### Nicht kommutativ!

$$a : b \neq b : a \quad \text{(im Allgemeinen)}$$

**Beispiel:** $12 : 3 = 4$, aber $3 : 12 = 0{,}25$

### Nicht assoziativ!

$$(a : b) : c \neq a : (b : c) \quad \text{(im Allgemeinen)}$$

**Beispiel:**
- $(24 : 6) : 2 = 4 : 2 = 2$
- $24 : (6 : 2) = 24 : 3 = 8$

### Neutrales Element (rechts)

$$a : 1 = a$$

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[03-Multiplikation|Multiplikation]] – Umkehroperation
- → [[05-Rationale-Zahlen|Brüche]] – Division führt zu Brüchen
- → [[08-Punkt-vor-Strich|Punkt vor Strich]] – Division ist Punktrechnung

> [!warning] **Prüfungsrelevant**
> - Fachbegriffe: Dividend, Divisor, Quotient
> - Division durch Null ist verboten
> - Vorzeichenregeln: gleich → plus, verschieden → minus
> - Division ist **nicht** kommutativ und **nicht** assoziativ
> - $0 : a = 0$ (für $a \neq 0$)

> [!question] **Typische Prüfungsfragen**
> - Berechne schriftlich: $8736 : 24$
> - Berechne: $(-36) : (-4)$
> - Warum ist $5 : 0$ nicht erlaubt?
> - Berechne: $48 : 8 : 2$ (von links nach rechts!)

## Quellen

- Padberg, Friedhelm: *Didaktik der Arithmetik*. Springer, 2017.

> [!tip] **Weiterführende Links**
> - [[05-Kommutativgesetz|Nächstes Kapitel: Kommutativgesetz]]
