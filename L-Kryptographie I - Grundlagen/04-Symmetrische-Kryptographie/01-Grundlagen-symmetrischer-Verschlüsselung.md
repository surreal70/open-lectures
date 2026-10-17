---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - symmetrisch
---

# Grundlagen symmetrischer Verschlüsselung

> [!info] **Lernziele**
> - Das Prinzip symmetrischer Verschlüsselung verstehen
> - Vor- und Nachteile gegenüber asymmetrischen Verfahren einordnen
> - Das Schlüsselaustauschproblem als zentrale Herausforderung erkennen

---

## Inhalt

### Das Grundprinzip

Bei der **symmetrischen Verschlüsselung** verwenden Sender und Empfänger **denselben geheimen Schlüssel** $K$ für Ver- und Entschlüsselung:

$$C = E(K, M) \qquad M = D(K, C)$$

Beide Parteien müssen diesen Schlüssel kennen – und niemand sonst. Daraus ergibt sich die zentrale Eigenschaft: Die Sicherheit hängt vollständig von der Geheimhaltung des gemeinsamen Schlüssels ab.

### Vorteile

- **Geschwindigkeit:** Symmetrische Verfahren sind um Größenordnungen schneller als asymmetrische. AES wird in moderner Hardware direkt unterstützt (AES-NI).
- **Kompakte Schlüssel:** 128- oder 256-Bit-Schlüssel bieten hohe Sicherheit.
- **Eignung für große Datenmengen:** ideal für Festplatten-, Datenbank- und Transportverschlüsselung.

### Das Schlüsselaustauschproblem

Der entscheidende Nachteil: Beide Seiten brauchen **vorab** denselben Schlüssel – doch wie tauscht man ihn über einen unsicheren Kanal aus, ohne dass ein Angreifer ihn abfängt?

Zusätzlich skaliert die Schlüsselanzahl schlecht: Bei $n$ Teilnehmern, die paarweise sicher kommunizieren wollen, werden $\binom{n}{2} = \frac{n(n-1)}{2}$ Schlüssel benötigt.

> [!tip] **Lösung: hybride Verschlüsselung**
> In der Praxis kombiniert man beide Welten: Ein asymmetrisches Verfahren (→ Modul 5) tauscht einen zufälligen symmetrischen Sitzungsschlüssel sicher aus, mit dem dann die eigentliche (schnelle) symmetrische Verschlüsselung erfolgt. Genau so arbeitet TLS.

### Confusion und Diffusion

Moderne symmetrische Chiffren folgen zwei von **Claude Shannon** formulierten Designprinzipien:

- **Confusion:** Der Zusammenhang zwischen Schlüssel und Chiffretext soll möglichst komplex sein (realisiert durch Substitution).
- **Diffusion:** Die Information eines Klartextbits soll sich über viele Chiffretextbits verteilen (realisiert durch Permutation). Das Ändern eines einzigen Klartextbits soll etwa die Hälfte der Ausgabebits ändern (Lawineneffekt).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Symmetrisch: ein gemeinsamer geheimer Schlüssel für Ver- und Entschlüsselung
> - Vorteile: sehr schnell, kompakte Schlüssel, ideal für große Datenmengen
> - Kernproblem: sicherer Schlüsselaustausch; $n(n-1)/2$ Schlüssel bei $n$ Parteien
> - Lösung in der Praxis: hybride Verschlüsselung; Design folgt Confusion und Diffusion

---

## Übungen

1. Warum sind symmetrische Verfahren schneller als asymmetrische?
2. Wie viele Schlüssel benötigen 10 Teilnehmer für paarweise sichere Kommunikation?
3. Erklären Sie Confusion und Diffusion je an einem Beispiel.

---

← [[00-Symmetrisch-Index|Übersicht]] | [[02-Blockchiffren-und-Stromchiffren|Weiter →]]
