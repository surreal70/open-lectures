---
title: "Rechnen mit Dezimalzahlen"
chapter: "04"
section: "02"
type: topic
status: "draft - review pending"
learning_objectives:
  - "Dezimalzahlen addieren und subtrahieren können"
  - "Dezimalzahlen multiplizieren können"
  - "Dezimalzahlen dividieren können"
  - "Die Kommastellung bei Rechenoperationen beherrschen"
tags:
  - mathematik
  - dezimalzahlen
  - rechnen
  - grundrechenarten
created: 2026-10-13
modified: 2025-01-20
---

# Rechnen mit Dezimalzahlen

> [!info] Lernziele
> - Dezimalzahlen addieren und subtrahieren können
> - Dezimalzahlen multiplizieren können
> - Dezimalzahlen dividieren können
> - Die Kommastellung bei Rechenoperationen beherrschen

## Überblick

Die Grundrechenarten mit Dezimalzahlen folgen den bekannten Regeln, erfordern aber besondere Aufmerksamkeit bei der Kommastellung. Dieses Kapitel vermittelt die systematische Anwendung der vier Grundrechenarten.

### Warum das Komma so wichtig ist

Beim Rechnen mit Dezimalzahlen ist die korrekte Platzierung des Kommas entscheidend. Ein falsch gesetztes Komma kann das Ergebnis um den Faktor 10, 100 oder mehr verfälschen. In der Praxis kann das gravierende Folgen haben – etwa wenn bei einer Medikamentendosierung 0,5 mg statt 5 mg berechnet wird, oder wenn eine Rechnung 150,00 € statt 15,00 € beträgt.

Die gute Nachricht: Die Regeln sind logisch und konsistent. Wer sie einmal verstanden hat, kann sicher mit Dezimalzahlen rechnen.

## Addition und Subtraktion

### Grundregel

> [!tip] Wichtig
> Bei Addition und Subtraktion müssen die Kommas **untereinander** stehen!

### Schriftliche Addition

**Beispiel:** 12,45 + 3,7 + 0,125

```
   12,450
    3,700
+   0,125
─────────
   16,275
```

**Schritte:**
1. Zahlen untereinander schreiben (Komma unter Komma)
2. Fehlende Stellen mit Nullen auffüllen
3. Von rechts nach links addieren

### Schriftliche Subtraktion

**Beispiel:** 25,3 − 8,47

```
   25,30
−   8,47
────────
   16,83
```

### Häufige Fehler vermeiden

| Falsch | Richtig |
|--------|---------|
| 12,45 + 3,7 = 12,82 | 12,45 + 3,70 = 16,15 |
| Kommas nicht ausgerichtet | Kommas untereinander |

> [!warning] **Häufiger Fehler: Stellen verwechseln**
> Bei der Addition 12,45 + 3,7 schreiben manche:
> ```
>    12,45
> +   3,7
> ────────
>    12,82  ✗ FALSCH!
> ```
> Das Problem: Die 7 wurde zu den Hundertsteln addiert statt zu den Zehnteln.
> 
> **Richtig:** Erst auf gleiche Stellenzahl bringen:
> ```
>    12,45
> +   3,70
> ────────
>    16,15  ✓ RICHTIG!
> ```

> [!tip] **Praktischer Tipp**
> Schreibe immer zuerst alle Zahlen untereinander, mit dem Komma exakt ausgerichtet. Fülle dann fehlende Stellen mit Nullen auf, bevor du zu rechnen beginnst.

## Multiplikation

### Grundregel

> [!tip] Kommaregel bei Multiplikation
> Die Anzahl der Nachkommastellen im Ergebnis = Summe der Nachkommastellen beider Faktoren

### Warum funktioniert diese Regel?

Die Regel hat einen einfachen mathematischen Hintergrund: Wenn wir z.B. 2,5 × 1,4 rechnen, können wir das so verstehen:
- 2,5 = 25 Zehntel = 25/10
- 1,4 = 14 Zehntel = 14/10
- Also: (25/10) × (14/10) = 350/100 = 3,50

