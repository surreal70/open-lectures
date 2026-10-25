---
title: Unabhängige Ereignisse - Grundlagen
chapter: "14"
section: "14.10"
type: lecture
created: 2026-10-13
modified: 2026-10-25
status: final
tags:
  - mathematik/wahrscheinlichkeit
  - unabhaengigkeit
---

# Unabhängige Ereignisse - Grundlagen

## Einführung

> [!info] **Lernziele**
> Nach dieser Lektion können Sie:
> - Unabhängige Ereignisse erkennen
> - Mit unabhängigen Ereignissen rechnen

---

## Überblick

Im Alltag beeinflussen sich viele Ereignisse gegenseitig: Wenn es heute regnet, ist es wahrscheinlicher, dass auch morgen Wolken am Himmel sind. Aber manche Ereignisse stehen in keinem Zusammenhang: Das Wetter in München beeinflusst nicht, welche Karte Sie aus einem Stapel in Hamburg ziehen.

In der Wahrscheinlichkeitsrechnung ist diese Unterscheidung fundamental wichtig. Bei **unabhängigen Ereignissen** können wir einfach multiplizieren – bei **abhängigen Ereignissen** müssen wir vorsichtiger sein.

---

## Definition

> [!note] **Definition**
> Zwei Ereignisse A und B sind **unabhängig**, wenn das Eintreten von A keinen Einfluss auf die Wahrscheinlichkeit von B hat (und umgekehrt).
> 
> Mathematische Formulierung:
> $$P(A \cap B) = P(A) \cdot P(B)$$

### Intuitive Erklärung

Unabhängigkeit bedeutet: Egal ob A eingetreten ist oder nicht – die Wahrscheinlichkeit für B bleibt gleich. Die Ereignisse „wissen nichts voneinander".

Bei einem fairen Würfel: Ob der erste Wurf eine 6 zeigt, hat keinen Einfluss darauf, was der zweite Wurf zeigt. Der Würfel hat kein „Gedächtnis".

---

## Beispiele

### Unabhängige Ereignisse

| Situation | Warum unabhängig? |
|-----------|-------------------|
| Würfeln und Münze werfen | Verschiedene Objekte, keine physische Verbindung |
| Zwei getrennte Würfelwürfe | Jeder Wurf ist ein neues Experiment |
| Geburtstage zweier zufälliger Personen | Keine Verbindung zwischen den Personen |
| Lottozahlen verschiedener Ziehungen | Jede Ziehung ist unabhängig |

### Abhängige Ereignisse

| Situation | Warum abhängig? |
|-----------|-----------------|
| Ziehen ohne Zurücklegen | Die erste Kugel beeinflusst, was noch in der Urne ist |
| Wetter heute und morgen | Wettermuster setzen sich oft fort |
| Prüfung bestanden & gut gelernt | Lernen beeinflusst das Ergebnis |
| Zwei Karten aus demselben Stapel | Nach der ersten Karte ändert sich der Stapel |

---

## Rechnen mit unabhängigen Ereignissen

> [!example] **Würfel und Münze**
> A = "Sechs würfeln" → $P(A) = \frac{1}{6}$
> B = "Kopf werfen" → $P(B) = \frac{1}{2}$
> 
> Die Ereignisse sind unabhängig, also:
> $P(A \cap B) = P(A) \cdot P(B) = \frac{1}{6} \cdot \frac{1}{2} = \frac{1}{12} \approx 8{,}3\%$

> [!example] **Dreimal würfeln: Dreimal Sechs**
> Jeder Wurf ist unabhängig vom vorherigen.
> 
> $P(\text{3× Sechs}) = \frac{1}{6} \cdot \frac{1}{6} \cdot \frac{1}{6} = \frac{1}{216} \approx 0{,}46\%$

---

## Der Spielerfehlschluss

> [!warning] **Häufiger Fehler: Der Spielerfehlschluss (Gambler's Fallacy)**
> „Die Münze hat 5-mal Kopf gezeigt, jetzt **muss** Zahl kommen!"
> 
> **Das ist falsch!** Bei unabhängigen Ereignissen hat jeder Wurf die gleiche Wahrscheinlichkeit – egal was vorher passiert ist. Die Münze hat kein Gedächtnis.
> 
> Nach 5× Kopf ist P(Kopf) beim 6. Wurf immer noch genau 50%.

Dieser Denkfehler ist so verbreitet, dass er einen eigenen Namen hat. Er führt Spieler oft zu falschen Entscheidungen – etwa beim Roulette, wo nach einer langen Serie von „Rot" fälschlicherweise auf „Schwarz" gesetzt wird.

### Warum erscheint es anders?

Das Gesetz der großen Zahlen sagt: Bei **vielen** Versuchen nähert sich die relative Häufigkeit der Wahrscheinlichkeit an. Aber das bedeutet nicht, dass nach einer Abweichung eine „Korrektur" kommt. Vielmehr werden die Abweichungen durch viele weitere Versuche immer unbedeutender.

---

## Unabhängigkeit prüfen

In Aufgaben können Sie oft aus dem Kontext erkennen, ob Unabhängigkeit vorliegt:

| Schlüsselwörter | Bedeutung |
|-----------------|-----------|
| „mit Zurücklegen" | unabhängig |
| „ohne Zurücklegen" | abhängig |
| „zwei verschiedene..." | meist unabhängig |
| „aus demselben Stapel/Urne..." | abhängig |
| „nacheinander, dann..." | Kontext prüfen! |

> [!tip] **Praktische Faustregel**
> Fragen Sie sich: „Ändert das Ergebnis des ersten Versuchs etwas an den Bedingungen für den zweiten?"
> - Ja → abhängig (Wahrscheinlichkeiten passen sich an)
> - Nein → unabhängig (einfach multiplizieren)

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[09-Pfadregeln|Pfadregeln]] – Bei Unabhängigkeit sind alle Kantengewichte einer Stufe gleich
- → [[04-Haeufigkeit-und-Wahrscheinlichkeit|Häufigkeit und Wahrscheinlichkeit]] – Das Gesetz der großen Zahlen
- → [[08-Baumdiagramme|Baumdiagramme]] – Darstellung von unabhängigen und abhängigen Experimenten
- → [[12-Praktische-Zufallsexperimente|Praktische Zufallsexperimente]] – Urnenmodelle mit und ohne Zurücklegen

---

**Navigation:** [[09-Pfadregeln|← Pfadregeln]] | [[11-Kombinatorik|Kombinatorik →]]
