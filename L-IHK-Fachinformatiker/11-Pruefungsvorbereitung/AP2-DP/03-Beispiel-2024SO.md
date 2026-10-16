---
title: "AP2 DP – Beispielaufgabe Sommer 2024"
created: 2026-10-13
modified: 2026-10-13
type: exercise
tags:
  - pruefung
  - ap2
  - daten-prozessanalyse
  - beispielaufgabe
  - sequenzdiagramm
source: proTirone (CC-BY-4.0)
---

# AP2 DP – Beispielaufgabe Sommer 2024

> [!info] Kontext
> Einlasskontrolle bei einer Veranstaltung mit Token-basierter Authentifizierung.

## Aufgabe 1a: Sequenzdiagramm

### Anforderung

Analysieren Sie das gegebene Sequenzdiagramm zur Token-Generierung.

> [!note] Hinweis
> Das Diagramm zeigt die Kommunikation zwischen API und Auth-Server.

---

## Aufgabe 1b: Zeiten aus Diagramm ermitteln

### Anforderung

Ergänzen Sie die fehlenden Zeiten in der Tabelle.

### Lösung

| Bezeichnung | Beschreibung | API | Auth-Server |
|-------------|--------------|-----|-------------|
| t_running | Prozess läuft | 3ms | 5ms |
| t_waiting | Prozess wartet | **5ms** | **0ms** |
| t_token | Gesamtzeit für Token-Generierung | **8ms** | **5ms** |

### Erklärung

```
API:
├── t_running = 3ms (eigene Verarbeitung)
├── t_waiting = 5ms (wartet auf Auth-Server)
└── t_token   = 3ms + 5ms = 8ms

Auth-Server:
├── t_running = 5ms (Token generieren)
├── t_waiting = 0ms (wartet auf niemanden)
└── t_token   = 5ms
```

---

## Aufgabe 1c: Kapazitätsberechnung

### Aufgabe 1ca: Wie viele Kontrollgeräte?

**Gegeben:**
- 60.000 Besucher
- 10 Eingänge
- Kontrollzeitraum: 1 Stunde (18:00 - 19:00)
- Kontrollzeit pro Person: 3 Sekunden
- Reserve: 5%

### Lösung

```
Schritt 1: Besucher pro Eingang
  60.000 ÷ 10 = 6.000 Besucher/Eingang

Schritt 2: Verfügbare Zeit in Sekunden
  1 Stunde = 3.600 Sekunden

Schritt 3: Kapazität pro Gerät
  3.600s ÷ 3s = 1.200 Personen/Gerät

Schritt 4: Geräte pro Eingang
  6.000 ÷ 1.200 = 5 Geräte/Eingang

Schritt 5: Geräte gesamt (ohne Reserve)
  5 × 10 = 50 Geräte

Schritt 6: Mit 5% Reserve
  50 + (50 × 0,05) = 50 + 2,5 = 52,5

Ergebnis: 53 Kontrollgeräte (aufgerundet)
```

> [!tip] Merke
> Bei Kapazitätsberechnungen immer **aufrunden** auf ganze Einheiten!

### Aufgabe 1cb: Skalierung

**Frage:** Wie kann die Kapazität der Auth-Server erhöht werden?

**Antwort:** Mehrere Auth-Server über einen **Loadbalancer** zu einer Kontrolleinheit verbinden.

---

## Berechnungsschema

> [!abstract] Allgemeines Schema für Kapazitätsberechnungen
> 
> ```
> 1. Gesamtmenge ÷ Anzahl Einheiten = Menge pro Einheit
> 2. Verfügbare Zeit ÷ Zeit pro Vorgang = Kapazität pro Gerät
> 3. Menge pro Einheit ÷ Kapazität = Benötigte Geräte
> 4. Benötigte Geräte × (1 + Reserve%) = Gesamtbedarf
> 5. Aufrunden auf ganze Zahl
> ```

## Lernpunkte

> [!success] Wichtige Erkenntnisse
> 1. **Sequenzdiagramme**: Laufzeiten = Pfeillängen (zeitlich)
> 2. **Wartezeit** = Zeit, die auf Antwort gewartet wird
> 3. **Kapazitätsrechnung**: Systematisch Schritt für Schritt
> 4. **Reserve einplanen**: Typisch 5-10%, dann aufrunden

## Querverweise

- → [[01-Aufgabentypen|Aufgabentypen AP2 DP]]
- → [[02-Beispiel-2023SO|Beispiel 2023 Sommer]]
- → [[../../10-Fachrichtungen/10c-Daten-Prozessanalyse/01-Prozessdokumentation/02-BPMN|BPMN]]

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (CC-BY-4.0). Originalaufgabe IHK AP2 Sommer 2024.
