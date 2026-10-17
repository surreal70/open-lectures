# How To: Create Your Own Vault

This guide explains how to build a brand-new lecture vault in this repository with Kiro – from the first conceptual thoughts to a finalized, convention-compliant Obsidian vault. It describes a recommended end-to-end workflow, provides ready-to-use example prompts, points to the existing steering and skills, and shows how to add your own.

> This repository is driven by Kiro (an AI agent). The fastest way to build a vault is to describe what you want in natural language and let the agent scaffold, fill, and check it – guided by the repository's steering files and skills.

---

## ⚖️ Licensing — Read This First

**Everything you add to this repository falls under the repository's license: [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](./LICENSE).**

That means content you contribute here may be:

- used, studied, shared and adapted by others **for free**,
- **with attribution**, and
- **for non-commercial purposes only**.

**If you do not want your material under these terms, create your own, separate repository instead of adding it here.**

And in the other direction: if you create a **derivative work** based on an existing vault (adapting, extending, remixing), you must honor the same license — **give attribution** to the original author(s) and keep the use **non-commercial**.

> ‼️ **Third-party material (sources, images, curricula): always respect copyright.** Only add content you created yourself or that is clearly licensed for this purpose (e.g. public domain or a compatible license). When in doubt, link to the original source instead of copying it, and record the source. This applies to text, images, diagrams, exercises, and exam questions alike.

---

## Publishing Your Vault Back to open-lectures

If you want to contribute your vault back into the open-lectures repository, keep your own Kiro configuration from clashing with the repository's shared setup.

**Avoid collisions with the global Kiro config.** The repository has shared steering, hooks, and skills under `.kiro/`. If you created your own, do **one** of the following so they don't overwrite or conflict with the global ones:

- **Namespace them.** Give your files an individual prefix, e.g. `.kiro/steering/myvault-conventions.md`, `.kiro/skills/myvault-exporter/`, `.kiro/hooks/myvault-check.json`.
- **Keep them out of sync.** Use `.gitignore` so your personal control files are not committed/synchronized into the shared repo.
- **Use a separate Kiro config.** Maintain your own Kiro control directory, independent of this repository, and only bring the vault content over.

> ‼️ **NEVER put passwords or credentials in your vault.** No access tokens, API keys, logins, or secrets — not in notes, not in frontmatter, not in steering/hooks/skills, not in example code. Anything committed here is public under the repository license. If a secret ever lands in a file, treat it as compromised, remove it, and rotate it.

---

## Workflow Overview

Creating a vault is a staged process. Work **top to bottom**, and within each content stage **module by module** rather than everything at once. Keep files as `draft` until the very end.

| # | Stage | Goal |
|---|-------|------|
| 1 | Scope & boundaries | Decide what the vault covers — and what it does not |
| 2 | Depth | Decide the target level and technical depth |
| 3 | Syllabus | Define the curriculum (own, from syllabi, or existing curricula — mind copyright) |
| 4 | Scaffold | Let the vault-creator build the empty structure |
| 5 | Metadata | Provide and apply the frontmatter defaults |
| 6 | Base content | Generate base content; optionally let the agent insert ASCII diagrams where helpful |
| 7 | Structure check | Review the result of the previous steps; correct precisely, piece by piece |
| 8 | Scope & depth tuning | Adjust content to the intended scope and technical depth (the AI can help) |
| 9 | Editorial pass | Check factual correctness, logic, and didactic sequencing |
| 10 | Graphics | Convert ASCII diagrams to PNGs per the guidelines; verify each is factually correct and appropriate; check captions |
| 11 | Images | Add image material — **mind copyright!** |
| 12 | Registers | Generate glossary, list of abbreviations, list of figures |
| 13 | Final review | Factual, content, and didactic review — ideally with a third person |
| 14 | Finalize | Only now mark files as `final`; before that they stay `draft` (version them if needed) |
| 15 | Continuous improvement | Fix errors, adjust/update content over time, and act on feedback |

---

## The 14 Steps in Detail

### 1. Think about scope and boundaries

Before anything is generated, be clear about **what belongs in the vault and what does not**. A sharp scope prevents sprawling, uneven material later. Note explicitly which neighbouring topics are *out* of scope and, where useful, which other vault covers them.

> **Prompt**
> I'm planning a vault on "[subject]". Help me define the scope: list what should be covered, what should be explicitly excluded, and which adjacent topics belong in other vaults. Ask me questions where the boundary is unclear.

### 2. Think about the depth

Decide the **target audience and level** (e.g. lower secondary, Abitur, undergraduate, professional certification). The depth determines vocabulary, which proofs/derivations are shown, and how much prior knowledge is assumed.

> **Prompt**
> The vault targets [audience/level]. Propose a suitable technical depth: what level of rigor, which derivations or proofs to include or omit, and what prior knowledge I may assume. Point out where depth decisions have didactic consequences.

