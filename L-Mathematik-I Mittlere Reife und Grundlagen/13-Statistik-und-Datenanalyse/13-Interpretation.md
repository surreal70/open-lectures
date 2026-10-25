---
title: Interpretation statistischer Daten
chapter: "13"
section: "13.13"
type: lecture
created: 2026-10-13
modified: 2026-10-25
status: final
tags:
  - mathematik/statistik
  - interpretation
  - kritik
---

# Interpretation statistischer Daten

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Statistische Darstellungen kritisch hinterfragen
> - Manipulationen erkennen
> - Daten korrekt interpretieren

Statistiken begegnen uns täglich: in Nachrichten, Werbung, Politik und Wissenschaft. Doch nicht jede Statistik ist aussagekräftig, und manche sind sogar irreführend – absichtlich oder unabsichtlich. In diesem Abschnitt lernen Sie, statistische Darstellungen kritisch zu hinterfragen.

### Historischer Hintergrund

Der britische Premierminister Benjamin Disraeli (1804–1881) soll gesagt haben: *„Es gibt drei Arten von Lügen: Lügen, verdammte Lügen und Statistiken."* Dieses Zitat (oft fälschlich Mark Twain zugeschrieben) zeigt, dass das Misstrauen gegenüber Statistiken schon lange existiert.

Das Problem ist nicht die Statistik selbst – sie ist ein wertvolles Werkzeug. Das Problem liegt in ihrer unsachgemäßen Anwendung oder absichtlichen Manipulation. Wer die Tricks kennt, kann sich schützen.

> [!tip] **Grundregel der statistischen Kompetenz**
> Nicht „Glaube keiner Statistik!" ist die richtige Haltung, sondern: **„Verstehe, was die Statistik zeigt – und was nicht."**

## Typische Manipulationen

### Achsenmanipulation

Die häufigste und wirksamste Manipulationstechnik betrifft die Achsenskalierung:

> [!warning] **Abgeschnittene y-Achse**
> Eine y-Achse, die **nicht bei 0 beginnt**, übertreibt Unterschiede optisch dramatisch.
> 
> **Beispiel:** Verkaufszahlen von 980 und 1000 Stück
> - Mit y-Achse ab 0: Die Balken sind fast gleich hoch (Unterschied kaum sichtbar)
> - Mit y-Achse ab 970: Ein Balken ist doppelt so hoch wie der andere!
> 
> Der reale Unterschied beträgt nur 2%, aber das manipulierte Diagramm suggeriert einen dramatischen Anstieg.

> [!tip] **So erkennst du die Manipulation**
> Prüfe immer: Beginnt die y-Achse bei 0? Wenn nicht, sei skeptisch und berechne den tatsächlichen prozentualen Unterschied.

### Irreführende Diagramme

Weitere Manipulationstechniken bei Diagrammen:

- **Verzerrte Proportionen:** Unterschiedlich breite Balken täuschen größere Unterschiede vor
- **3D-Effekte:** Perspektivische Darstellungen verzerren die Wahrnehmung – nähere Elemente wirken größer
- **Ungeeignete Diagrammtypen:** Ein Kreisdiagramm für Zeitverläufe oder 20 Kategorien ist unbrauchbar
- **Fehlende Beschriftungen:** Ohne Achsenbeschriftung und Einheiten ist keine Interpretation möglich
- **Unterdrückte Nulllinie:** Bei Liniendiagrammen werden kleine Schwankungen zu dramatischen „Abstürzen"

> [!example] **3D-Effekt-Problem**
> Ein 3D-Kreisdiagramm zeigt die vorderen Segmente vergrößert und die hinteren verkleinert – selbst wenn die Werte identisch sind. **Empfehlung:** Verwende immer 2D-Diagramme!

### Irreführende Formulierungen

Auch Textaussagen können irreführen:

- „8 von 10 Zahnärzten empfehlen..." – Wie wurden die Zahnärzte ausgewählt? Wurden nur Zahnärzte befragt, die das Produkt kennen?
- „Bis zu 50% günstiger!" – Das Maximum ist nicht der Regelfall
- „Die Mehrheit ist dafür" – 51% ist auch eine Mehrheit, aber keine überwältigende

## Kritische Fragen

