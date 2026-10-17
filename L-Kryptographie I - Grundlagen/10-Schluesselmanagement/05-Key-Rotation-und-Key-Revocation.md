---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - schluessel
---

# Key Rotation und Key Revocation

> [!info] **Lernziele**
> - Zweck und Ablauf der Schlüsselrotation verstehen
> - Schlüsselwiderruf (Revocation) einordnen
> - Den Umgang mit kompromittierten Schlüsseln kennen

---

## Inhalt

### Key Rotation

**Key Rotation** bedeutet, Schlüssel in regelmäßigen Abständen durch neue zu ersetzen. Gründe:

- **Schadensbegrenzung:** Ein unentdeckt kompromittierter Schlüssel ist nur bis zur nächsten Rotation nutzbar.
- **Kryptoperiode begrenzen:** Je weniger Daten mit einem Schlüssel verschlüsselt wurden, desto geringer das Risiko (z. B. Geburtstagsgrenzen bei Blockchiffren).
- **Compliance:** Viele Richtlinien schreiben Rotation vor.

Mit **Envelope Encryption** (KEK/DEK, → [[03-Schluesselverteilung-und-Speicherung]]) ist Rotation effizient: Rotiert man den KEK, muss nur der verschlüsselte DEK neu verschlüsselt werden, nicht alle Daten.

### Key Revocation

**Revocation** erklärt einen Schlüssel/ein Zertifikat vorzeitig für ungültig – etwa bei Kompromittierung, Mitarbeiteraustritt oder fehlerhafter Ausstellung. Mechanismen bei Zertifikaten: **CRL** und **OCSP** (→ Modul 8).

### Reaktion auf Kompromittierung

> [!danger] **Incident-Ablauf bei Schlüsselkompromittierung**
> 1. **Sperren/Widerrufen** des betroffenen Schlüssels (Revocation).
> 2. **Neuen Schlüssel** erzeugen und ausrollen (Rotation).
> 3. **Betroffene Daten** neu verschlüsseln bzw. neu signieren.
> 4. **Analyse:** Umfang des Schadens ermitteln (welche Daten/Sitzungen betroffen).
> Perfect Forward Secrecy (→ [[06-Perfect-Forward-Secrecy]]) begrenzt dabei den Schaden auf aktuelle statt vergangene Sitzungen.

### Praxis

- **Automatisierung** ist essenziell – manuelle Rotation wird oft vergessen (vgl. ACME für Zertifikate, → Modul 8).
- **Übergangsphasen** einplanen: alter und neuer Schlüssel müssen kurzzeitig parallel gültig sein, damit nichts bricht.
- **Schlüsselversionierung:** Chiffretexte vermerken, mit welcher Schlüsselversion sie erzeugt wurden.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Rotation ersetzt Schlüssel regelmäßig und begrenzt Schäden und Kryptoperioden
> - Envelope Encryption macht Rotation effizient (nur KEK/DEK neu verschlüsseln)
> - Revocation erklärt Schlüssel vorzeitig für ungültig (CRL/OCSP bei Zertifikaten)
> - Bei Kompromittierung: widerrufen, rotieren, Daten neu schützen, analysieren

---

## Übungen

1. Nennen Sie zwei Gründe für regelmäßige Schlüsselrotation.
2. Wie vereinfacht Envelope Encryption die Rotation?
3. Welche Schritte umfasst die Reaktion auf einen kompromittierten Schlüssel?

---

← [[04-Key-Derivation-Functions-KDF|← Zurück]] | [[00-Schluessel-Index|Übersicht]] | [[06-Hardware-Security-Modules-HSM|Weiter →]]
