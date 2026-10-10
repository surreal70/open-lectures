#!/usr/bin/env python3
"""Generate Process Memory Layout diagram as PNG - Theme-agnostic version"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch

# Create figure with transparent background
fig, ax = plt.subplots(1, 1, figsize=(10, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 14)
ax.set_aspect('equal')
ax.axis('off')

# Theme-agnostic colors
header_gray = '#4A5568'
text_dark = '#A0AEC0'         # Lighter gray for better dark mode visibility
text_light = '#F7FAFC'
border_color = '#718096'

# Memory section colors
kernel_color = '#E53E3E'      # Red for kernel (danger/restricted)
stack_color = '#805AD5'       # Purple for stack
free_color = '#A0AEC0'        # Gray for free space
heap_color = '#38A169'        # Green for heap
bss_color = '#D69E2E'         # Yellow/Gold for BSS
data_color = '#DD6B20'        # Orange for Data
text_color = '#3182CE'        # Blue for Text/Code

# Box dimensions
box_x = 1.5
box_width = 5
x_right = box_x + box_width + 0.3  # Position for right-side annotations

# Draw address labels
ax.text(0.5, 13.3, 'Hohe Adressen', ha='left', va='center', 
        fontsize=10, color=text_dark, style='italic')
ax.text(0.5, 0.7, 'Niedrige Adressen', ha='left', va='center', 
        fontsize=10, color=text_dark, style='italic')

# Memory sections from top to bottom
sections = [
    # (y_bottom, height, color, label, sublabel, right_annotation)
    (12.0, 1.2, kernel_color, 'Kernel-Space', '', '← Für Benutzer nicht zugänglich'),
    (9.5, 2.4, stack_color, 'Stack', '(lokale Variablen,\nRücksprungadressen)', '↓ Wächst nach unten'),
    (7.0, 2.4, free_color, 'Freier Bereich', '↕', ''),
    (5.0, 1.9, heap_color, 'Heap', '(dynamischer Speicher,\nmalloc, new)', '↑ Wächst nach oben'),
    (4.0, 0.9, bss_color, 'BSS', '', '← Uninitialisierte globale Variablen'),
    (3.0, 0.9, data_color, 'Data', '', '← Initialisierte globale Variablen'),
    (1.5, 1.4, text_color, 'Text / Code', '', '← Programmcode (read-only)'),
]

for y, h, color, label, sublabel, annotation in sections:
    # Draw the box
    box = FancyBboxPatch((box_x, y), box_width, h,
                          boxstyle="square,pad=0",
                          facecolor=color, edgecolor=border_color, 
                          linewidth=2, alpha=0.85)
    ax.add_patch(box)
    
    # Main label
    label_y = y + h/2 + (0.15 if sublabel else 0)
    ax.text(box_x + box_width/2, label_y, label, ha='center', va='center',
            fontsize=12, fontweight='bold', color=text_light)
    
    # Sublabel if exists
    if sublabel:
        ax.text(box_x + box_width/2, y + h/2 - 0.3, sublabel, ha='center', va='center',
                fontsize=9, color=text_light)
    
    # Right-side annotation
    if annotation:
        ax.text(x_right, y + h/2, annotation, ha='left', va='center',
                fontsize=9, color=text_dark, family='monospace')

# Address labels on the right edge
ax.text(box_x + box_width + 0.1, 13.2, '0xFFFFFFFF', ha='left', va='center',
        fontsize=9, color=text_dark, family='monospace')
ax.text(box_x + box_width + 0.1, 1.5, '0x00000000', ha='left', va='center',
        fontsize=9, color=text_dark, family='monospace')

# Arrows for growth direction
# Stack arrow (down)
ax.annotate('', xy=(box_x - 0.3, 9.5), xytext=(box_x - 0.3, 11.8),
            arrowprops=dict(arrowstyle='->', color=stack_color, lw=2))

# Heap arrow (up)
ax.annotate('', xy=(box_x - 0.3, 6.9), xytext=(box_x - 0.3, 5.1),
            arrowprops=dict(arrowstyle='->', color=heap_color, lw=2))

# Title
ax.text(box_x + box_width/2, 13.7, 'Speicherlayout eines Prozesses', 
        ha='center', va='center', fontsize=14, fontweight='bold', color=text_dark)
ax.text(box_x + box_width/2, 13.3, '(32-bit Adressraum)', 
        ha='center', va='center', fontsize=10, color=text_dark, style='italic')

# Save with transparent background
output_path = "/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/03-Prozesse/assets/memory-layout.png"
plt.savefig(output_path, dpi=150, bbox_inches='tight', 
            transparent=True, pad_inches=0.2)
plt.close()

print(f"Saved: {output_path}")
