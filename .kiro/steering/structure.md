---
inclusion: auto
name: Project Structure
description: File and folder organization in the open-lectures repository
---

# Project Structure

## Repository Layout

```
open-lectures/
├── README.md / README.de.md     # Repository documentation
├── HOWTO.md / HOWTO.de.md       # Obsidian usage guide
├── LICENSE                       # CC BY-NC 4.0
├── .kiro/steering/              # AI steering rules
├── L-<Lecture-Name>/            # Lecture vaults (L- prefix)
├── tmp/                          # Temporary files (gitignored)
└── Repository-Improvements/      # Meta-documentation
```

## Vault Naming

Lecture vaults use `L-` prefix: `L-Betriebssysteme, Rechnernetze und verteilte Systeme/`
Howto vaults use `H-` prefix: `H-Coffee and Tee`

## Vault Internal Structure

Each vault follows this pattern:

```
L-VaultName/
├── .obsidian/           # Obsidian configuration
├── .assets/             # Vault-wide shared assets
├── .templates/          # Note templates
├── 00-Organisation/     # Course info, schedule, contacts
├── 00-Meta/             # Vault metadata
├── 01-TopicA/           # First main topic
├── 02-TopicB/           # Second main topic
├── ...                  # Additional numbered topics
├── 0n-Praesentationen/  # Presentation slides
├── 0n-Aufgaben/         # Exercises and tasks
├── 0n-Anhang/           # Appendix materials
├── Glossar.md           # Term definitions
├── Abkuerzungsverzeichnis.md  # Abbreviations
└── Start.md             # Entry point / MOC
```

## Chapter Structure

Each topic directory contains:

```
02-TopicB/
├── 01-SubtopicName/
│   ├── 01-FirstNote.md
│   ├── 02-SecondNote.md
│   └── assets/          # Images for this chapter
├── 02-AnotherSubtopic/
└── 00-TopicB-Index.md   # Chapter overview
```

## File Naming

- **Directories**: `NN-Name/` where NN is two-digit order prefix
- **Files**: `NN-Title.md` within directories
- **Assets**: Descriptive names in chapter `assets/` folders
- Reference images by filename only: `![[image.png]]`

## Frontmatter Required

Every content file needs:

```yaml
---
author: Name
created: YYYY-MM-DD
modified: YYYY-MM-DD
tags:
  - content
---
```

## Key Files

| File | Purpose |
|------|---------|
| `Start.md` | Vault entry point, links to all sections |
| `Glossar.md` | Central term definitions |
| `*-Index.md` | Chapter overview pages |
| `COMPLIANCE-REPORT.md` | Automated structure validation results |
