---
author: Andreas Hümmer
title: Distributivgesetz
status: draft - review pending
tags:
  - content
  - mathematik
  - rechengesetze
created: 2026-10-13
modified: 2026-10-16
---

# Distributivgesetz

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das Distributivgesetz kennen und anwenden können
> - Klammern ausmultiplizieren können
> - Ausklammern als Umkehrung beherrschen

---

## Überblick

Das **Distributivgesetz** (Verteilungsgesetz) verbindet Multiplikation mit Addition und Subtraktion. Es ermöglicht das Ausmultiplizieren von Klammern und das Ausklammern gemeinsamer Faktoren.

### Historischer Hintergrund

Der Begriff „distributiv" stammt vom lateinischen „distribuere" (= verteilen). Das Gesetz beschreibt, wie sich die Multiplikation auf eine Summe „verteilt". Es ist das einzige Rechengesetz, das zwei verschiedene Operationen miteinander verbindet. Ohne das Distributivgesetz könnten wir Klammern nicht auflösen und Algebra wäre unmöglich. Es bildet die Grundlage für das Ausmultiplizieren von Klammern, das Lösen von Gleichungen und viele weitere algebraische Techniken.

### Warum ist das Distributivgesetz so wichtig?

Das Distributivgesetz ist das „Arbeitstier" der Algebra. Es ermöglicht:
- Klammern aufzulösen (Ausmultiplizieren)
- Terme zu vereinfachen (Ausklammern)
- Kopfrechentricks anzuwenden
- Binomische Formeln herzuleiten (→ [[08-Binomische-Formeln|Binomische Formeln]])

---

## Definition

$$a \cdot (b + c) = a \cdot b + a \cdot c$$
$$a \cdot (b - c) = a \cdot b - a \cdot c$$

Auch von rechts:
$$(b + c) \cdot a = b \cdot a + c \cdot a$$

---

## Ausmultiplizieren (Klammern auflösen)

**Beispiel 1:**
$$5 \cdot (3 + 4) = 5 \cdot 3 + 5 \cdot 4 = 15 + 20 = 35$$

**Beispiel 2:**
$$3 \cdot (10 - 2) = 3 \cdot 10 - 3 \cdot 2 = 30 - 6 = 24$$

**Beispiel 3 (mit Variablen):**
$$2 \cdot (x + 5) = 2x + 10$$

---

## Ausklammern (Faktorisieren)

Die Umkehrung: Gemeinsame Faktoren vor die Klammer ziehen.

**Beispiel 1:**
$$6 + 9 = 3 \cdot 2 + 3 \cdot 3 = 3 \cdot (2 + 3) = 3 \cdot 5 = 15$$

**Beispiel 2:**
$$4x + 4y = 4 \cdot (x + y)$$

---

## Anschauliche Erklärung

Ein Rechteck mit Breite $a$ und Länge $(b + c)$:

```
        b       c
    ┌───────┬───────┐
    │       │       │
  a │   ab  │  ac   │
    │       │       │
    └───────┴───────┘
    
Fläche = a · (b + c) = a·b + a·c
```

---

## Anwendung: Kopfrechnen

Das Distributivgesetz ist der Schlüssel zu vielen Kopfrechentricks. Anstatt komplizierte Multiplikationen direkt auszuführen, zerlegen wir sie in einfachere Teile.

**99 · 7:**
$$99 \cdot 7 = (100 - 1) \cdot 7 = 700 - 7 = 693$$

**13 · 5 + 7 · 5:**
$$13 \cdot 5 + 7 \cdot 5 = (13 + 7) \cdot 5 = 20 \cdot 5 = 100$$

**47 · 8:**
$$47 \cdot 8 = (50 - 3) \cdot 8 = 400 - 24 = 376$$

> [!tip] **Kopfrechenstrategie**
> Zerlege „krumme" Zahlen in eine runde Zahl plus/minus eine kleine Zahl:
> - $98 = 100 - 2$
> - $52 = 50 + 2$
> - $199 = 200 - 1$

> [!warning] **Häufiger Fehler**
> Das Distributivgesetz gilt nur für Multiplikation und Addition/Subtraktion, **nicht** für Division!
> 
> **Falsch:** $(a + b) : c = a : c + b : c$ ✗ (gilt manchmal zufällig, aber nicht allgemein)
> **Richtig:** $a \cdot (b + c) = a \cdot b + a \cdot c$ ✓

---

## Zusammenhänge

- → [[05-Kommutativgesetz|Kommutativgesetz]]
- → [[06-Assoziativgesetz|Assoziativgesetz]]
- → [[10-Klammerregeln|Klammerregeln]]

> [!warning] **Prüfungsrelevant**
> - $a \cdot (b + c) = a \cdot b + a \cdot c$
> - Ausmultiplizieren und Ausklammern als Umkehrungen
> - Anwendung beim Kopfrechnen

> [!question] **Typische Prüfungsfragen**
> - Multipliziere aus: $4 \cdot (x - 3)$
> - Klammere aus: $15 + 25$
> - Berechne geschickt: $98 \cdot 6$

## Quellen

- Padberg, Friedhelm: *Didaktik der Arithmetik*. Springer, 2017.
