# Enhancement-Plan: Moderat-Stil für Mathematik I

Dieses Dokument beschreibt den Plan zur Erweiterung aller Kapitel (02–15) mit kontextbasiertem Text im **Moderat-Stil**.

---

## Referenz: Der Moderat-Stil (aus Kapitel 01)

Der Moderat-Stil fügt ca. 50% mehr erklärenden Text hinzu und umfasst:

- **Historischer Kontext**: Wer hat es entwickelt/entdeckt, wann, warum?
- **Alltagsbezug**: Reale Anwendungen, wo begegnet das im Leben?
- **Konzeptuelle "Warum"-Erklärungen**: Warum funktioniert das so? Intuition vermitteln
- **Häufige Fehler**: `[!warning] Häufiger Fehler` Callout für typische Stolpersteine
- **Merkregeln/Memory Aids**: `[!tip]` Callout für Eselsbrücken und Merkhilfen
- **Anschauliche Beschreibungen**: Bildhafte, intuitive Erklärungen
- **Querverweise**: Wiki-Links zu verwandten Themen `[[...]]`

**Was unverändert bleibt:**
- YAML-Frontmatter
- Sektionsstruktur (Überschriften)
- Bestehende Callouts
- LaTeX-Mathematik
- Tabellen

---

## Kapitel 02: Grundrechenarten und Rechengesetze

**Pfad:** `/media/andhue/Wissen/open-lectures/L-Mathematik-I Mittlere Reife und Grundlagen/02-Grundrechenarten-und-Rechengesetze`

**Dateien (12 Content-Dateien):**
- `01-Addition.md`
- `02-Subtraktion.md`
- `03-Multiplikation.md`
- `04-Division.md`
- `05-Kommutativgesetz.md`
- `06-Assoziativgesetz.md`
- `07-Distributivgesetz.md`
- `08-Punkt-vor-Strich.md`
- `09-Reihenfolge-der-Operationen.md`
- `10-Klammerregeln.md`
- `11-Ueberschlagsrechnung.md`
- `12-Plausibilitaetspruefungen.md`

**Enhancement-Schwerpunkte:**
1. **Historische Ursprünge**: Entwicklung der Rechenzeichen (+, -, ×, ÷) – wann und durch wen wurden sie eingeführt? (z.B. Robert Recorde für =, 1557)
2. **Alltagsbeispiele**: Supermarkt-Situationen für Addition/Subtraktion, Rezepte verdoppeln/halbieren für Multiplikation/Division
3. **Die drei Rechengesetze**: Anschauliche Erklärungen mit konkreten Beispielen – warum funktioniert Kommutativität bei Multiplikation, aber nicht bei Division?
4. **Typische Fehlerquellen**: Division durch Null, Vorzeichenfehler, "Punkt vor Strich"-Verstöße

---

## Kapitel 03: Bruchrechnung

**Pfad:** `/media/andhue/Wissen/open-lectures/L-Mathematik-I Mittlere Reife und Grundlagen/03-Bruchrechnung`

**Dateien (12 Content-Dateien):**
- `01-Grundlagen-der-Brueche.md`
- `02-Echte-und-unechte-Brueche.md`
- `03-Gemischte-Zahlen.md`
- `04-Brueche-erweitern.md`
- `05-Brueche-kuerzen.md`
- `06-Hauptnenner-bestimmen.md`
- `07-Addition-von-Bruechen.md`
- `08-Subtraktion-von-Bruechen.md`
- `09-Multiplikation-von-Bruechen.md`
- `10-Division-von-Bruechen.md`
- `11-Umwandlung-Brueche-Dezimalzahlen.md`
- `12-Anwendungsaufgaben.md`

**Enhancement-Schwerpunkte:**
1. **Historische Ursprünge**: Ägyptische Brüche (nur Stammbrüche), babylonisches Sexagesimalsystem, mittelalterliche Bruchschreibweise
2. **Alltagsbezug**: Pizza-Metapher, Kuchen teilen, Rezepte anpassen, Rabatte ("ein Drittel günstiger")
3. **Warum-Erklärungen**: Warum muss man bei Division "mit dem Kehrwert multiplizieren"? Anschauliche Erklärung
4. **Häufige Fehler**: Zähler statt Nenner addieren, falsches Kürzen, Fehler beim Umwandeln gemischter Zahlen

---

## Kapitel 04: Dezimalzahlen und Prozentrechnung

**Pfad:** `/media/andhue/Wissen/open-lectures/L-Mathematik-I Mittlere Reife und Grundlagen/04-Dezimalzahlen-und-Prozentrechnung`

