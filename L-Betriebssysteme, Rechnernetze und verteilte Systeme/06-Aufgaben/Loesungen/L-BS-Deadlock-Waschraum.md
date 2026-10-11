---
author: Andreas Hümmer
title: 'Lösung: Das Waschraum-Problem'
tags:
  - loesung
  - bs
  - deadlock
  - semaphore
bereich: BS
created: '2026-10-09'
modified: '2026-10-09'
---

# Lösung: Das Waschraum-Problem

**Zugehörige Übung:** [[UE-BS-Deadlock-Waschraum|Übung: Das Waschraum-Problem]]

---

## Teil 1: Analyse

### Aufgabe 1.1: Deadlock-Erkennung

**a) Ressourcen und Kapazitäten:**

> [!success] **Musterlösung**
> | Ressource | Kapazität |
> |-----------|-----------|
> | Waschbecken | 3 |
> | Handtuchspender | 1 |
> | Toilettenkabinen | 2 |

**b) Deadlock-Szenario:**

> [!success] **Musterlösung**
> **Szenario mit 4 Mitarbeitern:**
> 
> 1. **Mitarbeiter A, B, C** belegen alle 3 Waschbecken
> 2. Mitarbeiter A will den Handtuchspender → belegt ihn
> 3. Mitarbeiter B und C wollen auch den Handtuchspender → müssen warten
> 4. **Mitarbeiter D** kommt herein, will Hände waschen
> 5. D kann kein Waschbecken bekommen (alle belegt von A, B, C)
> 6. A, B, C halten Waschbecken und warten auf Handtuch
> 7. Der Handtuchspender wird von A gehalten, A benutzt ihn, gibt frei
> 8. **Aber:** Wenn A den Handtuchspender hält UND B, C warten, UND ein anderer Mitarbeiter (mit dem Handtuchspender) auf ein Waschbecken wartet...
> 
> **Konkreter Deadlock:**
> - Mitarbeiter X hält Waschbecken 1, wartet auf Handtuchspender
> - Mitarbeiter Y hatte vorher (im falschen Ablauf) den Handtuchspender genommen BEVOR er ein Waschbecken hatte, und wartet jetzt auf ein Waschbecken
> 
> **Zyklus:** X → Handtuch → Y → Waschbecken → X

**c) Coffman-Bedingungen:**

> [!success] **Musterlösung**
> | Bedingung | Erfüllt? | Begründung |
> |-----------|:--------:|------------|
> | Mutual Exclusion | ✓ Ja | Jedes Waschbecken kann nur von einer Person genutzt werden |
> | Hold and Wait | ✓ Ja | Person hält Waschbecken und wartet auf Handtuchspender |
> | No Preemption | ✓ Ja | Man kann niemandem das Waschbecken wegnehmen |
> | Circular Wait | ✓ Ja | X wartet auf Handtuch (von Y), Y wartet auf Waschbecken (von X) |
> 
> **Alle vier Bedingungen erfüllt → Deadlock möglich!**

---

### Aufgabe 1.2: Problem im Ablauf

**a) Warum ist "Hold and Wait" das Problem?**

> [!success] **Musterlösung**
> Im ursprünglichen Ablauf hält eine Person das Waschbecken **während sie auf den Handtuchspender wartet**. Das bedeutet:
> 
> - Die Person blockiert das Waschbecken für andere
> - Gleichzeitig wartet sie auf eine andere Ressource
> - Wenn alle Waschbecken so blockiert werden, kann niemand mehr ein Waschbecken bekommen
> - Wenn jemand den Handtuchspender hält und auf ein Waschbecken wartet → Zyklus → Deadlock
> 
> **Das ist die klassische "Hold and Wait"-Situation.**

**b) Ablauf ändern:**

> [!success] **Musterlösung**
> **Lösung: Waschbecken freigeben BEVOR man den Handtuchspender anfordert!**
> 
> ```
> 1. Waschbecken belegen
> 2. Hände waschen
> 3. Waschbecken freigeben  ← HIER ZUERST!
> 4. Handtuchspender anfordern
> 5. Hände trocknen
> 6. Handtuchspender freigeben
> ```
> 
> Jetzt gilt: Wenn man auf den Handtuchspender wartet, hält man kein Waschbecken mehr.
> → **Hold and Wait ist gebrochen** → Kein Deadlock möglich!

---

## Teil 2: Lösung mit Semaphoren

### Aufgabe 2.1: Semaphore definieren

> [!success] **Musterlösung**
> ```pseudocode
> // Semaphore für die Ressourcen:
> Semaphore waschbecken = 3;    // 3 Waschbecken verfügbar
> Semaphore handtuch = 1;       // 1 Handtuchspender
> Semaphore toilette = 2;       // 2 Toilettenkabinen
> ```
> 
> Counting Semaphore entsprechen genau der Anzahl verfügbarer Ressourcen.

---

### Aufgabe 2.2: Korrigierter Ablauf

