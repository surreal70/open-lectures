---
author: Andreas Hümmer
title: Konsistenzmodelle
tags:
  - content
  - vs
  - konsistenz
  - modelle
  - eventual-consistency
  - acid
created: '2026-10-07'
modified: '2026-10-29'
bereich: VS
---

# Konsistenzmodelle

> [!info] Lernziele
> - Verschiedene Konsistenzmodelle kennen und einordnen
> - ACID-Eigenschaften erklären können
> - Unterschied zwischen Strong und Eventual Consistency verstehen
> - Anwendungsfälle für verschiedene Modelle benennen

## Einleitung

Konsistenzmodelle definieren, welche Garantien ein verteiltes System bezüglich der Sichtbarkeit und Reihenfolge von Datenänderungen bietet. Sie bilden die Grundlage für Entscheidungen über Systemarchitekturen.

> [!important] Kernkonzept
> **Konsistenz** garantiert, dass sich Daten für einen Beobachter immer in einem **gültigen Zustand** befinden. Zwischenzustände sind nach außen nicht sichtbar. Je stärker das Konsistenzmodell, desto mehr Koordination ist erforderlich – und desto geringer die Performance.

> [!example] Analogie
> Konsistenzmodelle sind wie verschiedene Nachrichtenkanäle: **Strikte Konsistenz** ist ein Live-Telefonat – beide hören sofort, was der andere sagt. **Eventual Consistency** ist wie ein Gruppenchat mit schlechter Verbindung – alle sehen irgendwann alle Nachrichten, aber nicht unbedingt in derselben Reihenfolge oder zum selben Zeitpunkt.

## ACID-Eigenschaften

Transaktionen in Datenbanksystemen müssen den **ACID-Eigenschaften** genügen:

| Eigenschaft | Beschreibung |
|-------------|--------------|
| **A**tomicity (Atomarität) | Transaktion ist entweder vollständig oder gar nicht – bei Fehlern wird der vorherige Zustand wiederhergestellt |
| **C**onsistency (Konsistenz) | Daten befinden sich immer in einem gültigen Zustand – keine Zwischenzustände sichtbar |
| **I**solation (Isolierung) | Gleichzeitige Zugriffe beeinflussen sich nicht – Schreibzugriffe werden serialisiert |
| **D**urability (Dauerhaftigkeit) | Erfolgreiche Änderungen bleiben auch bei Systemausfällen bestehen |

![[acid-eigenschaften.png]]
*<span class="fig-id">04-03-02-acid-eigenschaften</span>: Die vier ACID-Eigenschaften einer Transaktion.*

## Hierarchie der Konsistenzmodelle

Von stark zu schwach geordnet:

![[konsistenz-hierarchie.png]]
*<span class="fig-id">04-03-02-konsistenz-hierarchie</span>: Die Hierarchie der Konsistenzmodelle von stark (oben) bis schwach (unten).*

### Modelle im Detail

| Modell | Garantie | Performance | Anwendung |
|--------|----------|-------------|-----------|
| **Strikte Konsistenz** | Alle Ops instantan global sichtbar | Sehr niedrig | Theoretisches Ideal |
| **Linearisierbarkeit** | Echtzeitreihenfolge wird eingehalten | Niedrig | Bankensysteme, Locks |
| **Sequentielle Konsistenz** | Eine globale Reihenfolge aller Ops | Mittel | Multi-Prozessor-Systeme |
| **Kausale Konsistenz** | Kausal abhängige Ops geordnet | Höher | Social Media, Messaging |
| **Read-your-writes** | Eigene Schreibops sofort sichtbar | Hoch | Session-basierte Apps |
| **Eventual Consistency** | Konvergenz nach endlicher Zeit | Sehr hoch | DNS, CDNs, Caches |

### Strikte Konsistenz

Die strikte Konsistenz ist das stärkste Modell: Jede Schreiboperation wird **instantan** für alle Knoten sichtbar. In der Praxis ist dies physikalisch unmöglich, da Informationen nicht schneller als mit Lichtgeschwindigkeit übertragen werden können. Strikte Konsistenz dient daher primär als theoretisches Referenzmodell.

