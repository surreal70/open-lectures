---
name: lecture-processor
description: Transform raw or draft lecture notes into properly formatted Obsidian documents. Use when cleaning up quick capture notes, imported content, or rough drafts. Applies structure, formatting, and metadata conventions while preserving content.
---

# Lecture Processor — Open Lectures

Convert raw, unstructured, or imported content into properly formatted lecture notes.

## Use cases

1. **Quick capture cleanup** — Notes taken during a lecture with `(?)` markers and TODOs
2. **Import conversion** — Content from PDFs, Word docs, or other sources
3. **Draft refinement** — Rough outlines that need full structure
4. **Format migration** — Existing notes that don't follow conventions

## Input types accepted

- Bullet-point notes
- Unformatted text dumps
- Partially structured Markdown
- Pasted content from external sources
- Notes with TODO markers and questions

## Output

A properly structured lecture note following all conventions:
- Complete frontmatter
- Full section structure (Lernziele → Quellen)
- Cleaned formatting
- Resolved TODOs (or flagged for user)
- Wiki-link cross-references

## Workflow

1. **Receive raw content:**
   - User provides content directly in chat, OR
   - User points to existing file to process

2. **Analyze content:**
   - Identify main topic and subtopics
   - Find existing structure (headings, lists)
   - Locate `(?)` uncertain markers
   - Find `TODO:` items
   - Identify potential cross-reference targets
   - Detect any existing frontmatter

3. **Plan transformation:**
   - Map content to required sections
   - Identify gaps (missing Lernziele, no sources, etc.)
   - List questions that need user input

4. **Handle uncertainties:**
   
   For `(?)` markers:
   ```markdown
   Original: "The algorithm runs in O(n²) time (?)"
   
   Options:
   a) Verify and remove marker
   b) Flag for user to confirm
   c) Research and correct
   ```
   
   For `TODO:` items:
   ```markdown
   Original: "TODO: add diagram of process flow"
   
   Options:
   a) Create the content now
   b) Convert to [!question] callout for later
   c) Remove if no longer needed
   ```

5. **Ask clarifying questions:**
   - What should the file be named?
   - Where should it be saved?
   - Any specific learning objectives to emphasize?
   - Should uncertain items be flagged or resolved?

6. **Transform content:**

   **Add frontmatter:**
   ```yaml
   ---
   author: [Determine from context or ask]
   title: [Extract from content]
   tags:
     - content
     - [derived topic tags]
   created: [Today or original date if known]
   modified: [Today]
   ---
   ```

   **Structure sections:**
   - Derive Lernziele from content themes
   - Write Überblick from introduction or first paragraphs
   - Organize body into logical H2 sections
   - Generate Zusammenhänge from mentioned topics
   - Extract or create Prüfungsrelevant points
   - Formulate Prüfungsfragen from key concepts
   - Compile Quellen from any citations found
   - Add Weiterführende Links if URLs present

   **Clean formatting:**
   - Fix inconsistent heading levels
   - Standardize list formatting
   - Convert external links to proper format
   - Convert internal references to wiki-links
   - Fix code block language identifiers
   - Standardize callout syntax

7. **Present transformed note:**
   - Show complete processed note
   - Highlight what was changed/added
   - List any remaining TODOs or uncertainties
   - Ask for approval

8. **Save if approved:**
   - Write to specified location
   - Or replace original file (with confirmation)

## Processing rules

### Preserve
- Technical accuracy of content
- Code examples (fix formatting only)
- Mathematical formulas
- Specific terminology
- Author's explanations and examples

### Transform
- Unstructured text → proper sections
- Inline TODOs → callouts or resolved
- Plain URLs → proper links
- Inconsistent formatting → standardized
- Missing metadata → generated

### Flag for user
- Uncertain facts `(?)`
- Missing required information
- Ambiguous content organization
- Potential factual errors

## Language handling

- Preserve original language of content
- If mixed, ask user for preferred primary language
- Technical terms may remain in English within German text