Wir multiplizieren die Zahlen ohne Komma (25 × 14 = 350) und teilen dann durch so viele Zehnerpotenzen, wie wir Nachkommastellen hatten (10 × 10 = 100, also 2 Stellen).

### Beispiel 1: Dezimalzahl × Dezimalzahl

**Berechne:** 2,5 × 1,4

```
    25 × 14 = 350
    
    2,5  → 1 Nachkommastelle
  × 1,4  → 1 Nachkommastelle
  ─────
    3,50 → 2 Nachkommastellen
```

**Ergebnis:** 2,5 × 1,4 = 3,5

### Beispiel 2: Mehrere Nachkommastellen

**Berechne:** 3,25 × 0,4

```
    325 × 4 = 1300
    
    3,25 → 2 Nachkommastellen
  × 0,4  → 1 Nachkommastelle
  ─────
    1,300 → 3 Nachkommastellen
```

**Ergebnis:** 3,25 × 0,4 = 1,3

### Multiplikation mit Zehnerpotenzen

Das Verschieben des Kommas bei Multiplikation/Division mit Zehnerpotenzen ist einer der praktischsten Rechentricks überhaupt. In der Wissenschaft, Technik und im Alltag (z.B. beim Umrechnen von Einheiten) wird er ständig angewendet.

| Operation | Regel | Beispiel |
|-----------|-------|----------|
| × 10 | Komma 1 Stelle nach rechts | 2,34 × 10 = 23,4 |
| × 100 | Komma 2 Stellen nach rechts | 2,34 × 100 = 234 |
| × 1000 | Komma 3 Stellen nach rechts | 2,34 × 1000 = 2340 |
| × 0,1 | Komma 1 Stelle nach links | 2,34 × 0,1 = 0,234 |
| × 0,01 | Komma 2 Stellen nach links | 2,34 × 0,01 = 0,0234 |

> [!tip] **Merkregel: Größer oder kleiner?**
> - Multiplizieren mit Zahlen > 1: Das Ergebnis wird **größer** → Komma nach rechts
> - Multiplizieren mit Zahlen < 1: Das Ergebnis wird **kleiner** → Komma nach links
> 
> Diese Überlegung hilft auch zur Kontrolle: Wenn du 5,2 × 0,1 rechnest und 52 herausbekommst, stimmt etwas nicht – das Ergebnis müsste kleiner als 5,2 sein!

## Division

### Grundregel

> [!tip] Division durch Dezimalzahlen
> Den Divisor zur ganzen Zahl machen, indem man bei Dividend und Divisor das Komma um die gleiche Stellenzahl verschiebt.

### Beispiel 1: Dezimalzahl ÷ ganze Zahl

**Berechne:** 15,6 ÷ 4

```
    15,6 ÷ 4 = ?
    
    15 ÷ 4 = 3 Rest 3
    36 ÷ 4 = 9
    
    Ergebnis: 3,9
```

### Beispiel 2: Dezimalzahl ÷ Dezimalzahl

**Berechne:** 7,2 ÷ 0,3

**Schritt 1:** Divisor zur ganzen Zahl machen
```
    7,2 ÷ 0,3 = 72 ÷ 3  (beide × 10)
```

**Schritt 2:** Division ausführen
```
    72 ÷ 3 = 24
```

**Ergebnis:** 7,2 ÷ 0,3 = 24

### Division durch Zehnerpotenzen

| Operation | Regel | Beispiel |
|-----------|-------|----------|
| ÷ 10 | Komma 1 Stelle nach links | 23,4 ÷ 10 = 2,34 |
| ÷ 100 | Komma 2 Stellen nach links | 234 ÷ 100 = 2,34 |
| ÷ 1000 | Komma 3 Stellen nach links | 2340 ÷ 1000 = 2,34 |
| ÷ 0,1 | Komma 1 Stelle nach rechts | 2,34 ÷ 0,1 = 23,4 |
| ÷ 0,01 | Komma 2 Stellen nach rechts | 2,34 ÷ 0,01 = 234 |

