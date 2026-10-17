---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - zkp
  - vertiefung
---

# zk-STARKs

> [!info] **Lernziele**
> - zk-STARKs verstehen und von zk-SNARKs abgrenzen
> - Die Vorteile (kein Trusted Setup, quantenresistent) einordnen
> - Die Abwägungen kennen

---

## Inhalt

### Was bedeutet zk-STARK?

**zk-STARK** steht für **Zero-Knowledge Scalable Transparent ARgument of Knowledge**. Es ist eine Weiterentwicklung, die zwei Schwächen der SNARKs adressiert:

| Teil | Bedeutung |
|------|-----------|
| **Scalable** | effizient auch für sehr große Berechnungen; Prüfung skaliert gut |
| **Transparent** | **kein Trusted Setup** nötig |

### Die zwei Hauptvorteile

> [!tip] **Transparent und quantenresistent**
> 1. **Kein Trusted Setup:** zk-STARKs nutzen nur öffentliche Zufälligkeit – es gibt keinen „toxic waste" und damit keinen kritischen Vertrauenspunkt (anders als bei vielen SNARKs, → [[03-zk-SNARKs]]).
> 2. **Quantenresistent:** Sie beruhen ausschließlich auf **Hashfunktionen** (keine elliptischen Kurven/Pairings), sind also durch Shor nicht bedroht (→ Modul 13).

### Die Abwägung

| Aspekt | zk-SNARK | zk-STARK |
|--------|----------|----------|
| Trusted Setup | oft nötig | **nein** |
| Beweisgröße | sehr klein (~Hunderte Byte) | **größer** (KB bis zweistellige KB) |
| Quantenresistenz | nein (ECC/Pairings) | **ja** (nur Hashes) |
| Prüfzeit | sehr schnell | schnell, skaliert gut |

Der Preis für Transparenz und Quantenresistenz sind **größere Beweise**.

### Einsatz

zk-STARKs werden u. a. in **Ethereum-Skalierungslösungen** (StarkNet/StarkEx) eingesetzt, wo das Fehlen eines Trusted Setup und die Skalierbarkeit besonders geschätzt werden.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - zk-STARK: skalierbar und transparent (kein Trusted Setup)
> - Beruht nur auf Hashfunktionen → quantenresistent
> - Nachteil gegenüber SNARKs: größere Beweise
> - Einsatz in Ethereum-Skalierung (StarkNet/StarkEx)

---

## Übungen

1. Wofür stehen die Buchstaben in „zk-STARK"?
2. Welche zwei Hauptvorteile bieten STARKs gegenüber SNARKs?
3. Welcher Nachteil steht diesen Vorteilen gegenüber?

---

← [[03-zk-SNARKs|← Zurück]] | [[00-ZKP-Index|Übersicht]] | [[05-Anwendungsfaelle-ZKP|Weiter →]]
