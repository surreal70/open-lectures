---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - pqc
---

# Gitterbasierte Kryptographie

> [!info] **Lernziele**
> - Das Grundprinzip gitterbasierter Kryptographie verstehen
> - Die zugrunde liegenden harten Probleme (LWE/SIS) einordnen
> - Verstehen, warum Gitter die Basis der NIST-Standards sind

---

## Inhalt

### Was ist ein Gitter?

Ein **Gitter (Lattice)** ist die Menge aller ganzzahligen Linearkombinationen von Basisvektoren – anschaulich ein regelmäßiges Punktraster, das sich in viele Dimensionen erstreckt. Kryptographie nutzt Gitter in **hunderten** Dimensionen.

### Die harten Probleme

Die Sicherheit beruht auf Problemen, die auch für Quantencomputer schwer sind:

| Problem | Kurzbeschreibung |
|---------|------------------|
| **SVP** (Shortest Vector) | den kürzesten Vektor im Gitter finden |
| **CVP** (Closest Vector) | den dem Zielpunkt nächsten Gitterpunkt finden |
| **LWE** (Learning With Errors) | lineare Gleichungen mit kleinem Rauschen lösen |
| **SIS** (Short Integer Solution) | eine kurze Lösung eines Gleichungssystems finden |

**LWE** ist besonders wichtig: Man addiert zu linearen Gleichungen kleine zufällige **Fehler**, wodurch das Lösen praktisch unmöglich wird – selbst mit Quantencomputern.

### Warum Gitter?

> [!tip] **Vorteile gitterbasierter Verfahren**
> - **Quantenresistenz:** kein effizienter (Quanten-)Algorithmus für LWE/SIS bekannt.
> - **Vielseitigkeit:** eignen sich für Verschlüsselung, Schlüsselkapselung, Signaturen – und sogar **homomorphe Verschlüsselung** (→ Modul 18).
> - **Effizienz:** akzeptable Schlüssel-/Chiffregrößen und gute Performance.
> - **Beweisbare Sicherheit:** teils auf Worst-Case-Gitterprobleme reduzierbar.

Deshalb basieren **zwei der drei** NIST-Standards (ML-KEM und ML-DSA) auf Gittern.

### Nachteil

Gegenüber ECC sind Schlüssel und Chiffretexte **größer** (Kilobyte statt Bytes). Das ist in den meisten Anwendungen vertretbar, kann aber bei sehr beschränkten Geräten/Protokollen relevant werden.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Gitter sind hochdimensionale Punktraster aus Basisvektoren
> - Harte Probleme: SVP, CVP, LWE, SIS – auch quantenresistent
> - LWE (lineare Gleichungen mit Rauschen) ist die zentrale Grundlage
> - Vielseitig und effizient → Basis von ML-KEM und ML-DSA; Nachteil: größere Schlüssel

---

## Übungen

1. Was ist ein Gitter im kryptographischen Sinn?
2. Erklären Sie die Grundidee des LWE-Problems.
3. Warum sind gitterbasierte Verfahren besonders vielseitig?

---

← [[04-Post-Quanten-Kryptographie-Ueberblick|← Zurück]] | [[00-PQC-Index|Übersicht]] | [[06-ML-KEM-FIPS-203|Weiter →]]
