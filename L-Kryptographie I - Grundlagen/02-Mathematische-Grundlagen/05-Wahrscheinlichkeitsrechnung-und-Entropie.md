---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - mathematik
---

# Wahrscheinlichkeitsrechnung und Entropie

> [!info] **Lernziele**
> - Grundbegriffe der Wahrscheinlichkeit für die Kryptographie anwenden
> - Entropie als Maß für Unsicherheit und Zufall verstehen
> - Die Bedeutung guter Zufallsquellen und von Schlüsselstärke einschätzen

---

## Inhalt

### Wahrscheinlichkeit in der Kryptographie

Viele kryptographische Aussagen sind **probabilistisch**: Ein Angreifer soll einen Schlüssel nur mit *vernachlässigbarer* Wahrscheinlichkeit erraten. Zentral ist die **Gleichverteilung**: Ein Schlüssel aus $k$ Bit ist nur dann maximal sicher, wenn jeder der $2^k$ Werte gleich wahrscheinlich ist.

Ein wichtiges Werkzeug ist das **Geburtstagsparadoxon**: In einer Menge von etwa $\sqrt{N}$ zufälligen Werten aus $N$ Möglichkeiten tritt mit hoher Wahrscheinlichkeit eine Kollision auf. Daraus folgt: Eine Hashfunktion mit $n$-Bit-Ausgabe bietet nur etwa $n/2$ Bit Kollisionssicherheit (→ Modul 6).

### Entropie

Die **Shannon-Entropie** misst die mittlere Unsicherheit einer Zufallsvariablen $X$ in Bit:

$$H(X) = -\sum_{i} p_i \log_2 p_i$$

- Maximal ist die Entropie bei **Gleichverteilung**: für $N$ gleich wahrscheinliche Werte ist $H = \log_2 N$.
- Je vorhersehbarer eine Quelle, desto niedriger die Entropie.

Beispiel: Ein fairer Münzwurf hat $H = 1$ Bit. Eine Münze, die zu 90 % Kopf zeigt, hat nur $H \approx 0{,}47$ Bit – deutlich weniger Zufall.

### Entropie und Schlüsselstärke

Die Entropie beziffert die **effektive** Schlüsselstärke. Ein 128-Bit-Schlüssel aus einem schlechten Zufallsgenerator mit nur 40 Bit echter Entropie bietet auch nur 40 Bit Sicherheit – angreifbar trotz formal „128 Bit".

> [!danger] **Schwache Zufallsquellen**
> Reale Sicherheitsvorfälle entstanden durch unzureichende Entropie bei der Schlüsselerzeugung (z. B. der Debian-OpenSSL-Bug 2008, bei dem der Schlüsselraum drastisch schrumpfte). Kryptographische Schlüssel müssen aus einem **CSPRNG** (kryptographisch sicherer Zufallsgenerator) stammen.

### Passwörter und Entropie

Auch die Stärke von Passwörtern misst man in Entropie-Bits. Ein zufälliges Passwort aus einem Zeichenvorrat der Größe $z$ und Länge $\ell$ hat $\ell \cdot \log_2 z$ Bit Entropie. Menschlich gewählte Passwörter haben meist viel weniger, weil sie nicht gleichverteilt sind.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Sicherheit wird oft probabilistisch definiert; Gleichverteilung ist ideal
> - Entropie $H(X) = -\sum p_i \log_2 p_i$ misst Unsicherheit in Bit
> - Effektive Schlüsselstärke = tatsächliche Entropie, nicht nominelle Bitlänge
> - Das Geburtstagsparadoxon halbiert die Kollisionssicherheit von Hashes

---

## Übungen

1. Berechnen Sie die Entropie eines fairen Würfels (6 gleich wahrscheinliche Seiten).
2. Wie viele Bit Entropie hat ein zufälliges 12-Zeichen-Passwort aus 94 druckbaren ASCII-Zeichen?
3. Warum bietet eine 256-Bit-Hashfunktion nur etwa 128 Bit Kollisionssicherheit?

---

← [[04-Gruppen-Ringe-und-endliche-Koerper|← Zurück]] | [[00-Mathematik-Index|Übersicht]] | [[06-Komplexitaetstheorie|Weiter →]]
