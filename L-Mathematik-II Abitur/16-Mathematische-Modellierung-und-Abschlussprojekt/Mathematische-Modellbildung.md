---
author: Andreas Hümmer
title: Mathematische Modellbildung
tags:
  - content
  - mathe
  - modellierung
  - anwendung
  - abitur
created: 2025-06-28
modified: 2025-06-28
---

# Mathematische Modellbildung

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Modellierungskreislauf beschreiben und anwenden können
> - Reale Situationen in mathematische Modelle übersetzen
> - Die Grenzen und Annahmen von Modellen kritisch reflektieren
> - Modellvalidierung und -verbesserung verstehen

---

## Überblick

Die **mathematische Modellbildung** ist die Kunst, reale Phänomene mit mathematischen Werkzeugen zu beschreiben. Ein Modell ist dabei immer eine vereinfachte Abbildung der Wirklichkeit — es erfasst die wesentlichen Aspekte eines Problems und lässt unwichtige Details weg.

In der Schulmathematik begegnen dir Modelle ständig: Die Beschreibung eines Wurfes als Parabel, das Wachstum einer Population durch eine Exponentialfunktion oder die Optimierung einer Verpackung. Das Besondere an diesem Kapitel ist der bewusste Blick auf den **Prozess** der Modellierung selbst.

## Der Modellierungskreislauf

Der Modellierungskreislauf beschreibt die Schritte von der realen Situation zur mathematischen Lösung und zurück:

```
┌─────────────────────────────────────────────────────────┐
│                    REALE WELT                           │
│                                                         │
│   Situation → Vereinfachung → Reales Modell             │
│       ↑                            ↓                    │
│       │                      Mathematisieren            │
│       │                            ↓                    │
│   Validieren            MATHEMATISCHE WELT              │
│       ↑                            ↓                    │
│   Interpretation ← Lösung ← Mathematisches Modell       │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Schritt 1: Situationsanalyse

Am Anfang steht die genaue Betrachtung der realen Situation:
- Welches Problem soll gelöst werden?
- Welche Größen spielen eine Rolle?
- Welche Zusammenhänge bestehen zwischen den Größen?

### Schritt 2: Vereinfachung und Annahmen

Ein Modell muss die Realität vereinfachen, um handhabbar zu sein:
- Welche Faktoren sind vernachlässigbar?
- Welche Idealisierungen sind sinnvoll?
- Unter welchen Bedingungen gilt das Modell?

**Beispiel**: Beim schiefen Wurf vernachlässigen wir oft den Luftwiderstand — das ist bei langsamen Würfen eine gute Näherung, bei schnellen Geschossen jedoch problematisch.

### Schritt 3: Mathematisierung

Die Übersetzung in die Sprache der Mathematik:
- Variablen festlegen (mit Einheiten!)
- Funktionale Zusammenhänge aufstellen
- Gleichungen oder Ungleichungen formulieren

### Schritt 4: Mathematische Bearbeitung

Die rein mathematische Lösung des Problems:
- Gleichungen lösen
- Extremwerte bestimmen
- Funktionen analysieren

### Schritt 5: Interpretation und Validierung

Rückübersetzung in die reale Welt:
- Was bedeutet die mathematische Lösung konkret?
- Ist das Ergebnis plausibel?
- Stimmt es mit Beobachtungen überein?

## Arten mathematischer Modelle

### Deterministische Modelle

Diese Modelle liefern bei gleichen Eingaben immer dieselben Ergebnisse:

$$y = f(x)$$

**Beispiele**:
- Fallgesetze: $s(t) = \frac{1}{2}gt^2$
- Zinseszinsformel: $K(n) = K_0 \cdot (1 + p)^n$
- Exponentielles Wachstum: $N(t) = N_0 \cdot e^{kt}$

### Stochastische Modelle

Diese Modelle berücksichtigen Zufallseinflüsse:

$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$

**Beispiele**:
- Qualitätskontrolle mit Stichproben
- Wartezeit-Modelle
- Epidemieausbreitung mit Zufallskontakten

### Diskrete vs. kontinuierliche Modelle

| Diskret | Kontinuierlich |
|---------|----------------|
| Folgen: $a_n$ | Funktionen: $f(t)$ |
| Differenzengleichungen | Differentialgleichungen |
| Zähldaten | Messdaten |

**Beispiel**: Bevölkerungswachstum kann diskret (Jahr für Jahr) oder kontinuierlich modelliert werden.

## Konkrete Modellierungsbeispiele

### Beispiel 1: Abkühlung einer Tasse Kaffee

**Situation**: Eine Tasse Kaffee kühlt von $90°C$ auf Raumtemperatur ($20°C$) ab.

**Annahmen**:
- Die Abkühlungsgeschwindigkeit ist proportional zur Temperaturdifferenz
- Die Raumtemperatur bleibt konstant

**Mathematisches Modell** (Newton'sches Abkühlungsgesetz):

$$\frac{dT}{dt} = -k(T - T_U)$$

wobei $T$ die Kaffeetemperatur, $T_U = 20°C$ die Umgebungstemperatur und $k > 0$ eine Konstante ist.

**Lösung**:

$$T(t) = T_U + (T_0 - T_U) \cdot e^{-kt} = 20 + 70 \cdot e^{-kt}$$

**Interpretation**: Der Kaffee nähert sich asymptotisch der Raumtemperatur an. Je heißer der Kaffee, desto schneller kühlt er ab.

### Beispiel 2: Optimale Verpackung

**Situation**: Eine zylindrische Dose soll $V = 500\,\text{ml}$ fassen. Wie müssen Radius und Höhe gewählt werden, um minimalen Materialverbrauch zu erreichen?

**Variablen**: Radius $r$, Höhe $h$

**Nebenbedingung**: $V = \pi r^2 h = 500$

**Zielfunktion** (Oberfläche minimieren):

$$A(r) = 2\pi r^2 + 2\pi r h = 2\pi r^2 + 2\pi r \cdot \frac{500}{\pi r^2} = 2\pi r^2 + \frac{1000}{r}$$

**Ableitung und Nullstellen**:

$$A'(r) = 4\pi r - \frac{1000}{r^2} = 0 \quad \Rightarrow \quad r = \sqrt[3]{\frac{250}{\pi}} \approx 4{,}30\,\text{cm}$$

**Interpretation**: Die optimale Dose hat $r \approx 4{,}30\,\text{cm}$ und $h \approx 8{,}60\,\text{cm}$, also $h = 2r$.

### Beispiel 3: Infektionsausbreitung (SIR-Modell)

**Situation**: Ausbreitung einer Krankheit in einer Population.

**Variablen**:
- $S(t)$: Anzahl der Anfälligen (Susceptible)
- $I(t)$: Anzahl der Infizierten (Infected)
- $R(t)$: Anzahl der Genesenen (Recovered)

**Modellgleichungen**:

$$\frac{dS}{dt} = -\beta S I$$
$$\frac{dI}{dt} = \beta S I - \gamma I$$
$$\frac{dR}{dt} = \gamma I$$

wobei $\beta$ die Infektionsrate und $\gamma$ die Genesungsrate beschreibt.

## Modellgüte und Grenzen

### Validierung

Ein Modell muss überprüft werden:
- **Plausibilitätsprüfung**: Sind die Vorhersagen realistisch?
- **Vergleich mit Daten**: Stimmen Modell und Messwerte überein?
- **Grenzfallbetrachtung**: Verhält sich das Modell bei extremen Werten sinnvoll?

### Typische Fehlerquellen

1. **Überanpassung**: Zu viele Parameter machen das Modell instabil
2. **Falsche Annahmen**: Das Modell passt nicht zur Situation
3. **Extrapolation**: Vorhersagen außerhalb des Gültigkeitsbereichs

> [!warning] **Wichtig für die Prüfung**
> In Abituraufgaben musst du oft:
> - Gegebene Modelle auf neue Situationen anwenden
> - Die Bedeutung von Parametern erklären
> - Grenzen des Modells diskutieren

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Exponentialfunktionen]] — Grundlage vieler Wachstumsmodelle
- → [[Vollstaendige-Kurvendiskussion]] — Analyse von Modellfunktionen
- → [[Extremwertprobleme]] — Optimierungsaufgaben lösen
- → [[Wachstumsmodelle]] — Vertiefung der Wachstumstypen
- → [[Optimierungsprobleme]] — Weitere Optimierungsbeispiele

> [!warning] **Prüfungsrelevant**
> - Der Modellierungskreislauf ist ein Kernkonzept
> - Annahmen und Vereinfachungen müssen benannt werden können
> - Die Interpretation mathematischer Ergebnisse im Sachkontext ist zentral
> - Modellgrenzen kritisch zu reflektieren wird erwartet

> [!question] **Typische Prüfungsfragen**
> - Welche Annahmen liegen einem gegebenen Modell zugrunde?
> - Interpretieren Sie den Parameter $k$ im Zusammenhang.
> - Diskutieren Sie die Grenzen des Modells für große Zeiträume.
> - Wie würde sich das Modell ändern, wenn Bedingung X nicht mehr gilt?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 2. Springer Vieweg, 2015
- Tietze, U.-P. et al.: Mathematikunterricht in der Sekundarstufe II, Band 1. Vieweg, 2000
- ISB Bayern: Lehrplan Mathematik, Gymnasium

> [!tip] **Weiterführende Links**
> - [[Wachstumsmodelle]] — Exponentielles und logistisches Wachstum im Detail
> - [[Numerische-Naeherungsverfahren]] — Wenn exakte Lösungen nicht möglich sind
> - [[Mathematische-Simulationen]] — Modelle am Computer untersuchen
