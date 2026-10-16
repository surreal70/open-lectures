---
title: "Ishikawa-Diagramm (Ursache-Wirkungsdiagramm)"
created: 2026-10-13
modified: 2026-10-13
type: lecture
tags:
  - lf11c
  - prozessanalyse
  - ishikawa
  - fischgraete
  - ursache-wirkung
  - qualitaetsmanagement
source: proTirone (CC-BY-4.0)
---

# Ishikawa-Diagramm

> [!info] Lernziele
> - Ishikawa-Diagramm erstellen können
> - Die „Ms" als Einflusskategorien kennen
> - Vor- und Nachteile des Verfahrens einordnen

## Bezeichnungen

Das **Ursache-Wirkungsdiagramm** hat mehrere Namen:

| Name | Herkunft |
|------|----------|
| **Ishikawa-Diagramm** | Nach Kaoru Ishikawa (Erfinder) |
| **Fischgräten-Diagramm** | Form erinnert an Fischgräten |
| **Fishbone Diagram** | Englische Bezeichnung |

## Zweck und Eigenschaften

- **Assoziatives Verfahren** zum vollständigen Erfassen aller Einflüsse
- **Trennt** Identifikation von Analyse
- **Stellt grafisch dar**, welche Ursachen zu einem Ergebnis führen
- **Expliziert faktische Abhängigkeiten**
- Stammt aus dem **Qualitätsmanagement**

## Die Einflusskategorien (Ms)

### Die vier Ms (Grundform)

```
         Material          Maschine
              \              /
               \            /
                ═══════════════════▶ PROBLEM/ZIEL
               /            \
              /              \
          Methode          Mensch
```

### Die acht Ms (Erweiterte Form)

| Kategorie | Beschreibung |
|-----------|--------------|
| **Material** | Rohstoffe, Komponenten, Daten |
| **Maschine** | Geräte, Software, Werkzeuge |
| **Methode** | Verfahren, Prozesse, Arbeitsanweisungen |
| **Mensch** | Personal, Qualifikation, Motivation |
| **Management** | Führung, Organisation, Entscheidungen |
| **Mitwelt** (Milieu) | Umgebung, Arbeitsplatz, Klima |
| **Messung** | Prüfverfahren, Kennzahlen, Kontrolle |
| **Money** (Geld) | Budget, Ressourcen, Investitionen |

## Vorgehensweise

### Phase I: Formaler Start

1. **Zieleintrag**: Rechts den Fehlerbefund oder das Ziel eintragen
2. **Hauptlinie**: Von links nach rechts zum Ziel zeichnen
3. **Kategorien**: Ober- und unterhalb die Einflusskategorien eintragen
4. **Verbindungen**: Jede Kategorie mit schrägem Pfeil zur Hauptlinie verbinden

### Phase II: Assoziative Sammlung

5. **Ursachen sammeln**: Zu jeder Kategorie konkrete Ursachen eintragen
6. **Vollständigkeitscheck**: Systematisch alle Kategorien durchgehen
7. **Bewertung**: Experten klassifizieren die Ursachen nach Wirkungsgrad

## Beispiel: Softwarefehler

```
    MATERIAL                    MASCHINE
    │                           │
    ├─ Fehlerhafte API         ├─ Veraltete Server
    ├─ Unvollständige Specs    ├─ Speichermangel
    │                           │
    └───────────┐       ┌───────┘
                ↘       ↙
═════════════════════════════════════▶ SYSTEMABSTURZ
                ↗       ↖
    ┌───────────┘       └───────┐
    │                           │
    ├─ Kein Code-Review        ├─ Übermüdung
    ├─ Fehlende Tests          ├─ Mangelnde Schulung
    │                           │
    METHODE                     MENSCH
```

## Bewertung des Verfahrens

### Vorteile

> [!success] Stärken
> - Gute Diskussionsgrundlage für Gruppenarbeit
> - Ermöglicht vielseitige Betrachtungsweise
> - Wenig Aufwand bei der Durchführung
> - Leicht erlern- und anwendbar

### Nachteile

> [!warning] Schwächen
> - Unübersichtlich bei komplexen Problemen
> - Keine vernetzten Ursache-Wirkungs-Zusammenhänge
> - Erfasst keine Wechselwirkungen
> - Keine zeitlichen Abhängigkeiten darstellbar

## Prüfungsrelevanz

> [!question] Typische Prüfungsfragen
> - Welche Einflusskategorien werden im Ishikawa-Diagramm verwendet?
> - Zeichnen Sie ein Ishikawa-Diagramm für ein gegebenes Problem
> - Nennen Sie Vor- und Nachteile des Verfahrens
> - Was ist der Unterschied zum Fehlerbaum?

## Querverweise

- → [[01-FMEA|FMEA]] – Quantitative Fehlerbewertung
- → [[02-ABC-Analyse|ABC-Analyse]] – Fehlerpriorisierung
- → [[05-Fehlerbaum|Fehlerbaumanalyse]] – Alternative zur Ursachenanalyse

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (CC-BY-4.0).
