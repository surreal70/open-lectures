---
inclusion: auto
name: System Date Rule
description: Rules for handling dates after session start or context compaction
---

# Systemdatum-Regel

## Wann das Systemdatum abgefragt werden muss

Das im Kontext gecachte Datum (`current_date_and_time`) kann nach einem Kontextwechsel (Context Compaction) veraltet sein. Daher gilt:

### Pflicht zur Datumsabfrage

**IMMER** das aktuelle Systemdatum mit `date +%Y-%m-%d` abfragen in folgenden Situationen:

1. **Bei Session-Start** – bevor Frontmatter-Felder mit Datumsangaben bearbeitet werden
2. **Nach Kontextwechsel (Context Compaction)** – erkennbar am `[SYSTEM NOTE: This conversation was summarized...]` Block
3. **Bei Unsicherheit** – im Zweifel lieber einmal zu viel abfragen

### Anwendung

Bevor ein `modified`-, `created`- oder anderes Datumsfeld im YAML-Frontmatter gesetzt oder geprüft wird:

```bash
date +%Y-%m-%d
```

Das Ergebnis dieses Befehls ist das **verbindliche aktuelle Datum**, nicht der Wert aus `current_date_and_time` im Kontext.

### Warum diese Regel?

- Context Compaction kann Stunden oder Tage nach dem ursprünglichen Session-Start erfolgen
- Das ursprünglich injizierte Datum bleibt im komprimierten Kontext erhalten, obwohl es nicht mehr aktuell ist
- Falsche Datumsangaben im Frontmatter führen zu inkonsistenten Metadaten
