---
inclusion: manual
name: Lecture Notes
description: Guidelines for creating and structuring lecture notes in Obsidian
---

# Obsidian Lecture Notes Guidelines

Guidelines for creating well-structured lecture notes in this Obsidian vault.

## Vault Directory Structure

Each vault follows this directory structure:

```
vault-name/
├── 00-Organisation/           # Organisatorisches (Termine, Kontakte, etc.)
├── 01-TOP1/                   # Erstes Hauptthema
├── 02-TOP2/                   # Zweites Hauptthema
├── 03-TOP3/                   # Drittes Hauptthema
├── (04-TOPn/)                 # Optional: weitere Themenkapitel
├── Praesentationen/           # PowerPoint und andere Präsentationen
├── Uebungsaufgaben/           # Übungen und Aufgaben
├── Pruefungen/                # Musterklausuren und alte Prüfungen
├── Anhang/                    # Diverses Material
├── .templates/                # Verstecktes Template-Verzeichnis
├── Glossar.md                 # Begriffsdefinitionen
└── Abkuerzungsverzeichnis.md  # Abkürzungen und ihre Bedeutungen
```

### Strukturregeln

| Kapiteltyp | Präfix | Beispiel |
|------------|--------|----------|
| Organisation | `00-` | `00-Organisation/` |
| Themenkapitel | `01-`, `02-`, ... | `01-Grundlagen/`, `02-Vertiefung/` |
| Zusatzkapitel | optional | `Praesentationen/` oder `05-Praesentationen/` |

### Pflichtverzeichnisse

**Mit Index-Präfix (Hauptinhalt):**
- `00-Organisation` - Kursorganisation, Termine, Dozenten, Metadaten
- `01-TOP1` bis `0n-TOPn` - Mindestens 3 Themenkapitel (nach Bedarf erweiterbar)

**Ohne Präfix (Zusatzmaterial) — Präfix optional:**
- `Praesentationen` - Folien, PPT-Dateien
- `Uebungsaufgaben` - Übungen mit Lösungen
- `Pruefungen` - Musterklausuren, alte Prüfungen
- `Anhang` - Sonstiges Material

Hinweis: Zusatzkapitel können optional nummerierte Präfixe haben (z.B. `05-Praesentationen/`), um die Sortierung im Dateisystem zu kontrollieren.

**Versteckt:**
- `.templates` - Vorlagen für neue Dokumente

**Markdown-Dateien im Hauptverzeichnis:**
- `Glossar.md` - Zentrale Begriffsdefinitionen
- `Abkuerzungsverzeichnis.md` - Alle verwendeten Abkürzungen

## File Naming Convention

Content files within directories **must** have a numeric prefix for ordering, but **without** duplicating the parent directory's prefix:

```
02-Betriebssysteme/
└── 01-Einfuehrung/
    ├── 01-Historie.md
    ├── 02-Definition.md
    ├── 03-Aufgaben.md
    └── assets/
```

**Format:** `NN-Titel.md` where `NN` is a two-digit number (01, 02, 03, ...) unique within that directory.

**Correct:** `01-Einfuehrung/01-Historie.md`  
**Wrong:** `01-Einfuehrung/01-01-Historie.md` (directory prefix duplicated)

### Chapter Asset Directories

Each chapter directory contains an `assets/` folder for images and attachments:

```
02-Betriebssysteme/
└── 02-Architektur/
    ├── 02-01-Kerneltypen.md
    ├── 02-02-Schichtenmodell.md
    └── assets/
        ├── monolithischer-kernel.png
        ├── mikrokernel.png
        └── hybridkernel.png
```

Reference images using **filename only**: `![[monolithischer-kernel.png]]`

Obsidian resolves filenames via "shortest path". Use descriptive, unique filenames to avoid collisions.

## Frontmatter (Metadata)

Every content file starts with YAML frontmatter.

```yaml
---
author: Name des Autors
created: YYYY-MM-DD
modified: YYYY-MM-DD
tags:
  - folder-tag
---
```

### Required Frontmatter Fields

| Feld | Beschreibung |
|------|--------------|
| `author` | Name des Erstellers |
| `created` | Erstellungsdatum (YYYY-MM-DD) |
| `modified` | Änderungsdatum (YYYY-MM-DD) – **muss bei jeder Änderung aktualisiert werden** |
| `tags` | Mindestens ein Tag entsprechend dem übergeordneten Ordner |

### Standard Tags (nach Ordnerzugehörigkeit)

| Ordner | Standard-Tag |
|--------|--------------|
| `00-Organisation/` | `organisation` |
| `01-TOP1/` bis `0n-TOPn/` | `content` |
| `Praesentationen/` | `praesentation` |
| `Uebungsaufgaben/` | `uebung` |
| `Pruefungen/` | `pruefung` |
| `Anhang/` | `anhang` |

Vaults können zusätzliche individuelle Tags definieren (z.B. `bs`, `rn`, `vs` für Themenbereiche).

## Note Structure

Each content note **must** follow this structure in the specified order:

