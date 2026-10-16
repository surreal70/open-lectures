---
title: "Zinsrechnung"
chapter: "04"
section: "10"
type: topic
status: "draft - review pending"
learning_objectives:
  - "Die Begriffe Kapital, Zinssatz und Zinsen verstehen"
  - "Zinsen für verschiedene Zeiträume berechnen können"
  - "Mit der Zinsformel arbeiten können"
  - "Alltagsrelevante Zinsaufgaben lösen"
tags:
  - mathematik
  - prozent
  - zinsen
  - kapital
  - finanzen
created: 2026-10-13
modified: 2025-01-20
---

# Zinsrechnung

> [!info] Lernziele
> - Die Begriffe Kapital, Zinssatz und Zinsen verstehen
> - Zinsen für verschiedene Zeiträume berechnen können
> - Mit der Zinsformel arbeiten können
> - Alltagsrelevante Zinsaufgaben lösen

## Überblick

Die Zinsrechnung ist eine Anwendung der Prozentrechnung, bei der die Zeit als zusätzlicher Faktor berücksichtigt wird. Sie ist grundlegend für das Verständnis von Geldanlagen, Krediten und Finanzprodukten.

### Historischer Hintergrund

Die Idee, für geliehenes Geld eine Gebühr zu verlangen, ist uralt. Bereits im antiken Babylon (ca. 2000 v. Chr.) gab es Zinsen – damals allerdings oft in Form von Naturalien wie Getreide. Das Wort „Zins" stammt vom lateinischen „census" (Abgabe, Steuer).

Im Mittelalter war das Verleihen von Geld gegen Zinsen in Europa zeitweise verboten (Zinsverbot der Kirche), was zur Entstehung des modernen Bankwesens in Italien führte. Heute sind Zinsen das zentrale Instrument der Geldpolitik und beeinflussen Wirtschaft, Immobilienpreise und unsere Sparentscheidungen.

### Alltagsrelevanz

Zinsen betreffen fast jeden:
- **Sparen:** Was bringt ein Sparkonto, ein Festgeld, ein ETF?
- **Kredite:** Was kostet ein Autokredit, eine Baufinanzierung?
- **Dispositionskredit:** Wie teuer wird das Überziehen des Girokontos?
- **Ratenkauf:** Lohnt sich die „0%-Finanzierung" wirklich?

## Grundbegriffe

### Die drei Grundgrößen

| Begriff | Symbol | Bedeutung | Beispiel |
|---------|--------|-----------|----------|
| **Kapital** | K | Der angelegte/geliehene Betrag | 1000 € |
| **Zinssatz** | p% | Der Prozentsatz pro Jahr | 3% |
| **Zinsen** | Z | Der Ertrag/die Kosten | 30 € |

### Entsprechung zur Prozentrechnung

| Prozentrechnung | Zinsrechnung |
|-----------------|--------------|
| Grundwert G | Kapital K |
| Prozentsatz p% | Zinssatz p% |
| Prozentwert W | Zinsen Z |

## Jahreszinsen

### Formel

$$Z = K \times \frac{p}{100}$$

oder

$$Z = K \times p\%$$

### Beispiel

**Aufgabe:** Wie viel Zinsen erhält man für 2500 € bei 2,5% Zinsen pro Jahr?

$$Z = 2500 \times \frac{2,5}{100} = 2500 \times 0,025 = 62,50 €$$

**Antwort:** Man erhält **62,50 €** Zinsen.

## Zinsen für andere Zeiträume

### Monatszinsen

**Formel:**
$$Z_m = K \times \frac{p}{100} \times \frac{m}{12}$$

wobei m = Anzahl der Monate

**Beispiel:** 3000 € für 4 Monate bei 6% p.a.
$$Z = 3000 \times 0,06 \times \frac{4}{12} = 3000 \times 0,06 \times \frac{1}{3} = 60 €$$

### Tageszinsen

**Formel (kaufmännisch):**
$$Z_t = K \times \frac{p}{100} \times \frac{t}{360}$$

wobei t = Anzahl der Tage (Bankjahr = 360 Tage)

> [!note] **Warum 360 statt 365 Tage?**
> Im kaufmännischen Bereich rechnet man traditionell mit 360 Tagen pro Jahr (12 Monate à 30 Tage). Diese Vereinfachung stammt aus der Zeit vor Taschenrechnern, als das Rechnen mit 360 deutlich einfacher war. In der Wissenschaft und bei manchen modernen Finanzprodukten wird dagegen mit 365 (oder 366) Tagen gerechnet – das nennt man dann „taggenaue Verzinsung".

**Beispiel:** 5000 € für 45 Tage bei 4% p.a.
$$Z = 5000 \times 0,04 \times \frac{45}{360} = 5000 \times 0,04 \times 0,125 = 25 €$$

### Übersicht Zeitfaktoren