### Linearisierbarkeit

Linearisierbarkeit (auch: atomare Konsistenz) garantiert, dass Operationen so erscheinen, als würden sie zu einem **eindeutigen Zeitpunkt** stattfinden – und zwar in einer Reihenfolge, die mit der realen Zeit übereinstimmt. Wenn Client A eine Schreiboperation abschließt, bevor Client B liest, sieht Client B garantiert den neuen Wert.

> [!example] Praxisbeispiel: Banküberweisung
> Bei einer Überweisung von Konto A nach Konto B muss sichergestellt sein, dass der Betrag nicht doppelt existiert oder verschwindet. Linearisierbarkeit garantiert, dass alle Beobachter denselben konsistenten Kontostand sehen.

### Sequentielle Konsistenz

Sequentielle Konsistenz erfordert, dass alle Knoten dieselbe **globale Reihenfolge** aller Operationen sehen – diese muss jedoch nicht mit der realen Zeit übereinstimmen. Die Reihenfolge der Operationen eines einzelnen Prozesses bleibt erhalten.

### Kausale Konsistenz

Kausale Konsistenz garantiert nur die Ordnung von Operationen, die **kausal voneinander abhängen**. Wenn Operation B das Ergebnis von Operation A verwendet, sehen alle Knoten A vor B. Unabhängige Operationen können in beliebiger Reihenfolge erscheinen.

> [!example] Praxisbeispiel: Social Media
> In einem Kommentarsystem muss eine Antwort auf einen Beitrag immer nach dem ursprünglichen Beitrag erscheinen. Zwei unabhängige Kommentare können jedoch in unterschiedlicher Reihenfolge angezeigt werden.

### Read-your-writes-Konsistenz

Dieses Modell garantiert, dass ein Client seine **eigenen Schreiboperationen** sofort sieht. Andere Clients sehen die Änderungen möglicherweise verzögert. Dies ist besonders wichtig für Session-basierte Anwendungen, bei denen Benutzer erwarten, dass ihre Eingaben sofort sichtbar sind.

> [!example] Praxisbeispiel: Warenkorb
> Wenn ein Benutzer einen Artikel in den Warenkorb legt, muss dieser sofort im Warenkorb erscheinen – auch wenn andere Server die Änderung noch nicht repliziert haben.

### Eventual Consistency

Eventual Consistency ist das schwächste Konsistenzmodell: Es garantiert lediglich, dass alle Replikate **irgendwann** denselben Zustand erreichen, wenn keine neuen Schreiboperationen mehr stattfinden. Es gibt keine Garantie, wann dies geschieht oder welchen Wert ein Lesevorgang zwischenzeitlich liefert.

> [!example] Praxisbeispiel: DNS
> Das Domain Name System verwendet Eventual Consistency mit TTL-basierten Caches. Nach einer DNS-Änderung dauert es Stunden oder Tage, bis alle DNS-Server weltweit den neuen Eintrag haben.

## Strong vs. Eventual Consistency

Der fundamentale Trade-off in verteilten Systemen liegt zwischen **Strong Consistency** und **Eventual Consistency**. Die Wahl hängt von den Anforderungen der Anwendung ab.

| Aspekt | Strong Consistency | Eventual Consistency |
|--------|-------------------|---------------------|
| **Garantie** | Neuester Wert sofort | Irgendwann konsistent |
| **Latenz** | Höher (Koordination nötig) | Niedriger |
| **Verfügbarkeit** | Bei Partition eingeschränkt | Bleibt verfügbar |
| **Komplexität** | System komplexer | Anwendung komplexer |
| **Anwendung** | Finanztransaktionen | Social Media, IoT |

### Wann Strong Consistency?

Strong Consistency ist unverzichtbar, wenn **Inkonsistenzen nicht toleriert** werden können:

- **Finanztransaktionen**: Kontostände müssen exakt stimmen
- **Inventarsysteme**: Lagerbestände dürfen nicht negativ werden
- **Reservierungssysteme**: Doppelbuchungen müssen verhindert werden
- **Distributed Locks**: Kritische Abschnitte dürfen nicht mehrfach betreten werden

### Wann Eventual Consistency?

