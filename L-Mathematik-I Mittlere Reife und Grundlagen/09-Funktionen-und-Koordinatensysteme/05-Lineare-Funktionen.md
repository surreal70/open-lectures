---
title: "Lineare Funktionen"
created: 2026-10-13
modified: 2026-10-19
chapter: "09"
section: "05"
status: "draft - review pending"
type: lecture
keywords:
  - Lineare Funktion
  - Gerade
  - Steigung
  - y-Achsenabschnitt
  - Proportionalität
---

# Lineare Funktionen

> [!info] Lernziele
> - Lineare Funktionen erkennen und beschreiben
> - Den Graphen als Gerade identifizieren
> - Steigung und y-Achsenabschnitt aus der Gleichung ablesen
> - Den Unterschied zwischen proportionalen und allgemeinen linearen Funktionen verstehen

## Definition

Eine **lineare Funktion** hat die allgemeine Form:

$$f(x) = mx + b$$

| Parameter | Bedeutung | Andere Namen |
|---|---|---|
| $m$ | **Steigung** | Anstieg, Steigungsfaktor |
| $b$ | **y-Achsenabschnitt** | Ordinatenabschnitt |

> [!note] Eigenschaft
> Der Graph einer linearen Funktion ist immer eine **Gerade**. Daher auch der Name „linear" – von lateinisch *linea* (Linie).

> [!info] **Warum sind lineare Funktionen so wichtig?**
> Lineare Funktionen sind die einfachsten und zugleich häufigsten Funktionen in der Praxis:
> - **Telefonrechnung**: Grundgebühr + Kosten pro Minute
> - **Taxifahrt**: Grundpreis + Kosten pro Kilometer
> - **Lohn**: Stundenlohn × Arbeitsstunden (bei gleichem Stundensatz)
> - **Temperaturumrechnung**: Celsius ↔ Fahrenheit
>
> Selbst komplizierte Zusammenhänge werden oft durch lineare Funktionen angenähert – eine Technik, die in Wissenschaft und Technik als „Linearisierung" bekannt ist.

## Proportionale Funktionen (Sonderfall)

Wenn $b = 0$, heißt die Funktion **proportional** oder **direkt proportional**:

$$f(x) = mx$$

**Eigenschaften**:
- Die Gerade geht durch den **Ursprung** $(0, 0)$
- $f(x)$ ist proportional zu $x$
- Verdoppelt sich $x$, verdoppelt sich auch $f(x)$

Der y-Achsenabschnitt $b = 0$ bedeutet anschaulich: Es gibt keinen „Startwert" oder „Grundbetrag". Beim Einkauf etwa ist der Gesamtpreis bei einem festen Stückpreis proportional zur Menge – kaufst du nichts, zahlst du nichts. Sobald aber ein fester Zusatzbetrag hinzukommt (z. B. eine Grundgebühr oder Versandkosten), ist $b \neq 0$ und die Funktion ist zwar noch linear, aber **nicht mehr proportional**. Mehr dazu in [[../05-Verhaeltnisse-und-Proportionalitaet/04-Direkte-Proportionalitaet|Direkte Proportionalität]].

> [!example] Beispiel
> $f(x) = 3x$
> 
> | $x$ | 1 | 2 | 3 | 4 |
> |---|---|---|---|---|
> | $f(x)$ | 3 | 6 | 9 | 12 |
> 
> Der Quotient $\frac{f(x)}{x} = 3$ ist konstant.

## Steigung $m$

Die **Steigung** gibt an, um wie viel der y-Wert zunimmt, wenn x um 1 zunimmt. Sie ist das Maß dafür, wie „schräg" die Gerade verläuft.

