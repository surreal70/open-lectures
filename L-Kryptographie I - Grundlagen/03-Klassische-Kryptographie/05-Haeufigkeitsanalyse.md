---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - klassisch
---

# Häufigkeitsanalyse

> [!info] **Lernziele**
> - Das Prinzip der Häufigkeitsanalyse verstehen
> - Monoalphabetische Chiffren damit brechen können
> - Die Grenzen der Methode einordnen

---

## Inhalt

### Die Grundidee

Die **Häufigkeitsanalyse** ist die älteste systematische Kryptoanalyse-Technik, beschrieben bereits im 9. Jahrhundert von **al-Kindī**. Sie nutzt aus, dass Buchstaben in jeder natürlichen Sprache **unterschiedlich häufig** vorkommen. Bei einer monoalphabetischen Substitution bleibt diese Verteilung erhalten – nur die Buchstaben-Etiketten sind vertauscht.

### Buchstabenhäufigkeiten im Deutschen

Die häufigsten Buchstaben der deutschen Sprache (ungefähre relative Häufigkeit):

| Buchstabe | Häufigkeit |
|-----------|-----------|
| E | ~17 % |
| N | ~10 % |
| I | ~8 % |
| S / R | ~7 % |
| A / T | ~6 % |

Findet man im Chiffretext einen Buchstaben mit ~17 % Anteil, ist er mit hoher Wahrscheinlichkeit das verschlüsselte `E`.

### Vorgehen beim Brechen

1. **Häufigkeiten zählen:** Vorkommen jedes Chiffrebuchstabens auszählen.
2. **Erstzuordnung:** Die häufigsten Chiffrebuchstaben den häufigsten Klartextbuchstaben (E, N, I …) zuordnen.
3. **Muster nutzen:** Kurze Wörter, doppelte Buchstaben und typische Bigramme (`EN`, `ER`, `CH`, `EI`) und Trigramme (`SCH`, `DER`, `UND`) eingrenzen.
4. **Iterativ verfeinern:** Teilweise entschlüsselten Text lesen, Zuordnungen korrigieren, bis der Klartext lesbar ist.

### Über einzelne Buchstaben hinaus

Neben Einzelhäufigkeiten liefern **N-Gramme** (Bigramme, Trigramme) starke Hinweise. Auch die Wortlänge und die Position von Zeichen helfen. Diese Techniken brechen jede monoalphabetische Substitution bei ausreichender Textlänge zuverlässig.

### Grenzen

- **Kurze Texte:** Zu wenig Material verzerrt die Statistik; die Methode wird unzuverlässig.
- **Polyalphabetische Verfahren:** Vigenère verschleiert die Verteilung – erst nach Bestimmung der Schlüssellänge (→ [[02-Vigenère-Verschluesselung]]) lässt sich die Analyse gruppenweise anwenden.
- **Moderne Chiffren:** AES & Co. erzeugen eine (praktisch) gleichverteilte Ausgabe – Häufigkeitsanalyse ist wirkungslos.

> [!note] **Historische Bedeutung**
> Die Häufigkeitsanalyse beendete die jahrhundertelange Dominanz der monoalphabetischen Substitution und trieb die Entwicklung polyalphabetischer Verfahren voran – ein frühes Beispiel für den Wettlauf zwischen Kryptographie und Kryptoanalyse.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Häufigkeitsanalyse nutzt die ungleiche Buchstabenverteilung natürlicher Sprache
> - Bricht monoalphabetische Substitution trotz großem Schlüsselraum
> - N-Gramme (Bi-/Trigramme) verstärken die Methode
> - Wirkungslos bei polyalphabetischen und modernen Verfahren mit gleichverteilter Ausgabe

---

## Übungen

1. Nennen Sie die vier häufigsten Buchstaben im Deutschen.
2. Beschreiben Sie Schritt für Schritt, wie Sie eine monoalphabetische Substitution brechen würden.
3. Warum versagt die Häufigkeitsanalyse bei AES-verschlüsselten Daten?

---

← [[04-Enigma-und-historische-Verschluesselungsmaschinen|← Zurück]] | [[00-Klassisch-Index|Übersicht]] | [[06-Grundlagen-der-Kryptoanalyse|Weiter →]]
