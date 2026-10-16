---
title: "Steigungen und Neigungswinkel"
created: 2026-10-13
modified: 2026-10-13
chapter: "11"
section: "11"
status: "draft - review pending"
type: lecture
keywords:
  - Steigung
  - Neigungswinkel
  - Prozent
  - Gefälle
  - Rampe
---

# Steigungen und Neigungswinkel

> [!info] Lernziele
> - Den Zusammenhang zwischen Steigung und Winkel verstehen
> - Prozentangaben in Winkel umrechnen und umgekehrt
> - Praktische Anwendungen bei Rampen, Straßen und Dächern beherrschen
> - Die verschiedenen Angabeformen kennen

## Steigung und Tangens

Die **Steigung** einer Geraden oder Fläche ist definiert als:

$$\text{Steigung} = \frac{\text{Höhenunterschied}}{\text{Horizontale Entfernung}} = \tan(\alpha)$$

```
         ╱│
        ╱ │ Höhe h
       ╱α │
      ╱───┘
       Länge l
       
    Steigung = h/l = tan(α)
```

## Angabeformen der Steigung

### Als Dezimalzahl

$$m = 0{,}15$$

### In Prozent

$$m = 15\%$$

> [!note] Umrechnung
> $$\text{Steigung in \%} = \text{Dezimalzahl} \times 100$$
> $$\text{Dezimalzahl} = \frac{\text{Prozent}}{100}$$

### Als Verhältnis

$$m = 1:6{,}67$$ (bedeutet: 1 m Höhe auf 6,67 m Länge)

### Als Winkel

$$\alpha = \arctan(m)$$

## Umrechnungstabelle

| Prozent | Dezimal | Winkel |
|---|---|---|
| 5% | 0,05 | 2,9° |
| 10% | 0,10 | 5,7° |
| 15% | 0,15 | 8,5° |
| 20% | 0,20 | 11,3° |
| 25% | 0,25 | 14,0° |
| 50% | 0,50 | 26,6° |
| 100% | 1,00 | 45° |

> [!warning] Achtung
> 100% Steigung ist **nicht** senkrecht! Es entspricht nur einem 45°-Winkel.

## Umrechnungsformeln

### Von Prozent zu Winkel

$$\alpha = \arctan\left(\frac{p}{100}\right)$$

> [!example] Beispiel
> 12% Steigung:
> $$\alpha = \arctan(0{,}12) \approx 6{,}8°$$

### Von Winkel zu Prozent

$$p = \tan(\alpha) \times 100$$

> [!example] Beispiel
> 8° Neigung:
> $$p = \tan(8°) \times 100 = 0{,}14 \times 100 = 14\%$$

## Praktische Anwendungen

### Straßenschilder

```
   ╱╲
  ╱12%╲
 ╱────╲
```

Ein Schild „12% Steigung" bedeutet:
- Auf 100 m horizontaler Strecke gewinnt man 12 m Höhe
- Neigungswinkel: ca. 6,8°

### Rollstuhlrampen

> [!note] Vorschriften
> - Maximale Steigung für Rollstuhlrampen: **6%** (ca. 3,4°)
> - Besser: 4-5%

> [!example] Beispiel
> Höhenunterschied 80 cm. Wie lang muss die Rampe bei 6% Steigung sein?
> 
> $$l = \frac{h}{\tan(\alpha)} = \frac{0{,}8}{\tan(3{,}4°)} = \frac{0{,}8}{0{,}06} \approx 13{,}3 \text{ m}$$

### Dachneigung

Übliche Dachneigungen:
- Flachdach: 2-7° (3-12%)
- Steildach: 35-55° (70-140%)
- Normales Satteldach: ca. 30-45° (58-100%)

### Skipisten

| Kategorie | Farbe | Steigung |
|---|---|---|
| Leicht | Blau | < 25% |
| Mittel | Rot | 25-40% |
| Schwer | Schwarz | > 40% |

## Gefälle vs. Steigung

- **Steigung**: Die Straße geht bergauf
- **Gefälle**: Die Straße geht bergab

Mathematisch ist der Betrag gleich, nur das Vorzeichen unterscheidet sich.

## Berechnung der tatsächlichen Weglänge

Die **Weglänge** (entlang der Schräge) ist länger als die horizontale Entfernung:

$$s = \frac{h}{\sin(\alpha)} = \frac{l}{\cos(\alpha)}$$

> [!example] Beispiel
> Horizontale Entfernung 100 m, Steigung 15%
> 
> $\alpha = \arctan(0{,}15) = 8{,}5°$
> 
> $s = \frac{100}{\cos(8{,}5°)} = \frac{100}{0{,}989} \approx 101{,}1$ m

## Zusammenfassung

> [!abstract] Kernpunkte
> - Steigung = $\tan(\alpha) = \frac{\text{Höhe}}{\text{horizontale Länge}}$
> - Prozent zu Winkel: $\alpha = \arctan\left(\frac{p}{100}\right)$
> - Winkel zu Prozent: $p = \tan(\alpha) \times 100$
> - 100% Steigung = 45°-Winkel
> - Praktische Anwendungen: Straßen, Rampen, Dächer, Pisten

## Übungsaufgaben

1. Rechne die Steigungen in Winkel um:
   - 8%
   - 25%
   - 75%

2. Rechne die Winkel in Prozent um:
   - 5°
   - 15°
   - 30°

3. Eine Rollstuhlrampe soll einen Höhenunterschied von 45 cm überwinden. Bei maximal 6% Steigung: Wie lang muss sie sein?

4. Ein Berghang hat eine Neigung von 35°. Wie viel Höhenmeter gewinnt man auf 500 m Wegstrecke (gemessen in der Schräge)?

5. Die Zugspitzbahn überwindet auf einer Strecke von 4,5 km einen Höhenunterschied von 1950 m. Berechne die durchschnittliche Steigung in Prozent.

---

**Navigation**: [[10-Berechnung-Winkel|← Winkel]] | [[00-Pythagoras-Trigonometrie-Index|Übersicht]] | [[12-Vermessungsaufgaben|Vermessungsaufgaben →]]
