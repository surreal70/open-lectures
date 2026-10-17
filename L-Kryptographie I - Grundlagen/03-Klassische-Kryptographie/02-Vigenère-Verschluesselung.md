---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - klassisch
---

# Vigenère-Verschlüsselung

> [!info] **Lernziele**
> - Die Vigenère-Chiffre als polyalphabetisches Verfahren verstehen
> - Mit einem Schlüsselwort ver- und entschlüsseln
> - Nachvollziehen, warum und wie sie gebrochen wurde

---

## Inhalt

### Vom mono- zum polyalphabetischen Verfahren

Die Schwäche monoalphabetischer Chiffren ist, dass jeder Buchstabe stets gleich ersetzt wird. Die **Vigenère-Chiffre** (16. Jahrhundert) behebt das: Sie verwendet ein **Schlüsselwort**, das mehrere unterschiedliche Caesar-Verschiebungen steuert. Derselbe Klartextbuchstabe wird je nach Position unterschiedlich verschlüsselt – daher **polyalphabetisch**.

### Funktionsweise

Das Schlüsselwort wird zyklisch unter den Klartext geschrieben. Jeder Klartextbuchstabe wird um den Wert seines zugehörigen Schlüsselbuchstabens verschoben:

$$c_i = (m_i + k_{i \bmod \ell}) \bmod 26$$

wobei $\ell$ die Länge des Schlüsselworts ist.

Beispiel mit Schlüsselwort `KEY`:

```
Klartext:    A N G R I F F
Schlüssel:   K E Y K E Y K
Verschiebung:10 4 24 10 4 24 10
Chiffre:     K R E B M D P
```

Entschlüsselt wird durch Subtraktion: $m_i = (c_i - k_{i \bmod \ell}) \bmod 26$.

### Warum lange als unknackbar galt

Weil ein Buchstabe je nach Schlüsselposition unterschiedlich abgebildet wird, verwischt die Vigenère-Chiffre die Häufigkeitsverteilung der Sprache. Sie galt über 300 Jahre als „le chiffre indéchiffrable".

### Der Bruch: Kasiski und Friedman

Die Chiffre ist dennoch brechbar, sobald man die **Schlüssellänge** $\ell$ kennt:

- **Kasiski-Test (1863):** Wiederholte Buchstabenfolgen im Chiffretext deuten auf Abstände hin, die Vielfache der Schlüssellänge sind. Der ggT dieser Abstände liefert Kandidaten für $\ell$.
- **Friedman-Test / Koinzidenzindex:** Ein statistisches Maß schätzt die Schlüssellänge aus der Häufigkeit zufälliger Übereinstimmungen.

Ist $\ell$ bekannt, zerfällt der Chiffretext in $\ell$ Gruppen, von denen jede mit einer **einzigen** Caesar-Verschiebung verschlüsselt wurde – und jede Gruppe ist dann per Häufigkeitsanalyse lösbar (→ [[05-Haeufigkeitsanalyse]]).

> [!note] **Grenzfall One-Time-Pad**
> Wird das Schlüsselwort so lang wie der Klartext, zufällig und nur einmal verwendet, wird die Vigenère-Chiffre zum **One-Time-Pad** – dem einzigen beweisbar sicheren Verfahren. Die Schwäche liegt also nicht im Prinzip, sondern in kurzen, wiederholten Schlüsseln.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Vigenère ist polyalphabetisch: ein Schlüsselwort steuert wechselnde Verschiebungen
> - Verschlüsselung: $c_i = (m_i + k_{i \bmod \ell}) \bmod 26$
> - Brechbar über die Schlüssellänge (Kasiski-/Friedman-Test), dann Häufigkeitsanalyse pro Gruppe
> - Mit zufälligem Schlüssel voller Länge wird daraus das sichere One-Time-Pad

---

## Übungen

1. Verschlüsseln Sie „KRYPTO" mit dem Schlüsselwort „BEN".
2. Erklären Sie, warum die Vigenère-Chiffre die Häufigkeitsverteilung verschleiert.
3. Welche Rolle spielt die Schlüssellänge beim Kasiski-Test?

---

← [[01-Caesar--und-Substitutionschiffren|← Zurück]] | [[00-Klassisch-Index|Übersicht]] | [[03-Transpositionsverfahren|Weiter →]]
