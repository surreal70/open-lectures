---
author: Andreas Hümmer
title: Partielle Integration – Integration von Produkten
tags:
  - content
  - mathe
  - integralrechnung
  - partielle-integration
  - produktintegration
created: 2025-06-26
modified: 2025-06-26
---

# Partielle Integration

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Das Prinzip der partiellen Integration als Umkehrung der Produktregel verstehen
> - Die Formel der partiellen Integration sicher anwenden können
> - Sinnvolle Wahlen für $u$ und $v'$ treffen können
> - Spezialfälle wie zyklische Integration erkennen und lösen können

---

## Überblick

Die **partielle Integration** (auch: **Produktintegration**) ist eine Technik zur Integration von Produkten zweier Funktionen. Sie basiert auf der Umkehrung der **Produktregel** der Differentialrechnung und ist neben der Substitution die zweite fundamentale Integrationsmethode.

Die Methode ist besonders nützlich, wenn:
- Ein Produkt aus einer algebraischen und einer transzendenten Funktion integriert werden soll
- Logarithmus- oder Arkusfunktionen integriert werden sollen
- Substitution nicht zum Ziel führt

---

## Herleitung der Formel

### Ausgangspunkt: Die Produktregel

Die Produktregel der Differentialrechnung lautet:

$$(u \cdot v)' = u' \cdot v + u \cdot v'$$

### Integration beider Seiten

Integrieren wir beide Seiten dieser Gleichung:

$$\int (u \cdot v)' \, dx = \int u' \cdot v \, dx + \int u \cdot v' \, dx$$

Da $\int (u \cdot v)' \, dx = u \cdot v$ (bis auf Konstante), erhalten wir:

$$u \cdot v = \int u' \cdot v \, dx + \int u \cdot v' \, dx$$

### Formel der partiellen Integration

Umgestellt ergibt sich die **Formel der partiellen Integration**:

$$\boxed{\int u \cdot v' \, dx = u \cdot v - \int u' \cdot v \, dx}$$

> [!tip] **Merkregel**
> "Das Integral des Produkts = erstes mal Integral des zweiten minus Integral von (Ableitung des ersten mal Integral des zweiten)"

---

## Systematisches Vorgehen

### Schritt-für-Schritt-Anleitung

1. **Produkt identifizieren**: Schreibe den Integranden als Produkt $u \cdot v'$
2. **Faktoren zuordnen**: Wähle, welcher Faktor $u$ und welcher $v'$ sein soll
3. **Ableitungen/Stammfunktionen bilden**: Berechne $u'$ und $v$
4. **Formel anwenden**: Setze in $\int u \cdot v' \, dx = u \cdot v - \int u' \cdot v \, dx$ ein
5. **Neues Integral lösen**: Das entstehende Integral sollte einfacher sein

### Die LIATE-Regel zur Faktorwahl

> [!tip] **LIATE-Regel**
> Wähle als $u$ (das abgeleitet wird) den Faktor, der in der folgenden Liste zuerst kommt:
> - **L**ogarithmen: $\ln x$, $\log x$
> - **I**nverse trigonometrische Funktionen: $\arcsin x$, $\arctan x$
> - **A**lgebraische Funktionen: $x$, $x^2$, $x^n$
> - **T**rigonometrische Funktionen: $\sin x$, $\cos x$
> - **E**xponentialfunktionen: $e^x$, $a^x$

---

## Beispiele

### Beispiel 1: Polynom mal Exponentialfunktion

Berechne $\int x \cdot e^x \, dx$

**Lösung:**

Nach LIATE: $u = x$ (algebraisch), $v' = e^x$ (exponentiell)

Berechne:
- $u = x \Rightarrow u' = 1$
- $v' = e^x \Rightarrow v = e^x$

Einsetzen:
$$\int x \cdot e^x \, dx = x \cdot e^x - \int 1 \cdot e^x \, dx = x \cdot e^x - e^x + C$$

$$= e^x(x - 1) + C$$

**Probe durch Ableiten:** $\frac{d}{dx}[e^x(x-1)] = e^x(x-1) + e^x \cdot 1 = e^x \cdot x = x \cdot e^x$ ✓

### Beispiel 2: Logarithmusfunktion

Berechne $\int \ln x \, dx$

**Lösung:**

Trick: Schreibe $\ln x = \ln x \cdot 1$

Nach LIATE: $u = \ln x$ (Logarithmus), $v' = 1$

Berechne:
- $u = \ln x \Rightarrow u' = \frac{1}{x}$
- $v' = 1 \Rightarrow v = x$

Einsetzen:
$$\int \ln x \, dx = \ln x \cdot x - \int \frac{1}{x} \cdot x \, dx = x \ln x - \int 1 \, dx$$

$$= x \ln x - x + C = x(\ln x - 1) + C$$

### Beispiel 3: Zweifache partielle Integration

Berechne $\int x^2 \cdot e^x \, dx$

**Lösung:**

**Erste partielle Integration:**
- $u = x^2 \Rightarrow u' = 2x$
- $v' = e^x \Rightarrow v = e^x$

$$\int x^2 \cdot e^x \, dx = x^2 \cdot e^x - \int 2x \cdot e^x \, dx$$

**Zweite partielle Integration** für $\int 2x \cdot e^x \, dx$:
- $u = 2x \Rightarrow u' = 2$
- $v' = e^x \Rightarrow v = e^x$

