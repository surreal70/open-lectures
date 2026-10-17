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

# Partially vs Fully Homomorphic Encryption

> [!info] **Lernziele**
> - Die Abstufungen homomorpher Verschlüsselung unterscheiden
> - Den Durchbruch der vollhomomorphen Verschlüsselung einordnen
> - Die Rolle des „Bootstrapping" verstehen

---

## Inhalt

### Die Abstufungen

Nicht jede homomorphe Verschlüsselung erlaubt beliebige Berechnungen. Man unterscheidet:

| Typ | Erlaubte Operationen |
|-----|----------------------|
| **PHE** (Partially Homomorphic) | **eine** Operation beliebig oft (nur + oder nur ·) |
| **SHE** (Somewhat Homomorphic) | beide Operationen, aber nur **begrenzt** oft |
| **FHE** (Fully Homomorphic) | **beliebige** Berechnungen, unbegrenzt |

### PHE – teilweise homomorph

Beispiele (→ [[01-Homomorphe-Verschluesselung]]):

- **RSA/ElGamal:** nur Multiplikation.
- **Paillier:** nur Addition.

Nützlich für eng umrissene Aufgaben (z. B. verschlüsselte Summenbildung bei Wahlen/Statistik).

### Das Rauschproblem und SHE

Gitterbasierte HE fügt bei der Verschlüsselung **Rauschen** hinzu (LWE, → [[05-Gitterbasierte-Kryptographie]]). Jede Operation **vergrößert** das Rauschen. Wird es zu groß, ist korrektes Entschlüsseln unmöglich. Daher erlaubt **SHE** nur eine begrenzte Anzahl Operationen.

### FHE und Bootstrapping

> [!tip] **Gentrys Durchbruch (2009)**
> Craig Gentry zeigte die erste **vollhomomorphe** Verschlüsselung. Der Schlüsseltrick ist **Bootstrapping**: Das Verfahren entschlüsselt den Chiffretext **homomorph** (mit einem verschlüsselten Schlüssel) und „frischt" ihn dadurch auf – das Rauschen wird zurückgesetzt. So lassen sich beliebig viele Operationen verketten.

Bootstrapping ist allerdings **sehr teuer**, weshalb FHE in der Praxis noch langsam ist. Moderne Schemata (BGV, BFV, CKKS, TFHE) verbessern die Effizienz schrittweise.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - PHE: eine Operation beliebig oft; SHE: beide, aber begrenzt; FHE: beliebige Berechnungen
> - Gitterbasierte HE arbeitet mit Rauschen, das bei Operationen wächst
> - FHE (Gentry 2009) nutzt Bootstrapping, um das Rauschen zurückzusetzen
> - Bootstrapping ist mächtig, aber rechenintensiv (BGV/BFV/CKKS/TFHE optimieren)

---

## Übungen

1. Grenzen Sie PHE, SHE und FHE voneinander ab.
2. Warum begrenzt das Rauschen die Zahl der Operationen bei SHE?
3. Was leistet Bootstrapping bei FHE?

---

← [[01-Homomorphe-Verschluesselung|← Zurück]] | [[00-Advanced-Index|Übersicht]] | [[03-Multi-Party-Computation-MPC|Weiter →]]
