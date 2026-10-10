---
author: Kiro (automated)
created: 2026-10-09
modified: 2026-10-09
tags:
  - meta
  - compliance
  - report
---

# Vault Compliance Report

**Generated:** 2026-10-09 19:30:06  
**Vault:** Betriebssysteme, Rechnernetze und verteilte Systeme

---

## Summary

| Metric | Value |
|--------|-------|
| Total markdown files | 283 |
| Steering compliance | 90% |
| Valid links | 177 (49%) |
| Broken links | 185 (51%) |

---

## Part 1: Steering Compliance

### ✅ Compliant (17 items)

| Rule | Status | Details |
|------|--------|---------|
| Directory structure | ✅ | `00-Organisation/`, `02-07/` topic folders |
| Hidden folders | ✅ | `.assets/`, `.templates/`, `.obsidian/` |
| Numeric prefix on directories | ✅ | All main folders prefixed |
| Numeric prefix on files | ✅ | Content files use `NN-Name.md` |
| H1 title in documents | ✅ | Present in all content files |
| `author` field | ✅ | 286/286 files (100%) |
| `created` date | ✅ | All files have created date |
| `modified` date | ✅ | All files have modified date |
| Tags in frontmatter | ✅ | All files have tags |
| Standard tags | ✅ | `content`, `organisation` etc. added |
| Individual tags preserved | ✅ | `bs`, `rn`, `vs` etc. kept |
| Glossar.md location | ✅ | In vault root |
| Abkuerzungsverzeichnis.md location | ✅ | In vault root |
| Templates hidden | ✅ | `.templates/` |
| Assets hidden | ✅ | `.assets/` at vault root and per-chapter |
| Per-chapter assets | ✅ | `![[./.assets/...]]` relative paths |
| Supplementary folder prefixes | ✅ | Optional per steering |

### ⚠️ Partial Compliance (4 items)

| Rule | Expected | Actual | Compliance |
|------|----------|--------|------------|
| Überblick section | All content files | 146/283 (52%) | 🟡 Partial |
| Lernziele callout | All content files | 19/283 (7%) | 🟡 Low |
| Zusammenhänge section | All content files | 60/283 (21%) | 🟡 Partial |
| Quellen section | All content files | 105/283 (37%) | 🟡 Partial |

---

## Part 2: Link Consistency

### Statistics

| Category | Count | Percentage |
|----------|-------|------------|
| Total unique links | 362 | 100% |
| Valid links | 177 | 49% |
| Broken links | 185 | 51% |

### Broken Links by Category

| Category | Count | Description | Action |
|----------|-------|-------------|--------|
| Asset references | 79 | Links to `.assets/*.png/jpg` | Assets not yet created |
| Folder links | 14 | Links to folders without index file | Create index files |
| Concept links | 13 | `[[DNS]]`, `[[HTTP]]`, etc. | Create alias files or use full paths |
| RFC/IEEE references | 12 | `[[RFC xxxx]]`, `[[IEEE xxx]]` | Create reference stubs |
| Template placeholders | 9 | `[[bild.png]]`, `[[Verwandtes-Konzept]]` | Expected (template content) |
| Legacy link | 1 | `[[Abkuerzungsverzeichnis]]` | Should be `[[Abkuerzungsverzeichnis]]` |
| Other | 57 | Various short-name links | Review individually |

### Sample Broken Links

**Asset links (files not created yet):**
- `[[.assets/zuse-z3-deutsches-museum.jpg]]`
- `[[.assets/eniac.jpg]]`
- `[[.assets/von-neumann-detail.png]]`

**Folder links (need index files):**
- `[[01-Grundlagen]]`
- `[[02-Referenzmodelle]]`
- `[[03-Physikalische-Schicht]]`

**Concept links (need aliases):**
- `[[DNS]]`, `[[HTTP]]`, `[[TCP]]`
- `[[OSI-Modell]]`, `[[Routing]]`

---

## Part 3: Remaining Open Items

| # | Item | Count | Priority | Status |
|---|------|-------|----------|--------|
| 1 | Asset files not created | 79 | 🟡 Medium | Content needed |
| 2 | Lernziele callout missing | 264 files | 🟡 Medium | Add to content files |
| 3 | Folder index files | 14 folders | 🟡 Medium | Create index.md files |
| 4 | Concept alias files | 13 | 🟢 Low | Optional |
| 5 | RFC/IEEE stubs | 12 | 🟢 Low | Optional |
| 6 | Legacy Abkuerzungen link | 1 | 🟢 Low | Fix link |
| 7 | Zusammenhänge section | 223 files | 🟢 Low | Add to content |
| 8 | Quellen section | 178 files | 🟢 Low | Add to content |

---

## Part 4: Vault Structure

```
Betriebssysteme, Rechnernetze und verteilte Systeme/
├── .assets/                    ✅ Hidden
│   ├── diagrams/
│   ├── icons/
│   ├── images/
│   └── screenshots/
├── .obsidian/                  ✅ Hidden
├── .templates/                 ✅ Hidden
├── 00-Organisation/            ✅ Merged (was 00-Meta + 01-Orga)
│   ├── 00-Organisation-Index.md
│   ├── 01-Kursueberblick.md
│   ├── 02-Bewertung.md
│   ├── 03-Zeitplan.md
│   ├── 04-Kontakt.md
│   ├── 05-FAQ.md
│   ├── 06-Voraussetzungen.md
│   └── 07-Fachliteratur.md
├── 02-Betriebssysteme/         ✅ (49 files)
├── 03-Rechnernetze/            ✅ (24 files)
├── 04-Verteilte-Systeme/       ✅ (13 files)
├── 05-Praesentationen/         ✅ (prefix optional)
├── 06-Aufgaben/                ✅ (prefix optional)
├── 07-Anhang/                  ✅ (prefix optional)
├── Glossar.md                  ✅ In root
├── Abkuerzungsverzeichnis.md   ✅ In root
└── Start.md
```

---

## Recommendations

### High Priority
1. **Create missing asset files** or remove references
2. **Add Lernziele callouts** to content files using template

### Medium Priority
3. **Create index files** for RN/VS subfolders
4. **Add Zusammenhänge sections** with crosslinks
5. **Add Quellen sections** with references

### Low Priority
6. **Create concept aliases** (optional, for convenience)
7. **Create RFC/IEEE stubs** (optional)

---

## Change Log

| Date | Changes |
|------|---------|
| 2026-10-09 18:56 | Initial compliance check |
| 2026-10-09 18:52 | Merged 00-Meta + 01-Orga → 00-Organisation |
| 2026-10-09 18:52 | Hidden assets/ → .assets/, templates/ → .templates/ |
| 2026-10-09 18:52 | Fixed Betriebssysteme article paths |
| 2026-10-09 18:45 | Added author field to all files |
| 2026-10-09 18:45 | Added standard tags (content, organisation, etc.) |
| 2026-10-09 18:45 | Moved Glossar.md and Abkuerzungsverzeichnis.md to root |
