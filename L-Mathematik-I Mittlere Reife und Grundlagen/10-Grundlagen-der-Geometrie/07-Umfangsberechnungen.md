---
title: "Umfangsberechnungen"
created: 2026-10-13
modified: 2026-10-25
chapter: "10"
section: "07"
status: final
type: lecture
keywords:
  - Umfang
  - Dreieck
  - Viereck
  - Kreis
  - zusammengesetzte Figuren
---

# Umfangsberechnungen

> [!info] Lernziele
> - Umfänge von Dreiecken, Vierecken und Kreisen berechnen
> - Umfänge zusammengesetzter Figuren bestimmen
> - Formeln korrekt anwenden
> - Praktische Aufgaben lösen

---

## Einführung

Der Umfang ist ein grundlegendes Maß in der Geometrie und im praktischen Leben unverzichtbar. Immer wenn wir etwas „umranden", „einzäunen" oder „einfassen" wollen, benötigen wir den Umfang.

## Der Begriff Umfang

Der **Umfang** einer Figur ist die Gesamtlänge ihrer Begrenzungslinie. Stellt euch vor, eine Ameise läuft einmal um die Figur herum – die Strecke, die sie zurücklegt, ist der Umfang.

> [!tip] **Praktische Bedeutung**
> - Länge eines **Zauns** um ein Grundstück
> - Länge einer **Bordsteinkante** um einen Parkplatz
> - Material für den **Rahmen** eines Bildes
> - Länge des **Gummibands** um ein Kartenspiel
> - **Stoffmenge** für den Saum eines Kleidungsstücks

> [!warning] **Häufiger Fehler: Umfang vs. Fläche**
> Umfang und Fläche sind grundverschiedene Größen! Der Umfang ist eine **Länge** (in cm, m), die Fläche ein **Flächeninhalt** (in cm², m²). Ein großer Umfang bedeutet nicht automatisch eine große Fläche – ein langes, schmales Rechteck hat viel Umfang, aber wenig Fläche.

---

## Umfang von Dreiecken

### Allgemeines Dreieck

$$U = a + b + c$$

> [!example] Beispiel
> $a = 5$ cm, $b = 7$ cm, $c = 6$ cm
> 
> $U = 5 + 7 + 6 = 18$ cm

### Gleichseitiges Dreieck

$$U = 3a$$

### Gleichschenkliges Dreieck

Mit Basis $c$ und Schenkeln $a = b$:

$$U = 2a + c$$

## Umfang von Vierecken

### Allgemeines Viereck

$$U = a + b + c + d$$

### Rechteck

Mit Länge $l$ und Breite $b$:

$$U = 2l + 2b = 2(l + b)$$

> [!example] Beispiel
> Rechteck mit $l = 8$ cm, $b = 5$ cm
> 
> $U = 2(8 + 5) = 2 \cdot 13 = 26$ cm

### Quadrat

$$U = 4a$$

> [!example] Beispiel
> Quadrat mit $a = 6$ cm
> 
> $U = 4 \cdot 6 = 24$ cm

### Parallelogramm

$$U = 2(a + b)$$

### Raute

$$U = 4a$$

### Trapez

$$U = a + b + c + d$$

(Alle vier Seiten addieren)

## Umfang des Kreises

$$U = 2\pi r = \pi d$$

> [!example] Beispiel
> Kreis mit $r = 4$ cm
> 
> $U = 2\pi \cdot 4 = 8\pi \approx 25{,}13$ cm

## Zusammengesetzte Figuren

Bei zusammengesetzten Figuren müssen nur die **äußeren Begrenzungslinien** berücksichtigt werden.

### Beispiel 1: Rechteck mit Halbkreis

![[umfang-rechteck-halbkreis.png]]
*<span class="fig-id">10-07-umfang-rechteck-halbkreis</span>: Zusammengesetzte Figur aus Rechteck ($10 \times 6$ cm) und angesetztem Halbkreis ($d = 6$ cm).*

Ein Rechteck ($l = 10$ cm, $b = 6$ cm) mit einem angesetzten Halbkreis (Durchmesser = 6 cm).

