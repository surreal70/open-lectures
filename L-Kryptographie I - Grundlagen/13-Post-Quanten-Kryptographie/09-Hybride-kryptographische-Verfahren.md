---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - pqc
---

# Hybride kryptographische Verfahren

> [!info] **Lernziele**
> - Das Prinzip hybrider PQC-Verfahren verstehen
> - Die Begründung für den hybriden Ansatz nachvollziehen
> - Konkrete Beispiele einordnen

---

## Inhalt

### Die Idee

Ein **hybrides Verfahren** kombiniert ein **klassisches** (z. B. X25519/ECDH) mit einem **Post-Quanten**-Verfahren (z. B. ML-KEM). Der resultierende Sitzungsschlüssel wird aus **beiden** Anteilen abgeleitet.

```
gemeinsames Geheimnis = KDF( X25519-Anteil  ||  ML-KEM-Anteil )
```

### Warum hybrid?

> [!tip] **Sicher, solange eines hält**
> Der hybride Schlüssel bleibt sicher, solange **mindestens eines** der beiden Verfahren sicher ist:
> - Wird das junge PQC-Verfahren gebrochen (es ist neu, vgl. SIKE-Bruch → [[04-Post-Quanten-Kryptographie-Ueberblick]]), schützt noch das bewährte klassische.
> - Kommt der Quantencomputer, schützt das PQC-Verfahren, während das klassische fällt.
>
> Man setzt also nicht alles auf eine Karte – ideal für die unsichere Übergangsphase.

### Konkrete Beispiele

- **X25519MLKEM768** – hybrider Schlüsselaustausch in **TLS 1.3**, bereits in Browsern/Servern verbreitet.
- **Hybride Zertifikate/Signaturen:** klassische + PQC-Signatur parallel.
- **SSH** und VPNs integrieren zunehmend hybride KEX-Methoden.

### Abwägung

| Vorteil | Nachteil |
|---------|----------|
| Sicherheit solange ein Verfahren hält | größere Schlüssel/Handshakes |
| sanfter Migrationspfad | etwas mehr Rechenaufwand |
| Schutz gegen „harvest now, decrypt later" | höhere Komplexität |

Angesichts der Jugend der PQC-Verfahren empfehlen NIST und BSI für die Übergangszeit überwiegend **hybride** Lösungen.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Hybrid = klassisches + PQC-Verfahren, Schlüssel aus beiden Anteilen abgeleitet
> - Sicher, solange mindestens eines der beiden Verfahren hält
> - Beispiel: X25519MLKEM768 in TLS 1.3
> - Empfohlener Migrationspfad; Nachteil: größere Handshakes, mehr Komplexität

---

## Übungen

1. Wie entsteht der Sitzungsschlüssel bei einem hybriden Verfahren?
2. Warum ist der hybride Ansatz in der Übergangsphase besonders sinnvoll?
3. Nennen Sie ein konkretes hybrides Verfahren aus TLS 1.3.

---

← [[08-SLH-DSA-FIPS-205|← Zurück]] | [[00-PQC-Index|Übersicht]] | [[10-Migration-zu-quantenresistenten-Systemen|Weiter →]]
