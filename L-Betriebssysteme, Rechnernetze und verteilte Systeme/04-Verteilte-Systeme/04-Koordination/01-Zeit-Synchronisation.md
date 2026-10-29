---
author: Andreas Hümmer
title: Zeit-Synchronisation in Verteilten Systemen
tags:
  - content
  - vs
  - koordination
  - zeit
  - synchronisation
created: '2026-10-07'
modified: '2026-10-29'
bereich: VS
---

# Zeit-Synchronisation in Verteilten Systemen

> [!info] Lernziele
> - Problem der Zeitsynchronisation in verteilten Systemen verstehen
> - Unterschied zwischen externer und interner Synchronisation kennen
> - Cristians und Berkeley-Algorithmus erklären können
> - Google TrueTime und dessen Bedeutung für verteilte Datenbanken verstehen
> - Grenzen physikalischer Zeitsynchronisation einordnen

> [!note] Verweis
> Für Details zum **Network Time Protocol (NTP)** mit Stratum-Hierarchie, Offset-Berechnung und Sicherheitsaspekten siehe [[../../03-Rechnernetze/04-Basisprotokolle/04-NTP|NTP – Network Time Protocol]].

## Einleitung

Zeit-Synchronisation ist eine fundamentale Herausforderung in verteilten Systemen. Da physikalische Uhren aufgrund von Quarz-Ungenauigkeiten driften, müssen Mechanismen zur Synchronisation eingesetzt werden.

> [!important] Kernkonzept
> **Physikalische Uhren driften** – keine zwei Uhren laufen exakt gleich. In verteilten Systemen, wo verschiedene Knoten basierend auf Zeitstempeln Entscheidungen treffen, kann Uhrendrift zu inkonsistenten Zuständen führen. Die Frage ist: **Externe** Synchronisation (mit einer Referenzzeit) oder **interne** Synchronisation (untereinander übereinstimmen)?

> [!example] Analogie
> Zeit-Synchronisation ist wie das Stellen von Uhren in verschiedenen Büros: Selbst wenn alle Uhren morgens synchronisiert werden, gehen sie abends unterschiedlich – manche vor, manche nach. Ein Mitarbeiter, der um 17:00 Uhr einen Bericht abschickt, könnte laut der Uhr eines anderen Büros "aus der Zukunft" senden.

## Probleme physikalischer Uhren

### Drift, Skew und Offset

| Begriff | Definition | Auswirkung |
|---------|------------|------------|
| **Drift** | Rate der Abweichung von der Referenzzeit | Uhren weichen kontinuierlich voneinander ab |
| **Skew** | Momentane Differenz zwischen zwei Uhren | Ereignisse erscheinen in falscher Reihenfolge |
| **Offset** | Absoluter Zeitunterschied zur Referenz | Zeitstempel sind nicht vergleichbar |

**Typische Drift-Raten:**
- Quarzuhr: ±10 ppm (parts per million) → ~0,86 Sekunden/Tag
- Temperaturkompensiert: ±1 ppm → ~86 ms/Tag
- Atomuhr: ±10⁻¹² → vernachlässigbar

### Externe vs. Interne Synchronisation

| Typ | Ziel | Beispiel |
|-----|------|----------|
| **Externe Synchronisation** | Alle Uhren stimmen mit einer autoritativen Quelle überein | NTP mit Stratum-0-Referenz |
| **Interne Synchronisation** | Alle Uhren stimmen untereinander überein (nicht unbedingt mit Realzeit) | Berkeley-Algorithmus |

## Synchronisationsalgorithmen

### Cristians Algorithmus (1989)

Für **externe Synchronisation** mit einem Zeitserver:

**Ablauf:**
1. Client sendet Request an Zeitserver zum Zeitpunkt T₀
2. Server empfängt Request, liest seine Zeit T_server
3. Server sendet Response mit T_server
4. Client empfängt Response zum Zeitpunkt T₁
5. Client setzt Uhr auf: **T_server + RTT/2**

**Annahme:** Die Netzwerklatenz ist symmetrisch (Hinweg = Rückweg).

> [!warning] Limitationen
> - Geht von symmetrischen Netzwerklatenzen aus – oft nicht erfüllt
> - Single Point of Failure (nur ein Server)
> - Server-Zeit muss vertrauenswürdig sein

**Genauigkeit:** Wenn RTT = Round-Trip-Time und die minimale Übertragungszeit min bekannt ist:
- Fehler ≤ (RTT/2 - min)

### Berkeley-Algorithmus (1989)

Für **interne Synchronisation** ohne externe Referenz:

**Ablauf:**
1. **Master** sendet seine Zeit an alle Slaves
2. Slaves antworten mit ihrer **Differenz** zur Master-Zeit
3. Master berechnet **Durchschnitt** (verwirft Ausreißer)
4. Master sendet **Korrekturen** (Δt) an alle Teilnehmer

