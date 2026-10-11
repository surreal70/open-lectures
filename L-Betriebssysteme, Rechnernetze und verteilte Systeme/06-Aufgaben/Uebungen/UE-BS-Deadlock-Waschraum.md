---
author: Andreas Hümmer
title: 'Übung: Das Waschraum-Problem'
tags:
  - uebung
  - bs
  - deadlock
  - semaphore
  - synchronisation
punkte_gesamt: 20
bearbeitungszeit: 45
bereich: BS
created: '2026-10-09'
modified: '2026-10-09'
---

# Übung: Das Waschraum-Problem

**Bereich:** BS – Deadlocks und Semaphore
**Gesamtpunktzahl:** 20 Punkte
**Bearbeitungszeit:** ca. 45 Minuten

---

> [!info] **Lernziele**
> Nach dieser Übung solltest du:
> - Deadlock-Situationen in realen Szenarien erkennen können
> - Lösungen mit Semaphoren entwerfen können
> - Die Coffman-Bedingungen praktisch anwenden können
> - Pseudocode für Synchronisationsprobleme schreiben können

---

## Das Szenario

In einem Bürogebäude gibt es einen gemeinsamen **Waschraum** mit folgender Ausstattung:

- **3 Waschbecken** (zum Händewaschen)
- **2 Toilettenkabinen**
- **1 Handtuchspender** (zum Händetrocknen)

Mitarbeiter nutzen den Waschraum nach folgendem Schema:

```
1. Waschbecken belegen
2. Hände waschen
3. Handtuchspender benutzen (während Waschbecken noch belegt)
4. Hände trocknen
5. Waschbecken freigeben
6. Optional: Toilette benutzen
```

> [!warning] **Das Problem**
> Beobachten Sie: Ein Mitarbeiter hält das Waschbecken, während er auf den Handtuchspender wartet. Ein anderer hält den Handtuchspender und wartet auf ein freies Waschbecken (um seine Hände zu waschen, bevor er sie trocknet).

---

## Teil 1: Analyse (8 Punkte)

### Aufgabe 1.1: Deadlock-Erkennung (4 Punkte)

**Kann in diesem Szenario ein Deadlock entstehen?**

a) Identifizieren Sie die **Ressourcen** und ihre **Kapazitäten**. (1 Punkt)

| Ressource | Kapazität |
|-----------|-----------|
| | |
| | |
| | |

b) Beschreiben Sie ein konkretes **Deadlock-Szenario** mit mindestens zwei Mitarbeitern. (2 Punkte)

_Dein Szenario:_

<br><br><br><br>

c) Welche der **Coffman-Bedingungen** sind erfüllt? (1 Punkt)

| Bedingung | Erfüllt? | Begründung |
|-----------|:--------:|------------|
| Mutual Exclusion | ☐ Ja ☐ Nein | |
| Hold and Wait | ☐ Ja ☐ Nein | |
| No Preemption | ☐ Ja ☐ Nein | |
| Circular Wait | ☐ Ja ☐ Nein | |

---

### Aufgabe 1.2: Problem im Ablauf (4 Punkte)

Der ursprüngliche Ablauf ist problematisch:

```
1. Waschbecken belegen
2. Hände waschen
3. Handtuchspender benutzen (Waschbecken noch belegt!)  ← Problem
4. Hände trocknen
5. Waschbecken freigeben
```

a) **Warum ist "Hold and Wait" hier das Problem?** (2 Punkte)

_Dein Antwort:_

<br><br><br>

b) **Wie könnte man den Ablauf ändern, um Hold and Wait zu vermeiden?** (2 Punkte)

_Dein Antwort:_

<br><br><br>

---

## Teil 2: Lösung mit Semaphoren (12 Punkte)

### Aufgabe 2.1: Semaphore definieren (3 Punkte)

Definieren Sie die notwendigen Semaphore für eine **deadlock-freie** Lösung.

```pseudocode
// Semaphore für die Ressourcen:
Semaphore waschbecken = ???    // Wie viele?
Semaphore handtuch = ???       // Wie viele?
Semaphore toilette = ???       // Wie viele?

// Weitere Semaphore falls nötig:

```

---

### Aufgabe 2.2: Korrigierter Ablauf (5 Punkte)

Schreiben Sie den **korrigierten Ablauf** als Pseudocode mit P/V-Operationen.

**Hinweis:** Der Schlüssel liegt darin, das Waschbecken **vor** dem Handtuchspender freizugeben!

```pseudocode
void mitarbeiter_waschraum() {
    // 1. Waschbecken anfordern
    
    
    // 2. Hände waschen
    wasche_haende();
    
    // 3. Waschbecken freigeben (VOR dem Handtuch!)
    
    
    // 4. Handtuchspender anfordern
    
    
    // 5. Hände trocknen
    trockne_haende();
    
    // 6. Handtuchspender freigeben
    
    
    // 7. Optional: Toilette
    if (muss_auf_toilette) {
        
        
        benutze_toilette();
        
        
    }
}
```

---

### Aufgabe 2.3: Erklärung (4 Punkte)

a) **Warum verhindert Ihre Lösung Deadlocks?** Welche Coffman-Bedingung wird gebrochen? (2 Punkte)

_Dein Antwort:_

<br><br><br>

b) **Was wäre, wenn ein Mitarbeiter die Hände waschen UND trocknen will, während er das Waschbecken hält?** (Tipp: Denken Sie an die Ressourcen-Ordnung) (2 Punkte)

_Dein Antwort:_

<br><br><br>

---

## Bonus: Alternative Lösung (5 Punkte) ⭐⭐⭐

Eine alternative Lösung verwendet **Ressourcen-Ordnung**. Alle Ressourcen bekommen eine Nummer, und Mitarbeiter müssen sie immer in aufsteigender Reihenfolge anfordern.

**Aufgabe:** Weisen Sie den Ressourcen Nummern zu und schreiben Sie den Ablauf.

```pseudocode
// Ressourcen-Nummern:
// Toilette    = 1
// Waschbecken = 2
// Handtuch    = 3

void mitarbeiter_mit_ressourcenordnung() {
    // Alle benötigten Ressourcen in aufsteigender Reihenfolge anfordern
    
    
    
    // Aktionen durchführen
    
    
    
    // Ressourcen freigeben (Reihenfolge hier egal)
    
    
    
}
```

**Frage:** Welchen Nachteil hat diese Lösung gegenüber der Lösung aus Aufgabe 2.2?

_Dein Antwort:_

<br><br><br>

---

## Reflexion

> [!question] **Zum Nachdenken**
> 1. Gibt es in Ihrem Alltag ähnliche Situationen, in denen Deadlocks entstehen könnten?
> 2. Wie löst man das Problem in der Realität? (Tipp: Soziale Konventionen)
> 3. Warum ist der Handtuchspender ein Engpass (Bottleneck)?

---

## Quellen

- [[04-Deadlocks|Deadlocks]]
- [[05-Synchronisationsmechanismen|Synchronisationsmechanismen]]
