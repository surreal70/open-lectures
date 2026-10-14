---
name: source-extractor
description: Extract and process text content from source files like PDFs, Word documents, or other formats. Use when converting existing lecture materials, importing external content, or extracting information from reference documents. Handles various input formats and prepares content for further processing.
---

# Source Extractor — Open Lectures

Extract text and structure from external source files for use in lecture note creation.

## ⚠️ Copyright-Hinweis — Wichtig!

> **Dieser Skill dient ausschließlich der Verarbeitung von:**
> - **Eigenen Materialien** — Ihre persönlichen Notizen, Skripte, Ausarbeitungen
> - **Frei lizenzierten Inhalten** — CC-BY, CC-BY-SA, Public Domain, MIT, etc.
> - **Mit Genehmigung** — Materialien, für die Sie explizite Erlaubnis haben
>
> **Dieser Skill ist NICHT dazu gedacht:**
> - Urheberrechtlich geschützte Bücher, Papers oder Skripte zu kopieren
> - Kostenpflichtige Inhalte zu extrahieren und weiterzuverbreiten
> - Copyright-Schutzmechanismen zu umgehen
>
> **Ihre Verantwortung:**
> - Prüfen Sie vor der Extraktion die Lizenz/Copyright-Situation
> - Respektieren Sie die Rechte der Urheber
> - Geben Sie Quellen korrekt an (Attribution)
> - Im Zweifel: Nicht extrahieren oder Erlaubnis einholen

Die Open Lectures stehen unter CC-BY-NC 4.0. Inhalte, die Sie einfügen, müssen mit dieser Lizenz kompatibel sein.

## Use cases

1. **PDF extraction** — Extract text from lecture slides, papers, or scanned documents
2. **Document conversion** — Process Word, PowerPoint, or other Office formats
3. **Batch processing** — Extract content from multiple files in a directory
4. **Content preparation** — Prepare extracted text for the lecture-processor skill

## Supported input formats

| Format | Extension | Extraction Method | Notes |
|--------|-----------|-------------------|-------|
| PDF | `.pdf` | `pdftotext` | Use `-layout` for formatted output |
| Word | `.docx` | `pandoc` or `docx2txt` | Preserves basic structure |
| PowerPoint | `.pptx` | `pptx2md` or manual | Slide-by-slide extraction |
| Plain text | `.txt`, `.md` | Direct read | No conversion needed |
| HTML | `.html` | `pandoc` or `html2text` | Strip tags, preserve structure |
| LaTeX | `.tex` | Direct read or `pandoc` | Preserve math notation |

## Workflow

### 1. Identify source file(s)

Ask user for:
- File path or directory
- Specific pages/sections if applicable
- Expected content type (slides, paper, notes)

### 2. License Check (MANDATORY)

**Before any extraction, perform a license check:**

1. **Search for license indicators in the document:**
   - Copyright notices (©, "Copyright", "All rights reserved")
   - License statements (CC-BY, MIT, GPL, "Public Domain")
   - Publisher information
   - "Do not distribute" or similar restrictions

2. **Check metadata:**
   ```bash
   # PDF metadata
   pdfinfo "input.pdf" | grep -i -E "(author|creator|producer|copyright)"
   
   # Extract first/last pages for copyright info
   pdftotext -f 1 -l 2 "input.pdf" - | grep -i -E "(copyright|license|©|\(c\))"
   ```

3. **Classify the license:**

| Category | Examples | CC-BY-NC 4.0 Compatible | Action |
|----------|----------|------------------------|--------|
| ✅ **Compatible** | CC-BY, CC-BY-SA, CC-BY-NC, CC0, Public Domain, MIT, Apache | Yes | Proceed |
| ⚠️ **Requires check** | CC-BY-ND, CC-BY-NC-ND, GPL | Maybe | Ask user |
| ❌ **Incompatible** | "All rights reserved", Commercial publishers, No license stated | No | **STOP - Require explicit consent** |
| 👤 **Own content** | User confirms ownership | Yes | Proceed |

4. **Decision flow:**

```
┌─────────────────────────────────────────────────────────────┐
│                    LICENSE CHECK                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  License found?                                             │
│       │                                                     │
│       ├── YES, Compatible (CC-BY, Public Domain, etc.)      │
│       │       └── ✅ PROCEED with extraction                │
│       │                                                     │
│       ├── YES, Incompatible or restrictive                  │
│       │       └── ⛔ STOP - Show warning, require consent   │
│       │                                                     │
│       └── NO license information found                      │
│               │                                             │
│               └── ⚠️ ASK USER:                              │
│                   "No license found. Is this:"              │
│                   a) Your own content?                      │
│                   b) Content you have permission for?       │
│                   c) Unknown origin?                        │
│                                                             │
│                   If (a) or (b): Proceed with user confirm  │
│                   If (c): STOP - Cannot extract             │
└─────────────────────────────────────────────────────────────┘
```

5. **When incompatible license detected - MANDATORY CONSENT:**

```
⛔ LICENSE WARNING ⛔

The document appears to have a restrictive or incompatible license:
- Detected: [Copyright notice / License type]
- Source: [Where found in document]

This content may NOT be compatible with CC-BY-NC 4.0.

To proceed, you must explicitly confirm ONE of the following:
1. "I am the copyright holder of this content"
2. "I have written permission from the copyright holder"
3. "This is for personal study only and will NOT be committed to the repository"

Type your confirmation or "abort" to cancel.
```

**If user does not provide explicit confirmation → ABORT extraction.**

**If user confirms option 3 (personal study):**
- Extract to `/tmp/` only (not tracked by git)
- Add header: `<!-- PERSONAL STUDY ONLY - DO NOT COMMIT -->`
- Remind user not to commit this content

### 3. Check available tools

