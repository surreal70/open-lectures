---
title: "Dreiecke"
created: 2026-10-13
modified: 2026-10-25
chapter: "10"
section: "04"
status: final
type: lecture
keywords:
  - Dreieck
  - Innenwinkelsumme
  - Dreieckarten
  - Höhe
  - Seitenhalbierende
---

# Dreiecke

> [!info] Lernziele
> - Die verschiedenen Dreieckarten kennen und unterscheiden
> - Die Innenwinkelsumme anwenden können
> - Besondere Linien im Dreieck kennen
> - Dreiecke konstruieren können

---

## Einführung

Das Dreieck ist die einfachste geschlossene Figur mit geraden Seiten – und gleichzeitig eine der wichtigsten Formen in Mathematik, Natur und Technik. Mit nur drei Punkten, die nicht auf einer Geraden liegen, ist ein Dreieck eindeutig bestimmt.

### Warum sind Dreiecke so besonders?

Das Dreieck hat eine einzigartige Eigenschaft: Es ist **formstabil**. Während sich ein Viereck zu einem Parallelogramm „verbiegen" lässt, behält ein Dreieck immer seine Form. Deshalb finden wir Dreiecke überall, wo Stabilität gefragt ist:

- **Brückenbau**: Fachwerkbrücken bestehen aus Dreiecken
- **Kräne und Gerüste**: Dreiecksstrukturen verhindern das Umkippen
- **Dachstühle**: Dreieckige Verstrebungen tragen das Gewicht
- **Fahrradrahmen**: Das klassische „Diamant"-Rahmen besteht aus zwei Dreiecken

> [!note] **Euklids Dreiecksgeometrie**
> Euklids „Elemente" widmen dem Dreieck besondere Aufmerksamkeit. Viele seiner 465 Sätze handeln von Dreiecken – vom berühmten Satz des Pythagoras bis zu den Kongruenzsätzen. Das Dreieck ist das Fundament, auf dem die gesamte euklidische Geometrie aufbaut.

---

## Definition und Bezeichnung

Ein **Dreieck** ist eine geschlossene Figur aus drei Seiten und drei Ecken.

### Standardbezeichnung

![[dreieck-bezeichnung.png]]
*<span class="fig-id">10-04-dreieck-bezeichnung</span>: Standardbezeichnung: Ecken $A$, $B$, $C$, gegenüberliegende Seiten $a$, $b$, $c$ und Winkel $\alpha$, $\beta$, $\gamma$.*

| Element | Bezeichnung |
|---|---|
| Eckpunkte | $A$, $B$, $C$ (gegen den Uhrzeigersinn) |
| Seiten | $a = \overline{BC}$, $b = \overline{CA}$, $c = \overline{AB}$ |
| Winkel | $\alpha$ bei $A$, $\beta$ bei $B$, $\gamma$ bei $C$ |

> [!tip] Merkregel
> Jede Seite liegt dem gleichnamigen Winkel/Eckpunkt **gegenüber**:
> - Seite $a$ liegt gegenüber von Ecke $A$ (und Winkel $\alpha$)

## Die Innenwinkelsumme

> [!warning] Fundamentaler Satz
> Die Summe der Innenwinkel eines Dreiecks beträgt immer **180°**:
> $$\alpha + \beta + \gamma = 180°$$

Dieser Satz ist einer der wichtigsten in der Geometrie. Er gilt für **jedes** Dreieck – egal ob klein oder groß, spitz oder stumpfwinklig.

> [!note] **Warum ist die Winkelsumme 180°?**
> Der Beweis nutzt die [[03-Winkelberechnungen|Winkelsätze am Parallelenschnitt]]: Zeichnet man durch einen Eckpunkt eine Parallele zur gegenüberliegenden Seite, entstehen Wechselwinkel, die zeigen, dass die drei Winkel zusammen einen gestreckten Winkel (180°) bilden.

### Anwendung

> [!example] Beispiel
> Gegeben: $\alpha = 45°$, $\beta = 70°$
> 
> $\gamma = 180° - 45° - 70° = 65°$

> [!warning] **Häufiger Fehler**
> Manche Schüler verwechseln die Innenwinkelsumme des Dreiecks (180°) mit der des Vierecks (360°). Merkregel: Dreieck = **drei**mal 60° = 180°.

## Dreieckarten nach Seiten

![[dreieck-nach-seiten.png]]
*<span class="fig-id">10-04-dreieck-nach-seiten</span>: Einteilung nach Seitenlängen: gleichseitig, gleichschenklig und ungleichseitig.*

### Gleichseitiges Dreieck

Alle drei Seiten gleich lang: $a = b = c$

Alle Winkel gleich: $\alpha = \beta = \gamma = 60°$

### Gleichschenkliges Dreieck

Zwei Seiten gleich lang (z.B. $a = b$)

Die Basiswinkel sind gleich: $\alpha = \beta$

### Ungleichseitiges Dreieck