## Überschlagsrechnung

### Warum Überschlagen?

- Kontrolle der Ergebnisse
- Schnelle Schätzung im Alltag
- Erkennen von Eingabefehlern beim Taschenrechner

Im Zeitalter von Taschenrechnern und Computern mag Überschlagsrechnung überflüssig erscheinen – doch das Gegenteil ist der Fall. Gerade weil wir Ergebnisse oft nicht mehr selbst nachrechnen, ist es umso wichtiger, Fehler erkennen zu können. Ein vertippter Wert oder ein falsch gesetztes Komma fällt nur auf, wenn wir eine ungefähre Vorstellung vom erwarteten Ergebnis haben.

### Methode

1. Zahlen auf "runde" Werte runden
2. Kopfrechnung durchführen
3. Mit exaktem Ergebnis vergleichen

### Beispiel

**Berechne:** 4,87 × 2,13

**Überschlag:** 5 × 2 = 10

**Exakt:** 4,87 × 2,13 = 10,3731

**Kontrolle:** 10,37 ≈ 10 ✓

> [!tip] **Überschlag im Alltag**
> Im Supermarkt kannst du mit Überschlagsrechnung schnell prüfen, ob du genug Geld dabei hast:
> - 3,49 € ≈ 3,50 €
> - 2,99 € ≈ 3,00 €
> - 4,79 € ≈ 5,00 €
> - **Summe:** ca. 11,50 € – passt ein 20-€-Schein? Ja, mit Reserve!

## Rechengesetze

Alle bekannten Rechengesetze gelten auch für Dezimalzahlen:

### Kommutativgesetz
- Addition: a + b = b + a → 2,5 + 1,3 = 1,3 + 2,5
- Multiplikation: a × b = b × a → 2,5 × 1,4 = 1,4 × 2,5

### Assoziativgesetz
- Addition: (a + b) + c = a + (b + c)
- Multiplikation: (a × b) × c = a × (b × c)

### Distributivgesetz
- a × (b + c) = a × b + a × c
- **Beispiel:** 2,5 × 4,2 = 2,5 × 4 + 2,5 × 0,2 = 10 + 0,5 = 10,5

## Zusammenhänge

### Beziehung zu anderen Themen

- **Bruchrechnung:** Division entspricht dem Bruch (15 ÷ 4 = 15/4)
- **Prozentrechnung:** Prozente werden als Dezimalzahlen multipliziert
- **Taschenrechnernutzung:** Verständnis der Kommaregeln zur Kontrolle

### Voraussetzungen

- [[01-Dezimalzahlen]] - Grundverständnis Dezimalzahlen
- [[02-Grundrechenarten-und-Rechengesetze/00-Grundrechenarten-Index|Grundrechenarten]]

## Prüfungsrelevanz

> [!warning] Prüfungsrelevanz: Sehr hoch
> Sicheres Rechnen mit Dezimalzahlen ist Grundvoraussetzung für die gesamte Prozentrechnung und alle kaufmännischen Aufgaben.

## Typische Prüfungsfragen

1. **Addition:** Berechne 12,456 + 3,78 + 0,9
2. **Multiplikation:** Berechne 2,4 × 0,35
3. **Division:** Berechne 8,4 ÷ 0,12
4. **Textaufgabe:** Ein Stoff kostet 12,50 € pro Meter. Wie viel kosten 2,4 m?
5. **Überschlag:** Schätze das Ergebnis von 4,97 × 3,02 und berechne dann exakt.

## Quellen

- Lambacher Schweizer Mathematik 6
- Schulbuch Mathematik Realschule Bayern

## Weiterführende Links

- [[03-Rundungsregeln]] - Runden der Ergebnisse
- [[04-Einfuehrung-in-die-Prozentrechnung]] - Anwendung in der Prozentrechnung
