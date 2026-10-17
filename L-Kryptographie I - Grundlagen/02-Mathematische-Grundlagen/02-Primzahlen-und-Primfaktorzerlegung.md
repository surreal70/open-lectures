---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - mathematik
---

# Primzahlen und Primfaktorzerlegung

> [!info] **Lernziele**
> - Primzahlen und ihre Bedeutung für die Kryptographie verstehen
> - Primzahltests und Primzahlerzeugung einordnen
> - Das Faktorisierungsproblem als Sicherheitsgrundlage von RSA erkennen

---

## Inhalt

### Primzahlen

Eine **Primzahl** ist eine natürliche Zahl $p > 1$, die nur durch 1 und sich selbst teilbar ist (2, 3, 5, 7, 11, …). Der **Fundamentalsatz der Arithmetik** besagt: Jede natürliche Zahl $> 1$ lässt sich eindeutig als Produkt von Primzahlen darstellen.

$$360 = 2^3 \cdot 3^2 \cdot 5$$

Primzahlen sind die „Atome" der Zahlentheorie – und das Rückgrat asymmetrischer Verfahren.

### Warum Primzahlen in der Kryptographie?

Die Sicherheit von RSA beruht auf einer **Einwegfunktion**:

- Zwei große Primzahlen $p$ und $q$ zu **multiplizieren** ist einfach: $n = p \cdot q$.
- Aus $n$ die Faktoren $p$ und $q$ **zurückzugewinnen** (Faktorisierung) ist für ausreichend große $n$ praktisch unmöglich.

Für RSA-2048 hat $n$ etwa 617 Dezimalstellen. Kein bekannter klassischer Algorithmus faktorisiert das in praktikabler Zeit.

> [!note] **Zusammenhang zu Quantencomputern**
> Der Shor-Algorithmus kann Faktorisierung auf einem hinreichend großen Quantencomputer effizient lösen – deshalb gilt RSA als langfristig gefährdet (→ Modul 13: Post-Quanten-Kryptographie).

### Primzahltests

Da man für die Schlüsselerzeugung große Primzahlen braucht, testet man zufällig gewählte Zahlen auf Primalität:

| Test | Typ | Eigenschaft |
|------|-----|-------------|
| Probedivision | deterministisch | nur für kleine Zahlen praktikabel |
| Fermat-Test | probabilistisch | schnell, aber Carmichael-Zahlen täuschen ihn |
| **Miller-Rabin** | probabilistisch | Standard in der Praxis, Fehlerwahrscheinlichkeit beliebig klein wählbar |
| AKS | deterministisch | theoretisch polynomiell, praktisch zu langsam |

**Miller-Rabin** ist der De-facto-Standard: Mit $k$ Runden sinkt die Irrtumswahrscheinlichkeit auf höchstens $4^{-k}$.

### Primzahlerzeugung

Für einen Schlüssel erzeugt man Primzahlen so:

1. Zufällige ungerade Zahl der gewünschten Bitlänge wählen.
2. Mit kleinen Primzahlen vortesten (Probedivision).
3. Miller-Rabin mehrfach anwenden.
4. Bei Nichtbestehen die nächste Kandidatin probieren.

Nach dem **Primzahlsatz** liegt die Dichte der Primzahlen nahe $x$ bei etwa $1/\ln x$ – unter 2048-Bit-Zahlen ist also etwa jede 1420. Zahl prim, sodass die Suche schnell terminiert.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Jede Zahl hat eine eindeutige Primfaktorzerlegung (Fundamentalsatz)
> - Multiplizieren ist leicht, Faktorisieren ist schwer – Basis von RSA
> - Große Primzahlen erzeugt man mit probabilistischen Tests (Miller-Rabin)
> - Quantencomputer (Shor) bedrohen die Faktorisierungsannahme

---

## Übungen

1. Zerlegen Sie $84$ und $1001$ in Primfaktoren.
2. Erklären Sie, warum das Multiplizieren zweier Primzahlen eine Einwegfunktion bildet.
3. Warum verwendet man probabilistische statt deterministischer Primzahltests?

---

← [[01-Zahlentheorie-und-modulare-Arithmetik|← Zurück]] | [[00-Mathematik-Index|Übersicht]] | [[03-Euklidischer-Algorithmus|Weiter →]]
