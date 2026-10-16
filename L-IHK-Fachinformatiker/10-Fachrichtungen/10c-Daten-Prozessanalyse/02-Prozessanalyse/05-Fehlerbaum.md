---
title: "Fehlerbaumanalyse (FTA)"
created: 2026-10-13
modified: 2026-10-13
type: lecture
tags:
  - lf11c
  - prozessanalyse
  - fehlerbaum
  - fta
  - zuverlaessigkeit
source: proTirone (CC-BY-4.0)
---

# Fehlerbaumanalyse (FTA)

> [!info] Lernziele
> - Fehlerbaumanalyse verstehen und anwenden
> - Boolesche Logik (UND/ODER) im Fehlerbaum einsetzen
> - Ausfallwahrscheinlichkeiten berechnen

## Definition

Die **Fehlerbaumanalyse** (englisch: *Fault Tree Analysis*, FTA) ist:

- Ein Verfahren zur **Zuverlässigkeitsanalyse** technischer Systeme
- Nutzt die **boolesche Algebra** zur Berechnung
- Ist **DIN-normiert** (DIN EN 61025)
- Arbeitet „halb assoziativ" (systematisch + kreativ)

## Vorgehensweise

### Schritt 1: Systemstruktur

Zeichne die Struktur des zu begutachtenden Systems als Baum von Subsystemen.

### Schritt 2: Fehlerbaum erstellen

Für jedes Subsystem alle Zustände auflisten, die zu einem Ausfall führen können.

### Schritt 3: Ursachen verknüpfen

Sammle zu jedem Zustand die auslösenden Zustände mit logischen Verknüpfungen:

| Gatter | Symbol | Bedeutung |
|--------|--------|-----------|
| **UND** | ∧ | Alle Eingänge müssen wahr sein |
| **ODER** | ∨ | Mindestens ein Eingang muss wahr sein |

### Schritt 4: Wahrscheinlichkeiten berechnen

- Trage an jedem Blatt die Ausfallwahrscheinlichkeit ein
- Berechne die Gesamtausfallwahrscheinlichkeit

## Beispiel: Serverausfall

```
                    ┌─────────────────┐
                    │  SERVERAUSFALL  │
                    │   (Top-Event)   │
                    └────────┬────────┘
                             │
                         ┌───┴───┐
                         │  ODER │
                         └───┬───┘
              ┌──────────────┼──────────────┐
              │              │              │
        ┌─────┴─────┐  ┌─────┴─────┐  ┌─────┴─────┐
        │ Hardware- │  │ Software- │  │  Strom-   │
        │  ausfall  │  │  absturz  │  │  ausfall  │
        └─────┬─────┘  └─────┬─────┘  └─────┬─────┘
              │              │              │
          ┌───┴───┐      ┌───┴───┐          │
          │  UND  │      │ ODER  │      P = 0,01
          └───┬───┘      └───┬───┘
         ┌────┴────┐    ┌────┴────┐
         │         │    │         │
     ┌───┴───┐ ┌───┴───┐ ┌───┴───┐ ┌───┴───┐
     │ CPU   │ │ RAM   │ │Memory │ │ Bug   │
     │defekt │ │defekt │ │ Leak  │ │       │
     └───────┘ └───────┘ └───────┘ └───────┘
     P = 0,02  P = 0,03  P = 0,05  P = 0,04
```

### Berechnung

**Hardware-Ausfall (UND-Verknüpfung):**
$$P_{HW} = P_{CPU} \times P_{RAM} = 0,02 \times 0,03 = 0,0006$$

**Software-Absturz (ODER-Verknüpfung):**
$$P_{SW} = 1 - (1 - P_{Leak})(1 - P_{Bug}) = 1 - (0,95 \times 0,96) = 0,088$$

**Serverausfall (ODER-Verknüpfung):**
$$P_{total} = 1 - (1 - P_{HW})(1 - P_{SW})(1 - P_{Strom})$$
$$P_{total} = 1 - (0,9994 \times 0,912 \times 0,99) = 0,097 \approx 9,7\%$$

## Bewertung

### Vorteile

> [!success] Stärken
> - Verspricht mathematische Genauigkeit
> - Systematische Erfassung aller Fehlerursachen
> - Quantifizierbare Ergebnisse
> - DIN-normiert und etabliert

### Nachteile

> [!warning] Schwächen
> - Aufwendiges Verfahren
> - Mathematisch komplex bei großen Systemen
> - Setzt bekannte Ausfallwahrscheinlichkeiten voraus
> - Statisches Modell (keine zeitlichen Abhängigkeiten)

## Vergleich mit Ishikawa

| Aspekt | Fehlerbaum | Ishikawa |
|--------|------------|----------|
| Ansatz | Top-down (vom Fehler zur Ursache) | Assoziativ (Sammlung) |
| Logik | Boolesch (UND/ODER) | Kategorisierung |
| Quantifizierung | Wahrscheinlichkeiten | Qualitativ |
| Komplexität | Hoch | Niedrig |

## Prüfungsrelevanz

> [!question] Typische Prüfungsfragen
> - Welche logischen Verknüpfungen gibt es im Fehlerbaum?
> - Berechnen Sie die Ausfallwahrscheinlichkeit für einen gegebenen Baum
> - Unterschied zwischen UND- und ODER-Gatter?

## Querverweise

- → [[01-FMEA|FMEA]] – Alternative Risikoanalyse
- → [[03-Ishikawa|Ishikawa-Diagramm]] – Qualitative Ursachenanalyse
- → [[../04-Statistik/01-Grundlagen|Statistik-Grundlagen]] – Wahrscheinlichkeitsrechnung

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (CC-BY-4.0).
