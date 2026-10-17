---
author: Andreas Hümmer
title: Interpretation statistischer Ergebnisse
tags:
  - content
  - mathe
  - statistik
  - interpretation
  - signifikanz
  - kommunikation
created: 2025-06-26
modified: 2025-06-26
---

# Interpretation statistischer Ergebnisse

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Statistische Ergebnisse korrekt interpretieren und kommunizieren können
> - Typische Fehlinterpretationen erkennen und vermeiden können
> - Zwischen statistischer und praktischer Signifikanz unterscheiden können
> - Statistische Aussagen in den Medien kritisch bewerten können

---

## Überblick

Statistische Ergebnisse sind nur dann wertvoll, wenn sie korrekt interpretiert und kommuniziert werden. Leider führen Missverständnisse über statistische Konzepte häufig zu Fehlschlüssen – sowohl in wissenschaftlichen Arbeiten als auch in der öffentlichen Berichterstattung. Dieses Kapitel behandelt die korrekte Interpretation und häufige Fehler.

---

## Korrekte Interpretation von Testergebnissen

### Was bedeutet „signifikant"?

**Korrekt:** „Die Daten sind mit der Nullhypothese nicht gut vereinbar. Unter der Annahme, dass $H_0$ wahr ist, wäre ein solches oder extremeres Ergebnis sehr unwahrscheinlich."

**Falsch:** „Die Nullhypothese ist widerlegt" oder „Die Alternativhypothese ist bewiesen"

### Was bedeutet „nicht signifikant"?

**Korrekt:** „Die Daten liefern keine ausreichende Evidenz gegen $H_0$. Wir können $H_0$ nicht verwerfen."

**Falsch:** „$H_0$ ist wahr" oder „Es gibt keinen Effekt"

> [!warning] **Wichtiger Unterschied**
> „Kein Beweis für einen Effekt" ≠ „Beweis für keinen Effekt"
> 
> Absence of evidence is not evidence of absence.

---

## Häufige Fehlinterpretationen

### Fehler 1: p-Wert als Wahrscheinlichkeit für $H_0$

**Falsch:** „Der p-Wert von 0,03 bedeutet, dass $H_0$ nur mit 3% Wahrscheinlichkeit wahr ist."

**Richtig:** „Wenn $H_0$ wahr wäre, würde man in 3% der Fälle ein solches oder extremeres Ergebnis beobachten."

Der p-Wert sagt nichts darüber aus, wie wahrscheinlich $H_0$ ist!

### Fehler 2: Konfidenzintervall als Aufenthaltsort des Parameters

**Falsch:** „Der wahre Parameter liegt mit 95% Wahrscheinlichkeit im Intervall [0,42; 0,58]."

**Richtig:** „Wenn wir dieses Verfahren oft wiederholen, enthalten 95% der so konstruierten Intervalle den wahren Parameter."

Der Parameter ist eine feste (unbekannte) Zahl – er „bewegt" sich nicht.

### Fehler 3: Signifikanz mit Wichtigkeit verwechseln

**Falsch:** „Der Unterschied ist hochsignifikant, also ist er auch wichtig."

**Richtig:** Signifikanz sagt nur, dass ein Effekt existiert, nicht wie groß oder wichtig er ist.

**Beispiel:** Eine Studie mit 100.000 Teilnehmern könnte zeigen, dass Medikament A den Blutdruck um 0,5 mmHg mehr senkt als B. Statistisch signifikant, aber klinisch irrelevant.

### Fehler 4: Korrelation mit Kausalität verwechseln

**Falsch:** „Die Studie zeigt, dass Fernsehen dumm macht."

**Richtig:** „Die Studie zeigt einen Zusammenhang zwischen TV-Konsum und Testergebnissen. Die Ursache-Wirkungs-Beziehung ist unklar."

Mögliche Erklärungen:
- TV → schlechtere Leistung (Kausalität)
- Schlechtere Leistung → mehr TV (umgekehrte Kausalität)
- Dritte Variable (z.B. sozioökonomischer Status) beeinflusst beides

---

## Effektgröße und praktische Signifikanz

### Was ist die Effektgröße?

Die **Effektgröße** quantifiziert die Stärke eines Effekts unabhängig vom Stichprobenumfang.

**Cohens d** für Mittelwertvergleiche:
$$d = \frac{\bar{x}_1 - \bar{x}_2}{s}$$

| Effektgröße $d$ | Interpretation |
|-----------------|----------------|
| $\lvert d \rvert < 0{,}2$ | Kleiner Effekt |
| $0{,}2 \leq \lvert d \rvert < 0{,}8$ | Mittlerer Effekt |
| $\lvert d \rvert \geq 0{,}8$ | Großer Effekt |

### Praktische vs. statistische Signifikanz

| | Statistische Signifikanz | Praktische Signifikanz |
|-|--------------------------|------------------------|
| **Frage** | Ist der Effekt real (nicht zufällig)? | Ist der Effekt bedeutsam? |
| **Abhängig von** | Stichprobenumfang, Streuung, $\alpha$ | Kontext, Kosten, Konsequenzen |
| **Große Stichprobe** | Auch kleine Effekte werden signifikant | Kleine Effekte bleiben unwichtig |

---

## Kommunikation statistischer Ergebnisse

### Richtige Formulierungen

