---
inclusion: auto
name: Tech Stack
description: Technology stack and tools used in the open-lectures project
---

# Technology Stack

## Primary Platform

**Obsidian** - Knowledge base application working on local Markdown files
- Each lecture is a self-contained Obsidian vault
- Uses wiki-style `[[links]]` for internal navigation
- Supports LaTeX math, Mermaid diagrams, and callout blocks

## File Format

- **Markdown** (.md) with YAML frontmatter
- **PNG** for images (transparent background, theme-agnostic colors)
- **Canvas** files for Obsidian visual notes

## Version Control

**Git** - All content is version-controlled

## No Build System

This is a content repository. There is no compilation, testing, or deployment pipeline.

## Editor Requirements

- **Obsidian** (recommended): Free download at obsidian.md
- Any Markdown editor works for basic editing, but advanced features (wiki-links, callouts, graph view) require Obsidian

## Common Tasks

| Task | How To |
|------|--------|
| View content | Open vault folder in Obsidian |
| Create new note | Use templates in `.templates/` directory |
| Add images | Place in `assets/` folder, reference with `![[filename.png]]` |
| Check links | Use Obsidian's graph view or search for broken links |
| Validate structure | Run compliance check against steering rules |

## Obsidian Plugins (Optional)

The vaults may include `.obsidian/` configurations with community plugins:
- Calendar, Dataview, Excalidraw, Spaced Repetition

## External Dependencies

None. All content is self-contained within the repository.
