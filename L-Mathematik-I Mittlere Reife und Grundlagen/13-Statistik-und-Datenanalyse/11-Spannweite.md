---
title: Spannweite
chapter: "13"
section: "13.11"
type: lecture
created: 2026-10-13
modified: 2026-10-25
status: final
tags:
  - mathematik/statistik
  - spannweite
  - streuung
---

# Spannweite

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Die Spannweite berechnen
> - Die Streuung von Daten einschätzen
> - Vor- und Nachteile der Spannweite kennen

Nachdem wir die **Lageparameter** (Mittelwert, Median, Modalwert) kennengelernt haben, wenden wir uns nun den **Streuungsmaßen** zu. Diese beschreiben, wie stark die einzelnen Werte um das Zentrum der Verteilung schwanken.

Die **Spannweite** ist das einfachste Streuungsmaß: Sie gibt den Abstand zwischen dem größten und dem kleinsten Wert an – also den Bereich, in dem sich alle Daten befinden.

### Warum Streuung wichtig ist

> [!tip] **Anschauliches Beispiel**
> Zwei Klassen schreiben dieselbe Arbeit und erreichen beide einen Durchschnitt von 3,0.
> 
> **Klasse A:** Noten 1, 2, 3, 4, 5 (Spannweite = 4)
> **Klasse B:** Noten 2, 3, 3, 3, 4 (Spannweite = 2)
> 
> Der Mittelwert allein verbirgt, dass in Klasse A die Leistungen viel stärker auseinandergehen. Die Spannweite zeigt diesen Unterschied auf einen Blick.

## Definition

> [!note] Formel
> $$R = x_{max} - x_{min}$$
> 
> **Spannweite** = größter Wert − kleinster Wert

Das Symbol $R$ kommt vom englischen *range* (Bereich, Reichweite). Die Spannweite hat dieselbe Einheit wie die Daten selbst (z.B. Grad Celsius bei Temperaturen, Euro bei Preisen).

## Beispiel

> [!example] Temperaturen einer Woche
> **Tageshöchstwerte:** 18, 22, 25, 19, 28, 21, 24 °C
> 
> **Schritt 1:** Größten und kleinsten Wert finden
> - $x_{max} = 28$ °C
> - $x_{min} = 18$ °C
> 
> **Schritt 2:** Differenz bilden
> $$R = 28 - 18 = 10 \text{ °C}$$
> 
> Die Spannweite beträgt 10 °C – die Temperaturen schwankten also um maximal 10 Grad.

![[spannweite.png]]
*<span class="fig-id">13-11-spannweite</span>: Die Tageshöchstwerte auf dem Zahlenstrahl; die Spannweite $R$ ist der Abstand zwischen kleinstem (18 °C) und größtem Wert (28 °C).*

## Interpretation

Die Spannweite gibt einen schnellen Überblick über die Streuung:

- **Große Spannweite** → Die Werte sind weit gestreut, es gibt große Unterschiede
- **Kleine Spannweite** → Die Werte liegen eng beieinander, die Daten sind homogen

> [!example] **Vergleich zweier Datensätze**
> 
> **Datensatz A:** Noten 2, 3, 3, 3, 4 → Spannweite = 4 − 2 = 2
> **Datensatz B:** Noten 1, 1, 3, 5, 5 → Spannweite = 5 − 1 = 4
> 
> Obwohl beide Datensätze den Median 3 haben, ist die Streuung in Datensatz B doppelt so groß.

## Vor- und Nachteile

| Vorteile | Nachteile |
|----------|-----------|
| Sehr einfach zu berechnen | Berücksichtigt nur zwei Werte |
| Schneller Überblick | Ignoriert die Verteilung der übrigen Werte |
| Leicht verständlich | **Sehr anfällig für Ausreißer** |
| Guter erster Eindruck | Sagt nichts über die „typische" Streuung |

> [!warning] **Häufiger Fehler: Ausreißer-Problem**
> Die Spannweite reagiert extrem empfindlich auf Ausreißer – ein einziger Extremwert kann sie dramatisch verändern:
> 
> **Daten A:** 10, 11, 12, 13, 14 → R = 14 − 10 = **4**
> **Daten B:** 10, 11, 12, 13, 50 → R = 50 − 10 = **40**
> 
> Ein einziger Ausreißer (50) verzehnfacht die Spannweite! Die Spannweite von 40 suggeriert eine große Streuung, obwohl 4 von 5 Werten eng beieinander liegen.

> [!tip] **Praxis-Tipp**
> Wenn du die Spannweite berechnest und sie auffällig groß erscheint, prüfe die Daten auf Ausreißer! In solchen Fällen ist die [[12-Standardabweichung|Standardabweichung]] ein besseres Streuungsmaß.

## Anwendung im Alltag

Die Spannweite wird in vielen Bereichen verwendet:

- **Wetter:** „Die Temperaturen schwankten zwischen 5 und 25 Grad" (Spannweite: 20°)
- **Sport:** Punktebereich bei einer Wertung
- **Qualitätskontrolle:** Toleranzbereich von Produkten
- **Finanzen:** Kursschwankungen einer Aktie (Tageshoch minus Tagestief)

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[08-Arithmetisches-Mittel|Arithmetisches Mittel]] – Lageparameter
- → [[09-Median|Median]] – Robuster Lageparameter
- → [[12-Standardabweichung|Standardabweichung]] – Differenzierteres Streuungsmaß
- → [[13-Interpretation|Interpretation]] – Statistische Kennwerte deuten

> [!warning] **Prüfungsrelevant**
> - Formel: $R = x_{max} - x_{min}$
> - Interpretation: große vs. kleine Spannweite
> - Hauptnachteil: Anfälligkeit für Ausreißer

---

**Navigation:** [[10-Modalwert|← Modalwert]] | [[12-Standardabweichung|Standardabweichung →]]
