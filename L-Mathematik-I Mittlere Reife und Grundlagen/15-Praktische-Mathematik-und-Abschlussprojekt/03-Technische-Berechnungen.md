---
title: Technische Berechnungen
chapter: "15"
section: "15.3"
type: lecture
created: 2026-10-13
modified: 2026-10-25
status: final
tags:
  - mathematik/anwendung
  - technik
---

# Technische Berechnungen

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Technische Größen berechnen
> - Formeln aus der Physik anwenden

Technische Berechnungen verbinden Mathematik mit der physischen Welt. Ob Handwerker, Ingenieur oder Techniker – wer mit Technik arbeitet, braucht mathematische Werkzeuge. Die Formeln mögen abstrakt erscheinen, doch sie beschreiben sehr konkrete Phänomene: wie schnell ein Auto fährt, wie schwer ein Metallblock ist oder wie ein Hebel funktioniert.

### Mathematik im technischen Beruf

In technischen Berufen begegnen uns ständig Berechnungen:

| Beruf | Typische Berechnungen |
|-------|----------------------|
| Elektriker | Spannung, Stromstärke, Widerstand (Ohmsches Gesetz) |
| Mechaniker | Drehmoment, Übersetzungen, Kräfte |
| Bauarbeiter | Statik, Lasten, Materialmengen |
| Tischler | Maße, Winkel, Materialverschnitt |
| Kfz-Mechatroniker | Verdichtung, Hubraum, Kraftstoffverbrauch |

---

## Geschwindigkeit, Weg, Zeit

> [!note] Formeln
> $$v = \frac{s}{t} \quad s = v \cdot t \quad t = \frac{s}{v}$$

Diese drei Formeln sind eigentlich nur eine einzige Formel, die nach verschiedenen Größen umgestellt wurde. Das Verständnis dieses Zusammenhangs ist wichtiger als das Auswendiglernen:

- **v** (velocity) = Geschwindigkeit – wie schnell?
- **s** (Strecke) = Weg – wie weit?
- **t** (time) = Zeit – wie lange?

> [!tip] **Merkregel: Das Dreieck**
> ![[praxis-vst-dreieck.png]]
> *<span class="fig-id">15-03-vst-dreieck</span>: Das v-s-t-Dreieck als Merkhilfe für die Formeln $v=\tfrac{s}{t}$, $s=v\cdot t$ und $t=\tfrac{s}{v}$.*
> 
> Decken Sie die gesuchte Größe ab:
> - s abdecken → v × t (nebeneinander = multiplizieren)
> - v abdecken → s ÷ t (übereinander = dividieren)
> - t abdecken → s ÷ v

> [!example] Beispiel
> Ein Auto fährt 120 km in 1,5 Stunden.
> $v = \frac{120}{1{,}5} = 80$ km/h

### Praktische Anwendungen

> [!example] Reiseplanung
> Sie fahren von München nach Hamburg (ca. 780 km). Mit einer Durchschnittsgeschwindigkeit von 100 km/h (inkl. Pausen für Tanken):
> $$t = \frac{780 \text{ km}}{100 \text{ km/h}} = 7{,}8 \text{ h} \approx 7 \text{ h } 48 \text{ min}$$

> [!warning] **Häufiger Fehler: Einheiten mischen**
> Achten Sie darauf, dass alle Größen zueinander passen:
> - km/h mit km und h
> - m/s mit m und s
> 
> Niemals: km/h mit m oder s ohne Umrechnung!

---

## Dichte

> [!note] Formel
> $$\varrho = \frac{m}{V}$$

Die Dichte (griechisch: rho, ϱ) gibt an, wie viel Masse pro Volumeneinheit ein Stoff hat. Sie ist eine charakteristische Materialeigenschaft.

| Material | Dichte (g/cm³) |
|----------|---------------|
| Wasser | 1,00 |
| Aluminium | 2,70 |
| Eisen/Stahl | 7,87 |
| Kupfer | 8,96 |
| Gold | 19,32 |
| Luft | 0,0013 |

### Warum Dichte wichtig ist

Die Dichte erklärt viele Alltagsphänomene:
- Warum schwimmt Holz (ρ ≈ 0,5 g/cm³) auf Wasser?
- Warum ist ein Goldbarren so schwer?
- Warum steigt warme Luft auf? (geringere Dichte als kalte Luft)

