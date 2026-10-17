---
author: Andreas Hümmer
title: Reelle Zahlen – eine erste Einführung
status: final
tags:
  - content
  - mathematik
  - zahlenmengen
  - reelle-zahlen
created: 2026-10-13
modified: 2026-10-16
---

# Reelle Zahlen – eine erste Einführung

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Menge der reellen Zahlen $\mathbb{R}$ kennen
> - Den Unterschied zwischen rationalen und irrationalen Zahlen verstehen
> - Beispiele für irrationale Zahlen nennen können
> - Verstehen, warum $\mathbb{R}$ den Zahlenstrahl „vollständig" füllt

---

## Überblick

Die reellen Zahlen umfassen alle Zahlen, die auf dem Zahlenstrahl liegen. Sie entstehen durch die Erweiterung der rationalen Zahlen um die **irrationalen Zahlen** – Zahlen, die sich nicht als Bruch darstellen lassen. Damit wird der Zahlenstrahl „lückenlos" gefüllt.

Die Entdeckung irrationaler Zahlen war für die antiken Griechen ein Schock. Die Pythagoreer glaubten, dass sich alle Verhältnisse in der Natur durch ganze Zahlen oder deren Quotienten ausdrücken ließen. Als sie entdeckten, dass die Diagonale eines Quadrats mit Seitenlänge 1 nicht als Bruch darstellbar ist (sie entspricht $\sqrt{2}$), erschütterte dies ihr Weltbild zutiefst. Der Legende nach wurde der Entdecker Hippasus für diese „ketzerische" Erkenntnis aus der pythagoreischen Gemeinschaft ausgestoßen.

---

## Definition der reellen Zahlen

Die **reellen Zahlen** $\mathbb{R}$ umfassen alle Zahlen auf dem Zahlenstrahl:

$$\mathbb{R} = \mathbb{Q} \cup \text{(irrationale Zahlen)}$$

Sie setzen sich zusammen aus:
- **Rationale Zahlen** $\mathbb{Q}$: Alle Brüche – also abbrechende oder periodische Dezimalzahlen
- **Irrationale Zahlen**: Alle nicht-abbrechenden, nicht-periodischen Dezimalzahlen

Der Name „reell" (von lat. „res" = Sache, Ding) soll ausdrücken, dass diese Zahlen „wirkliche" Punkte auf einer Geraden beschreiben – im Gegensatz zu den später eingeführten „imaginären" Zahlen.

---

## Die Zahlenmengenhierarchie

Die verschiedenen Zahlenmengen bauen wie Matroschka-Puppen aufeinander auf:

![[zahlenmengen-hierarchie.png]]
*<span class="fig-id">01-01-06-zahlenmengen-hierarchie</span>: Die Zahlenmengen bauen wie Matroschka-Puppen aufeinander auf – jede Erweiterung umschließt die vorherige: ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ.*

Die Hierarchie als mathematische Formel:

$$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$$

Jede Stufe erweitert die vorherige: Die natürlichen Zahlen werden zu den ganzen Zahlen (durch Hinzunahme von 0 und negativen Zahlen), die ganzen zu den rationalen (durch Hinzunahme der Brüche), und die rationalen zu den reellen (durch Hinzunahme der irrationalen Zahlen).

---

## Irrationale Zahlen

**Irrationale Zahlen** sind reelle Zahlen, die sich **nicht** als Bruch zweier ganzer Zahlen darstellen lassen. Das Wort „irrational" kommt vom lateinischen „irrationalis" und bedeutet ursprünglich „ohne Verhältnis" – diese Zahlen können nicht als Verhältnis (ratio) ganzer Zahlen geschrieben werden.

### Eigenschaften irrationaler Zahlen