| Zeitraum | Faktor |
|----------|--------|
| 1 Jahr | 1 |
| 6 Monate | 1/2 = 0,5 |
| 3 Monate | 1/4 = 0,25 |
| 1 Monat | 1/12 |
| 1 Tag | 1/360 (kaufm.) |

## Weitere Berechnungen

### Kapital berechnen

**Gesucht:** Wie viel muss man anlegen, um bestimmte Zinsen zu erhalten?

$$K = \frac{Z \times 100}{p}$$

**Beispiel:** Wie viel Kapital braucht man für 150 € Zinsen bei 3%?
$$K = \frac{150 \times 100}{3} = 5000 €$$

### Zinssatz berechnen

**Gesucht:** Welcher Zinssatz liegt vor?

$$p = \frac{Z \times 100}{K}$$

**Beispiel:** 80 € Zinsen für 2000 € Kapital. Zinssatz?
$$p = \frac{80 \times 100}{2000} = 4\%$$

### Zeit berechnen

**Gesucht:** Wie lange muss das Geld angelegt werden?

$$t = \frac{Z \times 360}{K \times p} \times 100 \text{ (in Tagen)}$$

**Beispiel:** Wann sind 40 € Zinsen erreicht bei 4800 € und 5%?
$$t = \frac{40 \times 360 \times 100}{4800 \times 5} = \frac{1.440.000}{24.000} = 60 \text{ Tage}$$

## Die allgemeine Zinsformel

### Zusammenfassung

$$Z = K \times \frac{p}{100} \times \frac{t}{360}$$

### Formeldreieck

```
           ┌──────────┐
           │    Z     │
           └────┬─────┘
      ┌─────────┼─────────┐
      │         │         │
┌─────┴─────┐ ┌─┴──┐ ┌────┴────┐
│   K × p   │ │ × │ │ t / 360 │
└───────────┘ └────┘ └─────────┘
```

### Umgestellte Formeln

| Gesucht | Formel |
|---------|--------|
| Zinsen Z | $Z = K \times \frac{p}{100} \times \frac{t}{360}$ |
| Kapital K | $K = \frac{Z \times 100 \times 360}{p \times t}$ |
| Zinssatz p | $p = \frac{Z \times 100 \times 360}{K \times t}$ |
| Zeit t | $t = \frac{Z \times 100 \times 360}{K \times p}$ |

## Beispielaufgaben

### Beispiel 1: Sparbuch

**Aufgabe:** 8000 € werden für 9 Monate bei 1,5% p.a. angelegt.

$$Z = 8000 \times \frac{1,5}{100} \times \frac{9}{12} = 8000 \times 0,015 \times 0,75 = 90 €$$

### Beispiel 2: Dispositionskredit

**Aufgabe:** Ein Girokonto ist 75 Tage mit 1200 € im Minus. Der Dispozins beträgt 12% p.a.

$$Z = 1200 \times \frac{12}{100} \times \frac{75}{360} = 1200 \times 0,12 \times 0,2083 = 30 €$$

### Beispiel 3: Zinseszinsfreies Darlehen

**Aufgabe:** Ein Darlehen über 15.000 € wird nach 2 Jahren mit insgesamt 16.200 € zurückgezahlt. Wie hoch war der Zinssatz?

**Zinsen:** 16.200 − 15.000 = 1.200 € (für 2 Jahre)
**Pro Jahr:** 1.200 ÷ 2 = 600 €

$$p = \frac{600 \times 100}{15.000} = 4\%$$

## Zusammenhänge

### Beziehung zu anderen Themen

- **Prozentrechnung:** Zinsen = Prozentwert mit Zeitfaktor
- **Dreisatz:** Alternative Lösungsmethode
- **Zinseszins:** Erweiterung für mehrere Perioden

### Voraussetzungen

- [[04-Einfuehrung-in-die-Prozentrechnung]] - Grundbegriffe
- [[05-Prozentwert]] - Berechnung

## Prüfungsrelevanz

> [!warning] Prüfungsrelevanz: Hoch
> Einfache Zinsrechnung ist Standardstoff. Besonders wichtig: Jahreszinsen und Monatszinsen.

## Typische Prüfungsfragen

1. **Jahreszinsen:** Berechne die Zinsen für 4500 € bei 2,5% p.a.
2. **Monatszinsen:** 6000 € werden 8 Monate bei 3% angelegt. Wie viel Zinsen?
3. **Tageszinsen:** 2000 € für 90 Tage bei 4,5% p.a. Zinsen?
4. **Kapital gesucht:** Für 45 € Jahreszinsen bei 1,5% p.a. braucht man wie viel Kapital?
5. **Kredit:** Ein Kredit über 5000 € zu 8% p.a. für 6 Monate. Wie viel Zinsen fallen an?

## Quellen

- Lambacher Schweizer Mathematik 7
- Schulbuch Mathematik Realschule Bayern

## Weiterführende Links

- [[11-Zinseszins-Grundlagen]] - Zinseszinsrechnung
- [[12-Praktische-wirtschaftliche-Anwendungen]] - Weitere Finanzanwendungen
