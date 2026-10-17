---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - hash
---

# Kollisionsresistenz und Preimage-Resistenz

> [!info] **Lernziele**
> - Urbild-, Zweite-Urbild- und Kollisionsresistenz präzise unterscheiden
> - Den Einfluss des Geburtstagsparadoxons auf die Sicherheit verstehen
> - Die praktische Bedeutung gebrochener Resistenzen einordnen

---

## Inhalt

### Die drei Resistenzbegriffe

| Begriff | Angreifer-Aufgabe | Aufwand (n-Bit-Hash) |
|---------|-------------------|----------------------|
| **Urbildresistenz** | zu gegebenem $h$ ein $m$ mit $H(m)=h$ finden | $2^{n}$ |
| **Zweite-Urbildresistenz** | zu gegebenem $m_1$ ein $m_2 \neq m_1$ mit gleichem Hash finden | $2^{n}$ |
| **Kollisionsresistenz** | *irgendein* Paar $m_1 \neq m_2$ mit gleichem Hash finden | $2^{n/2}$ |

Der entscheidende Unterschied: Bei den Urbild-Varianten ist der Hashwert bzw. die Nachricht **vorgegeben**. Bei einer Kollision darf der Angreifer **beide** Nachrichten frei wählen – das ist deutlich leichter.

### Das Geburtstagsparadoxon

Warum ist Kollisionsresistenz nur $2^{n/2}$ statt $2^{n}$ wert? Wegen des **Geburtstagsparadoxons** (→ [[05-Wahrscheinlichkeitsrechnung-und-Entropie]]): In einer Menge von etwa $\sqrt{N} = 2^{n/2}$ zufälligen Hashwerten wird mit hoher Wahrscheinlichkeit eine Kollision auftreten.

**Konsequenz:** Eine $n$-Bit-Hashfunktion bietet nur **$n/2$ Bit Kollisionssicherheit**. Für 128 Bit Kollisionssicherheit braucht man daher einen **256-Bit-Hash** (z. B. SHA-256).

### Hierarchie der Eigenschaften

Kollisionsresistenz ist die stärkste Anforderung: Wer Kollisionsresistenz bricht, gefährdet damit noch nicht zwingend die Urbildresistenz, aber Kollisionsresistenz impliziert (unter üblichen Annahmen) Zweite-Urbildresistenz.

### Praktische Bedeutung

> [!danger] **Reale Kollisionsangriffe auf veraltete Hashes**
> - **MD4** (1990, 128 Bit): schon früh gebrochen, Kollisionen praktisch sofort berechenbar – vollständig obsolet (noch in Altprotokollen wie NTLM anzutreffen).
> - **MD5** (1992, 128 Bit): Kollisionen in Sekunden erzeugbar; 2008 wurde ein gefälschtes CA-Zertifikat demonstriert, 2012 nutzte die Schadsoftware **Flame** MD5-Kollisionen.
> - **SHA-1** (1995, 160 Bit): 2017 erste praktische Kollision („SHAttered") durch Google/CWI; seitdem für Signaturen verboten.
>
> Diese Verfahren sind zu kurz (128/160 Bit → nur 64/80 Bit Kollisionssicherheit) **und** strukturell schwach. Für Sicherheitszwecke sind sie durch SHA-2, SHA-3 oder BLAKE2/3 zu ersetzen.
>
> Kollisionsresistenz ist besonders für **digitale Signaturen** kritisch: Kann ein Angreifer zwei Dokumente mit gleichem Hash erzeugen, lässt sich eine Signatur von einem harmlosen auf ein schädliches Dokument übertragen.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Urbild-/Zweite-Urbildresistenz: $2^n$ Aufwand; Kollisionsresistenz nur $2^{n/2}$
> - Grund für $n/2$: Geburtstagsparadoxon – daher 256-Bit-Hash für 128 Bit Sicherheit
> - Kollisionsresistenz ist die stärkste und für Signaturen kritische Eigenschaft
> - MD4, MD5 und SHA-1 sind durch praktische Kollisionen gebrochen – nicht mehr verwenden

---

## Übungen

1. Worin unterscheidet sich eine Kollision von einem zweiten Urbild?
2. Wie viele Bit Kollisionssicherheit bietet SHA-512?
3. Warum ist Kollisionsresistenz speziell für digitale Signaturen so wichtig?

---

← [[03-BLAKE2-und-BLAKE3|← Zurück]] | [[00-Hashfunktionen-Index|Übersicht]] | [[05-Message-Authentication-Codes-MAC-HMAC|Weiter →]]
