# .kiro - AI Agent Configuration

Dieses Verzeichnis enthält Konfigurationen und Tools für die Arbeit mit AI-Agenten wie [Kiro](https://kiro.dev).

## ⚠️ Hinweis zu externen Inhalten

Die hier bereitgestellten Skills ermöglichen die Extraktion und Verarbeitung externer Dokumente (PDFs, Word, etc.). **Bitte beachten Sie:**

- ✅ **Erlaubt:** Eigene Notizen, CC-lizenzierte Inhalte, Public Domain, Materialien mit Genehmigung
- ❌ **Nicht erlaubt:** Urheberrechtlich geschützte Werke ohne Genehmigung

Inhalte, die Sie in dieses Repository einfügen, müssen mit der **CC-BY-NC 4.0 Lizenz** kompatibel sein. Im Zweifel: Quellen prüfen, Erlaubnis einholen, oder nicht verwenden.

## Für wen ist das relevant?

- **Obsidian-Nutzer**: Sie können dieses Verzeichnis komplett ignorieren. Die Vaults funktionieren ohne AI-Unterstützung.
- **Contributor mit AI-Unterstützung**: Hier finden Sie Skills und Steering-Dateien, die die Arbeit mit Kiro vereinfachen.

## Verzeichnisstruktur

```
.kiro/
├── README.md           # Diese Datei
├── requirements.txt    # Python-Dependencies für AI-Tools
├── settings/           # Kiro-Einstellungen
├── skills/             # Wiederverwendbare AI-Workflows
│   ├── create-png/           # PNG-Grafiken erstellen
│   ├── exercise-generator/   # Übungsaufgaben generieren
│   ├── lecture-processor/    # Rohe Notizen formatieren
│   ├── lecture-writer/       # Neue Vorlesungen schreiben
│   ├── markdown-validator/   # Markdown-Konventionen prüfen
│   ├── source-extractor/     # Text aus PDFs/Docs extrahieren
│   └── vault-creator/        # Neue Vaults scaffolden
└── steering/           # Kontext-Dateien für AI-Verhalten
    ├── obsidian-lecture-notes.md  # Vorlesungsnotiz-Konventionen
    ├── obsidian-markdown.md       # Markdown-Regeln
    ├── structure.md               # Repo-Struktur
    └── tech.md                    # Tech-Stack
```

## Setup für AI-gestützte Arbeit

### 1. System-Tools installieren

```bash
# Debian/Ubuntu
sudo apt install poppler-utils pandoc tesseract-ocr

# macOS (Homebrew)
brew install poppler pandoc tesseract

# Windows (Chocolatey)
choco install poppler pandoc tesseract
```

### 2. Python-Dependencies installieren (optional)

Falls Sie Python-basierte Extraktion oder Bildverarbeitung nutzen:

```bash
# Mit virtuellem Environment (empfohlen)
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
pip install -r .kiro/requirements.txt
```

### 3. Kiro starten

Öffnen Sie das Repository in Kiro. Die Skills und Steering-Dateien werden automatisch erkannt.

## Skills verwenden

In Kiro können Sie Skills mit `#skill-name` aktivieren:

| Skill | Zweck | Aktivierung |
|-------|-------|-------------|
| **lecture-writer** | Neue Vorlesungsnotiz erstellen | `#lecture-writer` |
| **lecture-processor** | Rohe Notizen formatieren | `#lecture-processor` |
| **source-extractor** | Text aus PDFs extrahieren | `#source-extractor` |
| **exercise-generator** | Übungsaufgaben erstellen | `#exercise-generator` |
| **markdown-validator** | Konventionen prüfen | `#markdown-validator` |
| **create-png** | Diagramme als PNG | `#create-png` |
| **vault-creator** | Neuen Vault anlegen | `#vault-creator` |

## Beispiel-Workflow

```
User: #source-extractor Extrahiere input-betriebssysteme/lecture-01.pdf

Agent: [Extrahiert Text aus PDF]

User: #lecture-processor Formatiere das als Vorlesungsnotiz

Agent: [Erstellt strukturierte Markdown-Datei]
```

## Ohne AI arbeiten

Dieses Repository ist vollständig ohne AI-Unterstützung nutzbar:

1. Öffnen Sie einen Vault (z.B. `L-Betriebssysteme, Rechnernetze und verteilte Systeme/`) in Obsidian
2. Nutzen Sie die Templates in `.templates/` für neue Notizen
3. Folgen Sie den Konventionen in `HOWTO.de.md`

Die `.kiro/`-Verzeichnisse können Sie in Obsidian über Einstellungen → Dateien & Links → Ausgeschlossene Dateien ausblenden.