| Eigenschaft | Bedeutung | Beispiel |
|-------------|-----------|----------|
| Nicht-abbrechend | Die Dezimaldarstellung hat unendlich viele Stellen | $\sqrt{2} = 1{,}41421356...$ |
| Nicht-periodisch | Keine Ziffernfolge wiederholt sich endlos | Bei $\pi$ gibt es kein Muster |
| Nicht als Bruch | Kein $\frac{p}{q}$ mit $p, q \in \mathbb{Z}$ existiert | $\sqrt{2} \neq \frac{a}{b}$ für alle ganzen $a, b$ |

### Berühmte irrationale Zahlen

Die Mathematik kennt viele wichtige irrationale Zahlen, die in verschiedenen Kontexten auftreten:

| Zahl | Symbol | Ungefährer Wert | Bedeutung und Vorkommen |
|------|--------|-----------------|-------------------------|
| Wurzel aus 2 | $\sqrt{2}$ | $1{,}41421356...$ | Diagonale im Einheitsquadrat; verhältnis von Bildschirmdiagonale zu Seite bei DIN-Format |
| Kreiszahl | $\pi$ | $3{,}14159265...$ | Verhältnis von Kreisumfang zu Durchmesser; überall in der Mathematik präsent |
| Eulersche Zahl | $e$ | $2{,}71828182...$ | Basis des natürlichen Logarithmus; beschreibt exponentielles Wachstum |
| Goldener Schnitt | $\varphi$ | $1{,}61803398...$ | $\frac{1+\sqrt{5}}{2}$; harmonische Proportionen in Kunst und Natur |

> [!note] **Die Kreiszahl $\pi$**
> $\pi$ ist vielleicht die berühmteste Zahl der Mathematik. Sie gibt an, wie oft der Durchmesser eines Kreises in seinen Umfang passt – und dieses Verhältnis ist für jeden Kreis gleich, egal wie groß oder klein er ist. Die Ziffernfolge von $\pi$ wurde mittlerweile auf Billionen von Nachkommastellen berechnet, ohne dass ein Muster erkennbar wurde.

---

## Beweis: $\sqrt{2}$ ist irrational

Der Beweis, dass $\sqrt{2}$ irrational ist, ist einer der ältesten und schönsten der Mathematik. Er verwendet die Methode des **Widerspruchsbeweises**: Man nimmt das Gegenteil an und zeigt, dass dies zu einem logischen Widerspruch führt.

> [!example] **Beweis (Widerspruchsbeweis)**
> **Annahme:** Nehmen wir an, $\sqrt{2}$ wäre rational. Dann ließe sie sich als Bruch $\sqrt{2} = \frac{p}{q}$ schreiben, wobei $p, q \in \mathbb{Z}$, $q \neq 0$, und der Bruch vollständig gekürzt ist (kein gemeinsamer Teiler).
>
> **Schritt 1: Quadrieren**
> $$\sqrt{2} = \frac{p}{q} \implies 2 = \frac{p^2}{q^2} \implies p^2 = 2q^2$$
>
> **Schritt 2: p ist gerade**
> Da $p^2 = 2q^2$, ist $p^2$ durch 2 teilbar, also gerade.
> Wenn $p^2$ gerade ist, muss auch $p$ gerade sein (das Quadrat einer ungeraden Zahl ist ungerade).
> Also: $p = 2k$ für eine ganze Zahl $k$.
>
> **Schritt 3: q ist auch gerade**
> Einsetzen in $p^2 = 2q^2$:
> $$(2k)^2 = 2q^2 \implies 4k^2 = 2q^2 \implies q^2 = 2k^2$$
> Also ist auch $q^2$ gerade, und damit $q$ gerade.
>
> **Widerspruch:** Wenn $p$ und $q$ beide gerade sind, haben sie den gemeinsamen Teiler 2. Aber wir hatten angenommen, der Bruch sei vollständig gekürzt!
>
> **Fazit:** Die Annahme, $\sqrt{2}$ sei rational, führt zu einem Widerspruch. Also muss $\sqrt{2}$ irrational sein.

