---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - architektur
  - vertiefung
---

# Defense in Depth mit Kryptographie

> [!info] **Lernziele**
> - Das Prinzip Defense in Depth verstehen
> - Kryptographie als eine von mehreren Schichten einordnen
> - Schichten sinnvoll kombinieren

---

## Inhalt

### Das Prinzip

**Defense in Depth** bedeutet, Sicherheit durch **mehrere, unabhängige Schichten** zu erreichen, statt sich auf eine einzige Maßnahme zu verlassen. Fällt eine Schicht aus, schützen die anderen weiter.

> [!tip] **Kryptographie ist eine Schicht, nicht die Lösung**
> Verschlüsselung allein macht kein System sicher. Sie ist **eine** Schicht neben Zugriffskontrolle, Netzwerksicherheit, Monitoring, sicherer Softwareentwicklung und organisatorischen Maßnahmen. Ein System mit perfekter Krypto, aber offenem Zugriff oder verwundbarem Code ist unsicher.

### Kryptographische Schichten kombinieren

Mehrere Krypto-Maßnahmen können sich ergänzen:

| Ebene | Maßnahme |
|-------|----------|
| Transport | TLS (→ Modul 9) |
| Speicher | Festplatten-/DB-Verschlüsselung (→ Modul 11) |
| Anwendung | Feld-/E2E-Verschlüsselung sensibler Daten |
| Schlüssel | HSM/KMS, Rotation (→ Modul 10) |
| Nachweise | Signaturen, Zertifikate, CT (→ Modul 7–8) |

So bleiben Daten z. B. selbst dann geschützt, wenn eine einzelne Schicht (etwa die Festplattenverschlüsselung bei laufendem System) umgangen wird.

### Beispiel: zusammenwirkende Schichten

> [!example] **Mehrschichtiger Schutz**
> Patientendaten werden applikationsseitig verschlüsselt (Betreiber sieht nur Chiffretext), **zusätzlich** über TLS übertragen, **zusätzlich** in einer verschlüsselten DB gespeichert, mit Schlüsseln im HSM und Zugriff nur über authentifizierte, protokollierte Wege. Kein einzelner Fehler kompromittiert alles.

### Abgrenzung: keine Redundanz um der Redundanz willen

> [!warning] **Angemessenheit**
> Defense in Depth heißt nicht „so viele Krypto-Schichten wie möglich". Jede Schicht muss einen **realen** Teil des Bedrohungsmodells (→ [[01-Threat-Modeling-fuer-Kryptographie]]) abdecken. Unnötige Komplexität ist selbst eine Fehlerquelle.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Defense in Depth = mehrere unabhängige Schutzschichten
> - Kryptographie ist eine Schicht neben Zugriffskontrolle, Netz, Monitoring, SecDev
> - Krypto-Ebenen (Transport, Speicher, Anwendung, Schlüssel, Nachweise) ergänzen sich
> - Schichten am Bedrohungsmodell ausrichten, nicht beliebig stapeln

---

## Übungen

1. Was bedeutet Defense in Depth?
2. Warum genügt Verschlüsselung allein nicht für ein sicheres System?
3. Nennen Sie drei kryptographische Schichten, die sich ergänzen können.

---

← [[04-Kryptographie-Migration-Strategien|← Zurück]] | [[00-Architektur-Index|Übersicht]] | [[06-Kryptographie-in-Microservices|Weiter →]]
