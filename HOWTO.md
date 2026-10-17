# How to Use This Repository

This guide explains how to use the lecture materials in this repository with Obsidian.

## What is Obsidian?

Obsidian is a powerful knowledge base application that works on top of local Markdown files. It's ideal for studying because it allows you to:

- Link concepts together
- Visualize connections between topics
- Search across all your notes
- Work offline with your own files

## Getting Obsidian

### Download

Obsidian is available for all major platforms:

| Platform | Download |
|----------|----------|
| Windows | [obsidian.md/download](https://obsidian.md/download) |
| macOS | [obsidian.md/download](https://obsidian.md/download) |
| Linux | [obsidian.md/download](https://obsidian.md/download) (AppImage, Snap, Flatpak) |
| iOS | App Store |
| Android | Google Play Store |

Obsidian is **free for personal use**.

### Installation

1. Download the installer for your platform
2. Run the installer
3. Launch Obsidian

## Opening a Vault from This Repository

1. Clone or download this repository
2. Open Obsidian
3. Click "Open folder as vault"
4. Navigate to a lecture directory (e.g., `algorithmen-datenstrukturen/`)
5. Select the folder and click "Open"

Each lecture directory is an independent vault – open them separately.

---

## Obsidian Quick Reference

### Navigation

| Action | Shortcut |
|--------|----------|
| Quick switcher (find file) | `Ctrl/Cmd + O` |
| Search in all files | `Ctrl/Cmd + Shift + F` |
| Toggle left sidebar | `Ctrl/Cmd + /` |
| Toggle right sidebar | `Ctrl/Cmd + Shift + /` |
| Back | `Ctrl/Cmd + Alt + ←` |
| Forward | `Ctrl/Cmd + Alt + →` |

### Editing

| Action | Shortcut |
|--------|----------|
| Bold | `Ctrl/Cmd + B` |
| Italic | `Ctrl/Cmd + I` |
| Internal link | `[[` |
| Toggle edit/preview | `Ctrl/Cmd + E` |
| Toggle reading view | `Ctrl/Cmd + Shift + E` |

### Links and References

```markdown
[[Note Name]]                    Link to note
[[Note Name|Display Text]]       Link with alias
[[Note Name#Heading]]            Link to heading
![[Note Name]]                   Embed note
![[image.png]]                   Embed image
```

### Callout Boxes

```markdown
> [!info] Title
> Content here

> [!warning] Title
> Content here

> [!tip] Title
> Content here
```

Available types: `note`, `abstract`, `info`, `tip`, `success`, `question`, `warning`, `failure`, `danger`, `bug`, `example`, `quote`

### Code Blocks

````markdown
```python
def hello():
    print("Hello")
```
````

### Math (LaTeX)

```markdown
Inline: $E = mc^2$

Block:
$$
\int_0^\infty e^{-x^2} dx
$$
```

### Tables

```markdown
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
```

### Task Lists

```markdown
- [ ] Unchecked
- [x] Checked
```

---

## Obsidian How-To

### How to Follow Links

- **Click** on a `[[link]]` to open it
- **Ctrl/Cmd + Click** to open in new tab
- **Hover** over a link to preview content

### How to Use the Graph View

1. Click the graph icon in the left sidebar (or `Ctrl/Cmd + G`)
2. See all notes and their connections
3. Click on a node to navigate to that note
4. Use filters to focus on specific tags or folders

### How to Search Effectively

1. Press `Ctrl/Cmd + Shift + F` for global search
2. Use search operators:
   - `tag:#prüfung` – find notes with tag
   - `path:01-Grundlagen` – search in folder
   - `file:Komplexität` – search filenames
   - `"exact phrase"` – exact match

### How to Use Tags

Tags help organize and find content:

```markdown
#prüfungsrelevant
#todo/review
#concept/algorithmus
```

Click on any tag to see all notes with that tag.

### How to Customize Your View

1. **Themes**: Settings → Appearance → Themes
2. **Font size**: Settings → Appearance → Font size
3. **Dark/Light mode**: Settings → Appearance → Base color scheme

### How to Export Notes

- **PDF**: Right-click note → Export to PDF
- **Markdown**: Notes are already Markdown files – copy them anywhere

### Recommended Plugins (Optional)

These community plugins enhance the study experience:

| Plugin | Purpose |
|--------|---------|
| Calendar | Navigate notes by date |
| Dataview | Query and filter notes |
| Excalidraw | Create diagrams |
| Spaced Repetition | Flashcard review |

To install: Settings → Community plugins → Browse

---

## Tips for Studying

1. **Use the Graph View** to understand topic relationships
2. **Search for `[!warning]`** to find exam-relevant content
3. **Follow crosslinks** in the "Zusammenhänge" section
4. **Check "Typische Prüfungsfragen"** for exam preparation
5. **Use tags** to filter content (e.g., `#prüfungsrelevant`)

## Troubleshooting

### Notes don't render correctly

- Make sure you're in "Reading view" (`Ctrl/Cmd + E`)
- Check if the `.obsidian` folder exists in the vault

### Links are broken

- Internal links use `[[Note Name]]` syntax
- External links use `[text](url)` syntax

### Images don't display

Obsidian has inconsistent behavior with hidden directories (folders starting with `.`):

- **Problem**: Images in hidden folders like `.assets/` may not display correctly, even though Obsidian claims to index them
- **Solution**: Use visible `assets/` folders for chapter-level images
- **Reference**: Use filename only: `![[image.png]]` – Obsidian finds the file via "shortest path" matching
- **Avoid**: Full paths like `![[folder/.assets/image.png]]` can cause issues

If images suddenly stop working after moving files, try:
1. Reload Obsidian (`Ctrl/Cmd + R` or restart)
2. Check that the image file actually exists in the `assets/` folder
3. Ensure the filename in the link matches exactly (case-sensitive on some systems)

### Math doesn't display

- LaTeX rendering is built-in
- Inline math uses single `$`: `$x^2$`
- Block math uses double `$$`

---

## CSS Snippets (Customising Appearance)

Some vaults ship **CSS snippets** that improve presentation — for example constraining figure width or styling figure captions. Snippets live in the vault under `.obsidian/snippets/` and must be **enabled once**.

### Enabling a snippet

1. Settings → **Appearance**
2. Scroll down to the **CSS snippets** section
3. Click the **reload icon** so existing snippets appear
4. Toggle the desired snippet **on**

### The `lecture-figures` snippet

Where present, this snippet does the following:

- **Figures** are constrained to **75% of the content width** and centered, so graphics stay proportional to the text instead of filling the whole page width.
- **Figure identifiers** (`<span class="fig-id">…</span>` below figures) are shown in bold blue.

> [!note] **Figure identifiers and captions**
> Figures are given a caption and a unique identifier, e.g.:
> ```markdown
> ![[zahlenstrahl-natuerliche.png]]
> *<span class="fig-id">01-01-03-zahlenstrahl-natuerliche</span>: Number line of the natural numbers.*
> ```
> The identifier (`<topic>-<chapter>-<file>-<image-name>`) is unique across the vault. Without the snippet enabled, it simply renders as plain text.

> [!tip] **Per-image width**
> Independent of the snippet, the display width of a single image can be set directly in the link: `![[image.png|600]]` (width in pixels). The snippet applies vault-wide; the pixel value applies only to that one image.

---

## Further Resources

- [Obsidian Help](https://help.obsidian.md/)
- [Obsidian Forum](https://forum.obsidian.md/)
- [Obsidian Discord](https://discord.gg/obsidianmd)
