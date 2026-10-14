# Open Lectures

[![Lizenz: CC BY-NC 4.0](https://img.shields.io/badge/Lizenz-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/deed.de)
[![Inhalt: Bildung](https://img.shields.io/badge/Inhalt-Bildung-blue.svg)](#)
[![Format: Obsidian](https://img.shields.io/badge/Format-Obsidian-purple.svg)](https://obsidian.md/)
[![Sprache: Deutsch](https://img.shields.io/badge/Sprache-Deutsch-yellow.svg)](#)

Eine Sammlung offener Vorlesungsunterlagen, Arbeitsmaterialien und Kursinhalte im Obsidian-Format.

🇬🇧 [English Version](README.md)

## Über dieses Repository

Dieses Repository enthält strukturierte Vorlesungsunterlagen für verschiedene akademische Kurse. Jeder Kurs ist als eigenständiger Obsidian-Vault organisiert und eignet sich für Selbststudium, Prüfungsvorbereitung und Wissensmanagement.

Die Materialien umfassen:
- Umfassende Vorlesungsnotizen mit Lernzielen
- Übungsaufgaben mit Lösungen
- Musterklausuren und Prüfungsvorbereitungsmaterial
- Querverweise zwischen Konzepten und Glossare

**Sprache:** Die Kursmaterialien sind hauptsächlich auf **Deutsch**. Englische Übersetzungen können auf Anfrage erstellt werden.

**Neu bei Obsidian?** Siehe die [Anleitung](HOWTO.de.md) für Installationshinweise, eine Kurzreferenz und Tipps zum effektiven Lernen.

## Lizenz

Dieses Werk ist lizenziert unter **Creative Commons Namensnennung-Nicht kommerziell 4.0 International (CC BY-NC 4.0)**.

Sie dürfen:
- **Teilen** — das Material in jedwedem Format oder Medium vervielfältigen und weiterverbreiten
- **Bearbeiten** — das Material remixen, verändern und darauf aufbauen

Unter folgenden Bedingungen:
- **Namensnennung** — Sie müssen angemessene Urheber- und Rechteangaben machen
- **Nicht kommerziell** — Sie dürfen das Material nicht für kommerzielle Zwecke nutzen

Siehe [LICENSE](LICENSE) für den vollständigen Lizenztext.

## Vorlesungskatalog

| Vault | Beschreibung | Autor | Status |
|-------|--------------|-------|--------|
| `Betriebssysteme, Rechnernetze und verteilte Systeme` | Betriebssysteme, Rechnernetze und Verteilte Systeme – IU-Kursmaterialien. **BS** (Prozesse, Scheduling, Speicher, Synchronisation, E/A, Dateisysteme), **RN** (OSI/TCP-IP-Modelle, alle Schichten, Sicherheit), **VS** (Grundlagen, Kommunikation, Konsistenz, Koordination) | Andreas Hümmer | in Entwicklung (BS: v0.9.3, RN: v0.1, VS: v0.1) |

## Mitwirken

Beiträge und Feedback sind willkommen und sehr erwünscht!

Ob Sie:
- Fehler oder Ungenauigkeiten melden möchten
- Verbesserungsvorschläge haben
- Neue Inhalte hinzufügen möchten
- Materialien übersetzen möchten

Bitte öffnen Sie gerne ein Issue oder reichen Sie einen Pull Request ein. Jeder Beitrag hilft, diese Bildungsressourcen für alle zu verbessern.

## Über KI-Unterstützung

Dieses Projekt nutzt KI-Unterstützung (Kiro) zur Unterstützung des Entwicklungsworkflows:

- **Strukturelle Integrität** — Steering-Dateien definieren Formatierungsregeln, Dokumentstruktur und Konventionen. Die KI validiert Inhalte gegen diese Regeln und erstellt Compliance-Berichte (siehe [Beispielbericht](Betriebssysteme,%20Rechnernetze%20und%20verteilte%20Systeme/COMPLIANCE-REPORT.md)).
- **Konsistente Darstellung** — Automatisierte Prüfungen stellen einheitliche Frontmatter, Callout-Nutzung, Querverweise und Tagging über alle Dokumente sicher.
- **Inhaltskonvertierung** — Reformatierungsaufgaben wie das Umwandeln von ASCII-Diagrammen in PNG-Grafiken oder das Umstrukturieren importierter Inhalte.
- **Ideensammlung** — Sammeln und Organisieren von Gedanken, Notizen und Überlegungen zu Themen und Teilprojekten.

Die eigentlichen Bildungsinhalte werden von menschlichen Autoren erstellt. Die KI unterstützt bei der Mechanik der Pflege eines gut organisierten Vaults.

### Setup für AI-gestützte Arbeit

Für die Nutzung der Obsidian-Vaults sind **keine zusätzlichen Tools erforderlich**.

Wenn Sie jedoch mit Kiro oder einem anderen AI-Agenten an diesem Repository arbeiten möchten, finden Sie im Verzeichnis [`.kiro/`](.kiro/README.md) alle nötigen Informationen:

- **Skills** für wiederkehrende Aufgaben (PDF-Extraktion, Vorlesungserstellung, Validierung)
- **Steering-Dateien** die die Konventionen definieren
- **requirements.txt** für optionale Python-Dependencies

```bash
# Optionale System-Tools (für PDF-Verarbeitung etc.)
sudo apt install poppler-utils pandoc  # Debian/Ubuntu

# Optionale Python-Dependencies
pip install -r .kiro/requirements.txt
```
