---
inclusion: fileMatch
fileMatchPattern: "**/L-Mathematik*/**"
---

# PNG-Grafiken für Mathematik-Vaults

Diese Regeln gelten **zusätzlich** zu den allgemeinen PNG-Regeln aus dem `create-png` Skill und überschreiben diese bei Konflikten.

## Farbschema

### Primärfarbe: Blau
- **Hauptfarbe:** `#2563EB` (mittleres Blau)
- **Dunkel:** `#1E40AF` (für Kontrast, Schatten)
- **Hell:** `#60A5FA` (für Flächen, Hervorhebungen)

### Maximal 1-3 Farben pro Grafik
- Verwende möglichst nur eine Farbe (monochrom)
- Bei Bedarf: Variationen von Blau (hell/dunkel)
- Vermeide zusätzliche Farben außer Blau-Tönen

### Hintergrund
- **Abweichend von der allgemeinen Regel:** KEIN transparenter Hintergrund
- **Stattdessen:** Mittleres bis helles Grau (`#E5E7EB` oder `#F3F4F6`)
- Dies verbessert die Lesbarkeit in beiden Obsidian-Themes

## Workflow bei Grafikerstellung

### Pflicht-Rückfrage
Vor dem Erstellen einer PNG-Grafik in einem Mathematik-Vault **MUSS** folgende Frage gestellt werden:

> "Soll die Grafik **einfarbig** (nur ein Blau-Ton) oder **mehrfarbig** (2-3 Blau-Variationen) sein?"

Erst nach Beantwortung dieser Frage wird die Grafik erstellt.

**Ausnahme (siehe Vault-spezifische Defaults unten):** Ist für den betreffenden Vault ein Standard festgelegt, entfällt die Rückfrage und der Standard wird direkt angewendet.

## Vault-spezifische Defaults

### `L-Mathematik-I Mittlere Reife und Grundlagen`
- **Standard-Farbwahl: mehrfarbig** (2–3 Blau-Variationen).
- Die oben genannte Pflicht-Rückfrage **entfällt** für diesen Vault; Grafiken werden standardmäßig mehrfarbig erstellt.
- **Begründung:** Für die didaktischen Darstellungen in diesem Grundlagen-Vault (z. B. Venn-Diagramme mit Schnitt-/Vereinigungsmengen, Flächen- und Konstruktionsskizzen) verbessern mehrere Blau-Variationen die Unterscheidbarkeit und das Verständnis deutlich. Mehrfarbig ist daher die bevorzugte, als sinnvoll bestätigte Voreinstellung.
- Abweichung bleibt möglich: Wird im Einzelfall ausdrücklich „einfarbig" gewünscht, gilt diese Einzelanweisung vor dem Default.

## Anwendungsbeispiele

### Einfarbig (empfohlen für einfache Grafiken)
- Koordinatensysteme
- Einzelne Funktionsgraphen
- Geometrische Grundformen
- Zahlenstrahl

### Mehrfarbig (für komplexere Darstellungen)
- Mehrere Funktionen im Vergleich
- Flächenberechnungen (Fläche vs. Rand)
- Konstruktionsschritte
- Vektoraddition

## Technische Umsetzung

```
Hintergrund:  #E5E7EB (helles Grau)
Linien:       #2563EB (Blau)
Flächen:      #60A5FA (helles Blau, 50% Deckkraft)
Beschriftung: #1E40AF (dunkles Blau)
```
