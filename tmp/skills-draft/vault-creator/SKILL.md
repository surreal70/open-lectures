---
name: vault-creator
description: Scaffold a new Obsidian lecture vault with all required directories, templates, and index files. Use when starting a new course or lecture series. Creates the complete folder structure following open-lectures conventions.
---

# Vault Creator — Open Lectures

Create a complete, ready-to-use Obsidian vault structure for a new lecture course.

## Output

A fully scaffolded vault directory containing:
- All required directories with proper naming
- Index files for each section
- Template files
- Glossary and abbreviation files
- Start page (MOC)
- Basic Obsidian configuration

## Required information

1. **Vault name** — Course title (e.g., "Kryptographie", "Mathematik-I")
2. **Main topics** — List of chapter topics (minimum 3)
3. **Author** — Default author for generated files
4. **Language** — Primary language (default: German)

## Generated structure

```
L-[VaultName]/
├── .obsidian/
│   ├── app.json
│   └── appearance.json
├── .assets/
│   └── .gitkeep
├── .templates/
│   ├── 00-templates-Index.md
│   ├── Konzept-Template.md
│   ├── Praesentation-Template.md
│   ├── Pruefung-Template.md
│   └── Uebung-Template.md
├── 00-Meta/
│   └── 00-Meta-Index.md
├── 00-Organisation/
│   ├── 00-Organisation-Index.md
│   ├── 01-Kursueberblick.md
│   ├── 02-Bewertung.md
│   ├── 03-Zeitplan.md
│   ├── 04-Kontakt.md
│   ├── 05-FAQ.md
│   ├── 06-Voraussetzungen.md
│   └── 07-Fachliteratur.md
├── 01-[Topic1]/
│   ├── 00-[Topic1]-Index.md
│   └── assets/
├── 02-[Topic2]/
│   ├── 00-[Topic2]-Index.md
│   └── assets/
├── 03-[Topic3]/
│   ├── 00-[Topic3]-Index.md
│   └── assets/
├── [NN]-Praesentationen/
│   └── 00-Praesentationen-Index.md
├── [NN]-Aufgaben/
│   ├── 00-Aufgaben-Index.md
│   ├── Uebungen/
│   └── Pruefungen/
├── [NN]-Anhang/
│   └── 00-Anhang-Index.md
├── Glossar.md
├── Abkuerzungsverzeichnis.md
└── Start.md
```

## Workflow

1. **Gather requirements:**
   - Course name and identifier
   - List of main topics/chapters
   - Author name
   - Any specific requirements

2. **Validate inputs:**
   - Vault name follows convention (no special characters except hyphens)
   - At least 3 main topics provided
   - No naming conflicts with existing vaults

3. **Calculate structure:**
   - Assign chapter numbers to topics
   - Determine supplementary chapter numbers (Praesentationen, Aufgaben, Anhang)

4. **Generate files:**
   
   **Start.md (MOC):**
   ```markdown
   ---
   author: [Author]
   created: [Date]
   modified: [Date]
   tags:
     - moc
     - index
   ---

   # [Course Name]

   Willkommen zum Kurs **[Course Name]**.

   ## Kursstruktur

   ### Organisation
   - [[00-Organisation-Index|Kursorganisation]]

   ### Kapitel
   - [[00-[Topic1]-Index|[Topic1]]]
   - [[00-[Topic2]-Index|[Topic2]]]
   - [[00-[Topic3]-Index|[Topic3]]]

   ### Material
   - [[00-Praesentationen-Index|Präsentationen]]
   - [[00-Aufgaben-Index|Übungen & Prüfungen]]
   - [[00-Anhang-Index|Anhang]]

   ### Referenz
   - [[Glossar]]
   - [[Abkuerzungsverzeichnis|Abkürzungen]]
   ```

   **Index files:** Basic structure with links to future content

   **Glossar.md:**
   ```markdown
   ---
   author: [Author]
   created: [Date]
   modified: [Date]
   tags:
     - glossar
     - referenz
   ---

   # Glossar

   Zentrale Begriffsdefinitionen für diesen Kurs.

   ## A

   ## B

   [Continue A-Z sections]
   ```

5. **Create minimal Obsidian config:**
   - Reasonable defaults for appearance
   - Enable core plugins (file-explorer, search, graph)
   - Set attachment folder to chapter `assets/`

6. **Present plan:**
   - Show directory tree
   - List all files to be created
   - Ask for approval before creating

7. **Create vault:**
   - Create all directories
   - Write all files
   - Report completion

## Post-creation

After vault is created:
- User should open it in Obsidian to verify
- Suggest running `markdown-validator` on the generated files
- Remind to update repository README with new vault entry
