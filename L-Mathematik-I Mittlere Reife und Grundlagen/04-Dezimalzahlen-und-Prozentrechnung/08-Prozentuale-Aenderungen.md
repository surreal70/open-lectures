---
title: "Prozentuale Änderungen"
chapter: "04"
section: "08"
type: topic
status: "draft - review pending"
learning_objectives:
  - "Prozentuale Zunahme und Abnahme berechnen können"
  - "Den neuen Wert nach prozentualer Änderung bestimmen"
  - "Die prozentuale Änderung zwischen zwei Werten berechnen"
  - "Mehrfache prozentuale Änderungen verstehen"
tags:
  - mathematik
  - prozent
  - aenderung
  - zunahme
  - abnahme
created: 2026-10-13
modified: 2025-01-20
---

# Prozentuale Änderungen

> [!info] Lernziele
> - Prozentuale Zunahme und Abnahme berechnen können
> - Den neuen Wert nach prozentualer Änderung bestimmen
> - Die prozentuale Änderung zwischen zwei Werten berechnen
> - Mehrfache prozentuale Änderungen verstehen

## Überblick

Prozentuale Änderungen beschreiben, um wie viel Prozent ein Wert zu- oder abnimmt. Dies ist fundamental für Preisänderungen, Wachstum, Rabatte und viele weitere Anwendungen.

### Alltagsrelevanz

