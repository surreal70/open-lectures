---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - mathematik
---

# Komplexitätstheorie

> [!info] **Lernziele**
> - Die Landau-Notation zur Einordnung von Laufzeiten verstehen
> - Die Klassen P und NP sowie „schwere" Probleme einordnen
> - Erkennen, warum Kryptographie auf Berechnungshärte beruht

---

## Inhalt

### Laufzeit und Landau-Notation

Die Komplexitätstheorie untersucht, wie der Rechenaufwand eines Algorithmus mit der Eingabegröße $n$ wächst. Die **Landau-Notation** ($O$-Notation) beschreibt das asymptotische Verhalten:

| Klasse | Name | Beispiel |
|--------|------|----------|
| $O(1)$ | konstant | Array-Zugriff |
| $O(\log n)$ | logarithmisch | euklidischer Algorithmus |
| $O(n)$ | linear | Liste durchsuchen |
| $O(n^k)$ | polynomiell | Matrixmultiplikation |
| $O(2^n)$ | exponentiell | Brute-Force über alle Schlüssel |

Entscheidend ist die Grenze zwischen **polynomiell** (praktisch lösbar) und **exponentiell / superpolynomiell** (praktisch unlösbar für große $n$).

### Die Klassen P und NP

- **P:** Probleme, die in polynomieller Zeit **gelöst** werden können.
- **NP:** Probleme, deren Lösung in polynomieller Zeit **verifiziert** werden kann.

Die offene Frage **P = NP?** gehört zu den größten ungelösten Problemen der Informatik. Die Kryptographie **hofft** (und setzt darauf), dass $P \neq NP$ – andernfalls wären viele Verfahren gefährdet.

> [!note] **Wichtige Klarstellung**
> Die Sicherheit heutiger Verfahren beruht nicht direkt auf NP-Vollständigkeit, sondern auf spezifischen Problemen, die man für schwer hält: **Faktorisierung** (RSA) und **diskreter Logarithmus** (Diffie-Hellman, ECC). Diese liegen in NP, gelten aber als „mittelschwer" – sie sind nicht als NP-vollständig bekannt.

### Berechnungshärte als Sicherheitsgrundlage

Kryptographie nutzt Probleme, bei denen eine Richtung leicht und die Umkehrung schwer ist (**Einwegfunktionen**):

| Verfahren | Leicht | Schwer |
|-----------|--------|--------|
| RSA | Multiplizieren $p \cdot q$ | Faktorisieren von $n$ |
| Diffie-Hellman | $g^x \bmod p$ berechnen | diskreten Logarithmus $x$ finden |
| ECC | Punktmultiplikation $kP$ | $k$ aus $kP$ zurückrechnen |

Sicherheit bedeutet hier: Der beste bekannte Angriff braucht **superpolynomiellen** Aufwand. Die Schlüssellänge wird so gewählt, dass dieser Aufwand jenseits des praktisch Machbaren liegt (→ Modul 5: Schlüssellängen und Sicherheitsniveaus).

### Grenzen des Modells

Komplexitätsaussagen sind **asymptotisch** und beziehen sich auf klassische Rechner. Quantencomputer verändern die Landschaft: Der Shor-Algorithmus löst Faktorisierung und diskreten Logarithmus in polynomieller Zeit – deshalb die Entwicklung der Post-Quanten-Kryptographie (→ Modul 13).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Die Landau-Notation beschreibt das asymptotische Wachstum von Laufzeiten
> - Grenze polynomiell (machbar) vs. exponentiell (unmachbar) ist entscheidend
> - Kryptographie beruht auf vermuteter Härte: Faktorisierung, diskreter Logarithmus
> - Quantencomputer brechen diese Annahmen für RSA/ECC (Shor)

---

## Übungen

1. Ordnen Sie $O(n^2)$, $O(2^n)$, $O(\log n)$ und $O(n \log n)$ nach Wachstum.
2. Erklären Sie den Unterschied zwischen „in P lösbar" und „in NP verifizierbar".
3. Warum wäre die Kryptographie gefährdet, falls $P = NP$ bewiesen würde?

---

← [[05-Wahrscheinlichkeitsrechnung-und-Entropie|← Zurück]] | [[00-Mathematik-Index|Übersicht]] | [[00-Klassisch-Index|Nächstes Modul →]]
