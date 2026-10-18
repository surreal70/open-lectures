---
title: "Lineare Gleichungen"
created: 2026-10-13
modified: 2026-10-16
chapter: "08"
section: "04"
status: final
type: lecture
keywords:
  - Lineare Gleichung
  - Erste Grades
  - Lösung
  - Normalform
---

# Lineare Gleichungen

> [!info] Lernziele
> - Lineare Gleichungen erkennen und in Normalform bringen
> - Systematisch lineare Gleichungen lösen können
> - Sonderfälle (keine Lösung, unendlich viele Lösungen) identifizieren
> - Lösungen verifizieren

## Historischer Kontext

Lineare Gleichungen sind die ältesten und grundlegendsten algebraischen Gleichungen. Schon die **alten Ägypter** (ca. 1650 v. Chr.) lösten im Papyrus Rhind lineare Gleichungen – allerdings mit der „Methode der falschen Annahme": Man rät einen Wert, prüft das Ergebnis und korrigiert proportional.

Der Name „linear" kommt vom lateinischen „linea" (Linie), weil die grafische Darstellung einer linearen Gleichung $ax + b = c$ im Koordinatensystem eine **Gerade** (Linie) ergibt. Diese Verbindung zwischen Algebra und Geometrie wurde erst im 17. Jahrhundert durch René Descartes systematisch erforscht.

> [!tip] **Alltagsrelevanz**
> Lineare Gleichungen begegnen uns überall:
> - **Einkaufen**: „3 Äpfel kosten 4,50 €. Was kostet ein Apfel?" → $3x = 4{,}50$
> - **Reisen**: „Wie lange brauche ich für 180 km bei 60 km/h?" → $60t = 180$
> - **Finanzen**: „Wie viel muss ich sparen, wenn ich 500 € habe und 800 € brauche?" → $500 + x = 800$

## Definition

Eine **lineare Gleichung** (Gleichung ersten Grades) ist eine Gleichung, in der die Variable nur in der ersten Potenz vorkommt. Der Name „ersten Grades" bezieht sich auf den höchsten Exponenten der Variablen, der hier 1 ist (also $x^1 = x$).

### Normalform

$$ax + b = 0 \quad \text{mit } a \neq 0$$

- $a$: Koeffizient der Variablen
- $b$: Konstante
- $x$: Variable

### Allgemeine Form

$$ax + b = cx + d$$

> [!example] Beispiele für lineare Gleichungen
> - $3x + 5 = 14$ ✓
> - $2x - 7 = x + 3$ ✓
> - $\frac{x}{4} = 8$ ✓
> - $x^2 + 3 = 12$ ✗ (quadratisch)

## Lösungsverfahren

Der große Vorteil linearer Gleichungen ist, dass sich alle nach demselben festen Schema lösen lassen. Man muss nicht raten oder probieren wie die alten Ägypter, sondern kann Schritt für Schritt vorgehen, bis die Variable allein steht. Dieses Standardvorgehen funktioniert unabhängig davon, ob Klammern, Brüche oder Dezimalzahlen auftreten – die folgenden Beispiele zeigen es in steigender Schwierigkeit.

### Standardvorgehen

1. Vereinfachen (Klammern auflösen, zusammenfassen)
2. Alle Terme mit $x$ auf eine Seite bringen
3. Alle Konstanten auf die andere Seite bringen
4. Durch den Koeffizienten von $x$ dividieren
5. Probe durchführen

### Beispiel 1: Einfache lineare Gleichung

$$5x - 3 = 22$$

$$5x = 25 \quad | +3$$
$$x = 5 \quad | :5$$

**Probe**: $5 \cdot 5 - 3 = 25 - 3 = 22$ ✓

### Beispiel 2: Variable auf beiden Seiten

$$7x - 4 = 3x + 12$$

$$7x - 3x = 12 + 4 \quad | -3x, +4$$
$$4x = 16$$
$$x = 4 \quad | :4$$

**Probe**: $7 \cdot 4 - 4 = 28 - 4 = 24$ und $3 \cdot 4 + 12 = 12 + 12 = 24$ ✓

### Beispiel 3: Mit Brüchen

$$\frac{2x}{3} + 1 = 5$$

$$\frac{2x}{3} = 4 \quad | -1$$
$$2x = 12 \quad | \cdot 3$$
$$x = 6 \quad | :2$$

**Probe**: $\frac{2 \cdot 6}{3} + 1 = \frac{12}{3} + 1 = 4 + 1 = 5$ ✓

## Sonderfälle

Nicht jede lineare Gleichung führt auf genau eine Zahl als Lösung. Manchmal fällt die Variable beim Umformen vollständig weg, und zurück bleibt eine reine Aussage über Zahlen. Ob diese Aussage wahr oder falsch ist, entscheidet dann über die Lösungsmenge. Es lohnt sich, diese beiden Sonderfälle zu kennen, damit man sie beim Rechnen nicht als Fehler missversteht.

### Fall 1: Keine Lösung (Widerspruch)

$$2x + 5 = 2x - 3$$
$$5 = -3 \quad | -2x$$

Diese Aussage ist **falsch** – die Gleichung hat **keine Lösung**.

