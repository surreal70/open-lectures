---
title: Arithmetisches Mittel
chapter: "13"
section: "13.8"
type: lecture
created: 2026-10-13
modified: 2025-01-17
status: draft - review pending
tags:
  - mathematik/statistik
  - mittelwert
  - lageparameter
---

# Arithmetisches Mittel

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Das arithmetische Mittel berechnen
> - Vor- und Nachteile kennen
> - Den Durchschnitt interpretieren

Das arithmetische Mittel – umgangssprachlich „Durchschnitt" genannt – ist der bekannteste und am häufigsten verwendete statistische Kennwert. Es fasst eine Datenmenge in einer einzigen Zahl zusammen und gibt an, wo das „Zentrum" der Daten liegt.

### Historischer Hintergrund

Das Konzept des Mittelwerts ist uralt. Schon im antiken Babylon wurden Mittelwerte für astronomische Berechnungen verwendet. Der Begriff „arithmetisches Mittel" geht auf die Pythagoreer zurück, die verschiedene Arten von Mittelwerten untersuchten (arithmetisches, geometrisches, harmonisches Mittel). Im 17. Jahrhundert wurde der Durchschnitt zu einem zentralen Werkzeug der Statistik, als Astronomen wie Tycho Brahe mehrere Messungen mittelten, um Messfehler auszugleichen.

> [!tip] **Alltagsrelevanz**
> Das arithmetische Mittel begegnet uns ständig: Notendurchschnitt, Durchschnittstemperatur, Durchschnittseinkommen, Durchschnittsgeschwindigkeit. Die Fähigkeit, Durchschnitte zu berechnen und kritisch zu interpretieren, ist eine wichtige Alltagskompetenz.

## Definition

> [!note] Formel
> $$\bar{x} = \frac{x_1 + x_2 + ... + x_n}{n} = \frac{\sum_{i=1}^{n} x_i}{n}$$
> 
> **Arithmetisches Mittel** = Summe aller Werte geteilt durch Anzahl der Werte

Das Symbol $\bar{x}$ (sprich: „x-quer") bezeichnet das arithmetische Mittel einer Stichprobe. In der Formel steht $\sum$ (griechisches Sigma) für „Summe".

### Anschauliche Interpretation

Das arithmetische Mittel kann als **Schwerpunkt** oder **Gleichgewichtspunkt** der Daten verstanden werden. Stell dir eine Wippe vor, auf der die Datenwerte als Gewichte platziert sind – der Punkt, an dem die Wippe im Gleichgewicht ist, entspricht dem arithmetischen Mittel.

## Berechnung

> [!example] Beispiel: Klassenarbeitsnoten
> Noten: 2, 3, 1, 4, 2, 3, 2, 5, 3, 2
> 
> **Schritt 1:** Summe berechnen
> $$2 + 3 + 1 + 4 + 2 + 3 + 2 + 5 + 3 + 2 = 27$$
> 
> **Schritt 2:** Durch Anzahl teilen
> $$\bar{x} = \frac{27}{10} = 2{,}7$$
> 
> Der Notendurchschnitt beträgt 2,7.

## Mit Häufigkeitstabelle

Wenn Werte mehrfach vorkommen, ist die Berechnung mit Häufigkeiten effizienter:

> [!note] Gewichtete Formel
> $$\bar{x} = \frac{\sum (x_i \cdot H_i)}{n}$$
> 
> Dabei ist $H_i$ die absolute Häufigkeit des Wertes $x_i$.

> [!example] Beispiel
> | Note $x$ | Häufigkeit $H$ | $x \cdot H$ |
> |---------|---------------:|------------:|
> | 1 | 2 | 2 |
> | 2 | 5 | 10 |
> | 3 | 8 | 24 |
> | 4 | 3 | 12 |
> | 5 | 2 | 10 |
> | **Σ** | **20** | **58** |
> 
> $$\bar{x} = \frac{58}{20} = 2{,}9$$

Der Vorteil dieser Methode: Du musst nicht jeden einzelnen Wert aufschreiben, sondern arbeitest direkt mit der Häufigkeitstabelle.

## Vor- und Nachteile

| Vorteile | Nachteile |
|----------|-----------|
| Berücksichtigt alle Werte | Anfällig für Ausreißer |
| Leicht zu berechnen | Kann unrealistische Werte ergeben |
| Gut für weitere Berechnungen | Nicht für ordinale Daten geeignet |
| Eindeutig definiert | Nur für metrische Daten sinnvoll |

> [!warning] **Häufiger Fehler: Ausreißer ignorieren**
> Das arithmetische Mittel reagiert empfindlich auf extreme Werte (Ausreißer).
> 
> **Beispiel: Einkommen in einer Gruppe**
> Einkommen: 2000, 2200, 2100, 2300, **50000** €
> 
> $$\bar{x} = \frac{58600}{5} = 11720 \text{ €}$$
> 
> Das Mittel von 11.720 € ist **nicht repräsentativ** – vier von fünf Personen verdienen deutlich weniger! Der eine Großverdiener „zieht" den Durchschnitt nach oben.

> [!tip] **Wann ist der Durchschnitt aussagekräftig?**
> - Bei symmetrischen Verteilungen ohne Ausreißer
> - Wenn alle Werte „in einer Liga spielen"
> - Wenn du mit dem Mittelwert weiterrechnen willst
> 
> Bei schiefen Verteilungen oder Ausreißern ist der [[09-Median|Median]] oft besser geeignet!

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[09-Median|Median]] – Robustere Alternative bei Ausreißern
- → [[10-Modalwert|Modalwert]] – Der häufigste Wert
- → [[12-Standardabweichung|Standardabweichung]] – Streuung um den Mittelwert
- → [[04-Absolute-und-relative-Haeufigkeiten|Häufigkeiten]] – Für die gewichtete Berechnung

> [!warning] **Prüfungsrelevant**
> - Formel für das arithmetische Mittel (mit und ohne Häufigkeiten)
> - Berechnung durchführen können
> - Anfälligkeit für Ausreißer kennen und erklären

---

**Navigation:** [[07-Histogramme|← Histogramme]] | [[09-Median|Median →]]
