---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - klassisch
---

# Caesar- und Substitutionschiffren

> [!info] **Lernziele**
> - Die Caesar-Chiffre und allgemeine monoalphabetische Substitution verstehen
> - Ver- und Entschlüsselung durchführen können
> - Die Schwächen dieser Verfahren gegenüber Kryptoanalyse erkennen

---

## Inhalt

### Die Caesar-Chiffre

Die **Caesar-Chiffre** ist eine der ältesten bekannten Verschlüsselungen, benannt nach Julius Caesar. Sie verschiebt jeden Buchstaben des Klartexts um eine feste Anzahl $k$ von Stellen im Alphabet.

Mathematisch, mit Buchstaben als Zahlen $0$ (A) bis $25$ (Z):

$$c = (m + k) \bmod 26 \qquad m = (c - k) \bmod 26$$

Beispiel mit Schlüssel $k = 3$:

```
Klartext:  K R Y P T O
           10 17 24 15 19 14
+3 mod 26: 13 20 1  18 22 17
Chiffre:   N U B S W R
```

Der Schlüsselraum ist winzig: Es gibt nur **25 sinnvolle Schlüssel** ($k = 1 \dots 25$). Ein Angreifer probiert sie alle durch (Brute Force) – das nennt man **exhaustive Schlüsselsuche**.

### Monoalphabetische Substitution

Eine Verallgemeinerung ersetzt jeden Klartextbuchstaben durch einen **beliebig** zugeordneten Chiffrebuchstaben (statt nur zu verschieben). Der Schlüssel ist eine vollständige Permutation des Alphabets:

```
Klar:    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Chiffre: Q W E R T Z U I O P A S D F G H J K L Y X C V B N M
```

Das vergrößert den Schlüsselraum dramatisch auf $26! \approx 4 \cdot 10^{26}$ Möglichkeiten – Brute Force ist damit chancenlos.

### Warum dennoch unsicher?

Trotz des riesigen Schlüsselraums ist die monoalphabetische Substitution **leicht zu brechen**: Jeder Klartextbuchstabe wird immer auf denselben Chiffrebuchstaben abgebildet. Dadurch bleibt die **Häufigkeitsverteilung** der Sprache erhalten. Mit Häufigkeitsanalyse (→ [[05-Haeufigkeitsanalyse]]) lässt sich das Verfahren ohne Durchprobieren aller Schlüssel knacken.

> [!example] **Affine Chiffre**
> Eine Variante ist die affine Chiffre $c = (a \cdot m + b) \bmod 26$. Damit sie umkehrbar ist, muss $a$ teilerfremd zu 26 sein (damit $a^{-1} \bmod 26$ existiert, → [[03-Euklidischer-Algorithmus]]).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Caesar: Verschiebung um festen Wert $k$, nur 25 Schlüssel – trivial per Brute Force zu brechen
> - Monoalphabetische Substitution: beliebige Permutation, $26!$ Schlüssel
> - Großer Schlüsselraum schützt nicht: Häufigkeitsverteilung bleibt erhalten
> - Beide Verfahren sind heute nur noch von historischem/didaktischem Wert

---

## Übungen

1. Verschlüsseln Sie „GEHEIM" mit der Caesar-Chiffre und $k = 5$.
2. Warum bietet der Schlüsselraum von $26!$ keinen echten Schutz?
3. Für welche Werte von $a$ ist die affine Chiffre $c = (a \cdot m + b) \bmod 26$ umkehrbar?

---

← [[00-Klassisch-Index|Übersicht]] | [[02-Vigenère-Verschluesselung|Weiter →]]
