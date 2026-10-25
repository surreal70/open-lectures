---
title: Einheiten sicher umrechnen
chapter: "15"
section: "15.2"
type: lecture
created: 2026-10-13
modified: 2026-10-25
status: draft - review pending
tags:
  - mathematik/anwendung
  - einheiten
---

# Einheiten sicher umrechnen

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Längen-, Flächen- und Volumeneinheiten umrechnen
> - Zeit- und Geschwindigkeitseinheiten umwandeln

Das Umrechnen von Einheiten gehört zu den grundlegendsten mathematischen Fertigkeiten im Alltag und Beruf. Ob beim Kochen (ml in Esslöffel), beim Reisen (Meilen in Kilometer) oder im Handwerk (cm² in m²) – überall begegnen uns verschiedene Maßeinheiten.

### Das metrische System

Das heute weltweit verwendete **Système International d'Unités (SI)** wurde 1799 während der Französischen Revolution eingeführt. Die Grundidee war revolutionär einfach: Alle Umrechnungen basieren auf Zehnerpotenzen. Dies war ein enormer Fortschritt gegenüber den chaotischen alten Maßsystemen, in denen beispielsweise 12 Zoll einen Fuß ergaben und 3 Fuß eine Elle.

> [!note] **Das dezimale Prinzip**
> Die Vorsilben im SI-System folgen einer klaren Logik:
> - **kilo** (k) = 1000 = 10³
> - **hekto** (h) = 100 = 10²
> - **dezi** (d) = 0,1 = 10⁻¹
> - **zenti** (c) = 0,01 = 10⁻²
> - **milli** (m) = 0,001 = 10⁻³

---

## Längeneinheiten

| Einheit | Faktor |
|---------|--------|
| 1 km | = 1000 m |
| 1 m | = 100 cm |
| 1 cm | = 10 mm |

### Die Einheitenkette

Eine praktische Darstellung für Längenumrechnungen:

![[praxis-einheitenkette.png]]
*<span class="fig-id">15-02-einheitenkette</span>: Die Längen-Einheitenkette – nach rechts wird mit dem Stufenfaktor multipliziert, nach links dividiert.*

> [!tip] **Merkregel: Stufen zählen**
> Zählen Sie die Stufen zwischen den Einheiten und multiplizieren/dividieren Sie entsprechend:
> - Von **cm** nach **m**: 2 Stufen nach links → ÷ 100
> - Von **km** nach **mm**: 6 Stufen nach rechts → × 1.000.000

> [!example] Beispiel
> 2,5 km in cm umrechnen:
> - km → m: × 1000 → 2500 m
> - m → cm: × 100 → 250.000 cm
> - Oder direkt: × 100.000 (5 Stufen)

---

## Flächeneinheiten

Faktor jeweils **100** (= 10²):
- 1 m² = 100 dm² = 10.000 cm²
- 1 ha = 10.000 m²
- 1 km² = 100 ha

### Warum quadrieren?

Bei Flächeneinheiten werden die Längenumrechnungen **quadriert**. Der Grund ist anschaulich: Ein Quadratmeter ist ein Quadrat mit 1 m Seitenlänge. In Zentimetern hat dieses Quadrat Seiten von 100 cm. Die Fläche ist also:

$$1 \text{ m}^2 = 100 \text{ cm} \times 100 \text{ cm} = 10.000 \text{ cm}^2$$

> [!warning] **Häufiger Fehler: Längen- und Flächenfaktoren verwechseln**
> - Länge: 1 m = 100 cm → Faktor 100
> - Fläche: 1 m² = 10.000 cm² → Faktor 10.000 (= 100²)
> 
> Viele Schüler rechnen Flächen mit dem Längenfaktor um und erhalten dadurch Ergebnisse, die um den Faktor 100 daneben liegen!

### Landwirtschaftliche Einheiten

Die Einheit **Hektar (ha)** ist besonders in der Landwirtschaft verbreitet:
- 1 ha = 100 m × 100 m = 10.000 m²
- 1 km² = 100 ha (ein Quadrat von 10 × 10 Feldern)

