---
title: "Zinseszins-Grundlagen"
chapter: "04"
section: "11"
type: topic
status: "draft - review pending"
learning_objectives:
  - "Den Unterschied zwischen einfachen Zinsen und Zinseszins verstehen"
  - "Die Zinseszinsformel anwenden können"
  - "Kapitalentwicklung über mehrere Jahre berechnen"
  - "Die Wirkung des Zinseszinseffekts erkennen"
tags:
  - mathematik
  - prozent
  - zinseszins
  - exponentiell
  - wachstum
created: 2026-10-13
modified: 2026-10-13
---

# Zinseszins-Grundlagen

> [!info] Lernziele
> - Den Unterschied zwischen einfachen Zinsen und Zinseszins verstehen
> - Die Zinseszinsformel anwenden können
> - Kapitalentwicklung über mehrere Jahre berechnen
> - Die Wirkung des Zinseszinseffekts erkennen

## Überblick

Beim **Zinseszins** werden die Zinsen nicht ausgezahlt, sondern dem Kapital zugeschlagen. Im nächsten Jahr werden dann Zinsen auf das erhöhte Kapital (einschließlich der Vorjahreszinsen) berechnet – "Zinsen auf Zinsen".

## Einfache Zinsen vs. Zinseszins

### Einfache Zinsen (lineare Verzinsung)

Die Zinsen werden jedes Jahr nur auf das ursprüngliche Kapital berechnet.

$$Z_{\text{gesamt}} = K \times \frac{p}{100} \times n$$

wobei n = Anzahl der Jahre

### Zinseszins (exponentielle Verzinsung)

Die Zinsen werden jedes Jahr auf das jeweils aktuelle Kapital (inkl. bisheriger Zinsen) berechnet.

### Vergleich am Beispiel

**1000 € bei 5% für 3 Jahre:**

| Jahr | Einfache Zinsen | Zinseszins |
|------|-----------------|------------|
| Start | 1000,00 € | 1000,00 € |
| Jahr 1 | 1050,00 € (+50) | 1050,00 € (+50,00) |
| Jahr 2 | 1100,00 € (+50) | 1102,50 € (+52,50) |
| Jahr 3 | 1150,00 € (+50) | 1157,63 € (+55,13) |
| **Differenz** | | **+7,63 €** |

## Die Zinseszinsformel

### Grundformel

$$K_n = K_0 \times \left(1 + \frac{p}{100}\right)^n$$

oder mit dem **Wachstumsfaktor** q:

$$K_n = K_0 \times q^n$$

wobei $q = 1 + \frac{p}{100}$

### Bedeutung der Variablen

| Variable | Bedeutung |
|----------|-----------|
| K₀ | Anfangskapital |
| Kₙ | Endkapital nach n Jahren |
| p | Zinssatz in Prozent |
| n | Anzahl der Jahre |
| q | Wachstumsfaktor (1 + p/100) |

### Wachstumsfaktoren

| Zinssatz | Wachstumsfaktor q |
|----------|-------------------|
| 1% | 1,01 |
| 2% | 1,02 |
| 3% | 1,03 |
| 5% | 1,05 |
| 10% | 1,10 |

## Beispielrechnungen

### Beispiel 1: Kapitalentwicklung

**Aufgabe:** 5000 € werden 4 Jahre zu 3% p.a. mit Zinseszins angelegt.

$$K_4 = 5000 \times 1,03^4 = 5000 \times 1,1255 = 5627,54 €$$

**Zinsen insgesamt:** 5627,54 − 5000 = 627,54 €

### Beispiel 2: Vergleich mit einfachen Zinsen

**Aufgabe:** Vergleiche die Ergebnisse für 10.000 € bei 4% nach 10 Jahren.

**Einfache Zinsen:**
$$K = 10.000 + 10.000 \times 0,04 \times 10 = 10.000 + 4000 = 14.000 €$$

**Zinseszins:**
$$K_{10} = 10.000 \times 1,04^{10} = 10.000 \times 1,4802 = 14.802,44 €$$

**Differenz:** 14.802,44 − 14.000 = **802,44 €** mehr durch Zinseszins

### Beispiel 3: Kurze Laufzeit

**Aufgabe:** 2000 € für 2 Jahre bei 2,5% p.a.

$$K_2 = 2000 \times 1,025^2 = 2000 \times 1,050625 = 2101,25 €$$

## Umgekehrte Berechnungen

### Anfangskapital berechnen

