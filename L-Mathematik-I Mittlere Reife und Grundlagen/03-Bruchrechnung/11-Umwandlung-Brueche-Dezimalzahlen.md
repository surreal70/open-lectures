---
author: Open Lectures
title: Umwandlung von Brüchen in Dezimalzahlen
status: draft - review pending
tags:
  - content
  - mathematik
  - bruchrechnung
created: 2026-10-13
modified: 2026-10-16
---

# Umwandlung von Brüchen in Dezimalzahlen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Brüche durch Division in Dezimalzahlen umwandeln können
> - Abbrechende und periodische Dezimalzahlen unterscheiden können
> - Dezimalzahlen in Brüche umwandeln können

---

## Überblick

Brüche und Dezimalzahlen sind zwei verschiedene Darstellungen derselben Zahlen. Die Umwandlung erfolgt durch Division (Zähler durch Nenner) oder durch Erweitern auf Zehnerpotenzen.

Die Fähigkeit, zwischen Brüchen und Dezimalzahlen zu wechseln, ist im Alltag sehr nützlich: Preise werden als Dezimalzahlen angegeben (3,99 €), aber Rabatte oft als Brüche („ein Drittel günstiger"). Auch Taschenrechner zeigen Ergebnisse als Dezimalzahlen – um zu verstehen, was $0{,}333...$ bedeutet, muss man wissen, dass es $\frac{1}{3}$ ist.

Interessanterweise lassen sich nicht alle Brüche als „schöne" endliche Dezimalzahlen schreiben. Manche Brüche erzeugen **periodische** Dezimalzahlen – Dezimalzahlen, bei denen sich eine Ziffernfolge unendlich wiederholt.

---

## Bruch → Dezimalzahl

### Methode: Division

$$\frac{a}{b} = a : b$$

Jeder Bruch ist eine Division. Um die Dezimalzahl zu erhalten, führe die Division aus:

**Beispiel:** $\frac{3}{4} = 3 : 4 = 0{,}75$

**Schriftlich:**
```
  3 : 4 = 0,75
  3,00
  -2 8   (4 × 7 = 28)
    20
   -20   (4 × 5 = 20)
     0
```

### Abbrechende Dezimalzahlen

Entstehen, wenn der Nenner nur Faktoren 2 und 5 hat:

| Bruch | Division | Dezimalzahl |
|-------|----------|-------------|
| $\frac{1}{2}$ | $1 : 2$ | $0{,}5$ |
| $\frac{3}{4}$ | $3 : 4$ | $0{,}75$ |
| $\frac{7}{8}$ | $7 : 8$ | $0{,}875$ |
| $\frac{3}{5}$ | $3 : 5$ | $0{,}6$ |

> [!note] **Warum nur 2 und 5?**
> Unser Dezimalsystem basiert auf 10, und $10 = 2 \cdot 5$. 
> 
> Wenn der Nenner nur aus den Primfaktoren 2 und 5 besteht, lässt sich der Bruch auf einen Nenner erweitern, der eine Zehnerpotenz ist:
> - $\frac{3}{4} = \frac{3}{2^2} = \frac{3 \cdot 25}{100} = \frac{75}{100} = 0{,}75$
> - $\frac{1}{8} = \frac{1}{2^3} = \frac{125}{1000} = 0{,}125$

### Periodische Dezimalzahlen

Entstehen bei allen anderen Nennern (die Primfaktoren außer 2 und 5 enthalten):

| Bruch | Dezimalzahl | Periode |
|-------|-------------|---------|
| $\frac{1}{3}$ | $0{,}\overline{3}$ | 3 |
| $\frac{2}{3}$ | $0{,}\overline{6}$ | 6 |
| $\frac{1}{6}$ | $0{,}1\overline{6}$ | 6 |
| $\frac{1}{7}$ | $0{,}\overline{142857}$ | 142857 |
| $\frac{1}{9}$ | $0{,}\overline{1}$ | 1 |
| $\frac{1}{11}$ | $0{,}\overline{09}$ | 09 |

Der Strich über den Ziffern zeigt die **Periode** an – die Ziffernfolge, die sich unendlich wiederholt.

> [!note] **Warum entstehen Perioden?**
> Bei der Division können nur endlich viele verschiedene Reste auftreten (0 bis Nenner-1). Wenn kein Rest 0 wird, muss irgendwann ein Rest wiederholt auftreten – ab da wiederholt sich die Rechnung und damit die Ziffernfolge.
>
> Bei $\frac{1}{7}$ gibt es 6 mögliche Reste (1-6), daher hat die Periode maximal 6 Ziffern: 142857.

> [!tip] **Schnelles Erkennen**
> - Nenner ist Zehnerpotenz (10, 100, 1000): direkt ablesbar ($\frac{7}{100} = 0{,}07$)
> - Nenner hat nur Faktoren 2 und/oder 5: abbrechend
> - Nenner hat 3, 7, 9, 11 oder andere Primfaktoren: periodisch

---

## Dezimalzahl → Bruch

### Abbrechende Dezimalzahlen

Als Bruch mit Zehnerpotenzen schreiben, dann kürzen:

$$0{,}75 = \frac{75}{100} = \frac{3}{4}$$

**Methode:** Zähle die Nachkommastellen – so viele Nullen hat der Nenner.
- 1 Nachkommastelle → Nenner 10
- 2 Nachkommastellen → Nenner 100
- 3 Nachkommastellen → Nenner 1000

| Dezimalzahl | Als Bruch | Gekürzt |
|-------------|-----------|---------|
| $0{,}5$ | $\frac{5}{10}$ | $\frac{1}{2}$ |
| $0{,}25$ | $\frac{25}{100}$ | $\frac{1}{4}$ |
| $0{,}125$ | $\frac{125}{1000}$ | $\frac{1}{8}$ |
| $0{,}375$ | $\frac{375}{1000}$ | $\frac{3}{8}$ |

### Periodische Dezimalzahlen

**Reine Periode** (Periode beginnt direkt nach dem Komma): $0{,}\overline{3}$

Sei $x = 0{,}333...$
Dann $10x = 3{,}333...$
Also $10x - x = 3$
$9x = 3$ → $x = \frac{3}{9} = \frac{1}{3}$

> [!tip] **Schnelle Regel für reine Perioden**
> Periode mit so vielen Neunen wie Periodenziffern:
> - $0{,}\overline{3} = \frac{3}{9} = \frac{1}{3}$
> - $0{,}\overline{12} = \frac{12}{99} = \frac{4}{33}$
> - $0{,}\overline{142857} = \frac{142857}{999999} = \frac{1}{7}$

**Gemischte Periode** (nicht-periodischer Teil vor der Periode): $0{,}1\overline{6}$

Diese sind komplizierter umzuwandeln. Der allgemeine Ansatz nutzt Multiplikation, um die Periode zu isolieren.

---

## Wichtige Entsprechungen

Diese Werte sollte man auswendig kennen:

| Bruch | Dezimal | Prozent |
|-------|---------|---------|
| $\frac{1}{2}$ | 0,5 | 50% |
| $\frac{1}{4}$ | 0,25 | 25% |
| $\frac{3}{4}$ | 0,75 | 75% |
| $\frac{1}{5}$ | 0,2 | 20% |
| $\frac{1}{8}$ | 0,125 | 12,5% |
| $\frac{1}{3}$ | 0,3̄ | 33,3̄% |
| $\frac{2}{3}$ | 0,6̄ | 66,6̄% |
| $\frac{1}{10}$ | 0,1 | 10% |

> [!warning] **Häufiger Fehler: Rundungsfehler**
> $\frac{1}{3} \neq 0{,}33$ und $\frac{1}{3} \neq 0{,}333$
>
> $\frac{1}{3} = 0{,}\overline{3}$ (unendlich viele Dreien!)
>
> Wenn du $\frac{1}{3}$ als $0{,}33$ eintippst, rechnest du eigentlich mit $\frac{33}{100}$ – das ist ein kleiner, aber wichtiger Unterschied.

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[01-Grundlagen-der-Brueche|Grundlagen der Brüche]] – Bruch als Division
- → [[04-Dezimalzahlen-und-Prozentrechnung/01-Dezimalzahlen|Dezimalzahlen]] – Ausführliche Behandlung
- → [[04-Dezimalzahlen-und-Prozentrechnung/04-Einfuehrung-in-die-Prozentrechnung|Prozentrechnung]] – Die dritte Darstellungsform

> [!warning] **Prüfungsrelevant**
> - Bruch → Dezimal: Zähler durch Nenner dividieren
> - Abbrechend: Nenner hat nur Faktoren 2 und 5
> - Periodisch: Alle anderen Nenner

> [!question] **Typische Prüfungsfragen**
> - Wandle $\frac{5}{8}$ in eine Dezimalzahl um.
> - Wandle $0{,}375$ in einen Bruch um.
> - Ist $\frac{3}{7}$ abbrechend oder periodisch?

## Quellen

- Padberg, Friedhelm: *Didaktik der Bruchrechnung*. Springer, 2009.
