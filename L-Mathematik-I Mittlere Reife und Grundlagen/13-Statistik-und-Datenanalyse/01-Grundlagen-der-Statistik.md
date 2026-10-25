---
title: Grundlagen der Statistik
chapter: "13"
section: "13.1"
type: lecture
created: 2026-10-13
modified: 2026-10-25
status: final
tags:
  - mathematik/statistik
  - grundlagen
---

# Grundlagen der Statistik

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Erklären, was Statistik ist und wozu sie dient
> - Grundbegriffe der Statistik anwenden
> - Zwischen verschiedenen Merkmalsarten unterscheiden

## Was ist Statistik?

> [!note] Definition
> **Statistik** ist die Wissenschaft vom Sammeln, Ordnen, Darstellen und Auswerten von Daten.

Das Wort „Statistik" leitet sich vom lateinischen *status* (Zustand) ab. Ursprünglich bezeichnete es die systematische Erfassung von Staatsdaten – daher auch der Begriff „Staatskunde". Heute ist Statistik jedoch weit mehr: Sie ist ein unverzichtbares Werkzeug in Wissenschaft, Wirtschaft und Alltag.

### Historischer Hintergrund

Die Geschichte der Statistik reicht weit zurück. Schon die alten Ägypter führten um 3000 v. Chr. Volkszählungen durch, um Steuern und Arbeitskräfte für den Pyramidenbau zu planen. Im Römischen Reich gab es regelmäßige Zensus (von lat. *censere* = schätzen), die alle Bürger und ihren Besitz erfassten.

Die moderne Statistik als mathematische Wissenschaft entstand jedoch erst im 17. Jahrhundert. John Graunt (1620–1674) gilt als einer der Begründer: Er analysierte Londoner Sterberegister und entdeckte Muster in Geburts- und Sterberaten. Der belgische Mathematiker Adolphe Quetelet (1796–1874) führte den Begriff des „Durchschnittsmenschen" ein und zeigte, dass gesellschaftliche Phänomene statistischen Gesetzmäßigkeiten folgen.

> [!tip] **Statistik als Kulturtechnik**
> In unserer datengetriebenen Welt ist statistische Kompetenz so wichtig wie Lesen und Schreiben. Wer Statistiken versteht, kann Nachrichten kritisch einordnen, Werbung hinterfragen und fundierte Entscheidungen treffen.

### Anwendungsgebiete

Statistik begegnet uns in nahezu allen Lebensbereichen:

- **Wirtschaft**: Umsatzanalysen, Marktforschung, Qualitätskontrolle in der Produktion
- **Medizin**: Wirksamkeitsstudien für Medikamente, Epidemiologie (z.B. Corona-Inzidenzen)
- **Sport**: Spielerstatistiken, Leistungsanalysen, Ranglisten und Quoten
- **Politik**: Wahlprognosen, Meinungsumfragen, Bevölkerungsstatistik
- **Schule**: Notenauswertungen, Klassenspiegel, Bildungsstudien (PISA)
- **Alltag**: Wetterbericht (Regenwahrscheinlichkeit), Produktbewertungen, Versicherungstarife

## Grundbegriffe

### Grundgesamtheit und Stichprobe

Ein zentrales Konzept der Statistik ist die Unterscheidung zwischen der Gesamtheit aller interessierenden Objekte und einer ausgewählten Teilmenge daraus.

| Begriff | Bedeutung | Beispiel |
|---------|-----------|----------|
| **Grundgesamtheit** | Alle zu untersuchenden Objekte | Alle Schüler Deutschlands |
| **Stichprobe** | Ausgewählte Teilmenge | 500 befragte Schüler |

In der Praxis ist es oft unmöglich oder zu teuer, die gesamte Grundgesamtheit zu untersuchen. Stattdessen zieht man eine **repräsentative Stichprobe** – eine Teilmenge, die die Eigenschaften der Grundgesamtheit widerspiegelt. Die Kunst besteht darin, die Stichprobe so zu wählen, dass man von ihr zuverlässig auf die Grundgesamtheit schließen kann.

> [!warning] **Häufiger Fehler: Verzerrte Stichproben**
> Eine Stichprobe ist **nicht repräsentativ**, wenn bestimmte Gruppen über- oder unterrepräsentiert sind.
> 
> Beispiel: Eine Online-Umfrage zur Internetnutzung erreicht nur Menschen, die ohnehin online sind – ältere Menschen ohne Internetzugang werden systematisch ausgeschlossen.