```markdown
---
author: Max Mustermann
created: 2026-10-01
modified: 2026-10-09
tags:
  - content
  - algorithmen
---

# Titel des Dokuments

> [!info] **Lernziele**
> - Lernziel 1
> - Lernziel 2
> - Lernziel 3

## Überblick

Kurze Zusammenfassung des Themas und seiner Bedeutung.

## Thema 1

Inhalt zu Thema 1...

## Thema 2

Inhalt zu Thema 2...

## Thema 3

Inhalt zu Thema 3...

## Zusammenhänge

Querverweise zu anderen relevanten Dokumenten im Vault:

- → [[Verwandtes Thema A]]
- → [[Verwandtes Thema B]]
- → [[Grundlagen aus Dokument C]]

> [!warning] **Prüfungsrelevant**
> - Wichtiger Punkt 1
> - Wichtiger Punkt 2

> [!question] **Typische Prüfungsfragen**
> - Frage 1?
> - Frage 2?

## Quellen

- Quelle 1: Autor, Titel, Jahr
- Quelle 2: Autor, Titel, Jahr

> [!tip] **Weiterführende Links**
> - [Externe Ressource 1](URL)
> - [Externe Ressource 2](URL)
> - [[Vertiefendes Dokument im Vault]]
```

### Strukturübersicht

| Reihenfolge | Element | Beschreibung |
|-------------|---------|--------------|
| 1 | Frontmatter | YAML-Metadaten (author, created, modified, tags) |
| 2 | Titel (H1) | `# Dokumenttitel` |
| 3 | Callout: Lernziele | `[!info]` - Kompetenzziele |
| 4 | Überblick | Einführung ins Thema |
| 5 | Thema 1...n | Hauptinhalte (min. 3 Themen als Start) |
| 6 | Zusammenhänge | Crosslinks zu anderen Vault-Dokumenten |
| 7 | Callout: Prüfungsrelevant | `[!warning]` - Klausurrelevante Punkte |
| 8 | Callout: Prüfungsfragen | `[!question]` - Typische Fragen |
| 9 | Quellen | Literatur und Referenzen |
| 10 | Callout: Weiterführende Links | `[!tip]` - Zusätzliche Ressourcen |

## Linking Strategy

- Link to related lecture notes using `[[Folder/NN-Note-Name]]`
- Link to concept notes for recurring topics
- Create MOC (Map of Content) notes for each course to navigate lectures

## Tagging Convention

Tags are primarily determined by the folder the file resides in (see Standard Tags above). Additional tags can be added for:

- `#concept/topic` - for key concepts
- `#todo/review` - notes needing review
- `#todo/expand` - sections to expand later

## During-Lecture Capture

For real-time note-taking:

- Use bullet points for quick capture
- Mark uncertain content with `(?)`
- Use `> [!question]` callouts for questions to ask
- Leave `TODO:` markers for sections to complete later

## Post-Lecture Processing

After the lecture:

1. Review and clean up raw notes
2. Add proper headings and structure
3. Create links to related concepts
4. Add summary and key takeaways
5. Generate any diagrams or illustrations
6. Move todos to a task list or remove completed ones

## Mathematical Content

For lectures with math:

- Use LaTeX for all formulas
- Number important equations for reference
- Include derivation steps, not just results

## Code Examples

For programming lectures:

- Include complete, runnable code snippets
- Add comments explaining key lines
- Note the language/environment used

## File Naming (Old Convention - Deprecated)

~~Use consistent naming: `YYYY-MM-DD-course-topic.md`~~

**Neue Konvention:** Siehe "File Naming Convention" oben – Dateien verwenden numerische Präfixe (`NN-Titel.md`).


## Farbcodierung der Callout-Boxen

In diesem Vault werden verschiedene Callout-Boxen verwendet, um Informationen zu kategorisieren. Die Farbcodierung ist konsistent über alle Dokumente:

### Lernziele und Informationen

> [!info] **Lernziele**
> Blaue Boxen mit dem Info-Symbol kennzeichnen die **Lernziele** am Anfang jedes Kapitels. Sie beschreiben, welche Kompetenzen nach dem Durcharbeiten erworben werden sollten.

> [!note] **Hinweis / Erklärung**
> Blaue Boxen mit Notiz-Symbol enthalten ergänzende Erklärungen und Hintergrundinformationen.

### Prüfungsrelevante Inhalte

> [!warning] **Prüfungsrelevant**
> Gelb/orange Boxen markieren **prüfungsrelevante Themen**. Diese Inhalte sollten für die Prüfung beherrscht werden.

> [!question] **Häufige Prüfungsfragen**
> Hellblaue Boxen mit Fragezeichen enthalten typische **Prüfungsfragen**, die in Klausuren vorkommen können.

### Lerntipps und Merkhilfen

> [!tip] **Merkhilfen / Tipps**
> Grüne Boxen enthalten **Eselsbrücken und Merkhilfen**, die das Lernen erleichtern.

> [!example] **Beispiele**
> Violette Boxen zeigen **praktische Beispiele** zur Veranschaulichung von Konzepten.

### Warnungen und wichtige Hinweise

> [!danger] **Achtung / Fehlerquellen**
> Rote Boxen warnen vor **häufigen Fehlern** und Missverständnissen.

> [!bug] **Bekannte Probleme**
> Rote Boxen mit Bug-Symbol weisen auf **bekannte Probleme** oder Einschränkungen hin.

### Zusatzinformationen

> [!quote] **Zitate / Definitionen**
> Graue Boxen enthalten **Zitate** aus Fachliteratur oder formale **Definitionen**.

> [!abstract] **Zusammenfassung**
> Graue Boxen mit Abstract-Symbol fassen **Kernpunkte** eines Abschnitts zusammen.

### Nicht prüfungsrelevant

> [!info] **Nicht prüfungsrelevant**
> Blaue Boxen mit diesem Titel kennzeichnen **interessante Zusatzinformationen**, die für die Prüfung nicht relevant sind, aber das Verständnis vertiefen.

---

## Verwendete Symbole und Konventionen

| Symbol | Bedeutung |
|--------|-----------|
| `→` | Verweis auf anderes Dokument (Crosslink) |
| `[[...]]` | Obsidian-interner Link |
