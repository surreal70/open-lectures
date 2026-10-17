---
author: Andreas Hümmer
title: Unabhängigkeit von Ereignissen
tags:
  - content
  - mathe
  - stochastik
  - unabhaengigkeit
  - ereignisse
created: 2025-07-01
modified: 2025-07-01
---

# Unabhängigkeit von Ereignissen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die Definition der stochastischen Unabhängigkeit verstehen
> - Unabhängigkeit von Disjunktheit unterscheiden können
> - Unabhängigkeit rechnerisch überprüfen können
> - Praktische Beispiele für unabhängige und abhängige Ereignisse kennen

---

## Überblick

Zwei Ereignisse heißen stochastisch unabhängig, wenn das Eintreten des einen Ereignisses keinen Einfluss auf die Wahrscheinlichkeit des anderen hat. Dieses Konzept ist fundamental für die Wahrscheinlichkeitsrechnung und besonders wichtig bei Bernoulli-Experimenten und der Binomialverteilung.

## Definition der Unabhängigkeit

### Formale Definition

Zwei Ereignisse $A$ und $B$ heißen **stochastisch unabhängig**, wenn gilt:

$$P(A \cap B) = P(A) \cdot P(B)$$

### Äquivalente Formulierungen

Für $P(B) > 0$ ist Unabhängigkeit gleichwertig mit:
$$P(A|B) = P(A)$$

Und für $P(A) > 0$:
$$P(B|A) = P(B)$$

### Interpretation

Bei unabhängigen Ereignissen:
- Die Kenntnis über $B$ ändert nichts an der Wahrscheinlichkeit von $A$
- Das Eintreten von $B$ hat keinen Einfluss auf $A$ (und umgekehrt)

## Beispiele für Unabhängigkeit

### Beispiel 1: Zweimaliger Münzwurf

Sei $A$ = „1. Wurf zeigt Kopf" und $B$ = „2. Wurf zeigt Kopf".

**Überprüfung:**
- $P(A) = \frac{1}{2}$
- $P(B) = \frac{1}{2}$
- $P(A \cap B) = \frac{1}{4}$ (beide Kopf)

$$P(A) \cdot P(B) = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4} = P(A \cap B) \quad \checkmark$$

Die Ereignisse sind unabhängig.

### Beispiel 2: Würfelwurf

Ein Würfel wird einmal geworfen.
- $A$ = „Augenzahl ist gerade" = $\{2, 4, 6\}$
- $B$ = „Augenzahl ist größer als 3" = $\{4, 5, 6\}$

**Überprüfung:**
- $P(A) = \frac{3}{6} = \frac{1}{2}$
- $P(B) = \frac{3}{6} = \frac{1}{2}$
- $A \cap B = \{4, 6\}$, also $P(A \cap B) = \frac{2}{6} = \frac{1}{3}$

$$P(A) \cdot P(B) = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4} \neq \frac{1}{3} = P(A \cap B)$$

Die Ereignisse sind **nicht** unabhängig!

### Beispiel 3: Kartenziehen mit Zurücklegen

Aus einem Skatspiel (32 Karten) wird eine Karte gezogen, notiert, zurückgelegt und erneut gezogen.

- $A$ = „1. Karte ist Herz"
- $B$ = „2. Karte ist Herz"

Durch das Zurücklegen sind die Ziehungen unabhängig:
$$P(A \cap B) = P(A) \cdot P(B) = \frac{8}{32} \cdot \frac{8}{32} = \frac{1}{16}$$

## Unabhängigkeit vs. Disjunktheit

### Häufiger Irrtum

Viele verwechseln „unabhängig" mit „disjunkt" (sich ausschließend). Diese Begriffe sind jedoch **völlig verschieden**:

| Eigenschaft | Unabhängig | Disjunkt |
|-------------|------------|----------|
| Definition | $P(A \cap B) = P(A) \cdot P(B)$ | $A \cap B = \emptyset$ |
| Schnittmenge | kann beliebig sein | ist leer |
| Bedeutung | kein Informationsgehalt | schließen sich aus |

### Wichtige Beobachtung

Für zwei Ereignisse $A$ und $B$ mit $P(A) > 0$ und $P(B) > 0$:

$$\text{Disjunkt} \Rightarrow \text{abhängig (nicht unabhängig!)}$$

**Beweis:** Wenn $A \cap B = \emptyset$, dann:
$$P(A \cap B) = 0 \neq P(A) \cdot P(B) > 0$$

### Visualisierung

**Disjunkte Ereignisse:**
```
┌─────────────────────────────────────┐
│              Ω                      │
│    ┌─────┐         ┌─────┐          │
│    │  A  │         │  B  │          │
│    └─────┘         └─────┘          │
│                                     │
└─────────────────────────────────────┘
A und B haben keine gemeinsamen Elemente
```

**Unabhängige Ereignisse:**
```
┌─────────────────────────────────────┐
│              Ω                      │
│    ┌───────────────┐                │
│    │       A       │                │
│    │   ┌───────┐   │                │
│    │   │ A ∩ B │   │                │
│    └───┼───────┼───┘                │
│        │   B   │                    │
│        └───────┘                    │
└─────────────────────────────────────┘
P(A∩B) = P(A)·P(B)
```

