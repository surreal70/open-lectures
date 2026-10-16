---
author: Open Lectures
title: Brüche kürzen
status: draft - review pending
tags:
  - content
  - mathematik
  - bruchrechnung
created: 2026-10-13
modified: 2026-10-13
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

---

## Definition

$$\frac{a}{b} = \frac{a : n}{b : n} \quad \text{für } n \neq 0$$

**Beispiel:** $\frac{8}{12}$ kürzen durch 4:

$$\frac{8}{12} = \frac{8 : 4}{12 : 4} = \frac{2}{3}$$

---

## Schrittweises Kürzen

Manchmal erkennt man nicht sofort den größten gemeinsamen Teiler:

$$\frac{24}{36}$$

1. Durch 2 kürzen: $\frac{12}{18}$
2. Durch 2 kürzen: $\frac{6}{9}$
3. Durch 3 kürzen: $\frac{2}{3}$

**Oder direkt:** ggT(24, 36) = 12 → $\frac{24 : 12}{36 : 12} = \frac{2}{3}$

---

## Vollständig kürzen

Ein Bruch ist **vollständig gekürzt**, wenn Zähler und Nenner keinen gemeinsamen Teiler (außer 1) mehr haben.

| Bruch | Kürzen | Vollständig gekürzt |
|-------|--------|---------------------|
| $\frac{6}{8}$ | durch 2 | $\frac{3}{4}$ |
| $\frac{15}{25}$ | durch 5 | $\frac{3}{5}$ |
| $\frac{18}{24}$ | durch 6 | $\frac{3}{4}$ |

---

## Tipps zum Erkennen gemeinsamer Teiler

| Teilbar durch | Erkennungsmerkmal |
|---------------|-------------------|
| 2 | Letzte Ziffer ist gerade |
| 3 | Quersumme durch 3 teilbar |
| 5 | Endet auf 0 oder 5 |
| 10 | Endet auf 0 |

---

## Kürzen vor dem Multiplizieren

> [!tip] **Rechenvorteile**
> Beim Multiplizieren von Brüchen kann man **vorher kürzen** (über Kreuz):
>
> $$\frac{3}{8} \cdot \frac{4}{9} = \frac{\cancel{3}^1}{8} \cdot \frac{4}{\cancel{9}^3} = \frac{1 \cdot 4}{8 \cdot 3} = \frac{4}{24} = \frac{1}{6}$$
>
> Oder noch einfacher: $\frac{1}{\cancel{8}^2} \cdot \frac{\cancel{4}^1}{3} = \frac{1}{6}$

---

## Zusammenhänge

- → [[04-Brueche-erweitern|Brüche erweitern]] – Umkehrung
- → [[09-Multiplikation-von-Bruechen|Multiplikation von Brüchen]]

> [!warning] **Prüfungsrelevant**
> - Kürzen: Zähler UND Nenner durch dieselbe Zahl teilen
> - Vollständig gekürzt: kein gemeinsamer Teiler mehr
> - Beim Multiplizieren: vorher kürzen spart Arbeit

> [!question] **Typische Prüfungsfragen**
> - Kürze $\frac{42}{56}$ vollständig.
> - Warum ist $\frac{8}{12} = \frac{2}{3}$?

## Quellen

- Padberg, Friedhelm: *Didaktik der Bruchrechnung*. Springer, 2009.
