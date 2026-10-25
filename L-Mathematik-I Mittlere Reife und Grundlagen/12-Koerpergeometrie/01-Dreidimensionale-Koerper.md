---
title: Dreidimensionale Körper - Einführung
chapter: "12"
section: "12.1"
type: lecture
created: 2026-10-13
modified: 2026-10-25
status: final
tags:
  - mathematik/geometrie/koerper
  - raumgeometrie
  - 3D
---

# Dreidimensionale Körper

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Den Unterschied zwischen 2D und 3D erklären
> - Grundlegende Körperarten benennen und unterscheiden
> - Eigenschaften wie Ecken, Kanten und Flächen identifizieren
> - Körper im Alltag erkennen und klassifizieren

## Von der Fläche zum Körper

### Die drei Dimensionen

In der [[10-Grundlagen-der-Geometrie/00-Geometrie-Index|ebenen Geometrie]] haben wir mit zwei Dimensionen gearbeitet:
- **Länge** (1. Dimension)
- **Breite** (2. Dimension)

Dreidimensionale Körper haben zusätzlich:
- **Höhe/Tiefe** (3. Dimension)

Der Schritt von der Fläche zum Körper ist ein fundamentaler Sprung im mathematischen Denken. Während wir auf einem Blatt Papier nur zwei Richtungen kennen (links-rechts und oben-unten), leben wir in einer dreidimensionalen Welt mit einer zusätzlichen Richtung (vor-zurück). Die alten Griechen nannten die Lehre von den Körpern „Stereometrie" (von griechisch „stereos" = fest, körperlich), während wir heute meist von Raumgeometrie sprechen.

> [!example] Beispiel: Vom Quadrat zum Würfel
> - **Quadrat (2D):** 4 Seiten, 4 Ecken, 1 Fläche
> - **Würfel (3D):** 12 Kanten, 8 Ecken, 6 Flächen

### Körper vs. Fläche

| Eigenschaft | 2D-Fläche | 3D-Körper |
|-------------|-----------|-----------|
| Ausdehnung | Länge × Breite | Länge × Breite × Höhe |
| Maßeinheit | cm², m² | cm³, m³, Liter |
| Messgröße | Flächeninhalt | Volumen (Rauminhalt) |
| Rand | Umfang | Oberfläche |

## Klassifikation der Körper

### Polyeder (Vielflächner)

Körper, die nur von ebenen Flächen begrenzt werden:

**Regelmäßige Körper (Platonische Körper):**

Die fünf platonischen Körper sind nach dem griechischen Philosophen Platon (ca. 428–348 v. Chr.) benannt, der ihnen kosmische Bedeutung zuschrieb. Sie sind die einzigen Körper, bei denen alle Flächen aus demselben regelmäßigen Vieleck bestehen und an jeder Ecke gleich viele Flächen zusammentreffen:

- [[02-Wuerfel|Würfel]] (Hexaeder) - 6 Quadrate
- Tetraeder - 4 gleichseitige Dreiecke
- Oktaeder - 8 gleichseitige Dreiecke
- Dodekaeder - 12 Fünfecke
- Ikosaeder - 20 gleichseitige Dreiecke

![[platonische-koerper.png]]
*<span class="fig-id">12-01-platonische-koerper</span>: Die fünf platonischen Körper als Schrägbilder – vom Tetraeder (4 Flächen) bis zum Ikosaeder (20 Flächen). Verdeckte Kanten sind gestrichelt dargestellt.*