### 3. Create a syllabus

Turn scope and depth into a **concrete curriculum**: an ordered list of modules (chapters), each with a short learning goal. Base it on your own outline, on official syllabi, or on existing curricula — **but respect copyright**: use curricula as orientation, do not copy protected text verbatim.

> **Prompt**
> Draft a syllabus for "[subject]" at [level]: modules in teaching order, each with a one-line learning objective. Base it on [my notes / the structure typical for this subject]. Do not copy any copyrighted curriculum text verbatim — use it only as orientation. Wait for my confirmation.

### 4. Commission the vault-creator

Let the `vault-creator` skill build the empty structure: directories, index files, templates, and basic Obsidian configuration.

> **Prompt**
> Load the vault-creator skill and scaffold a vault named "[Vault Name]" for "[Course Title]". Modules: [Topic 1], [Topic 2], [Topic 3], … . Author: [Your Name]. Language: German. Follow the repository conventions.

### 5. Provide and apply metadata

Agree on the **frontmatter defaults** (author, created/modified dates, tags, and a `status` of `draft`) and let the agent apply them consistently across all generated files.

> **Prompt**
> Set the frontmatter defaults for "[Vault Name]": author "[Your Name]", status "draft", created today, tags [list]. Apply them to every note and report any file that was missing frontmatter.

### 6. Generate base content

Fill the modules with **base content first** — don't aim for final depth yet. Tell the agent where to add ASCII diagrams from the context or your source material (they are easy to refine and later convert to PNGs).

> **Prompt**
> Load the lecture-writer skill and write base content for Module [N] "[Chapter Title]" of "[Vault Name]": one note per subtopic with learning objectives, exam relevance, and cross-references. Keep it at base depth and status draft. Where a concept benefits from a sketch, insert a simple ASCII diagram in a code block.

> ‼️ If you draw on your own documents or public-domain/compatibly-licensed sources, keep the copyright note from the top in mind and record sources.

### 7. Check the structure

Review the output of the previous steps: naming, indexes, cross-links, frontmatter, folder layout. Have corrections made **precisely and incrementally** — ask for reasoning where a change is non-obvious, and fix things step by step rather than all at once.

> **Prompt**
> Audit the structure of "[Vault Name]" so far: file naming, index files, cross-links, and frontmatter. List problems with a short reason each. Then fix them one group at a time, pausing after each so I can confirm — do not change everything at once.

### 8. Tune scope and depth

Now bring the content to the **intended scope and technical depth**. Expand thin sections, trim out-of-scope detours, and align difficulty with the decisions from steps 1–2. The AI can suggest where content is too shallow or too deep.

> **Prompt**
> Compare Module [N] against our agreed scope and depth ([recap]). Point out sections that are too shallow, too deep, or out of scope, and propose concrete adjustments before applying them.

### 9. Editorial pass

Check **factual correctness, internal logic, and didactic ordering**: does each concept build on what came before? Are definitions introduced before they are used?

> **Prompt**
> Do an editorial pass over Module [N]: verify factual correctness, logical consistency, and didactic sequencing (nothing used before it is introduced). Report issues with reasoning, then fix them incrementally.

### 10. Convert ASCII diagrams to PNG graphics

Convert the ASCII diagrams into PNGs **per the graphics guidelines**. For each diagram, verify that the rendering is **factually correct** and **appropriate** for the concept it illustrates, and that the **figure caption** follows the convention (identifier + description).

> **Prompt**
> Convert the ASCII diagrams in [file] to PNGs following the create-png skill and the math-graphics steering. For each, confirm the depiction is mathematically/factually correct and suited to the point being made. Show light/dark previews before applying, and use the correct figure-caption format.

> For structural diagrams (learning paths, flows, hierarchies) prefer **Mermaid** blocks so they stay editable and width-safe.

### 11. Add image material

Add photographs or other images where they help — **and mind copyright strictly**. Use only self-made images or clearly compatible licenses; store assets next to the note per the conventions and caption them.

> **Prompt**
> Suggest where an image would strengthen Module [N], and list what each image should show. I will provide images I'm allowed to use. Do not download or embed third-party images without a confirmed compatible license.

### 12. Generate the registers

Let the agent create the **glossary, the list of abbreviations, and the list of figures** from the finished content.

> **Prompt**
> Generate a glossary, a list of abbreviations, and a list of figures for "[Vault Name]" from the existing notes. Link glossary terms where they first appear.

### 13. Final review

Do a **final review** — factual, content, and didactic — ideally **with or by a third person**. A second pair of eyes catches gaps that the author and the AI both miss.

> **Prompt**
> Prepare a review checklist for "[Vault Name]" covering factual accuracy, completeness, and didactic flow, so a reviewer (a person) can work through it module by module.

### 14. Finalize

**Only after the review** mark the files as `final`. Until then they remain `draft`; version them if you track revisions. Then commit.

