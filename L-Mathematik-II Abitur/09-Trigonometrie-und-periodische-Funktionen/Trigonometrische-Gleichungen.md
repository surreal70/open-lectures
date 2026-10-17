---
author: Andreas Hümmer
title: Trigonometrische Gleichungen
tags:
  - content
  - mathe
  - trigonometrie
  - gleichungen
  - loesungsverfahren
created: 2025-06-20
modified: 2025-06-20
---

# Trigonometrische Gleichungen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Grundlegende trigonometrische Gleichungen systematisch lösen können
> - Die allgemeine Lösungsstruktur mit $k \in \mathbb{Z}$ verstehen
> - Substitutionen und Umformungen gezielt einsetzen können
> - Lösungen in vorgegebenen Intervallen vollständig angeben können

---

## Überblick

**Trigonometrische Gleichungen** sind Gleichungen, in denen die Unbekannte als Argument einer trigonometrischen Funktion auftritt. Aufgrund der Periodizität von Sinus, Kosinus und Tangens haben diese Gleichungen typischerweise **unendlich viele Lösungen**. Die systematische Bestimmung aller Lösungen und die Einschränkung auf ein bestimmtes Intervall sind zentrale Fertigkeiten im Abitur.

## Grundtypen und ihre Lösungen

### Typ 1: $\sin(x) = a$

Für $|a| \leq 1$ gilt:

$$\sin(x) = a \quad \Leftrightarrow \quad x = \arcsin(a) + 2k\pi \quad \text{oder} \quad x = \pi - \arcsin(a) + 2k\pi$$

mit $k \in \mathbb{Z}$.

**Beispiel:** $\sin(x) = \frac{1}{2}$

$$x_1 = \arcsin\left(\frac{1}{2}\right) = \frac{\pi}{6}$$
$$x_2 = \pi - \frac{\pi}{6} = \frac{5\pi}{6}$$

Allgemeine Lösung:
$$x = \frac{\pi}{6} + 2k\pi \quad \text{oder} \quad x = \frac{5\pi}{6} + 2k\pi, \quad k \in \mathbb{Z}$$

### Typ 2: $\cos(x) = a$

Für $|a| \leq 1$ gilt:

$$\cos(x) = a \quad \Leftrightarrow \quad x = \pm \arccos(a) + 2k\pi$$

mit $k \in \mathbb{Z}$.

**Beispiel:** $\cos(x) = -\frac{1}{2}$

$$x = \pm \arccos\left(-\frac{1}{2}\right) = \pm \frac{2\pi}{3}$$

Allgemeine Lösung:
$$x = \frac{2\pi}{3} + 2k\pi \quad \text{oder} \quad x = -\frac{2\pi}{3} + 2k\pi, \quad k \in \mathbb{Z}$$

### Typ 3: $\tan(x) = a$

$$\tan(x) = a \quad \Leftrightarrow \quad x = \arctan(a) + k\pi$$

mit $k \in \mathbb{Z}$.

**Beispiel:** $\tan(x) = 1$

$$x = \arctan(1) + k\pi = \frac{\pi}{4} + k\pi, \quad k \in \mathbb{Z}$$

## Lösungsstrategien

### Strategie 1: Direkte Umkehrfunktion

Wenn die Gleichung bereits in der Form $\sin(x) = a$, $\cos(x) = a$ oder $\tan(x) = a$ vorliegt:

1. Prüfen, ob Lösungen existieren ($|a| \leq 1$ bei sin/cos)
2. Hauptlösung mit Taschenrechner oder bekannten Werten bestimmen
3. Alle Lösungen durch Periodizität ergänzen

### Strategie 2: Substitution bei mehrfachen Argumenten

Bei Gleichungen wie $\sin(2x) = a$ oder $\cos(3x) = a$:

1. Substitution: $u = 2x$ (bzw. $u = 3x$)
2. Gleichung $\sin(u) = a$ lösen
3. Rücksubstitution und Division

**Beispiel:** Löse $\sin(2x) = \frac{\sqrt{3}}{2}$ im Intervall $[0, 2\pi]$

Substitution: $u = 2x$, Intervall für $u$: $[0, 4\pi]$

$$\sin(u) = \frac{\sqrt{3}}{2}$$
$$u = \frac{\pi}{3} + 2k\pi \quad \text{oder} \quad u = \frac{2\pi}{3} + 2k\pi$$

In $[0, 4\pi]$: $u \in \left\{\frac{\pi}{3}, \frac{2\pi}{3}, \frac{7\pi}{3}, \frac{8\pi}{3}\right\}$

Rücksubstitution: $x = \frac{u}{2}$:
$$x \in \left\{\frac{\pi}{6}, \frac{\pi}{3}, \frac{7\pi}{6}, \frac{4\pi}{3}\right\}$$

### Strategie 3: Quadratische Gleichungen in sin/cos

Bei Gleichungen wie $2\sin^2(x) - \sin(x) - 1 = 0$:

1. Substitution: $u = \sin(x)$
2. Quadratische Gleichung $2u^2 - u - 1 = 0$ lösen
3. Für jede Lösung $u$ die Gleichung $\sin(x) = u$ lösen

**Beispiel:** $2\sin^2(x) - \sin(x) - 1 = 0$

Substitution $u = \sin(x)$:
$$2u^2 - u - 1 = 0$$
$$u = \frac{1 \pm \sqrt{1 + 8}}{4} = \frac{1 \pm 3}{4}$$
$$u_1 = 1, \quad u_2 = -\frac{1}{2}$$

Rücksubstitution:
- $\sin(x) = 1 \Rightarrow x = \frac{\pi}{2} + 2k\pi$
- $\sin(x) = -\frac{1}{2} \Rightarrow x = -\frac{\pi}{6} + 2k\pi$ oder $x = \pi + \frac{\pi}{6} + 2k\pi$

### Strategie 4: Anwendung von Identitäten

Verwende trigonometrische Identitäten, um die Gleichung zu vereinfachen.

**Beispiel:** $\sin^2(x) = \cos^2(x)$

Mit $\sin^2(x) + \cos^2(x) = 1$:
$$\sin^2(x) = 1 - \sin^2(x)$$
$$2\sin^2(x) = 1$$
$$\sin(x) = \pm \frac{1}{\sqrt{2}}$$

Lösung: $x = \frac{\pi}{4} + \frac{k\pi}{2}$, $k \in \mathbb{Z}$

Alternativ: $\tan(x) = \pm 1 \Rightarrow x = \pm \frac{\pi}{4} + k\pi$

## Lösungen in vorgegebenen Intervallen

### Systematisches Vorgehen

1. Allgemeine Lösung bestimmen
2. Werte von $k$ finden, für die die Lösung im Intervall liegt
3. Alle gültigen Lösungen aufzählen

**Beispiel:** Alle Lösungen von $\cos(x) = \frac{1}{2}$ in $[-\pi, \pi]$

Allgemeine Lösung: $x = \pm \frac{\pi}{3} + 2k\pi$

Für $k = 0$: $x = \frac{\pi}{3}$ und $x = -\frac{\pi}{3}$ ✓

Für $k = 1$: $x = \frac{\pi}{3} + 2\pi$ (nicht in $[-\pi, \pi]$)

Lösungen: $x \in \left\{-\frac{\pi}{3}, \frac{\pi}{3}\right\}$

## Komplexere Gleichungen

### Gleichungen mit Phasenverschiebung

**Beispiel:** $\sin\left(x - \frac{\pi}{4}\right) = \frac{1}{2}$

Substitution: $u = x - \frac{\pi}{4}$

$$\sin(u) = \frac{1}{2}$$
$$u = \frac{\pi}{6} + 2k\pi \quad \text{oder} \quad u = \frac{5\pi}{6} + 2k\pi$$

Rücksubstitution:
$$x = \frac{\pi}{6} + \frac{\pi}{4} + 2k\pi = \frac{5\pi}{12} + 2k\pi$$
$$x = \frac{5\pi}{6} + \frac{\pi}{4} + 2k\pi = \frac{13\pi}{12} + 2k\pi$$

### Gleichungen mit verschiedenen Funktionen

**Beispiel:** $\sin(x) = \cos(x)$

Division durch $\cos(x)$ (für $\cos(x) \neq 0$):
$$\tan(x) = 1$$
$$x = \frac{\pi}{4} + k\pi, \quad k \in \mathbb{Z}$$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Sinus-und-Kosinus]] – Eigenschaften der beteiligten Funktionen
- → [[Trigonometrische-Identitaeten]] – Umformungen für komplexe Gleichungen
- → [[Additionstheoreme]] – Gleichungen mit Winkelsummen
- → [[Einheitskreis]] – Geometrische Interpretation der Lösungen

> [!warning] **Prüfungsrelevant**
> - Die allgemeine Lösungsstruktur mit $+ 2k\pi$ bzw. $+ k\pi$ sicher beherrschen
> - Substitution bei mehrfachen Argumenten ($\sin(2x)$, $\cos(3x)$, ...)
> - Quadratische Gleichungen in $\sin(x)$ oder $\cos(x)$ lösen können
> - Lösungen in vorgegebenen Intervallen vollständig angeben

> [!question] **Typische Prüfungsfragen**
> - Bestimmen Sie alle Lösungen von $2\cos^2(x) - 1 = 0$ im Intervall $[0, 2\pi]$.
> - Lösen Sie die Gleichung $\sin(2x) = \cos(x)$.
> - Wie viele Lösungen hat $\sin(3x) = 0$ im Intervall $[0, \pi]$?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I.N. et al.: Taschenbuch der Mathematik. Verlag Europa-Lehrmittel, 2020.
- Lambacher Schweizer: Mathematik für Gymnasien, Oberstufe. Klett Verlag, 2019.

> [!tip] **Weiterführende Links**
> - [[Trigonometrische-Identitaeten]] – Nützliche Umformungen
> - [[Sinus--und-Kosinusfunktionen]] – Gleichungen mit Parametern
