---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - klassisch
---

# Transpositionsverfahren

> [!info] **Lernziele**
> - Das Prinzip der Transposition von der Substitution abgrenzen
> - Spalten- und Skytale-Transposition anwenden
> - Die Schwächen und den Nutzen in Kombinationsverfahren verstehen

---

## Inhalt

### Substitution vs. Transposition

Klassische Verfahren beruhen auf zwei Grundprinzipien:

- **Substitution:** Zeichen werden **ersetzt** (Caesar, Vigenère).
- **Transposition:** Zeichen werden **umgeordnet** – der Zeichenvorrat bleibt gleich, nur ihre Reihenfolge ändert sich.

Bei einer reinen Transposition bleibt die Buchstabenhäufigkeit des Klartexts vollständig erhalten; verändert wird allein die Position.

### Die Skytale

Das älteste bekannte Transpositionsverfahren ist die **Skytale** (Sparta). Ein Pergamentstreifen wird spiralförmig um einen Stab gewickelt und längs beschrieben. Abgewickelt ergibt sich eine vertauschte Reihenfolge; nur ein Stab gleichen Durchmessers macht den Text wieder lesbar. Der Stabdurchmesser ist der Schlüssel.

### Spaltentransposition

Beim gängigeren Verfahren der **Spaltentransposition** schreibt man den Klartext zeilenweise in ein Raster fester Breite und liest ihn spaltenweise in einer durch ein Schlüsselwort bestimmten Reihenfolge aus.

Beispiel: Klartext `ANGRIFFBEINACHT`, Schlüsselwort `ZEBRA` (Spaltenreihenfolge nach alphabetischem Rang der Buchstaben: A=1, B=2, E=3, R=4, Z=5):

```
Schlüssel:  Z E B R A
Rang:       5 3 2 4 1
            ---------
            A N G R I
            F F B E I
            N A C H T
```

Spalten in Rang-Reihenfolge auslesen (1,2,3,4,5):

```
Rang 1 (A): I I T
Rang 2 (B): G B C
Rang 3 (E): N F A
Rang 4 (R): R E H
Rang 5 (Z): A F N
→ Chiffre: IITGBCNFAREHAFN
```

### Sicherheit und Bedeutung

Reine Transpositionen sind ebenfalls schwach: Da die Buchstabenhäufigkeit unverändert bleibt, erkennt ein Angreifer schnell, dass eine Transposition (keine Substitution) vorliegt. Durch Ausprobieren von Rasterbreiten und Anagramm-Techniken lassen sie sich brechen.

> [!example] **Kombination = Produktchiffre**
> Ihre eigentliche Stärke entfalten Transpositionen in **Kombination** mit Substitution. Moderne Blockchiffren wie **AES** wechseln bewusst zwischen Substitutions- und Permutationsschritten (**Confusion und Diffusion** nach Shannon) ab – das Grundprinzip der Transposition lebt dort fort.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Transposition ordnet Zeichen um, statt sie zu ersetzen
> - Skytale (Stabdurchmesser) und Spaltentransposition (Schlüsselwort) sind klassische Beispiele
> - Buchstabenhäufigkeit bleibt erhalten → allein schwach und erkennbar
> - In Kombination mit Substitution Grundlage moderner Produktchiffren (Diffusion)

---

## Übungen

1. Grenzen Sie Substitution und Transposition mit je einem Beispiel ab.
2. Verschlüsseln Sie „TRANSPOSITION" mit Spaltentransposition und Schlüsselwort „KEY".
3. Warum verrät eine reine Transposition dem Angreifer ihre Natur?

---

← [[02-Vigenère-Verschluesselung|← Zurück]] | [[00-Klassisch-Index|Übersicht]] | [[04-Enigma-und-historische-Verschluesselungsmaschinen|Weiter →]]