**Dateien (12 Content-Dateien):**
- `01-Dezimalzahlen.md`
- `02-Rechnen-mit-Dezimalzahlen.md`
- `03-Rundungsregeln.md`
- `04-Einfuehrung-in-die-Prozentrechnung.md`
- `05-Prozentwert.md`
- `06-Prozentsatz.md`
- `07-Grundwert.md`
- `08-Prozentuale-Aenderungen.md`
- `09-Rabatte-und-Preisberechnungen.md`
- `10-Zinsrechnung.md`
- `11-Zinseszins-Grundlagen.md`
- `12-Praktische-wirtschaftliche-Anwendungen.md`

**Enhancement-Schwerpunkte:**
1. **Historische Entwicklung**: Entstehung des Dezimalsystems (Simon Stevin, 1585), Ursprung des %-Zeichens (per cento)
2. **Wirtschaftliche Alltagsanwendungen**: MwSt-Berechnung, Inflationsverständnis, Kreditzinsen, Gehaltsverhandlungen
3. **Rundungsfallen**: Kaufmännische vs. mathematische Rundung, Fehlerfortpflanzung bei mehrfachem Runden
4. **Häufige Fehler**: "Von" vs. "Um" bei Prozentangaben (Erhöhung um 50% vs. auf 150%), Zinseszins-Missverständnisse

---

## Kapitel 05: Verhältnisse und Proportionalität

**Pfad:** `/media/andhue/Wissen/open-lectures/L-Mathematik-I Mittlere Reife und Grundlagen/05-Verhaeltnisse-und-Proportionalitaet`

**Dateien (10 Content-Dateien):**
- `01-Verhaeltnisse.md`
- `02-Proportionen.md`
- `03-Dreisatz.md`
- `04-Direkte-Proportionalitaet.md`
- `05-Indirekte-Proportionalitaet.md`
- `06-Umrechnungen-von-Einheiten.md`
- `07-Massstaebe.md`
- `08-Geschwindigkeit-Strecke-und-Zeit.md`
- `09-Dichte-und-Masse.md`
- `10-Technische-Verhaeltnisberechnungen.md`

**Enhancement-Schwerpunkte:**
1. **Goldener Schnitt**: Historische Bedeutung in Architektur und Kunst (Parthenon, Da Vinci)
2. **Praktische Dreisatz-Anwendungen**: Rezepte umrechnen, Kraftstoffverbrauch, Arbeitszeit-Berechnungen
3. **Direkt vs. Indirekt**: Intuitive Erklärung – mehr Arbeiter = weniger Zeit (indirekt), mehr Strecke = mehr Zeit (direkt)
4. **Maßstäbe**: Landkarten lesen, Modellbau, technische Zeichnungen

---

## Kapitel 06: Potenzen, Wurzeln und Zahlendarstellung

**Pfad:** `/media/andhue/Wissen/open-lectures/L-Mathematik-I Mittlere Reife und Grundlagen/06-Potenzen-Wurzeln-und-Zahlendarstellung`

**Dateien (12 Content-Dateien):**
- `01-Potenzschreibweise.md`
- `02-Potenzen-mit-natuerlichen-Exponenten.md`
- `03-Potenzgesetze.md`
- `04-Potenzen-mit-negativen-Exponenten.md`
- `05-Zehnerpotenzen.md`
- `06-Quadratwurzeln.md`
- `07-Rechnen-mit-Quadratwurzeln.md`
- `08-Wurzelgesetze.md`
- `09-Kubikwurzeln-Grundlagen.md`
- `10-Wissenschaftliche-Schreibweise.md`
- `11-Naeherungsverfahren.md`
- `12-Anwendungen-in-Wissenschaft-und-Technik.md`

**Enhancement-Schwerpunkte:**
1. **Historische Entdeckungen**: √2 und die Krise der Pythagoreer (irrationale Zahlen), Entstehung des Wurzelzeichens
2. **Große und kleine Zahlen**: Astronomie (Lichtjahre), Biologie (Zellgrößen), Informatik (Bytes, Gigabytes)
3. **Warum-Erklärungen**: Warum ist $a^0 = 1$? Warum ist $a^{-n} = \frac{1}{a^n}$?
4. **Häufige Fehler**: $(a+b)^2 \neq a^2 + b^2$, falsche Anwendung der Potenzgesetze

---

## Kapitel 07: Terme und algebraische Ausdrücke

**Pfad:** `/media/andhue/Wissen/open-lectures/L-Mathematik-I Mittlere Reife und Grundlagen/07-Terme-und-algebraische-Ausdruecke`

