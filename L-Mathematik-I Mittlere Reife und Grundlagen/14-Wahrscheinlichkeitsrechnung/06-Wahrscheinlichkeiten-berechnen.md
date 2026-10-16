---
title: Wahrscheinlichkeiten berechnen
chapter: "14"
section: "14.6"
type: lecture
created: 2026-10-13
modified: 2025-01-20
status: draft - review pending
tags:
  - mathematik/wahrscheinlichkeit
  - berechnung
---

# Wahrscheinlichkeiten berechnen

## Einführung

> [!info] **Lernziele**
> Nach dieser Lektion können Sie:
> - Wahrscheinlichkeiten mit der Laplace-Formel berechnen
> - Ergebnisse als Bruch, Dezimalzahl und Prozent angeben

---

## Überblick

Nachdem wir die Grundbegriffe kennengelernt haben, geht es nun ans praktische Rechnen. In diesem Kapitel werden die grundlegenden Rechenregeln für Wahrscheinlichkeiten vorgestellt – die sogenannten Axiome nach Kolmogorow. Diese Regeln bilden das Fundament, auf dem alle weiteren Berechnungen aufbauen.

Der russische Mathematiker Andrei Kolmogorow (1903–1987) formulierte 1933 die axiomatische Grundlage der modernen Wahrscheinlichkeitstheorie. Seine drei einfachen Axiome sind so allgemeingültig, dass sie alle bekannten Anwendungen der Wahrscheinlichkeitsrechnung abdecken.

---

## Grundregeln

> [!note] **Axiome (nach Kolmogorow)**
> 1. $0 \leq P(E) \leq 1$ – Wahrscheinlichkeiten liegen zwischen 0 und 1
> 2. $P(Ω) = 1$ – Das sichere Ereignis hat Wahrscheinlichkeit 1
> 3. $P(∅) = 0$ – Das unmögliche Ereignis hat Wahrscheinlichkeit 0

### Interpretation der Werte

| Wahrscheinlichkeit | Bedeutung | Beispiel |
|--------------------|-----------|----------|
| $P(E) = 0$ | Ereignis tritt nie ein | „Würfel zeigt 7" |
| $P(E) = 0{,}5$ | Ereignis tritt in der Hälfte der Fälle ein | „Münze zeigt Kopf" |
| $P(E) = 1$ | Ereignis tritt immer ein | „Würfel zeigt 1–6" |

> [!tip] **Anschauliche Interpretation**
> Stellen Sie sich Wahrscheinlichkeit als „Anteil der günstigen Fälle" vor:
> - $P = 0{,}25$ bedeutet: In etwa 25 von 100 Versuchen tritt das Ereignis ein
> - $P = 0{,}01$ bedeutet: In etwa 1 von 100 Versuchen (sehr selten)
> - $P = 0{,}99$ bedeutet: In etwa 99 von 100 Versuchen (fast sicher)

---

## Darstellungsformen

Wahrscheinlichkeiten können auf verschiedene Weisen angegeben werden. Alle drei Formen sind gleichwertig:

| Form | Beispiel | Verwendung |
|------|----------|------------|
| Bruch | $\frac{1}{6}$ | Exakt, für Berechnungen bevorzugt |
| Dezimalzahl | 0,167 | Für Vergleiche und Taschenrechner |
| Prozent | 16,7% | Im Alltag, Kommunikation |

### Umrechnung

$$\frac{1}{6} = 1 : 6 = 0{,}1\overline{6} \approx 0{,}167 = 16{,}7\%$$

> [!tip] **Praktischer Hinweis**
> In Prüfungen ist es oft am sichersten, das Ergebnis als gekürzten Bruch anzugeben. So vermeiden Sie Rundungsfehler. Zusätzlich können Sie den Prozent- oder Dezimalwert angeben.

---

## Beispiele

> [!example] **Zweimal Würfeln – Summe 7**
> **Schritt 1:** Ergebnismenge bestimmen
> Alle Paare (1. Wurf, 2. Wurf): |Ω| = 6 × 6 = 36
> 
> **Schritt 2:** Günstige Ergebnisse zählen
> Summe 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1)
> → 6 günstige Ergebnisse
> 
> **Schritt 3:** Laplace-Formel anwenden
> $P(\text{Summe 7}) = \frac{6}{36} = \frac{1}{6} \approx 16{,}7\%$

> [!example] **Warum ist Summe 7 am wahrscheinlichsten?**
> Bei zwei Würfeln sind die Summen 2 bis 12 möglich. Aber nicht alle sind gleich wahrscheinlich!
> 
> | Summe | Möglichkeiten | Anzahl | P |
> |-------|--------------|--------|---|
> | 2 | (1,1) | 1 | 2,8% |
> | 7 | (1,6), (2,5), ... | 6 | 16,7% |
> | 12 | (6,6) | 1 | 2,8% |
> 
> Die Summe 7 hat die meisten Möglichkeiten und ist daher am wahrscheinlichsten.

---

## Rechenregeln für verknüpfte Ereignisse

Für komplexere Berechnungen gibt es zusätzliche Regeln:

### Additionsregel (für disjunkte Ereignisse)

Wenn A und B sich ausschließen ($A \cap B = ∅$):
$$P(A \cup B) = P(A) + P(B)$$

> [!example] **Beispiel: Würfel**
> A = „1 oder 2" und B = „5 oder 6" sind disjunkt.
> $P(A \cup B) = \frac{2}{6} + \frac{2}{6} = \frac{4}{6} = \frac{2}{3}$

### Allgemeine Additionsregel

Wenn A und B sich überschneiden können:
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

> [!warning] **Häufiger Fehler**
> Bei „A oder B" wird oft vergessen, die Schnittmenge abzuziehen. Wenn Sie P(A) und P(B) einfach addieren, zählen Sie die gemeinsamen Elemente doppelt!

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[05-Laplace-Experimente|Laplace-Experimente]] – Die Grundformel für Wahrscheinlichkeiten
- → [[07-Gegenereignisse|Gegenereignisse]] – Berechnung über das Komplement
- → [[09-Pfadregeln|Pfadregeln]] – Berechnung bei mehrstufigen Experimenten
- → [[../03-Bruchrechnung/00-Bruchrechnung-Index|Bruchrechnung]] – Grundlage für das Rechnen mit Wahrscheinlichkeiten

---

**Navigation:** [[05-Laplace-Experimente|← Laplace]] | [[07-Gegenereignisse|Gegenereignisse →]]
