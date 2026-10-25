---
title: "Kongruenz"
created: 2026-10-13
modified: 2026-10-25
chapter: "10"
section: "10"
status: "draft - review pending"
type: lecture
keywords:
  - Kongruenz
  - Kongruenzsätze
  - deckungsgleich
  - SSS
  - SWS
---

# Kongruenz

> [!info] Lernziele
> - Den Begriff Kongruenz verstehen
> - Die Kongruenzsätze für Dreiecke kennen und anwenden
> - Kongruenz nachweisen können
> - Dreiecke konstruieren können

---

## Einführung

Kongruenz bedeutet „Deckungsgleichheit" – zwei Figuren sind kongruent, wenn sie exakt gleich groß und gleich geformt sind. Man könnte die eine Figur ausschneiden und passgenau auf die andere legen.

### Praktische Bedeutung

Das Konzept der Kongruenz ist grundlegend für viele praktische Anwendungen:
- **Industrie**: Massenproduktion identischer Bauteile
- **Qualitätskontrolle**: Prüfen, ob ein Werkstück der Vorlage entspricht
- **Kartografie**: Übertragen von Formen auf Karten
- **Architektur**: Symmetrische Bauelemente müssen kongruent sein
- **Beweise**: Die Kongruenzsätze ermöglichen strenge geometrische Beweise

> [!note] **Euklids Kongruenzbegriff**
> Euklid verwendete den Begriff „gleich" für kongruente Figuren. Die Kongruenzsätze für Dreiecke gehören zu den frühesten mathematischen Erkenntnissen und bilden die Grundlage vieler Beweise in seinen „Elementen".

---

## Definition

Zwei Figuren sind **kongruent** (deckungsgleich), wenn sie in Form und Größe übereinstimmen.

$$\triangle ABC \cong \triangle DEF$$

> [!note] Kongruenz bei Dreiecken
> Zwei Dreiecke sind kongruent, wenn alle entsprechenden Seiten und Winkel gleich sind.

### Kongruenz vs. Gleichheit

- Gleiche Figuren haben identische Position
- Kongruente Figuren können verschoben, gedreht oder gespiegelt sein

## Die vier Kongruenzsätze

### SSS – Seite-Seite-Seite

Zwei Dreiecke sind kongruent, wenn sie in allen **drei Seitenlängen** übereinstimmen.

![[kongruenz-sss.png]]
*<span class="fig-id">10-10-kongruenz-sss</span>: Kongruenzsatz SSS: Stimmen zwei Dreiecke in allen drei Seiten ($a$, $b$, $c$) überein, sind sie kongruent.*

### SWS – Seite-Winkel-Seite

Zwei Dreiecke sind kongruent, wenn sie in **zwei Seiten** und dem **eingeschlossenen Winkel** übereinstimmen.

![[kongruenz-sws.png]]
*<span class="fig-id">10-10-kongruenz-sws</span>: Kongruenzsatz SWS: zwei Seiten ($a$, $b$) und der eingeschlossene Winkel $\gamma$ bestimmen das Dreieck eindeutig.*

> [!warning] Wichtig
> Der Winkel muss **zwischen** den beiden Seiten liegen!

### WSW – Winkel-Seite-Winkel

Zwei Dreiecke sind kongruent, wenn sie in **einer Seite** und den **beiden anliegenden Winkeln** übereinstimmen.

![[kongruenz-wsw.png]]
*<span class="fig-id">10-10-kongruenz-wsw</span>: Kongruenzsatz WSW: eine Seite ($c$) und die beiden anliegenden Winkel $\alpha$ und $\beta$ bestimmen das Dreieck eindeutig.*

### SsW – Seite-Seite-Winkel (gegenüber der größeren Seite)

Zwei Dreiecke sind kongruent, wenn sie in **zwei Seiten** und dem **Winkel gegenüber der größeren Seite** übereinstimmen.

> [!warning] Vorsicht
> Der Winkel muss der **größeren** der beiden Seiten gegenüberliegen, sonst gibt es zwei Lösungen!

## Nicht-Kongruenzsätze

### WWW – Warum nicht?

Drei gleiche Winkel garantieren **keine Kongruenz**, sondern nur **Ähnlichkeit**.

![[kongruenz-www.png]]
*<span class="fig-id">10-10-kongruenz-www</span>: WWW ist kein Kongruenzsatz: gleiche Winkel, aber unterschiedliche Größe – die Dreiecke sind nur ähnlich, nicht kongruent.*