> **Prompt**
> Mark all main chapter files of Module [N] in "[Vault Name]" as final (status: final) and commit. Leave anything still under review as draft.

### 15. Continuous improvement

A vault is never truly "done". Treat `final` as "ready to use", not "frozen". Over time you will **fix errors**, **adjust or update content** (new developments, clearer explanations, better examples), and **act on feedback** from learners, reviewers, or co-authors. Keep changes small, reasoned, and committed in labeled steps so the history stays reviewable; re-run the editorial and graphics checks for anything you touch, and respect copyright for any newly added material.

> **Prompt**
> Here is feedback on "[Vault Name]": [paste feedback / describe the error]. Propose concrete corrections with a short reason each, then apply them incrementally. Keep the figure captions and conventions intact, and flag anything that needs a factual or didactic re-check.

---

## Existing Steering

Steering files in `.kiro/steering/` encode the repository conventions so the agent stays consistent. Most apply automatically; you can also name one in a prompt to be sure it is honored.

| Steering file | Purpose |
|---------------|---------|
| `product.md` | What open-lectures is and who it is for |
| `structure.md` | Folder/file organization of the repository |
| `tech.md` | Tooling and tech stack |
| `obsidian-markdown.md` | Markdown conventions (wiki-links, callouts, figure captions, assets, frontmatter) |
| `obsidian-lecture-notes.md` | Didactic structure of a lecture note |
| `math-graphics.md` | Color scheme and rules for math PNG graphics |

---

## Existing Skills

Skills in `.kiro/skills/` package repeatable workflows. Ask Kiro to "load the [name] skill" or describe a matching task.

| Skill | Use it to … |
|-------|-------------|
| `vault-creator` | Scaffold a complete new vault (dirs, indexes, templates, config) |
| `lecture-writer` | Write structured academic lecture notes |
| `lecture-processor` | Clean up raw/imported notes into the house format |
| `exercise-generator` | Produce practice exercises and sample exams with solutions |
| `create-png` | Produce theme-safe PNG illustrations (color + grayscale pair) |
| `markdown-validator` | Audit notes against the steering conventions |
| `source-extractor` | Extract and organize source material |

## Hooks

Automations in `.kiro/hooks/` run on events — no manual action required:

| Hook | Trigger | Effect |
|------|---------|--------|
| `update-modified-date.json` | On file save | Sets the frontmatter `modified` field to today |
| `sync-english-docs.json` | On doc change | Keeps English/German docs in sync |
| `date-awareness.json` | Session start | Injects the current date into context |

---

## Adding Your Own Steering

Use steering to add rules that should apply across interactions — a house style, a naming rule, a domain convention.

1. Create a Markdown file in `.kiro/steering/`, e.g. `my-conventions.md`.
2. Choose an inclusion mode via frontmatter:
   - **Always** (default): no frontmatter needed; applied to every request.
   - **File-matched**: `inclusion: fileMatch` + `fileMatchPattern: 'README*'`.
   - **Manual**: `inclusion: manual` — you pull it in with `#` in chat.
   - **Auto (on demand)**: `inclusion: auto` + `name` + `description` — activated when the request matches the description.
3. Write the rules as clear, imperative bullet points.
4. Optionally embed other files with `#[[file:relative/path]]` to give the agent extra context (e.g. a spec).

```yaml
---
inclusion: auto
name: my-conventions
description: House rules for naming and tone in my vaults
---
```

---

## Adding Your Own Skill

Use a skill to package a repeatable workflow with its own instructions.

1. Create a directory in `.kiro/skills/`, e.g. `.kiro/skills/my-skill/`.
2. Add a `SKILL.md` with frontmatter describing name and purpose:

```yaml
---
name: my-skill
description: One sentence on what it does and when to use it. The agent reads this to decide when to apply the skill.
---
```

3. In the body, describe the required inputs, the output contract, and a step-by-step workflow. Keep instructions explicit — the agent follows them literally.
4. Optionally add helper scripts or reference files in the skill directory and point to them from `SKILL.md`.
5. Invoke it by asking Kiro to "load the my-skill skill" or by describing a matching task.

> Tip: Model your skill on an existing one (e.g. `create-png/SKILL.md`) to match structure and tone.

---

## Good Practices

- **Think before you generate.** Scope, depth, and syllabus (steps 1–3) decide the quality of everything downstream.
- **Work module by module.** Write → check → tune → review → finalize, one module at a time.
- **Correct incrementally.** Ask for reasoning and apply fixes in small groups, not all at once.
- **Keep graphics theme-safe and correct.** Color + grayscale variant, no pure black/white, and verify the depiction is factually right.
- **Respect copyright at every step** — text, curricula, images, exercises.
- **Stay draft until the final review passes.** Only then switch to `final`.
- **Commit in small, labeled steps** so work stays reviewable and reversible.
