# Review of Your Kiro Steering Files: What Should Stay Steering, and What Should Become a Skill?

I've reviewed all three files from your `open-lectures` repository:

1. `obsidian-lecture-notes.md` — 326 lines
2. `obsidian-markdown.md` — 227 lines
3. `repository-structure.md` — 83 lines

## 1. Overall assessment

Your current configuration already provides a solid foundation for creating structured educational material in Obsidian.

However, I see an opportunity to make it **more modular, easier to maintain, and more efficient for Kiro**.

The main issue is that your steering documents currently mix three different types of information:

- **Standards:** Rules that should always apply.
- **Workflows:** Instructions for performing specific tasks.
- **Templates:** Examples that define the structure of generated content.

I recommend separating them.

### The fundamental distinction

| Steering document | Skill |
|---|---|
| Defines rules and conventions | Defines how to perform a task |
| Describes what must be respected | Describes what steps to execute |
| Provides project context | Provides reusable procedures |
| Generally short and declarative | Can contain instructions, scripts, templates and references |
| Applied according to Kiro's inclusion settings | Loaded when the corresponding task requires it |
| Example: Use Obsidian wiki-links | Example: Generate a complete lecture chapter |

**My main recommendation is to keep your formatting, naming, metadata, and repository rules in steering files, while moving document creation, lecture processing, and repository maintenance workflows into Skills.**

---

## 2. Assessment of each existing file

### A. `obsidian-markdown.md`

**Recommendation: Keep approximately 80% as steering.**

This file contains mostly formatting conventions, which are exactly what steering documents are intended for.

Your existing rules include:

- Obsidian wiki-links and embeds.
- Diagram formatting.
- Image naming and captions.
- Asset directories.
- Frontmatter.
- Callouts.
- Code blocks.
- Mathematical formulas.
- Mermaid diagrams.

These should generally remain steering instructions.

For example, your requirement that images be placed in chapter-specific `assets/` directories and referenced by filename is a repository-wide convention, not a workflow. obsidian-markdown

**What I would move into Skills:**

The process of generating illustrations, preparing diagrams, validating their display, and checking the rendered results.

A steering document should specify:

> Images must follow the project's naming and caption conventions.

An image-generation Skill should explain:

> Generate the illustration, apply the required conventions, save it in the correct directory, insert its reference, and validate the result.

I would rename this steering file to:

`obsidian-markdown-standards.md`

### B. `obsidian-lecture-notes.md`

**Recommendation: Split this file into steering, templates, and Skills.**

This file contains the greatest mixture of responsibilities.

It includes:

- Vault directory structure.
- File naming rules.
- Frontmatter requirements.
- Lecture note structure.
- Cross-referencing conventions.
- Note-taking workflows.
- Post-lecture processing.
- Mathematical content guidelines.
- Code example requirements.
- Callout conventions.

Your prescribed lecture structure includes learning objectives, an overview, topic sections, cross-references, examination notes, examination questions, sources, and further reading. obsidian-lecture-notes

I would preserve this structure, but move its detailed template into a reusable Markdown template file.

The steering document would simply require all newly generated lecture notes to follow that template.

**What should remain steering:**

- Mandatory frontmatter fields.
- File naming conventions.
- Required lecture sections.
- Tagging conventions.
- Obsidian linking rules.
- Mathematical notation requirements.
- Code example quality requirements.
- Callout conventions.

**What should become Skills:**

- Creating a new lecture chapter.
- Processing raw lecture notes.
- Generating examination questions.
- Creating exercises and solutions.
- Generating illustrations.
- Maintaining cross-references.

Your existing *During-Lecture Capture* and *Post-Lecture Processing* sections are particularly good candidates for a Skill because they describe sequences of activities rather than permanent formatting rules. obsidian-lecture-notes

I would rename the remaining steering file to:

`lecture-content-standards.md`

### C. `repository-structure.md`

**Recommendation: Keep the structural rules as steering and extract repository operations into Skills.**

This file describes your repository architecture, including independent Obsidian vaults and their naming conventions.

These are fundamental project constraints and should remain steering.

An important requirement is that individual vaults must not reference or share files with one another. repository-structure

I would preserve this rule exactly.

However, the file also contains procedural instructions for adding a vault, updating repository documentation, and maintaining status information. repository-structure

These operations belong in Skills.

I would rename the steering file to:

`repository-standards.md`

---

## 3. Problems and inconsistencies I found

Before reorganizing the files, I would resolve five issues.

### Issue 1: Inconsistent frontmatter definitions

