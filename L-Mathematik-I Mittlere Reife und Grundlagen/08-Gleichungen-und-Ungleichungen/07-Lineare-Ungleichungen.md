---
title: "Lineare Ungleichungen"
created: 2026-10-13
modified: 2026-10-16
chapter: "08"
section: "07"
status: "draft - review pending"
type: lecture
keywords:
  - Ungleichung
  - Intervall
  - Lösungsmenge
  - Vorzeichenwechsel
---

# Lineare Ungleichungen

> [!info] Lernziele
> - Den Unterschied zwischen Gleichungen und Ungleichungen verstehen
> - Ungleichungen systematisch lösen können
> - Die Vorzeichenregel bei Multiplikation/Division anwenden
> - Lösungsmengen in Intervallschreibweise und grafisch darstellen

## Historischer Kontext

Während Gleichungen schon in der Antike gelöst wurden, entwickelte sich die systematische Behandlung von **Ungleichungen** erst viel später. Der französische Mathematiker **Pierre Bouguer** führte 1734 die Symbole $<$ und $>$ ein, die wir heute verwenden. Die moderne Intervallnotation wurde im 19. Jahrhundert standardisiert.

Ungleichungen sind in der Praxis oft wichtiger als Gleichungen: Während eine Gleichung nach einem exakten Wert fragt („Wie viel genau?"), fragt eine Ungleichung nach einem Bereich („Mindestens wie viel?" oder „Höchstens wie viel?").

> [!tip] **Alltagsbeispiele für Ungleichungen**
> - **Geschwindigkeitsbegrenzung**: $v \leq 50$ km/h (höchstens 50 km/h)
> - **Mindestlohn**: $Stundenlohn \geq 12{,}41$ € (mindestens 12,41 €)
> - **Budgetplanung**: $Ausgaben < Einnahmen$ (weniger ausgeben als einnehmen)
> - **Notendurchschnitt**: $\varnothing \leq 2{,}5$ für eine Zulassung

## Ungleichungen vs. Gleichungen

| Gleichung | Ungleichung |
|---|---|
| $2x + 3 = 11$ | $2x + 3 < 11$ |
| Genau eine Lösung (meist) | Unendlich viele Lösungen (meist) |
| $x = 4$ | $x < 4$ (alle Zahlen kleiner als 4) |

Der fundamentale Unterschied: Eine Gleichung sucht einen **Punkt**, eine Ungleichung sucht einen **Bereich**.

### Ungleichungszeichen

| Zeichen | Bedeutung | Beispiel |
|---|---|---|
| $<$ | kleiner als | $x < 5$ |
| $>$ | größer als | $x > 3$ |
| $\leq$ | kleiner oder gleich | $x \leq 7$ |
| $\geq$ | größer oder gleich | $x \geq -2$ |

## Lösungsverfahren

### Grundregel

Ungleichungen werden **ähnlich wie Gleichungen** gelöst, mit einer wichtigen Ausnahme:

> [!danger] Vorzeichenregel
> Bei **Multiplikation oder Division mit einer negativen Zahl** muss das **Ungleichungszeichen umgedreht** werden!

### Beispiel 1: Einfache Ungleichung

$$3x + 5 < 14$$
$$3x < 9 \quad | -5$$
$$x < 3 \quad | :3$$

**Lösungsmenge**: $\mathbb{L} = \{x \in \mathbb{R} \mid x < 3\}$ oder $\mathbb{L} = (-\infty, 3)$

### Beispiel 2: Mit negativer Division

$$-2x + 6 > 10$$
$$-2x > 4 \quad | -6$$
$$x < -2 \quad | :(-2) \text{ ← Zeichen dreht sich!}$$

**Lösungsmenge**: $\mathbb{L} = (-\infty, -2)$

## Die Vorzeichenregel im Detail

### Warum dreht sich das Zeichen?

Betrachte die wahre Aussage: $3 < 5$

| Operation | Ergebnis | Aussage |
|---|---|---|
| $\cdot 2$ | $6 < 10$ | wahr ✓ |
| $\cdot (-2)$ | $-6 < -10$? | falsch! |
| $\cdot (-2)$ mit Umdrehen | $-6 > -10$ | wahr ✓ |

> [!tip] **Merksatz: Die Spiegelung am Zahlenstrahl**
> Multiplizieren oder Dividieren mit einer **negativen Zahl** → Ungleichungszeichen **umkehren**!
>
> Warum? Multiplizieren mit $-1$ spiegelt alle Zahlen am Nullpunkt: Positive werden negativ, negative werden positiv. Dabei vertauscht sich auch die Reihenfolge auf dem Zahlenstrahl!
>
> Beispiel: $2 < 5$, aber $-2 > -5$ (auf dem Zahlenstrahl liegt $-2$ rechts von $-5$)

> [!warning] **Häufiger Fehler: Vorzeichenregel vergessen**
> Dies ist der häufigste Fehler bei Ungleichungen:
> - **Falsch:** $-3x > 12 \Rightarrow x > -4$ (Zeichen nicht gedreht!)
> - **Richtig:** $-3x > 12 \Rightarrow x < -4$ (Division durch $-3$ dreht das Zeichen)

## Darstellung der Lösungsmenge

Weil eine Ungleichung meist einen ganzen Bereich und nicht nur eine einzelne Zahl beschreibt, braucht man geeignete Schreibweisen, um dieses Ergebnis festzuhalten. Dieselbe Lösungsmenge lässt sich auf drei Weisen ausdrücken: als Menge, als Intervall und als Bild auf der Zahlengeraden. Alle drei meinen dasselbe, betonen aber unterschiedliche Aspekte – die grafische Darstellung macht etwa besonders anschaulich, ob eine Grenze dazugehört oder nicht.

### Mengennotation

$$\mathbb{L} = \{x \in \mathbb{R} \mid x > 2\}$$
„Alle reellen Zahlen $x$, für die $x > 2$ gilt"

### Intervallschreibweise

| Ungleichung | Intervall |
|---|---|
| $x > 2$ | $(2, +\infty)$ |
| $x \geq 2$ | $[2, +\infty)$ |
| $x < 5$ | $(-\infty, 5)$ |
| $x \leq 5$ | $(-\infty, 5]$ |
| $2 < x < 5$ | $(2, 5)$ |
| $2 \leq x \leq 5$ | $[2, 5]$ |

> [!note] Konvention
> - Runde Klammer $($ oder $)$: Grenzwert **nicht** enthalten
> - Eckige Klammer $[$ oder $]$: Grenzwert **enthalten**
> - Bei $\pm\infty$ immer runde Klammer

### Grafische Darstellung (Zahlengerade)

**Beispiel**: $x \geq 2$

![[ungleichung-x-groesser-gleich-2.png]]
*<span class="fig-id">01-08-07-ungleichung-x-groesser-gleich-2</span>: Lösungsmenge von x ≥ 2 auf dem Zahlenstrahl – ausgefüllter Punkt bei 2 (gehört dazu), Strahl nach rechts.*

**Beispiel**: $x < -1$

![[ungleichung-x-kleiner-minus1.png]]
*<span class="fig-id">01-08-07-ungleichung-x-kleiner-minus1</span>: Lösungsmenge von x < −1 auf dem Zahlenstrahl – offener Punkt bei −1 (gehört nicht dazu), Strahl nach links.*

- Ausgefüllter Punkt ($\bullet$): Wert gehört dazu ($\leq$ oder $\geq$)
- Offener Punkt ($\circ$): Wert gehört nicht dazu ($<$ oder $>$)

## Ungleichungen mit Variablen auf beiden Seiten

$$5x - 3 > 2x + 9$$

**Schritt 1**: Variable auf eine Seite
$$5x - 2x > 9 + 3$$
$$3x > 12$$

**Schritt 2**: Isolieren
$$x > 4$$

**Lösungsmenge**: $\mathbb{L} = (4, +\infty)$

## Doppelungleichungen

Manchmal soll ein Wert nicht nur über oder unter einer Schranke liegen, sondern zwischen zwei Grenzen eingeschlossen sein. Dafür fasst man zwei Ungleichungen zu einer Doppelungleichung zusammen. Der Vorteil: Man muss nicht zwei getrennte Rechnungen führen, sondern kann alle drei Teile gleichzeitig umformen – solange man jede Operation konsequent auf alle drei anwendet.

Eine **Doppelungleichung** gibt einen Bereich an:

$$-3 < 2x + 1 \leq 7$$

**Lösung**: Alle drei Teile gleichzeitig umformen

$$-3 < 2x + 1 \leq 7 \quad | -1$$
$$-4 < 2x \leq 6 \quad | :2$$
$$-2 < x \leq 3$$

**Lösungsmenge**: $\mathbb{L} = (-2, 3]$

![[ungleichung-intervall.png]]
*<span class="fig-id">01-08-07-ungleichung-intervall</span>: Lösungsmenge des Intervalls (−2, 3] – offener Punkt bei −2 (gehört nicht dazu), ausgefüllter Punkt bei 3 (gehört dazu).*

## Sonderfälle

Wie bei linearen Gleichungen kann auch bei Ungleichungen die Variable beim Umformen vollständig wegfallen. Übrig bleibt dann ein Vergleich zweier fester Zahlen. Ist dieser Vergleich immer wahr, lösen alle reellen Zahlen die Ungleichung; ist er nie wahr, gibt es gar keine Lösung. Diese beiden Grenzfälle treten selten auf, sollten aber richtig gedeutet werden.

### Alle reellen Zahlen als Lösung

$$2x + 1 > 2x - 5$$
$$1 > -5$$ (immer wahr)

$$\mathbb{L} = \mathbb{R}$$

### Keine Lösung

$$3x + 2 < 3x - 4$$
$$2 < -4$$ (nie wahr)

$$\mathbb{L} = \emptyset$$

## Zusammenfassung

> [!abstract] Kernpunkte
> - Ungleichungen werden wie Gleichungen gelöst
> - Bei Multiplikation/Division mit negativer Zahl: Zeichen umdrehen!
> - Lösungsmengen sind oft Intervalle mit unendlich vielen Werten
> - Darstellung: Mengennotation, Intervallschreibweise oder Zahlengerade
> - $<$, $>$ → offenes Intervall; $\leq$, $\geq$ → geschlossenes Intervall

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[04-Lineare-Gleichungen|Lineare Gleichungen]] – Ähnliches Lösungsverfahren
- → [[02-Aequivalenzumformungen|Äquivalenzumformungen]] – Grundlegende Umformungen
- → [[01-Einfuehrung-in-die-Mathematik/02-Mathematische-Symbole|Vergleichszeichen]] – Die Symbole $<$, $>$, $\leq$, $\geq$
- → [[09-Funktionen-und-Koordinatensysteme/05-Lineare-Funktionen|Lineare Funktionen]] – Grafische Interpretation

## Übungsaufgaben

Löse und gib die Lösungsmenge in Intervallschreibweise an:

1. $2x + 7 < 15$
2. $-3x \geq 12$
3. $4x - 5 > x + 7$
4. $-2(x - 3) \leq 10$
5. $1 < 3x - 2 \leq 13$
6. $5 - 2x > 3x + 20$

Stelle die Lösungen auf einer Zahlengeraden dar.

---

**Navigation**: [[06-Bruchgleichungen|← Bruchgleichungen]] | [[00-Gleichungen-und-Ungleichungen-Index|Übersicht]] | [[08-Quadratische-Gleichungen|Quadratische Gleichungen →]]
