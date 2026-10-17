---
author: Andreas Hümmer
title: Brüche kürzen
status: draft - review pending
tags:
  - content
  - mathematik
  - bruchrechnung
created: 2026-10-13
modified: 2026-10-16
---

# Brüche kürzen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Brüche durch gemeinsame Teiler kürzen können
> - Brüche vollständig kürzen können
> - Verstehen, warum der Wert beim Kürzen gleich bleibt

---

## Überblick

Beim **Kürzen** eines Bruchs werden Zähler und Nenner durch dieselbe Zahl geteilt. Dies vereinfacht den Bruch, ohne seinen Wert zu ändern. Ein vollständig gekürzter Bruch hat keine gemeinsamen Teiler mehr in Zähler und Nenner.

Kürzen ist die **Umkehrung des Erweiterns**: Während wir beim Erweitern feiner unterteilen (mehr Teile), fassen wir beim Kürzen wieder zusammen (weniger Teile). Beide Operationen ändern nicht die dargestellte Menge – nur die Art, wie wir sie beschreiben.

In der Praxis ist Kürzen wichtig, um Brüche übersichtlich zu halten. $\frac{24}{36}$ sagt weniger direkt etwas aus als $\frac{2}{3}$ – obwohl beide denselben Wert haben. Ein vollständig gekürzter Bruch ist die **einfachste Form** eines Bruchs.

---

## Definition

$$\frac{a}{b} = \frac{a : n}{b : n} \quad \text{für } n \neq 0$$

**Beispiel:** $\frac{8}{12}$ kürzen durch 4:

$$\frac{8}{12} = \frac{8 : 4}{12 : 4} = \frac{2}{3}$$

> [!note] **Mathematische Begründung**
> Kürzen entspricht der Division durch 1:
> $$\frac{8}{12} = \frac{8}{12} : \frac{4}{4} = \frac{8}{12} : 1 = \frac{8 : 4}{12 : 4} = \frac{2}{3}$$
> 
> Da $\frac{4}{4} = 1$ ist, ändert die Division durch 1 den Wert nicht.

---

## Schrittweises Kürzen

Manchmal erkennt man nicht sofort den größten gemeinsamen Teiler (ggT). Dann kann man schrittweise mit kleineren Teilern kürzen:

$$\frac{24}{36}$$

1. Durch 2 kürzen: $\frac{12}{18}$
2. Durch 2 kürzen: $\frac{6}{9}$
3. Durch 3 kürzen: $\frac{2}{3}$

**Oder direkt:** ggT(24, 36) = 12 → $\frac{24 : 12}{36 : 12} = \frac{2}{3}$

> [!tip] **Praktischer Tipp**
> Wenn du den ggT nicht sofort siehst, kürze einfach mit offensichtlichen Teilern:
> - Beide Zahlen gerade? → Durch 2 kürzen
> - Beide durch 5 teilbar? → Durch 5 kürzen
> - Beide durch 3 teilbar? → Durch 3 kürzen
> 
> Wiederhole, bis nichts mehr geht.

---

## Vollständig kürzen

Ein Bruch ist **vollständig gekürzt**, wenn Zähler und Nenner keinen gemeinsamen Teiler (außer 1) mehr haben. Man sagt auch: Zähler und Nenner sind **teilerfremd**.

| Bruch | Kürzen | Vollständig gekürzt |
|-------|--------|---------------------|
| $\frac{6}{8}$ | durch 2 | $\frac{3}{4}$ |
| $\frac{15}{25}$ | durch 5 | $\frac{3}{5}$ |
| $\frac{18}{24}$ | durch 6 | $\frac{3}{4}$ |

> [!note] **Woran erkenne ich vollständig gekürzt?**
> Prüfe, ob Zähler und Nenner noch gemeinsame Teiler haben:
> - $\frac{3}{4}$: 3 ist prim, 4 = 2×2 → kein gemeinsamer Teiler → vollständig gekürzt ✓
> - $\frac{6}{9}$: 6 = 2×3, 9 = 3×3 → gemeinsamer Teiler 3 → noch kürzbar!

---

## Tipps zum Erkennen gemeinsamer Teiler

Die **Teilbarkeitsregeln** helfen beim schnellen Erkennen:

| Teilbar durch | Erkennungsmerkmal | Beispiel |
|---------------|-------------------|----------|
| 2 | Letzte Ziffer ist gerade (0, 2, 4, 6, 8) | 24, 36 → beide durch 2 teilbar |
| 3 | Quersumme durch 3 teilbar | 24: 2+4=6 ✓, 36: 3+6=9 ✓ |
| 5 | Endet auf 0 oder 5 | 15, 25, 30 |
| 9 | Quersumme durch 9 teilbar | 36: 3+6=9 ✓ |
| 10 | Endet auf 0 | 20, 100, 350 |

> [!tip] **Merkregel für die Quersumme**
> Die Quersumme ist die Summe aller Ziffern einer Zahl.
> - Quersumme von 123: 1 + 2 + 3 = 6
> - Quersumme von 4567: 4 + 5 + 6 + 7 = 22
>
> Wenn die Quersumme durch 3 (bzw. 9) teilbar ist, ist auch die Zahl selbst durch 3 (bzw. 9) teilbar.

---

## Kürzen vor dem Multiplizieren

> [!tip] **Rechenvorteile**
> Beim Multiplizieren von Brüchen kann man **vorher kürzen** (über Kreuz):
>
> $$\frac{3}{8} \cdot \frac{4}{9} = \frac{\cancel{3}^1}{8} \cdot \frac{4}{\cancel{9}^3} = \frac{1 \cdot 4}{8 \cdot 3} = \frac{4}{24} = \frac{1}{6}$$
>
> Oder noch einfacher: $\frac{1}{\cancel{8}^2} \cdot \frac{\cancel{4}^1}{3} = \frac{1}{6}$

Das „Kreuzkürzen" spart viel Rechenarbeit, weil wir mit kleineren Zahlen rechnen. Statt $\frac{3 \cdot 4}{8 \cdot 9} = \frac{12}{72}$ mühsam zu kürzen, erhalten wir direkt $\frac{1}{6}$.

> [!warning] **Häufiger Fehler**
> Beim Addieren/Subtrahieren darf man NICHT über Kreuz kürzen!
>
> **Falsch:** $\frac{\cancel{3}}{4} + \frac{2}{\cancel{6}} = ?$ ✗
>
> Kreuzkürzen funktioniert NUR bei der Multiplikation, weil dort Zähler mit Zähler und Nenner mit Nenner multipliziert werden.

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[04-Brueche-erweitern|Brüche erweitern]] – Die Umkehrung des Kürzens
- → [[09-Multiplikation-von-Bruechen|Multiplikation von Brüchen]] – Wo Kreuzkürzen hilft
- → [[06-Hauptnenner-bestimmen|Hauptnenner bestimmen]] – Braucht den ggT

> [!warning] **Prüfungsrelevant**
> - Kürzen: Zähler UND Nenner durch dieselbe Zahl teilen
> - Vollständig gekürzt: kein gemeinsamer Teiler mehr
> - Beim Multiplizieren: vorher kürzen spart Arbeit

> [!question] **Typische Prüfungsfragen**
> - Kürze $\frac{42}{56}$ vollständig.
> - Warum ist $\frac{8}{12} = \frac{2}{3}$?

## Quellen

- Padberg, Friedhelm: *Didaktik der Bruchrechnung*. Springer, 2009.
