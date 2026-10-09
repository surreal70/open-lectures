---
inclusion: auto
name: Repository Structure
description: Guidelines for the open-lectures repository structure and vault organization
---

# Repository Structure Guidelines

This document describes the structure of the `open-lectures` repository.

## Top-Level Repository Structure

```
open-lectures/
├── README.md                  # Repository description and overview
├── LICENSE                    # Licensing information
├── CONTRIBUTING.md            # Contribution guidelines (optional)
├── .gitignore                 # Git ignore patterns
├── .kiro/                     # Kiro configuration and steering
│   └── steering/              # Steering files
├── vault-1/                   # Independent Obsidian vault
├── vault-2/                   # Independent Obsidian vault
├── vault-n/                   # Additional vaults...
└── tmp/                       # Temporary files (gitignored)
```

## Vault Independence

Each vault is a **self-contained, independent Obsidian vault**:

- Vaults do not share files or cross-reference each other
- Each vault has its own `.obsidian/` configuration (if present)
- Vaults can be opened individually in Obsidian
- Vaults follow the structure defined in `obsidian-lecture-notes.md`

## Vault Naming Convention

Vault directories should use lowercase with hyphens:
- `algorithmen-datenstrukturen/`
- `lineare-algebra/`
- `softwaretechnik/`

## Content Status Table

The following table tracks all lecture vaults in this repository. **Update this table whenever a vault is added, modified, or reaches a new status.**

| Vault | Description | Author | Status |
|-------|-------------|--------|--------|
| `tmp/example-vault` | Example vault for steering verification | Kiro | in-development |

### Status Values

| Status | Meaning |
|--------|---------|
| `in-development` | Actively being created, not ready for use |
| `draft` | Initial content complete, under review |
| `v1.0`, `v1.1`, ... | Released version, ready for use |
| `archived` | No longer maintained |

## Maintenance Tasks

### Adding a New Vault

1. Create directory with appropriate name
2. Set up vault structure per `obsidian-lecture-notes.md`
3. Add entry to Content Status Table above
4. Update README.md if needed

### Updating the Content Status Table

Update the table when:
- A new vault is created
- A vault reaches a milestone (draft → v1.0)
- Content is significantly updated
- A vault is archived

### Regular Maintenance

On a regular basis (or on demand):
1. Review all vaults for status accuracy
2. Update `modified` dates in changed files
3. Ensure Content Status Table reflects current state
