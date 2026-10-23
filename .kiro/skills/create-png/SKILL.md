---
name: create-png
description: Create or revise PNG illustrations and technical diagrams for Open Lectures and Obsidian notes. Use when the user requests a PNG graphic, diagram, illustration, or an existing image to be exported as PNG. Enforce transparent backgrounds, legibility in dark and light themes, clipping-safe margins, interactive user approval of previews before applying, and paired color/grayscale outputs with the _g suffix.
---

# Create PNG — Open Lectures

Produce educational PNG illustrations that remain legible in both light and dark Obsidian themes. The approval gate below is mandatory; never treat a draft preview as permission to apply it.

## Required output contract

- Produce **two files** from the same approved illustration, with matching dimensions and content:
  - `<name>.png`: color version.
  - `<name>_g.png`: grayscale version; `_g` is inserted **before** `.png`.
- Export both as RGBA PNG with genuinely transparent backgrounds (alpha = 0 in unused areas). Never flatten transparency onto white, black, or checkerboard.
- Keep every visual element, including text, arrows, shadows, and strokes, completely inside the image canvas. Use a deliberate safety margin around the artwork; default to at least 5% of the shorter canvas dimension, unless the user requests edge-to-edge artwork. Do not clip or crop elements.
- Make both variants legible against **white/light and near-black/dark** backgrounds. Never use pure black (`#000000`) or pure white (`#FFFFFF`) for any visible illustration element (including strokes, fills, text, or icons). Prefer neutral grays or colors with sufficient contrast against **both** light and dark backgrounds. Avoid low-opacity features or relying on hue alone for semantic meaning; use clear shapes, labels, and redundant visual cues (symbols and line styles).
- Preserve the drawing's meaning in grayscale; do not merely desaturate away distinctions encoded only by color.
- Use descriptive, stable, lowercase, hyphenated filenames unless project conventions specify otherwise.
- Place final outputs in the relevant lecture chapter's `assets/` directory, following repository steering rules. If no target location is given, ask or use a working output directory pending approval; do not invent a vault path.

## Mandatory workflow

1. **Gather requirements:** Determine the illustration's subject, intended context, labels, aspect ratio/size, preferred output name, and destination when available. Use reasonable defaults for nonessential design choices.
2. **Prepare draft:** Draw or render the illustration on an RGBA transparent canvas. Prefer a reproducible vector source or high-resolution source where practical. Check text legibility and clear spatial hierarchy. Allow enough padding so labels, connectors, arrowheads, and effects do not touch the edges.
3. **Generate BOTH variants:** Create `<name>.png` and `<name>_g.png` with identical geometry. If using the bundled script, run `python scripts/prepare_png.py <draft-color.png> --outdir <draft-folder> --stem <name>`; it creates the color and grayscale PNGs and a preview sheet.
4. **Quality check:** Run the helper script (or equivalent checks) and review both variants on light and dark backgrounds. Verify real alpha transparency, identical dimensions, sufficient padding/no clipped edges, correct `_g` filename, no visible pure-black/pure-white pixels, readable contrast on both themes, and meaningful grayscale distinctions. Repair and re-run as needed. Automated edge checks are a safeguard, **not** proof that the original drawing was never clipped; inspect the source/render visually too.
5. **Show previews and STOP:** Display the actual previews to the user, including color and grayscale variants on both light and dark backgrounds. Briefly note any issues. Explicitly ask: **"Apply as is, or would you like modifications?"** Do not skip this question, and do not assume approval from silence.
6. **If modifications requested:** Revise the source, regenerate **both** variants, revalidate, show the updated previews, and ask again. Repeat until explicit approval.
7. **Only after explicit approval:** Copy/save the approved color and grayscale PNGs to the final destination; report both filenames and optionally embed the color image in the target Obsidian note only if requested. Do not deliver a preview composite as an illustration asset.

## Preview requirements

- The preview may have temporary opaque backgrounds for inspection; **the final PNGs must remain transparent**.
- Show both original color and grayscale versions on a light and a dark background, ideally as a labeled 2×2 contact sheet.
- Use `scripts/prepare_png.py` to generate a contact sheet (`<name>_preview.png`) when Pillow is available; otherwise prepare equivalent images with available tools.
- Put preview artifacts in a temporary/staging location. Do **not** add previews to the final Obsidian `assets/` folder unless specifically requested.

## Working directory for drafts

- **Always use `/tmp/open-lectures-drafts/` as the working directory** for Python scripts, draft PNGs, previews, and intermediate files.
- Create the directory if it doesn't exist: `mkdir -p /tmp/open-lectures-drafts/`
- Never store drafts or working files inside `.kiro/` or the workspace — these are temporary artifacts that should not be versioned or persist across sessions.
- Only the final approved PNGs get copied to the chapter's `assets/` directory.

## Failure behavior

- If the environment cannot generate or preview images, state exactly what is blocked and do not claim the files passed validation.
- If transparency, padding, or theme contrast is inadequate, correct the artwork before requesting approval.
- Do not place a PNG in the final notes, commit it to a repository, or overwrite existing assets until the user has approved the preview and any overwrite.