### Merkmale und Merkmalsausprägungen

> [!note] Definition
> Ein **Merkmal** ist eine Eigenschaft, die untersucht wird.
> Die **Merkmalsausprägungen** sind die möglichen Werte.

Merkmale sind die Eigenschaften, die wir an den untersuchten Objekten (den „statistischen Einheiten") erfassen. Jedes Merkmal kann verschiedene Ausprägungen annehmen.

> [!example] Beispiele
> | Merkmal | Merkmalsausprägungen | Art |
> |---------|---------------------|-----|
> | Augenfarbe | blau, grün, braun | qualitativ |
> | Schulnote | 1, 2, 3, 4, 5, 6 | qualitativ (ordinal) |
> | Körpergröße | 150 cm, 175 cm, ... | quantitativ |
> | Anzahl Geschwister | 0, 1, 2, 3, ... | quantitativ |

## Merkmalsarten

Die Unterscheidung verschiedener Merkmalsarten ist wichtig, weil sie bestimmt, welche statistischen Methoden anwendbar sind.

### Qualitative Merkmale

Qualitative Merkmale beschreiben Eigenschaften, die nicht durch Zahlen gemessen werden:

- **Nominal:** Keine natürliche Rangordnung vorhanden
  - Beispiele: Geschlecht, Lieblingsfarbe, Nationalität, Blutgruppe
  - Man kann nur feststellen, ob zwei Werte gleich oder verschieden sind
  
- **Ordinal:** Mit natürlicher Rangordnung
  - Beispiele: Schulnoten, Zufriedenheitsstufen (sehr gut/gut/befriedigend), Platzierungen
  - Man kann Werte nach „größer/kleiner" oder „besser/schlechter" ordnen
  - Die Abstände zwischen den Stufen sind jedoch nicht gleich

> [!tip] **Merkregel**
> **Nominal** = nur **N**amen (keine Ordnung)
> **Ordinal** = **O**rdnung möglich

### Quantitative Merkmale

Quantitative Merkmale werden durch Zahlenwerte ausgedrückt:

- **Diskret:** Nur bestimmte, abzählbare Werte möglich
  - Beispiele: Anzahl Geschwister, Würfelaugen, Tore in einem Spiel
  - Zwischen zwei aufeinanderfolgenden Werten gibt es keine weiteren Werte
  
- **Stetig:** Theoretisch jeder Wert in einem Intervall möglich
  - Beispiele: Körpergröße, Gewicht, Temperatur, Zeit
  - Messwerte sind nur durch die Genauigkeit des Messgeräts begrenzt

> [!example] **Anschauliche Unterscheidung**
> - **Diskret**: Wie viele Äpfel hast du? → 0, 1, 2, 3, ... (keine halben Äpfel)
> - **Stetig**: Wie schwer ist der Apfel? → 150,3 g, 150,31 g, 150,312 g, ...

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[02-Datenerhebung|Datenerhebung]] – Wie man Daten systematisch sammelt
- → [[04-Absolute-und-relative-Haeufigkeiten|Häufigkeiten]] – Wie oft kommt etwas vor?
- → [[08-Arithmetisches-Mittel|Arithmetisches Mittel]] – Durchschnitt als Lagemaß
- → [[../14-Wahrscheinlichkeitsrechnung/04-Haeufigkeit-und-Wahrscheinlichkeit|Häufigkeit und Wahrscheinlichkeit]] – Verbindung zur Wahrscheinlichkeitsrechnung

## Zusammenfassung

> [!abstract] Kernpunkte
> - Statistik = Daten sammeln, ordnen, darstellen, auswerten
> - Grundgesamtheit vs. Stichprobe (repräsentativ!)
> - Qualitative Merkmale: nominal (keine Ordnung) oder ordinal (mit Rangfolge)
> - Quantitative Merkmale: diskret (abzählbar) oder stetig (messbar)

> [!warning] **Prüfungsrelevant**
> - Definition von Statistik und ihre vier Aufgaben
> - Unterschied Grundgesamtheit und Stichprobe
> - Einordnung von Merkmalen (qualitativ/quantitativ, nominal/ordinal/diskret/stetig)

---

**Navigation:** [[00-Statistik-Index|← Übersicht]] | [[02-Datenerhebung|Datenerhebung →]]
