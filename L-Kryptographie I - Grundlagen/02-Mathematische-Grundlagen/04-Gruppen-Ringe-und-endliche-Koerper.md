---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - mathematik
---

# Gruppen, Ringe und endliche Körper

> [!info] **Lernziele**
> - Die algebraischen Strukturen Gruppe, Ring und Körper unterscheiden
> - Endliche Körper (Galois-Felder) und ihre Bedeutung verstehen
> - Den Bezug zu AES und elliptischen Kurven herstellen

---

## Inhalt

### Gruppen

Eine **Gruppe** $(G, \ast)$ ist eine Menge mit einer Verknüpfung $\ast$, die vier Eigenschaften erfüllt:

1. **Abgeschlossenheit:** $a \ast b \in G$
2. **Assoziativität:** $(a \ast b) \ast c = a \ast (b \ast c)$
3. **Neutrales Element:** es gibt $e$ mit $a \ast e = a$
4. **Inverses Element:** zu jedem $a$ existiert $a^{-1}$ mit $a \ast a^{-1} = e$

Gilt zusätzlich $a \ast b = b \ast a$, heißt die Gruppe **abelsch**. Beispiel: $(\mathbb{Z}_n, +)$ ist eine abelsche Gruppe. Die invertierbaren Elemente unter Multiplikation bilden die Gruppe $\mathbb{Z}_n^{\ast}$.

> [!example] **Zyklische Gruppen**
> Eine Gruppe ist **zyklisch**, wenn ein Element $g$ (ein **Generator**) durch wiederholte Verknüpfung alle Elemente erzeugt. Das Diffie-Hellman-Verfahren und ECC beruhen darauf, dass das Umkehren dieser Erzeugung (der **diskrete Logarithmus**) schwer ist.

### Ringe

Ein **Ring** $(R, +, \cdot)$ besitzt zwei Verknüpfungen: Bezüglich $+$ ist er eine abelsche Gruppe, $\cdot$ ist assoziativ, und es gelten die Distributivgesetze. Ein multiplikatives Inverses wird **nicht** für alle Elemente verlangt. Beispiel: $(\mathbb{Z}_n, +, \cdot)$ ist ein Ring.

### Körper

Ein **Körper** ist ein Ring, in dem **jedes Element außer 0** ein multiplikatives Inverses hat. In einem Körper kann man uneingeschränkt addieren, subtrahieren, multiplizieren und dividieren.

- $\mathbb{Z}_p$ ist genau dann ein Körper, wenn $p$ **prim** ist (dann ist jedes Element $\neq 0$ invertierbar).
- $\mathbb{Z}_6$ ist kein Körper: $2$ und $3$ haben kein Inverses.

### Endliche Körper (Galois-Felder)

**Endliche Körper** $\mathrm{GF}(q)$ existieren genau dann, wenn $q = p^m$ eine Primzahlpotenz ist. Zwei Fälle sind kryptographisch wichtig:

| Körper | Form | Anwendung |
|--------|------|-----------|
| $\mathrm{GF}(p)$ | $\mathbb{Z}_p$ (Primkörper) | Diffie-Hellman, DSA |
| $\mathrm{GF}(2^m)$ | Polynome über $\mathbb{Z}_2$ | AES, einige ECC-Kurven |

**AES** rechnet im Körper $\mathrm{GF}(2^8)$: Jedes Byte ist ein Polynom vom Grad $< 8$ mit Koeffizienten aus $\{0,1\}$. Multiplikation erfolgt modulo eines irreduziblen Polynoms. Genau das macht die AES-S-Box und die MixColumns-Operation mathematisch sauber invertierbar.

**Elliptische Kurven** (→ Modul 5) werden über endlichen Körpern definiert; die Punkte der Kurve bilden eine abelsche Gruppe, in der der diskrete Logarithmus schwer ist.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Gruppe: eine Verknüpfung mit Neutral- und Inversenelementen
> - Ring: zwei Verknüpfungen, aber nicht jedes Element multiplikativ invertierbar
> - Körper: Division (außer durch 0) immer möglich – $\mathbb{Z}_p$ nur für primes $p$
> - Endliche Körper $\mathrm{GF}(p)$ und $\mathrm{GF}(2^m)$ sind Grundlage von AES, DH und ECC

---

## Übungen

1. Ist $(\mathbb{Z}_5, +, \cdot)$ ein Körper? Begründen Sie.
2. Nennen Sie ein Element in $\mathbb{Z}_8$, das kein multiplikatives Inverses besitzt.
3. In welchem endlichen Körper rechnet AES, und warum ist diese Struktur vorteilhaft?

---

← [[03-Euklidischer-Algorithmus|← Zurück]] | [[00-Mathematik-Index|Übersicht]] | [[05-Wahrscheinlichkeitsrechnung-und-Entropie|Weiter →]]
