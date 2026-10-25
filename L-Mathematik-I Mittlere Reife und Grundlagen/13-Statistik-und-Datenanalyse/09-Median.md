---
title: Median (Zentralwert)
chapter: "13"
section: "13.9"
type: lecture
created: 2026-10-13
modified: 2026-10-25
status: draft - review pending
tags:
  - mathematik/statistik
  - median
  - lageparameter
---

# Median (Zentralwert)

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Den Median bestimmen
> - Median und Mittelwert vergleichen
> - Den geeigneten Lageparameter wählen

Der Median – auch Zentralwert genannt – ist ein **robuster** Lageparameter: Er wird von Ausreißern kaum beeinflusst. Während ein einzelner extremer Wert den Durchschnitt stark verzerren kann, bleibt der Median davon nahezu unberührt.

### Historischer Hintergrund

Das Konzept des Medians wurde im 19. Jahrhundert vom belgischen Statistiker Adolphe Quetelet populär gemacht. Der Begriff stammt vom lateinischen *medianus* (in der Mitte befindlich). In der modernen Statistik hat der Median große Bedeutung, weil er weniger anfällig für Verzerrungen ist als der Mittelwert – deshalb werden Einkommensstatistiken oft als Median angegeben.

## Definition

> [!note] Definition
> Der **Median** ist der mittlere Wert einer **geordneten** Datenreihe. Er teilt die Daten in zwei gleich große Hälften: 50% der Werte liegen darunter, 50% darüber.

> [!tip] **Anschauliche Vorstellung**
> Stelle alle Schüler nach Körpergröße sortiert in einer Reihe auf. Der Schüler, der genau in der Mitte steht, repräsentiert den Median der Körpergröße.

## Berechnung

### Schritt 1: Daten ordnen

Bringe alle Werte in aufsteigende Reihenfolge – vom kleinsten zum größten.

### Schritt 2: Mittleren Wert bestimmen

Die Berechnung hängt davon ab, ob die Anzahl der Werte ungerade oder gerade ist:

### Ungerade Anzahl

Bei $n$ Werten (ungerade): Der Median ist der $\left(\frac{n+1}{2}\right)$-te Wert.

> [!example] Beispiel (ungerade Anzahl)
> **Rohdaten:** 3, 7, 2, 9, 5
> 
> **Schritt 1 – Ordnen:** 2, 3, **5**, 7, 9
> 
> **Schritt 2 – Position berechnen:** $\frac{5+1}{2} = 3$, also der 3. Wert
> 
> **Median = 5**

### Gerade Anzahl

Bei $n$ Werten (gerade): Der Median ist das arithmetische Mittel der beiden mittleren Werte.

> [!example] Beispiel (gerade Anzahl)
> **Rohdaten:** 4, 8, 2, 6, 1, 9
> 
> **Schritt 1 – Ordnen:** 1, 2, **4**, **6**, 8, 9
> 
> **Schritt 2 – Mittlere Positionen:** $\frac{6}{2} = 3$ und $\frac{6}{2}+1 = 4$
> 
> Die beiden mittleren Werte sind der 3. (= 4) und 4. (= 6) Wert.
> 
> **Median** = $\frac{4 + 6}{2} = 5$

> [!tip] **Merkregel**
> - **Ungerade Anzahl:** Der mittlere Wert ist eindeutig – nimm ihn!
> - **Gerade Anzahl:** Es gibt zwei mittlere Werte – nimm ihren Durchschnitt!

## Vergleich mit Mittelwert

Das folgende Beispiel zeigt den entscheidenden Unterschied zwischen Median und arithmetischem Mittel:

> [!example] **Einkommensbeispiel**
> Fünf Personen verdienen: 2000, 2100, 2200, 2300, 50000 €
> 
> **Arithmetisches Mittel:**
> $$\bar{x} = \frac{2000 + 2100 + 2200 + 2300 + 50000}{5} = \frac{58600}{5} = 11720 \text{ €}$$
> 
> **Median:**
> Geordnet: 2000, 2100, **2200**, 2300, 50000
> Median = 2200 €
> 
> | Kennwert | Ergebnis | Interpretation |
> |----------|----------|----------------|
> | Mittelwert | 11.720 € | Durch den Großverdiener stark nach oben gezogen |
> | Median | 2.200 € | Spiegelt das „typische" Einkommen wider |
> 
> Der Median ist hier deutlich aussagekräftiger!

> [!warning] **Häufiger Fehler: Daten nicht ordnen**
> Der häufigste Fehler bei der Median-Berechnung: Die Daten werden nicht sortiert!
> 
> Bei den Rohdaten 3, 7, 2, 9, 5 ist der „mittlere" Wert 2 – aber das ist **nicht** der Median! Erst nach dem Ordnen (2, 3, 5, 7, 9) sieht man, dass der Median 5 ist.

## Wann welchen Wert verwenden?

| Situation | Empfohlener Lageparameter |
|-----------|---------------------------|
| Symmetrische Verteilung, keine Ausreißer | **Mittelwert** (nutzt alle Informationen) |
| Ausreißer vorhanden | **Median** (robust gegen Extremwerte) |
| Schiefe Verteilung (z.B. Einkommen) | **Median** (gibt das „typische" an) |
| Ordinale Daten (z.B. Schulnoten) | **Median** (Mittelwert ist streng genommen nicht sinnvoll) |
| Für Weiterberechnungen (z.B. Standardabweichung) | **Mittelwert** (mathematisch günstiger) |

> [!tip] **Faustregel für die Praxis**
> - In Nachrichten über Einkommen, Vermögen oder Immobilienpreise ist der **Median** aussagekräftiger
> - Bei „normalen" Daten ohne Extremwerte liefern Median und Mittelwert ähnliche Ergebnisse

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[08-Arithmetisches-Mittel|Arithmetisches Mittel]] – Empfindlicher für Ausreißer
- → [[10-Modalwert|Modalwert]] – Der häufigste Wert
- → [[11-Spannweite|Spannweite]] – Streuung der Daten
- → [[07-Histogramme|Histogramme]] – Verteilungsformen erkennen

> [!warning] **Prüfungsrelevant**
> - Median-Berechnung für ungerade und gerade Anzahl
> - **Wichtig:** Daten zuerst ordnen!
> - Vergleich: Wann Median, wann Mittelwert?
> - Median ist robust gegen Ausreißer

---

**Navigation:** [[08-Arithmetisches-Mittel|← Arithmetisches Mittel]] | [[10-Modalwert|Modalwert →]]