$$\mathbb{L} = \{\} = \emptyset$$

> [!note] Interpretation
> Es gibt keinen Wert für $x$, der die Gleichung erfüllen kann. Die Gleichung ist ein **Widerspruch**.

### Fall 2: Unendlich viele Lösungen (Identität)

$$3x + 6 = 3(x + 2)$$
$$3x + 6 = 3x + 6$$
$$0 = 0 \quad | -3x, -6$$

Diese Aussage ist **immer wahr** – jeder Wert für $x$ ist eine Lösung.

$$\mathbb{L} = \mathbb{R}$$

> [!note] Interpretation
> Die Gleichung ist eine **Identität** – beide Seiten sind für alle $x$ gleich.

### Übersicht der Fälle

| Ergebnis | Bedeutung | Lösungsmenge |
|---|---|---|
| $x = \text{Zahl}$ | Eindeutige Lösung | $\mathbb{L} = \{\text{Zahl}\}$ |
| Wahre Aussage ($0 = 0$) | Identität | $\mathbb{L} = \mathbb{R}$ |
| Falsche Aussage ($5 = 3$) | Widerspruch | $\mathbb{L} = \emptyset$ |

## Komplexere Beispiele

Auch wenn Brüche oder Dezimalzahlen auftauchen, ändert sich am Grundprinzip nichts. Es kommt lediglich ein vorbereitender Schritt hinzu: Man beseitigt zunächst die Brüche oder Kommas und bringt die Gleichung damit auf eine einfache Form, die sich dann wie gewohnt lösen lässt. Die folgenden beiden Beispiele zeigen genau diesen Zwischenschritt.

### Mit mehreren Brüchen

$$\frac{x-1}{2} + \frac{x+3}{4} = 3$$

**Schritt 1**: Hauptnenner bestimmen (hier: 4)

$$\frac{2(x-1)}{4} + \frac{x+3}{4} = 3$$

**Schritt 2**: Mit Hauptnenner multiplizieren

$$2(x-1) + (x+3) = 12$$

**Schritt 3**: Auflösen und vereinfachen

$$2x - 2 + x + 3 = 12$$
$$3x + 1 = 12$$
$$3x = 11$$
$$x = \frac{11}{3}$$

### Mit Dezimalzahlen

$$0{,}5x + 1{,}2 = 2{,}7$$

**Tipp**: Mit 10 multiplizieren, um Dezimalzahlen zu eliminieren

$$5x + 12 = 27$$
$$5x = 15$$
$$x = 3$$

## Strategien und Tipps

> [!tip] **Praktische Hinweise**
> - **Brüche vermeiden**: Früh mit dem Hauptnenner multiplizieren – das macht die Rechnung übersichtlicher
> - **Dezimalzahlen**: Mit passender Zehnerpotenz multiplizieren (z.B. $\cdot 10$ bei einer Nachkommastelle)
> - **Vorzeichen**: Besonders beim Minuszeichen vor Klammern aufpassen – hier passieren die meisten Fehler
> - **Probe**: Immer in die Originalgleichung einsetzen, nicht in Zwischenschritte

> [!warning] **Häufiger Fehler: Vorzeichenfehler**
> Der häufigste Fehler bei linearen Gleichungen ist das falsche Vorzeichen:
> - **Falsch:** $5x - 3 = 2x + 9 \Rightarrow 5x + 2x = 9 + 3$ 
> - **Richtig:** $5x - 3 = 2x + 9 \Rightarrow 5x - 2x = 9 + 3$
>
> Merke: Beim Übertragen auf die andere Seite wechselt das Vorzeichen!

## Zusammenfassung

> [!abstract] Kernpunkte
> - Lineare Gleichungen haben die Variable nur in der 1. Potenz
> - Lösung durch systematisches Isolieren der Variablen
> - Drei mögliche Fälle: eine Lösung, keine Lösung, unendlich viele Lösungen
> - Bei Brüchen: Mit Hauptnenner multiplizieren
> - Probe sichert das Ergebnis ab

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[02-Aequivalenzumformungen|Äquivalenzumformungen]] – Die Werkzeuge zum Lösen
- → [[05-Gleichungen-mit-Klammern|Gleichungen mit Klammern]] – Erweiterung mit Klammern
- → [[07-Lineare-Ungleichungen|Lineare Ungleichungen]] – Ähnlich, aber mit Ungleichheitszeichen
- → [[09-Funktionen-und-Koordinatensysteme/05-Lineare-Funktionen|Lineare Funktionen]] – Grafische Darstellung

## Übungsaufgaben

Löse die folgenden linearen Gleichungen:

1. $4x + 9 = 25$
2. $6x - 5 = 2x + 11$
3. $3(x - 4) = 2x + 1$
4. $\frac{x}{3} + \frac{x}{6} = 5$
5. $5(x + 1) = 5x + 7$
6. $0{,}25x - 0{,}5 = 1{,}5$

---

**Navigation**: [[03-Ueberpruefung-von-Loesungen|← Überprüfung]] | [[00-Gleichungen-und-Ungleichungen-Index|Übersicht]] | [[05-Gleichungen-mit-Klammern|Gleichungen mit Klammern →]]
