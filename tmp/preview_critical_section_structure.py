#!/usr/bin/env python3
"""
Diagram: Kritischer Abschnitt - Struktur
Flowchart: Entry Section -> Critical Section -> Exit Section -> Remainder
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np

# Colors (theme-agnostic)
box_fill = '#3182CE'
box_fill_critical = '#E53E3E'
text_color = '#A0AEC0'
arrow_color = '#A0AEC0'

fig, ax = plt.subplots(1, 1, figsize=(8, 12))
ax.set_xlim(0, 8)
ax.set_ylim(0, 12)
ax.set_aspect('equal')
ax.axis('off')
fig.patch.set_alpha(0)
ax.set_facecolor('none')

def draw_box(ax, x, y, width, height, title, subtitle, color=box_fill, 
             border_width=1.5, title_size=11, subtitle_size=9):
    box = FancyBboxPatch((x - width/2, y - height/2), width, height,
                         boxstyle="round,pad=0.02,rounding_size=0.15",
                         facecolor=color, edgecolor=text_color, linewidth=border_width)
    ax.add_patch(box)
    ax.text(x, y + 0.2, title, ha='center', va='center', fontsize=title_size,
            color='white', fontweight='bold')
    if subtitle:
        ax.text(x, y - 0.25, subtitle, ha='center', va='center', fontsize=subtitle_size,
                color='white', alpha=0.9)
    return y - height/2  # Return bottom y for arrow

def draw_arrow_down(ax, x, y_start, y_end, color=arrow_color):
    ax.annotate('', xy=(x, y_end), xytext=(x, y_start),
                arrowprops=dict(arrowstyle='->', color=color, lw=2))

# Title
ax.text(4, 11.3, 'Kritischer Abschnitt – Struktur', ha='center', va='center',
        fontsize=14, color=text_color, fontweight='bold')

# Positions
center_x = 4
box_width = 5.5
box_height = 1.3
critical_height = 2.0

# Entry Section
y1 = 9.5
draw_box(ax, center_x, y1, box_width, box_height, 
         'Entry Section', '(Erlaubnis einholen / warten)')

# Arrow
draw_arrow_down(ax, center_x, y1 - box_height/2 - 0.1, y1 - box_height/2 - 0.7)

# Critical Section (highlighted, larger)
y2 = 7.0
critical_box = FancyBboxPatch((center_x - box_width/2, y2 - critical_height/2), 
                               box_width, critical_height,
                               boxstyle="round,pad=0.02,rounding_size=0.15",
                               facecolor=box_fill_critical, edgecolor='white', 
                               linewidth=3)
ax.add_patch(critical_box)
ax.text(center_x, y2 + 0.5, 'KRITISCHER ABSCHNITT', ha='center', va='center', 
        fontsize=12, color='white', fontweight='bold')
ax.text(center_x, y2, '(Zugriff auf gemeinsame Ressource)', ha='center', va='center', 
        fontsize=9, color='white')
ax.text(center_x, y2 - 0.5, 'Nur EIN Prozess gleichzeitig!', ha='center', va='center', 
        fontsize=10, color='white', fontweight='bold', style='italic')

# Arrow
draw_arrow_down(ax, center_x, y2 - critical_height/2 - 0.1, y2 - critical_height/2 - 0.7)

# Exit Section
y3 = 4.3
draw_box(ax, center_x, y3, box_width, box_height, 
         'Exit Section', '(Ressource freigeben)')

# Arrow
draw_arrow_down(ax, center_x, y3 - box_height/2 - 0.1, y3 - box_height/2 - 0.7)

# Remainder Section
y4 = 2.0
draw_box(ax, center_x, y4, box_width, box_height, 
         'Remainder Section', '(Nicht-kritischer Code)', color='#718096')

# Loop arrow back to top
# Draw curved arrow from bottom back to top
from matplotlib.patches import FancyArrowPatch, Arc
import matplotlib.patches as mpatches

# Right side loop
loop_x = center_x + box_width/2 + 0.5
ax.plot([loop_x, loop_x], [y4, y1], color=arrow_color, lw=1.5, linestyle='--', alpha=0.6)
ax.annotate('', xy=(center_x + box_width/2 + 0.1, y1), 
            xytext=(loop_x, y1),
            arrowprops=dict(arrowstyle='->', color=arrow_color, lw=1.5, alpha=0.6))
ax.plot([center_x + box_width/2 + 0.1, loop_x], [y4 - box_height/2, y4 - box_height/2], 
        color=arrow_color, lw=1.5, linestyle='--', alpha=0.6)

ax.text(loop_x + 0.3, (y1 + y4)/2, 'while(true)', ha='left', va='center',
        fontsize=9, color=text_color, alpha=0.7, rotation=90)

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/tmp/preview-critical-section-structure.png',
            dpi=150, bbox_inches='tight', transparent=True, pad_inches=0.1)
plt.close()
print("Created: preview-critical-section-structure.png")