**Dateien (11 Content-Dateien):**
- `01-Variablen-und-Platzhalter.md`
- `02-Mathematische-Terme.md`
- `03-Einsetzen-von-Variablen.md`
- `04-Zusammenfassen-gleichartiger-Terme.md`
- `05-Ausmultiplizieren.md`
- `06-Ausklammern.md`
- `07-Vereinfachen-von-Termen.md`
- `08-Binomische-Formeln.md`
- `09-Faktorisierung.md`
- `10-Umstellen-einfacher-Formeln.md`
- `11-Anwendungen-der-Algebra.md`

**Enhancement-Schwerpunkte:**
1. **Geschichte der Algebra**: Al-Chwarizmi und die Entstehung des Begriffs "Algebra" (al-jabr), Entwicklung der Symbolschreibweise
2. **Binomische Formeln**: Geometrische Visualisierung (Flächenmodell), Merksprüche ("erste hoch zwei...")
3. **Praktische Anwendungen**: Formeln in Physik, Wirtschaft, Programmierung
4. **Häufige Fehler**: Falsche Vorzeichen beim Ausklammern, Verwechslung bei binomischen Formeln

---

## Kapitel 08: Gleichungen und Ungleichungen

**Pfad:** `/media/andhue/Wissen/open-lectures/L-Mathematik-I Mittlere Reife und Grundlagen/08-Gleichungen-und-Ungleichungen`

**Dateien (12 Content-Dateien):**
- `01-Grundlagen-von-Gleichungen.md`
- `02-Aequivalenzumformungen.md`
- `03-Ueberpruefung-von-Loesungen.md`
- `04-Lineare-Gleichungen.md`
- `05-Gleichungen-mit-Klammern.md`
- `06-Bruchgleichungen.md`
- `07-Lineare-Ungleichungen.md`
- `08-Quadratische-Gleichungen.md`
- `09-Loesungsformel-quadratische-Gleichungen.md`
- `10-Faktorisierung-quadratischer-Gleichungen.md`
- `11-Lineare-Gleichungssysteme.md`
- `12-Textaufgaben.md`

**Enhancement-Schwerpunkte:**
1. **Geschichte**: Babylonische Gleichungslösung, indische Mathematiker und die Lösungsformel
2. **Waagen-Metapher**: Gleichungen als Balance – was man links tut, muss man auch rechts tun
3. **Textaufgaben-Strategien**: Systematisches Vorgehen, typische Schlüsselwörter erkennen
4. **Häufige Fehler**: Vorzeichenfehler bei Äquivalenzumformungen, Definitionsbereich bei Bruchgleichungen vergessen

---

## Kapitel 09: Funktionen und Koordinatensysteme

**Pfad:** `/media/andhue/Wissen/open-lectures/L-Mathematik-I Mittlere Reife und Grundlagen/09-Funktionen-und-Koordinatensysteme`

**Dateien (11 Content-Dateien):**
- `01-Kartesisches-Koordinatensystem.md`
- `02-Punkte-und-Koordinaten.md`
- `03-Einfuehrung-Funktionen.md`
- `04-Funktionstabellen-und-Graphen.md`
- `05-Lineare-Funktionen.md`
- `06-Steigung-und-Achsenabschnitt.md`
- `07-Geradengleichungen.md`
- `08-Quadratische-Funktionen.md`
- `09-Parabeln.md`
- `10-Schnittpunkte.md`
- `11-Anwendungen-Funktionen.md`

**Enhancement-Schwerpunkte:**
1. **René Descartes**: Geschichte des kartesischen Koordinatensystems, Verbindung von Algebra und Geometrie
2. **Steigung im Alltag**: Straßenschilder, Dächer, Rollstuhlrampen, Skipistenneigung
3. **Funktionen verstehen**: Automaten-Metapher (Input → Output), Abhängigkeiten im Alltag
4. **Häufige Fehler**: x- und y-Achse verwechseln, Steigung falsch ablesen, Vorzeichen bei Schnittpunkten

---

## Kapitel 10: Grundlagen der Geometrie

**Pfad:** `/media/andhue/Wissen/open-lectures/L-Mathematik-I Mittlere Reife und Grundlagen/10-Grundlagen-der-Geometrie`

**Dateien (12 Content-Dateien):**
- `01-Punkte-Strecken-Geraden.md`
- `02-Winkel-und-Winkelarten.md`
- `03-Winkelberechnungen.md`
- `04-Dreiecke.md`
- `05-Vierecke.md`
- `06-Kreise.md`
- `07-Umfangsberechnungen.md`
- `08-Flaechenberechnungen.md`
- `09-Symmetrie.md`
- `10-Kongruenz.md`
- `11-Aehnlichkeit.md`
- `12-Geometrische-Konstruktionen.md`