> [!success] **Musterlösung**
> ```pseudocode
> void mitarbeiter_waschraum() {
>     // 1. Waschbecken anfordern
>     P(waschbecken);
>     
>     // 2. Hände waschen
>     wasche_haende();
>     
>     // 3. Waschbecken freigeben (VOR dem Handtuch!)
>     V(waschbecken);
>     
>     // 4. Handtuchspender anfordern
>     P(handtuch);
>     
>     // 5. Hände trocknen
>     trockne_haende();
>     
>     // 6. Handtuchspender freigeben
>     V(handtuch);
>     
>     // 7. Optional: Toilette
>     if (muss_auf_toilette) {
>         P(toilette);
>         benutze_toilette();
>         V(toilette);
>     }
> }
> ```
> 
> **Der entscheidende Unterschied:** `V(waschbecken)` kommt **vor** `P(handtuch)`!

---

### Aufgabe 2.3: Erklärung

**a) Warum verhindert die Lösung Deadlocks?**

> [!success] **Musterlösung**
> Die Lösung bricht die **Hold and Wait**-Bedingung:
> 
> - Wenn ein Mitarbeiter auf den Handtuchspender wartet (`P(handtuch)`), hält er **keine andere Ressource**
> - Er hat das Waschbecken bereits freigegeben
> - Daher kann kein zyklisches Warten entstehen
> 
> **Ohne Hold and Wait → Kein Deadlock möglich!**

**b) Was wenn man Waschbecken halten will während man trocknet?**

> [!success] **Musterlösung**
> Wenn der Mitarbeiter das Waschbecken während des Trocknens halten will, könnte man **Ressourcen-Ordnung** verwenden:
> 
> **Nummerierung:** Waschbecken=1, Handtuch=2
> 
> **Regel:** Immer in aufsteigender Reihenfolge anfordern!
> 
> ```pseudocode
> P(waschbecken);    // Erst 1
> P(handtuch);       // Dann 2 (nie umgekehrt!)
> wasche_haende();
> trockne_haende();
> V(handtuch);
> V(waschbecken);
> ```
> 
> Wenn ALLE Mitarbeiter diese Reihenfolge einhalten, kann kein Zyklus entstehen: Niemand, der ein Waschbecken hält, wartet auf jemanden, der "nur" den Handtuchspender hält.
> 
> **Problem:** Das Waschbecken wird länger blockiert als nötig (während des Trocknens), obwohl es nicht benutzt wird. → Geringere Effizienz.

---

## Bonus: Alternative Lösung

> [!success] **Musterlösung**
> ```pseudocode
> // Ressourcen-Nummern:
> // Toilette    = 1 (niedrigste Priorität)
> // Waschbecken = 2
> // Handtuch    = 3 (höchste Priorität)
> 
> void mitarbeiter_mit_ressourcenordnung() {
>     // Bestimme alle benötigten Ressourcen VOR dem Anfordern
>     boolean braucht_toilette = muss_auf_toilette;
>     
>     // Alle Ressourcen in aufsteigender Reihenfolge anfordern
>     if (braucht_toilette) {
>         P(toilette);        // 1 zuerst
>     }
>     P(waschbecken);         // dann 2
>     P(handtuch);            // dann 3
>     
>     // Aktionen durchführen (Reihenfolge hier egal)
>     if (braucht_toilette) {
>         benutze_toilette();
>     }
>     wasche_haende();
>     trockne_haende();
>     
>     // Ressourcen freigeben (Reihenfolge hier egal)
>     V(handtuch);
>     V(waschbecken);
>     if (braucht_toilette) {
>         V(toilette);
>     }
> }
> ```

**Nachteil gegenüber Lösung 2.2:**

> [!success] **Musterlösung**
> **Massive Ineffizienz!**
> 
> - Der Mitarbeiter muss **alle Ressourcen gleichzeitig** halten
> - Er blockiert das Waschbecken schon, während er noch auf der Toilette sitzt
> - Er blockiert den Handtuchspender, während er noch die Hände wäscht
> - Die Ressourcen sind viel länger belegt als nötig
> 
> **Vergleich:**
> - **Lösung 2.2:** Waschbecken ist nur während des Waschens belegt (~30 Sek)
> - **Ressourcen-Ordnung:** Waschbecken ist während Toilette+Waschen+Trocknen belegt (~5 Min)
> 
> Bei hoher Auslastung würde die Ressourcen-Ordnung zu langen Wartezeiten führen. Die Lösung aus 2.2 ist effizienter, weil sie Ressourcen so früh wie möglich freigibt.

---

## Zusammenfassung: Deadlock-Vermeidung

| Strategie | Umsetzung im Waschraum | Vor-/Nachteile |
|-----------|------------------------|----------------|
| **Hold and Wait brechen** | Waschbecken freigeben vor Handtuch-Anforderung | ✓ Effizient, ✗ Logik muss angepasst werden |
| **Ressourcen-Ordnung** | Alle Ressourcen in fester Reihenfolge anfordern | ✓ Einfache Regel, ✗ Sehr ineffizient |
| **Alle auf einmal anfordern** | Vor Betreten: Waschbecken UND Handtuch reservieren | ✓ Kein Hold and Wait, ✗ Wartezeit erhöht |

---

## Quellen

- [[04-Deadlocks|Deadlocks]]
- [[05-Synchronisationsmechanismen|Synchronisationsmechanismen]]
