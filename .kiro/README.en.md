# .kiro - AI Agent Configuration

This directory contains configurations and tools for working with AI agents like [Kiro](https://kiro.dev).

## ⚠️ Note on External Content

The skills provided here enable extraction and processing of external documents (PDFs, Word, etc.). **Please note:**

- ✅ **Allowed:** Your own notes, CC-licensed content, Public Domain, materials with permission
- ❌ **Not allowed:** Copyrighted works without permission

Content you add to this repository must be compatible with the **CC-BY-NC 4.0 license**. When in doubt: check sources, obtain permission, or don't use.

## Who is this relevant for?

- **Obsidian users**: You can completely ignore this directory. The vaults work without AI support.
- **Contributors with AI support**: Here you'll find skills and steering files that simplify working with Kiro.

## Directory Structure

```
.kiro/
├── README.md           # German version
├── README.en.md        # This file (English)
├── requirements.txt    # Python dependencies for AI tools
├── settings/           # Kiro settings
├── skills/             # Reusable AI workflows
│   ├── create-png/           # Create PNG graphics
│   ├── exercise-generator/   # Generate exercises
│   ├── lecture-processor/    # Format raw notes
│   ├── lecture-writer/       # Write new lectures
│   ├── markdown-validator/   # Check markdown conventions
│   ├── source-extractor/     # Extract text from PDFs/docs
│   └── vault-creator/        # Scaffold new vaults
└── steering/           # Context files for AI behavior
    ├── obsidian-lecture-notes.md  # Lecture note conventions
    ├── obsidian-markdown.md       # Markdown rules
    ├── structure.md               # Repo structure
    └── tech.md                    # Tech stack
```

## Setup for AI-Assisted Work

### 1. Install System Tools

```bash
# Debian/Ubuntu
sudo apt install poppler-utils pandoc tesseract-ocr

# macOS (Homebrew)
brew install poppler pandoc tesseract

# Windows (Chocolatey)
choco install poppler pandoc tesseract
```

### 2. Install Python Dependencies (optional)

If you use Python-based extraction or image processing:

```bash
# With virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
pip install -r .kiro/requirements.txt
```

### 3. Start Kiro

Open the repository in Kiro. Skills and steering files are automatically detected.

## Using Skills

In Kiro, you can activate skills with `#skill-name`:

| Skill | Purpose | Activation |
|-------|---------|------------|
| **lecture-writer** | Create new lecture note | `#lecture-writer` |
| **lecture-processor** | Format raw notes | `#lecture-processor` |
| **source-extractor** | Extract text from PDFs | `#source-extractor` |
| **exercise-generator** | Create exercises | `#exercise-generator` |
| **markdown-validator** | Check conventions | `#markdown-validator` |
| **create-png** | Diagrams as PNG | `#create-png` |
| **vault-creator** | Create new vault | `#vault-creator` |

## Example Workflow

```
User: #source-extractor Extract input-betriebssysteme/lecture-01.pdf

Agent: [Extracts text from PDF]

User: #lecture-processor Format this as a lecture note

Agent: [Creates structured Markdown file]
```

## Working Without AI

This repository is fully usable without AI support:

1. Open a vault (e.g., `L-Betriebssysteme, Rechnernetze und verteilte Systeme/`) in Obsidian
2. Use the templates in `.templates/` for new notes
3. Follow the conventions in `HOWTO.md`

You can hide `.kiro/` directories in Obsidian via Settings → Files & Links → Excluded Files.