> [!example] Beispiel
> 500 g Eisen, $\varrho = 7{,}87$ g/cm³
> $V = \frac{500}{7{,}87} \approx 63{,}5$ cm³

> [!example] Praxisaufgabe: Goldbarren
> Ein Goldbarren hat die Maße 5 cm × 3 cm × 2 cm.
> - Volumen: $V = 5 \times 3 \times 2 = 30$ cm³
> - Masse: $m = \varrho \times V = 19{,}32 \times 30 = 579{,}6$ g ≈ **580 g**

---

## Hebelgesetz

$$F_1 \cdot l_1 = F_2 \cdot l_2$$

Das Hebelgesetz wurde bereits von Archimedes (ca. 287–212 v. Chr.) formuliert. Der berühmte Ausspruch „Gib mir einen Hebel und einen festen Punkt, und ich werde die Welt bewegen" stammt von ihm.

### Das Prinzip

Ein Hebel ist im Gleichgewicht, wenn das Produkt aus Kraft und Hebelarm auf beiden Seiten gleich ist:

![[praxis-hebel.png]]
*<span class="fig-id">15-03-hebel</span>: Das Hebelgesetz – im Gleichgewicht gilt $F_1 \cdot l_1 = F_2 \cdot l_2$.*

> [!example] Beispiel: Wippe
> Ein Kind (30 kg) sitzt 2 m vom Drehpunkt entfernt. Wo muss ein Erwachsener (75 kg) sitzen, damit die Wippe im Gleichgewicht ist?
> 
> $$30 \cdot 2 = 75 \cdot l_2$$
> $$l_2 = \frac{60}{75} = 0{,}8 \text{ m}$$

### Anwendungen im Alltag

- **Schraubenschlüssel**: Längerer Griff = weniger Kraft nötig
- **Nussknacker**: Kurzer Hebel am Objekt, langer Hebel für die Hand
- **Schubkarre**: Rad als Drehpunkt, Last zwischen Rad und Griffen
- **Brecheisen**: Kleiner Ansatzpunkt, langer Hebel multipliziert die Kraft

> [!tip] **Merkregel**
> „Langer Arm, wenig Kraft – kurzer Arm, viel Kraft"
> Je länger der Hebelarm, desto weniger Kraft braucht man.

---

## Elektrische Grundgrößen

In der Elektrotechnik sind drei Grundgrößen fundamental:

> [!note] Ohmsches Gesetz
> $$U = R \cdot I$$
> - **U** = Spannung in Volt (V)
> - **R** = Widerstand in Ohm (Ω)
> - **I** = Stromstärke in Ampere (A)

| Größe | Einheit | Alltagsvergleich |
|-------|---------|------------------|
| Spannung (U) | Volt | „Druck" im Stromkreis |
| Stromstärke (I) | Ampere | „Menge" des fließenden Stroms |
| Widerstand (R) | Ohm | „Bremse" für den Strom |

> [!example] Beispiel
> Eine LED-Lampe hat einen Widerstand von 100 Ω und wird mit 12 V betrieben.
> $$I = \frac{U}{R} = \frac{12}{100} = 0{,}12 \text{ A} = 120 \text{ mA}$$

---

## Zusammenhänge

Technische Berechnungen verbinden mathematisches Wissen mit physikalischen Prinzipien:

- → [[../05-Verhaeltnisse-und-Proportionalitaet/08-Geschwindigkeit-Strecke-und-Zeit|Geschwindigkeit, Strecke, Zeit]] – vertiefte Behandlung
- → [[../05-Verhaeltnisse-und-Proportionalitaet/09-Dichte-und-Masse|Dichte und Masse]] – weitere Beispiele
- → [[02-Einheiten-umrechnen|Einheiten umrechnen]] – wichtige Grundlage
- → [[../08-Gleichungen-und-Ungleichungen/10-Faktorisierung-quadratischer-Gleichungen|Formeln umstellen]] – mathematische Technik

---

**Navigation:** [[02-Einheiten-umrechnen|← Einheiten]] | [[04-Wirtschaftliche-Berechnungen|Wirtschaft →]]
