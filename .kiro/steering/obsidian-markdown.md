---
inclusion: fileMatch
fileMatchPattern: "**/*.md"
---

# Obsidian Markdown Guidelines

When working with Markdown files in this Obsidian vault, follow these conventions.

## Wiki-Style Internal Links

Use Obsidian's wiki-link syntax for internal links:

- `[[Note Name]]` - link to another note
- `[[Note Name|Display Text]]` - link with custom display text
- `[[Note Name#Heading]]` - link to a specific heading
- `[[Note Name#^block-id]]` - link to a specific block

## Embeds

Embed content from other notes:

- `![[Note Name]]` - embed entire note
- `![[Note Name#Heading]]` - embed specific section
- `![[image.png]]` - embed images from the vault
- `![[image.png|300]]` - embed with width constraint

## Illustrations

### ASCII Art and Text Diagrams

- ASCII illustrations must respect Obsidian's page width limitations
- Keep ASCII art narrow enough to display without horizontal scrolling
- Use monospace code blocks for ASCII diagrams:
  ```
  ┌─────────┐
  │  Box    │
  └─────────┘
  ```

### Generated and Derived Graphics

When creating graphics (e.g., rendered from ASCII, generated diagrams, exports):

- **Format**: PNG with transparent background
- **Theme-agnostic**: Use colors that work on both dark and light mode themes
  - Avoid pure black (`#000000`) or pure white (`#FFFFFF`) for lines/shapes
  - Prefer neutral grays or colors with sufficient contrast in both modes
  - Test visibility in both Obsidian themes before finalizing
- Store generated graphics in the `.assets/` directory alongside the source note

### Figure Captions

Every illustration or picture must have a description beneath it:

- **Identifier format**: `<topic-prefix>-<chapter-prefix>-<file-prefix>-<image-name>` 
  - The prefixes are derived from the directory structure where the file resides
  - The image name is the filename without extension
- **Color coding**: The identifier is styled in blue using CSS class

**Required CSS snippet** (Settings → Appearance → CSS snippets):

```css
/* .obsidian/snippets/figure-captions.css */
.fig-id {
  color: #4a86e8;
  font-weight: bold;
}
```

**Usage:**

```markdown
![[eniac.jpg]]
*<span class="fig-id">02-01-01-eniac</span>: Der ENIAC war einer der ersten vollelektronischen Universalrechner.*
```

**Examples based on directory structure:**

| File Location | Image | Figure ID |
|---------------|-------|-----------|
| `02-Betriebssysteme/01-Einfuehrung/01-01-Historie.md` | `eniac.jpg` | `02-01-01-eniac` |
| `02-Betriebssysteme/02-Architektur/02-01-Kerneltypen.md` | `monolithischer-kernel.png` | `02-02-01-monolithischer-kernel` |
| `03-Rechnernetze/04-Transport/03-02-TCP.md` | `tcp-handshake.png` | `03-04-02-tcp-handshake` |

The pattern ensures globally unique figure identifiers across the entire vault.

## Assets and Attachments

Pictures, attachments, and other media files used in a Markdown file must be stored in an `assets/` directory within the same directory as the Markdown file:

```
vault/
└── 02-Topic/
    └── 01-Chapter/
        ├── 01-some-note.md
        ├── 02-another-note.md
        └── assets/
            ├── screenshot.png
            └── diagram.png
```

- Directory name: `assets/` (visible directory for chapter-level assets)
- Reference assets using **filename only**: `![[screenshot.png]]`
- Obsidian resolves filenames via "shortest path" matching
- Keep assets co-located with their referencing notes for organization
- When moving a note, move its corresponding `assets/` contents as well
- **Important**: Use unique, descriptive filenames to avoid collisions across the vault

**Note**: The vault-root `.assets/` directory (hidden) is reserved for shared vault-wide assets like logos. Chapter-level `assets/` directories are visible.

## Tags

Use tags for organization:

- `#tag` - inline tags
- Place tags in YAML frontmatter when appropriate:
  ```yaml
  ---
  tags:
    - topic
    - subtopic
  ---
  ```

## Frontmatter

Include YAML frontmatter for metadata:

```yaml
---
title: Note Title
date: YYYY-MM-DD
tags: []
aliases: []
---
```

## Callouts

Use Obsidian callout syntax for highlighted blocks:

```markdown
> [!note]
> This is a note callout.

> [!warning]
> This is a warning.

> [!tip]
> Helpful tip here.

> [!info]
> Informational content.

> [!question]
> A question or consideration.
```

Callout types: `note`, `abstract`, `info`, `tip`, `success`, `question`, `warning`, `failure`, `danger`, `bug`, `example`, `quote`

## Code Blocks

Use fenced code blocks with language identifiers:

````markdown
```python
def example():
    pass
```
````

## Task Lists

- `- [ ]` - unchecked task
- `- [x]` - completed task
- `- [/]` - in progress (with Tasks plugin)
- `- [-]` - cancelled (with Tasks plugin)

## Footnotes

Use standard Markdown footnotes:

```markdown
Here is a statement[^1].

[^1]: This is the footnote content.
```

## Math (LaTeX)

- Inline: `$E = mc^2$`
- Block:
  ```markdown
  $$
  \int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
  $$
  ```

## Mermaid Diagrams

Use mermaid code blocks for diagrams:

````markdown
```mermaid
graph TD
    A[Start] --> B[Process]
    B --> C[End]
```
````

**Page width considerations**: Obsidian renders Mermaid diagrams within the note's content width. Keep diagrams compact to avoid horizontal overflow:

- Prefer vertical layouts (`TD`, `TB`) over horizontal (`LR`, `RL`) for complex diagrams
- Use short, concise node labels
- Break large diagrams into multiple smaller ones
- For wide diagrams, consider using subgraphs to organize content vertically
- Test diagram rendering in both editing and reading view

## Best Practices

1. **Atomic notes**: Keep notes focused on a single concept
2. **Descriptive titles**: Use clear, searchable note titles
3. **Link liberally**: Create connections between related notes
4. **Use headings**: Structure content with proper heading hierarchy (H1 for title, H2+ for sections)
5. **Consistent naming**: Follow a naming convention for files (e.g., kebab-case or Title Case)
