---
title: Wirtschaftliche Berechnungen
chapter: "15"
section: "15.4"
type: lecture
created: 2026-10-13
modified: 2025-07-18
status: draft - review pending
tags:
  - mathematik/anwendung
  - wirtschaft
  - prozent
---

# Wirtschaftliche Berechnungen

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Rabatte und Aufschläge berechnen
> - Zins- und Zinseszinsrechnung durchführen
> - Steuern berechnen

Wirtschaftsmathematik begegnet uns täglich: beim Einkaufen, bei der Gehaltsabrechnung, beim Sparen und bei Kreditentscheidungen. Die Grundlage bildet die [[../04-Dezimalzahlen-und-Prozentrechnung/04-Einfuehrung-in-die-Prozentrechnung|Prozentrechnung]], die hier in konkreten Anwendungsszenarien vertieft wird.

### Warum wirtschaftliche Kompetenz wichtig ist

Wer diese Berechnungen beherrscht, kann:
- Sonderangebote kritisch bewerten
- Kreditangebote vergleichen
- Die eigene Gehaltsabrechnung verstehen
- Finanzielle Entscheidungen fundiert treffen

> [!note] **Der Ursprung des Prozentzeichens**
> Das Symbol „%" entwickelte sich aus der italienischen Kaufmannssprache. „Per cento" (pro Hundert) wurde abgekürzt zu „p. 100", dann zu „p̈c̈" und schließlich zum heutigen %-Zeichen.

---

## Rabatt

> [!note] Formel
> Endpreis = Grundpreis × (1 - Rabatt%)

Ein Rabatt ist eine Preisminderung, die vom Verkäufer gewährt wird. Der reduzierte Preis ergibt sich aus dem Originalpreis abzüglich des Rabattbetrags.

> [!example] Beispiel
> 80 € Artikel, 15% Rabatt
> Endpreis = 80 × 0,85 = 68 €

### Rabatt rückwärts berechnen

Oft ist der Endpreis bekannt und der Originalpreis gesucht:

> [!example] Vom Endpreis zum Originalpreis
> Ein Fernseher kostet nach 20% Rabatt noch 479 €. Was war der Originalpreis?
> 
> Nach 20% Rabatt bleiben 80% = 0,80 des Originals:
> $$\text{Original} = \frac{479}{0{,}80} = 598{,}75 \text{ €}$$

> [!warning] **Häufiger Fehler: Prozent „draufrechnen"**
> Wenn ein Artikel um 20% reduziert wurde, kann man den Originalpreis **nicht** durch Addition von 20% zurückbekommen:
> - ❌ Falsch: 479 € + 20% = 479 × 1,20 = 574,80 €
> - ✓ Richtig: 479 € ÷ 0,80 = 598,75 €
> 
> Der Unterschied: 20% vom reduzierten Preis ist weniger als 20% vom Originalpreis!

### Mehrere Rabatte nacheinander

Bei mehreren Rabattaktionen werden diese **multiplikativ** verrechnet, nicht addiert:

> [!example] Doppelter Rabatt
> Ein Möbelhaus bietet 15% Rabatt + zusätzlich 10% für Neukunden.
> 
> Das ist **nicht** 25% Rabatt!
> 
> Rechnung für einen 500 €-Schrank:
> - Nach 15%: $500 × 0{,}85 = 425$ €
> - Nach zusätzlichen 10%: $425 × 0{,}90 = 382{,}50$ €
> - Gesamtrabatt: $\frac{500 - 382{,}50}{500} = 23{,}5\%$

---

## Zinsrechnung

> [!note] Formeln
> **Einfacher Zins:** $Z = K \cdot p \cdot t$
> **Zinseszins:** $K_n = K_0 \cdot (1 + p)^n$

### Einfache Zinsrechnung

Bei der einfachen Zinsrechnung werden die Zinsen nicht wieder angelegt:

- **K** = Kapital (Anfangsbetrag)
- **p** = Zinssatz (als Dezimalzahl: 3% = 0,03)
- **t** = Zeit in Jahren
- **Z** = Zinsen

> [!example] Einfacher Zins
> 2000 € werden zu 2,5% für 3 Jahre angelegt (ohne Zinseszins).
> $$Z = 2000 \times 0{,}025 \times 3 = 150 \text{ €}$$
> Endkapital: 2000 + 150 = 2150 €

### Zinseszins

Der Zinseszins ist eines der mächtigsten Konzepte der Finanzmathematik. Albert Einstein soll ihn als „achtes Weltwunder" bezeichnet haben.

