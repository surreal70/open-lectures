---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - klassisch
---

# Grundlagen der Kryptoanalyse

> [!info] **Lernziele**
> - Ziele und Vorgehensweisen der Kryptoanalyse verstehen
> - Klassische Analysetechniken systematisch einordnen
> - Die Brücke von klassischer zu moderner Kryptoanalyse schlagen

---

## Inhalt

### Was ist Kryptoanalyse?

**Kryptoanalyse** ist die Wissenschaft vom Brechen kryptographischer Verfahren – das Gegenstück zur Kryptographie. Ihr Ziel ist es, ohne Kenntnis des Schlüssels an den Klartext zu gelangen oder den Schlüssel selbst zu rekonstruieren. Sie ist kein rein feindliches Werkzeug: Jede seriöse Chiffre muss der Kryptoanalyse standhalten, um als sicher zu gelten.

### Ansatzpunkte des Angreifers

Erfolgreiche Angriffe nutzen typischerweise eine oder mehrere der folgenden Schwächen:

| Ansatzpunkt | Beschreibung |
|-------------|--------------|
| **Statistische Muster** | Sprachstatistik bleibt erhalten (Häufigkeitsanalyse) |
| **Kleiner Schlüsselraum** | Vollständige Schlüsselsuche (Brute Force) |
| **Struktur des Verfahrens** | Konstruktionsfehler (z. B. Enigma-Selbstabbildung) |
| **Bekannter/wählbarer Klartext** | Cribs, Chosen-Plaintext (→ [[05-Kryptographische-Angriffsmodelle]]) |
| **Bedien- und Implementierungsfehler** | Schlüsselwiederverwendung, vorhersehbare Nachrichten |

### Klassische Techniken im Überblick

Die in diesem Modul behandelten Methoden lassen sich einordnen:

- **Brute Force:** alle Schlüssel durchprobieren – wirksam bei Caesar (25 Schlüssel).
- **Häufigkeitsanalyse:** Sprachstatistik ausnutzen – bricht monoalphabetische Substitution.
- **Kasiski-/Friedman-Test:** Schlüssellänge polyalphabetischer Chiffren bestimmen – öffnet Vigenère.
- **Anagramming:** Umordnungen rückgängig machen – gegen Transpositionschiffren.
- **Mustererkennung / Cribs:** vermutete Klartextteile einsetzen – zentral beim Enigma-Bruch.

### Das Prinzip hinter allen Angriffen

Alle klassischen Angriffe beruhen auf **Redundanz und Struktur**, die das Verfahren nicht ausreichend verbirgt. Die moderne Kryptographie zieht daraus die Konsequenz: Eine gute Chiffre soll eine Ausgabe erzeugen, die statistisch **nicht von Zufall unterscheidbar** ist (→ [[05-Kryptographische-Angriffsmodelle]], Stichwort IND-CPA/IND-CCA).

### Von klassischer zu moderner Kryptoanalyse

Moderne Verfahren erfordern weiterentwickelte Techniken: **differenzielle** und **lineare Kryptoanalyse** gegen Blockchiffren, **Seitenkanalangriffe** auf Implementierungen (→ Modul 12) sowie mathematische Angriffe auf asymmetrische Verfahren (Faktorisierung, diskreter Logarithmus). Das Grundmotiv bleibt identisch: jede ausnutzbare Struktur aufspüren.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Kryptoanalyse bricht Verfahren bzw. rekonstruiert Schlüssel – Prüfstein jeder Chiffre
> - Angriffe nutzen Statistik, kleinen Schlüsselraum, Struktur oder Bedienfehler
> - Klassische Techniken: Brute Force, Häufigkeitsanalyse, Kasiski, Anagramming, Cribs
> - Moderne Chiffren zielen auf eine von Zufall ununterscheidbare Ausgabe

---

## Übungen

1. Grenzen Sie Kryptographie und Kryptoanalyse voneinander ab.
2. Ordnen Sie jedem klassischen Verfahren dieses Moduls die passende Angriffstechnik zu.
3. Warum ist „nicht von Zufall unterscheidbar" das Ziel moderner Chiffren?

---

← [[05-Haeufigkeitsanalyse|← Zurück]] | [[00-Klassisch-Index|Übersicht]] | [[00-Symmetrisch-Index|Nächstes Modul →]]