Alle Seiten verschieden lang: $a \neq b \neq c$

Alle Winkel verschieden.

## Dreieckarten nach Winkeln

![[dreieck-nach-winkeln.png]]
*<span class="fig-id">10-04-dreieck-nach-winkeln</span>: Einteilung nach Winkeln: spitzwinklig (alle < 90°), rechtwinklig (ein Winkel = 90°) und stumpfwinklig (ein Winkel > 90°).*

### Spitzwinkliges Dreieck

Alle Winkel kleiner als 90°.

### Rechtwinkliges Dreieck

Ein Winkel ist genau 90°.

![[dreieck-rechtwinklig.png]]
*<span class="fig-id">10-04-dreieck-rechtwinklig</span>: Im rechtwinkligen Dreieck liegt die Hypotenuse dem rechten Winkel gegenüber; die beiden anderen Seiten sind die Katheten.*

Die Seite gegenüber dem rechten Winkel heißt **Hypotenuse**.
Die anderen beiden Seiten heißen **Katheten**.

### Stumpfwinkliges Dreieck

Ein Winkel ist größer als 90°.

## Besondere Linien im Dreieck

### Höhe

Die **Höhe** $h_a$ ist das Lot von der Ecke $A$ auf die Gegenseite $a$.

![[dreieck-hoehe.png]]
*<span class="fig-id">10-04-dreieck-hoehe</span>: Die Höhe $h_a$ ist das Lot von Ecke $A$ auf die Gegenseite mit Fußpunkt $F$.*

- Jedes Dreieck hat drei Höhen
- Die Höhen schneiden sich im **Höhenschnittpunkt** $H$

### Seitenhalbierende (Median)

Die **Seitenhalbierende** $s_a$ verbindet Ecke $A$ mit dem Mittelpunkt von Seite $a$.

- Die drei Seitenhalbierenden schneiden sich im **Schwerpunkt** $S$
- Der Schwerpunkt teilt jede Seitenhalbierende im Verhältnis 2:1

![[dreieck-seitenhalbierende.png]]
*<span class="fig-id">10-04-dreieck-seitenhalbierende</span>: Die drei Seitenhalbierenden verbinden jede Ecke mit dem Mittelpunkt der Gegenseite und schneiden sich im Schwerpunkt $S$.*

### Mittelsenkrechte

Die **Mittelsenkrechte** einer Seite steht senkrecht auf dieser und geht durch ihren Mittelpunkt.

- Die drei Mittelsenkrechten schneiden sich im **Umkreismittelpunkt** $U$

![[dreieck-mittelsenkrechte.png]]
*<span class="fig-id">10-04-dreieck-mittelsenkrechte</span>: Die Mittelsenkrechten schneiden sich im Umkreismittelpunkt $U$, dem Mittelpunkt des Umkreises durch alle drei Ecken.*

### Winkelhalbierende

Die **Winkelhalbierende** teilt einen Winkel in zwei gleich große Teile.

- Die drei Winkelhalbierenden schneiden sich im **Inkreismittelpunkt** $I$

![[dreieck-winkelhalbierende.png]]
*<span class="fig-id">10-04-dreieck-winkelhalbierende</span>: Die Winkelhalbierenden schneiden sich im Inkreismittelpunkt $I$, dem Mittelpunkt des Inkreises, der alle drei Seiten berührt.*

## Übersicht: Besondere Punkte

| Punkt | Schnittpunkt von | Symbol |
|---|---|---|
| Höhenschnittpunkt | Höhen | $H$ |
| Schwerpunkt | Seitenhalbierenden | $S$ |
| Umkreismittelpunkt | Mittelsenkrechten | $U$ |
| Inkreismittelpunkt | Winkelhalbierenden | $I$ |

## Dreiecksungleichung

> [!warning] Existenzbedingung
> Ein Dreieck existiert nur, wenn jede Seite **kleiner** ist als die Summe der anderen beiden:
> 
> $$a < b + c$$
> $$b < a + c$$
> $$c < a + b$$

### Anschauliche Begründung

Warum muss das so sein? Stell dir vor, du baust ein Dreieck aus drei Stäben. Zwei Stäbe sind an der Grundseite (Länge $c$) mit Gelenken befestigt und sollen sich oben zur Spitze treffen.

- Sind die beiden oberen Stäbe **zusammen länger** als die Grundseite, treffen sie sich und bilden eine Spitze – ein Dreieck entsteht.
- Sind sie **zusammen genau so lang** wie die Grundseite, klappen sie flach auf die Grundseite. Alle drei Punkte liegen auf einer Geraden – ein „entartetes" Dreieck ohne Fläche.
- Sind sie **zusammen kürzer** als die Grundseite, können sie sich gar nicht erreichen – es klafft eine Lücke, kein Dreieck ist möglich.

