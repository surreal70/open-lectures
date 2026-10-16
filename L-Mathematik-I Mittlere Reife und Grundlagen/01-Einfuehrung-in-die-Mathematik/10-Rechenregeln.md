---
author: Open Lectures
title: Mathematische Notation und Rechenregeln
status: draft - review pending
tags:
  - content
  - mathematik
  - rechenregeln
  - notation
created: 2026-10-13
modified: 2026-10-13
---

# Mathematische Notation und Rechenregeln

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Rechengesetze (Kommutativ-, Assoziativ-, Distributivgesetz) kennen und anwenden
> - Die Reihenfolge der Rechenoperationen beherrschen
> - Terme korrekt aufstellen und umformen können
> - Klammern richtig setzen und auflösen können

---

## Überblick

Die Rechenregeln bilden das Grundgerüst der Mathematik. Sie legen fest, in welcher Reihenfolge Operationen ausgeführt werden und welche Umformungen erlaubt sind. Das Beherrschen dieser Regeln ist Voraussetzung für alle weiteren mathematischen Themen.

---

## Die Rechengesetze

### Kommutativgesetz (Vertauschungsgesetz)

Bei Addition und Multiplikation darf die Reihenfolge der Zahlen vertauscht werden:

| Operation | Gesetz | Beispiel |
|-----------|--------|----------|
| Addition | $a + b = b + a$ | $3 + 5 = 5 + 3 = 8$ |
| Multiplikation | $a \cdot b = b \cdot a$ | $4 \cdot 7 = 7 \cdot 4 = 28$ |

> [!warning] **Achtung**
> Subtraktion und Division sind **nicht** kommutativ:
> - $5 - 3 = 2$, aber $3 - 5 = -2$
> - $6 : 2 = 3$, aber $2 : 6 = \frac{1}{3}$

### Assoziativgesetz (Verbindungsgesetz)

Bei Addition und Multiplikation dürfen Klammern beliebig gesetzt werden:

| Operation | Gesetz | Beispiel |
|-----------|--------|----------|
| Addition | $(a + b) + c = a + (b + c)$ | $(2 + 3) + 4 = 2 + (3 + 4) = 9$ |
| Multiplikation | $(a \cdot b) \cdot c = a \cdot (b \cdot c)$ | $(2 \cdot 3) \cdot 4 = 2 \cdot (3 \cdot 4) = 24$ |

> [!note] **Praktische Bedeutung**
> Dank des Assoziativgesetzes können wir $2 + 3 + 4$ ohne Klammern schreiben – das Ergebnis ist unabhängig von der Klammerung.

### Distributivgesetz (Verteilungsgesetz)

Multiplikation kann über Addition/Subtraktion „verteilt" werden:

$$a \cdot (b + c) = a \cdot b + a \cdot c$$
$$a \cdot (b - c) = a \cdot b - a \cdot c$$

**Beispiele:**

$$3 \cdot (4 + 5) = 3 \cdot 4 + 3 \cdot 5 = 12 + 15 = 27$$
$$5 \cdot (10 - 2) = 5 \cdot 10 - 5 \cdot 2 = 50 - 10 = 40$$

> [!tip] **Umkehrung: Ausklammern**
> Das Distributivgesetz funktioniert auch rückwärts:
> $$6 + 9 = 3 \cdot 2 + 3 \cdot 3 = 3 \cdot (2 + 3) = 3 \cdot 5 = 15$$

---

## Reihenfolge der Rechenoperationen

### Die Regel: „Klammer vor Punkt vor Strich"

Die Operationen werden in folgender Reihenfolge ausgeführt:

| Priorität | Operation | Beispiel |
|-----------|-----------|----------|
| 1 (höchste) | Klammern | $(3 + 2)$ wird zuerst berechnet |
| 2 | Potenzen | $2^3$ wird vor $\cdot$ berechnet |
| 3 | Punktrechnung ($\cdot$, $:$) | $4 \cdot 5$ vor $+$ |
| 4 (niedrigste) | Strichrechnung ($+$, $-$) | Zuletzt |

### Beispiele

**Beispiel 1:** $3 + 4 \cdot 2$
$$= 3 + 8 = 11 \quad \text{(Punkt vor Strich)}$$

**Beispiel 2:** $(3 + 4) \cdot 2$
$$= 7 \cdot 2 = 14 \quad \text{(Klammer zuerst)}$$

**Beispiel 3:** $2 + 3 \cdot 4^2$
$$= 2 + 3 \cdot 16 = 2 + 48 = 50$$

**Beispiel 4:** $24 : 4 \cdot 2$
$$= 6 \cdot 2 = 12 \quad \text{(von links nach rechts)}$$

> [!warning] **Bei gleicher Priorität**
> Operationen gleicher Priorität werden **von links nach rechts** ausgeführt:
> $$20 - 5 + 3 = 15 + 3 = 18$$
> $$24 : 4 : 2 = 6 : 2 = 3$$

---

## Klammerregeln

### Klammern auflösen

**Plus vor der Klammer:**
$$+(a + b) = a + b$$
$$+(a - b) = a - b$$

**Minus vor der Klammer:**
$$-(a + b) = -a - b$$
$$-(a - b) = -a + b$$

> [!tip] **Merkregel**
> Ein Minus vor der Klammer kehrt alle Vorzeichen in der Klammer um.