Your two Obsidian steering files define different metadata structures.

**`obsidian-markdown.md`:**
```yaml
---
title: Note Title
date: YYYY-MM-DD
tags: []
aliases: []
---
```

**`obsidian-lecture-notes.md`:**
```yaml
---
author: Author Name
created: YYYY-MM-DD
modified: YYYY-MM-DD
tags:
  - content
---
```

Both definitions are currently valid according to their respective steering files, but they are not equivalent.

**Recommendation:** Define one canonical frontmatter schema and use it everywhere.

For example:

```yaml
---
title: "Introduction to Cryptography"
author: "Author Name"
created: 2026-10-10
modified: 2026-10-10
tags:
  - cryptography
  - lecture
aliases: []
---
```

Keep the schema in one steering document and reference it from the others.

### Issue 2: Inconsistent asset directory naming

Your files reference both:

```text
.assets/
```

and:

```text
assets/
```

The markdown rules mention `.assets/` for generated graphics but also require chapter-level `assets/` directories. obsidian-markdown obsidian-markdown

I recommend:

```text
vault/
├── .assets/                  # Shared vault-wide assets
└── 01-Topic/
    └── 01-Chapter/
        └── assets/           # Chapter-specific assets
```

This matches the later, more explicit distinction already present in your Markdown rules.

### Issue 3: Inconsistent file naming

One document requires:

```text
NN-Titel.md
```

However, examples also use filenames such as:

```text
02-01-Kerneltypen.md
```

These conventions should be reconciled.

I recommend using **one local sequence number per directory**:

```text
02-Betriebssysteme/
└── 02-Architektur/
    ├── 01-Kerneltypen.md
    ├── 02-Schichtenmodell.md
    └── assets/
```

The full path provides the chapter context, so repeating the parent prefix in the filename is unnecessary.

Your figure-caption identifier can still incorporate the complete directory hierarchy.

### Issue 4: Repository status tracking

Your repository steering file contains a table for tracking vault statuses.

It also requires the table to be updated when a vault is added, substantially modified, or changes status. repository-structure

I would move the actual status table out of steering.

Instead, create:

```text
open-lectures/
└── docs/
    └── vault-status.md
```

Then create a `vault-maintenance` Skill responsible for updating it.

This separates operational data from instructions.

### Issue 5: Lecture note templates are embedded in steering

Your lecture-note steering file contains an entire example document.

While helpful, maintaining the example inside steering means the model may need to process a long template even when it isn't creating a lecture.

I would move it to:

```text
.kiro/skills/lecture-writer/assets/lecture-template.md
```

The steering file should contain only the rules that all lecture notes must respect.

The Skill would load the template when generating new lectures.

---

# 4. My proposed new architecture

I recommend **three steering documents and six Skills** as an initial implementation.

