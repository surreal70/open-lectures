---
title: Pfadregeln
chapter: "14"
section: "14.9"
type: lecture
created: 2026-10-13
modified: 2026-10-25
status: final
tags:
  - mathematik/wahrscheinlichkeit
  - pfadregeln
---

# Pfadregeln

## Einführung

> [!info] **Lernziele**
> Nach dieser Lektion können Sie:
> - Die Produktregel anwenden
> - Die Summenregel anwenden

---

## Überblick

Die Pfadregeln sind das Herzstück der Arbeit mit Baumdiagrammen. Sie verwandeln ein gezeichnetes Baumdiagramm in konkrete Wahrscheinlichkeiten. Mit nur zwei einfachen Regeln – multiplizieren entlang eines Pfades, addieren bei mehreren Pfaden – lassen sich auch komplexe Wahrscheinlichkeiten berechnen.

Diese Regeln folgen direkt aus den Grundgesetzen der Wahrscheinlichkeitsrechnung, aber das Baumdiagramm macht ihre Anwendung besonders anschaulich und übersichtlich.

---

## 1. Pfadmultiplikationsregel (Produktregel)

> [!note] **Regel**
> Die Wahrscheinlichkeit eines Pfades = **Produkt** aller Kantenwahrscheinlichkeiten entlang des Pfades.

### Anschauliche Erklärung

Jede Stufe „filtert" die Möglichkeiten. Wenn bei der 1. Stufe nur ½ der Fälle zu einem bestimmten Ergebnis führen und bei der 2. Stufe wieder nur ½, dann führen insgesamt nur ½ × ½ = ¼ aller Fälle zu diesem kombinierten Ergebnis.

> [!example] **Zweimal Kopf**
> ![[pfad-produktregel.png]]
> *<span class="fig-id">14-09-pfad-produktregel</span>: Entlang des hervorgehobenen Pfades $K \to K$ werden die Kantengewichte multipliziert: $\tfrac{1}{2} \cdot \tfrac{1}{2} = \tfrac{1}{4}$.*
> 
> Pfad Start → K → K:
> $P(K \cap K) = P(K) \cdot P(K) = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4} = 25\%$

> [!tip] **Merkregel**
> „Entlang des Pfades **mal**nehmen" – weil wir auf dem Weg von Stufe zu Stufe wandern und dabei multiplizieren.

---

## 2. Pfadadditionsregel (Summenregel)

> [!note] **Regel**
> Die Wahrscheinlichkeit eines Ereignisses = **Summe** der Wahrscheinlichkeiten aller Pfade, die zu diesem Ereignis führen.

### Anschauliche Erklärung

Wenn mehrere Pfade zum gleichen Ereignis führen, sind das verschiedene Möglichkeiten, wie das Ereignis eintreten kann. Diese Möglichkeiten schließen sich gegenseitig aus (jeder Versuch folgt genau einem Pfad), daher addieren wir ihre Wahrscheinlichkeiten.

> [!example] **Genau einmal Kopf bei zweimal Werfen**
> ![[pfad-summenregel.png]]
> *<span class="fig-id">14-09-pfad-summenregel</span>: Zwei Pfade führen zu „genau einmal Kopf" ($KZ$ und $ZK$); ihre Wahrscheinlichkeiten werden addiert.*
> 
> Das Ereignis „genau einmal Kopf" kann auf zwei Wegen eintreten:
> - Pfad K-Z: $P = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$
> - Pfad Z-K: $P = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$
> 
> Summe: $P(\text{genau 1× K}) = \frac{1}{4} + \frac{1}{4} = \frac{1}{2} = 50\%$

> [!tip] **Merkregel**
> „Verschiedene Pfade **plus**rechnen" – weil mehrere Wege zum Ziel führen und wir alle zählen.

---

## Zusammenfassung der beiden Regeln

| Regel | Operation | Anwendung | Gedächtnisstütze |
|-------|-----------|-----------|------------------|
| Produktregel | Multiplizieren | Entlang **eines** Pfades | „UND" → mal |
| Summenregel | Addieren | **Mehrere** günstige Pfade | „ODER" → plus |

### Die Schlüsselwörter

- **UND** (beide Ereignisse müssen eintreten) → **Multiplizieren**
  - „Erst Kopf UND dann Kopf" = K × K
- **ODER** (eines von mehreren Ereignissen) → **Addieren**
  - „Erst K dann Z ODER erst Z dann K" = KZ + ZK

---

## Vollständiges Beispiel

> [!example] **Dreimal Münze werfen: Mindestens zweimal Kopf**
> 
> **Schritt 1:** Günstige Pfade identifizieren
> - KKK (3× Kopf) ✓
> - KKZ (2× Kopf) ✓
> - KZK (2× Kopf) ✓
> - ZKK (2× Kopf) ✓
> 
> **Schritt 2:** Pfadwahrscheinlichkeiten berechnen (Produktregel)
> - P(KKK) = ½ × ½ × ½ = ⅛
> - P(KKZ) = ½ × ½ × ½ = ⅛
> - P(KZK) = ½ × ½ × ½ = ⅛
> - P(ZKK) = ½ × ½ × ½ = ⅛
> 
> **Schritt 3:** Addieren (Summenregel)
> $P(\text{mind. 2× K}) = \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} = \frac{4}{8} = \frac{1}{2} = 50\%$

---

## Anwendung bei unterschiedlichen Wahrscheinlichkeiten

Die Pfadregeln gelten auch, wenn die Wahrscheinlichkeiten nicht überall gleich sind – etwa beim Ziehen ohne Zurücklegen:

> [!example] **Urne: 3 rote, 2 blaue Kugeln – beide rot (ohne Zurücklegen)**
> 
> Pfad R → R:
> - 1. Zug rot: $P = \frac{3}{5}$
> - 2. Zug rot (nach 1× rot): $P = \frac{2}{4}$ (nur noch 2 rote von 4)
> 
> $P(\text{beide rot}) = \frac{3}{5} \cdot \frac{2}{4} = \frac{6}{20} = \frac{3}{10} = 30\%$

> [!warning] **Häufiger Fehler**
> Bei „ohne Zurücklegen" nicht vergessen: Die Wahrscheinlichkeiten ändern sich von Stufe zu Stufe! Im obigen Beispiel darf man **nicht** $\frac{3}{5} \cdot \frac{3}{5}$ rechnen.

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[08-Baumdiagramme|Baumdiagramme]] – Die visuelle Grundlage für die Pfadregeln
- → [[10-Unabhaengige-Ereignisse|Unabhängige Ereignisse]] – Warum die Produktregel funktioniert
- → [[07-Gegenereignisse|Gegenereignisse]] – Alternative bei „mindestens einmal"
- → [[11-Kombinatorik|Kombinatorik]] – Zählen der günstigen Pfade bei vielen Stufen

---

**Navigation:** [[08-Baumdiagramme|← Baumdiagramme]] | [[10-Unabhaengige-Ereignisse|Unabhängigkeit →]]
