# So nutzt du dieses Repository

Diese Anleitung erklärt, wie du die Vorlesungsunterlagen in diesem Repository mit Obsidian verwendest.

## Was ist Obsidian?

Obsidian ist eine leistungsstarke Wissensdatenbank-Anwendung, die auf lokalen Markdown-Dateien arbeitet. Sie ist ideal zum Lernen, weil du:

- Konzepte miteinander verknüpfen kannst
- Zusammenhänge zwischen Themen visualisieren kannst
- Über alle Notizen hinweg suchen kannst
- Offline mit deinen eigenen Dateien arbeiten kannst

---

## Obsidian installieren

### Download

Obsidian ist für alle gängigen Plattformen verfügbar:

| Plattform | Download |
|-----------|----------|
| Windows | [obsidian.md/download](https://obsidian.md/download) |
| macOS | [obsidian.md/download](https://obsidian.md/download) |
| Linux | [obsidian.md/download](https://obsidian.md/download) (AppImage, Snap, Flatpak) |
| iOS | App Store |
| Android | Google Play Store |

Obsidian ist **kostenlos für den persönlichen Gebrauch**.

### Installation

1. Lade das Installationsprogramm für deine Plattform herunter
2. Führe die Installation aus
3. Starte Obsidian

---

## Repository beziehen und Vault öffnen

### Option 1: Mit Git (empfohlen für Updates)

```bash
# Repository klonen
git clone https://github.com/surreal70/open-lectures.git

# Später: Aktualisierungen holen
cd open-lectures
git pull
```

### Option 2: Als ZIP herunterladen

1. Gehe zur Repository-Seite auf GitHub
2. Klicke auf "Code" → "Download ZIP"
3. Entpacke das ZIP in einen Ordner deiner Wahl

### Vault in Obsidian öffnen

1. Starte Obsidian
2. Klicke auf "Ordner als Vault öffnen" ("Open folder as vault")
3. Navigiere zum Vorlesungsverzeichnis, z.B.:
   ```
   open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/
   ```
4. Wähle den Ordner aus und klicke auf "Öffnen"

> [!tip] **Hinweis**
> Jedes Vorlesungsverzeichnis ist ein eigenständiger Vault – öffne sie separat.

---

## Kurzreferenz: Obsidian-Shortcuts

### Navigation

| Aktion | Tastenkürzel |
|--------|--------------|
| Schnellwechsler (Datei finden) | `Strg/Cmd + O` |
| In allen Dateien suchen | `Strg/Cmd + Umschalt + F` |
| Linke Seitenleiste umschalten | `Strg/Cmd + /` |
| Graph-Ansicht öffnen | `Strg/Cmd + G` |
| Zurück | `Strg/Cmd + Alt + ←` |
| Vorwärts | `Strg/Cmd + Alt + →` |

### Bearbeiten

| Aktion | Tastenkürzel |
|--------|--------------|
| Fett | `Strg/Cmd + B` |
| Kursiv | `Strg/Cmd + I` |
| Interner Link | `[[` tippen |
| Bearbeiten/Vorschau umschalten | `Strg/Cmd + E` |

---

## Navigation durch die Unterlagen

### Struktur verstehen

Die Vaults sind hierarchisch aufgebaut:

```
L-Betriebssysteme, Rechnernetze und verteilte Systeme/
├── 00-Startseite.md              ← Einstiegspunkt
├── 02-Betriebssysteme/
│   ├── 00-Betriebssysteme-Index.md
│   ├── 01-Einfuehrung/
│   │   ├── 01-Historie.md
│   │   ├── 02-Definition.md
│   │   └── ...
│   ├── 02-Architektur/
│   ├── 03-Prozesse/
│   └── ...
├── 03-Rechnernetze/
└── 04-Verteilte-Systeme/
```

### Links folgen

- **Klicke** auf einen `[[Link]]`, um ihn zu öffnen
- **Strg/Cmd + Klick**, um in neuem Tab zu öffnen
- **Hover** über einen Link für eine Vorschau

### Graph-Ansicht nutzen

1. Drücke `Strg/Cmd + G` oder klicke auf das Graph-Symbol
2. Sieh alle Notizen und ihre Verbindungen
3. Klicke auf einen Knoten, um zur Notiz zu navigieren
4. Nutze Filter, um bestimmte Tags oder Ordner zu fokussieren

---

## Effektiv lernen mit diesem Vault

### 1. Prüfungsrelevante Inhalte finden

Suche nach Callout-Boxen mit Prüfungshinweisen:

```
> [!warning] **Prüfungsrelevant**
```

Nutze die globale Suche (`Strg/Cmd + Umschalt + F`) und suche nach:
- `[!warning]` – Prüfungsrelevante Markierungen
- `[!question]` – Häufige Prüfungsfragen
- `[!tip]` – Merkhilfen

### 2. Querverweise nutzen

Jede Notiz hat einen Abschnitt "Zusammenhänge" mit Links zu verwandten Themen. Folge diesen Links, um das Gesamtbild zu verstehen.

### 3. Abbildungsverzeichnis nutzen

Für eine Übersicht aller Diagramme und Abbildungen:
```
Abbildungsverzeichnis.md
```

### 4. Tags zur Navigation verwenden

Klicke auf Tags wie `#bs` oder `#prüfungsrelevant`, um alle Notizen mit diesem Tag zu sehen.

---

## Callout-Typen verstehen

Die Unterlagen verwenden verschiedene Callout-Boxen:

| Callout | Bedeutung |
|---------|-----------|
| `[!info] **Lernziele**` | Was du nach diesem Kapitel können solltest |
| `[!quote]` | Formale Definitionen |
| `[!warning] **Prüfungsrelevant**` | Besonders wichtig für Prüfungen |
| `[!question]` | Häufige Prüfungsfragen |
| `[!tip]` | Merkhilfen und Eselsbrücken |
| `[!info] **Nicht prüfungsrelevant**` | Hintergrundwissen, nicht klausurrelevant |
| `[!note] **Videos**` | Weiterführende Video-Ressourcen |

---

## Problemlösung

### Notizen werden nicht korrekt dargestellt

- Stelle sicher, dass du in der "Leseansicht" bist (`Strg/Cmd + E`)
- Prüfe, ob der `.obsidian`-Ordner im Vault existiert

### Links funktionieren nicht

- Interne Links verwenden `[[Notizname]]`-Syntax
- Externe Links verwenden `[Text](URL)`-Syntax

### Bilder werden nicht angezeigt

- Bilder befinden sich im `assets/`-Ordner des jeweiligen Kapitels
- Verwende nur den Dateinamen: `![[bild.png]]`
- Bei Problemen: Obsidian neu starten (`Strg/Cmd + R`)

### Mathe-Formeln werden nicht angezeigt

- LaTeX-Rendering ist eingebaut
- Inline-Mathe mit einfachem `$`: `$x^2$`
- Block-Mathe mit doppeltem `$$`

---

## CSS-Snippets (Darstellung anpassen)

Einige Vaults enthalten **CSS-Snippets**, die die Darstellung verbessern – etwa die Breite von Abbildungen begrenzen oder Bildunterschriften formatieren. Snippets liegen im Vault unter `.obsidian/snippets/` und müssen **einmalig aktiviert** werden.

### Snippet aktivieren

1. Einstellungen → **Erscheinungsbild**
2. Abschnitt **CSS-Snippets** nach unten scrollen
3. Auf das **Neu-laden-Symbol** klicken, damit vorhandene Snippets erscheinen
4. Das gewünschte Snippet per Schalter **einschalten**

### Snippet `lecture-figures`

Dieses Snippet (sofern im Vault vorhanden) bewirkt:

- **Abbildungen** werden auf **75 % der Inhaltsbreite** begrenzt und zentriert – so passen Grafiken proportional zum Text und nehmen nicht die volle Seitenbreite ein.
- **Figur-Identifier** (`<span class="fig-id">…</span>` unter Abbildungen) werden blau und fett dargestellt.

> [!note] **Figur-Identifier und Bildunterschriften**
> Abbildungen werden mit einer Bildunterschrift und einem eindeutigen Identifier versehen, z. B.:
> ```markdown
> ![[zahlenstrahl-natuerliche.png]]
> *<span class="fig-id">01-01-03-zahlenstrahl-natuerliche</span>: Zahlenstrahl der natürlichen Zahlen.*
> ```
> Der Identifier (`<topic>-<kapitel>-<datei>-<bildname>`) ist vault-weit eindeutig. Ohne aktiviertes Snippet wird er einfach als normaler Text angezeigt.

> [!tip] **Eigene Breite pro Bild**
> Unabhängig vom Snippet kann die Anzeigebreite einzelner Bilder direkt im Link gesetzt werden: `![[bild.png|600]]` (Breite in Pixel). Das Snippet wirkt vault-weit, die Pixelangabe nur für das jeweilige Bild.

---

## Empfohlene Plugins (optional)

Diese Community-Plugins verbessern das Lernerlebnis:

| Plugin | Zweck |
|--------|-------|
| **Dataview** | Notizen abfragen und filtern |
| **Spaced Repetition** | Karteikarten-Wiederholung |
| **Excalidraw** | Eigene Diagramme erstellen |
| **Calendar** | Notizen nach Datum navigieren |

Installation: Einstellungen → Community-Plugins → Durchsuchen

---

## Updates erhalten

Wenn du das Repository mit Git geklont hast:

```bash
cd open-lectures
git pull
```

> [!warning] **Achtung bei lokalen Änderungen**
> Wenn du eigene Notizen hinzugefügt hast, sichere sie vor dem Pull oder nutze Git-Branching.

---

## Weitere Ressourcen

- [Obsidian Hilfe (englisch)](https://help.obsidian.md/)
- [Obsidian Forum](https://forum.obsidian.md/)
- [Obsidian Discord](https://discord.gg/obsidianmd)
- [Obsidian auf YouTube](https://www.youtube.com/results?search_query=obsidian+tutorial+deutsch)
