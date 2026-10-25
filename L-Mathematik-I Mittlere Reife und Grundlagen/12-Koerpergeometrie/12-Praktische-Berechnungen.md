---
title: Praktische Berechnungen
chapter: "12"
section: "12.12"
type: lecture
created: 2026-10-13
modified: 2026-10-25
status: draft - review pending
tags:
  - mathematik/geometrie/koerper
  - anwendungen
  - praxis
---

# Praktische Berechnungen

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Körperberechnungen auf Alltagsprobleme anwenden
> - Füllmengen und Materialverbrauch berechnen
> - Textaufgaben systematisch lösen
> - Ergebnisse auf Plausibilität prüfen

Die Körpergeometrie ist keine abstrakte Theorie – sie begegnet uns täglich im praktischen Leben. Ob wir ein Aquarium befüllen, einen Raum streichen, ein Paket versenden oder einen Kuchen backen: Überall stecken Körperberechnungen dahinter. In diesem Kapitel verbinden wir alle gelernten Formeln mit realen Anwendungen.

## Anwendungsgebiete

### Füllmengen

Füllmengenberechnungen beantworten die Frage: „Wie viel passt hinein?"

> [!example] Aquarium
> Ein rechteckiges Aquarium hat die Maße 80 cm × 40 cm × 50 cm und wird bis 5 cm unter den Rand gefüllt.
> 
> **Füllhöhe:** 50 - 5 = 45 cm
> $$V = 80 \cdot 40 \cdot 45 = 144.000 \text{ cm}^3 = 144 \text{ Liter}$$

> [!example] Regentonne
> Eine zylindrische Regentonne hat 60 cm Durchmesser und 90 cm Höhe.
> $$V = \pi \cdot 30^2 \cdot 90 = 81.000\pi \approx 254.469 \text{ cm}^3 \approx 254 \text{ Liter}$$

> [!tip] **Liter-Umrechnung merken**
> - 1 Liter = 1 dm³ = 1000 cm³
> - Ein Würfel mit 10 cm Kantenlänge fasst genau 1 Liter

### Materialverbrauch

Materialberechnungen beantworten die Frage: „Wie viel brauche ich für die Hülle?"

> [!example] Lackbedarf
> Ein kugelförmiger Tank hat 2 m Durchmesser. Lackverbrauch: 0,15 L/m²
> 
> **Oberfläche:**
> $$O = 4\pi \cdot 1^2 = 4\pi \approx 12{,}57 \text{ m}^2$$
> 
> **Lackbedarf:**
> $$\text{Lack} = 12{,}57 \cdot 0{,}15 \approx 1{,}9 \text{ Liter}$$

> [!example] Geschenkpapier
> Ein Geschenkkarton hat die Maße 30 cm × 20 cm × 10 cm.
> $$O = 2(30 \cdot 20 + 30 \cdot 10 + 20 \cdot 10) = 2(600 + 300 + 200) = 2200 \text{ cm}^2$$
> 
> Mit 20% Zugabe für Überlappungen: $2200 \cdot 1{,}2 = 2640 \text{ cm}^2 \approx 0{,}26 \text{ m}^2$

### Dichte und Masse

Die Verbindung von Volumen und Masse erfolgt über die Dichte:

> [!note] Formel
> $$m = \varrho \cdot V$$
> Masse = Dichte × Volumen

> [!example] Eisenkugel
> Eine Eisenkugel hat den Radius $r = 5$ cm. Dichte von Eisen: $\varrho = 7{,}87$ g/cm³
> 
> **Volumen:**
> $$V = \frac{4}{3}\pi \cdot 5^3 = \frac{500\pi}{3} \approx 523{,}6 \text{ cm}^3$$
> 
> **Masse:**
> $$m = 7{,}87 \cdot 523{,}6 \approx 4121 \text{ g} \approx 4{,}1 \text{ kg}$$

> [!example] Goldbarren
> Ein Goldbarren (Quader) hat die Maße 10 cm × 5 cm × 2 cm. Golddichte: 19,3 g/cm³
> $$V = 10 \cdot 5 \cdot 2 = 100 \text{ cm}^3$$
> $$m = 19{,}3 \cdot 100 = 1930 \text{ g} = 1{,}93 \text{ kg}$$

### Kosten und Wirtschaftlichkeit

> [!example] Betonkosten
> Ein Fundament ist ein Quader: 4 m × 3 m × 0,3 m. Beton kostet 120 €/m³.
> $$V = 4 \cdot 3 \cdot 0{,}3 = 3{,}6 \text{ m}^3$$
> Mit 10% Sicherheitszuschlag: $3{,}6 \cdot 1{,}1 = 3{,}96$ m³
> $$\text{Kosten} = 4 \cdot 120 = 480 \text{ €}$$

## Lösungsstrategie für Textaufgaben

> [!tip] **6-Schritte-Methode**
> 1. **Skizze anfertigen** – Visualisiere das Problem
> 2. **Körperform identifizieren** – Welcher Grundkörper liegt vor?
> 3. **Gegebene Werte notieren** – Was ist bekannt?
> 4. **Passende Formel wählen** – Volumen, Oberfläche oder beides?
> 5. **Einheiten vereinheitlichen** – Alles in cm oder alles in m!
> 6. **Berechnen und prüfen** – Ist das Ergebnis plausibel?

> [!warning] **Typische Fehlerquellen**
> - Einheiten nicht umgerechnet (cm und m gemischt)
> - Radius statt Durchmesser verwendet (oder umgekehrt)
> - Faktor $\frac{1}{3}$ bei Pyramide/Kegel vergessen
> - Oberfläche statt Volumen berechnet (oder umgekehrt)
> - Ergebnis nicht auf Plausibilität geprüft

## Plausibilitätsprüfung

> [!tip] **Ist mein Ergebnis sinnvoll?**
> - Ein Liter Wasser wiegt 1 kg – passt die berechnete Masse?
> - Ein Würfel mit 10 cm Kantenlänge fasst 1 Liter – ist mein Volumen in der richtigen Größenordnung?
> - Eine DIN-A4-Seite hat ca. 600 cm² – passt meine Oberfläche dazu?
> - Überschlagsrechnung: Stimmt die Größenordnung?

---

**Navigation:** [[11-Zusammengesetzte-Koerper|← Zusammengesetzte Körper]] | [[../13-Statistik-und-Datenanalyse/00-Statistik-Index|Statistik →]]
