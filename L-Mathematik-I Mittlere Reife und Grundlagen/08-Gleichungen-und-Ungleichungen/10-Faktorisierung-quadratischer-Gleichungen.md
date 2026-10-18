---
title: "Faktorisierung quadratischer Gleichungen"
created: 2026-10-13
modified: 2026-10-16
chapter: "08"
section: "10"
status: "draft - review pending"
type: lecture
keywords:
  - Faktorisierung
  - Nullstellen
  - Satz von Vieta
  - Linearfaktoren
---

# Faktorisierung quadratischer Gleichungen

> [!info] Lernziele
> - Quadratische Ausdrücke in Linearfaktoren zerlegen können
> - Den Zusammenhang zwischen Nullstellen und Faktoren verstehen
> - Den Satz von Vieta anwenden können
> - Durch geschicktes Raten Lösungen finden

## Historischer Hintergrund: Der Satz von Vieta

Der **Satz von Vieta** ist nach dem französischen Mathematiker **François Viète** (1540–1603) benannt, der als „Vater der modernen Algebra" gilt. Viète führte als Erster systematisch Buchstaben für unbekannte Größen ein und entdeckte den eleganten Zusammenhang zwischen den Koeffizienten einer Gleichung und ihren Lösungen.

Dieser Satz ist besonders nützlich, weil er es ermöglicht, Lösungen durch systematisches Probieren zu finden – ohne die p-q-Formel anwenden zu müssen. Bei „schönen" Zahlen ist das oft schneller und weniger fehleranfällig.

## Das Prinzip der Faktorisierung

Wenn eine quadratische Gleichung die Lösungen $x_1$ und $x_2$ hat, lässt sie sich schreiben als:

$$x^2 + px + q = (x - x_1)(x - x_2)$$

Dieses Prinzip basiert auf dem **Nullproduktsatz**: Ein Produkt ist genau dann Null, wenn mindestens einer der Faktoren Null ist. Wenn also $(x - x_1)(x - x_2) = 0$, dann muss $x = x_1$ oder $x = x_2$ sein.

> [!example] Beispiel
> Die Gleichung $x^2 - 5x + 6 = 0$ hat die Lösungen $x_1 = 2$ und $x_2 = 3$.
> 
> Also: $x^2 - 5x + 6 = (x - 2)(x - 3)$
> 
> **Probe durch Ausmultiplizieren**:
> $(x - 2)(x - 3) = x^2 - 3x - 2x + 6 = x^2 - 5x + 6$ ✓

## Der Satz von Vieta

Besonders praktisch wird die Faktorisierung durch eine Beobachtung, die bereits Viète machte: Zwischen den Lösungen einer Gleichung und ihren Koeffizienten $p$ und $q$ besteht ein fester Zusammenhang. Kennt man diesen, muss man die Lösungen nicht immer mühsam ausrechnen, sondern kann sie bei passenden Zahlen direkt ablesen oder zumindest überprüfen.

Für eine quadratische Gleichung in Normalform $x^2 + px + q = 0$ mit den Lösungen $x_1$ und $x_2$ gilt:

$$\boxed{x_1 + x_2 = -p}$$
$$\boxed{x_1 \cdot x_2 = q}$$

> [!tip] Merkregel
> - Die **Summe** der Lösungen ist $-p$ (negatives $p$)
> - Das **Produkt** der Lösungen ist $q$

### Herleitung

Aus $(x - x_1)(x - x_2) = x^2 - x_2 x - x_1 x + x_1 x_2$

$= x^2 - (x_1 + x_2)x + x_1 \cdot x_2$

Vergleich mit $x^2 + px + q$:
- $p = -(x_1 + x_2)$, also $x_1 + x_2 = -p$
- $q = x_1 \cdot x_2$

## Anwendungen des Satzes von Vieta

Der Zusammenhang zwischen Summe, Produkt und Koeffizienten ist nicht nur theoretisch schön, sondern lässt sich auf drei ganz unterschiedliche Weisen nutzen. Je nachdem, was man bereits weiß, hilft Vieta beim Finden, beim Überprüfen oder beim Ergänzen von Lösungen. Die folgenden drei Anwendungen zeigen das jeweils an einem Beispiel.

### 1. Lösungen durch Raten finden

Wenn $p$ und $q$ „schöne" Zahlen sind, kann man oft die Lösungen erraten.

> [!example] Beispiel
> $$x^2 - 7x + 12 = 0$$
> 
> Gesucht: Zwei Zahlen mit
> - Summe = $-(-7) = 7$
> - Produkt = $12$
> 
> Kandidaten für Produkt 12: $1 \cdot 12$, $2 \cdot 6$, $3 \cdot 4$
> 
> Summe 7: $3 + 4 = 7$ ✓
> 
> **Lösung**: $x_1 = 3$, $x_2 = 4$

### 2. Lösungen überprüfen

Nach dem Berechnen mit der p-q-Formel kann man die Lösungen mit Vieta kontrollieren.

> [!example] Beispiel
> $$x^2 + 2x - 15 = 0$$
> 
> p-q-Formel ergibt: $x_1 = 3$, $x_2 = -5$
> 
> **Kontrolle mit Vieta**:
> - Summe: $3 + (-5) = -2 = -p$ ✓
> - Produkt: $3 \cdot (-5) = -15 = q$ ✓

