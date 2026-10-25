---
title: Ereignisse
chapter: "14"
section: "14.3"
type: lecture
created: 2026-10-13
modified: 2026-10-25
status: final
tags:
  - mathematik/wahrscheinlichkeit
  - ereignis
---

# Ereignisse

## Einführung

> [!info] **Lernziele**
> Nach dieser Lektion können Sie:
> - Ereignisse als Teilmengen von Ω beschreiben
> - Spezielle Ereignisse erkennen

---

## Überblick

In der Praxis interessieren wir uns oft nicht für ein einzelnes, ganz bestimmtes Ergebnis, sondern für eine Gruppe von Ergebnissen. Beim Würfeln fragen wir vielleicht: „Ist eine gerade Zahl gefallen?" – dabei ist es uns egal, ob es die 2, 4 oder 6 war. Solche Gruppen von Ergebnissen nennen wir **Ereignisse**.

Die Unterscheidung zwischen Ergebnis und Ereignis ist grundlegend für die Wahrscheinlichkeitsrechnung. Ein Ergebnis ist ein einzelner, konkreter Ausgang des Experiments (z.B. „die 4 ist gefallen"). Ein Ereignis ist eine Menge von Ergebnissen, die wir gemeinsam betrachten (z.B. „eine gerade Zahl ist gefallen" = {2, 4, 6}).

---

## Definition

> [!note] **Definition**
> Ein **Ereignis** ist eine Teilmenge der Ergebnismenge Ω.

Mathematisch ausgedrückt: Wenn $Ω$ alle möglichen Ergebnisse enthält, dann ist jedes Ereignis $E$ eine Menge mit $E \subseteq Ω$.

Diese Definition mag zunächst abstrakt erscheinen, ist aber äußerst praktisch: Sie erlaubt uns, mit Ereignissen genauso zu rechnen wie mit Mengen – wir können sie vereinigen, schneiden und komplementieren.

---

## Beispiele (Würfel)

Für den Würfel mit $Ω = \{1, 2, 3, 4, 5, 6\}$ sind beispielsweise folgende Ereignisse denkbar:

- **E₁:** "Gerade Zahl" = {2, 4, 6}
- **E₂:** "Zahl größer als 4" = {5, 6}
- **E₃:** "Primzahl" = {2, 3, 5}
- **E₄:** "Höchstens 3" = {1, 2, 3}
- **E₅:** "Mindestens 2" = {2, 3, 4, 5, 6}

> [!tip] **Formulierung beachten**
> Achten Sie auf die genaue Formulierung:
> - „größer als 4" bedeutet: nur 5 und 6 (die 4 gehört nicht dazu)
> - „mindestens 4" bedeutet: 4, 5 und 6 (die 4 gehört dazu)
> - „höchstens 4" bedeutet: 1, 2, 3 und 4 (die 4 gehört dazu)

---

## Spezielle Ereignisse

Es gibt drei besondere Ereignisse, die in der Wahrscheinlichkeitsrechnung eine wichtige Rolle spielen:

| Bezeichnung | Symbol | Beschreibung | Beispiel (Würfel) |
|-------------|--------|--------------|-------------------|
| Sicheres Ereignis | Ω | Tritt bei jedem Versuch ein | „Zahl zwischen 1 und 6" |
| Unmögliches Ereignis | ∅ | Tritt niemals ein | „Zahl = 7" |
| Elementarereignis | {ω} | Besteht aus genau einem Ergebnis | „Genau eine 3" = {3} |

### Das sichere Ereignis

Das sichere Ereignis $Ω$ enthält alle möglichen Ergebnisse. Es tritt mit Sicherheit ein, egal was passiert – daher der Name. Die Wahrscheinlichkeit beträgt immer $P(Ω) = 1$.

### Das unmögliche Ereignis

Das unmögliche Ereignis $∅$ (die leere Menge) enthält kein einziges Ergebnis. Es kann niemals eintreten. Die Wahrscheinlichkeit beträgt immer $P(∅) = 0$.

> [!example] **Beispiel: Schnittmenge als unmögliches Ereignis**
> Beim Würfeln: 
> - E₁ = „gerade Zahl" = {2, 4, 6}
> - E₂ = „Zahl kleiner als 2" = {1}
> 
> $E_1 \cap E_2 = ∅$ (keine Zahl ist sowohl gerade als auch kleiner als 2)

---

## Verknüpfung von Ereignissen

Ereignisse lassen sich mit den bekannten Mengenoperationen verknüpfen:

| Operation | Symbol | Bedeutung | Beispiel |
|-----------|--------|-----------|----------|
| Vereinigung | $A \cup B$ | A **oder** B (oder beide) | „gerade oder größer als 4" |
| Schnittmenge | $A \cap B$ | A **und** B (beide gleichzeitig) | „gerade und größer als 4" |
| Komplement | $\bar{A}$ | **nicht** A | „keine gerade Zahl" |

> [!example] **Beispiel mit konkreten Mengen**
> - $E_1$ = „gerade" = {2, 4, 6}
> - $E_2$ = „größer als 4" = {5, 6}
> 
> - $E_1 \cup E_2$ = {2, 4, 5, 6} (gerade ODER größer als 4)
> - $E_1 \cap E_2$ = {6} (gerade UND größer als 4)
> - $\bar{E_1}$ = {1, 3, 5} (nicht gerade = ungerade)

> [!warning] **Häufiger Fehler: „Oder" vs. „Und"**
> Im Alltag sagen wir oft „oder" wenn wir eigentlich „und" meinen:
> - „Nehmen Sie Milch oder Zucker?" – gemeint ist meist, ob man beides, eines oder keines möchte
> 
> In der Mathematik ist „oder" (∪) **inklusiv**: „A oder B" bedeutet „A oder B oder beides". Die Schnittmenge ist erlaubt!

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[02-Ergebnismengen|Ergebnismengen]] – Die Grundmenge Ω, aus der Ereignisse gebildet werden
- → [[07-Gegenereignisse|Gegenereignisse]] – Das Komplement $\bar{A}$ und seine Berechnung
- → [[../01-Einfuehrung-in-die-Mathematik/02-Mathematische-Symbole|Mathematische Symbole]] – Mengensymbole $\cup$, $\cap$, $\subseteq$

---

**Navigation:** [[02-Ergebnismengen|← Ergebnismengen]] | [[04-Haeufigkeit-und-Wahrscheinlichkeit|Häufigkeit →]]
