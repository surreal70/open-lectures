---
title: "Grundlagen von Gleichungen"
created: 2026-10-13
modified: 2025-07-21
chapter: "08"
section: "01"
status: "draft - review pending"
type: lecture
keywords:
  - Gleichung
  - Variable
  - Lösung
  - Lösungsmenge
  - Aussage
---

# Grundlagen von Gleichungen

> [!info] Lernziele
> - Den Begriff der Gleichung mathematisch definieren können
> - Variablen und ihre Rolle in Gleichungen verstehen
> - Lösungen und Lösungsmengen bestimmen können
> - Arten von Gleichungen unterscheiden können

## Historischer Hintergrund

Das Lösen von Gleichungen ist eine der ältesten mathematischen Tätigkeiten. Schon die **Babylonier** vor etwa 4000 Jahren lösten auf Tontafeln Gleichungen – allerdings nicht mit Symbolen, sondern in Worten. Eine typische babylonische Aufgabe lautete etwa: „Ich habe die Fläche und die Seite eines Quadrats addiert und 0;45 erhalten" (in ihrem Sexagesimalsystem). 

Die Ägypter nannten die Unbekannte „aha" (Haufen) und lösten lineare Gleichungen mit einer Methode, die der heutigen „falschen Annahme" ähnelt: Man rät einen Wert, prüft das Ergebnis und korrigiert dann proportional.

Das Wort **Variable** kommt vom lateinischen „variare" (verändern) – eine Variable ist also ein „veränderlicher" Wert, der unterschiedliche Zahlen annehmen kann.

## Was ist eine Gleichung?

Eine **Gleichung** ist eine mathematische Aussage, die behauptet, dass zwei Ausdrücke denselben Wert haben. Die beiden Seiten werden durch ein Gleichheitszeichen (=) verbunden.

Im Alltag begegnen uns Gleichungen ständig, oft ohne dass wir es merken: Wenn wir berechnen, wie viel Wechselgeld wir bekommen sollten, oder wenn wir ausrechnen, wie viele Kilometer wir noch fahren können, bis der Tank leer ist – all das sind im Grunde Gleichungen.

### Bestandteile einer Gleichung

$$\underbrace{3x + 5}_{\text{linke Seite}} = \underbrace{17}_{\text{rechte Seite}}$$

**Elemente**:
- **Linke Seite**: Der Ausdruck links vom Gleichheitszeichen
- **Rechte Seite**: Der Ausdruck rechts vom Gleichheitszeichen
- **Variable** (Unbekannte): Der Buchstabe, dessen Wert gesucht wird (hier: $x$)
- **Koeffizienten**: Zahlen vor der Variablen (hier: 3)
- **Konstanten**: Feste Zahlenwerte (hier: 5 und 17)

## Variablen und Unbekannte

### Begriff der Variablen

Eine **Variable** ist ein Symbol (meist ein Buchstabe), das als Platzhalter für einen noch unbekannten Wert steht.

| Übliche Variablen | Verwendung |
|---|---|
| $x, y, z$ | Standardvariablen |
| $a, b, c$ | Parameter oder Koeffizienten |
| $n, m, k$ | Natürliche Zahlen, Anzahlen |
| $t$ | Zeit |

### Definitionsbereich

Der **Definitionsbereich** $\mathbb{D}$ (auch *Definitionsmenge* oder *Grundmenge*) ist die Menge aller Werte, die man für die Variable **einsetzen darf**. Erst wenn der Definitionsbereich feststeht, ist eine Gleichung vollständig bestimmt – denn er legt fest, welche Einsetzungen überhaupt sinnvoll und erlaubt sind.

Man schreibt ihn meist als $\mathbb{D} = \ldots$ vor oder neben die Gleichung, zum Beispiel:
$$\frac{1}{x} = 2, \quad \mathbb{D} = \mathbb{R} \setminus \{0\}$$

### Warum braucht man den Definitionsbereich?

Nicht jeder Wert ist für jede Gleichung zulässig. Setzt man einen verbotenen Wert ein, entsteht ein undefinierter oder sinnloser Ausdruck. Der Definitionsbereich schließt genau diese Werte von vornherein aus. Das ist aus zwei Gründen wichtig:

- **Mathematisch:** Manche Rechenoperationen sind nur für bestimmte Zahlen definiert (z. B. keine Division durch Null).
- **Inhaltlich (Sachkontext):** In Anwendungsaufgaben sind oft nur bestimmte Zahlen sinnvoll (z. B. keine negative Personenzahl).

### Typische Einschränkungen