**Enhancement-Schwerpunkte:**
1. **Euklid und die Elemente**: Grundlage der Geometrie seit über 2000 Jahren, axiomatische Methode
2. **Geometrie in Architektur und Natur**: Bienenwaben (Sechsecke), Kuppeln (Kugeln), Brücken (Dreiecke)
3. **Kreiszahl π**: Geschichte der Berechnung, Archimedes, warum π irrational ist
4. **Häufige Fehler**: Umfang vs. Fläche verwechseln, Einheiten (cm vs. cm²)

---

## Kapitel 11: Satz des Pythagoras und Trigonometrie

**Pfad:** `/media/andhue/Wissen/open-lectures/L-Mathematik-I Mittlere Reife und Grundlagen/11-Satz-des-Pythagoras-und-Trigonometrie`

**Dateien (12 Content-Dateien):**
- `01-Rechtwinklige-Dreiecke.md`
- `02-Satz-des-Pythagoras.md`
- `03-Berechnung-unbekannter-Seiten.md`
- `04-Anwendungen-Pythagoras.md`
- `05-Einfuehrung-Trigonometrie.md`
- `06-Sinus.md`
- `07-Kosinus.md`
- `08-Tangens.md`
- `09-Berechnung-Seitenlaengen.md`
- `10-Berechnung-Winkel.md`
- `11-Steigungen-Neigungswinkel.md`
- `12-Vermessungsaufgaben.md`

**Enhancement-Schwerpunkte:**
1. **Pythagoras und seine Schule**: Geschichte, war der Satz schon vorher bekannt? (Babylonier, Ägypter, Chinesen)
2. **Praktische Anwendungen**: Leiterlängen, Fernseher-Diagonale, Navigation, Abstandsberechnung
3. **SOH-CAH-TOA**: Merkspruch für sin/cos/tan, anschauliche Erklärung mit Dreiecken
4. **Häufige Fehler**: Kathete und Hypotenuse verwechseln, Taschenrechner auf Grad vs. Radiant

---

## Kapitel 12: Körpergeometrie

**Pfad:** `/media/andhue/Wissen/open-lectures/L-Mathematik-I Mittlere Reife und Grundlagen/12-Koerpergeometrie`

**Dateien (12 Content-Dateien):**
- `01-Dreidimensionale-Koerper.md`
- `02-Wuerfel.md`
- `03-Quader.md`
- `04-Prisma.md`
- `05-Zylinder.md`
- `06-Pyramide.md`
- `07-Kegel.md`
- `08-Kugel.md`
- `09-Volumenberechnung.md`
- `10-Oberflaechenberechnung.md`
- `11-Zusammengesetzte-Koerper.md`
- `12-Praktische-Berechnungen.md`

**Enhancement-Schwerpunkte:**
1. **Archimedes und die Kugel**: Entdeckung der Kugelvolumen-Formel, Grabinschrift mit Kugel und Zylinder
2. **Verpackungen und Effizienz**: Warum sind Dosen zylindrisch? Optimale Verpackungsformen
3. **Körper in Architektur**: Pyramiden von Gizeh, Kuppeln, moderne Gebäude
4. **Häufige Fehler**: Grundfläche vs. Mantelfläche, cm³ vs. Liter, Faktor 1/3 bei Kegel/Pyramide vergessen

---

## Kapitel 13: Statistik und Datenanalyse

**Pfad:** `/media/andhue/Wissen/open-lectures/L-Mathematik-I Mittlere Reife und Grundlagen/13-Statistik-und-Datenanalyse`

**Dateien (13 Content-Dateien):**
- `01-Grundlagen-der-Statistik.md`
- `02-Datenerhebung.md`
- `03-Tabellen.md`
- `04-Absolute-und-relative-Haeufigkeiten.md`
- `05-Balkendiagramme.md`
- `06-Kreisdiagramme.md`
- `07-Histogramme.md`
- `08-Arithmetisches-Mittel.md`
- `09-Median.md`
- `10-Modalwert.md`
- `11-Spannweite.md`
- `12-Standardabweichung.md`
- `13-Interpretation.md`