Prozentuale Änderungen begegnen uns überall:
- **Wirtschaft:** Inflation (z.B. „3,2% Preissteigerung"), Wirtschaftswachstum, Börsenkurse
- **Gesundheit:** Gewichtsveränderung, Heilungsraten, Wirksamkeit von Medikamenten
- **Umwelt:** Bevölkerungswachstum, CO₂-Reduktionsziele, Artenrückgang
- **Technik:** Leistungssteigerung von Computern, Energieeinsparung, Effizienzverbesserung

Das Verständnis prozentualer Änderungen ist essentiell, um Nachrichten, Statistiken und Werbung kritisch einordnen zu können.

### Zunahme vs. Abnahme: Die Richtung der Änderung

Bei einer Zunahme wird etwas größer, bei einer Abnahme kleiner. Mathematisch drücken wir das durch positive und negative Vorzeichen oder durch unterschiedliche Faktoren aus.

## Grundbegriffe

### Prozentuale Zunahme

Eine **Zunahme** liegt vor, wenn der neue Wert größer als der alte ist.

$$\text{Neuer Wert} = \text{Alter Wert} + \text{Zunahme}$$

### Prozentuale Abnahme

Eine **Abnahme** liegt vor, wenn der neue Wert kleiner als der alte ist.

$$\text{Neuer Wert} = \text{Alter Wert} - \text{Abnahme}$$

## Berechnung des neuen Wertes

### Bei Zunahme (Erhöhung)

**Formel:**
$$\text{Neuer Wert} = \text{Alter Wert} \times (1 + \frac{p}{100})$$

oder

$$\text{Neuer Wert} = \text{Alter Wert} \times \frac{100 + p}{100}$$

**Beispiel:** 200 € werden um 15% erhöht.

$$\text{Neuer Wert} = 200 \times 1,15 = 230 €$$

### Bei Abnahme (Verminderung)

**Formel:**
$$\text{Neuer Wert} = \text{Alter Wert} \times (1 - \frac{p}{100})$$

oder

$$\text{Neuer Wert} = \text{Alter Wert} \times \frac{100 - p}{100}$$

**Beispiel:** 200 € werden um 15% reduziert.

$$\text{Neuer Wert} = 200 \times 0,85 = 170 €$$

### Faktortabelle

| Änderung | Faktor | Beispiel |
|----------|--------|----------|
| +50% | 1,50 | 100 × 1,50 = 150 |
| +25% | 1,25 | 100 × 1,25 = 125 |
| +10% | 1,10 | 100 × 1,10 = 110 |
| +5% | 1,05 | 100 × 1,05 = 105 |
| −5% | 0,95 | 100 × 0,95 = 95 |
| −10% | 0,90 | 100 × 0,90 = 90 |
| −25% | 0,75 | 100 × 0,75 = 75 |
| −50% | 0,50 | 100 × 0,50 = 50 |

## Berechnung der prozentualen Änderung

### Formel

$$p = \frac{\text{Neuer Wert} - \text{Alter Wert}}{\text{Alter Wert}} \times 100$$

oder

$$p = \left(\frac{\text{Neuer Wert}}{\text{Alter Wert}} - 1\right) \times 100$$

### Beispiel: Preiserhöhung

**Aufgabe:** Der Preis steigt von 80 € auf 92 €. Um wie viel Prozent?

$$p = \frac{92 - 80}{80} \times 100 = \frac{12}{80} \times 100 = 15\%$$

### Beispiel: Preissenkung

**Aufgabe:** Der Preis fällt von 150 € auf 120 €. Um wie viel Prozent?

$$p = \frac{120 - 150}{150} \times 100 = \frac{-30}{150} \times 100 = -20\%$$

Das negative Vorzeichen zeigt eine **Abnahme** von 20%.

## Mehrfache prozentuale Änderungen

### Aufeinanderfolgende Änderungen

> [!warning] **Häufiger Fehler: Prozente addieren**
> Aufeinanderfolgende Prozentänderungen werden **nicht addiert**, sondern **multipliziert**!

**Beispiel:** Erst +20%, dann −20%

$$100 \times 1,20 = 120$$
$$120 \times 0,80 = 96$$

**Ergebnis:** 96 (nicht 100!)

### Warum heben sich +20% und −20% nicht auf?

Das ist eine der wichtigsten Erkenntnisse der Prozentrechnung und gleichzeitig eine häufige Fehlerquelle. Der Grund: Die beiden Prozentangaben beziehen sich auf **unterschiedliche Grundwerte**!

- +20% bezieht sich auf 100 → ergibt 120
- −20% bezieht sich jetzt auf 120 (nicht auf 100!) → ergibt 96

20% von 120 sind eben mehr als 20% von 100. Deshalb endet man unter dem Ausgangswert.

> [!tip] **Anschauliche Erklärung**
> Stell dir einen Luftballon vor:
> - Du bläst ihn um 50% auf → er ist jetzt 1,5-mal so groß
> - Dann lässt du 50% der Luft ab → aber 50% von dem größeren Ballon!
> - Der Ballon ist jetzt nur noch 75% seiner ursprünglichen Größe

### Formel für mehrfache Änderungen

$$\text{Endwert} = \text{Startwert} \times (1 + p_1\%) \times (1 + p_2\%) \times ...$$

### Beispiel: Doppelter Rabatt

**Aufgabe:** Ein Artikel hat 30% Rabatt. Zusätzlich gibt es 10% Kundenrabatt. Wie viel zahlt man bei 200 € Originalpreis?

$$200 \times 0,70 \times 0,90 = 200 \times 0,63 = 126 €$$

**Hinweis:** Der Gesamtrabatt ist 37%, nicht 40%!

## Hin- und Rückrechnung

### Problem: Nicht-Symmetrie

+20% und −20% heben sich **nicht** auf!

| Startwert | +20% | dann −20% | Ergebnis |
|-----------|------|-----------|----------|
| 100 | 120 | 96 | 96 (nicht 100) |
| 200 | 240 | 192 | 192 |

### Welche Abnahme hebt +p% auf?

Wenn ein Wert um p% gestiegen ist, muss er um weniger als p% fallen, um den Ausgangswert zu erreichen.

**Formel:**
$$\text{Ausgleichende Abnahme} = \frac{p}{100 + p} \times 100$$

**Beispiel:** Nach +25% Anstieg braucht man:
$$\frac{25}{125} \times 100 = 20\%$$ Abnahme

### Welche Zunahme hebt −p% auf?

**Formel:**
$$\text{Ausgleichende Zunahme} = \frac{p}{100 - p} \times 100$$

**Beispiel:** Nach −20% Abnahme braucht man:
$$\frac{20}{80} \times 100 = 25\%$$ Zunahme

## Anwendungsbeispiele

### Beispiel 1: Inflation

**Aufgabe:** Die Inflation beträgt 3% pro Jahr. Wie viel sind 1000 € nach 2 Jahren wert (Kaufkraft)?

$$\text{Kaufkraft} = 1000 \times 0,97^2 = 1000 \times 0,9409 = 940,90 €$$

### Beispiel 2: Bevölkerungswachstum

**Aufgabe:** Eine Stadt hat 50.000 Einwohner. Bei 2% Wachstum pro Jahr: Wie viele nach 3 Jahren?

$$50.000 \times 1,02^3 = 50.000 \times 1,0612 = 53.060$$

### Beispiel 3: Wertverlust

**Aufgabe:** Ein Auto verliert pro Jahr 15% an Wert. Neuwert: 20.000 €. Wert nach 4 Jahren?

$$20.000 \times 0,85^4 = 20.000 \times 0,522 = 10.440 €$$

## Zusammenhänge

### Beziehung zu anderen Themen

- **Zinsrechnung:** Zinsen sind prozentuale Zunahme
- **Rabattrechnung:** Rabatt ist prozentuale Abnahme
- **Exponentielles Wachstum:** Mehrfache Änderungen

### Voraussetzungen

- [[04-Einfuehrung-in-die-Prozentrechnung]] - Grundbegriffe
- [[05-Prozentwert]] - Berechnung von Anteilen

## Prüfungsrelevanz

> [!warning] Prüfungsrelevanz: Sehr hoch
> Prozentuale Änderungen sind Kernstoff und kommen in vielen Sachzusammenhängen vor.

## Typische Prüfungsfragen

1. **Erhöhung:** Ein Gehalt von 2400 € wird um 3,5% erhöht. Wie hoch ist das neue Gehalt?
2. **Senkung:** Der Preis wird um 15% gesenkt. Der neue Preis ist 170 €. Wie hoch war der alte?
3. **Änderung berechnen:** Der Preis steigt von 45 € auf 54 €. Um wie viel Prozent?
4. **Doppelte Änderung:** Erst 20% Rabatt, dann nochmal 10%. Wie viel Prozent Gesamtrabatt?
5. **Rückrechnung:** Um wie viel Prozent muss ein um 25% erhöhter Preis sinken, um wieder den Ausgangspreis zu erreichen?

## Quellen

- Lambacher Schweizer Mathematik 7
- Schulbuch Mathematik Realschule Bayern

## Weiterführende Links

- [[09-Rabatte-und-Preisberechnungen]] - Rabattrechnung
- [[10-Zinsrechnung]] - Anwendung bei Zinsen
- [[11-Zinseszins-Grundlagen]] - Mehrfache Änderungen
