---
author: Andreas Hümmer
title: Logische Uhren
tags:
  - content
  - vs
  - koordination
  - logische-uhren
  - lamport
  - vektor
  - kausalitaet
created: '2026-10-07'
modified: '2026-10-29'
bereich: VS
---

# Logische Uhren

> [!info] Lernziele
> - Konzept der logischen Uhren vs. physikalische Uhren verstehen
> - Lamport-Uhren und ihre Regeln anwenden können
> - Vektoruhren verstehen und vergleichen können
> - Happened-before Relation formal definieren

## Einleitung

Logische Uhren ermöglichen die Ordnung von Ereignissen in verteilten Systemen ohne Bezug auf physikalische Zeit. Sie erfassen die **kausale Ordnung** zwischen Ereignissen – was vor was passiert ist.

> [!important] Kernkonzept
> Logische Uhren ordnen Ereignisse basierend auf **Kausalität**, nicht auf physikalischer Zeit. Die zentrale Frage ist nicht "Wann ist etwas passiert?" sondern "Was hat was verursacht?". **Lamport-Uhren** liefern eine totale Ordnung, **Vektoruhren** können zusätzlich Nebenläufigkeit erkennen.

> [!example] Analogie
> Logische Uhren sind wie Kapitelnummern in einem Buch: Kapitel 3 kommt nach Kapitel 2, unabhängig davon, wann du sie gelesen hast. Wenn jemand Kapitel 5 erwähnt, weißt du, dass er Kapitel 1-4 bereits kennen muss (Kausalität). Zwei Leser können parallel Kapitel 3 und Kapitel 7 verschiedener Bücher lesen – sie sind nebenläufig.

## Happened-Before Relation

Leslie Lamport definierte 1978 die "happened-before" Relation (→):

### Definition

1. **Lokale Ordnung**: Wenn a und b Ereignisse im selben Prozess sind und a vor b kommt, dann a → b
2. **Nachrichtenübertragung**: Wenn a das Senden einer Nachricht und b das Empfangen derselben ist, dann a → b
3. **Transitivität**: Wenn a → b und b → c, dann a → c

> [!warning] Wichtig
> a → b bedeutet, dass a **kausal vor** b liegt. Wenn weder a → b noch b → a gilt, sind die Ereignisse **nebenläufig** (a || b).

## Lamport-Uhren

### Regeln

1. Jeder Prozess hat einen lokalen Zähler C, initialisiert auf 0
2. **Vor jedem lokalen Ereignis**: C := C + 1
3. **Beim Senden einer Nachricht**: C := C + 1, sende C mit der Nachricht
4. **Beim Empfangen einer Nachricht mit Zeitstempel T**: C := max(C, T) + 1

![[lamport-uhr.png]]
*<span class="fig-id">04-04-02-lamport-uhr</span>: Lamport-Uhr – Nachrichtenaustausch zwischen drei Prozessen mit Zeitstempelberechnung.*

### Eigenschaften

| Eigenschaft | Erfüllt |
|-------------|---------|
| a → b ⟹ C(a) < C(b) | ✓ |
| C(a) < C(b) ⟹ a → b | ✗ |
| Erkennt Nebenläufigkeit | ✗ |

> [!warning] Limitation
> Lamport-Uhren garantieren nur: Wenn a → b, dann C(a) < C(b). Der Umkehrschluss gilt nicht! Gleiche Zeitstempel bedeuten nicht Gleichzeitigkeit.

## Vektoruhren

Vektoruhren erweitern Lamport-Uhren um die Fähigkeit, Nebenläufigkeit zu erkennen.

### Regeln

Bei n Prozessen hat jeder einen Vektor V[1..n]:

1. **Initialisierung**: V[i] = [0, 0, ..., 0]
2. **Vor jedem lokalen Ereignis** in Prozess i: V[i][i] := V[i][i] + 1
3. **Beim Senden** in Prozess i: V[i][i] := V[i][i] + 1, sende V[i] mit
4. **Beim Empfangen** von V' in Prozess i: 
   - Für alle j: V[i][j] := max(V[i][j], V'[j])
   - V[i][i] := V[i][i] + 1

### Vergleich von Vektoruhren

| Vergleich | Bedeutung |
|-----------|-----------|
| V ≤ W ⟺ ∀i: V[i] ≤ W[i] | V vor oder gleich W |
| V < W ⟺ V ≤ W ∧ V ≠ W | V strikt vor W (a → b) |
| V || W ⟺ ¬(V ≤ W) ∧ ¬(W ≤ V) | Nebenläufig |

![[vektoruhr.png]]
*<span class="fig-id">04-04-02-vektoruhr</span>: Vektoruhren – Beispiel mit drei Prozessen, zeigt kausale Beziehungen und Nebenläufigkeit.*

**Beispiel-Vergleich**:
- [2,0,0] < [2,3,0]: Kausal davor (→)
- [2,0,0] || [0,1,0]: Nebenläufig

## Vergleich der Uhren

| Aspekt | Lamport | Vektor |
|--------|---------|--------|
| **Speicher** | O(1) | O(n) |
| **Nachrichtengröße** | O(1) | O(n) |
| **Erkennt a → b** | ✓ | ✓ |
| **Erkennt a ∥ b** | ✗ | ✓ |
| **Totale Ordnung** | Mit Prozess-ID | Nein |

## Zusammenhänge

| Thema | Beziehung | Verweis |
|-------|-----------|---------|
| Zeit-Synchronisation | Alternative zu logischen Uhren | [[01-Zeit-Synchronisation]] |
| Konsensalgorithmen | nutzen logische Ordnung | [[03-Konsensalgorithmen]] |
| Lamport-Uhren | werden erweitert durch Vektoruhren | siehe oben |
| Kausale Konsistenz | wird durch logische Uhren ermöglicht | [[../03-Konsistenz/02-Konsistenzmodelle]] |

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
NA

> [!question] Verständnisfragen
> - Warum können Lamport-Uhren keine Nebenläufigkeit erkennen?
> - Was bedeutet V < W bei Vektoruhren?
> - Wann sind zwei Ereignisse nebenläufig?

> [!tip] Merkhilfe
> **Lamport**: "Wenn a → b, dann ist die Uhr von a kleiner"
> - Einfach: Ein Zähler pro Prozess
> - Limitation: C(a) < C(b) sagt NICHT, dass a → b
> 
> **Vektor**: "Jeder merkt sich, was er von allen anderen weiß"
> - Komplex: Ein Zähler pro Prozess im Vektor
> - Mächtig: Kann Nebenläufigkeit erkennen

---

> [!tip] **Weiterführende Ressourcen**
> - [[01-Zeit-Synchronisation]] – Physikalische Alternative
> - [[03-Konsensalgorithmen]] – Anwendung logischer Ordnung
> - [[../03-Konsistenz/02-Konsistenzmodelle]] – Kausale Konsistenz

---

## Quellen

- Lamport, Leslie: Time, Clocks, and the Ordering of Events in a Distributed System, Communications of the ACM, 1978