> [!info] **Historischer Kontext**
> Platon ordnete vier dieser Körper den klassischen Elementen zu: Tetraeder = Feuer (wegen der „scharfen" Spitzen), Würfel = Erde (wegen der Stabilität), Oktaeder = Luft, Ikosaeder = Wasser. Das Dodekaeder repräsentierte das Universum als Ganzes.

**Prismen und Pyramiden:**
- [[03-Quader|Quader]] - rechteckige Grundfläche
- [[04-Prisma|Prisma]] - beliebige Vieleck-Grundfläche
- [[06-Pyramide|Pyramide]] - Vieleck mit Spitze

### Runde Körper

Körper mit gekrümmten Oberflächen:
- [[05-Zylinder|Zylinder]] - runde Säule
- [[07-Kegel|Kegel]] - runde Spitze
- [[08-Kugel|Kugel]] - perfekt rund

Runde Körper kann man sich als Grenzfälle von Vielflächnern vorstellen: Ein Zylinder entsteht, wenn man ein Prisma mit immer mehr Seitenflächen betrachtet – im Grenzfall unendlich vieler Seiten wird die Mantelfläche glatt. Ebenso entsteht ein Kegel aus einer Pyramide und eine Kugel aus einem Körper mit unendlich vielen Flächen.

## Eigenschaften von Körpern

### Ecken, Kanten, Flächen

> [!note] Eulersche Polyederformel
> Für jeden konvexen Polyeder gilt:
> $$E + F = K + 2$$
> wobei $E$ = Ecken, $F$ = Flächen, $K$ = Kanten

Diese bemerkenswerte Formel wurde 1750 vom Schweizer Mathematiker Leonhard Euler (1707–1783) entdeckt. Sie gilt für alle konvexen Polyeder – also für alle Vielflächner, bei denen keine Fläche nach innen gewölbt ist. Die Formel zeigt, dass bei Körpern ein tieferer Zusammenhang zwischen Ecken, Kanten und Flächen besteht, der nicht von der genauen Form abhängt.

**Beispiele:**

| Körper | Ecken (E) | Flächen (F) | Kanten (K) | E + F = K + 2 |
|--------|-----------|-------------|------------|---------------|
| Würfel | 8 | 6 | 12 | 8 + 6 = 12 + 2 ✓ |
| Tetraeder | 4 | 4 | 6 | 4 + 4 = 6 + 2 ✓ |
| Quader | 8 | 6 | 12 | 8 + 6 = 12 + 2 ✓ |
| Quadr. Pyramide | 5 | 5 | 8 | 5 + 5 = 8 + 2 ✓ |

> [!tip] **Anwendung der Eulerschen Formel**
> Wenn du zwei der drei Größen (Ecken, Kanten, Flächen) kennst, kannst du die dritte berechnen. Beispiel: Ein Körper hat 6 Ecken und 9 Kanten. Wie viele Flächen? → $6 + F = 9 + 2$, also $F = 5$.

### Volumen und Oberfläche

Jeder Körper hat zwei wichtige Maße:

**Volumen (V):**
- Rauminhalt des Körpers
- Maßeinheit: cm³, dm³ = Liter, m³
- Antwort auf: "Wie viel passt hinein?"

**Oberfläche (O):**
- Gesamtfläche aller Außenflächen
- Maßeinheit: cm², m²
- Antwort auf: "Wie viel Material braucht man zum Einpacken?"

> [!warning] **Häufiger Fehler: Verwechslung der Einheiten**
> Volumen wird in Kubikeinheiten gemessen (cm³, m³), Oberfläche in Quadrateinheiten (cm², m²). Diese Verwechslung ist einer der häufigsten Fehler bei Körperberechnungen!
> 
> - **Falsch:** „Das Volumen beträgt 50 cm²"
> - **Richtig:** „Das Volumen beträgt 50 cm³"

> [!tip] **Umrechnung: Volumen und Liter**
> - 1 cm³ = 1 ml (Milliliter)
> - 1 dm³ = 1 Liter = 1000 cm³
> - 1 m³ = 1000 Liter
> 
> Ein Würfel mit 10 cm Kantenlänge fasst genau 1 Liter: $10^3 = 1000$ cm³ = 1 dm³ = 1 L

## Körper im Alltag

### Erkennung und Zuordnung

Geometrische Körper begegnen uns im Alltag ständig – die Natur und der Mensch nutzen sie aus guten Gründen. Würfel und Quader lassen sich platzsparend stapeln, Zylinder sind stabil und leicht herzustellen, Kugeln rollen in alle Richtungen gleich gut.

> [!example] Alltagsbeispiele
> | Gegenstand | Körperform |
> |------------|------------|
> | Würfelzucker | Würfel |
> | Schuhkarton | Quader |
> | Konservendose | Zylinder |
> | Eistüte | Kegel |
> | Fußball | Kugel (näherungsweise) |
> | Toblerone | Dreiecksprisma |
> | Zelt | Pyramide/Prisma |
> | Bleistift | Sechseckprisma + Kegel |

> [!info] **Warum haben Dosen eine Zylinderform?**
> Die zylindrische Form von Getränke- und Konservendosen ist kein Zufall: Sie bietet ein gutes Verhältnis von Volumen zu Materialverbrauch unter allen leicht herstellbaren Formen. Außerdem lassen sich Zylinder auf Förderbändern gut transportieren und liegen angenehm in der Hand.

### Praktische Bedeutung

Körperberechnungen sind wichtig für:
- **Bauwesen:** Betonmengen, Raumvolumen, Tragfähigkeit
- **Verpackung:** Kartonbedarf, Materialkosten, optimale Verpackungsgrößen
- **Technik:** Tankgrößen, Behältervolumen, Rohrleitungen
- **Alltag:** Füllmengen, Lagerkapazität, Renovierungen

In der Architektur spielen geometrische Körper eine besondere Rolle: Die Pyramiden von Gizeh sind das berühmteste Beispiel für Pyramidenformen, moderne Hochhäuser sind oft Quader oder Prismen, und Kuppeldächer (wie beim Petersdom in Rom) basieren auf Halbkugeln oder Kugelabschnitten.

## Darstellung von Körpern

### Netz eines Körpers

Ein Körpernetz zeigt alle Flächen flach ausgebreitet:

> [!example] Würfelnetz
> ![[wuerfelnetz.png]]
> *<span class="fig-id">12-01-wuerfelnetz</span>: Ein Würfelnetz aus sechs Quadraten, das zusammengefaltet einen Würfel ergibt.*

### Schrägbild

Zweidimensionale Darstellung eines 3D-Körpers:
- Vorderfläche wird unverzerrt gezeichnet
- Tiefenlinien werden schräg (meist 45°) und verkürzt dargestellt
- Verkürzungsfaktor meist 0,5

## Zusammenfassung

> [!abstract] Kernpunkte
> - **Dreidimensionale Körper** haben Länge, Breite und Höhe
> - **Polyeder** werden von ebenen Flächen begrenzt
> - **Runde Körper** haben gekrümmte Oberflächen
> - Jeder Körper hat **Volumen** (Rauminhalt) und **Oberfläche**
> - Die **Eulersche Formel** verknüpft Ecken, Kanten und Flächen

## Übungsaufgaben

> [!question] Aufgabe 1
> Ordnen Sie folgende Gegenstände den Körperformen zu:
> Dartpfeil, Globus, Rubik's Cube, Campingzelt, Getränkedose, Toblerone

> [!question] Aufgabe 2
> Ein Körper hat 6 Ecken und 9 Kanten. Wie viele Flächen hat er?
> (Nutzen Sie die Eulersche Formel)

> [!question] Aufgabe 3
> Zeichnen Sie das Netz eines Quaders mit den Maßen 3 cm × 2 cm × 1 cm.

---

**Navigation:** [[00-Koerpergeometrie-Index|← Kapitelübersicht]] | [[02-Wuerfel|Würfel →]]
