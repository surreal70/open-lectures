---
title: Zufallsexperimente simulieren
chapter: "15"
section: "15.8"
type: lecture
created: 2026-10-13
modified: 2026-10-25
status: draft - review pending
tags:
  - mathematik/wahrscheinlichkeit
  - simulation
  - python
---

# Zufallsexperimente simulieren

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Zufallszahlen erzeugen
> - Experimente simulieren
> - Relative Häufigkeiten mit Wahrscheinlichkeiten vergleichen

Simulation ist eine mächtige Methode, um Wahrscheinlichkeiten zu verstehen und zu überprüfen. Statt tausende Würfel zu werfen oder Münzen zu flippen, lassen wir den Computer die Arbeit erledigen – in Sekundenbruchteilen.

### Warum simulieren?

Simulationen haben mehrere Vorteile gegenüber theoretischen Berechnungen:

| Vorteil | Beschreibung |
|---------|--------------|
| **Verständnis** | Ergebnisse werden greifbar und anschaulich |
| **Komplexität** | Auch schwer berechenbare Probleme können simuliert werden |
| **Überprüfung** | Theoretische Ergebnisse können experimentell bestätigt werden |
| **Exploration** | „Was-wäre-wenn"-Szenarien durchspielen |

> [!note] **Monte-Carlo-Methode**
> Die Technik, Probleme durch zufällige Stichproben zu lösen, heißt „Monte-Carlo-Methode" – benannt nach dem berühmten Casino in Monaco. Sie wurde in den 1940er Jahren bei der Entwicklung der Atombombe eingesetzt und ist heute ein Standardwerkzeug in Wissenschaft und Technik.

---

## Python: random-Modul

```python
import random

# Würfel simulieren
wurf = random.randint(1, 6)

# Münze werfen
muenze = random.choice(['Kopf', 'Zahl'])
```

### Wichtige Funktionen

| Funktion | Beschreibung | Beispiel |
|----------|--------------|----------|
| `random.randint(a, b)` | Zufällige Ganzzahl von a bis b (inklusive) | `random.randint(1, 6)` |
| `random.random()` | Zufällige Dezimalzahl zwischen 0 und 1 | `0.7423...` |
| `random.choice(liste)` | Zufälliges Element aus Liste | `random.choice(['A','B','C'])` |
| `random.shuffle(liste)` | Liste zufällig mischen | Mischen eines Kartendecks |
| `random.sample(liste, k)` | k zufällige Elemente (ohne Zurücklegen) | Lottoziehung |

> [!tip] **Reproduzierbare Zufallszahlen**
> Mit `random.seed(zahl)` können Sie den Zufallsgenerator initialisieren. Gleicher Seed = gleiche Zufallsfolge. Nützlich für Tests und Debugging.
> ```python
> random.seed(42)
> print(random.randint(1,100))  # Immer dasselbe Ergebnis
> ```

---

## Simulation: Würfel 1000x

```python
import random

wuerfe = [random.randint(1,6) for _ in range(1000)]
sechsen = wuerfe.count(6)
print(f"Relative Häufigkeit: {sechsen/1000}")
# Erwartet: ≈ 0.167 (1/6)
```

### Schritt-für-Schritt erklärt

1. **Zufallszahlen erzeugen**: Die List Comprehension `[random.randint(1,6) for _ in range(1000)]` erzeugt 1000 Würfelwürfe
2. **Zählen**: `.count(6)` zählt, wie oft die 6 vorkommt
3. **Relative Häufigkeit**: Anzahl der Sechsen geteilt durch Gesamtzahl

> [!example] Erweitertes Beispiel: Alle Augenzahlen
> ```python
> import random
> 
> n = 10000  # Anzahl Würfe
> wuerfe = [random.randint(1,6) for _ in range(n)]
> 
> print("Augenzahl | Häufigkeit | Rel. Häufigkeit | Theorie")
> print("-" * 55)
> for zahl in range(1, 7):
>     anzahl = wuerfe.count(zahl)
>     rel_haeuf = anzahl / n
>     print(f"    {zahl}     |    {anzahl:4}   |     {rel_haeuf:.4f}     |  0.1667")
> ```

---

## Gesetz der großen Zahlen

Je mehr Durchläufe, desto näher kommt die relative Häufigkeit an die theoretische Wahrscheinlichkeit.

