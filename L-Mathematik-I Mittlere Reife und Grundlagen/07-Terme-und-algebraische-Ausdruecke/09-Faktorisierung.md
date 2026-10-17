---
title: "Faktorisierung"
chapter: "07"
section: "09"
type: topic
status: final
learning_objectives:
  - "Terme in Produkte zerlegen"
  - "Binomische Formeln rückwärts anwenden"
  - "Gemeinsame Faktoren erkennen"
  - "Verschiedene Faktorisierungsmethoden kombinieren"
tags:
  - mathematik
  - faktorisierung
  - terme
  - produkt
created: 2026-10-13
modified: 2026-10-16
---

# Faktorisierung

> [!info] Lernziele
> - Terme in Produkte zerlegen
> - Binomische Formeln rückwärts anwenden
> - Gemeinsame Faktoren erkennen
> - Verschiedene Faktorisierungsmethoden kombinieren

## Überblick

**Faktorisierung** bedeutet, einen Term als Produkt von Faktoren zu schreiben – das Gegenteil von Ausmultiplizieren.

Das Wort „Faktor" kommt vom lateinischen *facere* (machen). Faktoren sind die „Bausteine", aus denen ein Produkt besteht: In $3 \cdot 5 = 15$ sind 3 und 5 die Faktoren von 15. Bei der Faktorisierung zerlegen wir einen Term in solche Bausteine.

> [!info] **Warum ist Faktorisierung wichtig?**
> - **Brüche kürzen:** Nur faktorisierte Terme lassen sich kürzen
> - **Gleichungen lösen:** Die Faktorisierung ermöglicht das Lösen durch „Nullproduktregel" (wenn $a \cdot b = 0$, dann $a = 0$ oder $b = 0$)
> - **Vereinfachung:** Faktorisierte Terme sind oft kompakter und übersichtlicher
> - **Mathematik verstehen:** Die Struktur eines Terms wird sichtbar

## Methoden

### 1. Ausklammern

$$6x + 9 = 3(2x + 3)$$
$$x^2 + 3x = x(x + 3)$$

### 2. Binomische Formeln rückwärts

Die binomischen Formeln können auch „rückwärts" angewendet werden. Dazu muss man das Muster erkennen:

| Muster | Faktorisiert | Erkennungsmerkmal |
|--------|--------------|-------------------|
| $a^2 + 2ab + b^2$ | $(a + b)^2$ | Positives mittleres Glied |
| $a^2 - 2ab + b^2$ | $(a - b)^2$ | Negatives mittleres Glied |
| $a^2 - b^2$ | $(a + b)(a - b)$ | Differenz zweier Quadrate |

> [!tip] **So erkennst du binomische Formeln**
> 1. Prüfe: Sind der erste und letzte Term Quadratzahlen?
> 2. Prüfe: Ist das mittlere Glied = $2 \cdot \sqrt{\text{erstes}} \cdot \sqrt{\text{letztes}}$?
> 3. Bei $a^2 - b^2$: Gibt es kein mittleres Glied und ist ein Minus dazwischen?

### 3. Kombinierte Methode

Manchmal muss man mehrere Methoden nacheinander anwenden. Die Strategie: Erst ausklammern, dann prüfen, ob binomische Formeln passen.

Erst ausklammern, dann binomische Formel:

$$2x^2 - 8 = 2(x^2 - 4) = 2(x + 2)(x - 2)$$

> [!warning] **Häufiger Fehler: Zu früh aufhören**
> Prüfe nach jedem Schritt, ob du weiterfaktorisieren kannst!
> 
> **Nicht vollständig:** $x^3 - 4x = x(x^2 - 4)$
> **Vollständig:** $x^3 - 4x = x(x^2 - 4) = x(x+2)(x-2)$

## Beispiele

| Ausdruck | Faktorisiert |
|----------|--------------|
| $x^2 - 9$ | $(x + 3)(x - 3)$ |
| $x^2 + 6x + 9$ | $(x + 3)^2$ |
| $4x^2 - 25$ | $(2x + 5)(2x - 5)$ |
| $3x^2 - 12$ | $3(x^2 - 4) = 3(x+2)(x-2)$ |

## Zusammenhänge

### Voraussetzungen

- [[06-Ausklammern]]
- [[08-Binomische-Formeln]]

## Prüfungsrelevanz

> [!warning] Prüfungsrelevanz: Hoch
> Wichtig für Bruchgleichungen und quadratische Gleichungen.

## Typische Prüfungsfragen

1. Faktorisiere vollständig: $x^2 - 16$
2. Faktorisiere: $x^2 - 10x + 25$
3. Faktorisiere: $5x^2 - 20$

## Quellen

- Lambacher Schweizer Mathematik 8

## Weiterführende Links

- [[08-Binomische-Formeln]]
- [[08-Gleichungen-und-Ungleichungen/00-Gleichungen-Index|Gleichungen]]