**Beispiele:**
$$5 + (3 - 2) = 5 + 3 - 2 = 6$$
$$5 - (3 - 2) = 5 - 3 + 2 = 4$$
$$5 - (3 + 2) = 5 - 3 - 2 = 0$$

### Verschachtelte Klammern

Bei mehreren Klammern von innen nach außen auflösen:

$$3 \cdot [2 + (4 - 1)]$$
$$= 3 \cdot [2 + 3]$$
$$= 3 \cdot 5$$
$$= 15$$

---

## Rechengesetze für Brüche

### Addition und Subtraktion

Nur bei **gleichem Nenner** direkt möglich:
$$\frac{a}{c} + \frac{b}{c} = \frac{a + b}{c}$$

Bei verschiedenen Nennern erst **erweitern**:
$$\frac{1}{2} + \frac{1}{3} = \frac{3}{6} + \frac{2}{6} = \frac{5}{6}$$

### Multiplikation

Zähler mal Zähler, Nenner mal Nenner:
$$\frac{a}{b} \cdot \frac{c}{d} = \frac{a \cdot c}{b \cdot d}$$

**Beispiel:**
$$\frac{2}{3} \cdot \frac{4}{5} = \frac{2 \cdot 4}{3 \cdot 5} = \frac{8}{15}$$

### Division

Mit dem Kehrwert multiplizieren:
$$\frac{a}{b} : \frac{c}{d} = \frac{a}{b} \cdot \frac{d}{c} = \frac{a \cdot d}{b \cdot c}$$

**Beispiel:**
$$\frac{3}{4} : \frac{2}{5} = \frac{3}{4} \cdot \frac{5}{2} = \frac{15}{8}$$

---

## Potenzgesetze (Vorschau)

| Gesetz | Formel | Beispiel |
|--------|--------|----------|
| Multiplikation gleicher Basis | $a^m \cdot a^n = a^{m+n}$ | $2^3 \cdot 2^2 = 2^5 = 32$ |
| Division gleicher Basis | $a^m : a^n = a^{m-n}$ | $2^5 : 2^2 = 2^3 = 8$ |
| Potenz einer Potenz | $(a^m)^n = a^{m \cdot n}$ | $(2^3)^2 = 2^6 = 64$ |
| Potenz eines Produkts | $(a \cdot b)^n = a^n \cdot b^n$ | $(2 \cdot 3)^2 = 4 \cdot 9 = 36$ |

---

## Übersicht: Neutrale Elemente

| Operation | Neutrales Element | Eigenschaft |
|-----------|-------------------|-------------|
| Addition | $0$ | $a + 0 = a$ |
| Multiplikation | $1$ | $a \cdot 1 = a$ |

### Inverse Elemente

| Operation | Inverses zu $a$ | Eigenschaft |
|-----------|-----------------|-------------|
| Addition | $-a$ | $a + (-a) = 0$ |
| Multiplikation | $\frac{1}{a}$ (für $a \neq 0$) | $a \cdot \frac{1}{a} = 1$ |

---

## Zusammenfassung der Rechengesetze

```
┌─────────────────────────────────────────────────────────┐
│                    RECHENGESETZE                        │
├─────────────────────────────────────────────────────────┤
│ Kommutativgesetz:                                       │
│   a + b = b + a       a · b = b · a                    │
│                                                         │
│ Assoziativgesetz:                                       │
│   (a + b) + c = a + (b + c)                            │
│   (a · b) · c = a · (b · c)                            │
│                                                         │
│ Distributivgesetz:                                      │
│   a · (b + c) = a · b + a · c                          │
│                                                         │
│ Reihenfolge:                                           │
│   Klammer → Potenz → Punkt → Strich                    │
└─────────────────────────────────────────────────────────┘
```

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[02-Mathematische-Symbole|Mathematische Symbole]] – Notation
- → [[05-Rationale-Zahlen|Rationale Zahlen]] – Bruchrechnung
- → [[08-Positive-und-negative-Zahlen|Vorzeichen]] – Vorzeichenregeln

> [!warning] **Prüfungsrelevant**
> - Kommutativ-, Assoziativ-, Distributivgesetz
> - Reihenfolge: Klammer vor Potenz vor Punkt vor Strich
> - Minus vor Klammer kehrt Vorzeichen um
> - Bruchrechnung: Addition mit Hauptnenner, Multiplikation Zähler·Zähler / Nenner·Nenner
> - Division durch Bruch = Multiplikation mit Kehrwert

> [!question] **Typische Prüfungsfragen**
> - Berechne: $5 + 3 \cdot (4 - 2)^2$
> - Vereinfache: $3 \cdot (x + 2) - 2 \cdot (x - 1)$
> - Berechne: $\frac{2}{3} + \frac{3}{4}$
> - Welches Rechengesetz wurde angewendet: $3 \cdot 7 = 7 \cdot 3$?

## Quellen

- Padberg, Friedhelm: *Didaktik der Arithmetik*. Springer, 2017.
- Scheid, Harald: *Elemente der Arithmetik und Algebra*. Springer, 2016.

> [!tip] **Weiterführende Links**
> - [Mathebibel: Rechengesetze](https://www.mathebibel.de/rechengesetze)
> - [[02-Grundrechenarten-Index|Nächstes Modul: Grundrechenarten]]