> [!tip] Vorteile
> - Keine externe Referenz nötig
> - Robuster gegen einzelne fehlerhafte Uhren (Ausreißer-Filterung)
> - Master kann selbst eine falsche Uhr haben – Durchschnitt gleicht aus

> [!warning] Nachteile
> - Master ist Single Point of Failure
> - Erfordert Master-Election bei Ausfall
> - Keine Garantie für "echte" Zeit

**Anwendung:** Ursprünglich für BSD UNIX entwickelt, heute relevant für geschlossene Cluster ohne Internet-Zugang.

## Moderne Ansätze

### Vergleich der Synchronisationsmethoden

| System | Typ | Genauigkeit | Einsatz |
|--------|-----|-------------|---------|
| **NTP** | Extern | 1-100 ms | Allgemeine IT-Systeme |
| **PTP** (IEEE 1588) | Extern | < 1 µs | Industrie, Finanzhandel |
| **GPS** | Extern | ~10 ns | Referenzuhren, Mobilfunk |
| **Berkeley** | Intern | Variable | Geschlossene Cluster |
| **TrueTime** | Extern | ~7 ms Unsicherheit | Google Spanner |

### Google TrueTime

> [!important] Innovation
> TrueTime gibt nicht einen Zeitpunkt zurück, sondern ein **Intervall [earliest, latest]**, das die Unsicherheit explizit macht.

**API:**
- `TT.now()` → Intervall [earliest, latest]
- `TT.after(t)` → true, wenn t definitiv vergangen ist
- `TT.before(t)` → true, wenn t definitiv in der Zukunft liegt

**Implementierung:**
- Kombination aus GPS-Empfängern und Atomuhren in jedem Rechenzentrum
- Unsicherheitsintervall typisch: 1-7 ms
- Ermöglicht **external consistency** in Spanner

> [!example] Anwendung in Spanner
> Bei einem Commit wartet Spanner, bis `TT.after(commit_timestamp)` wahr ist. Dadurch ist garantiert, dass alle anderen Knoten den Commit in der korrekten Reihenfolge sehen – selbst ohne verteilte Sperren.

## Grenzen physikalischer Synchronisation

| Grenze | Ursache | Konsequenz |
|--------|---------|------------|
| **Netzwerklatenz** | Variable Verzögerungen | Perfekte Sync unmöglich |
| **Drift** | Physikalische Uhren-Ungenauigkeit | Kontinuierliche Re-Sync nötig |
| **Relativität** | Bei hohen Geschwindigkeiten/Gravitation | Für IT meist vernachlässigbar |
| **Byzantinische Fehler** | Defekte/manipulierte Uhren | Ausreißer-Filterung nötig |

> [!tip] Konsequenz für Verteilte Systeme
> Da perfekte physikalische Synchronisation unmöglich ist, nutzen viele Systeme **logische Uhren** (→ [[02-Logische-Uhren]]), die nur die Kausalität von Ereignissen erfassen, nicht die absolute Zeit.

## Zusammenhänge

| Thema | Beziehung | Verweis |
|-------|-----------|---------|
| Logische Uhren | Alternative zur physikalischen Zeit | [[02-Logische-Uhren]] |
| NTP-Protokoll | Standardprotokoll für externe Sync | [[../../03-Rechnernetze/04-Basisprotokolle/04-NTP]] |
| Konsensalgorithmen | Benötigen oft Zeitbounds | [[03-Konsensalgorithmen]] |
| Konsistenz | TrueTime ermöglicht external consistency | [[../03-Konsistenz/02-Konsistenzmodelle]] |

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
NA

> [!question] Verständnisfragen
> - Warum reicht NTP nicht für alle Anwendungsfälle?
> - Was ist der Unterschied zwischen Drift und Skew?
> - Wann würde man Berkeley statt NTP verwenden?
> - Wie löst TrueTime das Problem der Unsicherheit?

> [!tip] Merkhilfe
> **Cristian**: Server hat **die** Zeit → Client stellt nach (passiv)
> **Berkeley**: **Demokratie** → Durchschnitt aller Uhren (aktiv)
> **TrueTime**: Nicht "wann?", sondern **"frühestens/spätestens wann?"**

---

> [!tip] **Weiterführende Ressourcen**
> - [[02-Logische-Uhren]] – Alternative ohne physikalische Zeit
> - [[03-Konsensalgorithmen]] – Koordination zwischen Knoten
> - [[../../03-Rechnernetze/04-Basisprotokolle/04-NTP]] – NTP-Protokolldetails

---

## Quellen

- Cristian, Flaviu: Probabilistic Clock Synchronization, Distributed Computing, 1989
- Gusella, Riccardo; Zatti, Stefano: The Accuracy of the Clock Synchronization Achieved by TEMPO in Berkeley UNIX 4.3BSD, IEEE Transactions on Software Engineering, 1989
- Corbett, James C. et al.: Spanner – Google's Globally-Distributed Database, OSDI, 2012
