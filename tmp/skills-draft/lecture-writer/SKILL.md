---
name: lecture-writer
description: Create structured academic lecture notes for Obsidian vaults. Use when asked to write a new lecture chapter, course notes, or educational content following the open-lectures format with learning objectives, topics, exam relevance, and proper cross-references.
---

# Lecture Writer — Open Lectures

Create complete, well-structured lecture notes that follow repository conventions.

## Required output

- A Markdown file following the full lecture note structure
- Proper YAML frontmatter with all required fields
- Learning objectives (`[!info]` callout)
- Overview section
- At least 3 topic sections with substantive content
- Cross-references section (Zusammenhänge)
- Exam-relevant callout (`[!warning]`)
- Typical exam questions (`[!question]`)
- Sources section
- Further reading (`[!tip]` callout)

## Workflow

1. **Gather requirements:**
   - Topic and scope
   - Target vault and chapter location
   - Educational level (undergraduate, graduate, professional)
   - Specific learning objectives (or derive from topic)
   - Related existing notes to cross-reference

2. **Determine file location:**
   - Identify target directory (e.g., `L-VaultName/02-Topic/03-Chapter/`)
   - Determine next available file number prefix
   - Create descriptive filename: `NN-TopicName.md`

3. **Generate frontmatter:**
   ```yaml
   ---
   author: [Ask user or use default]
   title: [Topic title]
   tags:
     - content
     - [topic-specific tags]
   created: [Today's date YYYY-MM-DD]
   modified: [Today's date YYYY-MM-DD]
   ---
   ```

4. **Write content following this structure:**

   ```markdown
   # [Title]

   > [!info] **Lernziele**
   > Nach diesem Kapitel solltest du:
   > - [Objective 1]
   > - [Objective 2]
   > - [Objective 3]

   ---

   ## Überblick

   [Brief introduction to the topic and its significance]

   ## [Topic Section 1]

   [Substantive content with examples, diagrams where helpful]

   ## [Topic Section 2]

   [Continue with logical progression]

   ## [Topic Section 3]

   [Additional content as needed]

   ## Zusammenhänge

   Querverweise zu verwandten Themen:

   - → [[Related Topic A]]
   - → [[Related Topic B]]
   - → [[Prerequisite Topic C]]

   > [!warning] **Prüfungsrelevant**
   > - [Key point 1]
   > - [Key point 2]
   > - [Key point 3]

   > [!question] **Typische Prüfungsfragen**
   > - [Question 1]?
   > - [Question 2]?
   > - [Question 3]?

   ## Quellen

   - [Source 1: Author, Title, Year]
   - [Source 2: Author, Title, Year]

   > [!tip] **Weiterführende Links**
   > - [External Resource](URL)
   > - [[Internal deep-dive note]]
   ```

5. **Quality checks before delivery:**
   - All required sections present in correct order
   - Frontmatter complete with valid dates
   - At least 3 learning objectives
   - At least 3 exam-relevant points
   - At least 2 exam questions
   - Cross-references use `[[wiki-link]]` syntax
   - No pure black/white in any embedded diagrams
   - Sources are real and verifiable (never invent references)

6. **Present to user:**
   - Show the complete note
   - Confirm target file path
   - Ask for approval before saving

## Language

Write content in **German** unless the user explicitly requests English. Use formal academic German appropriate for university-level education.

## Content guidelines

- Prefer concrete examples over abstract explanations
- Include tables for comparisons where appropriate
- Use code blocks with language identifiers for technical content
- Add ASCII diagrams or request PNG creation for complex visuals
- Define technical terms on first use
- Build on concepts that should exist in prerequisite notes
