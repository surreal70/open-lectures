#!/usr/bin/env python3
"""
Generates Pruefungsrelevanz.md by scanning all lecture markdown files
for exam relevance callouts and questions.

Usage:
    python3 generate_pruefungsrelevanz.py

Output:
    Overwrites Pruefungsrelevanz.md in the vault root with current status.
"""

import os
import re
from pathlib import Path
from collections import defaultdict

VAULT_PATH = "/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme"

# Only scan these content directories
CONTENT_DIRS = ['02-Betriebssysteme', '03-Rechnernetze', '04-Verteilte-Systeme']

def analyze_file(filepath):
    """
    Analyze a markdown file for exam relevance info.
    Returns dict with:
      - has_callout: bool - does the file have a Prüfungsrelevant callout?
      - is_relevant: bool/None - True if relevant, False if N/A, None if no callout
      - has_questions: bool - does the file have exam questions?
    """
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception:
        return None
    
    result = {
        'has_callout': False,
        'is_relevant': None,
        'has_questions': False
    }
    
    # Check for Prüfungsrelevant callout
    # Pattern: > [!warning] Prüfungsrelevant or > [!warning] **Prüfungsrelevant** (case insensitive)
    callout_match = re.search(r'>\s*\[!warning\]\s*\*{0,2}Prüfungsrelevant\*{0,2}', content, re.IGNORECASE)
    
    if callout_match:
        result['has_callout'] = True
        
        # Get the content after the callout to check if it's N/A
        # Look for the callout block content (lines starting with >)
        pos = callout_match.end()
        remaining = content[pos:pos+500]  # Check next 500 chars
        
        # Extract callout content (lines starting with >)
        callout_lines = []
        for line in remaining.split('\n'):
            if line.strip().startswith('>'):
                callout_lines.append(line)
            elif line.strip() == '':
                continue
            else:
                break
        
        callout_content = '\n'.join(callout_lines)
        
        # Check if content is N/A or empty
        if re.search(r'\bN/?A\b', callout_content, re.IGNORECASE) or not callout_content.strip():
            result['is_relevant'] = False
        else:
            result['is_relevant'] = True
    
    # Check for exam questions section
    # Two formats:
    # 1. **Typische Prüfungsfragen:** followed by numbered list
    # 2. > [!question] **Häufige/Typische Prüfungsfragen** as callout
    questions_match = re.search(
        r'(\*{0,2}Typische\s+Prüfungsfragen\s*:?\*{0,2}\s*\n+\s*(\d+\.|-)|>\s*\[!question\]\s*\*{0,2}(Häufige|Typische)\s+Prüfungsfragen\*{0,2})',
        content,
        re.IGNORECASE
    )
    
    if questions_match:
        result['has_questions'] = True
    
    return result

def get_display_name(filepath):
    """Get the display name for a file (without extension, for wiki link)."""
    return filepath.stem

def scan_vault(vault_path):
    """
    Scan the vault and collect exam relevance data.
    Returns dict organized by chapter.
    """
    data = defaultdict(lambda: defaultdict(list))
    
    for content_dir in CONTENT_DIRS:
        dir_path = Path(vault_path) / content_dir
        if not dir_path.exists():
            continue
        
        for root, dirs, files in os.walk(dir_path):
            # Skip hidden directories and assets
            dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'assets']
            
            for filename in files:
                if not filename.endswith('.md'):
                    continue
                
                # Skip index files
                if filename.endswith('-Index.md') or filename == '00-Index.md':
                    continue
                
                filepath = Path(root) / filename
                rel_path = filepath.relative_to(vault_path)
                
                analysis = analyze_file(filepath)
                if analysis is None:
                    continue
                
                # Determine chapter and subchapter from path
                parts = rel_path.parts
                main_chapter = parts[0] if len(parts) > 0 else 'Sonstige'
                
                # Get subchapter if exists
                subchapter = None
                if len(parts) > 2:
                    subchapter = parts[1]
                
                data[main_chapter][subchapter or 'root'].append({
                    'name': get_display_name(filepath),
                    'path': str(rel_path),
                    **analysis
                })
    
    return data

def generate_markdown(data):
    """Generate the Pruefungsrelevanz.md content."""
    
    lines = [
        "---",
        "title: Prüfungsrelevanz Übersicht",
        "created: 2025-01-15",
        "modified: 2026-10-29",
        "---",
        "",
        "# Prüfungsrelevanz Übersicht",
        "",
        "Diese Datei gibt einen Überblick über den Status der Prüfungsrelevanz-Callouts in allen Vorlesungsdateien.",
        "",
        "## Legende",
        "",
        "| Symbol | Bedeutung |",
        "|--------|-----------|",
        "| ✅ | Vorhanden / Prüfungsrelevant |",
        "| ❌ | Nicht vorhanden / Nicht prüfungsrelevant (N/A) |",
        "",
    ]
    
    # Calculate statistics
    total_files = 0
    files_with_callout = 0
    files_relevant = 0
    files_not_relevant = 0
    files_with_questions = 0
    
    for chapter, subchapters in data.items():
        for subchapter, files in subchapters.items():
            for f in files:
                total_files += 1
                if f['has_callout']:
                    files_with_callout += 1
                    if f['is_relevant']:
                        files_relevant += 1
                    else:
                        files_not_relevant += 1
                if f['has_questions']:
                    files_with_questions += 1
    
    lines.extend([
        "## Statistik",
        "",
        f"- **Dateien mit Prüfungsrelevanz-Callout:** {files_with_callout} von {total_files}",
        f"- **Davon prüfungsrelevant:** {files_relevant}",
        f"- **Davon nicht prüfungsrelevant (N/A):** {files_not_relevant}",
        f"- **Dateien mit Prüfungsfragen:** {files_with_questions}",
        "",
        "## Dateien nach Kapitel",
        ""
    ])
    
    # Sort chapters
    chapter_order = ['02-Betriebssysteme', '03-Rechnernetze', '04-Verteilte-Systeme']
    
    for chapter in chapter_order:
        if chapter not in data:
            continue
        
        lines.append(f"\n### {chapter}\n")
        lines.append("| Datei | Callout | Prüfungsrelevant | Fragen |")
        lines.append("|-------|---------|------------------|--------|")
        
        # Sort subchapters
        subchapters = sorted(data[chapter].keys())
        
        for subchapter in subchapters:
            files = data[chapter][subchapter]
            
            # Sort files by name
            files_sorted = sorted(files, key=lambda x: x['name'])
            
            for f in files_sorted:
                name = f['name']
                
                # Callout status
                callout = "✅" if f['has_callout'] else "❌"
                
                # Relevance status
                if f['is_relevant'] is None:
                    relevant = "❌"
                elif f['is_relevant']:
                    relevant = "✅"
                else:
                    relevant = "❌"
                
                # Questions status
                questions = "✅" if f['has_questions'] else "❌"
                
                lines.append(f"| [[{name}]] | {callout} | {relevant} | {questions} |")
    
    return '\n'.join(lines)

def main():
    print(f"Scanning vault: {VAULT_PATH}")
    
    data = scan_vault(VAULT_PATH)
    
    # Count files
    total = sum(len(files) for subchapters in data.values() for files in subchapters.values())
    print(f"Found {total} content files")
    
    content = generate_markdown(data)
    
    output_path = Path(VAULT_PATH) / "Pruefungsrelevanz.md"
    output_path.write_text(content, encoding='utf-8')
    print(f"Written to: {output_path}")

if __name__ == '__main__':
    main()
