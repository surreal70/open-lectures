---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - angriffe
---

# Side-Channel-Angriffe

> [!info] **Lernziele**
> - Das Konzept der Seitenkanalangriffe verstehen
> - Verschiedene Seitenkanäle kennen
> - Gegenmaßnahmen einordnen

---

## Inhalt

### Was ist ein Seitenkanal?

Ein **Seitenkanalangriff (Side-Channel Attack)** greift nicht die Mathematik an, sondern die **physische Implementierung**. Er nutzt messbare Nebeneffekte der Berechnung, die unbeabsichtigt Information über Geheimnisse preisgeben.

> [!note] **Kernidee**
> Der Algorithmus kann beweisbar sicher sein – die konkrete Hardware/Software „flüstert" das Geheimnis dennoch über einen unbeabsichtigten Kanal. Kryptoanalyse verlagert sich von der Theorie zur physischen Realität.

### Arten von Seitenkanälen

| Seitenkanal | Gemessen wird |
|-------------|---------------|
| **Timing** | Ausführungszeit (→ [[04-Timing-Angriffe]]) |
| **Power Analysis** | Stromverbrauch (SPA/DPA) |
| **Elektromagnetisch** | EM-Abstrahlung |
| **Akustisch** | Geräusche (z. B. CPU-Spulen) |
| **Cache** | Cache-Zugriffsmuster (Flush+Reload) |
| **Fehlerinjektion** | gezielt induzierte Rechenfehler (Fault Attacks) |

**Power-Analyse** (besonders **Differential Power Analysis, DPA**) ist bei Smartcards hochwirksam: Aus vielen Stromverbrauchsmessungen lässt sich statistisch der Schlüssel ableiten.

### Mikroarchitektur-Angriffe

> [!warning] **Spectre und Meltdown (2018)**
> Moderne CPUs leaken über **spekulative Ausführung** und Cache-Zustände Daten über Prozessgrenzen hinweg. Diese Mikroarchitektur-Seitenkanäle betreffen nicht nur Kryptografie, sondern die Isolation ganzer Systeme.

### Gegenmaßnahmen

- **Konstante-Zeit-Code** (keine datenabhängigen Zweige/Zugriffe).
- **Masking/Blinding:** Geheimnisse mit Zufall überlagern, sodass Messungen nichts verraten.
- **Rauschen/Abschirmung** bei Hardware (gegen Power/EM).
- **Hardware mit Seitenkanalschutz** (zertifizierte Smartcards, HSMs → [[06-Hardware-Security-Modules-HSM]]).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Seitenkanalangriffe nutzen physische Nebeneffekte statt mathematischer Schwächen
> - Kanäle: Timing, Stromverbrauch (DPA), EM, akustisch, Cache, Fehlerinjektion
> - Spectre/Meltdown zeigten Mikroarchitektur-Leaks über Prozessgrenzen
> - Abwehr: konstante Zeit, Masking/Blinding, Abschirmung, geschützte Hardware

---

## Übungen

1. Was unterscheidet einen Seitenkanalangriff von einem klassischen kryptoanalytischen Angriff?
2. Nennen Sie drei Arten von Seitenkanälen.
3. Welche Gegenmaßnahmen gibt es gegen Power-Analyse?

---

← [[04-Timing-Angriffe|← Zurück]] | [[00-Angriffe-Index|Übersicht]] | [[06-Fehlerhafte-Zufallszahlengeneratoren|Weiter →]]
