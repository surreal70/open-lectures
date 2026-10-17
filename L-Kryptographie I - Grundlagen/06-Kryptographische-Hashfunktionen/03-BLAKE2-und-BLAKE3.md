---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - hash
---

# BLAKE2 und BLAKE3

> [!info] **Lernziele**
> - BLAKE2 und BLAKE3 als moderne Hashfunktionen einordnen
> - Ihre Geschwindigkeits- und Designvorteile verstehen
> - Wissen, wann sie gegenüber SHA-2/SHA-3 sinnvoll sind

---

## Inhalt

### Herkunft

**BLAKE2** und **BLAKE3** sind moderne kryptographische Hashfunktionen, hervorgegangen aus BLAKE, einem der Finalisten des SHA-3-Wettbewerbs. Ihr Hauptargument: sehr hohe **Geschwindigkeit** bei gleichzeitig hoher Sicherheit.

### BLAKE2

BLAKE2 (2012) ist in Software oft **schneller als MD5, SHA-1, SHA-2 und SHA-3** – und dabei sicher. Zwei Varianten:

- **BLAKE2b:** optimiert für 64-Bit-Plattformen, bis 512 Bit Ausgabe.
- **BLAKE2s:** optimiert für 8- bis 32-Bit-Plattformen.

BLAKE2 bietet eingebaute Funktionen für Schlüsselung (als MAC), Personalisierung und Baum-Hashing – ohne die Length-Extension-Schwäche von SHA-2.

### BLAKE3

BLAKE3 (2020) treibt das Konzept weiter:

- **Extrem schnell** durch massive **Parallelisierung** (interne Baumstruktur / Merkle-Tree).
- **Eine** Funktion statt vieler Varianten; Ausgabe beliebig lang (XOF – extendable output function).
- Nutzbar als Hash, MAC (mit Schlüssel) und Key-Derivation-Function.

Die interne Baumstruktur erlaubt es, große Datenmengen über mehrere CPU-Kerne parallel zu verarbeiten – ein deutlicher Vorteil bei großen Dateien.

### Einordnung

| Funktion | Jahr | Stärke |
|----------|------|--------|
| BLAKE2 | 2012 | schnell, vielseitig, sicher |
| BLAKE3 | 2020 | maximale Geschwindigkeit, parallelisierbar, XOF |

> [!note] **Standardisierung**
> SHA-2 und SHA-3 sind durch NIST (FIPS) standardisiert und daher oft in Compliance-Kontexten vorgeschrieben. BLAKE2/3 sind nicht NIST-standardisiert, aber kryptographisch anerkannt und weit verbreitet (z. B. in vielen Tools und Protokollen). Die Wahl hängt oft von regulatorischen Anforderungen ab (→ Modul 14).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - BLAKE2/3 sind moderne, sehr schnelle und sichere Hashfunktionen
> - BLAKE2 (b/s) ist schneller als SHA-2/3 und ohne Length-Extension-Schwäche
> - BLAKE3 ist stark parallelisierbar und eine XOF (beliebige Ausgabelänge)
> - Nicht NIST-standardisiert → in Compliance-Kontexten SHA-2/3 bevorzugen

---

## Übungen

1. Was unterscheidet BLAKE2b von BLAKE2s?
2. Welche Eigenschaft macht BLAKE3 bei großen Dateien besonders schnell?
3. Wann würden Sie trotz BLAKE3 lieber SHA-2 oder SHA-3 einsetzen?

---

← [[02-SHA-2-und-SHA-3|← Zurück]] | [[00-Hashfunktionen-Index|Übersicht]] | [[04-Kollisionsresistenz-und-Preimage-Resistenz|Weiter →]]
