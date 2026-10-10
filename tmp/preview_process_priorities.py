#!/usr/bin/env python3
"""Preview: Process Types and Priorities"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# Theme-agnostic colors
text_outside = '#A0AEC0'
text_light = '#F7FAFC'
border_color = '#718096'

# Priority level colors (gradient from red=high to blue=low)
system_color = '#E53E3E'      # Red - highest
interactive_color = '#ED8936' # Orange - high
batch_color = '#ECC94B'       # Yellow - medium
user_color = '#4299E1'        # Blue - normal

fig, ax = plt.subplots(1, 1, figsize=(10, 7))
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.set_aspect('equal')
ax.axis('off')

# Title
ax.text(5, 6.5, 'Prozesstypen und Prioritäten', ha='center', va='center',
        fontsize=14, fontweight='bold', color=text_outside)

# Priority arrow (vertical)
ax.annotate('', xy=(1.5, 1.0), xytext=(1.5, 5.8),
            arrowprops=dict(arrowstyle='<->', color=text_outside, lw=2))
ax.text(1.5, 6.1, 'PRIORITÄT', ha='center', va='center',
        fontsize=10, fontweight='bold', color=text_outside)
ax.text(0.5, 5.5, 'höchste', ha='center', va='center',
        fontsize=9, color=text_outside)
ax.text(0.5, 1.3, 'niedrigste', ha='center', va='center',
        fontsize=9, color=text_outside)

# Priority levels
levels = [
    (5.2, system_color, 'Systemprozesse', '(Kernel, Treiber)'),
    (4.0, interactive_color, 'Interaktive Prozesse', '(Benutzereingaben)'),
    (2.8, batch_color, 'Batchprozesse', '(Hintergrundaufgaben)'),
    (1.6, user_color, 'Benutzerprozesse', '(normale Anwendungen)'),
]

for y, color, label, desc in levels:
    # Horizontal line from arrow
    ax.plot([1.7, 2.5], [y, y], color=border_color, lw=1.5)
    
    # Box
    box = FancyBboxPatch((2.5, y - 0.35), 3.5, 0.7,
                          boxstyle="round,pad=0.02,rounding_size=0.1",
                          facecolor=color, edgecolor=border_color, linewidth=1.5)
    ax.add_patch(box)
    ax.text(4.25, y, label, ha='center', va='center',
            fontsize=10, fontweight='bold', color=text_light)
    
    # Description
    ax.text(6.3, y, desc, ha='left', va='center',
            fontsize=9, color=text_outside)

# Save preview
output_path = "/media/andhue/Wissen/open-lectures/tmp/preview-process-priorities.png"
plt.savefig(output_path, dpi=150, bbox_inches='tight', 
            transparent=True, pad_inches=0.2)
plt.close()
print(f"Preview saved: {output_path}")