```bash
# Check for PDF tools
which pdftotext    # poppler-utils
which pdfplumber   # Python library
which pdf2txt      # pdfminer

# Check for document converters
which pandoc       # Universal converter
which docx2txt     # Word documents
which antiword     # Older .doc files

# Check for other tools
which html2text    # HTML conversion
which xlsx2csv     # Excel files
```

### 4. Extract content

**PDF extraction:**
```bash
# Layout-preserving (best for slides/tables)
pdftotext -layout "input.pdf" -

# Simple text extraction
pdftotext "input.pdf" -

# Specific pages
pdftotext -f 5 -l 10 "input.pdf" -
```

**Word extraction:**
```bash
# Using pandoc (preserves structure)
pandoc -f docx -t markdown "input.docx"

# Using docx2txt (plain text)
docx2txt "input.docx" -
```

**PowerPoint extraction:**
```bash
# Using pandoc
pandoc -f pptx -t markdown "input.pptx"
```

**HTML extraction:**
```bash
# Using pandoc
pandoc -f html -t markdown "input.html"

# Using html2text
html2text "input.html"
```

### 5. Analyze extracted content

After extraction, identify:
- **Structure elements**: Headings, sections, slide breaks
- **Tables**: May need reformatting for Markdown
- **Code blocks**: Identify language, fix formatting
- **Images**: Note references (cannot extract images directly)
- **Math formulas**: Preserve LaTeX notation
- **Lists**: Bullet points, numbered lists
- **Metadata**: Title, author, date if present

### 6. Clean and normalize

**Common cleanup tasks:**
- Remove excessive whitespace
- Fix broken line wraps
- Reconstruct tables
- Identify and mark slide/page breaks
- Convert special characters
- Fix encoding issues

**Slide-specific cleanup:**
```
# Slide markers (from PDF slides)
Look for patterns like:
- Page numbers at bottom
- Repeated headers/footers
- "© Author" copyright lines
- Slide titles at top

# Convert to structure:
---
## Slide: [Title]
[Content]
---
```

### 7. Output options

**Option A: Raw extraction**
- Save to `/tmp/` or workspace `tmp/`
- Preserve original structure
- Add extraction metadata header

**Option B: Structured outline**
- Identify logical sections
- Create Markdown headers
- Group related content

**Option C: Direct to lecture-processor**
- Pass extracted content to lecture-processor skill
- Chain the workflows

### 8. Save extracted content

```markdown
---
source_file: [Original filename]
source_format: [PDF/DOCX/etc.]
extracted_date: [Today]
extraction_tool: [pdftotext/pandoc/etc.]
pages_extracted: [all or range]
---

# Extracted Content: [Source Name]

[Extracted text follows...]
```

## Handling specific content types

### Lecture slides (PDF)

Slides typically have:
- Title on each slide
- Bullet points
- Diagrams (noted as `[FIGURE]` or `[DIAGRAM]`)
- Footer with page number and copyright

**Processing strategy:**
1. Extract with `-layout` to preserve structure
2. Identify slide boundaries (page breaks, title patterns)
3. Convert each slide to a section
4. Mark image placeholders
5. Preserve tables as best as possible

### Academic papers (PDF)

Papers typically have:
- Abstract
- Sections with numbered headings
- References
- Footnotes

**Processing strategy:**
1. Extract full text
2. Identify section headers
3. Handle multi-column layouts (may need manual cleanup)
4. Extract bibliography separately

### Presentation scripts (DOCX/TXT)

Scripts may have:
- Speaker notes
- Timestamps
- Cue markers

**Processing strategy:**
1. Identify main content vs. speaker notes
2. Extract core information
3. Convert cues to callouts if relevant

## Error handling

| Issue | Solution |
|-------|----------|
| Tool not installed | Suggest installation command |
| Encrypted PDF | Ask for password or note limitation |
| Scanned PDF (images) | Suggest OCR tool (tesseract) |
| Corrupted file | Report error, try alternative tool |
| Encoding issues | Try different encoding flags |
| Empty extraction | Check file, try alternative method |

## Tool installation hints

```bash
# Debian/Ubuntu
sudo apt install poppler-utils    # pdftotext
sudo apt install pandoc           # Universal converter
sudo apt install tesseract-ocr    # OCR for scanned docs

# macOS (Homebrew)
brew install poppler
brew install pandoc
brew install tesseract

# Python alternatives
pip install pdfplumber    # PDF with better table handling
pip install python-docx   # Word documents
pip install pptx          # PowerPoint
```

## Integration with other skills

**Chain with lecture-processor:**
1. Extract content with source-extractor
2. Review extracted text
3. Pass to lecture-processor for formatting
4. Review and save final note

**Chain with lecture-writer:**
1. Extract key topics from source
2. Use as input/reference for lecture-writer
3. Incorporate specific examples from source

## Quality checklist

After extraction, verify:
- [ ] Text is readable (no garbled characters)
- [ ] Structure is identifiable
- [ ] Tables are roughly preserved
- [ ] No critical content missing
- [ ] Encoding is correct (umlauts, special chars)
- [ ] Image locations are noted

## Example session

```
User: Extract the content from input-betriebssysteme-pdfs/lecture-01.pdf

Agent: I'll extract the PDF content. Let me check the available tools first.

[Checks pdftotext is available]

Agent: Extracting with layout preservation...

[Runs: pdftotext -layout "lecture-01.pdf" -]

Agent: I've extracted 15 slides covering:
1. Introduction (slides 1-3)
2. History of Networks (slides 4-8)
3. Network Types (slides 9-12)
4. Summary (slides 13-15)

There are 3 diagrams referenced that couldn't be extracted.

Would you like me to:
a) Save the raw extraction to tmp/
b) Structure it into sections
c) Pass it directly to lecture-processor
```
