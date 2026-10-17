---
author: Andreas Hümmer
title: Arithmetische Folgen
tags:
  - content
  - mathe
  - folgen
  - arithmetische-folge
  - analysis
created: 2025-06-17
modified: 2025-06-17
---

# Arithmetische Folgen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Definition einer arithmetischen Folge verstehen und anwenden können
> - Das explizite Bildungsgesetz und die rekursive Darstellung beherrschen
> - Die Summenformel für arithmetische Reihen herleiten und anwenden können
> - Anwendungsaufgaben zu arithmetischen Folgen lösen können

---

## Überblick

Eine **arithmetische Folge** ist eine Zahlenfolge, bei der die Differenz zwischen aufeinanderfolgenden Gliedern konstant ist. Diese konstante Differenz wird als **Differenz** $d$ bezeichnet. Arithmetische Folgen modellieren lineare Wachstums- oder Abnahmeprozesse und sind das diskrete Pendant zu linearen Funktionen.

Typische Anwendungen sind gleichmäßige Abzahlungen, regelmäßige Einsparungen oder die Sitzreihen in einem Amphitheater, bei dem jede Reihe eine feste Anzahl mehr Sitze hat als die vorherige.

## Definition und Eigenschaften

### Definition

Eine Folge $(a_n)$ heißt **arithmetische Folge**, wenn für alle $n \in \mathbb{N}$ gilt:

$$a_{n+1} - a_n = d \quad \text{(konstante Differenz)}$$

Äquivalent: Die Differenz $d = a_{n+1} - a_n$ ist unabhängig von $n$.

### Charakteristische Größen

| Größe | Symbol | Bedeutung |
|-------|--------|-----------|
| Anfangsglied | $a_1$ | Erster Wert der Folge |
| Differenz | $d$ | Konstanter Zuwachs pro Schritt |
| $n$-tes Glied | $a_n$ | Wert an Position $n$ |

### Darstellungsformen

**Explizite Darstellung:**
$$a_n = a_1 + (n-1) \cdot d$$

**Rekursive Darstellung:**
$$a_{n+1} = a_n + d \quad \text{mit Startwert } a_1$$

**Beispiel:** Arithmetische Folge mit $a_1 = 3$ und $d = 4$

$$a_n = 3 + (n-1) \cdot 4 = 4n - 1$$

Die Folge lautet: $(3, 7, 11, 15, 19, \ldots)$

## Die Gaußsche Summenformel

### Herleitung

Die Summe der ersten $n$ Glieder einer arithmetischen Folge heißt **arithmetische Reihe**:

$$S_n = a_1 + a_2 + \ldots + a_n = \sum_{k=1}^{n} a_k$$

**Trick von Gauß:** Schreibe die Summe vorwärts und rückwärts:

$$\begin{align}
S_n &= a_1 + a_2 + \ldots + a_{n-1} + a_n \\
S_n &= a_n + a_{n-1} + \ldots + a_2 + a_1
\end{align}$$

Addition ergibt:
$$2S_n = (a_1 + a_n) + (a_2 + a_{n-1}) + \ldots = n \cdot (a_1 + a_n)$$

### Summenformel

$$\boxed{S_n = \frac{n}{2} \cdot (a_1 + a_n) = \frac{n}{2} \cdot (2a_1 + (n-1) \cdot d)}$$

**Merkregel:** "Anzahl mal Durchschnitt" – die Summe ist die Anzahl der Glieder multipliziert mit dem arithmetischen Mittel aus erstem und letztem Glied.

### Beispiel: Summe der ersten 100 natürlichen Zahlen

$$S_{100} = 1 + 2 + 3 + \ldots + 100$$

Mit $a_1 = 1$, $a_{100} = 100$, $n = 100$:

$$S_{100} = \frac{100}{2} \cdot (1 + 100) = 50 \cdot 101 = 5050$$

## Mittelwert-Eigenschaft

### Arithmetisches Mittel

In einer arithmetischen Folge ist jedes Glied (außer dem ersten und letzten) das **arithmetische Mittel** seiner beiden Nachbarn:

$$a_n = \frac{a_{n-1} + a_{n+1}}{2}$$

**Beweis:** Mit $a_{n-1} = a_n - d$ und $a_{n+1} = a_n + d$:

$$\frac{a_{n-1} + a_{n+1}}{2} = \frac{(a_n - d) + (a_n + d)}{2} = \frac{2a_n}{2} = a_n \quad \checkmark$$

Diese Eigenschaft kann genutzt werden, um zu prüfen, ob drei Zahlen Teil einer arithmetischen Folge sein können.

## Bestimmung einer arithmetischen Folge

### Aus zwei Gliedern

Gegeben seien $a_m$ und $a_k$ mit $m < k$. Dann:

$$d = \frac{a_k - a_m}{k - m}$$

$$a_1 = a_m - (m-1) \cdot d$$

**Beispiel:** Gegeben: $a_3 = 11$ und $a_7 = 27$

$$d = \frac{27 - 11}{7 - 3} = \frac{16}{4} = 4$$

$$a_1 = 11 - 2 \cdot 4 = 3$$

Also: $a_n = 3 + (n-1) \cdot 4 = 4n - 1$

### Aus Anfangsglied und Summe

Gegeben seien $a_1$ und $S_n$. Dann:

$$d = \frac{2(S_n - n \cdot a_1)}{n(n-1)}$$

## Anwendungsbeispiele

### Beispiel 1: Ratenzahlung

Ein Kredit von 12.000 € wird in 24 Monatsraten abbezahlt. Die erste Rate beträgt 600 €, jede weitere Rate ist 10 € geringer.

**Gesucht:** Wie viel wurde insgesamt zurückgezahlt?

**Lösung:** 
- $a_1 = 600$, $d = -10$, $n = 24$
- $a_{24} = 600 + 23 \cdot (-10) = 370$
- $S_{24} = \frac{24}{2} \cdot (600 + 370) = 12 \cdot 970 = 11.640$ €

### Beispiel 2: Sitzreihen im Theater

Ein Theater hat 20 Reihen. Die erste Reihe hat 15 Sitze, jede weitere Reihe 3 Sitze mehr.

**Gesucht:** 
a) Wie viele Sitze hat die letzte Reihe?
b) Wie viele Sitze hat das Theater insgesamt?

**Lösung:**
a) $a_{20} = 15 + 19 \cdot 3 = 72$ Sitze

b) $S_{20} = \frac{20}{2} \cdot (15 + 72) = 10 \cdot 87 = 870$ Sitze

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Zahlenfolgen]] – Allgemeiner Folgenbegriff
- → [[Geometrische-Folgen]] – Folgen mit konstantem Quotienten (nicht konstanter Differenz)
- → [[Lineare-Funktionen]] – Kontinuierliches Pendant zur arithmetischen Folge
- → [[Grenzwerte-von-Folgen]] – Arithmetische Folgen haben keinen endlichen Grenzwert (außer $d = 0$)

> [!warning] **Prüfungsrelevant**
> - Explizite Formel $a_n = a_1 + (n-1) \cdot d$ muss sicher beherrscht werden
> - Summenformel $S_n = \frac{n}{2}(a_1 + a_n)$ ist Standardwissen
> - Textaufgaben zu Ratenzahlung und gleichmäßigem Wachstum sind häufig
> - Unterscheidung zu geometrischen Folgen wird gerne abgefragt

> [!question] **Typische Prüfungsfragen**
> - Bestimme das Bildungsgesetz der arithmetischen Folge mit $a_3 = 10$ und $a_8 = 25$.
> - Berechne die Summe aller natürlichen Zahlen von 50 bis 150.
> - Ein Betrieb steigert seine Produktion jährlich um 200 Einheiten. Im ersten Jahr wurden 1500 Einheiten produziert. Nach wie vielen Jahren ist die Gesamtproduktion erstmals größer als 50.000 Einheiten?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Bronstein, I. N. et al.: Taschenbuch der Mathematik. Europa-Lehrmittel, 2020.
- Tietze, J.: Einführung in die angewandte Wirtschaftsmathematik. Springer Spektrum, 2019.

> [!tip] **Weiterführende Links**
> - [[Unendliche-geometrische-Reihen]] – Was passiert bei unendlich vielen Summanden?
> - [[Wachstumsprozesse]] – Vergleich linearer und exponentieller Modelle
