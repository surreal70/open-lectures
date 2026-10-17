---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - asymmetrisch
  - public-key
---

# Elliptische-Kurven-Kryptographie ECC

> [!info] **Lernziele**
> - Das Grundprinzip elliptischer Kurven in der Kryptographie verstehen
> - Den Vorteil kürzerer Schlüssel gegenüber RSA einordnen
> - Das ECDLP als Sicherheitsgrundlage kennen

---

## Inhalt

### Was sind elliptische Kurven?

Die **Elliptische-Kurven-Kryptographie (ECC)** nutzt die Punkte einer elliptischen Kurve über einem endlichen Körper. Eine solche Kurve hat (über $\mathbb{R}$ anschaulich) die Form:

$$y^2 = x^3 + ax + b$$

Über einem endlichen Körper $\mathrm{GF}(p)$ (→ [[04-Gruppen-Ringe-und-endliche-Koerper]]) bilden die Kurvenpunkte zusammen mit einem „Punkt im Unendlichen" eine **abelsche Gruppe**. Auf dieser Gruppe definiert man eine **Punktaddition** – geometrisch über Sekante/Tangente, algebraisch über Formeln.

### Skalarmultiplikation als Einwegfunktion

Die zentrale Operation ist die **Skalarmultiplikation**: einen Punkt $P$ $k$-mal zu sich selbst addieren,

$$Q = k \cdot P.$$

- **Leicht:** $Q$ aus $k$ und $P$ berechnen (per Double-and-Add).
- **Schwer:** $k$ aus $Q$ und $P$ zurückgewinnen – das **Elliptic Curve Discrete Logarithm Problem (ECDLP)**.

Hier ist $k$ der private Schlüssel, $Q$ der öffentliche.

### Der Vorteil: kürzere Schlüssel

Für das ECDLP sind keine subexponentiellen Angriffe bekannt (anders als bei der Faktorisierung). Dadurch bietet ECC **gleiche Sicherheit bei deutlich kürzeren Schlüsseln**:

| Sicherheitsniveau | RSA | ECC |
|-------------------|-----|-----|
| 128 Bit | 3072 Bit | 256 Bit |
| 256 Bit | 15360 Bit | 512 Bit |

Kürzere Schlüssel bedeuten weniger Rechenaufwand, Speicher und Bandbreite – ideal für Mobilgeräte, Smartcards und IoT.

### Standardkurven

Verbreitete Kurven sind die NIST-Kurven (z. B. **P-256**) sowie die modernen, von Bernstein entworfenen Kurven **Curve25519** (für Schlüsselaustausch, → [[05-ECDH-und-X25519]]) und **Ed25519** (für Signaturen, → Modul 7).

> [!tip] **Quantenbedrohung**
> Wie RSA ist auch ECC durch den Shor-Algorithmus gefährdet. ECC gilt sogar als etwas **leichter** für Quantenangriffe (kleinere Parameter), weshalb der Übergang zu Post-Quanten-Verfahren wichtig ist (→ Modul 13).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - ECC rechnet in der Gruppe der Punkte einer elliptischen Kurve über $\mathrm{GF}(p)$
> - Skalarmultiplikation $Q = kP$ ist leicht, das Umkehren (ECDLP) schwer
> - Gleiche Sicherheit wie RSA bei viel kürzeren Schlüsseln (256 Bit ≈ RSA-3072)
> - Moderne Kurven: Curve25519 (Austausch), Ed25519 (Signatur); quantengefährdet

---

## Übungen

1. Welche Operation bildet die kryptographische Einwegfunktion bei ECC?
2. Welche RSA-Schlüssellänge entspricht etwa einem 256-Bit-ECC-Schlüssel?
3. Nennen Sie je eine moderne Kurve für Schlüsselaustausch und für Signaturen.

---

← [[03-Diffie-Hellman-Schlüsselaustausch|← Zurück]] | [[00-Asymmetrisch-Index|Übersicht]] | [[05-ECDH-und-X25519|Weiter →]]