> [!tip] **Checkliste für kritisches Lesen**
> Bei jeder Statistik solltest du folgende Fragen stellen:
> 
> 1. **Wie groß war die Stichprobe?** – 10 Befragte sind nicht repräsentativ
> 2. **Wie wurden die Daten erhoben?** – Online-Umfrage erreicht andere Menschen als Telefonbefragung
> 3. **Wer wurde befragt?** – Selbstselektion verzerrt Ergebnisse
> 4. **Beginnt die y-Achse bei 0?** – Wenn nicht: Manipulation!
> 5. **Sind die Achsen beschriftet?** – Ohne Einheiten keine Interpretation
> 6. **Was zeigt die Statistik NICHT?** – Ausgelassene Daten können wichtig sein
> 7. **Wer hat die Studie durchgeführt?** – Eine Schokoladenstudie, bezahlt von einem Schokoladenhersteller?
> 8. **Welcher Zeitraum wird betrachtet?** – Die Auswahl des Zeitraums kann Trends verstecken oder erfinden

## Korrelation ≠ Kausalität

> [!warning] **Der wichtigste Unterschied!**
> Dass zwei Dinge **zusammenhängen** (korrelieren), bedeutet **nicht**, dass eines das andere **verursacht** (Kausalität)!

Dies ist einer der häufigsten Fehlschlüsse bei der Interpretation von Statistiken.

> [!example] **Klassisches Beispiel**
> **Beobachtung:** Eisverkauf und Sonnenbrandrate steigen beide im Sommer.
> **Falsche Schlussfolgerung:** Eis verursacht Sonnenbrand.
> **Richtige Erklärung:** Beide hängen von einer dritten Variable ab – der Sonneneinstrahlung. Heißes Wetter führt zu mehr Eiskonsum UND zu mehr Sonnenbrand.

> [!example] **Weiteres Beispiel**
> **Beobachtung:** Menschen mit größeren Schuhgrößen können besser rechnen.
> **Falsche Schlussfolgerung:** Große Füße machen schlauer.
> **Richtige Erklärung:** Erwachsene haben größere Füße als Kinder UND können besser rechnen. Die Korrelation verschwindet, wenn man nur Erwachsene betrachtet.

> [!tip] **Merkregel**
> Wenn A und B zusammenhängen, gibt es vier Möglichkeiten:
> 1. A verursacht B
> 2. B verursacht A
> 3. Eine dritte Variable C verursacht A und B
> 4. Es ist Zufall (bei kleinen Stichproben)

## Fehlende Information erkennen

Oft ist das, was eine Statistik **nicht** zeigt, genauso wichtig wie das Gezeigte:

- **Absolute vs. relative Zahlen:** „100% mehr Risiko" klingt dramatisch – aber wenn das Ausgangsrisiko 0,001% war, ist das neue Risiko immer noch nur 0,002%
- **Zeitlicher Kontext:** Ein Umsatzrekord nach Jahren der Verluste ist weniger beeindruckend
- **Bezugsgruppe:** „Beliebtestes Produkt unter Testern" – aber wie viele Produkte wurden getestet?

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[05-Balkendiagramme|Balkendiagramme]] – Korrekte Darstellung
- → [[06-Kreisdiagramme|Kreisdiagramme]] – Wann geeignet, wann nicht
- → [[08-Arithmetisches-Mittel|Arithmetisches Mittel]] – Vorsicht bei Ausreißern
- → [[09-Median|Median]] – Oft aussagekräftiger als der Durchschnitt

## Zusammenfassung des Kapitels Statistik

> [!abstract] **Kapitelüberblick**
> 
> **Datenerhebung:**
> - Urliste, Strichliste, Tabellen
> - Erhebungsmethoden: Befragung, Beobachtung, Messung
> 
> **Darstellung:**
> - Balken- und Säulendiagramme (Vergleiche)
> - Kreisdiagramme (Anteile)
> - Histogramme (Verteilungen)
> 
> **Lageparameter (Wo liegt das Zentrum?):**
> - Arithmetisches Mittel (Durchschnitt)
> - Median (robuster Zentralwert)
> - Modalwert (häufigster Wert)
> 
> **Streuungsmaße (Wie stark schwanken die Daten?):**
> - Spannweite (einfach, aber grob)
> - Standardabweichung (differenziert)
> 
> **Interpretation:**
> - Kritisch und vorsichtig
> - Manipulation erkennen
> - Korrelation ≠ Kausalität

> [!warning] **Prüfungsrelevant**
> - Achsenmanipulation erkennen (y-Achse beginnt nicht bei 0)
> - Korrelation vs. Kausalität unterscheiden
> - Kritische Fragen an Statistiken stellen können
> - Wissen, wann welcher Lageparameter und welches Diagramm geeignet ist

---

**Navigation:** [[12-Standardabweichung|← Standardabweichung]] | [[../14-Wahrscheinlichkeitsrechnung/00-Wahrscheinlichkeit-Index|Wahrscheinlichkeit →]]
