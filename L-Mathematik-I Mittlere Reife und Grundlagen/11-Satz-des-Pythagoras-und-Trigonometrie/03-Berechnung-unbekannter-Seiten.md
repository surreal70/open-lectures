---
title: "Berechnung unbekannter Seiten"
created: 2026-10-13
modified: 2026-10-13
chapter: "11"
section: "03"
status: "draft - review pending"
type: lecture
keywords:
  - Pythagoras
  - Anwendung
  - Seitenberechnung
  - Wurzel
---

# Berechnung unbekannter Seiten

> [!info] Lernziele
> - Den Satz des Pythagoras zur Berechnung von Seiten anwenden
> - Die Formel nach der gesuchten Größe umstellen
> - Systematisch vorgehen bei der Problemlösung
> - Typische Aufgabentypen beherrschen

## Systematisches Vorgehen

### Schritt-für-Schritt

```
1. Skizze anfertigen
         ↓
2. Rechtwinkliges Dreieck identifizieren
         ↓
3. Hypotenuse und Katheten benennen
         ↓
4. Bekannte Werte einsetzen
         ↓
5. Nach der Unbekannten umstellen
         ↓
6. Ausrechnen
         ↓
7. Ergebnis prüfen (Plausibilität)
```

## Hypotenuse berechnen

### Formel

$$c = \sqrt{a^2 + b^2}$$

> [!example] Beispiel
> Ein rechtwinkliges Dreieck hat die Katheten $a = 5$ cm und $b = 12$ cm.
> 
> **Gesucht**: Hypotenuse $c$
> 
> **Lösung**:
> $$c = \sqrt{5^2 + 12^2} = \sqrt{25 + 144} = \sqrt{169} = 13 \text{ cm}$$
> 
> **Prüfung**: $c = 13$ ist größer als beide Katheten ✓

## Kathete berechnen

### Formel (nach a umgestellt)

$$a = \sqrt{c^2 - b^2}$$

### Formel (nach b umgestellt)

$$b = \sqrt{c^2 - a^2}$$

> [!example] Beispiel
> Gegeben: $c = 10$ cm, $a = 6$ cm
> 
> **Gesucht**: Kathete $b$
> 
> **Lösung**:
> $$b = \sqrt{10^2 - 6^2} = \sqrt{100 - 36} = \sqrt{64} = 8 \text{ cm}$$
> 
> **Prüfung**: $6^2 + 8^2 = 36 + 64 = 100 = 10^2$ ✓

## Praktische Beispiele

### Beispiel 1: Leiter an der Wand

Eine 5 m lange Leiter steht 1,5 m von der Hauswand entfernt. Wie hoch reicht sie?

```
         │
         │● Oberkante
         │╲
    h=?  │ ╲ 5 m
         │  ╲
         │   ╲
    ─────┴────●
         1,5 m
```

**Lösung**:
$$h = \sqrt{5^2 - 1{,}5^2} = \sqrt{25 - 2{,}25} = \sqrt{22{,}75} \approx 4{,}77 \text{ m}$$

### Beispiel 2: Diagonale im Rechteck

Ein Rechteck hat die Seiten 6 cm und 8 cm. Wie lang ist die Diagonale?

```
    ┌────────────┐
    │╲           │
    │ ╲     d    │ 6
    │  ╲         │
    └───╲────────┘
           8
```

**Lösung**:
$$d = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10 \text{ cm}$$

### Beispiel 3: Entfernung zwischen zwei Punkten

Im Koordinatensystem: $A(2, 1)$ und $B(6, 4)$. Wie groß ist der Abstand?

```
    y
    ↑
  4 ┤        ● B
    │       ╱│
    │     ╱  │3
  1 ┤   ●    │
    │   A    │
    └───┬────┬──→ x
        2    6
         └4┘
```

**Lösung**:
$$d = \sqrt{(6-2)^2 + (4-1)^2} = \sqrt{16 + 9} = \sqrt{25} = 5$$

## Häufige Fehler vermeiden

> [!warning] Typische Fehler
> 
> **Fehler 1**: Hypotenuse und Kathete verwechseln
> - Die Hypotenuse ist IMMER die längste Seite
> - Sie liegt dem rechten Winkel gegenüber
> 
> **Fehler 2**: Falsches Vorzeichen unter der Wurzel
> - Bei der Kathete: $a = \sqrt{c^2 - b^2}$, nicht $\sqrt{b^2 - c^2}$
> - Der größere Wert ($c^2$) steht vorne!
> 
> **Fehler 3**: Wurzel vergessen
> - $a^2 = 64$ bedeutet $a = 8$, nicht $a = 64$!

## Sonderfälle

### Gleichschenklig-rechtwinkliges Dreieck

Bei $a = b$ (beide Katheten gleich):

$$c = \sqrt{a^2 + a^2} = \sqrt{2a^2} = a\sqrt{2}$$

> [!example] Beispiel
> $a = b = 5$ cm → $c = 5\sqrt{2} \approx 7{,}07$ cm

### Verdopplung/Halbierung

Wenn alle Seiten mit demselben Faktor multipliziert werden, bleibt das Dreieck rechtwinklig.

$(3, 4, 5)$ → $(6, 8, 10)$ → $(9, 12, 15)$ ...

## Zusammenfassung

> [!abstract] Kernpunkte
> - Hypotenuse: $c = \sqrt{a^2 + b^2}$
> - Kathete: $a = \sqrt{c^2 - b^2}$ oder $b = \sqrt{c^2 - a^2}$
> - Immer zuerst die Hypotenuse identifizieren
> - Bei der Kathete: größeres Quadrat minus kleineres Quadrat
> - Ergebnis auf Plausibilität prüfen

## Übungsaufgaben

1. Berechne die fehlende Seite:
   - $a = 9$ cm, $b = 12$ cm, $c = ?$
   - $a = 7$ cm, $c = 25$ cm, $b = ?$
   - $b = 20$ cm, $c = 29$ cm, $a = ?$

2. Die Diagonale eines Quadrats ist 10 cm lang. Wie lang ist die Seite?

3. Ein Dach hat eine Breite von 8 m und eine Höhe von 3 m. Wie lang ist die Dachschräge?

4. Zwei Punkte haben die Koordinaten $P(1, 2)$ und $Q(7, 10)$. Berechne den Abstand.

5. Eine Rutsche ist 4 m lang. Die Plattform ist 2,5 m hoch. Wie weit von der Plattform entfernt endet die Rutsche?

---

**Navigation**: [[02-Satz-des-Pythagoras|← Satz des Pythagoras]] | [[00-Pythagoras-Trigonometrie-Index|Übersicht]] | [[04-Anwendungen-Pythagoras|Anwendungen →]]
