---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - mathematik
---

# Zahlentheorie und modulare Arithmetik

> [!info] **Lernziele**
> - Teilbarkeit, Kongruenzen und Restklassen verstehen
> - In modularer Arithmetik rechnen (Addition, Multiplikation, Potenzieren)
> - Modulare Inverse berechnen und ihre Rolle in der Kryptographie einordnen

---

## Inhalt

### Teilbarkeit und Kongruenzen

Die Zahlentheorie ist das mathematische Fundament der modernen Kryptographie. Zentral ist der Begriff der **Kongruenz**: Zwei ganze Zahlen $a$ und $b$ heißen **kongruent modulo $n$**, wenn sie bei Division durch $n$ denselben Rest lassen:

$$a \equiv b \pmod{n} \quad \Longleftrightarrow \quad n \mid (a - b)$$

Beispiel: $17 \equiv 5 \pmod{12}$, denn $17 - 5 = 12$ ist durch 12 teilbar. Anschaulich ist das die „Uhrzeit-Arithmetik": 17 Uhr entspricht 5 Uhr am 12-Stunden-Zifferblatt.

### Rechnen in $\mathbb{Z}_n$

Die Restklassen modulo $n$ bilden die Menge $\mathbb{Z}_n = \{0, 1, 2, \dots, n-1\}$. Addition und Multiplikation funktionieren wie gewohnt, nur wird am Ende der Rest modulo $n$ genommen:

| Operation | Beispiel (mod 7) |
|-----------|------------------|
| Addition | $5 + 4 = 9 \equiv 2 \pmod 7$ |
| Subtraktion | $3 - 5 = -2 \equiv 5 \pmod 7$ |
| Multiplikation | $4 \cdot 5 = 20 \equiv 6 \pmod 7$ |

Wichtige Rechenregel: Man darf **jederzeit** reduzieren. Das hält Zwischenergebnisse klein – entscheidend, wenn Kryptoverfahren mit hunderten Stellen rechnen.

### Modulares Potenzieren

Verfahren wie RSA beruhen auf $c = m^e \bmod n$ mit sehr großen Exponenten. Naives Ausrechnen von $m^e$ wäre unmöglich groß. Stattdessen nutzt man **Square-and-Multiply**: den Exponenten binär zerlegen und abwechselnd quadrieren und multiplizieren, jeweils modulo $n$.

Beispiel $7^{13} \bmod 11$ mit $13 = 1101_2$:

```
7^1  mod 11 = 7
7^2  mod 11 = 49 mod 11 = 5
7^4  mod 11 = 5^2 mod 11 = 25 mod 11 = 3
7^8  mod 11 = 3^2 mod 11 = 9
7^13 = 7^8 · 7^4 · 7^1 = 9 · 3 · 7 = 189 mod 11 = 2
```

### Modulare Inverse

Das **multiplikative Inverse** von $a$ modulo $n$ ist die Zahl $a^{-1}$ mit

$$a \cdot a^{-1} \equiv 1 \pmod{n}.$$

Es existiert **genau dann**, wenn $\gcd(a, n) = 1$ (also $a$ und $n$ teilerfremd sind). Beispiel: $3^{-1} \equiv 4 \pmod{11}$, denn $3 \cdot 4 = 12 \equiv 1 \pmod{11}$.

Modulare Inverse sind in der Kryptographie allgegenwärtig – etwa bei der Berechnung des privaten RSA-Exponenten $d \equiv e^{-1} \pmod{\varphi(n)}$. Berechnet werden sie mit dem erweiterten euklidischen Algorithmus (→ [[03-Euklidischer-Algorithmus]]).

### Der kleine Satz von Fermat

Für eine Primzahl $p$ und $a$ mit $\gcd(a,p)=1$ gilt:

$$a^{p-1} \equiv 1 \pmod{p}.$$

Dieser Satz vereinfacht modulares Potenzieren und ist Grundlage mehrerer Primzahltests (→ [[02-Primzahlen-und-Primfaktorzerlegung]]).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Kongruenz $a \equiv b \pmod n$ bedeutet gleicher Rest bei Division durch $n$
> - In $\mathbb{Z}_n$ darf jederzeit modulo reduziert werden
> - Modulares Potenzieren erfolgt effizient per Square-and-Multiply
> - Das Inverse $a^{-1} \bmod n$ existiert genau dann, wenn $\gcd(a,n)=1$

---

## Übungen

1. Berechnen Sie $(23 + 19) \bmod 7$ und $(23 \cdot 19) \bmod 7$.
2. Bestimmen Sie $3^{20} \bmod 11$ mit Square-and-Multiply.
3. Finden Sie das multiplikative Inverse von $5$ modulo $13$.

---

← [[00-Mathematik-Index|Zurück zur Übersicht]] | [[02-Primzahlen-und-Primfaktorzerlegung|Weiter →]]