## Unabhängigkeit mehrerer Ereignisse

### Paarweise Unabhängigkeit

$A$, $B$, $C$ heißen **paarweise unabhängig**, wenn:
- $P(A \cap B) = P(A) \cdot P(B)$
- $P(A \cap C) = P(A) \cdot P(C)$
- $P(B \cap C) = P(B) \cdot P(C)$

### Vollständige Unabhängigkeit

$A$, $B$, $C$ heißen **(vollständig) unabhängig**, wenn zusätzlich:
$$P(A \cap B \cap C) = P(A) \cdot P(B) \cdot P(C)$$

### Wichtig

Paarweise Unabhängigkeit impliziert **nicht** vollständige Unabhängigkeit!

**Gegenbeispiel:** Es gibt Beispiele, bei denen drei Ereignisse paarweise, aber nicht vollständig unabhängig sind.

## Anwendung: Multiplikation von Wahrscheinlichkeiten

Bei unabhängigen Ereignissen $A_1, A_2, \ldots, A_n$ gilt:

$$P(A_1 \cap A_2 \cap \ldots \cap A_n) = P(A_1) \cdot P(A_2) \cdot \ldots \cdot P(A_n)$$

### Beispiel: Mehrfacher Münzwurf

Wie groß ist die Wahrscheinlichkeit, bei 5 Würfen einer fairen Münze 5-mal Kopf zu erhalten?

$$P(\text{5× Kopf}) = \left(\frac{1}{2}\right)^5 = \frac{1}{32}$$

### Beispiel: Mindestens-Aufgabe

Wie groß ist die Wahrscheinlichkeit, bei 4 Würfelwürfen mindestens einmal eine 6 zu werfen?

**Über Gegenereignis:**
$$P(\text{mind. eine 6}) = 1 - P(\text{keine 6})$$
$$= 1 - \left(\frac{5}{6}\right)^4 = 1 - \frac{625}{1296} = \frac{671}{1296} \approx 51{,}8\%$$

## Unabhängigkeit überprüfen

### Methode 1: Definition prüfen

Berechne $P(A)$, $P(B)$, $P(A \cap B)$ und vergleiche:
$$P(A \cap B) \stackrel{?}{=} P(A) \cdot P(B)$$

### Methode 2: Bedingte Wahrscheinlichkeit

Berechne $P(A|B)$ und vergleiche mit $P(A)$:
$$P(A|B) \stackrel{?}{=} P(A)$$

### Beispielrechnung

Urne mit 6 Kugeln: 2 rote große, 1 rote kleine, 2 blaue große, 1 blaue kleine.

- $R$ = „Kugel ist rot", $P(R) = \frac{3}{6} = \frac{1}{2}$
- $G$ = „Kugel ist groß", $P(G) = \frac{4}{6} = \frac{2}{3}$
- $R \cap G$ = „rot und groß", $P(R \cap G) = \frac{2}{6} = \frac{1}{3}$

**Prüfung:**
$$P(R) \cdot P(G) = \frac{1}{2} \cdot \frac{2}{3} = \frac{1}{3} = P(R \cap G) \quad \checkmark$$

Die Ereignisse „rot" und „groß" sind unabhängig!

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Bedingte-Wahrscheinlichkeit]] — Definition über $P(A|B) = P(A)$
- → [[Wiederholung-der-Wahrscheinlichkeitsrechnung]] — Grundlagen
- → [[Bernoulli-Experimente]] — Unabhängige Wiederholungen
- → [[Baumdiagramme]] — Multiplikation bei unabhängigen Stufen

> [!warning] **Prüfungsrelevant**
> - Definition: $P(A \cap B) = P(A) \cdot P(B)$
> - Strenge Unterscheidung: Unabhängig ≠ Disjunkt!
> - Rechnerische Überprüfung der Unabhängigkeit
> - Anwendung bei „mindestens"-Aufgaben über das Gegenereignis

> [!question] **Typische Prüfungsfragen**
> - Ein Würfel wird geworfen. Sind die Ereignisse „gerade Zahl" und „Primzahl" unabhängig?
> - Erkläre den Unterschied zwischen unabhängigen und disjunkten Ereignissen an einem Beispiel.
> - Bei drei unabhängigen Versuchen mit Erfolgswahrscheinlichkeit 0,7: Wie groß ist P(mind. ein Erfolg)?

## Quellen

- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 3, Springer Vieweg, 2016
- Bronstein, I.N. et al.: Taschenbuch der Mathematik, Verlag Europa-Lehrmittel, 2020
- ISB Bayern: Lehrplan Mathematik Gymnasium, Stochastik

> [!tip] **Weiterführende Links**
> - [[Bernoulli-Experimente]] — Anwendung auf wiederholte unabhängige Versuche
> - [[Bernoulli-Ketten]] — Formeln für unabhängige Wiederholungen