Dieser Beweis zeigt, dass es Punkte auf dem Zahlenstrahl gibt, die von keiner rationalen Zahl getroffen werden – eine tiefgreifende Erkenntnis.

---

## Wo begegnen uns irrationale Zahlen?

Irrationale Zahlen sind keine mathematische Kuriosität, sondern treten in der realen Welt häufig auf.

### In der Geometrie

| Figur | Irrationale Länge | Herleitung |
|-------|-------------------|------------|
| Einheitsquadrat | Diagonale: $\sqrt{2} \approx 1{,}414$ | Pythagoras: $1^2 + 1^2 = d^2$ |
| Gleichseitiges Dreieck (Seite 2) | Höhe: $\sqrt{3} \approx 1{,}732$ | Pythagoras im halbierten Dreieck |
| Kreis (Durchmesser 1) | Umfang: $\pi \approx 3{,}14$ | Definition von $\pi$ |
| Goldenes Rechteck | Seitenverhältnis: $\varphi \approx 1{,}618$ | Goldener Schnitt |
| Pentagon | Diagonale zu Seite: $\varphi$ | Regelmäßiges Fünfeck |

### In der Natur

Die Natur „verwendet" irrationale Zahlen an vielen Stellen:

- **Spiralen**: Schneckenhäuser, Galaxien und die Anordnung von Sonnenblumenkernen folgen oft Mustern, die mit dem goldenen Schnitt $\varphi$ zusammenhängen
- **Kreise**: Räder, Planeten, Wellen – überall wo Kreise vorkommen, spielt $\pi$ eine Rolle
- **Wachstum**: Exponentielles Wachstum (Bakterienpopulationen, Zinseszins) wird durch die Eulersche Zahl $e$ beschrieben
- **Blattstellung**: Viele Pflanzen ordnen ihre Blätter in Winkeln an, die mit dem goldenen Schnitt zusammenhängen

---

## Vollständigkeit der reellen Zahlen

Ein fundamentaler Unterschied zwischen $\mathbb{Q}$ und $\mathbb{R}$ ist die **Vollständigkeit**.

> [!note] **Vollständigkeit: Was bedeutet das?**
> Die reellen Zahlen „füllen" den Zahlenstrahl **lückenlos** aus.
> 
> In $\mathbb{Q}$ gibt es „Lücken": Der Punkt, der dem Wert $\sqrt{2}$ entspricht, liegt zwar auf dem Zahlenstrahl, aber es gibt keine rationale Zahl, die genau diesen Punkt trifft. Man kann sich mit Brüchen beliebig nahe an $\sqrt{2}$ herantasten ($\frac{14}{10}, \frac{141}{100}, \frac{1414}{1000}, ...$), erreicht ihn aber nie exakt.
>
> In $\mathbb{R}$ gibt es keine solchen Lücken: **Jeder** Punkt auf dem Zahlenstrahl entspricht genau einer reellen Zahl.

### Visualisierung

![[zahlenstrahl-reell.png]]
*<span class="fig-id">01-01-06-zahlenstrahl-reell</span>: Auf dem Zahlenstrahl liegen rationale Zahlen (z. B. 1, in ℚ und ℝ) und irrationale Zahlen (z. B. √2, nur in ℝ) nebeneinander – zusammen füllen sie die Linie lückenlos.*

Die rationalen Zahlen sind wie Perlen auf einer Schnur verteilt – dicht, aber mit winzigen Lücken dazwischen. Die reellen Zahlen füllen diese Lücken und ergeben eine durchgehende Linie.

### Praktische Bedeutung

Die Vollständigkeit ist wichtig für:
- **Geometrie**: Jede Länge, jeder Winkel, jede Fläche kann durch eine reelle Zahl exakt angegeben werden
- **Analysis**: Grenzwerte existieren immer in $\mathbb{R}$ (nicht immer in $\mathbb{Q}$)
- **Physik**: Messgrößen wie Zeit, Länge, Masse werden als reelle Zahlen modelliert