> [!example] Beispiel
> 1000 € zu 3% für 5 Jahre
> $K_5 = 1000 \cdot 1{,}03^5 \approx 1159{,}27$ €

Bei einfachem Zins wären es nur: $1000 + 1000 × 0{,}03 × 5 = 1150$ €

Der Unterschied von 9,27 € mag gering erscheinen, aber über längere Zeiträume wird der Effekt dramatisch:

| Jahre | Einfacher Zins (3%) | Zinseszins (3%) |
|-------|--------------------|-----------------| 
| 10 | 1.300 € | 1.343,92 € |
| 20 | 1.600 € | 1.806,11 € |
| 30 | 1.900 € | 2.427,26 € |
| 40 | 2.200 € | 3.262,04 € |

> [!tip] **Die 72er-Regel**
> Eine schnelle Abschätzung, wann sich Kapital verdoppelt:
> $$\text{Verdoppelungszeit} \approx \frac{72}{\text{Zinssatz in } \%}$$
> 
> Bei 3% Zinsen: 72 ÷ 3 = 24 Jahre bis zur Verdopplung
> Bei 6% Zinsen: 72 ÷ 6 = 12 Jahre bis zur Verdopplung

---

## Mehrwertsteuer

- Netto + 19% = Brutto
- Brutto ÷ 1,19 = Netto

Die Mehrwertsteuer (MwSt.) oder Umsatzsteuer ist eine Verbrauchssteuer, die auf fast alle Waren und Dienstleistungen erhoben wird.

### Die zwei Steuersätze

| Satz | Anwendung |
|------|-----------|
| **19%** | Regelsteuersatz (die meisten Waren) |
| **7%** | Ermäßigter Satz (Lebensmittel, Bücher, ÖPNV) |

> [!example] Von Netto zu Brutto und zurück
> **Netto → Brutto** (Händler berechnet Preis für Kunden):
> - Nettobetrag: 100 €
> - MwSt. (19%): 100 × 0,19 = 19 €
> - Bruttobetrag: 100 + 19 = 119 € **oder** 100 × 1,19 = 119 €
> 
> **Brutto → Netto** (aus Kassenbon Nettopreis ermitteln):
> - Bruttobetrag: 59,50 €
> - Nettobetrag: 59,50 ÷ 1,19 = 50 €
> - MwSt.: 59,50 - 50 = 9,50 €

> [!warning] **Häufiger Fehler: 19% vom Brutto abziehen**
> ❌ Falsch: 119 € - 19% = 119 × 0,81 = 96,39 €
> ✓ Richtig: 119 € ÷ 1,19 = 100 €
> 
> 19% vom Bruttobetrag ist mehr als die enthaltene MwSt.!

---

## Gewinn und Verlust

Im kaufmännischen Bereich sind folgende Berechnungen üblich:

> [!note] Kalkulationsschema
> ```
> Einkaufspreis (netto)
> + Bezugskosten (Transport, Verpackung)
> = Bezugspreis
> + Handlungskosten (Miete, Personal, ...)
> = Selbstkosten
> + Gewinnzuschlag
> = Verkaufspreis (netto)
> + Mehrwertsteuer
> = Verkaufspreis (brutto)
> ```

> [!example] Handelskalkulation
> Ein Händler kauft Ware für 40 € (netto) ein, kalkuliert 50% Aufschlag und verkauft mit 19% MwSt.
> 
> - Einkauf: 40 €
> - Aufschlag (50%): 40 × 0,50 = 20 €
> - Verkaufspreis netto: 60 €
> - MwSt. (19%): 60 × 0,19 = 11,40 €
> - **Verkaufspreis brutto: 71,40 €**

---

## Zusammenhänge

Wirtschaftliche Berechnungen bauen auf den Grundlagen der Prozentrechnung auf:

- → [[../04-Dezimalzahlen-und-Prozentrechnung/04-Einfuehrung-in-die-Prozentrechnung|Einführung Prozentrechnung]] – Grundlagen
- → [[../04-Dezimalzahlen-und-Prozentrechnung/10-Zinsrechnung|Zinsrechnung]] – vertiefte Behandlung
- → [[../04-Dezimalzahlen-und-Prozentrechnung/11-Zinseszins-Grundlagen|Zinseszins]] – mathematische Hintergründe
- → [[09-Mathematische-Modelle|Mathematische Modelle]] – Wirtschaftsszenarien modellieren

---

**Navigation:** [[03-Technische-Berechnungen|← Technik]] | [[05-Funktionen-graphisch|Funktionen →]]
