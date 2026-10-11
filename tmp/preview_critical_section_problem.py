#!/usr/bin/env python3
"""
Diagram: Problem - Gemeinsame Ressourcen
Two processes accessing a shared variable
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Colors (theme-agnostic)
box_fill = '#3182CE'
box_fill_light = '#4299E1'
text_color = '#A0AEC0'
arrow_color = '#A0AEC0'
highlight_color = '#E53E3E'

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.set_aspect('equal')
ax.axis('off')
fig.patch.set_alpha(0)
ax.set_facecolor('none')

def draw_box(ax, x, y, width, height, text, color=box_fill, fontsize=10):
    box = FancyBboxPatch((x - width/2, y - height/2), width, height,
                         boxstyle="round,pad=0.02,rounding_size=0.15",
                         facecolor=color, edgecolor=text_color, linewidth=1.5)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            color='white', fontweight='bold')
    return box

def draw_arrow(ax, start, end, color=arrow_color, style='-'):
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', color=color, lw=2,
                               linestyle=style))

# Title
ax.text(5, 5.5, 'Problem: Gemeinsame Ressourcen', ha='center', va='center',
        fontsize=14, color=text_color, fontweight='bold')

# Process A (left)
draw_box(ax, 1.5, 3.5, 2.2, 1.2, 'Prozess A\nx = x + 1', color=box_fill)

# Shared Variable (center)
draw_box(ax, 5, 3.5, 2, 1.2, 'x = 5', color='#805AD5')
ax.text(5, 2.5, 'Gemeinsame\nVariable', ha='center', va='center',
        fontsize=9, color=text_color)

# Process B (right)
draw_box(ax, 8.5, 3.5, 2.2, 1.2, 'Prozess B\nx = x * 2', color=box_fill)

# Arrows to shared variable
draw_arrow(ax, (2.6, 3.5), (4, 3.5))
draw_arrow(ax, (7.4, 3.5), (6, 3.5))

# Warning box at bottom
warning_box = FancyBboxPatch((1.5, 0.8), 7, 1.2,
                              boxstyle="round,pad=0.02,rounding_size=0.15",
                              facecolor=highlight_color, edgecolor=text_color, 
                              linewidth=1.5, alpha=0.9)
ax.add_patch(warning_box)
ax.text(5, 1.4, 'Ohne Koordination: Ergebnis unvorhersagbar!', 
        ha='center', va='center', fontsize=11, color='white', fontweight='bold')

# Solution hint
ax.text(5, 0.3, 'Lösung: Nur EIN Prozess darf gleichzeitig auf x zugreifen',
        ha='center', va='center', fontsize=10, color=text_color, style='italic')

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/tmp/preview-critical-section-problem.png',
            dpi=150, bbox_inches='tight', transparent=True, pad_inches=0.1)
plt.close()
print("Created: preview-critical-section-problem.png")