Kiro currently supports workspace Skills in `.kiro/skills/`, with a `SKILL.md` entry point. Skills can activate automatically or be invoked as slash commands. See the [official Kiro Skills documentation](https://kiro.dev/docs/skills/). [Kiro](https://kiro.dev/docs/skills/?utm_source=chatgpt.com)

### Proposed repository layout

```text
open-lectures/
│
├── .kiro/
│   │
│   ├── steering/
│   │   │
│   │   ├── repository-standards.md
│   │   │
│   │   ├── obsidian-markdown-standards.md
│   │   │
│   │   └── lecture-content-standards.md
│   │
│   └── skills/
│       │
│       ├── vault-creator/
│       │   └── SKILL.md
│       │
│       ├── lecture-writer/
│       │   ├── SKILL.md
│       │   └── assets/
│       │       └── lecture-template.md
│       │
│       ├── lecture-processor/
│       │   └── SKILL.md
│       │
│       ├── exercise-generator/
│       │   └── SKILL.md
│       │
│       ├── markdown-validator/
│       │   ├── SKILL.md
│       │   └── scripts/
│       │       └── validate.py
│       │
│       └── vault-maintenance/
│           └── SKILL.md
│
├── docs/
│   └── vault-status.md
│
├── mathematik-1/
│
├── mathematik-2/
│
├── kryptographie/
│
├── informatik/
│
├── README.md
│
└── LICENSE
```

The vault names above are illustrative, not an assumption that these directories already exist.

---

# 5. Recommended steering documents

| File | Purpose | Inclusion |
|---|---|---|
| `repository-standards.md` | Repository structure, vault independence, naming | `always` |
| `obsidian-markdown-standards.md` | Wiki-links, assets, callouts, diagrams, formatting | `fileMatch` |
| `lecture-content-standards.md` | Mandatory structure, learning objectives, metadata, teaching conventions | `auto` |

The `fileMatch` document should target Markdown files in your vaults. If Kiro also processes configuration Markdown or Skill files, I would narrow its scope where possible.

For lecture-content standards, I would use `auto` rather than the current `manual` setting. Your current lecture-notes file uses manual inclusion, meaning it must be explicitly selected rather than automatically applied based on the task. obsidian-lecture-notes

Using `auto` makes sense when you want Kiro to recognize lecture-related tasks without manually activating the rules.

---

# 6. Recommended Skills

I would start with the following six.

| Skill | Input | Output |
|---|---|---|
| **vault-creator** | Course name, subject, level | Complete Obsidian vault structure |
| **lecture-writer** | Topic, level, learning objectives | Structured lecture chapter |
| **lecture-processor** | Raw lecture notes | Clean, organized lecture document |
| **exercise-generator** | Chapter and difficulty | Exercises and separate solutions |
| **markdown-validator** | Markdown file or vault | Validation report and optional fixes |
| **vault-maintenance** | Maintenance request | Updated indexes, links, status and metadata |

A particularly important distinction is that the **Markdown validator should enforce the steering rules rather than maintain a separate set of standards**.

Otherwise, you risk creating conflicting definitions in two places.

### Example: Lecture Writer Skill

A minimal Kiro Skill could look like this:

```markdown
---
name: lecture-writer
description: >
  Create structured academic lecture chapters
  for the open-lectures Obsidian repository.
  Use when generating new educational chapters,
  course notes, or detailed teaching material.
---

# Lecture Writer

## Workflow

1. Identify subject, educational level,
   learning objectives, and target vault.

2. Read applicable repository and
   lecture-content steering rules.

3. Load the lecture template from:
   assets/lecture-template.md

4. Generate the lecture content.

5. Include explanations, examples,
   and appropriate cross-references.

6. Add relevant examination questions.

7. Include verifiable sources.
   Never invent references.

8. Apply the required YAML frontmatter.

9. Save the Markdown file using the
   repository naming conventions.

10. Validate the resulting document.
```

This is a reusable workflow rather than a permanent repository rule.

You could activate it in Kiro with a request such as:

```text
/lecture-writer Create a chapter about AES encryption
for an undergraduate cryptography course.
```

---

# 7. How the new system would work

Imagine you ask Kiro:

> Create a complete lecture about symmetric cryptography for undergraduate students.

The workflow would be:

```text
                    USER REQUEST
                          |
                          v
                     KIRO AGENT
                          |
          +---------------+---------------+
          |                               |
          v                               v
    STEERING FILES                   SKILL SELECTION
          |                               |
          |                               v
          |                         lecture-writer
          |                               |
          v                               v
    Repository Rules                Lecture Template
    Markdown Rules                  Content Generation
    Lecture Standards               Examples and Questions
          |                               |
          +---------------+---------------+
                          |
                          v
                  GENERATED LECTURE
                          |
                          v
                   markdown-validator
                          |
                          v
                     OBSIDIAN VAULT
```

The steering files establish constraints. The writing Skill performs the task. The validation Skill checks the output.

This separation makes it easier to extend the system later.

---

# 8. What I would prioritize

I would implement the changes in three phases.

**Phase 1 – Consolidate the standards.** Resolve the inconsistent frontmatter, file naming, and asset directory conventions. Then shorten the three existing steering files without removing essential requirements.

**Phase 2 – Extract the core workflows.** Implement `lecture-writer`, `vault-creator`, and `markdown-validator` first. These provide the most immediate value for your educational content.

**Phase 3 – Extend the automation.** Add `exercise-generator`, `lecture-processor`, and `vault-maintenance`. Later, you could introduce more specialized Skills for mathematics, chemistry, programming, and cryptography.

### Final recommendation

**Don't convert all your steering files into Skills.** Most of your existing Markdown and repository conventions belong in steering.

The biggest improvement would be to extract the procedures for generating, processing, validating, and maintaining lecture content.

I would also avoid duplicating standards across multiple steering files. Each rule should have one authoritative location.

Your existing conventions are detailed enough to support a highly automated educational content system; the next step is to separate the rules from the operations that use them.

**Would you like me to take the next step and actually refactor your three uploaded files into the proposed steering documents and six ready-to-install Kiro Skills, preserving your existing conventions wherever they don't conflict?**