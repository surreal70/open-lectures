---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - klassisch
---

# Enigma und historische Verschlüsselungsmaschinen

> [!info] **Lernziele**
> - Den Aufbau und die Funktionsweise der Enigma verstehen
> - Nachvollziehen, wie die Enigma gebrochen wurde
> - Die historische und kryptographische Bedeutung einordnen

---

## Inhalt

### Rotor-Chiffriermaschinen

Mit der Industrialisierung der Kommunikation entstanden **elektromechanische Chiffriermaschinen**. Die bekannteste ist die **Enigma**, die vom deutschen Militär im Zweiten Weltkrieg eingesetzt wurde. Sie realisiert eine sehr komplexe **polyalphabetische Substitution**, die sich mit jedem Tastendruck ändert.

### Aufbau der Enigma

Die Enigma kombiniert mehrere Komponenten:

| Komponente | Funktion |
|------------|----------|
| **Walzen (Rotoren)** | Jede realisiert eine feste Substitution; sie drehen sich bei jedem Tastendruck weiter |
| **Steckerbrett** | Vertauscht vor und nach den Walzen zusätzlich Buchstabenpaare |
| **Umkehrwalze (Reflektor)** | Leitet den Strom zurück durch die Walzen |

Durch die Rotation ändert sich das Substitutionsalphabet nach **jedem** Buchstaben. Die Zahl der möglichen Einstellungen (Walzenlage, Ringstellung, Steckerverbindungen) ging in die Größenordnung von $10^{23}$ – für damalige Verhältnisse astronomisch.

### Eine folgenreiche Schwäche

Trotz der riesigen Zahl an Einstellungen hatte die Enigma einen gravierenden Konstruktionsfehler: Durch die Umkehrwalze konnte **kein Buchstabe auf sich selbst** abgebildet werden. Diese Eigenschaft, zusammen mit vorhersehbaren Nachrichtenteilen („Cribs", z. B. Wetterberichte) und Bedienfehlern, lieferte den Codebrechern wichtige Ansatzpunkte.

### Der Bruch

- **Polen (1932):** Mathematiker um **Marian Rejewski** rekonstruierten die Verdrahtung und bauten elektromechanische „Bomby".
- **Bletchley Park:** Das britische Team um **Alan Turing** entwickelte die **Bombe**, eine Maschine, die mögliche Enigma-Einstellungen massenhaft durchtestete und dabei die Selbstabbildungs-Schwäche ausnutzte.

Das systematische Entschlüsseln (Deckname „Ultra") gilt als kriegsverkürzend und markiert die **Geburtsstunde der maschinellen Kryptoanalyse** und letztlich des Computers.

> [!note] **Lehre für die moderne Kryptographie**
> Die Enigma bestätigt Kerckhoffs' Prinzip (→ [[06-Kerckhoffs-Prinzip]]): Ein großer Schlüsselraum nützt nichts, wenn das Verfahren strukturelle Schwächen hat. Sicherheit entsteht durch sorgfältige Analyse, nicht durch bloße Komplexität.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Die Enigma ist eine Rotor-Maschine mit wechselnder polyalphabetischer Substitution
> - Riesiger Schlüsselraum ($\sim 10^{23}$), aber strukturelle Schwächen
> - Kein Buchstabe konnte auf sich selbst abgebildet werden – entscheidender Angriffspunkt
> - Gebrochen in Polen und Bletchley Park; Ursprung der maschinellen Kryptoanalyse

---

## Übungen

1. Beschreiben Sie die Rolle von Walzen, Steckerbrett und Umkehrwalze.
2. Welche Konstruktionsschwäche half beim Brechen der Enigma?
3. Warum widerlegt die Enigma die Annahme „großer Schlüsselraum = sicher"?

---

← [[03-Transpositionsverfahren|← Zurück]] | [[00-Klassisch-Index|Übersicht]] | [[05-Haeufigkeitsanalyse|Weiter →]]