---

## Intervallschreibweise

Für Teilmengen der reellen Zahlen verwendet man **Intervalle** – eine kompakte Notation für „alle Zahlen zwischen zwei Grenzen":

| Notation | Name | Bedeutung | Enthält die Grenzen? |
|----------|------|-----------|----------------------|
| $[a, b]$ | Geschlossenes Intervall | Alle $x$ mit $a \leq x \leq b$ | Ja, beide |
| $(a, b)$ | Offenes Intervall | Alle $x$ mit $a < x < b$ | Nein, keine |
| $[a, b)$ | Links geschlossen, rechts offen | Alle $x$ mit $a \leq x < b$ | Nur $a$ |
| $(a, b]$ | Links offen, rechts geschlossen | Alle $x$ mit $a < x \leq b$ | Nur $b$ |
| $[a, \infty)$ | Halbgerade nach rechts | Alle $x$ mit $x \geq a$ | Nur $a$ |
| $(-\infty, b]$ | Halbgerade nach links | Alle $x$ mit $x \leq b$ | Nur $b$ |

**Beispiele:**
- $[0, 1]$ enthält alle Zahlen von 0 bis 1, einschließlich 0 und 1
- $(0, 1)$ enthält alle Zahlen zwischen 0 und 1, aber nicht 0 und 1 selbst
- $[0, \infty)$ sind alle nicht-negativen reellen Zahlen

> [!tip] **Merkregel: Klammern**
> - **Eckige Klammer** $[ \, ]$ = Grenze ist **enthalten** (einschließlich)
> - **Runde Klammer** $( \, )$ = Grenze ist **ausgeschlossen** (ausschließlich)
> - Bei $\pm\infty$ immer runde Klammer, da $\infty$ keine Zahl ist

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[05-Rationale-Zahlen|Rationale Zahlen]] – Die Grundlage: $\mathbb{Q} \subset \mathbb{R}$
- → [[07-Zahlenstrahl-und-Zahlenmengen|Zahlenstrahl und Zahlenmengen]] – Visualisierung aller Mengen
- → [[02-Mathematische-Symbole|Mathematische Symbole]] – Intervallnotation

> [!warning] **Prüfungsrelevant**
> - $\mathbb{R} = \mathbb{Q} \cup$ (irrationale Zahlen)
> - Irrationale Zahlen: nicht-abbrechend, nicht-periodisch, nicht als Bruch darstellbar
> - Beispiele: $\sqrt{2}$, $\pi$, $e$, $\varphi$
> - $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$
> - $\mathbb{R}$ ist vollständig (keine Lücken im Zahlenstrahl)
> - Intervallnotation: $[a,b]$ geschlossen, $(a,b)$ offen

> [!question] **Typische Prüfungsfragen**
> - Ist $\sqrt{9}$ rational oder irrational? Begründe.
> - Nenne drei irrationale Zahlen.
> - Was bedeutet es, dass $\mathbb{R}$ „vollständig" ist?
> - Ordne die Zahlenmengen nach Inklusionsbeziehung: $\mathbb{Q}$, $\mathbb{N}$, $\mathbb{R}$, $\mathbb{Z}$
> - Welche Zahlen gehören zum Intervall $[-2, 3)$?

## Quellen

- Heuser, Harro: *Lehrbuch der Analysis, Teil 1*. Teubner, 2009.
- Beutelspacher, Albrecht: *Zahlen*. Rowohlt, 2013.
- Maor, Eli: *e: The Story of a Number*. Princeton University Press, 1994.

> [!tip] **Weiterführende Links**
> - [Mathebibel: Reelle Zahlen](https://www.mathebibel.de/reelle-zahlen)
> - [[07-Zahlenstrahl-und-Zahlenmengen|Nächstes Kapitel: Zahlenstrahl und Zahlenmengen]]
