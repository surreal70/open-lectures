---
name: markdown-validator
description: Validate Obsidian lecture notes against repository steering rules. Use when checking if a note complies with conventions, auditing a chapter or vault, or generating a compliance report. Checks frontmatter, structure, callouts, figure captions, asset locations, and cross-references.
---

# Markdown Validator — Open Lectures

Validate lecture notes against the open-lectures steering rules and report issues.

## Validation scope

Can validate:
- A single Markdown file
- All files in a chapter directory
- An entire vault
- Specific aspects only (e.g., just frontmatter)

## Checks performed

### 1. Frontmatter validation
- [ ] YAML frontmatter present and valid
- [ ] Required fields: `author`, `created`, `modified`, `tags`
- [ ] Date format: `YYYY-MM-DD`
- [ ] `modified` date not before `created` date
- [ ] At least one tag present
- [ ] Standard folder tag included (`content`, `organisation`, `praesentation`, `uebung`, `pruefung`, `anhang`)

### 2. Structure validation (for content notes)
- [ ] Single H1 title at top
- [ ] `[!info]` Lernziele callout present after title
- [ ] Überblick section present
- [ ] At least 3 topic sections (H2)
- [ ] Zusammenhänge section with cross-references
- [ ] `[!warning]` Prüfungsrelevant callout present
- [ ] `[!question]` Prüfungsfragen callout present
- [ ] Quellen section present
- [ ] `[!tip]` Weiterführende Links callout present
- [ ] Sections in correct order

### 3. File naming validation
- [ ] Filename matches pattern `NN-Title.md`
- [ ] No duplicate prefixes with parent directory
- [ ] Lowercase with hyphens (no spaces)

### 4. Asset validation
- [ ] Referenced images exist in `assets/` directory
- [ ] Image references use filename only: `![[image.png]]`
- [ ] Figure captions present with correct ID format
- [ ] Figure ID matches directory structure pattern

### 5. Link validation
- [ ] Internal links use `[[wiki-link]]` syntax
- [ ] Cross-reference links point to existing files
- [ ] No broken internal links
- [ ] External links use `[text](url)` format

### 6. Callout validation
- [ ] Valid callout types used
- [ ] Callouts have titles where expected
- [ ] Appropriate callout types for context

## Workflow

1. **Determine scope:**
   - Ask user for target: file, directory, or vault
   - Ask if full validation or specific checks only

2. **Read target files:**
   - Parse frontmatter
   - Extract document structure
   - Identify all references and links

3. **Run all applicable checks:**
   - Track issues by severity: ERROR, WARNING, INFO
   - Note line numbers where possible

4. **Generate report:**
   ```markdown
   # Validation Report

   **Target:** [path]
   **Date:** [timestamp]
   **Files checked:** [count]

   ## Summary

   | Severity | Count |
   |----------|-------|
   | Errors   | N     |
   | Warnings | N     |
   | Info     | N     |

   ## Issues by File

   ### [filename.md]

   | Line | Severity | Check | Issue |
   |------|----------|-------|-------|
   | 1    | ERROR    | frontmatter | Missing `author` field |
   | 45   | WARNING  | structure | Zusammenhänge section missing |

   ## Passed Checks

   - [List of checks that passed]
   ```

5. **Offer fixes:**
   - For auto-fixable issues (missing dates, tag formatting), offer to apply fixes
   - For structural issues, provide specific guidance
   - Never auto-fix without user approval

## Output options

- **Console:** Display report in chat
- **File:** Save as `COMPLIANCE-REPORT.md` in vault root or specified location
- **Both:** Display summary, save full report

## Severity definitions

| Severity | Meaning |
|----------|---------|
| ERROR | Violates required convention, must fix |
| WARNING | Deviates from best practice, should fix |
| INFO | Suggestion for improvement, optional |