| Situation | Bedingung | Ausgeschlossen wird | Beispiel-Definitionsbereich |
|-----------|-----------|---------------------|------------------------------|
| Bruch mit Variable im Nenner | Nenner $\neq 0$ | Nullstellen des Nenners | $\frac{1}{x-2}=5 \Rightarrow \mathbb{D} = \mathbb{R}\setminus\{2\}$ |
| Quadratwurzel mit Variable | Radikand $\geq 0$ | negative Radikanden | $\sqrt{x}=4 \Rightarrow \mathbb{D} = \{x \mid x \geq 0\}$ |
| Logarithmus (später) | Argument $> 0$ | null und negative Werte | $\mathbb{D} = \{x \mid x > 0\}$ |
| Sachaufgabe (Anzahl) | nur sinnvolle Werte | negative/gebrochene Anzahlen | $\mathbb{D} = \mathbb{N}_0$ |

> [!example] Beispiele für Definitionsbereiche
> - Bei $x + 3 = 7$: $\mathbb{D} = \mathbb{R}$ (alle reellen Zahlen erlaubt)
> - Bei $\frac{1}{x} = 2$: $\mathbb{D} = \mathbb{R} \setminus \{0\}$ (Division durch Null ausgeschlossen)
> - Bei $\frac{5}{x-2} = 1$: $\mathbb{D} = \mathbb{R} \setminus \{2\}$ (für $x=2$ wäre der Nenner null)
> - Bei $\sqrt{x} = 4$: $\mathbb{D} = \{x \mid x \geq 0\}$ (keine Wurzel aus negativen Zahlen)
> - Bei Altersberechnungen: $\mathbb{D} = \mathbb{N}_0$ (nur nicht-negative ganze Zahlen sinnvoll)

> [!warning] **Definitionsbereich zuerst bestimmen!**
> Bestimme den Definitionsbereich **immer vor dem Lösen** – nicht erst danach. Sonst kann es passieren, dass du einen Wert als „Lösung" erhältst, der gar nicht eingesetzt werden darf. Solche Werte heißen **Scheinlösungen** und müssen am Ende verworfen werden (siehe Bruchgleichungen).

> [!note] **Zusammenhang mit der Lösungsmenge**
> Der Definitionsbereich sagt, was man einsetzen **darf**; die Lösungsmenge sagt, was die Gleichung tatsächlich **löst**. Die Lösungsmenge ist deshalb immer eine Teilmenge des Definitionsbereichs: $\mathbb{L} \subseteq \mathbb{D}$.

## Lösungen und Lösungsmengen

### Was ist eine Lösung?

Eine **Lösung** einer Gleichung ist ein Wert für die Variable, der die Gleichung zu einer wahren Aussage macht.

> [!example] Beispiel
> Gleichung: $2x + 3 = 11$
> 
> Probe mit $x = 4$:
> $$2 \cdot 4 + 3 = 8 + 3 = 11 \checkmark$$
> 
> Also ist $x = 4$ eine Lösung.

### Lösungsmenge

Die **Lösungsmenge** $\mathbb{L}$ enthält alle Werte aus dem Definitionsbereich, die die Gleichung zu einer wahren Aussage machen. Sie ist damit stets eine Teilmenge des Definitionsbereichs:
$$\mathbb{L} \subseteq \mathbb{D}$$

**Mögliche Fälle**:

| Fall | Beschreibung | Beispiel | Lösungsmenge |
|---|---|---|---|
| Genau eine Lösung | Eindeutig lösbar | $2x = 6$ | $\mathbb{L} = \{3\}$ |
| Unendlich viele Lösungen | Identität | $x + 1 = 1 + x$ | $\mathbb{L} = \mathbb{R}$ |
| Keine Lösung | Widerspruch | $x + 1 = x$ | $\mathbb{L} = \{\}$ |

> [!important] **Die Lösungsmenge hängt vom Definitionsbereich ab**
> Eine Lösungsmenge ist nur zusammen mit dem zugrunde gelegten Definitions- bzw. Grundbereich eindeutig. **Dieselbe Gleichung kann über verschiedenen Grundmengen verschiedene Lösungsmengen haben.** Daher gehört der Definitionsbereich zur vollständigen Angabe einer Lösung dazu.
>
> **Beispiel** $x + 5 = 2$:
> - über $\mathbb{D} = \mathbb{N}$:  $\mathbb{L} = \{\}$ (denn $-3 \notin \mathbb{N}$)
> - über $\mathbb{D} = \mathbb{Z}$:  $\mathbb{L} = \{-3\}$
>
> Man gibt die Lösung deshalb sauber **mit Bezug auf den Definitionsbereich** an, z. B.:
> $$\frac{5}{x-2} = 1, \quad \mathbb{D} = \mathbb{R}\setminus\{2\} \;\Rightarrow\; \mathbb{L} = \{7\}$$