### SSW – Warum problematisch?

Zwei Seiten und ein Winkel, der **nicht** eingeschlossen ist, können zu **zwei verschiedenen Dreiecken** führen (uneindeutig).

## Anwendung der Kongruenzsätze

### Kongruenz nachweisen

1. Entsprechende Seiten und Winkel zuordnen
2. Prüfen, welcher Kongruenzsatz anwendbar ist
3. Benötigte Übereinstimmungen zeigen

> [!example] Beispiel
> Gegeben: $\triangle ABC$ mit $a = 5$ cm, $b = 7$ cm, $\gamma = 60°$
> und $\triangle DEF$ mit $d = 5$ cm, $e = 7$ cm, $\zeta = 60°$
> 
> Es gilt: $a = d$, $b = e$, $\gamma = \zeta$ (eingeschlossener Winkel)
> 
> Nach **SWS**: $\triangle ABC \cong \triangle DEF$

### Dreiecke konstruieren

| Gegeben | Kongruenzsatz | Konstruierbar? |
|---|---|---|
| $a, b, c$ | SSS | ja (eindeutig) |
| $a, b, \gamma$ | SWS | ja (eindeutig) |
| $c, \alpha, \beta$ | WSW | ja (eindeutig) |
| $\alpha, \beta, \gamma$ | – | nein (nur Winkel → unendlich viele ähnliche) |

## Konstruktionsbeispiel: SSS

Konstruiere ein Dreieck mit $a = 4$ cm, $b = 3$ cm, $c = 5$ cm.

1. Seite $c$ als Strecke $\overline{AB}$ zeichnen (5 cm)
2. Kreis um $A$ mit Radius $b = 3$ cm
3. Kreis um $B$ mit Radius $a = 4$ cm
4. Schnittpunkt der Kreise = Punkt $C$
5. Dreieck $ABC$ verbinden

## Zusammenfassung

> [!abstract] Kernpunkte
> - Kongruente Figuren sind deckungsgleich (gleiche Form und Größe)
> - Die vier Kongruenzsätze: SSS, SWS, WSW, SsW
> - WWW ist **kein** Kongruenzsatz (nur Ähnlichkeit)
> - Mit Kongruenzsätzen kann man Dreiecke eindeutig konstruieren
> - Kongruenzsätze helfen beim Beweisen in der Geometrie

## Zusammenhänge

Die Kongruenzsätze sind fundamental für viele geometrische Themen:

- → [[11-Aehnlichkeit|Ähnlichkeit]] – Kongruenz ist der Spezialfall mit Streckfaktor $k = 1$
- → [[12-Geometrische-Konstruktionen|Konstruktionen]] – Die Kongruenzsätze bestimmen, welche Dreiecke konstruierbar sind
- → [[04-Dreiecke|Dreiecke]] – Eigenschaften und Klassifikation von Dreiecken
- → [[02-Satz-des-Pythagoras|Satz des Pythagoras]] – Basiert auf Kongruenzbeweisen
- → [[09-Symmetrie|Symmetrie]] – Gespiegelte Figuren sind kongruent

> [!tip] **Die vier Kongruenzsätze merken**
> Merke dir: **S**eite, **W**inkel – und die Kombinationen SSS, SWS, WSW, SsW. WWW reicht nicht (nur gleiche Form, nicht Größe)!

## Übungsaufgaben

1. Entscheide, welcher Kongruenzsatz anwendbar ist:
   - $a = 6$, $b = 8$, $c = 10$
   - $a = 5$, $c = 7$, $\beta = 50°$
   - $\alpha = 40°$, $\beta = 60°$, $c = 8$

2. Konstruiere ein Dreieck mit:
   - $a = 6$ cm, $b = 4$ cm, $c = 5$ cm (SSS)
   - $b = 5$ cm, $c = 7$ cm, $\alpha = 40°$ (SWS)
   - $c = 6$ cm, $\alpha = 50°$, $\beta = 70°$ (WSW)

3. Warum kann man aus drei Winkeln kein eindeutiges Dreieck konstruieren?

4. Zwei Dreiecke haben: $a_1 = 5$, $b_1 = 7$, $\gamma_1 = 55°$ und $a_2 = 5$, $b_2 = 7$, $\gamma_2 = 55°$. Sind sie kongruent? Begründe.

---

**Navigation**: [[09-Symmetrie|← Symmetrie]] | [[00-Geometrie-Index|Übersicht]] | [[11-Aehnlichkeit|Ähnlichkeit →]]
