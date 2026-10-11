#!/usr/bin/env python3
"""
Diagram: Synchronisation Overview - Flow from concurrency to problems/solutions
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Colors (theme-agnostic)
box_fill = '#3182CE'
box_fill_dark = '#2C5282'
box_fill_success = '#38A169'
text_color = '#A0AEC0'
arrow_color = '#A0AEC0'

fig, ax = plt.subplots(1, 1, figsize=(10, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 12)
ax.set_aspect('equal')
ax.axis('off')
fig.patch.set_alpha(0)
ax.set_facecolor('none')

def draw_box(ax, x, y, width, height, text, color=box_fill, fontsize=11, multiline=False):
    box = FancyBboxPatch((x - width/2, y - height/2), width, height,
                         boxstyle="round,pad=0.02,rounding_size=0.15",
                         facecolor=color, edgecolor=text_color, linewidth=1.5)
    ax.add_patch(box)
    if multiline:
        ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
                color='white', fontweight='bold', linespacing=1.4)
    else:
        ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
                color='white', fontweight='bold')
    return box

def draw_arrow(ax, start, end, color=arrow_color):
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', color=color, lw=2,
                               connectionstyle='arc3,rad=0'))

# Title
ax.text(5, 11.5, 'Synchronisation – Überblick', ha='center', va='center',
        fontsize=16, color=text_color, fontweight='bold')

# Top: Nebenläufige Prozesse/Threads
draw_box(ax, 5, 10.2, 5, 0.8, 'Nebenläufige Prozesse/Threads', color=box_fill)

# Arrow down
draw_arrow(ax, (5, 9.8), (5, 9.2))

# Middle: Gemeinsame Ressourcen
draw_box(ax, 5, 8.5, 6, 1.2, 'Gemeinsame Ressourcen\n(Variablen, Dateien, Geräte, Speicher)', 
         color=box_fill, fontsize=10, multiline=True)

# Arrow down splitting
draw_arrow(ax, (5, 7.9), (5, 7.3))

# Split label
ax.text(5, 7.1, '?', ha='center', va='center', fontsize=14, color=text_color, fontweight='bold')

# Two branches
draw_arrow(ax, (5, 6.9), (2.8, 5.8))
draw_arrow(ax, (5, 6.9), (7.2, 5.8))

# Left: OHNE SYNCHRONISATION (red-ish)
box_bad = FancyBboxPatch((0.5, 3.2), 4.5, 2.5,
                         boxstyle="round,pad=0.02,rounding_size=0.15",
                         facecolor='#C53030', edgecolor=text_color, linewidth=1.5)
ax.add_patch(box_bad)
ax.text(2.75, 5.2, 'OHNE SYNCHRONISATION', ha='center', va='center',
        fontsize=11, color='white', fontweight='bold')
ax.text(2.75, 4.5, '• Inkonsistente Daten', ha='center', va='center',
        fontsize=9, color='white')
ax.text(2.75, 4.0, '• Nicht-reproduzierbare', ha='center', va='center',
        fontsize=9, color='white')
ax.text(2.75, 3.6, '  Ergebnisse', ha='center', va='center',
        fontsize=9, color='white')

# Right: MIT SYNCHRONISATION (green)
box_good = FancyBboxPatch((5, 3.2), 4.5, 2.5,
                          boxstyle="round,pad=0.02,rounding_size=0.15",
                          facecolor=box_fill_success, edgecolor=text_color, linewidth=1.5)
ax.add_patch(box_good)
ax.text(7.25, 5.2, 'MIT SYNCHRONISATION', ha='center', va='center',
        fontsize=11, color='white', fontweight='bold')
ax.text(7.25, 4.5, '• Koordinierter Zugriff', ha='center', va='center',
        fontsize=9, color='white')
ax.text(7.25, 4.0, '• Konsistente Daten', ha='center', va='center',
        fontsize=9, color='white')
ax.text(7.25, 3.6, '• Vorhersagbares Verhalten', ha='center', va='center',
        fontsize=9, color='white')

# Bottom arrows converging to result
draw_arrow(ax, (2.75, 3.2), (2.75, 2.2))
draw_arrow(ax, (7.25, 3.2), (7.25, 2.2))

# Results (using X instead of emoji for font compatibility)
ax.text(2.75, 1.7, 'X  Fehler', ha='center', va='center',
        fontsize=12, color='#C53030', fontweight='bold')
ax.text(7.25, 1.7, '✓ Korrekt', ha='center', va='center',
        fontsize=12, color=box_fill_success, fontweight='bold')

# Bottom summary
ax.text(5, 0.5, 'Ziel: Vorteile der Nebenläufigkeit nutzen,\nGefahren durch Synchronisation vermeiden',
        ha='center', va='center', fontsize=10, color=text_color, style='italic')

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/tmp/preview-sync-overview.png',
            dpi=150, bbox_inches='tight', transparent=True, pad_inches=0.1)
plt.close()
print("Created: preview-sync-overview.png")