Diese Einheit entstand ebenfalls in der Französischen Revolution als „Hektare" – wörtlich „hundert Ar" (1 Ar = 100 m²).

---

## Volumeneinheiten

Faktor jeweils **1000** (= 10³):
- 1 m³ = 1000 dm³ = 1000 Liter
- 1 Liter = 1000 ml = 1000 cm³

### Der Kubik-Effekt

Bei Volumeneinheiten werden die Längenumrechnungen **kubiert**:

$$1 \text{ m}^3 = 100 \text{ cm} \times 100 \text{ cm} \times 100 \text{ cm} = 1.000.000 \text{ cm}^3$$

> [!tip] **Merkregel: Liter und Kubik**
> Die wichtigste Beziehung für den Alltag:
> - **1 Liter = 1 dm³ = 1000 cm³ = 1000 ml**
> - **1 ml = 1 cm³** (ein Würfel mit 1 cm Kantenlänge)

> [!example] Beispiel: Aquarium
> Ein Aquarium hat die Maße 80 cm × 40 cm × 50 cm.
> - Volumen: $80 \times 40 \times 50 = 160.000$ cm³
> - In Litern: $160.000 \div 1000 = 160$ Liter

---

## Geschwindigkeit

$$1 \frac{\text{km}}{\text{h}} = \frac{1000 \text{ m}}{3600 \text{ s}} = \frac{1}{3{,}6} \frac{\text{m}}{\text{s}}$$

> [!tip] Merkregel
> km/h → m/s: durch 3,6
> m/s → km/h: mal 3,6

### Warum 3,6?

Die Herleitung ist einfach:
- 1 km = 1000 m
- 1 h = 3600 s (60 min × 60 s)
- Also: $\frac{1000}{3600} = \frac{1}{3,6}$

> [!example] Praktische Anwendungen
> - Usain Bolt lief 100 m in 9,58 s → ca. 10,4 m/s → ca. **37,6 km/h**
> - Autobahn 130 km/h → ca. **36 m/s** (pro Sekunde ein halbes Fußballfeld!)
> - Schallgeschwindigkeit: ca. 340 m/s → ca. **1224 km/h**

---

## Zeiteinheiten

| Umrechnung | Faktor |
|------------|--------|
| 1 Minute | = 60 Sekunden |
| 1 Stunde | = 60 Minuten = 3600 Sekunden |
| 1 Tag | = 24 Stunden = 1440 Minuten |

> [!note] **Historischer Hintergrund**
> Das Sexagesimalsystem (Basis 60) für Zeit stammt von den Babyloniern vor ca. 4000 Jahren. 60 hat viele Teiler (1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60), was das Teilen einfacher macht. Deshalb hat unsere Uhr auch heute noch 60 Minuten und 60 Sekunden.

---

## Zusammenfassung

| Typ | Umrechnung | Faktor |
|-----|------------|--------|
| Länge | m → cm | × 100 |
| Fläche | m² → cm² | × 10.000 |
| Volumen | m³ → cm³ | × 1.000.000 |
| Geschwindigkeit | km/h → m/s | ÷ 3,6 |

## Zusammenhänge

Einheitenumrechnung verbindet sich mit vielen anderen Themen:

- → [[../05-Verhaeltnisse-und-Proportionalitaet/06-Umrechnungen-von-Einheiten|Umrechnungen von Einheiten]] – vertiefte Behandlung
- → [[../06-Potenzen-Wurzeln-und-Zahlendarstellung/05-Zehnerpotenzen|Zehnerpotenzen]] – mathematische Grundlage
- → [[03-Technische-Berechnungen|Technische Berechnungen]] – praktische Anwendung
- → [[../10-Grundlagen-der-Geometrie/07-Umfangsberechnungen|Umfangsberechnungen]] – Längeneinheiten in der Geometrie

---

**Navigation:** [[01-Textaufgaben-loesen|← Textaufgaben]] | [[03-Technische-Berechnungen|Technik →]]