**Umfang**:
- Obere Seite: $10$ cm
- Beide senkrechte Seiten: $2 \times 6 = 12$ cm
- Unterer Teil: $(10 - 6) = 4$ cm gerade + Halbkreis
- Halbkreis: $\frac{1}{2} \cdot \pi \cdot 6 = 3\pi$ cm

$$U = 10 + 12 + 4 + 3\pi = 26 + 3\pi \approx 35{,}42 \text{ cm}$$

### Beispiel 2: L-förmige Figur

![[umfang-l-figur.png]]
*<span class="fig-id">10-07-umfang-l-figur</span>: L-förmige Figur mit äußeren Maßen $12 \times 8$ cm und einem Ausschnitt von $6 \times 4$ cm.*

Äußere Maße: $12 \times 8$ cm, Ausschnitt: $6 \times 4$ cm

**Umfang**: $12 + 8 + 6 + 4 + 6 + 4 = 40$ cm

## Formelübersicht

| Figur | Umfangsformel |
|---|---|
| Dreieck | $U = a + b + c$ |
| Gleichseitiges Dreieck | $U = 3a$ |
| Rechteck | $U = 2(l + b)$ |
| Quadrat | $U = 4a$ |
| Parallelogramm | $U = 2(a + b)$ |
| Raute | $U = 4a$ |
| Kreis | $U = 2\pi r$ |
| Halbkreis | $U = \pi r + 2r$ |

## Rückwärtsrechnen

### Seitenlänge aus Umfang

> [!example] Beispiel: Quadrat
> Ein Quadrat hat den Umfang 36 cm. Wie lang ist eine Seite?
> 
> $$a = \frac{U}{4} = \frac{36}{4} = 9 \text{ cm}$$

> [!example] Beispiel: Rechteck
> Ein Rechteck hat den Umfang 28 cm und die Länge 8 cm. Wie breit ist es?
> 
> $28 = 2(8 + b)$
> $14 = 8 + b$
> $b = 6$ cm

## Zusammenfassung

> [!abstract] Kernpunkte
> - Umfang = Summe aller Randlängen
> - Bei regelmäßigen Figuren: vereinfachte Formeln
> - Bei zusammengesetzten Figuren: nur äußere Begrenzung zählt
> - Kreisumfang enthält immer $\pi$
> - Formeln lassen sich nach gesuchten Größen umstellen

## Zusammenhänge

- → [[08-Flaechenberechnungen|Flächenberechnungen]] – Umfang und Fläche sind verschiedene Konzepte
- → [[06-Kreise|Kreise]] – Der Kreisumfang führt zur Kreiszahl π
- → [[04-Dreiecke|Dreiecke]] und [[05-Vierecke|Vierecke]] – Die Figuren, deren Umfang wir berechnen
- → [[11-Aehnlichkeit|Ähnlichkeit]] – Bei Streckfaktor $k$ ändert sich der Umfang um Faktor $k$

## Übungsaufgaben

1. Berechne den Umfang:
   - Dreieck: $a = 4$ cm, $b = 6$ cm, $c = 5$ cm
   - Rechteck: $l = 12$ cm, $b = 7$ cm
   - Kreis: $r = 3{,}5$ cm

2. Bestimme die fehlende Seite:
   - Quadrat mit $U = 52$ cm
   - Rechteck mit $U = 40$ cm und $l = 12$ cm

3. Ein Fußballfeld ist 100 m lang und 70 m breit. Wie lang ist die Umrandung?

4. Berechne den Umfang der zusammengesetzten Figur: Halbkreis auf einem Quadrat mit Seitenlänge 8 cm.

5. Ein Gartengrundstück hat die Form eines Rechtecks mit aufgesetztem Dreieck. Rechteck: $20 \times 15$ m, Dreieck: Basis 15 m, Schenkel je 10 m. Wie viel Meter Zaun werden benötigt?

---

**Navigation**: [[06-Kreise|← Kreise]] | [[00-Geometrie-Index|Übersicht]] | [[08-Flaechenberechnungen|Flächenberechnungen →]]