### 3. Fehlende Lösung bestimmen

Wenn eine Lösung bekannt ist, kann die andere mit Vieta gefunden werden.

> [!example] Beispiel
> $$x^2 - 8x + 15 = 0$$ hat die Lösung $x_1 = 3$. Wie lautet $x_2$?
> 
> Mit Vieta: $x_1 + x_2 = -p = 8$
> $$3 + x_2 = 8$$
> $$x_2 = 5$$

## Faktorisierung durchführen

Sind die Lösungen erst einmal bekannt, ist die Zerlegung in Linearfaktoren nur noch ein kleiner Schritt. Man kann dabei zwei Wege gehen: entweder man bestimmt die Lösungen zuerst und setzt sie in die Faktorform ein, oder man sucht direkt das passende Zahlenpaar. Beide Methoden führen zum selben Ergebnis und ergänzen sich gut.

### Methode 1: Über die Lösungen

1. Lösungen $x_1$ und $x_2$ bestimmen (p-q-Formel oder Raten)
2. Faktorform aufschreiben: $(x - x_1)(x - x_2)$

> [!example] Beispiel
> $$x^2 + x - 6 = 0$$
> 
> **Raten**: Produkt $= -6$, Summe $= -1$
> - $2 \cdot (-3) = -6$ ✓
> - $2 + (-3) = -1$ ✓
> 
> **Faktorform**: $(x - 2)(x + 3)$

### Methode 2: Direkte Zerlegung

Man sucht zwei Zahlen, deren Produkt $q$ und deren Summe $-p$ ist.

$$x^2 + px + q = (x + a)(x + b)$$

wobei $a + b = p$ und $a \cdot b = q$.

## Sonderfälle

### Doppellösung ($D = 0$)

$$x^2 - 6x + 9 = 0$$

Lösung: $x_1 = x_2 = 3$

Faktorform: $(x - 3)^2$

### Keine reellen Lösungen ($D < 0$)

$$x^2 + 4 = 0$$

Keine Faktorisierung in reelle Linearfaktoren möglich.

### Mit ganzzahligen Lösungen erkennen

> [!tip] Wann hat die Gleichung ganzzahlige Lösungen?
> - $q$ muss als Produkt zweier ganzer Zahlen darstellbar sein
> - Diese Zahlen müssen die Summe $-p$ haben
> 
> Beispiel: $x^2 - 2x - 8 = 0$
> - Produkt $= -8$: Möglichkeiten: $1 \cdot (-8)$, $(-1) \cdot 8$, $2 \cdot (-4)$, $(-2) \cdot 4$
> - Summe $= 2$: $(-2) + 4 = 2$ ✓
> - Lösungen: $x_1 = -2$, $x_2 = 4$

## Übersichtstabelle: Vieta

| Gleichung | $-p$ | $q$ | Lösungen |
|---|---|---|---|
| $x^2 - 5x + 6 = 0$ | 5 | 6 | $2, 3$ |
| $x^2 + x - 12 = 0$ | -1 | -12 | $3, -4$ |
| $x^2 - 4x + 4 = 0$ | 4 | 4 | $2, 2$ |
| $x^2 + 6x + 9 = 0$ | -6 | 9 | $-3, -3$ |

## Zusammenfassung

> [!abstract] Kernpunkte
> - Quadratische Terme können in Linearfaktoren zerlegt werden: $(x - x_1)(x - x_2)$
> - Der Satz von Vieta verbindet Lösungen mit Koeffizienten:
>   - Summe der Lösungen = $-p$
>   - Produkt der Lösungen = $q$
> - Vieta ermöglicht das Finden von Lösungen durch systematisches Probieren
> - Vieta dient zur Kontrolle berechneter Lösungen
> - Bei Doppellösungen: $(x - x_1)^2$

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[09-Loesungsformel-quadratische-Gleichungen|Lösungsformel]] – Alternative Methode mit p-q-Formel
- → [[08-Quadratische-Gleichungen|Quadratische Gleichungen]] – Grundlagen und Übersicht
- → [[07-Terme-und-algebraische-Ausdruecke/06-Ausklammern|Ausklammern]] – Verwandte Technik
- → [[07-Terme-und-algebraische-Ausdruecke/08-Binomische-Formeln|Binomische Formeln]] – Für Doppellösungen $(x-a)^2$

## Übungsaufgaben

1. Faktorisiere durch Raten: $x^2 - 9x + 20 = 0$

2. Bestimme die fehlende Lösung: $x^2 + 3x - 18 = 0$ hat $x_1 = 3$. Wie lautet $x_2$?

3. Prüfe mit Vieta: Sind $x_1 = -2$ und $x_2 = 7$ Lösungen von $x^2 - 5x - 14 = 0$?

4. Faktorisiere: $x^2 - 10x + 25 = 0$

5. Für welchen Wert von $k$ hat $x^2 - 6x + k = 0$ eine Doppellösung?

6. Stelle die Gleichung auf: Lösungen sind $x_1 = -3$ und $x_2 = 5$.

---

**Navigation**: [[09-Loesungsformel-quadratische-Gleichungen|← Lösungsformel]] | [[00-Gleichungen-und-Ungleichungen-Index|Übersicht]] | [[11-Lineare-Gleichungssysteme|Gleichungssysteme →]]