> [!tip] **Grundmenge $\mathbb{G}$ und Definitionsbereich $\mathbb{D}$**
> Genau genommen legt die **Grundmenge $\mathbb{G}$** fest, in welchem Zahlbereich man überhaupt sucht (z. B. $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$), während der **Definitionsbereich $\mathbb{D}$** diese zusätzlich auf die erlaubten Einsetzungen einschränkt (z. B. Nenner $\neq 0$). Die Lösungsmenge wird dann bezogen auf $\mathbb{D}$ angegeben. In der Mittelstufe werden $\mathbb{G}$ und $\mathbb{D}$ oft vereinfachend gleichgesetzt.

## Arten von Gleichungen

### Nach Variablenanzahl

- **Eine Variable**: $3x + 5 = 14$
- **Zwei Variablen**: $2x + 3y = 12$
- **Mehrere Variablen**: $x + y + z = 10$

### Nach höchster Potenz

| Gleichungstyp | Höchste Potenz | Beispiel |
|---|---|---|
| Linear | 1 | $3x + 2 = 8$ |
| Quadratisch | 2 | $x^2 - 4x + 3 = 0$ |
| Kubisch | 3 | $x^3 - x = 0$ |

### Spezielle Gleichungstypen

- **Bruchgleichungen**: Enthalten Variable im Nenner: $\frac{3}{x} = 6$
- **Wurzelgleichungen**: Enthalten Variable unter Wurzel: $\sqrt{x} = 3$
- **Betragsgleichungen**: Enthalten Variable im Betrag: $|x - 2| = 5$

## Das Waagschalen-Prinzip

Eine Gleichung kann als **Waage im Gleichgewicht** verstanden werden. Diese Vorstellung ist nicht nur eine moderne Lehrmethode – schon die alten Ägypter verwendeten Waagen als Symbol für Gerechtigkeit und Ausgewogenheit, und die mathematische Interpretation liegt nahe:

![[gleichung-waage.png]]
*<span class="fig-id">01-08-01-gleichung-waage</span>: Eine Gleichung als Waage im Gleichgewicht – die linke Seite (3x + 5) und die rechte Seite (17) halten sich die Waage; was man auf einer Seite tut, muss man auch auf der anderen tun.*

Das Waagen-Prinzip macht die Grundregel des Gleichungslösens anschaulich: Die Waage bleibt nur im Gleichgewicht, wenn wir auf beiden Seiten dasselbe tun.

**Regeln**:
- Beide Seiten müssen immer gleich behandelt werden
- Was links geschieht, muss auch rechts geschehen
- Das Gleichgewicht darf nie gestört werden

> [!tip] **Merksatz: Die goldene Regel**
> Was du auf der einen Seite tust, musst du auch auf der anderen Seite tun – sonst kippt die Waage! 
>
> Diese Regel ist so fundamental, dass sie die Grundlage aller Äquivalenzumformungen bildet. Ob Addition, Subtraktion, Multiplikation oder Division – die Operation muss immer auf **beide** Seiten angewendet werden.

> [!warning] **Häufiger Fehler**
> Anfänger vergessen oft, eine Operation auf beiden Seiten durchzuführen:
> - **Falsch:** $x + 5 = 12 \Rightarrow x = 12 - 5 + 5 = 12$ (Fehler: rechts nicht subtrahiert)
> - **Richtig:** $x + 5 = 12 \Rightarrow x + 5 - 5 = 12 - 5 \Rightarrow x = 7$

## Zusammenfassung

> [!abstract] Kernpunkte
> - Eine Gleichung ist eine Aussage über die Gleichheit zweier Ausdrücke
> - Die Variable ist der unbekannte Wert, der gesucht wird
> - Die Lösungsmenge enthält alle Werte, die die Gleichung erfüllen
> - Das Waagschalen-Prinzip hilft beim Verständnis von Umformungen

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[02-Aequivalenzumformungen|Äquivalenzumformungen]] – Wie man Gleichungen systematisch löst
- → [[07-Terme-und-algebraische-Ausdruecke/02-Mathematische-Terme|Mathematische Terme]] – Aufbau von Ausdrücken
- → [[04-Lineare-Gleichungen|Lineare Gleichungen]] – Der wichtigste Gleichungstyp

## Übungsaufgaben

1. Bestimme, ob die folgenden Werte Lösungen sind:
   - $x = 3$ für $2x - 1 = 5$
   - $x = -2$ für $3x + 8 = 2$
   - $x = 0$ für $5x = 0$

2. Gib den Definitionsbereich an:
   - $\frac{5}{x-2} = 1$
   - $\sqrt{x} = 4$

3. Klassifiziere die Gleichungen nach Typ:
   - $4x - 7 = 13$
   - $x^2 = 25$
   - $\frac{x+1}{x} = 3$

---

**Navigation**: [[00-Gleichungen-und-Ungleichungen-Index|← Übersicht]] | [[02-Aequivalenzumformungen|Äquivalenzumformungen →]]
