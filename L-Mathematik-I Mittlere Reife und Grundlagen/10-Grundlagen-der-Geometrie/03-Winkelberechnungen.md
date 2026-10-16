---
title: "Winkelberechnungen"
created: 2026-10-13
modified: 2026-10-13
chapter: "10"
section: "03"
status: "draft - review pending"
type: lecture
keywords:
  - Scheitelwinkel
  - Nebenwinkel
  - Stufenwinkel
  - Wechselwinkel
  - Parallelenschnitt
---

# Winkelberechnungen

> [!info] Lernziele
> - Winkelbeziehungen bei sich schneidenden Geraden kennen
> - Stufenwinkel und Wechselwinkel am Parallelenschnitt anwenden
> - Unbekannte Winkel systematisch berechnen
> - Die Winkelsätze in Aufgaben anwenden

## Winkel an sich schneidenden Geraden

Wenn sich zwei Geraden schneiden, entstehen vier Winkel.

```
           g
          ╱
    α₂   ╱   α₁
        ╱
───────●───────── h
      ╱
 α₃  ╱  α₄
    ╱
```

### Nebenwinkel

**Nebenwinkel** liegen auf derselben Seite einer Geraden nebeneinander.

$$\alpha + \beta = 180°$$

> [!example] Beispiel
> $\alpha_1 + \alpha_2 = 180°$
> 
> Wenn $\alpha_1 = 70°$, dann $\alpha_2 = 110°$.

### Scheitelwinkel

**Scheitelwinkel** liegen sich am Schnittpunkt gegenüber.

$$\alpha_1 = \alpha_3 \quad \text{und} \quad \alpha_2 = \alpha_4$$

Scheitelwinkel sind **gleich groß**.

> [!example] Beispiel
> Wenn $\alpha_1 = 70°$, dann auch $\alpha_3 = 70°$.

## Winkel am Parallelenschnitt

Wenn eine Gerade $t$ (Transversale) zwei parallele Geraden $g \parallel h$ schneidet, entstehen besondere Winkelbeziehungen.

```
              t
             ╱
      α₁    ╱  α₂
    ─────g─●────────
          ╱
    α₃   ╱  α₄
        ╱
   β₁  ╱  β₂
─────h●────────
     ╱
β₃  ╱  β₄
   ╱
```

### Stufenwinkel (F-Winkel)

**Stufenwinkel** liegen auf derselben Seite der Transversalen, einer bei $g$, einer bei $h$.

Bei parallelen Geraden: **Stufenwinkel sind gleich groß**.

$$\alpha_1 = \beta_1 \quad \text{und} \quad \alpha_2 = \beta_2$$

> [!tip] Merkregel
> Die Form eines „F" hilft beim Erkennen:
> ```
>     F
> ────┼────
>     │
>     ├────
>     │
> ```

### Wechselwinkel (Z-Winkel)

**Wechselwinkel** liegen auf verschiedenen Seiten der Transversalen, einer bei $g$, einer bei $h$.

Bei parallelen Geraden: **Wechselwinkel sind gleich groß**.

$$\alpha_1 = \beta_3 \quad \text{und} \quad \alpha_3 = \beta_1$$

> [!tip] Merkregel
> Die Form eines „Z" hilft beim Erkennen:
> ```
>     ╱────
>    ╱
>   ╱
>  ╱────
> ```

### Übersicht der Winkelbeziehungen

| Winkelart | Lage | Beziehung |
|---|---|---|
| Nebenwinkel | nebeneinander | $\alpha + \beta = 180°$ |
| Scheitelwinkel | gegenüber | $\alpha = \beta$ |
| Stufenwinkel | gleiche Seite, parallel | $\alpha = \beta$ |
| Wechselwinkel | verschiedene Seiten, parallel | $\alpha = \beta$ |

## Anwendungsbeispiele

### Beispiel 1: Scheitelwinkel

Gegeben: $\alpha = 65°$

```
         ╱
    ?   ╱  65°
       ╱
──────●────────
     ╱
 ?  ╱  ?
   ╱
```

**Lösung**:
- Scheitelwinkel: $65°$
- Nebenwinkel: $180° - 65° = 115°$

Alle Winkel: $65°$, $115°$, $65°$, $115°$

### Beispiel 2: Parallelenschnitt

Gegeben: $g \parallel h$, $\alpha = 72°$

```
              t
             ╱
      72°   ╱  ?
    ─────g─●────────
          ╱
    ?    ╱  ?
        ╱
```

**Lösung**:
- Nebenwinkel zu 72°: $180° - 72° = 108°$
- Scheitelwinkel zu 72°: $72°$
- Stufenwinkel bei $h$: $72°$ und $108°$

### Beispiel 3: Komplexe Aufgabe

Gegeben: $g \parallel h$, $\alpha = 3x + 10°$, $\beta = 5x - 20°$ sind Wechselwinkel.

**Lösung**:
Wechselwinkel sind gleich groß:
$$3x + 10 = 5x - 20$$
$$30 = 2x$$
$$x = 15°$$

Also: $\alpha = \beta = 3 \cdot 15 + 10 = 55°$

## Tipps zum Berechnen

> [!tip] Systematisches Vorgehen
> 1. Zeichnung anfertigen oder ergänzen
> 2. Bekannte Winkel eintragen
> 3. Art der Winkelbeziehung identifizieren
> 4. Entsprechende Regel anwenden
> 5. Ergebnis überprüfen

## Zusammenfassung

> [!abstract] Kernpunkte
> - Nebenwinkel: ergänzen sich zu 180°
> - Scheitelwinkel: sind gleich groß
> - Bei parallelen Geraden gilt zusätzlich:
>   - Stufenwinkel (F-Winkel): gleich groß
>   - Wechselwinkel (Z-Winkel): gleich groß
> - Diese Regeln ermöglichen die Berechnung unbekannter Winkel

## Übungsaufgaben

1. Zwei Geraden schneiden sich. Ein Winkel beträgt 47°. Berechne alle anderen Winkel.

2. Bei einem Parallelenschnitt ist ein Stufenwinkel 118°. Bestimme alle acht Winkel.

3. Zwei Wechselwinkel sind $(2x + 30)°$ und $(4x - 10)°$. Berechne $x$ und die Winkelgröße.

4. Erkläre, warum Stufenwinkel bei nicht-parallelen Geraden nicht gleich groß sein müssen.

5. In einer Figur sind $\alpha$ und $\beta$ Nebenwinkel mit $\alpha = 3\beta$. Berechne beide Winkel.

---

**Navigation**: [[02-Winkel-und-Winkelarten|← Winkelarten]] | [[00-Geometrie-Index|Übersicht]] | [[04-Dreiecke|Dreiecke →]]