Eventual Consistency ist akzeptabel, wenn **temporäre Inkonsistenzen tolerierbar** sind:

- **Social Media Feeds**: Likes und Kommentare müssen nicht sofort global sichtbar sein
- **Produktbewertungen**: Neue Bewertungen können verzögert erscheinen
- **Besucherzähler**: Exakte Echtzeit-Zahlen sind nicht kritisch
- **DNS**: Änderungen propagieren über Stunden/Tage

> [!note] Kompromiss in der Praxis
> Viele Systeme verwenden **hybride Ansätze**: Strong Consistency für kritische Operationen (z.B. Bestellung abschließen) und Eventual Consistency für unkritische Daten (z.B. Produktempfehlungen).

## BASE als Alternative zu ACID

Während ACID für traditionelle relationale Datenbanken entwickelt wurde, entstand BASE als Paradigma für **hochskalierbare, verteilte Systeme**, die Verfügbarkeit über strikte Konsistenz priorisieren.

| ACID | BASE |
|------|------|
| **A**tomicity | **B**asically **A**vailable |
| **C**onsistency | **S**oft state |
| **I**solation | **E**ventual consistency |
| **D**urability | – |

### BASE im Detail

- **Basically Available**: Das System ist grundsätzlich verfügbar, auch wenn einzelne Knoten ausfallen. Antworten können jedoch veraltet oder unvollständig sein.

- **Soft State**: Der Systemzustand kann sich auch ohne neue Eingaben ändern, da Daten im Hintergrund zwischen Replikaten synchronisiert werden.

- **Eventual Consistency**: Nach einer gewissen Zeit ohne neue Schreiboperationen konvergieren alle Replikate zum selben Zustand.

### ACID vs. BASE: Wann welches Modell?

| Kriterium | ACID bevorzugen | BASE bevorzugen |
|-----------|-----------------|-----------------|
| **Datenintegrität** | Kritisch | Tolerierbar |
| **Skalierbarkeit** | Moderat | Extrem hoch |
| **Latenzanforderung** | Flexibel | Sehr niedrig |
| **Netzwerkpartitionen** | Selten/kontrolliert | Häufig/erwartet |
| **Beispielsysteme** | Banken, ERP | Social Media, IoT |

> [!tip] Merksatz
> **ACID** für Daten, bei denen Fehler teuer sind (Geld, Verträge, Inventar).
> **BASE** für Daten, bei denen Geschwindigkeit wichtiger ist als Perfektion (Feeds, Empfehlungen, Analytics).

## Zusammenhänge

| Thema | Beziehung | Verweis |
|-------|-----------|---------|
| CAP-Theorem | definiert Grenzen der Konsistenzmodelle | [[01-CAP-Theorem]] |
| Replikation | setzt Konsistenzmodelle um | [[03-Replikation]] |
| ACID vs. BASE | alternative Ansätze | siehe oben |
| Performance | wird durch Konsistenzwahl beeinflusst | – |

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - Erklären Sie die ACID-Eigenschaften
> - Unterscheiden Sie Strong und Eventual Consistency

> [!question] Verständnisfragen
> - Warum ist strikte Konsistenz praktisch nicht erreichbar?
> - Wann ist Eventual Consistency akzeptabel?
> - Was bedeutet BASE und wie unterscheidet es sich von ACID?

> [!tip] Merkhilfe
> **ACID = Zuverlässig aber langsam** (traditionelle Datenbanken)
> **BASE = Schnell aber eventuell inkonsistent** (NoSQL, verteilte Systeme)
> 
> Eselsbrücke: ACID ist wie ein Bankautomat (sicher), BASE wie ein Social-Media-Feed (schnell, aber manchmal verzögert)

---

> [!tip] **Weiterführende Ressourcen**
> - [[01-CAP-Theorem]] – Trade-offs in verteilten Systemen
> - [[03-Replikation]] – Umsetzung von Konsistenz
> - [[../04-Koordination/02-Logische-Uhren]] – Kausalität erfassen

---

## Quellen

- Härder, Theo & Reuter, Andreas: Principles of Transaction-Oriented Database Recovery, ACM Computing Surveys, 1983
