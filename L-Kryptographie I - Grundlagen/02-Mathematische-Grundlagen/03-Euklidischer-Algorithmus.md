---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - mathematik
---

# Euklidischer Algorithmus

> [!info] **Lernziele**
> - Den größten gemeinsamen Teiler mit dem euklidischen Algorithmus berechnen
> - Den erweiterten euklidischen Algorithmus anwenden
> - Modulare Inverse damit praktisch bestimmen

---

## Inhalt

### Der größte gemeinsame Teiler (ggT)

Der **größte gemeinsame Teiler** $\gcd(a, b)$ ist die größte Zahl, die sowohl $a$ als auch $b$ teilt. Zwei Zahlen mit $\gcd(a,b)=1$ heißen **teilerfremd (koprim)** – eine zentrale Bedingung für die Existenz modularer Inverse.

### Der euklidische Algorithmus

Die Idee: $\gcd(a, b) = \gcd(b, a \bmod b)$, bis der Rest 0 wird. Der letzte nicht-null Rest ist der ggT.

Beispiel $\gcd(48, 18)$:

```
48 = 2 · 18 + 12
18 = 1 · 12 +  6
12 = 2 ·  6 +  0   → ggT = 6
```

Der Algorithmus ist extrem effizient: Die Anzahl der Schritte wächst nur logarithmisch mit den Eingaben (Satz von Lamé).

### Der erweiterte euklidische Algorithmus

Dieser berechnet zusätzlich zwei Koeffizienten $x$ und $y$, welche die **Bézout-Identität** erfüllen:

$$a \cdot x + b \cdot y = \gcd(a, b).$$

Das ist genau das Werkzeug, um **modulare Inverse** zu finden. Ist $\gcd(a, n) = 1$, liefert

$$a \cdot x + n \cdot y = 1 \quad \Longrightarrow \quad a \cdot x \equiv 1 \pmod{n},$$

also ist $x = a^{-1} \bmod n$.

### Beispiel: Inverse von 7 modulo 26

Zuerst vorwärts (euklidisch):

```
26 = 3 · 7 + 5
 7 = 1 · 5 + 2
 5 = 2 · 2 + 1
 2 = 2 · 1 + 0   → ggT = 1 (also invertierbar)
```

Dann rückwärts einsetzen:

```
1 = 5 − 2·2
  = 5 − 2·(7 − 1·5) = 3·5 − 2·7
  = 3·(26 − 3·7) − 2·7 = 3·26 − 11·7
```

Daraus: $-11 \cdot 7 \equiv 1 \pmod{26}$, und $-11 \equiv 15 \pmod{26}$. Also $7^{-1} \equiv 15 \pmod{26}$ (Probe: $7 \cdot 15 = 105 = 4 \cdot 26 + 1$).

> [!example] **Kryptographischer Bezug**
> Bei RSA wird der private Exponent als $d \equiv e^{-1} \pmod{\varphi(n)}$ genau mit diesem Verfahren berechnet. Das Beispiel mod 26 entspricht außerdem der Schlüsselinversion bei der affinen Chiffre (26 Buchstaben).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - $\gcd(a,b)=\gcd(b, a \bmod b)$ – der euklidische Algorithmus ist logarithmisch schnell
> - Der erweiterte Algorithmus liefert $ax + by = \gcd(a,b)$ (Bézout)
> - Damit berechnet man modulare Inverse: aus $ax+ny=1$ folgt $x = a^{-1} \bmod n$
> - Grundlage der RSA-Schlüsselerzeugung

---

## Übungen

1. Berechnen Sie $\gcd(1071, 462)$ mit dem euklidischen Algorithmus.
2. Bestimmen Sie mit dem erweiterten Algorithmus das Inverse von $11$ modulo $26$.
3. Warum existiert kein Inverses von $4$ modulo $26$?

---

← [[02-Primzahlen-und-Primfaktorzerlegung|← Zurück]] | [[00-Mathematik-Index|Übersicht]] | [[04-Gruppen-Ringe-und-endliche-Koerper|Weiter →]]
