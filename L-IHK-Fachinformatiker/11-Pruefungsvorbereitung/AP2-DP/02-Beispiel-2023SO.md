---
title: "AP2 DP – Beispielaufgabe Sommer 2023"
created: 2026-10-13
modified: 2026-10-13
type: exercise
tags:
  - pruefung
  - ap2
  - daten-prozessanalyse
  - beispielaufgabe
  - pseudocode
source: proTirone (CC-BY-4.0)
---

# AP2 DP – Beispielaufgabe Sommer 2023

> [!info] Kontext
> Auswertung einer Interessentenliste für ein Fitnessstudio.

## Aufgabe 2a: Pseudocode schreiben

### Anforderung

Schreiben Sie eine Funktion `Auswerten`, die eine Liste von Interessenten auswertet und ein Statistik-Objekt zurückgibt.

**Gegeben:**
- Klasse `Interessent` mit Attributen:
  - `DatumKontakt`
  - `DatumGespraech`
  - `DatumTraining`
  - `DatumVertrag`
- Klasse `Statistik` mit Konstruktor:
  - `Statistik(anzahlErfolg, anteilErfolg, avgDauerAbbruch)`

### Lösungsansatz (Bottom-Up)

> [!tip] Vorgehen
> 1. Funktionsheader oben hinschreiben
> 2. Return-Statement am Ende hinschreiben
> 3. Konstruktor-Parameter berechnen
> 4. Schleifen und Variablen ergänzen

### Lösung

```pseudocode
FUNKTION Auswerten(liste: Interessent[]) : Statistik

  erfolgsanzahl = 0
  misserfolgstage = 0 

  FÜR candidate IN liste:
    WENN Empty(candidate.DatumVertrag):
      // Kein Vertrag → Misserfolg
      // Finde letzten Kontaktpunkt
      lastcontact = candidate.DatumTraining
      WENN Empty(lastcontact): 
        lastcontact = candidate.DatumGespraech
      WENN Empty(lastcontact): 
        lastcontact = candidate.DatumKontakt
      
      // Tage bis Abbruch addieren
      misserfolgstage += DateDiff(candidate.DatumKontakt, lastcontact) 
    SONST:
      // Vertrag vorhanden → Erfolg
      erfolgsanzahl += 1

  // Anteil berechnen
  erfolgZuInteresse = erfolgsanzahl / liste.Length

  // Durchschnittliche Abbruchdauer
  avgAufwand = 0
  WENN liste.Length > erfolgsanzahl:  // Division by Zero vermeiden
    avgAufwand = misserfolgstage / (liste.Length - erfolgsanzahl)

  RÜCKGABE new Statistik(erfolgsanzahl, erfolgZuInteresse, avgAufwand)
```

### Wichtige Hinweise

> [!warning] Typischer Fehler
> Bei der Ermittlung des letzten Kontaktpunkts muss von hinten nach vorne geprüft werden (Training → Gespräch → Kontakt), nicht umgekehrt!

---

## Aufgabe 2b: Statistik-Aussagen bewerten

### Anforderung

Bewerten Sie die Aussagekraft der drei Statistik-Werte für die Prozessqualität.

### Lösung

| Kennzahl | Beschreibung | Aussagekraft |
|----------|--------------|--------------|
| `AnzahlErfolg` | Absolute Anzahl geschlossener Verträge | Allein keine Aussagekraft (fehlt Bezugsgröße) |
| `AnteilErfolg` | Verhältnis Verträge zu Interessenten | **Hoch**: 1 = alle wurden Kunden, 0 = keiner |
| `AvgDauerAbbruch` | Durchschnittliche Tage bis Abbruch | Gering: Misst nur „vergebene Mühe", nicht Qualität |

---

## Aufgabe 2c: Weitere Kriterien

### Anforderung

Nennen Sie weitere Kriterien zur Prozessbewertung.

### Lösung

- Quantifizierung der Qualität des Probetrainings (Kundensicht)
- Nachbefragung der Nicht-Kunden (Warum kein Vertrag?)
- Vergleich mit Branchendurchschnitt
- Entwicklung der Kennzahlen über Zeit (Trend)

---

## Lernpunkte

> [!success] Wichtige Erkenntnisse
> 1. **Pseudocode Bottom-Up** schreiben: Return zuerst, dann auffüllen
> 2. **Division by Zero** immer abfangen
> 3. **Schleifen über Listen**: `FÜR element IN liste`
> 4. **Statistische Kennzahlen** interpretieren, nicht nur berechnen

## Querverweise

- → [[01-Aufgabentypen|Aufgabentypen AP2 DP]]
- → [[03-Beispiel-2024SO|Beispiel 2024 Sommer]]
- → [[../../10-Fachrichtungen/10c-Daten-Prozessanalyse/05-Statistik/01-Grundlagen|Statistik-Grundlagen]]

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (CC-BY-4.0). Originalaufgabe IHK AP2 Sommer 2023.