**Enhancement-Schwerpunkte:**
1. **Geschichte der Statistik**: Ursprung im Staatswesen (lat. status), Florence Nightingale und Datenvisualisierung
2. **Irreführende Statistik**: Wie Diagramme manipuliert werden können (abgeschnittene Achsen, 3D-Effekte)
3. **Mittelwert vs. Median**: Wann welches Maß sinnvoller ist (Ausreißer, Einkommensverteilung)
4. **Häufige Fehler**: Korrelation ≠ Kausalität, falsche Schlüsse aus kleinen Stichproben

---

## Kapitel 14: Wahrscheinlichkeitsrechnung

**Pfad:** `/media/andhue/Wissen/open-lectures/L-Mathematik-I Mittlere Reife und Grundlagen/14-Wahrscheinlichkeitsrechnung`

**Dateien (12 Content-Dateien):**
- `01-Zufallsexperimente.md`
- `02-Ergebnismengen.md`
- `03-Ereignisse.md`
- `04-Haeufigkeit-und-Wahrscheinlichkeit.md`
- `05-Laplace-Experimente.md`
- `06-Wahrscheinlichkeiten-berechnen.md`
- `07-Gegenereignisse.md`
- `08-Baumdiagramme.md`
- `09-Pfadregeln.md`
- `10-Unabhaengige-Ereignisse.md`
- `11-Kombinatorik.md`
- `12-Praktische-Zufallsexperimente.md`

**Enhancement-Schwerpunkte:**
1. **Geschichte**: Blaise Pascal, Pierre de Fermat und das Glücksspiel-Problem (1654), Laplace
2. **Spielerfehlschluss**: Warum "überfällige" Zahlen beim Lotto nicht wahrscheinlicher sind
3. **Baumdiagramme systematisch**: Schritt-für-Schritt-Anleitung mit Pfadregeln
4. **Häufige Fehler**: "Oder" mit Schnittmenge verwechseln, bedingte Wahrscheinlichkeit ignorieren

---

## Kapitel 15: Praktische Mathematik und Abschlussprojekt

**Pfad:** `/media/andhue/Wissen/open-lectures/L-Mathematik-I Mittlere Reife und Grundlagen/15-Praktische-Mathematik-und-Abschlussprojekt`

**Dateien (10 Content-Dateien):**
- `01-Textaufgaben-loesen.md`
- `02-Einheiten-umrechnen.md`
- `03-Technische-Berechnungen.md`
- `04-Wirtschaftliche-Berechnungen.md`
- `05-Funktionen-graphisch.md`
- `06-Tabellenkalkulation.md`
- `07-Python-Mathematik.md`
- `08-Simulation.md`
- `09-Mathematische-Modelle.md`
- `10-Abschlusspruefung.md`

**Enhancement-Schwerpunkte:**
1. **Mathematik im Beruf**: Konkrete Beispiele aus verschiedenen Berufsfeldern (Handwerk, IT, Kaufleute)
2. **Digitale Werkzeuge**: Warum Tabellenkalkulation und Programmierung mathematisches Denken fördern
3. **Modellierungskreislauf**: Realität → Modell → Lösung → Interpretation → Realität
4. **Prüfungsvorbereitung**: Strategien für typische Prüfungsaufgaben, Zeitmanagement

---

## Zusammenfassung

| Kapitel | Pfad-Suffix | Content-Dateien | Status |
|---------|-------------|-----------------|--------|
| 02 | `02-Grundrechenarten-und-Rechengesetze` | 12 | Ausstehend |
| 03 | `03-Bruchrechnung` | 12 | Ausstehend |
| 04 | `04-Dezimalzahlen-und-Prozentrechnung` | 12 | Ausstehend |
| 05 | `05-Verhaeltnisse-und-Proportionalitaet` | 10 | Ausstehend |
| 06 | `06-Potenzen-Wurzeln-und-Zahlendarstellung` | 12 | Ausstehend |
| 07 | `07-Terme-und-algebraische-Ausdruecke` | 11 | Ausstehend |
| 08 | `08-Gleichungen-und-Ungleichungen` | 12 | Ausstehend |
| 09 | `09-Funktionen-und-Koordinatensysteme` | 11 | Ausstehend |
| 10 | `10-Grundlagen-der-Geometrie` | 12 | Ausstehend |
| 11 | `11-Satz-des-Pythagoras-und-Trigonometrie` | 12 | Ausstehend |
| 12 | `12-Koerpergeometrie` | 12 | Ausstehend |
| 13 | `13-Statistik-und-Datenanalyse` | 13 | Ausstehend |
| 14 | `14-Wahrscheinlichkeitsrechnung` | 12 | Ausstehend |
| 15 | `15-Praktische-Mathematik-und-Abschlussprojekt` | 10 | Ausstehend |

**Gesamtzahl Content-Dateien:** 163
