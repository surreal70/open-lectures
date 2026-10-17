---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - advanced
  - vertiefung
---

# Homomorphe Verschlüsselung

> [!info] **Lernziele**
> - Das Prinzip homomorpher Verschlüsselung verstehen
> - Erkennen, warum „Rechnen auf verschlüsselten Daten" revolutionär ist
> - Anwendungsfälle einordnen

---

## Inhalt

### Die zentrale Idee

**Homomorphe Verschlüsselung (HE)** erlaubt es, **Berechnungen direkt auf verschlüsselten Daten** durchzuführen – ohne sie zu entschlüsseln. Das Ergebnis bleibt verschlüsselt und ergibt beim Entschlüsseln genau das, was die Berechnung auf den Klartexten geliefert hätte.

$$\text{Dec}\big(\; f(\text{Enc}(a), \text{Enc}(b))\;\big) = f(a, b)$$

### Warum ist das besonders?

> [!tip] **Rechnen, ohne zu sehen**
> Ein Cloud-Dienst könnte sensible Daten (z. B. Gesundheitsdaten) **verarbeiten**, ohne sie je im Klartext zu sehen. Vertraulichkeit bleibt während der gesamten Verarbeitung erhalten – ein Schutz des Zustands **„in use"**, nicht nur at rest oder in transit (→ [[08-Kryptographie-in-Cloud-Umgebungen]]).

### Ein einfaches Beispiel

Manche klassischen Verfahren sind **teilweise** homomorph:

- **RSA** ist multiplikativ homomorph: $\text{Enc}(a) \cdot \text{Enc}(b) = \text{Enc}(a \cdot b)$.
- **Paillier** ist additiv homomorph: $\text{Enc}(a) \cdot \text{Enc}(b) = \text{Enc}(a + b)$.

Die Abstufungen (teilweise vs. voll homomorph) behandelt das nächste Kapitel (→ [[02-Partially-vs-Fully-Homomorphic-Encryption]]).

### Grundlage und Grenzen

Moderne (voll) homomorphe Verfahren beruhen auf **gitterbasierter Kryptographie** (→ [[05-Gitterbasierte-Kryptographie]]) und sind damit zugleich quantenresistent.

> [!warning] **Hoher Aufwand**
> Der große Nachteil ist die **Performance**: Vollständig homomorphe Berechnungen sind um Größenordnungen langsamer als Klartextberechnungen. HE ist daher (noch) auf spezifische, hochsensible Anwendungen beschränkt.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Homomorphe Verschlüsselung erlaubt Rechnen auf verschlüsselten Daten
> - Entschlüsseltes Ergebnis = Berechnung auf den Klartexten
> - Schützt Daten „in use"; RSA/Paillier sind teilweise homomorph
> - Basis moderner Verfahren ist gitterbasiert (quantenresistent), aber sehr rechenintensiv

---

## Übungen

1. Was ermöglicht homomorphe Verschlüsselung grundsätzlich?
2. Nennen Sie je ein multiplikativ und ein additiv homomorphes Verfahren.
3. Warum wird HE trotz ihrer Mächtigkeit noch wenig eingesetzt?

---

← [[00-Advanced-Index|Übersicht]] | [[02-Partially-vs-Fully-Homomorphic-Encryption|Weiter →]]