| Situation | Empfohlene Formulierung |
|-----------|------------------------|
| $H_0$ abgelehnt | „Die Daten sprechen für $H_1$" / „Der Effekt ist statistisch signifikant" |
| $H_0$ nicht abgelehnt | „Die Daten liefern keine ausreichende Evidenz gegen $H_0$" |
| Konfidenzintervall | „Wir sind zu 95% konfident, dass der wahre Wert im Intervall liegt" |
| Korrelation | „Es besteht ein Zusammenhang zwischen X und Y" (nicht: „X verursacht Y") |

### Beispiel: Medikamentenstudie

**Rohdaten:** 
- Kontrollgruppe: 45 von 100 genesen (45%)
- Behandlungsgruppe: 56 von 100 genesen (56%)
- p-Wert = 0,043

**Schlechte Kommunikation:**
„Das neue Medikament heilt signifikant mehr Patienten. Die Nullhypothese wurde widerlegt."

**Gute Kommunikation:**
„In der behandelten Gruppe genasen 56% der Patienten im Vergleich zu 45% in der Kontrollgruppe. Dieser Unterschied ist statistisch signifikant (p = 0,043). Die absolute Risikoreduktion beträgt 11 Prozentpunkte. Um einen zusätzlichen Patienten zu heilen, müssten etwa 9 Patienten behandelt werden (NNT = 9)."

---

## Kritische Bewertung von Statistiken

### Checkliste für statistische Aussagen

1. **Stichprobe:** Wie wurde sie ausgewählt? Ist sie repräsentativ?
2. **Größe:** Wie groß ist $n$? Kleine Stichproben sind unzuverlässiger.
3. **Signifikanzniveau:** Wurde $\alpha$ vorab festgelegt?
4. **Effektgröße:** Wie groß ist der Effekt tatsächlich?
5. **Konfidenzintervall:** Wie präzise ist die Schätzung?
6. **Kausalität:** Wird aus Korrelation auf Ursache geschlossen?
7. **Interessenkonflikte:** Wer hat die Studie finanziert?

### Warnsignale

- „Studie beweist..." (Statistik beweist nichts, sie liefert Evidenz)
- Keine Angabe von Konfidenzintervallen oder Effektgrößen
- Sehr kleine Stichproben bei weitreichenden Behauptungen
- Keine Angabe zum Studiendesign
- „Experten sagen..." ohne Quellenangabe

---

## Beispiel: Zeitungsmeldung analysieren

### Meldung

> „Neue Studie: Kaffeetrinker leben länger! Wer täglich Kaffee trinkt, hat ein um 12% geringeres Sterberisiko, zeigt eine Untersuchung mit 500.000 Teilnehmern."

### Kritische Analyse

**Was ist unklar?**
- Studiendesign (Beobachtungsstudie oder Experiment?)
- Konfidenzintervall für die 12%
- Mögliche Störfaktoren (Confounder)
- Absolute Risikoreduktion
- Definition von „Kaffeetrinker"

**Mögliche Probleme:**
- Korrelation ≠ Kausalität (gesündere Menschen trinken vielleicht auch mehr Kaffee)
- Selektionsbias (wer nimmt an solchen Studien teil?)
- 12% relative Risikoreduktion klingt viel, könnte aber absolut klein sein

**Bessere Interpretation:**
„Eine Beobachtungsstudie zeigt einen statistischen Zusammenhang zwischen Kaffeekonsum und geringerer Sterblichkeit. Ob Kaffee tatsächlich lebensverlängernd wirkt oder andere Faktoren verantwortlich sind, kann die Studie nicht klären."

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Signifikanzniveau]] – Was statistische Signifikanz bedeutet
- → [[Fehler-erster-und-zweiter-Art]] – Mögliche Fehlentscheidungen
- → [[Konfidenzintervalle-Grundlagen]] – Korrekte Interpretation von Intervallen
- → [[Korrelation-und-Regression-Grundlagen]] – Zusammenhang vs. Kausalität
- → [[Stichproben]] – Repräsentativität und Verzerrung

> [!warning] **Prüfungsrelevant**
> - Korrekte Formulierung von Testergebnissen
> - Unterscheidung „$H_0$ nicht abgelehnt" vs. „$H_0$ bewiesen"
> - p-Wert ist NICHT die Wahrscheinlichkeit für $H_0$
> - Statistische Signifikanz sagt nichts über praktische Relevanz
> - Korrelation impliziert keine Kausalität
> - Kritische Bewertung statistischer Aussagen in Sachzusammenhängen

> [!question] **Typische Prüfungsfragen**
> - Eine Studie zeigt, dass ein Zusammenhang zwischen X und Y besteht (p = 0,02). Kann man daraus schließen, dass X die Ursache von Y ist? Begründe.
> - Der p-Wert eines Tests beträgt 0,04. Ist die Aussage „$H_0$ ist mit 96% Wahrscheinlichkeit falsch" korrekt? Erkläre.
> - In einer Studie mit 50.000 Teilnehmern wurde ein hochsignifikanter Unterschied von 0,5 Punkten auf einer Zufriedenheitsskala gefunden. Bewerte dieses Ergebnis.

---

## Quellen

- Fahrmeir, L. et al.: Statistik – Der Weg zur Datenanalyse. Springer, 2016.
- Gigerenzer, G.: Das Einmaleins der Skepsis – Über den richtigen Umgang mit Zahlen und Risiken. Berlin Verlag, 2002.
- ISB Bayern: Abiturprüfungen Mathematik.

> [!tip] **Weiterführende Links**
> - [[Korrelation-und-Regression-Grundlagen]] – Mehr zu Zusammenhängen zwischen Variablen
> - [[Glossar]] – Definitionen statistischer Fachbegriffe
