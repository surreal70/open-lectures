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

# Threat Modeling für Kryptographie

> [!info] **Lernziele**
> - Threat Modeling für kryptographische Systeme durchführen
> - Das STRIDE-Modell einordnen
> - Angemessene Schutzmaßnahmen ableiten

---

## Inhalt

### Warum Threat Modeling?

Bevor man Kryptographie einsetzt, muss man wissen, **wogegen** man sich schützt. **Threat Modeling** ist der strukturierte Prozess, Bedrohungen systematisch zu identifizieren und passende Gegenmaßnahmen abzuleiten – die Grundlage jeder sinnvollen Sicherheitsarchitektur.

> [!tip] **Die Kernfragen**
> 1. Was wird geschützt (Werte/Assets)?
> 2. Wer ist der Angreifer (Fähigkeiten, Motivation)?
> 3. Welche Angriffe sind möglich (Angriffsflächen)?
> 4. Welche Gegenmaßnahmen sind angemessen?

### STRIDE

Ein verbreitetes Modell ist **STRIDE** – es ordnet Bedrohungen Kategorien zu, denen jeweils Schutzziele (→ [[03-Schutzziele]]) gegenüberstehen:

| STRIDE | Bedrohung | Krypto-Gegenmaßnahme |
|--------|-----------|----------------------|
| **S**poofing | Identitätsfälschung | Authentifizierung, Signaturen |
| **T**ampering | Manipulation | MAC/AEAD, Signaturen |
| **R**epudiation | Abstreiten | digitale Signaturen (Nichtabstreitbarkeit) |
| **I**nformation Disclosure | Datenabfluss | Verschlüsselung |
| **D**enial of Service | Verfügbarkeit | (meist nicht-kryptografisch) |
| **E**levation of Privilege | Rechteausweitung | Zugriffskontrolle, Authentifizierung |

### Das Angreifermodell

Zentral ist das **Angreifermodell** (→ [[05-Kryptographische-Angriffsmodelle]]): Ist der Angreifer passiv (lauscht) oder aktiv (manipuliert)? Hat er Netzwerkzugriff, physischen Zugriff, oder ist er gar der Betreiber selbst (dann braucht es E2EE)? Die Antworten bestimmen die nötigen Verfahren.

### Angemessenheit

> [!warning] **Nicht über- und nicht unterschützen**
> Threat Modeling verhindert beides: **zu wenig** Schutz (offene Lücken) und **zu viel** (unnötige Komplexität, die selbst zur Fehlerquelle wird). Maßnahmen sollen zum tatsächlichen Risiko passen (→ [[09-Kryptographisches-Inventar-und-Risikomanagement]]).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Threat Modeling klärt vor dem Krypto-Einsatz: was, wogegen, wie
> - STRIDE kategorisiert Bedrohungen; jede hat passende (Krypto-)Gegenmaßnahmen
> - Das Angreifermodell bestimmt die nötigen Verfahren (passiv/aktiv, Betreiber = E2EE)
> - Maßnahmen risikoangemessen wählen – weder zu wenig noch zu viel

---

## Übungen

1. Welche vier Kernfragen beantwortet ein Threat Model?
2. Ordnen Sie drei STRIDE-Kategorien passende kryptographische Gegenmaßnahmen zu.
3. Warum ist das Angreifermodell für die Verfahrenswahl entscheidend?

---

← [[00-Architektur-Index|Übersicht]] | [[02-Architekturentscheidungen-Kryptographie|Weiter →]]