$$\int 2x \cdot e^x \, dx = 2x \cdot e^x - \int 2 \cdot e^x \, dx = 2x \cdot e^x - 2e^x$$

**Zusammensetzen:**
$$\int x^2 \cdot e^x \, dx = x^2 \cdot e^x - (2x \cdot e^x - 2e^x) + C$$

$$= e^x(x^2 - 2x + 2) + C$$

---

## Partielle Integration bei bestimmten Integralen

Die Formel für bestimmte Integrale lautet:

$$\int_a^b u \cdot v' \, dx = \left[u \cdot v\right]_a^b - \int_a^b u' \cdot v \, dx$$

### Beispiel: Bestimmtes Integral

Berechne $\int_0^1 x \cdot e^{-x} \, dx$

**Lösung:**

$u = x$, $v' = e^{-x}$ $\Rightarrow$ $u' = 1$, $v = -e^{-x}$

$$\int_0^1 x \cdot e^{-x} \, dx = \left[-x \cdot e^{-x}\right]_0^1 - \int_0^1 (-e^{-x}) \, dx$$

$$= \left[-x \cdot e^{-x}\right]_0^1 + \int_0^1 e^{-x} \, dx$$

$$= (-1 \cdot e^{-1} - 0) + \left[-e^{-x}\right]_0^1$$

$$= -e^{-1} + (-e^{-1} - (-e^0))$$

$$= -e^{-1} - e^{-1} + 1 = 1 - \frac{2}{e} \approx 0{,}264$$

---

## Spezialfall: Zyklische Integration

Manchmal führt die partielle Integration zurück zum ursprünglichen Integral. Dies nennt man **zyklische Integration**.

### Beispiel: $\int e^x \cdot \sin x \, dx$

**Erste partielle Integration:**
- $u = \sin x \Rightarrow u' = \cos x$
- $v' = e^x \Rightarrow v = e^x$

$$\int e^x \sin x \, dx = e^x \sin x - \int e^x \cos x \, dx$$

**Zweite partielle Integration:**
- $u = \cos x \Rightarrow u' = -\sin x$
- $v' = e^x \Rightarrow v = e^x$

$$\int e^x \cos x \, dx = e^x \cos x - \int e^x \cdot (-\sin x) \, dx = e^x \cos x + \int e^x \sin x \, dx$$

**Einsetzen:**
$$\int e^x \sin x \, dx = e^x \sin x - \left(e^x \cos x + \int e^x \sin x \, dx\right)$$

$$\int e^x \sin x \, dx = e^x \sin x - e^x \cos x - \int e^x \sin x \, dx$$

**Nach dem Integral auflösen:**
$$2 \int e^x \sin x \, dx = e^x(\sin x - \cos x)$$

$$\int e^x \sin x \, dx = \frac{e^x(\sin x - \cos x)}{2} + C$$

---

## Zusammenfassung: Wann welche Methode?

| Integraltyp | Methode | Beispiel |
|-------------|---------|----------|
| $\int x^n \cdot e^{ax} \, dx$ | Partielle Integration | $\int x^2 e^x \, dx$ |
| $\int x^n \cdot \sin(ax) \, dx$ | Partielle Integration | $\int x \cos x \, dx$ |
| $\int \ln x \, dx$ | Partielle Integration | – |
| $\int \arctan x \, dx$ | Partielle Integration | – |
| $\int f(g(x)) \cdot g'(x) \, dx$ | Substitution | $\int 2x \cdot e^{x^2} \, dx$ |

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Substitution|Substitution]] – Alternative Integrationstechnik
- → [[Produktregel|Produktregel]] – Die zugrunde liegende Differentiationsregel
- → [[Exponentialfunktionen|Exponentialfunktionen]] – Häufig bei partieller Integration
- → [[Trigonometrische-Funktionen|Trigonometrische Funktionen]] – Zyklische Integration
- → [[Logarithmusfunktionen|Logarithmusfunktionen]] – Integration von $\ln x$

> [!warning] **Prüfungsrelevant**
> - Die Faktorwahl (LIATE-Regel) ist entscheidend für den Erfolg
> - Bei $\int \ln x \, dx$ und $\int \arctan x \, dx$ wird mit "1" multipliziert
> - Zyklische Integration erfordert Auflösen nach dem gesuchten Integral
> - Bei bestimmten Integralen nicht vergessen: $[u \cdot v]_a^b$ auswerten!

> [!question] **Typische Prüfungsfragen**
> - Berechne $\int x \cdot \sin x \, dx$ mit partieller Integration.
> - Bestimme $\int_1^e x \cdot \ln x \, dx$.
> - Erkläre, warum bei $\int e^x \cos x \, dx$ das ursprüngliche Integral wieder auftaucht und wie man damit umgeht.

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1, Springer Vieweg, 2018
- Bronstein, I. N. et al.: Taschenbuch der Mathematik, Europa-Lehrmittel, 2020
- ISB Bayern: Lehrplan Mathematik Gymnasium, Analysis

> [!tip] **Weiterführende Links**
> - [[Substitution|Substitution]] – Die andere zentrale Integrationstechnik
> - [[Hauptsatz-der-Differential--und-Integralrechnung|Hauptsatz der Differential- und Integralrechnung]]