**Formel:**
$$K_0 = \frac{K_n}{q^n}$$

**Beispiel:** Welches Kapital ergibt nach 5 Jahren bei 4% ein Endkapital von 6083,26 €?

$$K_0 = \frac{6083,26}{1,04^5} = \frac{6083,26}{1,2167} = 5000 €$$

### Laufzeit berechnen

**Formel:**
$$n = \frac{\log(K_n/K_0)}{\log(q)}$$

**Beispiel:** Wann verdoppelt sich 1000 € bei 5%?

$$n = \frac{\log(2000/1000)}{\log(1,05)} = \frac{\log(2)}{\log(1,05)} = \frac{0,301}{0,0212} ≈ 14,2 \text{ Jahre}$$

## Die 72er-Regel (Faustformel)

### Verdoppelungszeit abschätzen

$$\text{Verdoppelungszeit} ≈ \frac{72}{\text{Zinssatz in \%}}$$

### Beispiele

| Zinssatz | Verdoppelungszeit |
|----------|-------------------|
| 1% | 72 Jahre |
| 2% | 36 Jahre |
| 3% | 24 Jahre |
| 6% | 12 Jahre |
| 12% | 6 Jahre |

## Tabellarische Darstellung

### Jahr für Jahr berechnen

**2000 € bei 3% für 5 Jahre:**

| Jahr | Kapital Anfang | Zinsen | Kapital Ende |
|------|----------------|--------|--------------|
| 1 | 2000,00 € | 60,00 € | 2060,00 € |
| 2 | 2060,00 € | 61,80 € | 2121,80 € |
| 3 | 2121,80 € | 63,65 € | 2185,45 € |
| 4 | 2185,45 € | 65,56 € | 2251,01 € |
| 5 | 2251,01 € | 67,53 € | 2318,54 € |

**Kontrolle:** $2000 \times 1,03^5 = 2318,55 €$ ✓

## Der Zinseszinseffekt

### Visualisierung

```
Kapital
  ↑
  │                          ·····
  │                    ·····
  │               ·····     Zinseszins
  │          ·····          (exponentiell)
  │     ·····
  │····──────────────────── Einfache Zinsen
  │                         (linear)
  └─────────────────────────────→ Zeit
```

### Langfristige Wirkung

**10.000 € bei 5% für verschiedene Laufzeiten:**

| Jahre | Mit Zinseszins | Ohne Zinseszins | Differenz |
|-------|----------------|-----------------|-----------|
| 10 | 16.289 € | 15.000 € | 1.289 € |
| 20 | 26.533 € | 20.000 € | 6.533 € |
| 30 | 43.219 € | 25.000 € | 18.219 € |
| 40 | 70.400 € | 30.000 € | 40.400 € |

## Zusammenhänge

### Beziehung zu anderen Themen

- **Einfache Zinsen:** Spezialfall für n = 1
- **Prozentuale Änderungen:** Mehrfache Anwendung
- **Exponentialfunktion:** Mathematischer Hintergrund

### Voraussetzungen

- [[10-Zinsrechnung]] - Einfache Zinsrechnung
- [[08-Prozentuale-Aenderungen]] - Mehrfache Änderungen

## Prüfungsrelevanz

> [!warning] Prüfungsrelevanz: Mittel-Hoch
> Zinseszins kommt vor allem in Textaufgaben vor. Wichtig: Unterschied zu einfachen Zinsen erkennen.

## Typische Prüfungsfragen

1. **Endkapital:** 3000 € werden 5 Jahre zu 2,5% angelegt. Endkapital mit Zinseszins?
2. **Vergleich:** Vergleiche 4000 € bei 3% für 8 Jahre: einfache Zinsen vs. Zinseszins.
3. **Tabellarisch:** Stelle die Kapitalentwicklung von 1000 € bei 4% für 4 Jahre tabellarisch dar.
4. **Anfangskapital:** Welches Anfangskapital ergibt bei 3% nach 6 Jahren 5970,26 €?
5. **Verdoppelung:** Nach wie vielen Jahren verdoppelt sich ein Kapital bei 6% Zinsen (ungefähr)?

## Quellen

- Lambacher Schweizer Mathematik 8
- Schulbuch Mathematik Realschule Bayern

## Weiterführende Links

- [[10-Zinsrechnung]] - Einfache Zinsrechnung
- [[12-Praktische-wirtschaftliche-Anwendungen]] - Anwendungen