Kurz gesagt: Der direkte Weg von einer Ecke zur anderen (die eine Seite) ist immer **kürzer** als jeder Umweg über die dritte Ecke (die beiden anderen Seiten). Das ist dieselbe Idee wie bei der [[01-Punkte-Strecken-Geraden|Strecke als kürzester Verbindung]] zweier Punkte.

### Kurzform: Nur die längste Seite prüfen

Man muss nicht alle drei Ungleichungen testen. Es genügt, die **längste** Seite zu betrachten:

> [!tip] Merkregel
> Ist die **längste** Seite kleiner als die Summe der beiden anderen, ist die Bedingung automatisch für alle drei Seiten erfüllt.

Der Grund: Ist $c$ die längste Seite, dann sind $a < b + c$ und $b < a + c$ ohnehin erfüllt (eine kleinere Zahl ist immer kleiner als eine größere plus etwas Positives). Nur $c < a + b$ kann überhaupt „scheitern".

### Der Grenzfall: entartetes Dreieck

Gilt statt „$<$" die **Gleichheit**, z. B. $c = a + b$, so liegen alle drei Ecken auf einer Geraden. Man spricht von einem **entarteten Dreieck**: Es hat die Fläche $0$ und keine echten Innenwinkel. Deshalb steht in der Bedingung bewusst ein echtes Kleiner-Zeichen ($<$) und kein $\leq$.

### Beispiele

> [!example] Beispiel 1 – kein Dreieck
> Können die Seiten $a = 3$, $b = 4$, $c = 8$ ein Dreieck bilden?
> 
> Längste Seite ist $c = 8$. Prüfung: $a + b = 3 + 4 = 7 < 8$ ✗
> 
> Die beiden kurzen Seiten sind zusammen kürzer als die lange – **kein Dreieck möglich**.

> [!example] Beispiel 2 – gültiges Dreieck
> Können die Seiten $a = 5$, $b = 6$, $c = 9$ ein Dreieck bilden?
> 
> Längste Seite ist $c = 9$. Prüfung: $a + b = 5 + 6 = 11 > 9$ ✓
> 
> Die Bedingung ist erfüllt – **ein Dreieck existiert**.

> [!example] Beispiel 3 – Grenzfall
> Seiten $a = 4$, $b = 6$, $c = 10$:
> 
> $a + b = 4 + 6 = 10 = c$ → Gleichheit
> 
> Es entsteht ein **entartetes Dreieck** (alle Punkte auf einer Geraden, Fläche $0$) – im strengen Sinn kein echtes Dreieck.

## Zusammenfassung

> [!abstract] Kernpunkte
> - Dreiecke haben drei Seiten, drei Ecken und drei Winkel
> - Die Innenwinkelsumme beträgt immer 180°
> - Einteilung nach Seiten: gleichseitig, gleichschenklig, ungleichseitig
> - Einteilung nach Winkeln: spitz-, recht-, stumpfwinklig
> - Besondere Linien: Höhen, Seitenhalbierende, Mittelsenkrechte, Winkelhalbierende
> - Die Dreiecksungleichung muss erfüllt sein

## Zusammenhänge

Das Dreieck ist das zentrale Objekt der ebenen Geometrie und verknüpft viele Themen:

- → [[02-Satz-des-Pythagoras|Satz des Pythagoras]] – Fundamentaler Satz für rechtwinklige Dreiecke
- → [[05-Einfuehrung-Trigonometrie|Trigonometrie]] – Sinus, Kosinus, Tangens im rechtwinkligen Dreieck
- → [[10-Kongruenz|Kongruenzsätze]] – Wann sind zwei Dreiecke deckungsgleich?
- → [[11-Aehnlichkeit|Ähnlichkeit]] – Gleiche Form, verschiedene Größe
- → [[08-Flaechenberechnungen|Flächenberechnung]] – $A = \frac{1}{2} \cdot g \cdot h$
- → [[12-Geometrische-Konstruktionen|Konstruktionen]] – Dreiecke mit Zirkel und Lineal konstruieren

## Übungsaufgaben

1. Berechne den fehlenden Winkel:
   - $\alpha = 55°$, $\beta = 75°$
   - $\alpha = 90°$, $\gamma = 38°$
   - $\beta = \gamma = 50°$

2. Klassifiziere die Dreiecke nach Seiten und Winkeln:
   - $a = 5$, $b = 5$, $c = 8$, $\gamma = 106°$
   - $a = b = c = 6$
   - $a = 3$, $b = 4$, $c = 5$, $\gamma = 90°$

3. Prüfe, ob ein Dreieck mit den Seitenlängen existieren kann:
   - $a = 4$, $b = 5$, $c = 6$
   - $a = 2$, $b = 3$, $c = 7$
   - $a = 5$, $b = 5$, $c = 10$

4. Ein gleichschenkliges Dreieck hat den Basiswinkel $\alpha = 70°$. Berechne alle Winkel.

---

**Navigation**: [[03-Winkelberechnungen|← Winkelberechnungen]] | [[00-Geometrie-Index|Übersicht]] | [[05-Vierecke|Vierecke →]]