Anschaulich ist die Steigung wie die **Neigung einer Straße oder Rampe**: Eine Steigung von $m = 0{,}1$ bedeutet, dass es pro Meter in der Waagerechten um 10 cm nach oben geht – eine flache Rampe. Je größer $m$, desto steiler. Genau diese Vorstellung steckt auch hinter den Prozentangaben auf Verkehrsschildern („12 % Steigung"). Bei linearen Funktionen ist diese Neigung **überall gleich** – das ist der Grund, warum der Graph eine Gerade und keine Kurve ist.

### Interpretation

| Steigung | Bedeutung | Graph |
|---|---|---|
| $m > 0$ | Funktion steigt | von links unten nach rechts oben |
| $m < 0$ | Funktion fällt | von links oben nach rechts unten |
| $m = 0$ | konstant | horizontale Gerade |
| $|m|$ groß | steile Gerade | |
| $|m|$ klein | flache Gerade | |

### Grafische Darstellung

![[steigung-vorzeichen.png]]
*<span class="fig-id">01-09-05-steigung-vorzeichen</span>: Bei positiver Steigung ($m > 0$) verläuft die Gerade von links unten nach rechts oben (steigend), bei negativer Steigung ($m < 0$) von links oben nach rechts unten (fallend).*

### Berechnung der Steigung

Aus zwei Punkten $P_1(x_1, y_1)$ und $P_2(x_2, y_2)$:

$$m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{\Delta y}{\Delta x}$$

Hinter dieser Formel steckt das **Steigungsdreieck**: $\Delta x$ (gesprochen „Delta x") ist der waagerechte Abstand der beiden Punkte, $\Delta y$ der senkrechte. Man geht also von $P_1$ aus ein Stück nach rechts ($\Delta x$) und dann nach oben oder unten ($\Delta y$) bis zu $P_2$. Das Verhältnis „Höhenunterschied durch waagerechte Strecke" ist die Steigung. Weil die Gerade überall gleich geneigt ist, liefert **jedes** Steigungsdreieck entlang der Geraden denselben Wert $m$ – egal, wie groß du es wählst.

> [!warning] **Reihenfolge beachten**
> Die Punkte müssen in Zähler und Nenner in **derselben Reihenfolge** eingesetzt werden. Wenn oben $y_2 - y_1$ steht, muss unten $x_2 - x_1$ stehen – nicht $x_1 - x_2$. Sonst erhältst du das falsche Vorzeichen.

> [!example] Beispiel
> $P_1(1, 2)$ und $P_2(4, 8)$
> 
> $$m = \frac{8 - 2}{4 - 1} = \frac{6}{3} = 2$$
>
> Deutung: Von $P_1$ nach $P_2$ geht es $\Delta x = 3$ nach rechts und $\Delta y = 6$ nach oben. Pro Schritt nach rechts steigt die Gerade also um $2$.

## y-Achsenabschnitt $b$

Der **y-Achsenabschnitt** ist der y-Wert, an dem die Gerade die y-Achse schneidet.

$$b = f(0)$$

> [!example] Beispiel
> $f(x) = 2x + 3$
> 
> $f(0) = 2 \cdot 0 + 3 = 3$
> 
> Die Gerade schneidet die y-Achse bei $(0, 3)$.

## Beispiele linearer Funktionen

### Verschiedene Steigungen

![[verschiedene-steigungen.png]]
*<span class="fig-id">01-09-05-verschiedene-steigungen</span>: Drei Ursprungsgeraden mit unterschiedlichen Steigungen – je größer $m$, desto steiler die Gerade ($m = 2$ steiler als $m = 1$ steiler als $m = 0{,}5$).*

### Verschiedene y-Achsenabschnitte

![[verschiedene-achsenabschnitte.png]]
*<span class="fig-id">01-09-05-verschiedene-achsenabschnitte</span>: Drei Geraden mit gleicher Steigung ($m = 1$), aber unterschiedlichem y-Achsenabschnitt – sie sind parallel und gegeneinander verschoben: $f$ schneidet die y-Achse bei $3$, $g$ bei $1$, $h$ bei $-2$.*

> [!note] Beobachtung
> Geraden mit **gleicher Steigung** sind **parallel** zueinander. Sie verlaufen in dieselbe Richtung, schneiden sich aber nie (außer sie sind identisch).

> [!warning] **Häufiger Fehler**
> Die Steigung $m$ wird oft mit dem y-Achsenabschnitt $b$ verwechselt. Merke: $m$ steht **vor** dem $x$ (Multiplikation), $b$ steht **alleine** (Addition). In $f(x) = 3x + 5$ ist $m = 3$ und $b = 5$, nicht umgekehrt!

## Gleichung aufstellen

### Aus Steigung und y-Achsenabschnitt

Gegeben: $m = 2$, $b = -1$

$$f(x) = 2x - 1$$

### Aus zwei Punkten

1. Steigung berechnen: $m = \frac{y_2 - y_1}{x_2 - x_1}$
2. Einen Punkt einsetzen und $b$ berechnen
3. Gleichung aufstellen

> [!example] Beispiel
> $P_1(2, 5)$ und $P_2(4, 9)$
> 
> **Schritt 1**: $m = \frac{9 - 5}{4 - 2} = \frac{4}{2} = 2$
> 
> **Schritt 2**: $f(x) = 2x + b$, mit $P_1$: $5 = 2 \cdot 2 + b$ → $b = 1$
> 
> **Schritt 3**: $f(x) = 2x + 1$

## Nullstelle

Die **Nullstelle** ist der x-Wert, an dem $f(x) = 0$.

$$mx + b = 0$$
$$x = -\frac{b}{m}$$

> [!example] Beispiel
> $f(x) = 3x - 6$
> 
> $3x - 6 = 0$
> $x = 2$
> 
> Die Gerade schneidet die x-Achse bei $(2, 0)$.

## Zusammenfassung

> [!abstract] Kernpunkte
> - Lineare Funktionen: $f(x) = mx + b$
> - Der Graph ist eine Gerade
> - $m$ = Steigung (positiv: steigend, negativ: fallend)
> - $b$ = y-Achsenabschnitt (wo die Gerade die y-Achse schneidet)
> - Proportionale Funktionen gehen durch den Ursprung ($b = 0$)
> - Parallele Geraden haben die gleiche Steigung

## Zusammenhänge

Lineare Funktionen sind verbunden mit:

- → [[06-Steigung-und-Achsenabschnitt|Steigung und Achsenabschnitt]] – Detaillierte Analyse der Parameter
- → [[07-Geradengleichungen|Geradengleichungen]] – Gleichungen aus Punkten aufstellen
- → [[../05-Verhaeltnisse-und-Proportionalitaet/04-Direkte-Proportionalitaet|Direkte Proportionalität]] – Zusammenhang zu proportionalen Funktionen
- → [[10-Schnittpunkte|Schnittpunkte]] – Wo sich Geraden schneiden
- → [[11-Anwendungen-Funktionen|Anwendungen]] – Praktische Nutzung linearer Funktionen

## Übungsaufgaben

1. Gib Steigung und y-Achsenabschnitt an:
   - $f(x) = 4x + 2$
   - $g(x) = -2x + 5$
   - $h(x) = \frac{1}{2}x$

2. Zeichne die Graphen von $f(x) = 2x - 3$ und $g(x) = -x + 1$.

3. Bestimme die Gleichung der Geraden durch:
   - $P(0, 4)$ mit Steigung $m = 3$
   - $A(1, 3)$ und $B(3, 7)$

4. Berechne die Nullstelle von:
   - $f(x) = 5x - 15$
   - $g(x) = -2x + 8$

---

**Navigation**: [[04-Funktionstabellen-und-Graphen|← Funktionstabellen]] | [[00-Funktionen-Index|Übersicht]] | [[06-Steigung-und-Achsenabschnitt|Steigung und Achsenabschnitt →]]
