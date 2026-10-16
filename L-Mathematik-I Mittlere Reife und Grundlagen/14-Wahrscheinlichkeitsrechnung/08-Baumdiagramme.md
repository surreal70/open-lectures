---
title: Baumdiagramme
chapter: "14"
section: "14.8"
type: lecture
created: 2026-10-13
modified: 2025-01-20
status: draft - review pending
tags:
  - mathematik/wahrscheinlichkeit
  - baumdiagramm
---

# Baumdiagramme

## Einführung

> [!info] **Lernziele**
> Nach dieser Lektion können Sie:
> - Baumdiagramme für mehrstufige Experimente erstellen
> - Pfade ablesen und beschreiben

---

## Überblick

Bei mehrstufigen Zufallsexperimenten kann die Anzahl der möglichen Ergebnisse schnell unübersichtlich werden. Baumdiagramme sind ein visuelles Werkzeug, das Ordnung in diese Komplexität bringt. Sie zeigen alle möglichen Verläufe eines Experiments systematisch auf und machen die Berechnung von Wahrscheinlichkeiten anschaulich.

Das Baumdiagramm wurde im 19. Jahrhundert als Darstellungsform populär und ist heute das Standardwerkzeug für mehrstufige Wahrscheinlichkeitsprobleme. Sein großer Vorteil: Es garantiert, dass wir keine Möglichkeit übersehen und keine doppelt zählen.

---

## Aufbau

Ein Baumdiagramm besteht aus Knoten (Kreise) und Kanten (Linien), die die Knoten verbinden:

```
        Start
       /     \
     K(½)    Z(½)     ← 1. Stufe
    /  \    /  \
  K(½) Z(½) K(½) Z(½)  ← 2. Stufe
  
  KK   KZ   ZK   ZZ   ← Ergebnisse
```

### Leserichtung

- Von oben nach unten (oder von links nach rechts)
- Jede Ebene entspricht einer Stufe des Experiments
- Jeder vollständige Pfad vom Start bis zum Ende entspricht einem Ergebnis

---

## Elemente

| Element | Bedeutung | Visualisierung |
|---------|-----------|----------------|
| Startknoten | Ausgangspunkt, vor dem 1. Versuch | Oberster Punkt |
| Knoten | Zustand nach einer Stufe | Verzweigungspunkte |
| Kante | Übergang zum nächsten Zustand | Linien zwischen Knoten |
| Pfad | Weg vom Start zum Endergebnis | Eine Abfolge von Kanten |
| Kantengewicht | Wahrscheinlichkeit des Übergangs | Zahl an der Kante |

---

## Beispiel: Zweimal Münze werfen

```
              Start
             /     \
          K(½)     Z(½)
          /  \     /  \
       K(½) Z(½) K(½) Z(½)
       
Pfade und Ergebnisse:
- Start → K → K = KK (Kopf-Kopf)
- Start → K → Z = KZ (Kopf-Zahl)
- Start → Z → K = ZK (Zahl-Kopf)
- Start → Z → Z = ZZ (Zahl-Zahl)
```

### Systematisches Ablesen

Um kein Ergebnis zu vergessen, liest man systematisch:
1. Vom Startknoten aus die erste Verzweigung (hier: K)
2. Von dort alle weiteren Verzweigungen bis zum Ende
3. Zurück zur nächsten Verzweigung auf der ersten Stufe (hier: Z)
4. Wieder alle weiteren Verzweigungen ablesen

> [!tip] **Kontrollmöglichkeit**
> Bei $n$ Stufen mit je $k$ Möglichkeiten muss das Baumdiagramm genau $k^n$ Endpunkte haben.
> - Zweimal Münze: $2^2 = 4$ Endpunkte ✓
> - Dreimal würfeln: $6^3 = 216$ Endpunkte (zu viele zum Zeichnen!)

---

## Baumdiagramm erstellen – Schritt für Schritt

1. **Startknoten** zeichnen
2. **1. Stufe:** Für jedes mögliche Ergebnis eine Kante nach unten, mit Wahrscheinlichkeit beschriften
3. **2. Stufe:** Von jedem Knoten wieder für jedes mögliche Ergebnis eine Kante
4. **Wiederholen** für alle weiteren Stufen
5. **Ergebnisse** am Ende jedes Pfades notieren

> [!example] **Beispiel: Urne mit 3 roten und 2 blauen Kugeln, 2× ziehen ohne Zurücklegen**
> ```
>               Start
>              /     \
>           R(3/5)  B(2/5)
>           /  \     /  \
>        R(2/4) B(2/4) R(3/4) B(1/4)
>        
> Beachte: Die Wahrscheinlichkeiten ändern sich!
> Nach Ziehen einer roten Kugel:
> - Noch 2 rote und 2 blaue von 4 Kugeln
> ```

---

## Wann Baumdiagramme besonders hilfreich sind

- **Mehrstufige Experimente:** Mehrere Würfe, Züge, Versuche nacheinander
- **Abhängige Wahrscheinlichkeiten:** Wenn sich die Chancen von Stufe zu Stufe ändern
- **Komplexe Ereignisse:** „Genau einmal Kopf", „Mindestens eine rote Kugel"
- **Übersicht behalten:** Bei mehr als 2-3 Stufen unverzichtbar

> [!warning] **Häufiger Fehler**
> Bei „Ziehen ohne Zurücklegen" ändern sich die Wahrscheinlichkeiten von Stufe zu Stufe! Vergessen Sie nicht, die Kantengewichte entsprechend anzupassen.
> 
> **Falsch:** Immer $\frac{3}{5}$ für „rot" eintragen
> **Richtig:** Nach Ziehen einer roten Kugel nur noch $\frac{2}{4}$ für „rot"

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[02-Ergebnismengen|Ergebnismengen]] – Das Baumdiagramm zeigt alle Elemente von Ω
- → [[09-Pfadregeln|Pfadregeln]] – Wie man aus dem Baumdiagramm Wahrscheinlichkeiten berechnet
- → [[10-Unabhaengige-Ereignisse|Unabhängige Ereignisse]] – Wann die Kantengewichte konstant bleiben
- → [[11-Kombinatorik|Kombinatorik]] – Alternative zum Zeichnen bei sehr großen Bäumen

---

**Navigation:** [[07-Gegenereignisse|← Gegenereignisse]] | [[09-Pfadregeln|Pfadregeln →]]