Dieses fundamentale Gesetz der Wahrscheinlichkeitstheorie wurde erstmals von Jakob Bernoulli (1655–1705) bewiesen und erklärt, warum Simulationen funktionieren.

### Visualisierung des Konvergierens

![[praxis-simulation.png]]
*<span class="fig-id">15-08-simulation</span>: Simulierte relative Häufigkeit der 6 bei wachsender Wurfzahl – sie nähert sich dem theoretischen Wert $\tfrac{1}{6} \approx 0{,}167$ an.*

> [!example] Konvergenz beobachten
> ```python
> import random
> 
> kumuliert = 0
> for i in range(1, 10001):
>     wurf = random.randint(1, 6)
>     if wurf == 6:
>         kumuliert += 1
>     if i in [10, 100, 1000, 10000]:
>         print(f"Nach {i:5} Würfen: {kumuliert/i:.4f}")
> ```
> 
> Typische Ausgabe:
> ```
> Nach    10 Würfen: 0.2000
> Nach   100 Würfen: 0.1700
> Nach  1000 Würfen: 0.1630
> Nach 10000 Würfen: 0.1672
> ```

---

## Komplexere Simulationen

### Das Geburtstagsproblem

Wie wahrscheinlich ist es, dass in einer Gruppe von 23 Personen mindestens zwei am selben Tag Geburtstag haben?

> [!example] Simulation des Geburtstagsproblems
> ```python
> import random
> 
> def geburtstag_simulation(gruppengröße, durchläufe=10000):
>     treffer = 0
>     for _ in range(durchläufe):
>         geburtstage = [random.randint(1, 365) 
>                        for _ in range(gruppengröße)]
>         if len(geburtstage) != len(set(geburtstage)):
>             treffer += 1
>     return treffer / durchläufe
> 
> print(f"23 Personen: {geburtstag_simulation(23):.2%}")
> # Ergebnis: ca. 50%!
> ```

Dieses überraschende Ergebnis (auch „Geburtstagsparadoxon" genannt) zeigt, dass unsere Intuition bei Wahrscheinlichkeiten oft trügt.

### Monty-Hall-Problem

Das berühmte Ziegenproblem: Sie wählen eine von drei Türen. Hinter einer ist ein Auto, hinter den anderen Ziegen. Der Moderator öffnet eine Tür mit einer Ziege. Sollten Sie wechseln?

> [!example] Monty-Hall-Simulation
> ```python
> import random
> 
> def monty_hall(wechseln, durchläufe=10000):
>     gewinne = 0
>     for _ in range(durchläufe):
>         auto = random.randint(0, 2)
>         wahl = random.randint(0, 2)
>         # Wechseln gewinnt genau dann, wenn erste Wahl falsch war
>         if wechseln:
>             if wahl != auto:
>                 gewinne += 1
>         else:
>             if wahl == auto:
>                 gewinne += 1
>     return gewinne / durchläufe
> 
> print(f"Bleiben:  {monty_hall(False):.2%}")
> print(f"Wechseln: {monty_hall(True):.2%}")
> # Ergebnis: Wechseln gewinnt in ca. 67% der Fälle!
> ```

> [!warning] **Häufiger Fehler: Zu wenige Durchläufe**
> Bei wenigen Durchläufen können die Ergebnisse stark schwanken. Für zuverlässige Ergebnisse:
> - Einfache Experimente: mind. 1.000 Durchläufe
> - Komplexe Experimente: 10.000+ Durchläufe
> - Sehr seltene Ereignisse: noch mehr

---

## Zusammenhänge

Simulationen verbinden Wahrscheinlichkeitstheorie mit praktischer Anwendung:

- → [[../14-Wahrscheinlichkeitsrechnung/04-Haeufigkeit-und-Wahrscheinlichkeit|Häufigkeit und Wahrscheinlichkeit]] – theoretische Grundlage
- → [[../14-Wahrscheinlichkeitsrechnung/05-Laplace-Experimente|Laplace-Experimente]] – Würfel, Münzen, Karten
- → [[07-Python-Mathematik|Python für Mathematik]] – Programmiergrundlagen
- → [[09-Mathematische-Modelle|Mathematische Modelle]] – Simulation als Modellierungswerkzeug

---

**Navigation:** [[07-Python-Mathematik|← Python]] | [[09-Mathematische-Modelle|Modelle →]]
