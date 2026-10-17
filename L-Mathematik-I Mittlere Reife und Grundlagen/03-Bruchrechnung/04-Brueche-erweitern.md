---
author: Andreas Hümmer
title: Brüche erweitern
status: draft - review pending
tags:
  - content
  - mathematik
  - bruchrechnung
created: 2026-10-13
modified: 2026-10-16
---

# Brüche erweitern

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Brüche mit beliebigen Faktoren erweitern können
> - Verstehen, warum der Wert beim Erweitern gleich bleibt
> - Brüche auf einen gemeinsamen Nenner bringen können

---

## Überblick

Beim **Erweitern** eines Bruchs werden Zähler und Nenner mit derselben Zahl multipliziert. Der Wert des Bruchs bleibt dabei unverändert – nur die Darstellung ändert sich.

Dieses Konzept ist fundamental für die Bruchrechnung: Ohne Erweitern könnten wir Brüche mit verschiedenen Nennern nicht addieren oder subtrahieren. Die Idee dahinter ist einfach: Wenn wir einen Kuchen feiner schneiden (mehr Teile), aber entsprechend mehr Stücke nehmen, haben wir immer noch dieselbe Menge Kuchen.

Das Erweitern ist eng verwandt mit dem Konzept der **Äquivalenz**: Verschiedene Brüche können denselben Wert darstellen. $\frac{1}{2}$, $\frac{2}{4}$, $\frac{3}{6}$ und $\frac{50}{100}$ sind alle gleichwertig – sie bezeichnen alle „die Hälfte".

---

## Definition

$$\frac{a}{b} = \frac{a \cdot n}{b \cdot n} \quad \text{für } n \neq 0$$

**Beispiel:** $\frac{2}{3}$ erweitern mit 4:

$$\frac{2}{3} = \frac{2 \cdot 4}{3 \cdot 4} = \frac{8}{12}$$

> [!note] **Was bedeutet „erweitern"?**
> Der Name kommt daher, dass die Zahlen im Bruch „größer" (erweitert) werden – aber der Bruch selbst bleibt gleich groß! Es ist wie bei einem Foto: Wenn du ein Bild vergrößerst, werden die Pixel mehr, aber das Motiv bleibt dasselbe.

---

## Visualisierung

$\frac{1}{2}$ erweitert auf $\frac{2}{4}$:

![[bruch-erweitern.png]]
*<span class="fig-id">01-03-04-bruch-erweitern</span>: Erweitern von ½ auf 2/4 – dieselbe Fläche, nur feiner unterteilt: links 1 von 2 Teilen, rechts 2 von 4 Teilen gefüllt.*

Beide zeigen dieselbe Menge – nur feiner unterteilt! Das linke Rechteck ist in 2 Teile geteilt, davon ist 1 gefüllt. Das rechte ist in 4 Teile geteilt, davon sind 2 gefüllt. Die gefüllte Fläche ist identisch.

> [!tip] **Anschauliche Vorstellung**
> Stell dir vor, du schneidest ein Pizzastück ($\frac{1}{2}$) in der Mitte durch. Jetzt hast du 2 kleinere Stücke, aber zusammen sind sie genauso viel Pizza wie vorher. Aus $\frac{1}{2}$ wurde $\frac{2}{4}$ – der Wert hat sich nicht geändert.

---

## Warum bleibt der Wert gleich?

Erweitern entspricht der Multiplikation mit 1:

$$\frac{a}{b} \cdot \frac{n}{n} = \frac{a}{b} \cdot 1 = \frac{a}{b}$$

Da $\frac{n}{n} = 1$ ist, ändert sich der Wert nicht.

> [!note] **Mathematische Begründung**
> Die Multiplikation mit 1 verändert keine Zahl: $5 \cdot 1 = 5$, $\frac{2}{3} \cdot 1 = \frac{2}{3}$.
> 
> Da $\frac{4}{4} = 1$, $\frac{7}{7} = 1$, $\frac{100}{100} = 1$ gilt, ist Erweitern nichts anderes als geschicktes Multiplizieren mit 1.

Dies ist auch der Grund, warum wir nur mit Zahlen ≠ 0 erweitern dürfen: $\frac{0}{0}$ ist nicht definiert!

---

## Beispiele

| Ursprung | Erweitern mit | Ergebnis |
|----------|---------------|----------|
| $\frac{1}{4}$ | 3 | $\frac{3}{12}$ |
| $\frac{2}{5}$ | 2 | $\frac{4}{10}$ |
| $\frac{3}{7}$ | 5 | $\frac{15}{35}$ |

### Auf einen bestimmten Nenner erweitern

Manchmal müssen wir einen Bruch auf einen vorgegebenen Nenner bringen. Dann fragen wir: „Mit welcher Zahl muss ich den Nenner multiplizieren, um den gewünschten Nenner zu erhalten?"

**Beispiel:** Erweitere $\frac{3}{4}$ auf Nenner 20.
- Frage: $4 \cdot ? = 20$
- Antwort: $4 \cdot 5 = 20$
- Also: $\frac{3}{4} = \frac{3 \cdot 5}{4 \cdot 5} = \frac{15}{20}$

> [!warning] **Häufiger Fehler**
> Nur den Nenner erweitern, den Zähler vergessen:
>
> **Falsch:** $\frac{3}{4} = \frac{3}{20}$ ✗ (nur der Nenner wurde verändert)
>
> **Richtig:** $\frac{3}{4} = \frac{15}{20}$ ✓ (Zähler UND Nenner mit 5 multipliziert)

---

## Anwendung: Gemeinsamer Nenner

Um Brüche zu addieren, müssen sie den gleichen Nenner haben. Hier zeigt sich der praktische Nutzen des Erweiterns:

**Beispiel:** $\frac{1}{3} + \frac{1}{4}$

- $\frac{1}{3}$ erweitern mit 4: $\frac{4}{12}$
- $\frac{1}{4}$ erweitern mit 3: $\frac{3}{12}$
- Jetzt addieren: $\frac{4}{12} + \frac{3}{12} = \frac{7}{12}$

Beide Brüche wurden so erweitert, dass sie den gemeinsamen Nenner 12 haben. Erst dann konnten wir die Zähler addieren.

> [!tip] **Alltagsbeispiel**
> Stell dir vor, du möchtest $\frac{1}{3}$ kg Äpfel und $\frac{1}{4}$ kg Birnen wiegen. Die Waage zeigt aber nur Zwölftel-Kilo an. Also rechnest du um:
> - $\frac{1}{3}$ kg = $\frac{4}{12}$ kg
> - $\frac{1}{4}$ kg = $\frac{3}{12}$ kg
> - Zusammen: $\frac{7}{12}$ kg

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[05-Brueche-kuerzen|Brüche kürzen]] – Die Umkehrung des Erweiterns
- → [[06-Hauptnenner-bestimmen|Hauptnenner bestimmen]] – Den kleinsten gemeinsamen Nenner finden
- → [[07-Addition-von-Bruechen|Addition von Brüchen]] – Wo Erweitern gebraucht wird

> [!warning] **Prüfungsrelevant**
> - Erweitern: Zähler UND Nenner mit derselben Zahl multiplizieren
> - Der Wert bleibt gleich
> - Notwendig, um Brüche auf gleichen Nenner zu bringen

> [!question] **Typische Prüfungsfragen**
> - Erweitere $\frac{3}{5}$ auf Nenner 20.
> - Warum ist $\frac{2}{3} = \frac{8}{12}$?

## Quellen

- Padberg, Friedhelm: *Didaktik der Bruchrechnung*. Springer, 2009.
